from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from collections.abc import Callable, Sequence
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
FORMAL: Final = ROOT / "路遥/人生/《人生》阅读笔记.md"
EVIDENCE_ROOT: Final = ROOT / ".omo/evidence"
PREFLIGHT: Final = EVIDENCE_ROOT / "ren-sheng-whole-book-preflight.md"
LEDGER: Final = EVIDENCE_ROOT / "ren-sheng-whole-book-consolidation-ledger.md"
ANCHOR_MAP: Final = EVIDENCE_ROOT / "ren-sheng-whole-book-anchor-map.md"
FINAL_QA: Final = EVIDENCE_ROOT / "final-ren-sheng-whole-book-consolidation-qa.md"
FINAL_SHA256: Final = "03cbe76f586b80a68db054f13d2dac04e5ee743d979dac4631b95ef54b25063f"
PLAN: Final = ROOT / ".omo/plans/consolidate-ren-sheng-whole-book-notes.md"
SEALED_PLAN_SHA256: Final = "8795332a59d1293daaee67d7d0c406bffacdedbd5d5d781f52e5b60215bca306"
CHECKBOX_RE: Final = re.compile(r"(?m)^(\s*- \[)[x~](\])")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.is_file() else "MISSING"


def canonical_plan_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return sha256_bytes(CHECKBOX_RE.sub(r"\1 \2", text).encode("utf-8"))


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


def run_validator(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, check=False, capture_output=True, text=True)


def final_check_args() -> list[str]:
    return ["final-check", "--formal", str(FORMAL), "--evidence-root", str(EVIDENCE_ROOT), "--preflight", str(PREFLIGHT)]


class FinalCheckContractTests(unittest.TestCase):
    def test_final_check_check_only_requires_current_artifact(self) -> None:
        result = run_validator([*final_check_args(), "--check-only"])
        summary = decode_map(result.stdout, "stdout")
        if FINAL_QA.exists():
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(summary["status"], "PASS")
        else:
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn("unreadable final QA artifact", json.dumps(summary["failures"], ensure_ascii=False))

    def test_final_check_writes_pass_artifact_and_receipt(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-final-") as raw_tmp:
            receipt = Path(raw_tmp) / "receipt.jsonl"
            result = run_validator([*final_check_args(), "--receipt", str(receipt)])
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            counts = require_map(summary["counts"], "counts")
            self.assertEqual(summary["command"], "final-check")
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(counts["final_formal_sha256"], FINAL_SHA256)
            self.assertEqual(counts["source_units"], 266)
            self.assertEqual(counts["final_cards"], 165)
            self.assertTrue(FINAL_QA.is_file())
            qa_text = FINAL_QA.read_text(encoding="utf-8")
            for phrase in ("Status: PASS", "266 source units", "165 + N_new = 165", "all eight Phase 4 axes", "push is prohibited"):
                self.assertIn(phrase, qa_text)
            record = decode_map(receipt.read_text(encoding="utf-8").splitlines()[-1], "receipt")
            self.assertEqual(record["todo"], 10)
            self.assertEqual(record["subcommand"], "final-check")
            self.assertIn({"path": "路遥/人生/《人生》阅读笔记.md", "phase": "post-Todo9-final", "sha256": FINAL_SHA256}, require_list(record["phase_input_hashes"], "phase_input_hashes"))
            self.assertIn("final_qa", require_map(record["output_hashes"], "output_hashes"))

    def test_final_check_validates_checkbox_normalized_plan_control_hash(self) -> None:
        result = run_validator([*final_check_args(), "--check-only"])
        self.assertEqual(result.returncode, 0, result.stderr)
        counts = require_map(decode_map(result.stdout, "stdout")["counts"], "counts")
        self.assertEqual(counts["current_plan_sha256"], sha256_path(PLAN))
        self.assertEqual(counts["canonical_plan_sha256"], canonical_plan_sha256(PLAN))
        self.assertEqual(counts["canonical_plan_sha256"], SEALED_PLAN_SHA256)
        self.assertEqual(counts["review_seal_plan_sha256"], SEALED_PLAN_SHA256)
        qa_text = FINAL_QA.read_text(encoding="utf-8")
        self.assertIn("checkbox-normalized", qa_text)
        self.assertIn(SEALED_PLAN_SHA256, qa_text)

    def test_final_anchor_check_accepts_current_final_formal(self) -> None:
        result = run_validator(["final-anchor-check", "--formal", str(FORMAL), "--ledger", str(LEDGER), "--anchor-map", str(ANCHOR_MAP), "--check-only"])
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = decode_map(result.stdout, "stdout")
        counts = require_map(summary["counts"], "counts")
        self.assertEqual(summary["command"], "final-anchor-check")
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual(counts["final_cards"], 165)
        self.assertEqual(counts["n_new"], 0)
        self.assertEqual(counts["article_links_none"], 67)
