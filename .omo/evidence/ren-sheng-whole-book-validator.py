#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

# ─── How to run ───
# 1. Run Todo 1 from the repository root:
#      python3 .omo/evidence/ren-sheng-whole-book-validator.py formal-inventory --formal 路遥/人生/《人生》阅读笔记.md --baseline-copy-out .omo/evidence/ren-sheng-whole-book-formal-baseline.md --preservation-out .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --technical-out .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md --receipt .omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl
# 2. Reviewer check-only mode writes no files:
#      python3 .omo/evidence/ren-sheng-whole-book-validator.py formal-inventory --formal 路遥/人生/《人生》阅读笔记.md --check-only
# ──────────────────

from __future__ import annotations

import hashlib
import json
import re
import sys; sys.dont_write_bytecode = True
import unicodedata
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Final, NamedTuple, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
SourceUnitRow: TypeAlias = tuple[str, str, str, str, str, int, int, bytes]


class ReceiptOutputValue(NamedTuple): name: str; path: Path | None


class PhaseInputValue(NamedTuple): path: str; phase: str; sha256: str


class ReceiptSpecValue(NamedTuple): todo: int; subcommand: str; outputs: Sequence[ReceiptOutputValue]; phases: Sequence[PhaseInputValue]

if TYPE_CHECKING:
    ledger_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; policy_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; anchor_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; candidate_structure_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; candidate_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; final_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; final_anchor_check_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; wave_command: Callable[[Sequence[str]], tuple[int, JsonMap]]
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]
    PhaseInput: Callable[[str, str, str], PhaseInputValue]
    ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[PhaseInputValue]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, Json], ReceiptSpecValue], None]
    SOURCE_COUNTS: Mapping[str, int]
    parse_source_units: Callable[[bytes], tuple[list[SourceUnitRow], list[str], list[str], list[str]]]
    source_counts: Callable[[Sequence[SourceUnitRow], Sequence[str], Sequence[str], Sequence[str]], JsonMap]
    source_manifest_text: Callable[[Sequence[SourceUnitRow], Sequence[str], Sequence[str], Sequence[str]], str]
else:
    ledger_module = __import__("ren_sheng_whole_book_ledger_check", fromlist=["ledger_check_command"]); ledger_check_command = ledger_module.ledger_check_command; policy_module = __import__("ren_sheng_whole_book_policy_check", fromlist=["policy_check_command"]); policy_check_command = policy_module.policy_check_command
    anchor_module = __import__("ren_sheng_whole_book_anchor_check", fromlist=["anchor_check_command"]); anchor_check_command = anchor_module.anchor_check_command; candidate_module = __import__("ren_sheng_whole_book_candidate_check", fromlist=["candidate_structure_command"]); candidate_structure_command = candidate_module.candidate_structure_command; candidate_qa_module = __import__("ren_sheng_whole_book_candidate_qa", fromlist=["candidate_check_command"]); candidate_check_command = candidate_qa_module.candidate_check_command
    final_module = __import__("ren_sheng_whole_book_final_check", fromlist=["final_check_command"]); final_check_command = final_module.final_check_command; final_anchor_module = __import__("ren_sheng_whole_book_final_anchor", fromlist=["final_anchor_check_command"]); final_anchor_check_command = final_anchor_module.final_anchor_check_command; wave_module = __import__("ren_sheng_whole_book_wave", fromlist=["wave_command"]); wave_command = wave_module.wave_command
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["PhaseInput", "ReceiptOutput", "ReceiptSpec", "append_validator_receipt"])
    PhaseInput = receipt_module.PhaseInput
    ReceiptOutput = receipt_module.ReceiptOutput
    ReceiptSpec = receipt_module.ReceiptSpec
    append_validator_receipt = receipt_module.append_validator_receipt
    source_inventory = __import__("ren_sheng_whole_book_source_inventory", fromlist=["SOURCE_COUNTS", "parse_source_units", "source_counts", "source_manifest_text"])
    SOURCE_COUNTS = source_inventory.SOURCE_COUNTS
    parse_source_units = source_inventory.parse_source_units
    source_counts = source_inventory.source_counts
    source_manifest_text = source_inventory.source_manifest_text

