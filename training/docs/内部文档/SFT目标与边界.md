# Planner SFT 目标与边界

Planner SFT 的目标是让模型把结构化 `PlannerContext` 稳定转换成合法的 `TripPlan JSON`。它负责学习输出协议和基础业务规则，不负责替代后端的确定性计算。

## SFT 学什么

- 只输出可解析的 JSON，符合后端 `TripPlan` schema。
- 日期、天数、天气和住宿晚数与请求一致。
- 景点、酒店和餐饮优先从 `tool_snapshot` 候选中选择。
- 复制候选中的地址、坐标和价格 hint，不编造精确事实。
- 识别 `party`、`budget_constraint`、饮食限制和同行人约束。
- 按当前价格单位组织酒店、门票、餐饮和交通预算。
- 每天包含完整的景点和三餐结构，不使用泛化占位餐饮。

## 工程侧保证什么

- 后端负责构造 `PlannerContext`，并把请求、人数、预算和候选数据结构化。
- 后端负责外部工具调用、价格 hint、确定性预算重算和最终 schema 校验。
- 评测脚本负责检查输出是否满足协议，不把文本中的模糊猜测当成结构化事实。
- 推理服务在模型输出不合法时负责重试或返回错误。

## 不把这些混进 SFT 目标

- 不用训练让模型记住实时票价、天气或路线。
- 不用训练替代高德、路线和价格服务。
- 不用 DPO pair 修复 JSON 或 schema 错误。
- 不把不同请求协议、不同价格单位的数据混进同一个训练 run。

## 最小验收

数据进入训练前，必须完成：

```text
生成 records
  -> 预算审计
  -> 可用性分类
  -> LLaMA-Factory 导出
  -> SFT JSON 校验
```

所有步骤由 `training/scripts/run_pipeline.py --stage sft` 统一调度。
