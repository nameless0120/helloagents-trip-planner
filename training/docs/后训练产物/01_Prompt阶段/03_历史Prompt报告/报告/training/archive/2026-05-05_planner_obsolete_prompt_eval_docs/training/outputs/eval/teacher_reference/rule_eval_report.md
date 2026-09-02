# Rule Eval Report: teacher_reference

- records: 91
- generations: `training/outputs/eval/teacher_reference/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 91 | 91 | 100.00% |
| budget_consistent | 91 | 91 | 100.00% |
| city_ok | 91 | 91 | 100.00% |
| date_range_ok | 91 | 91 | 100.00% |
| day_dates_ok | 91 | 91 | 100.00% |
| day_index_ok | 91 | 91 | 100.00% |
| days_len_ok | 91 | 91 | 100.00% |
| hard_pass | 91 | 91 | 100.00% |
| invalid_hotel_name_ok | 91 | 91 | 100.00% |
| json_extract_ok | 91 | 91 | 100.00% |
| location_object_ok | 91 | 91 | 100.00% |
| meal_complete | 91 | 91 | 100.00% |
| middle_hotel_ok | 91 | 91 | 100.00% |
| schema_ok | 91 | 91 | 100.00% |
| weather_dates_ok | 91 | 91 | 100.00% |
| weather_match | 91 | 91 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9976,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
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
