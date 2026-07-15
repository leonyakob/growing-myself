# clean-weread-split-artifacts - Work Plan

## TL;DR (For humans)
**What you'll get:** 清理拆分提示词时留下的工程痕迹，让这些文件更像长期可用的执行提示词，而不是一次性拆分任务记录。

**Why this approach:** 只改会误导后续执行的文字：历史 QA 路径、Task 8 / snapshot / ledger / Wave 2 这类拆分语境。不重构阶段设计，不润色内容，不重新拆文件。它会明确改变一个 QA 默认行为：未指定当前任务/计划 evidence 路径时，不再让长期阶段提示词自行编造 `.omo/evidence/...` 路径，而是在最终回复列 QA 通过/未通过项。

**What it will NOT do:** 不改微信读书 workflow，不改四阶段边界，不改《人生》的双 bookId、人物/主题规则或 7 个回归哨兵，不整理任何阅读材料。

**Effort:** Quick
**Risk:** Low - 风险主要是误删《人生》专属保护规则，所以计划要求逐项回归检查。
**Decisions to sanity-check:** 统一 QA 表述改成“使用当前任务/当前计划明确指定的 evidence；未指定则最终回复列 QA 清单”；同书 AGENTS 规则改成稳定长期表述，不再提 Task 8。

Your next move: 审核本计划；确认后再让执行 session 按本计划改提示词。Full execution detail follows below.

---

> TL;DR (machine): Quick / Low-risk markdown cleanup plan for removing stale split-task artifacts from WeChat Reading prompt files while preserving router/stage behavior.

## Scope
### Must have
- Clean only long-term prompt files that still contain split-task engineering artifacts discovered in the previous review.
- Replace historical `split-weread-prompts-by-stage` QA evidence paths with a reusable current-task QA instruction.
- Adopt this explicit QA fallback behavior: when no current task/plan evidence path is specified, future stage prompts report QA pass/fail in the final response instead of inventing a default `.omo/evidence/...` file.
- Replace `Task 8`, `snapshot`, `ledger`, `preservation ledger`, `快照`, and `Wave 2` wording with stable long-term wording.
- Preserve the actual safety meaning behind those lines:
  - `/home/king/github/growing-myself/路遥/人生/AGENTS.md` is read only if it exists at execution time.
  - Do not fabricate same-book AGENTS rules.
  - Do not import sibling-book `AGENTS.md`, especially from `路遥/平凡的世界`.
  - Do not modify unrelated prompt files or other books unless the current task explicitly asks for it.
- Preserve all existing router and stage boundaries.
- Preserve all 微信读书 / AGENTS literary rules, including 五异法扫描、问题阶梯、张力地图、轻卡/主卡边界、文本落点、提问可以跳远，论证不能偷步。
- Preserve all 《人生》专属 facts: personal/imported `bookId=CB_2tb79r78T38k74M75h8iz4C3`, official `bookId=25164497`, character/theme examples, article direction set, and 7 regression sentinels.

### Must NOT have (guardrails, anti-slop, scope boundaries)
- Do not edit any reading notes, middle drafts, formal reading notes, exported WeChat data, or book content.
- Do not restructure the prompt architecture or merge/split files.
- Do not rewrite the router tables unless a stale artifact appears inside the targeted line.
- Do not normalize language style merely for consistency.
- Do not remove useful execution boundaries, QA requirements, or scope guards.
- Do not replace 《人生》 specific examples with generic wording.
- Do not create or assume `/home/king/github/growing-myself/路遥/人生/AGENTS.md`; only preserve the “read if exists” rule.
- Do not use the API interruption from the prior planning session as a task result, blocker, or prompt-file fact.

