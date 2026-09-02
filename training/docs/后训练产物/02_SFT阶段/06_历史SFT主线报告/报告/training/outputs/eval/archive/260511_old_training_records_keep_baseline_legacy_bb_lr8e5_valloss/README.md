# 260511 Old Eval Records Archive

归档时间：2026-05-11

本次归档目标：只保留三个活跃评估入口，其余近期 eval 结果、对比报告、日志和临时 shard 移入 archive。

活跃保留：

- baseline：`training/outputs/eval/by_model/base_qwen25_7b/260507_realbudget_standard_w10` 和 `260507_realbudget_hard_w10`
- v2b：`training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v2b/260507_realbudget_standard_w10` 和 `260507_realbudget_hard_w10`
- lr8e-5 valloss：`training/outputs/eval/sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_standard_w10` 和 `sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_hard_w10`
- 主对比报告：`training/outputs/eval/comparisons/260510_v3_valloss_lr8e5_vs_v2b_prev_baseline_full_report/`

本目录内容：

- `by_model/`：归档的旧模型 eval 分组。
- `top_level_runs/`：归档的 final208 / step104 等顶层 eval run。
- `comparisons/`：归档的旧对比报告和 lr6e-5 对比报告。
- `logs/`：归档的旧 vLLM/eval 日志。
- `shards/`：归档的临时 eval shard。
