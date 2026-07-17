from __future__ import annotations

import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, NamedTuple, TypeAlias

class ReceiptOutputValue(NamedTuple): name: str; path: Path | None


class PhaseInputValue(NamedTuple): path: str; phase: str; sha256: str


class ReceiptSpecValue(NamedTuple): todo: int; subcommand: str; outputs: Sequence[ReceiptOutputValue]; phases: Sequence[PhaseInputValue]


if TYPE_CHECKING:
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]; ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[PhaseInputValue]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, "Json"], ReceiptSpecValue], None]; sha256_bytes: Callable[[bytes], str]
else:
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    ReceiptOutput = receipt_module.ReceiptOutput; ReceiptSpec = receipt_module.ReceiptSpec; append_validator_receipt = receipt_module.append_validator_receipt; sha256_bytes = receipt_module.sha256_bytes

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
ARTICLE_DIRECTIONS: Final = ("人物线", "城乡主题", "尊严主题", "爱情线", "知识分子困境", "写法线索")
TRAJECTORY_HEADINGS: Final = (
    "特权态度：从只写“痛恨特权”推进到“也痛恨自己没有特权”的挑战",
    "劳动与身份：从“高加林不愿掏炭”推进到他能承受新闻现场之苦、真正差别在身份意义",
    "职业热爱：从“热爱让苦甘之如饴”收稳为记者身份重新编码痛感，并保留田晓霞联想但不混同两人",
    "县城空间：从“县城变小等于忘本”修正为身份落差投向空间的心理投影，不把后来的失败倒灌进当时场景",
    "爱情与位置：保留“农民时爱巧珍、干部时爱黄亚萍”的原始锋利表达，同时补足“位置影响哪一种爱被承认”的证据桥",
    "黄亚萍物质付出：从“这不是牺牲”修正为“有真实成本，但不等同于巧珍在匮乏中的托举”",
)
ARTICLE_FIELDS: Final = ("核心问题", "可回链锚点", "保留的用户原句", "文本张力", "可用文本证据", "目前缺口")
TRAJECTORY_FIELDS: Final = ("当时的读法", "后来出现的证据", "全书后的修正", "误读的价值", "文章索引用法")
PART_HEADERS: Final = ("## Part A. All 108 replacement rows", "## Part B. Ledger-approved repair/new-card fragments", "## Part C. Complete target-bound `## 全书收束整合`")
SECTION_HEADERS: Final = ("### 一、阅读现场档案", "### 二、文章素材索引", "### 三、阅读轨迹与判断变化", "### 四、待回看 / 归档不迁移")
TECHNICAL_TOKEN_RE: Final = re.compile(r"external-源ID(?:s)?|源ID(?:s)?|源\s+ID(?:s)?|chapterUid|bookId|\brange\b|(?<!\d)\d+\s*-\s*\d+(?!\d)")
CARD_BODY_RE: Final = re.compile(r"(?m)^>\s|^\*\*【划线原文】\*\*|^\*\*【我自己写的内容】\*\*|^\*\*【我的原想法】\*\*|^\*\*【AI评价】\*\*|^\*\*【AI修正】\*\*|^\*\*【AI补充】\*\*")
ANCHOR_RE: Final = re.compile(r"`([^`]+)`")


@dataclass(frozen=True, slots=True)
class Cli:
    candidate: Path
    ledger: Path
    technical: Path
    anchor_map: Path
    check_only: bool
    receipt: Path | None


@dataclass(frozen=True, slots=True)
class Row:
    cells: Mapping[str, str]

    def get(self, key: str) -> str:
        return self.cells.get(key, "").strip()


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


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "candidate-structure":
        return "usage: candidate-structure is required"
    values: dict[str, str | bool] = {"check-only": False}
    tokens = list(argv[1:])
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == "--check-only":
            values["check-only"] = True; index += 1
        elif token.startswith("--") and index + 1 < len(tokens):
            values[token.removeprefix("--")] = tokens[index + 1]; index += 2
        else:
            return f"invalid invocation token: {token}"
    required = ("candidate", "ledger", "technical", "anchor-map")
    if any(not isinstance(values.get(key), str) for key in required):
        return "--candidate --ledger --technical and --anchor-map are required"
    receipt = values.get("receipt")
    return Cli(Path(str(values["candidate"])), Path(str(values["ledger"])), Path(str(values["technical"])), Path(str(values["anchor-map"])), values["check-only"] is True, Path(receipt) if isinstance(receipt, str) else None)


