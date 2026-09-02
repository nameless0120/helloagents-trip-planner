# Planner SFT 数据生成口径审核

这份文档在正式造 Planner SFT 数据前使用，用来对齐三件事：请求分布、Planner 生成 prompt、评测/清洗口径。

## 1. 当前结论

当前 Planner SFT 数据生成可以进入 smoke 阶段，但必须坚持这些口径：

- 请求端预算是整趟总预算。
- 酒店 `hotel.estimated_cost` 表示单房每晚价。
- 房间数 `rooms = ceil(party.total / 2)`。
- 单城多日行程默认连续入住同一家酒店，中间住宿日 `day.hotel` 不能变化。
- 酒店预算 `total_hotels = sum(non_null_day.hotel.estimated_cost) * rooms`。
- 景点 `ticket_price` 表示成人单人票价。
- 景点预算 `total_attractions = sum(ticket_price) * party.total`。
- 餐饮 `meal.estimated_cost` 表示单人单餐价。
- 餐饮预算 `total_meals = sum(meal.estimated_cost) * party.total`。
- `budget.total = total_attractions + total_hotels + total_meals + total_transportation`。
- 精确预算加总由数据生成后处理重算，不能把强模型算术错误写进 SFT。

## 2. 请求分布

来源：`training/scripts/planner/data/generate_sft_data.py` controlled request。

### 同行类型

| 类型 | 权重 | 说明 |
| --- | ---: | --- |
| friends | 22 | 2-4 个成人朋友 |
| couple | 20 | 2 个成人 |
| solo | 15 | 1 人 |
| family_with_children | 18 | 2 成人 + 1/2 孩子 |
| family_with_elders | 10 | 1/2 成人 + 1/2 老人 |
| family_mixed | 7 | 2 成人 + 1/2 孩子 + 1/2 老人，三代同游 |
| business | 4 | 1-3 成人商务/同事 |
| other | 4 | 其他轻量场景 |

说明：`family_mixed` 已进入普通 SFT 分布，不只存在于 harder eval。

### 城市层级

| 层级 | 权重 | 城市示例 |
| --- | ---: | --- |
| major | 35 | 北京、上海、广州、深圳、成都、杭州、重庆、西安 |
| popular | 40 | 南京、苏州、厦门、青岛、长沙、武汉、昆明、大理等 |
| long_tail | 25 | 珠海、福州、泉州、洛阳、扬州、黄山、张家界等 |

### 天数与日期

| 字段 | 分布 |
| --- | --- |
| travel_days | 2天 18%，3天 42%，4天 28%，5天 12% |
| date_bucket | 历史 30%，近未来 30%，远未来 40% |

说明：暂不加入 6 天，保持当前 2-5 天口径。

### 预算档位

| 档位 | 权重 | 人均日非住宿预算候选 |
| --- | ---: | --- |
| limited | 25 | 140 / 180 / 220 |
| standard | 40 | 220 / 260 / 300 |
| comfortable | 23 | 360 / 450 / 550 |
| premium | 9 | 700 / 850 / 1000 |
| luxury | 3 | 1300 / 1700 / 2200 |

请求预算公式：

```text
party_total = max(party.total, 1)
lodging_nights = max(travel_days - 1, 0)
rooms = ceil(party_total / 2)
daily_total = per_person_day * party_total * travel_days * transportation_factor
lodging_total = lodging_per_night_by_accommodation * lodging_nights * rooms
budget_amount = round_to_100((daily_total + lodging_total) * city_factor)
```

这已经和评测里的酒店两人一间口径一致。

### 住宿与交通

住宿由预算档位和同行类型共同决定：

- 亲子：更偏亲子酒店/舒适型酒店。
- 三代同游：更偏舒适型酒店/亲子酒店。
- limited：更偏经济型酒店/民宿。
- premium/luxury：更偏高端酒店。

交通由城市和同行类型共同决定：

- 家庭/老人/三代：更偏打车。
- 商务：更偏打车。
- 地铁城市：更偏地铁+步行。
- 大理/丽江/桂林/三亚/张家界/黄山：提高自驾和打车比例。

### 偏好和约束

正向偏好来自主题池：美食、历史文化、自然风光、城市公园、休闲慢游、城市地标、第一次来、摄影、城市漫步、购物商圈、主题乐园、户外轻徒步、夜市夜景、小众展览、艺术、海滨度假。

负向约束来自 avoid 和饮食解析：

- 海鲜过敏 -> `diet_avoid = [海鲜]`
- 清真 -> `diet_avoid = [猪肉, 酒]`
- 素食 -> `diet_avoid = [荤菜]`
- 少辣 -> `diet_avoid = [重辣]`
- 清淡饮食 -> `diet_avoid = [重口味]`

`family_with_children` 自动补 `亲子`；`family_with_elders` 自动补 `老人友好`；`family_mixed` 自动补 `亲子 + 老人友好`。

### 餐饮候选召回

餐饮候选来自 `food_query_groups` 分桶召回。当前主线不使用 topk context；`compact_for_planner` 只裁字段，不裁剪 `food_pois` 数量。

