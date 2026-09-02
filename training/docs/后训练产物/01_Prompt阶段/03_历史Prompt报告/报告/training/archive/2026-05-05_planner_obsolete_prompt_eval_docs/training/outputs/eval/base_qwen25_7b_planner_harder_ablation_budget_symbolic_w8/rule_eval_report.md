# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_budget_symbolic_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_budget_symbolic_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 293 | 293 | 100.00% |
| attraction_grounding_ok | 288 | 293 | 98.29% |
| budget_arithmetic_consistent | 274 | 293 | 93.52% |
| budget_consistent | 274 | 293 | 93.52% |
| budget_level_aligned | 285 | 293 | 97.27% |
| budget_preference_aligned | 285 | 293 | 97.27% |
| budget_within_user_budget | 293 | 293 | 100.00% |
| city_ok | 293 | 293 | 100.00% |
| date_range_ok | 293 | 293 | 100.00% |
| day_dates_ok | 293 | 293 | 100.00% |
| day_index_ok | 293 | 293 | 100.00% |
| days_len_ok | 293 | 293 | 100.00% |
| dpo_soft_pass | 19 | 293 | 6.48% |
| hard_pass | 253 | 293 | 86.35% |
| hotel_budget_covers_nights | 293 | 293 | 100.00% |
| hotel_distance_placeholder_ok | 293 | 293 | 100.00% |
| hotel_grounding_ok | 293 | 293 | 100.00% |
| invalid_hotel_name_ok | 293 | 293 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 21 | 293 | 7.17% |
| location_object_ok | 293 | 293 | 100.00% |
| meal_complete | 290 | 293 | 98.98% |
| meal_diversity_ok | 30 | 293 | 10.24% |
| meal_grounding_ok | 278 | 293 | 94.88% |
| meal_lunch_dinner_same_day_ok | 154 | 293 | 52.56% |
| meal_repeat_limit_ok | 50 | 293 | 17.06% |
| meal_specific_ok | 293 | 293 | 100.00% |
| meal_valid_semantics_ok | 280 | 293 | 95.56% |
| middle_hotel_ok | 292 | 293 | 99.66% |
| schema_ok | 293 | 300 | 97.67% |
| sft_hard_pass | 253 | 293 | 86.35% |
| weather_dates_ok | 293 | 293 | 100.00% |
| weather_match | 293 | 293 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.997,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3514,
    "p50": 0.25,
    "p90": 0.75
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.994,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 243,
  "meal_same_day_lunch_dinner_repeat": 139,
  "budget_arithmetic_inconsistent": 19,
  "meal_invalid_name": 13,
  "budget_preference_mismatch": 8,
  "schema": 6,
  "meal_grounding_miss": 2,
  "json_extract": 1,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-10", "lunch": "大队老渔村", "dinner": "大队老渔村"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 12, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-03", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}]}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆"}]}, {"name_key": "浆小白豆浆夜市", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "浆小白豆浆夜市"}, {"date": "2026-04-28", "type": "dinner", "name": "浆小白豆浆夜市"}, {"date": "2026-04-29", "type": "dinner", "name": "浆小白豆浆夜市"}, {"date": "2026-04-30", "type": "dinner", "name": "浆小白豆浆夜市"}]}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3220, "total": 2220, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 222.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-04->2026-04-08 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-05", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-04-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}, {"name_key": "金陵家宴·金陵春.南京菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-05", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-06", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-07", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-08", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}]}, {"name_key": "十朝春精菜馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "dinner", "name": "十朝春精菜馆"}, {"date": "2026-04-05", "type": "dinner", "name": "十朝春精菜馆"}, {"date": "2026-04-06", "type": "dinner", "name": "十朝春精菜馆"}, {"date": "2026-04-07", "type": "dinner", "name": "十朝春精菜馆"}, {"date": "2026-04-08", "type": "dinner", "name": "十朝春精菜馆"}]}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-06", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-03", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-04", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-05", "type": "dinner", "name": "民俗街夜市"}, {"date": "2026-04-06", "type": "dinner", "name": "民俗街夜市"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "食在香乡野本地菜", "dinner": "食在香乡野本地菜"}, {"date": "2026-04-07", "lunch": "食在香乡野本地菜", "dinner": "食在香乡野本地菜"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "碗碗都市香米粉店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-05", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-06", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}]}, {"name_key": "食在香乡野本地菜", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "食在香乡野本地菜"}, {"date": "2026-04-04", "type": "dinner", "name": "食在香乡野本地菜"}, {"date": "2026-04-05", "type": "lunch", "name": "食在香乡野本地菜"}, {"date": "2026-04-06", "type": "lunch", "name": "食在香乡野本地菜"}, {"date": "2026-04-07", "type": "lunch", "name": "食在香乡野本地菜"}, {"date": "2026-04-07", "type": "dinner", "name": "食在香乡野本地菜"}]}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南门涮肉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-08-03", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-08-04", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-08-05", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-08-06", "type": "dinner", "name": "南门涮肉(上海一店)"}]}, {"name_key": "浩海火烧云傣家菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-03", "type": "lunch", "name": "浩海火烧云傣家菜(新天地广场店)"}, {"date": "2026-08-04", "type": "lunch", "name": "浩海火烧云傣家菜(静安芮欧店)"}, {"date": "2026-08-05", "type": "lunch", "name": "浩海火烧云傣家菜(静安芮欧店)"}, {"date": "2026-08-06", "type": "lunch", "name": "浩海火烧云傣家菜(静安芮欧店)"}]}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}]}, {"name_key": "南堂馆川菜文化餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-09", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-10", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-11", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}]}]}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-05->2026-03-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "喜座·湖南美食村落(总店)", "dinner": "喜座·湖南美食村落(总店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "喜座·湖南美食村落", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-03-05", "type": "lunch", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-05", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-06", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-07", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-08", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}]}]}]`

### v3_harder_eval_000046
- request: 哈尔滨 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "遇见便当", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "遇见便当(群力店)"}, {"date": "2026-05-08", "type": "dinner", "name": "遇见便当(群力店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "遇见便当(群力店)"}, {"date": "2026-05-09", "type": "dinner", "name": "遇见便当(群力店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "遇见便当(群力店)"}, {"date": "2026-05-10", "type": "dinner", "name": "遇见便当(群力店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "遇见便当(群力店)"}, {"date": "2026-05-11", "type": "dinner", "name": "遇见便当(群力店)"}]}, {"name_key": "老厨家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "老厨家(中央大街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老厨家(中央大街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老厨家(中央大街店)"}, {"date": "2026-05-11", "type": "lunch", "name": "老厨家(中央大街店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4220, "total": 3220, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 268.33, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000040
- request: 南京 2026-07-03->2026-07-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-07", "type": "breakfast", "name": "麦当劳黄山路餐厅"}]}, {"name_key": "南京大牌档", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-04", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-05", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-07", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}]}, {"name_key": "李记清真馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "李记清真馆(打钉巷店)"}, {"date": "2026-07-04", "type": "dinner", "name": "李记清真馆(打钉巷店)"}, {"date": "2026-07-05", "type": "dinner", "name": "李记清真馆(打钉巷店)"}, {"date": "2026-07-06", "type": "dinner", "name": "李记清真馆(打钉巷店)"}, {"date": "2026-07-07", "type": "dinner", "name": "李记清真馆(打钉巷店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4375, "total": 3375, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 225.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000043
- request: 桂林 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-08", "type": "dinner", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-09", "type": "dinner", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-10", "type": "dinner", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-11", "type": "dinner", "name": "阿甘酒家(中山店)"}]}, {"name_key": "山味.本地农家菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "山味.本地农家菜"}, {"date": "2026-05-09", "type": "lunch", "name": "山味.本地农家菜"}, {"date": "2026-05-10", "type": "lunch", "name": "山味.本地农家菜"}, {"date": "2026-05-11", "type": "lunch", "name": "山味.本地农家菜"}]}]}]`

### v3_harder_eval_000049
- request: 珠海 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "云初甜品屋", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "云初甜品屋"}, {"date": "2026-05-09", "type": "breakfast", "name": "云初甜品屋"}, {"date": "2026-05-10", "type": "breakfast", "name": "云初甜品屋"}, {"date": "2026-05-11", "type": "breakfast", "name": "云初甜品屋"}]}, {"name_key": "粤禧顺·广东顺德菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "粤禧顺·广东顺德菜(情侣中路店)"}, {"date": "2026-05-09", "type": "lunch", "name": "粤禧顺·广东顺德菜(情侣中路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "粤禧顺·广东顺德菜(情侣中路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "粤禧顺·广东顺德菜(情侣中路店)"}]}, {"name_key": "渔记茶餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "渔记茶餐厅(横琴中央汇店)"}, {"date": "2026-05-09", "type": "dinner", "name": "渔记茶餐厅(横琴中央汇店)"}, {"date": "2026-05-10", "type": "dinner", "name": "渔记茶餐厅(横琴中央汇店)"}, {"date": "2026-05-11", "type": "dinner", "name": "渔记茶餐厅(横琴中央汇店)"}]}]}]`

### v3_harder_eval_000058
- request: 洛阳 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}]}]`