def part_texts(text: str, failures: list[str]) -> tuple[str, str, str]:
    positions = [text.find(header) for header in PART_HEADERS]
    if [text.count(header) for header in PART_HEADERS] != [1, 1, 1]:
        failures.append("candidate parts must appear exactly once")
    if any(position < 0 for position in positions) or positions != sorted(positions):
        failures.append("candidate parts are missing or out of order")
        return "", "", ""
    starts = [position + len(header) for position, header in zip(positions, PART_HEADERS, strict=True)]
    return text[starts[0]:positions[1]].strip(), text[starts[1]:positions[2]].strip(), text[starts[2]:].strip()


def part_a_ok(part_a: str, technical_text: str, failures: list[str]) -> int:
    candidate_rows = table_rows(part_a, "line")
    technical_rows = table_rows(technical_text, "line")
    if len(candidate_rows) != 108:
        failures.append(f"part A row count is not 108: {len(candidate_rows)}")
    by_line = {row.get("line"): row for row in technical_rows}
    for row in candidate_rows:
        current = by_line.get(row.get("line"))
        if current is None:
            failures.append(f"part A unexpected line: {row.get('line')}")
            continue
        for left, right in (("families", "families"), ("internal-before", "before"), ("target-after", "after")):
            if row.get(left) != current.get(right):
                failures.append(f"part A mismatch for line {row.get('line')} field {left}")
        token = TECHNICAL_TOKEN_RE.search(row.get("target-after"))
        if token is not None:
            failures.append(f"target-bound technical token in part A target-after line {row.get('line')}: {token.group(0)}")
    return len(candidate_rows)


def part_b_ok(part_b: str, ledger_text: str, failures: list[str]) -> int:
    approved = sum(1 for row in table_rows(ledger_text, "source_key") if any(row.get(field) != "none" for field in ("repair_hunk", "insertion_hunk", "future_anchor")))
    if approved == 0 and part_b != "none":
        failures.append("part B must be none when no ledger-approved repair/new-card fragment exists")
    if approved and part_b == "none":
        failures.append("part B cannot be none when ledger-approved fragments exist")
    if approved and ("internal-before" not in part_b or "target-after" not in part_b):
        failures.append("part B fragment blocks must expose internal-before and target-after fields")
    return approved


def section_map(part_c: str, failures: list[str]) -> dict[str, str]:
    if part_c.count("## 全书收束整合") != 1:
        failures.append("part C must contain exactly one whole-book heading")
    positions = [part_c.find(header) for header in SECTION_HEADERS]
    if [part_c.count(header) for header in SECTION_HEADERS] != [1, 1, 1, 1] or any(position < 0 for position in positions) or positions != sorted(positions):
        failures.append("part C direct children are missing or out of order")
        return {}
    starts = [position + len(header) for position, header in zip(positions, SECTION_HEADERS, strict=True)]
    return {header: (part_c[starts[index]:positions[index + 1]].strip() if index < 3 else part_c[starts[index]:].strip()) for index, header in enumerate(SECTION_HEADERS)}


def heading_blocks(text: str) -> tuple[tuple[str, str], ...]:
    lines = text.splitlines()
    indexes = [index for index, line in enumerate(lines) if line.startswith("#### ")]
    return tuple((lines[index][5:], "\n".join(lines[index + 1:indexes[offset + 1] if offset + 1 < len(indexes) else len(lines)]).strip()) for offset, index in enumerate(indexes))


def backticked_anchors(text: str) -> tuple[str, ...]:
    return tuple(match.group(1) for match in ANCHOR_RE.finditer(text))


