# 新版餐饮多样性 Baseline 规则评估对比

- 新版 run：`base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16`
- 对比口径：旧 baseline 使用同一版餐饮多样性 rule metrics 重新评估。

## 指标对比

| 指标 | 旧Prompt | 新Prompt | 变化 |
| --- | ---: | ---: | ---: |
| Schema通过 | 99.00% (297/300) | 98.67% (296/300) | -0.33% |
| Hard Pass | 8.42% (25/297) | 40.54% (120/296) | +32.12% |
| 餐饮多样性 | 10.44% (31/297) | 52.70% (156/296) | +42.26% |
| 同天午晚餐不同店 | 53.87% (160/297) | 71.62% (212/296) | +17.75% |
| 整趟餐厅重复不过量 | 17.51% (52/297) | 67.23% (199/296) | +49.72% |
| 餐饮food_pois命中 | 95.96% (285/297) | 87.16% (258/296) | -8.80% |
| 餐饮语义有效 | 96.63% (287/297) | 88.51% (262/296) | -8.12% |
| 预算加总一致 | 93.94% (279/297) | 88.51% (262/296) | -5.43% |

## 餐饮多样性数值

- 旧Prompt meal_diversity_unique_rate avg：`0.3525`
- 新Prompt meal_diversity_unique_rate avg：`0.7257`

## 新版主要失败类型

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

## 餐饮问题样本（前20条）

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- meal_repeat_too_many: `[{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(西街店)", "dinner": "椿记烧鹅(南溪店)"}]`
- meal_repeat_too_many: `[{"name_key": "椿记烧鹅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(南溪店)"}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- meal_repeat_too_many: `[{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- meal_repeat_too_many: `[{"name_key": "大鸽饭", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "大鸽饭(体育西店)"}, {"date": "2026-07-04", "type": "dinner", "name": "大鸽饭(棠下店)"}, {"date": "2026-07-05", "type": "lunch", "name": "大鸽饭(体育西店)"}, {"date": "2026-07-06", "type": "lunch", "name": "大鸽饭(棠下店)"}, {"date": "2026-07-07", "type": "lunch", "name": "大鸽饭(体育西店)"}]}, {"name_key": "松苑·浓汤广府菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-04", "type": "lunch", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-05", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-06", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}, {"date": "2026-07-07", "type": "dinner", "name": "松苑·浓汤广府菜(总店)"}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- meal_repeat_too_many: `[{"name_key": "清真刚刚烤肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-22", "type": "dinner", "name": "清真刚刚烤肉(小南门店)"}, {"date": "2026-04-23", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-24", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]`
- meal_repeat_too_many: `[{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- meal_repeat_too_many: `[{"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "哑巴生煎", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "哑巴生煎(临顿路店)"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]`
- meal_repeat_too_many: `[{"name_key": "则瓦米线·云南小吃集合", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- meal_grounding_miss: `[{"date": "2026-04-04", "type": "dinner", "name": "民俗街夜市"}]`
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-04-07", "lunch": "麦当劳(桂林临桂万达餐厅)", "dinner": "麦当劳(桂林临桂万达餐厅)"}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-06-21", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]`
- meal_repeat_too_many: `[{"name_key": "老姑东北人", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-19", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- meal_invalid_name: `[{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-08-04", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}, {"date": "2026-08-06", "lunch": "海福多共富海鲜面馆", "dinner": "海福多共富海鲜面馆"}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(深圳首店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-03-07", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-05-09", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-10", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-11", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}]`
- meal_repeat_too_many: `[{"name_key": "大毛.淮扬菜", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-10", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-10", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-11", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-11", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- meal_invalid_name: `[{"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]`
- meal_repeat_too_many: `[{"name_key": "杭州酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "杭州酒家(延安路店)"}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- meal_invalid_name: `[{"date": "2026-05-11", "type": "dinner", "name": "无", "reason": "empty_or_none"}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- meal_same_day_lunch_dinner_repeat: `[{"date": "2026-06-05", "lunch": "刘聋子牛肉粉馆(光谷新竹路店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]`
- meal_repeat_too_many: `[{"name_key": "刘聋子牛肉粉馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "lunch", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- meal_repeat_too_many: `[{"name_key": "四方坪三十栋饭店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-04", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-05", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-06", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}]}]`

### v3_harder_eval_000033
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- meal_repeat_too_many: `[{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-09", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "吴记小园楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-09", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-10", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-11", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-12", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}]}]`
