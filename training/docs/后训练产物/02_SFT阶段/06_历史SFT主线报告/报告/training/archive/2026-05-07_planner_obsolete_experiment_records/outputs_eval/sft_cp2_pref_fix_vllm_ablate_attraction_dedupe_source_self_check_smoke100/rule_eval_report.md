# Rule Eval Report: sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_source_self_check_smoke100

- records: 100
- generations: `training/outputs/eval/sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_source_self_check_smoke100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_pref_fix_attraction_prompt_ablation_attraction_dedupe_source_self_check_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 97 | 97 | 100.00% |
| attraction_budget_consistent | 9 | 97 | 9.28% |
| attraction_budget_party_relation_ok | 41 | 97 | 42.27% |
| attraction_count_ok | 97 | 97 | 100.00% |
| attraction_diversity_ok | 62 | 97 | 63.92% |
| attraction_grounding_ok | 89 | 97 | 91.75% |
| attraction_repeat_limit_ok | 62 | 97 | 63.92% |
| budget_arithmetic_consistent | 75 | 97 | 77.32% |
| budget_consistent | 75 | 97 | 77.32% |
| budget_level_aligned | 59 | 97 | 60.82% |
| budget_preference_aligned | 59 | 97 | 60.82% |
| budget_relationship_ok | 11 | 97 | 11.34% |
| budget_selection_ok | 48 | 97 | 49.48% |
| budget_user_constraint_ok | 91 | 97 | 93.81% |
| budget_within_user_budget | 95 | 97 | 97.94% |
| city_ok | 97 | 97 | 100.00% |
| date_range_ok | 97 | 97 | 100.00% |
| day_dates_ok | 97 | 97 | 100.00% |
| day_index_ok | 97 | 97 | 100.00% |
| days_len_ok | 97 | 97 | 100.00% |
| dpo_soft_pass | 27 | 97 | 27.84% |
| dpo_soft_recomputed_budget_pass | 19 | 97 | 19.59% |
| hard_pass | 82 | 97 | 84.54% |
| hotel_budget_covers_nights | 64 | 97 | 65.98% |
| hotel_budget_relation_ok | 65 | 97 | 67.01% |
| hotel_distance_placeholder_ok | 97 | 97 | 100.00% |
| hotel_grounding_ok | 96 | 97 | 98.97% |
| invalid_hotel_name_ok | 97 | 97 | 100.00% |
| json_extract_ok | 99 | 100 | 99.00% |
| legacy_hard_pass | 31 | 97 | 31.96% |
| location_object_ok | 97 | 97 | 100.00% |
| meal_budget_consistent | 0 | 97 | 0.00% |
| meal_complete | 97 | 97 | 100.00% |
| meal_cost_scale_ok | 31 | 97 | 31.96% |
| meal_diversity_ok | 68 | 97 | 70.10% |
| meal_grounding_ok | 91 | 97 | 93.81% |
| meal_lunch_dinner_same_day_ok | 85 | 97 | 87.63% |
| meal_repeat_limit_ok | 76 | 97 | 78.35% |
| meal_specific_ok | 96 | 97 | 98.97% |
| meal_valid_semantics_ok | 91 | 97 | 93.81% |
| middle_hotel_ok | 97 | 97 | 100.00% |
| recomputed_budget_fit_ok | 48 | 97 | 49.48% |
| recomputed_budget_hard_ok | 85 | 97 | 87.63% |
| recomputed_budget_level_aligned | 48 | 97 | 49.48% |
| recomputed_budget_preference_aligned | 48 | 97 | 49.48% |
| recomputed_budget_user_constraint_ok | 85 | 97 | 87.63% |
| recomputed_budget_within_user_budget | 94 | 97 | 96.91% |
| schema_ok | 97 | 100 | 97.00% |
| sft_budget_semantic_hard_pass | 9 | 97 | 9.28% |
| sft_hard_pass | 82 | 97 | 84.54% |
| sft_no_budget_sum_hard_pass | 82 | 97 | 84.54% |
| sft_strict_hard_pass | 0 | 97 | 0.00% |
| transportation_budget_nonnegative | 97 | 97 | 100.00% |
| weather_dates_ok | 97 | 97 | 100.00% |
| weather_match | 97 | 97 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9404,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9891,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9897,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7438,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 588.4251,
    "p50": 562.08,
    "p90": 814.5
  },
  "recomputed_budget_total": {
    "avg": 6373.7216,
    "p50": 6116.0,
    "p90": 10928.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 97,
  "attraction_budget_inconsistent": 88,
  "budget_relationship_mismatch": 86,
  "meal_cost_scale_too_low": 66,
  "budget_preference_mismatch": 38,
  "attraction_repeat_too_many": 35,
  "hotel_budget_underestimated": 33,
  "budget_arithmetic_inconsistent": 22,
  "meal_repeat_too_many": 21,
  "meal_same_day_lunch_dinner_repeat": 12,
  "meal_invalid_name": 6,
  "budget_hard_constraint_exceeded": 6,
  "schema": 2,
  "meal_placeholder": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-12", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 453, "expected_total_meals": 453, "reported_total_meals": 624, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 453, "expected_total_meals": 453, "reported_total_meals": 624, "reported_total_transportation": 300}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2650, "total": 2450, "diff": 200, "requested_budget": {"available": true, "amount": 3000, "scope": "total", "party_size": 1, "total": 3000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 816.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3000, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 625, "expected_total_meals": 625, "reported_total_meals": 1335, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 625, "expected_total_meals": 625, "reported_total_meals": 1335, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(依仁店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(七星路店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(七星路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 215, "expected_total_attractions": 430, "reported_total_attractions": 660, "meal_per_person_cost_sum": 585, "expected_total_meals": 1170, "reported_total_meals": 2856, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "束河古镇"}, {"date": "2026-05-13", "day_index": 3, "name": "束河古镇"}]}, {"name_key": "丽江古道藏家博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-12", "day_index": 2, "name": "丽江古道藏家博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-12", "type": "lunch", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-13", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 247, "expected_total_attractions": 494, "reported_total_attractions": 360, "meal_per_person_cost_sum": 937, "expected_total_meals": 1874, "reported_total_meals": 2784, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 247, "expected_total_attractions": 494, "reported_total_attractions": 360, "meal_per_person_cost_sum": 937, "expected_total_meals": 1874, "reported_total_meals": 2784, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 1180, "reported_total_attractions": 1160, "meal_per_person_cost_sum": 1039, "expected_total_meals": 4156, "reported_total_meals": 2904, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 1180, "reported_total_attractions": 1160, "meal_per_person_cost_sum": 1039, "expected_total_meals": 4156, "reported_total_meals": 2904, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "醉香隆(东湖店)", "dinner": "醉香隆(东湖店)"}, {"date": "2026-05-12", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 140, "meal_per_person_cost_sum": 895, "expected_total_meals": 1790, "reported_total_meals": 1200, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 140, "meal_per_person_cost_sum": 895, "expected_total_meals": 1790, "reported_total_meals": 1200, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2025-05-10", "day_index": 4, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 660, "meal_per_person_cost_sum": 783, "expected_total_meals": 1566, "reported_total_meals": 1254, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 660, "meal_per_person_cost_sum": 783, "expected_total_meals": 1566, "reported_total_meals": 1254, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安鼓楼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安鼓楼"}, {"date": "2026-08-07", "day_index": 3, "name": "西安鼓楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 737, "expected_total_meals": 3685, "reported_total_meals": 2950, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "平江路", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 0, "name": "平江路"}, {"date": "2026-05-10", "day_index": 2, "name": "平江路"}]}, {"name_key": "观前街", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-09", "day_index": 1, "name": "观前街"}, {"date": "2026-05-11", "day_index": 3, "name": "观前街"}, {"date": "2026-05-12", "day_index": 4, "name": "观前街"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 287, "expected_total_attractions": 574, "reported_total_attractions": 1120, "meal_per_person_cost_sum": 704, "expected_total_meals": 1408, "reported_total_meals": 1680, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "滨江道步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "滨江道步行街(天津·金街店)"}, {"date": "2026-07-07", "day_index": 2, "name": "滨江道步行街(天津·金街店)"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "青年餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-05", "type": "dinner", "name": "青年餐厅(津湾店)"}, {"date": "2026-07-06", "type": "dinner", "name": "青年餐厅(津湾店)"}, {"date": "2026-07-07", "type": "dinner", "name": "青年餐厅(津湾店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 330, "reported_total_attractions": 240, "meal_per_person_cost_sum": 691, "expected_total_meals": 2073, "reported_total_meals": 1899, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "海东茄子烧烤(古城店)", "dinner": "海东茄子烧烤(锦生店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5994, "total": 6094, "diff": -100, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 3, "total": 9800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 677.11, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 6400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 430, "expected_total_meals": 1290, "reported_total_meals": 1569, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "云南美术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "云南美术馆(五一路)"}, {"date": "2026-04-09", "day_index": 3, "name": "云南美术馆(五一路)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10150, "total": 9150, "diff": 1000, "requested_budget": {"available": true, "amount": 23400, "scope": "total", "party_size": 5, "total": 23400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 366.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 23400, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 15200, "target_max_total": 23400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-06", "lunch": "随园食单(善德居店)", "dinner": "随园食单(善德居店)"}, {"date": "2026-09-07", "lunch": "随园食单(善德居店)", "dinner": "随园食单(善德居店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "随园食单", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-06", "type": "lunch", "name": "随园食单(善德居店)"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)"}]}, {"name_key": "蒙自小黄牛米线", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-04", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-05", "type": "breakfast", "name": "蒙自小黄牛米线(S湾海景店)"}, {"date": "2026-09-06", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-07", "type": "breakfast", "name": "蒙自小黄牛米线"}]}]}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 75, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1246, "expected_total_meals": 1246, "reported_total_meals": 1364, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 75, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1246, "expected_total_meals": 1246, "reported_total_meals": 1364, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 75, "reported_total_attractions": 120, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-04-06", "type": "dinner", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 1060, "meal_per_person_cost_sum": 922, "expected_total_meals": 1844, "reported_total_meals": 3720, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 1060, "meal_per_person_cost_sum": 922, "expected_total_meals": 1844, "reported_total_meals": 3720, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南宋德寿宫遗址博物馆", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-05-02", "day_index": 2, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-05-03", "day_index": 3, "name": "南宋德寿宫遗址博物馆"}]}, {"name_key": "文房文化体验馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "文房文化体验馆"}, {"date": "2026-05-03", "day_index": 3, "name": "文房文化体验馆"}]}, {"name_key": "巧思梦幻屋", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "巧思梦幻屋"}, {"date": "2026-05-03", "day_index": 3, "name": "巧思梦幻屋"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 430, "expected_total_attractions": 1720, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 803, "expected_total_meals": 3212, "reported_total_meals": 1128, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 430, "expected_total_attractions": 1720, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 803, "expected_total_meals": 3212, "reported_total_meals": 1128, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-08", "lunch": "金陵家宴·金陵春.南京菜(夫子庙店)", "dinner": "金陵家宴·金陵春.南京菜(夫子庙店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6394, "total": 6494, "diff": -100, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 541.17, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 3300, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 105, "meal_per_person_cost_sum": 750, "expected_total_meals": 2250, "reported_total_meals": 1989, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南宋德寿宫遗址博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-21", "day_index": 1, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-06-24", "day_index": 4, "name": "南宋德寿宫遗址博物馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 40, "expected_total_attractions": 200, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1057, "expected_total_meals": 5285, "reported_total_meals": 3470, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000021
- request: 上海 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-06-21", "type": "lunch", "name": "Solo(衡山路店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-21", "type": "lunch", "name": "Solo(衡山路店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2550, "reported_total_hotels": 5100, "diff": 2550, "covers_nights": false}}]`
