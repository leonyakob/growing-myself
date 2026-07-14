# split-weread-prompts-by-stage - Work Plan

## TL;DR (For humans)

**What you'll get:** 两份微信读书提示词会被拆成“总入口 + 四个阶段执行提示词”：先拆通用提示词，确认没丢规则、没断引用后，再拆《人生》专用提示词。

**Why this approach:** 通用提示词是所有书目的底座，必须先拆好；《人生》含固定路径、双 bookId、主题方向和 7 个回归样本，必须在通用拆分通过后再继承同一结构，避免两边一起漂移。

**What it will NOT do:** 不整理微信读书材料，不改《人生》中间稿或正式阅读笔记，不提交运行时临时文件。

**Effort:** Medium
**Risk:** Medium - 主要风险是拆分后跨文件引用失效、阶段边界变软、书目专属回归样本丢失。
**Decisions to sanity-check:** 阶段文件采用“原总文件名 + 阶段后缀”的同目录命名；总入口保留权威规则和路由，阶段文件作为可复制执行工单；通用 QA 未通过不得进入《人生》拆分。

Your next move: review the amended plan summary and approve it for a later execution session, or request further changes. Full execution detail follows below.

---

> TL;DR (machine): Medium-risk Markdown prompt architecture split; sequential Wave 1 generic router/stages, hard QA gate, Wave 2 《人生》 router/stages, final cross-reference/regression QA.

## Scope

### Must have

#### Critical preflight gates added by Momus / Metis / Oracle review

1. **This plan is not execution authorization.** Do not run any split todo while the current user request is review, planning, audit, or plan improvement. Execution may begin only after review receipts are recorded, all `CHANGES_REQUIRED` items are resolved or explicitly waived, the amended plan is presented, and the user explicitly authorizes execution through the currently registered start-work entry for this client.
2. **Immutable source snapshots before rewrite.** Before changing either router source, create verbatim snapshots under `.omo/evidence/split-weread-prompts-by-stage/source/`:
   - `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
   - `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
   Immediately after creating each `*.before.md` snapshot and before any router rewrite, run and record `sha256sum "<live-source>" "<snapshot>"`, `wc -l "<live-source>" "<snapshot>"`, and `cmp -s "<live-source>" "<snapshot>" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'`. If this records `FAIL` or is missing, stop before rewrite. Record sha256, line count, heading inventory, target-file existence, and applicable `AGENTS.md` files. Downstream todos must use these snapshots or the verbatim move ledger, not the mutable router after rewrite. Treat live router paths as targets/outputs only after rewrite begins.
3. **Applicable AGENTS rules.** Generic router/stage prompts must require reading `/home/king/github/growing-myself/AGENTS.md` only. 《人生》 router/stage prompts must require reading `/home/king/github/growing-myself/AGENTS.md`, plus `/home/king/github/growing-myself/路遥/人生/AGENTS.md` only if that same-book file exists at execution time. Do not import sibling-book rules such as `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md`, and do not require the 《人生》 AGENTS file from generic prompts.
4. **Chinese hard-constraint preservation.** Every source sentence containing hard/normative language such as `必须`, `不得`, `不能`, `不要`, `只有`, `除非`, `优先`, `默认`, `若`, `如`, `不默认`, `不得替代`, `不能覆盖`, `禁止`, `严禁`, `只能`, `不可`, `务必`, `仍需`, `须`, or `需` must be preserved verbatim in the router/stage target or listed in evidence with a deliberate paraphrase justification. The ledger is not limited to this token list: any sentence controlling authorization, preservation, scope, sequencing, Git, QA, or source-original handling must be mapped or explicitly justified.
5. **No grep-only success.** Keyword searches are discovery aids only. Every task evidence file must include heading coverage, per-token PASS/FAIL rows for required terms, at least three exact-source-rule preservation samples, and read-based semantic QA notes.
6. **Untracked-file-safe verification.** Plain `git grep` and `git diff --check` are insufficient for newly created untracked stage/evidence files. Use `git grep --untracked` for literal searches and a no-index or equivalent whitespace check for new files.
7. **Router discoverability.** Each router must begin with `## 阶段文件索引（先选阶段）`, using a table with `用户意图 / 应打开的文件 / 允许产出 / 禁止事项`; links must be valid Markdown links that resolve to exact existing stage files.
8. **Structured evidence is mandatory.** Every task evidence file must contain: `Source snapshot used:`, `Applicable AGENTS.md:`, `Files changed:`, `Commands run:`, `Read-based QA notes:`, `Boundary checks:`, `PASS:` or `FAIL:`, and `Follow-ups / unresolved risks:`. Final verification fails if any planned evidence file is missing, empty, or lacks `PASS:`.
9. **Runtime artifact and dirty-worktree baseline.** At execution start, before creating snapshots, stage files, or rewriting routers, and before any evidence besides the baseline entries, capture both `GIT_MASTER=1 git status --short --untracked-files=all` and `GIT_MASTER=1 git status --short --untracked-files=all -- .omo/run-continuation`; write the captured outputs into `.omo/evidence/task-1-split-weread-prompts-by-stage.md` without letting the evidence-file creation affect the captured baseline. Always write the run-continuation baseline command output to `.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`: `GIT_MASTER=1 git ls-files -z --cached --others --exclude-standard -- .omo/run-continuation | LC_ALL=C sort -z | xargs -0 -r sha256sum > .omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`. If the manifest file is zero bytes, additionally record `RUN_CONTINUATION_BASELINE: EMPTY_OR_ABSENT` in Task 1 evidence. The manifest file must exist in both non-empty and empty cases. Also create `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256` before any planned output write. It must hash `.omo/plans/split-weread-prompts-by-stage.md` and `.omo/drafts/split-weread-prompts-by-stage.md` if they exist at execution start, plus any pre-existing dirty path that the user explicitly approves as baseline and that is not one of this plan's execution outputs or `.omo/run-continuation`. Record the exact protected path list in Task 1 evidence. At final verification, recreate the manifest from the recorded protected path list and compare it with `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256` using `cmp -s`; any difference is a failure. This is required because unchanged `git status --short --untracked-files=all` output is not proof that an already-dirty or already-untracked file was not edited. If the full baseline contains pre-existing dirty paths outside this plan/draft and `.omo/run-continuation`, stop for user review unless the user explicitly approves that baseline. At final verification, compare against the execution-start full-status baseline: non-baseline new/modified paths must be limited to planned prompt/evidence/snapshot outputs. Do not edit, delete, stage, or commit continuation artifacts unless the user explicitly asks. All final changed-file allow-list checks must use `GIT_MASTER=1 git status --short --untracked-files=all` so untracked files inside new directories cannot be hidden behind a directory entry.

