# consolidate-ren-sheng-whole-book-notes - Work Plan

## TL;DR (For humans)

**What you'll get:** 一份可由后续 worker 零访谈执行的《人生》第四阶段全书收束计划。执行结果保留现有四轮阅读卡作为档案底座，在正式阅读笔记末尾追加一个固定顺序的 `## 全书收束整合`，建立六类文章素材索引、真正有价值的阅读改判链和待回看清单；同时把当前读者可见的技术字段受控地清理掉。

**Why this approach:** 第4轮 001-132 已完成返工，正式稿也已有四轮完整档案，当前不能再次重跑第三阶段或重写全部卡片。安全做法是先在 `.omo/evidence/` 建立全书台账和保存清单，用唯一可读锚点替换 source 坐标，再只补缺口、建修订链和追加全书导航。

**What it will NOT do:** 不修改中间整理稿、提示词、fixture 或其他书目；不读取 sibling-book `AGENTS.md`；不抓取微信读书；不移动、删除、合并或整体洗稿现有合格卡；不把文章索引写成文章；不让 AI修正覆盖用户原文；不 commit、不 push。

**Effort:** XL

**Risk:** High - 当前正式稿有 108 条唯一 reader-facing 技术字段/坐标行；中间稿四轮共有 266 个 canonical source units，正式稿四轮共有 165 张 formal cards，二者必须形成闭合集合。主要风险是清理技术字段时误改正文、移除 source ID 后锚点冲突、漏掉前三轮未迁材料、重复复制已经完成的卡，以及以“整合”为名压缩阅读现场。

**Decisions:** 保留四轮原顺序；只允许技术 token 清理和 ledger 证明的局部修补；追加而不重构；内部 source mapping 永不进入正式稿；可读锚点采用 `第N轮 / 当前分类标题 / 卡片标题`；六类索引固定；六条真实阅读轨迹固定核对；九个 fixture 和七个哨兵全部 agent-executed QA。

Your next move after this plan is reviewed: start it only from a separate worker session such as `/start-work consolidate-ren-sheng-whole-book-notes`. Approval of this plan never authorizes Prometheus to execute it.

## Scope

### Must have

- Future execution may modify only `/home/king/github/growing-myself/路遥/人生/《人生》阅读笔记.md` as a reading-material file.
- Future execution may create only the following QA/working artifacts under `.omo/evidence/`:
  - `.omo/evidence/ren-sheng-whole-book-preflight.md`
  - `.omo/evidence/ren-sheng-whole-book-validator.py`
  - `.omo/evidence/ren-sheng-whole-book-validator-tests.py`
  - `.omo/evidence/ren-sheng-whole-book-formal-baseline.md`
  - `.omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`
  - `.omo/evidence/ren-sheng-whole-book-review-runtime-paths.jsonl`
  - `.omo/evidence/ren-sheng-whole-book-preservation-manifest.md`
  - `.omo/evidence/ren-sheng-whole-book-source-manifest.md`
  - `.omo/evidence/ren-sheng-whole-book-technical-field-inventory.md`
  - `.omo/evidence/ren-sheng-whole-book-consolidation-ledger.md`
  - `.omo/evidence/ren-sheng-whole-book-reconciliation.md`
  - `.omo/evidence/ren-sheng-whole-book-fixture-results.md`
  - `.omo/evidence/ren-sheng-whole-book-anchor-map.md`
  - `.omo/evidence/ren-sheng-whole-book-candidate-section.md`
  - `.omo/evidence/ren-sheng-whole-book-candidate-qa.md`
  - `.omo/evidence/ren-sheng-whole-book-metadata-cleanup.md`
  - `.omo/evidence/ren-sheng-whole-book-archive-audit.md`
  - `.omo/evidence/ren-sheng-whole-book-index-audit.md`
  - `.omo/evidence/ren-sheng-whole-book-trajectory-audit.md`
  - `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md`
  - `.omo/evidence/ren-sheng-whole-book-f1-plan-compliance.md`
  - `.omo/evidence/ren-sheng-whole-book-f2-preservation.md`
  - `.omo/evidence/ren-sheng-whole-book-f3-reading-surface.md`
  - `.omo/evidence/ren-sheng-whole-book-f4-fixture-anchor.md`
  - `.omo/evidence/ren-sheng-whole-book-f5-scope-git.md`
  - `.omo/evidence/ren-sheng-whole-book-final-wave-inputs.md`
- Before any reading-note edit, verify the Stage 4 trigger gate, root rules, router precedence, same-book `AGENTS.md` existence, user execution authorization, source freshness and dirty-worktree baseline.
- Preserve Round 1–4 in their current order and preserve every existing card in its current archive location, except:
  - remove reader-facing technical source tokens;
  - apply a ledger-proven local repair for missing readable evidence, semantic error or correction chain;
  - add an actually absent eligible card only when the ledger proves no formal canonical card exists.
- Create one source-ledger row for every one of the **266 canonical source units** in the intermediate draft: R1=54 (`001-053` plus `U01`), R2=52 (`001-046` plus `036A/039A/040A/041A/043A/046A`), R3=28 (`001-028`), R4=132 (`001-132`). Treat every R2 `A` key as an independent row with `variant_of=<base key>`; never merge it mechanically.
- Create one preservation row for every one of the **165 existing formal cards**: R1=20, R2=31, R3=15, R4=99. A formal card may have no source key only with explicit `formal-synthesis` or `legacy-formal` rationale.
- Close and report eight reconciliation sets: `source-only / formal-only / one-to-one / many-to-one / duplicate / revision-chain / planned-new-formal / unresolved`. The first four are mutually exclusive primary topology buckets for each source/formal relationship. `duplicate`, `revision-chain` and `planned-new-formal` are secondary tags allowed to overlap the primary buckets: `duplicate` normally overlaps `many-to-one`, `revision-chain` may overlap `one-to-one` or `many-to-one`, and `planned-new-formal` is a subset of current `source-only`. `unresolved` is an error set that must be empty. Every source-only/formal-only item needs a disposition.
- Every source-ledger row must contain: source key; exact source span and hashes; quote/user/external block counts and representative excerpts; current readable formal anchor or `target-absent`; all eight Phase 4 semantic axes (`source status`, `archive disposition`, `evidence role`, `article links`, `trajectory flags`, `external-reader relation`, `source relation`, `interpretation relation`); separate workflow/topology state; target-evidence checks; trajectory-chain links; missing fields; rationale; and one exact action from the complete schema below.
- Build a pre-edit preservation manifest with the full heading path, exact raw-byte span, quote/user/external-reader block counts, raw SHA-256 and normalized SHA-256 for every existing formal card. Normalization is fixed below and may not erase prose or punctuation.
- Treat the reviewed technical baseline as **108 unique reader-facing lines**: 99 unspaced `源ID/源IDs` heading lines (including one overlapping `external-源ID` heading), three spaced `源 ID` group headings, four `chapterUid/range` metadata lines, and two additional coordinate-only round headings. Six lines contain coordinate-shaped ranges, four overlapping the metadata lines and two coordinate-only. Recompute the exact families before execution; if the current hash or any family/cardinality differs, stop as stale input and request replanning.
- Reader-facing technical tokens must end at zero with no exceptions: `源ID`、`源IDs`、`source ID`、`source status`、`archive disposition`、`QA state`、`chapterUid`、`bookId`、`range=`、`抓取状态`、`官方版定位`、`点赞数` and coordinate-shaped ranges such as `5684-5721`.
- Approved technical-token transformations are limited to:
  - remove `【源ID：...】`, `【源IDs：...】` or `【external-源ID：...】` from all 99 affected card headings while retaining the complete human title and all other punctuation;
  - line 4770 becomes `## 三、人物主线卡（只承载人物弧线补证）`; line 5420 becomes `## 四、轻卡存档 / 阅读心流`; line 5749 becomes `## 五、主题素材库 / 待回看`;
  - line 5 becomes `- 阅读范围：开头至第五章。`; line 557 becomes `## 第2轮阅读笔记：第五章之后至第八章`; line 559 becomes `- 阅读范围：第五章之后，至第八章。`; line 1238 becomes `## 第3轮阅读笔记：第八章之后至第十二章`; line 1240 becomes `- 阅读范围：第八章之后，至第十二章。`; line 5929 becomes `- 第二十三章“我的亲人哪……”之后。`;
  - keep all source mappings in the internal ledger only.
- Use the unique readable-anchor grammar `第N轮 / 当前分类标题 / 卡片标题`. Add `章节或场景 / 引文短句（不超过20个汉字）` only when the three-part path is not unique.
- Append one new top-level `## 全书收束整合` after the existing Round 4 ending. Its direct children must occur exactly once and in this order:
  1. `### 一、阅读现场档案`
  2. `### 二、文章素材索引`
  3. `### 三、阅读轨迹与判断变化`
  4. `### 四、待回看 / 归档不迁移`
- `阅读现场档案` must treat the existing four rounds as the archive base. It may contain archive navigation and ledger-proven repair pointers, but it must not copy a qualified card body.
- `文章素材索引` must contain exactly six top-level directions: `人物线`、`城乡主题`、`尊严主题`、`爱情线`、`知识分子困境`、`写法线索`.
- Each article direction must include: a core question, at least three unique readable anchors from at least two rounds when qualifying evidence exists, one preserved user phrase, one textual tension, usable textual evidence, and an honest missing-evidence field. Do not invent evidence if a direction is thinner; state the gap.
- `人物线` may contain named sublines for `高加林 / 巧珍 / 黄亚萍 / 克南 / 德顺老汉`, with `刘玉海 / 高明楼` used only as ledger-supported group portraits; no other top-level article direction may split into new top-level rows.
- `阅读轨迹与判断变化` must contain only evidence-backed changes, using `当时的读法 / 后来出现的证据 / 全书后的修正 / 误读的价值 / 文章索引用法`.
- At minimum, reconcile these six real trajectory chains without erasing the original sharp wording:
  1. 特权态度：从只写“痛恨特权”推进到“也痛恨自己没有特权”的挑战。
  2. 劳动与身份：从“高加林不愿掏炭”推进到他能承受新闻现场之苦、真正差别在身份意义。
  3. 职业热爱：从“热爱让苦甘之如饴”收稳为记者身份重新编码痛感，并保留田晓霞联想但不混同两人。
  4. 县城空间：从“县城变小等于忘本”修正为身份落差投向空间的心理投影，不把后来的失败倒灌进当时场景。
  5. 爱情与位置：保留“农民时爱巧珍、干部时爱黄亚萍”的原始锋利表达，同时补足“位置影响哪一种爱被承认”的证据桥。
  6. 黄亚萍物质付出：从“这不是牺牲”修正为“有真实成本，但不等同于巧珍在匮乏中的托举”。
- `待回看 / 归档不迁移` may contain only concise reader-facing reasons; full source/duplicate/QA decisions stay in the internal ledger.
- Execute all nine fixture cases and all seven fixed regression sentinels before completion.

#### Planning-time technical-line inventory

- Inventory regex families are fixed as: `external-源ID(?:s)?`, `源ID(?:s)?`, `源\s+ID(?:s)?`, `chapterUid`, `\brange\b`, and `(?<!\d)\d+\s*-\s*\d+(?!\d)`. Scan line-by-line and deduplicate by file line number.
- The 99 unspaced source-ID heading lines are: `1704, 1742, 1784, 1825, 1866, 1909, 1948, 1987, 2024, 2061, 2098, 2139, 2182, 2220, 2257, 2296, 2333, 2367, 2406, 2446, 2478, 2512, 2550, 2588, 2626, 2661, 2703, 2741, 2779, 2817, 2853, 2889, 2925, 2963, 3000, 3038, 3076, 3114, 3154, 3192, 3230, 3268, 3307, 3345, 3385, 3425, 3465, 3506, 3547, 3581, 3615, 3653, 3690, 3724, 3759, 3799, 3834, 3862, 3896, 3933, 3970, 4008, 4043, 4082, 4121, 4160, 4200, 4242, 4281, 4317, 4357, 4398, 4430, 4462, 4503, 4543, 4583, 4621, 4658, 4695, 4720, 4745, 4773, 4795, 4839, 5103, 5177, 5275, 5423, 5523, 5659, 5709, 5752, 5810, 5833, 5856, 5879, 5902, 5917`. Line 5917 is the one `external-源ID` overlap.
- The three spaced source-ID group-heading lines are `4770, 5420, 5749`; their exact replacements are fixed above.
- The four `chapterUid/range` lines are `5, 559, 1240, 5929`. The two additional coordinate-only round headings are `557, 1238`. Coordinate matches therefore total six lines, with four overlaps; the unique union across all families is 108.
- `.omo/evidence/ren-sheng-whole-book-technical-field-inventory.md` must contain one row per unique line with planning-time line number, exact before text, all matched families, exact after text, and post-application byte span. The 99 source-ID heading replacements are deterministic deletion of only the final bracketed technical suffix; the other nine exact replacements are fixed in Scope. No worker-authored alternative wording is allowed.

#### Deterministic source and formal-card parsers

