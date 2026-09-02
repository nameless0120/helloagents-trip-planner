# Rule Eval Report: base_qwen25_7b_current_standard_w10

- records: 200
- generations: `training/outputs/eval/base_qwen25_7b_current_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 193 | 199 | 96.98% |
| attraction_budget_consistent | 34 | 199 | 17.09% |
| attraction_budget_party_relation_ok | 54 | 199 | 27.14% |
| attraction_count_ok | 199 | 199 | 100.00% |
| attraction_diversity_ok | 191 | 199 | 95.98% |
| attraction_grounding_ok | 196 | 199 | 98.49% |
| attraction_repeat_limit_ok | 191 | 199 | 95.98% |
| budget_arithmetic_consistent | 122 | 199 | 61.31% |
| budget_consistent | 122 | 199 | 61.31% |
| budget_level_aligned | 50 | 199 | 25.13% |
| budget_preference_aligned | 50 | 199 | 25.13% |
| budget_relationship_ok | 1 | 199 | 0.50% |
| budget_selection_ok | 108 | 199 | 54.27% |
| budget_user_constraint_ok | 196 | 199 | 98.49% |
| budget_within_user_budget | 198 | 199 | 99.50% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 23 | 199 | 11.56% |
| dpo_soft_recomputed_budget_pass | 47 | 199 | 23.62% |
| hard_pass | 175 | 199 | 87.94% |
| hotel_budget_covers_nights | 84 | 199 | 42.21% |
| hotel_budget_relation_ok | 88 | 199 | 44.22% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 24 | 199 | 12.06% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 0 | 199 | 0.00% |
| meal_complete | 198 | 199 | 99.50% |
| meal_cost_scale_ok | 36 | 199 | 18.09% |
| meal_diversity_ok | 88 | 199 | 44.22% |
| meal_grounding_ok | 183 | 199 | 91.96% |
| meal_lunch_dinner_same_day_ok | 174 | 199 | 87.44% |
| meal_repeat_limit_ok | 95 | 199 | 47.74% |
| meal_specific_ok | 194 | 199 | 97.49% |
| meal_valid_semantics_ok | 186 | 199 | 93.47% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 108 | 199 | 54.27% |
| recomputed_budget_hard_ok | 196 | 199 | 98.49% |
| recomputed_budget_level_aligned | 108 | 199 | 54.27% |
| recomputed_budget_preference_aligned | 108 | 199 | 54.27% |
| recomputed_budget_user_constraint_ok | 196 | 199 | 98.49% |
| recomputed_budget_within_user_budget | 192 | 199 | 96.48% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 1 | 199 | 0.50% |
| sft_hard_pass | 175 | 199 | 87.94% |
| sft_no_budget_sum_hard_pass | 175 | 199 | 87.94% |
| sft_strict_hard_pass | 0 | 199 | 0.00% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6548,
    "p50": 0.6667,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9852,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9852,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9882,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 483.7599,
    "p50": 458.5,
    "p90": 662.0
  },
  "recomputed_budget_total": {
    "avg": 4517.9849,
    "p50": 3956.0,
    "p90": 8272.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 198,
  "budget_relationship_mismatch": 198,
  "attraction_budget_inconsistent": 165,
  "meal_cost_scale_too_low": 163,
  "budget_preference_mismatch": 149,
  "hotel_budget_underestimated": 115,
  "meal_repeat_too_many": 104,
  "budget_arithmetic_inconsistent": 77,
  "meal_same_day_lunch_dinner_repeat": 25,
  "meal_invalid_name": 13,
  "attraction_repeat_too_many": 8,
  "accommodation_type_mismatch": 6,
  "meal_placeholder": 5,
  "meal_grounding_miss": 3,
  "budget_hard_constraint_exceeded": 3,
  "schema": 1
}
```

