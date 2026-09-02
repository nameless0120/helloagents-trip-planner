# Base vs SFT Relaxed Accommodation Comparison

本报告在评估时临时修复 `days[*].accommodation = null/缺失`，用于观察去掉该 schema 小坑后两个模型的差异。

## End-to-End Metrics

| Metric | base_qwen25_7b | sft_v2_clean |
| --- | ---: | ---: |
| call_ok | 91/91 (100.00%) | 91/91 (100.00%) |
| json_extract_ok | 91/91 (100.00%) | 89/91 (97.80%) |
| schema_ok | 91/91 (100.00%) | 89/91 (97.80%) |
| hard_pass | 74/91 (81.32%) | 88/91 (96.70%) |
| weather_match | 90/91 (98.90%) | 89/91 (97.80%) |
| attraction_count_ok | 88/91 (96.70%) | 88/91 (96.70%) |
| middle_hotel_ok | 78/91 (85.71%) | 89/91 (97.80%) |
| invalid_hotel_name_ok | 91/91 (100.00%) | 89/91 (97.80%) |
| budget_consistent | 86/91 (94.51%) | 76/91 (83.52%) |
| budget_arithmetic_consistent | 86/91 (94.51%) | 76/91 (83.52%) |
| budget_within_user_budget | 90/91 (98.90%) | 88/91 (96.70%) |
| budget_level_aligned | 70/91 (76.92%) | 63/91 (69.23%) |
| budget_preference_aligned | 70/91 (76.92%) | 62/91 (68.13%) |

## Relaxed Repair Counts

| Model | Repaired Records | Repaired Days |
| --- | ---: | ---: |
| base_qwen25_7b | 19 | 46 |
| sft_v2_clean | 0 | 0 |

## Conditional Metrics From Existing Summarizer

这些指标沿用原规则评估汇总，部分分母只覆盖 schema 通过样本。

```json
{
  "base_qwen25_7b": {
    "boolean_metrics": {
      "attraction_count_ok": {
        "pass": 88,
        "total": 91,
        "rate": 0.967
      },
      "budget_arithmetic_consistent": {
        "pass": 86,
        "total": 91,
        "rate": 0.9451
      },
      "budget_consistent": {
        "pass": 86,
        "total": 91,
        "rate": 0.9451
      },
      "budget_level_aligned": {
        "pass": 70,
        "total": 91,
        "rate": 0.7692
      },
      "budget_preference_aligned": {
        "pass": 70,
        "total": 91,
        "rate": 0.7692
      },
      "budget_within_user_budget": {
        "pass": 90,
        "total": 91,
        "rate": 0.989
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
        "pass": 74,
        "total": 91,
        "rate": 0.8132
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
        "pass": 91,
        "total": 91,
        "rate": 1.0
      },
      "middle_hotel_ok": {
        "pass": 78,
        "total": 91,
        "rate": 0.8571
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
        "pass": 90,
        "total": 91,
        "rate": 0.989
      }
    },
    "numeric_metrics": {
      "attraction_grounding_rate": {
        "avg": 0.996,
        "p50": 1.0,
        "p90": 1.0
      },
      "hotel_grounding_rate": {
        "avg": 0.8571,
        "p50": 1.0,
        "p90": 1.0
      }
    },
    "failure_stages": {
      "rule": 40
    },
    "error_types": {
      "budget_preference_mismatch": 21,
      "middle_hotel_null": 13,
      "budget_arithmetic_inconsistent": 5,
      "weather_mismatch": 1
    },
    "latency": {
      "avg": 41.9776,
      "p50": 40.922,
      "p90": 55.365,
      "p99": 64.575
    },
    "output_chars": {
      "avg": 5449.3516,
      "p50": 5295.0,
      "p90": 7132.0
    }
  },
  "sft_v2_clean": {
    "boolean_metrics": {
      "attraction_count_ok": {
        "pass": 88,
        "total": 89,
        "rate": 0.9888
      },
      "budget_arithmetic_consistent": {
        "pass": 76,
        "total": 89,
        "rate": 0.8539
      },
      "budget_consistent": {
        "pass": 76,
        "total": 89,
        "rate": 0.8539
      },
      "budget_level_aligned": {
        "pass": 63,
        "total": 89,
        "rate": 0.7079
      },
      "budget_preference_aligned": {
        "pass": 62,
        "total": 89,
        "rate": 0.6966
      },
      "budget_within_user_budget": {
        "pass": 88,
        "total": 89,
        "rate": 0.9888
      },
      "city_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "date_range_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "day_dates_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "day_index_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "days_len_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "hard_pass": {
        "pass": 88,
        "total": 89,
        "rate": 0.9888
      },
      "invalid_hotel_name_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "json_extract_ok": {
        "pass": 89,
        "total": 91,
        "rate": 0.978
      },
      "location_object_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "meal_complete": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "middle_hotel_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "schema_ok": {
        "pass": 89,
        "total": 91,
        "rate": 0.978
      },
      "weather_dates_ok": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      },
      "weather_match": {
        "pass": 89,
        "total": 89,
        "rate": 1.0
      }
    },
    "numeric_metrics": {
      "attraction_grounding_rate": {
        "avg": 0.9952,
        "p50": 1.0,
        "p90": 1.0
      },
      "hotel_grounding_rate": {
        "avg": 0.9888,
        "p50": 1.0,
        "p90": 1.0
      }
    },
    "failure_stages": {
      "rule": 41,
      "json_extract": 2
    },
    "error_types": {
      "budget_preference_mismatch": 27,
      "budget_arithmetic_inconsistent": 13,
      "json_extract": 2,
      "too_many_attractions": 1
    },
    "latency": {
      "avg": 51.0005,
      "p50": 50.466,
      "p90": 67.07,
      "p99": 81.464
    },
    "output_chars": {
      "avg": 5869.6264,
      "p50": 5801.0,
      "p90": 7544.0
    }
  }
}
```