## Verification strategy
> Zero human intervention - all verification is agent-executed.
- Test decision: none - markdown prompt cleanup. Verification is grep/read-based QA plus dry-run prompt-surface checks.
- Evidence: `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`
- Preferred search command: use `GIT_MASTER=1 git grep --untracked ...` because `rg` may be unavailable in this environment.
- For no-match `git grep` checks, expected PASS is empty stdout with exit code `1`; exit code `0` means the stale artifact still exists; exit code `>1` means command error.
- Evidence should record grep exit codes and match counts; do not rely only on visual path readability, because CJK paths may be shell-escaped depending on git/path settings.
- Each implementation todo must append evidence to the evidence file with:
  - exact files changed;
  - before/after summary;
  - happy-path QA command and result;
  - failure-path QA command and result;
  - any unrelated pre-existing issue observed.

## Execution strategy
### Parallel execution waves
> This is a Quick markdown cleanup; small sequential waves are intentional to avoid conflicting edits in the same prompt files.
- Wave 1: Reconfirm baseline artifacts and clean generic-stage QA evidence wording.
- Wave 2: Clean 《人生》 stage QA evidence wording and execution-QA line.
- Wave 3: After Wave 2, clean 《人生》 Task 8 / snapshot / ledger / Wave 2 wording while preserving same-book/sibling-book safety semantics.
- Wave 4: Preservation audit and final prompt-surface dry run.

### Dependency matrix
| Todo | Depends on | Blocks | Can parallelize with |
| --- | --- | --- | --- |
| 1 | none | 2, 3, 4, 5, 6 | none |
| 2 | 1 | 6 | 3, 4 |
| 3 | 1 | 4, 6 | 2 |
| 4 | 1, 3 | 5, 6 | 2 |
| 5 | 4 | 6 | none |
| 6 | 2, 3, 5 | Final verification | none |

## Todos
> Implementation + Test = ONE todo. Never separate.
<!-- APPEND TASK BATCHES BELOW THIS LINE WITH edit/apply_patch - never rewrite the headers above. -->
- [ ] 1. Reconfirm baseline and open execution evidence
  What to do / Must NOT do: In `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`, create a fresh run section at the bottom with timestamp, current `GIT_MASTER=1 git rev-parse --short HEAD`, and initial `GIT_MASTER=1 git status --short --untracked-files=all`. Record that this worker starts from the current filesystem state, not from the interrupted API response. All later todo evidence must be written under this fresh run section, not mixed with older evidence. Re-run the baseline scans below and paste/summarize results. Do not edit prompt files in this todo.
  Parallelization: Wave 1 | Blocked by: none | Blocks: 2, 3, 4, 5, 6
  References (executor has NO interview context - be exhaustive): prior review found stale evidence paths and `Task 8` / `snapshot` / `ledger` / `Wave 2` artifacts in the split WeChat Reading prompt files; current known examples include `微信读书通用提示词-第一阶段-生成中间整理稿.md:13`, `路遥/人生/《人生》微信读书提示词.md:43`, `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:23`, `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:442`.
  Acceptance criteria (agent-executable): Evidence file exists and includes a fresh run section with timestamp, HEAD, initial status, and output summaries for all baseline scans:
  - `GIT_MASTER=1 git grep --untracked -n -E "split-weread-prompts-by-stage|Task 8|snapshot|ledger|preservation ledger|Wave 2|快照|当前拆分任务|拆分任务的验证文件|Task 8 记录|snapshot 冻结" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"`
  - `GIT_MASTER=1 git grep --untracked -n -E "QA 证据路径|QA evidence path|QA evidence" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"`
  - `GIT_MASTER=1 git grep --untracked -n -F "sibling-book" -- "路遥/人生/《人生》微信读书提示词*.md"`
  - `GIT_MASTER=1 git grep --untracked -n -F "平凡的世界/AGENTS" -- "路遥/人生/《人生》微信读书提示词*.md"`
  - Protected 《人生》 identity/sentinel/article-direction check, one required match per string:
    ```bash
    for p in "CB_2tb79r78T38k74M75h8iz4C3" "25164497" "ID 003" "ID 006" "ID 021" "ID 109" "ID 117" "刘玉海救灾处" "黄亚萍的物质付出" "人物线" "城乡主题" "尊严主题" "爱情线" "知识分子困境" "写法线索"; do GIT_MASTER=1 git grep --untracked -nF "$p" -- "路遥/人生/《人生》微信读书提示词*.md" >/dev/null || exit 1; done
    ```
  - Literary-rule check, one required match per string in both second-stage files:
    ```bash
    for p in "五异法扫描" "问题阶梯（1星-5星）" "张力地图" "轻卡/主卡边界" "提问可以跳远，论证不能偷步" "保留有生命力的句子"; do for f in "微信读书通用提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"; do GIT_MASTER=1 git grep --untracked -nF "$p" -- "$f" >/dev/null || exit 1; done; done
    ```
  QA scenarios (name the exact tool + invocation): happy = run every baseline command and record matches/results under the fresh run section; failure = confirm `.omo/plans/clean-weread-split-artifacts.md` says the prior API interruption is not task output and no prompt-file edit has happened yet (`GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"`). Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

