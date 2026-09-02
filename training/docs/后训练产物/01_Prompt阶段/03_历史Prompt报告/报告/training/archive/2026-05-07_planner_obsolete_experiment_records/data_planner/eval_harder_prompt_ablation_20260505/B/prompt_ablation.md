# Prompt Ablation: B

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: B

## Blocks

### B

```text
住宿字段规则是硬约束。

每一天都必须有 accommodation：
- day.accommodation 永远填写用户请求中的住宿类型字符串。
- 不能写 null、无住宿、返程、当天返程。

day.hotel 表示“当天晚上是否在本城市住宿”：
- 如果当天晚上住在本城市，day.hotel 必须从 hotel_pois 选择一个真实酒店对象。
- 如果最后一天晚上离开城市、不再住宿，只有最后一天 day.hotel 可以是 null。
- 除最后一天外，day.hotel 不能是 null。
- 不能把“无”“无住宿”“返程”“当天返程”写进 hotel.name。

酒店预算计算：
- people = PlannerContext.party.total。
- rooms = ceil(people / 2)。
- 每个非 null day.hotel 都代表产生 1 晚住宿费用。
- 每晚住宿费用 = day.hotel.estimated_cost * rooms。
- budget.total_hotels = 所有非 null day.hotel 的每晚住宿费用之和。
- 如果 3 天游且最后一天 hotel=null，则通常只计算前 2 天酒店费用。
- 如果 3 天游且 3 天 hotel 都非 null，则计算 3 晚酒店费用。

输出前内部校验：
budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost * rooms 的总和。
```
