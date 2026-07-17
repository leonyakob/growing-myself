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
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]; PhaseInput: Callable[[str, str, str], PhaseInputValue]; ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[PhaseInputValue]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, "Json"], ReceiptSpecValue], None]; sha256_bytes: Callable[[bytes], str]
else:
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["PhaseInput", "ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    PhaseInput = receipt_module.PhaseInput; ReceiptOutput = receipt_module.ReceiptOutput; ReceiptSpec = receipt_module.ReceiptSpec; append_validator_receipt = receipt_module.append_validator_receipt; sha256_bytes = receipt_module.sha256_bytes

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
ARTICLE_DIRECTIONS: Final = ("人物线", "城乡主题", "尊严主题", "爱情线", "知识分子困境", "写法线索")
TRAJECTORY_CHAINS: Final = (
    "特权态度：从只写“痛恨特权”推进到“也痛恨自己没有特权”的挑战",
    "劳动与身份：从“高加林不愿掏炭”推进到真正差别在身份意义",
    "职业热爱：记者身份重新编码痛感，保留田晓霞联想但不混同",
    "县城空间：从忘本判断修正为空间里的身份落差投影",
    "爱情与位置：保留原始锋利表达，补足位置影响爱的证据桥",
    "黄亚萍物质付出：承认真成本，但不等同于巧珍匮乏中的托举",
)
REVIEWED_SHA256: Final = "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"
TECHNICAL_TOKEN_RE: Final = re.compile(r"源\s*ID|source\s*ID|former\s*ID|chapterUid|bookId|range=|raw_byte_span|line\s*\d+|\bR[1-4]:\d|\d+\s*-\s*\d+", flags=re.IGNORECASE)


@dataclass(frozen=True, slots=True)
class Cli:
    formal: Path
    technical: Path
    ledger: Path
    out: Path
    check_only: bool
    receipt: Path | None


@dataclass(frozen=True, slots=True)
class Card:
    key: str
    round_key: str
    line_no: int
    path: str


@dataclass(frozen=True, slots=True)
class Transform:
    line_no: int
    before: str
    after: str


@dataclass(frozen=True, slots=True)
class Row:
    cells: Mapping[str, str]

    def get(self, key: str) -> str:
        return self.cells.get(key, "").strip()


@dataclass(frozen=True, slots=True)
class AnchorRow:
    key: str
    round_key: str
    pre_path: str
    post_anchor: str
    article_links: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class AnchorModel:
    rows: tuple[AnchorRow, ...]
    n_new: int
    resolved_links: int
    insertion_targets: tuple[str, ...]


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


def technical_transforms(text: str) -> tuple[Transform, ...]:
    rows: list[Transform] = []
    for line in text.splitlines():
        parts = split_cells(line) if line.startswith("| ") else ()
        if len(parts) == 5 and parts[0].isdecimal():
            rows.append(Transform(int(parts[0]), parts[2], parts[3]))
    return tuple(rows)


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "anchor-check":
        return "usage: anchor-check is required"
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
    required = ("formal", "technical", "ledger", "out")
    if any(not isinstance(values.get(key), str) for key in required):
        return "--formal --technical --ledger and --out are required"
    receipt = values.get("receipt")
    return Cli(Path(str(values["formal"])), Path(str(values["technical"])), Path(str(values["ledger"])), Path(str(values["out"])), values["check-only"] is True, Path(receipt) if isinstance(receipt, str) else None)


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


def parse_cards(lines: Sequence[str]) -> tuple[Card, ...]:
    cards: list[Card] = []
    for index, line in enumerate(lines):
        round_key, _r4_h4 = is_card_heading(index + 1, line)
        if round_key:
            title = re.sub(r"^#{3,4}\s+", "", line)
            cards.append(Card(f"F{len(cards) + 1:03d}", round_key, index + 1, f"第{round_key[1]}轮 / {nearest_h2(lines, index)} / {title}"))
    return tuple(cards)


def transformed_lines(formal_text: str, transforms: Sequence[Transform], failures: list[str]) -> tuple[str, ...]:
    lines = formal_text.splitlines()
    if len(transforms) != 108:
        failures.append(f"technical transform count is not 108: {len(transforms)}")
    seen: set[int] = set()
    for item in transforms:
        if item.line_no in seen or item.line_no < 1 or item.line_no > len(lines):
            failures.append(f"technical transform line is invalid or duplicated: {item.line_no}")
            continue
        seen.add(item.line_no)
        if lines[item.line_no - 1] != item.before:
            failures.append(f"technical before text mismatch at line {item.line_no}")
            continue
        lines[item.line_no - 1] = item.after
    return tuple(lines)


def split_set(value: str) -> tuple[str, ...]:
    return () if value == "none" else tuple(part.strip() for part in value.split(";") if part.strip())


def article_links_by_formal_key(source_rows: Sequence[Row], failures: list[str]) -> tuple[dict[str, set[str]], int, tuple[str, ...]]:
    links: dict[str, set[str]] = {}
    resolved = 0
    insertion_targets: list[str] = []
    for row in source_rows:
        row_links = split_set(row.get("article_links"))
        bad = [link for link in row_links if link not in ARTICLE_DIRECTIONS]
        if bad:
            failures.append(f"{row.get('source_key')} invalid article link: {bad[0]}")
        formal_keys = split_set(row.get("formal_keys"))
        for formal_key in formal_keys:
            links.setdefault(formal_key, set()).update(row_links)
            if row_links:
                resolved += 1
        if row.get("workflow_state") == "planned-new-formal":
            if row.get("future_anchor") == "none" or row.get("insertion_hunk") == "none":
                failures.append(f"{row.get('source_key')} planned new formal row lacks fixed insertion target")
            else:
                insertion_targets.append(row.get("future_anchor"))
    return links, resolved, tuple(insertion_targets)


def build_model(formal_text: str, technical_text: str, ledger_text: str, failures: list[str]) -> AnchorModel:
    pre_cards = parse_cards(formal_text.splitlines())
    post_cards = parse_cards(transformed_lines(formal_text, technical_transforms(technical_text), failures))
    source_rows = table_rows(ledger_text, "source_key")
    formal_rows = table_rows(ledger_text, "formal_key")
    link_map, resolved_links, insertion_targets = article_links_by_formal_key(source_rows, failures)
    n_new = sum(1 for row in source_rows if row.get("workflow_state") == "planned-new-formal")
    if n_new:
        failures.append(f"planned-new-formal rows differ from accepted Todo 3 state: {n_new}")
    if len(pre_cards) != 165 or len(post_cards) != 165 or len(formal_rows) != 165:
        failures.append("formal card cardinality is not 165 before/after ledger coverage")
    formal_keys = {card.key for card in post_cards}
    if {row.get("formal_key") for row in formal_rows} != formal_keys:
        failures.append("ledger formal coverage differs from parsed formal cards")
    for key in link_map:
        if key not in formal_keys:
            failures.append(f"article link points to missing formal key: {key}")
    rows = tuple(AnchorRow(post.key, post.round_key, pre.path, post.path, tuple(sorted(link_map.get(post.key, set())))) for pre, post in zip(pre_cards, post_cards, strict=True))
    duplicates = len(rows) - len({row.post_anchor for row in rows})
    unresolved = sum(1 for row in rows if TECHNICAL_TOKEN_RE.search(row.post_anchor))
    if duplicates:
        failures.append(f"duplicate readable anchors remain: {duplicates}")
    if unresolved:
        failures.append(f"reader-facing anchors still contain technical tokens: {unresolved}")
    return AnchorModel(rows, n_new, resolved_links, insertion_targets)


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", "<br>")


def anchor_map_text(model: AnchorModel) -> str:
    lines = ["# Ren Sheng whole-book anchor map", "", f"Post-transform cards: {len(model.rows)}", f"N_new: {model.n_new}", "Duplicate readable anchors: none", "Unresolved anchors: none", "New-card insertion targets: none" if not model.insertion_targets else f"New-card insertion targets: {len(model.insertion_targets)}", "Article directions: 6", "Trajectory chains: 6", "", "## Existing formal-card anchors", "", "| formal_key | round | internal_pre_transform_path | post_transform_anchor | article_links | insertion_target |", "|---|---|---|---|---|---|"]
    lines.extend(f"| {row.key} | {row.round_key} | {escape_cell(row.pre_path)} | {escape_cell(row.post_anchor)} | {'; '.join(row.article_links) if row.article_links else 'none'} | none |" for row in model.rows)
    lines.extend(["", "## Appended-section blueprint", "", "Placement: after Round 4, after the existing four-round archive.", "", "```markdown", "## 全书收束整合", "### 一、阅读现场档案", "### 二、文章素材索引", "### 三、阅读轨迹与判断变化", "### 四、待回看 / 归档不迁移", "```", "", "## Article direction blueprint", "", "| article_direction | status |", "|---|---|"])
    lines.extend(f"| {direction} | fixed direction; anchors must resolve through post_transform_anchor |" for direction in ARTICLE_DIRECTIONS)
    lines.extend(["", "## Trajectory chain blueprint", "", "| trajectory_chain | required_fields |", "|---|---|"])
    lines.extend(f"| {escape_cell(chain)} | 当时的读法 / 后来出现的证据 / 全书后的修正 / 误读的价值 / 文章索引用法 |" for chain in TRAJECTORY_CHAINS)
    return "\n".join(lines) + "\n"


def summary_json(cli: Cli, model: AnchorModel, failures: Sequence[str]) -> JsonMap:
    counts: JsonMap = {"post_transform_cards": len(model.rows), "n_new": model.n_new, "duplicate_readable_anchors": len(model.rows) - len({row.post_anchor for row in model.rows}), "unresolved_anchors": sum(1 for row in model.rows if TECHNICAL_TOKEN_RE.search(row.post_anchor)), "resolved_article_links": model.resolved_links, "insertion_targets": len(model.insertion_targets), "article_directions": len(ARTICLE_DIRECTIONS), "trajectory_chains": len(TRAJECTORY_CHAINS)}
    inputs = (cli.formal, cli.technical, cli.ledger)
    return {"command": "anchor-check", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": list(failures), "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in inputs], "output_path": None if cli.check_only else str(cli.out)}


