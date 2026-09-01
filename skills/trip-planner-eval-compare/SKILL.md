---
name: trip-planner-eval-compare
description: 当用户要运行或对比 helloagents-trip-planner 的 Planner standard/hard 评测时使用；覆盖单模型评测、规则指标、切片汇总、可选 judge 和报告整理。
---

# Trip Planner Eval Compare

这个 skill 只处理模型评测和对比，不负责 SFT 数据生成或训练。评测输入固定使用：

```text
training/data/planner/eval/records.jsonl
training/data/planner/eval_hard/records.jsonl
```

## 当前流程

```text
冻结 records
  -> 模型服务生成
  -> eval_rule_metrics.py
  -> standard / hard 汇总
  -> 切片或 judge（按需）
```

## 硬规则

- 对比模型必须使用同一个 split、同一份 records 和同一套评测脚本。
- 模型输出写入 `training/outputs/eval/<run>/` 本地目录。
- 先检查生成失败、截断、schema 分母，再解释 hard/soft 指标。
- LLM judge 需要先确认 API、并发和成本边界。
- 没有模型服务时先用 `--dry-run` 检查命令。

具体命令见 `references/run_eval.md` 和 `references/compare_and_report.md`。
