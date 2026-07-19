# ren-sheng-stage5-question-compression - Work Plan

## TL;DR (For humans)
<!-- Fill this LAST, after the detailed plan below is written, so it summarizes the REAL plan. -->
<!-- Plain English for a non-engineer: NO file paths, NO todo numbers, NO wave/agent/tool names. -->

**What you'll get:** A fifth-stage whole-book回看 package for 路遥《人生》：把四轮阅读和全书收束材料压缩成 exactly three 可写文章的核心问题。每个问题都会保留你的原始触动，并配证据、反证、张力、细读点和写作路径。

**Why this approach:** 第四阶段已经建好了“阅读现场档案 + 文章素材索引”，但它只是导航；第五阶段要回到原卡片，把问题压缩、排序、反证化，避免把你的活句改成空泛总评。

**What it will NOT do:** 不修改《人生》阅读笔记；不替你伪造原文证据；不把文章素材索引当卡片本体；不把高加林、巧珍、黄亚萍等人物压成单一标签。

**Effort:** Medium
**Risk:** Medium - 主要风险是过度压缩后把你的锋利句子磨平，或把缺少原文复核的判断写得太确定；本计划用活句保护、证据/反证分级和待复核标记控制风险。
**Decisions to sanity-check:** 输出默认只进入最终回复和 `.omo/evidence/ren-sheng-stage5-question-compression/` 证据文件；不改阅读笔记；最终核心问题固定为 3 个；后续真正执行仍需要单独 start-work 入口。

Your next move: after this canonical plan passes Momus + Oracle review, start execution only through the current environment's registered start-work entry if you want Stage 5 content produced. Full execution detail follows below.

---

> TL;DR (machine): Medium effort, medium risk; plan a no-product-edit Stage 5 synthesis that outputs exactly three core questions with evidence/counterevidence, full-book tension map, five-anomaly close reading, writing conversion, Lu Yao method dossier, cross-work links, and strict QA.

## Scope
### Must have

1. Future worker must produce a complete Stage 5 deliverable for 路遥《人生》, not execute anything during this planning/review session.
2. The Stage 5 deliverable must contain exactly three final core questions.
3. Each core question must include:
   - user's original trigger/live sentence;
   - source card/scene anchors;
   - 1-star to 5-star question-ladder upgrade;
   - at least three positive evidence anchors;
   - at least two counterevidence or complication anchors;
   - evidence strength and counterevidence threat ratings;
   - a revised final 5-star expression;
   - `待原文复核` flags when exact original wording is not independently rechecked.
4. The deliverable must include a whole-book tension map grounded in scenes, actions, words, objects, or card anchors.
5. The deliverable must include at least five 五异法 close-reading points, covering all five categories if the existing materials support them: 逻辑反常、情感反常、字词突兀、结构断裂、刻意沉默.
6. The deliverable must include writing conversion in three layers: short notes, theme essays, and long-form/series directions.
7. The deliverable must include a 路遥写法档案 focused on concrete techniques: action, pause, repetition, spatial sense, body/object details, narration/judgment, and moral framing.
8. The deliverable must include cross-work links with comparison path, not just book-name piles.
9. The deliverable must preserve the user's strongest living sentences before analytical revision.
10. The worker must write intermediate evidence under `.omo/evidence/ren-sheng-stage5-question-compression/` so claims can be audited.

### Must NOT have (guardrails, anti-slop, scope boundaries)

