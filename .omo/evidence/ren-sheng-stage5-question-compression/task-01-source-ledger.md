# Task 01 Source Ledger, Stage 5 问题压缩前置台账

## 1. 任务边界与权威来源

- 本台账只服务 Stage 5 的证据化执行，不改产品阅读材料。
- 本任务的直接权威来源是 `/home/king/github/growing-myself/.omo/plans/ren-sheng-stage5-question-compression.md:58-120`。
- 其中必须继承的硬约束，集中见：
  - `:61-68`，证据根目录、分类规则、产品文件完整性检查。
  - `:69-82`，Stage 5 证据文件清单。
  - `:114-119`，Todo 1 的范围、引用源、验收标准、QA 场景。

## 2. Stage 5 输出边界

### 2.1 只允许的执行落点

- 本 worker 本次唯一允许新增或改动的执行路径，是：`.omo/evidence/ren-sheng-stage5-question-compression/`
- 本任务要求创建的文件是：`/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md`
- 后续 Stage 5 任务若继续执行，也只能把新增证据落到同一 evidence 目录下，不能越界到产品文件。

### 2.2 明确禁止的产品编辑

- Stage 5 最终输出不得修改 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`。
- 本任务也不得修改以下任何文件：
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
  - `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`
  - `/home/king/github/growing-myself/AGENTS.md`
  - `/home/king/github/growing-myself/.omo/plans/ren-sheng-stage5-question-compression.md`
  - `.omo/boulder.json`、各类 ledger、run-continuation 文件、以及任何 Git 状态本身
- `《人生》阅读笔记.md:5932-6040` 的“全书收束整合”只能当导航入口使用，不能被当作 Stage 5 证据正文去覆盖或替代原卡。

## 3. Source hierarchy A-D

> 使用顺序是从 A 到 D 逐级降权，不得倒置。A 是证据主仓，B 是导航，C 是规则，D 是补充联动。

### A级 用户原始卡片

**用途**

- Stage 5 的主证据层。
- 只要要压缩问题、提炼张力、建立证据表，优先回到用户卡片中的 `划线原文` 与 `我的原想法`。
- A 级材料优先于任何 AI 评价、文章索引和跨作品补充。

**精确来源路径与关键行段**

- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:3-5926`
  - `:3`，第 1 轮标题起点。
  - `:557`，第 2 轮标题起点。
  - `:1238`，第 3 轮标题起点。
  - `:1701`，第 4 轮标题起点。
- 可直接确认“用户原句 + 卡片结构”的窗口：
  - `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:15-37`，第 1 轮卡片内 `划线原文` 与 `我的原想法`。
  - `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:102-118`，第 1 轮卡片内跨人物比较问题，仍属于用户原想法。

**执行规则**

- A 级里的 `划线原文` 和 `我的原想法` 才能作为 Stage 5 后续压缩问题时的原始证据正文。
- 同一张卡里若同时有 `AI评价`、`AI修正`、`AI补充`，这些内容不能反客为主，只能回退为辅助判断。

### B级 第四阶段索引

**用途**

- 只做导航，不做证据本体。
- 作用是把 Stage 4 已经整理出的全书入口，映射回 A 级原卡所在区域。
- 不能把 B 级内容直接当成已经完成的证据表、问题池或文章正文。

**精确来源路径与关键行段**

- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5927-6040`
  - `:5927-5930`，全书整理完成位置，说明已转入全书回看阶段。
  - `:5932-5941`，`全书收束整合 > 阅读现场档案`，明确“四轮推进 + 卡片入口”。
  - `:5943-5957`，`文章素材索引` 起点，提供人物线、城乡主题等导航。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:83-88`
  - Router 对第四阶段的摘要，明确“先保住阅读现场和卡片本体，再建立文章方向导航”。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:146-158`
  - Router 级文章方向摘要，六条方向仅作总入口。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:33-40`
  - 第四阶段标准模型是 `阅读现场档案 + 文章素材索引`。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:144-196`
  - 明确正式阅读笔记中的全书结构与文章素材索引表头。

**执行规则**

- B 级只能回答“去哪里找卡”，不能回答“这张卡的证据已经充分”。
- 若某条 Stage 4 文章方向没有回指到 A 级原卡或用户原句，就不能拿来进入 Stage 5 的核心问题压缩。

### C级 提示词规则

**用途**

- 规定 Stage 5 的方法、文件边界、文本优先级和归档禁区。
- 用来约束后续 worker 的读法与写法，不直接替代文本证据。

**精确来源路径与关键行段**

- `/home/king/github/growing-myself/AGENTS.md:3-24`
  - 项目定位，强调“保留用户真实、有文气的反应，同时更深、更准、更贴文本”。
  - 五异法、问题阶梯、张力地图是强制方法词。
- `/home/king/github/growing-myself/AGENTS.md:63-84`
  - 处理整理与评价边界，外部读者材料只能做补充，不能替代用户判断。
- `/home/king/github/growing-myself/AGENTS.md:99-117`
  - 提问与视角补充规则，归档结构，文件与 Git 规则，尤其 `:107-112` 的“我自己写的内容 / AI评价 / AI修正 / AI补充”结构，和 `:116` 的“未经要求不要碰其他阅读材料”。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:28-64`
  - 《人生》的固定路径、双 `bookId`、执行前必读、不可降级原则与任务入口门。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:121-133`
  - 进入第四阶段前的检查与 Git 边界。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md:213-217`
  - 快捷请求路由，`全书收束整合` 必须走第四阶段文件，`只咨询规则` 留在 router。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:1-27`
  - 继承与执行边界，明确第四阶段输入输出文件、冲突规则、触发门、must not。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:68-77`
  - 第三阶段与第四阶段的分工，第四阶段不是重跑第三阶段。
