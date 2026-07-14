# Task 1 Evidence, split-weread-prompts-by-stage

EXECUTION_START_FULL_STATUS_BASELINE:

- Command: `GIT_MASTER=1 git status --short --untracked-files=all`
- Capture timing note: captured before snapshot creation and before any router/stage rewrite. Two baseline manifest outputs were created immediately afterward under `.omo/evidence/split-weread-prompts-by-stage/`; they are excluded from the execution-start baseline reproduced below.

```text
 M .omo/boulder.json
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
?? .omo/drafts/split-weread-prompts-by-stage.md
?? .omo/notepads/split-weread-prompts-by-stage/decisions.md
?? .omo/notepads/split-weread-prompts-by-stage/issues.md
?? .omo/notepads/split-weread-prompts-by-stage/learnings.md
?? .omo/notepads/split-weread-prompts-by-stage/problems.md
?? .omo/plans/split-weread-prompts-by-stage.md
?? .omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json
?? .omo/run-continuation/ses_0a01a8776ffeYwcR6fvZdAoY5r.json
?? .omo/run-continuation/ses_0a01a8e47ffeYr9v0ncZojf00k.json
?? .omo/run-continuation/ses_0a03136cdffeQeJo5HGzBeaFJ7.json
?? .omo/run-continuation/ses_0a0313cc1ffeDs4wk7mySXWaRG.json
?? .omo/run-continuation/ses_0a0315f0fffeYD4ht9ZodUJcEs.json
?? .omo/run-continuation/ses_0a053a4f2ffe2e6asIm1nmpIHX.json
?? .omo/run-continuation/ses_0a053a964ffeOp88fi1dr9HON7.json
?? .omo/run-continuation/ses_0a053adccffeyqD2TAxf3iYMwz.json
?? .omo/run-continuation/ses_0a05edc31ffeHyxJoXHbyXWUdH.json
?? .omo/run-continuation/ses_0a05ee03effe6FHPEnPt79F2P2.json
?? .omo/run-continuation/ses_0a05f004cffesHx8UcKTkCAy0F.json
?? .omo/run-continuation/ses_0a06c60bcffeSnl1YK3NSKOSqp.json
?? .omo/run-continuation/ses_0a06d5bcfffe71XStL7dXIsN2p.json
?? .omo/run-continuation/ses_0a06d601fffexgjjs2gZh4rM9d.json
?? .omo/run-continuation/ses_0a06d640affeioZOLLqybvmG08.json
?? .omo/run-continuation/ses_0a07d1be3ffe3cI1B0XREjk6R2.json
?? .omo/run-continuation/ses_0a07d1fbbffe9sfEFezX1ogxW4.json
?? .omo/run-continuation/ses_0a07d2374ffeKXyEHVKufwmLqb.json
?? .omo/run-continuation/ses_0a0aea4ebffe4R1xTrrbDBfsFs.json
?? .omo/run-continuation/ses_0a0af1498ffehIBXUvuU4B3XXW.json
?? .omo/run-continuation/ses_0a0af9914ffe6wbsKNkmiGksb8.json
?? .omo/run-continuation/ses_0a0bd9832ffeveDCOv3ovv2Orh.json
?? .omo/run-continuation/ses_0a0be0c42ffe6tD8gDjhyQE1rO.json
?? .omo/run-continuation/ses_0a0be802effevLZG8UMPoOoCT1.json
?? .omo/run-continuation/ses_0a0d4b290ffermbYAlRunogccm.json
?? .omo/run-continuation/ses_0a0d4b355ffecP8tv3AsIjvnBv.json
?? .omo/run-continuation/ses_0a38f3ab4ffeef29mCwDfOFb9p.json
?? .omo/run-continuation/ses_0a3a96147ffeZNiyUBCWeT5j8z.json
?? .omo/run-continuation/ses_0a3a9618dffe6DUIBa3NLfjSjD.json
?? .omo/run-continuation/ses_0a3a968d6ffeOFtqq2iaY1lKJK.json
?? .omo/run-continuation/ses_0a3a97e83ffepZ5hFW0heYU2RK.json
?? .omo/run-continuation/ses_0a3a98313ffeJB1LD2EloyPPNg.json
?? .omo/run-continuation/ses_0a3c98e9dffeoOfEBD4mt90n9u.json
?? .omo/run-continuation/ses_0a3ccb9cfffejI720jcbhHkaqt.json
?? .omo/run-continuation/ses_0a3ccba20ffe4cqWr5ftApuVgE.json
?? .omo/run-continuation/ses_0a3ccc30cffe7cQDnpeYZNFJZw.json
?? .omo/run-continuation/ses_0a3ccd654ffeC0Cl1YQTDkcMO1.json
?? .omo/run-continuation/ses_0a3ccec35ffevaFkGVBh6B49Jk.json
?? .omo/run-continuation/ses_0a3db3b18ffeOFwe4sqofWC3Oq.json
?? .omo/run-continuation/ses_0a3db48f9ffeBrHUVW9yXmRsBx.json
?? .omo/run-continuation/ses_0a3e2ddefffe9UlMJQZbBTSevf.json
?? .omo/run-continuation/ses_0a3f5807dffeWIV6VO7Q519CNY.json
?? .omo/run-continuation/ses_0a3f58101ffeFSXLqj87P2v6mX.json
?? .omo/run-continuation/ses_0a3f599dcffeymD00c5UFTJhR9.json
?? .omo/run-continuation/ses_0a4254ae4ffeHbwrgSj5gf86KV.json
?? .omo/run-continuation/ses_0a4254b6cffe0Nq6A3nrzYkESg.json
?? .omo/run-continuation/ses_0a42554d0ffe2cMSDPfgGsGJob.json
```

