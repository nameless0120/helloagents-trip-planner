# 变更记录

## 2026-09-01

- 统一后训练入口为 `training/scripts/run_pipeline.py`。
- 将 SFT 拆成 `sft-data` 和 `sft-audit` 两个阶段，读者可以分别运行数据生成和数据审计。
- 支持用 `--train-dataset`、`--train-eval-dataset` 直接训练已有导出数据。
- README 明确当前后训练主线，并补充 Best-of-N 和产品侧 rerank 的入口。
- 恢复 README 和教程中的 `helloagents-后训练数据` 网盘链接。
- 训练数据生成默认关闭 thinking，避免思考内容占用 JSON 输出预算。
- `training/scripts/serving/manage_planner_service.py` 支持一条命令启动、查看和停止 base、SFT、DPO 模型服务。
- 清理重复脚本、日期实验配置、过程报告和运行产物，只保留当前代码与当前协议。
- 补充 README、目录说明、训练教程和 LLaMA-Factory 本地改动说明。

感谢 [@cqray1990](https://github.com/cqray1990) 提交 [Issue #4](https://github.com/nameless0120/helloagents-trip-planner/issues/4)，帮助我们发现数据生成流程中的 `party` 字段问题。
