from __future__ import annotations

import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from re import Pattern
from typing import TYPE_CHECKING, Final, NamedTuple, Protocol, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]


class RowLike(Protocol):
    def get(self, key: str) -> str: ...


class ReceiptOutputValue(NamedTuple): name: str; path: Path | None


class PhaseInputValue(NamedTuple): path: str; phase: str; sha256: str


class ReceiptSpecValue(NamedTuple): todo: int; subcommand: str; outputs: Sequence[ReceiptOutputValue]; phases: Sequence[PhaseInputValue]


if TYPE_CHECKING:
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]; PhaseInput: Callable[[str, str, str], PhaseInputValue]; ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[PhaseInputValue]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, Json], ReceiptSpecValue], None]; sha256_bytes: Callable[[bytes], str]
    candidate_structure_command: Callable[[Sequence[str]], tuple[int, JsonMap]]; part_texts: Callable[[str, list[str]], tuple[str, str, str]]; table_rows: Callable[[str, str], tuple[RowLike, ...]]
    TECHNICAL_TOKEN_RE: Pattern[str]; CARD_BODY_RE: Pattern[str]
else:
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["PhaseInput", "ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    PhaseInput = receipt_module.PhaseInput; ReceiptOutput = receipt_module.ReceiptOutput; ReceiptSpec = receipt_module.ReceiptSpec; append_validator_receipt = receipt_module.append_validator_receipt; sha256_bytes = receipt_module.sha256_bytes
    candidate_module = __import__("ren_sheng_whole_book_candidate_check", fromlist=["CARD_BODY_RE", "TECHNICAL_TOKEN_RE", "candidate_structure_command", "part_texts", "table_rows"])
    CARD_BODY_RE = candidate_module.CARD_BODY_RE; TECHNICAL_TOKEN_RE = candidate_module.TECHNICAL_TOKEN_RE; candidate_structure_command = candidate_module.candidate_structure_command; part_texts = candidate_module.part_texts; table_rows = candidate_module.table_rows

REVIEWED_SHA256: Final = "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"
CANDIDATE_SHA256: Final = "8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4"
TOPOLOGY_COUNTS: Final[Mapping[str, int]] = {"source-only": 134, "formal-only": 67, "one-to-one": 88, "many-to-one": 44, "duplicate": 0, "revision-chain": 0, "planned-new-formal": 0, "unresolved": 0}


@dataclass(frozen=True, slots=True)
class Cli:
    formal: Path; source_manifest: Path; formal_manifest: Path; ledger: Path; reconciliation: Path; technical: Path; fixture_results: Path; anchor_map: Path; candidate: Path; out: Path; check_only: bool; receipt: Path | None


@dataclass(frozen=True, slots=True)
class Texts:
    source_manifest: str; formal_manifest: str; ledger: str; reconciliation: str; technical: str; fixture_results: str; anchor_map: str; candidate: str


@dataclass(frozen=True, slots=True)
class Counts:
    part_a_rows: int; part_b_fragments: int; source_units: int; formal_cards: int; technical_rows: int; internal_input_hits: int; target_bound_forbidden_hits: int; modeled_post_cards: int; n_new: int; missing_unbound: int; missing_repair_approved: int; planned_by_approved_insertion: int; unresolved_anchors: int; duplicate_anchors: int; copied_card_body_markers: int; fixture_pass: int; sentinel_pass: int; article_rows: int; trajectory_rows: int


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "candidate-check":
        return "usage: candidate-check is required"
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
    required = ("formal", "source-manifest", "formal-manifest", "ledger", "reconciliation", "technical", "fixture-results", "anchor-map", "candidate", "out")
    if any(not isinstance(values.get(key), str) for key in required):
        return "--formal --source-manifest --formal-manifest --ledger --reconciliation --technical --fixture-results --anchor-map --candidate and --out are required"
    receipt = values.get("receipt")
    return Cli(Path(str(values["formal"])), Path(str(values["source-manifest"])), Path(str(values["formal-manifest"])), Path(str(values["ledger"])), Path(str(values["reconciliation"])), Path(str(values["technical"])), Path(str(values["fixture-results"])), Path(str(values["anchor-map"])), Path(str(values["candidate"])), Path(str(values["out"])), values["check-only"] is True, Path(receipt) if isinstance(receipt, str) else None)


def input_paths(cli: Cli) -> tuple[Path, ...]:
    return (cli.formal, cli.source_manifest, cli.formal_manifest, cli.ledger, cli.reconciliation, cli.technical, cli.fixture_results, cli.anchor_map, cli.candidate)


def int_metric(text: str, label: str, failures: list[str]) -> int:
    match = re.search(rf"(?m)^-?\s*{re.escape(label)}:\s*(\d+)\s*$", text)
    if match is None:
        failures.append(f"missing integer metric: {label}")
        return 0
    return int(match.group(1))


def none_metric(text: str, label: str, failures: list[str]) -> int:
    match = re.search(rf"(?m)^{re.escape(label)}:\s*(none|\d+)\s*$", text)
    if match is None:
        failures.append(f"missing none/integer metric: {label}")
        return 0
    return 0 if match.group(1) == "none" else int(match.group(1))


def int_from_map(values: Mapping[str, Json], key: str, failures: list[str]) -> int:
    value = values.get(key)
    if type(value) is int:
        return value
    failures.append(f"candidate structure count is not integer: {key}")
    return 0


def pass_count(text: str, first_column: str) -> int:
    return sum(1 for row in table_rows(text, first_column) if row.get("verdict") == "PASS")


def structure_counts(cli: Cli, failures: list[str]) -> JsonMap:
    code, summary = candidate_structure_command(["candidate-structure", "--candidate", str(cli.candidate), "--ledger", str(cli.ledger), "--technical", str(cli.technical), "--anchor-map", str(cli.anchor_map), "--check-only"])
    if code != 0 or summary.get("status") != "PASS":
        failures.append("candidate-structure dependency did not pass")
        dependency_failures = summary.get("failures")
        if isinstance(dependency_failures, Sequence) and not isinstance(dependency_failures, str):
            failures.extend(item for item in dependency_failures if isinstance(item, str))
    counts = summary.get("counts")
    if not isinstance(counts, Mapping):
        failures.append("candidate-structure summary did not include counts")
        return {}
    return dict(counts)


def target_hits(candidate_text: str, failures: list[str]) -> tuple[int, int, int]:
    part_a, part_b, part_c = part_texts(candidate_text, failures)
    rows = table_rows(part_a, "line")
    internal_hits = sum(1 for row in rows if TECHNICAL_TOKEN_RE.search(row.get("internal-before")) is not None)
    part_b_target = "" if part_b == "none" else "\n".join(line for line in part_b.splitlines() if "target-after" in line)
    target_forbidden = sum(1 for row in rows if TECHNICAL_TOKEN_RE.search(row.get("target-after")) is not None) + sum(1 for _match in TECHNICAL_TOKEN_RE.finditer(part_b_target)) + sum(1 for _match in TECHNICAL_TOKEN_RE.finditer(part_c))
    card_body_hits = sum(1 for _match in CARD_BODY_RE.finditer(part_c))
    return internal_hits, target_forbidden, card_body_hits


def load_texts(cli: Cli) -> Texts:
    return Texts(cli.source_manifest.read_text(encoding="utf-8"), cli.formal_manifest.read_text(encoding="utf-8"), cli.ledger.read_text(encoding="utf-8"), cli.reconciliation.read_text(encoding="utf-8"), cli.technical.read_text(encoding="utf-8"), cli.fixture_results.read_text(encoding="utf-8"), cli.anchor_map.read_text(encoding="utf-8"), cli.candidate.read_text(encoding="utf-8"))


def build_counts(cli: Cli, texts: Texts, failures: list[str]) -> Counts:
    structure = structure_counts(cli, failures)
    internal_hits, forbidden_hits, card_body_hits = target_hits(texts.candidate, failures)
    counts = Counts(int_from_map(structure, "part_a_rows", failures), int_from_map(structure, "part_b_fragments", failures), int_metric(texts.source_manifest, "Source units", failures), int_metric(texts.formal_manifest, "Formal cards", failures), int_metric(texts.technical, "Technical union", failures), internal_hits, forbidden_hits, int_metric(texts.anchor_map, "Post-transform cards", failures), int_metric(texts.anchor_map, "N_new", failures), texts.ledger.count("missing-unbound"), texts.ledger.count("missing-repair-approved"), texts.ledger.count("planned-by-approved-insertion"), none_metric(texts.anchor_map, "Unresolved anchors", failures), none_metric(texts.anchor_map, "Duplicate readable anchors", failures), card_body_hits, pass_count(texts.fixture_results, "case"), pass_count(texts.fixture_results, "sentinel"), int_from_map(structure, "article_rows", failures), int_from_map(structure, "trajectory_rows", failures))
    for label, expected in TOPOLOGY_COUNTS.items():
        if int_metric(texts.reconciliation, label, failures) != expected:
            failures.append(f"reconciliation topology count mismatch: {label}")
    if '"unresolved": []' not in texts.reconciliation:
        failures.append("reconciliation unresolved list is not []")
    return counts


def validate_counts(counts: Counts, failures: list[str]) -> None:
    expected = (("part_a_rows", counts.part_a_rows, 108), ("part_b_fragments", counts.part_b_fragments, 0), ("source_units", counts.source_units, 266), ("formal_cards", counts.formal_cards, 165), ("technical_rows", counts.technical_rows, 108), ("internal_input_hits", counts.internal_input_hits, 108), ("target_bound_forbidden_hits", counts.target_bound_forbidden_hits, 0), ("modeled_post_cards", counts.modeled_post_cards, 165), ("n_new", counts.n_new, 0), ("missing_unbound", counts.missing_unbound, 0), ("missing_repair_approved", counts.missing_repair_approved, 0), ("planned_by_approved_insertion", counts.planned_by_approved_insertion, 0), ("unresolved_anchors", counts.unresolved_anchors, 0), ("duplicate_anchors", counts.duplicate_anchors, 0), ("copied_card_body_markers", counts.copied_card_body_markers, 0), ("fixture_pass", counts.fixture_pass, 9), ("sentinel_pass", counts.sentinel_pass, 7), ("article_rows", counts.article_rows, 6), ("trajectory_rows", counts.trajectory_rows, 6))
    for label, actual, wanted in expected:
        if actual != wanted:
            failures.append(f"{label} expected {wanted}, got {actual}")
    if counts.formal_cards + counts.n_new != counts.modeled_post_cards:
        failures.append("modeled post-card equation is not formal_cards + N_new")


def counts_json(counts: Counts) -> JsonMap:
    return {"part_a_rows": counts.part_a_rows, "part_b_fragments": counts.part_b_fragments, "source_units": counts.source_units, "formal_cards": counts.formal_cards, "technical_rows": counts.technical_rows, "internal_input_hits": counts.internal_input_hits, "target_bound_forbidden_hits": counts.target_bound_forbidden_hits, "modeled_post_cards": counts.modeled_post_cards, "n_new": counts.n_new, "missing_unbound": counts.missing_unbound, "missing_repair_approved": counts.missing_repair_approved, "planned_by_approved_insertion": counts.planned_by_approved_insertion, "unresolved_anchors": counts.unresolved_anchors, "duplicate_anchors": counts.duplicate_anchors, "copied_card_body_markers": counts.copied_card_body_markers, "fixture_pass": counts.fixture_pass, "sentinel_pass": counts.sentinel_pass, "article_rows": counts.article_rows, "trajectory_rows": counts.trajectory_rows}


def qa_text(counts: Counts, failures: Sequence[str]) -> str:
    status = "PASS" if not failures else "FAIL"
    lines = ["# Ren Sheng whole-book candidate QA", "", f"Status: {status}", "", "## Reproducible Todo 7 QA matrix", "", "| gate | status | evidence |", "|---|---|---|", f"| preservation hashes | PASS | Formal reviewed baseline `{REVIEWED_SHA256}`; source/formal manifests parse to {counts.source_units} source units and {counts.formal_cards} formal cards. |", f"| Part A in-memory transforms | PASS | Applied {counts.part_a_rows} Part A target-after rows in memory; internal input hits: expected and confined to internal-before ({counts.internal_input_hits}). |", f"| Part B repair/new-card fragments | PASS | part_b_fragments={counts.part_b_fragments}; zero bound repair/new-card fragments, so no hunk is required. |", f"| target-bound forbidden hits: {counts.target_bound_forbidden_hits} | PASS | Scanned Part A target-after, Part B target-after, and Part C for 源ID/chapterUid/bookId/range/coordinate/raw coordinate labels. |", f"| modeled-post card/anchor cardinality | PASS | {counts.formal_cards} + N_new = {counts.modeled_post_cards}; N_new={counts.n_new}; unresolved=[]; duplicate readable anchors: {counts.duplicate_anchors}. |", f"| target-evidence relations | PASS | missing-unbound: {counts.missing_unbound}; missing-repair-approved={counts.missing_repair_approved}; planned-by-approved-insertion={counts.planned_by_approved_insertion}. |", f"| fixture/sentinel policy | PASS | nine fixture PASS ({counts.fixture_pass}) and seven sentinel PASS ({counts.sentinel_pass}) parsed from fixture results. |", f"| article and trajectory topology | PASS | six article-row PASS ({counts.article_rows}) and six trajectory-chain PASS ({counts.trajectory_rows}) verified through candidate and anchor map. |", f"| copied qualified card bodies | PASS | zero copied qualified card bodies ({counts.copied_card_body_markers}); method scanned Part C for `> ` quote lines and card-body markers `**【划线原文】**`, `**【我自己写的内容】**`, `**【我的原想法】**`, `**【AI评价】**`, `**【AI修正】**`, `**【AI补充】**`. |", "", "## Required acceptance fields", "", "- internal input hits: expected and confined to internal-before", f"- target-bound forbidden hits: {counts.target_bound_forbidden_hits}", f"- modeled-post card/anchor cardinality: {counts.formal_cards} + N_new = {counts.modeled_post_cards}", f"- missing-unbound: {counts.missing_unbound}", "- unresolved=[]", f"- duplicate readable anchors: {counts.duplicate_anchors}", f"- nine fixture PASS: {counts.fixture_pass}", f"- seven sentinel PASS: {counts.sentinel_pass}", f"- six article-row PASS: {counts.article_rows}", f"- six trajectory-chain PASS: {counts.trajectory_rows}", "", "## Copied-body excerpt check", "", "- Part C is accepted only as whole-book index prose under `## 全书收束整合`, not copied card bodies.", "- Excerpt-level negative evidence for a read-only reviewer: the forbidden card-body openers searched were exactly `> `, `**【划线原文】**`, `**【我自己写的内容】**`, `**【我的原想法】**`, `**【AI评价】**`, `**【AI修正】**`, and `**【AI补充】**`; all produced 0 hits in Part C."]
    if failures:
        lines.extend(["", "## Failures", *[f"- {failure}" for failure in failures]])
    return "\n".join(lines) + "\n"


def summary_json(cli: Cli, counts: Counts, failures: Sequence[str]) -> JsonMap:
    return {"command": "candidate-check", "status": "PASS" if not failures else "FAIL", "counts": counts_json(counts), "failures": list(failures), "input_hashes": [{"path": str(path), "sha256": sha256_bytes(path.read_bytes())} for path in input_paths(cli)], "output_path": None if cli.check_only else str(cli.out)}


def validate(cli: Cli) -> tuple[int, JsonMap]:
    failures = [f"unreadable input: {path}" for path in input_paths(cli) if not path.is_file()]
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if not cli.check_only and ((cli.out.exists() and not cli.out.is_file()) or not cli.out.parent.exists()):
        failures.append(f"invalid output path: {cli.out}")
    if cli.receipt is not None and not cli.receipt.parent.exists():
        failures.append(f"invalid receipt path: {cli.receipt}")
    if failures:
        return 2, {"command": "candidate-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    texts = load_texts(cli)
    if sha256_bytes(cli.formal.read_bytes()) != REVIEWED_SHA256:
        failures.append("formal input SHA-256 does not match reviewed baseline")
    if sha256_bytes(cli.candidate.read_bytes()) != CANDIDATE_SHA256:
        failures.append("candidate input SHA-256 does not match Todo 6 candidate")
    counts = build_counts(cli, texts, failures)
    validate_counts(counts, failures)
    text = qa_text(counts, failures)
    if not failures and cli.check_only:
        if not cli.out.is_file():
            failures.append(f"unreadable candidate QA artifact: {cli.out}")
        else:
            try:
                artifact_text = cli.out.read_text(encoding="utf-8")
            except OSError:
                failures.append(f"unreadable candidate QA artifact: {cli.out}")
            else:
                if artifact_text != text:
                    failures.append("candidate QA artifact differs from current evidence set")
    if not failures and not cli.check_only:
        _ = cli.out.write_text(text, encoding="utf-8")
    summary = summary_json(cli, counts, failures)
    if cli.receipt is not None:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(7, "candidate-check", (ReceiptOutput("candidate_qa", cli.out),), (PhaseInput("路遥/人生/《人生》阅读笔记.md", "reviewed-baseline", REVIEWED_SHA256),)))
    return (0 if not failures else 1), summary


def candidate_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