EXECUTION_START_RUN_CONTINUATION_STATUS_BASELINE:

- Command: `GIT_MASTER=1 git status --short --untracked-files=all -- .omo/run-continuation`

```text
 M .omo/run-continuation/ses_0f41d88e9ffesnm1U1JjgxoufB.json
?? .omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json
?? .omo/run-continuation/ses_0a01a8776ffeYwcR6fvZdAoY5r.json
?? .omo/run-continuation/ses_0a01a8e47ffeYr9v0ncZojf00k.json
?? .omo/run-continuation/ses_0a03136cdffeQeJo5HGzBeaFJ7.json
?? .omo/run-continuation/ses_0a0313cc1ffeDs4wk7mySXWaRG.json
?? .omo/run-continuation/ses_0a0315f0fffeYD4ht9ZodUJcEs.json
?? .omo/run-continuation/ses_0a053a4f2ffe2e6asIm1nmpIHX.json
?? .omo/run-continuation/ses_0a053a964ffeOp88fi1dr9HON7.json
?? .omo/run-continuation/ses_0a053adccffeyqD2TAxf3iYMwz.json
?? .omo/run-continuation/ses_0a05edc31ffeHyxJoXHbyXWUdH.json
?? .omo/run-continuation/ses_0a05ee03effe6FHPEnPt79F2P2.json
?? .omo/run-continuation/ses_0a05f004cffesHx8UcKTkCAy0F.json
?? .omo/run-continuation/ses_0a06c60bcffeSnl1YK3NSKOSqp.json
?? .omo/run-continuation/ses_0a06d5bcfffe71XStL7dXIsN2p.json
?? .omo/run-continuation/ses_0a06d601fffexgjjs2gZh4rM9d.json
?? .omo/run-continuation/ses_0a06d640affeioZOLLqybvmG08.json
?? .omo/run-continuation/ses_0a07d1be3ffe3cI1B0XREjk6R2.json
?? .omo/run-continuation/ses_0a07d1fbbffe9sfEFezX1ogxW4.json
?? .omo/run-continuation/ses_0a07d2374ffeKXyEHVKufwmLqb.json
?? .omo/run-continuation/ses_0a0aea4ebffe4R1xTrrbDBfsFs.json
?? .omo/run-continuation/ses_0a0af1498ffehIBXUvuU4B3XXW.json
?? .omo/run-continuation/ses_0a0af9914ffe6wbsKNkmiGksb8.json
?? .omo/run-continuation/ses_0a0bd9832ffeveDCOv3ovv2Orh.json
?? .omo/run-continuation/ses_0a0be0c42ffe6tD8gDjhyQE1rO.json
?? .omo/run-continuation/ses_0a0be802effevLZG8UMPoOoCT1.json
?? .omo/run-continuation/ses_0a0d4b290ffermbYAlRunogccm.json
?? .omo/run-continuation/ses_0a0d4b355ffecP8tv3AsIjvnBv.json
?? .omo/run-continuation/ses_0a38f3ab4ffeef29mCwDfOFb9p.json
?? .omo/run-continuation/ses_0a3a96147ffeZNiyUBCWeT5j8z.json
?? .omo/run-continuation/ses_0a3a9618dffe6DUIBa3NLfjSjD.json
?? .omo/run-continuation/ses_0a3a968d6ffeOFtqq2iaY1lKJK.json
?? .omo/run-continuation/ses_0a3a97e83ffepZ5hFW0heYU2RK.json
?? .omo/run-continuation/ses_0a3a98313ffeJB1LD2EloyPPNg.json
?? .omo/run-continuation/ses_0a3c98e9dffeoOfEBD4mt90n9u.json
?? .omo/run-continuation/ses_0a3ccb9cfffejI720jcbhHkaqt.json
?? .omo/run-continuation/ses_0a3ccba20ffe4cqWr5ftApuVgE.json
?? .omo/run-continuation/ses_0a3ccc30cffe7cQDnpeYZNFJZw.json
?? .omo/run-continuation/ses_0a3ccd654ffeC0Cl1YQTDkcMO1.json
?? .omo/run-continuation/ses_0a3ccec35ffevaFkGVBh6B49Jk.json
?? .omo/run-continuation/ses_0a3db3b18ffeOFwe4sqofWC3Oq.json
?? .omo/run-continuation/ses_0a3db48f9ffeBrHUVW9yXmRsBx.json
?? .omo/run-continuation/ses_0a3e2ddefffe9UlMJQZbBTSevf.json
?? .omo/run-continuation/ses_0a3f5807dffeWIV6VO7Q519CNY.json
?? .omo/run-continuation/ses_0a3f58101ffeFSXLqj87P2v6mX.json
?? .omo/run-continuation/ses_0a3f599dcffeymD00c5UFTJhR9.json
?? .omo/run-continuation/ses_0a4254ae4ffeHbwrgSj5gf86KV.json
?? .omo/run-continuation/ses_0a4254b6cffe0Nq6A3nrzYkESg.json
?? .omo/run-continuation/ses_0a42554d0ffe2cMSDPfgGsGJob.json
```

