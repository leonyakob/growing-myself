from __future__ import annotations

import hashlib
import re
import unicodedata
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Final, NamedTuple, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]


class ReceiptOutputValue(NamedTuple): name: str; path: Path | None


class PhaseInputValue(NamedTuple): path: str; phase: str; sha256: str


class ReceiptSpecValue(NamedTuple): todo: int; subcommand: str; outputs: Sequence[ReceiptOutputValue]; phases: Sequence[PhaseInputValue]


class ReceiptStateValue(NamedTuple): records: int; required_passes: int; latest_record_hash: str; todo10_record_hash: str | None


if TYPE_CHECKING:
    ReceiptOutput: Callable[[str, Path | None], ReceiptOutputValue]; PhaseInput: Callable[[str, str, str], PhaseInputValue]; ReceiptSpec: Callable[[int, str, Sequence[ReceiptOutputValue], Sequence[PhaseInputValue]], ReceiptSpecValue]
    append_validator_receipt: Callable[[Path, Mapping[str, Json], ReceiptSpecValue], None]; sha256_bytes: Callable[[bytes], str]
    verify_receipt_chain: Callable[[Path, Path, Path, list[str]], ReceiptStateValue]
else:
    receipt_module = __import__("ren_sheng_whole_book_receipts", fromlist=["PhaseInput", "ReceiptOutput", "ReceiptSpec", "append_validator_receipt", "sha256_bytes"])
    PhaseInput = receipt_module.PhaseInput; ReceiptOutput = receipt_module.ReceiptOutput; ReceiptSpec = receipt_module.ReceiptSpec; append_validator_receipt = receipt_module.append_validator_receipt; sha256_bytes = receipt_module.sha256_bytes
    final_receipts = __import__("ren_sheng_whole_book_final_receipts", fromlist=["verify_receipt_chain"])
    verify_receipt_chain = final_receipts.verify_receipt_chain

FINAL_FORMAL_SHA256: Final = "03cbe76f586b80a68db054f13d2dac04e5ee743d979dac4631b95ef54b25063f"
SOURCE_DRAFT_SHA256: Final = "dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0"
SEALED_PLAN_SHA256: Final = "8795332a59d1293daaee67d7d0c406bffacdedbd5d5d781f52e5b60215bca306"
PREFIX_AFTER_TODO8_SHA256: Final = "105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0"
PLAN_PATH: Final = Path(".omo/plans/consolidate-ren-sheng-whole-book-notes.md")
REVIEW_SEAL_PATH: Final = Path(".omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json")
SOURCE_DRAFT: Final = Path("路遥/人生/《人生》中间整理稿.md")
FINAL_QA_NAME: Final = "final-ren-sheng-whole-book-consolidation-qa.md"
RECEIPT_NAME: Final = "ren-sheng-whole-book-validator-invocations.jsonl"
PART_C_HEADER: Final = "## Part C. Complete target-bound `## 全书收束整合`"
PLAN_CHECKBOX_RE: Final = re.compile(r"(?m)^(\s*- \[)[x~](\])")
TECHNICAL_TOKEN_RE: Final = re.compile(r"external-源ID(?:s)?|源ID(?:s)?|源\s+ID(?:s)?|chapterUid|bookId|\brange\b|(?<!\d)\d+\s*-\s*\d+(?!\d)")

