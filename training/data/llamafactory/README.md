# LLaMA-Factory 数据入口

这个目录只登记当前训练数据。`dataset_info.json` 保留通用的 SFT/DPO 数据集名，实际 train/val 文件由 `run_pipeline.py` 写入 `generated/`，该目录默认被忽略。

```text
training/data/llamafactory/
├── dataset_info.json
└── generated/              # 本地生成的 train/val 文件
```

SFT 和 DPO 训练配置分别使用：

```text
training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml
training/configs/qwen25_7b/dpo_qwen25_7b_lora.yaml
```

不要手动复制数据或维护多套 dataset 注册表。总入口会在导出阶段更新登记信息。
