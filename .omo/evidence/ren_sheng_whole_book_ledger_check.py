from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, NamedTuple, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]


class ReceiptOutputValue(NamedTuple): name: str; path: Path | None


class ReceiptSpecValue(NamedTuple): todo: int; subcommand: str; outputs: Sequence[ReceiptOutputValue]; phases: Sequence[Json]


if TYPE_CHECKING:
    decode_json_map: Callable[[str, str], JsonMap]
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]
    ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[Json]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, Json], ReceiptSpecValue], None]
    sha256_bytes: Callable[[bytes], str]
else:
    json_tools = __import__("ren_sheng_json_tools", fromlist=["decode_json_map"])
    decode_json_map = json_tools.decode_json_map
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    ReceiptOutput = receipt_module.ReceiptOutput
    ReceiptSpec = receipt_module.ReceiptSpec
    append_validator_receipt = receipt_module.append_validator_receipt
    sha256_bytes = receipt_module.sha256_bytes

SET_NAMES: Final = ("source-only", "formal-only", "one-to-one", "many-to-one", "duplicate", "revision-chain", "planned-new-formal", "unresolved")
SOURCE_STATUSES: Final = frozenset(("已在正式笔记中，结构合格，只补文章索引", "已在正式笔记中，但需补 readable evidence / 用户原句 / 外部原话", "中间稿已优化，尚未迁移", "中间稿与正式稿重复，需合并或建立修订链", "正式稿旧判断已被后文修正，保留为阅读轨迹", "仅外部读者材料，无用户卡片锚点", "来源不足，待回看"))
ARCHIVE_DISPOSITIONS: Final = frozenset(("保留为轻卡", "保留为完整卡", "提升为核心卡", "合并入其他卡", "归档不迁移", "待回看"))
EVIDENCE_ROLES: Final = frozenset(("主题证据", "人物线证据", "写法证据", "阅读轨迹证据"))
ARTICLE_LINKS: Final = frozenset(("人物线", "城乡主题", "尊严主题", "爱情线", "知识分子困境", "写法线索"))
TRAJECTORY_FLAGS: Final = frozenset(("早期误读", "后文修正", "判断变化"))
EXTERNAL_RELATIONS: Final = frozenset(("回声", "补充", "挑战", "反向解释", "独立精彩", "丢弃并说明理由", "无外部材料", "不适用"))
SOURCE_RELATIONS: Final = frozenset(("exact same quote", "overlapping quote", "same scene", "different quote", "not-applicable"))
INTERPRETATION_RELATIONS: Final = frozenset(("same insight", "corrected judgment", "different angle", "external echo", "external challenge", "no-comparable-judgment", "not-applicable"))
WORKFLOWS: Final = frozenset(("mapped-complete", "mapped-partial", "planned-new-formal", "intentionally-unmapped", "unresolved"))
TARGET_RELATIONS: Final = frozenset(("present-verbatim", "present-labelled-context", "intentionally-not-migrated", "missing-repair-approved", "planned-by-approved-insertion", "missing-unbound", "not-applicable"))
ACTIONS: Final = frozenset(("preserve-existing", "local-evidence-repair", "index-only", "merge-to-anchor", "new-card", "internal-only", "待回看", "归档不迁移", "stop-unresolved"))
PRIMARY_BUCKETS: Final = frozenset(("source-only", "one-to-one", "many-to-one"))
LEDGER_COLUMNS: Final = ("source_key", "raw_byte_span", "raw_sha256", "normalized_sha256", "quote_blocks", "user_blocks", "external_blocks", "current_target_anchor", "formal_keys", "source_status", "archive_disposition", "evidence_role", "article_links", "trajectory_flags", "external_reader_relation", "source_relation", "interpretation_relation", "workflow_state", "topology_relation", "target_quote_relation", "target_user_relation", "target_external_relation", "modeled_quote_relation", "modeled_user_relation", "modeled_external_relation", "missing_fields", "repair_hunk", "future_anchor", "insertion_hunk", "rationale", "action", "primary_bucket")
FORMAL_COLUMNS: Final = ("formal_key", "coverage", "source_keys", "rationale", "action")


