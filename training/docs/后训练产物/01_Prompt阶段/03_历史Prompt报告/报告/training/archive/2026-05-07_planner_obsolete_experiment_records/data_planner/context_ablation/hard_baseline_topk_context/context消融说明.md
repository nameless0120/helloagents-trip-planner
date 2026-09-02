# Context 消融记录：topk_context

- 来源 records：`training/data/v3/eval_harder_food_bucket_meal_ablation_budget_symbolic_no_route/records.jsonl`
- 样本数：300
- 改动范围：只改 PlannerContext JSON 和 planner_query 中的上下文；system_prompt 与后续 prompt 规则不变。

## 变体说明

- 裁剪 POI 冗余字段，并按固定 TopK 限制候选数量：`{'classic_pois': 8, 'preference_pois': 8, 'scenic_pois': 8, 'experience_pois': 4, 'hotel_pois': 6, 'food_pois': 10}`。

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