### v3_harder_eval_000050
- request: 深圳 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2026-04-05", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2026-04-06", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2026-04-07", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2026-04-08", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蘩楼", "count": 15, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-04", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-04", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-05", "type": "breakfast", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-05", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-05", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-06", "type": "breakfast", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-06", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-06", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "蘩楼(华强北总店)"}]}]}]`

### v3_harder_eval_000055
- request: 长沙 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-02", "lunch": "四方坪夜市", "dinner": "四方坪夜市"}, {"date": "2026-08-03", "lunch": "四方坪夜市", "dinner": "四方坪夜市"}, {"date": "2026-08-04", "lunch": "四方坪夜市", "dinner": "四方坪夜市"}, {"date": "2026-08-05", "lunch": "四方坪夜市", "dinner": "四方坪夜市"}, {"date": "2026-08-06", "lunch": "四方坪夜市", "dinner": "四方坪夜市"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四方坪夜市", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "lunch", "name": "四方坪夜市"}, {"date": "2026-08-02", "type": "dinner", "name": "四方坪夜市"}, {"date": "2026-08-03", "type": "lunch", "name": "四方坪夜市"}, {"date": "2026-08-03", "type": "dinner", "name": "四方坪夜市"}, {"date": "2026-08-04", "type": "lunch", "name": "四方坪夜市"}, {"date": "2026-08-04", "type": "dinner", "name": "四方坪夜市"}, {"date": "2026-08-05", "type": "lunch", "name": "四方坪夜市"}, {"date": "2026-08-05", "type": "dinner", "name": "四方坪夜市"}, {"date": "2026-08-06", "type": "lunch", "name": "四方坪夜市"}, {"date": "2026-08-06", "type": "dinner", "name": "四方坪夜市"}]}]}]`
