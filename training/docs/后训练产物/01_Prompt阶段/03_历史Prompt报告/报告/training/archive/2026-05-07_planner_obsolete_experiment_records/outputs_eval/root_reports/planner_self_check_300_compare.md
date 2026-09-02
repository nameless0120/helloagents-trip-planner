# Self Check Prompt 300 条重跑对比

对比对象：当前推荐 baseline `hard_compact` vs `room_person_price_self_check` 300 条全量重跑。

| 指标 | baseline_hard_compact | self_check_300 | 变化 |
| --- | --- | --- | --- |
| schema_ok | 98.7% | 97.7% | -1.0pp |
| sft_strict | 0.0% | 0.0% | +0.0pp |
| sft_semantic | 4.4% | 4.8% | +0.4pp |
| budget_rel | 6.8% | 8.2% | +1.4pp |
| hotel_rel | 39.5% | 42.3% | +2.8pp |
| attraction_rel | 28.0% | 30.0% | +2.0pp |
| meal_scale | 87.2% | 79.5% | -7.6pp |
| budget_user | 81.4% | 78.8% | -2.6pp |
| budget_arith | 69.6% | 56.3% | -13.3pp |
| accommodation_type | 90.5% | 85.3% | -5.2pp |
| attr_ground | 97.3% | 97.3% | -0.0pp |
| hotel_ground | 99.7% | 99.7% | +0.0pp |
| meal_ground | 96.6% | 91.8% | -4.8pp |
| meal_semantic | 97.3% | 92.8% | -4.5pp |
| meal_specific | 100.0% | 99.7% | -0.3pp |
| meal_diversity | 6.8% | 22.2% | +15.4pp |
| same_day_meal_ok | 55.1% | 67.9% | +12.9pp |

## 延迟与输出长度

| 版本 | avg latency | p90 latency | avg output chars | p90 output chars |
| --- | --- | --- | --- | --- |
| baseline_hard_compact | 60.8535 | 75.315 | 7142.2233 | 8727.0 |
| self_check_300 | 31.367 | 39.338 | 7234.6033 | 8892.0 |

## 结论

- self_check 让 `budget_relationship_ok` 从 6.8% 到 8.2%，`hotel_budget_relation_ok` 从 39.5% 到 42.3%，`attraction_budget_party_relation_ok` 从 28.0% 到 30.0%，属于小幅改善。
- 但它明显拉低了 `meal_grounding_ok`、`meal_cost_scale_ok`、`budget_arithmetic_consistent` 和 `accommodation_type_ok`，整体不适合替换当前 baseline。
- 餐饮多样性从 6.8% 到 22.2% 是亮点，但这是 DPO/软质量项，不应该压过 SFT 阶段的 grounding 和预算语义稳定性。
- 结论：baseline 仍建议用 `hard_compact`；self_check 可以作为 SFT 数据 prompt 的候选规则来源，但不要直接定为 baseline。

## 报告路径

- baseline: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_w10_room_person_eval/rule_eval_report.md`
- self_check: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_room_person_price_self_check_w10/rule_eval_report.md`
