# 后训练产物

这个目录是旅行助手后训练阶段的历史报告归档，按阶段和实验步骤整理实验记录、配置快照和评估结果。
它不是当前运行入口：里面的旧实验名称、参数和命令只用于说明当时结果。要运行当前流程，先看
[后训练总入口](../../scripts/run_pipeline.py)、[training/README.md](../../README.md) 和
[当前教程](../教程/旅行助手后训练实战教程.md)。本机完整工作台怎么找模型、数据、评测输出和缓存，见
[本地资产索引.md](本地资产索引.md)。

收录原则：

- `配置/`（目前只保留说明文档）记录当时实验的配置口径，不作为当前脚本入口。
- `报告/` 放 Markdown 评估报告、摘要、审计报告和小体积指标记录。
- 不放模型权重、`generations.jsonl`、大训练产物、服务日志和私有草稿。

## 目录

| 目录 | 内容 |
| --- | --- |
| `00_总览/` | 后训练教程、指标贡献补充、SFT 阶段总结、踩坑与经验总结。 |
| `01_Prompt阶段/01_Prompt消融/` | Prompt 消融实验记录卡、阶段总结，以及构建/刷新 prompt eval 的历史说明。 |
| `01_Prompt阶段/02_评测集与指标/` | 评测集与指标实验记录卡、standard/hard 评估集说明、预算口径和构建说明。 |
| `01_Prompt阶段/03_历史Prompt报告/` | 历史 Prompt 实验记录卡，以及 prompt、context ablation、预算 prompt、A/C/D 消融和 self-check 报告。 |
| `02_SFT阶段/00_数据生成与审计/` | SFT 数据生成与审计实验记录卡、清洗、预算审计、分布审计和目标边界。 |
| `02_SFT阶段/01_Clean_SFT训练/` | Clean SFT 实验记录卡、main-clean 配置，base 与 main-clean 评估报告。 |
| `02_SFT阶段/02_Usage700_Replay/` | Usage700 Replay 实验记录卡、训练/serve 配置、by-model 评估和横向对比报告。 |
| `02_SFT阶段/03_Patch700_Only诊断/` | Patch700-only 诊断实验记录卡、训练/serve 配置和 usage700/patch700 对比。 |
| `02_SFT阶段/04_Best-of-N_600_Replay/` | Best-of-N 600 实验记录卡、训练配置、数据脚本、ckpt96/ckpt192/final 评估。 |
| `02_SFT阶段/05_Best-of-N_1200_Retry/` | Best-of-N 1200 实验记录卡、retry 配置、ckpt52/ckpt104/ckpt156/final 评估与 600 final 对比。 |
| `02_SFT阶段/06_历史SFT主线报告/` | 历史 SFT 实验记录卡，早期主线 SFT 报告和评估标准。 |
| `03_DPO阶段/01_高置信偏好DPO试跑/` | 第一轮高置信偏好 DPO 试跑，验证流程和 checkpoint 保存策略。 |
| `03_DPO阶段/02_PlannerSoft规则DPO训练/` | 引入 planner soft 规则后的 DPO 训练记录、配置和 checkpoint sweep 结论。 |
| `03_DPO阶段/03_PlannerSoft扩数据与Direct偏好锚定/` | 扩充 planner soft 数据，并用 direct preference 稳住格式和基础能力。 |
| `03_DPO阶段/04_PlannerSoftClean单生成提升/` | 大规模 planner soft clean 数据训练，得到单生成主推 checkpoint。 |
| `03_DPO阶段/05_预算收尾数据DPO训练/` | 预算专项 clean pair 构造、anti-leak 检查和 DPO 训练记录。 |
| `03_DPO阶段/06_预算收尾继续训练验证/` | budget closing 继续训练，验证是否欠拟合。 |
| `04_Rerank阶段/01_SFT多温度候选Rerank/` | SFT 多温度候选 Rerank 实验记录卡、流程说明和 ckpt104/final1200/old600final 评估。 |
| `04_Rerank阶段/02_DPO多候选Rerank最终选择/` | DPO 多候选 Rerank 实验记录卡，ckpt64/ckpt138 对比和最终展示版本选择。 |

## 使用建议

实际运行先读 `training/docs/教程/旅行助手后训练实战教程.md`，再按阶段进入本目录看历史配置和报告。
每个步骤的归档路径见 `清单.md`。本目录保留历史结论，不承担当前代码的兼容入口。