1. Must not modify `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` unless the user separately gives an archival update instruction.
2. Must not modify any other reading material, prompt file, or AGENTS file.
3. Must not turn Stage 5 into another Stage 4 consolidation or a repeat of card sorting.
4. Must not let `文章素材索引` replace original cards; every load-bearing claim must trace back to a card/scene anchor.
5. Must not use `source ID`, `range`, `chapterUid`, `bookId`, `ledger`, `snapshot`, `task`, `wave`, or QA-state terms in the final reader-facing Stage 5 output.
6. Must not quote exact novel lines that are not present in the reading note or independently rechecked; use `待原文复核` instead.
7. Must not rewrite user sentences into academic/AI summary voice before preserving them.
8. Must not flatten Gao Jialin into “渣/虚荣/反派”, Qiaozhen into “恋爱脑/牺牲品”, Huang Yaping into “物质/坏”, Kenan into “工具人”, or Deshun into “道德传声筒”.
9. Must not treat external reader comments as user judgments; they can only be 回声、补充、挑战、反向解释 or discarded external material.
10. Must not run Git stage/commit/push.

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none + agent-executed literary QA. This is a reading/writing synthesis task, not code; verification is done through source-ledger checks, table completeness checks, grep/read audits, and adversarial review.
- Evidence root: `.omo/evidence/ren-sheng-stage5-question-compression/`
- Project root for all relative paths in this plan: `/home/king/github/growing-myself`. Any tool invocation that shows `.omo/...` or another relative path is project-root-relative; if a tool requires an absolute path, prefix this project root before running it.
- Source-text classification rule for all downstream work:
  - `用户原句`: text the user wrote in the reading note. Preserve directly and label as user voice.
  - `卡片内小说短语/场景锚点`: novel wording or scene descriptions already present inside the user's reading note. They can anchor analysis, but if used as exact novel quotation without rechecking the book text, mark `待原文复核`.
  - `AI概括`: prior AI评价/修正/补充 in the reading note. May guide analysis, but cannot replace user original feeling or novel/card evidence.
  - `AI自行回忆的小说原文`: prohibited. Do not invent or quote from memory.
