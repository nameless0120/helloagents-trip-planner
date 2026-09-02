# Rule Eval Report: 260513_bestofn1200_retry_ckpt156_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_ckpt156/260513_bestofn1200_retry_ckpt156_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 199 | 199 | 100.00% |
| attraction_budget_consistent | 76 | 199 | 38.19% |
| attraction_budget_party_relation_ok | 197 | 199 | 98.99% |
| attraction_count_ok | 199 | 199 | 100.00% |
| attraction_diversity_ok | 182 | 199 | 91.46% |
| attraction_grounding_ok | 198 | 199 | 99.50% |
| attraction_repeat_limit_ok | 182 | 199 | 91.46% |
| budget_arithmetic_consistent | 135 | 199 | 67.84% |
| budget_consistent | 135 | 199 | 67.84% |
| budget_level_aligned | 156 | 199 | 78.39% |
| budget_preference_aligned | 156 | 199 | 78.39% |
| budget_relationship_ok | 165 | 199 | 82.91% |
| budget_selection_ok | 124 | 199 | 62.31% |
| budget_user_constraint_ok | 199 | 199 | 100.00% |
| budget_within_user_budget | 196 | 199 | 98.49% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 128 | 199 | 64.32% |
| dpo_soft_recomputed_budget_pass | 108 | 199 | 54.27% |
| hard_pass | 195 | 199 | 97.99% |
| hotel_budget_covers_nights | 196 | 199 | 98.49% |
| hotel_budget_relation_ok | 198 | 199 | 99.50% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 199 | 200 | 99.50% |
| legacy_hard_pass | 118 | 199 | 59.30% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 3 | 199 | 1.51% |
| meal_complete | 199 | 199 | 100.00% |
| meal_cost_scale_ok | 168 | 199 | 84.42% |
| meal_diversity_ok | 175 | 199 | 87.94% |
| meal_grounding_ok | 196 | 199 | 98.49% |
| meal_lunch_dinner_same_day_ok | 192 | 199 | 96.48% |
| meal_repeat_limit_ok | 180 | 199 | 90.45% |
| meal_specific_ok | 199 | 199 | 100.00% |
| meal_valid_semantics_ok | 196 | 199 | 98.49% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 124 | 199 | 62.31% |
| recomputed_budget_hard_ok | 196 | 199 | 98.49% |
| recomputed_budget_level_aligned | 124 | 199 | 62.31% |
| recomputed_budget_preference_aligned | 124 | 199 | 62.31% |
| recomputed_budget_user_constraint_ok | 196 | 199 | 98.49% |
| recomputed_budget_within_user_budget | 183 | 199 | 91.96% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 161 | 199 | 80.90% |
| sft_hard_pass | 195 | 199 | 97.99% |
| sft_no_budget_sum_hard_pass | 195 | 199 | 97.99% |
| sft_strict_hard_pass | 1 | 199 | 0.50% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9261,
    "p50": 1.0,
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
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 721.3502,
    "p50": 558.5,
    "p90": 1225.75
  },
  "recomputed_budget_total": {
    "avg": 6787.809,
    "p50": 5690.0,
    "p90": 13316.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 196,
  "attraction_budget_inconsistent": 123,
  "budget_arithmetic_inconsistent": 64,
  "budget_preference_mismatch": 43,
  "budget_relationship_mismatch": 34,
  "meal_cost_scale_too_low": 31,
  "meal_repeat_too_many": 19,
  "attraction_repeat_too_many": 17,
  "meal_same_day_lunch_dinner_repeat": 7,
  "meal_invalid_name": 3,
  "hotel_budget_underestimated": 3,
  "json_extract": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-09", "type": "dinner", "name": "石屏会馆", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 851, "expected_total_meals": 1702, "reported_total_meals": 2200, "reported_total_transportation": 2500}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4954, "total": 5954, "diff": -1000, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 992.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 982, "expected_total_meals": 1964, "reported_total_meals": 2484, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2930, "total": 3030, "diff": -100, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 505.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 745, "expected_total_meals": 1490, "reported_total_meals": 1500, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 501, "expected_total_meals": 1002, "reported_total_meals": 834, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2184, "total": 2184, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 364.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 648, "expected_total_meals": 1296, "reported_total_meals": 1248, "reported_total_transportation": 80}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 751, "expected_total_meals": 2253, "reported_total_meals": 2109, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 751, "expected_total_meals": 2253, "reported_total_meals": 2109, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "七十二奇楼景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "七十二奇楼景区"}, {"date": "2026-05-14", "day_index": 3, "name": "七十二奇楼景区"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(张家界天子山餐厅)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 461, "expected_total_attractions": 1844, "reported_total_attractions": 2044, "meal_per_person_cost_sum": 675, "expected_total_meals": 2700, "reported_total_meals": 2856, "reported_total_transportation": 1700}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4050, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1098, "meal_per_person_cost_sum": 927, "expected_total_meals": 2781, "reported_total_meals": 3765, "reported_total_transportation": 1500}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·钟楼南大街店", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3852, "total": 4052, "diff": -200, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 506.5, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-05", "lunch": "肯德基(市民中心1号店)", "dinner": "肯德基(市民中心1号店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1125, "expected_total_meals": 1125, "reported_total_meals": 1056, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1125, "expected_total_meals": 1125, "reported_total_meals": 1056, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 440, "meal_per_person_cost_sum": 588, "expected_total_meals": 2352, "reported_total_meals": 2280, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 489, "expected_total_meals": 2934, "reported_total_meals": 3960, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 489, "expected_total_meals": 2934, "reported_total_meals": 3960, "reported_total_transportation": 1200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 221, "expected_total_meals": 442, "reported_total_meals": 504, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 221, "expected_total_meals": 442, "reported_total_meals": 504, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 370, "expected_total_meals": 1110, "reported_total_meals": 1059, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 24040, "total": 23040, "diff": 1000, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1920.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 7800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 1550, "expected_total_meals": 4650, "reported_total_meals": 7260, "reported_total_transportation": 7900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 1550, "expected_total_meals": 4650, "reported_total_meals": 7260, "reported_total_transportation": 7900}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1438, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1438, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8165, "total": 7165, "diff": 1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 796.11, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5400, "reported_total_hotels": 5400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 510, "expected_total_meals": 1530, "reported_total_meals": 1530, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 622, "expected_total_meals": 1244, "reported_total_meals": 1098, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "石路步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "石路步行街"}, {"date": "2026-05-04", "day_index": 4, "name": "石路步行街"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 573, "expected_total_attractions": 2292, "reported_total_attractions": 2696, "meal_per_person_cost_sum": 1149, "expected_total_meals": 4596, "reported_total_meals": 3600, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 573, "expected_total_attractions": 2292, "reported_total_attractions": 2696, "meal_per_person_cost_sum": 1149, "expected_total_meals": 4596, "reported_total_meals": 3600, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 155, "expected_total_attractions": 465, "reported_total_attractions": 510, "meal_per_person_cost_sum": 413, "expected_total_meals": 1239, "reported_total_meals": 1533, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 155, "expected_total_attractions": 465, "reported_total_attractions": 510, "meal_per_person_cost_sum": 413, "expected_total_meals": 1239, "reported_total_meals": 1533, "reported_total_transportation": 100}}]`
