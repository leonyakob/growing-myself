# add-whole-book-consolidation-model fixtures

用于全书收束整合的 deterministic dry-run 对照。每个 case 只给固定处理结果，不替代正式提示词。

## Case 1, partially migrated card

### 输入
- 划线原文："她说得平静，可我读到的不是接受，而是被现实磨平后的省力。"
- 我自己写的内容："我停在这里，是因为她连抱怨都省了，像把尊严也一起吞回去了。"
- 正式笔记现状：只剩一句 AI 概括，缺 `划线原文`，也缺用户原句。

### source status
- 已在正式笔记中，但需补 readable evidence / 用户原句 / 外部原话。

### archive treatment
- 保留为完整卡，只补齐缺失字段，不重写原卡判断。
- Preservation assertion：归档卡片仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- 在“阅读现场档案”里补回引文和用户原句，不重复扩写成新卡。

### article-index treatment
- 可在“人物被现实磨平”方向下引用这张卡，用短引文加原始触动，不复制整卡正文。

### forbidden failure
- 把旧 AI 概括当成完整卡，不补 `划线原文` 和 `我自己写的内容`。

## Case 2, duplicate same quote + same insight

### 输入
- 卡 A 划线原文："他站在门口没进去。"
- 卡 A 我自己写的内容："这一下停住，比进去更说明他的自卑。"
- 卡 B 划线原文相同，判断也仍是“门槛前的自卑”，只是措辞更啰嗦。

### source status
- 中间稿与正式稿重复，需合并或建立修订链。

### archive treatment
- 选更清楚的一张做代表卡，另一张合并入其他卡，只在内部台账记重复来源。
- Preservation assertion：代表归档卡片仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- “阅读现场档案”只保留代表卡，不并排放两张同义卡。

### article-index treatment
- 文章索引只引用代表卡，证据作用标成“人物线证据，门槛前停步”。

### forbidden failure
- 把两张重复卡都搬进正式稿，造成全书收束时的假充实。

## Case 3, duplicate same quote + changed judgment

### 输入
- 早期卡：划线原文 "他笑了笑，没有接话。" 我自己写的内容："我当时以为这是体面。"
- 后期卡：同一句划线原文。 我自己写的内容："现在看更像退让，他连辩解都觉得无用。"

### source status
- 正式稿旧判断已被后文修正，保留为阅读轨迹。

### archive treatment
- 建立修订链，早期卡保留，后期卡作为修正卡关联过去，不合并成单一结论。
- Preservation assertion：归档链条中的卡片仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- “阅读现场档案”保留当前可用版本。
- “阅读轨迹与判断变化”简写：当时读成体面，后来看成退让。

### article-index treatment
- 普通文章方向默认引用后期判断。
- 如果文章写“阅读中如何改判人物”，再连到早期误读卡。

### forbidden failure
- 只留下最后结论，悄悄抹掉早期读法。

## Case 4, same scene with different source ID/range

### 输入
- 卡 A 来自导入版 source ID 17，range 233-245，场景是高加林回村后站在院口发愣。
- 卡 B 来自公开版 source ID 88，range 410-426，同一场景，同一动作链，但引文起止略不同。
- 两张卡的核心判断都指向“回村不是归来，而是身份跌落后的停顿”。

### source status
- 中间稿与正式稿重复，需合并或建立修订链。

### archive treatment
- 视为同一场景卡，合并入其他卡，保留更完整的一段引文，另一张只在内部台账记跨版本来源。
- Preservation assertion：最终归档卡片仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- 正式稿用场景名和短引文做 readable anchor，不出现 source ID 或 range。

### article-index treatment
- 文章索引写“高加林回村院口发愣 / 引文短句”，不用技术来源号做锚点。

### forbidden failure
- 因为 source ID 不同，就把同一场景算成两张独立证据卡。

## Case 5, early misreading corrected later

### 输入
- 当时的读法："我最先把巧珍读成单纯付出型人物。"
- 后来出现的证据：她在关键处并不只是顺从，也在判断风险和体面。
- 全书后的修正："她不是只会给，她一直在算自己还能不能守住那点自尊。"
- 误读的价值：早期误读暴露了我自己也被“好女人叙事”带着走。

