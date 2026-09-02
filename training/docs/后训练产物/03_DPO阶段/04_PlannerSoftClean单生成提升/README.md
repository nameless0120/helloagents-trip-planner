# 04 PlannerSoft Clean 单生成提升

这一炉从 `260518 core1418_plus_direct402 checkpoint-126` 的 merge 模型继续做 DPO，目标是放大 planner soft clean 信号，同时保留 direct402 anchor。

- 实验记录：`报告/实验记录卡.md`
- 训练配置：`配置/dpo_260519_ps2400clean_plus_direct402_from_ckpt126_r32_3epoch_ctx24576_z3nooffload_label_logits_6gpu012345.yaml`
- 定位：单生成主推 checkpoint。
