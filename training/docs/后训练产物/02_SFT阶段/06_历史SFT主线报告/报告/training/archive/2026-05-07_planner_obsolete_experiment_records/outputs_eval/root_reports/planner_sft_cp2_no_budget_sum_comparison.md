# V3 SFT CP2 预算加和口径对比

日期：2026-05-06

## 对比对象

同一批 frozen eval：

`training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`

对比两组模型输出：

- Base A_C：`training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- SFT CP2：`training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`

本次只重跑 rule eval，不重新调用模型。

## 报告路径

| 版本 | 口径 | 报告 |
| --- | --- | --- |
| Base A_C | strict 原口径 | `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/rule_eval_report.md` |
| SFT CP2 | strict 原口径 | `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/rule_eval_report.md` |
| Base A_C | 去预算加和口径 | `training/outputs/eval/base_qwen25_7b_prompt_ablation_20260505_A_C_no_budget_sum/rule_eval_report.md` |
| SFT CP2 | 去预算加和口径 | `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8_no_budget_sum/rule_eval_report.md` |

## Pass 指标

| 指标 | Base A_C strict | SFT CP2 strict | Base A_C no-budget-sum | SFT CP2 no-budget-sum | SFT 相对 Base 提升 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `sft_strict_hard_pass` / 原 `sft_hard_pass` | 0.00% | 0.00% | 0.00% | 0.00% | 0.00pp |
| `sft_no_budget_sum_hard_pass` / 新 `sft_hard_pass` | - | - | 48.66% | 70.81% | +22.15pp |
| `dpo_soft_pass` | 0.00% | 0.00% | 6.04% | 21.48% | +15.44pp |
| `legacy_hard_pass` | 6.71% | 20.13% | 6.71% | 20.13% | +13.42pp |
| `sft_budget_semantic_hard_pass` | 3.36% | 6.38% | 3.36% | 6.38% | +3.02pp |

结论：严格账本口径下两者都被预算精确计算打成 0；去掉预算加和一票否决后，SFT 的协议执行收益变得清楚。

## SFT 硬协议指标

| 指标 | Base A_C | SFT CP2 | 变化 |
| --- | ---: | ---: | ---: |
| `json_extract_ok` | 100.00% | 100.00% | 0.00pp |
| `schema_ok` | 99.33% | 99.33% | 0.00pp |
| `city_ok` | 100.00% | 100.00% | 0.00pp |
| `date_range_ok` | 100.00% | 100.00% | 0.00pp |
| `days_len_ok` | 100.00% | 100.00% | 0.00pp |
| `day_dates_ok` | 100.00% | 100.00% | 0.00pp |
| `day_index_ok` | 100.00% | 100.00% | 0.00pp |
| `weather_match` | 99.66% | 98.99% | -0.67pp |
| `accommodation_type_ok` | 82.89% | 100.00% | +17.11pp |
| `middle_hotel_ok` | 100.00% | 100.00% | 0.00pp |
| `hotel_grounding_ok` | 98.66% | 100.00% | +1.34pp |
| `hotel_distance_placeholder_ok` | 100.00% | 100.00% | 0.00pp |
| `meal_complete` | 100.00% | 100.00% | 0.00pp |
| `meal_specific_ok` | 95.97% | 97.99% | +2.02pp |
| `meal_valid_semantics_ok` | 57.38% | 77.52% | +20.14pp |
| `meal_grounding_ok` | 52.68% | 70.13% | +17.45pp |
| `meal_diversity_ok` | 66.11% | 74.83% | +8.72pp |
| `attraction_count_ok` | 100.00% | 97.99% | -2.01pp |
| `attraction_grounding_ok` | 99.33% | 93.96% | -5.37pp |
| `attraction_diversity_ok` | 88.93% | 70.13% | -18.80pp |
| `transportation_budget_nonnegative` | 100.00% | 100.00% | 0.00pp |

## 预算诊断指标

预算诊断指标不进入当前 `sft_hard_pass` 一票否决，但继续保留，用于观察模型原生计算能力。

| 指标 | Base A_C | SFT CP2 | 变化 |
| --- | ---: | ---: | ---: |
| `budget_arithmetic_consistent` | 58.72% | 74.16% | +15.44pp |
| `hotel_budget_covers_nights` | 40.27% | 53.69% | +13.42pp |
| `hotel_budget_relation_ok` | 44.30% | 54.36% | +10.06pp |
| `attraction_budget_consistent` | 12.42% | 11.41% | -1.01pp |
| `attraction_budget_party_relation_ok` | 27.85% | 39.93% | +12.08pp |
| `meal_budget_consistent` | 0.34% | 0.00% | -0.34pp |
| `meal_cost_scale_ok` | 66.78% | 77.18% | +10.40pp |
| `budget_relationship_ok` | 8.05% | 13.76% | +5.71pp |
| `budget_user_constraint_ok` | 82.21% | 77.18% | -5.03pp |
| `budget_preference_aligned` | 34.56% | 57.05% | +22.49pp |

## 结论

1. SFT CP2 对格式和协议是有效的：在去预算加和口径下，`sft_hard_pass` 从 Base 的 48.66% 提升到 70.81%。
2. SFT 最大收益来自住宿类型、餐饮语义、餐饮 grounding、餐饮多样性和酒店 grounding。
3. 严格预算账本仍然不是 7B 模型稳定能力：`meal_budget_consistent` 基本为 0，`attraction_budget_consistent` 也没有提升。
4. 预算加和应保留为诊断项，最终线上输出建议通过工程后处理重算。
5. 当前 SFT 的下一步风险不是 JSON/schema，而是餐饮 grounding 仍只有 70.13%，以及景点 grounding / 景点重复相比 base 有回退。

## 后续建议

- 当前 SFT 阶段主看 `sft_no_budget_sum_hard_pass`、schema、POI grounding、住宿连续性、三餐完整。
- 预算精确账本进入后处理，不继续作为 SFT 第一阶段主验收项。
- 下一轮数据或训练若要补强，应优先补餐饮 grounding、景点类型边界和景点重复，而不是继续让模型硬算总账。
