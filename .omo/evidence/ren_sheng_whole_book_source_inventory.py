from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections.abc import Mapping, Sequence
from typing import Final, NamedTuple, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

SOURCE_COUNTS: Final[Mapping[str, int]] = {"R1": 54, "R2": 52, "R3": 28, "R4": 132}
SOURCE_REGIONS: Final[Mapping[str, tuple[int, int]]] = {"R1": (13, 1895), "R2": (2263, 4441), "R3": (4520, 5973), "R4": (6029, 14733)}
SOURCE_EXPECTED: Final[Mapping[str, tuple[str, ...]]] = {"R1": tuple(f"{number:03d}" for number in range(1, 54)) + ("U01",), "R2": tuple(f"{number:03d}" for number in range(1, 47)) + ("036A", "039A", "040A", "041A", "043A", "046A"), "R3": tuple(f"{number:03d}" for number in range(1, 29)), "R4": tuple(f"{number:03d}" for number in range(1, 133))}
SOURCE_VARIANTS: Final[Mapping[str, str]] = {"R2:036A": "R2:036", "R2:039A": "R2:039", "R2:040A": "R2:040", "R2:041A": "R2:041", "R2:043A": "R2:043", "R2:046A": "R2:046"}
SOURCE_H3_RE: Final = re.compile(r"^###\s+(?P<unit>\d{3}[A-Z]?|U\d{2})\.\s+(?P<title>.+)$")


class SourceUnit(NamedTuple): key: str; round_key: str; unit: str; variant_of: str; heading: str; start: int; end: int; raw: bytes


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>")


def parse_source_units(data: bytes) -> tuple[list[SourceUnit], list[str], list[str], list[str]]:
    lines, starts = split_lines(data)
    units: list[SourceUnit] = []
    ambiguous: list[str] = []
    for round_key, (start_line, terminator_line) in SOURCE_REGIONS.items():
        region_end = starts[terminator_line - 1]
        hits: list[tuple[int, re.Match[str]]] = []
        for index in range(start_line - 1, terminator_line - 1):
            match = SOURCE_H3_RE.match(lines[index])
            if match:
                hits.append((index, match))
        for position, (index, match) in enumerate(hits):
            end = starts[hits[position + 1][0]] if position + 1 < len(hits) else region_end
            unit = match.group("unit")
            key = f"{round_key}:{unit}"
            if not (starts[index] < end <= region_end):
                ambiguous.append(key)
            units.append(SourceUnit(key, round_key, unit, SOURCE_VARIANTS.get(key, ""), lines[index], starts[index], end, data[starts[index]:end]))
    keys = [unit.key for unit in units]
    expected = {f"{round_key}:{unit}" for round_key, round_units in SOURCE_EXPECTED.items() for unit in round_units}
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    missing = sorted(expected.difference(keys))
    ambiguous.extend(sorted(set(keys).difference(expected)))
    return units, missing, duplicates, sorted(ambiguous)


def source_counts(units: Sequence[SourceUnit], missing: Sequence[str], duplicates: Sequence[str], ambiguous: Sequence[str]) -> JsonMap:
    return {"source_units": len(units), "round_counts": {key: sum(1 for unit in units if unit.round_key == key) for key in SOURCE_COUNTS}, "missing_keys": list(missing), "duplicate_keys": list(duplicates), "ambiguous_boundaries": list(ambiguous), "r2_variants": sum(1 for unit in units if unit.variant_of)}


def excerpt(text: str, markers: Sequence[str]) -> str:
    source_lines = text.splitlines()
    for index, line in enumerate(source_lines):
        if any(marker in line for marker in markers):
            for candidate in source_lines[index + 1:]:
                stripped = candidate.strip().removeprefix("> ").removeprefix("- ").strip()
                if stripped and not stripped.startswith("**"):
                    return stripped[:96]
    return ""


def source_manifest_text(units: Sequence[SourceUnit], missing: Sequence[str], duplicates: Sequence[str], ambiguous: Sequence[str]) -> str:
    lines = ["# Ren Sheng whole-book source manifest", "", f"Source units: {len(units)}", f"Round counts: {json.dumps({key: sum(1 for unit in units if unit.round_key == key) for key in SOURCE_COUNTS}, ensure_ascii=False, sort_keys=True)}", f"Missing keys: {', '.join(missing) if missing else 'none'}", f"Duplicate keys: {', '.join(duplicates) if duplicates else 'none'}", f"Ambiguous boundaries: {', '.join(ambiguous) if ambiguous else 'none'}", f"R2 variants: {sum(1 for unit in units if unit.variant_of)}", "", "| source_key | round | unit | variant_of | heading | raw_byte_span | raw_sha256 | normalized_sha256 | quote_blocks | user_blocks | external_blocks | representative_quote | representative_user | representative_external |", "|---|---|---|---|---|---|---|---|---:|---:|---:|---|---|---|"]
    for unit in units:
        raw_text = unit.raw.decode("utf-8", "strict")
        row = [unit.key, unit.round_key, unit.unit, unit.variant_of, escape_cell(unit.heading), f"{unit.start}-{unit.end}", sha256_bytes(unit.raw), normalize_hash(unit.raw), str(raw_text.count("**划线原文：**")), str(raw_text.count("**我的原想法：**") + raw_text.count("**我自己写的内容：**")), str(raw_text.count("同位置其他书友高赞想法（外部读者）") + raw_text.count("第4轮外部高赞想法补正")), escape_cell(excerpt(raw_text, ("**划线原文：**",))), escape_cell(excerpt(raw_text, ("**我的原想法：**", "**我自己写的内容：**"))), escape_cell(excerpt(raw_text, ("同位置其他书友高赞想法（外部读者）", "第4轮外部高赞想法补正")))]
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines) + "\n"
