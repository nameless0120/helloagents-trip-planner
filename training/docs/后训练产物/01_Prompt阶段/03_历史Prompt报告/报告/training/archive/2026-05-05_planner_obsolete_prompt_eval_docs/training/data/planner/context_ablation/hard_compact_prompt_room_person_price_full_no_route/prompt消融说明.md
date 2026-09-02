# Prompt 消融记录：room_person_price_full

- 来源 records：`training/data/v3/context_ablation/hard_baseline_compact_context/records.jsonl`
- 样本数：300
- 改动范围：只追加 system_prompt 和 planner_query 规则，不改变 request/planner_context/tool_snapshot。
- 共同餐饮规则：lunch/dinner 宁可重复真实 food_pois，也不能写无、空、酒店晚餐或泛化餐厅。

## 附加规则

```text
餐饮兜底补充:
- lunch/dinner 首选不同的真实 food_pois 候选；同一天 lunch 和 dinner 不要选择同一家餐厅，整趟行程不要每天反复使用同一家店、同一品牌或同一种单品。
- 只有当可用 food_pois 明显不足、忌口过滤后选择很少时，才允许少量复用真实 food_pois；复用时优先选择已使用次数最少的候选。
- lunch/dinner 绝不能写“无”、空字符串、“酒店晚餐”“酒店午餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”“附近餐厅”“当地餐厅”等占位或住宿类餐饮。
- 酒店早餐/民宿早餐/客栈早餐作为 breakfast 可接受且可重复，不计入餐饮多样性惩罚；非住宿早餐不要连续多天固定同一家店或同一种早餐。

价格口径覆盖规则:
以下规则覆盖上文所有“酒店全体同行每晚费用、餐饮整组单餐费用”的旧说法。
- hotel.estimated_cost 表示“单间每晚房价”，按两人一间估算房间数：rooms = ceil(PlannerContext.party.total / 2)。
- meal.estimated_cost 表示“人均单餐费用”，不是整组费用。
- attraction.ticket_price 仍表示成人单人门票。

两人一间与人均餐费预算规则:
以下规则覆盖上文所有旧预算口径。
- hotel.estimated_cost 必须复制 hotel_pois.estimated_cost_hint，含义是“单间每晚房价”。
- 酒店总价必须体现房间数和住宿晚数：budget.total_hotels = 所有非 null day.hotel.estimated_cost 之和 × rooms，其中 rooms = ceil(PlannerContext.party.total / 2)。
- meal.estimated_cost 必须复制 food_pois.meal_cost_hint 或合法 fallback，含义是“人均单餐费用”。
- 餐饮总价必须体现人数：budget.total_meals = 所有 day.meals[].estimated_cost 之和 × PlannerContext.party.total。
- attraction.ticket_price 是成人单人门票，budget.total_attractions = 所有 ticket_price 之和 × PlannerContext.party.total。
- budget.total 可以后续由系统重算；但酒店房间数、餐饮人均价、景点单人票价这些业务口径不能错。
```
