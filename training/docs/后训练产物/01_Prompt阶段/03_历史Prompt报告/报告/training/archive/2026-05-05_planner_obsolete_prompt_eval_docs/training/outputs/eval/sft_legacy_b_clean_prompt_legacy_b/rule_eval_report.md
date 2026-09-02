# Rule Eval Report: sft_v2_clean_prompt_v2

- records: 91
- generations: `training/outputs/eval/sft_v2_clean_prompt_v2/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 87 | 88 | 98.86% |
| budget_arithmetic_consistent | 82 | 88 | 93.18% |
| budget_consistent | 82 | 88 | 93.18% |
| budget_level_aligned | 55 | 88 | 62.50% |
| budget_preference_aligned | 55 | 88 | 62.50% |
| budget_within_user_budget | 88 | 88 | 100.00% |
| city_ok | 88 | 88 | 100.00% |
| date_range_ok | 88 | 88 | 100.00% |
| day_dates_ok | 88 | 88 | 100.00% |
| day_index_ok | 88 | 88 | 100.00% |
| days_len_ok | 88 | 88 | 100.00% |
| hard_pass | 87 | 88 | 98.86% |
| invalid_hotel_name_ok | 88 | 88 | 100.00% |
| json_extract_ok | 89 | 91 | 97.80% |
| location_object_ok | 88 | 88 | 100.00% |
| meal_complete | 88 | 88 | 100.00% |
| middle_hotel_ok | 88 | 88 | 100.00% |
| schema_ok | 88 | 91 | 96.70% |
| weather_dates_ok | 88 | 88 | 100.00% |
| weather_match | 88 | 88 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9972,
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
  "budget_preference_mismatch": 33,
  "budget_arithmetic_inconsistent": 6,
  "json_extract": 2,
  "schema": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1650, "total": 1650, "diff": 0, "requested_budget": {"available": true, "amount": 7219, "scope": "per_person", "party_size": 3, "total": 21657}, "per_person_day": 137.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000971
- request: 广州 2025-08-04->2025-08-05 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '历史文化', '休闲慢游']
- errors: `[{"stage": "schema", "message": "2 validation errors for TripPlan\ndays.1.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type"}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1086, "total": 1086, "diff": 0, "requested_budget": {"available": true, "amount": 11994, "scope": "per_person", "party_size": 3, "total": 35982}, "per_person_day": 181.0, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1312, "total": 1312, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "per_person", "party_size": 2, "total": 20000}, "per_person_day": 164.0, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2580, "total": 2580, "diff": 0, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 322.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000435
- request: 长沙 2026-04-24->2026-04-25 days=2 transport=地铁+步行 hotel=民宿 prefs=['休闲慢游', '城市地标', '清真']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 680, "total": 680, "diff": 0, "requested_budget": {"available": true, "amount": 10461, "scope": "total", "party_size": 2, "total": 10461}, "per_person_day": 170.0, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3030, "total": 2930, "diff": 100, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 195.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000116
- request: 大理 2026-05-03->2026-05-06 days=4 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市公园', '休闲慢游', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3020, "total": 2020, "diff": 1000, "requested_budget": {"available": true, "amount": 17036, "scope": "total", "party_size": 3, "total": 17036}, "per_person_day": 168.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3020, "total": 2020, "diff": 1000, "requested_budget": {"available": true, "amount": 17036, "scope": "total", "party_size": 3, "total": 17036}, "per_person_day": 168.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000341
- request: 西安 2026-05-04->2026-05-06 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1220, "total": 1220, "diff": 0, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 135.56, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000242
- request: 呼和浩特 2025-08-04->2025-08-07 days=4 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '美食', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2150, "total": 2150, "diff": 0, "requested_budget": {"available": true, "amount": 15882, "scope": "total", "party_size": 3, "total": 15882}, "per_person_day": 179.17, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000146
- request: 贵阳 2026-01-31->2026-02-02 days=3 transport=地铁+步行 hotel=民宿 prefs=['城市公园', '城市地标', '夜市夜景', '自然风光']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 930, "total": 930, "diff": 0, "requested_budget": {"available": true, "amount": 12114, "scope": "total", "party_size": 1, "total": 12114}, "per_person_day": 310.0, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000531
- request: 苏州 2026-05-05->2026-05-07 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['购物商圈', '第一次来', '自然风光', '美食']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v2_request_000073
- request: 呼和浩特 2026-08-29->2026-08-31 days=3 transport=公共交通 hotel=民宿 prefs=['城市公园', '博物馆', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 970, "total": 970, "diff": 0, "requested_budget": {"available": true, "amount": 9863, "scope": "per_person", "party_size": 1, "total": 9863}, "per_person_day": 323.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000529
- request: 武汉 2026-06-15->2026-06-19 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '自然风光', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3072, "total": 2872, "diff": 200, "requested_budget": {"available": true, "amount": 8187, "scope": "per_person", "party_size": 3, "total": 24561}, "per_person_day": 191.47, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000248
- request: 杭州 2026-08-29->2026-09-01 days=4 transport=公共交通 hotel=经济型酒店 prefs=['第一次来', '小众展览', '自然风光', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1520, "total": 1520, "diff": 0, "requested_budget": {"available": true, "amount": 7561, "scope": "per_person", "party_size": 2, "total": 15122}, "per_person_day": 190.0, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000493
- request: 武汉 2026-08-29->2026-08-30 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '第一次来', '主题乐园', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 747, "total": 647, "diff": 100, "requested_budget": {"available": true, "amount": 16336, "scope": "total", "party_size": 3, "total": 16336}, "per_person_day": 107.83, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000704
- request: 北京 2026-04-24->2026-04-25 days=2 transport=打车 hotel=经济型酒店 prefs=['亲子', '城市地标', '历史文化', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 950, "total": 1050, "diff": -100, "requested_budget": {"available": true, "amount": 10296, "scope": "total", "party_size": 3, "total": 10296}, "per_person_day": 175.0, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000758
- request: 黄山 2026-05-03->2026-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '美食', '博物馆', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1586, "total": 1586, "diff": 0, "requested_budget": {"available": true, "amount": 14936, "scope": "total", "party_size": 3, "total": 14936}, "per_person_day": 132.17, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000761
- request: 福州 2025-08-04->2025-08-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['城市漫步', '城市公园', '历史文化', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2030, "total": 1830, "diff": 200, "requested_budget": {"available": true, "amount": 9127, "scope": "per_person", "party_size": 2, "total": 18254}, "per_person_day": 305.0, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000117
- request: 大理 2026-01-31->2026-02-02 days=3 transport=打车 hotel=经济型酒店 prefs=['亲子', '购物商圈', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1120, "total": 1120, "diff": 0, "requested_budget": {"available": true, "amount": 4850, "scope": "per_person", "party_size": 3, "total": 14550}, "per_person_day": 124.44, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`