def validate(cli: Cli) -> tuple[int, JsonMap]:
    inputs = (cli.formal, cli.technical, cli.ledger)
    failures = [f"unreadable input: {path}" for path in inputs if not path.is_file()]
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if not cli.check_only and ((cli.out.exists() and not cli.out.is_file()) or not cli.out.parent.exists()):
        failures.append(f"invalid output path: {cli.out}")
    if failures:
        return 2, {"command": "anchor-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    formal_text = cli.formal.read_text(encoding="utf-8")
    if sha256_bytes(cli.formal.read_bytes()) != REVIEWED_SHA256:
        failures.append("formal input SHA-256 does not match reviewed baseline")
    model = build_model(formal_text, cli.technical.read_text(encoding="utf-8"), cli.ledger.read_text(encoding="utf-8"), failures)
    if len(model.rows) + model.n_new != 165 + model.n_new:
        failures.append("post-transform anchor cardinality differs from 165 + N_new")
    text = anchor_map_text(model)
    if not failures and not cli.check_only:
        _ = cli.out.write_text(text, encoding="utf-8")
    summary = summary_json(cli, model, failures)
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(5, "anchor-check", (ReceiptOutput("anchor_map", cli.out),), (PhaseInput("路遥/人生/《人生》阅读笔记.md", "reviewed-baseline", REVIEWED_SHA256),)))
    return (0 if not failures else 1), summary


def anchor_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
