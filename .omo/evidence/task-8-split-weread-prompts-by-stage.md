# Task 8 Evidence, split-weread-prompts-by-stage

Source snapshot used:

- Live source: `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`
- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- Snapshot timing note: created in this Task 8 preflight before any router rewrite or any 《人生》 stage file creation.

```text
sha256sum "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"
906484dc2ab7a72c171775b49a21da6fe158356239337e3b9cddc69feda811c3  /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md
906484dc2ab7a72c171775b49a21da6fe158356239337e3b9cddc69feda811c3  /home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md
```

```text
wc -l "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"
  1269 /home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md
  1269 /home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md
  2538 total
```

```text
cmp -s "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'
SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS
```

Applicable AGENTS.md:

- Required root rule file: `/home/king/github/growing-myself/AGENTS.md`
- Same-book rule file check: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` does not exist at execution time, so Task 8 records root `AGENTS.md` only.
- Explicitly not imported: `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` and any sibling-book `AGENTS.md`.
- Rule consequence for later Wave 2 prompts: 《人生》 router and future stage prompts must require the root `AGENTS.md`; they must not invent a same-book `AGENTS.md` dependency while that file remains absent.

Files changed:

- `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md`
- `/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only; added after evidence completion)

Commands run:

- `ls "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage"`
- `ls "/home/king/github/growing-myself/.omo/evidence"`
- `ls "/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage"`
- `cp --preserve=all "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`
- `sha256sum "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`
- `wc -l "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`
- `cmp -s "/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md" "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'`
- `python3 - <<'PY' ... wave-2 target-file existence preflight ... PY`
- `python3 - <<'PY' ... immutable snapshot heading inventory with line numbers ... PY`
- `python3 - <<'PY' ... semantic normative-line candidate scan for ledger drafting ... PY`
- `functions.read` on `/home/king/github/growing-myself/AGENTS.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-7-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` ranges `1-918` and `919-1269`
- `functions.read` on `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- `functions.read` on `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md"`
- `GIT_MASTER=1 git diff --no-index --check /dev/null "/home/king/github/growing-myself/.omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git diff --check -- ".omo/notepads/split-weread-prompts-by-stage/learnings.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "CB_2tb79r78T38k74M75h8iz4C3" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "25164497" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 003" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 006" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 021" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 109" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "ID 117" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "刘玉海救灾处" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`
- `GIT_MASTER=1 git grep -F --untracked -n "黄亚萍的物质付出" -- ".omo/evidence/task-8-split-weread-prompts-by-stage.md"`

Target-file existence preflight:

| target path | status | result |
|---|---|---|
| `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` | EXISTS | PASS |
| `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第一阶段-生成中间整理稿.md` | MISSING | PASS |
| `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第二阶段-优化中间整理稿.md` | MISSING | PASS |
| `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第三阶段-迁移到正式阅读笔记.md` | MISSING | PASS |
| `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` | MISSING | PASS |

Anchor-range coverage from plan:

| plan anchor | snapshot meaning | disposition | status |
|---:|---|---|---|
| `1` | source title | 《人生》 router | PASS |
| `5` | fixed paths | 《人生》 router | PASS |
| `22` | task-entry gate | 《人生》 router | PASS |
| `34` | four-stage flow | 《人生》 router | PASS |
| `127` | Stage 1 data hard constraints | 《人生》 Stage 1 | PASS |
| `213` | dual `bookId` mapping inside public-review lookup rules | intentional duplication | PASS |
| `328` | literary-analysis quality rules | 《人生》 Stage 2 | PASS |
| `540` | Stage 1 execution template | 《人生》 Stage 1 | PASS |
| `825` | Stage 3 migration rules | 《人生》 Stage 3 | PASS |
| `957` | Stage 4 whole-book consolidation rules | 《人生》 Stage 4 | PASS |
| `1259` | 7 regression sentinels | intentional duplication | PASS |

Heading inventory

- Inventory source: immutable snapshot only.
- Inventory result: every snapshot heading/subheading below has exactly one disposition. `explicit out-of-scope stop` count is `0`.

