# 导出和校验

审计通过后，导出结果位于 `training/data/llamafactory/generated/`，并由总入口更新 `dataset_info.json`。

手动校验 SFT 文件：

```bash
.venv-training-py311/bin/python3 training/scripts/validation/validate_trip_plan.py \
  --sft training/data/llamafactory/generated/<sft_train>.json
```

同时校验 train 和 val 时分别传入两个文件。确认：

- 文件是非空 JSON 数组。
- 每条样本的消息结构完整。
- assistant 内容能解析为 `TripPlan`。
- 训练和验证文件来自同一轮 run。
