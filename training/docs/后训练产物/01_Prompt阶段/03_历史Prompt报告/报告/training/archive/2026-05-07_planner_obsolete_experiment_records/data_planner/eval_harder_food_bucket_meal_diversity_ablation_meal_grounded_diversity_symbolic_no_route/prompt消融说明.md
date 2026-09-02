# Prompt 消融记录：meal_grounded_diversity_symbolic

- 来源 records：`training/data/v3/eval_harder_food_bucket_meal_diversity_prompt_no_route/records.jsonl`
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

餐饮 grounding 与多样性均衡补充:
- food_pois 是餐饮来源上限，lunch/dinner 不要为了多样性编造不存在的餐厅。
- 如果存在足够 food_pois，优先做到每天 lunch/dinner 不同店、跨天少重复；如果候选不足，允许复用真实 food_pois，但必须在 description 中说明“附近可用候选有限，因此复用该真实餐厅”。
- 允许使用真实语义餐饮 fallback 的范围很窄：仅限城市级典型美食街/夜市/小吃集合，例如“上海城隍庙小吃”“西安回民街小吃”；不能用“附近餐厅”“当地餐厅”“酒店晚餐”这类泛化词。
- 酒店早餐/民宿早餐/客栈早餐作为 breakfast 可接受，可重复，不计入餐饮多样性惩罚。

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
