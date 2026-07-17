from __future__ import annotations

import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]

if TYPE_CHECKING:
    ReceiptOutput: Callable[[str, Path | None], Json]
    ReceiptSpec: Callable[[int, str, Sequence[Json], Sequence[Json]], Json]
    append_validator_receipt: Callable[[Path, Mapping[str, Json], Json], None]
    sha256_bytes: Callable[[bytes], str]
else:
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    ReceiptOutput = receipt_module.ReceiptOutput
    ReceiptSpec = receipt_module.ReceiptSpec
    append_validator_receipt = receipt_module.append_validator_receipt
    sha256_bytes = receipt_module.sha256_bytes

ACCEPTED_LEDGER_SHA256: Final = "10c7dde8f7792d9cb8f88abf9be6a526382267095e0c24f89f8814bddd957ee8"
CASE_COLUMNS: Final = ("case", "input_identity", "expected_source_status", "expected_archive_treatment", "expected_formal_note_treatment", "expected_article_index_treatment", "actual_decision", "evidence_anchor_or_policy_only", "forbidden_outcome", "verdict")
SENTINEL_COLUMNS: Final = ("sentinel", "location", "before_state_quotation", "future_readable_anchor", "expected_outcome", "actual_outcome", "forbidden_outcome", "verdict")


@dataclass(frozen=True, slots=True)
class Cli:
    fixture: Path
    results: Path
    ledger: Path
    formal_manifest: Path
    check_only: bool
    receipt: Path | None


@dataclass(frozen=True, slots=True)
class Row:
    cells: Mapping[str, str]

    def get(self, key: str) -> str:
        return self.cells.get(key, "").strip()


@dataclass(frozen=True, slots=True)
class FixtureCase:
    case: str
    title: str
    source_status: tuple[str, ...]
    archive_treatment: tuple[str, ...]
    formal_treatment: tuple[str, ...]
    index_treatment: tuple[str, ...]
    forbidden_failure: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class SentinelSpec:
    location: str
    before_quote: str
    anchor: str


SENTINELS: Final[Mapping[str, SentinelSpec]] = {
    "S1-space-reference-shift": SentinelSpec("formal line 2098", "他下了公共汽车，出了车站，猛一下觉得县城变化很大，变得让人感到很陌生。城郭是这么小！街道是这么短窄！好像经过了一番不幸的大变迁，人稀稀拉拉，四处静悄悄的，似乎没有什么声响。", "县城变小、陌生：见过更大世界后的空间失衡"),
    "S2-ethical-dialogue-contrast": SentinelSpec("formal line 2139", "现在让我们结束这个不幸的局面吧！你和亚萍仍然恢复你们的一切。我现在唯一要求你的，就是你能谅解我以前给你带来的痛苦……”“不！”克南也站起来，“尽管我爱亚萍，亚萍实际上是爱你的！我的痛苦已经过去了，一切我也都想通了……亚萍也不会离开你……”“我要离开她！我要主动和她断绝关系！这我已经决定了！”“她是爱你的……”“我真正爱的人实际上是另外一个！”高加林大声说。张克南惊讶地望着他，半天说不出话来了。", "克南的直线伦理与高加林的斜坡伦理"),
    "S3-relationship-chain-activation": SentinelSpec("formal line 2367", "占胜一条胳膊亲热地搂着加林的肩头，对他说：“旁的事我先不和你拉搭；我先只对你说一句话，你的工作我们会很快妥善解决的……”", "马占胜搂肩承诺工作：关系链如何让办事速度突然激活"),
    "S4-dignified-labor-drop": SentinelSpec("formal line 2446", "加林恐怕不愿去掏炭！", "“加林恐怕不愿去掏炭”：体面劳动与身份回落"),
    "S5-recognized-future-hardship": SentinelSpec("formal line 2661", "嗓门眼渴得像要烧着火，他就随便伏在路边的水坑里喝上几口。脚不知什么时候碰破了，连骨头都感到生疼。但所有这一切反而增加了他的愉快心情——这绝不是夸大的说法！真的，高加林此刻感到他真正像个新闻记者了", "喝路边水坑、脚流血：高加林肯为被认可的前途吃苦"),
    "S6-good-cadre-contrast": SentinelSpec("formal line 4795", "公社书记刘玉海浑身负了七处伤，都用纱布缠着，简直就像刚从打仗的火线上下来一般。", "刘玉海 / 好干部群像补证"),
    "S7-material-gift-relation": SentinelSpec("formal line 5010", "在物质方面，她对他更是非常豁达的。她的工资几乎全花在了他身上；给他买了春夏秋冬各式各样的时兴服装，还托人在北京买了一双三接头皮鞋（他还没敢穿）。平时，罐头、糕点、高级牛奶糖、咖啡、可可粉、麦乳精，不断头地给他送来—这些东西连县委书记恐怕也不常吃。她还把自己进口带日历全自动手表给了他；她自己却戴他的上海牌表。这些方面，亚萍是完全可以做出牺牲的……", "黄亚萍物质馈赠：有情意、有成本、不等同匮乏中托举"),
}


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


