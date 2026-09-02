# V3 Standard200 四版本完整指标对比

- 评测集：`training/data/v3/eval/records.jsonl`
- 样本数：200
- 推理设置：vLLM，单卡单进程，`workers=10`
- 版本：base / sftv1 / v2a / v2b

## 生成完整性

| model | raw_generations | unique_generations |
| --- | ---: | ---: |
| base | 200 | 200 |
| sftv1 | 200 | 200 |
| v2a | 200 | 200 |
| v2b | 200 | 200 |

## Boolean Metrics

| metric | key | base | sftv1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| JSON 可解析 | `json_extract_ok` | 99.50% (199/200) | 100.00% (200/200) | 100.00% (200/200) | 100.00% (200/200) |
| Schema 通过 | `schema_ok` | 98.50% (197/200) | 99.50% (199/200) | 98.50% (197/200) | 99.50% (199/200) |
| SFT hard | `sft_hard_pass` | 87.31% (172/197) | 90.95% (181/199) | 94.92% (187/197) | 95.98% (191/199) |
| SFT no-budget-sum hard | `sft_no_budget_sum_hard_pass` | 87.31% (172/197) | 90.95% (181/199) | 94.92% (187/197) | 95.98% (191/199) |
| SFT budget semantic hard | `sft_budget_semantic_hard_pass` | 2.54% (5/197) | 13.57% (27/199) | 31.98% (63/197) | 32.16% (64/199) |
| SFT strict hard | `sft_strict_hard_pass` | 0.00% (0/197) | 0.00% (0/199) | 0.00% (0/197) | 0.50% (1/199) |
| DPO soft | `dpo_soft_pass` | 12.69% (25/197) | 46.23% (92/199) | 52.28% (103/197) | 55.28% (110/199) |
| DPO soft（重算预算） | `dpo_soft_recomputed_budget_pass` | 19.80% (39/197) | 37.19% (74/199) | 49.24% (97/197) | 44.22% (88/199) |
| Legacy hard | `legacy_hard_pass` | 11.17% (22/197) | 42.21% (84/199) | 52.28% (103/197) | 55.78% (111/199) |
| 城市正确 | `city_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 起止日期正确 | `date_range_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 天数正确 | `days_len_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 每日日期正确 | `day_dates_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| day_index 正确 | `day_index_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 天气日期正确 | `weather_dates_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 天气内容匹配 | `weather_match` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 住宿类型正确 | `accommodation_type_ok` | 97.46% (192/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 中间日酒店非空 | `middle_hotel_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 酒店 grounding | `hotel_grounding_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 酒店名合法 | `invalid_hotel_name_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 酒店距离不编造 | `hotel_distance_placeholder_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| location 对象格式 | `location_object_ok` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 三餐完整 | `meal_complete` | 98.98% (195/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 餐饮具体性 | `meal_specific_ok` | 97.46% (192/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| 餐饮语义有效 | `meal_valid_semantics_ok` | 93.40% (184/197) | 97.99% (195/199) | 97.46% (192/197) | 98.49% (196/199) |
| 餐饮 grounding | `meal_grounding_ok` | 91.37% (180/197) | 97.99% (195/199) | 97.46% (192/197) | 97.99% (195/199) |
| 同日午晚餐不重复 | `meal_lunch_dinner_same_day_ok` | 87.31% (172/197) | 91.96% (183/199) | 95.43% (188/197) | 97.49% (194/199) |
| 餐厅复用限制 | `meal_repeat_limit_ok` | 49.75% (98/197) | 81.41% (162/199) | 90.36% (178/197) | 87.94% (175/199) |
| 餐饮多样性 | `meal_diversity_ok` | 46.19% (91/197) | 76.88% (153/199) | 86.80% (171/197) | 86.43% (172/199) |
| 景点数量正确 | `attraction_count_ok` | 100.00% (197/197) | 96.48% (192/199) | 99.49% (196/197) | 98.99% (197/199) |
| 景点 grounding | `attraction_grounding_ok` | 98.98% (195/197) | 96.48% (192/199) | 97.97% (193/197) | 98.99% (197/199) |
| 景点复用限制 | `attraction_repeat_limit_ok` | 94.42% (186/197) | 81.91% (163/199) | 92.89% (183/197) | 90.95% (181/199) |
| 景点多样性 | `attraction_diversity_ok` | 94.42% (186/197) | 81.91% (163/199) | 92.89% (183/197) | 90.95% (181/199) |
| 预算选择贴合 | `budget_selection_ok` | 47.21% (93/197) | 60.80% (121/199) | 61.42% (121/197) | 62.31% (124/199) |
| 重算预算贴合 | `recomputed_budget_fit_ok` | 47.21% (93/197) | 60.80% (121/199) | 61.42% (121/197) | 62.31% (124/199) |
| 重算 hard 预算不超 | `recomputed_budget_hard_ok` | 98.48% (194/197) | 98.99% (197/199) | 98.48% (194/197) | 98.99% (197/199) |
| 重算用户预算约束 | `recomputed_budget_user_constraint_ok` | 98.48% (194/197) | 98.99% (197/199) | 98.48% (194/197) | 98.99% (197/199) |
| 重算不超用户预算 | `recomputed_budget_within_user_budget` | 95.94% (189/197) | 98.99% (197/199) | 98.48% (194/197) | 99.50% (198/199) |
| 重算预算档位贴合 | `recomputed_budget_level_aligned` | 47.21% (93/197) | 60.80% (121/199) | 61.42% (121/197) | 62.31% (124/199) |
| 重算预算偏好贴合 | `recomputed_budget_preference_aligned` | 47.21% (93/197) | 60.80% (121/199) | 61.42% (121/197) | 62.31% (124/199) |
| 模型预算加总正确 | `budget_arithmetic_consistent` | 58.88% (116/197) | 71.86% (143/199) | 74.62% (147/197) | 75.38% (150/199) |
| 模型预算一致 | `budget_consistent` | 58.88% (116/197) | 71.86% (143/199) | 74.62% (147/197) | 75.38% (150/199) |
| 预算语义关系 | `budget_relationship_ok` | 2.54% (5/197) | 15.08% (30/199) | 32.99% (65/197) | 34.17% (68/199) |
| 模型预算用户约束 | `budget_user_constraint_ok` | 98.48% (194/197) | 98.49% (196/199) | 98.98% (195/197) | 99.50% (198/199) |
| 模型预算不超用户预算 | `budget_within_user_budget` | 96.95% (191/197) | 99.50% (198/199) | 100.00% (197/197) | 97.99% (195/199) |
| 模型预算档位贴合 | `budget_level_aligned` | 25.38% (50/197) | 74.37% (148/199) | 64.97% (128/197) | 74.87% (149/199) |
| 模型预算偏好贴合 | `budget_preference_aligned` | 25.38% (50/197) | 74.37% (148/199) | 64.97% (128/197) | 74.87% (149/199) |
| 酒店预算关系 | `hotel_budget_relation_ok` | 45.69% (90/197) | 75.38% (150/199) | 82.74% (163/197) | 88.94% (177/199) |
| 酒店预算覆盖晚数 | `hotel_budget_covers_nights` | 44.16% (87/197) | 74.37% (148/199) | 82.23% (162/197) | 87.94% (175/199) |
| 门票人数关系 | `attraction_budget_party_relation_ok` | 27.92% (55/197) | 46.23% (92/199) | 77.66% (153/197) | 83.92% (167/199) |
| 门票预算一致 | `attraction_budget_consistent` | 13.71% (27/197) | 15.58% (31/199) | 27.41% (54/197) | 31.16% (62/199) |
| 餐饮预算一致 | `meal_budget_consistent` | 0.00% (0/197) | 0.50% (1/199) | 0.51% (1/197) | 0.50% (1/199) |
| 餐饮人均尺度 | `meal_cost_scale_ok` | 18.78% (37/197) | 47.74% (95/199) | 49.75% (98/197) | 45.23% (90/199) |
| 交通预算非负 | `transportation_budget_nonnegative` | 100.00% (197/197) | 100.00% (199/199) | 100.00% (197/197) | 100.00% (199/199) |
| hard_pass | `hard_pass` | 87.31% (172/197) | 90.95% (181/199) | 94.92% (187/197) | 95.98% (191/199) |

## Numeric Metrics

| metric | key | base | sftv1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| 景点唯一率 | `attraction_diversity_unique_rate` | avg 0.9908 / p50 1 / p90 1 | avg 0.9741 / p50 1 / p90 1 | avg 0.9919 / p50 1 / p90 1 | avg 0.9901 / p50 1 / p90 1 |
| 景点 grounding rate | `attraction_grounding_rate` | avg 0.9977 / p50 1 / p90 1 | avg 0.996 / p50 1 / p90 1 | avg 0.9978 / p50 1 / p90 1 | avg 0.9988 / p50 1 / p90 1 |
| 酒店 grounding rate | `hotel_grounding_rate` | avg 1 / p50 1 / p90 1 | avg 1 / p50 1 / p90 1 | avg 1 / p50 1 / p90 1 | avg 1 / p50 1 / p90 1 |
| 餐饮唯一率 | `meal_diversity_unique_rate` | avg 0.6675 / p50 0.6667 / p90 1 | avg 0.8368 / p50 0.875 / p90 1 | avg 0.8874 / p50 0.9167 / p90 1 | avg 0.9007 / p50 1 / p90 1 |
| 餐饮 food_pois grounding rate | `meal_food_pois_grounding_rate` | avg 0.9869 / p50 1 / p90 1 | avg 0.9981 / p50 1 / p90 1 | avg 0.9974 / p50 1 / p90 1 | avg 0.998 / p50 1 / p90 1 |
| 餐饮 grounding rate | `meal_grounding_rate` | avg 0.9869 / p50 1 / p90 1 | avg 0.9981 / p50 1 / p90 1 | avg 0.9974 / p50 1 / p90 1 | avg 0.998 / p50 1 / p90 1 |
| 餐饮语义有效率 | `meal_semantic_valid_rate` | avg 0.9909 / p50 1 / p90 1 | avg 0.9981 / p50 1 / p90 1 | avg 0.9974 / p50 1 / p90 1 | avg 0.9984 / p50 1 / p90 1 |
| 重算人均每天预算 | `recomputed_budget_per_person_day` | avg 497.6 / p50 458.7 / p90 713.2 | avg 513.8 / p50 463.4 / p90 754.8 | avg 544.6 / p50 478 / p90 849.8 | avg 551.7 / p50 470.7 / p90 856.5 |
| 重算总预算 | `recomputed_budget_total` | avg 4627 / p50 3974 / p90 8676 | avg 4944 / p50 4072 / p90 8858 | avg 5259 / p50 4308 / p90 9999 | avg 5423 / p50 4248 / p90 1.052e+04 |

## Latency / Output

| metric | base | sftv1 | v2a | v2b |
| --- | ---: | ---: | ---: | ---: |
| latency.avg | 63.16 | 81.46 | 80.56 | 80.21 |
| latency.p50 | 60.6 | 78.74 | 77.04 | 77.33 |
| latency.p90 | 81.78 | 109.1 | 109.4 | 108.5 |
| latency.p99 | 99.07 | 129.3 | 132.6 | 130.4 |
| output_chars.avg | 5836 | 5921 | 5893 | 5822 |
| output_chars.p50 | 5683 | 5723 | 5677 | 5578 |
| output_chars.p90 | 7451 | 7891 | 8116 | 7885 |

## Failure Stages

| stage | base | sftv1 | v2a | v2b |
| --- | ---: | ---: | ---: | ---: |
| `json_extract` | 1 | 0 | 0 | 0 |
| `rule` | 1222 | 901 | 775 | 752 |
| `schema` | 2 | 1 | 3 | 1 |

## Error Types

| error_type | base | sftv1 | v2a | v2b |
| --- | ---: | ---: | ---: | ---: |
| `accommodation_type_mismatch` | 5 | 0 | 0 | 0 |
| `attraction_budget_inconsistent` | 170 | 168 | 143 | 137 |
| `attraction_repeat_too_many` | 11 | 36 | 14 | 18 |
| `budget_arithmetic_inconsistent` | 81 | 56 | 50 | 49 |
| `budget_hard_constraint_exceeded` | 3 | 3 | 2 | 1 |
| `budget_preference_mismatch` | 147 | 51 | 69 | 50 |
| `budget_relationship_mismatch` | 192 | 169 | 132 | 131 |
| `hotel_budget_underestimated` | 110 | 51 | 35 | 24 |
| `json_extract` | 1 | 0 | 0 | 0 |
| `meal_budget_inconsistent` | 197 | 199 | 197 | 198 |
| `meal_cost_scale_too_low` | 160 | 104 | 99 | 109 |
| `meal_grounding_miss` | 4 | 0 | 0 | 1 |
| `meal_invalid_name` | 13 | 4 | 5 | 3 |
| `meal_placeholder` | 5 | 0 | 0 | 0 |
| `meal_repeat_too_many` | 99 | 37 | 19 | 24 |
| `meal_same_day_lunch_dinner_repeat` | 25 | 16 | 9 | 5 |
| `schema` | 2 | 1 | 3 | 1 |
| `too_many_attractions` | 0 | 7 | 1 | 2 |

## Report Paths

- base: `training/outputs/eval/base_qwen25_7b_standard200_w10/rule_eval_report.md`
- sftv1: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_standard200_w10/rule_eval_report.md`
- v2a: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_standard200_w10/rule_eval_report.md`
- v2b: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2b_standard200_w10/rule_eval_report.md`
