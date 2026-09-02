# Prompt Ablation: D

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: D

## Blocks

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
