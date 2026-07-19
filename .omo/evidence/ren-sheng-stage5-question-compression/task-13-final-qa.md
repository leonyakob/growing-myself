# Task 13 Final QA，`《人生》` Stage 5 终稿护栏审计

## 结论

- 审计结论：`PASS`
- `task-12-final-output.md` 是否需要回补：`否`
- 本轮发现的唯一持续边界提醒：所有带 `待原文复核` 的短语仍只到读书卡片锚点这一级，后续若要落成小说逐字引文，仍须回原书核对。

## QA 表

| Check | Status | Evidence | If failed / correction |
| --- | --- | --- | --- |
| 恰好三道核心问题 | PASS | `task-12-final-output.md:7-31` 只有 `### 问题一/二/三` 三个核心题头。机械检查结果：`CORE_QUESTION_HEADINGS 3`，`EXTRA_CORE_LIKE 0`。 | 无需修正。 |
| 写作支路没有偷偷长成第四问或第五问 | PASS | `task-12-final-output.md:137-161` 只出现 `问题一的写作支路`、`问题二的写作支路`、`问题三的写作支路`。`grep("问题四|问题五|第四个核心问题|第五个核心问题")` 结果 `0` 命中。 | 无需修正。 |
| 三题前面都保住了用户原句引信 | PASS | `task-12-final-output.md:11-13`、`21-25`、`33-37` 都先给 `用户原句引信`。机械检查结果：`USER_TRIGGER_COUNT 3`，`BLOCKQUOTE_COUNT 5`。 | 无需修正。 |
| 用户原句与分析压缩有明确区分 | PASS | `task-12-final-output.md:11-17`、`21-29`、`33-41` 都按 `用户原句引信` 和 `分析压缩` 分栏，未把分析伪装成原句。 | 无需修正。 |
| 活句没有被 AI 平滑覆盖 | PASS | Q1 引信与 `task-04-live-sentence-library.md:20-27` 同句，仅补了句末标点。Q2 两句引信对应 `task-04-live-sentence-library.md:108-115`、`75-82`。Q3 两句引信对应 `task-04-live-sentence-library.md:174-181`、`119-126`。机械比对结果 5 段引信中 4 段全文精确命中 Task 04，Q1 为同句加句末句号。 | 无需修正。若后续正式归档要求逐字对齐，可只回收 Q1 句末标点，不动正文分析。 |
| 三问机制不重叠 | PASS | `task-12-final-output.md:17` 写安身位置，`:29` 写外部目光机制，`:41` 写权利先行与责任后撤。`task-12-final-output.md:221-223` 也自检区分了三问。对应的非重叠证明见 `task-06-core-question-selection.md:42-55`。 | 无需修正。 |
| 每题都有足够正证覆盖 | PASS | `task-12-final-output.md:45-77` 三张证据表都含多条正证。机械计数结果：`问题一 4 正证`，`问题二 5 正证`，`问题三 4 正证`。 | 无需修正。 |
| 每题都有反证/复杂化覆盖 | PASS | `task-12-final-output.md:53-54`、`65-66`、`76-77` 分别给出三题的反证/复杂化。机械计数结果：三题各 `2` 条反证/复杂化。 | 无需修正。 |
| 承重判断都能回到原卡或场景锚点，不靠 Stage 4 总括句撑住 | PASS | `task-12-final-output.md:49-76` 证据表全部用自然场景锚点，`83-95` 张力图也继续用 `回乡卖馍`、`广播站灯光`、`亲吻后刷牙`、`同车去县城`、`分手前先怕自己下不了台` 这类场面。`grep("Stage 4|第四阶段|阅读轨迹|文章素材索引")` 在 reader-facing 终稿中 `0` 命中。原卡回链依据见 `task-07-evidence-counterevidence.md:18-24`、`40-47`、`63-69`。 | 无需修正。 |
| 全书张力地图有具体锚点，不是抽象主题对词 | PASS | `task-12-final-output.md:79-95` 每一行都钉在具体场景上。它和 `task-08-tension-map.md:15-28` 的 TM-01 到 TM-14 对应稳定。 | 无需修正。 |
| 五异法五类齐全，而且每类都有锚点 | PASS | `task-12-final-output.md:99-107` 五类全列出，`109-135` 给出 7 个细读点。前序锚点依据见 `task-09-five-anomaly.md:19-25` 与 `31-40`。 | 无需修正。 |
| 五异法类别检查没有伪造“材料不足” | PASS | `task-12-final-output.md:103-107` 五类状态全部写 `充足`，且前序 `task-09-five-anomaly.md:56-57` 已确认五类都各有支撑点，没有硬造 `材料不足`。 | 无需修正。 |
| `待原文复核` 边界诚实，未把读书卡片短语冒充定本引文 | PASS | `task-12-final-output.md:189-215` 列出 9 个高频复核项，`:246` 再次声明这些短语只适合先当阅读锚点。另有一过性短语，如 `最好把巧珍也带出去` 见 `:76`，`有时` 见 `:119`，都已 inline 标 `待原文复核`。机械检查结果：`REVIEW_LINE_COUNT 29`。 | 无需修正。若后续要把一过性短语也集中入表，可另行增补，但当前已满足“清单列出或正文 inline 标注”口径。 |
| 没有未标注的假引文或假证据 | PASS | `grep("TODO|FIXME|HACK|TBD|待补|占位|placeholder|xxx")` 在 `task-12-final-output.md` 中 `0` 命中。全文回读未见把未核对短语写成已校原文的情况。所有高风险短语都落进 `待原文复核` 清单或正文 inline 标注。 | 无需修正。 |
| 无外部读者声音污染 | PASS | `grep("书友|高赞|external-only")` 在 `task-12-final-output.md` 中 `0` 命中。终稿只使用本轮已收束的本书场景与允许的跨作品联动，不引入新书友评论。 | 无需修正。 |
| reader-facing 终稿没有技术字段泄漏 | PASS | `grep("source ID|range|chapterUid|bookId|ledger|snapshot|task|wave|QA state|\\.omo")` 在 `task-12-final-output.md` 中 `0` 命中。 | 无需修正。 |
| 关键人物没有被写扁 | PASS | 开头总述 `task-12-final-output.md:5` 先声明人物都不该只剩一种标签。反证行 `:53-54`、`:65-66`、`:76-77` 分别保住土地回甜、真被打动、巧珍主动性、黄亚萍真实吸引力。自检段 `:223-229` 进一步点明最容易写坏的三种扁平化。对应哨兵见 `task-05-regression-sentinels.md:21-30`。 | 无需修正。 |
| 没有把巧珍，黄亚萍，德顺压成单一功能件 | PASS | `task-12-final-output.md:77` 写明巧珍并非纯受害者，黄亚萍也有真实吸引力和向远人生版本。`:223` 说德顺不是只会讲大道理。对应保护规则见 `task-05-regression-sentinels.md:22-25`。 | 无需修正。 |
| 没有产品文件改动，也没有碰提示词和 AGENTS | PASS | `git status --short --untracked-files=all` 输出只见 `.omo` runtime 状态、plan、evidence、notepads 等既有脏仓路径，未见 `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`，未见两份提示词文件，未见 `/home/king/github/growing-myself/AGENTS.md`。 | 无需修正。若后续 git status 出现这些路径，必须先回退再继续。 |
| Todo 12 仍是后续最终回复的唯一依据 | PASS | 计划文件 `ren-sheng-stage5-question-compression.md:202-207` 明写 `task-12-final-output.md` 是最终回复依据。此次 QA 全程围绕该文件核验，且未发现需要改写的 concrete failure。 | 无需修正。后续真正给用户的 Stage 5 reader-facing 终稿，仍必须以 `task-12-final-output.md` 为底稿，不可改用 QA 语言。 |
| 本轮无需对 Todo 12 回补 | PASS | 全表无 `FAIL` 行，所有强制检查均已通过，因此 `task-12-final-output.md` 本轮保持原样。 | 无需修正。若后续 F1-F4 再发现 concrete failure，再单点补丁并重跑 QA。 |

