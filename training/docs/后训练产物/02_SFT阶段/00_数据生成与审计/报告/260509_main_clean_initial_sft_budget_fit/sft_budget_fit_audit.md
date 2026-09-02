# V3 SFT 预算贴合审计

- records: `training/data/v3/sft/260509/main_clean/records.jsonl`
- audit_rows: `training/outputs/eval/audits/260509_main_clean_initial_sft_budget_fit/audit_rows.jsonl`
- 样本数：1865

## 总览

| 项 | 结果 |
|---|---:|
| 请求预算落在新分档范围 | 100.0% (1865) |
| teacher budget 落在请求目标区间 | 100.0% (1865) |
| 候选池高配可达请求预算 | 100.0% (1865/1865) |
| food_pois=0 | 0 |

## 按预算档位

| 档位 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 519 | 8000 | 6933 | 100.0% (519) | 100.0% (519) | 1.33 | 0 |
| limited | 335 | 3700 | 3022 | 100.0% (335) | 100.0% (335) | 1.46 | 0 |
| luxury | 16 | 13400 | 12431 | 100.0% (16) | 100.0% (16) | 1.31 | 0 |
| premium | 210 | 10800 | 9445 | 100.0% (210) | 100.0% (210) | 1.19 | 0 |
| standard | 785 | 5600 | 4466 | 100.0% (785) | 100.0% (785) | 1.21 | 0 |

## 按档位和约束

| 分组 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/hard | 12 | 6500 | 5271 | 100.0% (12) | 100.0% (12) | 1.46 | 0 |
| comfortable/soft | 507 | 8200 | 7016 | 100.0% (507) | 100.0% (507) | 1.33 | 0 |
| limited/hard | 87 | 3700 | 3014 | 100.0% (87) | 100.0% (87) | 1.42 | 0 |
| limited/soft | 248 | 3700 | 3026 | 100.0% (248) | 100.0% (248) | 1.47 | 0 |
| luxury/hard | 1 | 13300 | 12475 | 100.0% (1) | 100.0% (1) | 1.16 | 0 |
| luxury/soft | 15 | 13500 | 12388 | 100.0% (15) | 100.0% (15) | 1.32 | 0 |
| premium/hard | 3 | 10400 | 7885 | 100.0% (3) | 100.0% (3) | 1.03 | 0 |
| premium/soft | 207 | 10800 | 9480 | 100.0% (207) | 100.0% (207) | 1.20 | 0 |
| standard/hard | 65 | 6000 | 4190 | 100.0% (65) | 100.0% (65) | 1.26 | 0 |
| standard/soft | 720 | 5500 | 4505 | 100.0% (720) | 100.0% (720) | 1.20 | 0 |

## 优先复查样本

| record_id | level | strict | amount | recommended | teacher_total | request_status | teacher_status | high_ratio | food |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| v3_request_420944 | premium | soft | 31900 | 31900-45700 | 24004 | ok | ok | 1.43 | 39 |
| v3_request_420846 | premium | soft | 31500 | 31500-43000 | 30856 | ok | ok | 1.14 | 36 |
| v3_request_420899 | premium | soft | 39400 | 27900-39400 | 29780 | ok | ok | 1.13 | 35 |
| v3_request_420823 | premium | soft | 43000 | 31500-43000 | 43208 | ok | ok | 1.05 | 40 |
| v3_request_420861 | premium | soft | 28200 | 28200-39700 | 28200 | ok | ok | 1.27 | 40 |
| v3_request_420833 | premium | soft | 24900 | 24900-35300 | 19902 | ok | ok | 1.12 | 40 |
| v3_request_408594 | comfortable | soft | 26600 | 26600-36100 | 25892 | ok | ok | 1.61 | 37 |
| v3_request_420678 | comfortable | soft | 27400 | 27400-36900 | 27368 | ok | ok | 1.27 | 37 |
| v3_request_420891 | premium | soft | 31500 | 22300-31500 | 25236 | ok | ok | 1.19 | 40 |
| v3_request_420909 | premium | soft | 24700 | 24700-33900 | 24772 | ok | ok | 1.57 | 38 |
| v3_request_407078 | luxury | soft | 26000 | 26000-34700 | 26000 | ok | ok | 1.20 | 35 |
| v3_request_420868 | premium | soft | 22400 | 22400-31100 | 18200 | ok | ok | 1.36 | 40 |
| v3_request_404391 | luxury | soft | 22500 | 22500-30900 | 22392 | ok | ok | 1.31 | 40 |
| v3_request_407500 | comfortable | soft | 22300 | 22300-30600 | 17756 | ok | ok | 1.69 | 40 |
| v3_request_420822 | premium | soft | 24500 | 24500-32400 | 22013 | ok | ok | 1.06 | 38 |
| v3_request_408610 | comfortable | soft | 31500 | 23700-31500 | 31500 | ok | ok | 1.14 | 34 |
| v3_request_420931 | premium | soft | 20700 | 20700-28600 | 18661 | ok | ok | 1.05 | 40 |
| v3_request_420600 | comfortable | soft | 20300 | 20300-27800 | 22068 | ok | ok | 1.94 | 40 |
| v3_request_420969 | premium | soft | 17600 | 17600-25200 | 17532 | ok | ok | 1.18 | 39 |
| v3_request_407254 | comfortable | soft | 22700 | 22700-29800 | 21710 | ok | ok | 1.59 | 30 |
| v3_request_407690 | comfortable | soft | 27100 | 20200-27100 | 19375 | ok | ok | 1.02 | 40 |
| v3_request_420704 | comfortable | soft | 18900 | 18900-25800 | 17484 | ok | ok | 1.54 | 34 |
| v3_request_420810 | premium | soft | 15700 | 15700-22600 | 12828 | ok | ok | 1.58 | 36 |
| v3_request_420830 | premium | soft | 25400 | 18500-25400 | 25332 | ok | ok | 1.26 | 35 |
| v3_request_420847 | premium | soft | 28600 | 21500-28600 | 22130 | ok | ok | 1.07 | 36 |
| v3_request_420865 | premium | soft | 21000 | 21000-27900 | 17268 | ok | ok | 1.22 | 40 |
| v3_request_420871 | premium | soft | 17900 | 17900-24800 | 17292 | ok | ok | 1.77 | 40 |
| v3_request_420886 | premium | soft | 17900 | 17900-24800 | 13642 | ok | ok | 1.74 | 32 |
| v3_request_420926 | premium | soft | 27300 | 20400-27300 | 21197 | ok | ok | 1.15 | 33 |
| v3_request_420929 | premium | soft | 15800 | 15800-22700 | 15232 | ok | ok | 1.11 | 40 |

## 解释

- `请求预算OK`：用户预算金额是否落在新预算表按人数、天数、住宿、城市推导出的推荐区间内。
- `teacher预算OK`：SFT teacher 的 `trip_plan.budget.total` 是否落在该请求的 `budget_fit_policy` 目标区间内。
- `候选可达p50`：当前候选池粗估高配预算 / 用户预算；低于 1 表示候选供给可能不足。
