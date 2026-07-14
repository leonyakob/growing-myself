# add-whole-book-consolidation-model - Work Plan

## TL;DR (For humans)

**What you'll get:** A prompt-update plan that adds a fourth “whole-book consolidation” stage using the model you liked: “阅读现场档案 + 文章素材索引.” The result keeps every card traceable and alive, while building article-ready indexes that cite cards without replacing them.

**Why this approach:** It avoids the false choice between card archive and writing material. The reading-site archive remains the base layer; the article-material index becomes a second-layer navigation system. The plan now separates internal QA ledgers from the formal note and uses a multi-axis ledger so one card can keep its archive identity while serving multiple writing roles.

**What it will NOT do:** It will not edit prompts before your approval, restructure actual notes, fetch WeRead data, erase reading process, dump internal ledgers into formal notes, or turn article indexes into polished AI essays.

**Effort:** Medium
**Risk:** Medium - the main risk is accidental bloat: either the formal note absorbs process metadata, or the article index overwrites the reading-site archive.
**Decisions to sanity-check:** Fourth stage vs extending third stage; internal ledger vs formal output; multi-axis card ledger; “一卡双归宿”; required `.omo/evidence` dry-run fixtures.

Your next move: approve this reviewed plan, or request changes. Implementation will not start until you explicitly approve. Full execution detail follows below.

---

> TL;DR (machine): Add fourth-stage whole-book consolidation rules to generic and 《人生》 WeRead prompts; preserve reading-site archive and add article-material indexes; require fixture-based QA; no target edits before review and approval.

## Review receipts

| reviewer | session | verdict | incorporated changes |
|---|---|---|---|
| Momus | `ses_0a3f599dcffeymD00c5UFTJhR9` | OKAY | Confirmed file path and overall plan are actionable; recommended more literal QA invocations. |
| Oracle | `ses_0a3f5807dffeWIV6VO7Q519CNY` | REJECT before fixes, PASS after fixes | Added multi-axis ledger, artifact boundary rules, fourth-stage non-remigration rule, fixed dry-run fixtures, preservation/usefulness assertions, and bloat controls. Post-fix review confirmed all prior blockers resolved. |
| Metis | `ses_0a3f58101ffeFSXLqj87P2v6mX` | REJECT before fixes, PASS after fixes | Added internal ledger vs formal output separation, source-status branches, readable evidence anchors, expanded duplicate/external-reader branches, corrected-misreading structure, light-card index-only use, final-note skeleton, and fixture requirement. Post-fix review confirmed all prior blockers resolved. |

## Scope

### Must have

- Add a new fourth-stage concept to `微信读书通用提示词.md`: “读完整本书后的全书收束整合.” It must be distinct from the third-stage migration rules.
- Define the canonical model: **阅读现场档案 + 文章素材索引**.
- Define the core principle: **卡片档案为底座，文章素材索引为上层导航**.
- Add “一卡双归宿” rules: every valuable card keeps its reading-site archive identity, and may also be referenced by zero, one, or many article directions.
- Add an explicit artifact boundary:
  - internal consolidation ledger: may contain source IDs, ranges, duplicate decisions, source statuses, processing actions, and QA states;
  - formal reading note: contains readable archive cards and compact article indexes, never verbose processing rows or technical fields;
  - article material index: cites readable card anchors, quote snippets, original user reactions, tensions/problems, and missing-evidence fields.
- Replace the one-dimensional “final state” model with a multi-axis ledger:
  - source status: `已在正式笔记中，结构合格，只补文章索引` / `已在正式笔记中，但需补 readable evidence / 用户原句 / 外部原话` / `中间稿已优化，尚未迁移` / `中间稿与正式稿重复，需合并或建立修订链` / `正式稿旧判断已被后文修正，保留为阅读轨迹` / `仅外部读者材料，无用户卡片锚点` / `来源不足，待回看`;
  - archive disposition: `保留为轻卡` / `保留为完整卡` / `提升为核心卡` / `合并入其他卡` / `归档不迁移` / `待回看`;
  - evidence role: `主题证据` / `人物线证据` / `写法证据` / `阅读轨迹证据`;
  - article links: zero, one, or many article directions;
  - trajectory flags: `早期误读` / `后文修正` / `判断变化`;
  - external-reader relation: `回声` / `补充` / `挑战` / `反向解释` / `独立精彩` / `丢弃并说明理由`.