@dataclass(frozen=True, slots=True)
class Row:
    cells: Mapping[str, str]

    def get(self, key: str) -> str:
        return self.cells.get(key, "").strip()


@dataclass(frozen=True, slots=True)
class Cli:
    source_manifest: Path
    formal_manifest: Path
    ledger: Path
    reconciliation: Path
    fixture: Path
    check_only: bool
    receipt: Path | None


def cells(line: str) -> tuple[str, ...]:
    return tuple(cell.strip() for cell in line.strip().strip("|").split("|"))


def table_rows(text: str, first_column: str) -> tuple[Row, ...]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| {first_column} "):
            header = cells(line)
            rows: list[Row] = []
            for raw in lines[index + 2:]:
                if not raw.startswith("|"):
                    break
                values = cells(raw)
                rows.append(Row(dict(zip(header, values, strict=True))))
            return tuple(rows)
    return ()


def split_set(value: str) -> tuple[str, ...]:
    return () if value == "none" else tuple(part.strip() for part in value.split(";") if part.strip())


def parse_int(value: str, label: str, failures: list[str]) -> int:
    if value.isdecimal():
        return int(value)
    failures.append(f"{label} is not an integer: {value}")
    return 0


def topology_ok(value: str, source_keys: set[str]) -> bool:
    if value in {"one-to-one", "many-to-one", "no-formal-target", "unresolved"}:
        return True
    return any(value.startswith(f"{prefix}:") and value.split(":", 1)[1] in source_keys for prefix in ("duplicate-of", "variant-of", "revision-before", "revision-after"))


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "ledger-check":
        return "usage: ledger-check is required"
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
    required = ("source-manifest", "formal-manifest", "ledger", "reconciliation", "fixture")
    if any(not isinstance(values.get(key), str) for key in required):
        return "--source-manifest --formal-manifest --ledger --reconciliation and --fixture are required"
    receipt_value = values.get("receipt")
    return Cli(
        source_manifest=Path(str(values["source-manifest"])),
        formal_manifest=Path(str(values["formal-manifest"])),
        ledger=Path(str(values["ledger"])),
        reconciliation=Path(str(values["reconciliation"])),
        fixture=Path(str(values["fixture"])),
        check_only=values["check-only"] is True,
        receipt=Path(receipt_value) if isinstance(receipt_value, str) else None,
    )


def validate_sets(row: Row, failures: list[str]) -> None:
    for field, domain in (("evidence_role", EVIDENCE_ROLES), ("article_links", ARTICLE_LINKS), ("trajectory_flags", TRAJECTORY_FLAGS)):
        values = split_set(row.get(field))
        bad = [value for value in values if value not in domain]
        if row.get(field) == "" or bad:
            failures.append(f"{row.get('source_key')} invalid {field}: {row.get(field)}")


def validate_row(row: Row, source_keys: set[str], failures: list[str]) -> None:
    key = row.get("source_key")
    required_domains = (("source_status", SOURCE_STATUSES), ("archive_disposition", ARCHIVE_DISPOSITIONS), ("external_reader_relation", EXTERNAL_RELATIONS), ("source_relation", SOURCE_RELATIONS), ("interpretation_relation", INTERPRETATION_RELATIONS), ("workflow_state", WORKFLOWS), ("action", ACTIONS), ("primary_bucket", PRIMARY_BUCKETS))
    for field, domain in required_domains:
        value = row.get(field)
        if value not in domain:
            failures.append(f"{key} invalid {field}: {value}")
    if not topology_ok(row.get("topology_relation"), source_keys):
        failures.append(f"{key} invalid topology_relation: {row.get('topology_relation')}")
    for field in ("target_quote_relation", "target_user_relation", "target_external_relation", "modeled_quote_relation", "modeled_user_relation", "modeled_external_relation"):
        value = row.get(field)
        if value not in TARGET_RELATIONS or value == "missing-unbound":
            failures.append(f"{key} invalid {field}: {value}")
    validate_sets(row, failures)
    if row.get("external_reader_relation") == "丢弃并说明理由" and row.get("rationale") == "none":
        failures.append(f"{key} discarded external material lacks rationale")


