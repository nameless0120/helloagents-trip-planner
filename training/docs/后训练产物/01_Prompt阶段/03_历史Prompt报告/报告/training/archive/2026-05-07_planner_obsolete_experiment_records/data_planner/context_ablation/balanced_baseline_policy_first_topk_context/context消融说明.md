# Context 消融记录：policy_first_topk_context

- 来源 records：`training/data/v3/eval_harder_food_bucket_return_dinner_no_route/records.jsonl`
- 样本数：300
- 改动范围：只改 PlannerContext JSON 和 planner_query 中的上下文；system_prompt 与后续 prompt 规则不变。

## 变体说明

- 在 topk_context 基础上，把人数、预算、负向约束、住宿晚数等 policy_summary 前置。

## 平均候选数量

```json
{
  "classic_pois": 8.0,
  "preference_pois": 6.47,
  "scenic_pois": 8.0,
  "experience_pois": 3.0,
  "hotel_pois": 6.0,
  "food_pois": 9.93,
  "trip_weather": 4.2
}
```