RUN_CONTINUATION_SHA256_BASELINE:

- Command: `GIT_MASTER=1 git ls-files -z --cached --others --exclude-standard -- .omo/run-continuation | LC_ALL=C sort -z | xargs -0 -r sha256sum > .omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`
- Manifest path: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/run-continuation.before.sha256`
- Manifest size: `15128` bytes

PROTECTED_BASELINE_SHA256:

- Manifest path: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/protected-baseline.before.sha256`

Protected baseline path list:

1. `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`
2. `/home/king/github/growing-myself/.omo/drafts/split-weread-prompts-by-stage.md`
3. `/home/king/github/growing-myself/.omo/boulder.json`
4. `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/decisions.md`
5. `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/problems.md`

Protected baseline risks and output-approved exclusions:

- Output-approved, pre-existing dirty paths intentionally excluded from the protected baseline manifest because this task may append to them: `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md`, `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/issues.md`.
- `.omo/run-continuation/**` paths are intentionally excluded from `protected-baseline.before.sha256` because they are covered by the dedicated run-continuation status baseline and `run-continuation.before.sha256` manifest.

BASELINES_CAPTURED_BEFORE_PLANNED_OUTPUTS: PASS


Source snapshot used:

- Live source: `/home/king/github/growing-myself/微信读书通用提示词.md`
- Immutable snapshot: `/home/king/github/growing-myself/.omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md`
- Verification rerun in this continuation used the existing snapshot; no regeneration performed.

```text
sha256sum "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"
ee9c7758f60fb1a2fae60f6eb525c6f5f95c88d13ba6dd76732ca8b12fb24e40  微信读书通用提示词.md
ee9c7758f60fb1a2fae60f6eb525c6f5f95c88d13ba6dd76732ca8b12fb24e40  .omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md
```

```text
wc -l "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"
  1236 微信读书通用提示词.md
  1236 .omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md
  2472 total
```

```text
cmp -s "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'
SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS
```

Applicable AGENTS.md:

- `/home/king/github/growing-myself/AGENTS.md`
- Generic prompt/stage work in Task 1 uses root `AGENTS.md` only.
- Not applicable / explicitly not imported here: any `路遥/人生/**` prompt file, `/home/king/github/growing-myself/路遥/人生/AGENTS.md`, `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md`, or any sibling-book `AGENTS.md`.

Files changed:

- `/home/king/github/growing-myself/.omo/evidence/task-1-split-weread-prompts-by-stage.md`
- `/home/king/github/growing-myself/.omo/notepads/split-weread-prompts-by-stage/learnings.md` (append-only; added after evidence completion)

Commands run:

- Baseline-capture and manifest-creation commands are preserved in the baseline sections above and were not rerun in this continuation.
- `sha256sum "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"`
- `wc -l "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md"`
- `cmp -s "微信读书通用提示词.md" ".omo/evidence/split-weread-prompts-by-stage/source/微信读书通用提示词.before.md" && printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS\n' || printf 'SNAPSHOT_VERBATIM_BEFORE_REWRITE: FAIL\n'`
- `python3 - <<'PY' ... target-file existence preflight ... PY`
- `functions.read` on snapshot ranges `1-220`, `358-577`, `846-985`, `977-1136`, `1109-1188`, `1160-1236` for move-ledger and semantic QA grounding.
- `ast-grep` applicability: not applicable, Markdown prompt prose only.

Target-file existence preflight:

| target path | status |
|---|---|
| `/home/king/github/growing-myself/微信读书通用提示词.md` | EXISTS |
| `/home/king/github/growing-myself/微信读书通用提示词-第一阶段-生成中间整理稿.md` | MISSING |
| `/home/king/github/growing-myself/微信读书通用提示词-第二阶段-优化中间整理稿.md` | MISSING |
| `/home/king/github/growing-myself/微信读书通用提示词-第三阶段-迁移到正式阅读笔记.md` | MISSING |
| `/home/king/github/growing-myself/微信读书通用提示词-第四阶段-全书收束整合.md` | MISSING |

Heading inventory

- Inventory source: immutable snapshot only.
- Inventory result: every snapshot heading/subheading below has exactly one disposition; `explicit out-of-scope stop` count is `0`.

