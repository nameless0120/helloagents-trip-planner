# Prompt Ablation: A_D

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: A, D

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
