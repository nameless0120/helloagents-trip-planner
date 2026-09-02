# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_A

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/A/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 250 | 296 | 84.46% |
| attraction_budget_consistent | 39 | 296 | 13.18% |
| attraction_budget_party_relation_ok | 86 | 296 | 29.05% |
| attraction_count_ok | 296 | 296 | 100.00% |
| attraction_diversity_ok | 251 | 296 | 84.80% |
| attraction_grounding_ok | 295 | 296 | 99.66% |
| attraction_repeat_limit_ok | 251 | 296 | 84.80% |
| budget_arithmetic_consistent | 163 | 296 | 55.07% |
| budget_consistent | 163 | 296 | 55.07% |
| budget_level_aligned | 121 | 296 | 40.88% |
| budget_preference_aligned | 121 | 296 | 40.88% |
| budget_relationship_ok | 26 | 296 | 8.78% |
| budget_user_constraint_ok | 253 | 296 | 85.47% |
| budget_within_user_budget | 283 | 296 | 95.61% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 0 | 296 | 0.00% |
| hard_pass | 0 | 296 | 0.00% |
| hotel_budget_covers_nights | 106 | 296 | 35.81% |
| hotel_budget_relation_ok | 123 | 296 | 41.55% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 296 | 296 | 100.00% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 20 | 296 | 6.76% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_budget_consistent | 0 | 296 | 0.00% |
| meal_complete | 295 | 296 | 99.66% |
| meal_cost_scale_ok | 200 | 296 | 67.57% |
| meal_diversity_ok | 208 | 296 | 70.27% |
| meal_grounding_ok | 166 | 296 | 56.08% |
| meal_lunch_dinner_same_day_ok | 242 | 296 | 81.76% |
| meal_repeat_limit_ok | 233 | 296 | 78.72% |
| meal_specific_ok | 284 | 296 | 95.95% |
| meal_valid_semantics_ok | 192 | 296 | 64.86% |
| middle_hotel_ok | 296 | 296 | 100.00% |
| schema_ok | 296 | 300 | 98.67% |
| sft_budget_semantic_hard_pass | 10 | 296 | 3.38% |
| sft_hard_pass | 0 | 296 | 0.00% |
| transportation_budget_nonnegative | 296 | 296 | 100.00% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 296 | 296 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9702,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5289,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.829,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.829,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9022,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 295,
  "budget_relationship_mismatch": 270,
  "attraction_budget_inconsistent": 257,
  "hotel_budget_underestimated": 190,
  "budget_preference_mismatch": 175,
  "budget_arithmetic_inconsistent": 133,
  "meal_invalid_name": 104,
  "meal_cost_scale_too_low": 96,
  "meal_repeat_too_many": 63,
  "meal_same_day_lunch_dinner_repeat": 54,
  "accommodation_type_mismatch": 46,
  "attraction_repeat_too_many": 45,
  "budget_hard_constraint_exceeded": 43,
  "meal_grounding_miss": 26,
  "meal_placeholder": 12,
  "schema": 2,
  "json_extract": 2
}
```

## Failure Examples

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1958, "total": 1758, "diff": 200, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 586.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 200}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1910, "total": 1710, "diff": 200, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 570.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 270, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 270, "reported_total_transportation": 200}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-03-06", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6430, "total": 4400, "diff": 2030, "requested_budget": {"available": true, "amount": 4400, "scope": "total", "party_size": 3, "total": 4400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 488.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4400, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2900, "target_max_total": 4400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "dinner", "name": "厦门屿海民宿晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-07", "type": "dinner", "name": "厦门屿海民宿晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-08", "type": "dinner", "name": "厦门屿海民宿晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "厦门屿海民宿晚餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "厦门屿海民宿晚餐"}, {"date": "2026-05-07", "type": "dinner", "name": "厦门屿海民宿晚餐"}, {"date": "2026-05-08", "type": "dinner", "name": "厦门屿海民宿晚餐"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-04", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_per_person_cost_sum": 744, "expected_total_meals": 744, "reported_total_meals": 390, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "苏焰·地标天津菜(多伦道店)", "dinner": "苏焰·地标天津菜(金海道店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1488, "expected_total_meals": 4464, "reported_total_meals": 1620, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 4500, "reported_total_hotels": 2250, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 514, "expected_total_meals": 514, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 514, "expected_total_meals": 514, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-06-04", "type": "dinner", "name": "精武鸭脖.地标美食(顶秀嘉园店)", "estimated_cost": 18, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 315, "meal_per_person_cost_sum": 228, "expected_total_meals": 456, "reported_total_meals": 618, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 315, "meal_per_person_cost_sum": 228, "expected_total_meals": 456, "reported_total_meals": 618, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 1050, "reported_total_attractions": 315, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 4, "checked_count": 4, "failure_count": 1, "failures": [{"date": "2026-09-01", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)", "estimated_cost": 66, "min_expected_cost": 70}]}}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "星巴克", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-08", "type": "lunch", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-09", "type": "lunch", "name": "星巴克(成都大魔方招商花园城店)"}, {"date": "2026-05-10", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-11", "type": "lunch", "name": "星巴克(成都SKP店)"}]}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1710, "expected_total_meals": 3420, "reported_total_meals": 1440, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5640, "total": 5640, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 705.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-29", "type": "dinner", "name": "杭州西湖风景名胜区附近小吃"}, {"date": "2026-04-30", "type": "dinner", "name": "杭州西湖风景名胜区附近小吃"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1000, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 600, "reported_total_attractions": 220, "meal_per_person_cost_sum": 676, "expected_total_meals": 2704, "reported_total_meals": 384, "reported_total_transportation": 200}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"name_key": "友好友善茶饮巴士", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-05", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-06", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-07", "type": "dinner", "name": "友好友善茶饮巴士"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3280, "total": 6600, "diff": -3320, "requested_budget": {"available": true, "amount": 6200, "scope": "total", "party_size": 2, "total": 6200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 825.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6200, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1104, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-08", "day_index": 2, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1400, "reported_total_hotels": 600, "diff": -800, "covers_nights": false}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "扬州东关街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 1, "name": "扬州东关街"}, {"date": "2026-05-10", "day_index": 3, "name": "扬州东关街"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 4000, "diff": -3500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5325, "total": 6115, "diff": -790, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 382.19, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5900, "target_max_total": 9600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 4000, "diff": -3500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 145, "expected_total_attractions": 580, "reported_total_attractions": 165, "meal_per_person_cost_sum": 520, "expected_total_meals": 2080, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_per_person_cost_sum": 1136, "expected_total_meals": 2272, "reported_total_meals": 1008, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_per_person_cost_sum": 1136, "expected_total_meals": 2272, "reported_total_meals": 1008, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 2400, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-08", "type": "dinner", "name": "陶德砂锅(蜀汉店)", "estimated_cost": 69, "min_expected_cost": 70}]}}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城内的特色餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2780, "total": 2880, "diff": -100, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 360.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-02", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "dinner", "name": "苏州乐园森林世界餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 3750, "diff": -6250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4610, "total": 4000, "diff": 610, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 333.33, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 3750, "diff": -6250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 157, "expected_total_attractions": 471, "reported_total_attractions": 217, "meal_per_person_cost_sum": 1560, "expected_total_meals": 4680, "reported_total_meals": 540, "reported_total_transportation": 800}}]`
