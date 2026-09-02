# Pre High-End Context Eval Outputs

归档时间：2026-05-11

本目录保存高端 POI context rebuild 前的模型评测输出、分片和横向对比：

- `by_model/`
- `comparisons/`
- `sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_standard_w10/`
- `sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_hard_w10/`
- `shards/`

这些结果依赖旧版 frozen eval context。后续新一轮 base/SFT/DPO 横评应统一使用
`training/data/v3/eval/records.jsonl` 和 `training/data/v3/eval_hard/records.jsonl`
中 2026-05-11 重建后的 PlannerContext，避免新旧工具快照混用。
