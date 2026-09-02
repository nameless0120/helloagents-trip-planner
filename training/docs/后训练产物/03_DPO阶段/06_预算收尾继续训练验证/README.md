# 06 预算收尾继续训练验证

这一炉从 `260520 checkpoint-66` merge 后继续 DPO，把 learning rate 从 `1e-6` 提到 `1.5e-6`，验证上一炉是否只是欠拟合。

- 实验记录：`报告/实验记录卡.md`
- 训练配置：`配置/dpo_260521_closing_budget_clean_from_merged_ckpt66_r32_2epoch_lr1p5e6_ctx24576_z3nooffload_label_logits_4gpu0123.yaml`
- 定位：closing 数据继续训练验证。
