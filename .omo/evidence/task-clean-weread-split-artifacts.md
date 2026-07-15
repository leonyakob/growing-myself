# clean-weread-split-artifacts execution evidence

## Fresh run - 2026-07-15T14:27:00+08:00

### Todo 1. Reconfirm baseline and open execution evidence

Status: PASS

This fresh run starts from the current filesystem state. The interrupted API/Bash event before this section is infrastructure noise, not subtask output, not a blocker, and not prompt-file evidence.

Current HEAD:

```text
c01b696
```

Initial `GIT_MASTER=1 git status --short --untracked-files=all`:

```text
 M .omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
?? .omo/drafts/clean-weread-split-artifacts.md
?? .omo/plans/clean-weread-split-artifacts.md
?? .omo/run-continuation/ses_09ba17d73ffesi6cfZi1h31RJu.json
?? .omo/run-continuation/ses_09ba184ceffeC5rZSGmhZ09hTi.json
?? .omo/run-continuation/ses_09ba18c40ffeiHCgZpxEldagLs.json
?? .omo/run-continuation/ses_09baaa1dbffe6H0Q5Lj2uaV3Cq.json
?? .omo/run-continuation/ses_09baaa822ffelHwkmcb6IpuBpk.json
?? .omo/run-continuation/ses_09baaad50ffeet8Da8GgCRU0gL.json
?? .omo/run-continuation/ses_09bbb43aaffeNbZdzETzUfdEWt.json
?? .omo/run-continuation/ses_09bbb49f5ffeKPhuIIH7uYY8wp.json
?? .omo/run-continuation/ses_09bbb4ec8ffecvViFiJ1UJ2qqd.json
?? .omo/run-continuation/ses_09bccc041ffe87RwV31f7iAnkF.json
```

Baseline scan command 1:

```text
GIT_MASTER=1 git grep --untracked -n -E "split-weread-prompts-by-stage|Task 8|snapshot|ledger|preservation ledger|Wave 2|快照|当前拆分任务|拆分任务的验证文件|Task 8 记录|snapshot 冻结" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
```

Result: exit code 0, stale artifacts found as expected before cleanup. Match summary:

```text
generic Stage 1: line 13 split task evidence path
generic Stage 2: line 21 split task evidence path
generic Stage 3: line 11 split task evidence path
generic Stage 4: line 11 split task evidence path
《人生》 router: line 43 Task 8 / 快照 wording
《人生》 Stage 1: lines 7 and 14 Task 8 / split task evidence path
《人生》 Stage 2: lines 9, 23, 24, 442 Task 8 / preservation ledger / Wave 2 / split task evidence path
《人生》 Stage 3: lines 10 and 25 Task 8 ledger / snapshot / split task evidence path
《人生》 Stage 4: lines 10 and 26 Task 8 snapshot / split task evidence path
```

Baseline scan command 2:

```text
GIT_MASTER=1 git grep --untracked -n -E "QA 证据路径|QA evidence path|QA evidence" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
```

Result: exit code 0, historical QA evidence references found as expected before cleanup. Match summary:

```text
generic Stage 1/2/3/4: four QA evidence path matches
《人生》 Stage 1/2/3/4: four inheritance QA evidence path matches
```

Baseline scan command 3:

```text
GIT_MASTER=1 git grep --untracked -n -F "sibling-book" -- "路遥/人生/《人生》微信读书提示词*.md"
```

Result: exit code 0, four existing sibling-book guardrail matches found in router, Stage 1, Stage 3, and Stage 4.

Baseline scan command 4:

```text
GIT_MASTER=1 git grep --untracked -n -F "平凡的世界/AGENTS" -- "路遥/人生/《人生》微信读书提示词*.md"
```

Result: exit code 0, one existing explicit `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` prohibition found in the 《人生》 router.

Protected 《人生》 identity / sentinel / article-direction loop:

```text
CB_2tb79r78T38k74M75h8iz4C3 EXIT:0 COUNT:9
25164497 EXIT:0 COUNT:9
ID 003 EXIT:0 COUNT:3
ID 006 EXIT:0 COUNT:2
ID 021 EXIT:0 COUNT:2
ID 109 EXIT:0 COUNT:2
ID 117 EXIT:0 COUNT:2
刘玉海救灾处 EXIT:0 COUNT:2
黄亚萍的物质付出 EXIT:0 COUNT:2
人物线 EXIT:0 COUNT:9
城乡主题 EXIT:0 COUNT:5
尊严主题 EXIT:0 COUNT:4
爱情线 EXIT:0 COUNT:4
知识分子困境 EXIT:0 COUNT:6
写法线索 EXIT:0 COUNT:5
EXIT:0
```

Literary-rule loop across both second-stage files:

```text
五异法扫描 | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
五异法扫描 | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
问题阶梯（1星-5星） | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
问题阶梯（1星-5星） | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
张力地图 | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
张力地图 | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
轻卡/主卡边界 | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
轻卡/主卡边界 | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
提问可以跳远，论证不能偷步 | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:1
提问可以跳远，论证不能偷步 | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
保留有生命力的句子 | 微信读书通用提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
保留有生命力的句子 | 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md EXIT:0 COUNT:2
EXIT:0
```

Failure-path QA before prompt edits:

```text
GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
```

Result: no prompt-file diff before Todo 2, so the interrupted API/Bash event did not edit target prompt files.

Plan rule check:

```text
GIT_MASTER=1 git grep --untracked -n -F "Do not use the API interruption from the prior planning session as a task result" -- ".omo/plans/clean-weread-split-artifacts.md"
.omo/plans/clean-weread-split-artifacts.md:43:- Do not use the API interruption from the prior planning session as a task result, blocker, or prompt-file fact.
EXIT:0
```

Unrelated pre-existing dirty paths observed in initial status are recorded above. They are not task output unless later explicitly modified by this plan.

### Todo 2. Replace generic-stage stale QA evidence paths

Status: PASS

Files changed:

```text
微信读书通用提示词-第一阶段-生成中间整理稿.md
微信读书通用提示词-第二阶段-优化中间整理稿.md
微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md
微信读书通用提示词-第四阶段-全书收束整合.md
```

Before/after summary:

```text
Replaced exactly four generic-stage historical `task-3/4/5/6-split-weread-prompts-by-stage.md` QA evidence lines with the plan's reusable current-task/current-plan QA wording.
The fourth-stage blockquoted inheritance line kept its leading `>` prefix.
No stage boundary, workflow body, router, or reading material was edited in this todo.
```

Happy-path QA:

```text
GIT_MASTER=1 git grep --untracked -n "split-weread-prompts-by-stage" -- "微信读书通用提示词*.md"
EXIT:1
PASS: empty output + exit code 1 means no generic split artifact remains.

GIT_MASTER=1 git grep --untracked -n -F "不得复用未由当前任务或当前计划明确指定的 evidence 文件" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"
EXIT:0
PASS: exactly four matches, one in each generic stage file.
```

Failure-path QA:

```text
GIT_MASTER=1 git grep --untracked -n -E "AI修正|迁移到正式阅读笔记|全书收束整合|冲突规则" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md"
EXIT:0
PASS: stage-boundary guardrails remain visible after cleanup.
```

Diff scope check:

```text
GIT_MASTER=1 git diff --stat -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
4 generic prompt files changed, 4 insertions, 4 deletions.
GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
PASS: diff shows only the four planned QA-line replacements.
```

Markdown diagnostics:

```text
lsp_diagnostics on the four changed generic Markdown files reported no `.md` LSP server configured. This is recorded as tooling unavailability, not a Todo 2 failure.
```

### Todo 3. Replace 《人生》 stale QA evidence paths and the second-stage QA record sentence

Status: PASS

Files changed:

```text
路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md
路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md
路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md
路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md
```

Before/after summary:

```text
Replaced exactly four 《人生》 stage inheritance QA evidence lines that pointed to historical `task-10/11/12/13-split-weread-prompts-by-stage.md` evidence.
Replaced exactly one second-stage body QA sentence that wrote runtime QA into `task-11-split-weread-prompts-by-stage.md`.
The fourth-stage blockquoted inheritance line kept its leading `>` prefix.
No 《人生》 bookId, character/example, article-direction, stage-boundary, router, middle draft, or formal reading note content was edited in this todo.
```

Happy-path QA:

```text
GIT_MASTER=1 git grep --untracked -n "split-weread-prompts-by-stage" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: empty output + exit code 1 means no 《人生》 split evidence path remains.

GIT_MASTER=1 git grep --untracked -n -F "不得复用未由当前任务或当前计划明确指定的 evidence 文件" -- "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"
EXIT:0
PASS: exactly five matches: four inheritance QA lines plus the second-stage body QA sentence.
```

Failure-path QA / protected identity loop:

```text
CB_2tb79r78T38k74M75h8iz4C3 EXIT:0 COUNT:9
25164497 EXIT:0 COUNT:9
ID 003 EXIT:0 COUNT:3
ID 006 EXIT:0 COUNT:2
ID 021 EXIT:0 COUNT:2
ID 109 EXIT:0 COUNT:2
ID 117 EXIT:0 COUNT:2
刘玉海救灾处 EXIT:0 COUNT:2
黄亚萍的物质付出 EXIT:0 COUNT:2
人物线 EXIT:0 COUNT:9
城乡主题 EXIT:0 COUNT:5
尊严主题 EXIT:0 COUNT:4
爱情线 EXIT:0 COUNT:4
知识分子困境 EXIT:0 COUNT:6
写法线索 EXIT:0 COUNT:5
EXIT:0
PASS: all protected 《人生》 identity, sentinel, and article-direction strings remain present.
```

Diff scope check:

```text
GIT_MASTER=1 git diff --stat -- "路遥/人生/《人生》微信读书提示词*.md"
4 《人生》 stage files changed, 5 insertions, 5 deletions.
GIT_MASTER=1 git diff -- "路遥/人生/《人生》微信读书提示词*.md"
PASS: diff shows only the five planned QA wording replacements.
```

Markdown diagnostics:

```text
lsp_diagnostics on the four changed 《人生》 Markdown stage files reported no `.md` LSP server configured. This is recorded as tooling unavailability, not a Todo 3 failure.
```

### Todo 4. Replace Task 8 / snapshot / ledger wording with stable same-book AGENTS wording

Status: PASS

Files changed:

```text
路遥/人生/《人生》微信读书提示词.md
路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md
路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md
路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md
路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md
```

Before/after summary:

```text
Replaced exactly the five plan-mapped stale Task 8 / snapshot / ledger / preservation ledger / 快照 clauses with stable same-book AGENTS conditional wording.
Preserved required pre-read paths, list numbering, conflict rules, task boundaries, blockquote prefix in Stage 4, and sibling-book guardrails.
Todo 5's Wave 2 wording was intentionally left untouched in this todo.
```

Happy-path QA:

```text
GIT_MASTER=1 git grep --untracked -n -E "Task 8|snapshot|ledger|preservation ledger|快照" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: empty output + exit code 1 means no Task 8 / snapshot / ledger / preservation ledger / 快照 wording remains in 《人生》 prompts.

GIT_MASTER=1 git grep --untracked -n -F "仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: exactly five matches: router plus four stage files.
```

Failure-path QA / read-slice confirmation:

```text
Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md offset 40 limit 8:
PASS: router keeps root AGENTS pre-read, conditional same-book AGENTS rule, explicit 平凡的世界/AGENTS sibling-book prohibition, and router conflict rule.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md offset 3 limit 13:
PASS: Stage 1 keeps root/router pre-read paths, conditional same-book AGENTS rule, input/output paths, conflict rule, task boundary, sibling-book prohibition in Must NOT, and current-plan QA wording.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md offset 5 limit 20:
PASS: Stage 2 keeps root/router/middle-draft pre-read paths, conditional same-book AGENTS rule, exact input/output files, conflict rule, task boundary, and existing second-stage file/output boundaries. Wave 2 remains only because Todo 5 owns that replacement.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md offset 5 limit 21:
PASS: Stage 3 keeps root/router/middle-draft/formal-note pre-read paths, conditional same-book AGENTS rule, input/output paths, conflict rule, task boundary, sibling-book prohibition, and current-plan QA wording.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md offset 4 limit 23:
PASS: Stage 4 keeps blockquoted root/router/middle-draft/formal-note/fixture pre-read paths, conditional same-book AGENTS rule, input/output paths, conflict rule, trigger, task boundary, same-book/sibling-book prohibition, and current-plan QA wording.
```

