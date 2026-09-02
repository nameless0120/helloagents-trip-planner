# 260511 高端 POI 上下文主线评估

本目录是 GitHub 友好的精简评估包，只保留可读摘要和小体积指标 JSON。

## 文件说明

- `中文结果摘要.md`：中文主报告，按 Hard Pass、Soft Pass、预算相关指标展开。
- `mainline_comparison.md`：三模型主线对比原始 Markdown。
- `mainline_comparison.json`：三模型主线对比结构化摘要。
- `slice_standard.md` / `slice_standard.json`：standard 评估集切片指标。
- `slice_hard.md` / `slice_hard.json`：hard 评估集切片指标。
- `relaxed_grounding_audit.md`：POI 名称归一化修正后的 grounding 审计摘要。

## 模型角色

- `base`：原始基线。
- `legacy_b`：旧版本数据路线上的历史最好版本，只作为历史强对照，不作为当前主线。
- `valloss_lr8e5` / `lr8e-5`：当前新上下文 / 新数据路线候选。

## 提交边界

本目录不包含 `generations.jsonl`、服务日志、逐模型完整 rule eval JSON 或历史 audit 原始数据。这些文件留在本地 `training/outputs/eval/by_model/`、`training/outputs/eval/logs/`、`training/outputs/eval/audits/` 等目录中，由 `.gitignore` 继续忽略。
