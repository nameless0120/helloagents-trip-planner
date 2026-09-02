# Rule Eval Report: sft_v2_clean

- records: 91
- generations: `training/outputs/eval/sft_v2_clean/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 88 | 89 | 98.88% |
| budget_arithmetic_consistent | 76 | 89 | 85.39% |
| budget_consistent | 76 | 89 | 85.39% |
| budget_level_aligned | 63 | 89 | 70.79% |
| budget_preference_aligned | 62 | 89 | 69.66% |
| budget_within_user_budget | 88 | 89 | 98.88% |
| city_ok | 89 | 89 | 100.00% |
| date_range_ok | 89 | 89 | 100.00% |
| day_dates_ok | 89 | 89 | 100.00% |
| day_index_ok | 89 | 89 | 100.00% |
| days_len_ok | 89 | 89 | 100.00% |
| hard_pass | 88 | 89 | 98.88% |
| invalid_hotel_name_ok | 89 | 89 | 100.00% |
| json_extract_ok | 89 | 91 | 97.80% |
| location_object_ok | 89 | 89 | 100.00% |
| meal_complete | 89 | 89 | 100.00% |
| middle_hotel_ok | 89 | 89 | 100.00% |
| schema_ok | 89 | 91 | 97.80% |
| weather_dates_ok | 89 | 89 | 100.00% |
| weather_match | 89 | 89 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9952,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9888,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "budget_preference_mismatch": 27,
  "budget_arithmetic_inconsistent": 13,
  "json_extract": 2,
  "too_many_attractions": 1
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1460, "total": 1460, "diff": 0, "requested_budget": {"available": true, "amount": 7219, "scope": "per_person", "party_size": 3, "total": 21657}, "per_person_day": 121.67, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000864
- request: 昆明 2026-05-03->2026-05-04 days=2 transport=打车 hotel=经济型酒店 prefs=['亲子', '美食', '历史文化', '小众展览']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v2_request_000514
- request: 珠海 2026-05-04->2026-05-06 days=3 transport=自驾 hotel=舒适型酒店 prefs=['主题乐园', '美食', '历史文化', '素食']
- errors: `[{"stage": "rule", "type": "too_many_attractions", "details": [{"date": "2026-05-05", "count": 4}]}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 938, "total": 938, "diff": 0, "requested_budget": {"available": true, "amount": 11994, "scope": "per_person", "party_size": 3, "total": 35982}, "per_person_day": 156.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1950, "total": 1950, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "per_person", "party_size": 2, "total": 20000}, "per_person_day": 243.75, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2418, "total": 1818, "diff": 600, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 227.25, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2418, "total": 1818, "diff": 600, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 227.25, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3060, "total": 2060, "diff": 1000, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 137.33, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3060, "total": 2060, "diff": 1000, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 137.33, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000919
- request: 泉州 2026-06-15->2026-06-18 days=4 transport=地铁+步行 hotel=舒适型酒店 prefs=['老人友好', '博物馆', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2400, "total": 1400, "diff": 1000, "requested_budget": {"available": true, "amount": 1442, "scope": "per_person", "party_size": 3, "total": 4326}, "per_person_day": 116.67, "budget_level": "limited", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000341
- request: 西安 2026-05-04->2026-05-06 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2260, "total": 1760, "diff": 500, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 195.56, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2260, "total": 1760, "diff": 500, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 195.56, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000242
- request: 呼和浩特 2025-08-04->2025-08-07 days=4 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '美食', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1940, "total": 1740, "diff": 200, "requested_budget": {"available": true, "amount": 15882, "scope": "total", "party_size": 3, "total": 15882}, "per_person_day": 145.0, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000146
- request: 贵阳 2026-01-31->2026-02-02 days=3 transport=地铁+步行 hotel=民宿 prefs=['城市公园', '城市地标', '夜市夜景', '自然风光']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1240, "total": 1240, "diff": 0, "requested_budget": {"available": true, "amount": 12114, "scope": "total", "party_size": 1, "total": 12114}, "per_person_day": 413.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000373
- request: 青岛 2026-04-24->2026-04-26 days=3 transport=自驾 hotel=舒适型酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2400, "total": 1400, "diff": 1000, "requested_budget": {"available": true, "amount": 6620, "scope": "total", "party_size": 1, "total": 6620}, "per_person_day": 466.67, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000531
- request: 苏州 2026-05-05->2026-05-07 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['购物商圈', '第一次来', '自然风光', '美食']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v2_request_000073
- request: 呼和浩特 2026-08-29->2026-08-31 days=3 transport=公共交通 hotel=民宿 prefs=['城市公园', '博物馆', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 940, "total": 940, "diff": 0, "requested_budget": {"available": true, "amount": 9863, "scope": "per_person", "party_size": 1, "total": 9863}, "per_person_day": 313.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000529
- request: 武汉 2026-06-15->2026-06-19 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '自然风光', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3092, "total": 2092, "diff": 1000, "requested_budget": {"available": true, "amount": 8187, "scope": "per_person", "party_size": 3, "total": 24561}, "per_person_day": 139.47, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3092, "total": 2092, "diff": 1000, "requested_budget": {"available": true, "amount": 8187, "scope": "per_person", "party_size": 3, "total": 24561}, "per_person_day": 139.47, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000736
- request: 哈尔滨 2026-04-01->2026-04-03 days=3 transport=打车 hotel=舒适型酒店 prefs=['自然风光', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2835, "total": 2835, "diff": 0, "requested_budget": {"available": true, "amount": 1069, "scope": "per_person", "party_size": 2, "total": 2138}, "per_person_day": 472.5, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": false, "level_aligned": true, "preference_aligned": false}}]`

### v2_request_000248
- request: 杭州 2026-08-29->2026-09-01 days=4 transport=公共交通 hotel=经济型酒店 prefs=['第一次来', '小众展览', '自然风光', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1620, "total": 1620, "diff": 0, "requested_budget": {"available": true, "amount": 7561, "scope": "per_person", "party_size": 2, "total": 15122}, "per_person_day": 202.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000786
- request: 丽江 2025-08-04->2025-08-06 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市漫步', '购物商圈']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2411, "total": 1411, "diff": 1000, "requested_budget": {"available": true, "amount": 14550, "scope": "total", "party_size": 2, "total": 14550}, "per_person_day": 235.17, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000493
- request: 武汉 2026-08-29->2026-08-30 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '第一次来', '主题乐园', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 743, "total": 743, "diff": 0, "requested_budget": {"available": true, "amount": 16336, "scope": "total", "party_size": 3, "total": 16336}, "per_person_day": 123.83, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000758
- request: 黄山 2026-05-03->2026-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '美食', '博物馆', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1680, "total": 1680, "diff": 0, "requested_budget": {"available": true, "amount": 14936, "scope": "total", "party_size": 3, "total": 14936}, "per_person_day": 140.0, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`