- Add source-status handling before final material treatment, especially for already-migrated, partially migrated, unmigrated, conflicting, external-only, and insufficient-source materials.
- Add duplicate-resolution rules by source relation and interpretive relation:
  - exact same quote / overlapping quote / same scene / different quote;
  - same insight / corrected judgment / different angle / external echo / external challenge.
- Add corrected-misreading structure: `当时的读法`, `后来出现的证据`, `全书后的修正`, `误读的价值`, `文章索引用法`.
- Add light-card rule: “轻卡被文章索引引用” does not automatically promote it to a complete card; it can remain `轻卡` while serving as气氛证据、语言风格证据、主题回声 or article opening material.
- Add external-reader whole-book branches: duplicate representative, external-only strong material, external challenge correcting overreading, opposed but text-based comments, and weak/chicken-soup discard.
- Add canonical formal-note skeleton for fourth-stage output:

  ```markdown
  ## 全书收束整合

  ### 一、阅读现场档案
  > 保留或补齐卡片本体；已存在且合格的卡片不重复搬运。

  ### 二、文章素材索引
  > 只做导航，不吞掉卡片，不写成文章草稿。

  | 文章方向 | 核心问题 | 关联卡片 readable anchor | 原始触动/用户原句 | 张力 | 可用证据 | 缺失证据 |
  |---|---|---|---|---|---|---|

  ### 三、阅读轨迹与判断变化
  > 只收束真正能说明阅读变化的误读、犹豫、修正，不机械罗列全部过程。

  ### 四、待回看 / 归档不迁移
  > 简短记录原因；详细处理台账留在内部证据，不进入正式稿正文。
  ```

- Add `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` as a required implementation artifact before target prompt edits. It must contain concrete dry-run fixtures.
- Add dry-run QA scenarios with exact input, expected source status, expected archive treatment, expected formal-note treatment, expected article-index treatment, and forbidden failure for at least:
  1. partially migrated card;
  2. duplicate same quote + same insight;
  3. duplicate same quote + changed judgment;
  4. same scene / different source ID or range;
  5. early misreading corrected later;
  6. external high-like challenge;
  7. external-only strong comment;
  8. light card used as article evidence but not upgraded;
  9. final-note bloat prevention / archive-discard-with-reason case.
- Add article-index readable citation shape:

  ```markdown
  - 关联卡片：卡片标题 / 章节或场景 / 引文短句
  - 原始触动：保留我的原句或原句片段
  - 证据作用：它在这个文章方向中承担什么功能
  - 缺口：还缺哪类文本证据或对照材料
  ```

- Add QA failure checks for: source-ID-only article citations, formal note containing technical fields or internal state labels, light cards forcibly expanded, external comments rewritten as user judgment, early misreading silently overwritten, and article index copying full card bodies.
- Apply the same model to `路遥/人生/《人生》微信读书提示词.md` with fixed paths and 《人生》 regression samples preserved.
- Ensure the new section respects existing complex-task planning/review gates: Momus/Metis/Oracle review before execution, explicit authorization before edits.

### Must NOT have (guardrails, anti-slop, scope boundaries)

- Must not edit target prompt files until the reviewed plan is approved by the user.
- Must not call WeRead APIs or alter actual reading notes/middle drafts.
- Must not replace the third-stage migration rules; the fourth stage supplements them after whole-book completion.
- Must not globally re-run third-stage migration or rewrite already-stable cards unless a fixture/state explicitly says the card is missing, duplicated, or semantically wrong.
- Must not collapse reading-site archive and article-material index into one polished essay-like summary.
- Must not dump the internal consolidation ledger into the formal reading note.
- Must not use source IDs/ranges as reader-facing anchors in formal notes or article indexes.
- Must not use source IDs/ranges as the only evidence in article index entries.
- Must not erase shallow early thoughts, misreadings, hesitations, or changing judgments when they reveal the reading trajectory.
- Must not let AI修正 overwrite “我自己写的内容.”
- Must not make external high-like comments authoritative or first-person user judgments.
- Must not force every card into the final formal note; archive/discard-with-reason states are valid.
- Must not force every light card into a complete card when it is only useful as article evidence.
- Must not remove 《人生》 fixed paths or seven regression labels.
- Must not commit/push unless explicitly requested later.

## Verification strategy

> Zero human intervention - all verification is agent-executed.