## Failure Examples

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 310, "expected_total_attractions": 620, "reported_total_attractions": 520, "meal_per_person_cost_sum": 343, "expected_total_meals": 686, "reported_total_meals": 450, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 310, "expected_total_attractions": 620, "reported_total_attractions": 520, "meal_per_person_cost_sum": 343, "expected_total_meals": 686, "reported_total_meals": 450, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 2250, "expected_total_attractions": 620, "reported_total_attractions": 520, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 6, "failures": [{"date": "2026-09-04", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)", "estimated_cost": 10, "min_expected_cost": 20}, {"date": "2026-09-04", "type": "dinner", "name": "田源米粉(三多店)", "estimated_cost": 7, "min_expected_cost": 50}, {"date": "2026-09-05", "type": "breakfast", "name": "秋福米粉(桂林市正阳路步行街店)", "estimated_cost": 10, "min_expected_cost": 20}, {"date": "2026-09-05", "type": "lunch", "name": "食在香乡野本地菜", "estimated_cost": 40, "min_expected_cost": 50}, {"date": "2026-09-06", "type": "breakfast", "name": "老东江米粉(施家园路店)", "estimated_cost": 10, "min_expected_cost": 20}, {"date": "2026-09-06", "type": "lunch", "name": "廖哥土鲫鱼未来馆(桂星店)", "estimated_cost": 47, "min_expected_cost": 50}]}}}]`

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 310, "meal_per_person_cost_sum": 647, "expected_total_meals": 1294, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 310, "meal_per_person_cost_sum": 647, "expected_total_meals": 1294, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1350, "reported_total_hotels": 1350, "expected_total_attractions": 230, "reported_total_attractions": 310, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 326, "expected_total_meals": 652, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "南诏村·现炒云南菜", "dinner": "南诏村·现炒云南菜"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-13", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-13", "type": "dinner", "name": "南诏村·现炒云南菜"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 225, "meal_per_person_cost_sum": 422, "expected_total_meals": 844, "reported_total_meals": 312, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2090, "total": 1690, "diff": 400, "requested_budget": {"available": true, "amount": 1900, "scope": "total", "party_size": 2, "total": 1900, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 281.67, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1900, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1400, "target_max_total": 2000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 180, "expected_total_attractions": 360, "reported_total_attractions": 600, "meal_per_person_cost_sum": 491, "expected_total_meals": 982, "reported_total_meals": 540, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 180, "expected_total_attractions": 360, "reported_total_attractions": 600, "meal_per_person_cost_sum": 491, "expected_total_meals": 982, "reported_total_meals": 540, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-06", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2026-08-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-08", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 750, "diff": -250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 1020, "meal_per_person_cost_sum": 509, "expected_total_meals": 1018, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "猪脑壳凉面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "猪脑壳凉面(南正街)"}, {"date": "2026-05-12", "type": "breakfast", "name": "猪脑壳凉面(南正街)"}, {"date": "2026-05-13", "type": "breakfast", "name": "猪脑壳凉面(南正街)"}, {"date": "2026-05-14", "type": "breakfast", "name": "猪脑壳凉面(南正街)"}, {"date": "2026-05-15", "type": "breakfast", "name": "猪脑壳凉面(南正街)"}]}, {"name_key": "刘聋子粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "刘聋子粉馆(张家界总店)"}, {"date": "2026-05-12", "type": "lunch", "name": "刘聋子粉馆(张家界总店)"}, {"date": "2026-05-13", "type": "lunch", "name": "刘聋子粉馆(张家界总店)"}, {"date": "2026-05-14", "type": "lunch", "name": "刘聋子粉馆(张家界总店)"}, {"date": "2026-05-15", "type": "lunch", "name": "刘聋子粉馆(张家界总店)"}]}, {"name_key": "熊氏草帽面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "dinner", "name": "熊氏草帽面(46年老店)"}, {"date": "2026-05-12", "type": "dinner", "name": "熊氏草帽面(46年老店)"}, {"date": "2026-05-13", "type": "dinner", "name": "熊氏草帽面(46年老店)"}, {"date": "2026-05-14", "type": "dinner", "name": "熊氏草帽面(46年老店)"}, {"date": "2026-05-15", "type": "dinner", "name": "熊氏草帽面(46年老店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 320, "meal_per_person_cost_sum": 290, "expected_total_meals": 1160, "reported_total_meals": 360, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-09", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-11", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 254, "expected_total_attractions": 762, "reported_total_attractions": 510, "meal_per_person_cost_sum": 692, "expected_total_meals": 2076, "reported_total_meals": 1380, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-04", "lunch": "肯德基(杭州灵隐店)", "dinner": "肯德基(市民中心1号店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2100, "total": 2000, "diff": 100, "requested_budget": {"available": true, "amount": 2000, "scope": "total", "party_size": 1, "total": 2000, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 400.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2000, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1250, "reported_total_hotels": 1250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 120, "expected_total_attractions": 120, "reported_total_attractions": 260, "meal_per_person_cost_sum": 633, "expected_total_meals": 633, "reported_total_meals": 390, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "万福兴", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-01", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-02", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-03", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-04", "type": "dinner", "name": "万福兴(东中市总店)"}]}, {"name_key": "乾盛兴苏式面馆蟹黄面", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "乾盛兴苏式面馆蟹黄面(山塘街店)"}, {"date": "2026-05-02", "type": "lunch", "name": "乾盛兴苏式面馆蟹黄面(山塘街店)"}, {"date": "2026-05-03", "type": "lunch", "name": "乾盛兴苏式面馆蟹黄面(山塘街店)"}, {"date": "2026-05-04", "type": "lunch", "name": "乾盛兴苏式面馆蟹黄面(山塘街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 515, "expected_total_meals": 2060, "reported_total_meals": 1080, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 270, "meal_per_person_cost_sum": 464, "expected_total_meals": 1856, "reported_total_meals": 312, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 270, "meal_per_person_cost_sum": 464, "expected_total_meals": 1856, "reported_total_meals": 312, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 205, "meal_per_person_cost_sum": 283, "expected_total_meals": 849, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 205, "meal_per_person_cost_sum": 283, "expected_total_meals": 849, "reported_total_meals": 210, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "矮子馅饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "矮子馅饼(武汉总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "矮子馅饼(武汉总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 146, "expected_total_attractions": 876, "reported_total_attractions": 210, "meal_per_person_cost_sum": 234, "expected_total_meals": 1404, "reported_total_meals": 378, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-07", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1485, "total": 1385, "diff": 100, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 2, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 230.83, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1700, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 205, "meal_per_person_cost_sum": 320, "expected_total_meals": 640, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-06", "lunch": "南京大牌档(中山陵紫金坊店)", "dinner": "南京大牌档(1912总统府店)"}, {"date": "2026-07-08", "lunch": "十朝春精菜馆", "dinner": "十朝春精菜馆"}, {"date": "2026-07-09", "lunch": "小潘记鸭血粉丝汤", "dinner": "小潘记鸭血粉丝汤"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 485, "expected_total_attractions": 970, "reported_total_attractions": 505, "meal_per_person_cost_sum": 225, "expected_total_meals": 450, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 485, "expected_total_attractions": 970, "reported_total_attractions": 505, "meal_per_person_cost_sum": 225, "expected_total_meals": 450, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 970, "reported_total_attractions": 505, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5325, "total": 5375, "diff": -50, "requested_budget": {"available": true, "amount": 9900, "scope": "total", "party_size": 3, "total": 9900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 597.22, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 6400, "target_max_total": 10900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 800, "diff": 200, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 768, "expected_total_meals": 1536, "reported_total_meals": 540, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 800, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "古街依强稀饭(古街商厦店)", "estimated_cost": 17, "min_expected_cost": 35}]}}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-07-06", "type": "dinner", "name": "王庄夜市"}, {"date": "2026-07-07", "type": "dinner", "name": "王庄夜市"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1500, "total": 1400, "diff": 100, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 3, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 233.33, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6460, "total": 6380, "diff": 80, "requested_budget": {"available": true, "amount": 6900, "scope": "total", "party_size": 2, "total": 6900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 797.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 4500, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 5600, "reported_total_hotels": 5600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 180, "meal_per_person_cost_sum": 618, "expected_total_meals": 1236, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 180, "meal_per_person_cost_sum": 618, "expected_total_meals": 1236, "reported_total_meals": 480, "reported_total_transportation": 200}}]`
