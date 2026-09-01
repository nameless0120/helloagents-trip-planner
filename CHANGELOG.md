# 变更记录

## 2026-09-01

- 统一后训练入口为 `training/scripts/run_pipeline.py`。
- 统一 SFT 数据生成、预算审计、可用性分类、LLaMA-Factory 导出和格式校验流程。
- 训练数据生成默认关闭 thinking，避免思考内容占用 JSON 输出预算。
- 清理重复脚本、日期实验配置、过程报告和运行产物，只保留当前代码与当前协议。
- 补充 README、目录说明、训练教程和 LLaMA-Factory 本地改动说明。

感谢 [@cqray1990](https://github.com/cqray1990) 提交 [Issue #4](https://github.com/nameless0120/helloagents-trip-planner/issues/4)，帮助我们发现数据生成流程中的 `party` 字段问题。
