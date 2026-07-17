from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map

FINAL_FORMAL_SHA256: Final = "03cbe76f586b80a68db054f13d2dac04e5ee743d979dac4631b95ef54b25063f"
EXPECTED_OUTPUTS: Final[Mapping[int, Mapping[str, str]]] = {
    1: {"baseline_copy": "ren-sheng-whole-book-formal-baseline.md", "preservation": "ren-sheng-whole-book-preservation-manifest.md", "technical": "ren-sheng-whole-book-technical-field-inventory.md"},
    2: {"source_manifest": "ren-sheng-whole-book-source-manifest.md"},
    3: {"ledger": "ren-sheng-whole-book-consolidation-ledger.md", "reconciliation": "ren-sheng-whole-book-reconciliation.md"},
    4: {"fixture_results": "ren-sheng-whole-book-fixture-results.md"},
    5: {"anchor_map": "ren-sheng-whole-book-anchor-map.md"},
    6: {"candidate": "ren-sheng-whole-book-candidate-section.md"},
    7: {"candidate_qa": "ren-sheng-whole-book-candidate-qa.md"},
}
EXPECTED_SUBCOMMANDS: Final[Mapping[int, str]] = {
    1: "formal-inventory",
    2: "source-inventory",
    3: "ledger-check",
    4: "policy-check",
    5: "anchor-check",
    6: "candidate-structure",
    7: "candidate-check",
}


@dataclass(frozen=True, slots=True)
class ReceiptState:
    records: int
    required_passes: int
    latest_record_hash: str
    todo10_record_hash: str | None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.is_file() else "MISSING"


def record_hash(record: Mapping[str, Json]) -> str:
    payload = dict(record)
    _ = payload.pop("record_hash", None)
    return sha256_bytes(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def load_records(receipt: Path, failures: list[str]) -> tuple[JsonMap, ...]:
    if not receipt.is_file():
        failures.append(f"unreadable validator receipt JSONL: {receipt}")
        return ()
    records: list[JsonMap] = []
    prefix = b""
    previous_hash: str | None = None
    for line_no, raw in enumerate(receipt.read_bytes().splitlines(), start=1):
        try:
            record = decode_json_map(raw.decode("utf-8"), f"validator receipt line {line_no}")
        except AssertionError:
            failures.append(f"validator receipt line is not JSON: {line_no}")
            prefix += raw + b"\n"
            continue
        expected_prefix = sha256_bytes(prefix)
        if record.get("receipt_prefix_sha256") != expected_prefix:
            failures.append(f"validator receipt prefix hash drift at line {line_no}")
        if record.get("previous_record_hash") != previous_hash:
            failures.append(f"validator receipt previous hash drift at line {line_no}")
        if record.get("record_hash") != record_hash(record):
            failures.append(f"validator receipt record hash drift at line {line_no}")
        previous_value = record.get("record_hash")
        previous_hash = previous_value if isinstance(previous_value, str) else None
        records.append(record)
        prefix += raw + b"\n"
    return tuple(records)


def output_hashes(record: Mapping[str, Json], failures: list[str]) -> Mapping[str, Json]:
    values = record.get("output_hashes")
    if not isinstance(values, Mapping):
        failures.append("validator receipt output_hashes is not a mapping")
        return {}
    return values


def latest_pass(records: Sequence[Mapping[str, Json]], todo: int, subcommand: str) -> Mapping[str, Json] | None:
    matches = [record for record in records if record.get("todo") == todo and record.get("subcommand") == subcommand and record.get("status") == "PASS"]
    return matches[-1] if matches else None


def verify_expected_outputs(record: Mapping[str, Json], outputs: Mapping[str, str], evidence_root: Path, failures: list[str]) -> None:
    hashes = output_hashes(record, failures)
    for name, relative in outputs.items():
        expected = sha256_path(evidence_root / relative)
        actual = hashes.get(name)
        if actual != expected:
            failures.append(f"latest receipt output hash drift for {name}: expected {expected} got {actual}")


def phase_inputs(record: Mapping[str, Json]) -> Sequence[Json]:
    values = record.get("phase_input_hashes")
    return values if isinstance(values, Sequence) and not isinstance(values, str) else ()


def verify_todo10(records: Sequence[Mapping[str, Json]], final_qa: Path, failures: list[str]) -> str | None:
    record = latest_pass(records, 10, "final-check")
    if record is None:
        return None
    hashes = output_hashes(record, failures)
    expected_hash = sha256_path(final_qa)
    if hashes.get("final_qa") != expected_hash:
        failures.append(f"Todo 10 receipt final_qa hash drift: expected {expected_hash} got {hashes.get('final_qa')}")
    expected_phase = {"path": "路遥/人生/《人生》阅读笔记.md", "phase": "post-Todo9-final", "sha256": FINAL_FORMAL_SHA256}
    if expected_phase not in phase_inputs(record):
        failures.append("Todo 10 receipt is not bound to the post-Todo9 formal phase")
    value = record.get("record_hash")
    return value if isinstance(value, str) else None


def verify_receipt_chain(receipt: Path, evidence_root: Path, final_qa: Path, failures: list[str]) -> ReceiptState:
    records = load_records(receipt, failures)
    required_passes = 0
    for todo, subcommand in EXPECTED_SUBCOMMANDS.items():
        record = latest_pass(records, todo, subcommand)
        if record is None:
            failures.append(f"missing latest PASS receipt for Todo {todo} {subcommand}")
            continue
        required_passes += 1
        verify_expected_outputs(record, EXPECTED_OUTPUTS[todo], evidence_root, failures)
    todo10_hash = verify_todo10(records, final_qa, failures)
    latest = records[-1].get("record_hash") if records else None
    return ReceiptState(len(records), required_passes, latest if isinstance(latest, str) else "none", todo10_hash)
