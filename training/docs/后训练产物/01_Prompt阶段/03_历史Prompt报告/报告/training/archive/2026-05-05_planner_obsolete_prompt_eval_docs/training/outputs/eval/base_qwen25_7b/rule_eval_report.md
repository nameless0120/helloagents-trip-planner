# Rule Eval Report: base_qwen25_7b

- records: 91
- generations: `training/outputs/eval/base_qwen25_7b/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 71 | 72 | 98.61% |
| budget_arithmetic_consistent | 67 | 72 | 93.06% |
| budget_consistent | 67 | 72 | 93.06% |
| budget_level_aligned | 58 | 72 | 80.56% |
| budget_preference_aligned | 58 | 72 | 80.56% |
| budget_within_user_budget | 71 | 72 | 98.61% |
| city_ok | 72 | 72 | 100.00% |
| date_range_ok | 72 | 72 | 100.00% |
| day_dates_ok | 72 | 72 | 100.00% |
| day_index_ok | 72 | 72 | 100.00% |
| days_len_ok | 72 | 72 | 100.00% |
| hard_pass | 69 | 72 | 95.83% |
| invalid_hotel_name_ok | 72 | 72 | 100.00% |
| json_extract_ok | 91 | 91 | 100.00% |
| location_object_ok | 72 | 72 | 100.00% |
| meal_complete | 72 | 72 | 100.00% |
| middle_hotel_ok | 71 | 72 | 98.61% |
| schema_ok | 72 | 91 | 79.12% |
| weather_dates_ok | 72 | 72 | 100.00% |
| weather_match | 71 | 72 | 98.61% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.995,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9861,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "schema": 19,
  "budget_preference_mismatch": 14,
  "budget_arithmetic_inconsistent": 5,
  "weather_mismatch": 1,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2652, "total": 2652, "diff": 0, "requested_budget": {"available": true, "amount": 7219, "scope": "per_person", "party_size": 3, "total": 21657}, "per_person_day": 221.0, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000971
- request: 广州 2025-08-04->2025-08-05 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '历史文化', '休闲慢游']
- errors: `[{"stage": "schema", "message": "2 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000655
- request: 上海 2026-05-31->2026-06-03 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['第一次来', '海滨度假', '美食', '历史文化']
- errors: `[{"stage": "schema", "message": "4 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000662
- request: 厦门 2026-07-30->2026-07-31 days=2 transport=公共交通 hotel=经济型酒店 prefs=['历史文化', '购物商圈', '自然风光']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000992
- request: 洛阳 2026-06-30->2026-07-03 days=4 transport=公共交通 hotel=经济型酒店 prefs=['艺术', '海滨度假', '美食']
- errors: `[{"stage": "schema", "message": "4 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000864
- request: 昆明 2026-05-03->2026-05-04 days=2 transport=打车 hotel=经济型酒店 prefs=['亲子', '美食', '历史文化', '小众展览']
- errors: `[{"stage": "rule", "type": "weather_mismatch", "details": [{"date": "2026-05-04", "field": "day_weather", "expected": "小雨", "got": "晴"}]}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1660, "total": 1660, "diff": 0, "requested_budget": {"available": true, "amount": 11994, "scope": "per_person", "party_size": 3, "total": 35982}, "per_person_day": 276.67, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000599
- request: 哈尔滨 2026-04-01->2026-04-03 days=3 transport=打车 hotel=经济型酒店 prefs=['购物商圈', '城市地标', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2210, "total": 2110, "diff": 100, "requested_budget": {"available": true, "amount": 3951, "scope": "total", "party_size": 1, "total": 3951}, "per_person_day": 703.33, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "schema", "message": "4 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2060, "total": 2060, "diff": 0, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 257.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3880, "total": 3880, "diff": 0, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 258.67, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000102
- request: 上海 2026-07-30->2026-08-01 days=3 transport=自驾 hotel=经济型酒店 prefs=['亲子', '自然风光', '博物馆', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3179, "total": 2060, "diff": 1119, "requested_budget": {"available": true, "amount": 1296, "scope": "per_person", "party_size": 3, "total": 3888}, "per_person_day": 228.89, "budget_level": "limited", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000919
- request: 泉州 2026-06-15->2026-06-18 days=4 transport=地铁+步行 hotel=舒适型酒店 prefs=['老人友好', '博物馆', '城市地标']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000341
- request: 西安 2026-05-04->2026-05-06 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2148, "total": 2068, "diff": 80, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 229.78, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000876
- request: 丽江 2026-06-15->2026-06-18 days=4 transport=公共交通 hotel=经济型酒店 prefs=['购物商圈', '城市公园', '历史文化', '城市地标']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000242
- request: 呼和浩特 2025-08-04->2025-08-07 days=4 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '美食', '博物馆']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000531
- request: 苏州 2026-05-05->2026-05-07 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['购物商圈', '第一次来', '自然风光', '美食']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000658
- request: 北京 2026-06-30->2026-07-01 days=2 transport=打车 hotel=舒适型酒店 prefs=['城市公园', '城市漫步']
- errors: `[{"stage": "schema", "message": "2 validation errors for TripPlan\ndays.0.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000248
- request: 杭州 2026-08-29->2026-09-01 days=4 transport=公共交通 hotel=经济型酒店 prefs=['第一次来', '小众展览', '自然风光', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4120, "total": 3120, "diff": 1000, "requested_budget": {"available": true, "amount": 7561, "scope": "per_person", "party_size": 2, "total": 15122}, "per_person_day": 390.0, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000268
- request: 丽江 2026-05-03->2026-05-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市公园', '自然风光', '夜市夜景', '历史文化']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`
