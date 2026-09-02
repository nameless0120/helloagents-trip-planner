# Prompt Ablation: A_C_D

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: A, C, D

## Blocks

### A

```text
预算计算是最高优先级硬约束，必须严格执行。

内部计算流程必须按以下顺序完成，但不要输出计算过程：
A. 确定每天 attractions、meals、hotel。
B. 读取 PlannerContext.party.total，记为 people。
C. 计算 rooms = ceil(people / 2)。
D. 计算每一天是否产生住宿费用：
   - 如果 day.hotel 是 null，则该天 hotel_cost_for_budget = 0。
   - 如果 day.hotel 不是 null，则该天 hotel_cost_for_budget = day.hotel.estimated_cost * rooms。
   - day.hotel.estimated_cost 表示单间每晚价格，不是总价。
E. budget.total_hotels = 所有 day.hotel 非 null 的 hotel_cost_for_budget 之和。
F. budget.total_attractions = 所有 attractions.ticket_price 之和 * people。
G. budget.total_meals = 所有 meals.estimated_cost 之和 * people。
H. budget.total_transportation = 全体同行整趟本地交通估算，只能填写整数。
I. budget.total = budget.total_attractions + budget.total_hotels + budget.total_meals + budget.total_transportation。

价格复制规则：
- hotel.estimated_cost 必须复制 hotel_pois.estimated_cost_hint。
- attraction.ticket_price 必须复制对应 POI 的 ticket_price_hint。
- meal.estimated_cost 必须复制 food_pois.meal_cost_hint。
- 所有价格字段只能是整数数字，不能是字符串，不能是算式，不能是小数，不能是中文数字。

输出 JSON 前必须在内部逐项检查：
- total_attractions 是否等于所有门票相加后乘以 people。
- total_hotels 是否等于所有非 null 酒店每晚价乘以 rooms 后相加。
- total_meals 是否等于所有三餐人均价格相加后乘以 people。
- total 是否等于四个分项之和。
如果任一项不一致，必须先修正 budget，再输出最终 JSON。
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