- Preserve the existing two source prompts as the authoritative roots to be split:
  - `/home/king/github/growing-myself/微信读书通用提示词.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
- The live-source line anchors in this Scope section are planning-time orientation only. During execution, Todo 1 and Todo 8 may read the live source only to create their immutable `*.before.md` snapshots; every rewrite/stage todo after that must use the relevant snapshot and move ledger as its only source material.
- Wave 1 generic split outputs:
  - `/home/king/github/growing-myself/微信读书通用提示词.md` as router / authority / index
  - `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md`
  - `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md`
- Wave 2 《人生》 split outputs:
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` as router / authority / index
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- Every stage file must begin with an inheritance block:
  - applicable router path;
  - stage purpose;
  - required pre-read files, including root `AGENTS.md`, same-book `AGENTS.md` if present, and the router;
  - exact input files and output files;
  - conflict rule: if this stage prompt conflicts with the router, the router wins;
  - task boundary and Must NOT list;
  - QA evidence path for execution.
- Generic router must retain or summarize as authority:
  - core goals and evidence layer boundary from `微信读书通用提示词.md:5` to `微信读书通用提示词.md:12`;
  - placeholder/path rules from `微信读书通用提示词.md:16` to `微信读书通用提示词.md:27`;
  - non-degradation / task entry gate from `微信读书通用提示词.md:29` to `微信读书通用提示词.md:40`;
  - book-specific prompt generation boundary from `微信读书通用提示词.md:44` to `微信读书通用提示词.md:66`;
  - four-stage flow from `微信读书通用提示词.md:69` to `微信读书通用提示词.md:93`;
  - multi-round rules from `微信读书通用提示词.md:98` to `微信读书通用提示词.md:119`;
  - stage QA and conditional Git rules from `微信读书通用提示词.md:122` to `微信读书通用提示词.md:153`;
  - complex-task planning gate from `微信读书通用提示词.md:1109` to `微信读书通用提示词.md:1157`;
  - shortcut-template warning and regression-sample sedimentation mechanism from `微信读书通用提示词.md:1160` to `微信读书通用提示词.md:1236`.
- Generic stage files must receive detailed stage material:
  - Stage 1: data fetching, matching, color/category/type and intermediate draft format from `微信读书通用提示词.md:157` to `微信读书通用提示词.md:355`, plus `微信读书通用提示词.md:572` to `微信读书通用提示词.md:657`.
  - Stage 2: literary analysis quality and optimization rules from `微信读书通用提示词.md:358` to `微信读书通用提示词.md:569`, plus `微信读书通用提示词.md:661` to `微信读书通用提示词.md:843`.
  - Stage 3: migration, precheck, formal-note structure, cursor, material destination and anti-regression QA from `微信读书通用提示词.md:846` to `微信读书通用提示词.md:974`.
  - Stage 4: whole-book consolidation model and QA from `微信读书通用提示词.md:977` to `微信读书通用提示词.md:1106`.
- 《人生》 router must retain or summarize as authority:
  - fixed paths from `路遥/人生/《人生》微信读书提示词.md:5` to `路遥/人生/《人生》微信读书提示词.md:9`;
  - core goals from `路遥/人生/《人生》微信读书提示词.md:11` to `路遥/人生/《人生》微信读书提示词.md:18`;
  - task entry gate from `路遥/人生/《人生》微信读书提示词.md:22` to `路遥/人生/《人生》微信读书提示词.md:31`;
  - four-stage flow from `路遥/人生/《人生》微信读书提示词.md:34` to `路遥/人生/《人生》微信读书提示词.md:59`;
  - multi-round rules from `路遥/人生/《人生》微信读书提示词.md:63` to `路遥/人生/《人生》微信读书提示词.md:84`;
  - stage QA and Git rules from `路遥/人生/《人生》微信读书提示词.md:87` to `路遥/人生/《人生》微信读书提示词.md:124`;
  - known personal import bookId and official bookId mapping from `路遥/人生/《人生》微信读书提示词.md:213` to `路遥/人生/《人生》微信读书提示词.md:219`;
  - complex-task planning gate from `路遥/人生/《人生》微信读书提示词.md:1159` to `路遥/人生/《人生》微信读书提示词.md:1202`;
  - shortcut warning from `路遥/人生/《人生》微信读书提示词.md:1205` to `路遥/人生/《人生》微信读书提示词.md:1255`;
  - all 7 known regression risks from `路遥/人生/《人生》微信读书提示词.md:1259` to `路遥/人生/《人生》微信读书提示词.md:1269`.
- 《人生》 stage files must receive detailed stage material:
  - Stage 1: `路遥/人生/《人生》微信读书提示词.md:127` to `路遥/人生/《人生》微信读书提示词.md:325`, plus `路遥/人生/《人生》微信读书提示词.md:540` to `路遥/人生/《人生》微信读书提示词.md:633`.
  - Stage 2: `路遥/人生/《人生》微信读书提示词.md:328` to `路遥/人生/《人生》微信读书提示词.md:537`, plus `路遥/人生/《人生》微信读书提示词.md:637` to `路遥/人生/《人生》微信读书提示词.md:822`.
  - Stage 3: `路遥/人生/《人生》微信读书提示词.md:825` to `路遥/人生/《人生》微信读书提示词.md:954`.
  - Stage 4: `路遥/人生/《人生》微信读书提示词.md:957` to `路遥/人生/《人生》微信读书提示词.md:1156`.