EXPECTED_HASHES: Final[Mapping[str, str]] = {
    "ren-sheng-whole-book-candidate-section.md": "8a7bba7eb2e5c2a164166094423ace38629a303dcbc4fe5da51a3044106bb9a4",
    "ren-sheng-whole-book-candidate-qa.md": "15ae68fc6a15fa43a21d995d9fdf5236e47c31483abd222ead1c45bbd4470100",
    "ren-sheng-whole-book-metadata-cleanup.md": "f6868d82b1e14e92af4c4b47ddb6343dc5e84a489daedf76c7b7bad7f9dfc28d",
    "ren-sheng-whole-book-archive-audit.md": "be3e2197ebecb052b3c106f36c64792c2795d0c09a70fe5948c1d51c1f4c8705",
    "ren-sheng-whole-book-index-audit.md": "6f09a99a6248a2a90bc021185ff97c9109789e25bae88e983686767c2c1725c2",
    "ren-sheng-whole-book-trajectory-audit.md": "f86e9db19cde9aa29f3559a9c9c36e56aff6269a34358288f00a5cab46a0e5cd",
}
SEMANTIC_AXES: Final = ("source_status", "archive_disposition", "evidence_role", "article_links", "trajectory_flags", "external_reader_relation", "source_relation", "interpretation_relation")
RECONCILIATION_AXES: Final = ("source-only", "formal-only", "one-to-one", "many-to-one", "duplicate", "revision-chain", "planned-new-formal", "unresolved")
EXPECTED_RECONCILIATION: Final[Mapping[str, int]] = {"source-only": 134, "formal-only": 67, "one-to-one": 88, "many-to-one": 44, "duplicate": 0, "revision-chain": 0, "planned-new-formal": 0, "unresolved": 0}
SECTION_HEADERS: Final = ("### 一、阅读现场档案", "### 二、文章素材索引", "### 三、阅读轨迹与判断变化", "### 四、待回看 / 归档不迁移")
ARTICLE_DIRECTIONS: Final = ("#### 人物线", "#### 城乡主题", "#### 尊严主题", "#### 爱情线", "#### 知识分子困境", "#### 写法线索")
TRAJECTORY_HEADINGS: Final = (
    "#### 特权态度：从只写“痛恨特权”推进到“也痛恨自己没有特权”的挑战",
    "#### 劳动与身份：从“高加林不愿掏炭”推进到他能承受新闻现场之苦、真正差别在身份意义",
    "#### 职业热爱：从“热爱让苦甘之如饴”收稳为记者身份重新编码痛感，并保留田晓霞联想但不混同两人",
    "#### 县城空间：从“县城变小等于忘本”修正为身份落差投向空间的心理投影，不把后来的失败倒灌进当时场景",
    "#### 爱情与位置：保留“农民时爱巧珍、干部时爱黄亚萍”的原始锋利表达，同时补足“位置影响哪一种爱被承认”的证据桥",
    "#### 黄亚萍物质付出：从“这不是牺牲”修正为“有真实成本，但不等同于巧珍在匮乏中的托举”",
)


@dataclass(frozen=True, slots=True)
class Cli:
    formal: Path
    evidence_root: Path
    preflight: Path
    check_only: bool
    receipt: Path | None


@dataclass(frozen=True, slots=True)
class Counts:
    final_formal_sha256: str; source_draft_sha256: str; source_units: int; preserved_cards: int; final_cards: int; semantic_axes: int; reconciliation_axes: int; n_new: int; technical_rows: int; target_bound_hits: int; fixture_pass: int; sentinel_pass: int; section_children: int; article_directions: int; trajectory_chains: int; archive_rows: int; anchor_rows: int; duplicate_anchors: int; unresolved_anchors: int; article_links_none: int; receipt_required_passes: int; current_plan_sha256: str; canonical_plan_sha256: str; review_seal_plan_sha256: str


def normalize_bytes(data: bytes) -> str:
    text = data.decode("utf-8", "strict").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(unicodedata.normalize("NFC", text).encode("utf-8")).hexdigest()


def canonical_plan_sha256(path: Path) -> str:
    if not path.is_file():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    return hashlib.sha256(PLAN_CHECKBOX_RE.sub(r"\1 \2", text).encode("utf-8")).hexdigest()


def review_seal_plan_sha256(path: Path) -> str:
    if not path.is_file():
        return "MISSING"
    match = re.search(r'"plan_sha256"\s*:\s*"([0-9a-f]{64})"', path.read_text(encoding="utf-8"))
    return match.group(1) if match else "MISSING"


def parse_cli(argv: Sequence[str]) -> Cli | str:
    if not argv or argv[0] != "final-check":
        return "usage: final-check is required"
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
    if not isinstance(values.get("formal"), str) or not isinstance(values.get("evidence-root"), str) or not isinstance(values.get("preflight"), str):
        return "--formal --evidence-root and --preflight are required"
    receipt = values.get("receipt")
    return Cli(Path(str(values["formal"])), Path(str(values["evidence-root"])), Path(str(values["preflight"])), values["check-only"] is True, Path(receipt) if isinstance(receipt, str) else None)


