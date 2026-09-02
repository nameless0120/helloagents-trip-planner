# Rule Eval Report: sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_hard_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 63 | 300 | 21.00% |
| attraction_budget_party_relation_ok | 288 | 300 | 96.00% |
| attraction_count_ok | 300 | 300 | 100.00% |
| attraction_diversity_ok | 258 | 300 | 86.00% |
| attraction_grounding_ok | 291 | 300 | 97.00% |
| attraction_repeat_limit_ok | 258 | 300 | 86.00% |
| budget_arithmetic_consistent | 222 | 300 | 74.00% |
| budget_consistent | 222 | 300 | 74.00% |
| budget_level_aligned | 208 | 300 | 69.33% |
| budget_preference_aligned | 208 | 300 | 69.33% |
| budget_relationship_ok | 204 | 300 | 68.00% |
| budget_selection_ok | 153 | 300 | 51.00% |
| budget_user_constraint_ok | 287 | 300 | 95.67% |
| budget_within_user_budget | 300 | 300 | 100.00% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 143 | 300 | 47.67% |
| dpo_soft_recomputed_budget_pass | 97 | 300 | 32.33% |
| hard_pass | 284 | 300 | 94.67% |
| hotel_budget_covers_nights | 282 | 300 | 94.00% |
| hotel_budget_relation_ok | 285 | 300 | 95.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 300 | 300 | 100.00% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 152 | 300 | 50.67% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 220 | 300 | 73.33% |
| meal_diversity_ok | 234 | 300 | 78.00% |
| meal_grounding_ok | 293 | 300 | 97.67% |
| meal_lunch_dinner_same_day_ok | 289 | 300 | 96.33% |
| meal_repeat_limit_ok | 239 | 300 | 79.67% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 293 | 300 | 97.67% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 153 | 300 | 51.00% |
| recomputed_budget_hard_ok | 251 | 300 | 83.67% |
| recomputed_budget_level_aligned | 153 | 300 | 51.00% |
| recomputed_budget_preference_aligned | 153 | 300 | 51.00% |
| recomputed_budget_user_constraint_ok | 251 | 300 | 83.67% |
| recomputed_budget_within_user_budget | 285 | 300 | 95.00% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 180 | 300 | 60.00% |
| sft_hard_pass | 284 | 300 | 94.67% |
| sft_no_budget_sum_hard_pass | 284 | 300 | 94.67% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.984,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9953,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8274,
    "p50": 0.8333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 773.8516,
    "p50": 749.4,
    "p90": 1218.33
  },
  "recomputed_budget_total": {
    "avg": 8215.7033,
    "p50": 7498.0,
    "p90": 13704.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 237,
  "budget_relationship_mismatch": 96,
  "budget_preference_mismatch": 92,
  "meal_cost_scale_too_low": 80,
  "budget_arithmetic_inconsistent": 78,
  "meal_repeat_too_many": 61,
  "attraction_repeat_too_many": 42,
  "hotel_budget_underestimated": 18,
  "budget_hard_constraint_exceeded": 13,
  "meal_same_day_lunch_dinner_repeat": 11,
  "meal_invalid_name": 7
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 318, "expected_total_attractions": 318, "reported_total_attractions": 318, "meal_per_person_cost_sum": 546, "expected_total_meals": 546, "reported_total_meals": 582, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 437, "expected_total_attractions": 1311, "reported_total_attractions": 1269, "meal_per_person_cost_sum": 481, "expected_total_meals": 1443, "reported_total_meals": 1465, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 437, "expected_total_attractions": 1311, "reported_total_attractions": 1269, "meal_per_person_cost_sum": 481, "expected_total_meals": 1443, "reported_total_meals": 1465, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 345, "meal_per_person_cost_sum": 676, "expected_total_meals": 2028, "reported_total_meals": 1800, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 345, "meal_per_person_cost_sum": 676, "expected_total_meals": 2028, "reported_total_meals": 1800, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 405, "reported_total_attractions": 345, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-06", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "桂林市两江四湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-05", "day_index": 1, "name": "桂林市两江四湖景区"}, {"date": "2026-09-07", "day_index": 3, "name": "桂林市两江四湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1095, "expected_total_attractions": 2190, "reported_total_attractions": 2310, "meal_per_person_cost_sum": 599, "expected_total_meals": 1198, "reported_total_meals": 1438, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1095, "expected_total_attractions": 2190, "reported_total_attractions": 2310, "meal_per_person_cost_sum": 599, "expected_total_meals": 1198, "reported_total_meals": 1438, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州武林夜市", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州武林夜市"}, {"date": "2026-05-03", "day_index": 2, "name": "杭州武林夜市"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-02", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-03", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-04", "type": "lunch", "name": "杭州酒家(延安路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 218, "expected_total_attractions": 872, "reported_total_attractions": 716, "meal_per_person_cost_sum": 668, "expected_total_meals": 2672, "reported_total_meals": 2088, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-09", "lunch": "莱茵春天西餐厅(正义店)", "dinner": "莱茵春天西餐厅(美辰店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 2365, "meal_per_person_cost_sum": 795, "expected_total_meals": 3975, "reported_total_meals": 5845, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 2365, "meal_per_person_cost_sum": 795, "expected_total_meals": 3975, "reported_total_meals": 5845, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 1414, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 1414, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "银灯食府", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "银灯食府(丽丰国际中心店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-10", "type": "breakfast", "name": "银灯食府(文化公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 595, "expected_total_attractions": 595, "reported_total_attractions": 565, "meal_per_person_cost_sum": 1525, "expected_total_meals": 1525, "reported_total_meals": 836, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 595, "expected_total_attractions": 595, "reported_total_attractions": 565, "meal_per_person_cost_sum": 1525, "expected_total_meals": 1525, "reported_total_meals": 836, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 20600, "total": 21600, "diff": -1000, "requested_budget": {"available": true, "amount": 30900, "scope": "total", "party_size": 5, "total": 30900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 864.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 30900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 21600, "target_max_total": 30900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 5400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1225, "meal_per_person_cost_sum": 778, "expected_total_meals": 3890, "reported_total_meals": 5525, "reported_total_transportation": 8450}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-14", "lunch": "悦百味·品质川菜(UPARK公园店)", "dinner": "悦百味·品质川菜(成都环贸ICD店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "悦百味·品质川菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(UPARK公园店)"}, {"date": "2026-05-14", "type": "dinner", "name": "悦百味·品质川菜(成都环贸ICD店)"}, {"date": "2026-05-15", "type": "dinner", "name": "悦百味·品质川菜(悠方店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6666, "total": 7666, "diff": -1000, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 766.6, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-23", "lunch": "紫阳海鲜楼·传承闽味(长乐路总店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 435, "expected_total_attractions": 870, "reported_total_attractions": 842, "meal_per_person_cost_sum": 1393, "expected_total_meals": 2786, "reported_total_meals": 4874, "reported_total_transportation": 2200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 435, "expected_total_attractions": 870, "reported_total_attractions": 842, "meal_per_person_cost_sum": 1393, "expected_total_meals": 2786, "reported_total_meals": 4874, "reported_total_transportation": 2200}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 185, "meal_per_person_cost_sum": 545, "expected_total_meals": 545, "reported_total_meals": 616, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 325, "expected_total_attractions": 1300, "reported_total_attractions": 1232, "meal_per_person_cost_sum": 587, "expected_total_meals": 2348, "reported_total_meals": 1628, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 325, "expected_total_attractions": 1300, "reported_total_attractions": 1232, "meal_per_person_cost_sum": 587, "expected_total_meals": 2348, "reported_total_meals": 1628, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 502, "expected_total_attractions": 2008, "reported_total_attractions": 2608, "meal_per_person_cost_sum": 749, "expected_total_meals": 2996, "reported_total_meals": 3824, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 502, "expected_total_attractions": 2008, "reported_total_attractions": 2608, "meal_per_person_cost_sum": 749, "expected_total_meals": 2996, "reported_total_meals": 3824, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 2008, "reported_total_attractions": 2608, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 465, "meal_per_person_cost_sum": 569, "expected_total_meals": 1707, "reported_total_meals": 1434, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 465, "meal_per_person_cost_sum": 569, "expected_total_meals": 1707, "reported_total_meals": 1434, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 444, "expected_total_attractions": 1332, "reported_total_attractions": 1248, "meal_per_person_cost_sum": 1116, "expected_total_meals": 3348, "reported_total_meals": 2565, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 444, "expected_total_attractions": 1332, "reported_total_attractions": 1248, "meal_per_person_cost_sum": 1116, "expected_total_meals": 3348, "reported_total_meals": 2565, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 9213, "total": 9213, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1023.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 825, "expected_total_meals": 1650, "reported_total_meals": 1510, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 825, "expected_total_meals": 1650, "reported_total_meals": 1510, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1600, "reported_total_hotels": 1600, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-05-12", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-05-13", "type": "dinner", "name": "小鱼号酸菜鱼(积玉桥店)", "estimated_cost": 25, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1084, "expected_total_attractions": 2168, "reported_total_attractions": 2361, "meal_per_person_cost_sum": 665, "expected_total_meals": 1330, "reported_total_meals": 1294, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1084, "expected_total_attractions": 2168, "reported_total_attractions": 2361, "meal_per_person_cost_sum": 665, "expected_total_meals": 1330, "reported_total_meals": 1294, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6172, "total": 7172, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 717.2, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 791, "expected_total_attractions": 1582, "reported_total_attractions": 1688, "meal_per_person_cost_sum": 838, "expected_total_meals": 1676, "reported_total_meals": 2284, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 791, "expected_total_attractions": 1582, "reported_total_attractions": 1688, "meal_per_person_cost_sum": 838, "expected_total_meals": 1676, "reported_total_meals": 2284, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-22", "day_index": 1, "name": "杭州植物园"}, {"date": "2026-06-24", "day_index": 3, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 148, "expected_total_attractions": 740, "reported_total_attractions": 700, "meal_per_person_cost_sum": 1023, "expected_total_meals": 5115, "reported_total_meals": 6800, "reported_total_transportation": 5500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 148, "expected_total_attractions": 740, "reported_total_attractions": 700, "meal_per_person_cost_sum": 1023, "expected_total_meals": 5115, "reported_total_meals": 6800, "reported_total_transportation": 5500}}]`
