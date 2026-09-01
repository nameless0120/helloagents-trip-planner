# 训练交接

数据满足以下条件后，才进入训练：

```text
records
  -> 预算审计
  -> 可用性分类
  -> train/val 导出
  -> TripPlan 校验
```

SFT 训练配置：

```text
training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml
```

启动命令：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage train \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --train-dataset-dir training/data/llamafactory \
  --llamafactory-root ../LLaMA-Factory
```

训练前先用 `--dry-run` 检查配置、数据集登记和 LLaMA-Factory 路径。训练会占用 GPU，不能把 dry-run 结果当作训练完成。
