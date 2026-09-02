# V3 历史 Prompt 两层 Pass 对比

所有 full-run prompt 报告已用最新 `eval_rule_metrics.py` 重算。排序优先看 `dpo_soft_pass`，再看 `sft_hard_pass`。

| 版本 | 样本数 | sft_hard_pass | dpo_soft_pass | legacy_hard_pass | schema | 预算算术 | 餐饮语义合法 | 餐饮多样性 | 餐饮grounding | 预算偏好 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12 | 300 | 77.89% | 43.20% | 44.22% | 98.00% | 90.14% | 90.48% | 55.78% | 89.46% | 99.32% |
| base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12 | 300 | 80.87% | 39.93% | 41.61% | 99.33% | 90.94% | 92.28% | 50.34% | 90.60% | 97.32% |
| base_qwen25_7b_v3_harder_ablation_meal_count_limit_symbolic_w12 | 300 | 75.93% | 39.66% | 41.69% | 98.33% | 88.47% | 87.46% | 54.58% | 86.10% | 96.95% |
| base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16 | 300 | 75.34% | 38.85% | 40.54% | 98.67% | 88.51% | 88.51% | 52.70% | 87.16% | 97.64% |
| base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8 | 300 | 82.59% | 38.57% | 41.30% | 97.67% | 96.25% | 89.76% | 50.51% | 88.74% | 98.63% |
| base_qwen25_7b_v3_harder_no_route_meal_hotel_prompt_w8 | 300 | 57.04% | 33.33% | 39.18% | 97.00% | 96.22% | 62.20% | 74.23% | 58.42% | 96.22% |
| base_qwen25_7b_v3_harder_food_bucket_no_route_w8 | 300 | 53.72% | 26.01% | 28.04% | 98.67% | 94.93% | 60.81% | 62.84% | 60.81% | 97.64% |
| base_qwen25_7b_v3_harder_ablation_budget_symbolic_meal_semantic_w16 | 300 | 63.21% | 23.75% | 25.08% | 99.67% | 91.97% | 68.56% | 52.51% | 67.89% | 97.32% |
| base_qwen25_7b_v3_harder_meal_strict_prompt_w8 | 300 | 79.45% | 20.21% | 21.58% | 97.33% | 92.12% | 90.41% | 33.22% | 90.07% | 97.95% |
| base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun | 300 | 88.55% | 8.42% | 8.42% | 99.00% | 93.94% | 96.63% | 10.44% | 95.96% | 96.97% |
| base_qwen25_7b_v3_harder_ablation_budget_hard_w8 | 300 | 81.97% | 8.16% | 8.84% | 98.00% | 90.82% | 97.62% | 11.22% | 96.94% | 97.28% |
| base_qwen25_7b_v3_harder_ablation_budget_fewshot_w8 | 300 | 89.23% | 7.74% | 8.42% | 99.00% | 94.28% | 98.65% | 10.44% | 97.98% | 97.31% |
| base_qwen25_7b_v3_harder_ablation_budget_symbolic_w8 | 300 | 86.35% | 6.48% | 7.17% | 97.67% | 93.52% | 95.56% | 10.24% | 94.88% | 97.27% |
| base_qwen25_7b_v3_harder_ablation_budget_order_w8 | 300 | 83.28% | 5.46% | 5.80% | 97.67% | 91.81% | 95.22% | 10.24% | 94.88% | 97.61% |
| base_qwen25_7b_v3_harder_budget_prompt_w8 | 300 | 0.67% | 0.00% | 0.00% | 99.00% | 85.86% | 41.08% | 40.07% | 39.73% | 98.65% |
| base_qwen25_7b_v3_harder_no_route_w8 | 300 | 0.67% | 0.00% | 0.34% | 99.33% | 96.64% | 38.26% | 40.60% | 35.23% | 96.31% |
| base_qwen25_7b_v3_harder_no_route_w8_meal_hotel_strict | 300 | 0.67% | 0.00% | 0.34% | 99.33% | 96.64% | 38.26% | 40.60% | 35.23% | 96.31% |
| base_qwen25_7b_v3_harder_no_route_w8_meal_strict | 300 | 0.67% | 0.00% | 0.34% | 99.33% | 96.64% | 38.26% | 40.60% | 35.23% | 96.31% |
| base_qwen25_7b_v3_harder_budget_final_prompt_w8 | 300 | 0.34% | 0.00% | 0.34% | 99.00% | 93.94% | 40.74% | 40.74% | 39.39% | 97.64% |
| base_qwen25_7b_v3_harder_w8 | 300 | 0.00% | 0.00% | 0.00% | 97.33% | 93.49% | 40.07% | 40.41% | 38.01% | 98.63% |

## Top 5 by dpo_soft_pass

1. `base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12`: dpo=43.20%, sft=77.89%, legacy=44.22%
2. `base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12`: dpo=39.93%, sft=80.87%, legacy=41.61%
3. `base_qwen25_7b_v3_harder_ablation_meal_count_limit_symbolic_w12`: dpo=39.66%, sft=75.93%, legacy=41.69%
4. `base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16`: dpo=38.85%, sft=75.34%, legacy=40.54%
5. `base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8`: dpo=38.57%, sft=82.59%, legacy=41.30%
