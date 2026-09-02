# Rule Eval Report: debug_ablation_one

- records: 1
- generations: `training/outputs/eval/debug_ablation_one/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_hard_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 1 | 1 | 100.00% |
| budget_arithmetic_consistent | 1 | 1 | 100.00% |
| budget_consistent | 1 | 1 | 100.00% |
| budget_level_aligned | 1 | 1 | 100.00% |
| budget_preference_aligned | 1 | 1 | 100.00% |
| budget_within_user_budget | 1 | 1 | 100.00% |
| city_ok | 1 | 1 | 100.00% |
| date_range_ok | 1 | 1 | 100.00% |
| day_dates_ok | 1 | 1 | 100.00% |
| day_index_ok | 1 | 1 | 100.00% |
| days_len_ok | 1 | 1 | 100.00% |
| hard_pass | 1 | 1 | 100.00% |
| hotel_budget_covers_nights | 1 | 1 | 100.00% |
| hotel_distance_placeholder_ok | 1 | 1 | 100.00% |
| invalid_hotel_name_ok | 1 | 1 | 100.00% |
| json_extract_ok | 1 | 1 | 100.00% |
| location_object_ok | 1 | 1 | 100.00% |
| meal_complete | 1 | 1 | 100.00% |
| meal_grounding_ok | 1 | 1 | 100.00% |
| meal_specific_ok | 1 | 1 | 100.00% |
| middle_hotel_ok | 1 | 1 | 100.00% |
| schema_ok | 1 | 1 | 100.00% |
| weather_dates_ok | 1 | 1 | 100.00% |
| weather_match | 1 | 1 | 100.00% |

## Numeric Metrics

```json
{
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
  "meal_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{}
```

## Failure Examples