- Product-file integrity check: before execution starts, record a read-only baseline using full-repo `git status --short --untracked-files=all` so tracked changes and untracked new files are both visible. After execution, run the same command and compare against the baseline. During Stage 5 execution the only newly allowed changed or untracked paths are under `.omo/evidence/ren-sheng-stage5-question-compression/`; any new, changed, or untracked path outside that evidence directory, including reading notes, prompt files, `AGENTS.md`, or Git state changes, is a failure and must be reverted or explicitly reported before final response. No stage/commit/push is allowed.
- Required evidence files:
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md`
  - `.omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md`
- Reviewer receipts for this plan file are recorded in the draft, not in product notes: `.omo/drafts/ren-sheng-stage5-question-compression.md`.

## Execution strategy
### Parallel execution waves
> Target 5-8 todos per wave. Fewer than 3 (except the final) means you under-split.

- Wave 1, Grounding and extraction: Todos 1-5. Build the source boundary, article-index-to-card map, candidate question pool, live-sentence library, and regression sentinel set. Todo 1 must happen first; Todos 2-5 can run after Todo 1 and can be partially parallelized.
- Wave 2, Compression and analytical scaffolding: Todos 6-9. Select exactly three non-overlapping core questions, build evidence/counterevidence tables, create the tension map, and create 五异法 close-reading points. Todo 6 depends on Todos 2-5; Todos 7-9 depend on Todo 6.
- Wave 3, Writing conversion and finalization: Todos 10-13. Convert questions into writing paths, build Lu Yao method/cross-work dossiers, compose the final output, and run final QA. Todo 12 depends on Todos 6-11; Todo 13 depends on Todo 12.

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2,3,4,5 | none |
| 2 | 1 | 3,6 | 4,5 |
| 3 | 1,2 | 6 | 4,5 |
| 4 | 1 | 6,10,12 | 2,3,5 |
| 5 | 1 | 6,13 | 2,3,4 |
| 6 | 2,3,4,5 | 7,8,9,10,11,12 | none |
| 7 | 6 | 10,12,13 | 8,9 |
| 8 | 6 | 10,11,12,13 | 7,9 |
| 9 | 6 | 10,11,12,13 | 7,8 |
| 10 | 4,6,7,8,9 | 12,13 | 11 |
| 11 | 6,8,9 | 12,13 | 10 |
| 12 | 6,7,8,9,10,11 | 13 | none |
| 13 | 12 | final response | none |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->

- [x] 1. Source/rule preflight: Create the source ledger and output boundary for Stage 5.
  What to do / Must NOT do: Read the root rules, 《人生》 router, Stage 4 prompt, and current reading note headings; create `.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md` listing source hierarchy A-D, exact source paths, key line ranges, and final output boundary. Must NOT edit reading notes or prompt files.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2,3,4,5
  References (executor has NO interview context - be exhaustive): `/home/king/github/growing-myself/AGENTS.md:3-24`, `/home/king/github/growing-myself/AGENTS.md:63-84`, `/home/king/github/growing-myself/AGENTS.md:104-117`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:28-64`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:83-88`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:1-40`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:3-6040`.
  Acceptance criteria (agent-executable): Evidence file exists and contains: `A级 用户原始卡片`, `B级 第四阶段索引`, `C级 提示词规则`, `D级 跨作品联动`; it explicitly states final output must not modify `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`; it defines `用户原句`, `卡片内小说短语/场景锚点`, `AI概括`, and prohibited `AI自行回忆的小说原文`; it records the pre-execution full-repo `git status --short --untracked-files=all` baseline and the only allowed new/changed/untracked execution path `.omo/evidence/ren-sheng-stage5-question-compression/`.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md")` and confirm all four source levels, source-text classification rules, pre-execution full-repo status baseline, allowed-path rule, and no-product-edit boundary are present. failure: use `grep(pattern="修改.*《人生》阅读笔记|写入.*《人生》阅读笔记", path="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression", include="task-01-source-ledger.md", output_mode="content")`; if it suggests modifying the reading note as part of Stage 5, rewrite the boundary. Also run full-repo `git status --short --untracked-files=all`; if any newly changed or untracked path outside `.omo/evidence/ren-sheng-stage5-question-compression/` was caused by the worker, stop and revert/report before continuing. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md`.
  Commit: N | no git commit authorized.

- [x] 2. Stage boundary: Map Stage 4 article index back to original card areas before extracting questions.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md` with a table mapping Stage 4's six article directions to original card ranges and evidence gaps. Must NOT treat Stage 4's article index as enough proof by itself.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 3,6
  References (executor has NO interview context - be exhaustive): `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:146-158`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:131-140`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:185-197`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5932-6040`.
  Acceptance criteria (agent-executable): Evidence table has six rows for 人物线、城乡主题、尊严主题、爱情线、知识分子困境、写法线索; each row has at least two original-card anchors outside `5932-6040`; each row includes `可用证据` and `缺口`.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md")` and count six article-direction rows with original card anchors. failure: use `grep(pattern="5932-6040", path=".omo/evidence/ren-sheng-stage5-question-compression", include="task-02-stage-boundary.md", output_mode="content")`; for every row that uses `5932-6040`, confirm the same row also contains at least two original-card anchors outside that range. If not, go back to original reading-note sections and replace Stage-4-only support with original-card anchors. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md`.
  Commit: N | no git commit authorized.

- [x] 3. Question pool: Extract candidate core questions from all four rounds plus Stage 4 consolidation.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md`. Extract at least 12 candidate questions, each with source round/card, user's original trigger, scene/person, tension, preliminary star level, possible 5-star upgrade, evidence sufficiency, and counterevidence availability. Must NOT choose the final three yet.
  Parallelization: Wave 1 | Blocked by: 1,2 | Blocks: 6
  References (executor has NO interview context - be exhaustive): Round 1 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:13-293`; Round 2 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:567-1207`; Round 3 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1248-1697`; Round 4 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1704-2257`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:2294-5420`; Stage 4 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5932-6040`; question-ladder rule `/home/king/github/growing-myself/AGENTS.md:14-18`, `/home/king/github/growing-myself/AGENTS.md:99-102`.
  Acceptance criteria (agent-executable): Candidate pool contains at least 12 rows; at least three rows are not Gao-Jialin-only; every row has `原始触动`, `场景/人物`, `张力`, `星级`, `5星改写可能`, `证据是否足`, and `反证是否足`.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md")` and verify row count/fields. failure: if fewer than 12 candidates or if all candidates center only on Gao Jialin, reread Qiaozhen/Huang Yaping/Deshun/Kenan sections and add candidates. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md`.
  Commit: N | no git commit authorized.