- Intermediate-draft source-unit regex: `^###\s+(?P<unit>\d{3}[A-Z]?|U\d{2})\.\s+(?P<title>.+)$`. Stable key is `R<round>:<unit>`.
- R1 source region is line 13 `## 本轮新增整理` through immediately before line 1895 `## 本轮索引`: `001-053` plus `U01`, 54 units. R2 is line 2263 `## 第2轮整理` through before line 4441 `## 第2轮索引`: `001-046` plus the six `A` variants, 52 units. R3 is line 4520 through before line 5973: `001-028`, 28 units. R4 is line 6029 through before line 14733: `001-132`, 132 units.
- A source unit begins at its matched H3 heading byte and ends immediately before the next matched canonical-unit heading or enclosing region terminator. Preserve exact raw bytes. `U01` is a canonical unmatched-thought unit. Each R2 `A` unit is separate and carries `variant_of=R2:<base>`.
- Formal round boundaries are lines `3, 557, 1238, 1701`. R1-R3 cards match `^###\s+\d+\.\s+.+$` and end immediately before the next H3/H2/round heading. Expected cardinalities: R1=20 (`核心4/人物3/完整4/轻卡5/素材待回看4`), R2=31 (`4/3/4/17/3`), R3=15 (`4/1/3/4/3`).
- R4 formal cards are: 15 core H3 cards; 67 complete H4 cards; 6 character-group H3 cards; 4 light-group H3 cards; 6 theme-group H3 cards; 1 global-external H3 card; total 99. The ten H3 headings `A-J` at lines `2295, 2625, 2888, 3153, 3546, 3758, 4042, 4356, 4502, 4620` are structural containers, not cards. An H4 card ends before the next H4/H3/H2; an R4 card H3 ends before the next H3/H2.
- Title, round metadata, H2 category headings, R4 `A-J` containers, prose introductions, dividers and final cursor are non-card prefix content. They are protected by the whole-prefix byte gate even though they have no manifest card row.

#### Complete ledger schema and state matrix

- `source_status` preserves the seven Phase 4 meanings exactly: `已在正式笔记中，结构合格，只补文章索引 | 已在正式笔记中，但需补 readable evidence / 用户原句 / 外部原话 | 中间稿已优化，尚未迁移 | 中间稿与正式稿重复，需合并或建立修订链 | 正式稿旧判断已被后文修正，保留为阅读轨迹 | 仅外部读者材料，无用户卡片锚点 | 来源不足，待回看`.
- `archive_disposition` preserves the six Phase 4 archive identities exactly: `保留为轻卡 | 保留为完整卡 | 提升为核心卡 | 合并入其他卡 | 归档不迁移 | 待回看`. It records card identity/destination, never workflow action.
- `evidence_role` is a set drawn from `主题证据 | 人物线证据 | 写法证据 | 阅读轨迹证据`; an empty set is serialized `none`.
- `article_links`: an empty list or a subset of the six fixed article directions; serialize an empty list as `none`, never blank.
- `trajectory_flags` is an empty set or a subset of the Phase 4 flags `早期误读 | 后文修正 | 判断变化`; empty is `none`. `trajectory_chain_links` separately points to zero or more of the six plan-fixed correction chains.
- `external_reader_relation`: `回声 | 补充 | 挑战 | 反向解释 | 独立精彩 | 丢弃并说明理由 | 无外部材料 | 不适用`; `丢弃并说明理由` requires a rationale.
- `source_relation`: `exact same quote | overlapping quote | same scene | different quote | not-applicable`.
- `interpretation_relation`: `same insight | corrected judgment | different angle | external echo | external challenge | no-comparable-judgment | not-applicable`.
- `workflow_state` is separate from all semantic axes: `mapped-complete | mapped-partial | planned-new-formal | intentionally-unmapped | unresolved`.
- `topology_relation` is separate from `source_relation`: `one-to-one | many-to-one | duplicate-of:<source-key> | variant-of:<source-key> | revision-before:<source-key> | revision-after:<source-key> | no-formal-target | unresolved`.
- `target_evidence_relation` is recorded separately for quote, user and external blocks in both current and modeled-post states: `present-verbatim | present-labelled-context | intentionally-not-migrated | missing-repair-approved | planned-by-approved-insertion | missing-unbound | not-applicable`.
- `action`: `preserve-existing | local-evidence-repair | index-only | merge-to-anchor | new-card | internal-only | 待回看 | 归档不迁移 | stop-unresolved`.
- The validator first checks all eight semantic axes against Phase 4, then checks `workflow_state + topology_relation + action`; operational state never substitutes for a semantic axis.
- For `workflow_state=mapped-complete`, current target anchor is required, no required current/modeled-post block may be `missing-repair-approved`, `planned-by-approved-insertion` or `missing-unbound`, missing-fields is `none`, and action is `preserve-existing/index-only/merge-to-anchor`.
- For `workflow_state=mapped-partial`, current target anchor and nonempty missing-fields are required; every absent required current block is `missing-repair-approved` and binds to one exact repair hunk; action is `local-evidence-repair` or `merge-to-anchor`. After Todo 7 modeling, every required relation is satisfied and missing-fields becomes `none`.
- For `workflow_state=planned-new-formal`, current target is `target-absent`, `topology_relation=no-formal-target`, quote + user original + nonempty Phase 4 `evidence_role` are required, each required current target relation is `planned-by-approved-insertion`, and the row carries future readable anchor, post-transform category, insertion point and exact hunk; only action `new-card` is legal. `archive_disposition` must be `保留为轻卡/保留为完整卡/提升为核心卡`: a light card preserves at least `划线原文 + 我自己写的内容/我的原想法` without forced expansion; a complete/core card preserves those blocks plus `AI评价 / AI修正 / AI补充`, with AI修正 never replacing user text. The other three archive dispositions cannot create a card.
- For `workflow_state=intentionally-unmapped`, target is `target-absent`, rationale is mandatory, action is `internal-only/待回看/归档不迁移`, archive disposition is correspondingly `合并入其他卡/待回看/归档不迁移`, and the row cannot be main article evidence. `workflow_state=unresolved`, blanks, `topology_relation=unresolved`, `missing-unbound`, unbound approved-missing, or unsatisfied modeled-post evidence hard-stop the run.
- A formal-only preservation row has `source_keys=none`, one rationale from `formal-synthesis | legacy-formal`, and action `preserve-existing`. For many-to-one, every source row names the same representative target anchor; duplicate rows use `merge-to-anchor` and remain separately traceable. For a revision chain, both early and late source rows survive with paired before/after relations; the reader-facing trajectory preserves the early wording and later evidence rather than overwriting either.

#### Source-side and target-side preservation checks

- `.omo/evidence/ren-sheng-whole-book-source-manifest.md` has one row per 266 source units with key, raw byte offsets, raw SHA-256, normalized SHA-256, exact heading, counts of `划线原文`, `我自己写的内容/我的原想法`, external-reader original blocks, and representative short excerpts from each present block type.
- Every ledger row links to the source-manifest row and records current plus modeled-post target quote/user/external relations or the explicit `intentionally-not-migrated` rationale. `preserve-existing` and `index-only` are not accepted merely because a heading exists; the target-evidence checks must prove the needed source material is represented. `missing-repair-approved` and `planned-by-approved-insertion` are legal only before Todo 7 applies their exact bound hunks; they may not survive in modeled-post acceptance.
- Hash normalization is fixed: strict UTF-8 decode; convert CRLF/CR to LF; Unicode NFC normalization; remove at most one terminal LF from the extracted block; encode UTF-8; SHA-256. Also record raw-byte SHA-256. For pre/post card comparison, apply only the exact approved technical-line replacement to the pre-edit heading before normalized hashing. A ledger-approved repair is compared through its exact before/after hunk instead of hash equality.
- Whole-prefix authority: apply the ordered 108-row replacement manifest plus any separately approved repair or new-card insertion hunks to the reviewed original bytes in memory. The final bytes before the appended `## 全书收束整合` must equal that transformed baseline exactly. Every other pre-existing byte—including whitespace, prose, quotations, external-reader text, headings and order—must match; the new section is suffix-only.

### Must NOT have

- Must not start content mutation unless a separate worker session has explicit execution authorization; plan approval alone is not execution authorization.
- Must not edit `路遥/人生/《人生》中间整理稿.md`、`路遥/人生/《人生》微信读书提示词.md`、`路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md`、`.omo/evidence/fixtures/add-whole-book-consolidation-model.md` or any other reading material.
- Must not edit `.omo/plans/consolidate-ren-sheng-whole-book-notes.md`, `.omo/drafts/consolidate-ren-sheng-whole-book-notes.md` or `.omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json` during execution; the seal binds their final reviewed bytes.
- Must not read or import `/home/king/github/growing-myself/路遥/平凡的世界/AGENTS.md` or any sibling-book `AGENTS.md`.
- Must not call WeRead APIs or fetch new notes/comments.
- Must not move, merge, delete, reorder or globally rewrite an existing formal card. When the intermediate draft duplicates an existing formal card, the existing formal card is canonical; the duplicate remains internal-only.
- Must not turn the four rounds into a compressed summary, duplicate qualified cards under the new section, impose a card-count/word-count cap, or globally rerun Stage 3.
- Must not let `AI修正` overwrite `我自己写的内容/我的原想法`, rewrite external-reader text as the user's first-person view, promote every light card, or use external-only material as main evidence.
- Must not use technical identifiers as reader-facing anchors, copy whole card bodies into the article index, or draft finished essays.
- Must not overwrite, revert, delete, stage or commit the pre-existing `.omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json` change or any other tracked/untracked path present at execution preflight but outside the exact allowlist. Session-generated `.omo/run-continuation/*.json` files are unowned baseline state, not execution outputs.
- Fresh F1–F5 reviewer sessions may create runtime-only `.omo/run-continuation/<session_id>.json` after preflight. These paths are **not** ordinary `allowed_changed_paths` and never receive a glob exemption. For each reviewer attempt, either zero new reviewer runtime node or exactly one regular non-symlink node whose basename equals the actual returned session ID is allowed after authentication; more than one, wrong basename/type, missing session metadata when a new node appears, modified baseline/registered path outside the explicit execution-runtime exception, or later reviewer-path hash drift invalidates the wave. Zero-node NO_RESULT may have empty session metadata under the dedicated rule below. Runtime paths are never staged, edited or deleted.
- The one exact `execution_runtime.path` bound in Todo 0 is the only mutable preflight runtime exception. Todo 0 records `initial_state=absent|present`, `initial_kind=absent|regular` and nullable initial hash. Only `absent→regular` or `regular→regular` is legal; the current node must be a regular non-symlink at the same session-bound path, while hash may evolve. `absent→other`, `regular→absent`, rename, symlink/non-file or extra node is forbidden. The worker never edits/deletes/stages it; all other baseline continuation paths remain byte-stable and child reviewer paths follow registration/freeze.
- Must not stage, commit or push any file.

## Verification strategy

> Zero human intervention. Test decision: **none + document QA**. This is Markdown consolidation, so verification uses source manifests, deterministic fixture execution, exact read-back, semantic sentinel checks, forbidden-token scans and Git scope audits rather than program tests.

### Reviewed immutable baselines

Before Todo 1, compare exact bytes to all six reviewed baselines below. Any mismatch is `STOPPED: stale reviewed input`; line-count equality does not override a hash mismatch, and the worker may not refresh these values without a revised plan and renewed Metis/Momus/Oracle approval.

The final plan and draft are not self-hashed in this file. Their exact post-review lines/SHA-256 and the three unconditional approvals are pinned in `.omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json` under the seal protocol below; Todo 0 validates that control-plane artifact in addition to these six content baselines.

| file | lines | SHA-256 |
|---|---:|---|
| `AGENTS.md` | 117 | `6def8b9c885fef8394eeaee9f74c9e38f885d5d522c53838aedf13daa4376cf2` |
| `路遥/人生/《人生》微信读书提示词.md` | 230 | `914b2f4cad3c73e33da6ddb010b4762cd7c142e4b54037ba7a6a2d1653b91856` |
| `路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md` | 284 | `a31aef8b30291c29b804217e1f2ea243203679f9e1253dbb270ea752fcdab649` |
| `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` | 215 | `67f1f16a539a156db838fc58d4eeb6322a0d516d73b08a8bf6dcc8ebbb6877c3` |
| `路遥/人生/《人生》中间整理稿.md` | 15009 | `dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0` |
| `路遥/人生/《人生》阅读笔记.md` | 5930 | `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11` |

### Executable validator contract

Todo 1 must create `.omo/evidence/ren-sheng-whole-book-validator.py` and `.omo/evidence/ren-sheng-whole-book-validator-tests.py` before generating manifests. Both are execution-only QA artifacts, use Python 3 standard library only, never access the network and never mutate reading/source/governing files. Persistent outputs may write only an explicitly supplied `--out` path listed in Scope. The sole transient exception is `review-runtime-snapshot`: it may create exactly one new regular non-symlink file matching `/tmp/ren-sheng-<wave_id>-F[1-5]-<attempt_uuid>-runtime-before.json`, using exclusive create (`O_CREAT|O_EXCL`), rejecting any existing node, repository path, symlink, directory, different `/tmp` basename or additional output. It is deleted only after successful runtime registration; on any failure it remains for diagnosis. No other validator subcommand may write outside Scope.

