# V3 Prompt 预算消融汇总

## 核心指标

| Run | Total | hard_pass | json_extract_ok | schema_ok | meal_complete | meal_specific_ok | meal_grounding_ok | budget_arithmetic_consistent | hotel_budget_covers_nights | budget_preference_aligned | weather_match |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| return_dinner_old | 300 | 84.98% (249/293) | 99.67% (299/300) | 97.67% (293/300) | 99.66% (292/293) | 100.00% (293/293) | 88.74% (260/293) | 96.25% (282/293) | 100.00% (293/293) | 98.63% (289/293) | 100.00% (293/293) |
| meal_strict_old | 300 | 81.16% (237/292) | 100.00% (300/300) | 97.33% (292/300) | 97.95% (286/292) | 100.00% (292/292) | 90.07% (263/292) | 92.12% (269/292) | 99.66% (291/292) | 97.95% (286/292) | 100.00% (292/292) |
| budget_hard | 300 | 84.01% (247/294) | 100.00% (300/300) | 98.00% (294/300) | 96.26% (283/294) | 100.00% (294/294) | 96.94% (285/294) | 90.82% (267/294) | 100.00% (294/294) | 97.28% (286/294) | 99.66% (293/294) |
| budget_order | 300 | 84.30% (247/293) | 100.00% (300/300) | 97.67% (293/300) | 97.27% (285/293) | 100.00% (293/293) | 94.88% (278/293) | 91.81% (269/293) | 100.00% (293/293) | 97.61% (286/293) | 99.66% (292/293) |
| budget_fewshot | 300 | 88.89% (264/297) | 100.00% (300/300) | 99.00% (297/300) | 97.31% (289/297) | 100.00% (297/297) | 97.98% (291/297) | 94.28% (280/297) | 99.33% (295/297) | 97.31% (289/297) | 99.66% (296/297) |
| budget_symbolic | 300 | 87.37% (256/293) | 99.67% (299/300) | 97.67% (293/300) | 98.98% (290/293) | 100.00% (293/293) | 94.88% (278/293) | 93.52% (274/293) | 100.00% (293/293) | 97.27% (285/293) | 100.00% (293/293) |

## 主要错误数

| Run | budget_arithmetic_inconsistent | meal_grounding_miss | schema | json_extract | middle_hotel_null | hotel_budget_underestimated | budget_preference_mismatch |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| return_dinner_old | 11 | 33 | 6 | 1 | 0 | 0 | 4 |
| meal_strict_old | 23 | 29 | 8 | 0 | 0 | 1 | 6 |
| budget_hard | 27 | 9 | 6 | 0 | 1 | 0 | 8 |
| budget_order | 24 | 15 | 7 | 0 | 2 | 0 | 7 |
| budget_fewshot | 17 | 6 | 3 | 0 | 2 | 2 | 8 |
| budget_symbolic | 19 | 15 | 6 | 1 | 1 | 0 | 8 |

## 延迟和输出长度

| Run | latency_avg | output_chars_avg | output_chars_p90 |
| --- | ---: | ---: | ---: |
| return_dinner_old | 57.64s | 7123 | 8565 |
| meal_strict_old | 54.99s | 6939 | 8560 |
| budget_hard | 56.55s | 7060 | 8621 |
| budget_order | 56.65s | 7069 | 8714 |
| budget_fewshot | 56.36s | 6981 | 8635 |
| budget_symbolic | 55.54s | 6900 | 8341 |

## 示例数字污染检查

数字 few-shot 使用过 800/200/520/180/1700；symbolic 版本没有这些数字，但仍统计这些值的自然出现频率作为污染对照。

| Run | total_hotels=800 | total_attractions=200 | total_meals=520 | total_transportation=180 | total=1700 | 同条命中>=2 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| budget_hard | 2 | 0 | 0 | 0 | 0 | 0 |
| budget_order | 0 | 0 | 0 | 0 | 0 | 0 |
| budget_fewshot | 10 | 23 | 21 | 23 | 1 | 13 |
| budget_symbolic | 2 | 1 | 0 | 0 | 1 | 0 |
| return_dinner_old | 5 | 5 | 0 | 0 | 1 | 0 |

## 结论

- `budget_fewshot` 的规则指标最高，但存在明显示例数字污染，不能直接合入线上 prompt。
- `budget_symbolic` 去掉具体数字后，污染信号消失，预算算术正确率 93.52%，优于 `budget_hard`/`budget_order`，但低于数字 few-shot。
- `budget_symbolic` 的 hard_pass 87.37%，低于数字 few-shot 的 88.89%，但高于 `budget_hard`/`budget_order` 和旧 baseline；更适合作为线上 prompt 候选。
- symbolic 版本餐饮 grounding 为 94.88%，低于 `budget_hard` 的 96.94% 和数字 few-shot 的 97.98%，需要看失败样本是否可以再通过餐饮模块或 prompt 微调修复。
