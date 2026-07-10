# 《人生》第4轮正式笔记替换结构设计（Todo 3）

- Plan source: `.omo/plans/revise-ren-sheng-round4-notes.md` Todo 3.
- Classification source: `.omo/evidence/task-2-round4-classification.md`，尤其是 `Category summary` 与 `Promotion watchlist`。
- Inventory source: `.omo/evidence/task-1-round4-inventory.md`。
- Current formal-note shape checked only for structure/cursor: `路遥/人生/《人生》阅读笔记.md:1701-2239`。
- Scope: 本文件只设计目标 heading architecture，不写正式替换正文，不修改正式阅读笔记，不修改中间稿，不改计划 checkbox。

## 0. Non-negotiable structure decision

Todo 3 必须从 Todo 2 的重分级出发，而不是从当前正式稿的压缩形状出发。

- 当前正式稿第4轮是 `5` 个文章核心候选 + `4` 个完整阅读卡 + 宽泛人物线/轻卡/素材库；它还在开头明说“人物线压缩归并”“外部读者材料单独归入外部读者精彩高赞想法”。这正是本轮要修复的失败模式。
- Todo 2 已重新判定：`15` 个 `article-core candidate`，`67` 个 `complete reading card`，`27` 个 `人物主线卡`，`15` 个 `light card`，`8` 个 `theme/material bank`，`0` 个完全不迁移。
- 因此新结构至少要让 `15 + 67 = 82` 个强卡源 ID 在 heading level 可见。人物主线、轻卡、素材库只能承载 Todo 2 已判为对应类别的 ID，不能吞掉 article-core 或 complete-card ID。

## 1. Preserved reading range and cursor

Target section heading remains:

```markdown
## 第4轮阅读笔记：第十三章至第二十三章
```

Opening metadata should preserve the same conceptual range:

- 阅读范围：第十三章至第二十三章 / `chapterUid=16` 至 `chapterUid=26` / 至 `range=8942-8951`。
- 本轮重点可以重写，但必须覆盖：进城/借权、身份羞耻、黄亚萍与南京诱惑、巧珍分手与复原、克南伦理、终章土地/德顺/亲人。

Final cursor remains:

```markdown
## 七、下次接着整理位置

- 第二十三章 / `chapterUid=26` / `range=8942-8951` 之后。
- 当前最后一条划线原文：“我的亲人哪……”
```

Note for later todos: interface traces (`chapterUid`, `range`) are allowed in range/cursor only, not inside card bodies or external-reader entries.

## 2. Proposed top-level architecture

```markdown
## 第4轮阅读笔记：第十三章至第二十三章
### 结构说明：本轮按 Todo 2 重分级展开，不按当前 5+4 压缩稿控量

## 一、文章核心候选（15）
## 二、完整阅读卡（67）
## 三、人物主线卡（27 个源 ID，只承载人物弧线补证）
## 四、轻卡存档 / 阅读心流（15 个源 ID）
## 五、主题素材库 / 待回看（8 个源 ID）
## 六、全局外部读者残留材料（仅非卡片专属材料）
## 七、下次接着整理位置
```

Design rule: every source ID promoted in Todo 2 to `article-core candidate` or `complete reading card` gets a visible card heading below. Cross-links may point across sections, but cross-linking never replaces the source ID's own destination.

## 3. Section 一：文章核心候选（15 headings）

These are not capped. The current five retained core cards stay, but ten promoted cards must be added.

### 1. 借来的权力光：高玉德为什么非要带弟弟去吃这顿饭【源ID：009；status：retained-expand】

### 2. 同一句“乡巴佬”：身份位置如何改变刺痛度【源ID：030；status：promoted-from-current-人物线】

### 3. 一句“两个人都有点兴奋”：情感越界前最轻的一圈水纹【源ID：039；status：retained-expand】

### 4. 黄亚萍的爱情价值地图：爱一个人，也是爱一条去远方的路【源ID：048；status：retained-expand】

### 5. “让我好好想一想”：欲望已经点头，伦理还在拖他的手【源ID：053；status：retained-expand】

### 6. 不能为巧珍贻误转折：前途欲望和处理巧珍的伦理【源ID：057；status：promoted-from-current-external-only】

### 7. “自我毁灭”：阶层话语怎样刺中高加林的身份伤疤【源ID：060；status：promoted】

### 8. 门当户对刺痛自尊：高加林的自卑和自负怎样互相翻面【源ID：064；status：promoted】