- [ ] 2. Replace generic-stage stale QA evidence paths
  What to do / Must NOT do: In the four generic stage prompt files, replace exactly four stale `task-3/4/5/6-split-weread-prompts-by-stage.md` QA lines with reusable current-task/current-plan QA wording. Preserve each file's existing inheritance block style; for the blockquoted fourth-stage file, keep the `>` prefix. Do not change stage boundaries or workflow text.
  Exact replacement text for non-blockquoted generic stage files: `- QA 证据：优先使用当前任务或当前计划明确指定的 evidence 路径；若未指定 evidence 文件，则在最终回复中列出本阶段 QA 清单和通过/未通过项。不得复用未由当前任务或当前计划明确指定的 evidence 文件。`
  Exact replacement text for `微信读书通用提示词-第四阶段-全书收束整合.md`: `> - QA 证据：优先使用当前任务或当前计划明确指定的 evidence 路径；若未指定 evidence 文件，则在最终回复中列出本阶段 QA 清单和通过/未通过项。不得复用未由当前任务或当前计划明确指定的 evidence 文件。`
  Parallelization: Wave 1 | Blocked by: 1 | Blocks: 6
  References (executor has NO interview context - be exhaustive): `微信读书通用提示词-第一阶段-生成中间整理稿.md:13`; `微信读书通用提示词-第二阶段-优化中间整理稿.md:21`; `微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md:11`; `微信读书通用提示词-第四阶段-全书收束整合.md:11`.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git grep --untracked -n "split-weread-prompts-by-stage" -- "微信读书通用提示词*.md"` returns no matches under the no-match semantics in Verification strategy; `GIT_MASTER=1 git grep --untracked -n -F "不得复用未由当前任务或当前计划明确指定的 evidence 文件" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"` returns exactly four matches, one per generic stage file.
  QA scenarios (name the exact tool + invocation): happy = above two `git grep` commands pass; failure = `GIT_MASTER=1 git grep --untracked -n -E "AI修正|迁移到正式阅读笔记|全书收束整合|冲突规则" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"` still shows stage-boundary guardrails, proving the cleanup did not delete them. Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