| line | level | heading | disposition | note |
|---:|---:|---|---|---|
| 1 | 1 | 微信读书 Skill 通用整理提示词 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 16 | 2 | 0. 占位说明与路径规则 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 29 | 3 | 0.1 不可降级原则与任务入口门 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 44 | 2 | 1. 如何用通用提示词生成某本书专用提示词 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 60 | 3 | 专用提示词生成边界与验收门 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 69 | 2 | 2. 四阶段总流程 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 98 | 2 | 3. 多轮整理规则 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 105 | 2 | 第1轮整理：开头至第六章 | intentional duplication | 多轮整理示例标题，Router 规则示例，Stage 1 格式会再次承接。 |
| 107 | 2 | 第2轮整理：第七章至第十章 | intentional duplication | 多轮整理示例标题，Router 规则示例，Stage 1 格式会再次承接。 |
| 109 | 2 | 第3轮整理：…… | intentional duplication | 多轮整理示例标题，Router 规则示例，Stage 1 格式会再次承接。 |
| 122 | 2 | 4. 阶段切换前 QA 与条件式 Git 检查点 | generic router | 总入口权威规则、阶段路由、QA/Git 门。 |
| 157 | 2 | 5. 数据抓取硬约束 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 164 | 3 | 5.0 中间整理稿与正式阅读笔记的数据边界 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 189 | 3 | 5.1 跨段划线与想法匹配规则 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 233 | 3 | 5.2 同位置其他书友高赞想法默认伴随抓取规则 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 303 | 2 | 6. 颜色默认流向 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 332 | 2 | 7. 想法类别与卡片类型 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 334 | 3 | 7.1 想法类别 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 345 | 3 | 7.2 卡片类型 | generic Stage 1 | 数据抓取、匹配、颜色、分类。 |
| 358 | 2 | 8. 文学分析质量规则 | generic Stage 2 | 文学分析质量规则。 |
| 366 | 3 | 8.1 证据锚点与文本落点 | generic Stage 2 | 文学分析质量规则。 |
| 385 | 3 | 8.2 人物心理要写出过程，不要直接贴标签 | generic Stage 2 | 文学分析质量规则。 |
| 412 | 3 | 8.3 文本歧义与心理雾区不能一笔带过 | generic Stage 2 | 文学分析质量规则。 |
| 425 | 3 | 8.4 完整卡和主卡候选必须打开矛盾 | generic Stage 2 | 文学分析质量规则。 |
| 440 | 3 | 8.5 AI 要提供表达增量 | generic Stage 2 | 文学分析质量规则。 |
| 461 | 3 | 8.6 AI 可以反驳，但必须指出缺失的分析环节 | generic Stage 2 | 文学分析质量规则。 |
| 481 | 3 | 8.7 大胆分析，但不要省掉过程 | generic Stage 2 | 文学分析质量规则。 |
| 489 | 3 | 8.8 升级问题链后必须给出阶段性回答 | generic Stage 2 | 文学分析质量规则。 |
| 530 | 3 | 8.9 AI修正必须深化，不只是整理语序 | generic Stage 2 | 文学分析质量规则。 |
| 543 | 3 | 8.10 文学表达不是轻卡专属 | generic Stage 2 | 文学分析质量规则。 |
| 559 | 3 | 8.11 分析后命名，而非先命名硬套 | generic Stage 2 | 文学分析质量规则。 |
| 572 | 2 | 9. 第一阶段：生成中间整理稿 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 594 | 3 | 中间整理稿格式 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 597 | 1 | {作者}《{书名}》中间整理稿 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 599 | 2 | 整理说明 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 607 | 2 | 第N轮整理：范围说明 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 609 | 3 | 001. 章节名 / range | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 642 | 2 | 本轮索引 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 644 | 3 | 轻卡清单 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 646 | 3 | 完整卡候选 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 648 | 3 | 主卡候选 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 650 | 3 | 暂存素材 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 652 | 3 | 同位置其他书友高赞想法候选 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 654 | 3 | 颜色统计 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 656 | 3 | 下次接着整理位置 | generic Stage 1 | 第一阶段执行模板与中间稿格式。 |
| 661 | 2 | 10. 第二阶段：优化中间整理稿 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 677 | 3 | 10.1 本轮优化前诊断 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 682 | 2 | 第N轮优化前诊断 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 719 | 3 | 10.2 轻卡优化规则 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 747 | 3 | 10.3 完整卡 / 主卡优化规则 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 807 | 3 | 10.4 暂存素材处理规则 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 822 | 3 | 10.5 同位置其他书友高赞想法差异分析规则 | generic Stage 2 | 第二阶段执行模板与优化规则。 |
| 846 | 2 | 11. 第三阶段：迁移到正式阅读笔记 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 869 | 3 | 11.1 迁移前回源预检 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 879 | 3 | 11.2 正式阅读笔记结构与去除中间稿痕迹 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 918 | 3 | 11.3 正式阅读笔记游标更新规则 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 930 | 3 | 11.4 所有材料最终都要有归宿 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 943 | 3 | 11.5 外部读者材料迁移规则 | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 963 | 3 | 11.6 迁移后防回归 QA | generic Stage 3 | 第三阶段迁移与防回归 QA。 |
| 977 | 2 | 12. 第四阶段：读完整本书后的全书收束整合 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 983 | 3 | 12.1 第三阶段与第四阶段的边界 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 992 | 3 | 12.2 产物边界：内部整合台账与正式阅读笔记 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1000 | 3 | 12.3 多轴台账，不用单一“最终状态”替代材料 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1015 | 3 | 12.4 一卡双归宿，与两层正式稿结构 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1033 | 3 | 12.5 全书收束后的正式阅读笔记骨架 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1036 | 2 | 全书收束整合 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1038 | 3 | 一、阅读现场档案 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1041 | 3 | 二、文章素材索引 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1047 | 3 | 三、阅读轨迹与判断变化 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1050 | 3 | 四、待回看 / 归档不迁移 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1056 | 3 | 12.6 判重、回源与修订链规则 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1071 | 3 | 12.7 误读修正与阅读轨迹写法 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1083 | 3 | 12.8 轻卡、外部读者材料与防膨胀规则 | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1093 | 3 | 12.9 全书收束整合 QA | generic Stage 4 | 第四阶段全书收束规则与骨架。 |
| 1109 | 2 | 13. 大任务处理策略 | generic router | 复杂任务计划门，属于总入口权威约束。 |
| 1113 | 3 | 13.1 正常任务 | generic router | 复杂任务计划门，属于总入口权威约束。 |
| 1124 | 3 | 13.2 复杂任务 | generic router | 复杂任务计划门，属于总入口权威约束。 |
| 1154 | 3 | 13.3 止损与定点校补 | generic router | 复杂任务计划门，属于总入口权威约束。 |
| 1160 | 2 | 14. 辅助提示词快捷任务模板 | generic router | 快捷模板总则与回归样本沉淀机制归 Router 统领。 |
| 1168 | 3 | 只整理，不评价 | generic Stage 1 | 快捷模板直达第一阶段整理/筛选/初判。 |
| 1174 | 3 | 只判断轻卡、完整卡、主卡候选 | generic Stage 1 | 快捷模板直达第一阶段整理/筛选/初判。 |
| 1180 | 3 | 只优化轻卡 | generic Stage 2 | 快捷模板直达第二阶段优化/外部读者差异分析。 |
| 1186 | 3 | 只优化完整卡和主卡候选 | generic Stage 2 | 快捷模板直达第二阶段优化/外部读者差异分析。 |
| 1192 | 3 | 迁移前回源预检 | generic Stage 3 | 快捷模板直达第三阶段迁移与 QA。 |
| 1198 | 3 | 迁移后防回归 QA | generic Stage 3 | 快捷模板直达第三阶段迁移与 QA。 |
| 1204 | 3 | 读完整本书后执行全书收束整合 | generic Stage 4 | 快捷模板直达第四阶段全书收束或全书回看。 |
| 1210 | 3 | 当前章节热门划线与高赞想法扫描 | generic Stage 1 | 快捷模板直达第一阶段整理/筛选/初判。 |
| 1216 | 3 | 围绕我的判断查同位置其他书友高赞想法 | generic Stage 2 | 快捷模板直达第二阶段优化/外部读者差异分析。 |
| 1222 | 3 | 读完整本书后回看我的阅读风格 | generic Stage 4 | 快捷模板直达第四阶段全书收束或全书回看。 |
| 1230 | 2 | 15. 专用提示词回归样本沉淀规则 | generic router | 快捷模板总则与回归样本沉淀机制归 Router 统领。 |

