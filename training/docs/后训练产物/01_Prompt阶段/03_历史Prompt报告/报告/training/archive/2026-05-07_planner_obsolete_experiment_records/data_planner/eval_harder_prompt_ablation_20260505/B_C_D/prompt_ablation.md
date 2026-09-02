# Prompt Ablation: B_C_D

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: B, C, D

## Blocks

### B

```text
住宿字段规则是硬约束。

每一天都必须有 accommodation：
- day.accommodation 永远填写用户请求中的住宿类型字符串。
- 不能写 null、无住宿、返程、当天返程。

day.hotel 表示“当天晚上是否在本城市住宿”：
- 如果当天晚上住在本城市，day.hotel 必须从 hotel_pois 选择一个真实酒店对象。
- 如果最后一天晚上离开城市、不再住宿，只有最后一天 day.hotel 可以是 null。
- 除最后一天外，day.hotel 不能是 null。
- 不能把“无”“无住宿”“返程”“当天返程”写进 hotel.name。

酒店预算计算：
- people = PlannerContext.party.total。
- rooms = ceil(people / 2)。
- 每个非 null day.hotel 都代表产生 1 晚住宿费用。
- 每晚住宿费用 = day.hotel.estimated_cost * rooms。
- budget.total_hotels = 所有非 null day.hotel 的每晚住宿费用之和。
- 如果 3 天游且最后一天 hotel=null，则通常只计算前 2 天酒店费用。
- 如果 3 天游且 3 天 hotel 都非 null，则计算 3 晚酒店费用。

输出前内部校验：
budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost * rooms 的总和。
```

### C

```text
餐饮选择是硬约束，每天必须有 breakfast、lunch、dinner 三餐。

餐厅来源：
- lunch 和 dinner 必须从 food_pois 中选择真实餐厅。
- meal.name 必须完全复制 food_pois.name。
- meal.estimated_cost 必须复制 food_pois.meal_cost_hint。
- 禁止使用 hotel_pois 作为 lunch 或 dinner。
- 禁止使用泛化名称，例如“附近餐厅”“当地小吃”“特色餐厅”“早餐推荐”“午餐推荐”“晚餐推荐”“无”。

餐厅去重算法必须在内部执行：
1. 先列出所有 food_pois 候选。
2. 过滤 avoid_risk_keywords 非空的候选。
3. 给每个候选维护 used_count，初始为 0。
4. 为每一天选择 lunch 时，优先选择 used_count 最少、适合 lunch、距离当天景点区域更接近的候选。
5. 为同一天 dinner 选择时，禁止选择当天 lunch 的同一个 name。
6. dinner 同样优先选择 used_count 最少的候选。
7. 每选择一次餐厅，就把该 name 的 used_count 加 1。
8. 只有当可用 food_pois 数量不足以覆盖所有 lunch/dinner 时，才允许复用；复用时必须选择 used_count 最少的真实 food_pois。
9. breakfast 可以使用适合早餐/小吃/简餐的 food_pois，也可以在合理场景使用“酒店早餐/民宿早餐/客栈早餐”；住宿早餐不参与 used_count。

强制校验：
- 同一天 lunch.name 和 dinner.name 绝不能相同。
- 连续两天 dinner.name 尽量不能相同。
- 如果 food_pois 数量 >= 行程天数 * 2，则整趟行程所有 lunch/dinner 的 name 必须全部不同。
- 如果 food_pois 数量不足，则 lunch/dinner 应平均分散复用，不能每天固定同一家。
```

### D

```text
最终输出前必须执行一次内部自检，但不要输出自检过程。

自检清单：
1. JSON 第一个非空字符是 {，最后一个非空字符是 }。
2. days 数量等于旅行天数。
3. weather_info 数量等于旅行天数。
4. 每天 attractions 数量为 1-3。
5. 每天 meals 恰好包含 breakfast、lunch、dinner。
6. 每天 accommodation 都是住宿类型字符串。
7. 除最后一天返程外，day.hotel 不是 null。
8. hotel.distance 永远是空字符串 ""。
9. 所有 location 都是 {"longitude": 数字, "latitude": 数字}。
10. 所有价格字段都是整数数字。
11. budget.total_attractions = 所有 attractions.ticket_price 之和 * PlannerContext.party.total。
12. budget.total_hotels = 所有非 null day.hotel.estimated_cost 之和 * ceil(PlannerContext.party.total / 2)。
13. budget.total_meals = 所有 meals.estimated_cost 之和 * PlannerContext.party.total。
14. budget.total = budget.total_attractions + budget.total_hotels + budget.total_meals + budget.total_transportation。
15. 同一天 lunch.name 和 dinner.name 不相同。
16. food_pois 足够时，所有 lunch/dinner 不重复。

如果发现任何错误，必须先修改 JSON 内容，再输出。最终只能输出修正后的 JSON 对象。
```
