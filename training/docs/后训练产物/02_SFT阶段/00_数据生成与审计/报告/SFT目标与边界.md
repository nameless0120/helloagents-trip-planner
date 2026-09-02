# Planner SFT 目标与边界

更新时间：2026-05-06

这份文档用来固定 Planner 阶段 SFT 的训练目标、非目标和验收边界。它和这些文档配合使用：

- `training/docs/内部文档/Prompt消融阶段总结.md`：说明 prompt-only 已接近上限，冻结 `A_C` baseline。
- `training/docs/内部文档/SFT数据生成口径审核.md`：说明请求分布、字段口径、清洗和生成后处理。
- `training/docs/内部文档/评测指标.md`：说明完整评测指标分层。

一句话结论：

**Planner SFT 的目标是把模型训成可靠的结构化 Planner 输出器，而不是一次性训成最优旅行顾问。**

## 1. 背景判断

Prompt 消融阶段已经证明：

- prompt 能讲清楚字段语义、候选来源、价格 hint 和预算口径。
- prompt 不能稳定解决长 JSON 内部的跨字段算术和全局组合优化。
- 继续堆 prompt 会带来约束淹没：某些局部指标提升，其他硬约束下降。
- 预算精确加总、餐饮多样性、路线顺滑和体验质量不能全部压给 SFT 第一阶段。

因此 Planner 后训练要分工：

- SFT 学协议、格式、字段语义、grounding 和基础约束。
- 工程后处理负责确定性预算重算和可规则化修正。
- 预算贴合放到推理时修正：模型可以输出修正 patch，但是否接受由工程侧重算预算和规则验收决定。
- DPO 或 reranker 学软偏好、路线质量、体验质量和预算贴合审美。

## 2. SFT 主要目标

给定 `PlannerContext planner`，模型应该稳定输出一个后端可解析、可重算、可验证的 `TripPlan` JSON。

SFT 重点学习：

1. **输出协议**
   - 只输出 JSON 对象。
   - 不输出 Markdown、代码块、解释、前言、后记或 `<think>`。
   - 字段结构符合 `TripPlan` schema。

2. **行程结构完整性**
   - `city/start_date/end_date/days/weather_info/budget` 完整。
   - `days` 数量等于 `request.travel_days`。
   - 每天 `day_index/date` 正确。
   - 每天 `attractions` 为 1-3 个，不能用休息、自由活动、返程替代景点。
   - 每天都有 `breakfast/lunch/dinner`，包括最后一天。

3. **字段语义**
   - `day.accommodation` 每天固定等于用户请求住宿类型。
   - 中间住宿日 `day.hotel` 不能为空。
   - 单城多日行程默认连续入住同一家酒店，中间住宿日 `day.hotel` 不能变化。
   - 最后一天如果离城，可以 `hotel = null`。
   - 最后一天如果继续入住，也应沿用同一家酒店。
   - `hotel.distance` 在没有真实路线工具时必须是空字符串。
   - `location` 必须是对象，不是字符串。

4. **工具 grounding**
   - 景点优先来自 `classic_pois/preference_pois/scenic_pois/experience_pois`。
   - 中间住宿日酒店来自 `hotel_pois`。
   - lunch/dinner 必须来自 `food_pois`。
   - breakfast 优先来自 `food_breakfast` 或 `meal_roles` 含 breakfast 的 `food_pois`；住宿早餐只作为合理 fallback。
   - food_pois 候选充足时，lunch/dinner 不能重复同一餐厅名。
   - 不编造候选里没有的精确 POI、坐标、地址、价格或距离。

5. **价格单位和人数关系**
   - `hotel.estimated_cost` 是单间每晚价，复制 `hotel_pois.estimated_cost_hint`。
   - `attraction.ticket_price` 是成人单人票价，复制 `ticket_price_hint`。
   - `meal.estimated_cost` 是单人单餐价，复制 `food_pois.meal_cost_hint`。
   - 酒店总价按 `rooms = ceil(party.total / 2)`。
   - 景点总价按 `sum(ticket_price) * party.total`。
   - 餐饮总价按 `sum(meal.estimated_cost) * party.total`。

