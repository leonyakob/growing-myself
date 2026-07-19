# F4 Scope fidelity final verification

## 1. 核验目标与硬边界

- 计划锚点：`/home/king/github/growing-myself/.omo/plans/ren-sheng-stage5-question-compression.md:242-247` 要求本文件核验 Stage 5 是否发生未授权的归档编辑、提示词编辑、Git stage/commit/push、外部数据扩张，或超出现有锚点的跨书笔记读取。
- 根规则：`/home/king/github/growing-myself/AGENTS.md:107-117` 规定，只有用户明确要求时才执行归档，未经要求不要碰其他阅读材料，Git 也不能自行推进。
- 《人生》router 入口门：`/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:57-64` 要求复杂任务先计划、审看、再授权执行，不强制外部读者材料进入每张卡。
- 《人生》router Git 边界：`/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:127-133` 明确，未获用户明确授权，不执行 `stage`、`commit`、`push`。
- Stage 5 台账：`task-01-source-ledger.md:16-29,171-210` 把产品阅读材料、两份提示词、`AGENTS.md`、计划文件和 Git 状态都列为禁止越界对象，并记录了执行前全仓基线。
- 当前阶段 notepad 决议：`/home/king/github/growing-myself/.omo/notepads/ren-sheng-stage5-question-compression/decisions.md:4` 再次写明，不授权产品阅读笔记、提示词、`AGENTS`、Git stage/commit/push、外部数据扩张。

## 2. Task 01 基线与本次写前状态

### 2.1 Task 01 记录的执行前基线

- 基线文件：`/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md:171-210`
- 基线计数：`16` 条
- 基线解释要点：仓库起始即为 dirty worktree，后续核验看的是“新增增量有没有越界”，不是要求全仓变干净。

### 2.2 F4 写入前的当前全仓 `git status --short --untracked-files=all`

```text
 M .omo/boulder.json
 M .omo/run-continuation/ses_09b346be6ffelwOUgFIFbq8h9K.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
 M .omo/start-work/ledger.jsonl
?? .omo/drafts/ren-sheng-stage5-question-compression.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f1-plan-compliance.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f3-reader-qa.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md
?? .omo/notepads/ren-sheng-stage5-question-compression/decisions.md
?? .omo/notepads/ren-sheng-stage5-question-compression/issues.md
?? .omo/notepads/ren-sheng-stage5-question-compression/learnings.md
?? .omo/notepads/ren-sheng-stage5-question-compression/problems.md
?? .omo/plans/ren-sheng-stage5-question-compression.md
?? .omo/run-continuation/ses_089f1f6cfffeOFDJiZpnVMeJex.json
?? .omo/run-continuation/ses_08a01e102ffex0l05CD4YIFh2l.json
?? .omo/run-continuation/ses_08a2eb724ffeSeWmB2YfIQW2mL.json
?? .omo/run-continuation/ses_08a2ebba1ffe1FKct6YEvYtXVX.json
?? .omo/run-continuation/ses_08a3d8bb0ffe00igrWOj0B3POx.json
?? .omo/run-continuation/ses_08a3d8c54ffeMCQQmL9Pa0ZC4H.json
?? .omo/run-continuation/ses_08a3d9340ffedpznqUXBcY34WY.json
?? .omo/run-continuation/ses_08a4d14fcffeD7kDCqOq4wL2L8.json
?? .omo/run-continuation/ses_08a585f46ffeOqD9xPku57pauP.json
?? .omo/run-continuation/ses_08a67e6aaffeU1xcP5oAt13rtu.json
?? .omo/run-continuation/ses_08a67e741ffeaIl3q2PpnQrhsm.json
?? .omo/run-continuation/ses_08a67eb87ffe8x6U76b0R4zpr0.json
?? .omo/run-continuation/ses_08a74e17effeQcnriVAeVT4pdN.json
?? .omo/run-continuation/ses_08b39dc70ffemIK4C9GgO5z0AO.json
?? .omo/run-continuation/ses_08b39dea9ffe4D6vy1TP9Kcn8I.json
?? .omo/run-continuation/ses_08b3cad1bffeOsnszIH1e4X6rN.json
?? .omo/run-continuation/ses_08b3cadaaffewlpOnJOpqj09L9.json
?? .omo/run-continuation/ses_08b40d611ffezEZHH3KsyfetaU.json
?? .omo/run-continuation/ses_08ba1e178ffetVDAVVVSWhBGk1.json
?? .omo/run-continuation/ses_08bc3aed9ffec1Ne2mSFzQuzm0.json
?? .omo/run-continuation/ses_08bc3af34ffepnajXojZdqwFdZ.json
?? .omo/run-continuation/ses_08bc3aff7ffeC9jYMRpYWvzhbi.json
?? .omo/run-continuation/ses_08bcee345ffe1rHmUY32xkQfCs.json
```