Router

- Scope ranges covered: `5-12`, `16-27`, `29-40`, `44-66`, `69-93`, `98-119`, `122-153`, `1109-1157`, `1160-1236`.
- Headings/subheadings assigned here: `# 微信读书 Skill 通用整理提示词`, `## 0. 占位说明与路径规则`, `### 0.1 不可降级原则与任务入口门`, `## 1. 如何用通用提示词生成某本书专用提示词`, `### 专用提示词生成边界与验收门`, `## 2. 四阶段总流程`, `## 3. 多轮整理规则`, `## 4. 阶段切换前 QA 与条件式 Git 检查点`, `## 13. 大任务处理策略`, `### 13.1 正常任务`, `### 13.2 复杂任务`, `### 13.3 止损与定点校补`, `## 14. 辅助提示词快捷任务模板`, `## 15. 专用提示词回归样本沉淀规则`.
- Router-level authority preserved for downstream tasks: evidence-layer boundary, placeholder/path rules, non-degradation gate, stage routing overview, multi-round policy, stage-switch QA/Git gate, complex-task planning gate, shortcut-template warning, and regression-sample sedimentation mechanism.

Stage 1

- Scope ranges covered: `157-355`, `572-657`.
- Headings/subheadings assigned here: `## 5. 数据抓取硬约束`, `### 5.0 中间整理稿与正式阅读笔记的数据边界`, `### 5.1 跨段划线与想法匹配规则`, `### 5.2 同位置其他书友高赞想法默认伴随抓取规则`, `## 6. 颜色默认流向`, `## 7. 想法类别与卡片类型`, `### 7.1 想法类别`, `### 7.2 卡片类型`, `## 9. 第一阶段：生成中间整理稿`, `### 中间整理稿格式`, `# {作者}《{书名}》中间整理稿`, `## 整理说明`, `## 第N轮整理：范围说明`, `### 001. 章节名 / range`, `## 本轮索引`, `### 轻卡清单`, `### 完整卡候选`, `### 主卡候选`, `### 暂存素材`, `### 同位置其他书友高赞想法候选`, `### 颜色统计`, `### 下次接着整理位置`.
- Stage 1 carries data fetching, matching, official/public bookId mapping, external-reader location rules, color defaults, idea/card typing, and intermediate-draft format.

