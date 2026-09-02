# Prompt 消融记录：budget_hard

- 来源 records：`training/data/v3/eval_harder_food_bucket_meal_fallback_no_route/records.jsonl`
- 样本数：300
- 改动范围：只追加 system_prompt 和 planner_query 规则，不改变 request/planner_context/tool_snapshot。
- 共同餐饮规则：lunch/dinner 宁可重复真实 food_pois，也不能写无、空、酒店晚餐或泛化餐厅。

## 附加规则

```text
餐饮兜底补充:
- lunch/dinner 如果找不到完美匹配当天位置、口味或预算的餐厅，必须重复使用一个真实的 food_pois 候选；重复真实餐厅优于写空、写“无”、写酒店晚餐或编造泛化餐厅。
- lunch/dinner 绝不能写“无”、空字符串、“酒店晚餐”“酒店午餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”“附近餐厅”“当地餐厅”等占位或住宿类餐饮。

预算口径补充:
- hotel.estimated_cost 表示“全体同行每晚住宿费用”，不是单人价格；budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost 按住宿晚数加总。同一酒店住 N 晚，就按每晚费用乘 N 晚。
- meal.estimated_cost 表示“全体同行这一餐总费用”，不是单人价格；budget.total_meals 必须等于所有 meal.estimated_cost 直接加总，不要再乘 party.total。
- attraction.ticket_price 表示“成人单人门票”；budget.total_attractions 必须等于所有已选景点 ticket_price 之和再乘以 PlannerContext.party.total。
- budget.total 必须只由四个分项重新加总得到：total_attractions + total_hotels + total_meals + total_transportation。不要凭感觉填总价，不要照抄示例数字。
```
