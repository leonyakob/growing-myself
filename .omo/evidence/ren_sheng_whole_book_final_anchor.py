from __future__ import annotations

import hashlib
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

FINAL_FORMAL_SHA256: Final = "03cbe76f586b80a68db054f13d2dac04e5ee743d979dac4631b95ef54b25063f"
TECHNICAL_TOKEN_RE: Final = re.compile(r"external-源ID(?:s)?|源ID(?:s)?|源\s+ID(?:s)?|chapterUid|bookId|\brange\b|(?<!\d)\d+\s*-\s*\d+(?!\d)")


@dataclass(frozen=True, slots=True)
class Cli:
    formal: Path
    ledger: Path
    anchor_map: Path
    check_only: bool


@dataclass(frozen=True, slots=True)
class Row:
    cells: Mapping[str, str]

    def get(self, key: str) -> str:
        return self.cells.get(key, "").strip()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split_cells(line: str) -> tuple[str, ...]:
    return tuple(cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|"))


def table_rows(text: str, first_column: str) -> tuple[Row, ...]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| {first_column} "):
            header = split_cells(line)
            rows: list[Row] = []
            for raw in lines[index + 2:]:
                if not raw.startswith("|"):
                    break
                rows.append(Row(dict(zip(header, split_cells(raw), strict=True))))
            return tuple(rows)
    return ()


def int_metric(text: str, label: str) -> int:
    match = re.search(rf"(?m)^-?\s*{re.escape(label)}:\s*(\d+|none)\s*$", text)
    if match is None or match.group(1) == "none":
        return 0
    return int(match.group(1))


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


def nearest_h2(lines: Sequence[str], start_index: int) -> str:
    for index in range(start_index, -1, -1):
        if re.match(r"^##\s+(?!第\d轮)", lines[index]):
            return lines[index].removeprefix("## ")
    return "未分类"


def formal_paths(text: str) -> tuple[str, ...]:
    lines = text.splitlines()
    paths: list[str] = []
    for index, line in enumerate(lines):
        round_key, _r4_h4 = is_card_heading(index + 1, line)
        if round_key:
            title = re.sub(r"^#{3,4}\s+", "", line)
            paths.append(f"第{round_key[1]}轮 / {nearest_h2(lines, index)} / {title}")
    return tuple(paths)


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "final-anchor-check":
        return "usage: final-anchor-check is required"
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
    if not isinstance(values.get("formal"), str) or not isinstance(values.get("ledger"), str) or not isinstance(values.get("anchor-map"), str):
        return "--formal --ledger and --anchor-map are required"
    return Cli(Path(str(values["formal"])), Path(str(values["ledger"])), Path(str(values["anchor-map"])), values["check-only"] is True)


def validate(cli: Cli) -> tuple[int, JsonMap]:
    inputs = (cli.formal, cli.ledger, cli.anchor_map)
    failures = [f"unreadable input: {path}" for path in inputs if not path.is_file()]
    if failures:
        return 2, {"command": "final-anchor-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    formal_text = cli.formal.read_text(encoding="utf-8")
    anchor_text = cli.anchor_map.read_text(encoding="utf-8")
    ledger_text = cli.ledger.read_text(encoding="utf-8")
    paths = formal_paths(formal_text)
    anchor_rows = table_rows(anchor_text, "formal_key")
    ledger_rows = table_rows(ledger_text, "formal_key")
    anchor_paths = tuple(row.get("post_transform_anchor") for row in anchor_rows)
    article_links_none = sum(1 for row in anchor_rows if row.get("article_links") == "none" and row.get("insertion_target") == "none")
    duplicate_anchors = len(anchor_paths) - len(set(anchor_paths))
    unresolved_anchors = sum(1 for anchor in anchor_paths if TECHNICAL_TOKEN_RE.search(anchor) is not None)
    n_new = int_metric(anchor_text, "N_new")
    actual_sha = sha256_bytes(cli.formal.read_bytes())
    if actual_sha != FINAL_FORMAL_SHA256:
        failures.append(f"formal note SHA-256 drift: expected {FINAL_FORMAL_SHA256} got {actual_sha}")
    if len(paths) != 165 or len(anchor_rows) != 165 or len(ledger_rows) != 165:
        failures.append("final/formal/anchor cardinality is not 165")
    if n_new != 0:
        failures.append(f"N_new expected 0, got {n_new}")
    if set(anchor_paths) != set(paths):
        failures.append("anchor map post-transform anchors differ from final formal headings")
    if duplicate_anchors or unresolved_anchors:
        failures.append("duplicate or unresolved final anchors remain")
    if article_links_none != 67:
        failures.append(f"article_links=none/insertion_target=none rows expected 67, got {article_links_none}")
    counts: JsonMap = {"final_cards": len(paths), "anchor_rows": len(anchor_rows), "ledger_formal_rows": len(ledger_rows), "n_new": n_new, "duplicate_anchors": duplicate_anchors, "unresolved_anchors": unresolved_anchors, "article_links_none": article_links_none}
    summary: JsonMap = {"command": "final-anchor-check", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": failures, "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in inputs], "output_path": None}
    return (0 if not failures else 1), summary


def final_anchor_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