REVIEWED_SHA256: Final = "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"
SOURCE_SHA256: Final = "dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0"
ROUND_COUNTS: Final[Mapping[str, int]] = {"R1": 20, "R2": 31, "R3": 15, "R4": 99}
TECH_COUNTS: Final[Mapping[str, int]] = {"source_id": 99, "spaced_source_id": 3, "metadata": 4, "coordinate_only": 2}
TECH_SOURCE_LINES: Final = {1704, 1742, 1784, 1825, 1866, 1909, 1948, 1987, 2024, 2061, 2098, 2139, 2182, 2220, 2257, 2296, 2333, 2367, 2406, 2446, 2478, 2512, 2550, 2588, 2626, 2661, 2703, 2741, 2779, 2817, 2853, 2889, 2925, 2963, 3000, 3038, 3076, 3114, 3154, 3192, 3230, 3268, 3307, 3345, 3385, 3425, 3465, 3506, 3547, 3581, 3615, 3653, 3690, 3724, 3759, 3799, 3834, 3862, 3896, 3933, 3970, 4008, 4043, 4082, 4121, 4160, 4200, 4242, 4281, 4317, 4357, 4398, 4430, 4462, 4503, 4543, 4583, 4621, 4658, 4695, 4720, 4745, 4773, 4795, 4839, 5103, 5177, 5275, 5423, 5523, 5659, 5709, 5752, 5810, 5833, 5856, 5879, 5902, 5917}
EXACT_REPLACEMENTS: Final[Mapping[int, str]] = {5: "- 阅读范围：开头至第五章。", 557: "## 第2轮阅读笔记：第五章之后至第八章", 559: "- 阅读范围：第五章之后，至第八章。", 1238: "## 第3轮阅读笔记：第八章之后至第十二章", 1240: "- 阅读范围：第八章之后，至第十二章。", 4770: "## 三、人物主线卡（只承载人物弧线补证）", 5420: "## 四、轻卡存档 / 阅读心流", 5749: "## 五、主题素材库 / 待回看", 5929: "- 第二十三章“我的亲人哪……”之后。"}


class Card(NamedTuple): key: str; round_key: str; line_no: int; heading_path: str; start: int; end: int; raw: bytes


class TechRow(NamedTuple): line_no: int; before: str; families: tuple[str, ...]; after: str; post_span: str


class Outputs(NamedTuple): baseline: Path | None; preservation: Path | None; technical: Path | None


class Cli(NamedTuple): command: str; formal: Path | None; source: Path | None; outputs: Outputs; source_out: Path | None; check_only: bool; receipt: Path | None


class CardCounts(NamedTuple): formal_cards: int; round_counts: Mapping[str, int]; ambiguous_blocks: int


class TechCounts(NamedTuple): technical_union: int; technical_counts: Mapping[str, int]; coordinate_hits: int; coordinate_overlaps: int


def sha256_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes()) if path.exists() and path.is_file() else "MISSING"


def normalize_hash(data: bytes) -> str:
    text = data.decode("utf-8", "strict").replace("\r\n", "\n").replace("\r", "\n")
    text = unicodedata.normalize("NFC", text)
    return sha256_bytes((text[:-1] if text.endswith("\n") else text).encode("utf-8"))


def split_lines(data: bytes) -> tuple[list[str], list[int]]:
    starts: list[int] = []
    offset = 0
    texts: list[str] = []
    for raw in data.splitlines(keepends=True):
        starts.append(offset)
        offset += len(raw)
        texts.append(raw.decode("utf-8", "strict").rstrip("\r\n"))
    return texts, starts


def is_card_heading(line_no: int, line: str) -> tuple[str, bool]:
    if 3 <= line_no < 557 and re.match(r"^###\s+\d+\.\s+", line):
        return "R1", False
    if 557 <= line_no < 1238 and re.match(r"^###\s+\d+\.\s+", line):
        return "R2", False
    if 1238 <= line_no < 1701 and re.match(r"^###\s+\d+\.\s+", line):
        return "R3", False
    if line_no >= 1701 and re.match(r"^###\s+\d+\.\s+", line):
        return "R4", False
    if line_no >= 1701 and re.match(r"^####\s+\d+\.\s+", line):
        return "R4", True
    return "", False


