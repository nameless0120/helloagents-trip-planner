# Rule Eval Report: 260507_realbudget_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v2b/260507_realbudget_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 298 | 298 | 100.00% |
| attraction_budget_consistent | 43 | 298 | 14.43% |
| attraction_budget_party_relation_ok | 235 | 298 | 78.86% |
| attraction_count_ok | 295 | 298 | 98.99% |
| attraction_diversity_ok | 238 | 298 | 79.87% |
| attraction_grounding_ok | 290 | 298 | 97.32% |
| attraction_repeat_limit_ok | 238 | 298 | 79.87% |
| budget_arithmetic_consistent | 217 | 298 | 72.82% |
| budget_consistent | 217 | 298 | 72.82% |
| budget_level_aligned | 237 | 298 | 79.53% |
| budget_preference_aligned | 237 | 298 | 79.53% |
| budget_relationship_ok | 108 | 298 | 36.24% |
| budget_selection_ok | 163 | 298 | 54.70% |
| budget_user_constraint_ok | 281 | 298 | 94.30% |
| budget_within_user_budget | 290 | 298 | 97.32% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 160 | 298 | 53.69% |
| dpo_soft_recomputed_budget_pass | 113 | 298 | 37.92% |
| hard_pass | 280 | 298 | 93.96% |
| hotel_budget_covers_nights | 197 | 298 | 66.11% |
| hotel_budget_relation_ok | 214 | 298 | 71.81% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 298 | 298 | 100.00% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 115 | 298 | 38.59% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 0 | 298 | 0.00% |
| meal_complete | 298 | 298 | 100.00% |
| meal_cost_scale_ok | 189 | 298 | 63.42% |
| meal_diversity_ok | 256 | 298 | 85.91% |
| meal_grounding_ok | 291 | 298 | 97.65% |
| meal_lunch_dinner_same_day_ok | 288 | 298 | 96.64% |
| meal_repeat_limit_ok | 263 | 298 | 88.26% |
| meal_specific_ok | 298 | 298 | 100.00% |
| meal_valid_semantics_ok | 292 | 298 | 97.99% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| recomputed_budget_fit_ok | 163 | 298 | 54.70% |
| recomputed_budget_hard_ok | 267 | 298 | 89.60% |
| recomputed_budget_level_aligned | 163 | 298 | 54.70% |
| recomputed_budget_preference_aligned | 163 | 298 | 54.70% |
| recomputed_budget_user_constraint_ok | 267 | 298 | 89.60% |
| recomputed_budget_within_user_budget | 289 | 298 | 96.98% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 87 | 298 | 29.19% |
| sft_hard_pass | 280 | 298 | 93.96% |
| sft_no_budget_sum_hard_pass | 280 | 298 | 93.96% |
| sft_strict_hard_pass | 0 | 298 | 0.00% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 298 | 298 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9749,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9972,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8619,
    "p50": 0.8889,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 731.53,
    "p50": 689.6,
    "p90": 1133.25
  },
  "recomputed_budget_total": {
    "avg": 7881.5839,
    "p50": 6872.0,
    "p90": 13914.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "attraction_budget_inconsistent": 255,
  "budget_relationship_mismatch": 190,
  "meal_cost_scale_too_low": 109,
  "hotel_budget_underestimated": 101,
  "budget_arithmetic_inconsistent": 81,
  "budget_preference_mismatch": 61,
  "attraction_repeat_too_many": 60,
  "meal_repeat_too_many": 35,
  "budget_hard_constraint_exceeded": 17,
  "meal_same_day_lunch_dinner_repeat": 10,
  "meal_invalid_name": 6,
  "too_many_attractions": 3,
  "json_extract": 1,
  "schema": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 638, "expected_total_attractions": 638, "reported_total_attractions": 756, "meal_per_person_cost_sum": 496, "expected_total_meals": 496, "reported_total_meals": 682, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 638, "expected_total_attractions": 638, "reported_total_attractions": 756, "meal_per_person_cost_sum": 496, "expected_total_meals": 496, "reported_total_meals": 682, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理之眼梦幻大剧场", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 1, "name": "大理之眼梦幻大剧场(装修中)"}, {"date": "2026-05-13", "day_index": 2, "name": "大理之眼梦幻大剧场(装修中)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 257, "expected_total_attractions": 771, "reported_total_attractions": 888, "meal_per_person_cost_sum": 474, "expected_total_meals": 1422, "reported_total_meals": 1638, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 257, "expected_total_attractions": 771, "reported_total_attractions": 888, "meal_per_person_cost_sum": 474, "expected_total_meals": 1422, "reported_total_meals": 1638, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11001, "total": 10901, "diff": 100, "requested_budget": {"available": true, "amount": 9000, "scope": "total", "party_size": 3, "total": 9000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 908.42, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 9000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5400, "target_max_total": 9000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 465, "meal_per_person_cost_sum": 687, "expected_total_meals": 2061, "reported_total_meals": 1836, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 465, "meal_per_person_cost_sum": 687, "expected_total_meals": 2061, "reported_total_meals": 1836, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11000, "total": 10000, "diff": 1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1250.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1300, "meal_per_person_cost_sum": 591, "expected_total_meals": 1182, "reported_total_meals": 1600, "reported_total_transportation": 900}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 600, "reported_total_attractions": 440, "meal_per_person_cost_sum": 592, "expected_total_meals": 2368, "reported_total_meals": 2064, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 600, "reported_total_attractions": 440, "meal_per_person_cost_sum": 592, "expected_total_meals": 2368, "reported_total_meals": 2064, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 600, "reported_total_attractions": 440, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 678, "meal_per_person_cost_sum": 684, "expected_total_meals": 1368, "reported_total_meals": 1754, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 678, "meal_per_person_cost_sum": 684, "expected_total_meals": 1368, "reported_total_meals": 1754, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 220, "meal_per_person_cost_sum": 1251, "expected_total_meals": 1251, "reported_total_meals": 1410, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 220, "meal_per_person_cost_sum": 1251, "expected_total_meals": 1251, "reported_total_meals": 1410, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9100, "total": 10000, "diff": -900, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1000.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 311, "expected_total_attractions": 622, "reported_total_attractions": 542, "meal_per_person_cost_sum": 2215, "expected_total_meals": 4430, "reported_total_meals": 5558, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安钟楼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "西安钟楼"}, {"date": "2026-08-07", "day_index": 2, "name": "西安钟楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 9000, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 349, "expected_total_attractions": 1745, "reported_total_attractions": 1875, "meal_per_person_cost_sum": 802, "expected_total_meals": 4010, "reported_total_meals": 4915, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "云南美术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-09", "day_index": 2, "name": "云南美术馆(五一路)"}, {"date": "2026-04-10", "day_index": 3, "name": "云南美术馆(五一路)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 652, "expected_total_attractions": 3260, "reported_total_attractions": 3375, "meal_per_person_cost_sum": 833, "expected_total_meals": 4165, "reported_total_meals": 5850, "reported_total_transportation": 4000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-01", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-02", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-03", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "馋遇江南·隐轩精致雅宴", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "馋遇江南·隐轩精致雅宴(相城店)"}, {"date": "2026-05-01", "type": "dinner", "name": "馋遇江南·隐轩精致雅宴(相城店)"}, {"date": "2026-05-02", "type": "dinner", "name": "馋遇江南·隐轩精致雅宴(相城店)"}, {"date": "2026-05-03", "type": "dinner", "name": "馋遇江南·隐轩精致雅宴(相城店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1660, "meal_per_person_cost_sum": 1556, "expected_total_meals": 6224, "reported_total_meals": 3440, "reported_total_transportation": 3000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1660, "meal_per_person_cost_sum": 1556, "expected_total_meals": 6224, "reported_total_meals": 3440, "reported_total_transportation": 3000}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "成都博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-06", "day_index": 0, "name": "成都博物馆"}, {"date": "2026-06-07", "day_index": 1, "name": "成都博物馆"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 656, "expected_total_meals": 656, "reported_total_meals": 720, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2385, "total": 2385, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 795.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10100, "total": 10000, "diff": 100, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1250.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 1494, "expected_total_meals": 2988, "reported_total_meals": 3946, "reported_total_transportation": 1400}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5300, "total": 4300, "diff": 1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 268.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 405, "expected_total_attractions": 1620, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 577, "expected_total_meals": 2308, "reported_total_meals": 1768, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 405, "expected_total_attractions": 1620, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 577, "expected_total_meals": 2308, "reported_total_meals": 1768, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8184, "total": 5984, "diff": 2200, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 664.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 223, "expected_total_attractions": 669, "reported_total_attractions": 639, "meal_per_person_cost_sum": 937, "expected_total_meals": 2811, "reported_total_meals": 2545, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 223, "expected_total_attractions": 669, "reported_total_attractions": 639, "meal_per_person_cost_sum": 937, "expected_total_meals": 2811, "reported_total_meals": 2545, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 480, "expected_total_attractions": 1440, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 851, "expected_total_meals": 2553, "reported_total_meals": 2850, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 12290, "total": 12290, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 1024.17, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 12290, "total": 12290, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 1024.17, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "留园"}, {"date": "2026-05-13", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 376, "expected_total_attractions": 752, "reported_total_attractions": 860, "meal_per_person_cost_sum": 1013, "expected_total_meals": 2026, "reported_total_meals": 2858, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 740, "expected_total_attractions": 1480, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 693, "expected_total_meals": 1386, "reported_total_meals": 2064, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 740, "expected_total_attractions": 1480, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 693, "expected_total_meals": 1386, "reported_total_meals": 2064, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-09", "day_index": 0, "name": "汉口江滩"}, {"date": "2026-05-13", "day_index": 4, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5200, "total": 5100, "diff": 100, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 510.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-24", "day_index": 3, "name": "杭州植物园"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 386, "expected_total_attractions": 1930, "reported_total_attractions": 2700, "meal_per_person_cost_sum": 1050, "expected_total_meals": 5250, "reported_total_meals": 4960, "reported_total_transportation": 10000}}]`