def validate_workflow(row: Row, failures: list[str]) -> None:
    key = row.get("source_key")
    current = row.get("current_target_anchor")
    missing = row.get("missing_fields")
    action = row.get("action")
    workflow = row.get("workflow_state")
    current_relations = (row.get("target_quote_relation"), row.get("target_user_relation"), row.get("target_external_relation"))
    modeled_relations = (row.get("modeled_quote_relation"), row.get("modeled_user_relation"), row.get("modeled_external_relation"))
    if workflow == "mapped-complete" and (current == "target-absent" or missing != "none" or action not in {"preserve-existing", "index-only", "merge-to-anchor"} or any(value in {"missing-repair-approved", "planned-by-approved-insertion"} for value in (*current_relations, *modeled_relations))):
        failures.append(f"{key} illegal mapped-complete combination")
    if workflow == "mapped-partial" and (current == "target-absent" or missing == "none" or row.get("repair_hunk") == "none" or action not in {"local-evidence-repair", "merge-to-anchor"} or "missing-repair-approved" not in current_relations):
        failures.append(f"{key} illegal mapped-partial combination")
    if workflow == "planned-new-formal" and (current != "target-absent" or row.get("topology_relation") != "no-formal-target" or action != "new-card" or row.get("future_anchor") == "none" or row.get("insertion_hunk") == "none" or row.get("evidence_role") == "none"):
        failures.append(f"{key} illegal planned-new-formal combination")
    if workflow == "intentionally-unmapped" and (current != "target-absent" or row.get("rationale") == "none" or action not in {"internal-only", "待回看", "归档不迁移"}):
        failures.append(f"{key} illegal intentionally-unmapped combination")
    if workflow == "unresolved" or row.get("topology_relation") == "unresolved" or action == "stop-unresolved":
        failures.append(f"{key} unresolved row is forbidden")


def validate_special_relations(rows: Sequence[Row], row_by_key: Mapping[str, Row], failures: list[str]) -> None:
    for row in rows:
        key = row.get("source_key")
        topology = row.get("topology_relation")
        if topology.startswith("duplicate-of:") and (row.get("source_relation") != "exact same quote" or row.get("interpretation_relation") != "same insight" or row.get("action") != "merge-to-anchor"):
            failures.append(f"{key} duplicate row lacks exact/same/merge contract")
        if topology.startswith("revision-before:"):
            target = row_by_key.get(topology.split(":", 1)[1])
            if target is None or target.get("topology_relation") != f"revision-after:{key}":
                failures.append(f"{key} revision-before lacks paired revision-after")
        if row.get("source_status") == "仅外部读者材料，无用户卡片锚点" and (row.get("external_reader_relation") not in {"独立精彩", "丢弃并说明理由"} or row.get("evidence_role") != "none"):
            failures.append(f"{key} external-only row became main evidence")


def report_json(text: str, failures: list[str]) -> JsonMap:
    marker = "```json"
    start = text.find(marker)
    end = text.find("```", start + len(marker)) if start >= 0 else -1
    if start < 0 or end < 0:
        failures.append("reconciliation missing fenced JSON block")
        return {}
    return decode_json_map(text[start + len(marker):end], "reconciliation")