| line | level | heading | disposition | note |
|---:|---:|---|---|---|
| 1 | 1 | 《人生》微信读书整理提示词 | 《人生》 router | 总入口标题，统领 book-specific 路由与权威约束。 |
| 22 | 2 | 0. 不可降级原则与任务入口门 | 《人生》 router | 任务入口门、授权门和不可降级原则归 router。 |
| 34 | 2 | 1. 四阶段总流程 | 《人生》 router | 四阶段总流程与阶段边界概览归 router。 |
| 63 | 2 | 2. 多轮整理规则 | 《人生》 router | 多轮整理的轮次策略归 router。 |
| 70 | 2 | 第1轮整理：开头至第六章 | intentional duplication | 轮次标题示例既是 router 说明例子，也会在 Stage 1 模板重现。 |
| 72 | 2 | 第2轮整理：第七章至第十章 | intentional duplication | 轮次标题示例既是 router 说明例子，也会在 Stage 1 模板重现。 |
| 74 | 2 | 第3轮整理：…… | intentional duplication | 轮次标题示例既是 router 说明例子，也会在 Stage 1 模板重现。 |
| 87 | 2 | 3. 阶段切换前 QA 与条件性 Git 检查点 | 《人生》 router | 阶段切换 QA 与条件性 Git 授权门归 router。 |
| 127 | 2 | 4. 数据抓取硬约束 | 《人生》 Stage 1 | 数据抓取硬约束主体属于第一阶段执行工单。 |
| 134 | 3 | 4.0 中间整理稿与正式稿的数据边界 | 《人生》 Stage 1 | 中间稿与正式稿的数据边界先在 Stage 1 落地。 |
| 159 | 3 | 4.1 跨段划线与想法匹配规则 | 《人生》 Stage 1 | 跨段匹配规则属于第一阶段匹配逻辑。 |
| 203 | 3 | 4.2 同位置其他书友高赞想法默认伴随抓取规则 | intentional duplication | 同位置公开想法规则和双 bookId 映射既要在 router 摘要保留，也要在 Stage 1 详细执行。 |
| 273 | 2 | 5. 颜色默认流向 | 《人生》 Stage 1 | 颜色默认流向属于第一阶段整理输出规范。 |
| 302 | 2 | 6. 想法类别与卡片类型 | 《人生》 Stage 1 | 想法类别与卡片类型用于第一阶段轻量预分类。 |
| 304 | 3 | 6.1 想法类别 | 《人生》 Stage 1 | 想法类别用于第一阶段轻量预分类。 |
| 315 | 3 | 6.2 卡片类型 | 《人生》 Stage 1 | 卡片类型用于第一阶段轻量预分类。 |
| 328 | 2 | 7. 文学分析质量规则 | 《人生》 Stage 2 | 文学分析质量规则主体属于第二阶段。 |
| 336 | 3 | 7.1 证据锚点与文本落点 | 《人生》 Stage 2 | 证据锚点与文本落点属于第二阶段细读规则。 |
| 353 | 3 | 7.2 人物心理要写出过程，不要直接贴标签 | 《人生》 Stage 2 | 人物心理过程规则属于第二阶段细读规则。 |
| 380 | 3 | 7.3 文本歧义与心理雾区不能一笔带过 | 《人生》 Stage 2 | 心理雾区与歧义辨析属于第二阶段细读规则。 |
| 395 | 3 | 7.4 完整卡和主卡候选必须打开矛盾 | 《人生》 Stage 2 | 张力打开规则属于第二阶段。 |
| 410 | 3 | 7.5 AI 要提供表达增量 | 《人生》 Stage 2 | 表达增量规则属于第二阶段。 |
| 431 | 3 | 7.6 AI 可以反驳，但必须指出缺失的分析环节 | 《人生》 Stage 2 | 反驳与补桥规则属于第二阶段。 |
| 451 | 3 | 7.7 大胆分析，但不要省掉过程 | 《人生》 Stage 2 | 大胆分析但写出过程属于第二阶段。 |
| 459 | 3 | 7.8 升级问题链后必须给出阶段性回答 | 《人生》 Stage 2 | 双层问题链与阶段性回答属于第二阶段。 |
| 500 | 3 | 7.9 AI修正必须深化，不只是整理语序 | 《人生》 Stage 2 | AI修正深化规则属于第二阶段。 |
| 511 | 3 | 7.10 文学表达不是轻卡专属 | 《人生》 Stage 2 | 文学表达要求属于第二阶段。 |
| 527 | 3 | 7.11 分析后命名，而非先命名硬套 | 《人生》 Stage 2 | 分析后命名规则属于第二阶段。 |
| 540 | 2 | 8. 第一阶段：生成中间整理稿 | 《人生》 Stage 1 | 第一阶段执行提示属于 Stage 1。 |
| 564 | 3 | 中间整理稿格式 | 《人生》 Stage 1 | 中间整理稿格式属于 Stage 1。 |
| 567 | 1 | 路遥《人生》中间整理稿 | 《人生》 Stage 1 | 中间整理稿模板标题属于 Stage 1。 |
| 569 | 2 | 整理说明 | 《人生》 Stage 1 | 整理说明模板属于 Stage 1。 |
| 577 | 2 | 第N轮整理：范围说明 | 《人生》 Stage 1 | 轮次整理模板属于 Stage 1。 |
| 579 | 3 | 001. 章节名 / range | 《人生》 Stage 1 | 单条材料模板属于 Stage 1。 |
| 618 | 2 | 本轮索引 | 《人生》 Stage 1 | 本轮索引模板属于 Stage 1。 |
| 620 | 3 | 轻卡清单 | 《人生》 Stage 1 | 轻卡清单模板属于 Stage 1。 |
| 622 | 3 | 完整卡候选 | 《人生》 Stage 1 | 完整卡候选模板属于 Stage 1。 |
| 624 | 3 | 主卡候选 | 《人生》 Stage 1 | 主卡候选模板属于 Stage 1。 |
| 626 | 3 | 暂存素材 | 《人生》 Stage 1 | 暂存素材模板属于 Stage 1。 |
| 628 | 3 | 外部读者精彩高赞想法候选 | 《人生》 Stage 1 | 外部读者候选模板属于 Stage 1。 |
| 630 | 3 | 颜色统计 | 《人生》 Stage 1 | 颜色统计模板属于 Stage 1。 |
| 632 | 3 | 下次接着整理位置 | 《人生》 Stage 1 | 下次接着整理位置模板属于 Stage 1。 |
| 637 | 2 | 9. 第二阶段：优化中间整理稿 | 《人生》 Stage 2 | 第二阶段执行提示属于 Stage 2。 |
| 653 | 3 | 9.1 本轮优化前诊断 | 《人生》 Stage 2 | 优化前诊断说明属于 Stage 2。 |
| 658 | 2 | 第N轮优化前诊断 | 《人生》 Stage 2 | 优化前诊断模板标题属于 Stage 2。 |
| 695 | 3 | 9.2 轻卡优化规则 | 《人生》 Stage 2 | 轻卡优化规则属于 Stage 2。 |
| 723 | 3 | 9.3 完整卡 / 主卡优化规则 | 《人生》 Stage 2 | 完整卡 / 主卡优化规则属于 Stage 2。 |
| 786 | 3 | 9.4 暂存素材处理规则 | 《人生》 Stage 2 | 暂存素材处理规则属于 Stage 2。 |
| 801 | 3 | 9.5 高赞想法差异分析规则 | 《人生》 Stage 2 | 高赞想法差异分析规则属于 Stage 2。 |
| 825 | 2 | 10. 第三阶段：迁移到正式阅读笔记 | 《人生》 Stage 3 | 第三阶段迁移提示属于 Stage 3。 |
| 848 | 3 | 10.1 迁移前回源预检清单 | 《人生》 Stage 3 | 迁移前回源预检属于 Stage 3。 |
| 858 | 3 | 10.2 正式阅读笔记结构与去除中间稿痕迹 | 《人生》 Stage 3 | 正式阅读笔记结构规则属于 Stage 3。 |
| 896 | 3 | 10.3 正式阅读笔记游标更新规则 | 《人生》 Stage 3 | 正式稿游标更新规则属于 Stage 3。 |
| 908 | 3 | 10.4 所有材料最终都要有归宿 | 《人生》 Stage 3 | 材料归宿规则属于 Stage 3。 |
| 921 | 3 | 10.5 外部读者精彩高赞想法迁移规则 | 《人生》 Stage 3 | 外部读者高赞迁移规则属于 Stage 3。 |
| 941 | 3 | 10.6 迁移后防回归 QA 与最终验证波次 | 《人生》 Stage 3 | 迁移后防回归 QA 属于 Stage 3。 |
| 957 | 2 | 11. 第四阶段：读完整本书后的全书收束整合 | 《人生》 Stage 4 | 第四阶段全书收束提示属于 Stage 4。 |
| 974 | 3 | 11.1 默认模型与成品边界 | 《人生》 Stage 4 | 默认模型与成品边界属于 Stage 4。 |
| 987 | 3 | 11.2 第三阶段与第四阶段的分工 | 《人生》 Stage 4 | 第三阶段与第四阶段分工属于 Stage 4。 |
| 997 | 3 | 11.3 内部整合台账与多轴台账规则 | 《人生》 Stage 4 | 内部整合台账与多轴台账属于 Stage 4。 |
| 1025 | 3 | 11.4 一卡双归宿与全书级结构 | 《人生》 Stage 4 | 一卡双归宿规则属于 Stage 4。 |
| 1038 | 3 | 11.5 阅读现场档案结构与文章素材索引结构 | 《人生》 Stage 4 | 阅读现场档案与文章素材索引结构属于 Stage 4。 |
| 1051 | 2 | 全书收束整合 | 《人生》 Stage 4 | 全书收束整合骨架标题属于 Stage 4。 |
| 1053 | 3 | 一、阅读现场档案 | 《人生》 Stage 4 | 阅读现场档案骨架属于 Stage 4。 |
| 1056 | 4 | 1. 轻卡存档 | 《人生》 Stage 4 | 轻卡存档骨架属于 Stage 4。 |
| 1058 | 4 | 2. 完整卡 | 《人生》 Stage 4 | 完整卡骨架属于 Stage 4。 |
| 1060 | 4 | 3. 核心卡 | 《人生》 Stage 4 | 核心卡骨架属于 Stage 4。 |
| 1062 | 4 | 4. 外部读者随卡补充 | 《人生》 Stage 4 | 外部读者随卡补充骨架属于 Stage 4。 |
| 1064 | 3 | 二、文章素材索引 | 《人生》 Stage 4 | 文章素材索引骨架属于 Stage 4。 |
| 1076 | 3 | 三、阅读轨迹与判断变化 | 《人生》 Stage 4 | 阅读轨迹与判断变化骨架属于 Stage 4。 |
| 1079 | 3 | 四、待回看 / 归档不迁移 | 《人生》 Stage 4 | 待回看 / 归档不迁移骨架属于 Stage 4。 |
| 1083 | 3 | 11.6 重复卡、改判链与误读修正规则 | 《人生》 Stage 4 | 重复卡与修订链规则属于 Stage 4。 |
| 1122 | 3 | 11.7 外部读者材料与正式稿膨胀防控 | 《人生》 Stage 4 | 外部读者边界与防膨胀规则属于 Stage 4。 |
| 1134 | 3 | 11.8 第四阶段 QA 与 fixture 对照 | 《人生》 Stage 4 | 第四阶段 fixture QA 属于 Stage 4。 |
| 1159 | 2 | 12. 大任务处理策略 | 《人生》 router | 大任务处理策略与执行授权门归 router。 |
| 1163 | 3 | 12.1 正常任务 | 《人生》 router | 正常任务定义归 router 的全局执行门。 |
| 1174 | 3 | 12.2 复杂任务 | 《人生》 router | 复杂任务计划、审查与 start-work 入口门归 router。 |
| 1197 | 3 | 12.3 正式稿完成后的止损规则 | 《人生》 router | 正式稿止损与定点校补规则归 router。 |
| 1205 | 2 | 13. 辅助提示词 | 《人生》 router | 辅助提示词总则与模板警告归 router。 |
| 1209 | 3 | 只整理，不评价 | 《人生》 Stage 1 | 快捷模板直达第一阶段整理。 |
| 1215 | 3 | 只判断轻卡、完整卡、主卡候选 | 《人生》 Stage 1 | 快捷模板直达第一阶段轻量判类。 |
| 1221 | 3 | 只优化轻卡 | 《人生》 Stage 2 | 快捷模板直达第二阶段轻卡优化。 |
| 1227 | 3 | 只优化完整卡和主卡候选 | 《人生》 Stage 2 | 快捷模板直达第二阶段完整卡 / 主卡优化。 |
| 1233 | 3 | 当前章节热门想法扫描 | 《人生》 Stage 1 | 快捷模板直达热门划线与高赞扫描。 |
| 1239 | 3 | 围绕我的判断查高赞想法 | 《人生》 Stage 2 | 快捷模板直达围绕用户判断的高赞差异分析。 |
| 1245 | 3 | 读完整本书后执行全书收束整合 | 《人生》 Stage 4 | 快捷模板直达第四阶段全书收束整合。 |
| 1251 | 3 | 读完整本书后回看我的阅读风格 | 《人生》 Stage 4 | 快捷模板直达全书阅读风格回看。 |
| 1259 | 2 | 14. 《人生》已知回归风险与定点校勘样本 | intentional duplication | 七个回归样本必须留在 router，并被后续四个 stage prompt 继承为哨兵。 |

