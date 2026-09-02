# Prompt 消融记录：budget_relation_priority

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

预算语义关系补充:
- 这次优先保证预算口径关系正确，不要为了压低总价而少算人数、少算住宿晚数或把整组餐费写成单人价。
- 住宿费用必须体现天数关系：N 天通常 N-1 晚；最后一天 hotel=null 才不计住宿，其他有 hotel 的 day 都要体现一晚住宿费用。
- 景点费用必须体现人数关系：attraction.ticket_price 是成人单人门票；同行总人数越多，budget.total_attractions 应相应放大。
- 餐饮费用必须体现同行人数和预算档位：meal.estimated_cost 是整组人单餐费用，不是单人价。多人同行、舒适/高端预算时，午餐和晚餐不要写成明显偏低的小额单人餐费。

预算语义优先级补充:
- 如果无法同时做到预算总额完全精确和预算口径关系完全正确，优先保证口径关系：住宿晚数、景点门票人数、餐饮整组费用不能错。
- 不允许用“少算酒店晚数”“景点只算一个人”“多人正餐按单人价写”来让预算看起来更低。
- budget.total 可以后续由系统重新核算，但 day.hotel.estimated_cost、attraction.ticket_price、meal.estimated_cost 必须表达正确的业务语义。
- 输出前内部检查三句话：住了几晚？门票乘了几个人？每顿饭是不是整组费用？
```
