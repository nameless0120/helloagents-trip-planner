# 260511 Usage700 Follow-up Mainline Comparison

对比对象：`base`、`v2b`、上一主线 `prev_lr8e5`，以及本轮两版新模型 `replay_usage700_lr2e5` / `patch700_only_lr1e5`。standard 使用 `training/data/v3/eval/records.jsonl`，hard 使用 `training/data/v3/eval_hard/records.jsonl`；两个 split 都是 `260511_high_end_context_*_w10` 同口径。

## Model Roles

| 标签 | 角色 |
| --- | --- |
| `base` | 原始 Qwen2.5-7B-Instruct 基线 |
| `v2b` | 旧数据路线历史强对照，仅作 reference |
| `prev_lr8e5` | 上一版当前主线 / valloss lr8e-5 |
| `replay_usage700_lr2e5` | 最新 A：main_clean + realbudget usage700 replay，from lr6e-5, continue lr2e-5 |
| `patch700_only_lr1e5` | 最新 B：realbudget usage700 patch-only，from lr6e-5, lr1e-5 |

## Standard Core

| 指标 | base | v2b | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Hard Pass | 89.90% (178/198) | 93.47% (186/199) | 96.46% (191/198) | 95.50% (191/200) | 97.50% (195/200) |
| Soft Pass | 5.56% (11/198) | 55.28% (110/199) | 61.11% (121/198) | 61.00% (122/200) | 34.50% (69/200) |
| Soft Pass（重算预算） | 13.13% (26/198) | 42.71% (85/199) | 45.45% (90/198) | 50.50% (101/200) | 30.50% (61/200) |
| 重算预算贴合 | 43.94% (87/198) | 57.29% (114/199) | 57.07% (113/198) | 62.00% (124/200) | 39.50% (79/200) |
| 预算偏好对齐 | 18.18% (36/198) | 75.88% (151/199) | 77.27% (153/198) | 79.00% (158/200) | 45.00% (90/200) |
| 预算结构关系合理 | 6.06% (12/198) | 52.76% (105/199) | 56.57% (112/198) | 81.00% (162/200) | 53.50% (107/200) |
| 餐饮价格尺度合理 | 35.35% (70/198) | 68.34% (136/199) | 73.23% (145/198) | 83.00% (166/200) | 60.50% (121/200) |
| 餐饮多样性 | 30.81% (61/198) | 83.92% (167/199) | 88.38% (175/198) | 87.50% (175/200) | 82.50% (165/200) |
| 景点多样性 | 90.91% (180/198) | 91.46% (182/199) | 91.92% (182/198) | 94.00% (188/200) | 91.50% (183/200) |
| 餐饮 Grounding | 94.95% (188/198) | 98.99% (197/199) | 98.48% (195/198) | 98.00% (196/200) | 98.50% (197/200) |

## Hard Core

| 指标 | base | v2b | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Hard Pass | 83.28% (249/299) | 93.67% (281/300) | 91.97% (275/299) | 97.32% (291/299) | 98.33% (294/299) |
| Soft Pass | 3.34% (10/299) | 43.00% (129/300) | 46.15% (138/299) | 52.51% (157/299) | 35.79% (107/299) |
| Soft Pass（重算预算） | 3.34% (10/299) | 31.00% (93/300) | 35.12% (105/299) | 34.78% (104/299) | 29.77% (89/299) |
| 重算预算贴合 | 40.47% (121/299) | 50.33% (151/300) | 53.85% (161/299) | 48.83% (146/299) | 47.83% (143/299) |
| 预算偏好对齐 | 21.07% (63/299) | 68.67% (206/300) | 72.58% (217/299) | 72.58% (217/299) | 57.86% (173/299) |
| 预算结构关系合理 | 5.69% (17/299) | 42.67% (128/300) | 45.15% (135/299) | 67.22% (201/299) | 57.86% (173/299) |
| 餐饮价格尺度合理 | 38.80% (116/299) | 66.67% (200/300) | 68.56% (205/299) | 79.60% (238/299) | 66.22% (198/299) |
| 餐饮多样性 | 23.41% (70/299) | 85.33% (256/300) | 87.96% (263/299) | 83.28% (249/299) | 80.27% (240/299) |
| 景点多样性 | 75.59% (226/299) | 80.33% (241/300) | 78.93% (236/299) | 82.94% (248/299) | 81.61% (244/299) |
| 餐饮 Grounding | 92.98% (278/299) | 97.00% (291/300) | 97.32% (291/299) | 99.00% (296/299) | 99.33% (297/299) |

## Delta Vs Previous Mainline

### standard

| 指标 | replay vs prev | patch-only vs prev |
| --- | ---: | ---: |
| Hard Pass | -0.96pp | +1.04pp |
| Soft Pass | -0.11pp | -26.61pp |
| Soft Pass（重算预算） | +5.05pp | -14.95pp |
| 重算预算贴合 | +4.93pp | -17.57pp |
| 预算偏好对齐 | +1.73pp | -32.27pp |
| 预算结构关系合理 | +24.43pp | -3.07pp |
| 餐饮价格尺度合理 | +9.77pp | -12.73pp |
| 餐饮多样性 | -0.88pp | -5.88pp |
| 景点多样性 | +2.08pp | -0.42pp |
| 餐饮 Grounding | -0.48pp | +0.02pp |