def validate_report(report: JsonMap, rows: Sequence[Row], formal_rows: Sequence[Row], failures: list[str]) -> JsonMap:
    sets_value = report.get("sets")
    if not isinstance(sets_value, dict) or sorted(sets_value) != sorted(SET_NAMES):
        failures.append("reconciliation must emit exactly the eight named sets")
        return {}
    derived: dict[str, set[str]] = {name: set() for name in SET_NAMES}
    for row in rows:
        derived[row.get("primary_bucket")].add(row.get("source_key"))
        topology = row.get("topology_relation")
        if topology.startswith("duplicate-of:"):
            derived["duplicate"].add(row.get("source_key"))
        if topology.startswith("revision-before:") or topology.startswith("revision-after:"):
            derived["revision-chain"].add(row.get("source_key"))
        if row.get("workflow_state") == "planned-new-formal":
            derived["planned-new-formal"].add(row.get("source_key"))
    derived["formal-only"] = {row.get("formal_key") for row in formal_rows if row.get("coverage") == "formal-only"}
    for name, expected in derived.items():
        actual = sets_value.get(name)
        if not isinstance(actual, list) or set(str(item) for item in actual) != expected:
            failures.append(f"reconciliation set mismatch: {name}")
    primary = [derived[name] for name in ("source-only", "formal-only", "one-to-one", "many-to-one")]
    primary_union: set[str] = set()
    for group in primary:
        primary_union.update(group)
    if sum(len(group) for group in primary) != len(primary_union):
        failures.append("primary topology buckets are not mutually exclusive")
    if derived["unresolved"] or report.get("unresolved") != [] or report.get("n_new") != len(derived["planned-new-formal"]):
        failures.append("unresolved or N_new proof failed")
    return {name: len(derived[name]) for name in SET_NAMES}


def validate(cli: Cli) -> tuple[int, JsonMap]:
    failures = [f"unreadable input: {path}" for path in (cli.source_manifest, cli.formal_manifest, cli.ledger, cli.reconciliation, cli.fixture) if not path.is_file()]
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if failures:
        return 2, {"command": "ledger-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    source_text = cli.source_manifest.read_text(encoding="utf-8")
    formal_text = cli.formal_manifest.read_text(encoding="utf-8")
    ledger_text = cli.ledger.read_text(encoding="utf-8")
    report_text = cli.reconciliation.read_text(encoding="utf-8")
    source_rows = table_rows(source_text, "source_key")
    formal_manifest_rows = table_rows(formal_text, "formal_key")
    ledger_rows = table_rows(ledger_text, "source_key")
    formal_rows = table_rows(ledger_text, "formal_key")
    source_keys = {row.get("source_key") for row in source_rows}
    row_by_key = {row.get("source_key"): row for row in ledger_rows}
    if len(source_rows) != 266 or len(formal_manifest_rows) != 165 or len(ledger_rows) != 266 or set(row_by_key) != source_keys:
        failures.append("source/formal/ledger row counts or source key coverage differ from manifests")
    for column in LEDGER_COLUMNS:
        if any(row.get(column) == "" for row in ledger_rows):
            failures.append(f"blank ledger column: {column}")
    for row in ledger_rows:
        validate_row(row, source_keys, failures); validate_workflow(row, failures)
    validate_special_relations(ledger_rows, row_by_key, failures)
    formal_keys = {row.get("formal_key") for row in formal_manifest_rows}
    if len(formal_rows) != 165 or {row.get("formal_key") for row in formal_rows} != formal_keys or any(row.get(column) == "" for row in formal_rows for column in FORMAL_COLUMNS):
        failures.append("formal coverage table does not close all 165 formal rows")
    report = report_json(report_text, failures)
    set_counts = validate_report(report, ledger_rows, formal_rows, failures) if report else {}
    counts: JsonMap = {"source_rows": len(ledger_rows), "formal_rows": len(formal_rows), "sets": set_counts, "n_new": set_counts.get("planned-new-formal", 0)}
    summary: JsonMap = {"command": "ledger-check", "status": "PASS" if not failures else "FAIL", "counts": counts, "failures": failures, "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in (cli.source_manifest, cli.formal_manifest, cli.ledger, cli.reconciliation, cli.fixture)], "output_path": None if cli.check_only else {"ledger": str(cli.ledger), "reconciliation": str(cli.reconciliation)}}
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(3, "ledger-check", (ReceiptOutput("ledger", cli.ledger), ReceiptOutput("reconciliation", cli.reconciliation)), ()))
    return (0 if not failures else 1), summary


def ledger_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
