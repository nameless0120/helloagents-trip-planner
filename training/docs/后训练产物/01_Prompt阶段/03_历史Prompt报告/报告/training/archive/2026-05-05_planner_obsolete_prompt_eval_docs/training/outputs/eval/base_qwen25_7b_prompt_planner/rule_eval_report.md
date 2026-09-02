# Rule Eval Report: base_qwen25_7b_prompt_v3

- records: 91
- generations: `training/outputs/eval/base_qwen25_7b_prompt_v3/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 84 | 91 | 92.31% |
| budget_arithmetic_consistent | 89 | 91 | 97.80% |
| budget_consistent | 89 | 91 | 97.80% |
| budget_level_aligned | 77 | 91 | 84.62% |
| budget_preference_aligned | 76 | 91 | 83.52% |
| budget_within_user_budget | 89 | 91 | 97.80% |
| city_ok | 91 | 91 | 100.00% |
| date_range_ok | 91 | 91 | 100.00% |
| day_dates_ok | 91 | 91 | 100.00% |
| day_index_ok | 91 | 91 | 100.00% |
| days_len_ok | 91 | 91 | 100.00% |
| hard_pass | 84 | 91 | 92.31% |
| invalid_hotel_name_ok | 91 | 91 | 100.00% |
| json_extract_ok | 91 | 91 | 100.00% |
| location_object_ok | 91 | 91 | 100.00% |
| meal_complete | 91 | 91 | 100.00% |
| middle_hotel_ok | 91 | 91 | 100.00% |
| schema_ok | 91 | 91 | 100.00% |
| weather_dates_ok | 91 | 91 | 100.00% |
| weather_match | 91 | 91 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9963,
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
  "budget_preference_mismatch": 15,
  "budget_arithmetic_inconsistent": 2
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2060, "total": 2060, "diff": 0, "requested_budget": {"available": true, "amount": 7219, "scope": "per_person", "party_size": 3, "total": 21657}, "per_person_day": 171.67, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000992
- request: 洛阳 2026-06-30->2026-07-03 days=4 transport=公共交通 hotel=经济型酒店 prefs=['艺术', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2360, "total": 2360, "diff": 0, "requested_budget": {"available": true, "amount": 1414, "scope": "per_person", "party_size": 1, "total": 1414}, "per_person_day": 590.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": false, "level_aligned": true, "preference_aligned": false}}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1574, "total": 1574, "diff": 0, "requested_budget": {"available": true, "amount": 11994, "scope": "per_person", "party_size": 3, "total": 35982}, "per_person_day": 262.33, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1860, "total": 1860, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "per_person", "party_size": 2, "total": 20000}, "per_person_day": 232.5, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2060, "total": 2060, "diff": 0, "requested_budget": {"available": true, "amount": 21693, "scope": "total", "party_size": 2, "total": 21693}, "per_person_day": 257.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4420, "total": 4420, "diff": 0, "requested_budget": {"available": true, "amount": 13616, "scope": "per_person", "party_size": 3, "total": 40848}, "per_person_day": 294.67, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000341
- request: 西安 2026-05-04->2026-05-06 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '摄影']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2230, "total": 2060, "diff": 170, "requested_budget": {"available": true, "amount": 30291, "scope": "total", "party_size": 3, "total": 30291}, "per_person_day": 228.89, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000529
- request: 武汉 2026-06-15->2026-06-19 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '自然风光', '美食']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3682, "total": 3682, "diff": 0, "requested_budget": {"available": true, "amount": 8187, "scope": "per_person", "party_size": 3, "total": 24561}, "per_person_day": 245.47, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000248
- request: 杭州 2026-08-29->2026-09-01 days=4 transport=公共交通 hotel=经济型酒店 prefs=['第一次来', '小众展览', '自然风光', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2060, "total": 2060, "diff": 0, "requested_budget": {"available": true, "amount": 7561, "scope": "per_person", "party_size": 2, "total": 15122}, "per_person_day": 257.5, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000786
- request: 丽江 2025-08-04->2025-08-06 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市漫步', '购物商圈']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2320, "total": 1720, "diff": 600, "requested_budget": {"available": true, "amount": 14550, "scope": "total", "party_size": 2, "total": 14550}, "per_person_day": 286.67, "budget_level": "medium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true}}]`

### v2_request_000801
- request: 丽江 2026-04-24->2026-04-27 days=4 transport=打车 hotel=舒适型酒店 prefs=['自然风光', '城市地标', '清真']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2300, "total": 2300, "diff": 0, "requested_budget": {"available": true, "amount": 17112, "scope": "total", "party_size": 1, "total": 17112}, "per_person_day": 575.0, "budget_level": "luxury", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000933
- request: 成都 2026-01-01->2026-01-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['历史文化', '夜市夜景', '主题乐园', '艺术']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3080, "total": 2700, "diff": 380, "requested_budget": {"available": true, "amount": 22560, "scope": "total", "party_size": 2, "total": 22560}, "per_person_day": 270.0, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000382
- request: 广州 2026-05-02->2026-05-05 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '历史文化', '第一次来', '自然风光']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2480, "total": 2060, "diff": 420, "requested_budget": {"available": true, "amount": 4287, "scope": "per_person", "party_size": 3, "total": 12861}, "per_person_day": 171.67, "budget_level": "medium", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000822
- request: 丽江 2026-05-05->2026-05-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['历史文化', '自然风光']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3200, "total": 2220, "diff": 980, "requested_budget": {"available": true, "amount": 22256, "scope": "total", "party_size": 2, "total": 22256}, "per_person_day": 222.0, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3200, "total": 2220, "diff": 980, "requested_budget": {"available": true, "amount": 22256, "scope": "total", "party_size": 2, "total": 22256}, "per_person_day": 222.0, "budget_level": "upper", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000765
- request: 广州 2026-05-03->2026-05-05 days=3 transport=公共交通 hotel=经济型酒店 prefs=['休闲慢游', '历史文化', '自然风光', '小众展览']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2423, "total": 2423, "diff": 0, "requested_budget": {"available": true, "amount": 1177, "scope": "per_person", "party_size": 1, "total": 1177}, "per_person_day": 807.67, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": false, "level_aligned": false, "preference_aligned": false}}]`

### v2_request_000188
- request: 泉州 2026-06-30->2026-07-02 days=3 transport=打车 hotel=舒适型酒店 prefs=['亲子', '摄影', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2033, "total": 2033, "diff": 0, "requested_budget": {"available": true, "amount": 5723, "scope": "per_person", "party_size": 3, "total": 17169}, "per_person_day": 225.89, "budget_level": "upper", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false}}]`