- Replace stale numeric section references such as “第 11 节”, “第 13.2 节”, or “§11.1” with file-aware references using file names and stable section titles.
- Update the generic prompt-generation rule so future book-specific prompt generation creates a book-specific router plus four stage prompts, not a single old-format专用提示词 file.
- Explicitly map every shortcut template to router-only, a relevant stage file, or intentional duplication.
- Record task evidence under `.omo/evidence/task-<N>-split-weread-prompts-by-stage.md`.

### Must NOT have (guardrails, anti-slop, scope boundaries)

- Do not execute the split in the planning session; execution belongs to a later explicitly started work session.
- Do not edit reading materials, including:
  - `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`
  - other book folders or other reading notes.
- Do not create, edit, stage, or commit `.omo/run-continuation/*.json`.
- Do not remove user wording, source quotations, external-reader boundaries, QA gates, Git authorization gates, or complex-task review gates for brevity.
- Do not collapse four stages into one mega stage prompt.
- Do not let stage files override the router. Stage files may elaborate; the router remains authority.
- Do not copy 《人生》 examples, bookIds, paths, article directions, or regression samples into the generic prompt as generic truth.
- Do not rewrite the start-work instruction as `/shared/start-work`; use “the currently registered start-work entry for this client,” with `/start-work <plan-name>` and `$start-work <plan-name>` only as environment examples.
- Do not commit unless the user explicitly asks. If asked, inspect `GIT_MASTER=1 git status`, `GIT_MASTER=1 git diff`, and `GIT_MASTER=1 git log --oneline -10`; stage only plan-approved files.
- Do not overwrite any pre-existing target stage file unless the source snapshot / target-existence evidence proves it is plan-created or the user explicitly authorizes replacing it.

## Verification strategy

> Zero human intervention - all verification is agent-executed.

