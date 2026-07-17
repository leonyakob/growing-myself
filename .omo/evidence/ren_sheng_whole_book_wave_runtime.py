from __future__ import annotations

import json
import re
import uuid
from collections.abc import Callable, Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
Values: TypeAlias = Mapping[str, str | bool]


class SnapshotValue(NamedTuple):
    wave_id: str
    state: str
    reason: str
    input_hash: str
    snapshot_hash: str
    inputs: tuple[JsonMap, ...]
    text: str


if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]

    def json_fail(_command: str, _failures: Sequence[str], _reason: str = "INVALID") -> tuple[int, JsonMap]: ...
    def load_json_map(_path: Path, _failures: list[str], _label: str) -> JsonMap: ...
    def load_snapshot(_path: Path, _failures: list[str]) -> SnapshotValue | None: ...
    def path_value(_values: Values, _name: str) -> Path: ...
    def require(_values: Values, _names: Sequence[str]) -> list[str]: ...
    def sha256_bytes(_data: bytes) -> str: ...
    def sha256_path(_path: Path) -> str: ...
    def snapshot_check(_snapshot: SnapshotValue, _expected_wave_id: str) -> tuple[bool, str, list[str]]: ...
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map
    snapshot_module = __import__("ren_sheng_whole_book_wave_snapshot", fromlist=["json_fail", "load_json_map", "load_snapshot", "path_value", "require", "sha256_bytes", "sha256_path", "snapshot_check"])
    json_fail = snapshot_module.json_fail
    load_json_map = snapshot_module.load_json_map
    load_snapshot = snapshot_module.load_snapshot
    path_value = snapshot_module.path_value
    require = snapshot_module.require
    sha256_bytes = snapshot_module.sha256_bytes
    sha256_path = snapshot_module.sha256_path
    snapshot_check = snapshot_module.snapshot_check


def review_runtime_snapshot(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("preflight", "runtime-ledger", "workspace", "wave-id", "reviewer", "attempt-id", "out"))
    if failures:
        return json_fail("review-runtime-snapshot", failures)
    preflight = path_value(values, "preflight"); out = path_value(values, "out"); workspace = path_value(values, "workspace")
    if not preflight.is_file():
        failures.append(f"unreadable preflight: {preflight}")
    if not workspace.exists():
        failures.append(f"unreadable workspace: {workspace}")
    if (out.exists() and not out.is_file()) or not out.parent.exists():
        failures.append(f"invalid runtime snapshot output: {out}")
    if failures:
        return json_fail("review-runtime-snapshot", failures)
    data: JsonMap = {"schema_version": 1, "wave_id": str(values["wave-id"]), "reviewer": str(values["reviewer"]), "attempt_id": str(values["attempt-id"]), "preflight": str(preflight), "preflight_sha256": sha256_path(preflight), "runtime_ledger": str(values["runtime-ledger"]), "runtime_ledger_sha256": sha256_path(path_value(values, "runtime-ledger")), "workspace": str(workspace.resolve()), "captured_at": datetime.now(timezone.utc).isoformat()}
    _ = out.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return 0, {"command": "review-runtime-snapshot", "status": "PASS", "state": "CAPTURED", "output_path": str(out), "failures": []}


def str_field(values: Mapping[str, Json], key: str, default: str) -> str:
    value = values.get(key)
    return value if isinstance(value, str) else default


def result_fields(result: Mapping[str, Json]) -> tuple[str, str, str, str, str]:
    return str_field(result, "transport_status", "NO_RESULT"), str_field(result, "agent", ""), str_field(result, "session_id", ""), str_field(result, "full_message", ""), str_field(result, "tool_error", "")


def runtime_verdict(result: Mapping[str, Json]) -> tuple[str, str, str, str]:
    transport, agent, session_id, full_message, tool_error = result_fields(result)
    first_line = next((line.strip() for line in full_message.splitlines() if line.strip()), "")
    complete = transport == "COMPLETE" and agent == "Oracle" and bool(full_message.strip()) and tool_error == "" and first_line in {"APPROVED", "BLOCKED"}
    stored_transport = "COMPLETE" if complete else "NO_RESULT"
    verdict = first_line if complete else "NO_RESULT"
    return stored_transport, verdict, session_id, sha256_bytes(f"{full_message}\0{tool_error}".encode("utf-8"))


def runtime_path_state(path: Path) -> JsonMap:
    if path.is_symlink():
        return {"path": str(path.resolve()), "kind": "symlink", "sha256": "MISSING", "present": True}
    if path.is_file():
        return {"path": str(path.resolve()), "kind": "regular", "sha256": sha256_path(path), "present": True}
    if path.is_dir():
        return {"path": str(path.resolve()), "kind": "directory", "sha256": "MISSING", "present": True}
    return {"path": str(path.resolve()), "kind": "missing", "sha256": "MISSING", "present": False}