### hard

| 指标 | replay vs prev | patch-only vs prev |
| --- | ---: | ---: |
| Hard Pass | +5.35pp | +6.36pp |
| Soft Pass | +6.36pp | -10.36pp |
| Soft Pass（重算预算） | -0.34pp | -5.35pp |
| 重算预算贴合 | -5.02pp | -6.02pp |
| 预算偏好对齐 | +0.00pp | -14.72pp |
| 预算结构关系合理 | +22.07pp | +12.71pp |
| 餐饮价格尺度合理 | +11.04pp | -2.34pp |
| 餐饮多样性 | -4.68pp | -7.69pp |
| 景点多样性 | +4.01pp | +2.68pp |
| 餐饮 Grounding | +1.68pp | +2.01pp |

## Budget Detail

### standard

| 指标 | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: |
| 预算硬约束不超支 | 98.99% (196/198) | 100.00% (200/200) | 98.50% (197/200) |
| 预算偏好对齐 | 77.27% (153/198) | 79.00% (158/200) | 45.00% (90/200) |
| 重算预算贴合 | 57.07% (113/198) | 62.00% (124/200) | 39.50% (79/200) |
| 重算预算不超用户预算 | 95.45% (189/198) | 92.00% (184/200) | 96.00% (192/200) |
| 预算结构关系合理 | 56.57% (112/198) | 81.00% (162/200) | 53.50% (107/200) |
| 酒店预算关系合理 | 86.36% (171/198) | 99.00% (198/200) | 94.00% (188/200) |
| 景点预算人数关系合理 | 86.87% (172/198) | 99.00% (198/200) | 96.00% (192/200) |
| 餐饮价格尺度合理 | 73.23% (145/198) | 83.00% (166/200) | 60.50% (121/200) |
| 报告预算加总一致 | 76.26% (151/198) | 63.50% (127/200) | 83.00% (166/200) |
| 景点预算精确一致 | 32.32% (64/198) | 33.00% (66/200) | 51.50% (103/200) |
| 餐饮预算精确一致 | 0.00% (0/198) | 1.00% (2/200) | 0.50% (1/200) |
| 酒店预算覆盖住宿夜数 | 82.32% (163/198) | 97.50% (195/200) | 93.50% (187/200) |

### hard

| 指标 | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: |
| 预算硬约束不超支 | 87.29% (261/299) | 90.30% (270/299) | 81.27% (243/299) |
| 预算偏好对齐 | 72.58% (217/299) | 72.58% (217/299) | 57.86% (173/299) |
| 重算预算贴合 | 53.85% (161/299) | 48.83% (146/299) | 47.83% (143/299) |
| 重算预算不超用户预算 | 84.95% (254/299) | 83.28% (249/299) | 90.97% (272/299) |
| 预算结构关系合理 | 45.15% (135/299) | 67.22% (201/299) | 57.86% (173/299) |
| 酒店预算关系合理 | 74.58% (223/299) | 90.97% (272/299) | 89.97% (269/299) |
| 景点预算人数关系合理 | 81.61% (244/299) | 92.64% (277/299) | 93.65% (280/299) |
| 餐饮价格尺度合理 | 68.56% (205/299) | 79.60% (238/299) | 66.22% (198/299) |
| 报告预算加总一致 | 65.89% (197/299) | 63.88% (191/299) | 80.60% (241/299) |
| 景点预算精确一致 | 15.38% (46/299) | 26.09% (78/299) | 34.11% (102/299) |
| 餐饮预算精确一致 | 0.00% (0/299) | 0.33% (1/299) | 0.67% (2/299) |
| 酒店预算覆盖住宿夜数 | 73.24% (219/299) | 89.63% (268/299) | 87.96% (263/299) |

## Protocol And Grounding

### standard

| 指标 | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: |
| JSON 抽取 | 100.00% (200/200) | 100.00% (200/200) | 100.00% (200/200) |
| Schema | 99.00% (198/200) | 100.00% (200/200) | 100.00% (200/200) |
| 住宿类型正确 | 100.00% (198/198) | 100.00% (200/200) | 100.00% (200/200) |
| 天气匹配上下文 | 100.00% (198/198) | 99.50% (199/200) | 99.50% (199/200) |
| 餐饮 Grounding | 98.48% (195/198) | 98.00% (196/200) | 98.50% (197/200) |
| 餐饮语义有效 | 99.49% (197/198) | 98.50% (197/200) | 99.00% (198/200) |
| 景点 Grounding | 98.99% (196/198) | 99.00% (198/200) | 100.00% (200/200) |
| 酒店 Grounding | 100.00% (198/198) | 100.00% (200/200) | 100.00% (200/200) |

### hard