- Test decision: none + Markdown structural QA and prompt-surface manual QA. This is documentation/prompt architecture; no code test suite applies.
- Evidence: `.omo/evidence/task-<N>-split-weread-prompts-by-stage.md` plus `.omo/evidence/final-review-split-weread-prompts-by-stage.md`.
- Command rule: any literal search over new stage/evidence files must use one literal token at a time, e.g. `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- <files>`, or an equivalent per-file literal-token checker. A pattern like `A\|B\|C` is not sufficient by exit code; evidence must include one PASS/FAIL row for each required token.
- Whitespace rule: use `GIT_MASTER=1 git diff --check -- <tracked-modified-router-files>` for tracked rewritten routers. For untracked new stage/evidence files, run an untracked-file-safe whitespace check such as `GIT_MASTER=1 git diff --no-index --check /dev/null "<new-file>"` and record whether output contains whitespace errors; do not rely on plain `git diff --check` to inspect untracked files.
- Markdown rule: router QA must validate exact target existence, valid Markdown links, relative link resolution, and balanced code fences for every router/stage prompt. A raw filename grep hit is not enough.
- Semantic coverage rule: no task may pass on keyword hits alone. Evidence must include a heading coverage table mapping every assigned source heading to target heading/router summary, three exact-source-rule preservation samples, one positive dry-run scenario, and one boundary/failure dry-run scenario.
- Required checks:
  - `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- <changed-prompt-files>` and classify every hit as `local-valid`, `source-quote-only`, or `failure`. Do not use the default BRE form of this pattern; evidence must record the exact command including `-E`.
  - Per-token check for `CB_2tb79r78T38k74M75h8iz4C3` and `25164497` across the 《人生》 router and Stage 1 prompt; each token needs its own PASS row.
  - Per-token check for `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, and `黄亚萍的物质付出` in the 《人生》 router; each sentinel needs its own PASS row.
  - Generic contamination QA: generic router/stage outputs must not contain `高加林`, `巧珍`, `黄亚萍`, `刘玉海`, the two 《人生》 bookIds, or 《人生》 regression sample IDs unless explicitly marked as anti-contamination examples.
  - Agent-executed prompt-surface dry-run QA by reading each router and each stage file as a new-session entry prompt and recording: required pre-reads, exact input/output files, task boundary, Must NOT list, QA evidence path, whether file edits/Git are authorized, and the correct route for `只整理`, `只评价问题质量`, `只优化轻卡`, `提示词修改`, `状态检查`, and `全书收束整合`.

## Execution strategy

### Parallel execution waves

- Wave 1: Generic split only. Create/update the generic router and four generic stage files. No 《人生》 files are touched in this wave.
- Hard QA gate: Generic split must pass cross-reference, content-preservation, and prompt-surface QA before Wave 2 begins.
- Wave 2: 《人生》 split only. Reuse the generic architecture, preserve book-specific facts, and add 《人生》 regression checks.
- Final verification wave: run independent reviews after both waves.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2, 3, 4, 5, 6 | none |
| 2 | 1 | 7 | 3, 4, 5, 6 after 1 |
| 3 | 1 | 7 | 2, 4, 5, 6 after 1 |
| 4 | 1 | 7 | 2, 3, 5, 6 after 1 |
| 5 | 1 | 7 | 2, 3, 4, 6 after 1 |
| 6 | 1 | 7 | 2, 3, 4, 5 after 1 |
| 7 | 2, 3, 4, 5, 6 | 8, 9, 10, 11, 12, 13 | none |
| 8 | 7 | 9, 10, 11, 12, 13, 14 | none |
| 9 | 8 | 14 | 10, 11, 12, 13 after 8 |
| 10 | 8 | 14 | 9, 11, 12, 13 after 8 |
| 11 | 8 | 14 | 9, 10, 12, 13 after 8 |
| 12 | 8 | 14 | 9, 10, 11, 13 after 8 |
| 13 | 8 | 14 | 9, 10, 11, 12 after 8 |
| 14 | 8, 9, 10, 11, 12, 13 | final verification | none |

## Todos

> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->

- [x] 1. Generic source map and move ledger
  What to do / Must NOT do: Create the immutable generic source snapshot `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md` before any rewrite. Immediately after snapshot creation and before any router rewrite, run and record `sha256sum "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"`, `wc -l "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"`, and `cmp -s "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'`. Create `.omo/evidence/task-1-split-weread-prompts-by-stage.md` with that verbatim proof, sha256, line count, heading inventory, target-file existence preflight, applicable `AGENTS.md` files, and a move ledger mapping every generic source heading/subheading to exactly one disposition: generic router, generic Stage 1, generic Stage 2, generic Stage 3, generic Stage 4, intentional duplication, or explicit out-of-scope stop. Must include all line ranges listed in Scope, map every shortcut template, and include a Chinese hard-constraint preservation ledger for sentences containing `必须/不得/不能/不要/只有/除非/优先/默认/若/如/不默认/不得替代/不能覆盖/禁止/严禁/只能/不可/务必/仍需/须/需` plus any other sentence controlling authorization, preservation, scope, sequencing, Git, QA, or source-original handling. Must NOT omit shortcut templates, cross-genre caveats, or regression-sample sedimentation rules.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2, 3, 4, 5, 6
  References (pre-snapshot source-map anchors only; later generic todos must use the snapshot): `微信读书通用提示词.md:1`, `微信读书通用提示词.md:29`, `微信读书通用提示词.md:69`, `微信读书通用提示词.md:157`, `微信读书通用提示词.md:358`, `微信读书通用提示词.md:572`, `微信读书通用提示词.md:846`, `微信读书通用提示词.md:977`, `微信读书通用提示词.md:1109`, `微信读书通用提示词.md:1160`, `微信读书通用提示词.md:1230`.
  Acceptance criteria (agent-executable): evidence file contains headings `Source snapshot used:`, `Applicable AGENTS.md:`, `Heading inventory`, `Router`, `Stage 1`, `Stage 2`, `Stage 3`, `Stage 4`, `Duplicated inheritance blocks`, `Shortcut template map`, `Normative-language preservation ledger`, `PASS:`; every heading/subheading from the snapshot inventory has exactly one disposition; any unexpected new heading or unmapped snapshot heading is `FAIL` and stops execution for plan/user review; snapshot sha256, line count, and `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS` are recorded. Evidence must also contain `EXECUTION_START_FULL_STATUS_BASELINE:`, `EXECUTION_START_RUN_CONTINUATION_STATUS_BASELINE:`, `RUN_CONTINUATION_SHA256_BASELINE:`, `PROTECTED_BASELINE_SHA256:`, the exact baseline command strings containing `--untracked-files=all`, the protected baseline path list, and `BASELINES_CAPTURED_BEFORE_PLANNED_OUTPUTS: PASS`. The protected baseline path list must explicitly include `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md` and `/home/king/github/growing-myself/.omo/drafts/split-weread-prompts-by-stage.md` if they exist at execution start. It must also include every pre-existing dirty path that the user explicitly approved as baseline and that is not one of this plan's execution outputs or `.omo/run-continuation`. Missing any required protected path is `FAIL`, even if the later manifest comparison passes. Missing baseline evidence or a baseline captured after any snapshot/evidence/stage/router write is `FAIL`.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` the evidence file and snapshot, verify all headings exist, and record three exact hard-constraint source sentences plus their target disposition; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- ".omo/evidence/task-1-split-weread-prompts-by-stage.md"` once per stale-reference literal (`第 13.2 节`, `第 11 节`, `§11`) and ensure every hit is classified as `source-quote-only`, not target wording. Evidence `.omo/evidence/task-1-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 2. Generic router rewrite
  What to do / Must NOT do: Rewrite `/home/king/github/growing-myself/微信读书通用提示词.md` into the generic router using the immutable snapshot from Todo 1, not the mutable post-rewrite file. Keep title, purpose, core goals, placeholder/path rules, non-degradation gate, book-specific prompt generation rules, four-stage routing table, multi-round rules, stage-transition QA, conditional Git rules, complex-task planning gate, shortcut-template warning, and regression-sample sedimentation mechanism. Update the “如何生成专用提示词” rule so future books generate a book-specific router plus four stage prompts, not the old single-file format. Add `## 阶段文件索引（先选阶段）` at the top with valid Markdown links to the four generic stage files. Must NOT retain long duplicated stage execution bodies after they move, unless retained as router-level summary or authority rule.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:5`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:16`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:29`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:44`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:69`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:98`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:122`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1109`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1160`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1230`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词.md"` once per required token: `阶段文件索引（先选阶段）`, `微信读书通用提示词-第一阶段-生成中间整理稿.md`, `微信读书通用提示词-第二阶段-优化中间整理稿.md`, `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md`, `微信读书通用提示词-第四阶段-全书收束整合.md`; evidence contains one PASS row per token plus Markdown link-resolution results.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` the router and answer the route table for first/second/third/fourth-stage, only-organize, only-consulting, prompt-modification, and new book-specific prompt generation; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词.md"` once per forbidden universal-command literal (`/shared/start-work`, `裸 start-work`, `/start work`) and confirm any hit is not presented as a universal user instruction. Evidence `.omo/evidence/task-2-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 3. Generic Stage 1 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md` as a self-contained execution prompt for generating intermediate drafts. Use the Todo 1 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, task entry rules, API/data boundaries, matching rules, official/public bookId mapping rules for generic books, color default flow, idea categories, card types, Stage 1 execution template, intermediate draft format, and Stage 1 QA. Must NOT include deep literary optimization or formal-note migration as Stage 1 work.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:157`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:164`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:189`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:233`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:303`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:332`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:572`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:594`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"` once per required token: `/book/bookmarklist`, `/review/list/mine`, `/book/readreviews`, `颜色默认流向`, `想法类别`, `卡片判断`, `下次接着整理位置`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 1 prompt and verify it says first stage only organizes, lightly pre-classifies, fetches/sifts external-reader candidates, and writes the intermediate draft; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md"` once per boundary-sensitive literal (`AI修正`, `正式阅读笔记才是长期`, `迁移到正式阅读笔记`) and classify every hit as `boundary-only OK` or `forbidden instruction FAIL`. Evidence `.omo/evidence/task-3-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 4. Generic Stage 2 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md` from the generic source snapshot as a self-contained execution prompt for optimizing intermediate drafts. Use the Todo 1 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, literary analysis quality rules, pre-optimization diagnosis, light-card rules, complete/main-card rules, pending-material rules, external-reader difference analysis, Stage 2 QA, and the project literary-analysis toolbox from `/home/king/github/growing-myself/AGENTS.md`: 五异法扫描、问题阶梯（1星-5星）、张力地图、轻卡/主卡边界、细节卡从具体往抽象、主题卡从抽象往具体落、提问可以跳远，论证不能偷步、保留有生命力的句子、文本落点、另一个角度、扩写方向与跨作品联动路径. This AGENTS-derived toolbox is allowed source material despite the snapshot-only rule and must be recorded under `Applicable AGENTS.md`. Preserve the generic cross-genre caveat: literary works emphasize words/actions/psychology/narrative; non-fiction emphasizes concepts/argument/evidence/structure/rhetoric/implicit premises. Must NOT write to the formal reading note or make generic rules novel-only.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:358`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:366`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:385`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:412`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:425`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:489`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:530`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:661`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:677`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:719`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:747`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:807`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:822`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"` once per required token: `文学分析质量规则`, `本轮优化前诊断`, `AI轻评`, `AI修正`, `当前回答（沿原问题）`, `同位置其他书友高赞想法分析`, `五异法扫描`, `问题阶梯（1星-5星）`, `张力地图`, `轻卡/主卡边界`, `细节卡从具体往抽象`, `主题卡从抽象往具体落`, `提问可以跳远，论证不能偷步`, `保留有生命力的句子`, `文本落点`, `另一个角度`, `扩写方向与跨作品联动路径`; evidence contains one PASS row per token. Evidence must contain one PASS row for the full combined AGENTS phrase `提问可以跳远，论证不能偷步`; substring-only matches are insufficient.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 2 prompt and verify it preserves original user thoughts, writes AI material below them, preserves AGENTS literary toolbox items, and preserves the cross-genre caveat; failure: `GIT_MASTER=1 git grep --untracked -E -n '请写入：.*正式阅读笔记|更新到.*正式阅读笔记' -- "微信读书通用提示词-第二阶段-优化中间整理稿.md"` returns no Stage 3 execution instruction. Evidence `.omo/evidence/task-4-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 5. Generic Stage 3 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` as a self-contained execution prompt for migration. Use the Todo 1 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, migration trigger, pre-migration source checklist, formal note structure, cursor update, material destination rules, external-reader migration rules, and post-migration anti-regression QA. Must NOT perform fourth-stage whole-book consolidation.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:846`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:869`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:879`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:918`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:930`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:943`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:963`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"` once per required token: `迁移前回源预检`, `正式阅读笔记结构`, `下次接着整理位置`, `所有材料最终都要有归宿`, `迁移后防回归 QA`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 3 prompt and verify it requires `划线原文 / 我自己写的内容 / AI评价 / AI修正 / AI补充` and inherits AGENTS source-original preservation; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md"` once per Stage 4 boundary literal (`全书收束整合`, `文章素材索引`) and confirm every hit is only a boundary statement saying not to run Stage 4. Evidence `.omo/evidence/task-5-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 6. Generic Stage 4 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md` as a self-contained execution prompt for whole-book consolidation. Use the Todo 1 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, Stage 3/4 boundary, internal ledger vs. formal note boundary, multi-axis ledger, one-card-two-destinations, reading-site archive before article-material index, duplicate/misreading rules, light-card/external-reader anti-bloat rules, and fixture-based QA. Must NOT globally rerun Stage 3.
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 7
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:977`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:981`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:983`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:992`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1000`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1015`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1033`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1056`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1071`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1083`, `.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md:1093`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "微信读书通用提示词-第四阶段-全书收束整合.md"` once per required token: `阅读现场档案 + 文章素材索引`, `卡片档案为底座，文章素材索引为上层导航`, `内部整合台账`, `多轴`, `一卡双归宿`, `fixture`, `归档不迁移`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 4 prompt and `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`, then record all nine fixture cases in evidence; failure: `GIT_MASTER=1 git grep --untracked -E -n '全局重跑第三阶段|文章素材索引.*替代卡片|AI修正.*覆盖.*我自己写的内容' -- "微信读书通用提示词-第四阶段-全书收束整合.md"` must classify every hit as `boundary-only OK` or `forbidden instruction FAIL`. Evidence `.omo/evidence/task-6-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 7. Generic hard QA gate
  What to do / Must NOT do: Verify the generic router and four generic stage files before any 《人生》 file is touched. Audit cross-references, valid Markdown links, balanced code fences, conflict rules, target-existence preflight, applicable AGENTS evidence, absence of stale numeric section references, stage boundary integrity, generic/non-fiction cross-genre protection, shortcut routing, no 《人生》 contamination, and fixture coverage for Stage 4. Must NOT proceed to Wave 2 if any generic QA item fails.
  Parallelization: Hard QA gate | Blocked by: 2, 3, 4, 5, 6 | Blocks: 8, 9, 10, 11, 12, 13
  References (executor has NO interview context - be exhaustive): all generic output files listed in Scope; `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`.
  Acceptance criteria (agent-executable): tracked-router whitespace check plus untracked-safe whitespace checks for four stage files report no whitespace errors; evidence file says `GENERIC HARD QA: PASS` and contains per-file heading coverage, per-token PASS rows, Markdown link validation, code-fence validation, and no-contamination results.
  QA scenarios (name the exact tool + invocation): happy: run `GIT_MASTER=1 git grep --untracked -E -n "若.*总提示词.*冲突.*总提示词为准|如果.*总提示词.*冲突.*总提示词为准" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"` and record one PASS row per stage file; failure: run `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "微信读书通用提示词.md" "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"` and classify every hit; also run generic contamination QA against 《人生》 names/bookIds/sample IDs. Evidence `.omo/evidence/task-7-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split generic prompt by stage

