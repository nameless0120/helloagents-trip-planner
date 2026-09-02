# Training 目录约定

`training/` 包含当前代码、当前协议、可复用输入和历史报告。运行产生的大文件、日志、模型权重和临时数据由 `.gitignore` 排除；历史报告归档不承担当前运行入口。

## 目录职责

| 路径 | 用途 |
| --- | --- |
| `configs/qwen25_7b/` | 当前 SFT、DPO 配置 |
| `data/planner/eval/` | standard 冻结评测输入 |
| `data/planner/eval_hard/` | hard 冻结评测输入 |
| `data/planner/attraction_prices/` | 票价阶段的本地运行目录 |
| `data/planner/sft_runs/` | SFT 运行目录，默认本地生成 |
| `data/planner/dpo/` | DPO 运行目录，默认本地生成 |
| `data/llamafactory/` | LLaMA-Factory 数据登记和本地导出目录 |
| `patches/` | 第三方训练依赖补丁 |
| `docs/` | 教程、PlannerContext 协议、数据审计和评测指标 |
| `scripts/run_pipeline.py` | 后训练总入口 |
| `scripts/planner/` | SFT、审计、票价、评测输入和 Best-of-N |
| `scripts/eval/` | 通用评测和 DPO |
| `scripts/serving/` | Planner 模型服务 |
| `scripts/validation/` | SFT、DPO、评测数据校验 |
| `scripts/shared/` | JSONL、当前路径定义和 LLM 客户端公共代码 |
| `outputs/eval/` | 本地评测输出目录，只提交入口说明 |

## 数据生命周期

1. `run_pipeline.py` 为每一轮创建独立 run 目录。
2. records 先经过预算审计和可用性分类，再导出为 LLaMA-Factory 数据。
3. `eval/` 和 `eval_hard/` 只作为评测输入，不作为训练输入。
4. `data/llamafactory/generated/`、SFT/DPO run、评测输出和训练输出默认不提交。
5. 训练配置使用通用文件名；实验参数通过命令行和独立 run 目录记录。

## 入口规则

- SFT 数据由 `scripts/run_pipeline.py --stage sft-data` 调度，底层实现是
  `scripts/planner/data/generate_sft_data.py`。
- 完整流程从 `scripts/run_pipeline.py` 开始。
- 训练使用 `configs/qwen25_7b/sft_qwen25_7b_lora.yaml` 或 `dpo_qwen25_7b_lora.yaml`。
- 长上下文 DPO 训练前先应用 `patches/llamafactory-9a0cfdcc-local.patch`。
- 当前运行目录由 `scripts/shared/paths.py` 统一定义。
- 新脚本必须在对应目录 README 和总入口中有明确用途；没有当前调用关系的实验工具不放入主线。