Stage 2

- Scope ranges covered: `358-569`, `661-843`.
- Headings/subheadings assigned here: `## 8. 文学分析质量规则`, `### 8.1` through `### 8.11`, `## 10. 第二阶段：优化中间整理稿`, `### 10.1`, `## 第N轮优化前诊断`, `### 10.2`, `### 10.3`, `### 10.4`, `### 10.5`.
- Stage 2 carries evidence anchors, psychology process, ambiguity/张力 handling, two-layer question chains, current answers, AI修正 deepening, cross-genre caveat, and external-reader difference analysis.

Stage 3

- Scope ranges covered: `846-974`.
- Headings/subheadings assigned here: `## 11. 第三阶段：迁移到正式阅读笔记`, `### 11.1`, `### 11.2`, `### 11.3`, `### 11.4`, `### 11.5`, `### 11.6`.
- Stage 3 carries migration trigger, source-original preservation order, precheck, formal-note structure, cursor update, destination rules, and anti-regression QA.

Stage 4

- Scope ranges covered: `977-1106`.
- Headings/subheadings assigned here: `## 12. 第四阶段：读完整本书后的全书收束整合`, `### 12.1` through `### 12.9`, plus the skeleton headings `## 全书收束整合`, `### 一、阅读现场档案`, `### 二、文章素材索引`, `### 三、阅读轨迹与判断变化`, `### 四、待回看 / 归档不迁移`.
- Stage 4 carries the whole-book consolidation model, Stage 3/4 boundary, internal ledger vs formal note boundary, one-card-two-destinations, duplicate/revision-chain rules, anti-bloat rules, and fixture-based QA.

Duplicated inheritance blocks

These are intentional duplications to be repeated in all four future generic stage prompts:

1. Applicable router path.
2. Stage purpose.
3. Required pre-read files: root `AGENTS.md` and the router.
4. Exact input files and output files.
5. Conflict rule: if a stage prompt conflicts with the router, the router wins.
6. Task boundary and Must NOT list.
7. QA evidence path for execution.

Shortcut template map

| shortcut template | disposition |
|---|---|
| `只整理，不评价` | generic Stage 1 |
| `只判断轻卡、完整卡、主卡候选` | generic Stage 1 |
| `只优化轻卡` | generic Stage 2 |
| `只优化完整卡和主卡候选` | generic Stage 2 |
| `迁移前回源预检` | generic Stage 3 |
| `迁移后防回归 QA` | generic Stage 3 |
| `读完整本书后执行全书收束整合` | generic Stage 4 |
| `当前章节热门划线与高赞想法扫描` | generic Stage 1 |
| `围绕我的判断查同位置其他书友高赞想法` | generic Stage 2 |
| `读完整本书后回看我的阅读风格` | generic Stage 4 |

Normative-language preservation ledger

- Completeness check method: this continuation re-read the snapshot by scope area (`5-12`, `16-27`, `29-40`, `44-66`, `69-93`, `98-119`, `122-153`, `157-355`, `358-569`, `572-657`, `661-843`, `846-974`, `977-1106`, `1109-1157`, `1160-1236`) and paired that read-through with the existing heading inventory. Grouped rows below cover every normative/control heading area; representative exact-source quotes anchor each group.