- [ ] 3. Replace 《人生》 stale QA evidence paths and the second-stage QA record sentence
  What to do / Must NOT do: In the four 《人生》 stage files, replace exactly four stale `task-10/11/12/13-split-weread-prompts-by-stage.md` inheritance QA lines with reusable current-task/current-plan QA wording. Also replace exactly one second-stage body sentence that tells the agent to record QA into `task-11-split-weread-prompts-by-stage.md`. Preserve all 《人生》-specific bookId, character, example, stage, and literary-analysis content. For `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`, preserve the leading `>` blockquote prefix in the inheritance block.
  Exact replacement text for non-blockquoted 《人生》 stage inheritance QA lines: `- QA 证据：优先使用当前任务或当前计划明确指定的 evidence 路径；若未指定 evidence 文件，则在最终回复中列出本阶段 QA 清单和通过/未通过项。不得复用未由当前任务或当前计划明确指定的 evidence 文件。`
  Exact replacement text for `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`: `> - QA 证据：优先使用当前任务或当前计划明确指定的 evidence 路径；若未指定 evidence 文件，则在最终回复中列出本阶段 QA 清单和通过/未通过项。不得复用未由当前任务或当前计划明确指定的 evidence 文件。`
  Exact replacement for `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:442`: `输出完成后，至少逐条核对以下事项；若当前任务或当前计划明确指定 evidence 文件，则把结果写入该文件，否则在最终回复中列出 QA 清单和通过/未通过项。不得复用未由当前任务或当前计划明确指定的 evidence 文件：`
  Parallelization: Wave 2 | Blocked by: 1 | Blocks: 6
  References (executor has NO interview context - be exhaustive): `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:14`; `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:24`; `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:442`; `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:25`; `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:26`.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git grep --untracked -n "split-weread-prompts-by-stage" -- "路遥/人生/《人生》微信读书提示词*.md"` returns no matches under the no-match semantics in Verification strategy; `GIT_MASTER=1 git grep --untracked -n -F "不得复用未由当前任务或当前计划明确指定的 evidence 文件" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"` returns exactly five matches: four inheritance QA lines plus the second-stage body QA sentence.
  QA scenarios (name the exact tool + invocation): happy = both acceptance `git grep` commands pass; failure = run the protected 《人生》 identity/sentinel loop from Todo 1 again and require one match per protected string. Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

- [ ] 4. Replace Task 8 / snapshot / ledger wording with stable same-book AGENTS wording
  What to do / Must NOT do: In the 《人生》 router and four 《人生》 stage files, remove only stale trailing `Task 8` / `snapshot` / `ledger` / `preservation ledger` / `快照` clauses. Preserve all required pre-read paths, list numbering, list structure, conflict rules, task-boundary text, and blockquote prefixes. Do not collapse any pre-read bullet into only the same-book `AGENTS.md` rule. Preserve the real rule: read `/home/king/github/growing-myself/路遥/人生/AGENTS.md` only if it exists at execution time, do not assume it exists, and do not fabricate same-book rules. Do not remove the sibling-book prohibition.
  Exact replacement map:
    ```text
    路遥/人生/《人生》微信读书提示词.md:43
    2. `/home/king/github/growing-myself/路遥/人生/AGENTS.md` 仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则。

    路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:7
    - 执行前必读：`/home/king/github/growing-myself/AGENTS.md`、`/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`；`/home/king/github/growing-myself/路遥/人生/AGENTS.md` 仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则。

    路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:9
    4. `/home/king/github/growing-myself/路遥/人生/AGENTS.md`，仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则。

    路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:10
    - `/home/king/github/growing-myself/路遥/人生/AGENTS.md`，仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则。

    路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:10
    >   - `/home/king/github/growing-myself/路遥/人生/AGENTS.md`，仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则。
    ```
  Parallelization: Wave 3 | Blocked by: 1, 3 | Blocks: 5, 6
  References (executor has NO interview context - be exhaustive): `路遥/人生/《人生》微信读书提示词.md:43`; `路遥/人生/《人生》微信读书提示词.md:44`; `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:7`; `路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md:13`; `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:9`; `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:23`; `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:10`; `路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md:23`; `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:10`; `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:25`. Sibling-book prohibition baseline must remain in router line 44 equivalent, first-stage must-not block, third-stage must-not block, and fourth-stage blockquoted must-not block; do not invent it in second-stage unless current baseline proves it already exists there.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git grep --untracked -n -E "Task 8|snapshot|ledger|preservation ledger|快照" -- "路遥/人生/《人生》微信读书提示词*.md"` returns no matches under the no-match semantics in Verification strategy; `GIT_MASTER=1 git grep --untracked -n -F "仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则" -- "路遥/人生/《人生》微信读书提示词*.md"` returns exactly five matches: router plus four stage files. Sibling-book guardrails remain in the four baseline locations listed above, verified with per-file read slices.
  QA scenarios (name the exact tool + invocation): happy = both acceptance `git grep` commands pass; failure = use Read tool on these absolute slices and record the result: `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` offset 40 limit 8; `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` offset 3 limit 13; `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` offset 5 limit 20; `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` offset 5 limit 21; `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` offset 4 limit 23. Confirm each slice has no `Task 8` / `snapshot` / `ledger` / `快照` wording, retains required pre-read paths, and retains sibling-book prohibition where it existed in the baseline. `Wave 2` is allowed to remain until Todo 5. Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

- [ ] 5. Replace the `Wave 2` scope artifact in 《人生》 second-stage prompt
  What to do / Must NOT do: Replace `不得修改其他 Wave 2 文件。` with a stable scope guard. Do not broaden or weaken the existing boundary that second stage only edits the 《人生》中间整理稿.
  Exact replacement text, preserving the existing two-space nested-list indentation: `  - 不得修改本阶段精确输出以外的其他文件，除非当前任务明确要求。`
  Parallelization: Wave 3 | Blocked by: 4 | Blocks: 6
  References (executor has NO interview context - be exhaustive): `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:16` to `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md:24`.
  Acceptance criteria (agent-executable): `GIT_MASTER=1 git grep --untracked -n "Wave 2" -- "路遥/人生/《人生》微信读书提示词*.md"` returns no matches under the no-match semantics in Verification strategy; `GIT_MASTER=1 git grep --untracked -n -F "不得修改本阶段精确输出以外的其他文件，除非当前任务明确要求" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"` returns exactly one match.
  QA scenarios (name the exact tool + invocation): happy = both acceptance `git grep` commands pass; failure = `GIT_MASTER=1 git grep --untracked -n -E "不得写入 .*《人生》阅读笔记|不得改变中间整理稿的阅读顺序|不得覆盖我的原想法|不得执行第三阶段|不得执行第四阶段" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"` confirms the second-stage boundary remains intact. Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