- [x] 4. Live-sentence library: Preserve the user's strongest original sentences before analysis.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md` with at least 12 user sentences or sentence fragments, including why each has life, how to preserve it, and whether it may be lightly revised. Must NOT replace these with AI-neutral paraphrase.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 6,10,12
  References (executor has NO interview context - be exhaustive): living-sentence rule `/home/king/github/growing-myself/AGENTS.md:7-12`; user-expression preservation `/home/king/github/growing-myself/AGENTS.md:104-112`; known strong sentences include `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:29-36`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:159-174`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:585-591`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1269-1280`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1326-1338`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1916-1918`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5972-5974`.
  Acceptance criteria (agent-executable): Evidence file has at least 12 entries; each entry has `用户原句`, `生命力在哪里`, `保留方式`, `可否微调`; at least four entries preserve anger/口语/文气 rather than smoothing it away.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md")` and verify required fields. failure: if entries are mostly AI paraphrase instead of user original text, return to referenced note lines and replace with exact user fragments. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md`.
  Commit: N | no git commit authorized.

- [x] 5. Regression sentinels: Convert known 《人生》 semantic risks into Stage 5 QA checks.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md` with the seven router sentinels plus Stage 5-specific risks: over-moralizing Gao Jialin, erasing Qiaozhen's agency, flattening Huang Yaping's real costs, treating Deshun as only moral mouthpiece, and using cross-work links as name piles. Must NOT make these sentinels mandatory content in every final question; use them as QA samples.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 6,13
  References (executor has NO interview context - be exhaustive): `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:221-231`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:253-282`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5993-6040`.
  Acceptance criteria (agent-executable): Evidence file lists at least 12 sentinel checks; each has `risk`, `source`, `failure pattern`, and `required Stage 5 check`.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md")` and verify seven router sentinels plus Stage 5 risks. failure: if any sentinel instructs the worker to force unrelated content into the final output, revise it into a QA check only. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md`.
  Commit: N | no git commit authorized.

- [x] 6. Core-question selection: Select exactly three non-overlapping 5-star questions.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md` and select exactly three final questions from the pool. Include why each is selected, why near-duplicates are rejected, and a non-overlap proof. Must NOT select three questions that are all just versions of “高加林为什么失败/虚荣/负心”.
  Parallelization: Wave 2 | Blocked by: 2,3,4,5 | Blocks: 7,8,9,10,11,12
  References (executor has NO interview context - be exhaustive): candidate pool evidence from Todo 3; Stage 4 six directions `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5943-5991`; question quality rules `/home/king/github/growing-myself/AGENTS.md:86-102`; root analysis tools `/home/king/github/growing-myself/AGENTS.md:14-18`.
  Acceptance criteria (agent-executable): Exactly three final questions; each has `用户原始触动`, `覆盖方向`, `至少3个原卡锚点`, `至少2个潜在反证`, `5星问题表达`; table includes `rejected near-duplicates` with reasons; at least one question foregrounds a non-Gao-Jialin center or relationship/structure/writing problem.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md")` and verify exactly three selected rows and reject ledger. failure: if selected rows overlap by more than two primary evidence anchors or have the same central claim, merge/rewrite until distinct. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md`.
  Commit: N | no git commit authorized.

- [x] 7. Evidence/counterevidence: Build a graded evidence and反证 table for each selected question.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md`. For each of the three questions, add positive evidence, counterevidence/complications, strength/threat ratings, and how the final judgment changes. Must NOT force evidence to support the first draft if counterevidence weakens it.
  Parallelization: Wave 2 | Blocked by: 6 | Blocks: 10,12,13
  References (executor has NO interview context - be exhaustive): selected questions from Todo 6; original anchors from `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:13-293`, `567-1207`, `1248-1697`, `1704-2257`, `2294-5420`, `5932-6040`; counterevidence reminders from `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1590-1604`, `1834-1843`, `1978-1985`, `2029-2059`, `6029-6034`.
  Acceptance criteria (agent-executable): Three tables exist; each table has at least three positive evidence anchors, at least two counterevidence/complication anchors, strength values `强/中/弱`, threat values `高/中/低`, and a `判断如何修正` field; any non-rechecked exact quotation has `待原文复核`.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md")` and verify each of three questions has required evidence/counterevidence counts. failure: if a question has no meaningful counterevidence, return to question selection and replace or narrow it. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md`.
  Commit: N | no git commit authorized.

- [x] 8. Tension map: Build a whole-book 张力地图 tied to scenes and cards.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md` with at least eight tensions. Each must include opposing forces, scene/card anchors, persons involved, whether tension resolves or remains suspended, and which final question it serves. Must NOT list abstract pairs like `城乡/爱情/命运` without scene anchors.
  Parallelization: Wave 2 | Blocked by: 6 | Blocks: 10,11,12,13
  References (executor has NO interview context - be exhaustive): 张力地图 rule `/home/king/github/growing-myself/AGENTS.md:14-24`; Stage 4 article tensions `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5943-5991`; likely tension anchors `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:46-54`, `185-195`, `606-612`, `1292-1301`, `1360-1367`, `1413-1419`, `1890-1898`, `1928-1937`, `2078-2087`, `5993-6040`.
  Acceptance criteria (agent-executable): At least eight tension rows; every row has concrete scene/card anchor, not only theme labels; rows collectively cover Gao Jialin, Qiaozhen, Huang Yaping, Deshun/Kenan or another non-triangle figure, and social structure.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md")` and verify eight anchored rows. failure: if a row's evidence cell lacks a readable scene/card anchor, replace the row or add the anchor before continuing. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md`.
  Commit: N | no git commit authorized.

