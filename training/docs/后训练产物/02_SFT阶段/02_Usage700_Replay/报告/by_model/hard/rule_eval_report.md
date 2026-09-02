# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260511_replay_usage700_from_lr6e5_lr2e5/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 78 | 299 | 26.09% |
| attraction_budget_party_relation_ok | 277 | 299 | 92.64% |
| attraction_count_ok | 298 | 299 | 99.67% |
| attraction_diversity_ok | 248 | 299 | 82.94% |
| attraction_grounding_ok | 296 | 299 | 99.00% |
| attraction_repeat_limit_ok | 248 | 299 | 82.94% |
| budget_arithmetic_consistent | 191 | 299 | 63.88% |
| budget_consistent | 191 | 299 | 63.88% |
| budget_level_aligned | 217 | 299 | 72.58% |
| budget_preference_aligned | 217 | 299 | 72.58% |
| budget_relationship_ok | 201 | 299 | 67.22% |
| budget_selection_ok | 146 | 299 | 48.83% |
| budget_user_constraint_ok | 270 | 299 | 90.30% |
| budget_within_user_budget | 276 | 299 | 92.31% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 157 | 299 | 52.51% |
| dpo_soft_recomputed_budget_pass | 104 | 299 | 34.78% |
| hard_pass | 291 | 299 | 97.32% |
| hotel_budget_covers_nights | 268 | 299 | 89.63% |
| hotel_budget_relation_ok | 272 | 299 | 90.97% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 147 | 299 | 49.16% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 1 | 299 | 0.33% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 238 | 299 | 79.60% |
| meal_diversity_ok | 249 | 299 | 83.28% |
| meal_grounding_ok | 296 | 299 | 99.00% |
| meal_lunch_dinner_same_day_ok | 281 | 299 | 93.98% |
| meal_repeat_limit_ok | 260 | 299 | 86.96% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 297 | 299 | 99.33% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 146 | 299 | 48.83% |
| recomputed_budget_hard_ok | 216 | 299 | 72.24% |
| recomputed_budget_level_aligned | 146 | 299 | 48.83% |
| recomputed_budget_preference_aligned | 146 | 299 | 48.83% |
| recomputed_budget_user_constraint_ok | 216 | 299 | 72.24% |
| recomputed_budget_within_user_budget | 249 | 299 | 83.28% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 174 | 299 | 58.19% |
| sft_hard_pass | 291 | 299 | 97.32% |
| sft_no_budget_sum_hard_pass | 291 | 299 | 97.32% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 298 | 299 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9793,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.999,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8757,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 926.0883,
    "p50": 940.0,
    "p90": 1430.75
  },
  "recomputed_budget_total": {
    "avg": 9984.4181,
    "p50": 9324.0,
    "p90": 17595.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "attraction_budget_inconsistent": 221,
  "budget_arithmetic_inconsistent": 108,
  "budget_relationship_mismatch": 98,
  "budget_preference_mismatch": 82,
  "meal_cost_scale_too_low": 61,
  "attraction_repeat_too_many": 51,
  "meal_repeat_too_many": 39,
  "hotel_budget_underestimated": 31,
  "budget_hard_constraint_exceeded": 29,
  "meal_same_day_lunch_dinner_repeat": 18,
  "meal_invalid_name": 2,
  "schema": 1,
  "weather_mismatch": 1,
  "meal_grounding_miss": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.2.attractions.1.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.attractions.1.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.2.attractions.1.visit_duration\n  Field required [type=missing, input_value={'name': '自由活动', ...None, 'ticket_price': 0}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "大理古城"}, {"date": "2026-05-13", "day_index": 2, "name": "大理古城"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "lunch", "name": "洱海大游船", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8334, "total": 6234, "diff": 2100, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 692.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 622, "expected_total_meals": 1866, "reported_total_meals": 1419, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 622, "expected_total_meals": 1866, "reported_total_meals": 1419, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 520, "meal_per_person_cost_sum": 712, "expected_total_meals": 2848, "reported_total_meals": 2240, "reported_total_transportation": 240}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 520, "meal_per_person_cost_sum": 712, "expected_total_meals": 2848, "reported_total_meals": 2240, "reported_total_transportation": 240}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9930, "total": 10930, "diff": -1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1366.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1085, "expected_total_attractions": 2170, "reported_total_attractions": 1830, "meal_per_person_cost_sum": 1020, "expected_total_meals": 2040, "reported_total_meals": 2400, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1085, "expected_total_attractions": 2170, "reported_total_attractions": 1830, "meal_per_person_cost_sum": 1020, "expected_total_meals": 2040, "reported_total_meals": 2400, "reported_total_transportation": 1800}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-08", "lunch": "滋粥楼·顺德菜(番禺广场总店)", "dinner": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 485, "expected_total_attractions": 485, "reported_total_attractions": 535, "meal_per_person_cost_sum": 1371, "expected_total_meals": 1371, "reported_total_meals": 1006, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 485, "expected_total_attractions": 485, "reported_total_attractions": 535, "meal_per_person_cost_sum": 1371, "expected_total_meals": 1371, "reported_total_meals": 1006, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 686, "expected_total_attractions": 3430, "reported_total_attractions": 3165, "meal_per_person_cost_sum": 836, "expected_total_meals": 4180, "reported_total_meals": 5700, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 686, "expected_total_attractions": 3430, "reported_total_attractions": 3165, "meal_per_person_cost_sum": 836, "expected_total_meals": 4180, "reported_total_meals": 5700, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 399, "expected_total_attractions": 798, "reported_total_attractions": 758, "meal_per_person_cost_sum": 790, "expected_total_meals": 1580, "reported_total_meals": 2228, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 399, "expected_total_attractions": 798, "reported_total_attractions": 758, "meal_per_person_cost_sum": 790, "expected_total_meals": 1580, "reported_total_meals": 2228, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 839, "expected_total_attractions": 4195, "reported_total_attractions": 4195, "meal_per_person_cost_sum": 807, "expected_total_meals": 4035, "reported_total_meals": 5835, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 16200, "reported_total_hotels": 10800, "expected_total_attractions": 4195, "reported_total_attractions": 4195, "meal_scale_eval": {"ok": false, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-08-05", "type": "dinner", "name": "果渊斋老米家泡馍馆(回坊总店)", "estimated_cost": 31, "min_expected_cost": 50}, {"date": "2026-08-08", "type": "lunch", "name": "虎子水盆羊肉(翠华路总店)", "estimated_cost": 43, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9670, "total": 10670, "diff": -1000, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1067.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1248, "expected_total_attractions": 2496, "reported_total_attractions": 2470, "meal_per_person_cost_sum": 2627, "expected_total_meals": 5254, "reported_total_meals": 5400, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1248, "expected_total_attractions": 2496, "reported_total_attractions": 2470, "meal_per_person_cost_sum": 2627, "expected_total_meals": 5254, "reported_total_meals": 5400, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3574, "total": 3074, "diff": 500, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1024.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 845, "expected_total_meals": 845, "reported_total_meals": 509, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12102, "total": 12002, "diff": 100, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1500.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 576, "expected_total_attractions": 1152, "reported_total_attractions": 1188, "meal_per_person_cost_sum": 1474, "expected_total_meals": 2948, "reported_total_meals": 2614, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 1034, "expected_total_meals": 4136, "reported_total_meals": 5528, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 1034, "expected_total_meals": 4136, "reported_total_meals": 5528, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 627, "expected_total_meals": 2508, "reported_total_meals": 2100, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 627, "expected_total_meals": 2508, "reported_total_meals": 2100, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10897, "total": 7997, "diff": 2900, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 888.56, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 775, "expected_total_attractions": 2325, "reported_total_attractions": 2232, "meal_per_person_cost_sum": 2325, "expected_total_meals": 6975, "reported_total_meals": 4365, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 677, "expected_total_meals": 2031, "reported_total_meals": 1809, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 10529, "total": 10529, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 877.42, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 10529, "total": 10529, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 877.42, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1264, "expected_total_attractions": 2528, "reported_total_attractions": 2308, "meal_per_person_cost_sum": 809, "expected_total_meals": 1618, "reported_total_meals": 1800, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1264, "expected_total_attractions": 2528, "reported_total_attractions": 2308, "meal_per_person_cost_sum": 809, "expected_total_meals": 1618, "reported_total_meals": 1800, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 2528, "reported_total_attractions": 2308, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-14", "type": "lunch", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "湖北省博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "湖北省博物馆"}, {"date": "2026-05-13", "day_index": 4, "name": "湖北省博物馆"}]}, {"name_key": "东湖磨山景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-13", "day_index": 4, "name": "东湖磨山景区"}, {"date": "2026-05-13", "day_index": 4, "name": "东湖磨山景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 329, "expected_total_attractions": 658, "reported_total_attractions": 606, "meal_per_person_cost_sum": 1021, "expected_total_meals": 2042, "reported_total_meals": 2356, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 329, "expected_total_attractions": 658, "reported_total_attractions": 606, "meal_per_person_cost_sum": 1021, "expected_total_meals": 2042, "reported_total_meals": 2356, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7154, "total": 8154, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 815.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1554, "meal_per_person_cost_sum": 1102, "expected_total_meals": 2204, "reported_total_meals": 2600, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1554, "meal_per_person_cost_sum": 1102, "expected_total_meals": 2204, "reported_total_meals": 2600, "reported_total_transportation": 1800}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-24", "day_index": 3, "name": "杭州西湖风景名胜区"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州西湖风景名胜区"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 26760, "total": 25760, "diff": 1000, "requested_budget": {"available": true, "amount": 27000, "scope": "total", "party_size": 5, "total": 27000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1030.4, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 27000, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 18900, "target_max_total": 27000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 18000, "reported_total_hotels": 18000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 402, "expected_total_attractions": 2010, "reported_total_attractions": 1810, "meal_per_person_cost_sum": 1182, "expected_total_meals": 5910, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`