| snapshot area | representative exact-source sentences / control lines | completeness statement | disposition |
|---|---|---|---|
| `5-12` | `正式阅读笔记必须保留可读证据层...AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。` / ``source ID`...只服务中间整理...不默认进入正式阅读笔记正文。` | Re-read full core-goal block; all evidence-layer and technology-field control lines stay Router-level authority. | generic router |
| `16-27` | `若暂未确认，在专用提示词中写“待确认”。` / `不要把中间整理稿命名成单纯的 {书名}.md` | Re-read all placeholder/path bullets; path/placeholder constraints are Router-owned. | generic router |
| `29-40` | `必须保留真实状态，不得猜测、补写或伪造对应材料。` / `只有用户明确授权执行，才进入执行阶段。` / `只读咨询、规则解释和状态检查，不触发文件编辑、Git 操作或任何执行入口调用。` | Re-read the full entry-gate block; all authorization, sequencing, and no-execution controls stay Router-owned. | generic router |
| `44-66` | `专用提示词里不要再保留通用占位符。` / `书目专属事实未经核实，一律标为“待确认”，不能借用其他书的资料补全。` / `初次生成专用提示词不得虚构回归样本。` | Re-read specialized-prompt generation block; all cross-book contamination and unknown-fact rules stay Router-owned. | generic router |
| `69-93` | `第一阶段只做整理、轻量预分类和高赞想法初步筛选，不做深度评价，不写入正式阅读笔记。` / `正式阅读笔记中不保留中间稿编号...` / `不把文章素材索引写成文章草稿，也不把第三阶段全部重跑一遍。` | Re-read four-stage overview; stage boundaries are retained in Router route authority and elaborated later in each stage file. | generic router |
| `98-119` | `默认只优化第 N 轮新增内容，不重新优化整个中间稿。` / `默认优先迁移第 N 轮已优化完成...` / `只有当我明确说“回看全书中间稿”...才跨轮重写。` | Re-read multi-round rules; all round-scope controls remain Router-owned. | generic router |
| `122-153` | `AI 必须先完成第一阶段的 QA：` / `AI 必须先完成第二阶段的 QA：` / `只有当前用户指令明确要求 commit、push...才执行相应操作。` / `仍需遵守项目 AGENTS.md 的 Git 规则。` | Re-read stage-switch QA/Git gate; all entry/exit/Git authorization controls remain Router-owned. | generic router |
| `157-187` | `正式阅读笔记是面向阅读的长期文档...不默认写入正文，也不能以标题或编号形式伪装成证据层。` / `默认以“我的想法”为主索引整理...除非我明确要求整理纯划线。` / `不要只输出我的想法...必须尽量合并出对应的划线原文和划线颜色。` | Re-read Stage 1 data-boundary block; all source-merging and evidence-boundary rules move to Stage 1. | generic Stage 1 |
| `189-231` | `不要因为 ... range 不完全一致，就直接判断为“只有想法”或“无法匹配”。` / `必须标注“非精确 range 匹配”。` / `只允许在内部匹配；输出时只展示本轮新增内容。` | Re-read Stage 1 matching block; all match-order and anti-range-collapse rules move to Stage 1. | generic Stage 1 |
| `233-299` | `不得因为个人笔记 bookId 下 /book/bestbookmarks 为空...就判定同位置没有高赞想法。` / `只能作为辅助信号，不能单独证明文本同位置。` / `高赞想法只能作为外部读者材料，不得替代我的感受、问题和判断。` | Re-read external-reader lookup and filtering block; all public-book mapping and external-reader boundary rules move to Stage 1. | generic Stage 1 |
| `303-355` | `颜色只作为默认流向，不是最终卡片类型。` / `不要把颜色写成单纯数字。` / `整理时必须保持阅读顺序，不要为了按颜色分类而打散阅读线索。` | Re-read color/category/card-type block; all output-format and light preclassification controls move to Stage 1. | generic Stage 1 |
| `358-569` | `完整卡、主卡候选...必须至少绑定一个可回到原文的证据锚点。` / `不得把小说人物心理分析硬套到非虚构作品...` / `AI 必须继续补“当前回答（沿原问题）”...` / `如果 AI修正只是复述...必须重写。` | Re-read Stage 2 quality block; evidence anchoring, cross-genre caveat, psychology-process, and AI deepening rules all move to Stage 2. | generic Stage 2 |
| `572-657` | `第一阶段只做整理、轻量预分类...不写入正式阅读笔记。` / `即使内部需要拉取全书数据，也只输出本轮新增内容。` / `如果文件不存在就新建；如果已存在，就追加为新一轮整理。不要修改其他文件。` | Re-read Stage 1 execution template and output format; all first-stage execution boundaries move to Stage 1. | generic Stage 1 |
| `661-843` | `不要覆盖我的原想法...` / `如符合第 13.2 节任一复杂任务条件，必须先制定优化计划，再分批执行。` / `处理时必须遵守 /home/king/github/growing-myself/AGENTS.md...` / `外部读者原话必须逐字保留...不得改写成用户第一人称判断。` | Re-read Stage 2 execution block; optimization sequencing, AGENTS inheritance, and external-reader analysis constraints move to Stage 2. | generic Stage 2 |
| `846-974` | `每条迁移材料必须先保留书籍划线原文，再保留“我自己写的内容”。不要用 AI修正覆盖原文。` / `正式迁移前，必须建立仅供内部核对的清单...` / `迁移完成后，逐项完成以下 QA，未通过不得把迁移视为完成。` | Re-read Stage 3 migration and QA block; source-original preservation, precheck, and anti-regression controls move to Stage 3. | generic Stage 3 |
| `977-1106` | `第四阶段不是把第三阶段全局重跑一遍。除非...否则不要整体重迁已有正式稿。` / `原始“我自己写的内容”必须保留，AI修正只能另写，不能覆盖原文。` / `处理顺序也按这个台账走：先判 source status...不要跳过前两步。` / `QA 未通过时，不得把全书收束整合视为完成。` | Re-read Stage 4 model, ledger, revision-chain, anti-bloat, and QA blocks; all whole-book consolidation controls move to Stage 4. | generic Stage 4 |
| `1109-1157` | `复杂任务只改变执行组织方式...也不降低单卡深度。` / `必须先制定计划，再分步执行：` / `起草后必须交给 Momus、Metis、Oracle 审查...` / `不要把裸写 start-work 当成面向用户的通用执行命令...` | Re-read complex-task block; all planning, review, authorization, and start-work routing controls stay Router-owned. | generic router |
| `1160-1236` | `使用这些模板时，仍必须同时服从：AGENTS.md、第 0.1 节任务入口门、第 11 节迁移与 QA 要求、第 12 节全书收束整合规则、第 13 节复杂任务计划门...` / `这些模板不能绕过 QA、Git 授权、执行授权...` / `当《{书名}》已经读完...若属于复杂任务，必须先完成计划...` / `回归样本应写明...不应被复制到通用提示词或其他书目的专用提示词。` | Re-read late shortcut + regression section; global shortcut warning stays Router-owned, while individual shortcut bodies are mapped in the shortcut table above. | generic router + stage-specific shortcut mapping |