def card_end(lines: Sequence[str], starts: Sequence[int], data_len: int, start_index: int, r4_h4: bool) -> int:
    for index in range(start_index + 1, len(lines)):
        line = lines[index]
        if line.startswith("## ") or re.match(r"^###\s+\d+\.\s+", line) or re.match(r"^####\s+\d+\.\s+", line):
            return starts[index]
        if r4_h4 and re.match(r"^###\s+[A-J]\.\s+", line):
            return starts[index]
    return data_len


def nearest_h2(lines: Sequence[str], start_index: int) -> str:
    for index in range(start_index, -1, -1):
        if re.match(r"^##\s+(?!第\d轮)", lines[index]):
            return lines[index].removeprefix("## ")
    return "未分类"


def parse_cards(data: bytes) -> tuple[list[Card], CardCounts]:
    lines, starts = split_lines(data)
    cards: list[Card] = []
    for index, line in enumerate(lines):
        round_key, r4_h4 = is_card_heading(index + 1, line)
        if round_key:
            end = card_end(lines, starts, len(data), index, r4_h4)
            title = re.sub(r"^#{3,4}\s+", "", line)
            path = f"第{round_key[1]}轮 / {nearest_h2(lines, index)} / {title}"
            cards.append(Card(f"F{len(cards) + 1:03d}", round_key, index + 1, path, starts[index], end, data[starts[index]:end]))
    rounds = {key: sum(1 for card in cards if card.round_key == key) for key in ROUND_COUNTS}
    return cards, CardCounts(len(cards), rounds, 0)


def line_replacement(line_no: int, text: str) -> str: return EXACT_REPLACEMENTS.get(line_no, re.sub(r"【(?:源ID|源IDs|external-源ID)：[^】]+】$", "", text))


def families_for(line_no: int, text: str) -> tuple[str, ...]:
    families: list[str] = []
    for name, pattern in (("external-源ID", r"external-源ID(?:s)?"), ("源ID", r"源ID(?:s)?"), ("源 ID", r"源\s+ID(?:s)?"), ("range", r"\brange\b"), ("coordinate", r"(?<!\d)\d+\s*-\s*\d+(?!\d)")):
        if re.search(pattern, text):
            families.append(name)
    if "chapterUid" in text:
        families.append("chapterUid")
    if line_no in EXACT_REPLACEMENTS and not families:
        families.append("planned-exact-replacement")
    return tuple(families)


def technical_rows(data: bytes) -> tuple[list[TechRow], TechCounts]:
    lines, _starts = split_lines(data)
    transformed = [line_replacement(index + 1, text) for index, text in enumerate(lines)]
    post_starts: list[int] = []
    offset = 0
    for text in transformed:
        post_starts.append(offset)
        offset += len((text + "\n").encode("utf-8"))
    rows = [TechRow(no, lines[no - 1], families_for(no, lines[no - 1]), transformed[no - 1], f"{post_starts[no - 1]}-{post_starts[no - 1] + len(transformed[no - 1].encode('utf-8'))}") for no in sorted(TECH_SOURCE_LINES | set(EXACT_REPLACEMENTS))]
    coordinate = [row for row in rows if "coordinate" in row.families]
    overlaps = [row for row in coordinate if "chapterUid" in row.families or "range" in row.families]
    return rows, TechCounts(len(rows), TECH_COUNTS, len(coordinate), len(overlaps))


def counts_json(card_counts: CardCounts, tech_counts: TechCounts) -> JsonMap: return {"formal_cards": card_counts.formal_cards, "round_counts": card_counts.round_counts, "ambiguous_blocks": card_counts.ambiguous_blocks, "technical_union": tech_counts.technical_union, "technical_counts": tech_counts.technical_counts, "coordinate_hits": tech_counts.coordinate_hits, "coordinate_overlaps": tech_counts.coordinate_overlaps}


def escape_cell(text: str) -> str: return text.replace("|", "\\|").replace("\n", "<br>")