## 3. Python 机械对比，Task 01 基线 vs F4 写前状态

执行方式：读取 `task-01-source-ledger.md` 里的基线 code block，再调用当前 live `git status --short --untracked-files=all` 做集合比较。

```text
BASELINE_COUNT 16
CURRENT_COUNT 48
STAGED_ENTRY_COUNT 0
FORBIDDEN_STATUS_HIT_COUNT 0
NEW_VS_BASELINE_COUNT 32
NEW_VS_BASELINE_CLASS runtime_state 13
NEW_VS_BASELINE_CLASS stage5_evidence 15
NEW_VS_BASELINE_CLASS stage5_notepad 4
REMOVED_VS_BASELINE_COUNT 0
```

### 3.1 对比解释

- `STAGED_ENTRY_COUNT 0`，当前索引区没有 staged 项，所以至少没有走到 Git stage 这一步。
- `FORBIDDEN_STATUS_HIT_COUNT 0`，当前状态里没有命中以下四个禁止路径：
  - `路遥/人生/《人生》阅读笔记.md`
  - `路遥/人生/《人生》微信读书提示词.md`
  - `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
  - `AGENTS.md`
- 相对 Task 01 基线新增的 32 条里，没有任何产品阅读材料路径。
- 这 32 条新增全都还在 `.omo` 下面，分成三类：
  - `stage5_evidence 15`，包括 Task 01 到 Task 13 证据文件，以及已存在的 `final-verification-f1-plan-compliance.md`、`final-verification-f3-reader-qa.md`
  - `stage5_notepad 4`，是本阶段 notepad 工件
  - `runtime_state 13`，是 `.omo/run-continuation/*.json` 运行时状态漂移
- `REMOVED_VS_BASELINE_COUNT 0`，没有把 Task 01 基线里的任何脏路径“洗掉”来伪造干净结果。

### 3.2 对 Stage 5 总体边界的判断

- 从 Task 01 基线走到当前写前状态，能看到的新增都属于 `.omo` 执行工件或运行时状态。
- 没有证据显示产品阅读笔记被改动。
- 没有证据显示《人生》两份 prompt 被改动。
- 没有证据显示根 `AGENTS.md` 被改动。

## 4. grep 与回读核验

### 4.1 Git stage/commit/push 痕迹

- 对 Stage 5 证据目录执行 `grep("git add|git commit|git push|stage/commit/push")`，只命中 4 条“禁止或已核验无痕迹”的记录：
  - `task-07-evidence-counterevidence.md:91`
  - `task-09-five-anomaly.md:65`
  - `task-10-writing-conversion.md:280`
  - `task-13-final-qa.md:60`
- 未发现任何一条把 Git stage、commit、push 写成“已执行”的成功记录。
- 与 `STAGED_ENTRY_COUNT 0` 合并判断，当前没有 staged 索引痕迹，也没有 on-disk 证据表明本轮实际执行了 Git stage/commit/push。

### 4.2 外部数据扩张与技术泄漏

- `grep("书友|高赞|external-only|微信读书|WeChat", include="task-12-final-output.md")` 结果为 `No matches found`。
- `grep("\\.omo|source ID|range|chapterUid|bookId|ledger|snapshot|task|wave|QA state", include="task-12-final-output.md")` 结果为 `No matches found`。
- `task-13-final-qa.md:27-28,42-43` 也复核过同一结论，确认终稿没有外部读者声音污染，也没有技术字段泄漏。
- 这说明 Stage 5 的 reader-facing 终稿没有把新抓取的 WeChat / external-reader 内容扩进正文，也没有把内部执行字段漏给读者。

### 4.3 跨书读取边界

- 对 Stage 5 证据目录执行 `grep("平凡的世界/")`，结果为 `No matches found`。
- `task-11-method-and-crosswork.md:35-44` 虽然做了《平凡的世界》联动，但每一行都把主锚点落回 `《人生》阅读笔记.md` 的本地行段，例如 `:94-98`、`:567-612`、`:133-137`、`:2061-2087`，并明确写着“《人生》的主证据仍须回到高加林自己的场景链”。
- 现有证据只显示“允许的跨作品比较路径”，没有显示去读取其他书目的阅读笔记文件，也没有显示 sibling-book `AGENTS` 或其他跨书本地笔记路径被引入本轮 Stage 5 证据。

### 4.4 产品文件与 prompt 文件保护

- 当前 live `git status` 不包含 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`。
- 当前 live `git status` 不包含两份 prompt：
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
- 当前 live `git status` 不包含 `/home/king/github/growing-myself/AGENTS.md`。
- `task-13-final-qa.md:31` 也已有一次同结论的独立 QA 记录。

## 5. F4 自身写入前后对比

### 5.1 F4 写入前快照

- 采用上文 `2.2` 的全仓状态作为本文件写入前快照。

### 5.2 F4 写入后的全仓 `git status --short --untracked-files=all`

```text
 M .omo/boulder.json
 M .omo/run-continuation/ses_09b346be6ffelwOUgFIFbq8h9K.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
 M .omo/start-work/ledger.jsonl
?? .omo/drafts/ren-sheng-stage5-question-compression.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f1-plan-compliance.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f2-analysis-quality.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f3-reader-qa.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-02-stage-boundary.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-03-question-pool.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-04-live-sentence-library.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-05-regression-sentinels.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-06-core-question-selection.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-07-evidence-counterevidence.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-08-tension-map.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-09-five-anomaly.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-10-writing-conversion.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-11-method-and-crosswork.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-12-final-output.md
?? .omo/evidence/ren-sheng-stage5-question-compression/task-13-final-qa.md
?? .omo/notepads/ren-sheng-stage5-question-compression/decisions.md
?? .omo/notepads/ren-sheng-stage5-question-compression/issues.md
?? .omo/notepads/ren-sheng-stage5-question-compression/learnings.md
?? .omo/notepads/ren-sheng-stage5-question-compression/problems.md
?? .omo/plans/ren-sheng-stage5-question-compression.md
?? .omo/run-continuation/ses_089e5be1fffeMTKpqNXAjqJIaa.json
?? .omo/run-continuation/ses_089e5cbecffeOYuWdV25kLvtnD.json
?? .omo/run-continuation/ses_089f1f6cfffeOFDJiZpnVMeJex.json
?? .omo/run-continuation/ses_08a01e102ffex0l05CD4YIFh2l.json
?? .omo/run-continuation/ses_08a2eb724ffeSeWmB2YfIQW2mL.json
?? .omo/run-continuation/ses_08a2ebba1ffe1FKct6YEvYtXVX.json
?? .omo/run-continuation/ses_08a3d8bb0ffe00igrWOj0B3POx.json
?? .omo/run-continuation/ses_08a3d8c54ffeMCQQmL9Pa0ZC4H.json
?? .omo/run-continuation/ses_08a3d9340ffedpznqUXBcY34WY.json
?? .omo/run-continuation/ses_08a4d14fcffeD7kDCqOq4wL2L8.json
?? .omo/run-continuation/ses_08a585f46ffeOqD9xPku57pauP.json
?? .omo/run-continuation/ses_08a67e6aaffeU1xcP5oAt13rtu.json
?? .omo/run-continuation/ses_08a67e741ffeaIl3q2PpnQrhsm.json
?? .omo/run-continuation/ses_08a67eb87ffe8x6U76b0R4zpr0.json
?? .omo/run-continuation/ses_08a74e17effeQcnriVAeVT4pdN.json
?? .omo/run-continuation/ses_08b39dc70ffemIK4C9GgO5z0AO.json
?? .omo/run-continuation/ses_08b39dea9ffe4D6vy1TP9Kcn8I.json
?? .omo/run-continuation/ses_08b3cad1bffeOsnszIH1e4X6rN.json
?? .omo/run-continuation/ses_08b3cadaaffewlpOnJOpqj09L9.json
?? .omo/run-continuation/ses_08b40d611ffezEZHH3KsyfetaU.json
?? .omo/run-continuation/ses_08ba1e178ffetVDAVVVSWhBGk1.json
?? .omo/run-continuation/ses_08bc3aed9ffec1Ne2mSFzQuzm0.json
?? .omo/run-continuation/ses_08bc3af34ffepnajXojZdqwFdZ.json
?? .omo/run-continuation/ses_08bc3aff7ffeC9jYMRpYWvzhbi.json
?? .omo/run-continuation/ses_08bcee345ffe1rHmUY32xkQfCs.json
```

### 5.3 F4 自身写前写后增量解释

```text
POST_COUNT 52
STAGED_ENTRY_COUNT 0
FORBIDDEN_STATUS_HIT_COUNT 0
NEW_VS_PRE_COUNT 4
NEW_VS_PRE_CLASS runtime_state 2
NEW_VS_PRE_CLASS stage5_evidence 2
REMOVED_VS_PRE_COUNT 0
NEW_VS_PRE_LINES_START
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f2-analysis-quality.md
?? .omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md
?? .omo/run-continuation/ses_089e5be1fffeMTKpqNXAjqJIaa.json
?? .omo/run-continuation/ses_089e5cbecffeOYuWdV25kLvtnD.json
NEW_VS_PRE_LINES_END
NEW_VS_BASE_COUNT 36
NEW_VS_BASE_CLASS runtime_state 15
NEW_VS_BASE_CLASS stage5_evidence 17
NEW_VS_BASE_CLASS stage5_notepad 4
```

- `NEW_VS_PRE_COUNT 4` 说明，从 F4 开始写入到写后复查这段时间，只多出 4 条路径。
- 这 4 条路径全部都在 `.omo` 下面，没有任何产品阅读材料、提示词或 `AGENTS.md`。
- 其中 `final-verification-f4-scope-fidelity.md` 是本 worker 必须新增的目标文件。
- `final-verification-f2-analysis-quality.md` 是并行 final wave 的 sibling evidence artifact，仍在允许的 Stage 5 evidence 目录下。
- 另外 2 条是 `.omo/run-continuation/*.json`，属于运行时状态漂移，不属于产品输出。
- `STAGED_ENTRY_COUNT 0` 与 `FORBIDDEN_STATUS_HIT_COUNT 0` 在写后仍保持为零，所以本次 F4 自身没有把改动扩散到禁止路径，也没有产生 staged 索引项。

## 6. Readback 与 LSP 结果

- `read("/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md")` 已回读通过，确认本文件实际落盘，并且同时包含：
  - Task 01 基线解释
  - F4 写前全仓 `git status`
  - F4 写后全仓 `git status`
  - Python 基线对比与写前写后增量结果
  - 明确结论行 `VERDICT: APPROVE`
- `lsp_diagnostics("/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/final-verification-f4-scope-fidelity.md")` 返回：`No LSP server configured for extension: .md`。
- 这与 `problems.md:4`、`learnings.md:7` 的既有环境结论一致，因此本轮 Markdown 校验继续以 readback、grep、Python 机械对比和 live `git status` 为准。

## 7. 结论与 caveats

- 本仓库原本就不是 clean worktree，不能拿“是否全绿”当通过条件。
- `.omo/run-continuation/*.json`、`.omo/boulder.json`、`.omo/start-work/ledger.jsonl` 属于运行时状态，不属于产品阅读材料。
- 相对 Task 01 基线，当前能看见的新增都落在 `.omo`，没有越界到《人生》阅读笔记、两份 prompt 或 `AGENTS.md`。
- 就现有 on-disk 证据、live `git status`、grep 结果和 Python 机械对比而言，没有发现未授权归档编辑、未授权 prompt 编辑、Git stage/commit/push、外部数据扩张，或超出现有锚点的跨书笔记读取。

VERDICT: APPROVE