- [x] 9. Five-anomaly close reading: Produce at least five 五异法 points serving the three questions.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md`. Include at least one point for each 五异法 category if supported by the notes; each point must show the anomaly, why it matters, what question it serves, and what needs original-text复核. Must NOT turn 五异法 into generic labels without explaining the anomaly.
  Parallelization: Wave 2 | Blocked by: 6 | Blocks: 10,11,12,13
  References (executor has NO interview context - be exhaustive): 五异法 rule `/home/king/github/growing-myself/AGENTS.md:14-18`; likely anchors: `索性/刷牙/保密` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:159-194`; `履历表` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:573-610`; `有时` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1427-1458` and `1612-1628`; `乡巴佬` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1742-1773`; `两个人都有点兴奋` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1784-1814`; `让我好好想一想` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:1866-1898`; `痛不欲生/下不了台` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:2024-2050`; `苗/根/土/豆芽菜` `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:2061-2087`; method line `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5985-5991`.
  Acceptance criteria (agent-executable): At least five close-reading rows; all rows have `类别`, `异常处`, `为什么异常`, `服务哪个核心问题`, `文本复核状态`; the evidence file includes a five-category checklist for `逻辑反常`, `情感反常`, `字词突兀`, `结构断裂`, `刻意沉默`; each category is either supported by at least one anchored point or explicitly marked `材料不足` with reason; no row consists only of theme summary.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md")` and verify the five-category checklist plus anchored explanations. failure: if a category lacks either an anchored point or a `材料不足` reason, revise the file; if a category cannot be supported, mark `材料不足` with reason instead of fabricating a point, then add a supported extra point in another category if total rows fall below five. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md`.
  Commit: N | no git commit authorized.

- [x] 10. Writing conversion: Turn the three questions into short-note, theme-essay, and long-form paths.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md`. For each final question, propose at least one short note, one theme essay, and one longer/series direction with title, center question, usable cards, evidence, counterevidence, and danger point. Must NOT write full essays or over-polish into finished prose.
  Parallelization: Wave 3 | Blocked by: 4,6,7,8,9 | Blocks: 12,13
  References (executor has NO interview context - be exhaustive): writing/cross-work rules `/home/king/github/growing-myself/AGENTS.md:86-102`; live-sentence library from Todo 4; core questions from Todo 6; evidence tables from Todo 7; article directions `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5943-5991`; reading trajectory `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5993-6040`.
  Acceptance criteria (agent-executable): Evidence file contains three grouped sections, one per final question; each section has `短札`, `主题文章`, `长文/系列`; each proposed direction has title, center question, card anchors, key evidence, possible counterevidence, and danger point.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md")` and verify three-layer writing paths for all questions. failure: if any path lacks danger point or counterevidence, add it before composing final output. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md`.
  Commit: N | no git commit authorized.

- [x] 11. Method/cross-work: Build Lu Yao writing-method dossier and comparison paths.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md`. Include at least six Lu Yao technique observations and at least five cross-work comparison paths. Must NOT use generic terms like “现实主义很深刻” unless grounded in a concrete technique and card anchor.
  Parallelization: Wave 3 | Blocked by: 6,8,9 | Blocks: 12,13
  References (executor has NO interview context - be exhaustive): project writer-driven reading aim `/home/king/github/growing-myself/AGENTS.md:3-5`; cross-work requirements `/home/king/github/growing-myself/AGENTS.md:95-102`; Stage 4 writing-line anchors `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5985-5991`; method-heavy cards `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:338-399`, `496-504`, `998-1029`, `1550-1576`, `1612-1628`, `1784-1814`, `1866-1898`, `2061-2087`; cross-work anchors embedded throughout `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:94-98`, `133-137`, `193-195`, `289-293`, `611-612`, `1366-1367`, `1418-1419`, `1895-1898`, `2011-2013`, `2085-2087`.
  Acceptance criteria (agent-executable): At least six method observations, each with technique + card anchor + what it reveals; at least five comparison paths, each with source work/person, compared dimension, and how it advances the original 《人生》 question; no item is only a book-name list.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md")` and verify technique/anchor/comparison fields. failure: if any method item is abstract praise without technique, replace it with a card-grounded observation. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md`.
  Commit: N | no git commit authorized.

