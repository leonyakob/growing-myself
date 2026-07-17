from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | list["Json"] | dict[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map

ROOT: Final = Path(__file__).resolve().parents[2]
VALIDATOR: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-validator.py"
EVIDENCE_ROOT: Final = ROOT / ".omo/evidence"
PLAN: Final = ROOT / ".omo/plans/consolidate-ren-sheng-whole-book-notes.md"
SEALED_PLAN_SHA256: Final = "8795332a59d1293daaee67d7d0c406bffacdedbd5d5d781f52e5b60215bca306"


def sha256_bytes(data: bytes) -> str:
    return __import__("hashlib").sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.is_file() else "MISSING"


def decode_map(text: str, label: str) -> JsonMap:
    return decode_json_map(text, label)


def require_map(value: Json, label: str) -> JsonMap:
    if not isinstance(value, dict):
        raise AssertionError(f"{label} was not a JSON object")
    return value


def require_list(value: Json, label: str) -> list[Json]:
    if not isinstance(value, list):
        raise AssertionError(f"{label} was not a JSON array")
    return value


def run_validator(args: Sequence[str], env: Mapping[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, env=env, check=False, capture_output=True, text=True)


def no_bytecode_env() -> dict[str, str]:
    env = dict(os.environ)
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    return env


def snapshot_inputs(snapshot: Path) -> list[Json]:
    payload = snapshot.read_text(encoding="utf-8").split("```json\n", 1)[1].split("\n```", 1)[0]
    return require_list(decode_map(payload, "snapshot JSON")["inputs"], "snapshot inputs")


def snapshot_args(wave_id: str, out: Path) -> list[str]:
    return ["wave-snapshot-create", "--wave-id", wave_id, "--plan", ".omo/plans/consolidate-ren-sheng-whole-book-notes.md", "--brief", ".omo/drafts/consolidate-ren-sheng-whole-book-notes.md", "--review-seal", ".omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json", "--root-rules", "AGENTS.md", "--router", "路遥/人生/《人生》微信读书提示词.md", "--phase4", "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md", "--source", "路遥/人生/《人生》中间整理稿.md", "--formal", "路遥/人生/《人生》阅读笔记.md", "--evidence-root", ".omo/evidence", "--out", str(out)]


class WaveProtocolContractTests(unittest.TestCase):
    def test_validator_subprocess_does_not_write_evidence_bytecode(self) -> None:
        pycache = EVIDENCE_ROOT / "__pycache__"
        shutil.rmtree(pycache, ignore_errors=True)
        self.addCleanup(lambda: shutil.rmtree(pycache, ignore_errors=True))
        result = run_validator(["final-anchor-check", "--formal", "路遥/人生/《人生》阅读笔记.md", "--ledger", ".omo/evidence/ren-sheng-whole-book-consolidation-ledger.md", "--anchor-map", ".omo/evidence/ren-sheng-whole-book-anchor-map.md", "--check-only"], env=no_bytecode_env())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(pycache.exists(), "validator subprocess must not create .omo/evidence/__pycache__")

    def test_wave_snapshot_records_checkbox_normalized_plan_control_hash(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-wave-") as raw_tmp:
            snapshot = Path(raw_tmp) / "snapshot.md"
            wave_id = str(uuid.uuid4())
            created = run_validator(snapshot_args(wave_id, snapshot))
            self.assertEqual(created.returncode, 0, created.stderr)
            plan_rows = [require_map(item, "plan row") for item in snapshot_inputs(snapshot) if require_map(item, "input row").get("role") == "plan"]
            self.assertEqual(len(plan_rows), 1)
            self.assertEqual(plan_rows[0]["path"], str(PLAN.relative_to(ROOT)))
            self.assertEqual(plan_rows[0]["sha256"], sha256_path(PLAN))
            self.assertEqual(plan_rows[0]["canonical_checkbox_sha256"], SEALED_PLAN_SHA256)
            self.assertEqual(plan_rows[0]["review_seal_plan_sha256"], SEALED_PLAN_SHA256)
            self.assertEqual(plan_rows[0]["checkbox_normalization"], "- [x] and - [~] normalized to - [ ]")

    def test_wave_snapshot_check_detects_active_and_drift_states(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-wave-") as raw_tmp:
            snapshot = Path(raw_tmp) / "snapshot.md"
            wave_id = str(uuid.uuid4())
            created = run_validator(snapshot_args(wave_id, snapshot))
            self.assertEqual(created.returncode, 0, created.stderr)
            check = run_validator(["wave-snapshot-check", "--snapshot", str(snapshot), "--wave-id", wave_id, "--check-only"])
            self.assertEqual(check.returncode, 0, check.stderr)
            self.assertEqual(decode_map(check.stdout, "stdout")["state"], "ACTIVE")
            drifted = snapshot.read_text(encoding="utf-8").replace("state: ACTIVE", "state: ACTIVE\n<!-- drift -->", 1)
            _ = snapshot.write_text(drifted, encoding="utf-8")
            drift = run_validator(["wave-snapshot-check", "--snapshot", str(snapshot), "--wave-id", wave_id, "--check-only"])
            self.assertEqual(drift.returncode, 1)
            self.assertEqual(decode_map(drift.stdout, "stdout")["reason"], "INPUT_DRIFT")
            invalidated = run_validator(["wave-drift-invalidate", "--snapshot", str(snapshot), "--wave-id", wave_id, "--trigger", "F1"])
            self.assertEqual(invalidated.returncode, 0, invalidated.stderr)
            self.assertEqual(decode_map(invalidated.stdout, "stdout")["state"], "INVALIDATED")

    def test_runtime_and_receipt_protocol_round_trip(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-wave-") as raw_tmp:
            tmp = Path(raw_tmp)
            wave_id = str(uuid.uuid4())
            attempt_id = str(uuid.uuid4())
            snapshot = tmp / "snapshot.md"
            ledger = tmp / "runtime.jsonl"
            before = tmp / "before.json"
            result_json = tmp / "result.json"
            receipt = tmp / "ren-sheng-whole-book-f1-plan-compliance.md"
            workspace = tmp / "workspace"
            session_id = "ses_test"
            continuation = workspace / ".omo/run-continuation" / f"{session_id}.json"
            continuation.parent.mkdir(parents=True)
            original_runtime = '{"session":"ses_test"}\n'
            _ = continuation.write_text(original_runtime, encoding="utf-8")
            self.assertEqual(run_validator(snapshot_args(wave_id, snapshot)).returncode, 0)
            snap = run_validator(["review-runtime-snapshot", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--runtime-ledger", str(ledger), "--workspace", str(workspace), "--wave-id", wave_id, "--reviewer", "F1", "--attempt-id", attempt_id, "--out", str(before)])
            self.assertEqual(snap.returncode, 0, snap.stderr)
            _ = result_json.write_text(json.dumps({"transport_status": "COMPLETE", "agent": "Oracle", "session_id": session_id, "full_message": "APPROVED\nverified", "tool_error": ""}), encoding="utf-8")
            legacy_record: JsonMap = {"schema_version": 1, "wave_id": "ae8a2b65-da14-497c-acdf-db88cc30ff56", "reviewer": "F1", "attempt_id": "legacy", "runtime_attempt_id": "legacy", "transport_status": "COMPLETE", "verdict": "BLOCKED", "session_id": "ses_legacy", "message_hash": "legacy", "before_sha256": "legacy", "result_sha256": "legacy", "preflight_sha256": "legacy-preflight", "workspace": str(workspace.resolve())}
            _ = ledger.write_text(json.dumps(legacy_record, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
            register = run_validator(["review-runtime-register", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--before", str(before), "--result-json", str(result_json), "--workspace", str(workspace), "--wave-id", wave_id, "--reviewer", "F1", "--attempt-id", attempt_id, "--ledger", str(ledger)])
            self.assertEqual(register.returncode, 0, register.stderr)
            runtime_attempt_id = str(decode_map(register.stdout, "stdout")["runtime_attempt_id"])
            runtime_record = decode_map(ledger.read_text(encoding="utf-8").splitlines()[-1], "runtime ledger")
            nodes = require_list(runtime_record["runtime_nodes"], "runtime nodes")
            node = require_map(nodes[0], "runtime node")
            self.assertEqual(runtime_record["runtime_node_count"], 1)
            self.assertEqual(node["path"], str(continuation.resolve()))
            self.assertEqual(node["kind"], "regular")
            self.assertEqual(node["present"], True)
            self.assertEqual(node["sha256"], sha256_path(continuation))
            final_check = run_validator(["review-runtime-final-check", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--ledger", str(ledger), "--workspace", str(workspace), "--check-only"])
            self.assertEqual(final_check.returncode, 0, final_check.stderr)
            self.assertEqual(require_map(decode_map(final_check.stdout, "stdout")["counts"], "counts")["legacy_runtime_records"], 1)
            _ = continuation.write_text("drift\n", encoding="utf-8")
            drift = run_validator(["review-runtime-final-check", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--ledger", str(ledger), "--workspace", str(workspace), "--check-only"])
            self.assertEqual(drift.returncode, 1)
            self.assertIn("runtime ledger continuation node drift", json.dumps(decode_map(drift.stdout, "stdout"), ensure_ascii=False))
            _ = continuation.write_text(original_runtime, encoding="utf-8")
            append = run_validator(["review-receipt-append", "--snapshot", str(snapshot), "--wave-id", wave_id, "--reviewer", "F1", "--runtime-ledger", str(ledger), "--runtime-attempt-id", runtime_attempt_id, "--runtime-preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--runtime-workspace", str(workspace), "--result-json", str(result_json), "--out", str(receipt)])
            self.assertEqual(append.returncode, 0, append.stderr)
            summary = decode_map(append.stdout, "stdout")
            self.assertEqual(summary["status"], "PASS")
            check = run_validator(["review-receipt-check", "--snapshot", str(snapshot), "--wave-id", wave_id, "--reviewer", "F1", "--receipt", str(receipt), "--attempt-id", str(summary["attempt_id"]), "--message-hash", str(summary["message_hash"]), "--check-only"])
            self.assertEqual(check.returncode, 0, check.stderr)
            invalid = run_validator(["wave-invalidate", "--snapshot", str(snapshot), "--wave-id", wave_id, "--reviewer", "F1", "--receipt", str(receipt), "--reason", "BLOCKED"])
            self.assertEqual(invalid.returncode, 0, invalid.stderr)
            runtime_invalid = run_validator(["wave-runtime-invalidate", "--snapshot", str(snapshot), "--wave-id", wave_id, "--trigger", "F1", "--proof", str(before), "--before", str(before), "--result-json", str(result_json)])
            self.assertEqual(runtime_invalid.returncode, 0, runtime_invalid.stderr)

    def test_no_result_with_empty_session_records_zero_runtime_nodes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-wave-") as raw_tmp:
            tmp = Path(raw_tmp)
            wave_id = str(uuid.uuid4())
            attempt_id = str(uuid.uuid4())
            ledger = tmp / "runtime.jsonl"
            before = tmp / "before.json"
            result_json = tmp / "result.json"
            workspace = tmp / "workspace"
            workspace.mkdir()
            snap = run_validator(["review-runtime-snapshot", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--runtime-ledger", str(ledger), "--workspace", str(workspace), "--wave-id", wave_id, "--reviewer", "F2", "--attempt-id", attempt_id, "--out", str(before)])
            self.assertEqual(snap.returncode, 0, snap.stderr)
            _ = result_json.write_text(json.dumps({"transport_status": "NO_RESULT", "agent": "", "session_id": "", "full_message": "", "tool_error": "interrupted"}), encoding="utf-8")
            register = run_validator(["review-runtime-register", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--before", str(before), "--result-json", str(result_json), "--workspace", str(workspace), "--wave-id", wave_id, "--reviewer", "F2", "--attempt-id", attempt_id, "--ledger", str(ledger)])
            self.assertEqual(register.returncode, 0, register.stderr)
            runtime_record = decode_map(ledger.read_text(encoding="utf-8").splitlines()[-1], "runtime ledger")
            self.assertEqual(runtime_record["transport_status"], "NO_RESULT")
            self.assertEqual(runtime_record["verdict"], "NO_RESULT")
            self.assertEqual(runtime_record["session_id"], "")
            self.assertEqual(runtime_record["runtime_node_count"], 0)
            self.assertEqual(runtime_record["runtime_nodes"], [])
            self.assertEqual(run_validator(["review-runtime-final-check", "--preflight", ".omo/evidence/ren-sheng-whole-book-preflight.md", "--ledger", str(ledger), "--workspace", str(workspace), "--check-only"]).returncode, 0)