- Test decision: none; this is Markdown prompt editing. Verification is targeted read-back, full diff review, required/forbidden phrase checks, concrete dry-run fixture comparison, and `git diff --check`.
- Evidence: `.omo/evidence/task-<N>-add-whole-book-consolidation-model.md`
- Fixture: `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`

## Execution strategy

### Parallel execution waves

- Review wave before approval: Momus, Metis, and Oracle must review this plan file. Their blockers must be incorporated into this plan before the user is asked to approve implementation.
- Implementation Wave 0 after approval: create the dry-run fixture under `.omo/evidence/fixtures/` before editing target prompt files.
- Implementation Wave 1: generic prompt and 《人生》 prompt can be edited in parallel only by separate workers touching separate files.
- Final verification wave: independent reviewer validates both prompts against this plan and the dry-run fixture.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 0 | Reviewed plan approved by user | 1, 2, 3, 4, F1-F4 | none |
| 1 | 0 | 3, 4, F1-F4 | 2 |
| 2 | 0 | 3, 4, F1-F4 | 1 |
| 3 | 1, 2 | 4, F1-F4 | none |
| 4 | 1, 2, 3 | F1-F4 | none |

## Todos

- [x] 0. Dry-run fixture: create deterministic whole-book consolidation cases before prompt edits
  What to do / Must NOT do: Create `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`. Include nine concrete safe fixture cases: partially migrated card; duplicate same quote + same insight; duplicate same quote + changed judgment; same scene with different source ID/range; early misreading corrected later; external high-like challenge; external-only strong comment; light card used as article evidence but not upgraded; final-note bloat prevention / archive-discard-with-reason. Each case must include exact input, expected source status, expected archive treatment, expected formal-note treatment, expected article-index treatment, and forbidden failure. Do not edit target prompts in this todo.
  Parallelization: Wave 0 | Blocked by: reviewed plan approved by user | Blocks: 1, 2, 3, 4, F1-F4
  References (executor has NO interview context - be exhaustive): this plan’s Must Have fixture list; existing third-stage QA sections in both target prompts.
  Acceptance criteria (agent-executable): Fixture file exists and contains all nine cases; every case contains headings `输入`, `source status`, `archive treatment`, `formal-note treatment`, `article-index treatment`, and `forbidden failure`; every case includes preservation assertion: archive card still contains `划线原文` + `我自己写的内容` unless the material is external-only and explicitly labeled.
  QA scenarios (name the exact tool + invocation): happy: `read(filePath="/home/king/github/growing-myself/.omo/evidence/fixtures/add-whole-book-consolidation-model.md")` confirms all nine fixture case headings; failure: `GIT_MASTER=1 git grep -n 'source status\|archive treatment\|formal-note treatment\|article-index treatment\|forbidden failure' -- .omo/evidence/fixtures/add-whole-book-consolidation-model.md` must show all required categories. Evidence `.omo/evidence/task-0-add-whole-book-consolidation-model.md`.
  Commit: N | docs(weread): add whole-book consolidation fixtures

- [x] 1. Generic prompt: add fourth-stage whole-book consolidation model
  What to do / Must NOT do: Edit only `微信读书通用提示词.md`. Add a new section after the third-stage migration rules and before/near the large-task strategy, titled like `读完整本书后的全书收束整合` or `第四阶段：全书收束整合`. Define “阅读现场档案 + 文章素材索引” as the default model. Explain that third stage migrates optimized round material, while fourth stage consolidates the whole book after completion. Include: source freeze, internal consolidation ledger vs formal-note output boundary, source-status branches, multi-axis ledger, one-card-two-destinations, reading-site archive structure, article-material index structure, canonical formal-note skeleton, duplicate-resolution decision tree, later-correction/trajectory rules, light-card article-evidence-without-upgrade rule, external-reader material handling, final-note bloat prevention, and fixture-based QA.
  Parallelization: Wave 1 | Blocked by: 0 | Blocks: 3, 4, F1-F4
  References (executor has NO interview context - be exhaustive): `微信读书通用提示词.md:841-968` for third-stage migration rules; `微信读书通用提示词.md:899-906` and `微信读书通用提示词.md:962-968` for formal-note/process-residue QA; `微信读书通用提示词.md:925-936` for all-material destination rules; `微信读书通用提示词.md:1079-1083` for current whole-book style review shortcut; project `AGENTS.md` for preserving user voice, 五异法, 问题阶梯, 张力地图, light/main card distinction, and external-reader boundaries.
  Acceptance criteria (agent-executable): Target file contains `阅读现场档案 + 文章素材索引`, `一卡双归宿`, `全书收束整合`, `内部整合台账`, `文章素材索引只引用卡片，不吞掉卡片`, `source status`, `archive disposition`, and a formal-note skeleton with `阅读现场档案` before `文章素材索引`. The new section distinguishes third stage from fourth stage and says fourth stage must not globally re-run third-stage migration. The section explicitly says original `我自己写的内容` must not be overwritten by AI修正 and source IDs/ranges cannot be reader-facing article anchors.
  QA scenarios (name the exact tool + invocation): happy: `GIT_MASTER=1 git grep -n '阅读现场档案 + 文章素材索引\|一卡双归宿\|内部整合台账\|source status\|archive disposition\|文章素材索引只引用卡片' -- 微信读书通用提示词.md` confirms required model and boundaries; failure: `GIT_MASTER=1 git grep -n '文章素材索引.*替代卡片\|AI修正.*覆盖.*我自己写的内容\|所有轻卡.*完整卡\|source ID.*正式阅读笔记正文\|ID [0-9].*文章方向' -- 微信读书通用提示词.md` must return no bad-rule lines. Evidence `.omo/evidence/task-1-add-whole-book-consolidation-model.md`.
  Commit: N | docs(weread): add whole-book consolidation model

