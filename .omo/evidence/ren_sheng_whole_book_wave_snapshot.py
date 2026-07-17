from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
Values: TypeAlias = Mapping[str, str | bool]

if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map

SNAPSHOT_PLACEHOLDER: Final = "PENDING"
SNAPSHOT_HASH_RE: Final = re.compile(r"(?m)^snapshot_sha256: ([0-9a-f]{64}|PENDING)$")
PLAN_CHECKBOX_RE: Final = re.compile(r"(?m)^(\s*- \[)[x~](\])")
SEALED_PLAN_SHA256: Final = "8795332a59d1293daaee67d7d0c406bffacdedbd5d5d781f52e5b60215bca306"
INPUT_KEYS: Final = ("plan", "brief", "review-seal", "root-rules", "router", "phase4", "source", "formal")
EVIDENCE_INPUTS: Final = (
    "ren-sheng-whole-book-preflight.md",
    "ren-sheng-whole-book-formal-baseline.md",
    "ren-sheng-whole-book-preservation-manifest.md",
    "ren-sheng-whole-book-source-manifest.md",
    "ren-sheng-whole-book-consolidation-ledger.md",
    "ren-sheng-whole-book-reconciliation.md",
    "ren-sheng-whole-book-technical-field-inventory.md",
    "ren-sheng-whole-book-fixture-results.md",
    "ren-sheng-whole-book-anchor-map.md",
    "ren-sheng-whole-book-candidate-section.md",
    "ren-sheng-whole-book-candidate-qa.md",
    "ren-sheng-whole-book-metadata-cleanup.md",
    "ren-sheng-whole-book-archive-audit.md",
    "ren-sheng-whole-book-index-audit.md",
    "ren-sheng-whole-book-trajectory-audit.md",
    "final-ren-sheng-whole-book-consolidation-qa.md",
    "ren-sheng-whole-book-validator-invocations.jsonl",
)


@dataclass(frozen=True, slots=True)
class Snapshot:
    wave_id: str
    state: str
    reason: str
    input_hash: str
    snapshot_hash: str
    inputs: tuple[JsonMap, ...]
    text: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.is_file() else "MISSING"


def canonical_plan_sha256(path: Path) -> str:
    if not path.is_file():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    return sha256_bytes(PLAN_CHECKBOX_RE.sub(r"\1 \2", text).encode("utf-8"))


def review_seal_plan_sha256(path: Path) -> str:
    if not path.is_file():
        return "MISSING"
    match = re.search(r'"plan_sha256":"([0-9a-f]{64})"', path.read_text(encoding="utf-8"))
    return match.group(1) if match else "MISSING"


def plan_input_row(path: Path, review_seal: Path) -> JsonMap:
    canonical = canonical_plan_sha256(path)
    sealed = review_seal_plan_sha256(review_seal)
    return {"role": "plan", "path": str(path), "sha256": sha256_path(path), "canonical_checkbox_sha256": canonical, "review_seal_path": str(review_seal), "review_seal_plan_sha256": sealed, "checkbox_normalization": "- [x] and - [~] normalized to - [ ]", "sealed_plan_match": canonical == sealed == SEALED_PLAN_SHA256}


def json_fail(command: str, failures: Sequence[str], reason: str = "INVALID") -> tuple[int, JsonMap]:
    return 2, {"command": command, "status": "FAIL", "state": "INVALID", "reason": reason, "failures": list(failures), "counts": {}, "output_path": None}


def parse_values(argv: Sequence[str]) -> tuple[str, dict[str, str | bool] | str]:
    if not argv:
        return "invalid", "usage: wave command is required"
    values: dict[str, str | bool] = {"check-only": False}
    tokens = list(argv[1:])
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == "--check-only":
            values["check-only"] = True
            index += 1
        elif token.startswith("--") and index + 1 < len(tokens):
            values[token.removeprefix("--")] = tokens[index + 1]
            index += 2
        else:
            return argv[0], f"invalid invocation token: {token}"
    return argv[0], values