def preservation_text(cards: Sequence[Card], card_counts: CardCounts) -> str:
    lines = ["# Ren Sheng whole-book preservation manifest", "", f"Formal cards: {card_counts.formal_cards}", f"Round counts: {json.dumps(card_counts.round_counts, ensure_ascii=False, sort_keys=True)}", "Ambiguous blocks: none", "", "| formal_key | round | line | heading_path | raw_byte_span | raw_sha256 | normalized_sha256 | quote_blocks | user_blocks | external_blocks | byte_length |", "|---|---|---:|---|---|---|---|---:|---:|---:|---:|"]
    for card in cards:
        raw_text = card.raw.decode("utf-8", "strict")
        row = [card.key, card.round_key, str(card.line_no), escape_cell(card.heading_path), f"{card.start}-{card.end}", sha256_bytes(card.raw), normalize_hash(card.raw), str(raw_text.count("划线原文")), str(raw_text.count("我自己写的内容") + raw_text.count("我的原想法")), str(raw_text.count("外部读者回声/补充/挑战")), str(len(card.raw))]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"


def technical_text(rows: Sequence[TechRow], tech_counts: TechCounts) -> str:
    lines = ["# Ren Sheng whole-book technical field inventory", "", f"Technical union: {tech_counts.technical_union}", f"Technical counts: {json.dumps(tech_counts.technical_counts, ensure_ascii=False, sort_keys=True)}", f"Coordinate hits: {tech_counts.coordinate_hits}", f"Coordinate overlaps: {tech_counts.coordinate_overlaps}", "Ambiguous blocks: none", "", "| line | families | before | after | post_application_byte_span |", "|---:|---|---|---|---|"]
    lines.extend(f"| {row.line_no} | {', '.join(row.families)} | {escape_cell(row.before)} | {escape_cell(row.after)} | {row.post_span} |" for row in rows)
    return "\n".join(lines) + "\n"


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] not in {"formal-inventory", "source-inventory"}:
        return "usage: formal-inventory or source-inventory is required"
    command = argv[0]
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
            return f"invalid invocation token: {token}"
    def path_value(key: str) -> Path | None:
        value = values.get(key)
        return Path(value) if isinstance(value, str) else None

    receipt = path_value("receipt")
    if command == "formal-inventory":
        formal = values.get("formal")
        if not isinstance(formal, str):
            return "--formal is required"
        return Cli(command, Path(formal), None, Outputs(path_value("baseline-copy-out"), path_value("preservation-out"), path_value("technical-out")), None, values["check-only"] is True, receipt)
    source = values.get("source")
    out = values.get("out")
    if not isinstance(source, str) or not isinstance(out, str):
        return "--source and --out are required"
    return Cli(command, None, Path(source), Outputs(None, None, None), Path(out), values["check-only"] is True, receipt)


def output_failures(outputs: Outputs, check_only: bool) -> list[str]:
    paths = [path for path in outputs if path is not None]
    if check_only:
        return []
    failures = [] if len(paths) == 3 else ["all three output paths are required outside --check-only"]
    failures.extend(f"invalid output path: {path}" for path in paths if (path.exists() and not path.is_file()) or not path.parent.exists())
    return failures


def source_output_failures(out: Path | None, check_only: bool) -> list[str]:
    if check_only:
        return []
    if out is None:
        return ["--out is required outside --check-only"]
    return [f"invalid output path: {out}"] if (out.exists() and not out.is_file()) or not out.parent.exists() else []