- [x] 12. Final output: Compose the Stage 5 deliverable without editing product notes.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md` and use it as the source for the final response. The output must be in Chinese and organized for reading/writing use, not as a technical log. It must include a natural reader-facing `自检与可靠性说明` section that states what is solid, what counterevidence complicates, and what remains `待原文复核` without exposing `.omo` mechanics. Must NOT expose `.omo` task language, source IDs, range coordinates, book IDs, or QA machinery in the final reader-facing response.
  Parallelization: Wave 3 | Blocked by: 6,7,8,9,10,11 | Blocks: 13
  References (executor has NO interview context - be exhaustive): all prior evidence files; final output rules from `/home/king/github/growing-myself/AGENTS.md:7-24`, `/home/king/github/growing-myself/AGENTS.md:86-102`; no-archive-edit rule `/home/king/github/growing-myself/AGENTS.md:104-117`; Stage 4 final consolidation `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5932-6040`.
  Acceptance criteria (agent-executable): Final output contains these top-level sections: `三个核心问题`, `每题证据-反证表`, `全书张力地图`, `五异法细读点`, `写作转化`, `路遥写法档案`, `跨作品联动`, `待原文复核清单`, `自检与可靠性说明`; it preserves at least one user original sentence/trigger per core question before analysis; it distinguishes user original sentence from AI revision or analytical compression; it uses only natural card/scene anchors in reader-facing sections; it does not mention internal todo/wave/task mechanics; the final response to the user must be based on this file, not only stored silently.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md")` and verify all required sections, exactly three core-question headings, at least one user original sentence per question, and the reader-facing self-check section. failure: use `grep(pattern="source ID|range|chapterUid|bookId|ledger|snapshot|task|wave|QA state", path=".omo/evidence/ren-sheng-stage5-question-compression", include="task-12-final-output.md", output_mode="content")`; any match in reader-facing content must be removed or rewritten as natural Chinese. Use `grep(pattern="^#{1,4} .*核心问题|^\s*[一二三四五六七八九十]+、.*核心问题|^\s*[0-9]+[.、].*核心问题", path=".omo/evidence/ren-sheng-stage5-question-compression", include="task-12-final-output.md", output_mode="content")` and confirm exactly three core-question entries, with all other writing directions labeled `子问题` or `写作支路`, not extra core questions. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md`.
  Commit: N | no git commit authorized.

- [x] 13. Final QA: Audit the Stage 5 output against guardrails and report pass/fail evidence.
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md` with a checklist and corrections. Must NOT declare Stage 5 complete if any core question lacks counterevidence, any live sentence is overwritten, or any unsupported exact quotation remains unflagged.
  Parallelization: Final wave prep | Blocked by: 12 | Blocks: final response
  References (executor has NO interview context - be exhaustive): root guardrails `/home/king/github/growing-myself/AGENTS.md:7-24`, `/home/king/github/growing-myself/AGENTS.md:86-112`; router plan/QA gates `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:55-64`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:221-231`; Stage 4 QA `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:269-282`; final output from Todo 12.
  Acceptance criteria (agent-executable): QA file has explicit pass/fail rows for: exactly three questions; no hidden fourth/fifth core question in writing directions; evidence counts; counterevidence counts; non-overlap; every load-bearing claim traces to original card/scene anchors rather than Stage-4-only support; tension map anchors; five-anomaly anchors; five-anomaly category checklist with `材料不足` reasons when needed; live-sentence preservation; user original sentence vs AI revision distinction; no fake evidence; no product-file edits; no external-reader voice pollution; no technical fields in reader-facing output; no flattening of key figures; all `待原文复核` items listed; final response delivered/summarized from Todo 12.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md")` and verify all rows pass or have corrected action, then run full-repo `git status --short --untracked-files=all` and confirm any newly changed or untracked paths caused by the worker are only under `.omo/evidence/ren-sheng-stage5-question-compression/`. failure: if any QA row fails, patch the relevant evidence/final-output file and rerun this QA before final response; if any worker-caused changed or untracked path outside `.omo/evidence/ren-sheng-stage5-question-compression/` exists, revert/report the unauthorized edit before final response. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md`.
  Commit: N | no git commit authorized.

## Final verification wave
> Runs after ALL todos. ALL must APPROVE. For this no-product-edit Stage 5 task, completion means the worker delivers the final response plus evidence; do not ask the user for extra approval unless proposing an out-of-scope action such as editing the reading note, changing prompts, or running Git stage/commit/push.

- [x] F1. Plan compliance audit
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f1-plan-compliance.md` and verify the executed Stage 5 output follows this plan exactly. Must NOT accept a worker self-report without checking evidence files.
  References (executor has NO interview context - be exhaustive): this plan `## Scope`, `## Todos`, `## Success criteria`; Todo evidence files 1-13; final output `.omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md`; QA `.omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md`.
  Acceptance criteria (agent-executable): F1 evidence confirms every required evidence file exists, exactly three core questions are present, required final sections exist, all Todo 13 QA rows pass, and no final-output section is missing.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/final-verification-f1-plan-compliance.md")` plus `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md")` and confirm F1 verdict is APPROVE. failure: if any required evidence file or section is missing, mark F1 REJECT, create/repair the missing artifact, and rerun F1. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f1-plan-compliance.md`.
  Commit: N | no git commit authorized.