- [ ] 6. Preservation audit and prompt-surface dry run
  What to do / Must NOT do: After all cleanup edits, audit that only engineering artifacts changed. Do not “improve” wording beyond the targeted lines. Perform a dry-run prompt-surface check: read the router/stage entry blocks as a future agent would and confirm they no longer point to historical split-task evidence while still route correctly.
  Parallelization: Wave 4 | Blocked by: 2, 3, 5 | Blocks: Final verification
  References (executor has NO interview context - be exhaustive): all edited files from todos 2-5; root rule `AGENTS.md:14-18` (五异法、问题阶梯、张力地图), `AGENTS.md:20-24` (轻卡/主卡、细节卡/主题卡), `AGENTS.md:26-30` (微信读书 Skill 与文本证据优先), `AGENTS.md:63-71` (只整理/只评价/全面评价边界), `AGENTS.md:99-102` (提问可以跳远、另一个角度、跨作品联动), and `AGENTS.md:104-117` (归档结构、子目录 AGENTS、文件与 Git 规则) require preserving 微信读书 workflow, text evidence priority, light/main-card boundaries, and same-book prompt boundaries.
  Acceptance criteria (agent-executable):
  - `GIT_MASTER=1 git diff --stat -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"` shows only the intended prompt files changed.
  - `GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"` shows no broad rewrites and no reading-material edits.
  - `GIT_MASTER=1 git grep --untracked -n -E "当前拆分任务|拆分任务的验证文件|Task 8 记录|snapshot 冻结|preservation ledger" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"` returns no matches under the no-match semantics in Verification strategy.
  - Literary rules remain, one required match per string in both second-stage files:
    ```bash
    for p in "五异法扫描" "问题阶梯（1星-5星）" "张力地图" "轻卡/主卡边界" "提问可以跳远，论证不能偷步" "保留有生命力的句子"; do for f in "微信读书通用提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"; do GIT_MASTER=1 git grep --untracked -nF "$p" -- "$f" >/dev/null || exit 1; done; done
    ```
  - Router/stage boundary checks, one required match per file group:
    ```bash
    for f in "微信读书通用提示词.md" "路遥/人生/《人生》微信读书提示词.md"; do GIT_MASTER=1 git grep --untracked -nF "阶段文件索引" -- "$f" >/dev/null || exit 1; done
    for f in "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"; do GIT_MASTER=1 git grep --untracked -nF "冲突规则" -- "$f" >/dev/null || exit 1; done
    ```
  QA scenarios (name the exact tool + invocation): happy = run all acceptance commands and record pass/fail in the fresh evidence section; failure = inspect only the changed hunks from `GIT_MASTER=1 git diff --word-diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"` and reject any change that alters bookId rules, stage trigger gates, literary rules, or reading-note files. Evidence `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
  Commit: N | Do not commit unless the user explicitly asks after execution.

## Final verification wave
> Runs after ALL todos. ALL checks are agent-executed and recorded in evidence before reporting results to the user.
- [ ] F1. Plan compliance audit: Verify every changed prompt line maps to todos 2-5 and every acceptance command from todo 6 was recorded under the fresh run section in `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`.
- [ ] F2. Code/document quality review: Inspect the changed hunks from `GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"` and approve that wording is stable long-term prompt wording, not another task-specific artifact.
- [ ] F3. Agent-executed prompt-surface QA: Use Read tool on `/home/king/github/growing-myself/微信读书通用提示词.md` offset 1 limit 25, `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md` offset 1 limit 30, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` offset 1 limit 46, and `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` offset 1 limit 35. Record a pass/fail checklist in evidence: second-stage request maps to the second-stage file; exact output remains the middle draft; formal reading note remains forbidden; current-task/current-plan QA wording exists; historical split-task evidence path is absent; same-book `AGENTS.md` rule remains conditional; no `Task 8`/`ledger`/`snapshot`/`Wave 2` wording appears in these entry slices.
- [ ] F4. Scope fidelity: Run `GIT_MASTER=1 git status --short --untracked-files=all` and compare against the initial status recorded in Todo 1's fresh evidence section. Ignore paths that were already dirty in the initial status. New or newly changed paths after Todo 1 must be limited to the targeted prompt files plus `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`; no new/changed reading notes, middle drafts, formal notes, AGENTS files, or unrelated book files are allowed.

## Commit strategy
- No commit by default.
- If the user explicitly asks to commit after execution, inspect `git status`, `git diff`, and recent log first; stage only the prompt files intentionally changed by this plan plus the execution evidence file if the user wants evidence committed.
- Do not commit `.omo/plans/clean-weread-split-artifacts.md` unless the user explicitly wants plan artifacts committed.

## Success criteria
- No `split-weread-prompts-by-stage` remains in the target generic or 《人生》 prompt files; no-match checks use the Verification strategy exit-code rule.
- No `Task 8`, `snapshot`, `ledger`, `preservation ledger`, `快照`, or `Wave 2` remains in `路遥/人生/《人生》微信读书提示词*.md`; no-match checks use the Verification strategy exit-code rule.
- Current-task QA wording exists where historical split-task evidence paths used to exist.
- Same-book AGENTS rule still says the 《人生》 AGENTS file is read only if it exists; sibling-book AGENTS import remains prohibited.
- Router and four-stage boundaries remain intact.
- AGENTS literary-analysis rules remain intact in both second-stage files.
- 《人生》 dual bookId and 7 regression sentinels remain intact.
- Relative to the initial status recorded in Todo 1's fresh evidence section, only targeted prompt files changed plus `/home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md`; no reading material changed.
- Evidence file records all commands, results, and final prompt-surface dry run.
- Evidence file contains a fresh run section for this execution with timestamp, current HEAD, initial status, baseline scans, every todo result, and final verification results.
