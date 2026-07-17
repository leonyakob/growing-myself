from __future__ import annotations

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
FORMAL: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-formal-baseline.md"
TECHNICAL: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-technical-field-inventory.md"
LEDGER: Final = ROOT / ".omo/evidence/ren-sheng-whole-book-consolidation-ledger.md"
TECHNICAL_TOKEN_RE: Final = re.compile(r"源\s*ID|source\s*ID|former\s*ID|chapterUid|bookId|range=|raw_byte_span|line\s*\d+|\bR[1-4]:\d|\d+\s*-\s*\d+", flags=re.IGNORECASE)


def decode_map(text: str, label: str) -> JsonMap:
    return decode_json_map(text, label)


def require_map(value: Json, label: str) -> JsonMap:
    if not isinstance(value, dict):
        raise AssertionError(f"{label} was not a JSON object")
    return value


def run_validator(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATOR), *args], cwd=ROOT, check=False, capture_output=True, text=True)


def anchor_args(out: Path) -> list[str]:
    return ["anchor-check", "--formal", str(FORMAL), "--technical", str(TECHNICAL), "--ledger", str(LEDGER), "--out", str(out)]


def anchor_rows(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    header_line = next(line for line in lines if line.startswith("| formal_key "))
    header = [cell.strip() for cell in header_line.strip("|").split("|")]
    return [dict(zip(header, (cell.strip().replace("\\|", "|") for cell in line.strip("|").split("|")), strict=True)) for line in lines if line.startswith("| F")]


class AnchorCheckContractTests(unittest.TestCase):
    def test_anchor_check_writes_unique_post_transform_map(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-anchor-") as raw_tmp:
            out = Path(raw_tmp) / "anchor-map.md"
            result = run_validator(anchor_args(out))
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = decode_map(result.stdout, "stdout")
            counts = require_map(summary["counts"], "counts")
            self.assertEqual(summary["command"], "anchor-check")
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(counts["post_transform_cards"], 165)
            self.assertEqual(counts["n_new"], 0)
            self.assertEqual(counts["duplicate_readable_anchors"], 0)
            self.assertEqual(counts["unresolved_anchors"], 0)
            self.assertEqual(counts["article_directions"], 6)
            self.assertEqual(counts["trajectory_chains"], 6)
            text = out.read_text(encoding="utf-8")
            for needle in ("Duplicate readable anchors: none", "Unresolved anchors: none", "Article directions: 6", "Trajectory chains: 6", "## 全书收束整合", "阅读现场档案", "文章素材索引", "阅读轨迹与判断变化", "待回看 / 归档不迁移"):
                self.assertIn(needle, text)
            for direction in ("人物线", "城乡主题", "尊严主题", "爱情线", "知识分子困境", "写法线索"):
                self.assertIn(f"| {direction} |", text)
            self.assertEqual(text.count("fixed direction; anchors must resolve"), 6)
            self.assertEqual(text.count("当时的读法 / 后来出现的证据 / 全书后的修正"), 6)
            rows = anchor_rows(text)
            self.assertEqual(len(rows), 165)
            self.assertEqual(len({row["post_transform_anchor"] for row in rows}), 165)
            for row in rows:
                self.assertIsNone(TECHNICAL_TOKEN_RE.search(row["post_transform_anchor"]), row["post_transform_anchor"])

    def test_anchor_check_check_only_writes_nothing_and_rejects_receipt(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-anchor-") as raw_tmp:
            tmp = Path(raw_tmp)
            out = tmp / "anchor-map.md"
            result = run_validator([*anchor_args(out), "--check-only"])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(decode_map(result.stdout, "stdout")["output_path"], None)
            self.assertFalse(out.exists())
            receipt = tmp / "receipt.jsonl"
            rejected = run_validator([*anchor_args(out), "--check-only", "--receipt", str(receipt)])
            self.assertEqual(rejected.returncode, 2)
            self.assertFalse(receipt.exists())

    def test_anchor_check_rejects_incomplete_technical_transform_inventory(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-anchor-") as raw_tmp:
            tmp = Path(raw_tmp)
            bad_technical = tmp / "technical.md"
            text = "\n".join(line for line in TECHNICAL.read_text(encoding="utf-8").splitlines() if not line.startswith("| 1704 |")) + "\n"
            _ = bad_technical.write_text(text, encoding="utf-8")
            result = run_validator(["anchor-check", "--formal", str(FORMAL), "--technical", str(bad_technical), "--ledger", str(LEDGER), "--out", str(tmp / "anchor-map.md"), "--check-only"])
            self.assertEqual(result.returncode, 1)
            self.assertIn("technical", json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False))

    def test_anchor_check_rejects_reader_facing_technical_tokens(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ren-sheng-anchor-") as raw_tmp:
            tmp = Path(raw_tmp)
            bad_technical = tmp / "technical.md"
            text = TECHNICAL.read_text(encoding="utf-8").replace("### 1. 借来的权力光：高玉德为什么非要带弟弟去吃这顿饭 | 150891-150967", "### 1. 借来的权力光：高玉德为什么非要带弟弟去吃这顿饭【源ID：009】 | 150891-150967")
            _ = bad_technical.write_text(text, encoding="utf-8")
            result = run_validator(["anchor-check", "--formal", str(FORMAL), "--technical", str(bad_technical), "--ledger", str(LEDGER), "--out", str(tmp / "anchor-map.md"), "--check-only"])
            self.assertEqual(result.returncode, 1)
            failures = json.dumps(decode_map(result.stdout, "stdout")["failures"], ensure_ascii=False)
            self.assertIn("reader-facing anchors", failures)