- `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md:240-250`
  - 外部读者材料与正式稿膨胀防控，锚点必须可读，不能写技术坐标进正文。

**执行规则**

- C 级负责划边界，不负责替代 A 级细读。
- 任何 Stage 5 产出若违反 C 级规则，即使文字好看，也算失败。

### D级 跨作品联动

**用途**

- 只在 A 级卡片已经站稳后，作为补充比较材料或问题推进材料使用。
- 不允许用 D 级联动替代《人生》本书内部证据。

**精确来源路径与关键行段**

- `/home/king/github/growing-myself/AGENTS.md:96-102`
  - 根规则要求跨作品联动要说明联动路径，而不是只堆书名。
- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:27-55`
  - 第 1 轮卡片中已经出现《平凡的世界》、孙少平、孙家白面馍伦理等联动，是 D 级的现成本地来源。
- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:100-137`
  - “两种自尊”卡片把高加林和孙少平并置比较，并明确形成 `跨作品联动` 条目。
- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md:5944-5957`
  - 全书索引里的“人物线 / 城乡主题”继续保留可回链锚点，但仍应回到原卡核实。

**执行规则**

- D 级只能建立“比较路径”，不能直接承担《人生》文本的主证据职能。
- 若某个跨作品判断在 A 级卡片里没有用户原句或场景锚点支撑，就只能保留为待回看，不得强行纳入核心问题。

## 4. Source-text 分类规则

以下四类定义，直接继承自计划 `/home/king/github/growing-myself/.omo/plans/ren-sheng-stage5-question-compression.md:63-67`。

- `用户原句`
  - 定义：用户写在阅读笔记中的原话。
  - 用法：直接保留，明确标注为用户声音。
- `卡片内小说短语/场景锚点`
  - 定义：已经写进阅读笔记卡片里的小说措辞、场景描述、引文短句。
  - 用法：可以做分析锚点，但若要当作严格的小说原文逐字引用，必须标 `待原文复核`。
- `AI概括`
  - 定义：阅读笔记中现成的 `AI评价`、`AI修正`、`AI补充`。
  - 用法：只能帮助整理问题和判断，不能替代用户原句，也不能替代小说证据。
- `AI自行回忆的小说原文`
  - 定义：AI 未经本地来源复核，凭记忆补写的《人生》小说原文。
  - 状态：**禁止**。

## 5. 读取边界与执行口径

- `《人生》阅读笔记.md` 是 Stage 5 的主读取对象，但本阶段只读，不写。
- Stage 4 的 `文章素材索引` 是导航，不是证据正文。
- 后续 worker 若要提炼核心问题，必须遵守这个顺序：
  1. 先从 B 级索引找到候选卡。
  2. 再回到 A 级卡片抽取 `划线原文`、`我的原想法`、场景锚点。
  3. 之后才允许用 C 级规则收束问题质量。
  4. 最后才考虑 D 级跨作品联动是否有推进价值。

## 6. Pre-execution full-repo status baseline

采集命令：`git status --short --untracked-files=all`

采集位置：`/home/king/github/growing-myself`

采集结果，按命令原样记录如下：

```text
 M .omo/boulder.json
 M .omo/run-continuation/ses_09b346be6ffelwOUgFIFbq8h9K.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
 M .omo/start-work/ledger.jsonl
?? .omo/drafts/ren-sheng-stage5-question-compression.md
?? .omo/plans/ren-sheng-stage5-question-compression.md
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

**基线解释**

- 执行前仓库已经是 dirty worktree，不是空仓状态。
- 因此后续校验不能误判成“必须全仓 clean”，而要比较“本 worker 是否只新增了允许路径下的证据文件”。
- 对本 worker 来说，唯一允许新增的路径仍然只有 `.omo/evidence/ren-sheng-stage5-question-compression/`。

### 6.1 Post-write status comparison note