- [x] 8. 《人生》 source map and book-specific preservation ledger
  What to do / Must NOT do: Create immutable source snapshot `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md` before rewriting the 《人生》 router. Immediately after snapshot creation and before any router rewrite, run and record `sha256sum "路遥/人生/《人生》微信读书提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`, `wc -l "路遥/人生/《人生》微信读书提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`, and `cmp -s "路遥/人生/《人生》微信读书提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'`. Create `.omo/evidence/task-8-split-weread-prompts-by-stage.md` with that verbatim proof, sha256, line count, heading inventory, target-file existence preflight, applicable `AGENTS.md` files, and a move ledger mapping every 《人生》 source heading/subheading to exactly one disposition: 《人生》 router, 《人生》 Stage 1, 《人生》 Stage 2, 《人生》 Stage 3, 《人生》 Stage 4, intentional duplication, or explicit out-of-scope stop. Also list book-specific facts that must stay in the router and be inherited by all stage prompts: fixed paths, bookId mapping, book-specific literary examples, article directions, and 7 regression samples. Include hard-constraint preservation ledger and shortcut template map. Must NOT copy these into the generic prompt or import sibling-book `AGENTS.md` rules.
  Parallelization: Wave 2 | Blocked by: 7 | Blocks: 14
  References (pre-snapshot source-map anchors only; later 《人生》 todos must use the snapshot): `路遥/人生/《人生》微信读书提示词.md:1`, `路遥/人生/《人生》微信读书提示词.md:5`, `路遥/人生/《人生》微信读书提示词.md:22`, `路遥/人生/《人生》微信读书提示词.md:34`, `路遥/人生/《人生》微信读书提示词.md:127`, `路遥/人生/《人生》微信读书提示词.md:213`, `路遥/人生/《人生》微信读书提示词.md:328`, `路遥/人生/《人生》微信读书提示词.md:540`, `路遥/人生/《人生》微信读书提示词.md:825`, `路遥/人生/《人生》微信读书提示词.md:957`, `路遥/人生/《人生》微信读书提示词.md:1259`.
  Acceptance criteria (agent-executable): evidence file contains `Source snapshot used:`, `Applicable AGENTS.md:`, `Heading inventory`, all seven labels `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`, both bookIds, shortcut template map, normative-language ledger, `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`, and `PASS:`. Every heading/subheading from the snapshot inventory must have exactly one disposition; any unexpected new heading or unmapped snapshot heading is `FAIL` and stops execution for plan/user review.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` evidence and snapshot, confirm router/stage mapping and target existence; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"` once per required preservation literal (`CB_2tb79r78T38k74M75h8iz4C3`, `25164497`, `ID 003`, `黄亚萍的物质付出`) and record one PASS row per token. Evidence `.omo/evidence/task-8-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 9. 《人生》 router rewrite
  What to do / Must NOT do: Rewrite `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` into the 《人生》 router using the Todo 8 snapshot, not the mutable post-rewrite file. Keep fixed paths, core goals, task entry gate, four-stage routing table, multi-round rules, stage QA and conditional Git rules, bookId mapping, complex-task planning gate, shortcut warnings, Stage 4 article-direction summary, and all 7 regression samples. Add `## 阶段文件索引（先选阶段）` with valid Markdown links to the four 《人生》 stage files. Must NOT remove book-specific examples by treating the generic router as sufficient.
  Parallelization: Wave 2 | Blocked by: 8 | Blocks: 14
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:5`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:11`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:22`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:34`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:87`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:213`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1048`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1159`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1205`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1259`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词.md"` once per required token: `阶段文件索引（先选阶段）`, `《人生》微信读书提示词-第一阶段-生成中间整理稿.md`, `《人生》微信读书提示词-第二阶段-优化中间整理稿.md`, `《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md`, `《人生》微信读书提示词-第四阶段-全书收束整合.md`; evidence contains one PASS row per token plus Markdown link-resolution results.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` router and confirm it can route all four stages plus only-consulting/status-check and shortcut requests; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词.md"` once per sentinel token (`ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`) and record one PASS row per token. Evidence `.omo/evidence/task-9-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 10. 《人生》 Stage 1 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` as the 《人生》 Stage 1 execution prompt. Use the Todo 8 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, fixed paths, personal import bookId, official public bookId, import-to-official matching workflow, data fetching, color/type/card rules, Stage 1 template, and intermediate draft format. Must NOT do deep optimization or migration.
  Parallelization: Wave 2 | Blocked by: 8 | Blocks: 14
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:127`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:134`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:159`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:203`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:213`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:273`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:302`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:540`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:564`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"` once per required token: `CB_2tb79r78T38k74M75h8iz4C3`, `25164497`, `/book/bookmarklist`, `/review/list/mine`, `/book/readreviews`, `第N轮整理`, `外部读者精彩高赞想法候选`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 1 and confirm only first-stage organization is authorized; failure: `GIT_MASTER=1 git grep --untracked -E -n 'AI修正|迁移到.*正式阅读笔记|全书收束整合' -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md"` must classify every hit as `boundary-only OK` or `forbidden instruction FAIL`. Evidence `.omo/evidence/task-10-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 11. 《人生》 Stage 2 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` as the 《人生》 Stage 2 execution prompt. Use the Todo 8 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, fixed intermediate path, book-specific literary analysis examples, pre-optimization diagnosis, light-card rules, complete/main-card rules, pending-material rules, and external-reader high-like idea analysis. Also include the project literary-analysis toolbox from `/home/king/github/growing-myself/AGENTS.md`: 五异法扫描、问题阶梯（1星-5星）、张力地图、轻卡/主卡边界、细节卡从具体往抽象、主题卡从抽象往具体落、提问可以跳远，论证不能偷步、保留有生命力的句子、文本落点、另一个角度、扩写方向与跨作品联动路径. This AGENTS-derived toolbox is allowed source material despite the snapshot-only rule and must be recorded under `Applicable AGENTS.md`. Must NOT write to formal note.
  Parallelization: Wave 2 | Blocked by: 8 | Blocks: 14
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:328`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:366`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:380`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:391`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:459`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:500`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:527`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:637`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:653`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:695`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:723`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:801`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"` once per required token: `高加林`, `巧珍`, `强烈`, `不知为什么`, `本轮优化前诊断`, `AI轻评`, `AI修正`, `当前回答（沿原问题）`, `外部读者高赞想法分析`, `五异法扫描`, `问题阶梯（1星-5星）`, `张力地图`, `轻卡/主卡边界`, `细节卡从具体往抽象`, `主题卡从抽象往具体落`, `提问可以跳远，论证不能偷步`, `保留有生命力的句子`, `文本落点`, `另一个角度`, `扩写方向与跨作品联动路径`; evidence contains one PASS row per token. Evidence must contain one PASS row for the full combined AGENTS phrase `提问可以跳远，论证不能偷步`; substring-only matches are insufficient.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 2 and verify it keeps user original thoughts unchanged, adds AI material below, and preserves AGENTS literary toolbox items; failure: `GIT_MASTER=1 git grep --untracked -E -n '请把 .* 正式阅读笔记|更新到 /home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md' -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"` must return no Stage 3 execution instruction. Evidence `.omo/evidence/task-11-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 12. 《人生》 Stage 3 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` as the 《人生》 Stage 3 execution prompt. Use the Todo 8 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, fixed input/output paths, migration trigger, pre-migration checklist, formal note structure, cursor update, material destination rules, external-reader migration rules, and post-migration QA. Must NOT run whole-book consolidation.
  Parallelization: Wave 2 | Blocked by: 8 | Blocks: 14
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:825`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:848`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:858`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:896`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:908`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:921`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:941`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"` once per required token: `迁移前回源预检清单`, `正式阅读笔记结构`, `正式阅读笔记游标更新规则`, `所有材料最终都要有归宿`, `外部读者精彩高赞想法迁移规则`, `迁移后防回归 QA`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 3 and confirm formal-note technical-field prohibition is explicit and AGENTS source-original preservation is inherited; failure: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md"` once per Stage 4 boundary literal (`全书收束整合`, `文章素材索引`) and confirm every hit is only a boundary statement saying not to run Stage 4. Evidence `.omo/evidence/task-12-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 13. 《人生》 Stage 4 prompt
  What to do / Must NOT do: Create `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` as the 《人生》 Stage 4 execution prompt. Use the Todo 8 immutable snapshot and move ledger as the only source material; treat the live router path as target/output only after rewrite begins. Include inheritance block, fixed input/output paths, Stage 3/4 boundary, internal ledger, multi-axis ledger, one-card-two-destinations, reading-site archive and article-material index structure, 《人生》 article-direction table, duplicate/misreading rules, external-reader bloat rules, and fixture QA. Must NOT globally rerun Stage 3.
  Parallelization: Wave 2 | Blocked by: 8 | Blocks: 14
  References (executor has NO interview context - be exhaustive): `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:957`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:974`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:987`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:997`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1025`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1038`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1048`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1067`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1083`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1122`, `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md:1134`.
  Acceptance criteria (agent-executable): run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"` once per required token: `阅读现场档案`, `文章素材索引`, `人物线`, `城乡主题`, `尊严主题`, `爱情线`, `知识分子困境`, `写法线索`, `内部整合台账`, `一卡双归宿`, `fixture`; evidence contains one PASS row per token.
  QA scenarios (name the exact tool + invocation): happy: `functions.read` Stage 4 and `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`, then record all nine fixture cases; failure: `GIT_MASTER=1 git grep --untracked -E -n '全局重跑第三阶段|文章素材索引.*替代卡片|AI修正.*覆盖.*我的原想法|source ID.*文章方向锚点' -- "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"` must classify every hit as `boundary-only OK` or `forbidden instruction FAIL`. Evidence `.omo/evidence/task-13-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

- [x] 14. 《人生》 hard QA gate
  What to do / Must NOT do: Verify the 《人生》 router and four 《人生》 stage files. Audit cross-references, stage links, conflict rules, fixed paths, bookIds, regression samples, article directions, stage boundaries, and fixture QA. Must NOT mark the split complete until all 《人生》 regression sample checks pass.
  Parallelization: Wave 2 QA | Blocked by: 8, 9, 10, 11, 12, 13 | Blocks: final verification
  References (executor has NO interview context - be exhaustive): all 《人生》 output files listed in Scope; `.omo/evidence/fixtures/add-whole-book-consolidation-model.md`.
  Acceptance criteria (agent-executable): tracked-router whitespace check plus untracked-safe whitespace checks for four stage files report no whitespace errors; evidence file says `LIFE HARD QA: PASS` and contains per-file heading coverage, per-token PASS rows, Markdown link validation, code-fence validation, fixed path/bookId/regression sample validation, and contamination isolation results.
  QA scenarios (name the exact tool + invocation): happy: run `GIT_MASTER=1 git grep -F --untracked -n "<literal-token>" -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"` once per required sentinel/bookId (`CB_2tb79r78T38k74M75h8iz4C3`, `25164497`, `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出`) and record one PASS row per token with router plus relevant inherited references; failure: `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- "路遥/人生/《人生》微信读书提示词.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"` must classify every hit. Evidence `.omo/evidence/task-14-split-weread-prompts-by-stage.md`.
  Commit: N | docs(weread): split life prompt by stage