《人生》 router

- Scope ranges covered: `1-59`, `63-124`, `1159-1255`, plus router-level summaries of fixed paths, four-stage routing authority, multi-round rules, stage-switch QA/Git gates, complex-task planning gate, shortcut warnings, and book-specific inheritance facts.
- Headings/subheadings assigned here: `# 《人生》微信读书整理提示词`, `## 0. 不可降级原则与任务入口门`, `## 1. 四阶段总流程`, `## 2. 多轮整理规则`, `## 3. 阶段切换前 QA 与条件性 Git 检查点`, `## 12. 大任务处理策略`, `### 12.1`, `### 12.2`, `### 12.3`, `## 13. 辅助提示词`.
- Router-level authority preserved for downstream work: fixed paths, core goals, task-entry gate, four-stage flow, multi-round policy, conditional Git authorization, complex-task review gate, shortcut-template warning, and book-specific inheritance ledger.

《人生》 Stage 1

- Scope ranges covered: `127-325`, `540-633`, plus Stage-1-owned shortcut bodies `1209-1215` and `1233-1236`.
- Headings/subheadings assigned here: `## 4`, `### 4.0`, `### 4.1`, `## 5`, `## 6`, `### 6.1`, `### 6.2`, `## 8`, `### 中间整理稿格式`, `# 路遥《人生》中间整理稿`, `## 整理说明`, `## 第N轮整理：范围说明`, `### 001. 章节名 / range`, `## 本轮索引`, `### 轻卡清单`, `### 完整卡候选`, `### 主卡候选`, `### 暂存素材`, `### 外部读者精彩高赞想法候选`, `### 颜色统计`, `### 下次接着整理位置`, `### 只整理，不评价`, `### 只判断轻卡、完整卡、主卡候选`, `### 当前章节热门想法扫描`.
- Stage 1 carries data fetching, matching, range-merging, color/category/type judgment, import-to-official public-position lookup, external-reader candidate collection, and intermediate-draft format only.

