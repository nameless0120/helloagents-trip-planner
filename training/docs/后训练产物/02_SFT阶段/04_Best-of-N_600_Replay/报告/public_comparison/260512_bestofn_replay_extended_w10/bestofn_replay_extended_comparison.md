# 260512 Best-of-N Replay / Replay Usage700 / legacy_b / Mimo 扩展评估对比

- 更新时间：2026-05-12
- 当前候选：`final`
- 评估名：`260511_high_end_context_standard_w10` / `260511_high_end_context_hard_w10`
- 标准集：`training/data/planner/eval/records.jsonl`，200 条
- 困难集：`training/data/planner/eval_hard/records.jsonl`，300 条
- 本地 LoRA 对照：旧路线 `legacy_b`、前序新路线 `valloss_lr8e5`、上一轮 `replay_usage700`、Best-of-N replay `ckpt96`、`ckpt192`、`final`
- 外部参考：`mimo_v2_5_pro_external_mt1p5`
- 规则口径：当前 `eval_rule_metrics.py`；餐饮尺度按 lunch/dinner 人均单餐下限检查，早餐不参与 `meal_cost_scale`

## 通过口径

硬通过只看当前 `hard_pass` 口径的协议和 grounding 硬指标。预算合计、景点预算一致、餐饮预算一致、酒店覆盖晚数、用户预算约束等放在预算诊断区，不直接并入硬通过。

软通过链路为：硬通过 + 景点多样性 + 餐饮多样性 + 预算偏好贴合。重算预算软通过把预算偏好贴合替换为工程重算预算贴合。

## 500 条合并视图

| 指标 | legacy_b | lr8e-5 | replay_usage700 | ckpt96 | ckpt192 | final | Mimo |
|---|---:|---:|---:|---:|---:|---:|---:|
| 硬通过 | 93.6% (467/499) | 93.8% (466/497) | 96.6% (482/499) | 97.8% (486/497) | 98.0% (490/500) | **98.6% (492/499)** | 98.8% (482/488) |
| 软通过 | 47.9% (239/499) | 52.1% (259/497) | 55.9% (279/499) | 55.5% (276/497) | **56.0% (280/500)** | 55.9% (279/499) | 78.7% (384/488) |
| 重算预算软通过 | 35.7% (178/499) | 39.2% (195/497) | 41.1% (205/499) | **41.6% (207/497)** | 41.0% (205/500) | 40.5% (202/499) | 76.6% (374/488) |
| 预算关系一致 | 46.7% (233/499) | 49.7% (247/497) | 72.7% (363/499) | 78.5% (390/497) | 78.0% (390/500) | **79.6% (397/499)** | 48.6% (237/488) |
| 预算偏好贴合 | 71.5% (357/499) | 74.4% (370/497) | **75.2% (375/499)** | 71.0% (353/497) | 71.8% (359/500) | 70.5% (352/499) | 85.5% (417/488) |
| 重算预算贴合 | 53.1% (265/499) | **55.1% (274/497)** | 54.1% (270/499) | 52.7% (262/497) | 52.2% (261/500) | 51.3% (256/499) | 82.4% (402/488) |
| 餐饮尺度 | 67.3% (336/499) | 70.4% (350/497) | 81.0% (404/499) | 82.9% (412/497) | **83.2% (416/500)** | **83.2% (415/499)** | 52.0% (254/488) |
| 预算算术一致 | 65.5% (327/499) | **70.0% (348/497)** | 63.7% (318/499) | 65.8% (327/497) | 66.2% (331/500) | 67.3% (336/499) | 99.8% (487/488) |

## standard split

| 指标 | lr8e-5 | replay_usage700 | final |
|---|---:|---:|---:|
| 硬通过 | 96.5% | 95.5% | **99.0%** |
| 软通过 | 61.1% | 61.0% | **65.5%** |
| 重算预算软通过 | 45.5% | 50.5% | **53.5%** |
| 预算关系一致 | 56.6% | 81.0% | **84.0%** |
| 预算偏好贴合 | 77.3% | **79.0%** | 77.0% |
| 重算预算贴合 | 57.1% | **62.0%** | 59.5% |

