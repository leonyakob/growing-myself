#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

# ─── How to run ───
# 1. Run from the repository root:
#      PYTHONDONTWRITEBYTECODE=1 python3 .omo/evidence/ren-sheng-whole-book-validator-tests.py
# 2. Optional Todo 1 receipt mode:
#      PYTHONDONTWRITEBYTECODE=1 python3 .omo/evidence/ren-sheng-whole-book-validator-tests.py --receipt .omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl
# ──────────────────

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import uuid
from collections.abc import Callable, Sequence
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, Final, TypeAlias

sys.dont_write_bytecode = True
Json: TypeAlias = None | bool | int | float | str | list["Json"] | dict[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]
    LedgerCheckContractTests: type[unittest.TestCase]; PolicyCheckContractTests: type[unittest.TestCase]; AnchorCheckContractTests: type[unittest.TestCase]; CandidateCheckContractTests: type[unittest.TestCase]; FinalCheckContractTests: type[unittest.TestCase]; WaveProtocolContractTests: type[unittest.TestCase]
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map
    ledger_tests = __import__("ren_sheng_whole_book_ledger_tests", fromlist=["LedgerCheckContractTests"]); policy_tests = __import__("ren_sheng_whole_book_policy_tests", fromlist=["PolicyCheckContractTests"]); anchor_tests = __import__("ren_sheng_whole_book_anchor_tests", fromlist=["AnchorCheckContractTests"]); candidate_tests = __import__("ren_sheng_whole_book_candidate_tests", fromlist=["CandidateCheckContractTests"])
    LedgerCheckContractTests = ledger_tests.LedgerCheckContractTests; PolicyCheckContractTests = policy_tests.PolicyCheckContractTests; AnchorCheckContractTests = anchor_tests.AnchorCheckContractTests; CandidateCheckContractTests = candidate_tests.CandidateCheckContractTests
    final_tests = __import__("ren_sheng_whole_book_final_tests", fromlist=["FinalCheckContractTests"]); wave_tests = __import__("ren_sheng_whole_book_wave_tests", fromlist=["WaveProtocolContractTests"])
    FinalCheckContractTests = final_tests.FinalCheckContractTests; WaveProtocolContractTests = wave_tests.WaveProtocolContractTests

ROOT: Final = Path(__file__).resolve().parents[2]
VALIDATOR: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-validator.py"
FORMAL: Final = ROOT / "路遥/人生/《人生》阅读笔记.md"
FORMAL_BASELINE: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-formal-baseline.md"
SOURCE: Final = ROOT / "路遥/人生/《人生》中间整理稿.md"
REVIEWED_SHA256: Final = "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"
SOURCE_SHA256: Final = "dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0"
SOURCE_COUNTS: Final = {"R1": 54, "R2": 52, "R3": 28, "R4": 132}
SOURCE_REGIONS: Final = {"R1": (13, 1895), "R2": (2263, 4441), "R3": (4520, 5973), "R4": (6029, 14733)}
R2_VARIANTS: Final = {"R2:036A": "R2:036", "R2:039A": "R2:039", "R2:040A": "R2:040", "R2:041A": "R2:041", "R2:043A": "R2:043", "R2:046A": "R2:046"}


def sha256_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str: return sha256_bytes(path.read_bytes()) if path.exists() and path.is_file() else "MISSING"


def require_map(value: Json, label: str) -> JsonMap:
    if not isinstance(value, dict):
        raise AssertionError(f"{label} was not a JSON object")
    return value


def require_list(value: Json, label: str) -> list[Json]:
    if not isinstance(value, list):
        raise AssertionError(f"{label} was not a JSON array")
    return value


def decode_map(text: str, label: str) -> JsonMap:
    return decode_json_map(text, label)