def article_rows_ok(text: str, failures: list[str]) -> tuple[int, int]:
    blocks = heading_blocks(text)
    headings = tuple(heading for heading, _body in blocks)
    if headings != ARTICLE_DIRECTIONS:
        failures.append("article directions must match the fixed six headings")
    anchor_refs = 0
    for heading, body in blocks:
        for field in ARTICLE_FIELDS:
            if f"- {field}：" not in body:
                failures.append(f"article row missing field {field}: {heading}")
        anchors = tuple(dict.fromkeys(anchor for anchor in backticked_anchors(body) if anchor.startswith("第")))
        rounds = {anchor.split(" / ", 1)[0] for anchor in anchors}
        if len(anchors) < 3 or len(rounds) < 2:
            failures.append(f"article row lacks >=3 unique anchors from >=2 rounds: {heading}")
        anchor_refs += len(anchors)
    return len(blocks), anchor_refs


def trajectory_rows_ok(text: str, failures: list[str]) -> int:
    blocks = heading_blocks(text)
    if tuple(heading for heading, _body in blocks) != TRAJECTORY_HEADINGS:
        failures.append("trajectory headings must match the fixed six chains")
    for heading, body in blocks:
        for field in TRAJECTORY_FIELDS:
            if f"- {field}：" not in body:
                failures.append(f"trajectory row missing field {field}: {heading}")
    return len(blocks)


def anchor_counts(anchor_text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in table_rows(anchor_text, "formal_key"):
        key = row.get("post_transform_anchor")
        counts[key] = counts.get(key, 0) + 1
    return counts


def part_c_ok(part_c: str, anchor_text: str, failures: list[str]) -> tuple[int, int, int]:
    token = TECHNICAL_TOKEN_RE.search(part_c)
    if token is not None:
        failures.append(f"target-bound technical token in part C: {token.group(0)}")
    if CARD_BODY_RE.search(part_c):
        failures.append("part C contains copied card-body markers or quote blocks")
    sections = section_map(part_c, failures)
    if not sections:
        return 0, 0, 0
    article_rows, _article_anchor_refs = article_rows_ok(sections[SECTION_HEADERS[1]], failures)
    trajectory_rows = trajectory_rows_ok(sections[SECTION_HEADERS[2]], failures)
    counts = anchor_counts(anchor_text)
    part_c_anchors = tuple(anchor for anchor in backticked_anchors(part_c) if anchor.startswith("第"))
    for anchor in part_c_anchors:
        if counts.get(anchor) != 1:
            failures.append(f"readable anchor does not resolve exactly once: {anchor}")
    return article_rows, trajectory_rows, len(part_c_anchors)


def summary_json(cli: Cli, failures: Sequence[str], part_a_rows: int, part_b_fragments: int, article_rows: int, trajectory_rows: int, anchor_refs: int) -> JsonMap:
    counts: JsonMap = {"part_a_rows": part_a_rows, "part_b_fragments": part_b_fragments, "article_rows": article_rows, "trajectory_rows": trajectory_rows, "resolved_anchor_refs": anchor_refs}
    inputs = (cli.candidate, cli.ledger, cli.technical, cli.anchor_map)
    return {"command": "candidate-structure", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": list(failures), "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in inputs], "output_path": None if cli.check_only else {"candidate": str(cli.candidate)}}


def validate(cli: Cli) -> tuple[int, JsonMap]:
    inputs = (cli.candidate, cli.ledger, cli.technical, cli.anchor_map)
    failures = [f"unreadable input: {path}" for path in inputs if not path.is_file()]
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if cli.receipt is not None and not cli.receipt.parent.exists():
        failures.append(f"invalid receipt path: {cli.receipt}")
    if failures:
        return 2, {"command": "candidate-structure", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    part_a, part_b, part_c = part_texts(cli.candidate.read_text(encoding="utf-8"), failures)
    part_a_rows = part_a_ok(part_a, cli.technical.read_text(encoding="utf-8"), failures)
    part_b_fragments = part_b_ok(part_b, cli.ledger.read_text(encoding="utf-8"), failures)
    article_rows, trajectory_rows, anchor_refs = part_c_ok(part_c, cli.anchor_map.read_text(encoding="utf-8"), failures)
    summary = summary_json(cli, failures, part_a_rows, part_b_fragments, article_rows, trajectory_rows, anchor_refs)
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(6, "candidate-structure", (ReceiptOutput("candidate", cli.candidate),), ()))
    return (0 if not failures else 1), summary


def candidate_structure_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
