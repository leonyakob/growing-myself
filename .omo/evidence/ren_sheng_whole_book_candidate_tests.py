from __future__ import annotations

import json
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
CANDIDATE: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-candidate-section.md"
FORMAL: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-formal-baseline.md"
SOURCE_MANIFEST: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-source-manifest.md"
FORMAL_MANIFEST: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-preservation-manifest.md"
LEDGER: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-consolidation-ledger.md"
RECONCILIATION: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-reconciliation.md"
TECHNICAL: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-technical-field-inventory.md"
FIXTURE_RESULTS: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-fixture-results.md"
ANCHOR_MAP: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-anchor-map.md"
REVIEWED_SHA256: Final = "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"


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


def candidate_args(candidate: Path) -> list[str]:
    return ["candidate-structure", "--candidate", str(candidate), "--ledger", str(LEDGER), "--technical", str(TECHNICAL), "--anchor-map", str(ANCHOR_MAP)]


def candidate_check_args(out: Path) -> list[str]:
    return ["candidate-check", "--formal", str(FORMAL), "--source-manifest", str(SOURCE_MANIFEST), "--formal-manifest", str(FORMAL_MANIFEST), "--ledger", str(LEDGER), "--reconciliation", str(RECONCILIATION), "--technical", str(TECHNICAL), "--fixture-results", str(FIXTURE_RESULTS), "--anchor-map", str(ANCHOR_MAP), "--candidate", str(CANDIDATE), "--out", str(out)]