Diff scope check:

```text
GIT_MASTER=1 git diff --stat -- "路遥/人生/《人生》微信读书提示词*.md"
5 《人生》 prompt files show cumulative planned changes from Todo 3 and Todo 4.
GIT_MASTER=1 git diff -- "路遥/人生/《人生》微信读书提示词*.md"
PASS: Todo 4 hunks are limited to the five exact replacement-map lines; prior Todo 3 QA hunks remain as already recorded.
```

Markdown diagnostics:

```text
lsp_diagnostics on /home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md reported no `.md` LSP server configured. This is recorded as tooling unavailability, not a Todo 4 failure.
```

### Todo 5. Replace the Wave 2 scope artifact in 《人生》 second-stage prompt

Status: PASS

Files changed:

```text
路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md
```

Before/after summary:

```text
Replaced `不得修改其他 Wave 2 文件。` with the plan's stable scope guard: `不得修改本阶段精确输出以外的其他文件，除非当前任务明确要求。`
No second-stage output boundary was broadened: exact output remains the 《人生》中间整理稿, and formal reading note writes remain forbidden.
```

Happy-path QA:

```text
GIT_MASTER=1 git grep --untracked -n "Wave 2" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: empty output + exit code 1 means no Wave 2 artifact remains in 《人生》 prompts.

GIT_MASTER=1 git grep --untracked -n -F "不得修改本阶段精确输出以外的其他文件，除非当前任务明确要求" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"
EXIT:0
PASS: exactly one match at the second-stage must-not list.
```

Failure-path QA / boundary guardrails:

```text
GIT_MASTER=1 git grep --untracked -n -E "不得写入 .*《人生》阅读笔记|不得改变中间整理稿的阅读顺序|不得覆盖我的原想法|不得执行第三阶段|不得执行第四阶段" -- "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"
EXIT:0
PASS: second-stage boundaries remain present: formal-note write forbidden, middle-draft order protected, original thought protected, and Stage 3/4 execution forbidden.
```

Read-slice confirmation:

```text
Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md offset 16 limit 10:
PASS: line 23 contains the stable output-scope guard; lines 17-21 retain the existing second-stage boundary prohibitions.
```

Markdown diagnostics:

```text
lsp_diagnostics on /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md reported no `.md` LSP server configured. This is recorded as tooling unavailability, not a Todo 5 failure.
```

### Todo 6. Preservation audit and prompt-surface dry run

Status: PASS

Files audited:

```text
微信读书通用提示词-第一阶段-生成中间整理稿.md
微信读书通用提示词-第二阶段-优化中间整理稿.md
微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md
微信读书通用提示词-第四阶段-全书收束整合.md
路遥/人生/《人生》微信读书提示词.md
路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md
路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md
路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md
路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md
```

Happy-path QA:

```text
GIT_MASTER=1 git diff --stat -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: exactly 9 prompt files changed, 15 insertions and 15 deletions.

GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: diff shows only targeted engineering-artifact cleanup: historical QA evidence paths replaced with current-task/current-plan QA wording; Task 8 / snapshot / ledger / 快照 clauses replaced with conditional same-book AGENTS wording; Wave 2 scope wording replaced with stable output-scope guard.

GIT_MASTER=1 git grep --untracked -n -E "当前拆分任务|拆分任务的验证文件|Task 8 记录|snapshot 冻结|preservation ledger" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: empty output + exit code 1 means targeted stale split-artifact phrases are absent.
```

Preservation QA:

```text
Literary rules loop:
for p in "五异法扫描" "问题阶梯（1星-5星）" "张力地图" "轻卡/主卡边界" "提问可以跳远，论证不能偷步" "保留有生命力的句子"; do for f in "微信读书通用提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md"; do GIT_MASTER=1 git grep --untracked -nF "$p" -- "$f" >/dev/null || exit 1; done; done
EXIT:0
PASS: all required AGENTS literary rules remain present in both second-stage files.

Router/stage boundary loop:
for f in "微信读书通用提示词.md" "路遥/人生/《人生》微信读书提示词.md"; do GIT_MASTER=1 git grep --untracked -nF "阶段文件索引" -- "$f" >/dev/null || exit 1; done; for f in "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"; do GIT_MASTER=1 git grep --untracked -nF "冲突规则" -- "$f" >/dev/null || exit 1; done
EXIT:0
PASS: both routers still expose stage-file indexes and all stage files still expose conflict rules.
```