- [x] 2. 《人生》 prompt: add book-specific fourth-stage section without losing paths/regressions
  What to do / Must NOT do: Edit only `路遥/人生/《人生》微信读书提示词.md`. Add a book-specific version of the same fourth-stage model, using fixed paths for the 《人生》中间整理稿 and 《人生》阅读笔记. Preserve the existing third-stage migration rules, fixed paths, and all seven regression labels. Use 《人生》-appropriate wording for人物线、城乡主题、尊严主题、爱情线、知识分子困境、写法线索, but do not overfit the generic prompt to 《人生》. Include the same internal-ledger/formal-output boundary, multi-axis ledger, source-status branches, readable article anchors, and canonical fourth-stage formal-note skeleton.
  Parallelization: Wave 1 | Blocked by: 0 | Blocks: 3, 4, F1-F4
  References (executor has NO interview context - be exhaustive): `路遥/人生/《人生》微信读书提示词.md:820-948` for third-stage migration rules; `路遥/人生/《人生》微信读书提示词.md:876-884` for formal-note process residue boundary; `路遥/人生/《人生》微信读书提示词.md:903-914` for all-material destination rules; `路遥/人生/《人生》微信读书提示词.md:1038-1042` for current whole-book style review shortcut; `路遥/人生/《人生》微信读书提示词.md:1046-1056` for seven regression samples.
  Acceptance criteria (agent-executable): Target file contains `阅读现场档案 + 文章素材索引`, `一卡双归宿`, `全书收束整合`, fixed 《人生》 paths, `内部整合台账`, and `文章素材索引只引用卡片，不吞掉卡片`. All seven labels remain: `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`.
  QA scenarios (name the exact tool + invocation): happy: `GIT_MASTER=1 git grep -n '阅读现场档案 + 文章素材索引\|一卡双归宿\|内部整合台账\|ID 003\|ID 006\|ID 021\|ID 109\|ID 117\|刘玉海救灾处\|黄亚萍的物质付出' -- 路遥/人生/《人生》微信读书提示词.md` confirms model and regression labels; failure: `GIT_MASTER=1 git grep -n '文章素材索引.*替代卡片\|AI修正.*覆盖.*我的原想法\|所有轻卡.*完整卡\|source ID.*正式阅读笔记正文\|ID [0-9].*文章方向' -- 路遥/人生/《人生》微信读书提示词.md` must return no bad-rule lines. Evidence `.omo/evidence/task-2-add-whole-book-consolidation-model.md`.
  Commit: N | docs(ren-sheng): add whole-book consolidation model

