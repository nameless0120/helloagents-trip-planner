# Context 消融记录：compact_context

- 来源 records：`training/data/v3/eval_harder_food_bucket_return_dinner_no_route/records.jsonl`
- 样本数：300
- 改动范围：只改 PlannerContext JSON 和 planner_query 中的上下文；system_prompt 与后续 prompt 规则不变。

## 变体说明

- 不限制候选数量，只裁剪 POI 冗余字段。

## 平均候选数量

```json
{
  "classic_pois": 12.0,
  "preference_pois": 9.46,
  "scenic_pois": 17.68,
  "experience_pois": 4.52,
  "hotel_pois": 9.82,
  "food_pois": 15.59,
  "trip_weather": 4.2
}
```
