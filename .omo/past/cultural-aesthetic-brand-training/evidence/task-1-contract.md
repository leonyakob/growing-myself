# Task 1 Contract Evidence

## $ test -f .omo/drafts/cabt-00-contract.md
exit=0
stdout:
(empty)
stderr:
(empty)

## $ grep -n 文化阅读.*个人.*精华 .omo/drafts/cabt-00-contract.md
exit=0
stdout:
17:核心层级必须逐级展开：文化阅读 -> 个人文化精华提取 -> 现代转译 -> 个人观点 -> 审美表达 -> AI 中长视频协作 -> 品牌/频道系统.
19:最终方案必须把文化阅读和个人文化精华提取放在根部。审美表达、AI 脚本协作、品牌/频道系统都是下游结果，不能反过来主导训练。
stderr:
(empty)

## $ grep -n 10-20 .omo/drafts/cabt-00-contract.md
exit=0
stdout:
11:最终方案要服务的成果是稳定产出 10-20 分钟中长视频。视频要有文化根、个人观点、审美表达和温柔但有判断力的叙述节奏。
29:最终方案要教用户判断：为什么是我被这句话、这个人物、这个器物、这个空间击中；它和现代人的关系、时间、女性自我、秩序、品味、日常仪式有什么关系；它如何进入一条 10-20 分钟中长视频的核心观点。
41:7. 10-20 分钟中长视频系统
53:视频格式必须围绕 10-20 分钟中长视频训练，结构要容纳文化或文学或器物场景、解释转折、个人精华、现代转译、审美落点和温和行动引导。
stderr:
(empty)

## $ grep -n 30/90/180 .omo/drafts/cabt-00-contract.md
exit=0
stdout:
42:8. 30/90/180 天节奏
51:30/90/180 天节奏必须呈现为阶段训练安排，而不是逐日穷尽式日历。可以给日常模块、每周复盘、阶段输出和进阶标准，但不要写成完整 day-by-day calendar。
stderr:
(empty)

## $ grep -n 文学文化.*器物空间 .omo/drafts/cabt-00-contract.md
exit=0
stdout:
21:前 90 天训练重心必须是文学文化与器物空间。品牌/频道只做基础边界、语气和内容方向的整理，不进入商业化扩展。
stderr:
(empty)

## $ grep -n 不要.*短视频 .omo/drafts/cabt-00-contract.md
exit=0
stdout:
63:不要把短视频作为主要输出，不要用短视频钩子或平台算法逻辑来设计训练主线。
stderr:
(empty)

## $ python3 top-level-heading-check
top_level_heading_count=8
forbidden_heading_matches=(empty)
PASS

## Overall
PASS
