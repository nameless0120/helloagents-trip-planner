# V3 当前评测口径 Baseline 重算汇总

> 2026-05-05 更新：Planner prompt baseline 已冻结为 prompt ablation `A_C`，对应 `training/outputs/eval/prompt_ablation_20260505/baseline_freeze.md`，prompt_sha256 为 `dbe3f951082929b5de41e3de38f823356dd94a01896d81246e447d80a196e5c0`。下表保留的是上一阶段 context/generation baseline 重算结果，用作历史对照。

说明：本表只重算已有 generations，不重新调用模型。当前预算口径为：酒店单房每晚价，按两人一间折算；餐饮为单人单餐价；景点门票为单人票。

| 版本 | schema | SFT严格过 | DPO软过 | SFT语义硬过 | 预算关系 | 酒店关系 | 景点关系 | 餐饮尺度 | 用户预算 | 预算加总 | 景点ground | 酒店ground | 餐饮ground | 餐饮多样 | avg秒 | p90秒 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_full | 98.0% | 0.0% | 0.0% | 3.4% | 5.4% | 41.8% | 27.6% | 81.0% | 82.3% | 60.5% | 99.0% | 100.0% | 97.3% | 8.2% | 64.9 | 80.1 |
| hard_compact | 98.7% | 0.0% | 0.0% | 4.4% | 6.8% | 39.5% | 28.0% | 87.2% | 81.4% | 69.6% | 97.3% | 99.7% | 96.6% | 6.8% | 60.9 | 75.3 |
| hard_topk | 99.3% | 0.0% | 0.0% | 6.4% | 9.1% | 41.6% | 28.5% | 88.3% | 83.9% | 64.1% | 96.0% | 100.0% | 95.0% | 7.0% | 53.3 | 65.3 |
| hard_policy_topk | 99.0% | 0.0% | 0.0% | 5.1% | 7.7% | 40.1% | 32.3% | 84.5% | 83.8% | 64.6% | 97.6% | 100.0% | 96.0% | 14.5% | 54.2 | 66.1 |
| balanced_full | 97.3% | 0.0% | 0.0% | 4.1% | 6.5% | 39.4% | 28.8% | 61.6% | 85.6% | 62.7% | 96.9% | 99.7% | 87.3% | 51.0% | 65.1 | 79.0 |
| balanced_compact | 98.7% | 0.0% | 0.0% | 3.7% | 6.1% | 40.5% | 24.3% | 76.7% | 82.8% | 66.2% | 98.7% | 100.0% | 90.5% | 49.0% | 60.8 | 73.4 |
| balanced_topk | 98.7% | 0.0% | 0.0% | 4.0% | 6.1% | 39.9% | 25.0% | 78.0% | 83.5% | 67.6% | 97.3% | 100.0% | 86.2% | 56.4% | 50.6 | 60.1 |
| balanced_policy_topk | 99.0% | 0.3% | 0.0% | 3.0% | 7.1% | 38.7% | 26.6% | 78.8% | 88.9% | 66.0% | 95.6% | 100.0% | 85.5% | 51.2% | 50.7 | 60.9 |

## 结论

- 这批旧 generations 在新预算口径下 `sft_hard_pass` 和 `dpo_soft_pass` 基本为 0，这是预期内的：旧输出没有按“两人一间”和“餐饮单人价”生成，`meal_budget_consistent` 和 `attraction_budget_consistent` 会系统性失败。
- 用于定 baseline 时，不应该拿严格合成 pass 一票否决，而应该看结构稳定性、grounding、速度，以及新口径下的预算语义分项。
- 推荐把 `hard_compact` 定为当前 SFT baseline：schema 98.7%，景点/酒店/餐饮 grounding 分别约 97.3%/99.7%/96.6%，平均 60.9 秒；相比 full 更快，相比 topk 语义损失更小。
- `hard_topk` 的预算语义指标略高、速度更快，但它是靠减少候选上下文换来的，后续做训练数据 baseline 我不建议选它，容易把候选覆盖不足的问题藏进数据里。
- `balanced_*` 的餐饮多样性明显更好，但住宿类型和硬约束更弱，更适合作为 DPO 软偏好参考，不适合作为 SFT 主 baseline。
- `budget_arithmetic_consistent` 当前只作为观察项；精确加总后续交给工程后处理，不用拿它否定模型 baseline。

## 推荐 baseline

`base_qwen25_7b_v3_ctx_hard_compact_w10_room_person_eval`

对应原始生成目录：`training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_w10/`

对应重算报告：`training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_w10_room_person_eval/rule_eval_report.md`

## 对应报告目录

- hard_full: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_full_w10_room_person_eval/rule_eval_report.md`
- hard_compact: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_w10_room_person_eval/rule_eval_report.md`
- hard_topk: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_topk_w10_room_person_eval/rule_eval_report.md`
- hard_policy_topk: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_policy_first_topk_w10_room_person_eval/rule_eval_report.md`
- balanced_full: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_full_w10_room_person_eval/rule_eval_report.md`
- balanced_compact: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_compact_w10_room_person_eval/rule_eval_report.md`
- balanced_topk: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_topk_w10_room_person_eval/rule_eval_report.md`
- balanced_policy_topk: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_policy_first_topk_w10_room_person_eval/rule_eval_report.md`