- [x] 3. Add shortcut prompts for whole-book consolidation without bypassing gates
  What to do / Must NOT do: In both prompt files, update auxiliary shortcut sections to include a new shortcut for “读完整本书后执行全书收束整合.” This shortcut must say it remains subordinate to task entrance gates, complex-task planning, Momus/Metis/Oracle review, explicit execution authorization, QA, and conditional Git authorization. It must not imply immediate execution or note rewriting. It must explicitly name both layers: reading-site archive first, article-material index second.
  Parallelization: Wave 2 | Blocked by: 1, 2 | Blocks: 4, F1-F4
  References (executor has NO interview context - be exhaustive): `微信读书通用提示词.md:1023-1083`; `路遥/人生/《人生》微信读书提示词.md:998-1042`; existing workflow gate sections in both prompts.
  Acceptance criteria (agent-executable): Both auxiliary sections contain a whole-book consolidation shortcut. The shortcut mentions `阅读现场档案`, `文章素材索引`, and `不抹掉阅读过程` or equivalent. It does not contain wording that bypasses planning/review/authorization.
  QA scenarios (name the exact tool + invocation): happy: targeted reads of both auxiliary sections confirm the shortcut and boundary text; failure: `GIT_MASTER=1 git grep -n '全书收束.*直接执行\|整合.*不需要计划\|文章素材索引.*覆盖原卡\|文章素材索引.*替代阅读现场档案' -- 微信读书通用提示词.md 路遥/人生/《人生》微信读书提示词.md` must return no bad-rule lines. Evidence `.omo/evidence/task-3-add-whole-book-consolidation-model.md`.
  Commit: N | docs(weread): add whole-book shortcut prompt

- [x] 4. Cross-file consistency audit and fixture-based dry-run verification
  What to do / Must NOT do: After todos 0-3, verify that generic and 《人生》 prompts encode the same model while preserving their differences. Use `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` to run dry-run classification for all nine fixture cases. Must NOT rely on user subjective approval as QA.
  Parallelization: Final implementation wave | Blocked by: 0, 1, 2, 3 | Blocks: F1-F4
  References (executor has NO interview context - be exhaustive): all new fourth-stage and shortcut sections in both prompt files; `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git diff --check -- 微信读书通用提示词.md 路遥/人生/《人生》微信读书提示词.md .omo/evidence/fixtures/add-whole-book-consolidation-model.md` exits 0. Every fixture has deterministic source status, archive treatment, formal-note treatment, article-index treatment, and forbidden failure. Both files preserve reading-site archive before article index. Article index does not cite only source IDs/ranges and does not copy full card bodies.
  QA scenarios (name the exact tool + invocation): happy: write/read `.omo/evidence/task-4-add-whole-book-consolidation-model.md` containing the nine fixture outcomes and explicit PASS/FAIL for each; failure: any fixture lacks a deterministic state, allows article index to replace cards, allows formal note to contain technical fields/internal state labels, or allows a light card to be forcibly upgraded. Evidence `.omo/evidence/task-4-add-whole-book-consolidation-model.md`.
  Commit: N | docs(weread): verify whole-book consolidation rules

## Final verification wave

> Runs after all todos. All must approve before completion.

- [x] F1. Plan compliance audit: reviewer confirms every Must Have and Must NOT Have is satisfied in both prompt files.
- [x] F2. Preservation audit: reviewer confirms the model protects `划线原文`, `我自己写的内容`, original card structure, early misreadings/changed judgments, and light-card status.
- [x] F3. Writing-usefulness audit: reviewer confirms article-material index entries require card anchors, quote/evidence cues, original user reaction, tension/problem, internal or cross-work link when available, and missing-evidence/next-step fields.
- [x] F4. Scope fidelity: reviewer confirms no actual reading notes, middle drafts, or unrelated book files were modified, and 《人生》 regression labels remain.
- [x] F5. Fixture audit: reviewer confirms `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` covers all nine scenarios and the implementation evidence records deterministic outcomes.

## Commit strategy

No commit during implementation unless the user explicitly asks after approving and reviewing the final diff. If the user asks to commit implemented prompt changes, default to staging only the two target prompt files. Include `.omo` plan/evidence artifacts only if explicitly requested.

## Success criteria

- Momus, Metis, and Oracle have reviewed this plan file, and blockers are incorporated before implementation approval.
- The generic prompt contains a fourth-stage whole-book consolidation model using “阅读现场档案 + 文章素材索引.”
- The 《人生》 prompt contains the same model with fixed paths and all seven regression labels preserved.
- Both prompts state that card archive comes before article index, and article index cites cards rather than replacing them.
- Both prompts include internal-ledger vs formal-output boundaries and multi-axis ledger handling.
- Both prompts include deterministic state handling for partial migration, duplicates, changed judgments, corrected misreadings, light-card index use without forced upgrade, external-reader challenge, and note-bloat prevention.
- The dry-run fixture exists and verifies nine cases before target prompt edits are considered complete.
- No target prompt edits occur until the reviewed plan is approved.