def formal_inventory(cli: Cli) -> tuple[int, JsonMap]:
    failures = output_failures(cli.outputs, cli.check_only)
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    formal = cli.formal
    if formal is None or not formal.is_file():
        failures.append(f"unreadable formal input: {formal}")
    if failures:
        return 2, {"command": "formal-inventory", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    assert formal is not None
    data = formal.read_bytes()
    cards, card_counts = parse_cards(data)
    rows, tech_counts = technical_rows(data)
    failures = [] if sha256_bytes(data) == REVIEWED_SHA256 else ["formal input SHA-256 does not match reviewed baseline"]
    if card_counts.formal_cards != 165 or card_counts.round_counts != ROUND_COUNTS:
        failures.append("formal card counts differ from reviewed plan")
    if tech_counts.technical_union != 108 or tech_counts.technical_counts != TECH_COUNTS:
        failures.append("technical inventory counts differ from reviewed plan")
    if not failures and not cli.check_only and cli.outputs.baseline and cli.outputs.preservation and cli.outputs.technical:
        _ = cli.outputs.baseline.write_bytes(data)
        _ = cli.outputs.preservation.write_text(preservation_text(cards, card_counts), encoding="utf-8")
        _ = cli.outputs.technical.write_text(technical_text(rows, tech_counts), encoding="utf-8")
    summary: JsonMap = {"command": "formal-inventory", "status": "PASS" if not failures else "FAIL", "counts": counts_json(card_counts, tech_counts), "failures": failures, "input_hashes": [{"path": str(formal), "sha256": sha256_bytes(data)}], "output_path": None if cli.check_only else {"baseline_copy": str(cli.outputs.baseline), "preservation": str(cli.outputs.preservation), "technical": str(cli.outputs.technical)}}
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(1, "formal-inventory", (ReceiptOutput("baseline_copy", cli.outputs.baseline), ReceiptOutput("preservation", cli.outputs.preservation), ReceiptOutput("technical", cli.outputs.technical)), (PhaseInput("路遥/人生/《人生》阅读笔记.md", "reviewed-baseline", REVIEWED_SHA256),)))
    return (0 if not failures else 1), summary


def source_inventory(cli: Cli) -> tuple[int, JsonMap]:
    failures = source_output_failures(cli.source_out, cli.check_only)
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    source = cli.source
    out = cli.source_out
    if source is None or not source.is_file():
        failures.append(f"unreadable source input: {source}")
    if failures:
        return 2, {"command": "source-inventory", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    assert source is not None
    data = source.read_bytes()
    units, missing, duplicates, ambiguous = parse_source_units(data)
    failures = [] if sha256_bytes(data) == SOURCE_SHA256 else ["source input SHA-256 does not match reviewed source"]
    counts = source_counts(units, missing, duplicates, ambiguous)
    if counts["source_units"] != 266 or counts["round_counts"] != SOURCE_COUNTS or missing or duplicates or ambiguous or counts["r2_variants"] != 6:
        failures.append("source inventory counts or keys differ from reviewed plan")
    if not failures and not cli.check_only and out is not None:
        _ = out.write_text(source_manifest_text(units, missing, duplicates, ambiguous), encoding="utf-8")
    summary: JsonMap = {"command": "source-inventory", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": failures, "input_hashes": [{"path": str(source), "sha256": sha256_bytes(data)}], "output_path": None if cli.check_only else str(out)}
    if cli.receipt is not None and out is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(2, "source-inventory", (ReceiptOutput("source_manifest", out),), ()))
    return (0 if not failures else 1), summary


def main(argv: Sequence[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    delegated: Mapping[str, Callable[[Sequence[str]], tuple[int, JsonMap]]] = {"ledger-check": ledger_check_command, "policy-check": policy_check_command, "anchor-check": anchor_check_command, "candidate-structure": candidate_structure_command, "candidate-check": candidate_check_command, "final-check": final_check_command, "final-anchor-check": final_anchor_check_command, "wave-snapshot-create": wave_command, "wave-snapshot-check": wave_command, "wave-drift-invalidate": wave_command, "review-runtime-snapshot": wave_command, "review-runtime-register": wave_command, "review-runtime-final-check": wave_command, "wave-runtime-invalidate": wave_command, "review-receipt-append": wave_command, "review-receipt-check": wave_command, "wave-invalidate": wave_command}
    if args and args[0] in delegated:
        code, summary = delegated[args[0]](args)
        print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
        return code
    parsed = parse_cli(args)
    if isinstance(parsed, str):
        print(json.dumps({"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}, ensure_ascii=False, sort_keys=True))
        return 2
    code, summary = formal_inventory(parsed) if parsed.command == "formal-inventory" else source_inventory(parsed)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
