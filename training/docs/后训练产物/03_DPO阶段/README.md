# 03 DPO阶段

这个目录归档旅行助手的 DPO / 偏好优化训练阶段。外层路径沿用 SFT 阶段的写法：编号 + 方法模块 + 这一步的目的；日期、checkpoint、数据集代号放在实验卡正文里。

DPO 之后的多候选 rerank 不放在训练阶段里，统一归到 [04_Rerank阶段/02_DPO多候选Rerank最终选择/](../04_Rerank阶段/02_DPO多候选Rerank最终选择/)。

每个训练批次目录优先保留：

- `报告/`：实验记录卡，记录目标、数据配比、训练参数、日志观察、checkpoint 策略和复盘结论。
- `配置/`：对应训练 YAML，用于复现实验口径。

## 当前训练批次

| 批次 | 读者视角 |
| --- | --- |
| [01_高置信偏好DPO试跑/](01_高置信偏好DPO试跑/) | 先用最干净、最确定的偏好样本验证 DPO 流程是否能跑通。 |
| [02_PlannerSoft规则DPO训练/](02_PlannerSoft规则DPO训练/) | 把优化目标从单纯 hard pass 转向更贴近旅行规划质量的 planner soft。 |
| [03_PlannerSoft扩数据与Direct偏好锚定/](03_PlannerSoft扩数据与Direct偏好锚定/) | 扩大 planner soft 数据，同时保留 direct preference 作为稳定锚点。 |
| [04_PlannerSoftClean单生成提升/](04_PlannerSoftClean单生成提升/) | 用更大规模的 planner soft clean 数据，把单生成 planner soft 明显拉高。 |
| [05_预算收尾数据DPO训练/](05_预算收尾数据DPO训练/) | 针对预算偏保守、超支、边界和重复问题构造干净 pair，并记录 anti-leak 检查。 |
| [06_预算收尾继续训练验证/](06_预算收尾继续训练验证/) | 继续训练 budget closing 模型，验证上一轮是否只是学习率太小或欠拟合。 |

## 260519-260521 收尾结论

- 单生成最佳：`260519 ps2400clean_plus_direct402 checkpoint-138`。
- 多生成 rerank 最佳：`260521 closing checkpoint-64 rerank n4`，详见 `04_Rerank阶段/02_DPO多候选Rerank最终选择`。
- GitHub 展示主推：`ckpt64_rerank_n4`，500 条 planner soft 为 `80.6%`，hard split planner soft 为 `77.0%`。
