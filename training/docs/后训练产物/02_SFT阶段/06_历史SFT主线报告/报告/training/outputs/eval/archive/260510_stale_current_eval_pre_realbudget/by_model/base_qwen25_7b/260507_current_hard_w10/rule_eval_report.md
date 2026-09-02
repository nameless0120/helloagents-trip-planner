# Rule Eval Report: base_qwen25_7b_current_hard_w10

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_current_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 287 | 300 | 95.67% |
| attraction_budget_consistent | 39 | 300 | 13.00% |
| attraction_budget_party_relation_ok | 81 | 300 | 27.00% |
| attraction_count_ok | 297 | 300 | 99.00% |
| attraction_diversity_ok | 262 | 300 | 87.33% |
| attraction_grounding_ok | 296 | 300 | 98.67% |
| attraction_repeat_limit_ok | 262 | 300 | 87.33% |
| budget_arithmetic_consistent | 180 | 300 | 60.00% |
| budget_consistent | 180 | 300 | 60.00% |
| budget_level_aligned | 139 | 300 | 46.33% |
| budget_preference_aligned | 139 | 300 | 46.33% |
| budget_relationship_ok | 23 | 300 | 7.67% |
| budget_selection_ok | 54 | 300 | 18.00% |
| budget_user_constraint_ok | 214 | 300 | 71.33% |
| budget_within_user_budget | 265 | 300 | 88.33% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 49 | 300 | 16.33% |
| dpo_soft_recomputed_budget_pass | 21 | 300 | 7.00% |
| hard_pass | 186 | 300 | 62.00% |
| hotel_budget_covers_nights | 79 | 300 | 26.33% |
| hotel_budget_relation_ok | 130 | 300 | 43.33% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 300 | 300 | 100.00% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 26 | 300 | 8.67% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 225 | 300 | 75.00% |
| meal_diversity_ok | 216 | 300 | 72.00% |
| meal_grounding_ok | 197 | 300 | 65.67% |
| meal_lunch_dinner_same_day_ok | 255 | 300 | 85.00% |
| meal_repeat_limit_ok | 243 | 300 | 81.00% |
| meal_specific_ok | 288 | 300 | 96.00% |
| meal_valid_semantics_ok | 218 | 300 | 72.67% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 54 | 300 | 18.00% |
| recomputed_budget_hard_ok | 98 | 300 | 32.67% |
| recomputed_budget_level_aligned | 54 | 300 | 18.00% |
| recomputed_budget_preference_aligned | 54 | 300 | 18.00% |
| recomputed_budget_user_constraint_ok | 98 | 300 | 32.67% |
| recomputed_budget_within_user_budget | 119 | 300 | 39.67% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 7 | 300 | 2.33% |
| sft_hard_pass | 186 | 300 | 62.00% |
| sft_no_budget_sum_hard_pass | 186 | 300 | 62.00% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 299 | 300 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9755,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5311,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8439,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8439,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9081,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 745.8731,
    "p50": 690.0,
    "p90": 1184.67
  },
  "recomputed_budget_total": {
    "avg": 8372.3,
    "p50": 7470.0,
    "p90": 13944.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "budget_relationship_mismatch": 277,
  "attraction_budget_inconsistent": 261,
  "hotel_budget_underestimated": 221,
  "budget_preference_mismatch": 161,
  "budget_arithmetic_inconsistent": 120,
  "budget_hard_constraint_exceeded": 86,
  "meal_invalid_name": 82,
  "meal_cost_scale_too_low": 75,
  "meal_repeat_too_many": 57,
  "meal_same_day_lunch_dinner_repeat": 45,
  "attraction_repeat_too_many": 38,
  "meal_grounding_miss": 21,
  "accommodation_type_mismatch": 13,
  "meal_placeholder": 12,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"name_key": "自由人", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-08", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-09", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 327, "expected_total_meals": 327, "reported_total_meals": 180, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 327, "expected_total_meals": 327, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4255, "total": 4055, "diff": 200, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 337.92, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 175, "meal_per_person_cost_sum": 1560, "expected_total_meals": 4680, "reported_total_meals": 1080, "reported_total_transportation": 800}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6958, "total": 8158, "diff": -1200, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 509.88, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 5900, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 390, "meal_per_person_cost_sum": 1296, "expected_total_meals": 5184, "reported_total_meals": 1368, "reported_total_transportation": 200}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 460, "expected_total_attractions": 460, "reported_total_attractions": 1055, "meal_per_person_cost_sum": 998, "expected_total_meals": 998, "reported_total_meals": 465, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 460, "expected_total_attractions": 460, "reported_total_attractions": 1055, "meal_per_person_cost_sum": 998, "expected_total_meals": 998, "reported_total_meals": 465, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "知味观", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-04-28", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-04-29", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-04-30", "type": "lunch", "name": "知味观(湖滨总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "昆明海埂大坝", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "昆明海埂大坝"}, {"date": "2026-04-07", "day_index": 4, "name": "昆明海埂大坝"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "小人国主题公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-03", "type": "dinner", "name": "昆明捞渔河湿地公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-05", "type": "lunch", "name": "守望山·治愈系城市露营公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "lunch", "name": "昆明瀑布公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-07", "type": "lunch", "name": "昆明捞渔河湿地公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-07", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山野间餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-01", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-02", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-03", "type": "breakfast", "name": "山野间餐厅"}]}, {"name_key": "岩洞餐厅.天然岩洞特色菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-01", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-02", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-03", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}]}, {"name_key": "味道制造·桂林菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-01", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-02", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-03", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1170, "meal_per_person_cost_sum": 1096, "expected_total_meals": 2192, "reported_total_meals": 1200, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1170, "meal_per_person_cost_sum": 1096, "expected_total_meals": 2192, "reported_total_meals": 1200, "reported_total_transportation": 800}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "星巴克(成都大魔方招商花园城店)", "dinner": "星巴克(成都环球中心II店)"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-19", "type": "dinner", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-20", "type": "lunch", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-20", "type": "dinner", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-21", "type": "lunch", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-21", "type": "dinner", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-22", "type": "lunch", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-22", "type": "dinner", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-23", "type": "lunch", "name": "老孙家羊肉泡馍"}, {"date": "2026-04-23", "type": "dinner", "name": "老孙家羊肉泡馍"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 6750, "reported_total_hotels": 2250, "diff": -4500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5050, "total": 4950, "diff": 100, "requested_budget": {"available": true, "amount": 11100, "scope": "total", "party_size": 5, "total": 11100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 198.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 11100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 7200, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 6750, "reported_total_hotels": 2250, "diff": -4500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 2250, "reported_total_hotels": 1800, "diff": -450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 600, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 600, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5162, "total": 5362, "diff": -200, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 670.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 5800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 4100, "target_max_total": 6500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1778, "expected_total_meals": 3556, "reported_total_meals": 1212, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1778, "expected_total_meals": 3556, "reported_total_meals": 1212, "reported_total_transportation": 800}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-02", "lunch": "观锦餐厅(天廊店)", "dinner": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "lunch": "陈麻婆豆腐(旗舰店)", "dinner": "陈麻婆豆腐(旗舰店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2180, "total": 1980, "diff": 200, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 660.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 60, "reported_total_attractions": 180, "meal_per_person_cost_sum": 700, "expected_total_meals": 700, "reported_total_meals": 450, "reported_total_transportation": 200}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "陈氏海稍鱼(开发区店)", "dinner": "陈氏海稍鱼(开发区店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1395, "expected_total_meals": 4185, "reported_total_meals": 1650, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "苏焰·地标天津菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "lunch", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-03", "type": "lunch", "name": "苏焰·地标天津菜(多伦道店)"}, {"date": "2026-07-04", "type": "lunch", "name": "苏焰·地标天津菜(多伦道店)"}]}, {"name_key": "友达面馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "友达面馆(天津总店)"}, {"date": "2026-07-03", "type": "dinner", "name": "友达面馆(天津总店)"}, {"date": "2026-07-04", "type": "dinner", "name": "友达面馆(天津总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 240, "meal_per_person_cost_sum": 528, "expected_total_meals": 1584, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "dinner", "name": "武汉热干面", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "江城鱼丸", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "江城鱼丸", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "江城鱼丸", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-02", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "dinner", "name": "苏州乐园森林世界餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 3750, "diff": -6250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4570, "total": 5410, "diff": -840, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 450.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 3750, "diff": -6250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-03", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-04", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}]}, {"name_key": "清真马杰山牛肉汤馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-03", "type": "dinner", "name": "清真马杰山牛肉汤馆"}, {"date": "2025-05-04", "type": "dinner", "name": "清真马杰山牛肉汤馆"}, {"date": "2025-05-05", "type": "dinner", "name": "清真马杰山牛肉汤馆"}, {"date": "2025-05-06", "type": "dinner", "name": "清真马杰山牛肉汤馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1552, "expected_total_meals": 6208, "reported_total_meals": 1008, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 960, "meal_per_person_cost_sum": 640, "expected_total_meals": 1280, "reported_total_meals": 450, "reported_total_transportation": 800}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2020, "total": 1920, "diff": 100, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 1, "total": 2400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 384.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1300, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 45, "expected_total_attractions": 45, "reported_total_attractions": 152, "meal_per_person_cost_sum": 1190, "expected_total_meals": 1190, "reported_total_meals": 468, "reported_total_transportation": 200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好食堂", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "breakfast", "name": "友好食堂"}, {"date": "2026-06-18", "type": "breakfast", "name": "友好食堂"}, {"date": "2026-06-19", "type": "breakfast", "name": "友好食堂"}, {"date": "2026-06-20", "type": "breakfast", "name": "友好食堂"}, {"date": "2026-06-21", "type": "breakfast", "name": "友好食堂"}]}, {"name_key": "友好饭店·道乐日式拉面·烧鸟·酒场", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-19", "type": "lunch", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-20", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-21", "type": "lunch", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}]}, {"name_key": "友好饭店·新友记中餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·新友记中餐厅"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 7500, "reported_total_hotels": 2500, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7040, "total": 6040, "diff": 1000, "requested_budget": {"available": true, "amount": 16100, "scope": "total", "party_size": 5, "total": 16100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 241.6, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 16100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 10500, "target_max_total": 16100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 7500, "reported_total_hotels": 2500, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