def fixture_cases(text: str) -> tuple[FixtureCase, ...]:
    cases: list[FixtureCase] = []
    chunks = re.split(r"(?m)^## Case ", text)[1:]
    for chunk in chunks:
        header, body = chunk.split("\n", 1)
        number, title = header.split(", ", 1)
        fields: dict[str, list[str]] = {name: [] for name in ("source status", "archive treatment", "formal-note treatment", "article-index treatment", "forbidden failure")}
        current = ""
        for line in body.splitlines():
            if line.startswith("### "):
                current = line.removeprefix("### ").strip()
            elif current in fields and line.startswith("- "):
                fields[current].append(line.removeprefix("- ").strip())
        cases.append(FixtureCase(f"Case {number}", title.strip(), tuple(fields["source status"]), tuple(fields["archive treatment"]), tuple(fields["formal-note treatment"]), tuple(fields["article-index treatment"]), tuple(fields["forbidden failure"])))
    return tuple(cases)


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "policy-check":
        return "usage: policy-check is required"
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
    required = ("fixture", "results", "ledger", "formal-manifest")
    if any(not isinstance(values.get(key), str) for key in required):
        return "--fixture --results --ledger and --formal-manifest are required"
    receipt = values.get("receipt")
    return Cli(Path(str(values["fixture"])), Path(str(values["results"])), Path(str(values["ledger"])), Path(str(values["formal-manifest"])), values["check-only"] is True, Path(receipt) if isinstance(receipt, str) else None)


def require_columns(rows: Sequence[Row], columns: Sequence[str], label: str, failures: list[str]) -> None:
    for row in rows:
        missing = [column for column in columns if row.get(column) == ""]
        if missing:
            failures.append(f"{label} missing required fields: {', '.join(missing)}")


def policy_contains(cell: str, expected: str) -> bool:
    return expected in cell or expected.rstrip("。.") in cell