## 验证命令与结果

1. `read`
   - 已读 `plan` Todo 13 窗口，`task-12-final-output.md` 全文，`task-04` 到 `task-11`，以及 notepads 四个文件。
   - 结果：QA 范围，前序依据，活句库，反证表，张力图，五异法，写作支路，写法档案，跨作品路径都已对齐。

2. `grep`
   - `grep("source ID|range|chapterUid|bookId|ledger|snapshot|task|wave|QA state|\\.omo")`，结果 `0` 命中。
   - `grep("问题四|问题五|第四个核心问题|第五个核心问题|书友|高赞|bookId|chapterUid|range|source ID|ledger|snapshot|wave|QA state")`，结果 `0` 命中。
   - `grep("TODO|FIXME|HACK|TBD|待补|占位|placeholder|xxx")`，结果 `0` 命中。
   - `grep("^### 问题[一二三四五六七八九十]")`，结果只命中 `问题一/二/三` 及其证据表，写作支路和复核清单仍是 subordinate 标题。
   - `grep("回乡卖馍|广播站|刷牙|同车去县城|下不了台|庄稼地里|豆芽菜|乡巴佬|履历表")`，结果命中 36 处，说明承重场景仍在正文内可见。

3. `python3` 机械检查
   - 结果一：`CORE_QUESTION_HEADINGS 3`，`EXTRA_CORE_LIKE 0`，`USER_TRIGGER_COUNT 3`，`ANALYSIS_COUNT 3`，九个必需 `##` 区块齐全。
   - 结果二：`BLOCKQUOTE_COUNT 5`，其中 Q2/Q3 引信全文命中 Task 04，Q1 为同句加句末句号。
   - 结果三：证据表计数为 `问题一 4 正证 / 2 反证`，`问题二 5 正证 / 2 反证`，`问题三 4 正证 / 2 反证`。
   - 结果四：`待原文复核` 清单 9 项齐全，另有少量一过性短语采用正文 inline 标注而非清单重列。

4. `lsp_diagnostics`
   - 对 `task-12-final-output.md` 调用结果：`No LSP server configured for extension: .md`。
   - 本环境无 Markdown LSP，按 notepad 既定口径，改用 readback，grep，Python 机械检查和 git status 做确定性验证。

5. `git status --short --untracked-files=all`
   - 当前仓库本来就是脏工作区，含 `.omo/boulder.json`、`.omo/start-work/ledger.jsonl`、若干 `.omo/run-continuation/*.json`、既有 plan/evidence/notepads 路径。
   - 本次 QA 没有把改动扩散到 `《人生》阅读笔记.md`、两份提示词文件、`AGENTS.md`，也没有任何 stage/commit/push 痕迹。

## 修正记录

- 本轮未发现必须先修再过的 concrete failure。
- 因此 `task-12-final-output.md` 未改动。

## 最终判定

`task-12-final-output.md` 已通过 Todo 13 要求的终稿护栏审计，可以作为后续最终 reader-facing 回复的唯一底稿继续向前走。本文件本身是技术 QA 记录，不可直接替代读者可见终稿。
