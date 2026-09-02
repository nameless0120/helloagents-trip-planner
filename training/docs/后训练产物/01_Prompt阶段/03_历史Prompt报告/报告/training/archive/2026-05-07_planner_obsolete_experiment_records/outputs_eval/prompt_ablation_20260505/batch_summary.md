# Bigmodel Prompt Ablation 2026-05-05

重评口径：2026-05-05 修正后的 meal grounding 规则，只有 `type=breakfast` 的住宿早餐可豁免 `food_pois` grounding；午餐/晚餐必须命中 `food_pois`。本表基于既有 `generations.jsonl` 重新运行 rule eval，没有重新调用模型生成。

| variant | records | sft_hard_pass | sft_budget_semantic_hard_pass | dpo_soft_pass | budget_arithmetic_consistent | hotel_budget_covers_nights | meal_budget_consistent | meal_diversity_ok | meal_grounding_ok | meal_grounding_rate | latency_avg |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | 300 | 0.00% | 1.68% | 0.00% | 50.51% | 36.36% | 0.00% | 71.38% | 56.23% | 83.28% | 49.98 |
| A | 300 | 0.00% | 3.38% | 0.00% | 55.07% | 35.81% | 0.00% | 70.27% | 56.08% | 82.90% | 64.98 |
| B | 300 | 0.00% | 3.47% | 0.00% | 46.53% | 38.54% | 0.00% | 72.57% | 60.76% | 85.16% | 63.94 |
| C | 300 | 0.00% | 2.71% | 0.00% | 46.10% | 37.63% | 0.00% | 68.14% | 49.15% | 82.67% | 61.16 |
| D | 300 | 0.00% | 1.35% | 0.00% | 49.66% | 36.49% | 0.00% | 73.65% | 58.11% | 84.09% | 64.16 |
| A_C | 300 | 0.00% | 3.36% | 0.00% | 58.72% | 40.27% | 0.34% | 66.11% | 52.68% | 82.95% | 61.35 |
| A_D | 300 | 0.00% | 1.67% | 0.00% | 49.67% | 36.00% | 0.33% | 71.67% | 59.33% | 83.65% | 64.36 |
| B_C | 300 | 0.00% | 4.35% | 0.00% | 46.96% | 42.17% | 0.00% | 60.00% | 59.57% | 87.38% | 60.75 |
| B_D | 300 | 0.00% | 3.36% | 0.00% | 48.32% | 37.92% | 0.00% | 74.83% | 58.72% | 83.99% | 63.67 |
| C_D | 300 | 0.00% | 1.67% | 0.00% | 45.00% | 37.00% | 0.00% | 71.00% | 51.00% | 82.88% | 59.89 |
| A_C_D | 300 | 0.00% | 4.01% | 0.00% | 54.18% | 38.13% | 0.00% | 68.90% | 56.19% | 83.21% | 60.85 |
| B_C_D | 300 | 0.00% | 1.77% | 0.00% | 45.23% | 36.40% | 0.00% | 66.43% | 51.59% | 82.96% | 59.92 |

## Metric Notes

- `variant`: Prompt 消融版本名；baseline 是当前原始 prompt，A/B/C/D 是对应重点块，组合用下划线连接。
- `records`: 本组纳入 rule eval 汇总的样本数，通常是 300。schema 失败样本不会进入部分 schema 后规则指标的分母。
- `sft_hard_pass`: SFT 硬约束全通过率；包含 JSON/schema、城市日期、天气、住宿、三餐、景点、POI grounding、预算算术和用户预算等硬规则。
- `sft_budget_semantic_hard_pass`: 去掉部分精确预算算术后、更偏语义约束的硬通过率；仍检查住宿/餐饮/景点/天气等硬规则，并用 budget_relationship_ok 检查预算关系。
- `dpo_soft_pass`: 先通过 sft_hard_pass，再通过软质量项的比例；软质量项包括景点多样性、餐饮多样性、餐饮 grounding 和预算偏好贴合。
- `budget_arithmetic_consistent`: budget.total 是否严格等于 total_attractions + total_hotels + total_meals + total_transportation。
- `hotel_budget_covers_nights`: 酒店预算是否覆盖所有非 null day.hotel 对应的住宿晚数和房间数估算。
- `meal_budget_consistent`: budget.total_meals 是否等于所有 meal.estimated_cost 之和乘以同行人数。
- `meal_diversity_ok`: 餐饮多样性是否通过；要求同一天午晚餐不重复，并满足全程餐厅复用上限。
- `meal_grounding_ok`: 样本级全通过指标：整条行程所有餐饮名称都必须命中 food_pois；只有 type=breakfast 的酒店/民宿/客栈/住宿早餐可豁免。任意一餐 miss，整条样本失败。
- `meal_grounding_rate`: 餐次级命中率：所有 meal 中命中 food_pois 或合法住宿早餐的比例，用来辅助理解 meal_grounding_ok 的严格性。
- `latency_avg`: 本组生成平均耗时，单位秒；来自原 generations 的 latency_seconds。