Failure-path QA / changed-hunk inspection:

```text
GIT_MASTER=1 git diff --word-diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: word diff only changes planned engineering-artifact wording. It does not alter bookId rules, stage trigger gates, literary rules, reading-note files, middle drafts, or formal reading notes.
```

Prompt-surface dry run:

```text
Read /home/king/github/growing-myself/微信读书通用提示词.md offset 1 limit 25:
PASS: generic router still routes second-stage requests to the second-stage file, keeps stage index, and does not point to historical split-task evidence.

Read /home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md offset 1 limit 30:
PASS: generic Stage 2 exact output remains only `{中间稿路径}`; formal reading note writes and Stage 3/4 execution remain forbidden; current-task/current-plan QA wording exists; historical split-task evidence path is absent from the entry slice.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md offset 1 limit 46:
PASS: 《人生》 router still routes second-stage requests to the second-stage file, preserves dual bookId lines, preserves conditional same-book AGENTS rule, preserves sibling-book AGENTS prohibition, and contains no Task 8 / ledger / snapshot / Wave 2 wording in the entry slice.

Read /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md offset 1 limit 35:
PASS: 《人生》 Stage 2 exact output remains the middle draft, formal reading note writes remain forbidden, current-task/current-plan QA wording exists, same-book AGENTS rule remains conditional, and no Task 8 / ledger / snapshot / Wave 2 wording appears in the entry slice.
```

### Final verification wave

#### F1. Plan compliance audit

Status: PASS

```text
Every changed prompt hunk maps to Todos 2-5:
- Todo 2: four generic-stage QA evidence lines.
- Todo 3: four 《人生》 stage inheritance QA lines plus one 《人生》 Stage 2 body QA sentence.
- Todo 4: five 《人生》 same-book AGENTS conditional wording lines.
- Todo 5: one 《人生》 Stage 2 Wave 2 scope line.

Todo 6 acceptance commands and prompt-surface reads are recorded above under the fresh run section.
```

#### F2. Code/document quality review

Status: PASS

```text
GIT_MASTER=1 git diff -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: changed wording is stable long-term prompt wording, not a new task-specific artifact. QA fallback now points to current task/current plan or final-response QA; same-book AGENTS rule is conditional; Wave 2 is replaced by stable file-scope wording.
```

#### F3. Agent-executed prompt-surface QA

Status: PASS

```text
Checklist:
PASS: second-stage requests map to second-stage files in both generic and 《人生》 routers.
PASS: exact output remains the middle draft / `{中间稿路径}` in both second-stage entry blocks.
PASS: formal reading note writes remain forbidden in both second-stage entry blocks.
PASS: current-task/current-plan QA wording exists in both second-stage entry blocks.
PASS: historical `split-weread-prompts-by-stage` evidence path is absent from the read entry slices.
PASS: same-book `AGENTS.md` rule remains conditional in the 《人生》 router and Stage 2 entry slice.
PASS: no `Task 8` / `ledger` / `snapshot` / `Wave 2` wording appears in the four prompt-surface slices.
```

Additional final grep checks:

