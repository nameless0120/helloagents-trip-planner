# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_budget_hard_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_budget_hard_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_hard_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 293 | 294 | 99.66% |
| attraction_grounding_ok | 285 | 294 | 96.94% |
| budget_arithmetic_consistent | 267 | 294 | 90.82% |
| budget_consistent | 267 | 294 | 90.82% |
| budget_level_aligned | 286 | 294 | 97.28% |
| budget_preference_aligned | 286 | 294 | 97.28% |
| budget_within_user_budget | 294 | 294 | 100.00% |
| city_ok | 294 | 294 | 100.00% |
| date_range_ok | 294 | 294 | 100.00% |
| day_dates_ok | 294 | 294 | 100.00% |
| day_index_ok | 294 | 294 | 100.00% |
| days_len_ok | 294 | 294 | 100.00% |
| dpo_soft_pass | 24 | 294 | 8.16% |
| hard_pass | 241 | 294 | 81.97% |
| hotel_budget_covers_nights | 294 | 294 | 100.00% |
| hotel_distance_placeholder_ok | 294 | 294 | 100.00% |
| hotel_grounding_ok | 294 | 294 | 100.00% |
| invalid_hotel_name_ok | 294 | 294 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 26 | 294 | 8.84% |
| location_object_ok | 294 | 294 | 100.00% |
| meal_complete | 283 | 294 | 96.26% |
| meal_diversity_ok | 33 | 294 | 11.22% |
| meal_grounding_ok | 285 | 294 | 96.94% |
| meal_lunch_dinner_same_day_ok | 140 | 294 | 47.62% |
| meal_repeat_limit_ok | 66 | 294 | 22.45% |
| meal_specific_ok | 294 | 294 | 100.00% |
| meal_valid_semantics_ok | 287 | 294 | 97.62% |
| middle_hotel_ok | 293 | 294 | 99.66% |
| schema_ok | 294 | 300 | 98.00% |
| sft_hard_pass | 241 | 294 | 81.97% |
| weather_dates_ok | 294 | 294 | 100.00% |
| weather_match | 293 | 294 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9952,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3707,
    "p50": 0.3,
    "p90": 0.75
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9973,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 228,
  "meal_same_day_lunch_dinner_repeat": 154,
  "budget_arithmetic_inconsistent": 27,
  "budget_preference_mismatch": 8,
  "meal_invalid_name": 7,
  "schema": 6,
  "meal_grounding_miss": 2,
  "weather_mismatch": 1,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-10", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}, {"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-09", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-10", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-03", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "dinner", "name": "麦当劳黄山路餐厅"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-04", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-05", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}]}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四方小炒·云南菜小当家", "count": 11, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "breakfast", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "breakfast", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "breakfast", "name": "四方小炒·云南菜小当家(联盟店)"}]}, {"name_key": "从水炉·普洱生态菜馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-05", "type": "lunch", "name": "从水炉·普洱生态菜馆(南强店)"}, {"date": "2026-04-06", "type": "lunch", "name": "从水炉·普洱生态菜馆(南强店)"}, {"date": "2026-04-07", "type": "lunch", "name": "从水炉·普洱生态菜馆(南强店)"}, {"date": "2026-04-08", "type": "lunch", "name": "从水炉·普洱生态菜馆(南强店)"}]}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(西街店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(南溪店)", "dinner": "椿记烧鹅(南溪店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(南溪店)"}]}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天廊店)"}]}, {"name_key": "翠孃孃老火锅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "翠孃孃老火锅(春熙路老店)"}, {"date": "2026-05-10", "type": "dinner", "name": "翠孃孃老火锅(春熙路老店)"}, {"date": "2026-05-11", "type": "dinner", "name": "翠孃孃老火锅(春熙路老店)"}, {"date": "2026-05-12", "type": "dinner", "name": "翠孃孃老火锅(春熙路老店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3120, "total": 2060, "diff": 1060, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 206.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-04", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-05", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-06", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-07", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}]}, {"name_key": "滋粥楼·顺德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-04", "type": "dinner", "name": "滋粥楼·顺德菜(番禺广场总店)"}, {"date": "2026-07-05", "type": "dinner", "name": "滋粥楼·顺德菜(番禺广场总店)"}, {"date": "2026-07-06", "type": "dinner", "name": "滋粥楼·顺德菜(番禺广场总店)"}, {"date": "2026-07-07", "type": "dinner", "name": "滋粥楼·顺德菜(番禺广场总店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 400.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-28", "lunch": "老横泾面馆", "dinner": "老横泾面馆"}, {"date": "2026-04-29", "lunch": "老横泾面馆", "dinner": "老横泾面馆"}, {"date": "2026-04-30", "lunch": "老横泾面馆", "dinner": "老横泾面馆"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "老横泾面馆", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "dinner", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "dinner", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "dinner", "name": "老横泾面馆"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-05", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-03", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-05", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-05", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-06", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-20", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-21", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-22", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-23", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-24", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "国人川菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-20", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "dinner", "name": "国人川菜(李家村店)"}]}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-03", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-05", "lunch": "光头东烙馍村·水席洛阳菜(博物馆店)", "dinner": "光头东烙馍村·水席洛阳菜(博物馆店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "光头东烙馍村·水席洛阳菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-05", "type": "lunch", "name": "光头东烙馍村·水席洛阳菜(博物馆店)"}, {"date": "2025-05-05", "type": "dinner", "name": "光头东烙馍村·水席洛阳菜(博物馆店)"}, {"date": "2025-05-06", "type": "lunch", "name": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "type": "lunch", "name": "光头东烙馍村·水席洛阳菜(博物馆店)"}]}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2840, "total": 2840, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 355.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "南楼煎饼(南楼总店)", "dinner": "南楼煎饼(南楼总店)"}, {"date": "2026-07-04", "lunch": "天津卫码头(水上公园店)", "dinner": "天津卫码头(水上公园店)"}, {"date": "2026-07-05", "lunch": "魏斯理汉堡(天津乐宾百货店)", "dinner": "魏斯理汉堡(天津乐宾百货店)"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000021
- request: 上海 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "莱莱小笼", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-19", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-20", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-21", "type": "breakfast", "name": "莱莱小笼"}]}, {"name_key": "紫阳村地道家常菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-19", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-20", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-21", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}]}, {"name_key": "南门涮肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-19", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-20", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-21", "type": "dinner", "name": "南门涮肉(上海一店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "李百蟹·蟹黄面·平江河畔", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "李百蟹·蟹黄面·平江河畔(平江路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "李百蟹·蟹黄面·平江河畔(平江路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "李百蟹·蟹黄面·平江河畔(平江路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "李百蟹·蟹黄面·平江河畔(平江路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "李百蟹·蟹黄面·平江河畔(平江路店)"}]}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "穆得老周家牛肉烧饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-08", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-09", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}]}, {"name_key": "老济南济南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "老济南济南菜(大明湖店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老济南济南菜(大明湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老济南济南菜(大明湖店)"}]}, {"name_key": "鑫龙火锅城", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}]}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-22", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}]}, {"name_key": "入江南·金奖杭帮菜·浙江菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-19", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-20", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-21", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-22", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}]}, {"name_key": "老姑东北人", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-19", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}]`