def require(values: Values, names: Sequence[str]) -> list[str]:
    return [f"--{name} is required" for name in names if not isinstance(values.get(name), str)]


def path_value(values: Values, name: str) -> Path:
    return Path(str(values[name]))


def load_json_map(path: Path, failures: list[str], label: str) -> JsonMap:
    if not path.is_file():
        failures.append(f"unreadable {label}: {path}")
        return {}
    try:
        return decode_json_map(path.read_text(encoding="utf-8"), label)
    except AssertionError:
        failures.append(f"malformed {label}: {path}")
        return {}


def input_rows(values: Values, failures: list[str]) -> tuple[JsonMap, ...]:
    rows: list[JsonMap] = []
    review_seal = path_value(values, "review-seal")
    for key in INPUT_KEYS:
        path = path_value(values, key)
        if not path.is_file():
            failures.append(f"unreadable wave input: {path}")
        row = plan_input_row(path, review_seal) if key == "plan" else {"role": key, "path": str(path), "sha256": sha256_path(path)}
        if key == "plan" and row.get("sealed_plan_match") is not True:
            failures.append("checkbox-normalized plan hash does not match review seal plan hash")
        rows.append(row)
    evidence_root = path_value(values, "evidence-root")
    for name in EVIDENCE_INPUTS:
        path = evidence_root / name
        if not path.is_file():
            failures.append(f"unreadable wave evidence input: {path}")
        rows.append({"role": "evidence", "path": str(path), "sha256": sha256_path(path)})
    return tuple(rows)


