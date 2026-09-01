---
name: trip-planner-sft-data-loop
description: 当用户要为 helloagents-trip-planner 生成、审计、导出或校验一轮 Planner SFT 数据时使用；覆盖请求分布检查、PlannerContext smoke、SFT 生成、预算审计、可用性分类和训练前检查。
---

# Trip Planner SFT Data Loop

这个 skill 只负责一轮 SFT 数据 run，不负责训练过程和模型效果归因。正式流程统一从 `training/scripts/run_pipeline.py` 开始。

## 当前流程

```text
请求分布 dry-run
  -> PlannerContext smoke
  -> SFT records
  -> 预算审计
  -> 可用性分类
  -> LLaMA-Factory 导出
  -> TripPlan 校验
```

## 硬规则

- SFT run 写入 `training/data/planner/sft_runs/<run>/` 独立目录。
- 先做小批量检查，再扩量。
- 不只看生成成功数，还要看预算、候选 grounding、输出 schema 和可用性分类。
- `party`、`budget_constraint` 和 PlannerContext 必须保持结构化。
- 数据生成默认关闭 thinking，除非用户明确要求开启。
- 不把 `training/data/planner/eval/` 或 `eval_hard/` 作为训练输入。
- 用户没有给出并发和成本边界时，保持 `--workers 1`，先跑 smoke。

## 汇报

完成后说明 run 目录、成功/失败数量、主要错误、审计分类、校验结果和下一步建议。需要具体命令时读取 `references/` 下对应说明。
