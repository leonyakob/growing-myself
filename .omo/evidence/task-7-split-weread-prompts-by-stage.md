# Task 7 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Live QA targets:
  - `/home/king/github/growing-myself/微信读书通用提示词.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md`
- Upstream immutable snapshot consulted for stale-state comparison context: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Upstream evidence consulted and read in full before this gate:
  - `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-2-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-3-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-4-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-5-split-weread-prompts-by-stage.md`
  - `/home/king/github/growing-myself/.omo/evidence/task-6-split-weread-prompts-by-stage.md`
- Stage 4 fixture source consulted: `/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md`

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Generic QA conclusion after reread:
  - all four generic stage files explicitly require root `AGENTS.md`
  - no generic output imports `/home/king/github/growing-myself/路遥/人生/AGENTS.md`
  - no generic output imports `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md`

| AGENTS path check | Hit count across generic outputs | Evidence | Status |
| --- | ---: | --- | --- |
| `/home/king/github/growing-myself/AGENTS.md` | 5 | Stage 1 line 7, Stage 2 lines 6 and 292, Stage 3 line 5, Stage 4 line 5 | PASS |
| `/home/king/github/growing-myself/路遥/人生/AGENTS.md` | 0 | `AGENTS_PATH_CHECK` script output | PASS |
| `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` | 0 | `AGENTS_PATH_CHECK` script output | PASS |

Files changed:

- `/home/king/github/growing-myself/.omo/evidence/task-7-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only)

Commands run:

- `GIT_MASTER=1 git diff --check -- "微信读书通用提示词.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第一阶段-生成中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第二阶段-优化中间整理稿.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep --untracked -E -n "若.*总提示词.*冲突.*总提示词为准|如果.*总提示词.*冲突.*总提示词为准" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "微信读书通用提示词.md" "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"`
- `python3 - <<'PY' ... TARGET_EXISTENCE_PREFLIGHT / ROUTER_DISCOVERABILITY / MARKDOWN_LINKS / CODE_FENCES / STAGE_INHERITANCE_FIELDS / SHORTCUT_ROUTING / STAGE4_FIXTURE_COVERAGE / STAGE2_CROSS_GENRE ... PY`
- `python3 - <<'PY' ... GENERIC_CONTAMINATION_CHECK / AGENTS_PATH_CHECK ... PY`
- `python3 - <<'PY' ... HEADING_AND_BOUNDARY_CHECKS ... PY`

Read-based QA notes:

## Upstream evidence completeness

| Evidence file | Read result | QA gate note | Status |
| --- | --- | --- | --- |
| `task-1-split-weread-prompts-by-stage.md` | Full read completed | Snapshot, move ledger, protected-baseline notes, and PASS section all present | PASS |
| `task-2-split-weread-prompts-by-stage.md` | Full read completed | The inherited incompleteness risk is repaired. The file now contains untracked-safe whitespace evidence, dry-run routing table, link validation, and PASS section | PASS |
| `task-3-split-weread-prompts-by-stage.md` | Full read completed | Stage 1 token checks, boundary checks, and PASS section present | PASS |
| `task-4-split-weread-prompts-by-stage.md` | Full read completed | Stage 2 AGENTS toolbox, cross-genre caveat, and PASS section present | PASS |
| `task-5-split-weread-prompts-by-stage.md` | Full read completed | Stage 3 migration structure, boundary warnings, and PASS section present | PASS |
| `task-6-split-weread-prompts-by-stage.md` | Full read completed | Stage 4 fixture coverage, archive-before-index rule, and PASS section present | PASS |

## Target-existence preflight

| Target path | Result | Status |
| --- | --- | --- |
| `微信读书通用提示词.md` | EXISTS | PASS |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | EXISTS | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | EXISTS | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | EXISTS | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | EXISTS | PASS |
| `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` | EXISTS | PASS |

## Per-file heading coverage

