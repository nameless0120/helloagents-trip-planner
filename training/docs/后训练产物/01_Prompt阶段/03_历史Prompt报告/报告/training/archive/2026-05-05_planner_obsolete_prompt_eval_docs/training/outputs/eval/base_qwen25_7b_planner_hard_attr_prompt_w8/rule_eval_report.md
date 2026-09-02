# Rule Eval Report: base_qwen25_7b_v3_hard_attr_prompt_w8

- records: 120
- generations: `training/outputs/eval/base_qwen25_7b_v3_hard_attr_prompt_w8/generations.jsonl`
- records_path: `training/data/v3/eval_hard_prompt_attraction_required/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 117 | 118 | 99.15% |
| budget_arithmetic_consistent | 116 | 118 | 98.31% |
| budget_consistent | 116 | 118 | 98.31% |
| budget_level_aligned | 118 | 118 | 100.00% |
| budget_preference_aligned | 118 | 118 | 100.00% |
| budget_within_user_budget | 118 | 118 | 100.00% |
| city_ok | 118 | 118 | 100.00% |
| date_range_ok | 118 | 118 | 100.00% |
| day_dates_ok | 118 | 118 | 100.00% |
| day_index_ok | 118 | 118 | 100.00% |
| days_len_ok | 118 | 118 | 100.00% |
| hard_pass | 115 | 118 | 97.46% |
| hotel_budget_covers_nights | 118 | 118 | 100.00% |
| invalid_hotel_name_ok | 118 | 118 | 100.00% |
| json_extract_ok | 119 | 120 | 99.17% |
| location_object_ok | 118 | 118 | 100.00% |
| meal_complete | 118 | 118 | 100.00% |
| middle_hotel_ok | 118 | 118 | 100.00% |
| schema_ok | 118 | 120 | 98.33% |
| weather_dates_ok | 118 | 118 | 100.00% |
| weather_match | 118 | 118 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9989,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "budget_arithmetic_inconsistent": 2,
  "schema": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_eval_000022
- request: 桂林 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['自然风光', '摄影', '城市漫步', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2995, "total": 2060, "diff": 935, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_eval_000068
- request: 福州 2026-08-31->2026-09-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '历史文化', '城市漫步']
- errors: `[{"stage": "schema", "message": "4 validation errors for TripPlan\ndays.0.meals.0.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=37.2, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.0.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=18.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.2.meals.0.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=18.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.3.meals.0.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=18.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float"}]`

### v3_eval_000101
- request: 长沙 2026-04-03->2026-04-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_eval_000119
- request: 哈尔滨 2026-07-02->2026-07-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3125, "total": 2060, "diff": 1065, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 686.67, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