## Final verification wave

> Final verification is a two-step gate, not a single parallel write. F2-F5 checks may be investigated in parallel, but their results must be merged serially into named `F2`, `F3`, `F4`, and `F5` sections of `.omo/evidence/final-review-split-weread-prompts-by-stage.md`; F1 runs last after those sections exist and must fail if any section is missing, incomplete, or not `PASS:`. ALL must APPROVE. Surface results and wait for the user's explicit okay before declaring complete.

- [x] F1. Final compliance aggregator (runs after F2-F5)
  - After F2-F5 have completed and their results have been serially merged into named `F2`, `F3`, `F4`, and `F5` sections of `.omo/evidence/final-review-split-weread-prompts-by-stage.md`, read `.omo/plans/split-weread-prompts-by-stage.md` and only this plan's evidence files: `.omo/evidence/task-{1..14}-split-weread-prompts-by-stage.md` and `.omo/evidence/final-review-split-weread-prompts-by-stage.md`. Do not apply this plan's structured evidence schema to unrelated `.omo/evidence/**` files. Check the two source snapshots and the Stage 4 fixture only through the explicit snapshot/fixture rules below.
  - Confirm every planned output exists, no unplanned reading material changed, and Wave 2 evidence starts only after generic hard QA says PASS.
  - Structured evidence schema / `PASS:` requirements apply only to `.omo/evidence/task-*-split-weread-prompts-by-stage.md` and `.omo/evidence/final-review-split-weread-prompts-by-stage.md`.
  - Immutable source snapshots, fixture files, `.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`, and `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256` are exempt from structured evidence schema checks. Instead, confirm both `*.before.md` snapshots exist, Task 1 and Task 8 evidence each include `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`, and snapshot sha256 / line counts match Task 1 and Task 8 evidence; fixture files are checked only for existence and Stage 4 references; the run-continuation and protected-baseline manifests are checked only through F5 baseline comparison. Do not claim a snapshot is verbatim solely by comparing the post-rewrite snapshot hash to evidence.
  - Fail if any structured evidence file is missing, empty, lacks the mandatory schema, lacks `PASS:`, lacks source snapshot references, lacks required `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`, has unresolved `FAIL:` / `Follow-ups` items, or if `.omo/evidence/final-review-split-weread-prompts-by-stage.md` lacks completed named `F2`, `F3`, `F4`, and `F5` sections each containing `PASS:`.
