# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v2a_standard200_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_standard200_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 197 | 197 | 100.00% |
| attraction_budget_consistent | 54 | 197 | 27.41% |
| attraction_budget_party_relation_ok | 153 | 197 | 77.66% |
| attraction_count_ok | 196 | 197 | 99.49% |
| attraction_diversity_ok | 183 | 197 | 92.89% |
| attraction_grounding_ok | 193 | 197 | 97.97% |
| attraction_repeat_limit_ok | 183 | 197 | 92.89% |
| budget_arithmetic_consistent | 147 | 197 | 74.62% |
| budget_consistent | 147 | 197 | 74.62% |
| budget_level_aligned | 128 | 197 | 64.97% |
| budget_preference_aligned | 128 | 197 | 64.97% |
| budget_relationship_ok | 65 | 197 | 32.99% |
| budget_selection_ok | 121 | 197 | 61.42% |
| budget_user_constraint_ok | 195 | 197 | 98.98% |
| budget_within_user_budget | 197 | 197 | 100.00% |
| city_ok | 197 | 197 | 100.00% |
| date_range_ok | 197 | 197 | 100.00% |
| day_dates_ok | 197 | 197 | 100.00% |
| day_index_ok | 197 | 197 | 100.00% |
| days_len_ok | 197 | 197 | 100.00% |
| dpo_soft_pass | 103 | 197 | 52.28% |
| dpo_soft_recomputed_budget_pass | 97 | 197 | 49.24% |
| hard_pass | 187 | 197 | 94.92% |
| hotel_budget_covers_nights | 162 | 197 | 82.23% |
| hotel_budget_relation_ok | 163 | 197 | 82.74% |
| hotel_distance_placeholder_ok | 197 | 197 | 100.00% |
| hotel_grounding_ok | 197 | 197 | 100.00% |
| invalid_hotel_name_ok | 197 | 197 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 103 | 197 | 52.28% |
| location_object_ok | 197 | 197 | 100.00% |
| meal_budget_consistent | 1 | 197 | 0.51% |
| meal_complete | 197 | 197 | 100.00% |
| meal_cost_scale_ok | 98 | 197 | 49.75% |
| meal_diversity_ok | 171 | 197 | 86.80% |
| meal_grounding_ok | 192 | 197 | 97.46% |
| meal_lunch_dinner_same_day_ok | 188 | 197 | 95.43% |
| meal_repeat_limit_ok | 178 | 197 | 90.36% |
| meal_specific_ok | 197 | 197 | 100.00% |
| meal_valid_semantics_ok | 192 | 197 | 97.46% |
| middle_hotel_ok | 197 | 197 | 100.00% |
| recomputed_budget_fit_ok | 121 | 197 | 61.42% |
| recomputed_budget_hard_ok | 194 | 197 | 98.48% |
| recomputed_budget_level_aligned | 121 | 197 | 61.42% |
| recomputed_budget_preference_aligned | 121 | 197 | 61.42% |
| recomputed_budget_user_constraint_ok | 194 | 197 | 98.48% |
| recomputed_budget_within_user_budget | 194 | 197 | 98.48% |
| schema_ok | 197 | 200 | 98.50% |
| sft_budget_semantic_hard_pass | 63 | 197 | 31.98% |
| sft_hard_pass | 187 | 197 | 94.92% |
| sft_no_budget_sum_hard_pass | 187 | 197 | 94.92% |
| sft_strict_hard_pass | 0 | 197 | 0.00% |
| transportation_budget_nonnegative | 197 | 197 | 100.00% |
| weather_dates_ok | 197 | 197 | 100.00% |
| weather_match | 197 | 197 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9919,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9978,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8874,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 544.6189,
    "p50": 478.0,
    "p90": 849.83
  },
  "recomputed_budget_total": {
    "avg": 5259.0812,
    "p50": 4308.0,
    "p90": 9999.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 197,
  "attraction_budget_inconsistent": 143,
  "budget_relationship_mismatch": 132,
  "meal_cost_scale_too_low": 99,
  "budget_preference_mismatch": 69,
  "budget_arithmetic_inconsistent": 50,
  "hotel_budget_underestimated": 35,
  "meal_repeat_too_many": 19,
  "attraction_repeat_too_many": 14,
  "meal_same_day_lunch_dinner_repeat": 9,
  "meal_invalid_name": 5,
  "schema": 3,
  "budget_hard_constraint_exceeded": 2,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1700, "total": 1698, "diff": 2, "requested_budget": {"available": true, "amount": 2900, "scope": "total", "party_size": 2, "total": 2900, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 283.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 2900, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 1600, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 433, "expected_total_meals": 866, "reported_total_meals": 594, "reported_total_transportation": 156}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 854, "expected_total_meals": 1708, "reported_total_meals": 2122, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-04-07", "type": "lunch", "name": "芸南道过桥米线(昆明老街旗舰店)", "estimated_cost": 50, "min_expected_cost": 70}, {"date": "2026-04-08", "type": "breakfast", "name": "文山荷鲜居(文山早点)", "estimated_cost": 14, "min_expected_cost": 28}, {"date": "2026-04-09", "type": "lunch", "name": "密芷花园餐厅(西坝店)", "estimated_cost": 64, "min_expected_cost": 70}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-04-07", "type": "lunch", "name": "芸南道过桥米线(昆明老街旗舰店)", "estimated_cost": 50, "min_expected_cost": 70}, {"date": "2026-04-08", "type": "breakfast", "name": "文山荷鲜居(文山早点)", "estimated_cost": 14, "min_expected_cost": 28}, {"date": "2026-04-09", "type": "lunch", "name": "密芷花园餐厅(西坝店)", "estimated_cost": 64, "min_expected_cost": 70}]}}]`

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 105, "expected_total_attractions": 210, "reported_total_attractions": 220, "meal_per_person_cost_sum": 811, "expected_total_meals": 1622, "reported_total_meals": 1380, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 105, "expected_total_attractions": 210, "reported_total_attractions": 220, "meal_per_person_cost_sum": 811, "expected_total_meals": 1622, "reported_total_meals": 1380, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 436, "expected_total_attractions": 872, "reported_total_attractions": 791, "meal_per_person_cost_sum": 411, "expected_total_meals": 822, "reported_total_meals": 1056, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 436, "expected_total_attractions": 872, "reported_total_attractions": 791, "meal_per_person_cost_sum": 411, "expected_total_meals": 822, "reported_total_meals": 1056, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 20, "expected_total_attractions": 40, "reported_total_attractions": 40, "meal_per_person_cost_sum": 517, "expected_total_meals": 1034, "reported_total_meals": 830, "reported_total_transportation": 130}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_per_person_cost_sum": 474, "expected_total_meals": 948, "reported_total_meals": 1048, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_per_person_cost_sum": 474, "expected_total_meals": 948, "reported_total_meals": 1048, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 3, "failures": [{"date": "2026-08-05", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2026-08-08", "type": "lunch", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}, {"date": "2026-08-08", "type": "dinner", "name": "天发芽何记葫芦头泡馍", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1244, "meal_per_person_cost_sum": 739, "expected_total_meals": 2956, "reported_total_meals": 2356, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1244, "meal_per_person_cost_sum": 739, "expected_total_meals": 2956, "reported_total_meals": 2356, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 1204, "reported_total_attractions": 1244, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-05-14", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1059, "meal_per_person_cost_sum": 810, "expected_total_meals": 2430, "reported_total_meals": 2442, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1059, "meal_per_person_cost_sum": 810, "expected_total_meals": 2430, "reported_total_meals": 2442, "reported_total_transportation": 1100}}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-03", "day_index": 2, "name": "杭州植物园"}, {"date": "2026-05-05", "day_index": 4, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-03", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-04", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-05", "type": "lunch", "name": "杭州酒家(延安路店)"}]}, {"name_key": "江南忆味主题餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "dinner", "name": "江南忆味主题餐厅"}, {"date": "2026-05-02", "type": "dinner", "name": "江南忆味主题餐厅"}, {"date": "2026-05-03", "type": "dinner", "name": "江南忆味主题餐厅"}, {"date": "2026-05-04", "type": "dinner", "name": "江南忆味主题餐厅"}, {"date": "2026-05-05", "type": "dinner", "name": "江南忆味主题餐厅"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 170, "reported_total_attractions": 150, "meal_per_person_cost_sum": 813, "expected_total_meals": 813, "reported_total_meals": 500, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 1180, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 948, "expected_total_meals": 3792, "reported_total_meals": 2920, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 1180, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 948, "expected_total_meals": 3792, "reported_total_meals": 2920, "reported_total_transportation": 700}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 10000, "reported_total_hotels": 10000, "expected_total_attractions": 1180, "reported_total_attractions": 1080, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2026-05-02", "type": "breakfast", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 20}, {"date": "2026-05-02", "type": "dinner", "name": "万福兴(东中市总店)", "estimated_cost": 20, "min_expected_cost": 50}, {"date": "2026-05-03", "type": "breakfast", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 20}]}}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 476, "expected_total_meals": 1904, "reported_total_meals": 1416, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1840, "total": 1830, "diff": 10, "requested_budget": {"available": true, "amount": 3600, "scope": "total", "party_size": 3, "total": 3600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 305.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3600, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 2000, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 180, "meal_per_person_cost_sum": 406, "expected_total_meals": 1218, "reported_total_meals": 1086, "reported_total_transportation": 324}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 1600, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5296, "total": 5396, "diff": -100, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 6, "total": 13100, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 299.78, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 7200, "target_max_total": 14400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 1600, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 540, "meal_per_person_cost_sum": 610, "expected_total_meals": 3660, "reported_total_meals": 2856, "reported_total_transportation": 300}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_per_person_cost_sum": 431, "expected_total_meals": 862, "reported_total_meals": 624, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_per_person_cost_sum": 431, "expected_total_meals": 862, "reported_total_meals": 624, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-06-06", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 25}]}}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 661, "expected_total_meals": 1983, "reported_total_meals": 2292, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 661, "expected_total_meals": 1983, "reported_total_meals": 2292, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4602, "total": 4602, "diff": 0, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 3, "total": 6700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 383.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4800, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1150, "total": 1140, "diff": 10, "requested_budget": {"available": true, "amount": 1500, "scope": "total", "party_size": 2, "total": 1500, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 285.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1500, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1100, "target_max_total": 1600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 1, "expected_min_total_hotels": 250, "reported_total_hotels": 250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 280, "meal_per_person_cost_sum": 280, "expected_total_meals": 560, "reported_total_meals": 482, "reported_total_transportation": 138}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 620, "expected_total_meals": 1860, "reported_total_meals": 1950, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 620, "expected_total_meals": 1860, "reported_total_meals": 1950, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5864, "total": 6064, "diff": -200, "requested_budget": {"available": true, "amount": 6900, "scope": "total", "party_size": 2, "total": 6900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 758.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 4500, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4200, "reported_total_hotels": 4200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 837, "expected_total_meals": 1674, "reported_total_meals": 1224, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 837, "expected_total_meals": 1674, "reported_total_meals": 1224, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 400, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 312, "expected_total_meals": 936, "reported_total_meals": 711, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 400, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000022
- request: 桂林 2026-04-07->2026-04-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '自然风光', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4020, "total": 3920, "diff": 100, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 326.67, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3500, "target_max_total": 5000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 645, "reported_total_attractions": 690, "meal_per_person_cost_sum": 531, "expected_total_meals": 1593, "reported_total_meals": 1530, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 645, "reported_total_attractions": 690, "meal_per_person_cost_sum": 531, "expected_total_meals": 1593, "reported_total_meals": 1530, "reported_total_transportation": 600}}]`