```text
GIT_MASTER=1 git grep --untracked -n "split-weread-prompts-by-stage" -- "微信读书通用提示词*.md" "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: no split-task evidence path remains in target prompt files.

GIT_MASTER=1 git grep --untracked -n -E "Task 8|snapshot|ledger|preservation ledger|快照|Wave 2" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:1
PASS: no Task 8 / snapshot / ledger / preservation ledger / 快照 / Wave 2 artifact remains in 《人生》 prompts.

Protected 《人生》 identity / sentinel / article-direction loop:
for p in "CB_2tb79r78T38k74M75h8iz4C3" "25164497" "ID 003" "ID 006" "ID 021" "ID 109" "ID 117" "刘玉海救灾处" "黄亚萍的物质付出" "人物线" "城乡主题" "尊严主题" "爱情线" "知识分子困境" "写法线索"; do GIT_MASTER=1 git grep --untracked -nF "$p" -- "路遥/人生/《人生》微信读书提示词*.md" >/dev/null || exit 1; done
EXIT:0
PASS: all protected 《人生》 facts and sentinels remain present.

GIT_MASTER=1 git grep --untracked -n -F "不得复用未由当前任务或当前计划明确指定的 evidence 文件" -- "微信读书通用提示词-第一阶段-生成中间整理稿.md" "微信读书通用提示词-第二阶段-优化中间整理稿.md" "微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md" "微信读书通用提示词-第四阶段-全书收束整合.md" "路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md" "路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md" "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md"
EXIT:0
PASS: 9 matches total: four generic stage inheritance QA lines, four 《人生》 stage inheritance QA lines including the blockquoted Stage 4 inheritance line, and one 《人生》 Stage 2 body QA sentence.

GIT_MASTER=1 git grep --untracked -n -F "仅当执行时该文件真实存在才读取；不得假定它存在，也不得凭空补造同书规则" -- "路遥/人生/《人生》微信读书提示词*.md"
EXIT:0
PASS: exactly five matches: 《人生》 router plus four stage files.
```

#### F4. Scope fidelity

Status: PASS

Final `GIT_MASTER=1 git status --short --untracked-files=all`:

```text
 M .omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
 M 微信读书通用提示词-第一阶段-生成中间整理稿.md
 M 微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md
 M 微信读书通用提示词-第二阶段-优化中间整理稿.md
 M 微信读书通用提示词-第四阶段-全书收束整合.md
 M 路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md
 M 路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md
 M 路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md
 M 路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md
 M 路遥/人生/《人生》微信读书提示词.md
?? .omo/drafts/clean-weread-split-artifacts.md
?? .omo/evidence/task-clean-weread-split-artifacts.md
?? .omo/plans/clean-weread-split-artifacts.md
?? .omo/run-continuation/ses_09ba17d73ffesi6cfZi1h31RJu.json
?? .omo/run-continuation/ses_09ba184ceffeC5rZSGmhZ09hTi.json
?? .omo/run-continuation/ses_09ba18c40ffeiHCgZpxEldagLs.json
?? .omo/run-continuation/ses_09baaa1dbffe6H0Q5Lj2uaV3Cq.json
?? .omo/run-continuation/ses_09baaa822ffelHwkmcb6IpuBpk.json
?? .omo/run-continuation/ses_09baaad50ffeet8Da8GgCRU0gL.json
?? .omo/run-continuation/ses_09bbb43aaffeNbZdzETzUfdEWt.json
?? .omo/run-continuation/ses_09bbb49f5ffeKPhuIIH7uYY8wp.json
?? .omo/run-continuation/ses_09bbb4ec8ffecvViFiJ1UJ2qqd.json
?? .omo/run-continuation/ses_09bccc041ffe87RwV31f7iAnkF.json
```

Comparison against Todo 1 initial status:

```text
PASS: pre-existing dirty/untracked paths from initial status remain outside this task's scope and are ignored under the plan's F4 rule.
PASS: newly changed paths after Todo 1 are limited to the 9 targeted prompt files plus /home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md.
PASS: no reading notes, middle drafts, formal reading notes, AGENTS files, unrelated book files, or prompt plan files were newly modified by this execution.
```

#### Final Markdown diagnostics sweep

Status: PASS WITH TOOLING LIMITATION

```text
lsp_diagnostics was run on all 9 changed prompt Markdown files plus /home/king/github/growing-myself/.omo/evidence/task-clean-weread-split-artifacts.md.
Result for each file: No LSP server configured for extension: .md.
PASS: this repository has no Markdown LSP configured, so diagnostics could not provide Markdown semantic checks; grep/read/diff prompt-surface QA above is the applicable verification surface for this markdown-only cleanup.
```

#### Supplemental review note

Status: EVIDENCE CORRECTION ONLY

```text
补充复核：部分《人生》阶段文件使用英文 `conflict rule / Conflict rule`，而非中文“冲突规则”。具体是 `路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` 使用 `conflict rule`，`路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` 使用 `Conflict rule`。冲突规则语义保留；原 evidence 中“冲突规则”逐文件命中的表述不够严谨。这是 evidence 记录修正，不是提示词正文问题。
```
