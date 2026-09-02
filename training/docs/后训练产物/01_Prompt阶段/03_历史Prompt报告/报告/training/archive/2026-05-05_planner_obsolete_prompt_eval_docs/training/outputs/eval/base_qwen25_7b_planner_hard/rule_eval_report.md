# Rule Eval Report: base_qwen25_7b_v3_hard

- records: 120
- generations: `training/outputs/eval/base_qwen25_7b_v3_hard/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 81 | 117 | 69.23% |
| budget_arithmetic_consistent | 114 | 117 | 97.44% |
| budget_consistent | 114 | 117 | 97.44% |
| budget_level_aligned | 115 | 117 | 98.29% |
| budget_preference_aligned | 115 | 117 | 98.29% |
| budget_within_user_budget | 117 | 117 | 100.00% |
| city_ok | 117 | 117 | 100.00% |
| date_range_ok | 117 | 117 | 100.00% |
| day_dates_ok | 117 | 117 | 100.00% |
| day_index_ok | 117 | 117 | 100.00% |
| days_len_ok | 117 | 117 | 100.00% |
| hard_pass | 76 | 117 | 64.96% |
| hotel_budget_covers_nights | 117 | 117 | 100.00% |
| invalid_hotel_name_ok | 117 | 117 | 100.00% |
| json_extract_ok | 118 | 120 | 98.33% |
| location_object_ok | 117 | 117 | 100.00% |
| meal_complete | 115 | 117 | 98.29% |
| middle_hotel_ok | 117 | 117 | 100.00% |
| schema_ok | 117 | 120 | 97.50% |
| weather_dates_ok | 117 | 117 | 100.00% |
| weather_match | 116 | 117 | 99.15% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "budget_arithmetic_inconsistent": 3,
  "budget_preference_mismatch": 2,
  "json_extract": 2,
  "schema": 1,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_eval_000008
- request: 大理 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '历史文化', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2990, "total": 2990, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 373.75, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_eval_000022
- request: 桂林 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['自然风光', '摄影', '城市漫步', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2990, "total": 2060, "diff": 930, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_eval_000029
- request: 长沙 2026-03-04->2026-03-06 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多']
- errors: `[{"stage": "schema", "message": "2 validation errors for TripPlan\ndays.0.meals.0.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=39.9, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.0.meals.2.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=257.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float"}]`

### v3_eval_000046
- request: 哈尔滨 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['自然风光', '摄影', '城市漫步', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2935, "total": 2035, "diff": 900, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 407.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_eval_000061
- request: 天津 2026-04-26->2026-04-30 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['历史文化', '公园', '老人友好', '本地美食']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_eval_000059
- request: 宁波 2026-02-02->2026-02-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_eval_000084
- request: 呼和浩特 2026-02-02->2026-02-05 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '博物馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "weather_mismatch", "details": [{"date": "2026-02-02", "field": "day_temp", "expected": 0, "got": 25}, {"date": "2026-02-02", "field": "night_temp", "expected": -13, "got": 15}]}]`

### v3_eval_000116
- request: 大理 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '历史文化', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2810, "total": 2810, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 351.25, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_eval_000119
- request: 哈尔滨 2026-07-02->2026-07-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2060, "diff": 1020, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 686.67, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