- `food_base` 是兜底餐饮池，默认返回 20 个候选。
- `food_breakfast` 是早餐池，默认返回 8 个候选，关键词覆盖早餐/早点/早茶/包子/粥/面馆/糕点/咖啡；有明确饮食约束时会优先尝试“清真早餐”等约束早餐。
- 其他餐饮分桶默认返回 8 个候选。
- 合并后的 `food_pois` 总上限默认是 40。
- 普通朋友/情侣/独行等请求即使没有明确餐饮偏好，也至少应包含 `food_breakfast` + `food_base` 两个分桶，分别覆盖早餐和 3-5 天 lunch/dinner 候选余量。

## 3. Planner 生成 Prompt 口径

来源：`backend/app/agents/prompts.py::PLANNER_AGENT_PROMPT`。

和评测强相关的硬要求：

- 只输出 JSON 对象，不输出 Markdown、代码块、解释或 `<think>`。
- `weather_info` 必须覆盖每一天，只能用 `trip_weather`。
- 每天 `attractions` 必须 1-3 个，优先从候选池选，不用休息/自由活动/返程替代景点。
- `day.accommodation` 每天都固定填用户住宿类型，包括返程日。
- 中间住宿日 `day.hotel` 必须从 `hotel_pois` 选真实酒店。
- 中间住宿日必须沿用同一家酒店，不能第 1 晚住 A、第 2 晚住 B。
- 返程日可以 `hotel=null`。
- `hotel.distance` 必须是空字符串 `""`，不能编造伪距离。
- 每天必须有 breakfast/lunch/dinner，包括返程日 dinner。
- lunch/dinner 必须从 `food_pois` 复制真实餐厅，不允许“无/推荐/酒店晚餐/附近餐厅”等占位。
- breakfast 优先来自 `food_breakfast` 或 `meal_roles` 含 breakfast 的 `food_pois`；住宿早餐只作为合理 fallback。
- food_pois 候选充足时，整趟 lunch/dinner 不能重复同一餐厅名。
- 价格字段必须复制候选 hint：
  - `hotel.estimated_cost` = `hotel_pois.estimated_cost_hint`，单房每晚价。
  - `attraction.ticket_price` = `ticket_price_hint`，成人单人票价。
  - `meal.estimated_cost` = `food_pois.meal_cost_hint` 或餐别 fallback，单人单餐价。
- 酒店总价按 `ceil(party.total / 2)` 房间数计算。
- 景点总价按 `ticket_price * party.total`。
- 餐饮总价按 `meal.estimated_cost * party.total`。
- `budget.total` 由四项分项重新加总。

## 4. SFT 生成后处理

来源：`training/scripts/planner/data/generate_sft_data.py::recompute_budget`。

强模型输出通过 schema 后，会被重新计算预算：

```text
room_count = ceil(party.total / 2)
total_hotels = sum(day.hotel.estimated_cost) * room_count
total_attractions = sum(attraction.ticket_price) * party.total
total_meals = sum(meal.estimated_cost) * party.total
total = total_hotels + total_attractions + total_meals + total_transportation
```

这一步保证训练目标不会学习强模型的算术错误。

## 5. SFT 训练样本校验

来源：`training/scripts/planner/data/generate_sft_data.py::validate_training_plan`。

当前训练样本必须通过：

- 有 budget。
- `budget.total` 等于四个分项之和。
- 每天 `accommodation == request.accommodation`。
- 每天景点数 1-3。
- 住宿晚数范围内 hotel 不为空。
- 中间住宿日 hotel.name 必须和第 1 晚一致。
- 酒店价格匹配候选 hint。
- 景点票价匹配候选 hint。
- `budget.total_hotels` 按两人一间汇总。
- `budget.total_attractions` 按 party.total 汇总。
- `budget.total_meals` 按 party.total 汇总人均餐费。
- 预算总额符合 `budget_fit_policy`，允许少量 margin。

## 6. 评测指标对齐

来源：`training/scripts/eval/eval_rule_metrics.py` 与 `training/docs/内部文档/评测指标.md`。

SFT 严格 hard pass 包含：

- JSON/schema/date/weather/day_index。
- 住宿类型一致。
- 三餐完整、具体、语义合法。
- 景点数 1-3。
- 景点 grounding。
- 中间天酒店不为空、酒店名合法、酒店 grounding。
- `hotel.distance` 不编造。
- location 结构合法。
- 预算加总一致。
- 景点预算人数关系。
- 餐饮预算人数关系。
- 交通预算非负。
- hard 预算不超。
- 酒店预算覆盖住宿晚数和房间数。

阶段性预算语义 hard pass 包含：

- 酒店预算关系：住宿晚数和两人一间。
- 景点预算关系：单人票价乘人数。
- 餐饮价格尺度：不明显低于预算档位人均费用。
- `budget_relationship_ok` 表示三项同时通过。

DPO soft pass 额外包含：

- 景点多样性。
- 餐饮多样性。
- 更严格餐饮 grounding。
- 预算偏好匹配。

## 7. 当前仍需注意

- `meal_cost_scale_ok` 不建议放进最严格 `sft_hard_pass`，但可用于清洗明显脏样本。
- 餐饮多样性属于 DPO/软质量，不建议作为 SFT 主过滤项。
- `budget.total` 精确加总由工程后处理保证；训练数据会写正确值，但评测分析时不要把 prompt-only 的算术失败当成唯一瓶颈。
- 如果使用 `--request-source llm`，LLM 请求 prompt 已允许 `family_mixed`，但正式 Planner SFT 建议先用 `controlled`，减少分布漂移。
