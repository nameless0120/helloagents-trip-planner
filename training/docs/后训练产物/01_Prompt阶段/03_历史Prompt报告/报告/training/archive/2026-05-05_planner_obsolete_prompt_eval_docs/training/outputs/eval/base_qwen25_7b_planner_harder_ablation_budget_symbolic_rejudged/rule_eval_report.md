# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_budget_symbolic_rejudged

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_budget_symbolic_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 293 | 293 | 100.00% |
| budget_arithmetic_consistent | 274 | 293 | 93.52% |
| budget_consistent | 274 | 293 | 93.52% |
| budget_level_aligned | 285 | 293 | 97.27% |
| budget_preference_aligned | 285 | 293 | 97.27% |
| budget_within_user_budget | 293 | 293 | 100.00% |
| city_ok | 293 | 293 | 100.00% |
| date_range_ok | 293 | 293 | 100.00% |
| day_dates_ok | 293 | 293 | 100.00% |
| day_index_ok | 293 | 293 | 100.00% |
| days_len_ok | 293 | 293 | 100.00% |
| hard_pass | 258 | 293 | 88.05% |
| hotel_budget_covers_nights | 293 | 293 | 100.00% |
| hotel_distance_placeholder_ok | 293 | 293 | 100.00% |
| invalid_hotel_name_ok | 293 | 293 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| location_object_ok | 293 | 293 | 100.00% |
| meal_complete | 290 | 293 | 98.98% |
| meal_grounding_ok | 278 | 293 | 94.88% |
| meal_specific_ok | 293 | 293 | 100.00% |
| meal_valid_semantics_ok | 280 | 293 | 95.56% |
| middle_hotel_ok | 292 | 293 | 99.66% |
| schema_ok | 293 | 300 | 97.67% |
| weather_dates_ok | 293 | 293 | 100.00% |
| weather_match | 293 | 293 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.997,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.994,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "budget_arithmetic_inconsistent": 19,
  "meal_invalid_name": 13,
  "budget_preference_mismatch": 8,
  "schema": 6,
  "meal_grounding_miss": 2,
  "json_extract": 1,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3220, "total": 2220, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 222.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-05", "type": "dinner", "name": "民俗街夜市"}, {"date": "2026-04-06", "type": "dinner", "name": "民俗街夜市"}]}]`

### v3_harder_eval_000046
- request: 哈尔滨 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4220, "total": 3220, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 268.33, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000040
- request: 南京 2026-07-03->2026-07-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4375, "total": 3375, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 225.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000085
- request: 北京 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "schema", "message": "5 validation errors for TripPlan\ndays.0.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=53.5, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.1.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=53.5, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.2.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=53.5, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.3.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=53.5, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.4.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=53.5, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float"}]`

### v3_harder_eval_000096
- request: 南京 2026-05-06->2026-05-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000103
- request: 扬州 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "lunch", "name": "扬州忠强旅馆", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州忠强旅馆", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州忠强旅馆", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州忠强旅馆", "reason": "hotel_or_lodging_name"}]}]`

### v3_harder_eval_000132
- request: 黄山 2026-08-02->2026-08-05 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3112, "total": 3112, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 389.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000142
- request: 成都 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3110, "total": 2110, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 263.75, "budget_level": "limited", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000135
- request: 西安 2026-02-03->2026-02-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-02-07", "type": "dinner", "name": "西安徐北宾馆", "reason": "hotel_or_lodging_name"}]}]`

### v3_harder_eval_000205
- request: 丽江 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2060, "diff": 1020, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000220
- request: 大连 2026-06-03->2026-06-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4480, "total": 3480, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 232.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000270
- request: 桂林 2025-05-04->2025-05-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2025-05-06", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2025-05-07", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2025-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000280
- request: 重庆 2026-08-02->2026-08-06 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4440, "total": 3440, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 229.33, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2840, "total": 2840, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 355.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 900, "reported_total_hotels": 1200, "diff": 300, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000039
- request: 深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-11-08", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000052
- request: 苏州 2025-11-05->2025-11-08 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3258, "total": 3258, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 407.25, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1000, "diff": 250, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000068
- request: 福州 2026-09-01->2026-09-03 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3030, "total": 2030, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 338.33, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 2250, "diff": 750, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000065
- request: 天津 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2060, "diff": 1020, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