- [x] F2. Code quality review
  What to do / Must NOT do: Adapt this check as analysis/writing quality review. Create `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f2-analysis-quality.md` and verify the output is concrete, text-grounded, preserves user voice, uses 五异法/问题阶梯/张力地图, and avoids generic praise/moralizing. Must NOT judge by polish alone.
  References (executor has NO interview context - be exhaustive): `/home/king/github/growing-myself/AGENTS.md:3-24`, `/home/king/github/growing-myself/AGENTS.md:86-102`, live-sentence library from Todo 4, evidence/counterevidence from Todo 7, final output from Todo 12.
  Acceptance criteria (agent-executable): F2 evidence confirms each core question has user voice preserved, text/card anchors, counterevidence, and a 5-star writing-grade formulation; no key figure is flattened into a single moral label; writing-method and cross-work sections have concrete comparison/technique paths.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/final-verification-f2-analysis-quality.md")` and confirm F2 verdict is APPROVE with cited examples from the final output. failure: if any section uses generic claims such as `现实主义很深刻` without technique/card anchor, or replaces user voice with AI paraphrase, mark F2 REJECT and patch Todo 12 final output. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f2-analysis-quality.md`.
  Commit: N | no git commit authorized.

- [x] F3. Real manual QA
  What to do / Must NOT do: Adapt this as agent-simulated reader QA. Create `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f3-reader-qa.md`; read the final output as the user would and verify it can directly guide writing without opening internal evidence files. Must NOT require human confirmation to pass.
  References (executor has NO interview context - be exhaustive): final output from Todo 12; writing conversion from Todo 10; method/cross-work from Todo 11; final-output rules in Todo 12.
  Acceptance criteria (agent-executable): F3 evidence confirms the final response is understandable as a reader-facing Stage 5 deliverable, contains a natural `自检与可靠性说明`, does not leak `.omo` mechanics or technical IDs, and clearly distinguishes core questions from subquestions/writing branches.
  QA scenarios (name the exact tool + invocation): happy: use `read(filePath=".omo/evidence/ren-sheng-stage5-question-compression/final-verification-f3-reader-qa.md")` and confirm F3 verdict is APPROVE. failure: use `grep(pattern="\.omo|source ID|range|chapterUid|bookId|ledger|snapshot|task|wave|QA state", path=".omo/evidence/ren-sheng-stage5-question-compression", include="task-12-final-output.md", output_mode="content")`; if any technical leakage remains in reader-facing prose, patch Todo 12 final output and rerun F3. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f3-reader-qa.md`.
  Commit: N | no git commit authorized.

- [x] F4. Scope fidelity
  What to do / Must NOT do: Create `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md` and verify the worker did not execute unauthorized archival edits, prompt edits, Git stage/commit/push, external-data expansion, or cross-book note reading beyond existing anchors. Must NOT silently accept dirty product-file changes.
  References (executor has NO interview context - be exhaustive): no-edit rules `/home/king/github/growing-myself/AGENTS.md:104-117`; router gates `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:55-64`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:127-133`; Scope/Must NOT in this plan; source ledger from Todo 1.
  Acceptance criteria (agent-executable): F4 evidence includes the read-only command result for full-repo `git status --short --untracked-files=all` before and after execution; it confirms any newly changed or untracked paths caused by the worker are only under `.omo/evidence/ren-sheng-stage5-question-compression/`, and confirms no unauthorized product-file diffs, no `AGENTS.md` diffs, no prompt-file diffs, no Git stage/commit/push, and no out-of-scope external expansion.
  QA scenarios (name the exact tool + invocation): happy: run full-repo `git status --short --untracked-files=all` and compare against the pre-execution baseline; record that any worker-caused changed or untracked paths are only under `.omo/evidence/ren-sheng-stage5-question-compression/`; use `read(filePath="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md")` to confirm F4 APPROVE. failure: if any product file, prompt file, `AGENTS.md`, or other non-evidence path was modified or newly created by the worker, revert/report the unauthorized diff/untracked path and mark F4 REJECT until clean; if external/cross-book expansion occurred beyond existing anchors, remove that material and rerun F4. Evidence `.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md`.
  Commit: N | no git commit authorized.

