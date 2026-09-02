# Base vs SFT Relaxed Accommodation Comparison

本报告在评估时临时修复 `days[*].accommodation = null/缺失`，用于观察去掉该 schema 小坑后两个模型的差异。

## End-to-End Metrics

| Metric | base_qwen25_7b_prompt_v2 | sft_v2_clean_prompt_v2 |
| --- | ---: | ---: |
| call_ok | 91/91 (100.00%) | 91/91 (100.00%) |
| json_extract_ok | 91/91 (100.00%) | 89/91 (97.80%) |
| schema_ok | 91/91 (100.00%) | 88/91 (96.70%) |
| hard_pass | 86/91 (94.51%) | 87/91 (95.60%) |
| weather_match | 91/91 (100.00%) | 88/91 (96.70%) |
| attraction_count_ok | 87/91 (95.60%) | 87/91 (95.60%) |
| middle_hotel_ok | 91/91 (100.00%) | 88/91 (96.70%) |
| invalid_hotel_name_ok | 91/91 (100.00%) | 88/91 (96.70%) |
| budget_consistent | 88/91 (96.70%) | 82/91 (90.11%) |
| budget_arithmetic_consistent | 88/91 (96.70%) | 82/91 (90.11%) |
| budget_within_user_budget | 89/91 (97.80%) | 88/91 (96.70%) |
| budget_level_aligned | 67/91 (73.63%) | 55/91 (60.44%) |
| budget_preference_aligned | 66/91 (72.53%) | 55/91 (60.44%) |

## Relaxed Repair Counts

| Model | Repaired Records | Repaired Days |
| --- | ---: | ---: |
| base_qwen25_7b_prompt_v2 | 75 | 75 |
| sft_v2_clean_prompt_v2 | 0 | 0 |

## Conditional Metrics From Existing Summarizer

这些指标沿用原规则评估汇总，部分分母只覆盖 schema 通过样本。

```json
{
  "base_qwen25_7b_prompt_v2": {
    "boolean_metrics": {
      "attraction_count_ok": {
        "pass": 87,
        "total": 91,
        "rate": 0.956
      },
      "budget_arithmetic_consistent": {
        "pass": 88,
        "total": 91,
        "rate": 0.967
      },
      "budget_consistent": {
        "pass": 88,
        "total": 91,
        "rate": 0.967
      },
      "budget_level_aligned": {
        "pass": 67,
        "total": 91,
        "rate": 0.7363
      },
      "budget_preference_aligned": {
        "pass": 66,
        "total": 91,
        "rate": 0.7253
      },
      "budget_within_user_budget": {
        "pass": 89,
        "total": 91,
        "rate": 0.978
      },
      "city_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "date_range_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "day_dates_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "day_index_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "days_len_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "hard_pass": {
        "pass": 86,
        "total": 91,
        "rate": 0.9451
      },
      "invalid_hotel_name_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "json_extract_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "location_object_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "meal_complete": {
        "pass": 90,
        "total": 91,
        "rate": 0.989
      },
      "middle_hotel_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "schema_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "weather_dates_ok": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "weather_match": {
        "pass": 91,
        "total": 91,
        "rate": 1.0
      }
    },
    "numeric_metrics": {
      "attraction_grounding_rate": {
        "avg": 1.0,
        "p50": 1.0,
        "p90": 1.0
      },
      "hotel_grounding_rate": {
        "avg": 1.0,
        "p50": 1.0,
        "p90": 1.0
      }
    },
    "failure_stages": {
      "rule": 28
    },
    "error_types": {
      "budget_preference_mismatch": 25,
      "budget_arithmetic_inconsistent": 3
    },
    "latency": {
      "avg": 40.4476,
      "p50": 37.876,
      "p90": 57.11,
      "p99": 62.097
    },
    "output_chars": {
      "avg": 4392.1099,
      "p50": 3870.0,
      "p90": 6007.0
    }
  },
  "sft_v2_clean_prompt_v2": {
    "boolean_metrics": {
      "attraction_count_ok": {
        "pass": 87,
        "total": 88,
        "rate": 0.9886
      },
      "budget_arithmetic_consistent": {
        "pass": 82,
        "total": 88,
        "rate": 0.9318
      },
      "budget_consistent": {
        "pass": 82,
        "total": 88,
        "rate": 0.9318
      },
      "budget_level_aligned": {
        "pass": 55,
        "total": 88,
        "rate": 0.625
      },
      "budget_preference_aligned": {
        "pass": 55,
        "total": 88,
        "rate": 0.625
      },
      "budget_within_user_budget": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "city_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "date_range_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "day_dates_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "day_index_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "days_len_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "hard_pass": {
        "pass": 87,
        "total": 88,
        "rate": 0.9886
      },
      "invalid_hotel_name_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "json_extract_ok": {
        "pass": 89,
        "total": 91,
        "rate": 0.978
      },
      "location_object_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "meal_complete": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "middle_hotel_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "schema_ok": {
        "pass": 88,
        "total": 91,
        "rate": 0.967
      },
      "weather_dates_ok": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      },
      "weather_match": {
        "pass": 88,
        "total": 88,
        "rate": 1.0
      }
    },
    "numeric_metrics": {
      "attraction_grounding_rate": {
        "avg": 0.9972,
        "p50": 1.0,
        "p90": 1.0
      },
      "hotel_grounding_rate": {
        "avg": 1.0,
        "p50": 1.0,
        "p90": 1.0
      }
    },
    "failure_stages": {
      "rule": 40,
      "json_extract": 2,
      "schema": 1
    },
    "error_types": {
      "budget_preference_mismatch": 33,
      "budget_arithmetic_inconsistent": 6,
      "json_extract": 2,
      "schema": 1,
      "too_many_attractions": 1
    },
    "latency": {
      "avg": 54.6714,
      "p50": 49.934,
      "p90": 68.56,
      "p99": 89.102
    },
    "output_chars": {
      "avg": 5969.3407,
      "p50": 5662.0,
      "p90": 7381.0
    }
  }
}
```