def validate_cases(cases: Sequence[FixtureCase], rows: Sequence[Row], failures: list[str]) -> None:
    row_by_case = {row.get("case"): row for row in rows}
    expected = {case.case for case in cases}
    if set(row_by_case) != expected or len(rows) != 9:
        failures.append(f"fixture case coverage mismatch: expected {sorted(expected)}, got {sorted(row_by_case)}")
    for case in cases:
        row = row_by_case.get(case.case)
        if row is None:
            continue
        checks = ((case.source_status, "expected_source_status"), (case.archive_treatment, "expected_archive_treatment"), (case.formal_treatment, "expected_formal_note_treatment"), (case.index_treatment, "expected_article_index_treatment"), (case.forbidden_failure, "forbidden_outcome"))
        if case.title not in row.get("input_identity") or row.get("verdict") != "PASS" or row.get("forbidden_outcome") == "none":
            failures.append(f"{case.case} missing identity, forbidden outcome or PASS verdict")
        for expected_parts, field in checks:
            absent = [part for part in expected_parts if not policy_contains(row.get(field), part)]
            if absent:
                failures.append(f"{case.case} does not record fixture field {field}: {absent[0]}")
        if "policy-only" in row.get("evidence_anchor_or_policy_only") and not ("no fabricated formal content" in row.get("actual_decision") or "不新增正式内容" in row.get("actual_decision")):
            failures.append(f"{case.case} policy-only row can fabricate formal content")
    case7 = row_by_case.get("Case 7")
    if case7 is None:
        failures.append("Case 7 external-only policy row is missing")
    elif "external_reader_relation=独立精彩" not in case7.get("actual_decision") or "policy-only" not in case7.get("evidence_anchor_or_policy_only") or "不进入“阅读现场档案”" not in case7.get("expected_formal_note_treatment") or "主证据" in case7.get("actual_decision"):
        failures.append("Case 7 external-only material became main user evidence or fabricated formal content")


def validate_sentinels(rows: Sequence[Row], failures: list[str]) -> None:
    row_by_name = {row.get("sentinel"): row for row in rows}
    if set(row_by_name) != set(SENTINELS) or len(rows) != 7:
        failures.append(f"sentinel coverage mismatch: expected {sorted(SENTINELS)}, got {sorted(row_by_name)}")
    for name, spec in SENTINELS.items():
        row = row_by_name.get(name)
        if row is None:
            continue
        if row.get("location") != spec.location or row.get("before_state_quotation") != spec.before_quote or row.get("future_readable_anchor") != spec.anchor or row.get("verdict") != "PASS":
            failures.append(f"{name} sentinel fields do not match fixed regression policy")
        if row.get("forbidden_outcome") == "" or row.get("expected_outcome") == "" or row.get("actual_outcome") == "":
            failures.append(f"{name} sentinel missing expected/actual/forbidden outcome")
        if re.search(r"源ID|source\s*ID|range|R[1-4]:\d|\d+\s*-\s*\d+", row.get("future_readable_anchor"), flags=re.IGNORECASE):
            failures.append(f"{name} uses a technical future anchor")


def validate(cli: Cli) -> tuple[int, JsonMap]:
    inputs = (cli.fixture, cli.results, cli.ledger, cli.formal_manifest)
    failures = [f"unreadable input: {path}" for path in inputs if not path.is_file()]
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if failures:
        return 2, {"command": "policy-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    fixture_text = cli.fixture.read_text(encoding="utf-8")
    results_text = cli.results.read_text(encoding="utf-8")
    ledger_hash = sha256_bytes(cli.ledger.read_bytes())
    if ledger_hash != ACCEPTED_LEDGER_SHA256:
        failures.append("ledger hash differs from accepted Todo 3 state")
    cases = fixture_cases(fixture_text)
    case_rows = table_rows(results_text, "case")
    sentinel_rows = table_rows(results_text, "sentinel")
    formal_rows = table_rows(cli.formal_manifest.read_text(encoding="utf-8"), "formal_key")
    if len(cases) != 9 or len(formal_rows) != 165:
        failures.append("fixture or formal manifest count mismatch")
    require_columns(case_rows, CASE_COLUMNS, "fixture row", failures)
    require_columns(sentinel_rows, SENTINEL_COLUMNS, "sentinel row", failures)
    validate_cases(cases, case_rows, failures)
    validate_sentinels(sentinel_rows, failures)
    counts: JsonMap = {"fixture_rows": len(case_rows), "sentinel_rows": len(sentinel_rows)}
    summary: JsonMap = {"command": "policy-check", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": failures, "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in inputs], "output_path": None if cli.check_only else str(cli.results)}
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(4, "policy-check", (ReceiptOutput("fixture_results", cli.results),), ()))
    return (0 if not failures else 1), summary


def policy_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
