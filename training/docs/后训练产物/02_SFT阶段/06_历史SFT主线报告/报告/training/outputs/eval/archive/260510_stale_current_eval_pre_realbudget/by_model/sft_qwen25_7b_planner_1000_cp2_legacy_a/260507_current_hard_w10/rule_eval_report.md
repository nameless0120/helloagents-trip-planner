# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v1_current_hard_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_current_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 43 | 299 | 14.38% |
| attraction_budget_party_relation_ok | 110 | 299 | 36.79% |
| attraction_count_ok | 292 | 299 | 97.66% |
| attraction_diversity_ok | 204 | 299 | 68.23% |
| attraction_grounding_ok | 279 | 299 | 93.31% |
| attraction_repeat_limit_ok | 204 | 299 | 68.23% |
| budget_arithmetic_consistent | 233 | 299 | 77.93% |
| budget_consistent | 233 | 299 | 77.93% |
| budget_level_aligned | 171 | 299 | 57.19% |
| budget_preference_aligned | 171 | 299 | 57.19% |
| budget_relationship_ok | 48 | 299 | 16.05% |
| budget_selection_ok | 80 | 299 | 26.76% |
| budget_user_constraint_ok | 215 | 299 | 71.91% |
| budget_within_user_budget | 248 | 299 | 82.94% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 296 | 299 | 99.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 296 | 299 | 99.00% |
| dpo_soft_pass | 57 | 299 | 19.06% |
| dpo_soft_recomputed_budget_pass | 27 | 299 | 9.03% |
| hard_pass | 188 | 299 | 62.88% |
| hotel_budget_covers_nights | 171 | 299 | 57.19% |
| hotel_budget_relation_ok | 177 | 299 | 59.20% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 74 | 299 | 24.75% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 226 | 299 | 75.59% |
| meal_diversity_ok | 226 | 299 | 75.59% |
| meal_grounding_ok | 208 | 299 | 69.57% |
| meal_lunch_dinner_same_day_ok | 259 | 299 | 86.62% |
| meal_repeat_limit_ok | 242 | 299 | 80.94% |
| meal_specific_ok | 292 | 299 | 97.66% |
| meal_valid_semantics_ok | 231 | 299 | 77.26% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 80 | 299 | 26.76% |
| recomputed_budget_hard_ok | 119 | 299 | 39.80% |
| recomputed_budget_level_aligned | 80 | 299 | 26.76% |
| recomputed_budget_preference_aligned | 80 | 299 | 26.76% |
| recomputed_budget_user_constraint_ok | 119 | 299 | 39.80% |
| recomputed_budget_within_user_budget | 142 | 299 | 47.49% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 22 | 299 | 7.36% |
| sft_hard_pass | 188 | 299 | 62.88% |
| sft_no_budget_sum_hard_pass | 188 | 299 | 62.88% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 297 | 299 | 99.33% |
| weather_match | 297 | 299 | 99.33% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9453,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9911,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5281,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8346,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8346,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9233,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 659.258,
    "p50": 586.33,
    "p90": 1102.0
  },
  "recomputed_budget_total": {
    "avg": 7445.6555,
    "p50": 6615.0,
    "p90": 13176.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "attraction_budget_inconsistent": 256,
  "budget_relationship_mismatch": 251,
  "hotel_budget_underestimated": 128,
  "budget_preference_mismatch": 128,
  "attraction_repeat_too_many": 95,
  "budget_hard_constraint_exceeded": 84,
  "meal_cost_scale_too_low": 73,
  "meal_invalid_name": 68,
  "budget_arithmetic_inconsistent": 66,
  "meal_repeat_too_many": 57,
  "meal_same_day_lunch_dinner_repeat": 40,
  "meal_grounding_miss": 23,
  "meal_placeholder": 7,
  "too_many_attractions": 7,
  "weather_mismatch": 2,
  "schema": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1400, "total": 1300, "diff": 100, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 433.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 481, "expected_total_meals": 481, "reported_total_meals": 340, "reported_total_transportation": 100}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 252, "expected_total_attractions": 756, "reported_total_attractions": 651, "meal_per_person_cost_sum": 2160, "expected_total_meals": 6480, "reported_total_meals": 1449, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 252, "expected_total_attractions": 756, "reported_total_attractions": 651, "meal_per_person_cost_sum": 2160, "expected_total_meals": 6480, "reported_total_meals": 1449, "reported_total_transportation": 200}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "味道制造·桂林菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-01", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-02", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-03", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 710, "meal_per_person_cost_sum": 1096, "expected_total_meals": 2192, "reported_total_meals": 1260, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 600, "meal_per_person_cost_sum": 1213, "expected_total_meals": 4852, "reported_total_meals": 500, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 600, "meal_per_person_cost_sum": 1213, "expected_total_meals": 4852, "reported_total_meals": 500, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 960, "reported_total_attractions": 600, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11896, "total": 11996, "diff": -100, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 749.75, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 5900, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 1180, "meal_per_person_cost_sum": 984, "expected_total_meals": 3936, "reported_total_meals": 2016, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 1180, "meal_per_person_cost_sum": 984, "expected_total_meals": 3936, "reported_total_meals": 2016, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 434, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 486, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 434, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 486, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1800, "reported_total_hotels": 1800, "expected_total_attractions": 638, "reported_total_attractions": 434, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "流花湖公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-02", "day_index": 0, "name": "流花湖公园"}, {"date": "2026-07-06", "day_index": 4, "name": "流花湖公园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 255, "expected_total_attractions": 255, "reported_total_attractions": 430, "meal_per_person_cost_sum": 1132, "expected_total_meals": 1132, "reported_total_meals": 1080, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 255, "expected_total_attractions": 255, "reported_total_attractions": 430, "meal_per_person_cost_sum": 1132, "expected_total_meals": 1132, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "国立西南联合大学旧址", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "国立西南联合大学旧址"}, {"date": "2026-04-05", "day_index": 2, "name": "国立西南联合大学旧址"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-03", "type": "lunch", "name": "云南民族特色餐厅"}, {"date": "2026-04-03", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-04", "type": "lunch", "name": "民族风味餐厅"}, {"date": "2026-04-04", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-05", "type": "lunch", "name": "民族风味餐厅"}, {"date": "2026-04-05", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-06", "type": "lunch", "name": "民族风味餐厅"}, {"date": "2026-04-06", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-07", "type": "lunch", "name": "民族风味餐厅"}, {"date": "2026-04-07", "type": "dinner", "name": "本地家常菜馆"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-04-19", "day_index": 0, "name": "西安博物院"}, {"date": "2026-04-21", "day_index": 2, "name": "西安博物院"}, {"date": "2026-04-23", "day_index": 4, "name": "西安博物院"}]}, {"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-20", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2026-04-23", "day_index": 4, "name": "陕西历史博物馆"}]}, {"name_key": "大雁塔", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-20", "day_index": 1, "name": "大雁塔"}, {"date": "2026-04-22", "day_index": 3, "name": "大雁塔"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 165, "expected_total_attractions": 825, "reported_total_attractions": 1625, "meal_per_person_cost_sum": 1150, "expected_total_meals": 5750, "reported_total_meals": 2500, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蜀九香火锅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "蜀九香火锅(宽窄巷子店)"}, {"date": "2026-05-08", "type": "dinner", "name": "蜀九香火锅(春熙路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "蜀九香火锅(春熙路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "蜀九香火锅(春熙路店)"}, {"date": "2026-05-11", "type": "dinner", "name": "蜀九香火锅(春熙路店)"}]}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1704, "expected_total_meals": 3408, "reported_total_meals": 1644, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 4500, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "里白云南家常菜", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 675, "meal_per_person_cost_sum": 632, "expected_total_meals": 1896, "reported_total_meals": 1925, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 675, "meal_per_person_cost_sum": 632, "expected_total_meals": 1896, "reported_total_meals": 1925, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2193, "total": 2293, "diff": -100, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 764.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 305, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 688, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 305, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 688, "reported_total_transportation": 300}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 1484, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 1484, "reported_total_transportation": 600}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "东湖听涛景区内餐厅", "reason": "non_food_poi_name"}, {"date": "2026-05-06", "type": "lunch", "name": "黄鹤楼景区内餐厅", "reason": "non_food_poi_name"}, {"date": "2026-05-09", "type": "dinner", "name": "返程前晚餐", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 140, "meal_per_person_cost_sum": 610, "expected_total_meals": 1220, "reported_total_meals": 600, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 140, "meal_per_person_cost_sum": 610, "expected_total_meals": 1220, "reported_total_meals": 600, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州老灶头", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "lunch", "name": "苏州老灶头", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "lunch", "name": "苏州老灶头", "reason": "unknown_food_semantics"}, {"date": "2026-06-05", "type": "lunch", "name": "苏州老灶头", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5510, "total": 5460, "diff": 50, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 455.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "南京博物院"}, {"date": "2026-04-06", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 155, "expected_total_attractions": 155, "reported_total_attractions": 225, "meal_per_person_cost_sum": 735, "expected_total_meals": 735, "reported_total_meals": 1008, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 155, "expected_total_attractions": 155, "reported_total_attractions": 225, "meal_per_person_cost_sum": 735, "expected_total_meals": 735, "reported_total_meals": 1008, "reported_total_transportation": 200}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "隋唐城遗址植物园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2025-05-03", "day_index": 0, "name": "隋唐城遗址植物园"}, {"date": "2025-05-05", "day_index": 2, "name": "隋唐城遗址植物园"}, {"date": "2025-05-06", "day_index": 3, "name": "隋唐城遗址植物园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_per_person_cost_sum": 701, "expected_total_meals": 2804, "reported_total_meals": 1088, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "束河古镇"}, {"date": "2026-05-10", "day_index": 3, "name": "束河古镇"}]}, {"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 1, "name": "黑龙潭"}, {"date": "2026-05-09", "day_index": 2, "name": "黑龙潭"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 560, "expected_total_attractions": 1120, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 560, "expected_total_attractions": 1120, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南宋德寿宫遗址博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-18", "day_index": 1, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-06-21", "day_index": 4, "name": "南宋德寿宫遗址博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-19", "lunch": "友好饭店·新友记中餐厅", "dinner": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "lunch": "友好饭店·新友记中餐厅", "dinner": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "lunch": "友好饭店·新友记中餐厅", "dinner": "友好饭店·新友记中餐厅"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饭店·新友记中餐厅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-18", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "dinner", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·新友记中餐厅"}]}]}]`