### 9. 怕巧珍痛不欲生让他下不了台：把别人的伤换算成自己的风险【源ID：070；status：promoted】

### 10. 德顺骂“良心卖了”：土地尺度上的道德审判【源ID：084；status：promoted】

### 11. 县城变小、陌生：眼界崩塌和欲望退潮【源ID：109；status：promoted】

### 12. 克南的直线伦理与高加林的斜坡伦理【源ID：117；status：retained-expand】

### 13. “我真正爱的人实际上是另外一个”：更爱巧珍里的真情、偏见和自我辩护【源ID：120；status：promoted】

### 14. “并非结局”：故事有结局，人生没有结局【源ID：122；status：promoted】

### 15. 德顺生活哲学：劳动、跌倒和重新做人【源ID：130；status：promoted】

## 4. Section 二：完整阅读卡（67 headings）

Organization is by reading flow / chapter arc, not by a quota. Each heading below is a real destination. If Todo 4 later decides to merge prose for readability, it must still keep every source ID visible as a subheading or explicit card heading; no source ID in this section may vanish into a paragraph list.

### A. 第十三章：进城风声、关系办事和借权场面

#### 1. 村庄消息风和破墙烂院：外部荣光怎样照见贫穷现场【源ID：001】

#### 2. 动作零碎：希望如何先改造高加林的身体【源ID：002】

#### 3. 马占胜搂肩承诺工作：关系链如何让办事速度突然激活【源ID：003】

#### 4. 一声“老马”：同一称呼在新权力场里的变味【源ID：004】

#### 5. “加林恐怕不愿去掏炭”：体面劳动与身份回落【源ID：006】

#### 6. 瘦手哆嗦接酒：高玉德一杯酒里的翻身、羞怯和辛酸【源ID：010】

#### 7. 白天不能亲巧珍：亲密方式开始受场合和体面约束【源ID：012】

#### 8. “怔怔地望了一眼”：承诺和预感里的动作细读【源ID：013】

#### 9. 仍热爱故乡田地：离开土地的人为什么还被土地牵住【源ID：014】

### B. 下篇开端至救灾报道：县城欲望、职业复活和干部对照

#### 10. “我再也不能离开你了”：县城像恋人，也像审判者【源ID：019】

#### 11. 喝路边水坑、脚流血：高加林肯为被认可的前途吃苦【源ID：021】

#### 12. 第一个到达灾区：个体积极与系统迟缓【源ID：022】

#### 13. 硬要跟救灾队走：爱情亏欠与工作担当并存【源ID：024】

#### 14. 马占胜、高明楼和刘玉海：干部群像对照【源ID：026】

#### 15. 会议上毫不拘束提问：高加林的职业适配【源ID：027】

#### 16. 第一篇报道被播出：职业承认和景老师一字未改【源ID：028】

### C. 黄亚萍、克南与早期情感重排

#### 17. 克南是实业家：不是“没出息”的前置证据【源ID：029】

#### 18. 先顾虑黄亚萍与克南：公开关系和隐秘关系的伦理双标【源ID：031】

#### 19. “怕影响”而不说有对象：事业自保与暧昧保留【源ID：032】

#### 20. 克南照料黄亚萍：照料、感激与爱情温差【源ID：033】

#### 21. 黄亚萍不愿嫁农民：她的爱与生活边界【源ID：034】

#### 22. 骂克南“胖成个猪”：语言暴力与关系高位【源ID：036】

#### 23. 想到亚萍后更想巧珍：精神越界与补偿式深情【源ID：038】

### D. 关系冷却和越界推进

#### 24. “这不是在庄稼地里”：身份空间切割【源ID：040】

#### 25. “我不冷！你千万不要拿来！”：拒绝照料与身份切割【源ID：041】

#### 26. 巧珍贴身拿钱：务实照料链的具体动作【源ID：043】

#### 27. 红头巾的浪漫与实际：高加林的想象满足了谁【源ID：044】

#### 28. 亲热不如从前陶醉：关系退潮的身体证据【源ID：045】

#### 29. 黄亚萍“无论如何”要和高加林：同类感、占有欲与自我中心【源ID：046】

#### 30. 克南竟看不出她爱加林：老实、痛苦和关系盲区【源ID：049】

#### 31. 同时想黄亚萍和巧珍：两种女性、两种生活、两种自我想象【源ID：050】

#### 32. 风暴将临、激动又战栗：表白前心理风暴【源ID：051】

#### 33. “我希望不是他，而是你”：表白里的 offer 与前途诱惑【源ID：052】