- Every validator command exits `0` only when all assertions pass, `1` for a content/validation failure, and `2` for invalid invocation or unreadable input. It emits one JSON summary to stdout with `command`, `status`, `counts`, `failures`, `input_hashes` and `output_path`; stderr contains diagnostics only. Any nonzero exit blocks the next Todo.
- Every subcommand also accepts `--check-only`: it performs the same reads/assertions, writes no file, sets `output_path=null`, and emits the same JSON summary. F1–F5 reviewers must use this mode whenever they invoke the validator.
- Todos 1–10 pass `--receipt .omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`. After fully closing and hashing its named output(s), the validator atomically appends exactly one JSON line containing the stdout summary plus output hashes. It never appends into a manifest/candidate/audit input. `--check-only` forbids `--receipt` and writes nothing.
- Invocation JSONL schema is fixed: `schema_version=1`, `todo`, `subcommand`, `attempt_id` (UUID), `attempted_at` (UTC ISO-8601), sorted `stable_input_hashes`, sorted `phase_input_hashes` entries of `{path, phase, sha256}`, sorted `output_hashes`, `status=PASS|FAIL`, `failures`, `supersedes_attempt_id`, `receipt_prefix_sha256` (JSONL bytes before this append), `previous_record_hash`, and `record_hash`. Append order/hash chain is authoritative; records are never edited or deleted. The invocation JSONL itself is never included in `stable_input_hashes`; its state is represented only by the prefix/hash-chain fields, preventing self-reference.
- Formal-note phases are fixed: `reviewed-baseline` is the immutable reviewed SHA-256; Todos 1, 5 and 7 must record that phase/hash for their pre-mutation formal input; Todo 8 records `cleaned-prefix` and its exact SHA-256 after approved prefix hunks; Todo 9 records `final-suffix-appended`; Todo 10 records the same final hash. `prefix-check` and `section-check` prove the chain `reviewed-baseline -> cleaned-prefix -> final-suffix-appended`, including exact prefix equality and suffix boundary.
- A tests-first red attempt and retries remain historical. For each required Todo 1–9 subcommand, `final-check` selects the latest record whose stable inputs and stable outputs match current immutable artifacts **and** whose formal phase hash matches the pinned phase/transform chain above. Evolving formal-path hashes are never compared directly to the final current path outside their named phase. The selected record must be PASS; older FAIL/different-phase attempts are preserved but superseded. Missing matching PASS is blocking.
- During Todo 10 generation, `final-check` validates Todo 1–9 records and the complete invocation hash chain up to the current prefix, closes final QA, then appends its Todo 10 record with that `receipt_prefix_sha256`; it does not hash the future full JSONL as an input. Later F2 `final-check --check-only` requires the current JSONL to equal the verified prefix plus a valid latest Todo 10 record whose output hash matches current final QA, and requires that record to be PASS. Any later Todo 10 retry forms a new valid prefix/record pair and supersedes the prior attempt.
- The test runner uses `todo=1, subcommand=validator-tests`, hashes validator/test source plus fixture/current reviewed inputs, and uses an empty `output_hashes` map. Import/syntax/red failures must still be caught by the runner shell and appended as FAIL, so a later PASS can supersede them without erasing history.
- All file reads use strict UTF-8 and exact bytes. Regexes, region boundaries, normalization, eight semantic axes, workflow matrix, set overlap rules and 108 replacement rules are copied from this reviewed plan; the script may not infer alternative policy.
- `ren-sheng-whole-book-validator-tests.py` loads the hyphenated validator path with `importlib.util.spec_from_file_location` and uses `tempfile.TemporaryDirectory`; it tests source/formal boundaries, R2 variants, R4 A–J exclusions, semantic/workflow schema, set overlaps, evidence transitions, technical overlap, anchors, prefix/suffix, and all three invalidation classes. It also tests the runtime-snapshot transient template, exclusive creation, repository/different-name/symlink/directory rejection, successful cleanup and failure retention. It leaves no repository files. It accepts `--receipt` and atomically appends its PASS/FAIL JSON line to the invocation JSONL.
- Required subcommands and outputs:
  - `formal-inventory`: reads the reviewed formal note; writes a byte-for-byte baseline copy, the 165-card preservation manifest and 108-row technical inventory; asserts the copy hash equals the reviewed SHA-256 plus `20/31/15/99`, `99/3/4/2`, coordinate `6`, overlap `4`.
  - `source-inventory`: reads the intermediate draft; writes the 266-row source manifest; asserts `54/52/28/132`, `R1:U01`, six R2 variants and no ambiguous span.
  - `ledger-check`: reads both manifests, ledger, reconciliation and fixture; validates all eight Phase 4 axes, workflow/topology/action matrix, eight sets/overlaps, `N_new`, target evidence and `unresolved=[]`.
  - `policy-check`: reads fixture source, fixture results, ledger and formal manifest; asserts exactly nine fixture and seven sentinel rows, expected/actual/forbidden/evidence/verdict fields and all PASS.
  - `anchor-check`: reads title-affecting approved hunks from the ledger, applies them with the 108 heading transforms in memory, writes/revalidates the anchor map, and asserts `165 + N_new`, unique anchors and all links/insertion targets resolved. It does not read the not-yet-created candidate.
  - `candidate-structure`: reads candidate, ledger, technical inventory and anchor map; checks typed Parts A/B/C, fixed section order, six article rows, six trajectories, no copied complete card and exact bound hunks.
  - `candidate-check`: applies all candidate target-bound hunks in memory; validates `165 + N_new`, modeled-post evidence, anchors, fixtures/sentinels and scans only Part A/B `target-after` plus Part C for forbidden tokens.
  - `prefix-check`: compares reviewed formal baseline to the written formal note after Todo 8; reads the formal manifest, ledger and anchor map; writes metadata-cleanup and archive-audit reports; asserts exact 108 transforms + approved repair/new-card hunks, prefix equality, `165 + N_new`, archive identity/body structure, provenance/article-link separation and zero forbidden hits.
  - `section-check`: reads the post-Todo-9 formal note, anchor map and ledger; writes index/trajectory audits; asserts suffix-only Stage 4 section, four children in order, six article directions, six trajectory chains and all anchors resolved.
  - `final-anchor-check`: parses the already transformed/appended final formal note without applying the 108 transforms again; reads ledger and anchor map; asserts the actual `165 + N_new` heading/anchor set, post-transform category names, article-link and insertion resolution, and zero duplicate/unresolved/technical anchors. It is check-only in F4.
  - `final-check`: reads every required Todo 0–9 evidence file and final formal note, including validator/test receipts, but explicitly excludes not-yet-created F1–F5 receipts and final-wave snapshots; writes final QA; recomputes all numeric/hash/content/scope gates and fails if any required prior report is not PASS.
  - `wave-snapshot-create`: with no `--receipt`, hashes the exact F1–F5 inputs plus plan, draft, external review seal, governing/source/final files. It includes validator invocation JSONL but excludes F1–F5 receipts, the wave snapshot and the review-runtime ledger because those are append-only wave outputs. Runtime continuation paths are governed separately by preflight/runtime-ledger checks. It appends a new ACTIVE wave record and writes the snapshot last.
  - `wave-snapshot-check`: requires `--check-only`, selects the named `wave_id`, requires state `ACTIVE`, recomputes every input hash and `wave_input_set_sha256`, and writes nothing.
  - `wave-drift-invalidate`: is the sole no-receipt **INPUT_DRIFT** invalidator. It requires an internally valid ACTIVE wave and proven expected/observed input-set mismatch, then appends `INVALIDATED reason=INPUT_DRIFT`; it fails if inputs match, snapshot is corrupt or wave is not active.
  - `review-receipt-append`: first performs wave-snapshot-check, then atomically appends one attempt to the named F receipt. A valid COMPLETE result requires Oracle metadata and first-line verdict. Wrong agent, timeout, missing final message, active-gate rejection or explicit transport failure is normalized and appended as `NO_RESULT` rather than silently rejected. Malformed result JSON or snapshot mismatch exits nonzero without deleting/altering the source result. The receipt stores the full available message/error verbatim plus hashes and never changes reviewer inputs.
  - `review-receipt-append` additionally requires `--runtime-ledger`, `--runtime-attempt-id`, `--runtime-preflight` and `--runtime-workspace`; it reruns review-runtime-final-check, refuses to append unless the exact wave/reviewer/attempt/result-message hash is registered and complete runtime scope is PASS, and stores the runtime-ledger hash plus runtime-final-check JSON/hash in the reviewer receipt. Thus no reviewer verdict can exist without durable authenticated platform-side-effect evidence.
  - `review-receipt-check`: requires `--check-only`; verifies the named receipt contains the exact wave/reviewer/attempt/message hash returned by review-receipt-append and that the receipt append is intact. It writes nothing.
  - `review-runtime-snapshot`: before a fresh reviewer task, writes only to `/tmp`. It captures NUL-safe workspace inventory and hashes all continuation nodes, identifies the exact preflight-bound execution-runtime path separately, and binds to wave/reviewer/attempt UUID.
  - `review-runtime-register`: after the task, compares before/current workspace and returned metadata. It always registers a valid zero-new-node attempt; when transport/result metadata is incomplete it uses `runtime_mode=zero-node-no-result`, permits empty session ID, and binds wave/reviewer/attempt/result-message hash so a NO_RESULT receipt can be appended/retried. Wrong-agent with a real session ID still registers zero node or its exact node, then receipt logic normalizes the verdict to NO_RESULT. Any new continuation node requires a nonempty actual session ID and exactly one regular non-symlink `.omo/run-continuation/<actual_session_id>.json`; missing ID with a new node, wrong basename/type, multiple nodes or non-execution prior-path drift is `RUNTIME_PATH_DRIFT`. Success records runtime mode, nullable path/hash, session metadata and execution-runtime before/after state.
  - `review-runtime-final-check`: requires `--check-only`; it requires one-to-one frozen reviewer paths, no unregistered continuation path and no baseline/registered-node drift. For execution-runtime it validates exact session/path plus only `absent→regular` or `regular→regular`, requires current regular non-symlink, rejects deletion/rename/extra node, and reports initial/current kind/hash without requiring hash equality.
  - `wave-runtime-invalidate`: is the sole no-receipt **RUNTIME_PATH_DRIFT** invalidator. It requires an internally valid ACTIVE wave plus failed review-runtime-register proof and exact before/current/result context, then appends `INVALIDATED reason=RUNTIME_PATH_DRIFT`. Unauthenticated paths are never deleted/broadly exempted; this is terminal pending operator resolution.
  - `wave-invalidate`: is the only ordinary non-drift invalidator and is allowed only after a complete checked `BLOCKED` receipt. The three invalidation classes are mutually exclusive: input-set mismatch → `wave-drift-invalidate`; runtime-path/register mismatch → `wave-runtime-invalidate`; reviewer/content BLOCKED with stable inputs/runtime → receipt-bound `wave-invalidate`. Wrong class, missing proof/receipt or any other no-receipt invalidation fails. No fix begins before the applicable transition succeeds.

### Exact Todo QA invocation matrix

Run every command from `/home/king/github/growing-myself`; quote every path. A command is PASS only with exit `0`, stdout JSON `status=PASS`, expected counts below and the named output present. For every `validator.py` invocation in Todos 1–10, append the literal suffix `--receipt .omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`; the table omits only that repeated suffix. The output artifact is closed before the separate JSONL append and is never modified to embed its own receipt. Todo 0 is the sole non-validator exception and uses the exact standalone wrapper below.

This matrix is normative for Todos 0–10. Each Todo's prose `QA scenarios` explains the semantic failure mode but never substitutes for its exact matrix invocation; both the command result and prose acceptance criteria must pass.

Todo 0 exact standalone wrapper (the worker may set `REN_SHENG_EXECUTION_AUTHORIZED=1` only when the current separate worker session was explicitly started to execute this plan; it must set `REN_SHENG_AUTHORIZATION_REF` to the authorizing user-message/session reference, `REN_SHENG_EXECUTION_SESSION_ID` to its actual `ses_...` metadata, and `REN_SHENG_SIBLING_AGENTS_ACCESSED=0` only after checking its own transcript/tool history confirms no sibling-book `AGENTS.md` access):

