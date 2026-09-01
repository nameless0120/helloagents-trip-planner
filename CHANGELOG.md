# 变更记录

## 2026-09-01：后训练流程整理

### 变更

- 新增 `training/scripts/run_pipeline.py`，统一调度 SFT 数据生成、预算审计、可用性分类、导出、校验和训练。
- 将当前 SFT 数据生成入口固定为 `training/scripts/planner/data/generate_sft_data.py`，旧版 `eval/generate_sft_data.py` 保留为兼容入口。
- 修复旧入口的 `party`、`budget_constraint` 兼容字段和新数据脚本的模块导入问题。
- 数据生成模型默认关闭 thinking。关闭时不会发送 `reasoning_effort` 或 `thinking` 参数，避免 JSON 输出被思考过程耗尽；需要时仍可显式设置 `DATA_GEN_THINKING=true`。
- 补充训练配置、LLaMA-Factory 本地改动说明、目录说明和读者版运行文档。

### 验证

- 非思考模式实际调用 Planner 模型 1 次，成功生成 JSON 并通过基础 TripPlan schema 校验。
- 训练入口使用本地 Qwen2.5-7B-Instruct 和已有 SFT 数据完成单卡 1 个 epoch 的训练与评估。

### 致谢

感谢 [@nameless0120](https://github.com/nameless0120) 提交 [Issue #4](https://github.com/nameless0120/helloagents-trip-planner/issues/4)，帮我们发现旧版数据生成入口的 `party` 字段校验问题，也促成了这次数据生成、审计和训练流程的重新整理。