《人生》 Stage 2

- Scope ranges covered: `328-537`, `637-822`, plus Stage-2-owned shortcut bodies `1221-1242`.
- Headings/subheadings assigned here: `## 7`, `### 7.1` through `### 7.11`, `## 9`, `### 9.1`, `## 第N轮优化前诊断`, `### 9.2`, `### 9.3`, `### 9.4`, `### 9.5`, `### 只优化轻卡`, `### 只优化完整卡和主卡候选`, `### 围绕我的判断查高赞想法`.
- Stage 2 carries literary-analysis depth, evidence anchoring, psychology-process writing, tension opening, question-chain upgrading, current answers, AI修正 deepening, and external-reader difference analysis.

《人生》 Stage 3

- Scope ranges covered: `825-954`.
- Headings/subheadings assigned here: `## 10`, `### 10.1`, `### 10.2`, `### 10.3`, `### 10.4`, `### 10.5`, `### 10.6`.
- Stage 3 carries migration trigger, pre-migration source checklist, formal-note structure, cursor update, material destination rules, external-reader migration boundary, and anti-regression QA.

《人生》 Stage 4

- Scope ranges covered: `957-1156`, plus Stage-4-owned shortcut bodies `1245-1255`.
- Headings/subheadings assigned here: `## 11`, `### 11.1` through `### 11.8`, the Stage-4 skeleton headings `## 全书收束整合`, `### 一、阅读现场档案`, `#### 1. 轻卡存档`, `#### 2. 完整卡`, `#### 3. 核心卡`, `#### 4. 外部读者随卡补充`, `### 二、文章素材索引`, `### 三、阅读轨迹与判断变化`, `### 四、待回看 / 归档不迁移`, and `### 读完整本书后执行全书收束整合`, `### 读完整本书后回看我的阅读风格`.
- Stage 4 carries the whole-book consolidation model, reading-archive-before-article-index order, internal ledger boundary, one-card-two-destinations rule, duplicate/revision-chain handling, external-reader anti-bloat rules, fixture-based QA, and book-specific article-direction index.