def runtime_nodes(workspace: Path, transport_status: str, session_id: str) -> tuple[JsonMap, ...]:
    if transport_status != "COMPLETE" or not session_id:
        return ()
    return (runtime_path_state(workspace.resolve() / ".omo/run-continuation" / f"{session_id}.json"),)


def review_runtime_register(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("preflight", "before", "result-json", "workspace", "wave-id", "reviewer", "attempt-id", "ledger"))
    if failures:
        return json_fail("review-runtime-register", failures)
    before = load_json_map(path_value(values, "before"), failures, "runtime before")
    result = load_json_map(path_value(values, "result-json"), failures, "result JSON")
    if failures:
        return json_fail("review-runtime-register", failures)
    drift = before.get("preflight_sha256") != sha256_path(path_value(values, "preflight")) or before.get("workspace") != str(path_value(values, "workspace").resolve())
    if drift:
        return 1, {"command": "review-runtime-register", "status": "FAIL", "reason": "RUNTIME_PATH_DRIFT", "failures": ["runtime preflight/workspace drift"]}
    result_hash = sha256_path(path_value(values, "result-json"))
    runtime_attempt_id = sha256_bytes(f"{values['wave-id']}:{values['reviewer']}:{values['attempt-id']}:{result_hash}".encode("utf-8"))
    stored_transport, verdict, session_id, message_hash = runtime_verdict(result)
    nodes = runtime_nodes(path_value(values, "workspace"), stored_transport, session_id)
    record: JsonMap = {"schema_version": 1, "runtime_attempt_id": runtime_attempt_id, "wave_id": str(values["wave-id"]), "reviewer": str(values["reviewer"]), "attempt_id": str(values["attempt-id"]), "transport_status": stored_transport, "verdict": verdict, "session_id": session_id, "message_hash": message_hash, "runtime_nodes": list(nodes), "runtime_node_count": len(nodes), "before_sha256": sha256_path(path_value(values, "before")), "result_sha256": result_hash, "preflight_sha256": sha256_path(path_value(values, "preflight")), "workspace": str(path_value(values, "workspace").resolve()), "registered_at": datetime.now(timezone.utc).isoformat()}
    ledger = path_value(values, "ledger")
    if not ledger.parent.exists():
        return json_fail("review-runtime-register", [f"invalid runtime ledger path: {ledger}"])
    with ledger.open("ab") as handle:
        _ = handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True).encode("utf-8") + b"\n")
    return 0, {"command": "review-runtime-register", "status": "PASS", "runtime_attempt_id": runtime_attempt_id, "transport_status": stored_transport, "verdict": verdict, "failures": []}


def load_runtime_records(ledger: Path, failures: list[str]) -> tuple[JsonMap, ...]:
    if not ledger.is_file():
        failures.append(f"unreadable runtime ledger: {ledger}")
        return ()
    records: list[JsonMap] = []
    for raw in ledger.read_text(encoding="utf-8").splitlines():
        try:
            records.append(decode_json_map(raw, "runtime ledger line"))
        except AssertionError:
            failures.append("runtime ledger line is malformed JSON")
    return tuple(records)


def recorded_runtime_nodes(record: Mapping[str, Json], failures: list[str]) -> tuple[JsonMap, ...]:
    raw_nodes = record.get("runtime_nodes")
    if not isinstance(raw_nodes, Sequence) or isinstance(raw_nodes, str):
        failures.append("runtime ledger runtime_nodes is not an array")
        return ()
    nodes: list[JsonMap] = []
    for raw_node in raw_nodes:
        if not isinstance(raw_node, Mapping):
            failures.append("runtime ledger runtime node is not an object")
            continue
        nodes.append({"path": raw_node.get("path", ""), "kind": raw_node.get("kind", ""), "sha256": raw_node.get("sha256", ""), "present": raw_node.get("present", False)})
    if record.get("runtime_node_count") != len(nodes):
        failures.append("runtime ledger runtime_node_count mismatch")
    return tuple(nodes)


def is_legacy_runtime_record(record: Mapping[str, Json], current_preflight: str) -> bool:
    lacks_runtime_nodes = "runtime_nodes" not in record and "runtime_node_count" not in record
    return lacks_runtime_nodes and record.get("preflight_sha256") != current_preflight


def review_runtime_final_check(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("preflight", "ledger", "workspace"))
    if failures:
        return json_fail("review-runtime-final-check", failures)
    records = load_runtime_records(path_value(values, "ledger"), failures)
    current_preflight = sha256_path(path_value(values, "preflight")); current_workspace = str(path_value(values, "workspace").resolve())
    legacy_records = 0
    checked_records = 0
    for record in records:
        if is_legacy_runtime_record(record, current_preflight):
            legacy_records += 1
            continue
        checked_records += 1
        if record.get("preflight_sha256") != current_preflight or record.get("workspace") != current_workspace:
            failures.append("runtime ledger path drift")
        expected_nodes = runtime_nodes(Path(str(record.get("workspace", ""))), str_field(record, "transport_status", "NO_RESULT"), str_field(record, "session_id", ""))
        if recorded_runtime_nodes(record, failures) != expected_nodes:
            failures.append("runtime ledger continuation node drift")
    return (0 if not failures else 1), {"command": "review-runtime-final-check", "status": "PASS" if not failures else "FAIL", "counts": {"runtime_records": len(records), "checked_runtime_records": checked_records, "legacy_runtime_records": legacy_records}, "failures": failures, "output_path": None}


