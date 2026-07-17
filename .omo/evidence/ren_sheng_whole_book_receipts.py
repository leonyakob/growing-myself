from __future__ import annotations

import hashlib
import json
import re
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]


@dataclass(frozen=True, slots=True)
class ReceiptOutput:
    name: str
    path: Path | None


@dataclass(frozen=True, slots=True)
class PhaseInput:
    path: str
    phase: str
    sha256: str


@dataclass(frozen=True, slots=True)
class ReceiptSpec:
    todo: int
    subcommand: str
    outputs: Sequence[ReceiptOutput]
    phases: Sequence[PhaseInput]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.exists() and path.is_file() else "MISSING"


def previous_record_hash(prefix: bytes) -> str | None:
    if not prefix.splitlines():
        return None
    match = re.search(r'"record_hash":\s*"([0-9a-f]{64})"', prefix.splitlines()[-1].decode("utf-8"))
    return match.group(1) if match else None


def append_validator_receipt(receipt: Path, summary: Mapping[str, Json], spec: ReceiptSpec) -> None:
    prefix = receipt.read_bytes() if receipt.exists() else b""
    outputs: JsonMap = {item.name: sha256_path(item.path) for item in spec.outputs if item.path is not None and item.path.exists()}
    phases: list[Json] = [{"path": item.path, "phase": item.phase, "sha256": item.sha256} for item in spec.phases]
    record: JsonMap = {"schema_version": 1, "todo": spec.todo, "subcommand": spec.subcommand, "attempt_id": str(uuid.uuid4()), "attempted_at": datetime.now(timezone.utc).isoformat(), "stable_input_hashes": summary["input_hashes"], "phase_input_hashes": phases, "output_hashes": outputs, "status": "PASS" if summary["status"] == "PASS" else "FAIL", "failures": summary["failures"], "supersedes_attempt_id": None, "receipt_prefix_sha256": sha256_bytes(prefix), "previous_record_hash": previous_record_hash(prefix)}
    record["record_hash"] = sha256_bytes(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    with receipt.open("ab") as handle:
        _ = handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True).encode("utf-8") + b"\n")