Duplicated inheritance blocks

These are the intentional duplications that later 《人生》 stage prompts must repeat in their inheritance blocks or preserved book-specific constraint blocks:

1. Applicable router path.
2. Required pre-read files: root `AGENTS.md`, the router, and same-book `AGENTS.md` only if it exists at execution time.
3. Exact input files and output files.
4. Conflict rule: if a stage prompt conflicts with the router, the router wins.
5. Task boundary and Must NOT list.
6. QA evidence path for execution.
7. Fixed path trio for `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`, and `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
8. Book identity and dual-bookId preservation: import `CB_2tb79r78T38k74M75h8iz4C3`, official public `25164497`.
9. Stage-4 article-direction set and the 7 regression sentinels.

Book-specific preservation facts

| fact cluster | snapshot lines | exact-source facts that must survive | preservation target |
|---|---|---|---|
| Fixed paths | `5-9` | `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`, `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md` | Router keeps them as authority, all four stage prompts inherit them verbatim. |
| Core goals and evidence-layer boundary | `11-18` | 先中间整理、再优化分析、再迁移正式稿；正式阅读笔记必须保留划线原文、我的原想法、必要的外部读者原话；`source ID` 等技术字段不默认进入正式稿正文。 | Router summary plus Stage 1 and Stage 3 inherited boundary. |
| Import/public bookId mapping | `213-219` | Personal import bookId `CB_2tb79r78T38k74M75h8iz4C3`; official public bookId `25164497`; mapping must happen by chapter title, text overlap, and official-position lookup, not by raw imported coordinates. | Router summary + Stage 1 detailed execution + all stage inheritance awareness. |
| Book-specific literary examples | `374-376`, `391-393` | Example 1: 高加林察觉巧珍感情后，本能回避的分析层次。 Example 2: “强烈 / 最好 / 不知为什么 / 老半天 / 不怕我不要你了吗”被当作心理雾区入口。 | Stage 2 keeps full examples; router records them as book-specific examples that must not be genericized into universal rules. |
| Book-specific article directions | `1019`, `1067-1074` | `人物线`, `城乡主题`, `尊严主题`, `爱情线`, `知识分子困境`, `写法线索`, 以及 line `1035` 的 `高加林人物线` 例子。 | Stage 4 full execution + router summary + all stage inheritance as book-only direction set. |
| Book-specific reader/archive model | `967-971`, `1040-1046` | `阅读现场档案 + 文章素材索引`，并且 `文章素材索引只引用卡片，不吞掉卡片`。 | Router summary + Stage 4 full rules. |
| 7 regression samples | `1261-1269` | `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, `黄亚萍的物质付出` | Router must keep full list; all stage prompts inherit as non-regression sentinels. |

Shortcut template map

| shortcut template | disposition |
|---|---|
| `只整理，不评价` | 《人生》 Stage 1 |
| `只判断轻卡、完整卡、主卡候选` | 《人生》 Stage 1 |
| `只优化轻卡` | 《人生》 Stage 2 |
| `只优化完整卡和主卡候选` | 《人生》 Stage 2 |
| `当前章节热门想法扫描` | 《人生》 Stage 1 |
| `围绕我的判断查高赞想法` | 《人生》 Stage 2 |
| `读完整本书后执行全书收束整合` | 《人生》 Stage 4 |
| `读完整本书后回看我的阅读风格` | 《人生》 Stage 4 |

Normative-language preservation ledger

- Completeness method: the immutable snapshot was re-read by control area, not by token hit alone. Grouped rows below cover every substantive sentence that controls authorization, preservation, scope, sequencing, Git, QA, book identity, or source-original handling in the 《人生》 prompt. False-positive token hits such as `例如` are excluded when they are not normative.

