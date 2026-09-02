# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/base_qwen25_7b/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 278 | 299 | 92.98% |
| attraction_budget_consistent | 40 | 299 | 13.38% |
| attraction_budget_party_relation_ok | 86 | 299 | 28.76% |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_diversity_ok | 226 | 299 | 75.59% |
| attraction_grounding_ok | 295 | 299 | 98.66% |
| attraction_repeat_limit_ok | 226 | 299 | 75.59% |
| budget_arithmetic_consistent | 157 | 299 | 52.51% |
| budget_consistent | 157 | 299 | 52.51% |
| budget_level_aligned | 63 | 299 | 21.07% |
| budget_preference_aligned | 63 | 299 | 21.07% |
| budget_relationship_ok | 17 | 299 | 5.69% |
| budget_selection_ok | 121 | 299 | 40.47% |
| budget_user_constraint_ok | 269 | 299 | 89.97% |
| budget_within_user_budget | 277 | 299 | 92.64% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 10 | 299 | 3.34% |
| dpo_soft_recomputed_budget_pass | 10 | 299 | 3.34% |
| hard_pass | 249 | 299 | 83.28% |
| hotel_budget_covers_nights | 106 | 299 | 35.45% |
| hotel_budget_relation_ok | 137 | 299 | 45.82% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 296 | 299 | 99.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 14 | 299 | 4.68% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 1 | 299 | 0.33% |
| meal_complete | 298 | 299 | 99.67% |
| meal_cost_scale_ok | 116 | 299 | 38.80% |
| meal_diversity_ok | 70 | 299 | 23.41% |
| meal_grounding_ok | 278 | 299 | 92.98% |
| meal_lunch_dinner_same_day_ok | 237 | 299 | 79.26% |
| meal_repeat_limit_ok | 79 | 299 | 26.42% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 285 | 299 | 95.32% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 121 | 299 | 40.47% |
| recomputed_budget_hard_ok | 214 | 299 | 71.57% |
| recomputed_budget_level_aligned | 121 | 299 | 40.47% |
| recomputed_budget_preference_aligned | 121 | 299 | 40.47% |
| recomputed_budget_user_constraint_ok | 214 | 299 | 71.57% |
| recomputed_budget_within_user_budget | 236 | 299 | 78.93% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 7 | 299 | 2.34% |
| sft_hard_pass | 249 | 299 | 83.28% |
| sft_no_budget_sum_hard_pass | 249 | 299 | 83.28% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 298 | 299 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9533,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.99,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5,
    "p50": 0.4167,
    "p90": 0.8889
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9906,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 923.1573,
    "p50": 900.0,
    "p90": 1517.4
  },
  "recomputed_budget_total": {
    "avg": 9705.1037,
    "p50": 7920.0,
    "p90": 16760.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "budget_relationship_mismatch": 282,
  "attraction_budget_inconsistent": 259,
  "budget_preference_mismatch": 236,
  "meal_repeat_too_many": 220,
  "hotel_budget_underestimated": 193,
  "meal_cost_scale_too_low": 183,
  "budget_arithmetic_inconsistent": 142,
  "attraction_repeat_too_many": 73,
  "meal_same_day_lunch_dinner_repeat": 62,
  "budget_hard_constraint_exceeded": 30,
  "accommodation_type_mismatch": 21,
  "meal_invalid_name": 14,
  "meal_grounding_miss": 7,
  "weather_mismatch": 1,
  "schema": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "家旺小吃(解放路店)", "dinner": "家旺小吃(解放路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "家旺小吃", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "家旺小吃(解放路店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "家旺小吃(解放路店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "家旺小吃(解放路店)"}, {"date": "2026-05-13", "type": "lunch", "name": "家旺小吃(解放路店)"}, {"date": "2026-05-13", "type": "dinner", "name": "家旺小吃(解放路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6010, "total": 9520, "diff": -3510, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 3173.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "九孃豌豆粉店", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "九孃豌豆粉店"}, {"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店"}, {"date": "2026-05-13", "type": "breakfast", "name": "九孃豌豆粉店"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 3900, "diff": -3900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6795, "total": 6895, "diff": -100, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 766.11, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 3900, "diff": -3900, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京海底世界", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-08", "day_index": 2, "name": "南京海底世界"}, {"date": "2026-07-09", "day_index": 3, "name": "南京海底世界"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-07", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-08", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-09", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-02", "type": "dinner", "name": "钱潮夜市(地铁东城购物中心店)", "reason": "non_food_poi_name"}, {"date": "2026-05-03", "type": "dinner", "name": "闲林埠老街", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "肯德基", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-04", "type": "dinner", "name": "肯德基(市民中心1号店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 1410, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 880, "expected_total_meals": 1760, "reported_total_meals": 1260, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 1410, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 880, "expected_total_meals": 1760, "reported_total_meals": 1260, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 5200, "reported_total_hotels": 5200, "expected_total_attractions": 1410, "reported_total_attractions": 1155, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-09-05", "type": "dinner", "name": "松涧漓岸鱼餐吧", "estimated_cost": 50, "min_expected_cost": 70}, {"date": "2026-09-06", "type": "dinner", "name": "阳家将海鲜地摊烧烤", "estimated_cost": 50, "min_expected_cost": 70}, {"date": "2026-09-07", "type": "dinner", "name": "蜜棠升明月江景餐厅", "estimated_cost": 52, "min_expected_cost": 70}]}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "宽窄巷子景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "宽窄巷子景区"}, {"date": "2026-05-15", "day_index": 4, "name": "宽窄巷子景区"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}, {"name_key": "观锦餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "dinner", "name": "观锦餐厅(德商国际店)"}, {"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(德商国际店)"}, {"date": "2026-05-13", "type": "dinner", "name": "观锦餐厅(德商国际店)"}, {"date": "2026-05-14", "type": "dinner", "name": "观锦餐厅(德商国际店)"}, {"date": "2026-05-15", "type": "dinner", "name": "观锦餐厅(德商国际店)"}]}, {"name_key": "悦百味·品质川菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-13", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-15", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3194, "total": 2744, "diff": 450, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 274.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "昆明老街·美食天街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-07", "day_index": 0, "name": "昆明老街·美食天街(正义坊购物中心店)"}, {"date": "2026-04-11", "day_index": 4, "name": "昆明老街·美食天街(正义坊购物中心店)"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "莱茵春天西餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-08", "type": "dinner", "name": "莱茵春天西餐厅(正义店)"}, {"date": "2026-04-09", "type": "dinner", "name": "莱茵春天西餐厅(美辰店)"}, {"date": "2026-04-10", "type": "dinner", "name": "莱茵春天西餐厅(正义店)"}, {"date": "2026-04-11", "type": "dinner", "name": "莱茵春天西餐厅(正义店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 9000, "reported_total_hotels": 3000, "diff": -6000, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-10", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "银记肠粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "银记肠粉(北京路店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "银记肠粉(北京路店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "银记肠粉(北京路店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "银记肠粉(北京路店)"}, {"date": "2026-07-10", "type": "breakfast", "name": "银记肠粉(北京路店)"}]}, {"name_key": "民记煲仔饭", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "dinner", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-07", "type": "dinner", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-08", "type": "dinner", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-09", "type": "dinner", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-10", "type": "dinner", "name": "民记煲仔饭(北京路店)"}]}, {"name_key": "大鸽饭", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-07", "type": "lunch", "name": "大鸽饭(体育西店)"}, {"date": "2026-07-08", "type": "lunch", "name": "大鸽饭(北京路店)"}, {"date": "2026-07-09", "type": "lunch", "name": "大鸽饭(北京路店)"}, {"date": "2026-07-10", "type": "lunch", "name": "大鸽饭(北京路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 855, "expected_total_attractions": 855, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 715, "expected_total_meals": 715, "reported_total_meals": 504, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "铭家家宴·海鲜水饺·青岛菜·院子餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "lunch", "name": "铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店)"}, {"date": "2026-08-06", "type": "lunch", "name": "铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店)"}, {"date": "2026-08-07", "type": "lunch", "name": "铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店)"}, {"date": "2026-08-08", "type": "lunch", "name": "铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店)"}, {"date": "2026-08-09", "type": "lunch", "name": "铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店)"}]}, {"name_key": "魏家凉皮", "count": 9, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-06", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-07", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-08", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-09", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-09", "type": "dinner", "name": "魏家凉皮(西大街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 20250, "reported_total_hotels": 6750, "diff": -13500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 254, "expected_total_attractions": 1270, "reported_total_attractions": 240, "meal_per_person_cost_sum": 853, "expected_total_meals": 4265, "reported_total_meals": 1800, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-11", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-09", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-10", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-11", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 289, "expected_total_attractions": 578, "reported_total_attractions": 1015, "meal_per_person_cost_sum": 363, "expected_total_meals": 726, "reported_total_meals": 1080, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 289, "expected_total_attractions": 578, "reported_total_attractions": 1015, "meal_per_person_cost_sum": 363, "expected_total_meals": 726, "reported_total_meals": 1080, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9240, "total": 8840, "diff": 400, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1105.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 1380, "meal_per_person_cost_sum": 1229, "expected_total_meals": 2458, "reported_total_meals": 1860, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 1380, "meal_per_person_cost_sum": 1229, "expected_total_meals": 2458, "reported_total_meals": 1860, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "瓦当下·茶馆私房菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-01", "type": "lunch", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-02", "type": "lunch", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-03", "type": "lunch", "name": "瓦当下·茶馆私房菜(星悦汇店)"}]}, {"name_key": "玉桂樓·苏式美学园林餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "玉桂樓·苏式美学园林餐厅(斜塘老街店)"}, {"date": "2026-05-01", "type": "dinner", "name": "玉桂樓·苏式美学园林餐厅(斜塘老街店)"}, {"date": "2026-05-02", "type": "dinner", "name": "玉桂樓·苏式美学园林餐厅(斜塘老街店)"}, {"date": "2026-05-03", "type": "dinner", "name": "玉桂樓·苏式美学园林餐厅(斜塘老街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 11200, "reported_total_hotels": 5600, "diff": -5600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8325, "total": 8525, "diff": -200, "requested_budget": {"available": true, "amount": 16700, "scope": "total", "party_size": 4, "total": 16700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 532.81, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 16700, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 11700, "target_max_total": 18400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 11200, "reported_total_hotels": 5600, "diff": -5600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_per_person_cost_sum": 671, "expected_total_meals": 671, "reported_total_meals": 1110, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_per_person_cost_sum": 671, "expected_total_meals": 671, "reported_total_meals": 1110, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1950, "reported_total_hotels": 1950, "expected_total_attractions": 115, "reported_total_attractions": 180, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "TRUFFE BOULANGERIE B&C(全国首店)", "estimated_cost": 47, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-09", "type": "dinner", "name": "西工小街", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "lunch", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 5400, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 429, "expected_total_attractions": 1287, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 891, "expected_total_meals": 2673, "reported_total_meals": 1890, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 429, "expected_total_attractions": 1287, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 891, "expected_total_meals": 2673, "reported_total_meals": 1890, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "南楼煎饼(滨江道店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "南楼煎饼(滨江道店)"}]}, {"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "lunch", "name": "魏家凉皮(祈年大厦店)"}, {"date": "2026-07-07", "type": "lunch", "name": "魏家凉皮(体育中心店)"}, {"date": "2026-07-08", "type": "lunch", "name": "魏家凉皮(祈年大厦店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 10800, "reported_total_hotels": 5400, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 400, "meal_per_person_cost_sum": 1312, "expected_total_meals": 3936, "reported_total_meals": 1440, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-13", "day_index": 2, "name": "丽江古城"}, {"date": "2026-05-14", "day_index": 3, "name": "丽江古城"}]}, {"name_key": "束河古镇", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 1, "name": "束河古镇"}, {"date": "2026-05-13", "day_index": 2, "name": "束河古镇"}, {"date": "2026-05-14", "day_index": 3, "name": "束河古镇"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-13", "type": "lunch", "name": "云西小锅饭·云南民俗风味餐厅"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 480, "expected_total_attractions": 960, "reported_total_attractions": 960, "meal_per_person_cost_sum": 639, "expected_total_meals": 1278, "reported_total_meals": 1026, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "袁大头包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "breakfast", "name": "袁大头包子(解放公园店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "袁大头包子(解放公园店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "袁大头包子(解放公园店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "袁大头包子(解放公园店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "袁大头包子(解放公园店)"}]}, {"name_key": "矮子馅饼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "矮子馅饼(武汉总店)"}, {"date": "2026-05-11", "type": "lunch", "name": "矮子馅饼(大成路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "矮子馅饼(武汉总店)"}, {"date": "2026-05-13", "type": "lunch", "name": "矮子馅饼(武汉总店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-12", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-13", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2820, "total": 3010, "diff": -190, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 301.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 110, "meal_per_person_cost_sum": 319, "expected_total_meals": 638, "reported_total_meals": 510, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-11", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-12", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-13", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 1351, "expected_total_meals": 2702, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-21", "day_index": 0, "name": "杭州西湖风景名胜区"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州西湖风景名胜区"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 22500, "reported_total_hotels": 7500, "diff": -15000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10450, "total": 9500, "diff": 950, "requested_budget": {"available": true, "amount": 27000, "scope": "total", "party_size": 5, "total": 27000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 380.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 27000, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 18900, "target_max_total": 27000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 22500, "reported_total_hotels": 7500, "diff": -15000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