def split_cells(line: str) -> tuple[str, ...]:
    return tuple(cell.strip().replace("\\|", "|") for cell in line.strip().strip("|").split("|"))


def table_rows(text: str, first_column: str) -> tuple[Mapping[str, str], ...]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| {first_column} "):
            header = split_cells(line)
            rows: list[Mapping[str, str]] = []
            for raw in lines[index + 2:]:
                if not raw.startswith("|"):
                    break
                rows.append(dict(zip(header, split_cells(raw), strict=True)))
            return tuple(rows)
    return ()


def int_metric(text: str, label: str) -> int:
    match = re.search(rf"(?m)^-?\s*{re.escape(label)}:\s*(\d+|none)\s*$", text)
    return 0 if match is None or match.group(1) == "none" else int(match.group(1))


def is_card_heading(line_no: int, line: str) -> bool:
    return (3 <= line_no < 557 and re.match(r"^###\s+\d+\.\s+", line) is not None) or (557 <= line_no < 1238 and re.match(r"^###\s+\d+\.\s+", line) is not None) or (1238 <= line_no < 1701 and re.match(r"^###\s+\d+\.\s+", line) is not None) or (line_no >= 1701 and (re.match(r"^###\s+\d+\.\s+", line) is not None or re.match(r"^####\s+\d+\.\s+", line) is not None))


def final_card_count(formal_text: str) -> int:
    return sum(1 for index, line in enumerate(formal_text.splitlines(), start=1) if is_card_heading(index, line))


def verify_evidence_hashes(evidence_root: Path, failures: list[str]) -> None:
    for name, expected in EXPECTED_HASHES.items():
        path = evidence_root / name
        if not path.is_file():
            failures.append(f"unreadable evidence file: {name}")
            continue
        actual = sha256_bytes(path.read_bytes())
        if actual != expected:
            failures.append(f"evidence file hash drift: {name} expected {expected} got {actual}")


def verify_reconciliation(text: str, failures: list[str]) -> int:
    seen = 0
    for axis in RECONCILIATION_AXES:
        actual = int_metric(text, axis)
        expected = EXPECTED_RECONCILIATION[axis]
        if actual != expected:
            failures.append(f"reconciliation axis drift: {axis} expected {expected} got {actual}")
        else:
            seen += 1
    if '"unresolved": []' not in text:
        failures.append("reconciliation unresolved list is not []")
    return seen


def candidate_part_c(candidate_text: str) -> str:
    return candidate_text.split(PART_C_HEADER, 1)[1].strip() if PART_C_HEADER in candidate_text else ""


def suffix_text(formal_text: str, failures: list[str]) -> str:
    if formal_text.count("## 全书收束整合") != 1:
        failures.append("appended whole-book section must appear exactly once")
        return ""
    head, tail = formal_text.split("## 全书收束整合", 1)
    if sha256_bytes(head.encode("utf-8")) != PREFIX_AFTER_TODO8_SHA256:
        failures.append("prefix before 全书收束整合 drift")
    return "## 全书收束整合" + tail


def pass_rows(text: str, first_column: str) -> int:
    return sum(1 for row in table_rows(text, first_column) if row.get("verdict") == "PASS")


def status_pass(text: str, label: str, failures: list[str]) -> None:
    if "Status: PASS" not in text:
        failures.append(f"{label} artifact is not Status: PASS")


