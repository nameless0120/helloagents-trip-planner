# Rule Eval Report: base_qwen25_7b_v3_ctx_hard_compact_baseline_smoke20

- records: 20
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_baseline_smoke20/generations.jsonl`
- records_path: `training/data/v3/context_ablation/hard_baseline_compact_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 19 | 19 | 100.00% |
| attraction_budget_consistent | 0 | 19 | 0.00% |
| attraction_budget_party_relation_ok | 5 | 19 | 26.32% |
| attraction_count_ok | 19 | 19 | 100.00% |
| attraction_diversity_ok | 19 | 19 | 100.00% |
| attraction_grounding_ok | 19 | 19 | 100.00% |
| attraction_repeat_limit_ok | 19 | 19 | 100.00% |
| budget_arithmetic_consistent | 12 | 19 | 63.16% |
| budget_consistent | 12 | 19 | 63.16% |
| budget_level_aligned | 7 | 19 | 36.84% |
| budget_preference_aligned | 7 | 19 | 36.84% |
| budget_relationship_ok | 2 | 19 | 10.53% |
| budget_user_constraint_ok | 14 | 19 | 73.68% |
| budget_within_user_budget | 18 | 19 | 94.74% |
| city_ok | 19 | 19 | 100.00% |
| date_range_ok | 19 | 19 | 100.00% |
| day_dates_ok | 19 | 19 | 100.00% |
| day_index_ok | 19 | 19 | 100.00% |
| days_len_ok | 19 | 19 | 100.00% |
| dpo_soft_pass | 0 | 19 | 0.00% |
| hard_pass | 0 | 19 | 0.00% |
| hotel_budget_covers_nights | 14 | 19 | 73.68% |
| hotel_budget_relation_ok | 15 | 19 | 78.95% |
| hotel_distance_placeholder_ok | 19 | 19 | 100.00% |
| hotel_grounding_ok | 19 | 19 | 100.00% |
| invalid_hotel_name_ok | 19 | 19 | 100.00% |
| json_extract_ok | 20 | 20 | 100.00% |
| legacy_hard_pass | 0 | 19 | 0.00% |
| location_object_ok | 19 | 19 | 100.00% |
| meal_budget_consistent | 1 | 19 | 5.26% |
| meal_complete | 19 | 19 | 100.00% |
| meal_cost_scale_ok | 10 | 19 | 52.63% |
| meal_diversity_ok | 0 | 19 | 0.00% |
| meal_grounding_ok | 18 | 19 | 94.74% |
| meal_lunch_dinner_same_day_ok | 10 | 19 | 52.63% |
| meal_repeat_limit_ok | 3 | 19 | 15.79% |
| meal_specific_ok | 19 | 19 | 100.00% |
| meal_valid_semantics_ok | 19 | 19 | 100.00% |
| middle_hotel_ok | 19 | 19 | 100.00% |
| schema_ok | 19 | 20 | 95.00% |
| sft_budget_semantic_hard_pass | 1 | 19 | 5.26% |
| sft_hard_pass | 0 | 19 | 0.00% |
| transportation_budget_nonnegative | 19 | 19 | 100.00% |
| weather_dates_ok | 19 | 19 | 100.00% |
| weather_match | 19 | 19 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 1.0,
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
    "avg": 0.314,
    "p50": 0.25,
    "p90": 0.5
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9956,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9956,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "attraction_budget_inconsistent": 19,
  "meal_budget_inconsistent": 18,
  "budget_relationship_mismatch": 17,
  "meal_repeat_too_many": 16,
  "budget_preference_mismatch": 12,
  "meal_same_day_lunch_dinner_repeat": 9,
  "meal_cost_scale_too_low": 9,
  "budget_arithmetic_inconsistent": 7,
  "hotel_budget_underestimated": 5,
  "budget_hard_constraint_exceeded": 5,
  "schema": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(中山店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3750, "total": 3850, "diff": -100, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 154.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "秦大妈老字号 (南庄坪店)", "dinner": "秦大妈老字号 (南庄坪店)"}, {"date": "2026-05-10", "lunch": "大队老渔村", "dinner": "大队老渔村"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "expected_total_meals": 516, "reported_total_meals": 450, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮(杭州西溪印象城店)"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮(杭州西溪印象城店)"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮(杭州西溪印象城店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "魏家凉皮(杭州西溪印象城店)"}]}, {"name_key": "郑阿公顺德鸡煲饭双皮奶", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-28", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-04-29", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-04-30", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-05-01", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 30, "expected_total_attractions": 120, "reported_total_attractions": 300, "expected_total_meals": 2256, "reported_total_meals": 1008, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 30, "expected_total_attractions": 120, "reported_total_attractions": 300, "expected_total_meals": 2256, "reported_total_meals": 1008, "reported_total_transportation": 200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-04", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-05", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-06", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-07", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}]}, {"name_key": "银灯食府", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-04", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-05", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-06", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-07", "type": "dinner", "name": "银灯食府(文化公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 321, "expected_total_attractions": 321, "reported_total_attractions": 520, "expected_total_meals": 1050, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 321, "expected_total_attractions": 321, "reported_total_attractions": 520, "expected_total_meals": 1050, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}, {"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-09", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-10", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 2250, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 750, "expected_total_meals": 1368, "reported_total_meals": 594, "reported_total_transportation": 600}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3220, "total": 2220, "diff": 1000, "requested_budget": {"available": true, "amount": 7000, "scope": "total", "party_size": 2, "total": 7000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 222.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7000, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4600, "target_max_total": 7400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 120, "expected_total_meals": 620, "reported_total_meals": 432, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 120, "expected_total_meals": 620, "reported_total_meals": 432, "reported_total_transportation": 200}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-27", "type": "lunch", "name": "苏州乐园森林世界内的餐厅"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-30", "lunch": "平阊园苏式面馆", "dinner": "平阊园苏式面馆"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 255, "expected_total_meals": 2146, "reported_total_meals": 1416, "reported_total_transportation": 800}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "某有茶·黑糖珍珠奶茶", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(仓山万达金街店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 1240, "expected_total_meals": 1608, "reported_total_meals": 1440, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 1240, "expected_total_meals": 1608, "reported_total_meals": 1440, "reported_total_transportation": 800}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-20", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-21", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-22", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-23", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-24", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "国人川菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-20", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "dinner", "name": "国人川菜(李家村店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 254, "expected_total_attractions": 1270, "reported_total_attractions": 1200, "expected_total_meals": 4000, "reported_total_meals": 1020, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-05", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-03", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-05", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-05", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "川味麻辣香锅.万州烤鱼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)"}, {"date": "2026-05-07", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)"}, {"date": "2026-05-08", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)"}, {"date": "2026-05-09", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)"}, {"date": "2026-05-10", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 210, "expected_total_meals": 730, "reported_total_meals": 678, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 210, "expected_total_meals": 730, "reported_total_meals": 678, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "小欢喜苏帮菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "小欢喜苏帮菜"}, {"date": "2026-06-04", "type": "dinner", "name": "小欢喜苏帮菜"}, {"date": "2026-06-05", "type": "dinner", "name": "小欢喜苏帮菜"}, {"date": "2026-06-06", "type": "dinner", "name": "小欢喜苏帮菜"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6650, "total": 6600, "diff": 50, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 550.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 3750, "reported_total_hotels": 3750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 149, "expected_total_attractions": 447, "reported_total_attractions": 1050, "expected_total_meals": 2100, "reported_total_meals": 1050, "reported_total_transportation": 800}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 800, "diff": 100, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 1120, "expected_total_meals": 2156, "reported_total_meals": 1368, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-03", "type": "dinner", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "dinner", "name": "南楼煎饼"}, {"date": "2026-07-05", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-05", "type": "dinner", "name": "南楼煎饼"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4926, "total": 5506, "diff": -580, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 611.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 240, "expected_total_meals": 762, "reported_total_meals": 486, "reported_total_transportation": 600}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "哑巴生煎", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}]}, {"name_key": "烟雨人家特色农家菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-08", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-09", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-10", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4274, "total": 3274, "diff": 1000, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 2, "total": 6700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 327.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4400, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 590, "reported_total_attractions": 1050, "expected_total_meals": 3248, "reported_total_meals": 1424, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 12, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4604, "total": 4404, "diff": 200, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 550.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-19", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-20", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-21", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-22", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}]}, {"name_key": "老姑东北人", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4920, "total": 5000, "diff": -80, "requested_budget": {"available": true, "amount": 16100, "scope": "total", "party_size": 5, "total": 16100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 200.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 16100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 10500, "target_max_total": 16100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 30, "expected_total_attractions": 150, "reported_total_attractions": 120, "expected_total_meals": 3025, "reported_total_meals": 1800, "reported_total_transportation": 1000}}]`