def load_validator() -> ModuleType:
    spec = importlib.util.spec_from_file_location("ren_sheng_validator", VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load validator spec: {VALIDATOR}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_validator(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, check=False, capture_output=True, text=True)


def copy_formal_fixture(directory: Path) -> Path: target = directory / "formal.md"; _ = target.write_bytes(FORMAL_BASELINE.read_bytes()); return target


def copy_source_fixture(directory: Path) -> Path: target = directory / "source.md"; _ = target.write_bytes(SOURCE.read_bytes()); return target


def inventory_args(formal: Path, tmp: Path, suffix: str = "") -> list[str]:
    tail = f"-{suffix}" if suffix else ""
    return ["formal-inventory", "--formal", str(formal), "--baseline-copy-out", str(tmp / f"baseline{tail}.md"), "--preservation-out", str(tmp / f"preservation{tail}.md"), "--technical-out", str(tmp / f"technical{tail}.md")]


def source_args(source: Path, out: Path) -> list[str]:
    return ["source-inventory", "--source", str(source), "--out", str(out)]


def manifest_rows(text: str) -> list[dict[str, str]]:
    headers = [cell.strip() for cell in next(line for line in text.splitlines() if line.startswith("| source_key ")).strip("|").split("|")]
    return [dict(zip(headers, (cell.strip() for cell in line.strip("|").split("|")), strict=True)) for line in text.splitlines() if line.startswith("| R")]


def line_starts(data: bytes) -> list[int]:
    starts: list[int] = []
    offset = 0
    for raw in data.splitlines(keepends=True):
        starts.append(offset)
        offset += len(raw)
    return starts


def run_inventory(tmp: Path, suffix: str = "", receipt: Path | None = None) -> tuple[subprocess.CompletedProcess[str], Path, Path, Path]:
    formal = copy_formal_fixture(tmp)
    args = inventory_args(formal, tmp, suffix)
    if receipt is not None:
        args.extend(["--receipt", str(receipt)])
    result = run_validator(args)
    return result, tmp / f"baseline{'-' + suffix if suffix else ''}.md", tmp / f"preservation{'-' + suffix if suffix else ''}.md", tmp / f"technical{'-' + suffix if suffix else ''}.md"


class FormalInventoryContractTests(unittest.TestCase):
    def test_validator_module_is_importable_from_hyphenated_path(self) -> None:
        self.assertTrue(hasattr(load_validator(), "main"))

    def test_formal_inventory_writes_expected_artifacts(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-validator-") as raw_tmp:
            result, baseline, preservation, technical = run_inventory(Path(raw_tmp))
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            counts = require_map(summary["counts"], "counts")
            expected_counts: JsonMap = {"formal_cards": 165, "round_counts": {"R1": 20, "R2": 31, "R3": 15, "R4": 99}, "technical_union": 108, "technical_counts": {"source_id": 99, "spaced_source_id": 3, "metadata": 4, "coordinate_only": 2}, "coordinate_hits": 6, "coordinate_overlaps": 4, "ambiguous_blocks": 0}
            for key, expected in expected_counts.items():
                with self.subTest(key=key):
                    self.assertEqual(counts[key], expected)
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(summary["command"], "formal-inventory")
            self.assertEqual(sha256_path(baseline), REVIEWED_SHA256)
            self.assertEqual(baseline.read_bytes(), (Path(raw_tmp) / "formal.md").read_bytes())
            preservation_text = preservation.read_text(encoding="utf-8")
            technical_text = technical.read_text(encoding="utf-8")
            self.assertEqual(sum(1 for line in preservation_text.splitlines() if line.startswith("| F")), 165)
            self.assertEqual(sum(1 for line in technical_text.splitlines() if line.startswith("| ") and line[2:3].isdigit()), 108)
            for needle in ("Ambiguous blocks: none", "0-"):
                self.assertIn(needle, preservation_text)
            for needle in ("阅读范围：开头至第五章。", "## 第2轮阅读笔记：第五章之后至第八章", "## 第3轮阅读笔记：第八章之后至第十二章", "## 三、人物主线卡（只承载人物弧线补证）", "## 四、轻卡存档 / 阅读心流", "## 五、主题素材库 / 待回看", "### 1. 乡土温情可能带有路遥式理想化", "Coordinate hits: 6", "Coordinate overlaps: 4", "Ambiguous blocks: none"):
                with self.subTest(needle=needle):
                    self.assertIn(needle, technical_text)

    def test_check_only_and_receipt_chain(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-validator-") as raw_tmp:
            tmp = Path(raw_tmp)
            formal = copy_formal_fixture(tmp)
            baseline = tmp / "baseline.md"
            result = run_validator([*inventory_args(formal, tmp), "--check-only"])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIsNone(decode_map(result.stdout, "stdout")["output_path"])
            self.assertFalse(baseline.exists())
            receipt = tmp / "receipt.jsonl"
            rejected = run_validator(["formal-inventory", "--formal", str(formal), "--check-only", "--receipt", str(receipt)])
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(receipt.exists())
            for suffix in ("one", "two"):
                result, _baseline, _preservation, _technical = run_inventory(tmp, suffix, receipt)
                self.assertEqual(result.returncode, 0, result.stderr)
            records = [decode_map(line, "receipt") for line in receipt.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(records[0]["previous_record_hash"], None)
            self.assertEqual(records[1]["previous_record_hash"], records[0]["record_hash"])
            self.assertEqual(records[0]["receipt_prefix_sha256"], sha256_bytes(b""))
            self.assertEqual(sorted(require_map(records[1]["output_hashes"], "output_hashes")), ["baseline_copy", "preservation", "technical"])
            self.assertIn("reviewed-baseline", json.dumps(records[0], ensure_ascii=False))

    def test_stale_input_missing_input_and_bad_outputs_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-validator-") as raw_tmp:
            tmp = Path(raw_tmp)
            stale = copy_formal_fixture(tmp)
            _ = stale.write_text(stale.read_text(encoding="utf-8") + "\n<!-- stale -->\n", encoding="utf-8")
            stale_result = run_validator(inventory_args(stale, tmp))
            self.assertEqual(stale_result.returncode, 1)
            self.assertEqual(decode_map(stale_result.stdout, "stdout")["status"], "FAIL")
            missing_result = run_validator(["formal-inventory", "--formal", str(tmp / "missing.md"), "--check-only"])
            self.assertEqual(missing_result.returncode, 2)
            directory_output = tmp / "directory-output"
            directory_output.mkdir()
            formal = copy_formal_fixture(tmp)
            bad_output = run_validator(["formal-inventory", "--formal", str(formal), "--baseline-copy-out", str(directory_output), "--preservation-out", str(tmp / "preservation.md"), "--technical-out", str(tmp / "technical.md")])
            self.assertEqual(bad_output.returncode, 2)


class SourceInventoryContractTests(unittest.TestCase):
    def test_source_inventory_writes_266_fixed_region_rows(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-source-") as raw_tmp:
            tmp = Path(raw_tmp)
            out = tmp / "source-manifest.md"
            result = run_validator(source_args(copy_source_fixture(tmp), out))
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            counts = require_map(summary["counts"], "counts")
            self.assertEqual(summary["command"], "source-inventory")
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(counts["source_units"], 266)
            self.assertEqual(counts["round_counts"], SOURCE_COUNTS)
            self.assertEqual(counts["r2_variants"], 6)
            self.assertEqual(require_list(summary["input_hashes"], "input_hashes")[0], {"path": str(tmp / "source.md"), "sha256": SOURCE_SHA256})
            text = out.read_text(encoding="utf-8")
            for needle in ("Source units: 266", 'Round counts: {"R1": 54, "R2": 52, "R3": 28, "R4": 132}', "Missing keys: none", "Duplicate keys: none", "Ambiguous boundaries: none", "R2 variants: 6"):
                self.assertIn(needle, text)
            rows = manifest_rows(text)
            row_by_key = {row["source_key"]: row for row in rows}
            self.assertEqual(len(rows), 266)
            self.assertIn("R1:U01", row_by_key)
            for key, base in R2_VARIANTS.items():
                self.assertEqual(row_by_key[key]["variant_of"], base)
            starts = line_starts((tmp / "source.md").read_bytes())
            for row in rows:
                start, end = (int(part) for part in row["raw_byte_span"].split("-"))
                region_start, terminator = SOURCE_REGIONS[row["round"]]
                self.assertGreaterEqual(start, starts[region_start - 1], row["source_key"])
                self.assertLessEqual(end, starts[terminator - 1], row["source_key"])
                for field in ("source_key", "raw_byte_span", "raw_sha256", "normalized_sha256", "quote_blocks", "user_blocks", "external_blocks"):
                    self.assertNotEqual(row[field], "", f"blank {field} for {row['source_key']}")

    def test_source_check_only_writes_nothing_and_rejects_receipt(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-source-") as raw_tmp:
            tmp = Path(raw_tmp)
            out = tmp / "source-manifest.md"
            source = copy_source_fixture(tmp)
            result = run_validator([*source_args(source, out), "--check-only"])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(decode_map(result.stdout, "stdout")["output_path"], None)
            self.assertFalse(out.exists())
            receipt = tmp / "receipt.jsonl"
            rejected = run_validator([*source_args(source, out), "--check-only", "--receipt", str(receipt)])
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(receipt.exists())

    def test_source_malformed_inputs_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-source-") as raw_tmp:
            tmp = Path(raw_tmp)
            source = copy_source_fixture(tmp)
            _ = source.write_text(source.read_text(encoding="utf-8") + "\n<!-- stale -->\n", encoding="utf-8")
            stale = run_validator(source_args(source, tmp / "stale.md"))
            self.assertEqual(stale.returncode, 1)
            self.assertIn("source input SHA-256", json.dumps(decode_map(stale.stdout, "stdout"), ensure_ascii=False))
            missing = run_validator(["source-inventory", "--source", str(tmp / "missing.md"), "--out", str(tmp / "out.md"), "--check-only"])
            self.assertEqual(missing.returncode, 2)
            directory_output = tmp / "directory-output"
            directory_output.mkdir()
            bad_output = run_validator(source_args(copy_source_fixture(tmp), directory_output))
            self.assertEqual(bad_output.returncode, 2)

    def test_source_receipt_appends_todo_2_metadata_and_hash_chain(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-source-") as raw_tmp:
            tmp = Path(raw_tmp)
            receipt = tmp / "receipt.jsonl"
            out = tmp / "source-manifest.md"
            result = run_validator([*source_args(copy_source_fixture(tmp), out), "--receipt", str(receipt)])
            self.assertEqual(result.returncode, 0, result.stderr)
            record = decode_map(receipt.read_text(encoding="utf-8").splitlines()[-1], "receipt")
            self.assertEqual(record["todo"], 2)
            self.assertEqual(record["subcommand"], "source-inventory")
            self.assertEqual(record["status"], "PASS")
            self.assertEqual(record["receipt_prefix_sha256"], sha256_bytes(b""))
            self.assertEqual(record["previous_record_hash"], None)
            self.assertIn(SOURCE_SHA256, json.dumps(record["stable_input_hashes"], ensure_ascii=False))
            self.assertEqual(require_map(record["output_hashes"], "output_hashes")["source_manifest"], sha256_path(out))
            unhashed = dict(record)
            _ = unhashed.pop("record_hash")
            self.assertEqual(record["record_hash"], sha256_bytes(json.dumps(unhashed, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")))


def previous_record_hash(prefix: bytes) -> str | None:
    if not prefix.splitlines():
        return None
    record = decode_map(prefix.splitlines()[-1].decode("utf-8"), "receipt")
    value = record.get("record_hash")
    return value if isinstance(value, str) else None


def append_test_receipt(receipt: Path, result: unittest.TestResult) -> None:
    receipt.parent.mkdir(parents=True, exist_ok=True)
    prefix = receipt.read_bytes() if receipt.exists() else b""
    failures: list[Json] = [str(item[1]) for item in [*result.failures, *result.errors]]
    record: JsonMap = {"schema_version": 1, "todo": 1, "subcommand": "validator-tests", "attempt_id": str(uuid.uuid4()), "attempted_at": datetime.now(timezone.utc).isoformat(), "stable_input_hashes": [{"path": str(VALIDATOR.relative_to(ROOT)), "sha256": sha256_path(VALIDATOR)}, {"path": str(Path(__file__).resolve().relative_to(ROOT)), "sha256": sha256_path(Path(__file__).resolve())}, {"path": str(FORMAL.relative_to(ROOT)), "sha256": sha256_path(FORMAL)}], "phase_input_hashes": [{"path": str(FORMAL.relative_to(ROOT)), "phase": "reviewed-baseline", "sha256": sha256_path(FORMAL)}], "output_hashes": {}, "status": "PASS" if result.wasSuccessful() else "FAIL", "failures": failures, "supersedes_attempt_id": None, "receipt_prefix_sha256": sha256_bytes(prefix), "previous_record_hash": previous_record_hash(prefix)}
    record["record_hash"] = sha256_bytes(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    with receipt.open("ab") as handle:
        _ = handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True).encode("utf-8") + b"\n")


def parse_receipt_arg(argv: Sequence[str]) -> Path | None:
    if not argv:
        return None
    if len(argv) == 2 and argv[0] == "--receipt":
        return Path(argv[1])
    raise SystemExit("usage: ren-sheng-whole-book-validator-tests.py [--receipt PATH]")


def main(argv: Sequence[str] | None = None) -> int:
    receipt = parse_receipt_arg(sys.argv[1:] if argv is None else argv)
    suite = unittest.TestSuite((unittest.defaultTestLoader.loadTestsFromTestCase(FormalInventoryContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(SourceInventoryContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(LedgerCheckContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(PolicyCheckContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(AnchorCheckContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(CandidateCheckContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(FinalCheckContractTests), unittest.defaultTestLoader.loadTestsFromTestCase(WaveProtocolContractTests)))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if isinstance(receipt, Path):
        append_test_receipt(receipt, result)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