def build_counts(cli: Cli, failures: list[str]) -> Counts:
    root = cli.evidence_root
    formal_text = cli.formal.read_text(encoding="utf-8")
    source_hash = sha256_bytes(SOURCE_DRAFT.read_bytes()) if SOURCE_DRAFT.is_file() else "MISSING"
    current_plan_hash = sha256_bytes(PLAN_PATH.read_bytes()) if PLAN_PATH.is_file() else "MISSING"
    canonical_plan_hash = canonical_plan_sha256(PLAN_PATH)
    seal_plan_hash = review_seal_plan_sha256(REVIEW_SEAL_PATH)
    source_text = (root / "ren-sheng-whole-book-source-manifest.md").read_text(encoding="utf-8")
    preservation_text = (root / "ren-sheng-whole-book-preservation-manifest.md").read_text(encoding="utf-8")
    ledger_text = (root / "ren-sheng-whole-book-consolidation-ledger.md").read_text(encoding="utf-8")
    reconciliation_text = (root / "ren-sheng-whole-book-reconciliation.md").read_text(encoding="utf-8")
    technical_text = (root / "ren-sheng-whole-book-technical-field-inventory.md").read_text(encoding="utf-8")
    fixture_text = (root / "ren-sheng-whole-book-fixture-results.md").read_text(encoding="utf-8")
    anchor_text = (root / "ren-sheng-whole-book-anchor-map.md").read_text(encoding="utf-8")
    archive_text = (root / "ren-sheng-whole-book-archive-audit.md").read_text(encoding="utf-8")
    index_text = (root / "ren-sheng-whole-book-index-audit.md").read_text(encoding="utf-8")
    trajectory_text = (root / "ren-sheng-whole-book-trajectory-audit.md").read_text(encoding="utf-8")
    candidate_text = (root / "ren-sheng-whole-book-candidate-section.md").read_text(encoding="utf-8")
    suffix = suffix_text(formal_text, failures)
    if suffix.strip() != candidate_part_c(candidate_text):
        failures.append("final suffix differs from approved candidate Part C")
    actual_sha = sha256_bytes(cli.formal.read_bytes())
    if actual_sha != FINAL_FORMAL_SHA256:
        failures.append(f"formal note SHA-256 drift: expected {FINAL_FORMAL_SHA256} got {actual_sha}")
    if source_hash != SOURCE_DRAFT_SHA256:
        failures.append(f"source draft SHA-256 drift: expected {SOURCE_DRAFT_SHA256} got {source_hash}")
    if canonical_plan_hash != seal_plan_hash or seal_plan_hash != SEALED_PLAN_SHA256:
        failures.append(f"checkbox-normalized plan hash does not match review seal: canonical {canonical_plan_hash}, seal {seal_plan_hash}")
    semantic = sum(1 for axis in SEMANTIC_AXES if axis in ledger_text)
    missing_axes = [axis for axis in SEMANTIC_AXES if axis not in ledger_text]
    failures.extend(f"semantic axis absent from ledger: {axis}" for axis in missing_axes)
    status_pass(archive_text, "archive audit", failures); status_pass(index_text, "index audit", failures); status_pass(trajectory_text, "trajectory audit", failures)
    anchor_rows = table_rows(anchor_text, "formal_key")
    anchor_paths = tuple(row.get("post_transform_anchor", "") for row in anchor_rows)
    receipt_state = verify_receipt_chain(root / RECEIPT_NAME, root, root / FINAL_QA_NAME, failures)
    counts = Counts(actual_sha, source_hash, int_metric(source_text, "Source units"), int_metric(preservation_text, "Formal cards"), final_card_count(formal_text), semantic, verify_reconciliation(reconciliation_text, failures), int_metric(anchor_text, "N_new"), int_metric(technical_text, "Technical union"), len(TECHNICAL_TOKEN_RE.findall(formal_text)), pass_rows(fixture_text, "case"), pass_rows(fixture_text, "sentinel"), sum(1 for header in SECTION_HEADERS if suffix.count(header) == 1), sum(1 for heading in ARTICLE_DIRECTIONS if suffix.count(heading) == 1), sum(1 for heading in TRAJECTORY_HEADINGS if suffix.count(heading) == 1), sum(1 for line in archive_text.splitlines() if re.match(r"^\|\s*\d+\s*\|\s*F\d{3}\s*\|", line)), len(anchor_rows), len(anchor_paths) - len(set(anchor_paths)), sum(1 for anchor in anchor_paths if TECHNICAL_TOKEN_RE.search(anchor) is not None), sum(1 for row in anchor_rows if row.get("article_links") == "none" and row.get("insertion_target") == "none"), receipt_state.required_passes, current_plan_hash, canonical_plan_hash, seal_plan_hash)
    validate_counts(counts, failures)
    return counts


