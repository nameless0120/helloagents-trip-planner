# Prompt 消融记录：budget_symbolic_meal_semantic

- 来源 records：`training/data/v3/eval_harder_food_bucket_no_route/records.jsonl`
- 样本数：300
- 改动范围：只追加 system_prompt 和 planner_query 规则，不改变 request/planner_context/tool_snapshot。
- 共同餐饮规则：lunch/dinner 宁可重复真实 food_pois，也不能写无、空、酒店晚餐或泛化餐厅。

## 附加规则

```text
餐饮语义兜底补充:
- lunch/dinner 首选逐字复制 food_pois 中的真实餐厅 name/address/location/meal_cost_hint。
- 如果 food_pois 不能覆盖非常典型的本地餐饮场景，可以使用真实餐饮语义 fallback，例如“上海城隍庙小吃”“西安回民街小吃”“夜市小吃”“本地美食街”；但 name 必须明确包含小吃、夜市、美食、餐厅、饭店、酒家、茶社、面馆、粉店、火锅、烧烤、咖啡、甜品等餐饮语义，estimated_cost 参考同档位 food_pois 的 meal_cost_hint 估算，不能写 0。
- 绝不能把 hotel_pois 的酒店/宾馆/旅馆/民宿/客栈/公寓名称写成 meal.name；绝不能写“无”、空字符串、“酒店晚餐”“酒店午餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”。
- 绝不能把非餐饮 POI 写成 meal.name，例如电子游艺厅、博物馆、景点、公园、商场、培训机构。无法判断 fallback 是否餐饮时，重复使用一个真实 food_pois。

预算口径补充:
- hotel.estimated_cost 表示“全体同行每晚住宿费用”，不是单人价格；budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost 按住宿晚数加总。同一酒店住 N 晚，就按每晚费用乘 N 晚。
- meal.estimated_cost 表示“全体同行这一餐总费用”，不是单人价格；budget.total_meals 必须等于所有 meal.estimated_cost 直接加总，不要再乘 party.total。
- attraction.ticket_price 表示“成人单人门票”；budget.total_attractions 必须等于所有已选景点 ticket_price 之和再乘以 PlannerContext.party.total。
- budget.total 必须只由四个分项重新加总得到：total_attractions + total_hotels + total_meals + total_transportation。不要凭感觉填总价，不要照抄示例数字。

内部生成顺序补充:
1. 先从候选中确定每天的酒店、景点和三餐。
2. 再统计实际住宿晚数：最后一天 hotel=null 时不计住宿；最后一天仍入住时才计入一晚。
3. 再分别计算 total_attractions、total_hotels、total_meals、total_transportation。
4. 最后计算 budget.total，并只输出最终 JSON。
不要一边写每天行程一边顺手估 budget；budget 必须在所有 day 写完后统一复算。

预算算术口径示例:
- 酒店总价 = 每晚住宿费用 × 实际住宿晚数；最后一天 hotel=null 时不计住宿。
- 景点总价 = 所选景点成人单人门票之和 × PlannerContext.party.total。
- 餐饮总价 = 所有 breakfast/lunch/dinner 的整组 meal.estimated_cost 直接加总，不再乘人数。
- 总预算 = 景点总价 + 酒店总价 + 餐饮总价 + 全程本地交通。
这个示例只用于理解计算口径，不包含任何可复用数字；实际输出必须使用当前 PlannerContext 的候选价格和同行人数重新计算。
```
