# Rule Eval Report: base_qwen25_7b_pref_fix_vllm_20260506_A_C_w10

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_pref_fix_vllm_20260506_A_C_w10/generations.jsonl`
- records_path: `training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 281 | 299 | 93.98% |
| attraction_budget_consistent | 42 | 299 | 14.05% |
| attraction_budget_party_relation_ok | 87 | 299 | 29.10% |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_diversity_ok | 265 | 299 | 88.63% |
| attraction_grounding_ok | 291 | 299 | 97.32% |
| attraction_repeat_limit_ok | 265 | 299 | 88.63% |
| budget_arithmetic_consistent | 168 | 299 | 56.19% |
| budget_consistent | 168 | 299 | 56.19% |
| budget_level_aligned | 71 | 299 | 23.75% |
| budget_preference_aligned | 71 | 299 | 23.75% |
| budget_relationship_ok | 4 | 299 | 1.34% |
| budget_selection_ok | 152 | 299 | 50.84% |
| budget_user_constraint_ok | 289 | 299 | 96.66% |
| budget_within_user_budget | 298 | 299 | 99.67% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 26 | 299 | 8.70% |
| dpo_soft_recomputed_budget_pass | 38 | 299 | 12.71% |
| hard_pass | 234 | 299 | 78.26% |
| hotel_budget_covers_nights | 87 | 299 | 29.10% |
| hotel_budget_relation_ok | 130 | 299 | 43.48% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 24 | 299 | 8.03% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 296 | 299 | 99.00% |
| meal_cost_scale_ok | 53 | 299 | 17.73% |
| meal_diversity_ok | 109 | 299 | 36.45% |
| meal_grounding_ok | 257 | 299 | 85.95% |
| meal_lunch_dinner_same_day_ok | 241 | 299 | 80.60% |
| meal_repeat_limit_ok | 120 | 299 | 40.13% |
| meal_specific_ok | 286 | 299 | 95.65% |
| meal_valid_semantics_ok | 261 | 299 | 87.29% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 152 | 299 | 50.84% |
| recomputed_budget_hard_ok | 261 | 299 | 87.29% |
| recomputed_budget_level_aligned | 152 | 299 | 50.84% |
| recomputed_budget_preference_aligned | 152 | 299 | 50.84% |
| recomputed_budget_user_constraint_ok | 261 | 299 | 87.29% |
| recomputed_budget_within_user_budget | 288 | 299 | 96.32% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 1 | 299 | 0.33% |
| sft_hard_pass | 234 | 299 | 78.26% |
| sft_no_budget_sum_hard_pass | 234 | 299 | 78.26% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9792,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9955,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5978,
    "p50": 0.6,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9778,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9778,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9811,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 588.3311,
    "p50": 543.6,
    "p90": 894.33
  },
  "recomputed_budget_total": {
    "avg": 6213.893,
    "p50": 5894.0,
    "p90": 10968.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "budget_relationship_mismatch": 295,
  "attraction_budget_inconsistent": 257,
  "meal_cost_scale_too_low": 246,
  "budget_preference_mismatch": 228,
  "hotel_budget_underestimated": 212,
  "meal_repeat_too_many": 179,
  "budget_arithmetic_inconsistent": 131,
  "meal_same_day_lunch_dinner_repeat": 58,
  "meal_invalid_name": 38,
  "attraction_repeat_too_many": 34,
  "accommodation_type_mismatch": 18,
  "meal_placeholder": 13,
  "budget_hard_constraint_exceeded": 10,
  "meal_grounding_miss": 4,
  "schema": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-10", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-11", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}, {"date": "2026-05-12", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"name_key": "老火盆原生态餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-10", "type": "dinner", "name": "老火盆原生态餐厅(通达国际广场店)"}, {"date": "2026-05-11", "type": "dinner", "name": "老火盆原生态餐厅(通达国际广场店)"}, {"date": "2026-05-12", "type": "dinner", "name": "老火盆原生态餐厅(通达国际广场店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2335, "total": 2135, "diff": 200, "requested_budget": {"available": true, "amount": 2500, "scope": "total", "party_size": 1, "total": 2500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 711.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2500, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1600, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 560, "expected_total_attractions": 560, "reported_total_attractions": 740, "meal_per_person_cost_sum": 471, "expected_total_meals": 471, "reported_total_meals": 195, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2580, "total": 2550, "diff": 30, "requested_budget": {"available": true, "amount": 3000, "scope": "total", "party_size": 1, "total": 3000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 850.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3000, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_per_person_cost_sum": 701, "expected_total_meals": 701, "reported_total_meals": 450, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_per_person_cost_sum": 701, "expected_total_meals": 701, "reported_total_meals": 450, "reported_total_transportation": 600}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-13", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3698, "total": 3748, "diff": -50, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 2, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 468.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7900, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5100, "target_max_total": 8300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-06", "type": "dinner", "name": "桂林市临桂区森野手作艺术品馆", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6050, "total": 5050, "diff": 1000, "requested_budget": {"available": true, "amount": 12500, "scope": "total", "party_size": 2, "total": 12500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 631.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 12500, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 8800, "target_max_total": 14000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1170, "meal_per_person_cost_sum": 538, "expected_total_meals": 1076, "reported_total_meals": 1080, "reported_total_transportation": 800}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7265, "total": 7655, "diff": -390, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 4, "total": 15700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 478.44, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 10200, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 265, "meal_per_person_cost_sum": 586, "expected_total_meals": 2344, "reported_total_meals": 1200, "reported_total_transportation": 800}}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 579, "expected_total_meals": 1158, "reported_total_meals": 1050, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 12, "failure_count": 8, "failures": [{"date": "2026-06-20", "type": "dinner", "name": "阿信鲜捞", "estimated_cost": 45, "min_expected_cost": 70}, {"date": "2026-06-21", "type": "breakfast", "name": "古街依强稀饭(古街商厦店)", "estimated_cost": 17, "min_expected_cost": 28}, {"date": "2026-06-21", "type": "dinner", "name": "崔酱炸鸡(东街店)", "estimated_cost": 39, "min_expected_cost": 70}, {"date": "2026-06-22", "type": "breakfast", "name": "忠惠酱鸭捞化老铺(老药洲店)", "estimated_cost": 22, "min_expected_cost": 28}, {"date": "2026-06-22", "type": "dinner", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)", "estimated_cost": 17, "min_expected_cost": 70}, {"date": "2026-06-23", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(仓山万达金街店)", "estimated_cost": 14, "min_expected_cost": 28}, {"date": "2026-06-23", "type": "lunch", "name": "没牙伯花生汤店", "estimated_cost": 16, "min_expected_cost": 70}, {"date": "2026-06-23", "type": "dinner", "name": "崔酱炸鸡(烟台山店)", "estimated_cost": 44, "min_expected_cost": 70}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 12, "failure_count": 8, "failures": [{"date": "2026-06-20", "type": "dinner", "name": "阿信鲜捞", "estimated_cost": 45, "min_expected_cost": 70}, {"date": "2026-06-21", "type": "breakfast", "name": "古街依强稀饭(古街商厦店)", "estimated_cost": 17, "min_expected_cost": 28}, {"date": "2026-06-21", "type": "dinner", "name": "崔酱炸鸡(东街店)", "estimated_cost": 39, "min_expected_cost": 70}, {"date": "2026-06-22", "type": "breakfast", "name": "忠惠酱鸭捞化老铺(老药洲店)", "estimated_cost": 22, "min_expected_cost": 28}, {"date": "2026-06-22", "type": "dinner", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)", "estimated_cost": 17, "min_expected_cost": 70}, {"date": "2026-06-23", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(仓山万达金街店)", "estimated_cost": 14, "min_expected_cost": 28}, {"date": "2026-06-23", "type": "lunch", "name": "没牙伯花生汤店", "estimated_cost": 16, "min_expected_cost": 70}, {"date": "2026-06-23", "type": "dinner", "name": "崔酱炸鸡(烟台山店)", "estimated_cost": 44, "min_expected_cost": 70}]}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2025-05-10", "type": "dinner", "name": "回民街小吃"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-07", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 265, "expected_total_attractions": 530, "reported_total_attractions": 435, "meal_per_person_cost_sum": 409, "expected_total_meals": 818, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "矮子馅饼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-12", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"name_key": "肥肥虾庄", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "肥肥虾庄(江汉路黄鹤楼店)"}, {"date": "2026-05-10", "type": "lunch", "name": "肥肥虾庄(江汉路黄鹤楼店)"}, {"date": "2026-05-11", "type": "lunch", "name": "肥肥虾庄(江汉路黄鹤楼店)"}, {"date": "2026-05-12", "type": "lunch", "name": "肥肥虾庄(江汉路黄鹤楼店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3100, "total": 3000, "diff": 100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 300.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "meal_per_person_cost_sum": 751, "expected_total_meals": 1502, "reported_total_meals": 690, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安钟楼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安钟楼"}, {"date": "2026-08-07", "day_index": 3, "name": "西安钟楼"}]}, {"name_key": "回民街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "回民街"}, {"date": "2026-08-08", "day_index": 4, "name": "回民街"}]}, {"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2026-08-07", "day_index": 3, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-04", "lunch": "魏家凉皮(西大街店)", "dinner": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-08", "lunch": "魏家凉皮(西大街店)", "dinner": "魏家凉皮(秦飞大厦店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-05", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2026-08-06", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-07", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2026-08-08", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}, {"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "lunch", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-04", "type": "dinner", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-08", "type": "lunch", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-08", "type": "dinner", "name": "魏家凉皮(秦飞大厦店)"}]}]}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2195, "total": 1995, "diff": 200, "requested_budget": {"available": true, "amount": 9900, "scope": "total", "party_size": 2, "total": 9900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 199.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9900, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 6400, "target_max_total": 10400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 215, "expected_total_attractions": 430, "reported_total_attractions": 315, "meal_per_person_cost_sum": 943, "expected_total_meals": 1886, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-05", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}, {"date": "2026-07-06", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}]}, {"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-05", "type": "lunch", "name": "南楼煎饼(滨江道店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-07", "type": "lunch", "name": "南楼煎饼(滨江道店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3650, "total": 4650, "diff": -1000, "requested_budget": {"available": true, "amount": 8500, "scope": "total", "party_size": 3, "total": 8500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 516.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8500, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 8500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3576, "total": 3586, "diff": -10, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 3, "total": 9800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 398.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 6400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 228, "meal_per_person_cost_sum": 446, "expected_total_meals": 1338, "reported_total_meals": 498, "reported_total_transportation": 600}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-06", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-06", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-30", "type": "dinner", "name": "永乐夜市"}, {"date": "2026-05-01", "type": "dinner", "name": "杭州武林夜市"}, {"date": "2026-05-02", "type": "dinner", "name": "落日夜市"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "肯德基", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-03", "type": "dinner", "name": "肯德基(市民中心1号店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-04", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4000, "reported_total_hotels": 2000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2680, "total": 2880, "diff": -200, "requested_budget": {"available": true, "amount": 10300, "scope": "total", "party_size": 4, "total": 10300, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 144.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10300, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 5700, "target_max_total": 10300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4000, "reported_total_hotels": 2000, "diff": -2000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4400, "total": 4480, "diff": -80, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 560.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 9200, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 120, "meal_per_person_cost_sum": 877, "expected_total_meals": 1754, "reported_total_meals": 1080, "reported_total_transportation": 800}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-05", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 1650, "diff": -2750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 555, "expected_total_meals": 1665, "reported_total_meals": 420, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-10", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}, {"name_key": "金陵家宴·金陵春.南京菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-07", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-08", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-09", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-10", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}]}, {"name_key": "小厨娘淮扬菜·新街口艾尚天地店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-07", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-08", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-09", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-10", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2075, "total": 1975, "diff": 100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 395.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6040, "total": 5940, "diff": 100, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 495.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 510, "reported_total_attractions": 2470, "meal_per_person_cost_sum": 686, "expected_total_meals": 2058, "reported_total_meals": 1170, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 7500, "reported_total_hotels": 2500, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5750, "total": 6750, "diff": -1000, "requested_budget": {"available": true, "amount": 28000, "scope": "total", "party_size": 5, "total": 28000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 270.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 28000, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 18200, "target_max_total": 28000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 7500, "reported_total_hotels": 2500, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 175, "expected_total_attractions": 875, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 843, "expected_total_meals": 4215, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`