## Commit strategy

- No Git stage, commit, or push is authorized by this plan.
- If the user later explicitly asks for Git, a separate git-aware step must first inspect `git status` and stage only user-authorized files.
- Evidence files under `.omo/evidence/ren-sheng-stage5-question-compression/` are execution artifacts; product reading notes remain untouched unless separately authorized.

## Success criteria

1. Stage 5 execution produces exactly three core questions for 《人生》, each upgraded to a 5-star question with clear writing value.
2. Every selected question is backed by at least three positive evidence anchors and at least two counterevidence/complication anchors.
3. Evidence does not rely only on Stage 4 article-index summary; it traces back to original cards/scenes.
4. The final output preserves the user's living sentences and only improves them after identifying why they work.
5. The full-book tension map contains at least eight anchored tensions and covers人物、主题、社会结构、写法.
6. 五异法 close reading contains at least five anchored points, includes a five-category coverage checklist, marks unsupported categories as `材料不足` with reasons, and does not fabricate unsupported exact text.
7. Writing conversion gives usable short-note, essay, and long-form directions with danger points.
8. Lu Yao method dossier is technique-grounded, not generic “现实主义” praise.
9. Cross-work links explain comparison paths and what each comparison advances.
10. `待原文复核` is used wherever precise wording or source text needs rechecking.
11. No product reading material, prompt file, or Git history is modified during Stage 5 unless the user separately authorizes it.
12. Momus and Oracle review receipts for this canonical plan are recorded before this plan is handed off as reviewed.
13. The final reader-facing output includes `自检与可靠性说明` and makes clear which judgments are strongest, which are complicated by counterevidence, and which require original-text recheck.
14. All load-bearing final claims trace to original card/scene anchors; Stage 4 is never the only evidence for a central claim.