6. **基础约束遵守**
   - 遵守明确负向约束，例如清真、海鲜过敏、少辣、老人友好、亲子、省力等。
   - 不使用餐饮占位词，例如“附近餐厅”“特色餐厅”“本地早餐”“酒店晚餐”“无”。
   - `overall_suggestions` 不能和 `budget.total` 或用户预算关系矛盾。

## 3. SFT 非目标

这些能力不作为 Planner SFT 第一阶段的主胜利条件：

| 能力 | 不放进 SFT 主目标的原因 | 后续归属 |
| --- | --- | --- |
| 预算精确算术由模型原生完成 | 长 JSON 跨字段乘人数/房间数不稳定，SFT 后仍未解决，属于模型能力上限 | 工程重算 + 诊断指标 |
| soft budget 精准贴合用户金额 | 和候选价格、人数、住宿、家庭场景强耦合，容易造成掉样本 | 后处理、候选策略、DPO |
| 餐饮多样性最优 | 强去重规则会伤害 grounding 和 schema，且是体验偏好 | DPO、reranker、规则 |
| 路线顺滑/少绕路最优 | 当前无真实 route API，模型只能用 district/address/location 粗排 | route 工具、reranker、DPO |
| 景点体验质量最优 | 属于偏好排序和审美判断，不是协议学习 | DPO、人工偏好数据 |
| 行程风格特别自然、文案漂亮 | 会和 JSON 稳定性、字段约束争 token 和注意力 | DPO 或后期润色 |

## 4. 指标分层

### P0：SFT 必须硬过

P0 是 SFT 数据清洗和训练后验收的主目标。

- JSON 可解析，schema 通过。
- 城市、日期、天数、`day_index` 正确。
- `weather_info` 覆盖每一天，只使用 `trip_weather`。
- 每天 1-3 个景点。
- 每天三餐完整，包括返程日 dinner。
- `day.accommodation == request.accommodation`。
- 中间住宿日 `hotel != null`。
- 中间住宿日酒店必须和第 1 晚同一家，不能每天换酒店。
- 最后一天 `hotel` 可为 null，但不能写成“无住宿/返程”酒店。
- 景点、酒店、lunch/dinner grounding 正确。
- lunch/dinner 不是酒店名、不是泛化名、不是占位词。
- price hint 复制正确，且所选酒店/景点/餐饮可由工程侧回填价格。
- 酒店、景点、餐饮的人数/房间数关系作为预算语义观察项，不再要求模型原生精确加总。
- `budget.total` 等于四项分项之和属于兼容 schema 的诊断项；线上最终预算由工程侧重算。
- `overall_suggestions` 不出现预算金额或预算关系矛盾。

### P1：SFT 尽量学习，但不因单点失败扩大目标

P1 可以作为数据质量观察项，也可以适度过滤明显脏样本，但不应该让它主导数据生成失败率。

- soft budget 大体合理。
- 交通预算非负且量级正常。
- 餐饮价格尺度不明显异常。
- 景点和餐饮有基础多样性。
- 同一天 lunch/dinner 餐厅名不重复。
- 遵守节奏偏好，例如慢节奏不要每天 3 个高强度点。
- 亲子/老人场景避免明显不友好安排。

### P2：交给 DPO/规则/后处理

P2 不作为 SFT 主验收项。

- 餐厅全程去重最优。
- 菜系多样性最优。
- 景点组合体验最优。
- 路线最顺滑。
- 预算贴合用户金额最漂亮。
- 总体建议文案自然度。
- 取舍偏好，例如“少花钱但体验弱一点”还是“略超预算但体验更好”。

## 5. 预算目标边界

预算在 Planner 里分三层处理：

1. **结构账本必须正确**
   - 为兼容当前 `TripPlan` schema，SFT 数据可以保留经过工程重算的正确 `budget`。
   - 但训练后验收不再把模型原生预算精确加总作为主 hard pass。
   - 模型主要学习价格字段口径：酒店单间每晚价、景点成人单人票、餐饮单人人均价。

2. **用户 hard budget 不能明显违反**
   - `strictness=hard` 时，最终工程重算预算应尽量不超过 `amount`。
   - 模型选择的候选若重算后超预算，应进入推理时 patch/repair，而不是指望模型自报 budget 修正。
   - 若候选价格和人数导致自然成本很难压低，请优先在请求生成侧避免制造不现实 hard budget。

