# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_budget_symbolic_meal_semantic_w16

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_budget_symbolic_meal_semantic_w16/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_symbolic_meal_semantic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_grounding_ok | 296 | 299 | 99.00% |
| budget_arithmetic_consistent | 275 | 299 | 91.97% |
| budget_consistent | 275 | 299 | 91.97% |
| budget_level_aligned | 291 | 299 | 97.32% |
| budget_preference_aligned | 291 | 299 | 97.32% |
| budget_within_user_budget | 299 | 299 | 100.00% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 71 | 299 | 23.75% |
| hard_pass | 189 | 299 | 63.21% |
| hotel_budget_covers_nights | 298 | 299 | 99.67% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 298 | 299 | 99.67% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 75 | 299 | 25.08% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_diversity_ok | 157 | 299 | 52.51% |
| meal_grounding_ok | 203 | 299 | 67.89% |
| meal_lunch_dinner_same_day_ok | 225 | 299 | 75.25% |
| meal_repeat_limit_ok | 183 | 299 | 61.20% |
| meal_specific_ok | 297 | 299 | 99.33% |
| meal_valid_semantics_ok | 205 | 299 | 68.56% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| schema_ok | 299 | 300 | 99.67% |
| sft_hard_pass | 189 | 299 | 63.21% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9967,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6713,
    "p50": 0.7,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9653,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9653,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9667,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 116,
  "meal_invalid_name": 94,
  "meal_same_day_lunch_dinner_repeat": 74,
  "budget_arithmetic_inconsistent": 24,
  "budget_preference_mismatch": 8,
  "meal_grounding_miss": 2,
  "meal_placeholder": 2,
  "hotel_budget_underestimated": 1,
  "schema": 1
}
```

## Failure Examples

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-04", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-05", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}]}, {"name_key": "小潘记鸭血粉丝汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "小潘记鸭血粉丝汤"}, {"date": "2026-07-04", "type": "dinner", "name": "小潘记鸭血粉丝汤"}, {"date": "2026-07-05", "type": "dinner", "name": "小潘记鸭血粉丝汤"}, {"date": "2026-07-06", "type": "dinner", "name": "小潘记鸭血粉丝汤"}]}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-28", "type": "dinner", "name": "苏州乐园森林世界", "reason": "unknown_food_semantics"}, {"date": "2026-04-30", "type": "lunch", "name": "苏州乐园森林世界", "reason": "unknown_food_semantics"}, {"date": "2026-04-30", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "小街天府", "dinner": "小街天府"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "方中山胡辣汤(洛阳一店)", "dinner": "方中山胡辣汤(洛阳一店)"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3368, "total": 3368, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 421.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-07", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3035, "total": 2035, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 407.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 9, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "哑巴生煎", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "哑巴生煎(临顿路店)"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "农家菜老大", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-03", "type": "lunch", "name": "农家菜老大(松江店)"}, {"date": "2026-08-04", "type": "lunch", "name": "农家菜老大(九亭店)"}, {"date": "2026-08-05", "type": "lunch", "name": "农家菜老大(松江店)"}, {"date": "2026-08-06", "type": "lunch", "name": "农家菜老大(松江店)"}]}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-22", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "lunch", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000035
- request: 深圳 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蘩楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-02", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-03", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-04", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-05", "type": "dinner", "name": "蘩楼(华强北总店)"}]}, {"name_key": "欧记大排档·江西景德菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-02", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-03", "type": "lunch", "name": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-04", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-05", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}]}]}]`

### v3_harder_eval_000042
- request: 哈尔滨 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000037
- request: 贵阳 2026-01-04->2026-01-08 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-01-04", "lunch": "黔大叔大牌档(甲秀楼店)", "dinner": "黔大叔大牌档(甲秀楼店)"}, {"date": "2026-01-05", "lunch": "金顶山小耳朵清水烫", "dinner": "金顶山小耳朵清水烫"}, {"date": "2026-01-06", "lunch": "赛维利亚中西餐厅(金阳店)", "dinner": "赛维利亚中西餐厅(金阳店)"}, {"date": "2026-01-07", "lunch": "黔大叔大牌档(甲秀楼店)", "dinner": "黔大叔大牌档(甲秀楼店)"}, {"date": "2026-01-08", "lunch": "友谊路糯米饭", "dinner": "友谊路糯米饭"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "黔大叔大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-01-04", "type": "lunch", "name": "黔大叔大牌档(甲秀楼店)"}, {"date": "2026-01-04", "type": "dinner", "name": "黔大叔大牌档(甲秀楼店)"}, {"date": "2026-01-07", "type": "lunch", "name": "黔大叔大牌档(甲秀楼店)"}, {"date": "2026-01-07", "type": "dinner", "name": "黔大叔大牌档(甲秀楼店)"}]}]}]`

### v3_harder_eval_000045
- request: 济南 2026-04-04->2026-04-08 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "箪食巷私房菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "箪食巷私房菜(奥体店)"}, {"date": "2026-04-05", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}, {"date": "2026-04-06", "type": "lunch", "name": "箪食巷私房菜(经十路店)"}, {"date": "2026-04-07", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}, {"date": "2026-04-08", "type": "lunch", "name": "箪食巷私房菜(玉函店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2060, "diff": 1020, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000040
- request: 南京 2026-07-03->2026-07-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-07", "lunch": "麦当劳黄山路餐厅", "dinner": "麦当劳黄山路餐厅"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-07", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-07", "type": "lunch", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-07", "type": "dinner", "name": "麦当劳黄山路餐厅"}]}]}]`

### v3_harder_eval_000043
- request: 桂林 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-08", "type": "lunch", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-09", "type": "lunch", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-10", "type": "lunch", "name": "阿甘酒家(中山店)"}, {"date": "2026-05-11", "type": "lunch", "name": "阿甘酒家(中山店)"}]}, {"name_key": "食在香乡野本地菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "食在香乡野本地菜"}, {"date": "2026-05-08", "type": "dinner", "name": "食在香乡野本地菜"}, {"date": "2026-05-09", "type": "dinner", "name": "食在香乡野本地菜"}, {"date": "2026-05-10", "type": "dinner", "name": "食在香乡野本地菜"}, {"date": "2026-05-11", "type": "dinner", "name": "食在香乡野本地菜"}]}]}]`

### v3_harder_eval_000048
- request: 北京 2026-01-04->2026-01-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-01-04", "lunch": "紫光园·烤鸭·北京菜(前门大栅栏店)", "dinner": "紫光园·烤鸭·北京菜(前门大栅栏店)"}, {"date": "2026-01-05", "lunch": "胡大饭馆(簋街三店)", "dinner": "胡大饭馆(簋街三店)"}, {"date": "2026-01-06", "lunch": "紫光园·烤鸭·北京菜(前门大栅栏店)", "dinner": "紫光园·烤鸭·北京菜(前门大栅栏店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "紫光园·烤鸭·北京菜", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-01-04", "type": "lunch", "name": "紫光园·烤鸭·北京菜(前门大栅栏店)"}, {"date": "2026-01-04", "type": "dinner", "name": "紫光园·烤鸭·北京菜(前门大栅栏店)"}, {"date": "2026-01-06", "type": "lunch", "name": "紫光园·烤鸭·北京菜(前门大栅栏店)"}, {"date": "2026-01-06", "type": "dinner", "name": "紫光园·烤鸭·北京菜(前门大栅栏店)"}]}]}]`
