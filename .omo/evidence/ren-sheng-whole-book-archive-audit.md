# Ren Sheng whole-book archive audit

Status: PASS

## Brief C2 summary

- Final card rows audited: `165`; accepted `N_new=0`; expected final card count `165`.
- Preservation manifest rows: `165`; anchor-map rows: `165`; key sets equal: `True`.
- Repair/new-card provenance: Part B was `none`; every row below has `repair=0; new=0`.
- Article-link separation: `article_links` are index hints only; archive identity is always `formal_key + post_anchor`, never the article direction label.
- Identity/cardinality proof: F001-F165 remain in anchor-map order, each appears once, each post anchor is still in the final formal note, and modeled-post equality in metadata cleanup proves no unaffected card body moved/disappeared/duplicated.
- Formal post-cleanup SHA-256: `105f638d03e54fecf771f143aa0cc3292682084fa1e69601218b3f78b77ebcd0`.
- Source draft SHA-256: `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0`; source immutable.

## Card-by-card audit

| # | key | archive disposition | card-structure class | pre anchor | post anchor | preservation/repair/new-card provenance | article-link separation |
|---:|---|---|---|---|---|---|---|
| 1 | F001 | 保留为完整卡 | 核心候选 | same as post | 第1轮 / 一、文章核心候选 / 1. 白面饼、爱的过分与独生子：高加林悲剧的家庭根源 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 2 | F002 | 保留为完整卡 | 核心候选 | same as post | 第1轮 / 一、文章核心候选 / 2. 读书之后回不了土地：身份坠落与县城启蒙 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 3 | F003 | 保留为完整卡 | 核心候选 | same as post | 第1轮 / 一、文章核心候选 / 3. 两种自尊：高加林向外刺伤，孙少平向内约束 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 4 | F004 | 保留为完整卡 | 核心候选 | same as post | 第1轮 / 一、文章核心候选 / 4. 亲吻之后叫她刷牙：高加林爱情里的接纳、嫌弃与改造 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 5 | F005 | 保留为完整卡 | 人物主线 | same as post | 第1轮 / 二、人物主线卡 / 1. 黄亚萍：不是爱情的开始，而是出走想象的投影 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 6 | F006 | 保留为完整卡 | 人物主线 | same as post | 第1轮 / 二、人物主线卡 / 2. 巧珍：自卑、仰慕、行动型的爱与自我牺牲 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 7 | F007 | 保留为完整卡 | 人物主线 | same as post | 第1轮 / 二、人物主线卡 / 3. 高玉德：父辈恐惧与弱者生存策略 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 8 | F008 | 保留为完整卡 | 完整卡 | same as post | 第1轮 / 三、完整阅读卡 / 1. 路遥小说开头的阴云：环境怎样提前写出命运 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 9 | F009 | 保留为完整卡 | 完整卡 | same as post | 第1轮 / 三、完整阅读卡 / 2. 舀面瓢、火柴与煤油灯：日常物件怎样写灾难 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 10 | F010 | 保留为完整卡 | 完整卡 | same as post | 第1轮 / 三、完整阅读卡 / 3. 习惯权力的不公，却不能容忍不劳动的人 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 11 | F011 | 保留为完整卡 | 完整卡 | same as post | 第1轮 / 三、完整阅读卡 / 4. 一个称呼里的身份落差：“高老师” | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 12 | F012 | 保留为轻卡 | 轻卡 | same as post | 第1轮 / 四、轻卡存档 / 阅读心流 / 1. “核桃皮状” | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 13 | F013 | 保留为轻卡 | 轻卡 | same as post | 第1轮 / 四、轻卡存档 / 阅读心流 / 2. “盖满川” | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 14 | F014 | 保留为轻卡 | 轻卡 | same as post | 第1轮 / 四、轻卡存档 / 阅读心流 / 3. “熨帖舒服的疲倦” | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 15 | F015 | 保留为轻卡 | 轻卡 | same as post | 第1轮 / 四、轻卡存档 / 阅读心流 / 4. 倒叙真要命 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 16 | F016 | 保留为轻卡 | 轻卡 | same as post | 第1轮 / 四、轻卡存档 / 阅读心流 / 5. 弱者版“三十六计” | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 17 | F017 | 待回看 | 主题素材 | same as post | 第1轮 / 五、主题素材库 / 待回看 / 1. 高加林与孙少平出场条件对照 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 18 | F018 | 待回看 | 主题素材 | same as post | 第1轮 / 五、主题素材库 / 待回看 / 2. 川道地貌与空间等级 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 19 | F019 | 待回看 | 主题素材 | same as post | 第1轮 / 五、主题素材库 / 待回看 / 3. 无个人想法划线 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 20 | F020 | 待回看 | 主题素材 | same as post | 第1轮 / 五、主题素材库 / 待回看 / 4. 未稳定定位想法 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 21 | F021 | 保留为完整卡 | 核心候选 | same as post | 第2轮 / 一、文章核心候选 / 1. 一个吻为什么变成履历表：高加林爱情里的身份羞耻 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 22 | F022 | 保留为完整卡 | 核心候选 | same as post | 第2轮 / 一、文章核心候选 / 2. “睁眼瞎子”与“比爸妈还亲”：巧珍爱情里的教育创伤 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 23 | F023 | 保留为完整卡 | 核心候选 | same as post | 第2轮 / 一、文章核心候选 / 3. 鸡蛋、蛋糕和红药水：巧珍的爱为什么具体到让人心疼 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 24 | F024 | 保留为完整卡 | 核心候选 | same as post | 第2轮 / 一、文章核心候选 / 4. 不公开恋爱，却宣称巧珍已有对象：高加林爱情里的权利和责任 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 25 | F025 | 保留为完整卡 | 人物主线 | same as post | 第2轮 / 二、人物主线卡 / 1. 刘立本：疼女儿、要面子与门当户对的账本 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 26 | F026 | 保留为完整卡 | 人物主线 | same as post | 第2轮 / 二、人物主线卡 / 2. 高玉德：护犊子的一声吼，父爱和冲动都是真的 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 27 | F027 | 保留为完整卡 | 人物主线 | same as post | 第2轮 / 二、人物主线卡 / 3. 半壶水、针扎般心疼和两颗泪：高加林不是纯坏，也还没有稳定负责 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 28 | F028 | 保留为完整卡 | 完整卡 | same as post | 第2轮 / 三、完整阅读卡 / 1. 刷牙风波：村庄围观与巧珍的日常反抗 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 29 | F029 | 保留为完整卡 | 完整卡 | same as post | 第2轮 / 三、完整阅读卡 / 2. 向内归因的巧珍：行动力与自我委屈 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 30 | F030 | 保留为完整卡 | 完整卡 | same as post | 第2轮 / 三、完整阅读卡 / 3. 不选马栓：没读书的人也有精神向往 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 31 | F031 | 保留为完整卡 | 完整卡 | same as post | 第2轮 / 三、完整阅读卡 / 4. 读书要不要把拉家常读成炫耀：细读的边界 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 32 | F032 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 1. 熟人社会里的刷牙新闻 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 33 | F033 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 2. 没边界感的围观 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 34 | F034 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 3. 皮影戏式的日常写法 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 35 | F035 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 4. 刘立本粗俗骂人 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 36 | F036 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 5. 女为悦己者容 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 37 | F037 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 6. 恋爱初期的眼泪 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 38 | F038 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 7. 恋爱滤镜里的破衣服 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 39 | F039 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 8. 深情付错人的锋芒 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 40 | F040 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 9. 巧珍复盘后立刻行动 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 41 | F041 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 10. 他只是喜欢脸和身材吗 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 42 | F042 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 11. 知道却不回应 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 43 | F043 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 12. 玉皇大帝发誓 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 44 | F044 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 13. 巧珍主动勇敢 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 45 | F045 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 14. 这才是热恋 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 46 | F046 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 15. 刘立本精明错了地方 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 47 | F047 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 16. 生意人的场面礼貌 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 48 | F048 | 保留为轻卡 | 轻卡 | same as post | 第2轮 / 四、轻卡存档 / 阅读心流 / 17. 乖人不常恼 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 49 | F049 | 待回看 | 主题素材 | same as post | 第2轮 / 五、主题素材库 / 待回看 / 1. 刘立本家境和外貌气派 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 50 | F050 | 待回看 | 主题素材 | same as post | 第2轮 / 五、主题素材库 / 待回看 / 2. 高明楼与制度变动中的既得利益 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 51 | F051 | 待回看 | 主题素材 | same as post | 第2轮 / 五、主题素材库 / 待回看 / 3. 后文重点回看 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 52 | F052 | 保留为完整卡 | 核心候选 | same as post | 第3轮 / 一、文章核心候选 / 1. 同车不同心：巧珍的爱与高加林的报复 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 53 | F053 | 保留为完整卡 | 核心候选 | same as post | 第3轮 / 一、文章核心候选 / 2. 高加林的远方：爱情安慰失效以后，城市屈辱重新点燃了他 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 54 | F054 | 保留为完整卡 | 核心候选 | same as post | 第3轮 / 一、文章核心候选 / 3. 德顺爷爷的三板斧、臭香哲学和一生深情 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 55 | F055 | 保留为完整卡 | 核心候选 | same as post | 第3轮 / 一、文章核心候选 / 4. 巧珍的主体性怎样被爱情吸走 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 56 | F056 | 保留为完整卡 | 人物主线 | same as post | 第3轮 / 二、人物主线卡 / 1. 高明楼：父爱、识人、选择性开放与人情技术 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 57 | F057 | 保留为完整卡 | 完整卡 | same as post | 第3轮 / 三、完整阅读卡 / 1. 真话为什么要借权威的嘴：科学、愚昧和话语权 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 58 | F058 | 保留为完整卡 | 完整卡 | same as post | 第3轮 / 三、完整阅读卡 / 2. 现代文明的风：高加林为什么没有先成为传播者 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 59 | F059 | 保留为完整卡 | 完整卡 | same as post | 第3轮 / 三、完整阅读卡 / 3. 高加林在黑夜里忍了一次 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 60 | F060 | 保留为轻卡 | 轻卡 | same as post | 第3轮 / 四、轻卡存档 / 阅读心流 / 1. “有时”的冷淡 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 61 | F061 | 保留为轻卡 | 轻卡 | same as post | 第3轮 / 四、轻卡存档 / 阅读心流 / 2. 德顺老汉的臭香哲学 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 62 | F062 | 保留为轻卡 | 轻卡 | same as post | 第3轮 / 四、轻卡存档 / 阅读心流 / 3. 张克南母亲带来的尴尬 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 63 | F063 | 保留为轻卡 | 轻卡 | same as post | 第3轮 / 四、轻卡存档 / 阅读心流 / 4. 高加林的高级反击 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 64 | F064 | 待回看 | 主题素材 | same as post | 第3轮 / 五、主题素材库 / 待回看 / 1. 高明楼的正面能力与权力风险要继续并读 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 65 | F065 | 待回看 | 主题素材 | same as post | 第3轮 / 五、主题素材库 / 待回看 / 2. 巧珍能不能从“爱高加林”里分离出自己的精神需求 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 66 | F066 | 待回看 | 主题素材 | same as post | 第3轮 / 五、主题素材库 / 待回看 / 3. 高加林的城市火焰会烧向哪里 | preservation-only; repair=0; new=0 | none; identity stays formal_key+post_anchor |
| 67 | F067 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 1. 借来的权力光：高玉德为什么非要带弟弟去吃这顿饭【源ID：009】 | 第4轮 / 一、文章核心候选（15） / 1. 借来的权力光：高玉德为什么非要带弟弟去吃这顿饭 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 68 | F068 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 2. 同一句“乡巴佬”：身份位置如何改变刺痛度【源ID：030】 | 第4轮 / 一、文章核心候选（15） / 2. 同一句“乡巴佬”：身份位置如何改变刺痛度 | PartA card heading cleanup; repair=0; new=0 | article_links=尊严主题; non-identity index only |
| 69 | F069 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 3. 一句“两个人都有点兴奋”：情感越界前最轻的一圈水纹【源ID：039】 | 第4轮 / 一、文章核心候选（15） / 3. 一句“两个人都有点兴奋”：情感越界前最轻的一圈水纹 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 70 | F070 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 4. 黄亚萍的爱情价值地图：爱一个人，也是爱一条去远方的路【源ID：048】 | 第4轮 / 一、文章核心候选（15） / 4. 黄亚萍的爱情价值地图：爱一个人，也是爱一条去远方的路 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 71 | F071 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 5. “让我好好想一想”：欲望已经点头，伦理还在拖他的手【源ID：053】 | 第4轮 / 一、文章核心候选（15） / 5. “让我好好想一想”：欲望已经点头，伦理还在拖他的手 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 72 | F072 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 6. 不能为巧珍贻误转折：前途欲望和处理巧珍的伦理【源ID：057】 | 第4轮 / 一、文章核心候选（15） / 6. 不能为巧珍贻误转折：前途欲望和处理巧珍的伦理 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 73 | F073 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 7. “自我毁灭”：阶层话语怎样刺中高加林的身份伤疤【源ID：060】 | 第4轮 / 一、文章核心候选（15） / 7. “自我毁灭”：阶层话语怎样刺中高加林的身份伤疤 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 尊严主题; non-identity index only |
| 74 | F074 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 8. 门当户对刺痛自尊：高加林的自卑和自负怎样互相翻面【源ID：064】 | 第4轮 / 一、文章核心候选（15） / 8. 门当户对刺痛自尊：高加林的自卑和自负怎样互相翻面 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 尊严主题; non-identity index only |
| 75 | F075 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 9. 怕巧珍痛不欲生让他下不了台：把别人的伤换算成自己的风险【源ID：070】 | 第4轮 / 一、文章核心候选（15） / 9. 怕巧珍痛不欲生让他下不了台：把别人的伤换算成自己的风险 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 76 | F076 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 10. 德顺骂“良心卖了”：土地尺度上的道德审判【源ID：084】 | 第4轮 / 一、文章核心候选（15） / 10. 德顺骂“良心卖了”：土地尺度上的道德审判 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 城乡主题; non-identity index only |
| 77 | F077 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 11. 县城变小、陌生：见过更大世界后的空间失衡【源ID：109】 | 第4轮 / 一、文章核心候选（15） / 11. 县城变小、陌生：见过更大世界后的空间失衡 | PartA card heading cleanup; repair=0; new=0 | article_links=城乡主题; non-identity index only |
| 78 | F078 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 12. 克南的直线伦理与高加林的斜坡伦理【源ID：117】 | 第4轮 / 一、文章核心候选（15） / 12. 克南的直线伦理与高加林的斜坡伦理 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 79 | F079 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 13. “我真正爱的人实际上是另外一个”：更爱巧珍里的真情、偏见和自我辩护【源ID：120】 | 第4轮 / 一、文章核心候选（15） / 13. “我真正爱的人实际上是另外一个”：更爱巧珍里的真情、偏见和自我辩护 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 80 | F080 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 14. “并非结局”：故事有结局，人生没有结局【源ID：122】 | 第4轮 / 一、文章核心候选（15） / 14. “并非结局”：故事有结局，人生没有结局 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 81 | F081 | 保留为完整卡 | 核心候选 | 第4轮 / 一、文章核心候选（15） / 15. 德顺生活哲学：劳动、跌倒和重新做人【源ID：130】 | 第4轮 / 一、文章核心候选（15） / 15. 德顺生活哲学：劳动、跌倒和重新做人 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 82 | F082 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 1. 村庄消息风和破墙烂院：外部荣光怎样照见贫穷现场【源ID：001】 | 第4轮 / 二、完整阅读卡（67） / 1. 村庄消息风和破墙烂院：外部荣光怎样照见贫穷现场 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 83 | F083 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 2. 动作零碎：希望如何先改造高加林的身体【源ID：002】 | 第4轮 / 二、完整阅读卡（67） / 2. 动作零碎：希望如何先改造高加林的身体 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 写法线索; non-identity index only |
| 84 | F084 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 3. 马占胜搂肩承诺工作：关系链如何让办事速度突然激活【源ID：003】 | 第4轮 / 二、完整阅读卡（67） / 3. 马占胜搂肩承诺工作：关系链如何让办事速度突然激活 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 85 | F085 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 4. 一声“老马”：同一称呼在新权力场里的变味【源ID：004】 | 第4轮 / 二、完整阅读卡（67） / 4. 一声“老马”：同一称呼在新权力场里的变味 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 86 | F086 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 5. “加林恐怕不愿去掏炭”：体面劳动与身份回落【源ID：006】 | 第4轮 / 二、完整阅读卡（67） / 5. “加林恐怕不愿去掏炭”：体面劳动与身份回落 | PartA card heading cleanup; repair=0; new=0 | article_links=尊严主题; non-identity index only |
| 87 | F087 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 6. 瘦手哆嗦接酒：高玉德一杯酒里的翻身、羞怯和辛酸【源ID：010】 | 第4轮 / 二、完整阅读卡（67） / 6. 瘦手哆嗦接酒：高玉德一杯酒里的翻身、羞怯和辛酸 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 88 | F088 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 7. 白天不能亲巧珍：亲密方式开始受场合和体面约束【源ID：012】 | 第4轮 / 二、完整阅读卡（67） / 7. 白天不能亲巧珍：亲密方式开始受场合和体面约束 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 89 | F089 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 8. “怔怔地望了一眼”：承诺和预感里的动作细读【源ID：013】 | 第4轮 / 二、完整阅读卡（67） / 8. “怔怔地望了一眼”：承诺和预感里的动作细读 | PartA card heading cleanup; repair=0; new=0 | article_links=写法线索; non-identity index only |
| 90 | F090 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 9. 仍热爱故乡田地：离开土地的人为什么还被土地牵住【源ID：014】 | 第4轮 / 二、完整阅读卡（67） / 9. 仍热爱故乡田地：离开土地的人为什么还被土地牵住 | PartA card heading cleanup; repair=0; new=0 | article_links=城乡主题; non-identity index only |
| 91 | F091 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 10. “我再也不能离开你了”：县城像恋人，也像审判者【源ID：019】 | 第4轮 / 二、完整阅读卡（67） / 10. “我再也不能离开你了”：县城像恋人，也像审判者 | PartA card heading cleanup; repair=0; new=0 | article_links=城乡主题; non-identity index only |
| 92 | F092 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 11. 喝路边水坑、脚流血：高加林肯为被认可的前途吃苦【源ID：021】 | 第4轮 / 二、完整阅读卡（67） / 11. 喝路边水坑、脚流血：高加林肯为被认可的前途吃苦 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 93 | F093 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 12. 第一个到达灾区：个体积极与系统迟缓【源ID：022】 | 第4轮 / 二、完整阅读卡（67） / 12. 第一个到达灾区：个体积极与系统迟缓 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 94 | F094 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 13. 硬要跟救灾队走：爱情亏欠与工作担当并存【源ID：024】 | 第4轮 / 二、完整阅读卡（67） / 13. 硬要跟救灾队走：爱情亏欠与工作担当并存 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 95 | F095 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 14. 马占胜、高明楼和刘玉海：干部群像对照【源ID：026】 | 第4轮 / 二、完整阅读卡（67） / 14. 马占胜、高明楼和刘玉海：干部群像对照 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 96 | F096 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 15. 会议上毫不拘束提问：高加林的职业适配【源ID：027】 | 第4轮 / 二、完整阅读卡（67） / 15. 会议上毫不拘束提问：高加林的职业适配 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 97 | F097 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 16. 第一篇报道被播出：职业承认和景老师一字未改【源ID：028】 | 第4轮 / 二、完整阅读卡（67） / 16. 第一篇报道被播出：职业承认和景老师一字未改 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 98 | F098 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 17. 克南是实业家：不是“没出息”的前置证据【源ID：029】 | 第4轮 / 二、完整阅读卡（67） / 17. 克南是实业家：不是“没出息”的前置证据 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 99 | F099 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 18. 先顾虑黄亚萍与克南：公开关系和隐秘关系的伦理双标【源ID：031】 | 第4轮 / 二、完整阅读卡（67） / 18. 先顾虑黄亚萍与克南：公开关系和隐秘关系的伦理双标 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 100 | F100 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 19. “怕影响”而不说有对象：事业自保与暧昧保留【源ID：032】 | 第4轮 / 二、完整阅读卡（67） / 19. “怕影响”而不说有对象：事业自保与暧昧保留 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 101 | F101 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 20. 克南照料黄亚萍：照料、感激与爱情温差【源ID：033】 | 第4轮 / 二、完整阅读卡（67） / 20. 克南照料黄亚萍：照料、感激与爱情温差 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 102 | F102 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 21. 黄亚萍不愿嫁农民：她的爱与生活边界【源ID：034】 | 第4轮 / 二、完整阅读卡（67） / 21. 黄亚萍不愿嫁农民：她的爱与生活边界 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 103 | F103 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 22. 骂克南“胖成个猪”：语言暴力与关系高位【源ID：036】 | 第4轮 / 二、完整阅读卡（67） / 22. 骂克南“胖成个猪”：语言暴力与关系高位 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 104 | F104 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 23. 想到亚萍后更想巧珍：精神越界与补偿式深情【源ID：038】 | 第4轮 / 二、完整阅读卡（67） / 23. 想到亚萍后更想巧珍：精神越界与补偿式深情 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 105 | F105 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 24. “这不是在庄稼地里”：身份空间切割【源ID：040】 | 第4轮 / 二、完整阅读卡（67） / 24. “这不是在庄稼地里”：身份空间切割 | PartA card heading cleanup; repair=0; new=0 | article_links=尊严主题; non-identity index only |
| 106 | F106 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 25. “我不冷！你千万不要拿来！”：拒绝照料与身份切割【源ID：041】 | 第4轮 / 二、完整阅读卡（67） / 25. “我不冷！你千万不要拿来！”：拒绝照料与身份切割 | PartA card heading cleanup; repair=0; new=0 | article_links=尊严主题; non-identity index only |
| 107 | F107 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 26. 巧珍贴身拿钱：务实照料链的具体动作【源ID：043】 | 第4轮 / 二、完整阅读卡（67） / 26. 巧珍贴身拿钱：务实照料链的具体动作 | PartA card heading cleanup; repair=0; new=0 | article_links=写法线索; 爱情线; non-identity index only |
| 108 | F108 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 27. 红头巾的浪漫与实际：高加林的想象满足了谁【源ID：044】 | 第4轮 / 二、完整阅读卡（67） / 27. 红头巾的浪漫与实际：高加林的想象满足了谁 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 109 | F109 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 28. 亲热不如从前陶醉：关系退潮的身体证据【源ID：045】 | 第4轮 / 二、完整阅读卡（67） / 28. 亲热不如从前陶醉：关系退潮的身体证据 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 110 | F110 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 29. 黄亚萍“无论如何”要和高加林：同类感、占有欲与自我中心【源ID：046】 | 第4轮 / 二、完整阅读卡（67） / 29. 黄亚萍“无论如何”要和高加林：同类感、占有欲与自我中心 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 111 | F111 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 30. 克南竟看不出她爱加林：老实、痛苦和关系盲区【源ID：049】 | 第4轮 / 二、完整阅读卡（67） / 30. 克南竟看不出她爱加林：老实、痛苦和关系盲区 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 112 | F112 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 31. 同时想黄亚萍和巧珍：两种女性、两种生活、两种自我想象【源ID：050】 | 第4轮 / 二、完整阅读卡（67） / 31. 同时想黄亚萍和巧珍：两种女性、两种生活、两种自我想象 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 113 | F113 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 32. 风暴将临、激动又战栗：表白前心理风暴【源ID：051】 | 第4轮 / 二、完整阅读卡（67） / 32. 风暴将临、激动又战栗：表白前心理风暴 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 114 | F114 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 33. “我希望不是他，而是你”：表白里的 offer 与前途诱惑【源ID：052】 | 第4轮 / 二、完整阅读卡（67） / 33. “我希望不是他，而是你”：表白里的 offer 与前途诱惑 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 115 | F115 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 34. 现实与梦想互变：高加林价值秩序倒转【源ID：055】 | 第4轮 / 二、完整阅读卡（67） / 34. 现实与梦想互变：高加林价值秩序倒转 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 116 | F116 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 35. 像疯子一样转圈碰墙：分手方案、面子和自我人设【源ID：058】 | 第4轮 / 二、完整阅读卡（67） / 35. 像疯子一样转圈碰墙：分手方案、面子和自我人设 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 117 | F117 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 36. “巧珍从来也不这样对我说话”：怀念的是人，还是被供奉的感觉【源ID：061】 | 第4轮 / 二、完整阅读卡（67） / 36. “巧珍从来也不这样对我说话”：怀念的是人，还是被供奉的感觉 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 118 | F118 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 37. 恍惚地点头：半清醒状态里的顺势选择【源ID：062】 | 第4轮 / 二、完整阅读卡（67） / 37. 恍惚地点头：半清醒状态里的顺势选择 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 119 | F119 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 38. 厚嘴唇像蜜蜂翅膀：路遥身体细节写法卡【源ID：067】 | 第4轮 / 二、完整阅读卡（67） / 38. 厚嘴唇像蜜蜂翅膀：路遥身体细节写法卡 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 120 | F120 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 39. 硬把母亲推出房子：黄亚萍果断里的伤人硬度【源ID：068】 | 第4轮 / 二、完整阅读卡（67） / 39. 硬把母亲推出房子：黄亚萍果断里的伤人硬度 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 121 | F121 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 40. 半截分手话：高加林怎样把刀递给巧珍【源ID：071】 | 第4轮 / 二、完整阅读卡（67） / 40. 半截分手话：高加林怎样把刀递给巧珍 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 122 | F122 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 41. 头也不回飞跑而去：分手后的体面与尊严【源ID：074】 | 第4轮 / 二、完整阅读卡（67） / 41. 头也不回飞跑而去：分手后的体面与尊严 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 123 | F123 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 42. 青山绿水鲜明：轻松感与环境变亮的冷感【源ID：076】 | 第4轮 / 二、完整阅读卡（67） / 42. 青山绿水鲜明：轻松感与环境变亮的冷感 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 124 | F124 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 43. 两人公开高调骑车：公开陈列的伦理后果【源ID：078】 | 第4轮 / 二、完整阅读卡（67） / 43. 两人公开高调骑车：公开陈列的伦理后果 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 125 | F125 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 44. 亚萍任性、高加林不如从前自在：向上关系里交出主导权【源ID：079】 | 第4轮 / 二、完整阅读卡（67） / 44. 亚萍任性、高加林不如从前自在：向上关系里交出主导权 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 126 | F126 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 45. 进口削苹果刀丢了：精致物件与利己试探【源ID：080】 | 第4轮 / 二、完整阅读卡（67） / 45. 进口削苹果刀丢了：精致物件与利己试探 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 127 | F127 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 46. “故意开玩笑”测试听话程度：黄亚萍的服从性测试【源ID：081】 | 第4轮 / 二、完整阅读卡（67） / 46. “故意开玩笑”测试听话程度：黄亚萍的服从性测试 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 128 | F128 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 47. 坏情绪很快消失：野心排序如何压过愧疚【源ID：085】 | 第4轮 / 二、完整阅读卡（67） / 47. 坏情绪很快消失：野心排序如何压过愧疚 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 129 | F129 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 48. 巧珍从地上爬起来：复原能力的关键动作【源ID：086】 | 第4轮 / 二、完整阅读卡（67） / 48. 巧珍从地上爬起来：复原能力的关键动作 | PartA card heading cleanup; repair=0; new=0 | article_links=写法线索; 爱情线; non-identity index only |
| 130 | F130 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 49. 巧珍为什么要挣扎着下地去劳动：劳动与土地止痛【源ID：087】 | 第4轮 / 二、完整阅读卡（67） / 49. 巧珍为什么要挣扎着下地去劳动：劳动与土地止痛 | PartA card heading cleanup; repair=0; new=0 | article_links=城乡主题; 爱情线; non-identity index only |
| 131 | F131 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 50. 立本不再勉强女儿婚事：粗硬父爱转向温柔【源ID：089】 | 第4轮 / 二、完整阅读卡（67） / 50. 立本不再勉强女儿婚事：粗硬父爱转向温柔 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 132 | F132 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 51. 马拴“不嫌”：质朴、再婚伦理和现实支点【源ID：091】 | 第4轮 / 二、完整阅读卡（67） / 51. 马拴“不嫌”：质朴、再婚伦理和现实支点 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 133 | F133 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 52. “就在这几天”同意婚事：带痛继续生存【源ID：092】 | 第4轮 / 二、完整阅读卡（67） / 52. “就在这几天”同意婚事：带痛继续生存 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 134 | F134 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 53. 德顺老汉躺炕流泪：旧情与重感情【源ID：095】 | 第4轮 / 二、完整阅读卡（67） / 53. 德顺老汉躺炕流泪：旧情与重感情 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 135 | F135 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 54. “我还得活人”：巧珍把痛转成责任【源ID：098】 | 第4轮 / 二、完整阅读卡（67） / 54. “我还得活人”：巧珍把痛转成责任 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 136 | F136 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 55. 刘立本长舒一口气：父亲卸力和仪式收束【源ID：099】 | 第4轮 / 二、完整阅读卡（67） / 55. 刘立本长舒一口气：父亲卸力和仪式收束 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 137 | F137 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 56. 克南母亲喝骂：家庭权力、举报伦理和克南处境【源ID：100】 | 第4轮 / 二、完整阅读卡（67） / 56. 克南母亲喝骂：家庭权力、举报伦理和克南处境 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 138 | F138 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 57. 克南找黄亚萍坦白母亲所为：主动承担而不是甩锅【源ID：103】 | 第4轮 / 二、完整阅读卡（67） / 57. 克南找黄亚萍坦白母亲所为：主动承担而不是甩锅 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 139 | F139 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 58. 走后门被查实和叔父退回去：制度清算节点【源ID：104】 | 第4轮 / 二、完整阅读卡（67） / 58. 走后门被查实和叔父退回去：制度清算节点 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 140 | F140 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 59. 黄亚萍恨父亲冷酷：溺爱、主体性和绝对化语言【源ID：107】 | 第4轮 / 二、完整阅读卡（67） / 59. 黄亚萍恨父亲冷酷：溺爱、主体性和绝对化语言 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 141 | F141 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 60. 烟和火柴反复掏扔：心理失序的动作细读【源ID：111】 | 第4轮 / 二、完整阅读卡（67） / 60. 烟和火柴反复掏扔：心理失序的动作细读 | PartA card heading cleanup; repair=0; new=0 | article_links=写法线索; non-identity index only |
| 142 | F142 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 61. 克南不愿你们痛苦：温厚与无力感【源ID：116】 | 第4轮 / 二、完整阅读卡（67） / 61. 克南不愿你们痛苦：温厚与无力感 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 143 | F143 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 62. 黄亚萍“崇高的牺牲”：真情与自我戏剧化【源ID：119】 | 第4轮 / 二、完整阅读卡（67） / 62. 黄亚萍“崇高的牺牲”：真情与自我戏剧化 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 144 | F144 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 63. 巧珍跪求姐姐帮高加林：旧情未死与善良责任【源ID：124】 | 第4轮 / 二、完整阅读卡（67） / 63. 巧珍跪求姐姐帮高加林：旧情未死与善良责任 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 145 | F145 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 64. 巧珍拒绝再伤马拴：善良底色与责任感【源ID：125】 | 第4轮 / 二、完整阅读卡（67） / 64. 巧珍拒绝再伤马拴：善良底色与责任感 | PartA card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 146 | F146 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 65. 德顺说丢了金子：结尾价值判断的第一锤【源ID：129】 | 第4轮 / 二、完整阅读卡（67） / 65. 德顺说丢了金子：结尾价值判断的第一锤 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 147 | F147 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 66. 山、水、土地养活我们：土地与跌倒再起【源ID：131】 | 第4轮 / 二、完整阅读卡（67） / 66. 山、水、土地养活我们：土地与跌倒再起 | PartA card heading cleanup; repair=0; new=0 | article_links=城乡主题; non-identity index only |
| 148 | F148 | 保留为完整卡 | 完整卡 | 第4轮 / 二、完整阅读卡（67） / 67. “我的亲人哪……”：终章情感收束【源ID：132】 | 第4轮 / 二、完整阅读卡（67） / 67. “我的亲人哪……”：终章情感收束 | PartA card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 149 | F149 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 1. 高玉智 / 基层权力人物补证【源IDs：005】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 1. 高玉智 / 基层权力人物补证 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 150 | F150 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 2. 刘玉海 / 好干部群像补证【源IDs：023, 025】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 2. 刘玉海 / 好干部群像补证 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 151 | F151 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 3. 黄亚萍人物弧线：市民气息、自我中心、冷感语言和台阶【源IDs：035, 047, 063, 065, 066, 069, 077, 083, 105, 108, 121】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 3. 黄亚萍人物弧线：市民气息、自我中心、冷感语言和台阶 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 152 | F152 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 4. 克南人物弧线：低位修补、正直不忍和温厚伦理【源IDs：037, 101, 102】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 4. 克南人物弧线：低位修补、正直不忍和温厚伦理 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=爱情线; non-identity index only |
| 153 | F153 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 5. 巧珍、刘立本、马拴人物弧线：父爱转折、善良豁达和乡村婚姻秩序【源IDs：088, 090, 093, 094】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 5. 巧珍、刘立本、马拴人物弧线：父爱转折、善良豁达和乡村婚姻秩序 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; 爱情线; non-identity index only |
| 154 | F154 | 保留为完整卡 | 人物主线 | 第4轮 / 三、人物主线卡（27 个源 ID，只承载人物弧线补证） / 6. 高加林结尾人物弧线：被崇拜感失落、失势后的真实、身份敏感和忏悔开端【源IDs：082, 110, 115, 118, 126, 127】 | 第4轮 / 三、人物主线卡（只承载人物弧线补证） / 6. 高加林结尾人物弧线：被崇拜感失落、失势后的真实、身份敏感和忏悔开端 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; 尊严主题; non-identity index only |
| 155 | F155 | 保留为轻卡 | 轻卡 | 第4轮 / 四、轻卡存档 / 阅读心流（15 个源 ID） / 1. 命运转折、进城陶醉和职业热血的轻触点【源IDs：011, 015, 017, 018, 020】 | 第4轮 / 四、轻卡存档 / 阅读心流 / 1. 命运转折、进城陶醉和职业热血的轻触点 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 156 | F156 | 保留为轻卡 | 轻卡 | 第4轮 / 四、轻卡存档 / 阅读心流（15 个源 ID） / 2. 关系冷却、分手痛点和自我悲壮化的短刺【源IDs：042, 054, 059, 072, 073, 075】 | 第4轮 / 四、轻卡存档 / 阅读心流 / 2. 关系冷却、分手痛点和自我悲壮化的短刺 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 157 | F157 | 保留为轻卡 | 轻卡 | 第4轮 / 四、轻卡存档 / 阅读心流（15 个源 ID） / 3. 婚礼声里的局外人和黄土姑娘体面动作【源IDs：096, 097】 | 第4轮 / 四、轻卡存档 / 阅读心流 / 3. 婚礼声里的局外人和黄土姑娘体面动作 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=写法线索; non-identity index only |
| 158 | F158 | 保留为轻卡 | 轻卡 | 第4轮 / 四、轻卡存档 / 阅读心流（15 个源 ID） / 4. 失势后的自我评价和梦想幻觉意象【源IDs：112, 113】 | 第4轮 / 四、轻卡存档 / 阅读心流 / 4. 失势后的自我评价和梦想幻觉意象 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 159 | F159 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 1. 关系办事和权力潜规则素材【源IDs：007, 008, 016】 | 第4轮 / 五、主题素材库 / 待回看 / 1. 关系办事和权力潜规则素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 160 | F160 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 2. 爱情被前途编码素材【源IDs：056】 | 第4轮 / 五、主题素材库 / 待回看 / 2. 爱情被前途编码素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 161 | F161 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 3. 责任伦理与结构因素分歧素材【源IDs：106】 | 第4轮 / 五、主题素材库 / 待回看 / 3. 责任伦理与结构因素分歧素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 162 | F162 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 4. 布鞋、身份羞耻和迟到懂得素材【源IDs：114】 | 第4轮 / 五、主题素材库 / 待回看 / 4. 布鞋、身份羞耻和迟到懂得素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=尊严主题; non-identity index only |
| 163 | F163 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 5. 乡村权力风向感素材【源IDs：123】 | 第4轮 / 五、主题素材库 / 待回看 / 5. 乡村权力风向感素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 164 | F164 | 待回看 | 主题素材 | 第4轮 / 五、主题素材库 / 待回看（8 个源 ID） / 6. 乡土接纳与现实分歧素材【源IDs：128】 | 第4轮 / 五、主题素材库 / 待回看 / 6. 乡土接纳与现实分歧素材 | PartA ancestor/card heading cleanup; repair=0; new=0 | article_links=人物线; non-identity index only |
| 165 | F165 | 归档不迁移 | 外部读者残留 | 第4轮 / 六、全局外部读者残留材料（仅非卡片专属材料） / 1. 乡土温情可能带有路遥式理想化【external-源ID：128】 | 第4轮 / 六、全局外部读者残留材料（仅非卡片专属材料） / 1. 乡土温情可能带有路遥式理想化 | PartA heading+local range cleanup; repair=0; new=0 | none; identity stays formal_key+post_anchor |

## Article-link identity proof

- Anchor-map article direction blueprint count: `6` -> `人物线; 城乡主题; 尊严主题; 爱情线; 知识分子困境; 写法线索`.
- Distinct article links present on existing card rows: `5` -> `人物线; 写法线索; 城乡主题; 尊严主题; 爱情线`; `知识分子困境` remains a Todo 9 indexing direction, not a card identity.
- No card uses article direction as archive identity; article links remain separable evidence for Todo 9 indexing.
- Qualified-card movement check: `pre anchor -> post anchor` is one row per key, and no key is repeated or missing.
- Disappearance/duplication check: 165 preservation keys == 165 anchor keys == 165 final audited rows; duplicate readable anchors remain `none` in anchor map.
- Changed identity due to article links: none. Rows with article links keep the same `formal_key`; only heading metadata was cleaned where Part A approved it.