### source status
- 正式稿旧判断已被后文修正，保留为阅读轨迹。

### archive treatment
- 保留完整误读链，不把早期卡删掉，后文修正卡与之互链。
- Preservation assertion：误读卡和修正卡仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- 在“阅读轨迹与判断变化”里按“当时的读法 / 后来出现的证据 / 全书后的修正 / 误读的价值”简写。

### article-index treatment
- 普通主题文只用修正后的判断。
- 如果文章讨论读者如何被性别叙事带偏，可把误读链作为“阅读轨迹证据”。

### forbidden failure
- 把误读视为低质量废料直接清空，导致阅读过程失真。

## Case 6, external high-like challenge

### 输入
- 用户卡：划线原文 "她给他买了那件体面衣服。" 我自己写的内容："我当时只读到爱情里的照顾。"
- 外部高赞想法："这不只是照顾，也是物质能力对关系位置的重新分配。"

### source status
- 已在正式笔记中，结构合格，只补文章索引。

### archive treatment
- 用户卡保留为完整卡，外部想法只作为“挑战”关系挂在内部台账或补充栏。
- Preservation assertion：归档卡片仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- 正式稿主体仍先写用户卡，可补一句“有读者从物质位置变化读出挑战”。

### article-index treatment
- 在“爱情与阶层位置”方向下，以用户卡为主锚，再加一条“外部挑战，提醒别只读成照顾”。

### forbidden failure
- 把外部高赞评论改写成“我其实一直觉得这是权力变化”。

## Case 7, external-only strong comment

### 输入
- 此案例明确是 external-only。
- 外部高赞想法："真正刺人的不是贫穷本身，是人在被看见时还得假装不在乎。"
- 当前没有对应的用户划线卡，也没有用户自己的想法锚点。

### source status
- 仅外部读者材料，无用户卡片锚点。

### archive treatment
- external-only case，只在内部台账记为“独立精彩，待是否补用户锚点后再用”。
- 它不能被改写成用户的第一人称判断，不能伪造“我也觉得”。

### formal-note treatment
- 不进入“阅读现场档案”。
- 如需记录，只能在“待回看 / 归档不迁移”里简写原因，或暂不出现。

### article-index treatment
- 当前不单独进入文章索引，除非后来补到可链接的用户卡片锚点。

### forbidden failure
- 直接把这条外部评论写成用户卡，或把它当成文章索引的主证据。

## Case 8, light card used as article evidence but not upgraded

### 输入
- 划线原文："风从土坡上吹下来，吹得人不想说话。"
- 我自己写的内容："这句先别分析，我只是觉得土和风都很硬。"
- 卡片颜色与用途都更接近轻卡，暂时没有完整问题链。

### source status
- 中间稿已优化，尚未迁移。

### archive treatment
- 保留为轻卡，不因为后续可写文章，就硬升成完整卡。
- Preservation assertion：轻卡归档仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- “阅读现场档案”里按轻卡保留，不强补 AI 评价、问题链、扩写段。

### article-index treatment
- 可在“开篇气氛 / 土地质感 / 语言风格”方向下引用，证据作用标成“气氛证据”。

### forbidden failure
- 因为要写文章，就把轻卡强行扩成完整卡，假装它本来就有成熟判断。

## Case 9, final-note bloat prevention / archive-discard-with-reason

### 输入
- 划线原文："大家都沉默了一会儿。"
- 我自己写的内容："这里也有感觉。"
- 同章里已经有两张更完整的沉默卡，分别写清了场景张力和人物关系。
- 这张卡没有新增证据，也没有新的问题或判断。

### source status
- 已在正式笔记中，结构合格，只补文章索引。

### archive treatment
- 归档不迁移，理由是“同类证据已被更强卡覆盖，本卡无新增信息”。
- Preservation assertion：原始归档记录仍包含 `划线原文` + `我自己写的内容`。

### formal-note treatment
- 不进入正文卡片区。
- 如需交代，只在“待回看 / 归档不迁移”里留一句短原因，不带技术字段。

### article-index treatment
- 不入文章索引，避免一个主题下堆满低信息量沉默卡。

### forbidden failure
- 为了显得材料多，把这张弱卡也塞进正式稿正文，或把内部判重理由整行贴进读者可见部分。