standard 上 `final` 是清楚的升级：硬通过、软通过、预算关系、餐饮多样性、预算合计一致都更好。预算偏好和重算预算贴合小幅回落，但没有推翻 overall choice。

## hard split

| 指标 | lr8e-5 | replay_usage700 | final |
|---|---:|---:|---:|
| 硬通过 | 92.0% | 97.3% | **98.3%** |
| 软通过 | 46.2% | **52.5%** | 49.5% |
| 重算预算软通过 | **35.1%** | 34.8% | 31.8% |
| 预算关系一致 | 45.2% | 67.2% | **76.6%** |
| 预算偏好贴合 | 72.6% | **72.6%** | 66.2% |
| 重算预算贴合 | **53.9%** | 48.8% | 45.8% |

hard 上 `final` 更像“结构修补版”：预算关系、酒店预算关系、酒店覆盖晚数、景点预算人数关系明显提升；但预算偏好、重算预算贴合和 softpass 回落。后续如果继续做 SFT，需要优先补 hard split 的预算选品和偏好样本。

## 版本角色

| 版本 | 角色 | 结论 |
|---|---|---|
| `legacy_b` | 旧数据路线历史强对照 | 已被新路线在硬通过、软通过、预算关系、酒店/景点预算关系上明显超过 |
| `lr8e-5` | usage700 前的新路线 valloss 节点 | 硬通过低于后续版本，但重算预算贴合和预算算术是主要高点，不能从对比里省略 |
| `replay_usage700` | Best-of-N 前上一轮主线 | 仍是预算偏好、重算预算贴合、hard split softpass 的主要参考 |
| `ckpt96` | Best-of-N replay 中间点 | 重算预算软通过最高，但硬约束弱于 final |
| `ckpt192` | Best-of-N replay 中间点 | 合并 softpass 最高，但 hard split soft 指标仍不如 replay_usage700 |
| `final` | 当前最新硬约束主线 | 本地 LoRA hardpass、预算关系、预算算术整体最好，建议作为当前主线 |
| `Mimo` | 外部 teacher/reference | 适合蒸馏预算选品和多样性，但餐饮尺度需后处理 |

## 训练混比

| 项 | 数量 |
|---|---:|
| 旧 replay 训练样本 | 2309 |
| Best-of-N winner 训练样本 | 540 |
| Best-of-N 过采样样本 | 270 |
| 训练总量 | 3119 |
| 旧 replay 验证样本 | 256 |
| Best-of-N 验证样本 | 60 |
| 验证总量 | 316 |
| Best-of-N 训练有效占比 | 25.97% |
| shuffle seed | 260512 |

## 数据源

| 版本 | 标准集报告 | 困难集报告 |
|---|---|---|
| final | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_final/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_final/260511_high_end_context_hard_w10/rule_eval_report.json` |
| lr8e-5 | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260509_main_clean_cp2_legacy_b_valloss_lr8e5/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260509_main_clean_cp2_legacy_b_valloss_lr8e5/260511_high_end_context_hard_w10/rule_eval_report.json` |
| replay_usage700 | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260511_replay_usage700_from_lr6e5_lr2e5/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260511_replay_usage700_from_lr6e5_lr2e5/260511_high_end_context_hard_w10/rule_eval_report.json` |
| legacy_b | `training/outputs/eval/by_model/sft_qwen25_7b_planner_1000_cp2_legacy_b/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_1000_cp2_legacy_b/260511_high_end_context_hard_w10/rule_eval_report.json` |
| ckpt96 | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_ckpt96/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_ckpt96/260511_high_end_context_hard_w10/rule_eval_report.json` |
| ckpt192 | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_ckpt192/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260512_bestofn_replay_ckpt192/260511_high_end_context_hard_w10/rule_eval_report.json` |
| Mimo | `training/outputs/eval/by_model/mimo_v2_5_pro_external_mt1p5/260511_high_end_context_standard_w10/rule_eval_report.json` | `training/outputs/eval/by_model/mimo_v2_5_pro_external_mt1p5/260511_high_end_context_hard_w10/rule_eval_report.json` |

完整本地产物保留在 `training/outputs/eval/comparisons/260512_bestofn_replay_extended_vs_legacy_b_replay_mimo_w10/`。GitHub 报告包只收录轻量摘要和指标 JSON。
