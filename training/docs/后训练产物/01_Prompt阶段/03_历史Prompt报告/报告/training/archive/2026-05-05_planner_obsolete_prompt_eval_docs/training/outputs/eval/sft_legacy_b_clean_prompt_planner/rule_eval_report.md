# Rule Eval Report: sft_v2_clean_prompt_v3

- records: 91
- generations: `training/outputs/eval/sft_v2_clean_prompt_v3/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 90 | 90 | 100.00% |
| budget_arithmetic_consistent | 79 | 90 | 87.78% |
| budget_consistent | 79 | 90 | 87.78% |
| budget_level_aligned | 61 | 90 | 67.78% |
| budget_preference_aligned | 60 | 90 | 66.67% |
| budget_within_user_budget | 89 | 90 | 98.89% |
| city_ok | 90 | 90 | 100.00% |
| date_range_ok | 89 | 90 | 98.89% |
| day_dates_ok | 90 | 90 | 100.00% |
| day_index_ok | 90 | 90 | 100.00% |
| days_len_ok | 90 | 90 | 100.00% |
| hard_pass | 89 | 90 | 98.89% |
| invalid_hotel_name_ok | 90 | 90 | 100.00% |
| json_extract_ok | 91 | 91 | 100.00% |
| location_object_ok | 90 | 90 | 100.00% |
| meal_complete | 90 | 90 | 100.00% |
| middle_hotel_ok | 90 | 90 | 100.00% |
| schema_ok | 90 | 91 | 98.90% |
| weather_dates_ok | 90 | 90 | 100.00% |
| weather_match | 90 | 90 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9889,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "budget_preference_mismatch": 30,
  "budget_arithmetic_inconsistent": 11,
  "schema": 1
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1848, "total": 1848, "diff": 0, "requested_budget": {"available": true, "amount": 7219, "scope": "per_person", "party_size": 3, "total": 21657}, "per_person_day": 154.0, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000866
- request: 南京 2026-04-24->2026-04-28 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '摄影', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3680, "total": 2680, "diff": 1000, "requested_budget": {"available": true, "amount": 4865, "scope": "per_person", "party_size": 3, "total": 14595}, "per_person_day": 178.67, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3680, "total": 2680, "diff": 1000, "requested_budget": {"available": true, "amount": 4865, "scope": "per_person", "party_size": 3, "total": 14595}, "per_person_day": 178.67, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000381
- request: 北京 2026-04-27->2026-04-29 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['第一次来', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3020, "total": 2020, "diff": 1000, "requested_budget": {"available": true, "amount": 2517, "scope": "per_person", "party_size": 2, "total": 5034}, "per_person_day": 336.67, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000864
- request: 昆明 2026-05-03->2026-05-04 days=2 transport=打车 hotel=经济型酒店 prefs=['亲子', '美食', '历史文化', '小众展览']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1144, "total": 744, "diff": 400, "requested_budget": {"available": true, "amount": 7980, "scope": "total", "party_size": 3, "total": 7980}, "per_person_day": 124.0, "budget_level": "limited", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1550, "total": 1550, "diff": 0, "requested_budget": {"available": true, "amount": 11994, "scope": "per_person", "party_size": 3, "total": 35982}, "per_person_day": 258.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1650, "total": 1650, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "per_person", "party_size": 2, "total": 20000}, "per_person_day": 206.25, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2470, "total": 2570, "diff": -100, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 321.25, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000435
- request: 长沙 2026-04-24->2026-04-25 days=2 transport=地铁+步行 hotel=民宿 prefs=['休闲慢游', '城市地标', '清真']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 710, "total": 410, "diff": 300, "requested_budget": {"available": true, "amount": 10461, "scope": "total", "party_size": 2, "total": 10461}, "per_person_day": 102.5, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 710, "total": 410, "diff": 300, "requested_budget": {"available": true, "amount": 10461, "scope": "total", "party_size": 2, "total": 10461}, "per_person_day": 102.5, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3060, "total": 2060, "diff": 1000, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 137.33, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3060, "total": 2060, "diff": 1000, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 137.33, "budget_level": "luxury", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000116
- request: 大理 2026-05-03->2026-05-06 days=4 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市公园', '休闲慢游', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2000, "total": 1900, "diff": 100, "requested_budget": {"available": true, "amount": 17036, "scope": "total", "party_size": 3, "total": 17036}, "per_person_day": 158.33, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000341
- request: 西安 2026-05-04->2026-05-06 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1561, "total": 1561, "diff": 0, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 173.44, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000284
- request: 宁波 2026-06-15->2026-06-18 days=4 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '摄影', '休闲慢游', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2080, "diff": 1000, "requested_budget": {"available": true, "amount": 4499, "scope": "per_person", "party_size": 3, "total": 13497}, "per_person_day": 173.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3080, "total": 2080, "diff": 1000, "requested_budget": {"available": true, "amount": 4499, "scope": "per_person", "party_size": 3, "total": 13497}, "per_person_day": 173.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000242
- request: 呼和浩特 2025-08-04->2025-08-07 days=4 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '美食', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2420, "total": 1420, "diff": 1000, "requested_budget": {"available": true, "amount": 15882, "scope": "total", "party_size": 3, "total": 15882}, "per_person_day": 118.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2420, "total": 1420, "diff": 1000, "requested_budget": {"available": true, "amount": 15882, "scope": "total", "party_size": 3, "total": 15882}, "per_person_day": 118.33, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000146
- request: 贵阳 2026-01-31->2026-02-02 days=3 transport=地铁+步行 hotel=民宿 prefs=['城市公园', '城市地标', '夜市夜景', '自然风光']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1348, "total": 1348, "diff": 0, "requested_budget": {"available": true, "amount": 12114, "scope": "total", "party_size": 1, "total": 12114}, "per_person_day": 449.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000073
- request: 呼和浩特 2026-08-29->2026-08-31 days=3 transport=公共交通 hotel=民宿 prefs=['城市公园', '博物馆', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1030, "total": 1030, "diff": 0, "requested_budget": {"available": true, "amount": 9863, "scope": "per_person", "party_size": 1, "total": 9863}, "per_person_day": 343.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000529
- request: 武汉 2026-06-15->2026-06-19 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '自然风光', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3002, "total": 2902, "diff": 100, "requested_budget": {"available": true, "amount": 8187, "scope": "per_person", "party_size": 3, "total": 24561}, "per_person_day": 193.47, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000248
- request: 杭州 2026-08-29->2026-09-01 days=4 transport=公共交通 hotel=经济型酒店 prefs=['第一次来', '小众展览', '自然风光', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1468, "total": 1468, "diff": 0, "requested_budget": {"available": true, "amount": 7561, "scope": "per_person", "party_size": 2, "total": 15122}, "per_person_day": 183.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000493
- request: 武汉 2026-08-29->2026-08-30 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '第一次来', '主题乐园', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 986, "total": 986, "diff": 0, "requested_budget": {"available": true, "amount": 16336, "scope": "total", "party_size": 3, "total": 16336}, "per_person_day": 164.33, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000758
- request: 黄山 2026-05-03->2026-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '美食', '博物馆', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1470, "total": 1470, "diff": 0, "requested_budget": {"available": true, "amount": 14936, "scope": "total", "party_size": 3, "total": 14936}, "per_person_day": 122.5, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000117
- request: 大理 2026-01-31->2026-02-02 days=3 transport=打车 hotel=经济型酒店 prefs=['亲子', '购物商圈', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1610, "total": 1510, "diff": 100, "requested_budget": {"available": true, "amount": 4850, "scope": "per_person", "party_size": 3, "total": 14550}, "per_person_day": 167.78, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`
