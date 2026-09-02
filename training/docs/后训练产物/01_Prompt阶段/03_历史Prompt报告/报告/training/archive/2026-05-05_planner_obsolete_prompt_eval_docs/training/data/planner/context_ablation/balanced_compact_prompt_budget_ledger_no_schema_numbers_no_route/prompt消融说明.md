# Prompt 消融记录：budget_ledger_no_schema_numbers

- 来源 records：`training/data/v3/context_ablation/balanced_baseline_compact_context/records.jsonl`
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

预算账本强约束:
- budget 不是新的规划内容，而是对已经输出的 days 数组做机械汇总。先完整写好 days，再回扫 days 里的字段计算 budget。
- total_hotels 只等于所有非 null day.hotel.estimated_cost 的逐项加总；如果最后一天 hotel=null，就不计入最后一天；不要按 travel_days、party.total 或用户预算重新乘。
- total_attractions 只等于所有 days[].attractions[].ticket_price 的逐项加总后再乘 PlannerContext.party.total；不要把已经乘过人数的结果再写进 attraction.ticket_price。
- total_meals 只等于所有 days[].meals[].estimated_cost 的逐项加总；meal.estimated_cost 已经是整组单餐费用，绝不能再乘 PlannerContext.party.total。
- total_transportation 是唯一允许估算的预算分项，必须是非负整数；估完后也必须参与最终加总。
- 最后一步只做这一件事：budget.total = total_attractions + total_hotels + total_meals + total_transportation。若发现 total 不一致，必须改 budget.total，而不是留下近似值。
- 如果 budget_fit_policy 或 hard 预算上限与预算账本冲突，先调整酒店/景点/餐厅选择，再重新回扫计算；不要通过少算酒店晚数、少乘门票人数、少加餐费来“凑预算”。
```
