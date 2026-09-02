# Rule Eval Report: 260511_high_end_context_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260509_main_clean_cp2_v2b_valloss_lr8e5/260511_high_end_context_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 198 | 198 | 100.00% |
| attraction_budget_consistent | 64 | 198 | 32.32% |
| attraction_budget_party_relation_ok | 172 | 198 | 86.87% |
| attraction_count_ok | 195 | 198 | 98.48% |
| attraction_diversity_ok | 182 | 198 | 91.92% |
| attraction_grounding_ok | 196 | 198 | 98.99% |
| attraction_repeat_limit_ok | 182 | 198 | 91.92% |
| budget_arithmetic_consistent | 151 | 198 | 76.26% |
| budget_consistent | 151 | 198 | 76.26% |
| budget_level_aligned | 153 | 198 | 77.27% |
| budget_preference_aligned | 153 | 198 | 77.27% |
| budget_relationship_ok | 112 | 198 | 56.57% |
| budget_selection_ok | 113 | 198 | 57.07% |
| budget_user_constraint_ok | 196 | 198 | 98.99% |
| budget_within_user_budget | 197 | 198 | 99.49% |
| city_ok | 198 | 198 | 100.00% |
| date_range_ok | 198 | 198 | 100.00% |
| day_dates_ok | 198 | 198 | 100.00% |
| day_index_ok | 198 | 198 | 100.00% |
| days_len_ok | 198 | 198 | 100.00% |
| dpo_soft_pass | 121 | 198 | 61.11% |
| dpo_soft_recomputed_budget_pass | 90 | 198 | 45.45% |
| hard_pass | 191 | 198 | 96.46% |
| hotel_budget_covers_nights | 163 | 198 | 82.32% |
| hotel_budget_relation_ok | 171 | 198 | 86.36% |
| hotel_distance_placeholder_ok | 198 | 198 | 100.00% |
| hotel_grounding_ok | 198 | 198 | 100.00% |
| invalid_hotel_name_ok | 198 | 198 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 105 | 198 | 53.03% |
| location_object_ok | 198 | 198 | 100.00% |
| meal_budget_consistent | 0 | 198 | 0.00% |
| meal_complete | 198 | 198 | 100.00% |
| meal_cost_scale_ok | 145 | 198 | 73.23% |
| meal_diversity_ok | 175 | 198 | 88.38% |
| meal_grounding_ok | 195 | 198 | 98.48% |
| meal_lunch_dinner_same_day_ok | 189 | 198 | 95.45% |
| meal_repeat_limit_ok | 181 | 198 | 91.41% |
| meal_specific_ok | 198 | 198 | 100.00% |
| meal_valid_semantics_ok | 197 | 198 | 99.49% |
| middle_hotel_ok | 198 | 198 | 100.00% |
| recomputed_budget_fit_ok | 113 | 198 | 57.07% |
| recomputed_budget_hard_ok | 195 | 198 | 98.48% |
| recomputed_budget_level_aligned | 113 | 198 | 57.07% |
| recomputed_budget_preference_aligned | 113 | 198 | 57.07% |
| recomputed_budget_user_constraint_ok | 195 | 198 | 98.48% |
| recomputed_budget_within_user_budget | 189 | 198 | 95.45% |
| schema_ok | 198 | 200 | 99.00% |
| sft_budget_semantic_hard_pass | 101 | 198 | 51.01% |
| sft_hard_pass | 191 | 198 | 96.46% |
| sft_no_budget_sum_hard_pass | 191 | 198 | 96.46% |
| sft_strict_hard_pass | 0 | 198 | 0.00% |
| transportation_budget_nonnegative | 198 | 198 | 100.00% |
| weather_dates_ok | 198 | 198 | 100.00% |
| weather_match | 198 | 198 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9908,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8928,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 671.1392,
    "p50": 552.25,
    "p90": 1161.58
  },
  "recomputed_budget_total": {
    "avg": 6332.5051,
    "p50": 4808.0,
    "p90": 12475.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 198,
  "attraction_budget_inconsistent": 134,
  "budget_relationship_mismatch": 86,
  "meal_cost_scale_too_low": 53,
  "budget_arithmetic_inconsistent": 47,
  "budget_preference_mismatch": 45,
  "hotel_budget_underestimated": 35,
  "meal_repeat_too_many": 17,
  "attraction_repeat_too_many": 16,
  "meal_same_day_lunch_dinner_repeat": 9,
  "too_many_attractions": 3,
  "budget_hard_constraint_exceeded": 2,
  "schema": 2,
  "meal_grounding_miss": 2,
  "meal_invalid_name": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 465, "expected_total_meals": 930, "reported_total_meals": 1040, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 465, "expected_total_meals": 930, "reported_total_meals": 1040, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 4600, "diff": 2000, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 502, "expected_total_meals": 1004, "reported_total_meals": 1980, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2600, "reported_total_hotels": 4600, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-04-08", "type": "dinner", "name": "湖景坊·经典云南菜·过桥米线(海埂公园店)", "estimated_cost": 57, "min_expected_cost": 70}, {"date": "2026-04-09", "type": "dinner", "name": "菌小厨野生菌火锅(文明街传统老字号商街店)", "estimated_cost": 60, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 682, "expected_total_meals": 1364, "reported_total_meals": 1404, "reported_total_transportation": 250}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 682, "expected_total_meals": 1364, "reported_total_meals": 1404, "reported_total_transportation": 250}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3524, "total": 3524, "diff": 0, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 587.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 180, "expected_total_attractions": 360, "reported_total_attractions": 320, "meal_per_person_cost_sum": 467, "expected_total_meals": 934, "reported_total_meals": 1060, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 180, "expected_total_attractions": 360, "reported_total_attractions": 320, "meal_per_person_cost_sum": 467, "expected_total_meals": 934, "reported_total_meals": 1060, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 771, "expected_total_meals": 1542, "reported_total_meals": 1570, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 704, "expected_total_meals": 2112, "reported_total_meals": 2061, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 704, "expected_total_meals": 2112, "reported_total_meals": 2061, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1500, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 568, "meal_per_person_cost_sum": 597, "expected_total_meals": 1194, "reported_total_meals": 1732, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 568, "meal_per_person_cost_sum": 597, "expected_total_meals": 1194, "reported_total_meals": 1732, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 522, "expected_total_attractions": 2088, "reported_total_attractions": 2164, "meal_per_person_cost_sum": 747, "expected_total_meals": 2988, "reported_total_meals": 2904, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 522, "expected_total_attractions": 2088, "reported_total_attractions": 2164, "meal_per_person_cost_sum": 747, "expected_total_meals": 2988, "reported_total_meals": 2904, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1038, "meal_per_person_cost_sum": 763, "expected_total_meals": 2289, "reported_total_meals": 2762, "reported_total_transportation": 1100}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-断桥残雪", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州西湖风景名胜区-断桥残雪"}, {"date": "2026-05-05", "day_index": 4, "name": "杭州西湖风景名胜区-断桥残雪"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 200, "meal_per_person_cost_sum": 1011, "expected_total_meals": 1011, "reported_total_meals": 1100, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 200, "meal_per_person_cost_sum": 1011, "expected_total_meals": 1011, "reported_total_meals": 1100, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 530, "expected_total_meals": 2120, "reported_total_meals": 1840, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7556, "total": 7456, "diff": 100, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 414.22, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 559, "expected_total_meals": 3354, "reported_total_meals": 3360, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 559, "expected_total_meals": 3354, "reported_total_meals": 3360, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 702, "expected_total_meals": 1404, "reported_total_meals": 1418, "reported_total_transportation": 1700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 702, "expected_total_meals": 1404, "reported_total_meals": 1418, "reported_total_transportation": 1700}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 450, "meal_per_person_cost_sum": 293, "expected_total_meals": 879, "reported_total_meals": 1053, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 450, "meal_per_person_cost_sum": 293, "expected_total_meals": 879, "reported_total_meals": 1053, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 2703, "total": 2703, "diff": 0, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 450.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 435, "meal_per_person_cost_sum": 403, "expected_total_meals": 1209, "reported_total_meals": 1194, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 435, "meal_per_person_cost_sum": 403, "expected_total_meals": 1209, "reported_total_meals": 1194, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_per_person_cost_sum": 286, "expected_total_meals": 572, "reported_total_meals": 698, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_per_person_cost_sum": 286, "expected_total_meals": 572, "reported_total_meals": 698, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-06-07", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "dinner", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 1250, "expected_total_meals": 3750, "reported_total_meals": 4938, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 1250, "expected_total_meals": 3750, "reported_total_meals": 4938, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 15438, "total": 15438, "diff": 0, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1286.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 7800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 120, "reported_total_attractions": 120, "meal_per_person_cost_sum": 345, "expected_total_meals": 690, "reported_total_meals": 620, "reported_total_transportation": 380}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17300, "total": 14300, "diff": 3000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 715.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 10800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 480, "expected_total_attractions": 1920, "reported_total_attractions": 2120, "meal_per_person_cost_sum": 1342, "expected_total_meals": 5368, "reported_total_meals": 3380, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 480, "expected_total_attractions": 1920, "reported_total_attractions": 2120, "meal_per_person_cost_sum": 1342, "expected_total_meals": 5368, "reported_total_meals": 3380, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 325, "expected_total_meals": 975, "reported_total_meals": 1236, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 325, "expected_total_meals": 975, "reported_total_meals": 1236, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 6, "checked_count": 4, "failure_count": 1, "failures": [{"date": "2026-04-08", "type": "dinner", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`
