# Rule Eval Report: 260511_high_end_context_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260511_replay_usage700_from_lr6e5_lr2e5/260511_high_end_context_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 66 | 200 | 33.00% |
| attraction_budget_party_relation_ok | 198 | 200 | 99.00% |
| attraction_count_ok | 198 | 200 | 99.00% |
| attraction_diversity_ok | 188 | 200 | 94.00% |
| attraction_grounding_ok | 198 | 200 | 99.00% |
| attraction_repeat_limit_ok | 188 | 200 | 94.00% |
| budget_arithmetic_consistent | 127 | 200 | 63.50% |
| budget_consistent | 127 | 200 | 63.50% |
| budget_level_aligned | 158 | 200 | 79.00% |
| budget_preference_aligned | 158 | 200 | 79.00% |
| budget_relationship_ok | 162 | 200 | 81.00% |
| budget_selection_ok | 124 | 200 | 62.00% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 194 | 200 | 97.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 122 | 200 | 61.00% |
| dpo_soft_recomputed_budget_pass | 101 | 200 | 50.50% |
| hard_pass | 191 | 200 | 95.50% |
| hotel_budget_covers_nights | 195 | 200 | 97.50% |
| hotel_budget_relation_ok | 198 | 200 | 99.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 108 | 200 | 54.00% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 2 | 200 | 1.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 166 | 200 | 83.00% |
| meal_diversity_ok | 175 | 200 | 87.50% |
| meal_grounding_ok | 196 | 200 | 98.00% |
| meal_lunch_dinner_same_day_ok | 195 | 200 | 97.50% |
| meal_repeat_limit_ok | 180 | 200 | 90.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 197 | 200 | 98.50% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 124 | 200 | 62.00% |
| recomputed_budget_hard_ok | 198 | 200 | 99.00% |
| recomputed_budget_level_aligned | 124 | 200 | 62.00% |
| recomputed_budget_preference_aligned | 124 | 200 | 62.00% |
| recomputed_budget_user_constraint_ok | 198 | 200 | 99.00% |
| recomputed_budget_within_user_budget | 184 | 200 | 92.00% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 153 | 200 | 76.50% |
| sft_hard_pass | 191 | 200 | 95.50% |
| sft_no_budget_sum_hard_pass | 191 | 200 | 95.50% |
| sft_strict_hard_pass | 1 | 200 | 0.50% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 199 | 200 | 99.50% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9923,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9171,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 733.9649,
    "p50": 576.75,
    "p90": 1252.67
  },
  "recomputed_budget_total": {
    "avg": 6879.065,
    "p50": 5704.0,
    "p90": 14055.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 198,
  "attraction_budget_inconsistent": 134,
  "budget_arithmetic_inconsistent": 73,
  "budget_preference_mismatch": 42,
  "budget_relationship_mismatch": 38,
  "meal_cost_scale_too_low": 34,
  "meal_repeat_too_many": 20,
  "attraction_repeat_too_many": 12,
  "hotel_budget_underestimated": 5,
  "meal_same_day_lunch_dinner_repeat": 5,
  "meal_invalid_name": 3,
  "too_many_attractions": 2,
  "meal_grounding_miss": 1,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 738, "expected_total_meals": 1476, "reported_total_meals": 2300, "reported_total_transportation": 2400}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 750, "meal_per_person_cost_sum": 811, "expected_total_meals": 1622, "reported_total_meals": 2184, "reported_total_transportation": 900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 750, "meal_per_person_cost_sum": 811, "expected_total_meals": 1622, "reported_total_meals": 2184, "reported_total_transportation": 900}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 761, "expected_total_meals": 1522, "reported_total_meals": 1540, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 467, "expected_total_meals": 934, "reported_total_meals": 1084, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 250, "expected_total_attractions": 500, "reported_total_attractions": 480, "meal_per_person_cost_sum": 648, "expected_total_meals": 1296, "reported_total_meals": 1000, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 250, "expected_total_attractions": 500, "reported_total_attractions": 480, "meal_per_person_cost_sum": 648, "expected_total_meals": 1296, "reported_total_meals": 1000, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5079, "total": 4979, "diff": 100, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 3, "total": 5600, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 414.92, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 5900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 808, "expected_total_meals": 2424, "reported_total_meals": 2169, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 808, "expected_total_meals": 2424, "reported_total_meals": 2169, "reported_total_transportation": 1200}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 221, "expected_total_attractions": 884, "reported_total_attractions": 964, "meal_per_person_cost_sum": 701, "expected_total_meals": 2804, "reported_total_meals": 2836, "reported_total_transportation": 1600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 221, "expected_total_attractions": 884, "reported_total_attractions": 964, "meal_per_person_cost_sum": 701, "expected_total_meals": 2804, "reported_total_meals": 2836, "reported_total_transportation": 1600}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 719, "expected_total_meals": 1438, "reported_total_meals": 1636, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 719, "expected_total_meals": 1438, "reported_total_meals": 1636, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4050, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 373, "expected_total_attractions": 1119, "reported_total_attractions": 1059, "meal_per_person_cost_sum": 927, "expected_total_meals": 2781, "reported_total_meals": 3936, "reported_total_transportation": 6565}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 373, "expected_total_attractions": 1119, "reported_total_attractions": 1059, "meal_per_person_cost_sum": 927, "expected_total_meals": 2781, "reported_total_meals": 3936, "reported_total_transportation": 6565}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-05-04", "day_index": 3, "name": "杭州西湖风景名胜区-太子湾公园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 190, "meal_per_person_cost_sum": 1117, "expected_total_meals": 1117, "reported_total_meals": 1030, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 190, "meal_per_person_cost_sum": 1117, "expected_total_meals": 1117, "reported_total_meals": 1030, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 581, "expected_total_meals": 2324, "reported_total_meals": 1820, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 505, "expected_total_meals": 3030, "reported_total_meals": 4518, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 505, "expected_total_meals": 3030, "reported_total_meals": 4518, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2503, "total": 2403, "diff": 100, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 400.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 371, "expected_total_meals": 1113, "reported_total_meals": 1053, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 371, "expected_total_meals": 1113, "reported_total_meals": 1053, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1984, "total": 2084, "diff": -100, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 347.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 310, "expected_total_meals": 620, "reported_total_meals": 714, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_per_person_cost_sum": 661, "expected_total_meals": 1322, "reported_total_meals": 1550, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_per_person_cost_sum": 661, "expected_total_meals": 1322, "reported_total_meals": 1550, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 845, "expected_total_attractions": 2535, "reported_total_attractions": 2445, "meal_per_person_cost_sum": 443, "expected_total_meals": 1329, "reported_total_meals": 1836, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 845, "expected_total_attractions": 2535, "reported_total_attractions": 2445, "meal_per_person_cost_sum": 443, "expected_total_meals": 1329, "reported_total_meals": 1836, "reported_total_transportation": 1200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 701, "expected_total_attractions": 2103, "reported_total_attractions": 2163, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 5637, "reported_total_transportation": 1700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 701, "expected_total_attractions": 2103, "reported_total_attractions": 2163, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 5637, "reported_total_transportation": 1700}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 120, "reported_total_attractions": 120, "meal_per_person_cost_sum": 601, "expected_total_meals": 1202, "reported_total_meals": 994, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州博物馆西馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "苏州博物馆西馆"}, {"date": "2026-05-03", "day_index": 3, "name": "苏州博物馆西馆"}]}, {"name_key": "苏州丝绸博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "苏州丝绸博物馆"}, {"date": "2026-05-04", "day_index": 4, "name": "苏州丝绸博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16350, "total": 14350, "diff": 2000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 717.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 10800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 850, "expected_total_attractions": 3400, "reported_total_attractions": 3160, "meal_per_person_cost_sum": 1177, "expected_total_meals": 4708, "reported_total_meals": 2240, "reported_total_transportation": 150}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 345, "reported_total_attractions": 395, "meal_per_person_cost_sum": 413, "expected_total_meals": 1239, "reported_total_meals": 1209, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 345, "reported_total_attractions": 395, "meal_per_person_cost_sum": 413, "expected_total_meals": 1239, "reported_total_meals": 1209, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2404, "total": 2404, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 400.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 4300, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2600, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