| File | Heading coverage read back from current file | Coverage note | Status |
| --- | --- | --- | --- |
| `微信读书通用提示词.md` | `## 阶段文件索引（先选阶段）`, `## 0`, `### 0.1`, `## 1`, `## 2`, `## 3`, `## 4`, `## 5`, `## 6`, `## 7` | Router still acts as authority and entry gate, not as a mega-stage execution dump | PASS |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | `## 继承块`, `## 1` through `## 12`, plus `## 本轮索引` subheads | Stage 1 covers fetch, match, classify, draft format, and QA without Stage 2 or Stage 3 execution leakage | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | `## 继承块`, `## 文学分析质量规则`, all Stage 2 rule blocks, `## 第二阶段 QA` | Stage 2 covers diagnosis, optimization, AGENTS toolbox, and external-reader analysis without formal-note write | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | `## 继承块`, `## 第三阶段与第四阶段边界`, `## 迁移前回源预检`, `## 正式阅读笔记结构`, `## 下次接着整理位置`, `## 所有材料最终都要有归宿`, `## 外部读者材料迁移规则`, `## 迁移后防回归 QA` | Stage 3 covers migration-only structure and keeps Stage 4 terms as warning boundaries | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | blockquote inheritance block, `## 1` through `## 11`, plus skeleton heads `### 一` to `### 四` | Stage 4 covers whole-book consolidation, archive-first readable structure, and fixture-based QA | PASS |

## Router discoverability and shortcut routing

| Token or route case | Evidence | Expected route | Status |
| --- | --- | --- | --- |
| `## 阶段文件索引（先选阶段）` | first H2 in router | router top index | PASS |
| `| 用户意图 | 应打开的文件 | 允许产出 | 禁止事项 |` | router line 4 | exact table columns present | PASS |
| `只整理，不评价` | router lines 7 and 237 | Stage 1 | PASS |
| `只咨询规则` | router line 11 | router only | PASS |
| `状态检查` | router lines 11, 49, 56 | router only | PASS |
| `修改通用 router` | router line 12 | router only | PASS |
| `只优化轻卡` | router lines 8 and 238 | Stage 2 | PASS |
| `迁移前回源预检` | router lines 9, 233, 239 | Stage 3 | PASS |
| `全书收束整合` | router lines 10, 108, 109, 167, 240, 242 | Stage 4 | PASS |

## Markdown link validation

| Relative path | Occurrence lines | Existence | Status |
| --- | --- | --- | --- |
| `./微信读书通用提示词-第一阶段-生成中间整理稿.md` | router lines `6, 7, 97, 237` | EXISTS | PASS |
| `./微信读书通用提示词-第二阶段-优化中间整理稿.md` | router lines `8, 101, 238` | EXISTS | PASS |
| `./微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | router lines `9, 105, 239` | EXISTS | PASS |
| `./微信读书通用提示词-第四阶段-全书收束整合.md` | router lines `10, 109, 240` | EXISTS | PASS |

Read-based note: current generic stage files do not add extra Markdown links to local generic files. Their local-file references are inline code paths and were checked semantically during reread.

## Code-fence validation

| File | Triple-backtick count | Result | Status |
| --- | ---: | --- | --- |
| `微信读书通用提示词.md` | 8 | BALANCED | PASS |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | 4 | BALANCED | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | 12 | BALANCED | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | 6 | BALANCED | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | 4 | BALANCED | PASS |

## Conflict-rule results

| File | Grep hit | Status |
| --- | --- | --- |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | line 10, `如果本阶段提示词与总提示词冲突，以总提示词为准。` | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | line 11, `若本阶段提示词与总提示词冲突，以总提示词为准。` | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | line 8, `若本阶段提示词与总提示词冲突，以总提示词为准。` | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | line 8, `若本阶段提示词与总提示词冲突，以总提示词为准。` | PASS |

## Stale numeric reference result

- Exact stale-reference grep command returned no output.

| File | Grep classification | Status |
| --- | --- | --- |
| `微信读书通用提示词.md` | no-hit | PASS |
| `微信读书通用提示词-第一阶段-生成中间整理稿.md` | no-hit | PASS |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | no-hit | PASS |
| `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | no-hit | PASS |
| `微信读书通用提示词-第四阶段-全书收束整合.md` | no-hit | PASS |