Exact-source-rule preservation samples

1. `[11]` `正式阅读笔记必须保留可读证据层：书籍划线原文、我自己写的原想法，以及确有保留价值的外部读者原话。AI评价、AI修正、AI补充只能建立在这些原文之上，不能替代它们。` -> generic router.
2. `[383]` `文学作品与非虚构作品都适用这一原则...不得把小说人物心理分析硬套到非虚构作品，也不得把非虚构的概念概括替代文学作品的细读。` -> generic Stage 2.
3. `[861]` `每条迁移材料必须先保留书籍划线原文，再保留“我自己写的内容”。不要用 AI修正覆盖原文。` -> generic Stage 3.
4. `[1234]` `回归样本应写明：触发场景、错误类型、必须保留或核对的证据、禁止重犯的处理方式和可验证的通过条件。它服务于该书的后续整理与 QA，不应被复制到通用提示词或其他书目的专用提示词。` -> generic router.

Read-based QA notes:

- This continuation re-read the snapshot itself, not the live mutable router, for Stage 2 / Stage 3 / Stage 4 / complex-task / shortcut decisions.
- Heading inventory uses snapshot headings/subheadings only; the live router file was used only for existence verification and snapshot-verbatim comparison.
- Stage-boundary decision: the four-stage overview (`69-93`) remains Router authority, while detailed stage execution bodies move to Stage 1 / 2 / 3 / 4 respectively.
- Intentional-duplication decision: the example headings `第1轮整理 / 第2轮整理 / 第3轮整理` are kept as `intentional duplication` because they are Router-level examples and will also reappear in Stage 1 draft format.
- Cross-genre caveat check: snapshot line `383` is explicitly anchored to Stage 2, not flattened into Router.
- Regression-sample sedimentation check: snapshot lines `1230-1236` stay Router-owned, because they govern future per-book prompt QA rather than a single execution stage.
- Stale numeric reference handling decision: any surviving literal old-section reference in this evidence must appear only inside exact source quotes, never as new target wording.

Boundary checks:

- No rewrite of `/home/king/github/growing-myself/微信读书通用提示词.md` in this continuation.
- No generic stage prompt files created in this continuation.
- No `路遥/人生/**` files touched in this continuation.
- No `.omo/run-continuation/*.json` edits by this continuation.
- No manifest regeneration in this continuation; existing baseline manifests were reused and verified only.
- No edits to `/home/king/github/growing-myself/.omo/drafts/split-weread-prompts-by-stage.md`, `/home/king/github/growing-myself/.omo/plans/split-weread-prompts-by-stage.md`, `/home/king/github/growing-myself/.omo/boulder.json`, `decisions.md`, or `problems.md`.
- Not applicable in this task: malformed input, untrusted external text, cancel/resume logic, flaky tests, mid-operation interrupts.

Stale-reference classifications:

- Literal check A: 1 hit at evidence line `378`; classification `source-quote-only` because the hit lives inside a grouped exact-source quote from the snapshot Stage 2 execution block.
- Literal check B: 1 hit at evidence line `382`; classification `source-quote-only` because the hit lives inside a grouped exact-source quote from the snapshot shortcut-warning block.
- Literal check C: 0 hits; classification `no-hit / no target wording present`.

Follow-ups / unresolved risks:

- Non-blocking risk: this repo started dirty. The protected baseline manifest already covers `.omo/boulder.json`, `decisions.md`, and `problems.md`; this continuation intentionally avoids those paths.
- Non-blocking risk: `learnings.md` and `issues.md` were pre-existing empty untracked files. Only `learnings.md` will be appended, because the task explicitly allows non-protected notepad appends there.
- Non-blocking risk: grouped normative coverage is used for large sections. Completeness is justified by scope-by-scope snapshot rereads and the exhaustive heading inventory above.
- Blocking risk threshold: if any required evidence heading is still missing after verification, or if stale-reference hits are not source-quote-only, `PASS:` must not be claimed.

PASS:

- PASS: existing snapshot reused and re-verified with matching sha256, matching line counts, and `SNAPSHOT_VERBATIM_BEFORE_REWRITE: PASS`.
- PASS: heading inventory covers every snapshot heading/subheading with exactly one disposition.
- PASS: move-ledger sections cover every required Scope source range.
- PASS: shortcut templates are mapped individually.
- PASS: hard/normative and other control sentences are represented by grouped snapshot-area coverage plus exact preservation samples.
- PASS: stale-reference literal hits in this evidence are source-quote-only, not target wording.
- PASS: no blocking risk remains for independent Task 1 verification.
