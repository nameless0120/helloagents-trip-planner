# Rule Eval Report: base_qwen25_7b_v3_ctx_hard_compact_budget_ledger_smoke5

- records: 5
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_budget_ledger_smoke5/generations.jsonl`
- records_path: `training/data/v3/context_ablation/hard_compact_prompt_budget_ledger_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 5 | 5 | 100.00% |
| attraction_budget_consistent | 0 | 5 | 0.00% |
| attraction_count_ok | 5 | 5 | 100.00% |
| attraction_diversity_ok | 4 | 5 | 80.00% |
| attraction_grounding_ok | 5 | 5 | 100.00% |
| attraction_repeat_limit_ok | 4 | 5 | 80.00% |
| budget_arithmetic_consistent | 2 | 5 | 40.00% |
| budget_consistent | 2 | 5 | 40.00% |
| budget_level_aligned | 1 | 5 | 20.00% |
| budget_preference_aligned | 1 | 5 | 20.00% |
| budget_user_constraint_ok | 4 | 5 | 80.00% |
| budget_within_user_budget | 4 | 5 | 80.00% |
| city_ok | 5 | 5 | 100.00% |
| date_range_ok | 5 | 5 | 100.00% |
| day_dates_ok | 5 | 5 | 100.00% |
| day_index_ok | 5 | 5 | 100.00% |
| days_len_ok | 5 | 5 | 100.00% |
| dpo_soft_pass | 0 | 5 | 0.00% |
| hard_pass | 0 | 5 | 0.00% |
| hotel_budget_covers_nights | 5 | 5 | 100.00% |
| hotel_distance_placeholder_ok | 5 | 5 | 100.00% |
| hotel_grounding_ok | 5 | 5 | 100.00% |
| invalid_hotel_name_ok | 5 | 5 | 100.00% |
| json_extract_ok | 5 | 5 | 100.00% |
| legacy_hard_pass | 0 | 5 | 0.00% |
| location_object_ok | 5 | 5 | 100.00% |
| meal_budget_consistent | 0 | 5 | 0.00% |
| meal_complete | 5 | 5 | 100.00% |
| meal_diversity_ok | 2 | 5 | 40.00% |
| meal_grounding_ok | 4 | 5 | 80.00% |
| meal_lunch_dinner_same_day_ok | 3 | 5 | 60.00% |
| meal_repeat_limit_ok | 2 | 5 | 40.00% |
| meal_specific_ok | 5 | 5 | 100.00% |
| meal_valid_semantics_ok | 4 | 5 | 80.00% |
| middle_hotel_ok | 5 | 5 | 100.00% |
| schema_ok | 5 | 5 | 100.00% |
| sft_hard_pass | 0 | 5 | 0.00% |
| transportation_budget_nonnegative | 5 | 5 | 100.00% |
| weather_dates_ok | 5 | 5 | 100.00% |
| weather_match | 5 | 5 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9778,
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
    "avg": 0.5517,
    "p50": 0.6,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9833,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9833,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9833,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "attraction_budget_inconsistent": 5,
  "meal_budget_inconsistent": 5,
  "budget_preference_mismatch": 4,
  "meal_repeat_too_many": 3,
  "budget_arithmetic_inconsistent": 3,
  "meal_same_day_lunch_dinner_repeat": 2,
  "meal_invalid_name": 1,
  "budget_hard_constraint_exceeded": 1,
  "attraction_repeat_too_many": 1
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "桂林山水甲天下", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(金水湾店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1120, "expected_total_meals": 1196, "reported_total_meals": 660, "reported_total_transportation": 800}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(同德店)"}, {"date": "2026-04-05", "lunch": "四方小炒•云南菜小当家(同德店)", "dinner": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒•云南菜小当家(同德店)", "dinner": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒•云南菜小当家(同德店)", "dinner": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒•云南菜小当家(同德店)", "dinner": "四方小炒•云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒•云南菜小当家", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-04-05", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒•云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒•云南菜小当家(联盟店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4225, "total": 3225, "diff": 1000, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 129.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-10", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 320, "expected_total_meals": 503, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3110, "total": 2110, "diff": 1000, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 131.88, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 1140, "expected_total_meals": 120, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 1140, "expected_total_meals": 120, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "流花湖公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-03", "day_index": 0, "name": "流花湖公园"}, {"date": "2026-07-07", "day_index": 4, "name": "流花湖公园"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2995, "total": 2060, "diff": 935, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 412.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 705, "reported_total_attractions": 1115, "expected_total_meals": 1028, "reported_total_meals": 480, "reported_total_transportation": 200}}]`