3. **soft budget 贴合不作为 SFT 主瓶颈**
   - `strictness=soft` 可以允许一定上下浮动。
   - 不应为了追求 soft budget target range，牺牲 grounding、三餐、住宿或字段语义。
   - 大规模生成时建议把 soft budget 失败作为观察/抽检项，而不是第一阶段主硬闸。
   - 预算利用型补数进入 teacher 前应先做 context gate：候选池估算上限至少能达到用户预算 100%。
   - 高端酒店、高端餐饮和高价体验候选不足已记录到根目录 `TODO.md`，不在当前 SFT 阶段用模型硬学弥补。

2026-05-06 二次修正实验补充：

- 让模型第二次重写完整 `TripPlan` 不可取，会破坏 schema、字段完整性和 grounding。
- 更可控的做法是让第二次模型只输出预算修正 patch，例如 `replace_hotel / replace_meal / replace_attraction`。
- 工程侧应用 patch 后必须重新计算预算和规则指标；只有预算变好且已通过的 schema、grounding、多样性等指标不回退，才接受 patch。
- 在 A_C 300 条上，guarded patch 对 SFT cp2 的 `budget_selection_ok` 从 28.33% 提升到 30.33%，`planner_draft_hard_pass` 保持 63.00%。
- 这说明二次模型 patch 是保守增强层，不是预算贴合主解；预算主解仍应是工程重算、候选 rerank 和 deterministic repair。

## 6. 数据生成验收口径

Planner SFT 样本进入训练集前，至少应满足：

- P0 全部通过。
- 预算字段经过工程重算。
- 中间住宿日酒店连续稳定，不把同城多日行程写成每天换酒店。
- 原始强模型输出中的坏 JSON 不做本地宽松修复。
- 失败样本写入 `errors.jsonl`，不通过修 JSON 或补字段洗白。
- `overall_suggestions` 不复述一个与 `budget.total` 冲突的总费用。
- 旧 prompt/hash 的 smoke 数据必须归档，不能和当前 baseline 混入同一个训练文件。

不建议在第一阶段强制：

- soft budget 必须落在 target_min/target_max。
- 餐饮多样性必须达到 DPO soft pass。
- 路线质量必须达到人工满意级别。

## 7. 训练后验收建议

微调后建议分三张表看，不要只看一个总 hard pass：

1. **协议硬表**
   - schema/date/weather/day/hotel/meals/attractions/location。
   - 这是 SFT 是否成功的第一判断。

2. **grounding 与预算语义表**
   - POI grounding。
   - price hint 复制。
   - 酒店房间数、景点人数、餐饮人数关系。
   - budget 四项加总。

3. **软质量观察表**
   - 餐饮多样性。
   - 路线顺滑。
   - 景点体验。
   - budget preference fit。
   - 总体建议自然度。

如果 SFT 后 P0/P1 明显提升，而 P2 没有明显提升，这是可以接受的；P2 本来就不是 SFT 第一阶段的目标。

## 8. 当前 smoke 的启示

最近一轮 smoke20 使用 `DATA_GEN_THINKING=false`、20 workers、新 max_tokens 后：

- JSON 截断/解析不再是主要问题。
- 结构、grounding、预算重算后的成功样本可以做到干净。
- 主要掉样本来自 budget target range，尤其 limited/standard 与多人/家庭场景。
- `overall_suggestions` 曾出现口头预算和 `budget.total` 不一致，已加入清洗校验。

所以下一步不要继续堆 prompt，先做这些事：

- 实现目标成功数补齐生成逻辑。
- 降低 soft budget target range 对 SFT 造数的阻塞。
- 保持 P0 清洗严格。
- 把 P2 质量留给 DPO、规则和后处理。

## 9. 最终定义

Planner SFT 成功的定义：

**模型学会 TripPlan 协议和 PlannerContext grounding，能稳定输出结构完整、字段语义正确、价格口径正确、预算账本可重算的 JSON。**

Planner SFT 不承诺：

**一次性学会最优路线、最优餐饮多样性、最佳预算贴合和最自然旅行审美。**

这个边界后续不要轻易扩大。某个指标如果属于偏好排序、体验审美或全局优化，默认先进入 DPO、规则或后处理池，不要继续塞进 SFT 主目标。