def validate_counts(counts: Counts, failures: list[str]) -> None:
    expected = (("source_units", counts.source_units, 266), ("preserved_cards", counts.preserved_cards, 165), ("final_cards", counts.final_cards, 165), ("semantic_axes", counts.semantic_axes, 8), ("reconciliation_axes", counts.reconciliation_axes, 8), ("n_new", counts.n_new, 0), ("technical_rows", counts.technical_rows, 108), ("target_bound_hits", counts.target_bound_hits, 0), ("fixture_pass", counts.fixture_pass, 9), ("sentinel_pass", counts.sentinel_pass, 7), ("section_children", counts.section_children, 4), ("article_directions", counts.article_directions, 6), ("trajectory_chains", counts.trajectory_chains, 6), ("archive_rows", counts.archive_rows, 165), ("anchor_rows", counts.anchor_rows, 165), ("duplicate_anchors", counts.duplicate_anchors, 0), ("unresolved_anchors", counts.unresolved_anchors, 0), ("article_links_none", counts.article_links_none, 67), ("receipt_required_passes", counts.receipt_required_passes, 7))
    for label, actual, wanted in expected:
        if actual != wanted:
            failures.append(f"{label} expected {wanted}, got {actual}")
    if counts.preserved_cards + counts.n_new != counts.final_cards:
        failures.append("165 + N_new equation does not match final card count")


def counts_json(counts: Counts) -> JsonMap:
    return {"final_formal_sha256": counts.final_formal_sha256, "source_draft_sha256": counts.source_draft_sha256, "source_units": counts.source_units, "preserved_cards": counts.preserved_cards, "final_cards": counts.final_cards, "semantic_axes": counts.semantic_axes, "reconciliation_axes": counts.reconciliation_axes, "n_new": counts.n_new, "technical_rows": counts.technical_rows, "target_bound_hits": counts.target_bound_hits, "fixture_pass": counts.fixture_pass, "sentinel_pass": counts.sentinel_pass, "section_children": counts.section_children, "article_directions": counts.article_directions, "trajectory_chains": counts.trajectory_chains, "archive_rows": counts.archive_rows, "anchor_rows": counts.anchor_rows, "duplicate_anchors": counts.duplicate_anchors, "unresolved_anchors": counts.unresolved_anchors, "article_links_none": counts.article_links_none, "receipt_required_passes": counts.receipt_required_passes, "current_plan_sha256": counts.current_plan_sha256, "canonical_plan_sha256": counts.canonical_plan_sha256, "review_seal_plan_sha256": counts.review_seal_plan_sha256}


def final_qa_text(counts: Counts, failures: Sequence[str]) -> str:
    status = "PASS" if not failures else "FAIL"
    rows = [
        ("source preservation", f"immutable source SHA `{counts.source_draft_sha256}`; 266 source units parsed as {counts.source_units}."),
        ("formal preservation / 165 + N_new = 165", f"final formal SHA `{counts.final_formal_sha256}`; preserved cards {counts.preserved_cards}; final cards {counts.final_cards}; N_new={counts.n_new}."),
        ("all eight Phase 4 axes", f"ledger contains {counts.semantic_axes}/8 semantic axes without merging them into topology/action fields."),
        ("all eight reconciliation sets", f"source-only=134, formal-only=67, one-to-one=88, many-to-one=44, duplicate/revision-chain/planned-new-formal/unresolved=0; detected {counts.reconciliation_axes}/8."),
        ("108→0 cleanup", f"technical baseline rows={counts.technical_rows}; reader-facing target-bound technical hits in final formal note={counts.target_bound_hits}."),
        ("prefix/suffix", f"prefix before `## 全书收束整合` equals Todo 8 SHA `{PREFIX_AFTER_TODO8_SHA256}`; suffix matches approved candidate Part C."),
        ("section/article/trajectory", f"four child sections={counts.section_children}; article directions={counts.article_directions}; trajectory chains={counts.trajectory_chains}."),
        ("fixture/sentinel", f"fixture PASS rows={counts.fixture_pass}; sentinel PASS rows={counts.sentinel_pass}."),
        ("final anchors", f"anchor rows={counts.anchor_rows}; duplicate={counts.duplicate_anchors}; unresolved={counts.unresolved_anchors}; article_links=none rows={counts.article_links_none}."),
        ("content quality", "archive/index/trajectory audits are Status: PASS; candidate QA hash is pinned and proves zero copied card-body markers, external-reader subordination through Case 7, and no target-bound technical residue."),
        ("sealed plan control", f"current plan SHA `{counts.current_plan_sha256}` may differ from the review seal because operational checkboxes changed; checkbox-normalized canonical plan SHA `{counts.canonical_plan_sha256}` matches review seal plan SHA `{counts.review_seal_plan_sha256}`."),
        ("scope/git gates", "preflight correction/addendum classifies exact `ren_sheng_*.py` helper modules as validator support, orchestration files as control/runtime state, and reviewer sessions by exact runtime-ledger nodes; formal/source hashes plus baseline HEAD/refs/cached-diff/staged gates remain separate read-only checks; push is prohibited and is not claimed as post-state proof."),
        ("receipt chain", f"validator JSONL prefix chain is valid; latest Todo 1-7 PASS outputs match current artifacts ({counts.receipt_required_passes}/7); Todo 10 receipt is appended by `final-check --receipt` with the final_qa output hash."),
    ]
    lines = ["# Final Ren Sheng whole-book consolidation QA", "", f"Status: {status}", "", "## Todo 10 PASS matrix", "", "| gate | status | evidence |", "|---|---|---|"]
    lines.extend(f"| {gate} | PASS | {evidence} |" for gate, evidence in rows)
    lines.extend(["", "## Immutable hashes", "", f"- final formal note: `{counts.final_formal_sha256}`", f"- immutable source draft: `{SOURCE_DRAFT_SHA256}`", f"- Todo 8 prefix: `{PREFIX_AFTER_TODO8_SHA256}`", "", "## Push prohibition", "", "Push is prohibited. This row is an enforced scope rule, not a post-state proof from a push attempt.", ""])
    if failures:
        lines.extend(["## Failures", *[f"- {failure}" for failure in failures]])
    return "\n".join(lines) + "\n"


