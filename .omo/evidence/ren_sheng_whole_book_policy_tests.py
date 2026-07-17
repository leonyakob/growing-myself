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
FIXTURE: Final = ROOT / ".omo/evidence/fixtures/add-whole-book-consolidation-model.md"
RESULTS: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-fixture-results.md"
LEDGER: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-consolidation-ledger.md"
FORMAL_MANIFEST: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-preservation-manifest.md"


def decode_map(text: str, label: str) -> JsonMap:
    return decode_json_map(text, label)


def run_validator(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, check=False, capture_output=True, text=True)


def policy_args(results: Path) -> list[str]:
    return ["policy-check", "--fixture", str(FIXTURE), "--results", str(results), "--ledger", str(LEDGER), "--formal-manifest", str(FORMAL_MANIFEST)]


class PolicyCheckContractTests(unittest.TestCase):
    def test_policy_check_accepts_fixture_and_sentinel_results(self) -> None:
        result = run_validator([*policy_args(RESULTS), "--check-only"])
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = decode_map(result.stdout, "stdout")
        self.assertEqual(summary["command"], "policy-check")
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual(summary["counts"], {"fixture_rows": 9, "sentinel_rows": 7})

    def test_policy_check_rejects_missing_case_7_external_only_row(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-policy-") as raw_tmp:
            bad_results = Path(raw_tmp) / "bad-policy.md"
            text = "\n".join(line for line in RESULTS.read_text(encoding="utf-8").splitlines() if not line.startswith("| Case 7 |")) + "\n"
            _ = bad_results.write_text(text, encoding="utf-8")
            result = run_validator([*policy_args(bad_results), "--check-only"])
            self.assertEqual(result.returncode, 1)
            failures = json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False)
            self.assertIn("Case 7", failures)