def find_runtime_record(ledger: Path, runtime_attempt_id: str, failures: list[str]) -> JsonMap:
    for record in load_runtime_records(ledger, failures):
        if record.get("runtime_attempt_id") == runtime_attempt_id:
            return record
    failures.append(f"runtime attempt not found: {runtime_attempt_id}")
    return {}


def receipt_text(values: Values, snapshot: SnapshotValue, runtime_record: Mapping[str, Json], result: Mapping[str, Json], attempt_id: str, message_hash: str) -> str:
    transport, agent, session_id, full_message, tool_error = result_fields(result)
    stored_transport, verdict, _runtime_session, _runtime_hash = runtime_verdict(result)
    payload = json.dumps({"transport_status": transport, "agent": agent, "session_id": session_id, "full_message": full_message, "tool_error": tool_error, "runtime_record": dict(runtime_record)}, ensure_ascii=False, sort_keys=True, indent=2)
    return "\n".join(("# Ren Sheng final wave reviewer receipt", "", "schema_version: 1", f"wave_id: {snapshot.wave_id}", f"reviewer: {values['reviewer']}", f"attempt_id: {attempt_id}", f"runtime_attempt_id: {values['runtime-attempt-id']}", f"transport_status: {stored_transport}", f"verdict: {verdict}", f"session_id: {session_id}", f"message_hash: {message_hash}", f"wave_input_set_sha256: {snapshot.input_hash}", "", "```json", payload, "```", ""))


def review_receipt_append(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("snapshot", "wave-id", "reviewer", "runtime-ledger", "runtime-attempt-id", "runtime-preflight", "runtime-workspace", "result-json", "out"))
    if failures:
        return json_fail("review-receipt-append", failures)
    snapshot = load_snapshot(path_value(values, "snapshot"), failures)
    result = load_json_map(path_value(values, "result-json"), failures, "result JSON")
    runtime_record = find_runtime_record(path_value(values, "runtime-ledger"), str(values["runtime-attempt-id"]), failures)
    if snapshot is None or failures:
        return json_fail("review-receipt-append", failures)
    ok, reason, check_failures = snapshot_check(snapshot, str(values["wave-id"]))
    if not ok:
        return 1, {"command": "review-receipt-append", "status": "FAIL", "reason": reason, "failures": check_failures}
    stored_transport, verdict, session_id, message_hash = runtime_verdict(result)
    attempt_id = str(uuid.uuid4())
    out = path_value(values, "out")
    if (out.exists() and not out.is_file()) or not out.parent.exists():
        return json_fail("review-receipt-append", [f"invalid receipt output path: {out}"])
    _ = out.write_text(receipt_text(values, snapshot, runtime_record, result, attempt_id, message_hash), encoding="utf-8")
    return 0, {"command": "review-receipt-append", "status": "PASS", "attempt_id": attempt_id, "message_hash": message_hash, "transport_status": stored_transport, "verdict": verdict, "session_id": session_id, "failures": []}


def receipt_field(text: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}: (.+)$", text)
    return match.group(1).strip() if match else ""


def review_receipt_check(values: Values) -> tuple[int, JsonMap]:
    failures = require(values, ("snapshot", "wave-id", "reviewer", "receipt", "attempt-id", "message-hash"))
    if failures:
        return json_fail("review-receipt-check", failures)
    snapshot = load_snapshot(path_value(values, "snapshot"), failures)
    if snapshot is None:
        return json_fail("review-receipt-check", failures)
    ok, reason, check_failures = snapshot_check(snapshot, str(values["wave-id"]))
    if not ok:
        return 1, {"command": "review-receipt-check", "status": "FAIL", "reason": reason, "failures": check_failures}
    receipt_path = path_value(values, "receipt")
    if not receipt_path.is_file():
        return json_fail("review-receipt-check", [f"unreadable receipt: {receipt_path}"])
    text = receipt_path.read_text(encoding="utf-8")
    checks = (("wave_id", str(values["wave-id"])), ("reviewer", str(values["reviewer"])), ("attempt_id", str(values["attempt-id"])), ("message_hash", str(values["message-hash"])), ("wave_input_set_sha256", snapshot.input_hash))
    failures.extend(f"receipt field mismatch: {name}" for name, expected in checks if receipt_field(text, name) != expected)
    return (0 if not failures else 1), {"command": "review-receipt-check", "status": "PASS" if not failures else "FAIL", "state": snapshot.state, "failures": failures}
