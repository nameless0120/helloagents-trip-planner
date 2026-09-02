# Rule Eval Report: base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16_judge100

- records: 100
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16_judge100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_diversity_budget_symbolic_no_route/judge_sample100/records_sample100_seed20260504.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 98 | 98 | 100.00% |
| budget_arithmetic_consistent | 86 | 98 | 87.76% |
| budget_consistent | 86 | 98 | 87.76% |
| budget_level_aligned | 96 | 98 | 97.96% |
| budget_preference_aligned | 96 | 98 | 97.96% |
| budget_within_user_budget | 98 | 98 | 100.00% |
| city_ok | 98 | 98 | 100.00% |
| date_range_ok | 98 | 98 | 100.00% |
| day_dates_ok | 98 | 98 | 100.00% |
| day_index_ok | 98 | 98 | 100.00% |
| days_len_ok | 98 | 98 | 100.00% |
| hard_pass | 33 | 98 | 33.67% |
| hotel_budget_covers_nights | 98 | 98 | 100.00% |
| hotel_distance_placeholder_ok | 98 | 98 | 100.00% |
| invalid_hotel_name_ok | 98 | 98 | 100.00% |
| json_extract_ok | 100 | 100 | 100.00% |
| location_object_ok | 98 | 98 | 100.00% |
| meal_complete | 98 | 98 | 100.00% |
| meal_diversity_ok | 47 | 98 | 47.96% |
| meal_grounding_ok | 83 | 98 | 84.69% |
| meal_lunch_dinner_same_day_ok | 67 | 98 | 68.37% |
| meal_repeat_limit_ok | 64 | 98 | 65.31% |
| meal_specific_ok | 98 | 98 | 100.00% |
| meal_valid_semantics_ok | 84 | 98 | 85.71% |
| middle_hotel_ok | 98 | 98 | 100.00% |
| schema_ok | 98 | 100 | 98.00% |
| weather_dates_ok | 98 | 98 | 100.00% |
| weather_match | 98 | 98 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.705,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9871,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9871,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9891,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 34,
  "meal_same_day_lunch_dinner_repeat": 31,
  "meal_invalid_name": 14,
  "budget_arithmetic_inconsistent": 12,
  "budget_preference_mismatch": 2,
  "schema": 2,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "清真刚刚烤肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-22", "type": "dinner", "name": "清真刚刚烤肉(小南门店)"}, {"date": "2026-04-23", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-24", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 200.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-04", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}, {"date": "2026-08-06", "lunch": "海福多共富海鲜面馆", "dinner": "海福多共富海鲜面馆"}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000033
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-09", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "吴记小园楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-09", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-10", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-11", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-12", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}]}]}]`

### v3_harder_eval_000035
- request: 深圳 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-02", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(罗湖东门町店)"}]}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四方坪三十栋饭店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-04", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-05", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-06", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}]}]}]`

### v3_harder_eval_000039
- request: 深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蘩楼", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-11-05", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-06", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-07", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-08", "type": "lunch", "name": "蘩楼(华强北总店)"}]}, {"name_key": "南门涮肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-11-05", "type": "dinner", "name": "南门涮肉(深圳首店)"}, {"date": "2025-11-06", "type": "dinner", "name": "南门涮肉(深圳首店)"}, {"date": "2025-11-07", "type": "dinner", "name": "南门涮肉(深圳首店)"}, {"date": "2025-11-08", "type": "dinner", "name": "南门涮肉(深圳首店)"}]}]}]`

### v3_harder_eval_000045
- request: 济南 2026-04-04->2026-04-08 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "箪食巷私房菜(奥体店)", "dinner": "箪食巷私房菜(奥体店)"}, {"date": "2026-04-05", "lunch": "向民炒鸡老店", "dinner": "向民炒鸡老店"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "箪食巷私房菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "箪食巷私房菜(奥体店)"}, {"date": "2026-04-04", "type": "dinner", "name": "箪食巷私房菜(奥体店)"}, {"date": "2026-04-06", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}, {"date": "2026-04-07", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}, {"date": "2026-04-08", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}]}]}]`

### v3_harder_eval_000046
- request: 哈尔滨 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "福成厚江鱼壹号", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "福成厚江鱼壹号(群力店)"}, {"date": "2026-05-09", "type": "lunch", "name": "福成厚江鱼壹号(松北旗舰店)"}, {"date": "2026-05-10", "type": "lunch", "name": "福成厚江鱼壹号(松北旗舰店)"}, {"date": "2026-05-11", "type": "lunch", "name": "福成厚江鱼壹号(松北旗舰店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4190, "total": 3190, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 265.83, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000053
- request: 青岛 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-07", "lunch": "前海沿·青岛菜(五四广场永旺店)", "dinner": "前海沿·青岛菜(中山路天主教堂店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "前海沿·青岛菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "前海沿·青岛菜(五四广场永旺店)"}, {"date": "2025-05-07", "type": "lunch", "name": "前海沿·青岛菜(五四广场永旺店)"}, {"date": "2025-05-07", "type": "dinner", "name": "前海沿·青岛菜(中山路天主教堂店)"}, {"date": "2025-05-08", "type": "lunch", "name": "前海沿·青岛菜(中山路天主教堂店)"}]}]}]`

### v3_harder_eval_000064
- request: 杭州 2025-08-07->2025-08-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-08-09", "type": "dinner", "name": "杭州牵手驿家酒店", "reason": "hotel_or_lodging_name"}]}]`

### v3_harder_eval_000072
- request: 哈尔滨 2026-05-05->2026-05-08 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "遇见便当(群力店)", "dinner": "遇见便当(群力店)"}, {"date": "2026-05-08", "lunch": "福成厚江鱼壹号(群力店)", "dinner": "福成厚江鱼壹号(群力店)"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2963, "total": 2963, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 370.38, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000080
- request: 张家界 2026-05-05->2026-05-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-05", "lunch": "索溪山寨·湘西民间土菜(溪布街店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}]}]`

### v3_harder_eval_000081
- request: 青岛 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "前海沿·青岛菜(五四广场永旺店)", "dinner": "前海沿·青岛菜(中山路天主教堂店)"}]}]`

### v3_harder_eval_000083
- request: 成都 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-08-06", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000085
- request: 北京 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "浩海火烧云傣家菜(京广店)", "dinner": "浩海火烧云傣家菜(东安市场店)"}, {"date": "2026-05-10", "lunch": "北京凯瑞御仙都皇家菜博物馆", "dinner": "北京凯瑞御仙都皇家菜博物馆"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 600.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1400, "reported_total_hotels": 1400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000092
- request: 大理 2026-08-02->2026-08-05 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南诏村·现炒云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-08-03", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-08-04", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-08-05", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-08-03", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-08-04", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-08-05", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}]`