### E. 第十八章：前途、阶层话语和高加林的选择状态

#### 34. 现实与梦想互变：高加林价值秩序倒转【源ID：055】

#### 35. 像疯子一样转圈碰墙：分手方案、面子和自我人设【源ID：058】

#### 36. “巧珍从来也不这样对我说话”：怀念的是人，还是被供奉的感觉【源ID：061】

#### 37. 恍惚地点头：半清醒状态里的顺势选择【源ID：062】

#### 38. 厚嘴唇像蜜蜂翅膀：路遥身体细节写法卡【源ID：067】

#### 39. 硬把母亲推出房子：黄亚萍果断里的伤人硬度【源ID：068】

### F. 第十九章：分手现场、公开新关系和关系权力

#### 40. 半截分手话：高加林怎样把刀递给巧珍【源ID：071】

#### 41. 头也不回飞跑而去：分手后的体面与尊严【源ID：074】

#### 42. 青山绿水鲜明：轻松感与环境变亮的冷感【源ID：076】

#### 43. 两人公开高调骑车：公开陈列的伦理后果【源ID：078】

#### 44. 亚萍任性、高加林不如从前自在：向上关系里交出主导权【源ID：079】

#### 45. 进口削苹果刀丢了：精致物件与利己试探【源ID：080】

#### 46. “故意开玩笑”测试听话程度：黄亚萍的服从性测试【源ID：081】

#### 47. 坏情绪很快消失：野心排序如何压过愧疚【源ID：085】

### G. 第二十章：巧珍复原、父亲转向、马拴和德顺

#### 48. 巧珍从地上爬起来：复原能力的关键动作【源ID：086】

#### 49. 巧珍为什么要挣扎着下地去劳动：劳动与土地止痛【源ID：087】

#### 50. 立本不再勉强女儿婚事：粗硬父爱转向温柔【源ID：089】

#### 51. 马拴“不嫌”：质朴、再婚伦理和现实支点【源ID：091】

#### 52. “就在这几天”同意婚事：带痛继续生存【源ID：092】

#### 53. 德顺老汉躺炕流泪：旧情与重感情【源ID：095】

#### 54. “我还得活人”：巧珍把痛转成责任【源ID：098】

#### 55. 刘立本长舒一口气：父亲卸力和仪式收束【源ID：099】

### H. 第二十一章：举报、坦白、制度清算和家庭语言

#### 56. 克南母亲喝骂：家庭权力、举报伦理和克南处境【源ID：100】

#### 57. 克南找黄亚萍坦白母亲所为：主动承担而不是甩锅【源ID：103】

#### 58. 走后门被查实和叔父退回去：制度清算节点【源ID：104】

#### 59. 黄亚萍恨父亲冷酷：溺爱、主体性和绝对化语言【源ID：107】

### I. 第二十二章至终章前：失势、伦理摊牌和结尾前的心理动作

#### 60. 烟和火柴反复掏扔：心理失序的动作细读【源ID：111】

#### 61. 克南不愿你们痛苦：温厚与无力感【源ID：116】

#### 62. 黄亚萍“崇高的牺牲”：真情与自我戏剧化【源ID：119】

### J. 第二十三章：巧珍求情、责任边界、土地和亲人

#### 63. 巧珍跪求姐姐帮高加林：旧情未死与善良责任【源ID：124】

#### 64. 巧珍拒绝再伤马拴：善良底色与责任感【源ID：125】

#### 65. 德顺说丢了金子：结尾价值判断的第一锤【源ID：129】

#### 66. 山、水、土地养活我们：土地与跌倒再起【源ID：131】

#### 67. “我的亲人哪……”：终章情感收束【源ID：132】

## 5. Section 三：人物主线卡（27 source IDs, no swallowing）

人物主线卡只处理 Todo 2 明确归为 `人物主线卡` 的源 ID。它们可以串联人物弧线，但不得吸收上面任何 article-core 或 complete-card heading。

### 1. 高玉智 / 基层权力人物补证【源IDs：005】

- Text reason: `005` 是“组织信任”的议论式补证，服务高玉智正直真假，不独立成完整问题链。

### 2. 刘玉海 / 好干部群像补证【源IDs：023, 025】

- Text reason: `023, 025` 是刘玉海受伤和“只要人在”的人物刻度，服务 `026` 干部群像完整卡，但不替代 `026`。

### 3. 黄亚萍人物弧线：市民气息、自我中心、冷感语言和台阶【源IDs：035, 047, 063, 065, 066, 069, 077, 083, 105, 108, 121】