- [x] F2. Cross-reference and stale-section review
  - Run untracked-safe numeric section-reference grep across all 10 prompt outputs using exactly `GIT_MASTER=1 git grep --untracked -E -n '第[[:space:]]*[0-9]+(\.[0-9]+)?[[:space:]]*节|§[0-9]+(\.[0-9]+)?' -- <changed-prompt-files>`.
  - Confirm every remaining numeric reference is classified as local-valid, source-quote-only, or failure.
  - Validate Markdown links resolve relative to routers, target files exist, and code fences are balanced.
- [x] F3. Agent-executed prompt-surface dry-run QA
  - Use the routers and stage files as a user would in a fresh session: read each router, then select the correct stage file for first-stage organization, second-stage optimization, third-stage migration, fourth-stage whole-book consolidation, only-organize shortcut, only-consulting/status-check, prompt-modification, `只评价问题质量`, `只优化轻卡`, and `全书收束整合` tasks.
  - For each scenario, record required pre-reads, exact input/output files, task boundary, Must NOT list, QA evidence path, and whether file edits/Git are authorized.
  - Record observed routing in `.omo/evidence/final-review-split-weread-prompts-by-stage.md`.
- [x] F4. Regression and fixture review
  - Confirm `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` is referenced by both Stage 4 prompts.
  - Confirm 《人生》 7 regression samples remain in the router and are mentioned as inherited sentinels by relevant stage prompts.
  - Confirm generic outputs have no 《人生》 contamination and 《人生》 outputs preserve fixed paths, bookIds, article directions, and stage-relevant sentinel pointers.
