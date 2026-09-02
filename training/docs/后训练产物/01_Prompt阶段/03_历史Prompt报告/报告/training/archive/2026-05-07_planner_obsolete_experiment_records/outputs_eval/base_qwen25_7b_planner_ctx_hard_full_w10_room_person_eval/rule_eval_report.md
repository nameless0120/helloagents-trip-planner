# Rule Eval Report: base_qwen25_7b_v3_ctx_hard_full_w10_room_person_eval

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_full_w10/generations.jsonl`
- records_path: `training/data/v3/context_ablation/hard_baseline_full_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 256 | 294 | 87.07% |
| attraction_budget_consistent | 46 | 294 | 15.65% |
| attraction_budget_party_relation_ok | 81 | 294 | 27.55% |
| attraction_count_ok | 294 | 294 | 100.00% |
| attraction_diversity_ok | 257 | 294 | 87.41% |
| attraction_grounding_ok | 291 | 294 | 98.98% |
| attraction_repeat_limit_ok | 257 | 294 | 87.41% |
| budget_arithmetic_consistent | 178 | 294 | 60.54% |
| budget_consistent | 178 | 294 | 60.54% |
| budget_level_aligned | 99 | 294 | 33.67% |
| budget_preference_aligned | 99 | 294 | 33.67% |
| budget_relationship_ok | 16 | 294 | 5.44% |
| budget_user_constraint_ok | 242 | 294 | 82.31% |
| budget_within_user_budget | 276 | 294 | 93.88% |
| city_ok | 294 | 294 | 100.00% |
| date_range_ok | 294 | 294 | 100.00% |
| day_dates_ok | 294 | 294 | 100.00% |
| day_index_ok | 294 | 294 | 100.00% |
| days_len_ok | 294 | 294 | 100.00% |
| dpo_soft_pass | 0 | 294 | 0.00% |
| hard_pass | 0 | 294 | 0.00% |
| hotel_budget_covers_nights | 118 | 294 | 40.14% |
| hotel_budget_relation_ok | 123 | 294 | 41.84% |
| hotel_distance_placeholder_ok | 294 | 294 | 100.00% |
| hotel_grounding_ok | 294 | 294 | 100.00% |
| invalid_hotel_name_ok | 294 | 294 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 5 | 294 | 1.70% |
| location_object_ok | 294 | 294 | 100.00% |
| meal_budget_consistent | 0 | 294 | 0.00% |
| meal_complete | 293 | 294 | 99.66% |
| meal_cost_scale_ok | 238 | 294 | 80.95% |
| meal_diversity_ok | 24 | 294 | 8.16% |
| meal_grounding_ok | 286 | 294 | 97.28% |
| meal_lunch_dinner_same_day_ok | 150 | 294 | 51.02% |
| meal_repeat_limit_ok | 47 | 294 | 15.99% |
| meal_specific_ok | 294 | 294 | 100.00% |
| meal_valid_semantics_ok | 289 | 294 | 98.30% |
| middle_hotel_ok | 294 | 294 | 100.00% |
| schema_ok | 294 | 300 | 98.00% |
| sft_budget_semantic_hard_pass | 10 | 294 | 3.40% |
| sft_hard_pass | 0 | 294 | 0.00% |
| transportation_budget_nonnegative | 294 | 294 | 100.00% |
| weather_dates_ok | 294 | 294 | 100.00% |
| weather_match | 294 | 294 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9782,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3477,
    "p50": 0.25,
    "p90": 0.6667
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9943,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9943,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9952,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 294,
  "budget_relationship_mismatch": 278,
  "attraction_budget_inconsistent": 248,
  "meal_repeat_too_many": 247,
  "budget_preference_mismatch": 195,
  "hotel_budget_underestimated": 176,
  "meal_same_day_lunch_dinner_repeat": 144,
  "budget_arithmetic_inconsistent": 116,
  "meal_cost_scale_too_low": 56,
  "budget_hard_constraint_exceeded": 52,
  "accommodation_type_mismatch": 38,
  "attraction_repeat_too_many": 37,
  "schema": 6,
  "meal_invalid_name": 5,
  "meal_grounding_miss": 3
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-10", "lunch": "大队老渔村", "dinner": "大队老渔村"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}, {"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-09", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-10", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4194, "total": 4144, "diff": 50, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 460.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳黄山路餐厅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-03", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-04", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-05", "type": "dinner", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "breakfast", "name": "麦当劳黄山路餐厅"}, {"date": "2026-07-06", "type": "dinner", "name": "麦当劳黄山路餐厅"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-04", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-05", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "宽窄巷子景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 0, "name": "宽窄巷子景区"}, {"date": "2026-05-09", "day_index": 1, "name": "宽窄巷子景区"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "浆小白豆浆夜市", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-04-28", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-04-29", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-04-30", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1056, "expected_total_meals": 4224, "reported_total_meals": 1008, "reported_total_transportation": 800}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(中山店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4622, "total": 4612, "diff": 10, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 2, "total": 9100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 576.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6400, "target_max_total": 10200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-01", "lunch": "郑阿公顺德鸡煲饭双皮奶(萧山店)", "dinner": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "郑阿公顺德鸡煲饭双皮奶", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-28", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-04-29", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-04-30", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-05-01", "type": "lunch", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}, {"date": "2026-05-01", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "lunch", "name": "李志贤灌汤包子"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 224, "expected_total_attractions": 448, "reported_total_attractions": 480, "meal_per_person_cost_sum": 500, "expected_total_meals": 1000, "reported_total_meals": 432, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 224, "expected_total_attractions": 448, "reported_total_attractions": 480, "meal_per_person_cost_sum": 500, "expected_total_meals": 1000, "reported_total_meals": 432, "reported_total_transportation": 200}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "广州塔", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-04", "day_index": 1, "name": "广州塔"}, {"date": "2026-07-06", "day_index": 3, "name": "广州塔"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3035, "total": 2035, "diff": 1000, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 407.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 705, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 1090, "expected_total_meals": 1090, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-03", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-05", "type": "lunch", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-19", "lunch": "紫阳海鲜楼·传承闽味(长乐路总店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}, {"date": "2026-06-21", "lunch": "某有茶·黑糖珍珠奶茶(三坊七巷店)", "dinner": "某有茶·黑糖珍珠奶茶(仓山万达金街店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1472, "expected_total_meals": 2944, "reported_total_meals": 1254, "reported_total_transportation": 800}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "天津之眼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-03", "day_index": 0, "name": "天津之眼"}, {"date": "2026-07-05", "day_index": 2, "name": "天津之眼"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-03", "type": "dinner", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "dinner", "name": "南楼煎饼"}, {"date": "2026-07-05", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-05", "type": "dinner", "name": "南楼煎饼"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 3600, "diff": -1200, "covers_nights": false}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "苏福记", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "lunch", "name": "苏福记(高新店)"}, {"date": "2026-04-22", "type": "lunch", "name": "苏福记(高新店)"}, {"date": "2026-04-23", "type": "lunch", "name": "苏福记(高新店)"}, {"date": "2026-04-24", "type": "lunch", "name": "苏福记(高新店)"}]}, {"name_key": "乐班le’ban·农场餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2026-04-22", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2026-04-23", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2026-04-24", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 2250, "diff": -3150, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 200, "expected_total_attractions": 1000, "reported_total_attractions": 1800, "meal_per_person_cost_sum": 4280, "expected_total_meals": 21400, "reported_total_meals": 1620, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-06", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 670, "expected_total_meals": 1340, "reported_total_meals": 1026, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-03", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 12, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 960, "meal_per_person_cost_sum": 640, "expected_total_meals": 1280, "reported_total_meals": 450, "reported_total_transportation": 400}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "小街天府", "dinner": "小街天府"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1400, "reported_total_hotels": 1200, "diff": -200, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1424, "expected_total_meals": 5696, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-07", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4240, "total": 3240, "diff": 1000, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 2, "total": 6700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 324.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4400, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 90, "expected_total_attractions": 180, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 2880, "expected_total_meals": 5760, "reported_total_meals": 1440, "reported_total_transportation": 200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-22", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}]}, {"name_key": "老姑东北人", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}]}, {"name_key": "晚酒·阿英川菜馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "dinner", "name": "晚酒·阿英川菜馆(一店)"}, {"date": "2026-06-20", "type": "dinner", "name": "晚酒·阿英川菜馆(一店)"}, {"date": "2026-06-21", "type": "dinner", "name": "晚酒·阿英川菜馆(一店)"}, {"date": "2026-06-22", "type": "dinner", "name": "晚酒·阿英川菜馆(一店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4350, "total": 4550, "diff": -200, "requested_budget": {"available": true, "amount": 16100, "scope": "total", "party_size": 5, "total": 16100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 182.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 16100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 10500, "target_max_total": 16100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