- Text reason: these IDs are character-arc supplements. They may support `048, 060, 068, 107, 119` but cannot swallow those independent cards.

### 4. 克南人物弧线：低位修补、正直不忍和温厚伦理【源IDs：037, 101, 102】

- Text reason: these IDs support 克南的温厚/正直，但 `100, 103, 116, 117` remain separate strong headings.

### 5. 巧珍、刘立本、马拴人物弧线：父爱转折、善良豁达和乡村婚姻秩序【源IDs：088, 090, 093, 094】

- Text reason: these are small but necessary arc pieces; `086, 087, 089, 091, 092, 098, 099, 124, 125` remain independent complete cards.

### 6. 高加林结尾人物弧线：被崇拜感失落、失势后的真实、身份敏感和忏悔开端【源IDs：082, 110, 115, 118, 126, 127】

- Text reason: these IDs support the late 高加林 arc; `109, 111, 120, 122, 130, 131, 132` remain independent headings.

## 6. Section 四：轻卡存档 / 阅读心流（15 source IDs）

Light cards preserve reading现场感 and short affective cues. They are not a catch-all; each group has exact IDs and a text reason for staying light.

### 1. 命运转折、进城陶醉和职业热血的轻触点【源IDs：011, 015, 017, 018, 020】

- Text reason: these are atmosphere/transition cues; the stronger career cards are already split as `019, 021, 022, 024, 026, 027, 028`.

### 2. 关系冷却、分手痛点和自我悲壮化的短刺【源IDs：042, 054, 059, 072, 073, 075】

- Text reason: these carry tone/action flashes; the independent cards are `040, 041, 071, 074, 076`.

### 3. 婚礼声里的局外人和黄土姑娘体面动作【源IDs：096, 097】

- Text reason: short contrast/action records that support `098, 099` but do not need independent full scaffolding.

### 4. 失势后的自我评价和梦想幻觉意象【源IDs：112, 113】

- Text reason: compact reflective/imagistic cues; they can support `109, 111, 122, 130` but should not be inflated into full cards.

## 7. Section 五：主题素材库 / 待回看（8 source IDs）

Theme/material bank is for motifs or structural materials that do not yet form an independent card. It is not a disposal bucket.

### 1. 关系办事和权力潜规则素材【源IDs：007, 008, 016】

- Text reason: these are口语化制度逻辑和关系网络材料；they support `003, 004, 009, 026` but are not independent scenes.

### 2. 爱情被前途编码素材【源IDs：056】

- Text reason: `056` is a clear thematic statement; it should be used as a motif bridge for `053, 057, 060`.

### 3. 责任伦理与结构因素分歧素材【源IDs：106】

- Text reason: 老军人“不要抱怨生活” is a debate node about individual responsibility vs structure, not a full narrative card.

### 4. 布鞋、身份羞耻和迟到懂得素材【源IDs：114】

- Text reason: `114` is a motif object that should support `064, 109, 130` but not replace them.

### 5. 乡村权力风向感素材【源IDs：123】

- Text reason: 高明楼政治敏感 is political-weather material for final village structure, not a full card.

### 6. 乡土接纳与现实分歧素材【源IDs：128】

- Text reason: `128` source card is light/material, but its external-reader challenge has global value; see Section 六 for the external-reader placement.

## 8. Section 六：全局外部读者残留材料（non-card-specific only）

Default rule for Todo 4/8: high-value external reader original comments follow the specific article-core or complete-card they illuminate. They must not be centralized into a broad “精彩高赞想法” section.

### 1. 乡土温情可能带有路遥式理想化【external-source anchor：128；cross-links：122, 130, 131, 132】

- Why this remains global: the external challenge around `128` is not only about one sentence; it questions the whole ending's乡土接纳 scene. It should remain as a small global counterpoint after the card-specific comments, cross-linked to the ending cards.
- This is the only planned global external-reader leftover. It is justified by exact ID and text function, so it is not a catch-all bucket.

## 9. Catch-all audit

