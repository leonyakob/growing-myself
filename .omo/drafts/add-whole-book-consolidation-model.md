---
slug: add-whole-book-consolidation-model
status: completed
intent: clear
pending-action: none
approach: Add a fourth whole-book consolidation stage to the generic and 《人生》 WeRead prompts, centered on the “阅读现场档案 + 文章素材索引” model. The revised plan separates internal consolidation ledgers from formal-note output, models cards with multiple axes rather than one mixed final-state list, and requires concrete `.omo/evidence` dry-run fixtures before prompt edits.
---

# Draft: add-whole-book-consolidation-model

## Components (topology ledger)

| id | outcome | status | evidence path |
|---|---|---|---|
| C1 | Generic prompt gains a fourth-stage whole-book consolidation model | active | .omo/plans/add-whole-book-consolidation-model.md |
| C2 | 《人生》 prompt gains the same model with fixed paths and regression samples preserved | active | .omo/plans/add-whole-book-consolidation-model.md |
| C3 | The model preserves reading process and card lookup while adding writing-oriented article indexes | active | .omo/plans/add-whole-book-consolidation-model.md |
| C4 | QA prevents note dumping, AI over-polishing, false deduplication, source-ID-only citations, and external-reader overreach | active | .omo/plans/add-whole-book-consolidation-model.md |

## Open assumptions (announced defaults)

| assumption | adopted default | rationale | reversible? |
|---|---|---|---|
| Formal note target structure | Add fourth-stage rules without forcing immediate restructuring of existing notes | User asked for plan first; current prompts already separate migration from execution | Yes |
| Model name | Use “阅读现场档案 + 文章素材索引” as the canonical label | User explicitly liked this model | Yes |
| Default formal note shape | “卡片档案为底座，文章素材索引为上层导航” | Preserves reading process and supports writing without collapsing either layer | Yes |
| Article index behavior | Article directions cite card anchors, quote snippets, and user reactions; they do not replace or rewrite cards | Prevents erasing reading-site evidence | Yes |
| Dry-run fixtures | Create concrete `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` before target prompt edits during implementation | Metis required deterministic fixtures; target prompts stay unedited before approval | Yes |

## Findings (cited - path:lines)

- `微信读书通用提示词.md:841-968` currently defines the third-stage migration rules: migrate optimized material into formal notes, preserve quote/user thought, avoid technical fields, assign material destinations, and run post-migration QA.
- `微信读书通用提示词.md:925-936` already says all valuable material should eventually have a destination, but it does not define a fourth whole-book consolidation stage or a dual-layer reading-site/archive plus article-index model.
- `微信读书通用提示词.md:899-906` and `微信读书通用提示词.md:962-968` forbid process residue and require readable evidence in formal notes.
- `微信读书通用提示词.md:1079-1083` has a small “读完整本书后回看我的阅读风格” shortcut, but this is only a style review snippet, not a complete whole-book consolidation workflow.
- `路遥/人生/《人生》微信读书提示词.md:820-948` mirrors the third-stage migration logic for 《人生》, including material destinations, external-reader rules, and QA.
- `路遥/人生/《人生》微信读书提示词.md:876-884` forbids process/technical residue in formal notes.
- `路遥/人生/《人生》微信读书提示词.md:903-914` says all material should have a destination, but it does not yet distinguish reading-site archive from article-material index.
- `路遥/人生/《人生》微信读书提示词.md:1038-1042` has a “读完整本书后回看我的阅读风格” shortcut, but it does not provide a whole-book consolidation plan.
- `路遥/人生/《人生》微信读书提示词.md:1046-1056` contains seven book-specific regression samples that must remain intact if the prompt is later edited.

## Review receipts

| reviewer | session | verdict | incorporated changes |
|---|---|---|---|
| Momus | `ses_0a3f599dcffeymD00c5UFTJhR9` | OKAY | Confirmed file path and overall plan are actionable; recommended more literal QA invocations. |
| Oracle | `ses_0a3f5807dffeWIV6VO7Q519CNY` | REJECT before fixes, PASS after fixes | Added multi-axis ledger, artifact boundary rules, fourth-stage non-remigration rule, fixed dry-run fixtures, preservation/usefulness assertions, and bloat controls. Post-fix review confirmed all prior blockers resolved. |
| Metis | `ses_0a3f58101ffeFSXLqj87P2v6mX` | REJECT before fixes, PASS after fixes | Added internal ledger vs formal output separation, source-status branches, readable evidence anchors, expanded duplicate/external-reader branches, corrected-misreading structure, light-card index-only use, final-note skeleton, and fixture requirement. Post-fix review confirmed all prior blockers resolved. |

## Decisions (with rationale)

1. Add a new fourth stage rather than overloading the third-stage migration rules. Third stage = migrate optimized round material; fourth stage = whole-book consolidation after the book is finished.
2. Use a dual-layer model: reading-site archive as the base layer; article-material index as the navigation/writing layer.
3. Replace the one-dimensional “final state” list with a multi-axis ledger: source status, archive disposition, evidence role, article links, trajectory flags, external-reader relation, and internal-only processing action.
4. Keep the internal consolidation ledger out of formal-note body. It may contain source IDs, ranges, processing states, and duplicate decisions; formal notes must use readable card anchors, quote snippets, and user-original excerpts.
5. Require “一卡双归宿”: every valuable card keeps an archive identity and may also be referenced by zero, one, or many article directions.
6. Make article directions cite cards, quote snippets, original reactions, tension/problem, internal/cross-work links, and missing-evidence fields; article indexes must not copy full card bodies or become essays.
7. Preserve reading trajectory as a first-class output only when meaningful: early misreadings, shallow judgments, hesitations, and later corrections may be valuable, but trivial corrections need not bloat the formal note.
8. Deduplicate by source relation and interpretive function, not by source range alone.
9. Keep external reader material subordinate: original wording, clear relation label, never replacing the user’s感受、问题、判断.

## Scope IN

- Plan future edits to `/home/king/github/growing-myself/微信读书通用提示词.md`.
- Plan future edits to `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
- Plan creation of `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` during implementation before target prompt edits.
- Add a fourth-stage whole-book consolidation section.
- Add reading-site archive / article-material index model rules.
- Add multi-axis ledger fields for whole-book consolidation.
- Add source-status handling for already migrated, partially migrated, unmigrated, conflicting, external-only, and insufficient-source materials.
- Add duplicate, misreading-correction, light-card promotion/index-use, external-reader, and bloat-prevention branches.
- Add dry-run QA scenarios with fixed inputs, expected archive treatment, expected article-index treatment, and forbidden failures.

## Scope OUT (Must NOT have)

- Do not edit the two target prompt files until the user explicitly approves this reviewed plan.
- Do not restructure any actual reading note or middle draft in this task.
- Do not call WeRead APIs or fetch new data.
- Do not remove or weaken existing third-stage migration rules.
- Do not re-run third-stage migration globally during fourth-stage consolidation unless a material is missing, duplicated, semantically wrong, or explicitly marked for remigration.
- Do not place source IDs, bookId, chapterUid, range, process-state labels, or verbose processing ledger rows into formal note body.
- Do not remove 《人生》 regression samples or fixed paths.
- Do not turn article-material index into AI-written article drafts.
- Do not force every light card into a complete card.
- Do not commit or push unless the user explicitly asks after implementation.

## Open questions

None blocking. The user’s preference is clear: preserve the reading process and card lookup, while also building a strong article-material index. The plan adopts “archive first, index second” as the default.

## Approval gate

status: completed

Completed after user approval. Prompt edits, fixture QA, and final review wave passed; Git commit/push remain unauthorized unless separately requested.