class CandidateCheckContractTests(unittest.TestCase):
    def test_candidate_structure_accepts_current_candidate_and_counts(self) -> None:
        result = run_validator([*candidate_args(CANDIDATE), "--check-only"])
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = decode_map(result.stdout, "stdout")
        counts = require_map(summary["counts"], "counts")
        self.assertEqual(summary["command"], "candidate-structure")
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual(counts["part_a_rows"], 108)
        self.assertEqual(counts["part_b_fragments"], 0)
        self.assertEqual(counts["article_rows"], 6)
        self.assertEqual(counts["trajectory_rows"], 6)

    def test_candidate_structure_check_only_writes_no_receipt_and_rejects_receipt(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-") as raw_tmp:
            receipt = Path(raw_tmp) / "receipt.jsonl"
            result = run_validator([*candidate_args(CANDIDATE), "--check-only"])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(decode_map(result.stdout, "stdout")["output_path"], None)
            self.assertFalse(receipt.exists())
            rejected = run_validator([*candidate_args(CANDIDATE), "--check-only", "--receipt", str(receipt)])
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(receipt.exists())

    def test_candidate_structure_rejects_target_bound_technical_tokens(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-") as raw_tmp:
            for replacement in ("待回看提醒【源ID：999】。", "待回看提醒 `chapterUid=26`。"):
                with self.subTest(replacement=replacement):
                    bad_candidate = Path(raw_tmp) / f"bad-{abs(hash(replacement))}.md"
                    text = CANDIDATE.read_text(encoding="utf-8").replace("外部残留材料只作回看提醒。", replacement, 1)
                    _ = bad_candidate.write_text(text, encoding="utf-8")
                    result = run_validator([*candidate_args(bad_candidate), "--check-only"])
                    self.assertEqual(result.returncode, 1)
                    self.assertIn("technical", json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False))

    def test_candidate_structure_rejects_missing_article_direction(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-") as raw_tmp:
            bad_candidate = Path(raw_tmp) / "missing-article.md"
            text = CANDIDATE.read_text(encoding="utf-8").replace("#### 知识分子困境", "#### 知识困境", 1)
            _ = bad_candidate.write_text(text, encoding="utf-8")
            result = run_validator([*candidate_args(bad_candidate), "--check-only"])
            self.assertEqual(result.returncode, 1)
            self.assertIn("article", json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False))

    def test_candidate_structure_rejects_missing_trajectory_heading(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-") as raw_tmp:
            bad_candidate = Path(raw_tmp) / "missing-trajectory.md"
            text = CANDIDATE.read_text(encoding="utf-8").replace("#### 黄亚萍物质付出：从“这不是牺牲”修正为“有真实成本，但不等同于巧珍在匮乏中的托举”", "#### 物质付出", 1)
            _ = bad_candidate.write_text(text, encoding="utf-8")
            result = run_validator([*candidate_args(bad_candidate), "--check-only"])
            self.assertEqual(result.returncode, 1)
            self.assertIn("trajectory", json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False))

    def test_candidate_check_writes_todo7_qa_and_counts(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-check-") as raw_tmp:
            out = Path(raw_tmp) / "candidate-qa.md"
            result = run_validator(candidate_check_args(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            counts = require_map(summary["counts"], "counts")
            self.assertEqual(summary["command"], "candidate-check")
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(summary["output_path"], str(out))
            self.assertEqual(counts["modeled_post_cards"], 165)
            self.assertEqual(counts["n_new"], 0)
            self.assertEqual(counts["target_bound_forbidden_hits"], 0)
            self.assertEqual(counts["fixture_pass"], 9)
            self.assertEqual(counts["sentinel_pass"], 7)
            self.assertEqual(counts["article_rows"], 6)
            self.assertEqual(counts["trajectory_rows"], 6)
            qa_text = out.read_text(encoding="utf-8")
            self.assertIn("Status: PASS", qa_text)
            self.assertIn("165 + N_new = 165", qa_text)
            self.assertIn("unresolved=[]", qa_text)
            for phrase in ("internal input hits: expected and confined to internal-before", "target-bound forbidden hits: 0", "modeled-post card/anchor cardinality", "missing-unbound: 0", "duplicate readable anchors: 0", "nine fixture PASS", "seven sentinel PASS", "six article-row PASS", "six trajectory-chain PASS"):
                with self.subTest(phrase=phrase):
                    self.assertIn(phrase, qa_text)

    def test_candidate_check_check_only_fails_when_candidate_qa_artifact_is_missing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-check-") as raw_tmp:
            out = Path(raw_tmp) / "candidate-qa.md"
            missing = run_validator([*candidate_check_args(out), "--check-only"])
            self.assertEqual(missing.returncode, 1, missing.stderr)
            summary = decode_map(missing.stdout, "stdout")
            self.assertEqual(summary["status"], "FAIL")
            self.assertEqual(summary["output_path"], None)
            self.assertIn(f"unreadable candidate QA artifact: {out}", json.dumps(summary["failures"], ensure_ascii=False))
            self.assertFalse(out.exists())

    def test_candidate_check_check_only_fails_when_candidate_qa_artifact_is_stale(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-check-") as raw_tmp:
            out = Path(raw_tmp) / "candidate-qa.md"
            write = run_validator(candidate_check_args(out))
            self.assertEqual(write.returncode, 0, write.stderr)
            stale = out.read_text(encoding="utf-8") + "<!-- stale -->\n"
            _ = out.write_text(stale, encoding="utf-8")
            result = run_validator([*candidate_check_args(out), "--check-only"])
            self.assertEqual(result.returncode, 1, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            self.assertEqual(summary["status"], "FAIL")
            self.assertEqual(summary["output_path"], None)
            self.assertIn("candidate QA artifact differs from current evidence set", json.dumps(summary["failures"], ensure_ascii=False))
            self.assertEqual(out.read_text(encoding="utf-8"), stale)

    def test_candidate_check_check_only_passes_without_mutation_when_candidate_qa_matches(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-check-") as raw_tmp:
            out = Path(raw_tmp) / "candidate-qa.md"
            receipt = Path(raw_tmp) / "receipt.jsonl"
            write = run_validator(candidate_check_args(out))
            self.assertEqual(write.returncode, 0, write.stderr)
            before = out.read_bytes()
            result = run_validator([*candidate_check_args(out), "--check-only"])
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(summary["output_path"], None)
            self.assertEqual(out.read_bytes(), before)
            rejected = run_validator([*candidate_check_args(out), "--check-only", "--receipt", str(receipt)])
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(receipt.exists())

    def test_candidate_check_receipt_binds_reviewed_formal_baseline(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-candidate-check-") as raw_tmp:
            out = Path(raw_tmp) / "candidate-qa.md"
            receipt = Path(raw_tmp) / "receipt.jsonl"
            result = run_validator([*candidate_check_args(out), "--receipt", str(receipt)])
            self.assertEqual(result.returncode, 0, result.stderr)
            record = decode_map(receipt.read_text(encoding="utf-8").splitlines()[-1], "receipt")
            self.assertEqual(record["todo"], 7)
            self.assertEqual(record["subcommand"], "candidate-check")
            self.assertEqual(record["status"], "PASS")
            self.assertIn({"path": "路遥/人生/《人生》阅读笔记.md", "phase": "reviewed-baseline", "sha256": REVIEWED_SHA256}, require_list(record["phase_input_hashes"], "phase_input_hashes"))
            self.assertIn(str(FORMAL), json.dumps(record["stable_input_hashes"], ensure_ascii=False))
