# Training Scripts

训练脚本按职责分组，正式流程统一由 `run_pipeline.py` 调度。

```text
run_pipeline.py
  -> planner/data/       # SFT 数据
  -> planner/audit/      # 预算审计和样本分类
  -> planner/pricing/    # 景点票价候选
  -> planner/bestofn/    # 多候选采样和选择
  -> eval/               # DPO 和通用评测
  -> validation/         # 输出校验
  -> LLaMA-Factory      # 训练
```

常用命令见 [training README](../README.md) 和 [后训练教程](../docs/教程/旅行助手后训练实战教程.md)。

## 直接入口

| 路径 | 用途 |
| --- | --- |
| `run_pipeline.py` | 串联所有后训练阶段 |
| `planner/data/generate_sft_data.py` | 生成请求、PlannerContext 和 SFT records |
| `planner/audit/` | 预算贴合审计和可用性分类 |
| `planner/pricing/` | 景点候选收集、分桶和票价估算 |
| `planner/bestofn/` | 多候选生成、规则选择和导出 |
| `planner/eval/` | 构建评测输入和生成评测报告 |
| `eval/` | DPO、模型生成和规则评测 |
| `serving/` | 启动和管理 Planner 模型服务 |
| `validation/` | 校验 SFT、DPO 和 Eval 文件 |

底层脚本可以单独运行来定位问题，但新的一轮数据和训练应从总入口开始。
