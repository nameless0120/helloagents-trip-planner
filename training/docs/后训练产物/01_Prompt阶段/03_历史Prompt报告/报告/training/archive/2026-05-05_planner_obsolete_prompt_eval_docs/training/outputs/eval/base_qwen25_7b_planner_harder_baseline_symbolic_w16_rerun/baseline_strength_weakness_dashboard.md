# V3 Baseline Dashboard：symbolic prompt rerun


<img src="baseline_strength_weakness_dashboard.svg" alt="V3 symbolic baseline dashboard" width="100%" />

## 关键结论

- 这版作为 baseline 是合理的：hard_pass = **89.56% (266/297)**。
- 餐饮严格 food_pois 命中 = **95.96% (285/297)**；按“上海城隍庙小吃可接受、酒店晚餐/无/住宿名不可接受”的语义口径，餐饮有效 = **96.63% (287/297)**。
- 主要短板仍是预算算术：budget_arithmetic_consistent = **93.94% (279/297)**。
- 新的 meal semantic prompt 不适合合入；它会诱导模型大量写“无/酒店晚餐/非餐饮”。当前 baseline 应继续使用上一版 symbolic prompt。

## 指标表

| 指标 | 通过 | 总数 | 比例 |
| --- | ---: | ---: | ---: |
| Hard Pass | 266 | 297 | 89.56% |
| JSON/Schema | 297 | 300 | 99.00% |
| 餐饮语义有效 | 287 | 297 | 96.63% |
| 餐饮候选命中 | 285 | 297 | 95.96% |
| 预算算术 | 279 | 297 | 93.94% |
| 预算偏好 | 288 | 297 | 96.97% |
| 天气匹配 | 297 | 297 | 100.00% |
| 景点数量 | 297 | 297 | 100.00% |
| 酒店住宿晚数预算 | 297 | 297 | 100.00% |
| 中间天酒店非空 | 296 | 297 | 99.66% |
| 餐饮完整 | 292 | 297 | 98.32% |

## 主要错误类型

| 错误类型 | 次数 |
| --- | ---: |
| budget_arithmetic_inconsistent | 18 |
| meal_invalid_name | 10 |
| budget_preference_mismatch | 9 |
| schema | 3 |
| meal_grounding_miss | 2 |
| middle_hotel_null | 1 |

## 文件

- 规则报告：`training/outputs/eval/base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun/rule_eval_report.md`
- 生成结果：`training/outputs/eval/base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun/generations.jsonl`
- LLM judge dashboard：未跑，需要确认允许把 eval records 和模型输出发给外部强模型。
