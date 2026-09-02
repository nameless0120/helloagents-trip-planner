# V3 SFT 预算贴合审计

- records: `training/data/v3/sft_realbudget_runs/260508_main1000_w20_gate1_thinking_off/records.jsonl`
- audit_rows: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/budget_fit/audit_rows.jsonl`
- 样本数：1013

## 总览

| 项 | 结果 |
|---|---:|
| 请求预算落在新分档范围 | 100.0% (1013) |
| teacher budget 落在请求目标区间 | 86.7% (878) |
| 候选池高配可达请求预算 | 95.5% (967/1013) |
| food_pois=0 | 0 |

## 按预算档位

| 档位 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 290 | 7650 | 6131 | 100.0% (290) | 87.9% (255) | 1.36 | 0 |
| limited | 364 | 3750 | 3022 | 100.0% (364) | 92.0% (335) | 1.45 | 0 |
| luxury | 16 | 13400 | 12431 | 100.0% (16) | 100.0% (16) | 1.31 | 0 |
| premium | 45 | 12100 | 8170 | 100.0% (45) | 71.1% (32) | 1.15 | 0 |
| standard | 298 | 5400 | 4170 | 100.0% (298) | 80.5% (240) | 1.18 | 0 |

## 按档位和约束

| 分组 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/hard | 12 | 6500 | 5271 | 100.0% (12) | 100.0% (12) | 1.46 | 0 |
| comfortable/none | 29 | 10100 | 5600 | 100.0% (29) | 0.0% (0) | 1.17 | 0 |
| comfortable/soft | 249 | 7600 | 6565 | 100.0% (249) | 97.6% (243) | 1.38 | 0 |
| limited/hard | 88 | 3700 | 3047 | 100.0% (88) | 98.9% (87) | 1.41 | 0 |
| limited/none | 28 | 4050 | 2814 | 100.0% (28) | 0.0% (0) | 1.35 | 0 |
| limited/soft | 248 | 3700 | 3026 | 100.0% (248) | 100.0% (248) | 1.47 | 0 |
| luxury/hard | 1 | 13300 | 12475 | 100.0% (1) | 100.0% (1) | 1.16 | 0 |
| luxury/soft | 15 | 13500 | 12388 | 100.0% (15) | 100.0% (15) | 1.32 | 0 |
| premium/hard | 3 | 10400 | 7885 | 100.0% (3) | 100.0% (3) | 1.03 | 0 |
| premium/none | 12 | 11800 | 4139 | 100.0% (12) | 0.0% (0) | 0.83 | 0 |
| premium/soft | 30 | 12250 | 10850 | 100.0% (30) | 96.7% (29) | 1.24 | 0 |
| standard/hard | 14 | 5550 | 3972 | 100.0% (14) | 100.0% (14) | 1.25 | 0 |
| standard/none | 55 | 5000 | 3396 | 100.0% (55) | 0.0% (0) | 0.97 | 0 |
| standard/soft | 229 | 5500 | 4428 | 100.0% (229) | 98.7% (226) | 1.21 | 0 |

## 优先复查样本

| record_id | level | strict | amount | recommended | teacher_total | request_status | teacher_status | high_ratio | food |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| v3_request_407102 | premium | none | 32200 | 23000-32200 | 16552 | ok | no_budget_policy | 0.67 | 40 |
| v3_request_407121 | comfortable | none | 18400 | 18400-24700 | 7930 | ok | no_budget_policy | 1.03 | 38 |
| v3_request_409554 | premium | none | 14400 | 14400-20700 | 5392 | ok | no_budget_policy | 1.22 | 34 |
| v3_request_406072 | premium | none | 22700 | 16400-22700 | 10928 | ok | no_budget_policy | 0.54 | 39 |
| v3_request_407255 | premium | none | 21100 | 14800-21100 | 5546 | ok | no_budget_policy | 0.74 | 37 |
| v3_request_405307 | premium | none | 12100 | 12100-17300 | 4538 | ok | no_budget_policy | 0.87 | 37 |
| v3_request_409135 | comfortable | none | 20100 | 15100-20100 | 20024 | ok | no_budget_policy | 1.34 | 40 |
| v3_request_407050 | premium | none | 11500 | 11500-15700 | 5224 | ok | no_budget_policy | 0.70 | 32 |
| v3_request_408217 | comfortable | none | 12900 | 12900-17200 | 6115 | ok | no_budget_policy | 1.61 | 37 |
| v3_request_404096 | comfortable | none | 13700 | 9900-13700 | 6264 | ok | no_budget_policy | 1.31 | 30 |
| v3_request_404134 | comfortable | soft | 15500 | 11800-15500 | 10188 | ok | below | 1.29 | 37 |
| v3_request_404260 | comfortable | none | 10500 | 10500-14300 | 7156 | ok | no_budget_policy | 1.42 | 39 |
| v3_request_407154 | comfortable | soft | 15500 | 11800-15500 | 10707 | ok | below | 1.14 | 40 |
| v3_request_408651 | comfortable | none | 13800 | 10000-13800 | 4436 | ok | no_budget_policy | 0.83 | 40 |
| v3_request_408710 | comfortable | none | 13700 | 9900-13700 | 6132 | ok | no_budget_policy | 0.81 | 38 |
| v3_request_404234 | comfortable | none | 12800 | 9600-12800 | 5714 | ok | no_budget_policy | 1.02 | 32 |
| v3_request_408206 | comfortable | none | 9800 | 9800-13000 | 4852 | ok | no_budget_policy | 0.99 | 33 |
| v3_request_408249 | standard | none | 11600 | 11600-14900 | 11596 | ok | no_budget_policy | 1.58 | 31 |
| v3_request_407549 | comfortable | soft | 12100 | 8900-12100 | 8060 | ok | below | 1.13 | 31 |
| v3_request_405250 | comfortable | none | 12600 | 9500-12600 | 12585 | ok | no_budget_policy | 1.27 | 39 |
| v3_request_404218 | standard | none | 9700 | 9700-12500 | 9386 | ok | no_budget_policy | 0.93 | 24 |
| v3_request_404330 | comfortable | none | 10100 | 10100-13000 | 5116 | ok | no_budget_policy | 1.51 | 30 |
| v3_request_407665 | standard | none | 10700 | 10700-13200 | 7517 | ok | no_budget_policy | 0.99 | 34 |
| v3_request_404264 | standard | none | 12300 | 9800-12300 | 7243 | ok | no_budget_policy | 0.62 | 29 |
| v3_request_407001 | standard | none | 8400 | 8400-10900 | 5500 | ok | no_budget_policy | 1.02 | 29 |
| v3_request_408434 | premium | none | 8000 | 5700-8000 | 2776 | ok | no_budget_policy | 1.15 | 32 |
| v3_request_409229 | standard | none | 7800 | 7800-10000 | 7800 | ok | no_budget_policy | 1.39 | 23 |
| v3_request_407280 | standard | none | 9200 | 7100-9200 | 4746 | ok | no_budget_policy | 0.67 | 23 |
| v3_request_404186 | comfortable | none | 5000 | 5000-6900 | 3725 | ok | no_budget_policy | 1.76 | 40 |
| v3_request_404187 | comfortable | soft | 5300 | 5300-7200 | 3303 | ok | below | 1.36 | 40 |

## 解释

- `请求预算OK`：用户预算金额是否落在新预算表按人数、天数、住宿、城市推导出的推荐区间内。
- `teacher预算OK`：SFT teacher 的 `trip_plan.budget.total` 是否落在该请求的 `budget_fit_policy` 目标区间内。
- `候选可达p50`：当前候选池粗估高配预算 / 用户预算；低于 1 表示候选供给可能不足。
