# High-End Context Mainline Comparison

- records standard: `training/data/planner/eval/records.jsonl`
- records hard: `training/data/planner/eval_hard/records.jsonl`
- serving: vLLM, GPU 0/1/2, workers=10 per model, temperature=0.2
- models: `base`, `legacy_b`, `valloss_lr8e5`
- rule eval: rerun after POI name normalizer relaxed matching fix

## standard

| Metric | base | legacy_b | valloss_lr8e5 |
| --- | ---: | ---: | ---: |
| hard_pass | 89.90% (178/198) | 93.47% (186/199) | 96.46% (191/198) |
| sft_strict_hard_pass | 0.00% (0/198) | 0.00% (0/199) | 0.00% (0/198) |
| dpo_soft_pass | 5.56% (11/198) | 55.28% (110/199) | 61.11% (121/198) |
| dpo_soft_recomputed_budget_pass | 13.13% (26/198) | 42.71% (85/199) | 45.45% (90/198) |
| json_extract_ok | 100.00% (200/200) | 100.00% (200/200) | 100.00% (200/200) |
| schema_ok | 99.00% (198/200) | 99.50% (199/200) | 99.00% (198/200) |
| meal_grounding_ok | 94.95% (188/198) | 98.99% (197/199) | 98.48% (195/198) |
| meal_specific_ok | 100.00% (198/198) | 100.00% (199/199) | 100.00% (198/198) |
| meal_valid_semantics_ok | 96.46% (191/198) | 99.50% (198/199) | 99.49% (197/198) |
| meal_diversity_ok | 30.81% (61/198) | 83.92% (167/199) | 88.38% (175/198) |
| attraction_grounding_ok | 99.49% (197/198) | 97.99% (195/199) | 98.99% (196/198) |
| hotel_grounding_ok | 98.99% (196/198) | 100.00% (199/199) | 100.00% (198/198) |
| budget_user_constraint_ok | 98.99% (196/198) | 98.99% (197/199) | 98.99% (196/198) |
| budget_preference_aligned | 18.18% (36/198) | 75.88% (151/199) | 77.27% (153/198) |
| recomputed_budget_fit_ok | 43.94% (87/198) | 57.29% (114/199) | 57.07% (113/198) |
| budget_relationship_ok | 6.06% (12/198) | 52.76% (105/199) | 56.57% (112/198) |
| meal_cost_scale_ok | 35.35% (70/198) | 68.34% (136/199) | 73.23% (145/198) |
| latency_avg | 63.3056 | 79.1494 | 79.2151 |
| latency_p90 | 83.24 | 108.416 | 108.591 |
| output_chars_avg | 5843.245 | 5810.53 | 5818.745 |

### failure types

**base**

```json
{
  "meal_budget_inconsistent": 198,
  "budget_relationship_mismatch": 186,
  "attraction_budget_inconsistent": 172,
  "budget_preference_mismatch": 162,
  "meal_repeat_too_many": 132,
  "meal_cost_scale_too_low": 128,
  "hotel_budget_underestimated": 109,
  "budget_arithmetic_inconsistent": 93,
  "meal_same_day_lunch_dinner_repeat": 45,
  "attraction_repeat_too_many": 18,
  "meal_invalid_name": 7,
  "accommodation_type_mismatch": 5,
  "meal_grounding_miss": 3,
  "schema": 2,
  "budget_hard_constraint_exceeded": 2,
  "weather_mismatch": 1
}
```

**legacy_b**

```json
{
  "meal_budget_inconsistent": 199,
  "attraction_budget_inconsistent": 134,
  "budget_relationship_mismatch": 94,
  "meal_cost_scale_too_low": 63,
  "budget_arithmetic_inconsistent": 55,
  "budget_preference_mismatch": 48,
  "hotel_budget_underestimated": 24,
  "meal_repeat_too_many": 22,
  "meal_same_day_lunch_dinner_repeat": 17,
  "attraction_repeat_too_many": 17,
  "too_many_attractions": 7,
  "budget_hard_constraint_exceeded": 2,
  "meal_invalid_name": 1,
  "meal_grounding_miss": 1,
  "schema": 1
}
```

**valloss_lr8e5**

```json
{
  "meal_budget_inconsistent": 198,
  "attraction_budget_inconsistent": 134,
  "budget_relationship_mismatch": 86,
  "meal_cost_scale_too_low": 53,
  "budget_arithmetic_inconsistent": 47,
  "budget_preference_mismatch": 45,
  "hotel_budget_underestimated": 35,
  "meal_repeat_too_many": 17,
  "attraction_repeat_too_many": 16,
  "meal_same_day_lunch_dinner_repeat": 9,
  "too_many_attractions": 3,
  "budget_hard_constraint_exceeded": 2,
  "schema": 2,
  "meal_grounding_miss": 2,
  "meal_invalid_name": 1
}
```

