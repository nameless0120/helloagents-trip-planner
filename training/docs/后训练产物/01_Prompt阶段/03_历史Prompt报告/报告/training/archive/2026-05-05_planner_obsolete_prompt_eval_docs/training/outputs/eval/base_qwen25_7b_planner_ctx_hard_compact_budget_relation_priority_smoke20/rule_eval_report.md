# Rule Eval Report: base_qwen25_7b_v3_ctx_hard_compact_budget_relation_priority_smoke20

- records: 20
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_budget_relation_priority_smoke20/generations.jsonl`
- records_path: `training/data/v3/context_ablation/hard_compact_prompt_budget_relation_priority_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 19 | 20 | 95.00% |
| attraction_budget_consistent | 2 | 20 | 10.00% |
| attraction_budget_party_relation_ok | 6 | 20 | 30.00% |
| attraction_count_ok | 20 | 20 | 100.00% |
| attraction_diversity_ok | 18 | 20 | 90.00% |
| attraction_grounding_ok | 20 | 20 | 100.00% |
| attraction_repeat_limit_ok | 18 | 20 | 90.00% |
| budget_arithmetic_consistent | 11 | 20 | 55.00% |
| budget_consistent | 11 | 20 | 55.00% |
| budget_level_aligned | 8 | 20 | 40.00% |
| budget_preference_aligned | 8 | 20 | 40.00% |
| budget_relationship_ok | 1 | 20 | 5.00% |
| budget_user_constraint_ok | 16 | 20 | 80.00% |
| budget_within_user_budget | 19 | 20 | 95.00% |
| city_ok | 20 | 20 | 100.00% |
| date_range_ok | 20 | 20 | 100.00% |
| day_dates_ok | 20 | 20 | 100.00% |
| day_index_ok | 20 | 20 | 100.00% |
| days_len_ok | 20 | 20 | 100.00% |
| dpo_soft_pass | 0 | 20 | 0.00% |
| hard_pass | 0 | 20 | 0.00% |
| hotel_budget_covers_nights | 16 | 20 | 80.00% |
| hotel_budget_relation_ok | 17 | 20 | 85.00% |
| hotel_distance_placeholder_ok | 20 | 20 | 100.00% |
| hotel_grounding_ok | 20 | 20 | 100.00% |
| invalid_hotel_name_ok | 20 | 20 | 100.00% |
| json_extract_ok | 20 | 20 | 100.00% |
| legacy_hard_pass | 1 | 20 | 5.00% |
| location_object_ok | 20 | 20 | 100.00% |
| meal_budget_consistent | 0 | 20 | 0.00% |
| meal_complete | 20 | 20 | 100.00% |
| meal_cost_scale_ok | 6 | 20 | 30.00% |
| meal_diversity_ok | 5 | 20 | 25.00% |
| meal_grounding_ok | 19 | 20 | 95.00% |
| meal_lunch_dinner_same_day_ok | 13 | 20 | 65.00% |
| meal_repeat_limit_ok | 7 | 20 | 35.00% |
| meal_specific_ok | 20 | 20 | 100.00% |
| meal_valid_semantics_ok | 19 | 20 | 95.00% |
| middle_hotel_ok | 20 | 20 | 100.00% |
| schema_ok | 20 | 20 | 100.00% |
| sft_budget_semantic_hard_pass | 1 | 20 | 5.00% |
| sft_hard_pass | 0 | 20 | 0.00% |
| transportation_budget_nonnegative | 20 | 20 | 100.00% |
| weather_dates_ok | 20 | 20 | 100.00% |
| weather_match | 20 | 20 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9713,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.486,
    "p50": 0.5,
    "p90": 0.875
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 20,
  "budget_relationship_mismatch": 19,
  "attraction_budget_inconsistent": 18,
  "meal_cost_scale_too_low": 14,
  "meal_repeat_too_many": 13,
  "budget_preference_mismatch": 12,
  "budget_arithmetic_inconsistent": 9,
  "meal_same_day_lunch_dinner_repeat": 7,
  "hotel_budget_underestimated": 4,
  "budget_hard_constraint_exceeded": 4,
  "attraction_repeat_too_many": 2,
  "meal_invalid_name": 1,
  "accommodation_type_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-04", "type": "dinner", "name": "桂林山水甲天下", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5240, "total": 5040, "diff": 200, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 2, "total": 9100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 630.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6400, "target_max_total": 10200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1110, "expected_total_meals": 1218, "reported_total_meals": 1080, "reported_total_transportation": 800}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 1200, "expected_total_meals": 2825, "reported_total_meals": 1500, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-10", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 420, "expected_total_meals": 1616, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 420, "expected_total_meals": 1616, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 440, "reported_total_attractions": 420, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-04-28", "type": "lunch", "name": "魏家凉皮(杭州西溪印象城店)", "estimated_cost": 40, "min_expected_cost": 100}, {"date": "2026-05-01", "type": "lunch", "name": "泮芳春煎饺·米其林餐厅(中山南路店)", "estimated_cost": 60, "min_expected_cost": 100}]}}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-03", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "dinner", "name": "麦当劳黄山路餐厅"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-04", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-05", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(1912总统府店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2675, "total": 2635, "diff": 40, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 219.58, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1650, "reported_total_hotels": 1650, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2000, "diff": 1000, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 400.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 555, "expected_total_attractions": 555, "reported_total_attractions": 1120, "expected_total_meals": 1093, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 555, "expected_total_attractions": 555, "reported_total_attractions": 1120, "expected_total_meals": 1093, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 2250, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 750, "expected_total_meals": 1365, "reported_total_meals": 630, "reported_total_transportation": 600}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "成都大熊猫繁育研究基地", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-09", "day_index": 1, "name": "成都大熊猫繁育研究基地"}, {"date": "2026-05-12", "day_index": 4, "name": "成都大熊猫繁育研究基地"}]}, {"name_key": "天府艺术公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 2, "name": "天府艺术公园"}, {"date": "2026-05-12", "day_index": 4, "name": "天府艺术公园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天廊店)"}]}, {"name_key": "马旺子·川小馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "马旺子·川小馆(成都太古里店)"}, {"date": "2026-05-09", "type": "dinner", "name": "马旺子·川小馆(成都太古里店)"}, {"date": "2026-05-10", "type": "dinner", "name": "马旺子·川小馆(成都太古里店)"}, {"date": "2026-05-11", "type": "dinner", "name": "马旺子·川小馆(成都太古里店)"}, {"date": "2026-05-12", "type": "dinner", "name": "马旺子·川小馆(成都太古里店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3140, "total": 2140, "diff": 1000, "requested_budget": {"available": true, "amount": 7000, "scope": "total", "party_size": 2, "total": 7000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 214.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7000, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4600, "target_max_total": 7400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安城墙", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-04", "day_index": 0, "name": "西安城墙"}, {"date": "2025-05-08", "day_index": 4, "name": "西安城墙"}]}, {"name_key": "大雁塔", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-05", "day_index": 1, "name": "大雁塔"}, {"date": "2025-05-07", "day_index": 3, "name": "大雁塔"}]}, {"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-05", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2025-05-07", "day_index": 3, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3296, "total": 3376, "diff": -80, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 337.6, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3700, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-28", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-29", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-30", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 1050, "expected_total_meals": 4784, "reported_total_meals": 2832, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 1050, "expected_total_meals": 4784, "reported_total_meals": 2832, "reported_total_transportation": 800}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4902, "total": 5902, "diff": -1000, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 737.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 0, "expected_total_meals": 1658, "reported_total_meals": 1402, "reported_total_transportation": 800}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-20", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-21", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-22", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-23", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-24", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "国人川菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-20", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "dinner", "name": "国人川菜(李家村店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5020, "total": 4020, "diff": 1000, "requested_budget": {"available": true, "amount": 11100, "scope": "total", "party_size": 5, "total": 11100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 160.8, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 11100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 7200, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 143, "expected_total_attractions": 286, "reported_total_attractions": 140, "expected_total_meals": 878, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2210, "total": 2010, "diff": 200, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 670.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "expected_total_meals": 721, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 180, "expected_total_meals": 721, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 960, "expected_total_meals": 2156, "reported_total_meals": 1200, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 170, "expected_total_attractions": 510, "reported_total_attractions": 1050, "expected_total_meals": 2184, "reported_total_meals": 1464, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 170, "expected_total_attractions": 510, "reported_total_attractions": 1050, "expected_total_meals": 2184, "reported_total_meals": 1464, "reported_total_transportation": 400}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-05", "lunch": "天津卫码头(水上公园店)", "dinner": "天津卫码头(水上公园店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 1200, "expected_total_meals": 1041, "reported_total_meals": 660, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 1200, "expected_total_meals": 1041, "reported_total_meals": 660, "reported_total_transportation": 300}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-07", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "哑巴生煎", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 360, "expected_total_meals": 1826, "reported_total_meals": 1124, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 360, "expected_total_meals": 1826, "reported_total_meals": 1124, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}, {"name_key": "隔壁老王·家常云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-09", "type": "lunch", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-10", "type": "lunch", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-11", "type": "lunch", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 960, "expected_total_meals": 1544, "reported_total_meals": 486, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 960, "expected_total_meals": 1544, "reported_total_meals": 486, "reported_total_transportation": 400}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-20", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老姑东北人", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5010, "total": 5090, "diff": -80, "requested_budget": {"available": true, "amount": 16100, "scope": "total", "party_size": 5, "total": 16100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 203.6, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 16100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 10500, "target_max_total": 16100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
