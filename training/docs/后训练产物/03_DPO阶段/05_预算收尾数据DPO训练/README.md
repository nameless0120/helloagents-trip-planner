# 05 预算收尾数据 DPO 训练

这一炉从 `260519 checkpoint-138` merge 后继续 DPO，目标是用干净的预算收尾数据集中修预算偏保守、超支、边界和重复问题。

- 实验记录：`报告/实验记录卡.md`
- 训练配置：`配置/dpo_260520_closing_budget_clean_from_ckpt138_r32_2epoch_ctx24576_z3nooffload_label_logits_4gpu0123.yaml`
- 定位：预算专项收尾数据验证。