## hard

| Metric | base | legacy_b | valloss_lr8e5 |
| --- | ---: | ---: | ---: |
| hard_pass | 83.28% (249/299) | 93.67% (281/300) | 91.97% (275/299) |
| sft_strict_hard_pass | 0.00% (0/299) | 0.00% (0/300) | 0.00% (0/299) |
| dpo_soft_pass | 3.34% (10/299) | 43.00% (129/300) | 46.15% (138/299) |
| dpo_soft_recomputed_budget_pass | 3.34% (10/299) | 31.00% (93/300) | 35.12% (105/299) |
| json_extract_ok | 100.00% (300/300) | 100.00% (300/300) | 99.67% (299/300) |
| schema_ok | 99.67% (299/300) | 100.00% (300/300) | 99.67% (299/300) |
| meal_grounding_ok | 92.98% (278/299) | 97.00% (291/300) | 97.32% (291/299) |
| meal_specific_ok | 100.00% (299/299) | 100.00% (300/300) | 100.00% (299/299) |
| meal_valid_semantics_ok | 95.32% (285/299) | 98.67% (296/300) | 99.00% (296/299) |
| meal_diversity_ok | 23.41% (70/299) | 85.33% (256/300) | 87.96% (263/299) |
| attraction_grounding_ok | 98.66% (295/299) | 98.33% (295/300) | 96.32% (288/299) |
| hotel_grounding_ok | 99.00% (296/299) | 99.67% (299/300) | 99.67% (298/299) |
| budget_user_constraint_ok | 89.97% (269/299) | 86.00% (258/300) | 87.29% (261/299) |
| budget_preference_aligned | 21.07% (63/299) | 68.67% (206/300) | 72.58% (217/299) |
| recomputed_budget_fit_ok | 40.47% (121/299) | 50.33% (151/300) | 53.85% (161/299) |
| budget_relationship_ok | 5.69% (17/299) | 42.67% (128/300) | 45.15% (135/299) |
| meal_cost_scale_ok | 38.80% (116/299) | 66.67% (200/300) | 68.56% (205/299) |
| latency_avg | 72.9262 | 94.8352 | 94.9581 |
| latency_p90 | 89.427 | 115.814 | 115.492 |
| output_chars_avg | 6727.1567 | 6971.87 | 6989.9 |

### failure types

**base**

```json
{
  "meal_budget_inconsistent": 299,
  "budget_relationship_mismatch": 282,
  "attraction_budget_inconsistent": 259,
  "budget_preference_mismatch": 236,
  "meal_repeat_too_many": 220,
  "hotel_budget_underestimated": 193,
  "meal_cost_scale_too_low": 183,
  "budget_arithmetic_inconsistent": 142,
  "attraction_repeat_too_many": 73,
  "meal_same_day_lunch_dinner_repeat": 62,
  "budget_hard_constraint_exceeded": 30,
  "accommodation_type_mismatch": 21,
  "meal_invalid_name": 14,
  "meal_grounding_miss": 7,
  "weather_mismatch": 1,
  "schema": 1
}
```

**legacy_b**

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 260,
  "budget_relationship_mismatch": 172,
  "budget_arithmetic_inconsistent": 117,
  "meal_cost_scale_too_low": 100,
  "budget_preference_mismatch": 94,
  "hotel_budget_underestimated": 82,
  "attraction_repeat_too_many": 59,
  "budget_hard_constraint_exceeded": 42,
  "meal_repeat_too_many": 33,
  "meal_same_day_lunch_dinner_repeat": 14,
  "meal_grounding_miss": 5,
  "meal_invalid_name": 4,
  "too_many_attractions": 4
}
```

**valloss_lr8e5**

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 253,
  "budget_relationship_mismatch": 164,
  "budget_arithmetic_inconsistent": 102,
  "meal_cost_scale_too_low": 94,
  "budget_preference_mismatch": 82,
  "hotel_budget_underestimated": 80,
  "attraction_repeat_too_many": 63,
  "budget_hard_constraint_exceeded": 38,
  "meal_repeat_too_many": 29,
  "meal_same_day_lunch_dinner_repeat": 10,
  "meal_grounding_miss": 5,
  "too_many_attractions": 4,
  "meal_invalid_name": 3,
  "json_extract": 1
}
```