```bash
set -uo pipefail
cd /home/king/github/growing-myself
collision="$(find .omo/evidence -mindepth 1 -maxdepth 1 \( -name 'ren-sheng-whole-book-*' -o -name 'final-ren-sheng-whole-book-consolidation-qa.md' \) -print -quit)"
if test -n "$collision"; then
  python3 -c 'import json,sys; print(json.dumps({"command":"todo0-preflight","status":"FAIL","disposition":"STOPPED","failures":["evidence path collision: "+sys.argv[1]]},ensure_ascii=False,sort_keys=True))' "$collision"
  exit 1
fi
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
GIT_MASTER=1 git status --porcelain=v1 -z --branch --untracked-files=all >"$tmp/status.z"; printf '%s' "$?" >"$tmp/status.rc"
GIT_MASTER=1 git ls-files -m -o --exclude-standard -z >"$tmp/paths.z"; printf '%s' "$?" >"$tmp/paths.rc"
GIT_MASTER=1 git diff --binary >"$tmp/tracked.diff"; printf '%s' "$?" >"$tmp/tracked.rc"
GIT_MASTER=1 git diff --cached --binary >"$tmp/cached.diff"; printf '%s' "$?" >"$tmp/cached.rc"
GIT_MASTER=1 git rev-parse HEAD >"$tmp/head.oid"; printf '%s' "$?" >"$tmp/head.rc"
GIT_MASTER=1 git show-ref --head >"$tmp/refs.txt"; printf '%s' "$?" >"$tmp/refs.rc"
python3 - "$tmp" <<'PY'
from __future__ import annotations
import hashlib, json, os, re, sys
from pathlib import Path

root = Path.cwd()
tmp = Path(sys.argv[1])
authorized = os.environ.get("REN_SHENG_EXECUTION_AUTHORIZED") == "1"
auth_ref = os.environ.get("REN_SHENG_AUTHORIZATION_REF", "")
sibling_attestation = os.environ.get("REN_SHENG_SIBLING_AGENTS_ACCESSED", "")
execution_session_id = os.environ.get("REN_SHENG_EXECUTION_SESSION_ID", "")
expected = {
    "AGENTS.md": (117, "6def8b9c885fef8394eeaee9f74c9e38f885d5d522c53838aedf13daa4376cf2"),
    "路遥/人生/《人生》微信读书提示词.md": (230, "914b2f4cad3c73e33da6ddb010b4762cd7c142e4b54037ba7a6a2d1653b91856"),
    "路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md": (284, "a31aef8b30291c29b804217e1f2ea243203679f9e1253dbb270ea752fcdab649"),
    ".omo/evidence/fixtures/add-whole-book-consolidation-model.md": (215, "67f1f16a539a156db838fc58d4eeb6322a0d516d73b08a8bf6dcc8ebbb6877c3"),
    "路遥/人生/《人生》中间整理稿.md": (15009, "dadd95ed30f06b20f61dec7409cd8ff317b33132c33be616c8b0af000b248ef0"),
    "路遥/人生/《人生》阅读笔记.md": (5930, "7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11"),
}
failures: list[str] = []
if not authorized or not auth_ref:
    failures.append("explicit worker authorization/reference missing")
if sibling_attestation != "0":
    failures.append("no-sibling-AGENTS-access attestation missing")
if re.fullmatch(r"ses_[A-Za-z0-9]+", execution_session_id) is None:
    failures.append("valid execution session ID missing")
for name in ("status", "paths", "tracked", "cached", "head", "refs"):
    rc = int((tmp / f"{name}.rc").read_text(encoding="ascii"))
    if rc != 0:
        failures.append(f"git command failed: {name} rc={rc}")
files: dict[str, object] = {}
for rel, (want_lines, want_hash) in expected.items():
    data = (root / rel).read_bytes()
    got = {"lines": len(data.splitlines()), "sha256": hashlib.sha256(data).hexdigest()}
    files[rel] = got
    if got != {"lines": want_lines, "sha256": want_hash}:
        failures.append(f"immutable mismatch: {rel}")
seal_path = root / ".omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json"
seal_result: dict[str, object] = {"state": "missing-or-invalid"}
try:
    seal = json.loads(seal_path.read_text(encoding="utf-8"))
    payload = dict(seal)
    claimed_payload_hash = payload.pop("seal_payload_sha256")
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    got_payload_hash = hashlib.sha256(canonical).hexdigest()
    if got_payload_hash != claimed_payload_hash:
        failures.append("review seal payload hash mismatch")
    plan_rel = ".omo/plans/consolidate-ren-sheng-whole-book-notes.md"
    draft_rel = ".omo/drafts/consolidate-ren-sheng-whole-book-notes.md"
    control_files: dict[str, dict[str, object]] = {}
    for rel, line_key, hash_key in (
        (plan_rel, "plan_lines", "plan_sha256"),
        (draft_rel, "draft_lines", "draft_sha256"),
    ):
        data = (root / rel).read_bytes()
        current = {"lines": len(data.splitlines()), "sha256": hashlib.sha256(data).hexdigest()}
        control_files[rel] = current
        if current != {"lines": seal[line_key], "sha256": seal[hash_key]}:
            failures.append(f"sealed control file mismatch: {rel}")
    expected_agents = {"Metis": "Metis - Plan Consultant", "Momus": "Momus - Plan Critic", "Oracle": "oracle"}
    reviews = seal.get("reviews", [])
    if seal.get("schema_version") != 1 or seal.get("slug") != "consolidate-ren-sheng-whole-book-notes" or seal.get("all_approved") is not True:
        failures.append("review seal top-level approval/schema invalid")
    if [row.get("role") for row in reviews] != ["Metis", "Momus", "Oracle"]:
        failures.append("review seal roles/order invalid")
    for row in reviews:
        role = row.get("role")
        message = row.get("full_message", "")
        first = next((line.strip() for line in message.splitlines() if line.strip()), "")
        if role not in expected_agents or row.get("agent") != expected_agents.get(role):
            failures.append(f"review agent mismatch: {role}")
        if row.get("verdict") != "APPROVED" or first != "APPROVED":
            failures.append(f"review verdict not unconditional APPROVED: {role}")
        if hashlib.sha256(message.encode("utf-8")).hexdigest() != row.get("message_sha256"):
            failures.append(f"review message hash mismatch: {role}")
        if row.get("reviewed_plan_sha256") != seal.get("plan_sha256") or row.get("reviewed_draft_sha256") != seal.get("draft_sha256"):
            failures.append(f"reviewed control hash mismatch: {role}")
        if not row.get("session_id"):
            failures.append(f"review session missing: {role}")
    seal_result = {
        "state": "valid" if not any("review seal" in item or "review " in item or "sealed control" in item for item in failures) else "invalid",
        "payload_sha256": got_payload_hash,
        "control_files": control_files,
        "review_sessions": {row.get("role"): row.get("session_id") for row in reviews},
    }
except Exception as exc:
    failures.append(f"review seal missing/invalid: {exc}")
same_book_agents = root / "路遥/人生/AGENTS.md"
if same_book_agents.exists():
    same_bytes = same_book_agents.read_bytes()
    same_book_result: dict[str, object] = {
        "state": "present-conflict-stop",
        "sha256": hashlib.sha256(same_bytes).hexdigest(),
        "lines": len(same_bytes.splitlines()),
        "read_to_eof": True,
    }
    failures.append("same-book AGENTS appeared after review; replanning required")
else:
    same_book_result = {"state": "absent", "read_to_eof": False}
status_bytes = (tmp / "status.z").read_bytes()
tracked = (tmp / "tracked.diff").read_bytes()
cached = (tmp / "cached.diff").read_bytes()
if cached:
    failures.append("cached diff is not empty")
head_oid = (tmp / "head.oid").read_text(encoding="ascii").strip()
refs_bytes = (tmp / "refs.txt").read_bytes()
if not head_oid:
    failures.append("baseline HEAD missing")
path_rows: list[dict[str, str]] = []
for raw in (tmp / "paths.z").read_bytes().split(b"\0"):
    if not raw:
        continue
    rel = os.fsdecode(raw)
    path = root / rel
    if path.is_symlink():
        payload = os.readlink(path).encode("utf-8", "surrogateescape")
        kind = "symlink"
    elif path.is_file():
        payload = path.read_bytes()
        kind = "file"
    elif path.exists():
        payload = b"<non-file>"
        kind = "non-file"
    else:
        payload = b"<missing>"
        kind = "missing"
    path_rows.append({"path": rel, "kind": kind, "sha256": hashlib.sha256(payload).hexdigest()})
execution_runtime_path = f".omo/run-continuation/{execution_session_id}.json" if execution_session_id else ""
execution_runtime_initial: dict[str, object] = {
    "initial_state": "absent",
    "initial_kind": "absent",
    "initial_sha256": None,
}
if execution_runtime_path:
    execution_runtime_node = root / execution_runtime_path
    if execution_runtime_node.is_symlink():
        failures.append("execution runtime path is not a regular non-symlink file")
        execution_runtime_initial = {"initial_state": "present", "initial_kind": "symlink", "initial_sha256": None}
    elif execution_runtime_node.exists() and not execution_runtime_node.is_file():
        failures.append("execution runtime path is not a regular non-symlink file")
        execution_runtime_initial = {"initial_state": "present", "initial_kind": "non-file", "initial_sha256": None}
    elif execution_runtime_node.is_file():
        initial_bytes = execution_runtime_node.read_bytes()
        execution_runtime_initial = {
            "initial_state": "present",
            "initial_kind": "regular",
            "initial_sha256": hashlib.sha256(initial_bytes).hexdigest(),
        }
plan_text = (root / ".omo/plans/consolidate-ren-sheng-whole-book-notes.md").read_text(encoding="utf-8")
scope_prefix = plan_text.split("- Before any reading-note edit", 1)[0]
allowlist = sorted(set(re.findall(r"`(\.omo/evidence/[^`]+)`", scope_prefix)))
allowed_changed_paths = sorted(["路遥/人生/《人生》阅读笔记.md", *allowlist])
result = {
    "command": "todo0-preflight",
    "status": "PASS" if not failures else "FAIL",
    "disposition": "PROCEED" if not failures else "STOPPED",
    "authorization_ref": auth_ref,
    "explicit_worker_authorization": "PASS" if authorized and auth_ref else "FAIL",
    "router_precedence": "PASS" if files["路遥/人生/《人生》微信读书提示词.md"] == {"lines": 230, "sha256": expected["路遥/人生/《人生》微信读书提示词.md"][1]} else "FAIL",
    "no_sibling_agents_access": "PASS" if sibling_attestation == "0" else "FAIL",
    "same_book_agents": same_book_result,
    "review_seal": seal_result,
    "immutable_files": files,
    "git_status_z_sha256": hashlib.sha256(status_bytes).hexdigest(),
    "tracked_diff_sha256": hashlib.sha256(tracked).hexdigest(),
    "cached_diff_sha256": hashlib.sha256(cached).hexdigest(),
    "baseline_head_oid": head_oid,
    "baseline_refs_sha256": hashlib.sha256(refs_bytes).hexdigest(),
    "baseline_refs": refs_bytes.decode("utf-8", "strict").splitlines(),
    "baseline_paths": path_rows,
    "execution_runtime": {
        "session_id": execution_session_id,
        "path": execution_runtime_path,
        **execution_runtime_initial,
        "policy": "exact runtime-only path may be created/updated by platform; never staged/edited/deleted by worker",
    },
    "allowed_evidence_outputs": allowlist,
    "allowed_changed_paths": allowed_changed_paths,
    "failures": failures,
}
text = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
(root / ".omo/evidence/ren-sheng-whole-book-preflight.md").write_text(
    "# Ren Sheng whole-book preflight\n\n```json\n" + text + "\n```\n", encoding="utf-8"
)
print(json.dumps(result, ensure_ascii=False, sort_keys=True))
raise SystemExit(0 if not failures else 1)
PY
```

| Todo | exact invocation | required result |
|---|---|---|
| 0 | Execute the exact standalone wrapper above with authorization environment set only from the explicit worker-start message. | stdout JSON `status=PASS`; preflight created only after collision check; content baselines and review seal valid; same-book AGENTS absent; cached diff empty; NUL-safe status/diff/per-path hashes, exact baseline HEAD OID and complete `show-ref --head` bytes/hash stored; `allowed_changed_paths` equals target plus evidence |
| 1 | `python3 .omo/evidence/ren-sheng-whole-book-validator-tests.py --receipt .omo/evidence/ren-sheng-whole-book-validator-invocations.jsonl`; then `python3 .omo/evidence/ren-sheng-whole-book-validator.py formal-inventory --formal 路遥/人生/《人生》阅读笔记.md --baseline-copy-out .omo/evidence/ren-sheng-whole-book-formal-baseline.md --preservation-out .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --technical-out .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md` | tests PASS with receipt; baseline copy SHA-256 equals reviewed formal hash; formal `165`; technical union `108`; no ambiguous span/hit |
| 2 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py source-inventory --source 路遥/人生/《人生》中间整理稿.md --out .omo/evidence/ren-sheng-whole-book-source-manifest.md` | source `266`; round counts exact; missing/duplicate/ambiguous sets empty |
| 3 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py ledger-check --source-manifest .omo/evidence/ren-sheng-whole-book-source-manifest.md --formal-manifest .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --reconciliation .omo/evidence/ren-sheng-whole-book-reconciliation.md --fixture .omo/evidence/fixtures/add-whole-book-consolidation-model.md` | 266 source + 165 formal rows covered; eight axes/schema/sets PASS; `unresolved=[]`; `N_new` fixed |
| 4 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py policy-check --fixture .omo/evidence/fixtures/add-whole-book-consolidation-model.md --results .omo/evidence/ren-sheng-whole-book-fixture-results.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --formal-manifest .omo/evidence/ren-sheng-whole-book-preservation-manifest.md` | nine fixture + seven sentinel rows; all required fields; all PASS |
| 5 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py anchor-check --formal 路遥/人生/《人生》阅读笔记.md --technical .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --out .omo/evidence/ren-sheng-whole-book-anchor-map.md` | exactly `165 + N_new`; duplicate/unresolved anchors empty; all insertion targets fixed |
| 6 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py candidate-structure --candidate .omo/evidence/ren-sheng-whole-book-candidate-section.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --technical .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md --anchor-map .omo/evidence/ren-sheng-whole-book-anchor-map.md` | Parts A/B/C and all fixed structural counts PASS; zero unbound hunk/copied-card failures |
| 7 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py candidate-check --formal 路遥/人生/《人生》阅读笔记.md --source-manifest .omo/evidence/ren-sheng-whole-book-source-manifest.md --formal-manifest .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --reconciliation .omo/evidence/ren-sheng-whole-book-reconciliation.md --technical .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md --fixture-results .omo/evidence/ren-sheng-whole-book-fixture-results.md --anchor-map .omo/evidence/ren-sheng-whole-book-anchor-map.md --candidate .omo/evidence/ren-sheng-whole-book-candidate-section.md --out .omo/evidence/ren-sheng-whole-book-candidate-qa.md` | target-bound hits `0`; modeled-post cards `165 + N_new`; provisional states all satisfied; fixture/sentinel/anchor failures `0` |
| 8 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py prefix-check --baseline-formal .omo/evidence/ren-sheng-whole-book-formal-baseline.md --written-formal 路遥/人生/《人生》阅读笔记.md --baseline-sha256 7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11 --technical .omo/evidence/ren-sheng-whole-book-technical-field-inventory.md --candidate .omo/evidence/ren-sheng-whole-book-candidate-section.md --formal-manifest .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --anchor-map .omo/evidence/ren-sheng-whole-book-anchor-map.md --metadata-out .omo/evidence/ren-sheng-whole-book-metadata-cleanup.md --archive-out .omo/evidence/ren-sheng-whole-book-archive-audit.md` | independent baseline hash; prefix equality; all `165 + N_new` archive identities, provenance/article-link separation and body classes; `108→0` PASS |
| 9 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py section-check --formal 路遥/人生/《人生》阅读笔记.md --anchor-map .omo/evidence/ren-sheng-whole-book-anchor-map.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --index-out .omo/evidence/ren-sheng-whole-book-index-audit.md --trajectory-out .omo/evidence/ren-sheng-whole-book-trajectory-audit.md` | one suffix section; child order `1-4`; article rows `6`; trajectories `6`; anchor failures `0` |
| 10 | `python3 .omo/evidence/ren-sheng-whole-book-validator.py final-check --formal 路遥/人生/《人生》阅读笔记.md --evidence-root .omo/evidence --preflight .omo/evidence/ren-sheng-whole-book-preflight.md --out .omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md`; then `GIT_MASTER=1 git diff --check`; `GIT_MASTER=1 git status --porcelain=v1 -z --untracked-files=all`; `GIT_MASTER=1 git diff --binary`; `GIT_MASTER=1 git diff --cached --binary`; `GIT_MASTER=1 git rev-parse HEAD`; `GIT_MASTER=1 git show-ref --head` | every report/content gate PASS; path delta allowlisted; pre-existing path hashes, baseline HEAD and complete refs unchanged; cached diff and `git diff --check` empty |

Todo 8 baseline handling is mandatory: Todo 1 stores the reviewed formal bytes byte-for-byte at `.omo/evidence/ren-sheng-whole-book-formal-baseline.md` and verifies its hash before target mutation. `prefix-check` reads that immutable evidence copy; passing the same post-edit path as both logical arguments is forbidden.

Invocation phase binding is exact: Todo 1 `formal-inventory`, Todo 5 `anchor-check` and Todo 7 `candidate-check` record the formal path as phase `reviewed-baseline` with the reviewed hash; Todo 8 `prefix-check` records both `reviewed-baseline` for the baseline copy and `cleaned-prefix` for the written formal output; Todo 9 `section-check` records `final-suffix-appended`; Todo 10 `final-check` records the same final hash. Todos 2–4 and 6 have no evolving formal-path input. `final-check` validates these named phases through the transform chain, not by replacing historical hashes with the final path hash.

### Required evidence gates

1. **Preflight gate:** `.omo/evidence/ren-sheng-whole-book-preflight.md` records root/router/stage rules, explicit execution authorization, same-book `AGENTS.md` result, exact comparison to all six reviewed hashes/line counts, the `porcelain=v1 -z` dirty-worktree snapshot, tracked-diff hash, staged-diff hash, per-path hashes for pre-existing dirty/untracked files and the exact output allowlist. Every planned evidence path must be absent at preflight; otherwise stop rather than overwrite it.
2. **Preservation gate:** `.omo/evidence/ren-sheng-whole-book-source-manifest.md` contains all 266 source units; `.omo/evidence/ren-sheng-whole-book-preservation-manifest.md` contains all 165 existing formal cards and the whole-prefix baseline. For an unmodified card, pre/post normalized hashes must match. Any mismatch requires a ledger-named exact repair hunk and side-by-side read review; final prefix bytes must match the approved transformed baseline.
3. **Coverage gate:** the ledger has exactly 266 unique source keys and 165 unique baseline-formal keys. R1/R2/R3/R4 source cardinalities are 54/52/28/132; baseline-formal cardinalities are 20/31/15/99. All eight named sets are emitted under the primary-partition/secondary-overlap rules; every row has a disposition, `N_new = count(planned-new-formal)`, and `unresolved=[]`.
4. **Technical-field gate:** the planning baseline is 99 unspaced source-ID headings, three spaced group headings, four explicit chapter/range lines and two extra coordinate-only headings: 108 unique lines. Coordinate matches total six with four overlaps. Execution records all 108 exact before/after rows and requires zero target-surface hits for every forbidden-token family and coordinate regex. There is no cursor, group-heading or external-source exception.
5. **Anchor gate:** every readable anchor is unique and every article-index anchor resolves to exactly one heading in the in-memory post-transform formal model, including any ledger-approved new-card insertion. Zero unresolved and zero multiply-resolved anchors.
6. **Fixture gate:** all nine fixture cases record input, expected disposition, actual decision, evidence/anchor or `policy-only`, forbidden outcome and PASS/FAIL.
7. **Sentinel gate:** all seven fixed sentinels are read after source IDs disappear and verified through their readable anchors, not by hidden IDs.
8. **Reading-surface gate:** full read-back confirms the four-round archive remains before the appended full-book section; the four new subsections are in fixed order; article rows are navigation, not essays; original user voice and external-reader boundaries remain visible.
9. **Scope gate:** ordinary delta equals `allowed_changed_paths`; baseline paths, HEAD and refs remain unchanged except execution-runtime following only its declared absent/present→regular transition with exact session/path. The runtime ledger authenticates F1–F5 paths one-to-one and freezes them; no other continuation node appears/drifts. Use NUL-safe inventory, runtime-final-check, HEAD/refs and diff-check. Push remains prohibited, not post-state proof.
10. **Archive-identity gate:** `.omo/evidence/ren-sheng-whole-book-archive-audit.md` contains all `165 + N_new` post-transform cards, one legal Phase 4 archive disposition per card, required card-body structure for its class, stable archive identity independent of article links, and exact repair/new-card provenance. Zero missing, duplicate, silently promoted or silently demoted cards.

### Seven sentinel assertions

| sentinel | required post-edit assertion |
|---|---|
| Former ID 003 | Preserve the earlier `留意` versus later `很快妥善解决` contrast and the external challenge that he may hate lacking privilege, not privilege itself. |
| Former ID 006 | Preserve the distinction between unwillingness to mine coal and willingness to endure hardship when the work confirms a valued identity. |
| Former ID 021 | Preserve the original 田晓霞联想, the journalist-identity evidence and the explicit warning not to equate the two characters. |
| Former ID 109 | Preserve spatial projection analysis and prohibit backfilling later defeat into the present scene. |
| Former ID 117 | Preserve the user's sharp identity/love formulation plus the evidence bridge explaining how position controls which love is acknowledged. |
| 刘玉海救灾处 | State that the county rescue team arrived five hours later; do not invent a five-hour road delay. Preserve `七处伤` and leadership/action contrast. |
| 黄亚萍的物质付出 | Acknowledge real material cost while distinguishing it from 巧珍's deprivation-based support; neither erase nor equate the two. |

## Execution strategy

### Parallel execution waves

- **Wave 0, hard gate:** Todo 0 only. No content mutation.
- **Wave 1, preservation and coverage:** Todos 1, 2, then 3. Todo 1 freezes formal cards/technical transforms, Todo 2 freezes all source units, and Todo 3 closes their reconciliation; all remain `.omo/evidence` only.
- **Wave 2, policy and anchor design:** Todos 4 and 5 may run in parallel after Todo 3 because they write separate evidence files.
- **Wave 3, candidate before target:** Todo 6 composes proposed transforms, local repairs and the new full-book section in evidence; Todo 7 independently rejects or approves target-bound output. The formal note remains untouched.
- **Wave 4, controlled target mutation:** Todo 8 performs exact prefix transforms/local repairs; Todo 9 appends the approved full-book section. They are sequential because both edit the same file.
- **Wave 5, verification:** Todo 10 runs full content, preservation, fixture, sentinel, anchor, scope and Git QA.
- **Final verification wave:** F1–F5 run after Todo 10 and all must approve before completion can be reported.

### Dependency matrix

| Todo | Depends on | Blocks | Can parallelize with |
|---|---|---|---|
| 0 | explicit worker execution authorization | 1–10, F1–F5 | none |
| 1 | 0 | 2–10, F1–F5 | none |
| 2 | 1 | 3–10, F1–F5 | none |
| 3 | 1, 2 | 4–10, F1–F5 | none |
| 4 | 3 | 6–10, F1–F5 | 5 |
| 5 | 3 | 6–10, F1–F5 | 4 |
| 6 | 1–5 | 7–10, F1–F5 | none |
| 7 | 6 | 8–10, F1–F5 | none |
| 8 | 7 | 9, 10, F1–F5 | none |
| 9 | 8 | 10, F1–F5 | none |
| 10 | 9 | F1–F5 | none |

### Plan review receipts

The draft records review history but is not the final approval authority, avoiding a self-hash/receipt loop. After the final plan and draft bytes are frozen, Metis, Momus and Oracle must each read the same bytes to EOF and return unconditional `APPROVED`. Do not edit either file after the first of those final reviews begins.

Prometheus then creates exactly one external control-plane artifact: `.omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json`. Creating the seal is plan finalization, not execution. The seal schema is fixed:

- `schema_version=1`, `slug`, `created_at`, `plan_path`, `plan_lines`, `plan_sha256`, `draft_path`, `draft_lines`, `draft_sha256`, `all_approved=true`;
- `reviews`: exactly one latest entry each for `Metis`, `Momus`, `Oracle`, containing actual `agent`, `session_id`, `verdict=APPROVED`, `full_message`, `message_sha256`, `reviewed_plan_sha256`, and `reviewed_draft_sha256`;
- every reviewed hash must equal the top-level frozen hash; each full message's first non-whitespace line must be `APPROVED`; actual agent metadata must match the role;
- `seal_payload_sha256` is SHA-256 of canonical UTF-8 JSON (`ensure_ascii=false`, sorted keys, separators `(',', ':')`) over the object with `seal_payload_sha256` omitted.

The seal is written only after all three approvals and is never edited. Todo 0 recomputes the canonical payload hash, plan/draft line counts and hashes, role/session/agent/message hashes and verdict lines. Missing/invalid seal, modified plan/draft, absent role or conditional/non-APPROVED result is `STOPPED: unsealed or stale plan` before Todo 1. The final handoff cites the seal path; execution authorization remains a separate user action.

## Todos

- [x] 0. Preflight: enforce Stage 4 trigger, reviewed hashes and baseline-relative worktree scope before mutation
  - **What to do / Must NOT do:** First, without writing anything, require every enumerated output evidence path to be absent; if any exists, stop externally and do not overwrite it. Only after that check passes, re-read `/home/king/github/growing-myself/AGENTS.md`, the router and Phase 4 prompt; create the preflight report; and check whether `路遥/人生/AGENTS.md` now exists. If same-book rules are present, read them, record the conflict and stop for replanning because they were absent at review. Verify an explicit worker execution command/session; plan approval alone is insufficient. Compare exact bytes and line counts of all six reviewed files; any mismatch is recorded and stops before Todo 1. Capture `GIT_MASTER=1 git status --porcelain=v1 -z --branch --untracked-files=all`, tracked diff bytes/hash, cached diff bytes/hash, and content/status hashes for every pre-existing dirty or untracked path. Establish exact allowed new/changed paths. Do not read sibling-book AGENTS, edit reading files, overwrite evidence, stage, commit or push.
  - **Parallelization:** Wave 0 | Blocked by: explicit execution authorization | Blocks: 1–10, F1–F5
  - **References:** `Reviewed immutable baselines`; `AGENTS.md`; router `36-40,112-122`; Phase 4 `41-85`; approved draft. Planning-time Git facts: one tracked dirty continuation file, untracked plan/draft, several unowned run-continuation JSON files, empty staged diff and no existing untracked `.omo/evidence` output.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-preflight.md` contains PASS entries for authorization, precedence, same-book AGENTS absence, no sibling access, all six content baselines, canonical review seal, sealed current plan/draft hashes and three approvals, all planned evidence paths absent, empty staged diff, NUL-safe/per-path baseline hashes, exact baseline `HEAD` and complete refs, exact evidence outputs, and `allowed_changed_paths = target + evidence`. Any missing gate stops before Todo 1.
  - **QA scenarios:** Happy — independently recompute all six hashes and reproduce the baseline snapshot. Failure — if any planned evidence path already exists, write nothing and report `STOPPED: evidence path collision` to the user. For authorization absence, new same-book rules, reviewed-hash mismatch, staged changes or unexplained source/target delta after the path check, write `STOPPED: stale, conflicting, or unauthorized input` in the newly created preflight report and do not proceed. Evidence: `.omo/evidence/ren-sheng-whole-book-preflight.md` when creation is safe.
  - **Commit:** N | preflight evidence only

- [x] 1. Validator and formal preservation: test the QA tool, snapshot reviewed bytes, fingerprint 165 cards and freeze 108 transforms
  - **What to do / Must NOT do:** Load `shared/programming` because this Todo creates Python. Implement the two allowlisted standard-library-only validator files exactly to the executable contract; write unit tests first, then make them pass. Run the exact Todo 1 invocations. The validator copies the reviewed formal note byte-for-byte to the baseline evidence path, parses 165 cards with exact spans/hashes/block counts, and writes 108 exact before/family/after rows. The 99 bracketed headings delete only their final technical suffix; the other nine use fixed replacements. Do not edit the formal note, weaken tests, access the network or invent policy.
  - **Parallelization:** Wave 1 | Blocked by: 0 | Blocks: 2–10, F1–F5
  - **References:** formal note `1-5930`; parser/cardinalities and planning-time inventory in Scope; round starts `3,557,1238,1701`; Phase 4 technical boundary `87-125`.
  - **Acceptance criteria:** Both validator files exist; `python3 .omo/evidence/ren-sheng-whole-book-validator-tests.py` exits 0 with all named test families PASS. The baseline copy hash is `7533aacd799479ad4a6a142c9509047a4c71157a02e799b9e2509b14fe4e9a11`. Preservation manifest has exactly 165 unique rows with `20/31/15/99`, no blank span/hash/count and `Ambiguous blocks: none`. Technical inventory has exactly 108 unique rows with `99/3/4/2`, coordinate `6`, overlap `4` and exact after text.
  - **QA scenarios:** Happy — the exact Todo 1 command emits exit 0/status PASS and the test suite independently reproduces parser/transform assertions. Failure — test failure, baseline hash mismatch, ambiguous card, nontechnical byte change, omitted line 5917 or spaced group heading, or count mismatch blocks Todo 2; do not alter expected constants to force PASS. Evidence: validator files, baseline copy, preservation manifest and technical inventory.
  - **Commit:** N | preservation evidence only

- [x] 2. Source manifest: enumerate and fingerprint all 266 canonical units across R1–R4
  - **What to do / Must NOT do:** Parse the intermediate draft only within the four fixed source regions using stable keys and exact byte boundaries. Write one row per canonical unit with heading, offsets, raw/normalized hashes, quote/user/external block counts and representative excerpts. Include `R1:U01`; keep all six R2 `A` variants as separate rows with `variant_of`. Do not infer source units from later diagnostic/index sections and do not edit either source file.
  - **Parallelization:** Wave 1 | Blocked by: 1 | Blocks: 3–10, F1–F5
  - **References:** source parser in Scope; intermediate draft regions `13-1894`, `2263-4440`, `4520-5972`, `6029-14732`; complete source file `1-15009`.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-source-manifest.md` has exactly 266 unique keys with R1/R2/R3/R4 cardinalities `54/52/28/132`, no blank span/hash/count, exactly six R2 `variant_of` rows, one `R1:U01` row, `Missing keys: none`, `Duplicate keys: none`, and `Ambiguous boundaries: none`.
  - **QA scenarios:** Happy — a second extraction reproduces all key sets, byte spans and hashes. Failure — a region terminator is crossed, a diagnostic/index heading is counted as a source unit, a variant is folded into its base, or any user/external block is truncated: stop and revise the parser rather than guessing. Evidence: source manifest.
  - **Commit:** N | source evidence only

- [x] 3. Reconciliation ledger: close the 266-source / 165-formal topology with complete dispositions
  - **What to do / Must NOT do:** Build the consolidation ledger from both manifests. Map every source row to a current representative target, `target-absent`, or a future anchor allowed only by `planned-new-formal`; map every formal row back to source keys or formal-only rationale. Fill all eight Phase 4 semantic axes before workflow fields and emit all eight reconciliation sets with declared overlap rules. Case 2 uses `source_relation=exact same quote`, `interpretation_relation=same insight`, `topology_relation=duplicate-of`, `action=merge-to-anchor`. Case 3 uses `exact same quote`, `corrected judgment`, paired `revision-before/revision-after`, and preserves both user wordings. Case 4 uses `same scene`, `same insight`, `many-to-one` to one readable scene anchor. Fixture Case 7 uses `external_reader_relation=独立精彩` and cannot become main user evidence; discarded external material uses `丢弃并说明理由` plus rationale. Bind every repair/new-card state to exact hunks and card identity/structure.
  - **Parallelization:** Wave 1 | Blocked by: 1,2 | Blocks: 4–10, F1–F5
  - **References:** both manifests; complete schema/state matrix in Scope; Phase 4 axes `87-136`, duplicate/revision rules `189-229`; fixture Cases 1–4 `5-96`; formal note `1-5930`.
  - **Acceptance criteria:** The ledger has 266 source rows, links all 165 baseline formal rows, and every row passes the eight-semantic-axis plus workflow matrix. Reconciliation emits exactly the eight named sets, proves the first four primary buckets are mutually exclusive, documents legal secondary overlaps, proves `N_new = count(planned-new-formal)`, and ends `unresolved=[]`. No blank enum, invented null, `missing-unbound`, illegal semantic/workflow/action combination or duplicate key is allowed.
  - **QA scenarios:** Happy — set subtraction is fully explained and a schema validator accepts every row, including `mapped-partial` repairs and `planned-new-formal` insertions. Failure — a source maps to multiple representative anchors, a formal card disappears, `preserve/index-only` lacks target evidence, a duplicate becomes a second card, a repair lacks a bound hunk, a new card lacks future anchor/insertion location, or any row is unresolved: mark FAIL and stop. Evidence: ledger plus reconciliation report.
  - **Commit:** N | internal evidence only

- [x] 4. Fixture and sentinel policy: produce deterministic results for all nine cases and seven regressions
  - **What to do / Must NOT do:** Apply each case in `.omo/evidence/fixtures/add-whole-book-consolidation-model.md` as a policy dry-run. Record input, expected source/archive/formal/index treatment, actual decision, evidence anchor or `policy-only`, forbidden outcome and PASS/FAIL. Separately build the seven-sentinel table from the Verification strategy using the pre-edit formal content and future readable anchor. Do not use former IDs as final reader-facing labels and do not edit the formal note.
  - **Parallelization:** Wave 2 | Blocked by: 3 | Blocks: 6–10, F1–F5 | Can parallelize with: 5
  - **References:** fixture `1-215`; Stage 4 fixture table `244-270`; formal sentinel locations identified during planning around `2367`, `2446`, `2661`, `2098`, `2139`, `4795`, `5010`; project literary rules in `AGENTS.md`.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-fixture-results.md` has exactly nine fixture rows and seven sentinel rows. All are PASS before Todo 6. Policy-only cases are explicitly labeled and cannot cause fabricated formal content. Every sentinel has an exact future readable anchor and before-state quotation.
  - **QA scenarios:** Happy — count nine distinct `Case 1`–`Case 9` results and seven named sentinel results, each with expected/actual/forbidden/PASS. Failure — any fixture silently overwrites an early reading, promotes a light card, duplicates a scene, or lets external-only material become main proof; reject the policy and stop. Evidence: `.omo/evidence/ren-sheng-whole-book-fixture-results.md`.
  - **Commit:** N | fixture/sentinel evidence only

- [x] 5. Anchor and structure design: assign unique readable anchors and a fixed appended-section blueprint
  - **What to do / Must NOT do:** Build one in-memory post-transform heading model by applying all 108 category/heading transforms plus every approved title-affecting repair/new-card hunk. Map **all 165 baseline formal cards plus every `planned-new-formal` row**, whether or not `article_links` is empty, to `第N轮 / post-transform当前分类标题 / 卡片标题`. Record pre-transform path, post-transform anchor and exact insertion target for every new card. Resolve collisions only by adding `章节或场景 / 引文短句（≤20字）`. Draft the exact appended outline. Define `阅读现场档案` as navigation/repair pointers only; define six article rows and six trajectories; reserve `待回看` for ledger-supported concise items. Do not use source IDs or move existing cards.
  - **Parallelization:** Wave 2 | Blocked by: 3 | Blocks: 6–10, F1–F5 | Can parallelize with: 4
  - **References:** Stage 4 formal structure `140-188`; duplicate/trajectory rules `189-229`; existing formal headings from `路遥/人生/《人生》阅读笔记.md`; approved anchor grammar in Scope.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-anchor-map.md` maps exactly `165 + N_new` post-transform cards, including all new cards with `article_links=none`; records pre/post paths and insertion targets; contains `Duplicate readable anchors: none`; and lists six article directions. Every article link and future anchor resolves once. The top-level section appears only after Round 4 with fixed children.
  - **QA scenarios:** Happy — independently rebuild the post-transform heading model and reproduce cardinality `165 + N_new`, insertion targets, anchor frequencies and article resolutions. Failure — a new card is omitted, a category uses its pre-transform technical heading, a collision remains, an index row needs an ID, or the blueprint copies a body: stop and revise the map. Evidence: anchor map.
  - **Commit:** N | anchor/structure evidence only

- [x] 6. Candidate composition: write the complete proposed transforms and full-book section in evidence before target edits
  - **What to do / Must NOT do:** Create `.omo/evidence/ren-sheng-whole-book-candidate-section.md` with three typed parts: (A) all 108 replacement rows, each with clearly separated `internal-before` and `target-after` fields; (B) exact ledger-approved repair/new-card fragments with separate `internal-before` and `target-after`, or `none`; (C) the complete target-bound `## 全书收束整合`. Raw technical tokens may appear only in the internal-before fields of Parts A/B. In `阅读现场档案`, include `轻卡存档 / 完整卡 / 核心卡 / 外部读者随卡补充`; each points to existing archive locations and ledger-proven repairs without copying card bodies. Write exactly six article-direction rows, six trajectory chains and concise pending/archive reasons. Do not edit the formal note.
  - **Parallelization:** Wave 3 | Blocked by: 1–5 | Blocks: 7–10, F1–F5
  - **References:** approved draft; preservation manifest; ledger; fixture results; anchor map; Stage 4 `127-188,216-242`; `AGENTS.md` for user voice, 五异法, question ladder and tension map.
  - **Acceptance criteria:** Candidate contains the four sections exactly once and in order; six article rows exactly; every article row has ≥3 unique anchors from ≥2 rounds when evidence exists, user phrase, tension, evidence and gap; every trajectory follows the five-field correction-chain structure; every repair fragment cites a ledger row; no full existing card body is copied.
  - **QA scenarios:** Happy — full read of candidate confirms it reads as archive navigation plus writing navigation, not as an essay or duplicated notebook. Failure — any target-bound row uses source coordinates, external-only main proof, copied card body, fabricated evidence, or AI wording in place of user text; reject the candidate before Todo 7. Evidence: `.omo/evidence/ren-sheng-whole-book-candidate-section.md`.
  - **Commit:** N | candidate evidence only

- [x] 7. Candidate gate: independently verify preservation, anchors, fixtures, sentinels and no-duplication before formal edit
  - **What to do / Must NOT do:** Review the candidate against both manifests, reconciliation, fixture results and anchor map. Apply all 108 transforms and every bound repair/new-card hunk in memory. Reparse the modeled-post result; require `165 + N_new` cards, resolve every anchor, verify every repair/new-card source and insertion point, and recompute current→modeled-post target-evidence relations. Every `missing-repair-approved` or `planned-by-approved-insertion` current relation must become an allowed satisfied modeled-post relation; `missing-unbound` is forbidden. Compare all six trajectories with original user text and later evidence. Scan **only target-bound fields**: Part A `target-after`, Part B `target-after`, and Part C. Report internal-before hits separately. Do not edit the formal note.
  - **Parallelization:** Wave 3 | Blocked by: 6 | Blocks: 8–10, F1–F5
  - **References:** Todos 1–6 evidence; fixture `1-215`; Stage 4 QA `244-270`; sentinel assertions in this plan.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-candidate-qa.md` reports `internal input hits: expected and confined to internal-before`, `target-bound forbidden hits: 0`, modeled-post card/anchor cardinality `165 + N_new`, every bound missing/planned relation satisfied, zero `missing-unbound`, zero unresolved/duplicate anchors, zero copied qualified card bodies, `unresolved=[]`, nine fixture PASS, seven sentinel PASS, six article-row PASS and six trajectory-chain PASS. Every repair/new card has source quotation and exact hunk.
  - **QA scenarios:** Happy — a second read-only reviewer can reproduce every PASS from cited text. Failure — any assertion depends only on worker self-report or a grep count; replace it with exact source/target excerpts before approval. Evidence: `.omo/evidence/ren-sheng-whole-book-candidate-qa.md`.
  - **Commit:** N | candidate QA only

- [x] 8. Controlled cleanup: remove technical tokens and apply only ledger-approved local archive repairs
  - **What to do / Must NOT do:** After Todo 7 PASS, edit only `路遥/人生/《人生》阅读笔记.md`. Apply the exact Todo 1 replacement list: remove source-ID labels while retaining human titles, preserve meaningful grouped-heading prose, and convert round/cursor coordinates to the fixed reader-facing wording. Apply only Todo 7-approved repair/new-card fragments. Preserve Round 1–4 order and every unaffected byte after approved transforms. Do not append the new full-book section yet; do not move/merge/delete existing cards.
  - **Parallelization:** Wave 4 | Blocked by: 7 | Blocks: 9,10,F1–F5
  - **References:** preservation manifest; candidate parts A/B; candidate QA; Stage 4 technical boundary `125,239-240,265`.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-metadata-cleanup.md` records all 108 rows applied exactly once with family counts `99/3/4/2`, coordinate hits `6`, overlap `4`, then zero target-surface hits. It records all 165 baseline-card checks; reparses `165 + N_new`; confirms all modeled-post evidence and prefix equality; and reports `Unapproved mismatches: none`. `.omo/evidence/ren-sheng-whole-book-archive-audit.md` fulfills approved brief C2 with one row per `165 + N_new` card containing archive disposition, card-structure class, pre/post anchor, preservation/repair/new-card provenance and article-link separation; it proves no qualified card moved, disappeared, duplicated or changed identity merely because of an article link.
  - **QA scenarios:** Happy — forbidden target regexes return zero, unaffected hashes and prefix equality pass, and archive audit cardinality/identity equals `165 + N_new`. Failure — a technical line remains, any unapproved byte changes, a new complete/core card lacks required four-part AI sections, a light card is forcibly expanded, or an article link changes archive identity: restore/reject the exact hunk and repeat both audits. Evidence: metadata-cleanup and archive-audit reports.
  - **Commit:** N | target edit, never stage

- [x] 9. Whole-book section: append archive navigation, six article indexes, six trajectories and pending/archive reasons
  - **What to do / Must NOT do:** Append the Todo 7-approved target-bound Part C after the cleaned Round 4 ending in `路遥/人生/《人生》阅读笔记.md`. Keep direct-child order fixed. Ensure archive subsection text points back to existing cards and only mentions repairs rather than copying bodies. Keep exactly six top-level article directions and approved character sublines. Use only unique readable anchors. Preserve the six correction chains and concise待回看/归档 reasons. Do not alter any transformed-prefix byte during this todo.
  - **Parallelization:** Wave 4 | Blocked by: 8 | Blocks: 10,F1–F5
  - **References:** approved candidate; anchor map; Stage 4 `140-188,216-242`; ledger article links and trajectory flags.
  - **Acceptance criteria:** `.omo/evidence/ren-sheng-whole-book-index-audit.md` shows four direct children exactly once/in order, six article directions exactly once, every index anchor resolves once, every row includes required fields, and no card body or article draft was copied. `.omo/evidence/ren-sheng-whole-book-trajectory-audit.md` verifies all six correction chains and original user wording.
  - **QA scenarios:** Happy — full read from `## 全书收束整合` to EOF confirms a compact navigation layer with exact evidence. Failure — an article row becomes prose draft, a trajectory silently replaces the early view, or a pending item exposes internal state; remove the violating text and repeat both audits. Evidence: the two audit files above.
  - **Commit:** N | target edit, never stage

- [x] 10. Final QA: prove source preservation, content quality, fixtures, sentinels, anchors and scope
  - **What to do / Must NOT do:** Read the complete final formal note. Recompute all content gates and immutable inputs; review the entire diff. Compare final NUL-safe status/diff hashes, filesystem inventory, `HEAD` OID and complete local refs to Todo 0. Run `git diff --check`; require cached diff empty and HEAD/refs unchanged. Do not fix by deleting evidence, shortening cards or touching baseline-unowned paths. Never run push; report it as an enforced prohibition, not post-state proof.
  - **Parallelization:** Wave 5 | Blocked by: 9 | Blocks: F1–F5
  - **References:** all Todo 0–9 evidence, including the brief-C2 archive audit; target formal note; this plan's Scope/Verification; root `AGENTS.md`.
  - **Acceptance criteria:** Final QA covers every Must Have/Must NOT Have; 266/165 baselines and `165 + N_new` final cards; all eight Phase 4 axes and eight reconciliation sets; modeled-post/archive C2 evidence; 108→0, prefix/suffix, section/article/trajectory/fixture/sentinel/content and baseline-relative Git gates. The invocation JSONL hash chain is valid; each required Todo 1–9 invocation has a latest PASS matching current stable artifacts plus its pinned formal phase; no current phase lacks PASS. Todo 10 closes final QA, then appends a valid PASS record bound to the prior JSONL prefix and final-QA hash. All rows must PASS, and F2 later revalidates that exact prefix-plus-record relation in check-only mode.
  - **QA scenarios:** Happy — independent verifiers can reproduce each PASS from exact files and excerpts. Failure — any source loss, forbidden field, unresolved anchor, scope leak, stale fixture/sentinel or reading-surface problem blocks completion and triggers the smallest targeted correction followed by a full rerun. Evidence: `.omo/evidence/final-ren-sheng-whole-book-consolidation-qa.md`.
  - **Commit:** N | staged state, HEAD and refs must remain unchanged; push is prohibited

## Final verification wave

> Runs only after Todo 10. The parent worker launches **five fresh Oracle sessions**, one per F item, with `task(subagent_type="oracle", run_in_background=false, load_skills=[], description="F# ...", prompt=<exact template below>)`. Omit both `category` and `task_id`; never continue a prior reviewer session. All are read-only and may use only read/search plus validator `--check-only` or read-only Git commands.

Reviewer receipt protocol:

Create a wave with these exact commands after Todo 10 and before any F task:

```bash
wave_id="$(python3 -c 'import uuid; print(uuid.uuid4())')"
python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-snapshot-create \
  --wave-id "$wave_id" \
  --plan .omo/plans/consolidate-ren-sheng-whole-book-notes.md \
  --brief .omo/drafts/consolidate-ren-sheng-whole-book-notes.md \
  --review-seal .omo/reviews/consolidate-ren-sheng-whole-book-notes-review-seal.json \
  --root-rules AGENTS.md \
  --router 路遥/人生/《人生》微信读书提示词.md \
  --phase4 路遥/人生/《人生》微信读书提示词-第四阶段-全书收束整合.md \
  --source 路遥/人生/《人生》中间整理稿.md \
  --formal 路遥/人生/《人生》阅读笔记.md \
  --evidence-root .omo/evidence \
  --out .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md
python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-snapshot-check \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --check-only
```

Before each F task (after the pre-task wave-snapshot-check passes), create a unique runtime attempt and `/tmp` baseline:

```bash
review_attempt_id="$(python3 -c 'import uuid; print(uuid.uuid4())')"
runtime_before="/tmp/ren-sheng-$wave_id-F#-$review_attempt_id-runtime-before.json"
python3 .omo/evidence/ren-sheng-whole-book-validator.py review-runtime-snapshot \
  --preflight .omo/evidence/ren-sheng-whole-book-preflight.md \
  --runtime-ledger .omo/evidence/ren-sheng-whole-book-review-runtime-paths.jsonl \
  --workspace . --wave-id "$wave_id" --reviewer F# \
  --attempt-id "$review_attempt_id" --out "$runtime_before"
```

The parent must retain `wave_id`, `review_attempt_id` and `runtime_before` across the task call. It launches the F task only after both wave-snapshot-check and review-runtime-snapshot return PASS.

The exact mandatory first paragraph of **every** F1–F5 Oracle prompt is: `WAVE_ID=<literal wave_id>. READ-ONLY. Read .omo/plans/consolidate-ren-sheng-whole-book-notes.md and .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md to EOF. Run python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-snapshot-check --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md --wave-id <literal wave_id> --check-only. Require exit 0, JSON status=PASS, state=ACTIVE and matching wave_input_set_sha256 before any other review step; otherwise return BLOCKED immediately.` The parent substitutes the literal UUID, then appends the row-specific prompt text below. Therefore every actual prompt contains the plan, snapshot path, wave ID and hash-check command.

Immediately **before each Oracle task call**, the parent runs the same `wave-snapshot-check`. If it exits nonzero with JSON `reason=INPUT_DRIFT`, do not launch the task; run the first drift block below, require invalidation PASS, end the wave and start no fix until invalidation is durable. Any other check error is a hard stop requiring inspection, not a reviewer result.

```bash
set -euo pipefail
check_json="$(mktemp)"
if ! python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-snapshot-check \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --check-only >"$check_json"; then
  test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["reason"])' "$check_json")" = "INPUT_DRIFT"
  python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-drift-invalidate \
    --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
    --wave-id "$wave_id" --trigger F#
  rm -f "$check_json"
  exit 1
fi
rm -f "$check_json"
```

After each task call, the parent serializes the returned tool result—not a paraphrase—to `/tmp/ren-sheng-<wave_id>-F#-<review_attempt_id>-result.json` with schema `{"transport_status":"COMPLETE|NO_RESULT","agent":"Oracle|<actual>","session_id":"<id-or-empty>","full_message":"<verbatim final message or empty>","tool_error":"<empty-or-verbatim>"}` and runs:

```bash
set -euo pipefail
result_json="/tmp/ren-sheng-$wave_id-F#-$review_attempt_id-result.json"
receipt_path=".omo/evidence/ren-sheng-whole-book-f#-<fixed-name>.md"
runtime_check_json="/tmp/ren-sheng-$wave_id-F#-$review_attempt_id-runtime-check.json"
if ! python3 .omo/evidence/ren-sheng-whole-book-validator.py review-runtime-register \
  --preflight .omo/evidence/ren-sheng-whole-book-preflight.md \
  --before "$runtime_before" --result-json "$result_json" \
  --workspace . --wave-id "$wave_id" --reviewer F# \
  --attempt-id "$review_attempt_id" \
  --ledger .omo/evidence/ren-sheng-whole-book-review-runtime-paths.jsonl \
  >"$runtime_check_json"; then
  test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["reason"])' "$runtime_check_json")" = "RUNTIME_PATH_DRIFT"
  python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-runtime-invalidate \
    --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
    --wave-id "$wave_id" --trigger F# --proof "$runtime_check_json" \
    --before "$runtime_before" --result-json "$result_json"
  exit 1
fi
runtime_attempt_id="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["runtime_attempt_id"])' "$runtime_check_json")"
python3 .omo/evidence/ren-sheng-whole-book-validator.py review-runtime-final-check \
  --preflight .omo/evidence/ren-sheng-whole-book-preflight.md \
  --ledger .omo/evidence/ren-sheng-whole-book-review-runtime-paths.jsonl \
  --workspace . --check-only
rm -f "$runtime_before" "$runtime_check_json"
postcheck_json="$(mktemp)"
if ! python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-snapshot-check \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --check-only >"$postcheck_json"; then
  test "$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["reason"])' "$postcheck_json")" = "INPUT_DRIFT"
  python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-drift-invalidate \
    --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
    --wave-id "$wave_id" --trigger F# --result-json "$result_json"
  rm -f "$postcheck_json" "$result_json"
  exit 1
fi
rm -f "$postcheck_json"
append_json="$(python3 .omo/evidence/ren-sheng-whole-book-validator.py review-receipt-append \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --reviewer F# \
  --runtime-ledger .omo/evidence/ren-sheng-whole-book-review-runtime-paths.jsonl \
  --runtime-attempt-id "$runtime_attempt_id" \
  --runtime-preflight .omo/evidence/ren-sheng-whole-book-preflight.md \
  --runtime-workspace . \
  --result-json "$result_json" \
  --out "$receipt_path")"
test "$(python3 -c 'import json,sys; print(json.loads(sys.argv[1])["status"])' "$append_json")" = "PASS"
attempt_id="$(python3 -c 'import json,sys; print(json.loads(sys.argv[1])["attempt_id"])' "$append_json")"
message_hash="$(python3 -c 'import json,sys; print(json.loads(sys.argv[1])["message_hash"])' "$append_json")"
python3 .omo/evidence/ren-sheng-whole-book-validator.py review-receipt-check \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --reviewer F# --receipt "$receipt_path" \
  --attempt-id "$attempt_id" --message-hash "$message_hash" --check-only
rm -f "$result_json"
```

Replace `F#` and output with the table's exact reviewer/receipt before running the block. `review-receipt-append` stores `schema_version`, `wave_id`, reviewer, attempt UUID/time, session ID, transport state, first-line verdict, full verbatim message/error, message hash and current `wave_input_set_sha256`. A valid COMPLETE Oracle result retains its verdict; wrong agent metadata, timeout, active-gate rejection, missing final message or transport error is atomically recorded as `NO_RESULT` with the actual metadata/error rather than rejected. Malformed JSON or snapshot mismatch exits nonzero before append. Because the strict block checks append JSON and `review-receipt-check`, it deletes the temporary result only after durable receipt verification; any failure stops with the temporary file preserved. A recorded NO_RESULT authorizes a fresh same-F retry only while snapshot-check still passes. For a complete `BLOCKED`, append/check the receipt, then invalidate before any fix:

Fixed receipt mapping is literal: `F1=ren-sheng-whole-book-f1-plan-compliance.md`, `F2=ren-sheng-whole-book-f2-preservation.md`, `F3=ren-sheng-whole-book-f3-reading-surface.md`, `F4=ren-sheng-whole-book-f4-fixture-anchor.md`, `F5=ren-sheng-whole-book-f5-scope-git.md`, all under `.omo/evidence/`. No other output name is permitted.

```bash
python3 .omo/evidence/ren-sheng-whole-book-validator.py wave-invalidate \
  --snapshot .omo/evidence/ren-sheng-whole-book-final-wave-inputs.md \
  --wave-id "$wave_id" --reviewer F# \
  --receipt .omo/evidence/ren-sheng-whole-book-f#-<fixed-name>.md \
  --reason BLOCKED
```

1. The Oracle must read every listed input to EOF, execute the listed read-only steps, and return a final message whose first non-whitespace line is exactly `APPROVED` or `BLOCKED`.
2. Before F1, snapshot every reviewer input named in the F1–F5 table plus plan, approved brief, governing files, source and final formal note. Validator invocation JSONL is mandatory. Only F1–F5 receipts, review-runtime ledger and snapshot itself are excluded from the hashed input set. While ACTIVE, only current-wave receipt files and runtime ledger may append; all reviewer inputs are immutable. Snapshot mutation ends the active wave and is allowed only through exactly one proven transition: `INPUT_DRIFT` via wave-drift-invalidate, `RUNTIME_PATH_DRIFT` via wave-runtime-invalidate, or stable-input/runtime reviewer `BLOCKED` via checked receipt plus wave-invalidate. All other snapshot writes/no-receipt invalidations fail.
3. Thinking-only output, API/transport failure, active-gate rejection, timeout, missing final message or wrong agent metadata is `NO RESULT`. With zero new runtime node, review-runtime-register must create a `zero-node-no-result` row even when session ID is empty; with a real returned session/node it registers the exact node first. The checked NO_RESULT receipt then permits a fresh same-F retry while wave inputs still match.
4. Input drift is not a reviewer verdict. A pre-task drift skips the task; a post-task drift serializes the returned result as invalidated-wave context and uses `wave-drift-invalidate` without requiring a receipt. Only after durable drift invalidation may the worker diagnose/fix inputs, rerun the responsible Todo/Todo 10, create a new wave and restart all F items.
5. `APPROVED` is valid only when every condition is evidenced. Any caveat, conditional language or non-drift `BLOCKED` immediately ends the wave: first append/check the BLOCKED receipt, then run regular `wave-invalidate`, then—and only then—fix, rerun the responsible Todo and Todo 10, create a new wave and rerun **all F1–F5 from fresh sessions**.
6. The five final receipt files must each end with a latest unconditional `APPROVED` under the same non-invalidated `wave_id`. Do not modify final QA or reviewer inputs after that wave starts; the handoff cites receipts/session IDs directly. Reviewer approval never authorizes commit/push.

| F | exact fresh-task prompt, inputs and read-only steps | unconditional APPROVED condition | receipt |
|---|---|---|---|
| F1 | Prompt suffix after the mandatory wave paragraph: `READ-ONLY F1 plan-compliance audit. Read approved draft, review seal, root AGENTS, router, Phase 4 prompt, final formal note and final QA to EOF. Validate seal/control hashes and all three plan approvals. Crosswalk every Must Have/Must NOT Have and Todo 0-10 acceptance row to exact final evidence; verify append-not-restructure, no global Stage 3 rerun, fixed sections/directions/trajectories and no execution/Git overreach. Return APPROVED or BLOCKED with cited paths/lines.` | Seal and every scope/structure/policy row have exact evidence with no contradiction or out-of-scope change. | `.omo/evidence/ren-sheng-whole-book-f1-plan-compliance.md` |
| F2 | Prompt suffix after the mandatory wave paragraph: `READ-ONLY F2 preservation/archive audit. Read baseline copy, source/formal manifests, ledger, reconciliation, technical inventory, candidate, metadata cleanup, archive audit, final note and final QA to EOF. Run validator tests and final-check --check-only; independently sample every changed hunk and all user/quote/external block classes. Verify 266, 165, 165+N_new, eight semantic axes, card-body classes, prefix equality and no article-link identity change. Return APPROVED or BLOCKED.` Exact commands: `python3 .omo/evidence/ren-sheng-whole-book-validator-tests.py`; `python3 .omo/evidence/ren-sheng-whole-book-validator.py final-check --formal 路遥/人生/《人生》阅读笔记.md --evidence-root .omo/evidence --preflight .omo/evidence/ren-sheng-whole-book-preflight.md --check-only`. | Both commands exit 0/status PASS; all baseline and final cardinalities, hashes, exact hunks, archive identities/body structures and user/external blocks pass. | `.omo/evidence/ren-sheng-whole-book-f2-preservation.md` |
| F3 | Prompt suffix after the mandatory wave paragraph: `READ-ONLY F3 Chinese reading-surface audit. Read root AGENTS, complete final formal note, archive audit, index audit and trajectory audit to EOF. Evaluate the full note—not grep excerpts—using 五异法、问题阶梯、张力地图、轻卡/主卡与细节卡/主题卡 rules. Verify living user voice, textual landing after elegant claims, light-card restraint, external-reader labels/subordination, no copied cards, no essay draft, and useful retrieval. Return APPROVED or BLOCKED with exact quotations and anchors.` | Whole-note literary QA passes every named project rule; no flattening, AI overwrite, unsupported concept, forced promotion, duplication or external-reader takeover. | `.omo/evidence/ren-sheng-whole-book-f3-reading-surface.md` |
| F4 | Prompt suffix after the mandatory wave paragraph: `READ-ONLY F4 fixture/sentinel/anchor audit. Read fixture, fixture results, ledger, reconciliation, technical inventory, anchor map, candidate QA, final note and final QA to EOF. Run policy-check --check-only and final-anchor-check --check-only. Re-evaluate all nine cases, seven sentinels and every 165+N_new final anchor, including article_links=none. Return APPROVED or BLOCKED.` Exact commands: `python3 .omo/evidence/ren-sheng-whole-book-validator.py policy-check --fixture .omo/evidence/fixtures/add-whole-book-consolidation-model.md --results .omo/evidence/ren-sheng-whole-book-fixture-results.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --formal-manifest .omo/evidence/ren-sheng-whole-book-preservation-manifest.md --check-only`; `python3 .omo/evidence/ren-sheng-whole-book-validator.py final-anchor-check --formal 路遥/人生/《人生》阅读笔记.md --ledger .omo/evidence/ren-sheng-whole-book-consolidation-ledger.md --anchor-map .omo/evidence/ren-sheng-whole-book-anchor-map.md --check-only`. | Commands exit 0/status PASS; 9/7 semantic assertions and actual final `165 + N_new` anchors pass; no technical/pre-transform labels, duplicate/unresolved anchors or invented interpretation. | `.omo/evidence/ren-sheng-whole-book-f4-fixture-anchor.md` |
| F5 | Prompt suffix after the mandatory wave paragraph: `READ-ONLY F5 scope/Git audit. Read preflight, runtime ledger, allowlist and final QA. Confirm ordinary delta equals allowed_changed_paths; baseline paths/HEAD/refs are unchanged; execution-runtime follows only absent→regular or regular→regular at its exact session path; all prior reviewer rows remain exact. List post-F5-launch continuation delta separately for the parent gate. Treat push as prohibited, not inferable. Return APPROVED or BLOCKED.` Commands: `GIT_MASTER=1 git status --porcelain=v1 -z --branch --untracked-files=all`; `GIT_MASTER=1 git diff --binary`; `GIT_MASTER=1 git diff --cached --binary`; `GIT_MASTER=1 git diff --check`; `GIT_MASTER=1 git rev-parse HEAD`; `GIT_MASTER=1 git show-ref --head`. | Ordinary paths/prior reviewer paths exact; execution-runtime state transition/path/type legal; HEAD/refs/staged/diff pass. Current F5 path must pass parent registration before receipt. | `.omo/evidence/ren-sheng-whole-book-f5-scope-git.md` |

- [x] **F1. Plan compliance audit:** invoke the F1 task exactly; save a valid unconditional receipt.
- [x] **F2. Preservation and archive-identity audit:** invoke the F2 task exactly; save a valid unconditional receipt.
- [x] **F3. Reading-surface QA:** invoke the F3 task exactly; save a valid unconditional receipt.
- [x] **F4. Fixture/sentinel/anchor audit:** invoke the F4 task exactly; save a valid unconditional receipt.
- [x] **F5. Scope and Git audit:** invoke the F5 task exactly; save a valid unconditional receipt.

## Commit strategy

- Do not stage or commit during execution.
- Do not push.
- Preserve every preflight dirty/untracked path exactly as found, including `.omo/run-continuation/ses_0a00ec516ffewmDIxM2zMRTrXV.json` and session-generated continuation files.
- If the user later asks for Git work, that is a separate task requiring `shared/git-master`; every Git command must use `GIT_MASTER=1`, and staging must be limited to files the user explicitly names.

## Success criteria

- Explicit worker authorization and all Stage 4 gates pass before content mutation.
- The external review seal's canonical payload, current plan/draft hashes and unconditional Metis/Momus/Oracle receipts validate exactly; sealed plan/draft bytes remain unchanged throughout execution.
- The existing four-round archive stays in the same order; no qualified card is moved, duplicated, deleted or globally rewritten.
- All 266 source units are resolved exactly once with counts `54/52/28/132`; all 165 baseline formal cards have preservation rows with counts `20/31/15/99`; every ledger row preserves all eight Phase 4 semantic axes separately from workflow/topology/action; all eight reconciliation sets obey the primary/secondary overlap rules and `unresolved=[]`.
- The complete 108-line technical baseline (`99 unspaced + 3 spaced + 4 metadata + 2 coordinate-only`, with six coordinate hits/four overlaps) becomes zero on the target surface with no reader-visible exception; source traceability remains internal.
- Every unaffected card's normalized pre/post hash matches; every allowed mismatch is a cited exact repair hunk; the full transformed prefix passes byte equality and the new section is suffix-only.
- All `165 + N_new` post-transform readable anchors are unique—including new cards with no article links—and all article links resolve to exactly one formal card without source IDs or coordinates.
- All `165 + N_new` cards have one legal archive identity and required class-specific body structure; article links never silently promote, demote or replace that identity; approved brief C2 is evidenced by the archive-audit artifact.
- One `## 全书收束整合` exists after Round 4 with the four required child sections exactly once and in order.
- The article index contains exactly six top-level directions, preserves user phrases, names textual tensions and evidence gaps, and neither copies cards nor drafts essays.
- The six specified reading trajectories preserve early wording, later evidence, corrected judgment, misreading value and article-index use.
- All nine fixture cases and seven fixed sentinels pass after source IDs are removed.
- External-reader material remains labeled and subordinate; external-only material never becomes user evidence.
- `划线原文`、`我自己写的内容/我的原想法` and living Chinese prose remain intact; AI修正 never overwrites the user.
- Full read-back passes literary-quality QA under `AGENTS.md`.
- In the final single non-invalidated `wave_id`, F1–F5 each have a latest valid fresh-Oracle receipt ending in unconditional `APPROVED`, and that wave's reviewer inputs did not change between snapshot closure and its final approval. Receipts from older invalidated waves do not participate in success.
- Ordinary changed paths are exactly target plus evidence. Reviewer runtime paths are authenticated/frozen; execution-runtime follows only exact absent→regular or regular→regular state with mutable hash. No broad continuation glob exists. All other pre-existing paths, staged state, HEAD and refs remain at preflight. Push is prohibited but not claimed as post-state proof.