- 同样使用 `git status --short --untracked-files=all` 做写后对比时，应按“相对第 6 节基线的增量”解释结果，不按“仓库是否完全干净”解释结果。
- 本次 Todo 1 的预期 Stage 5 产出增量，只有 `/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md` 这一条 artifact 路径。
- `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` 以及同目录下的 prompt/router 文件，在写前基线与写后对比里都应保持未改动；若这些产品文件出现变更，即判失败。
- `.omo/run-continuation/*.json` 若在写后对比中新增、消失或数量变化，应解释为 orchestration/runtime state，由客户端续跑机制生成，不属于 Stage 5 产品输出，也不能被误记为阅读材料改动。
- `.omo/boulder.json`、`.omo/start-work/ledger.jsonl`、`.omo/drafts/ren-sheng-stage5-question-compression.md`、`.omo/plans/ren-sheng-stage5-question-compression.md` 等若继续保持脏状态，应按“基线已存在的非产品仓库状态”处理，不把它们误判成这次 Stage 5 artifact 写入造成的产品污染。

## 7. Verification plan

### 7.1 Happy checks

1. `read(filePath="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression/task-01-source-ledger.md")`
   - 确认四个 source level，`A级 用户原始卡片`、`B级 第四阶段索引`、`C级 提示词规则`、`D级 跨作品联动` 全部存在。
   - 确认 `用户原句`、`卡片内小说短语/场景锚点`、`AI概括`、`AI自行回忆的小说原文` 四项定义全部存在。
   - 确认“Stage 5 最终输出不得修改 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`”写明。
   - 确认 pre-execution `git status --short --untracked-files=all` 基线已原样记录。
   - 确认唯一允许执行路径 `.omo/evidence/ren-sheng-stage5-question-compression/` 已写明。
2. `git status --short --untracked-files=all`
   - 对比第 6 节基线，确认本 worker 只新增 evidence 目录下的本文件，没有把变化扩散到产品阅读材料或规则文件。

### 7.2 Failure checks

1. `grep(pattern="修改.*《人生》阅读笔记|写入.*《人生》阅读笔记", path="/home/king/github/growing-myself/.omo/evidence/ren-sheng-stage5-question-compression", include="task-01-source-ledger.md", output_mode="content")`
   - 若台账把 Stage 5 说成要写回 `《人生》阅读笔记.md`，则边界定义失败，必须重写。
   - 安全结果允许命中“不得修改”这类禁止语句，或命中这条校验命令本身；只有出现肯定式写回指令，才算失败。
2. `git status --short --untracked-files=all`
   - 若出现由本 worker 造成的 evidence 目录外新增或修改路径，则完整性检查失败，必须先回退或明确报告。
3. 人工抽读
   - 若 B 级被写成“证据正文”而不是“导航”，则任务失败。
   - 若 D 级跨作品联动没有回落到本地已有锚点，而是直接外扩想象，则任务失败。

## 8. UltraQA probe

| UltraQA class | 处理结果 | 一行理由 |
| --- | --- | --- |
| `malformed_input` | N/A | 本任务输入是明确的单文件修补与固定 9 类校验项，没有出现损坏路径、缺字段或不可解析输入需要恢复。 |
| `prompt_injection` | N/A | 本次只读取用户明确指定的本地计划/规则/证据文件，没有引入外部网页、远端数据或需执行的非可信提示源。 |
| `cancel_resume` | N/A | 本次验证修补过程中没有发生取消后恢复执行的情形，因此无需建立额外的 resume 补偿流程。 |
| `stale_state` | PASS | 已先读取计划、根规则、router、第四阶段文件与阅读笔记标题窗口，再写台账，避免用旧记忆代替本地现状。 |
| `dirty_worktree` | PASS | 已记录执行前全仓 `git status` 基线，并把“只允许 evidence 目录新增”写成硬边界。 |
| `hung_or_long_commands` | N/A | 本任务只用了 read/grep/git status 这类短命令，没有长跑任务、阻塞脚本或需要超时恢复的命令链。 |
| `flaky_tests` | N/A | 这里没有测试套件可跑，验收依赖 readback、grep 和 git status 这类确定性检查，不存在测试摇摆问题。 |
| `misleading_success_output` | PASS | 成功标准不是“文件创建了”而是“文件内含四级来源、分类规则、只读边界、基线与 QA”，缺一项都不算完成。 |
| `repeated_interruptions` | PASS | 本任务只依赖本地文件与本地 Git 状态，任何中断或额度提示都不能替代证据输出，恢复后仍以本地读回为准。 |

## 9. Worker handoff note

- Todo 2 到 Todo 5 的后续 worker，应把本文件当作 Stage 5 的固定入口，不要再重定义来源等级。
- 若后续任务需要引用第四阶段文章方向，必须先从本文件的 B 级入口找到锚点，再回源到 A 级卡片。
- 若后续任务发现某条判断只有 `AI概括` 而没有用户原句或场景锚点，应降级为待核，不得直接入核心问题池。