def input_set_hash(rows: Sequence[Mapping[str, Json]]) -> str:
    return sha256_bytes(json.dumps(list(rows), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def canonical_snapshot_hash(text: str) -> str:
    canonical = SNAPSHOT_HASH_RE.sub(f"snapshot_sha256: {SNAPSHOT_PLACEHOLDER}", text)
    return sha256_bytes(canonical.encode("utf-8"))


def snapshot_text(wave_id: str, state: str, reason: str, rows: Sequence[Mapping[str, Json]]) -> str:
    input_hash = input_set_hash(rows)
    payload = json.dumps({"inputs": list(rows)}, ensure_ascii=False, sort_keys=True, indent=2)
    text = "\n".join(("# Ren Sheng final wave input snapshot", "", f"wave_id: {wave_id}", f"state: {state}", f"reason: {reason}", f"wave_input_set_sha256: {input_hash}", f"snapshot_sha256: {SNAPSHOT_PLACEHOLDER}", "", "```json", payload, "```", ""))
    return SNAPSHOT_HASH_RE.sub(f"snapshot_sha256: {canonical_snapshot_hash(text)}", text)


def field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}: (.+)$", text)
    return match.group(1).strip() if match else ""


def load_snapshot(path: Path, failures: list[str]) -> Snapshot | None:
    if not path.is_file():
        failures.append(f"unreadable snapshot: {path}")
        return None
    text = path.read_text(encoding="utf-8")
    block = re.search(r"```json\n(.*?)\n```", text, re.S)
    if block is None:
        failures.append("snapshot JSON payload is absent")
        return None
    try:
        payload = decode_json_map(block.group(1), "snapshot JSON payload")
    except AssertionError:
        failures.append("snapshot JSON payload is malformed")
        return None
    inputs = payload.get("inputs")
    if not isinstance(inputs, list):
        failures.append("snapshot inputs payload is absent")
        return None
    rows: list[JsonMap] = []
    for item in inputs:
        if isinstance(item, Mapping):
            rows.append({key: value for key, value in item.items()})
    return Snapshot(field(text, "wave_id"), field(text, "state"), field(text, "reason"), field(text, "wave_input_set_sha256"), field(text, "snapshot_sha256"), tuple(rows), text)


def snapshot_check(snapshot: Snapshot, expected_wave_id: str) -> tuple[bool, str, list[str]]:
    if snapshot.wave_id != expected_wave_id:
        return False, "WAVE_ID_MISMATCH", ["snapshot wave_id does not match"]
    if canonical_snapshot_hash(snapshot.text) != snapshot.snapshot_hash:
        return False, "INPUT_DRIFT", ["snapshot bytes changed after creation"]
    if snapshot.state != "ACTIVE":
        return False, "WAVE_INVALIDATED", [f"snapshot state is {snapshot.state}"]
    current_rows = tuple(plan_input_row(Path(str(row.get("path", ""))), Path(str(row.get("review_seal_path", "")))) if row.get("role") == "plan" else {"role": row.get("role", ""), "path": row.get("path", ""), "sha256": sha256_path(Path(str(row.get("path", ""))))} for row in snapshot.inputs)
    if input_set_hash(current_rows) != snapshot.input_hash:
        return False, "INPUT_DRIFT", ["wave input set hash drift"]
    return True, "OK", []


def wave_snapshot_create(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, (*INPUT_KEYS, "evidence-root", "wave-id", "out"))
    if failures:
        return json_fail("wave-snapshot-create", failures)
    rows = input_rows(values, failures)
    out = path_value(values, "out")
    if (out.exists() and not out.is_file()) or not out.parent.exists():
        failures.append(f"invalid snapshot output path: {out}")
    if failures:
        return json_fail("wave-snapshot-create", failures)
    text = snapshot_text(str(values["wave-id"]), "ACTIVE", "none", rows)
    _ = out.write_text(text, encoding="utf-8")
    return 0, {"command": "wave-snapshot-create", "status": "PASS", "state": "ACTIVE", "wave_id": str(values["wave-id"]), "wave_input_set_sha256": input_set_hash(rows), "output_path": str(out), "failures": []}


def wave_snapshot_check(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("snapshot", "wave-id"))
    if failures:
        return json_fail("wave-snapshot-check", failures)
    load_failures: list[str] = []
    snapshot = load_snapshot(path_value(values, "snapshot"), load_failures)
    if snapshot is None:
        return 2, {"command": "wave-snapshot-check", "status": "FAIL", "state": "INVALID", "reason": "INVALID", "failures": load_failures}
    ok, reason, check_failures = snapshot_check(snapshot, str(values["wave-id"]))
    summary: JsonMap = {"command": "wave-snapshot-check", "status": "PASS" if ok else "FAIL", "state": snapshot.state, "reason": reason, "wave_input_set_sha256": snapshot.input_hash, "failures": check_failures}
    return (0 if ok else 1), summary


def invalidate_snapshot(values: Values, command: str, reason: str) -> tuple[int, JsonMap]:
    required = ("snapshot", "wave-id", "trigger") if command != "wave-invalidate" else ("snapshot", "wave-id", "reviewer", "receipt", "reason")
    failures = require(values, required)
    if failures:
        return json_fail(command, failures)
    snapshot_path = path_value(values, "snapshot")
    load_failures: list[str] = []
    snapshot = load_snapshot(snapshot_path, load_failures)
    if snapshot is None:
        return json_fail(command, load_failures)
    if snapshot.wave_id != str(values["wave-id"]):
        return json_fail(command, ["snapshot wave_id does not match"], "WAVE_ID_MISMATCH")
    if command == "wave-invalidate" and not path_value(values, "receipt").is_file():
        return json_fail(command, ["checked reviewer receipt is required before wave-invalidate"])
    _ = snapshot_path.write_text(snapshot_text(snapshot.wave_id, "INVALIDATED", reason, snapshot.inputs), encoding="utf-8")
    return 0, {"command": command, "status": "PASS", "state": "INVALIDATED", "reason": reason, "wave_id": snapshot.wave_id, "failures": []}
