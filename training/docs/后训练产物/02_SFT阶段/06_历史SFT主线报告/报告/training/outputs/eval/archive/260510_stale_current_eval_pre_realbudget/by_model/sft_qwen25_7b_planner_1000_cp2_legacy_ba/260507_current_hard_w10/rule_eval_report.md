# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v2a_current_hard_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_current_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 56 | 299 | 18.73% |
| attraction_budget_party_relation_ok | 170 | 299 | 56.86% |
| attraction_count_ok | 295 | 299 | 98.66% |
| attraction_diversity_ok | 232 | 299 | 77.59% |
| attraction_grounding_ok | 287 | 299 | 95.99% |
| attraction_repeat_limit_ok | 232 | 299 | 77.59% |
| budget_arithmetic_consistent | 235 | 299 | 78.60% |
| budget_consistent | 235 | 299 | 78.60% |
| budget_level_aligned | 211 | 299 | 70.57% |
| budget_preference_aligned | 211 | 299 | 70.57% |
| budget_relationship_ok | 72 | 299 | 24.08% |
| budget_selection_ok | 95 | 299 | 31.77% |
| budget_user_constraint_ok | 239 | 299 | 79.93% |
| budget_within_user_budget | 276 | 299 | 92.31% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 298 | 299 | 99.67% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 298 | 299 | 99.67% |
| dpo_soft_pass | 69 | 299 | 23.08% |
| dpo_soft_recomputed_budget_pass | 35 | 299 | 11.71% |
| hard_pass | 180 | 299 | 60.20% |
| hotel_budget_covers_nights | 166 | 299 | 55.52% |
| hotel_budget_relation_ok | 169 | 299 | 56.52% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 64 | 299 | 21.40% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 225 | 299 | 75.25% |
| meal_diversity_ok | 241 | 299 | 80.60% |
| meal_grounding_ok | 195 | 299 | 65.22% |
| meal_lunch_dinner_same_day_ok | 266 | 299 | 88.96% |
| meal_repeat_limit_ok | 247 | 299 | 82.61% |
| meal_specific_ok | 293 | 299 | 97.99% |
| meal_valid_semantics_ok | 210 | 299 | 70.23% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 95 | 299 | 31.77% |
| recomputed_budget_hard_ok | 123 | 299 | 41.14% |
| recomputed_budget_level_aligned | 95 | 299 | 31.77% |
| recomputed_budget_preference_aligned | 95 | 299 | 31.77% |
| recomputed_budget_user_constraint_ok | 123 | 299 | 41.14% |
| recomputed_budget_within_user_budget | 149 | 299 | 49.83% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 43 | 299 | 14.38% |
| sft_hard_pass | 180 | 299 | 60.20% |
| sft_no_budget_sum_hard_pass | 180 | 299 | 60.20% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 298 | 299 | 99.67% |
| weather_match | 298 | 299 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9742,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9945,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5509,
    "p50": 0.6,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8039,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8039,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8703,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 643.4937,
    "p50": 578.75,
    "p90": 1016.5
  },
  "recomputed_budget_total": {
    "avg": 7301.8127,
    "p50": 6290.0,
    "p90": 12625.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 295,
  "attraction_budget_inconsistent": 243,
  "budget_relationship_mismatch": 227,
  "hotel_budget_underestimated": 133,
  "meal_invalid_name": 89,
  "budget_preference_mismatch": 88,
  "meal_cost_scale_too_low": 74,
  "attraction_repeat_too_many": 67,
  "budget_arithmetic_inconsistent": 64,
  "budget_hard_constraint_exceeded": 60,
  "meal_repeat_too_many": 52,
  "meal_same_day_lunch_dinner_repeat": 33,
  "meal_grounding_miss": 15,
  "meal_placeholder": 6,
  "too_many_attractions": 4,
  "weather_mismatch": 1,
  "schema": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 489, "expected_total_meals": 489, "reported_total_meals": 300, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "业华湘·特色菜", "estimated_cost": 35, "min_expected_cost": 50}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "业华湘·特色菜", "estimated_cost": 35, "min_expected_cost": 50}]}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-26", "type": "dinner", "name": "苏州本帮菜馆"}, {"date": "2026-04-27", "type": "lunch", "name": "苏州本帮菜馆"}, {"date": "2026-04-27", "type": "dinner", "name": "苏帮菜馆"}, {"date": "2026-04-28", "type": "lunch", "name": "苏帮菜馆"}, {"date": "2026-04-28", "type": "dinner", "name": "苏帮菜馆"}, {"date": "2026-04-29", "type": "lunch", "name": "苏帮菜馆"}, {"date": "2026-04-29", "type": "dinner", "name": "苏帮菜馆"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1158, "expected_total_meals": 4632, "reported_total_meals": 2400, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1158, "expected_total_meals": 4632, "reported_total_meals": 2400, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1560, "expected_total_meals": 4680, "reported_total_meals": 1620, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1560, "expected_total_meals": 4680, "reported_total_meals": 1620, "reported_total_transportation": 200}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 3000, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 1410, "reported_total_attractions": 1410, "meal_per_person_cost_sum": 1148, "expected_total_meals": 2296, "reported_total_meals": 1608, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 3000, "expected_total_attractions": 1410, "reported_total_attractions": 1410, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 840, "meal_per_person_cost_sum": 1166, "expected_total_meals": 4664, "reported_total_meals": 1616, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 840, "meal_per_person_cost_sum": 1166, "expected_total_meals": 4664, "reported_total_meals": 1616, "reported_total_transportation": 100}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-04", "type": "dinner", "name": "西安饭庄", "reason": "unknown_food_semantics"}, {"date": "2025-05-05", "type": "dinner", "name": "西安饭庄", "reason": "unknown_food_semantics"}, {"date": "2025-05-06", "type": "dinner", "name": "西安饭庄", "reason": "unknown_food_semantics"}, {"date": "2025-05-07", "type": "dinner", "name": "西安饭庄", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 498, "meal_per_person_cost_sum": 770, "expected_total_meals": 1540, "reported_total_meals": 702, "reported_total_transportation": 80}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 498, "meal_per_person_cost_sum": 770, "expected_total_meals": 1540, "reported_total_meals": 702, "reported_total_transportation": 80}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 155, "meal_per_person_cost_sum": 786, "expected_total_meals": 786, "reported_total_meals": 648, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 155, "meal_per_person_cost_sum": 786, "expected_total_meals": 786, "reported_total_meals": 648, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 165, "reported_total_attractions": 155, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-07-02", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)", "estimated_cost": 26, "min_expected_cost": 35}, {"date": "2026-07-06", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)", "estimated_cost": 26, "min_expected_cost": 35}]}}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "捞鱼客水族娱乐馆(昆明海乐世界店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 3200, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 131, "expected_total_attractions": 655, "reported_total_attractions": 455, "meal_per_person_cost_sum": 885, "expected_total_meals": 4425, "reported_total_meals": 2280, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-19", "type": "dinner", "name": "西安饭庄(回民街店)", "reason": "unknown_food_semantics"}, {"date": "2026-04-20", "type": "dinner", "name": "西安饭庄(回民街店)", "reason": "unknown_food_semantics"}, {"date": "2026-04-21", "type": "dinner", "name": "西安饭庄(回民街店)", "reason": "unknown_food_semantics"}, {"date": "2026-04-22", "type": "dinner", "name": "西安饭庄(回民街店)", "reason": "unknown_food_semantics"}, {"date": "2026-04-23", "type": "dinner", "name": "西安饭庄(回民街店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 373, "expected_total_attractions": 1865, "reported_total_attractions": 1450, "meal_per_person_cost_sum": 1400, "expected_total_meals": 7000, "reported_total_meals": 3000, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "大蓉和(春熙店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "陈麻婆豆腐(总府路店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "蜀九香(都江堰店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "陈麻婆豆腐(武侯祠店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "蜀九香(武侯祠店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "陈麻婆豆腐(青羊店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "蜀九香(成华店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "陈麻婆豆腐(成华店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-11", "type": "lunch", "name": "蜀九香(春熙店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-11", "type": "dinner", "name": "陈麻婆豆腐(春熙店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "陈麻婆豆腐", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "陈麻婆豆腐(总府路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "陈麻婆豆腐(武侯祠店)"}, {"date": "2026-05-09", "type": "dinner", "name": "陈麻婆豆腐(青羊店)"}, {"date": "2026-05-10", "type": "dinner", "name": "陈麻婆豆腐(成华店)"}, {"date": "2026-05-11", "type": "dinner", "name": "陈麻婆豆腐(春熙店)"}]}, {"name_key": "蜀九香", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "蜀九香(都江堰店)"}, {"date": "2026-05-09", "type": "lunch", "name": "蜀九香(武侯祠店)"}, {"date": "2026-05-10", "type": "lunch", "name": "蜀九香(成华店)"}, {"date": "2026-05-11", "type": "lunch", "name": "蜀九香(春熙店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2900, "diff": 100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 2, "total": 3400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 290.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 3400, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 2200, "target_max_total": 3700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "里白云南家常菜", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6873, "total": 7873, "diff": -1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 874.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 632, "expected_total_meals": 1896, "reported_total_meals": 1248, "reported_total_transportation": 600}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1600, "expected_total_meals": 3200, "reported_total_meals": 2244, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 205, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 568, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 205, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 568, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 690, "meal_per_person_cost_sum": 1449, "expected_total_meals": 4347, "reported_total_meals": 2142, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 690, "meal_per_person_cost_sum": 1449, "expected_total_meals": 4347, "reported_total_meals": 2142, "reported_total_transportation": 300}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 480, "expected_total_attractions": 960, "reported_total_attractions": 640, "meal_per_person_cost_sum": 1440, "expected_total_meals": 2880, "reported_total_meals": 960, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 480, "expected_total_attractions": 960, "reported_total_attractions": 640, "meal_per_person_cost_sum": 1440, "expected_total_meals": 2880, "reported_total_meals": 960, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 3600, "reported_total_hotels": 3600, "expected_total_attractions": 960, "reported_total_attractions": 640, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 12, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_per_person_cost_sum": 719, "expected_total_meals": 2876, "reported_total_meals": 1488, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 600, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2025-05-06", "type": "lunch", "name": "清真马杰山牛肉汤馆", "estimated_cost": 18, "min_expected_cost": 25}]}}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-05", "day_index": 0, "name": "汉口江滩"}, {"date": "2026-05-07", "day_index": 2, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "汉味轩", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "汉味轩", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "汉味轩", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "汉味轩", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "汉味轩", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 300, "meal_per_person_cost_sum": 800, "expected_total_meals": 1600, "reported_total_meals": 640, "reported_total_transportation": 260}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州老城厢", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 220, "expected_total_attractions": 660, "reported_total_attractions": 510, "meal_per_person_cost_sum": 880, "expected_total_meals": 2640, "reported_total_meals": 1080, "reported_total_transportation": 300}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-04", "day_index": 1, "name": "南京博物院"}, {"date": "2026-04-07", "day_index": 4, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2000, "total": 1900, "diff": 100, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 1, "total": 2400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 380.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1300, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 125, "expected_total_attractions": 125, "reported_total_attractions": 125, "meal_per_person_cost_sum": 802, "expected_total_meals": 802, "reported_total_meals": 555, "reported_total_transportation": 120}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-21", "lunch": "友好饭店·新友记中餐厅", "dinner": "友好饭店·新友记中餐厅"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饭店·新友记中餐厅", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-18", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·新友记中餐厅"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}]`