- [x] F5. Scope fidelity and Git hygiene
  - Run `GIT_MASTER=1 git status --short --untracked-files=all`.
  - Compare the result with the execution-start full-status baseline. Ignoring paths that were already present in that baseline and remain unchanged in scope, any new/modified execution paths must be limited to the two routers, eight stage prompts, `.omo/evidence/task-*split-weread-prompts-by-stage.md`, `.omo/evidence/final-review-split-weread-prompts-by-stage.md`, the two immutable source snapshots under `.omo/evidence/split-weread-prompts-by-stage/source/*.before.md`, `.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`, and `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256`, unless the user explicitly approved more.
  - Compare final `GIT_MASTER=1 git status --short --untracked-files=all -- .omo/run-continuation` with the execution-start continuation status baseline, then compare the regenerated run-continuation sha256 manifest with the baseline using `cmp -s <(GIT_MASTER=1 git ls-files -z --cached --others --exclude-standard -- .omo/run-continuation | LC_ALL=C sort -z | xargs -0 -r sha256sum) ".omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256"`. A zero-row final manifest must compare equal to a zero-byte baseline manifest. Any status or manifest difference is a failure, even if the affected continuation artifact was already dirty or untracked at baseline. Do not delete or edit pre-existing continuation artifacts unless the user explicitly asks.
  - Before recreating the protected-baseline manifest, verify that the recorded protected path list contains the two plan/draft paths if they existed at execution start, plus every user-approved dirty non-output path. If any required protected path is absent from the recorded list, F5 is `FAIL` before `cmp -s`. Recreate the protected-baseline sha256 manifest from the protected path list recorded in Task 1 evidence and compare it with `.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256` using `cmp -s`; any difference is a failure, even if `GIT_MASTER=1 git status --short --untracked-files=all` is unchanged.

## Commit strategy

- Default: no commit. This plan does not authorize commit or push.
- If the user explicitly asks for a commit after execution and that instruction explicitly overrides the project default in `AGENTS.md` that normally restricts staging/committing to `AGENTS.md` files:
  1. run `GIT_MASTER=1 git status --short --untracked-files=all`;
  2. run `GIT_MASTER=1 git diff -- <planned files>`;
  3. run `GIT_MASTER=1 git log --oneline -10`;
  4. stage only planned prompt/evidence files, including immutable source snapshots;
  5. run `GIT_MASTER=1 git diff --cached --name-only` and `GIT_MASTER=1 git diff --cached --check`;
  6. commit with a concise docs-style message such as `docs(weread): split prompts by stage`.
- Never stage or commit `.omo/run-continuation/*.json` unless explicitly requested.

## Success criteria

- The generic router plus four generic stage prompts exist and pass the generic hard QA gate.
- The 《人生》 router plus four 《人生》 stage prompts exist and pass the 《人生》 hard QA gate.
- Every stage file can be used as a new-session execution prompt but explicitly inherits from its router.
- No stage file weakens core goals, evidence boundaries, source-original preservation, external-reader boundaries, Git authorization gates, complex-task planning gates, or stage-transition QA.
- No stale cross-file numeric section references remain.
- 《人生》 fixed paths, both bookIds, six Stage 4 article directions, and all 7 regression risks are preserved.
- Fourth-stage fixture-based QA is still required by both Stage 4 prompts.
- Agent-executed prompt-surface dry-run QA demonstrates that a real user can open either router and be routed to the correct stage prompt, with required pre-reads, boundaries, and QA evidence visible.
- Generic prompt generation now produces router + four stage prompts for future books.
- Generic outputs remain free of 《人生》 contamination; 《人生》 outputs retain book-specific facts and sentinel inheritance.
- Runtime continuation artifact status matches the execution-start baseline.
- No reading notes, intermediate drafts, other book prompts, or runtime continuation files are changed.
