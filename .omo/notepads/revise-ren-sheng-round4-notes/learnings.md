## Todo 3 structural learning - 2026-07-09

- 第4轮结构返工的关键不是“多写一点”，而是把 Todo 2 的强卡分类落实到 heading level：15 个 article-core candidate 和 67 个 complete reading card 都必须有可见去向。否则后续 Todo 4 写正文时，很容易重新滑回当前正式稿的 5 核心 + 4 完整卡压缩形状。
- 人物主线、轻卡、素材库可以保留，但只能承载 Todo 2 已归入这些类别的 ID；它们不能替代独立完整卡，尤其不能吞掉 `061, 076, 079, 081, 089, 091, 095, 099, 103, 104, 111, 116, 119, 124, 125` 这组高风险完整卡。
### Todo 4 Learnings
- We successfully used a script to extract the middle-draft data into the 4-part skeleton (`我自己写的内容`, `AI评价`, `AI修正`, `AI补充`) for all 132 IDs into `.omo/evidence/task-4-round4-replacement-draft.md`.
- No placeholders like "待补" were needed since we had the rich structure in the middle draft, and we safely placed all external comments (without interface traces) inside their specific cards.
- The global exception `128` was correctly moved to Section 6.
- The destination table cleanly mapped all 132 IDs exactly to their headings.
- Surgically fixed Todo 4 draft mapping table for ID 128 to clearly map to `## 六、全局外部读者残留材料 - 1. 乡土温情可能带有路遥式理想化`.
- Cleaned up root workspace by removing temporary python scripts.

## Todo 5 core-card learning - 2026-07-09

- 主卡 QA 不能只看四段式标题在不在。最容易漏掉的伪完成，是“问题链升级”存在，但没有把沿原问题 / 新增角度各自拆开，并且没有给两路问题各自落一条 current-answer。
- 从中间稿自动抬升到 replacement draft 时，最容易丢的不是用户原文，而是脚手架规范化。尤其 promoted article-core 一组，`057, 060, 064, 070, 084, 120, 122, 130`，常见问题是只有一条总回答，或把“可扩写方向”埋进泛化的主题句里。
- Todo 5 审核时，优先查三件事：1）是否同时有沿原问题和新增角度两条问题链，2）两条问题链是否各有 current-answer，3）外部读者原话是不是保留了原句而不是被摘要化。

## Todo 6 complete-card learning - 2026-07-09

- Todo 6 的真实断点不是“67 张完整卡都没落地”，而是当前 `task-4` 磁盘草稿已经有 `67` 个 complete-card heading，剩下工作主要是去向审计和脚手架 QA，不能误判成要整稿重写。
- 完整卡最常见的伪完成模式有两种：一种是两条问题链都在，但 `当前回答` 没显式落出来；另一种是 `AI修正` 已经把答案说透了，却又没在证据里说明“为什么故意保持较轻”，结果看起来像漏写。
- 保护组 `061, 076, 079, 081, 089, 091, 095, 099, 103, 104, 111, 116, 119, 124, 125` 必须先查 destination 再查 scaffold。先确认它们还在 `## 二、完整阅读卡` 里独立站住，再谈轻重，不然很容易被人物线或结尾总评重新吞回去。
- 终章里的 `129, 131, 132` 可以比中段完整卡更收，但前提是审计文件里要明确写清楚：它们仍然是独立完整卡，只是把更重的理论负担交给相邻核心卡 `122 / 130`，绝不能模糊成“终章总评里已经说到了”。
- 若一张完整卡刻意保持中量，必须在 evidence 里写明理由。不要把“我觉得不用再写了”留成隐含判断，否则后续 Todo 7/8 很容易把它当成可进一步下调的弱卡。

## Todo 7 light/material learning - 2026-07-09

- Todo 7 最容易出现的伪完成，不是漏了某个 ID，而是只把它放进轻卡或素材库，却不写“为什么它没有上提”。不写明理由，后续任务就会把它误读成弱料，而不是有意保轻。
- `128` 是一个双重用途源项。source text 本身应留在“主题素材库 / 待回看”，因为它提供的是乡土接纳场景和现实分歧的锚点；但它的外部读者挑战又确实跨越了单一卡片，所以还要在全局外部残留区保留争议锚点。映射若只写其一，后续审计就容易误判。
- `114` 是本轮最像“是不是该升完整卡”的边界项，但复核后仍应留在素材库。原因不是它不强，而是它的强更像终章 regret 的物件锚点；若在 `109, 111, 120, 130, 131` 已经独立成立的前提下再升格，得到的多半是重复，不是新增问题链。

## Todo 8 external-comments learning - 2026-07-09

- Todo 8 最容易误判成“要重新给大量卡片补评论”，但这次从当前磁盘状态复核后发现，核心卡和有公开来源的完整卡其实已经普遍保留了 `1-3` 条原话。真正缺的往往是正式 audit、例外说明，以及去掉重复安放和界面痕迹。
- `128` 的正确处理不是把外部读者三条原话同时留在素材库和全局残留区，而是 source text 留在 `## 五`，原话分歧只留在 `## 六`。这样才能既保住材料锚点，也不破坏“全局残留材料只收非卡片专属争议”的边界。
- 检查外部读者材料时，不能只 grep 评论块本身，还要顺手扫文件尾部游标、附记和残留说明。界面痕迹很容易从 `chapterUid / range` 这种位置说明里漏进 draft，影响最终验收。

## Todo 9 tone-cleanup learning - 2026-07-09

- 第 4 轮这种大段迁移，最稳的顺序不是“边搬边润”，而是先整段按 accepted draft 重建回正式稿，再只对 AI 段落做定点句子改写。这样更不容易误伤 source-ID 去向、双 current-answer、外部读者原话，或 `128` 的双安放边界。
- tone cleanup 不能机械追求把所有 `不是……而是……` 清零。真正该优先打掉的，是正文里一眼能看出模板味的长句和课堂解释腔；用户原话、外部读者原话，以及少量承担“误读 / 正解”分界功能的分析句，需要明确留痕说明，而不是硬抹平。

## Todo 10 final-QA learning - 2026-07-09

- 第4轮终审最容易漏掉的，不是 source ID 去向，而是“内容已经齐了，字段名却没统一”。`086, 087, 089, 091` 的分析内容都在，但只因为写成了 `问题链升级（沿原想法）`，最终机械审计就会把它判成缺 `沿原问题`。终审前必须把脚手架字段名也当成验收对象。
- 游标 QA 不能只死对最早 plan 里的机器坐标写法，还要对照后续已接受的去元数据清理。只要正式稿仍明确指向 `132 / “我的亲人哪……”` 之后，且最后一条原文一致，就应判为语义正确，不必把 `chapterUid` 和 `range` 再漏回正式稿。

## Todo 10 F1-cursor follow-up - 2026-07-09

- F1 级游标问题说明：如果 plan 把最终 cursor 明定为允许例外，就不能把它按“统一去元数据”顺手抹掉。第4轮里真正稳的规则不是“零 metadata 命中”，而是“除了最终 cursor 这一行外，其他地方零命中”。