## Whitespace checks

| Command target | Result | Status |
| --- | --- | --- |
| tracked router `微信读书通用提示词.md` | no output | PASS |
| untracked-safe Stage 1 check | no output | PASS |
| untracked-safe Stage 2 check | no output | PASS |
| untracked-safe Stage 3 check | no output | PASS |
| untracked-safe Stage 4 check | no output | PASS |

## No-contamination results

| Token | Result | Status |
| --- | --- | --- |
| `高加林` | ABSENT across all five generic outputs | PASS |
| `巧珍` | ABSENT across all five generic outputs | PASS |
| `黄亚萍` | ABSENT across all five generic outputs | PASS |
| `刘玉海` | ABSENT across all five generic outputs | PASS |
| `CB_2tb79r78T38k74M75h8iz4C3` | ABSENT across all five generic outputs | PASS |
| `25164497` | ABSENT across all five generic outputs | PASS |
| `ID 003` | ABSENT across all five generic outputs | PASS |
| `ID 006` | ABSENT across all five generic outputs | PASS |
| `ID 021` | ABSENT across all five generic outputs | PASS |
| `ID 109` | ABSENT across all five generic outputs | PASS |
| `ID 117` | ABSENT across all five generic outputs | PASS |
| `刘玉海救灾处` | ABSENT across all five generic outputs | PASS |
| `黄亚萍的物质付出` | ABSENT across all five generic outputs | PASS |

## Stage boundary checks

| Stage | Read-based evidence | Result | Status |
| --- | --- | --- | --- |
| Router | Lines 3 to 13 route requests by phase and forbid dumping long execution bodies back into the router | authority-only router preserved | PASS |
| Stage 1 | Lines 6 to 12 and 203 to 204 keep fetch, match, light pre-classification, and draft output only | no deep optimization or migration instruction | PASS |
| Stage 2 | Lines 4 to 20 and 231 to 407 keep optimization inside `{中间稿路径}`, preserve user originals, and forbid formal-note write | optimization-only boundary preserved | PASS |
| Stage 3 | Lines 4 to 10, 27 to 29, 33 to 38, and 59 to 90 keep migration-only scope, source-original preservation, and Stage 4 as warning only | migration-only boundary preserved | PASS |
| Stage 4 | Lines 4 to 10, 17, 26, 60 to 61, 74, 142 to 176 keep whole-book-only scope, forbid global Stage 3 rerun, and force archive before index | whole-book-only boundary preserved | PASS |

## Cross-genre protection result

| File | Evidence | Status |
| --- | --- | --- |
| `微信读书通用提示词-第二阶段-优化中间整理稿.md` | line 17 says generic rules cannot be novel-only, line 64 says literary and non-fiction works both follow the principle but with different analytical focus | PASS |

## Stage 4 fixture coverage result

| Case | Prompt evidence | Status |
| --- | --- | --- |
| 1. partially migrated card | Stage 4 lines 148 and 166 require补 readable evidence 与用户原句 | PASS |
| 2. duplicate same quote + same insight | Stage 4 lines 149 and 106 require representative-card merge into internal ledger | PASS |
| 3. duplicate same quote + changed judgment | Stage 4 lines 150 and 107 require revision chain, not flattened final verdict | PASS |
| 4. same scene with different source ID/range | Stage 4 lines 151 and 108 treat same action chain and tension as one scene card | PASS |
| 5. early misreading corrected later | Stage 4 lines 152 and 112 to 122 preserve reading trajectory | PASS |
| 6. external high-like challenge | Stage 4 lines 153 and 110 keep user card as主体, external material as challenge or supplement | PASS |
| 7. external-only strong comment | Stage 4 lines 154 and 127 keep external-only material out of formal-note主体 | PASS |
| 8. light card used as article evidence but not upgraded | Stage 4 lines 155 and 126 preserve light-card status even when article-index linked | PASS |
| 9. final-note bloat prevention / archive-discard-with-reason | Stage 4 lines 156, 130, and 131 preserve `归档不迁移` with readable, non-technical reason | PASS |