def summary_json(cli: Cli, counts: Counts, failures: Sequence[str]) -> JsonMap:
    return {"command": "final-check", "status": "PASS" if not failures else "FAIL", "counts": counts_json(counts), "failures": list(failures), "input_hashes": [{"path": str(cli.formal), "sha256": sha256_bytes(cli.formal.read_bytes())}, {"path": str(cli.preflight), "sha256": sha256_bytes(cli.preflight.read_bytes())}], "output_path": None if cli.check_only else str(cli.evidence_root / FINAL_QA_NAME)}


def validate(cli: Cli) -> tuple[int, JsonMap]:
    final_qa_path = cli.evidence_root / FINAL_QA_NAME
    failures: list[str] = []
    if not cli.formal.is_file():
        failures.append(f"unreadable formal note: {cli.formal}")
    if not cli.preflight.is_file():
        failures.append(f"unreadable preflight: {cli.preflight}")
    if cli.check_only and cli.receipt is not None:
        failures.append("--check-only forbids --receipt")
    if cli.receipt is not None and not cli.receipt.parent.exists():
        failures.append(f"invalid receipt path: {cli.receipt}")
    if failures:
        return 2, {"command": "final-check", "status": "FAIL", "counts": {}, "failures": failures, "input_hashes": [], "output_path": None}
    verify_evidence_hashes(cli.evidence_root, failures)
    counts = build_counts(cli, failures)
    text = final_qa_text(counts, failures)
    if not failures and cli.check_only:
        if not final_qa_path.is_file():
            failures.append(f"unreadable final QA artifact: {final_qa_path}")
        elif final_qa_path.read_text(encoding="utf-8") != text:
            failures.append("final QA artifact differs from current evidence set")
    if not failures and not cli.check_only:
        _ = final_qa_path.write_text(text, encoding="utf-8")
    summary = summary_json(cli, counts, failures)
    if cli.receipt is not None and not cli.check_only and not failures:
        append_validator_receipt(cli.receipt, summary, ReceiptSpec(10, "final-check", (ReceiptOutput("final_qa", final_qa_path),), (PhaseInput("路遥/人生/《人生》阅读笔记.md", "post-Todo9-final", FINAL_FORMAL_SHA256),)))
    return (0 if not failures else 1), summary


def final_check_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    parsed = parse_cli(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "counts": {}, "failures": [parsed], "input_hashes": [], "output_path": None}
    return validate(parsed)