| 指标 | prev_lr8e5 | replay_usage700_lr2e5 | patch700_only_lr1e5 |
| --- | ---: | ---: | ---: |
| JSON 抽取 | 99.67% (299/300) | 100.00% (300/300) | 100.00% (300/300) |
| Schema | 99.67% (299/300) | 99.67% (299/300) | 99.67% (299/300) |
| 住宿类型正确 | 100.00% (299/299) | 100.00% (299/299) | 100.00% (299/299) |
| 天气匹配上下文 | 100.00% (299/299) | 99.67% (298/299) | 99.33% (297/299) |
| 餐饮 Grounding | 97.32% (291/299) | 99.00% (296/299) | 99.33% (297/299) |
| 餐饮语义有效 | 99.00% (296/299) | 99.33% (297/299) | 100.00% (299/299) |
| 景点 Grounding | 96.32% (288/299) | 99.00% (296/299) | 99.67% (298/299) |
| 酒店 Grounding | 99.67% (298/299) | 100.00% (299/299) | 100.00% (299/299) |

## Generation Health

### standard

| 模型 | records | raw/unique | call fail | length 截断 | schema | latency avg/p90 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| base | training/data/v3/eval/records.jsonl | 200/200 | 0 | 0 | 99.00% (198/200) | 63.31s / 83.24s |
| v2b | training/data/v3/eval/records.jsonl | 200/200 | 0 | 0 | 99.50% (199/200) | 79.15s / 108.42s |
| prev_lr8e5 | training/data/v3/eval/records.jsonl | 200/200 | 0 | 0 | 99.00% (198/200) | 79.22s / 108.59s |
| replay_usage700_lr2e5 | training/data/v3/eval/records.jsonl | 200/200 | 0 | 0 | 100.00% (200/200) | 79.13s / 107.59s |
| patch700_only_lr1e5 | training/data/v3/eval/records.jsonl | 200/200 | 0 | 0 | 100.00% (200/200) | 72.08s / 97.36s |

### hard

| 模型 | records | raw/unique | call fail | length 截断 | schema | latency avg/p90 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| base | training/data/v3/eval_hard/records.jsonl | 300/300 | 0 | 0 | 99.67% (299/300) | 72.93s / 89.43s |
| v2b | training/data/v3/eval_hard/records.jsonl | 300/300 | 0 | 0 | 100.00% (300/300) | 94.84s / 115.81s |
| prev_lr8e5 | training/data/v3/eval_hard/records.jsonl | 300/300 | 0 | 0 | 99.67% (299/300) | 94.96s / 115.49s |
| replay_usage700_lr2e5 | training/data/v3/eval_hard/records.jsonl | 300/300 | 0 | 0 | 99.67% (299/300) | 92.98s / 114.61s |
| patch700_only_lr1e5 | training/data/v3/eval_hard/records.jsonl | 300/300 | 0 | 0 | 99.67% (299/300) | 86.29s / 104.95s |

## Top Error Types

| split | model | top errors |
| --- | --- | --- |
| standard | `prev_lr8e5` | meal_budget_inconsistent=198；attraction_budget_inconsistent=134；budget_relationship_mismatch=86；meal_cost_scale_too_low=53；budget_arithmetic_inconsistent=47；budget_preference_mismatch=45；hotel_budget_underestimated=35；meal_repeat_too_many=17 |
| standard | `replay_usage700_lr2e5` | meal_budget_inconsistent=198；attraction_budget_inconsistent=134；budget_arithmetic_inconsistent=73；budget_preference_mismatch=42；budget_relationship_mismatch=38；meal_cost_scale_too_low=34；meal_repeat_too_many=20；attraction_repeat_too_many=12 |
| standard | `patch700_only_lr1e5` | meal_budget_inconsistent=199；budget_preference_mismatch=110；attraction_budget_inconsistent=97；budget_relationship_mismatch=93；meal_cost_scale_too_low=79；budget_arithmetic_inconsistent=34；meal_repeat_too_many=27；attraction_repeat_too_many=17 |
| hard | `prev_lr8e5` | meal_budget_inconsistent=299；attraction_budget_inconsistent=253；budget_relationship_mismatch=164；budget_arithmetic_inconsistent=102；meal_cost_scale_too_low=94；budget_preference_mismatch=82；hotel_budget_underestimated=80；attraction_repeat_too_many=63 |
| hard | `replay_usage700_lr2e5` | meal_budget_inconsistent=298；attraction_budget_inconsistent=221；budget_arithmetic_inconsistent=108；budget_relationship_mismatch=98；budget_preference_mismatch=82；meal_cost_scale_too_low=61；attraction_repeat_too_many=51；meal_repeat_too_many=39 |
| hard | `patch700_only_lr1e5` | meal_budget_inconsistent=297；attraction_budget_inconsistent=197；budget_preference_mismatch=126；budget_relationship_mismatch=126；meal_cost_scale_too_low=101；budget_arithmetic_inconsistent=58；budget_hard_constraint_exceeded=56；attraction_repeat_too_many=55 |