| snapshot area | representative exact-source sentences / control lines | completeness statement | disposition |
|---|---|---|---|
| `13-18` | `正式阅读笔记必须保留三类原始材料...AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。` / ``source ID`...不默认进入读者可见的正式阅读笔记正文。` | Re-read the full core-goal block. All evidence-layer and source-original rules are preserved as router authority and later inherited by Stage 1 and Stage 3. | 《人生》 router |
| `24-30` | `质量、文本证据、分析深度和我的原意，高于上下文经济...` / `分批只能改变执行组织方式...` / `复杂任务...必须先制定详细计划...只有我再明确授权开始执行后，才可通过当前客户端实际注册的 start-work 入口进入执行阶段。` | Re-read the full entry-gate block. Authorization, sequencing, and no-universal-command rules remain router-owned. | 《人生》 router |
| `39-59` | `第一阶段只做整理...不写入正式阅读笔记。` / `未经明确要求，不要直接把微信读书导出的内容写入正式阅读笔记。` / `第四阶段...文章素材索引只引用卡片，不替代卡片，也不抹掉阅读过程。` | Re-read the four-stage overview. Stage boundaries stay in router authority before detailed stage files are written. | 《人生》 router |
| `77-83` | `默认只优化第 N 轮新增内容，不重新优化整个中间稿。` / `默认优先迁移第 N 轮已优化完成...` / `只有当我明确说“回看全书中间稿”...才跨轮重写或整体重排。` | Re-read all multi-round rules. Round-scope controls remain router-owned. | 《人生》 router |
| `95-123` | `AI 必须先完成阶段切换 QA...` / `若当前指令没有明确 Git 授权...不把提交或推送当成默认前置条件。` / `仍需遵守项目 AGENTS.md 的 Git 规则。` / `不要提交无关阅读材料...` | Re-read the full stage-switch QA/Git gate. All Git authorization and sequencing controls remain router-owned. | 《人生》 router |
| `136-157` | `中间整理稿是可回源的工作台，应保留...技术定位信息...正式阅读笔记...不默认保留接口字段。` / `默认以“我的想法”为主索引整理...除非我明确要求整理纯划线。` / `不要只输出我的想法...必须尽量合并出对应的划线原文和划线颜色。` | Re-read the Stage 1 data boundary block. All source-merging and readable-evidence rules move to Stage 1. | 《人生》 Stage 1 |
| `161-201` | `不要因为 ... range 不完全一致，就直接判断为“只有想法”或“无法匹配”。` / `必须标注“非精确 range 匹配”。` / `只允许在内部匹配；输出时只展示本轮新增内容。` / `不要强行归并，也不要因此重整旧材料。` | Re-read the full matching block. Match-order, anti-range-collapse, and output-scope rules move to Stage 1. | 《人生》 Stage 1 |
| `205-269` | `优先按文本内容对应判断...若个人笔记来自导入书，应先将导入版坐标映射到微信读书官方版坐标。` / `不能直接用个人导入版 ... 判定公开想法是否存在。` / `/book/underlines ... 只能作为辅助信号，不能单独证明文本同位置。` / `高赞想法只能作为外部读者材料，不得替代我的感受、问题和判断。` | Re-read the full same-position public-review block. Dual-bookId mapping and external-reader boundary are preserved as intentional duplication between router summary and Stage 1 detail. | intentional duplication |
| `275-298` | `颜色只作为默认流向，不是最终卡片类型。` / `不要把颜色写成单纯数字。` / `整理时必须保持阅读顺序，不要为了按颜色分类而打散阅读线索。` | Re-read the color block. Output-format and reading-order controls move to Stage 1. | 《人生》 Stage 1 |
| `334-536` | `开始完整卡或主卡候选分析前，必须先判断...` / `完整卡...必须能指出至少一个可回到原文的证据锚点。` / `不能只用抽象词概括。` / `遇到...模糊词...不能直接越过。` / `AI 必须继续补“当前回答（沿原问题）”...` / `如果 AI修正只是复述...必须重写。` | Re-read the full literary-analysis block. Evidence anchoring, psychology process, ambiguity handling, two-layer question chains, and AI deepening rules all move to Stage 2. | 《人生》 Stage 2 |
| `545-561` | `默认以“我的想法”为主索引整理...` / `必须同时调用 /book/bookmarklist 和 /review/list/mine` / `默认尝试抓取同位置其他书友高赞想法` / `第一阶段只做整理...不写入正式阅读笔记。` / `不要修改其他文件。` | Re-read the Stage 1 execution block. All first-stage execution boundaries and output restrictions move to Stage 1. | 《人生》 Stage 1 |
| `643-821` | `不要覆盖我的原想法...` / `如果完整卡候选超过 5 条...建议先制定优化计划，再分批执行。` / `处理时必须遵守 ... AGENTS.md` / `必须指出文本落点` / `外部读者原话...不得改写成笼统的“有读者说”` / `不得让高赞想法覆盖我的原想法...` | Re-read the full Stage 2 execution block. Optimization sequencing, AGENTS toolbox inheritance, and external-reader analysis constraints move to Stage 2. | 《人生》 Stage 2 |
| `827-953` | `只有当我明确说“把已优化内容更新到正式阅读笔记”时，才执行这一阶段。` / `每条迁移材料必须保留书籍划线原文和“我的原想法”，不要用 AI 修正覆盖原文。` / `正式迁移前，必须先建立仅供内部核对的迁移清单...` / `迁移完成后...未通过不得把迁移视为完成。` | Re-read the full Stage 3 migration block. Source-original preservation, precheck, and anti-regression controls move to Stage 3. | 《人生》 Stage 3 |
| `959-1155` | `只有当我明确说“我已经读完整本《人生》，请执行全书收束整合”...才执行这一阶段。` / `第四阶段默认不全局重跑第三阶段...` / `不得把 source ID...写成正式稿正文或文章方向锚点。` / `文章素材索引只引用卡片，不吞掉卡片。` / `不能把轻卡一律升级成完整卡。` | Re-read the full Stage 4 block. Whole-book-only scope, archive-first order, anti-bloat rules, and fixture QA all move to Stage 4. | 《人生》 Stage 4 |
| `1161-1201` | `复杂任务只改变执行组织方式，不得遗漏...` / `必须先制定计划，再分步执行。` / `计划草案先交 Momus、Metis、Oracle 审看...` / `不能把裸 start-work、/shared/start-work 或 /start work 当成统一命令。` / `后续只能做有明确目标的定点校补，不再整体重写...` | Re-read the full complex-task and stop-loss block. Planning, review, authorization, and no-wholesale-rewrite controls remain router-owned. | 《人生》 router |
| `1207-1255` | `以下 8 段只是快捷任务模板...不是流程豁免。` / `若模板和这些门槛冲突，以这些门槛为准...` / `只整理《人生》本轮新增微信读书笔记，不评价、不优化、不生成完整卡。` / `不要把轻卡强行改成完整卡。` / `高赞想法只能作为外部读者材料，不要替代我的感受和判断。` | Re-read the shortcut warning and all 8 template bodies. The warning stays router-owned, while each template body is routed in the shortcut map above. | 《人生》 router + stage-specific shortcut mapping |
| `1261-1269` | `这些样本用于复杂任务的计划、迁移后 QA 和最后抽读。` / `它们是防止语义回归的哨兵，不是要求把无关材料硬写进每一轮笔记。` / the seven sample rows below | Re-read the full regression-sentinel block. All 7 samples remain book-specific and must be inherited by all later Wave 2 prompt files. | intentional duplication |