- No `其他`, `杂项`, `待定`, or unbounded “素材” bucket is allowed.
- 人物主线 section has exact IDs and only contains IDs Todo 2 classified as `人物主线卡`.
- 轻卡 section has exact IDs and text reasons for light treatment.
- 主题素材库 has exact IDs and text reasons for material-bank treatment.
- 全局外部读者残留材料 has exactly one source anchor, `128`, because the external challenge targets the ending's overall乡土温情, not a single card.
- All article-core IDs are visible at heading level: `009, 030, 039, 048, 053, 057, 060, 064, 070, 084, 109, 117, 120, 122, 130`.
- All complete-card IDs are visible at heading level: `001, 002, 003, 004, 006, 010, 012, 013, 014, 019, 021, 022, 024, 026, 027, 028, 029, 031, 032, 033, 034, 036, 038, 040, 041, 043, 044, 045, 046, 049, 050, 051, 052, 055, 058, 061, 062, 067, 068, 071, 074, 076, 078, 079, 080, 081, 085, 086, 087, 089, 091, 092, 095, 098, 099, 100, 103, 104, 107, 111, 116, 119, 124, 125, 129, 131, 132`.

## 10. Why the new structure must be more granular than the current 5 core + 4 complete-card shape

1. Todo 2 establishes a material-value count, not an aesthetic preference: `15` article-core candidates and `67` complete reading cards. A 5+4 structure can only work by demoting or hiding most of those IDs.
2. The current formal note already shows the failure mode: `030` is buried in a 高加林人物线 despite plan protection; `057` survives only as external-reader correction; `019, 021, 022, 024, 026, 027, 028` are swallowed by “职业复活” light-card phrasing; `040, 041` are swallowed by “关系冷却”；ending materials are collapsed into one broad land/德顺 card.
3. Several Todo 2 promotions are article-level arguments, not supporting examples: `060, 064, 070, 084, 109, 120, 122, 130` each asks a different question. Compressing them into人物线 or terminal material bank would erase the user's problem-chain training.
4. The high-risk complete-card zone (`061, 076, 079, 081, 089, 091, 095, 099, 103, 104, 111, 116, 119, 124, 125`) contains independent actions, objects, ethical collisions, or question chains. None of them can be represented honestly by a generic “人物复杂性” or “结尾土地” bucket.
5. External-reader comments need card-local placement. The current separate external-reader section turns comments into detached applause/challenge; the new structure forces Todo 4/8 to attach them to the source card they actually test.

## 11. Collision risks for Todo 4-6

- **Risk: article-core swallowed by人物主线.** `030, 057, 060, 064, 070, 084, 109, 120, 122, 130` must remain article-core headings. They may cross-link to人物线 but cannot be summarized there.
- **Risk: complete cards swallowed by人物主线.** Protect especially `061, 076, 079, 081, 089, 091, 095, 099, 100, 103, 104, 111, 116, 119, 124, 125`.
- **Risk: current “职业复活” light-card group repeats.** `019, 021, 022, 024, 026, 027, 028` must appear as complete-card headings, not one career paragraph.
- **Risk: current “关系冷却中的小刺” repeats.** `040, 041, 043, 044, 045` must stay independent complete cards where classified, with `042` alone remaining light.
- **Risk: ending collapse.** `122` and `130` are article-core headings; `129, 131, 132` are complete-card headings. They can form a final arc, but not a single catch-all “土地与结尾” card.
- **Risk: external comments centralized again.** All card-specific external reader原话 should move into the matching article-core/complete card. Only the `128` ending-wide challenge stays global.
- **Risk: source IDs disappear during prose drafting.** Todo 4 should keep a source-ID mapping table and preserve heading-level ID visibility for all `15` article-core and `67` complete-card destinations.

## 12. Todo 4 handoff checklist

- Draft replacement prose in `.omo/evidence/task-4-round4-replacement-draft.md`, not in the formal note.
- Keep this outline's reading range and final cursor.
- Start from the 15 article-core headings and 67 complete-card headings above.
- For article-core and key complete cards, restore the four-part structure and required scaffolding: `我自己写的内容 / AI评价 / AI修正 / AI补充`, question-chain upgrade, current answer, new-angle question chain, new-angle answer, expansion direction, same-book linkage, cross-work linkage.
- Add external-reader original comments locally under matching cards; do not use “有读者说” as a replacement for original comments.
- If Todo 4 proposes any merge for reading flow, it must preserve source IDs at heading/subheading level and explain why no independent card is swallowed.

## 13. Verification summary

- Proposed article-core headings: 15.
- Proposed complete-card headings: 67.
- Current compressed shape rejected: yes; this file explains why 5 core + 4 complete-card is structurally too small.
- Unjustified catch-all bucket remains: no.
- Any remaining global bucket justified: yes, exact anchor `128`, because its external-reader challenge targets the whole ending's乡土温情 rather than one card.
- Formal reading note modified: no.
- Middle draft modified: no.
- Plan checkbox modified: no.
