# Prompt Ablation: A

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: A

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
