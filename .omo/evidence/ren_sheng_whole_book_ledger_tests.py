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
SOURCE_MANIFEST: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-source-manifest.md"
FORMAL_MANIFEST: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-preservation-manifest.md"
LEDGER: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-consolidation-ledger.md"
RECONCILIATION: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-reconciliation.md"
FIXTURE: Final = ROOT / ".omo/evidence/fixtures/add-whole-book-consolidation-model.md"
SET_NAMES: Final = ["source-only", "formal-only", "one-to-one", "many-to-one", "duplicate", "revision-chain", "planned-new-formal", "unresolved"]


def decode_map(text: str, label: str) -> JsonMap:
    return decode_json_map(text, label)


def require_map(value: Json, label: str) -> JsonMap:
    if not isinstance(value, dict):
        raise AssertionError(f"{label} was not a JSON object")
    return value


def run_validator(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, check=False, capture_output=True, text=True)


def ledger_args(ledger: Path, reconciliation: Path) -> list[str]:
    return ["ledger-check", "--source-manifest", str(SOURCE_MANIFEST), "--formal-manifest", str(FORMAL_MANIFEST), "--ledger", str(ledger), "--reconciliation", str(reconciliation), "--fixture", str(FIXTURE)]


class LedgerCheckContractTests(unittest.TestCase):
    def test_ledger_check_accepts_closed_todo3_artifacts(self) -> None:
        result = run_validator([*ledger_args(LEDGER, RECONCILIATION), "--check-only"])
        self.assertEqual(result.returncode, 0, result.stderr)
        summary = decode_map(result.stdout, "stdout")
        counts = require_map(summary["counts"], "counts")
        sets = require_map(counts["sets"], "sets")
        self.assertEqual(summary["command"], "ledger-check")
        self.assertEqual(summary["status"], "PASS")
        self.assertEqual(counts["source_rows"], 266)
        self.assertEqual(counts["formal_rows"], 165)
        self.assertEqual(sorted(sets), sorted(SET_NAMES))
        self.assertEqual(sets["unresolved"], 0)
        self.assertEqual(counts["n_new"], sets["planned-new-formal"])

    def test_ledger_check_rejects_missing_unbound_relation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-ledger-") as raw_tmp:
            bad_ledger = Path(raw_tmp) / "ledger.md"
            _ = bad_ledger.write_text(LEDGER.read_text(encoding="utf-8").replace(" | present-verbatim |", " | missing-unbound |", 1), encoding="utf-8")
            result = run_validator([*ledger_args(bad_ledger, RECONCILIATION), "--check-only"])
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing-unbound", json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False))