Regression-sentinel preservation ledger

| literal token | source role | preservation note | status |
|---|---|---|---|
| `CB_2tb79r78T38k74M75h8iz4C3` | personal import `bookId` | Must remain book-specific. Router summary and Stage 1 detailed mapping both need it. | PASS |
| `25164497` | official public `bookId` | Must remain book-specific. Router summary and Stage 1 detailed mapping both need it. | PASS |
| `ID 003` | regression sentinel 1 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `ID 006` | regression sentinel 2 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `ID 021` | regression sentinel 3 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `ID 109` | regression sentinel 4 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `ID 117` | regression sentinel 5 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `刘玉海救灾处` | regression sentinel 6 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |
| `黄亚萍的物质付出` | regression sentinel 7 | Must stay in router and inheritance ledger as a non-regression sample. | PASS |

Seven regression samples with source-meaning preservation

| sample | exact-source preservation fact | later target expectation |
|---|---|---|
| `ID 003` | `AI修正不能只把“留意”和“妥善解决”写成漂亮判断，必须补出前史。` | Router keeps full sentinel; later Stage 2 and Stage 3 QA must inherit it. |
| `ID 006` | `不能简单归因于他当过教师。要比较劳动在他眼中的位置、身份想象与尊严焦虑。` | Router keeps full sentinel; later Stage 2 must preserve the psychological bridge. |
| `ID 021` | `必须回应我对田晓霞的联想，不能偷换成少平的故事或用另一个人物代替原问题。` | Router keeps full sentinel; later Stage 2 must preserve the original question target. |
| `ID 109` | `不能把后文失势倒灌到当前场景。` | Router keeps full sentinel; later Stage 2 and Stage 3 must keep temporal evidence discipline. |
| `ID 117` | `不要因为句子过于整齐就批评它。应保留这句的文气，再补出...文本证据桥梁。` | Router keeps full sentinel; later Stage 2 must preserve style plus bridge. |
| `刘玉海救灾处` | `文本能支持的是救灾队伍迟到五小时，不能擅自改写成救灾队伍在路上耽搁五小时。` | Router keeps full sentinel; later prompts must not drift from textual support. |
| `黄亚萍的物质付出` | `不能简单说这不是牺牲。要承认其中真实的物质成本，同时区分它与巧珍在匮乏中的托举。` | Router keeps full sentinel; later prompts must preserve contrast without flattening. |

Exact-source-rule preservation samples

1. `[17]` `正式阅读笔记必须保留三类原始材料：书籍划线原文、我的原想法、必要的外部读者原话。AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。` -> 《人生》 router, later inherited by Stage 1 and Stage 3.
2. `[218]` `因此，不能直接用个人导入版 CB_... + chapterUid + range 判定公开想法是否存在。正确流程是：先用个人导入版整理我的阅读现场，再按章节标题、划线原文和文本重叠映射到官方版 25164497 的同一文本位置，最后用官方版 bookId + chapterUid + range 调 /book/readreviews。` -> intentional duplication between router summary and 《人生》 Stage 1.
3. `[840]` `每条迁移材料必须保留书籍划线原文和“我的原想法”，不要用 AI 修正覆盖原文。` -> 《人生》 Stage 3.
4. `[1040]` `正式阅读笔记中的全书收束整合部分，先处理“阅读现场档案”，再处理“文章素材索引”。顺序不能反过来。` -> 《人生》 Stage 4.
5. `[1267]` `不要因为句子过于整齐就批评它。应保留这句的文气，再补出使判断成立的文本证据桥梁。` -> intentional duplication as regression sentinel inherited by all later Wave 2 prompts.

Read-based QA notes:

- Task 8 work was grounded in the immutable snapshot after creation. No mapping decision here depends on any later mutable router rewrite, because no rewrite happened.
- Task 7 gate was re-read first and it does contain `GENERIC HARD QA: PASS`, so Wave 2 preflight is allowed to proceed.
- Same-book `AGENTS.md` is absent at execution time. This is not a blocker, but it is a real inheritance constraint. Later Wave 2 prompts must not pretend that `/home/king/github/growing-myself/路遥/人生/AGENTS.md` exists.
- Sibling-book `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` exists in the repo, which makes the non-import rule important. This evidence records that it was not imported.
- The move-ledger decision for `### 4.2 同位置其他书友高赞想法默认伴随抓取规则` is intentional duplication, not pure Stage 1, because the detailed operational rules belong in Stage 1 while the router must still preserve the dual-bookId fact and same-position warning.
- The move-ledger decision for `## 14. 《人生》已知回归风险与定点校勘样本` is intentional duplication, not pure router, because the router must keep the full list and all future stage prompts must inherit the sentinel ledger.
- Book-specific literary examples stay book-specific. The 高加林 / 巧珍心理例子 and the “强烈 / 最好 / 不知为什么 / 老半天”雾区例子 cannot be flattened into generic advice later.
- Stage 4 article directions stay book-specific as well. `人物线 / 城乡主题 / 尊严主题 / 爱情线 / 知识分子困境 / 写法线索` belong to 《人生》, not to the generic prompt family.
- No task-8 PASS row below is backed by token hits alone. Each one is tied to source rereads, heading mapping, and semantic placement in the ledger.

Boundary checks:

- This Task 8 preflight did not rewrite `/home/king/github/growing-myself/路遥/人生/《人生》微信读书提示词.md`.
- This Task 8 preflight did not create any of the four 《人生》 stage prompt files.
- This Task 8 preflight did not edit generic prompt files.
- This Task 8 preflight did not edit `/home/king/github/growing-myself/路遥/人生/《人生》中间整理稿.md`, `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md`, `.omo/run-continuation/*.json`, `.omo/drafts/*`, protected baseline manifests, `decisions.md`, or `problems.md`.
- The only writes are the immutable snapshot, this Task 8 evidence file, and one append-only note in `learnings.md`.
- Numeric references in this evidence are used only as source anchors or source-quote evidence, not as new target wording for future prompt text.
- Not applicable in this task: browser work, external web fetch, flaky tests, runtime debugging, or codegraph exploration.

Whitespace checks

| target | command style | result | status |
|---|---|---|---|
| snapshot `.omo/evidence/split-weread-prompts-by-stage/source/《人生》微信读书提示词.before.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| evidence `.omo/evidence/task-8-split-weread-prompts-by-stage.md` | `git diff --no-index --check /dev/null` | no output | PASS |
| append-only `.omo/notepads/split-weread-prompts-by-stage/learnings.md` | tracked `git diff --check --` | no output | PASS |

Literal preservation verification

| token | expected semantic location in this evidence | grep hit record | status |
|---|---|---|---|
| `CB_2tb79r78T38k74M75h8iz4C3` | bookId mapping ledger | grep hit confirms presence in duplicated inheritance block, book-specific preservation facts, and token ledger. | PASS |
| `25164497` | bookId mapping ledger | grep hit confirms presence in duplicated inheritance block, book-specific preservation facts, exact-source sample, and token ledger. | PASS |
| `ID 003` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `ID 006` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `ID 021` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `ID 109` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `ID 117` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `刘玉海救灾处` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |
| `黄亚萍的物质付出` | regression-sentinel ledger | grep hit confirms presence in 7-sample preservation list, token ledger, and sample-by-sample meaning row. | PASS |

Follow-ups / unresolved risks:

- Non-blocking: the repo is still dirty outside Task 8 scope. This preflight deliberately stayed inside the approved write set.
- Non-blocking: later Wave 2 prompt writers must use this immutable snapshot and this ledger, not the live mutable router file, as their source of truth.
- Non-blocking: `/home/king/github/growing-myself/路遥/人生/AGENTS.md` is absent today. If that file appears later, Task 9 to Task 13 should consciously decide whether to inherit it based on execution-time reality, not today’s assumption.
- Blocking threshold: if the literal-token grep rows or whitespace rows below remain `PENDING`, or if any heading is later found unmapped, Task 8 cannot claim PASS.

PASS:

- PASS: immutable snapshot created before any 《人生》 router rewrite or stage creation, with matching sha256, matching line counts, and `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`.
- PASS: target-file existence preflight for all five Wave 2 outputs is recorded.
- PASS: heading inventory maps every snapshot heading/subheading to exactly one disposition, with no `explicit out-of-scope stop` rows needed.
- PASS: anchor ranges from the plan are all covered and classified.
- PASS: applicable AGENTS evidence is correct for this execution state, root `AGENTS.md` only, same-book file absent, sibling-book rules not imported.
- PASS: fixed paths, dual-bookId mapping, book-specific literary examples, article directions, shortcut templates, and all 7 regression samples are preserved in the ledger.
- PASS: normative-language preservation ledger is read-based and grouped by semantic control area, not by grep-only hits.
- PASS: untracked-safe whitespace checks passed for the new snapshot and the new evidence, and the tracked append-only notepad diff check is clean.
- PASS: per-token `git grep --untracked` verification passed for `CB_2tb79r78T38k74M75h8iz4C3`, `25164497`, `ID 003`, `ID 006`, `ID 021`, `ID 109`, `ID 117`, `刘玉海救灾处`, and `黄亚萍的物质付出`.