## Semantic reread notes

- Router discoverability passes not just on token hits but on actual reading flow. A new session can choose stage first, then open the right file, without reading long copied execution bodies.
- Stage 1 keeps `AI修正` and migration terms only inside Must NOT and QA boundary language. The executable body remains on fetching, matching, output-state recording, and intermediate-draft structure.
- Stage 2 preserves the full literal `提问可以跳远，论证不能偷步`, and it keeps the root-AGENTS toolbox explicit rather than implied.
- Stage 3 keeps `全书收束整合` and `文章素材索引` only as Stage 4 boundary warnings. It does not perform whole-book work.
- Stage 4 keeps `阅读现场档案` before `文章素材索引` both in prose and in the final-note skeleton, which blocks the common failure mode where article navigation swallows the cards.
- The generic router and all four stages remain free of 《人生》 names, IDs, bookIds, and regression sentinels. The only file read here that still contains those book-specific literals is the independent Stage 4 fixture source, which is allowed and was not part of the contamination target set.

Boundary checks:

- This QA task did not edit `微信读书通用提示词.md` or any of the four generic stage files.
- This QA task did not touch any `路遥/人生/**` path.
- This QA task did not edit reading notes, intermediate drafts, formal reading notes, `.omo/run-continuation/*.json`, `.omo/plans/split-weread-prompts-by-stage.md`, `.omo/drafts/split-weread-prompts-by-stage.md`, `decisions.md`, or `problems.md`.
- The only writes are this Task 7 evidence file and one append-only note in `learnings.md`.
- Generated artifact recorded by this task: `/home/king/github/growing-myself/.omo/evidence/task-7-split-weread-prompts-by-stage.md`

PASS:

- GENERIC HARD QA: PASS
- PASS: router discoverability requirements are satisfied, including the exact top index heading, the exact table columns, and links to all four stage files.
- PASS: tracked-router and untracked-safe whitespace checks are all clean.
- PASS: the exact conflict-rule grep returned one valid hit per generic stage file.
- PASS: the exact stale numeric reference grep returned no hits, so there are no unclassified stale numeric section references in the generic router or stages.
- PASS: Markdown links to local generic stage files all resolve to existing targets.
- PASS: all five prompt files have balanced code fences.
- PASS: every stage file contains router path, required pre-read files, router-wins conflict rule, task boundary, Must NOT list, and QA evidence path.
- PASS: stage-boundary integrity holds across Stage 1, Stage 2, Stage 3, and Stage 4.
- PASS: Stage 2 preserves generic and non-fiction cross-genre protection.
- PASS: shortcut routing is coherent for only-organize, consulting/status-check, prompt modification, only-light-card optimization, migration precheck, and whole-book consolidation.
- PASS: Stage 4 references `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` and covers all nine required fixture cases.
- PASS: generic outputs contain no 《人生》 contamination tokens from the required sentinel list.
- PASS: Task 7 gate conditions are met, so Wave 2 may proceed.

Follow-ups / unresolved risks:

- Non-blocking: this gate passes for the current live generic outputs only. If any of the five generic prompt files change later, the gate should be rerun before relying on this PASS.
- Non-blocking: Stage 4 uses a blockquote-form inheritance block instead of a `## 继承块` heading, but the required fields are all present, and the gate criteria only require field presence, not a fixed heading label.
- Non-blocking: the repo remains generally dirty outside this task scope. This gate intentionally stayed inside the approved write set and did not attempt cleanup.
