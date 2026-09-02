# Rule Eval Report: base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_diversity_budget_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 296 | 296 | 100.00% |
| attraction_grounding_ok | 294 | 296 | 99.32% |
| budget_arithmetic_consistent | 262 | 296 | 88.51% |
| budget_consistent | 262 | 296 | 88.51% |
| budget_level_aligned | 289 | 296 | 97.64% |
| budget_preference_aligned | 289 | 296 | 97.64% |
| budget_within_user_budget | 296 | 296 | 100.00% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 115 | 296 | 38.85% |
| hard_pass | 223 | 296 | 75.34% |
| hotel_budget_covers_nights | 296 | 296 | 100.00% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 296 | 296 | 100.00% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 120 | 296 | 40.54% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_complete | 294 | 296 | 99.32% |
| meal_diversity_ok | 156 | 296 | 52.70% |
| meal_grounding_ok | 258 | 296 | 87.16% |
| meal_lunch_dinner_same_day_ok | 212 | 296 | 71.62% |
| meal_repeat_limit_ok | 199 | 296 | 67.23% |
| meal_specific_ok | 296 | 296 | 100.00% |
| meal_valid_semantics_ok | 262 | 296 | 88.51% |
| middle_hotel_ok | 296 | 296 | 100.00% |
| schema_ok | 296 | 300 | 98.67% |
| sft_hard_pass | 223 | 296 | 75.34% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 295 | 296 | 99.66% |

## Numeric Metrics

```json
{
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
    "avg": 0.7257,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9862,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9862,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9881,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 97,
  "meal_same_day_lunch_dinner_repeat": 84,
  "budget_arithmetic_inconsistent": 34,
  "meal_invalid_name": 34,
  "budget_preference_mismatch": 7,
  "meal_grounding_miss": 4,
  "schema": 4,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(西街店)", "dinner": "椿记烧鹅(南溪店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(南溪店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4410, "total": 6650, "diff": -2240, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 831.25, "budget_level": "premium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "大鸽饭", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "大鸽饭(体育西店)"}, {"date": "2026-07-04", "type": "dinner", "name": "大鸽饭(棠下店)"}, {"date": "2026-07-05", "type": "lunch", "name": "大鸽饭(体育西店)"}, {"date": "2026-07-06", "type": "lunch", "name": "大鸽饭(棠下店)"}, {"date": "2026-07-07", "type": "lunch", "name": "大鸽饭(体育西店)"}]}, {"name_key": "松苑·浓汤广府菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-04", "type": "lunch", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-05", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-06", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-07", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 400.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2840, "total": 2840, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 355.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "清真刚刚烤肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-22", "type": "dinner", "name": "清真刚刚烤肉(小南门店)"}, {"date": "2026-04-23", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-24", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 200.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "哑巴生煎", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 200.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-04", "type": "dinner", "name": "民俗街夜市"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-07", "lunch": "麦当劳(桂林临桂万达餐厅)", "dinner": "麦当劳(桂林临桂万达餐厅)"}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-21", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老姑东北人", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-19", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-04", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}, {"date": "2026-08-06", "lunch": "海福多共富海鲜面馆", "dinner": "海福多共富海鲜面馆"}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(深圳首店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-03-07", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-10", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-11", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "大毛.淮扬菜", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-10", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-10", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-11", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-11", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}]}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-05", "lunch": "刘聋子牛肉粉馆(光谷新竹路店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "lunch", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四方坪三十栋饭店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-04", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-05", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-06", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}]}]}]`
