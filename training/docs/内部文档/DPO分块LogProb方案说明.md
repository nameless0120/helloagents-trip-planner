# LLaMA-Factory 本地改动说明

更新时间：2026-08-31

本项目的长上下文 DPO 训练使用了一组 LLaMA-Factory 本地改动。主项目不直接复制 LLaMA-Factory 源码，而是记录基础 commit 和补丁，补丁文件位于：

```text
training/patches/llamafactory-9a0cfdcc-local.patch
```

当前补丁基于 LLaMA-Factory commit：

```text
9a0cfdccfa234304879f83e0c2c17b5ede8121fe
```

如果只安装官方 LLaMA-Factory，不应用这份补丁，长上下文 DPO 的显存占用和 v1 训练流程可能与本项目记录的结果不一致。

## 为什么需要这组改动

长上下文 DPO 计算 chosen/rejected 的 token log probability。原实现会先对完整 logits 做：

```python
logits.log_softmax(-1)
```

这个张量的形状接近 `[batch, seq_len, vocab_size]`。在 Qwen2.5-7B、24k 左右上下文和约 152k 词表的场景下，中间张量很大，可能在 DPO 第一步触发 OOM。

本地改动只保留 DPO 需要的目标 token log probability，并按 sequence 维度分块计算。数学形式仍然是：

```text
log p(y) = selected_logit - logsumexp(logits)
```

因此改变的是计算和显存占用，不是 DPO 的目标函数。

## 改了哪些文件

| 文件 | 改动 | 用途 |
| --- | --- | --- |
| `src/llamafactory/train/dpo/trainer.py` | 可选只返回 response label 对应位置的 logits；不再把 chosen/rejected 的完整 logits 留给 metrics；增加保存 activation 到 CPU 的选项 | 降低长上下文 DPO 的显存峰值 |
| `src/llamafactory/train/trainer_utils.py` | `get_batch_logps` 改为 sequence 分块计算；新增 `get_batch_logps_from_shifted_logits`；保留原实现回退开关 | 避免完整 `log_softmax` 中间张量 |
| `src/llamafactory/v1/config/training_args.py` | 增加 `eval_steps`、`eval_epochs`、`eval_global_batch_size`、`eval_batching_workers` | 配置 v1 eval 频率和批处理 |
| `src/llamafactory/v1/core/base_trainer.py` | 支持 `eval_dataset`、teacher-forcing eval、训练中 eval 和训练结束 eval；清理不应传给模型的 labels；兼容新版 `DTensor` | 补齐 v1 的验证流程并修复分布式兼容问题 |
| `src/llamafactory/v1/plugins/model_plugins/parallelization/sequence_parallel.py` | 不把 `labels` 和 `loss_weights` 传入模型；不强制复制成 fp32 logits | 降低 sequence parallel 的额外显存 |
| `src/llamafactory/v1/plugins/trainer_plugins/distributed/fsdp2.py` | 按参数所在设备初始化梯度；兼容不同 PyTorch 版本的 `DTensor` 导入路径 | 修复 FSDP2 梯度处理 |
| `src/llamafactory/v1/trainers/sft_trainer.py` | 将 `eval_dataset` 传给 v1 `SFTTrainer` | 让 v1 SFT 使用独立验证集 |

## 环境变量

统一入口在调用 LLaMA-Factory 时会保留用户已经设置的值，并为项目训练补上下面的默认值：

| 变量 | 默认值 | 作用 |
| --- | --- | --- |
| `LLAMAFACTORY_DPO_LABEL_LOGITS_ONLY` | `1` | DPO 只请求 response label 对应的 logits |
| `LLAMAFACTORY_LOGPS_CHUNK_SIZE` | `1024` | 每次处理的 sequence token 数 |
| `LLAMAFACTORY_LOGPS_CHECKPOINT` | `1` | 对分块 logprob 开启 checkpoint，降低反向传播显存 |
| `LLAMAFACTORY_LOGPS_UPCAST` | `0` | 是否只在当前 chunk 内把 logits 转成 fp32 |
| `FORCE_TORCHRUN` | `1` | 让 DeepSpeed 配置通过 `torchrun` 启动 |
| `LLAMAFACTORY_DPO_SAVE_ON_CPU` | 未设置 | 设为 `1` 后，把 forward 保存的 activation 放到 CPU；只在 CPU 内存和速度允许时使用 |
| `LLAMAFACTORY_DPO_SAVE_ON_CPU_PIN` | `1` | 配合上一个变量，控制 CPU activation 是否使用 pinned memory |
| `LLAMAFACTORY_LOGPS_ORIGINAL` | 未设置 | 设为 `1` 后回退到原始完整 `log_softmax`，只用于排查数值或兼容问题 |

仍然 OOM 时，可以先把 `LLAMAFACTORY_LOGPS_CHUNK_SIZE` 调到 `512`。如果显存有余量但训练速度较慢，可以尝试 `2048`。`LLAMAFACTORY_LOGPS_ORIGINAL=1` 会放弃这部分显存优化，不应作为长上下文训练的默认配置。

## 准备 LLaMA-Factory

从主项目根目录执行。下面的命令不会下载模型，也不会启动 GPU 训练：

```bash
cd ..
git clone https://github.com/hiyouga/LLaMA-Factory.git LLaMA-Factory
cd LLaMA-Factory
git checkout 9a0cfdccfa234304879f83e0c2c17b5ede8121fe
git apply ../helloagents-trip-planner/training/patches/llamafactory-9a0cfdcc-local.patch
```

然后按 LLaMA-Factory 的依赖说明准备训练环境，并把当前 checkout 以 editable 方式安装到该环境。已有完整训练环境时，可以使用：

```bash
../helloagents-trip-planner/.venv-training-py311/bin/python3 -m pip install -e . --no-deps
```

`run_pipeline.py` 还会把 `<llamafactory-root>/src` 放到 `PYTHONPATH`，并把工作目录切到 LLaMA-Factory 根目录，因此配置中类似 `examples/deepspeed/...` 的相对路径也能正确解析。

确认补丁已经应用：

```bash
git -C ../LLaMA-Factory apply --reverse --check \
  ../helloagents-trip-planner/training/patches/llamafactory-9a0cfdcc-local.patch
```

命令返回成功，表示当前 checkout 与项目补丁一致。若返回失败，先检查基础 commit 和本地源码是否被其他改动覆盖。

## 从统一入口启动训练

训练阶段必须显式指定配置。LLaMA-Factory 根目录默认取 `LLAMAFACTORY_ROOT`，未设置时取主项目同级的 `../LLaMA-Factory`。推荐先用 `sft-data` 和 `sft-audit` 生成并登记数据集，再单独启动训练：

```bash
cd helloagents-trip-planner
export RUN_NAME="$(date +%Y%m%d_%H%M%S)_reader"
export SFT_RUN="training/data/planner/sft_runs/${RUN_NAME}"
export SFT_DATASET="trip_planner_sft_${RUN_NAME}"

.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-data \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir "$SFT_RUN"

.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-audit \
  --records "$SFT_RUN/records.jsonl" \
  --sft-dir "$SFT_RUN" \
  --sft-dataset-prefix "$SFT_DATASET"

.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage train \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --train-dataset "${SFT_DATASET}_train" \
  --train-eval-dataset "${SFT_DATASET}_val" \
  --llamafactory-root ../LLaMA-Factory \
  --llamafactory-cli .venv-training-py311/bin/llamafactory-cli
```

入口会把 `--train-dataset`、`--train-eval-dataset`、`dataset_dir` 和训练输出目录传给 LLaMA-Factory。训练前会检查数据集是否已经登记且文件非空。DPO 数据构造和训练使用 `--stage dpo --stage train`，并改用 `dpo_qwen25_7b_lora.yaml`；DPO 数据生成阶段仍需要按 `training/README.md` 启动对应的模型服务和 judge 配置。已有 DPO 文件则可以只执行 `--stage train`，前提是配置中的数据集已经登记。

第一次建议先查看命令，不执行数据生成或训练：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage train \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --train-dataset "${SFT_DATASET}_train" \
  --train-eval-dataset "${SFT_DATASET}_val" \
  --llamafactory-root ../LLaMA-Factory \
  --dry-run
```

`--dry-run` 只打印将要调用的子命令；它不会验证本轮尚未生成的数据文件，也不会代表当前机器已经具备完整训练依赖。实际运行时，`preflight`、数据集检查、补丁检查和 `llamafactory-cli` 检查会在训练启动前执行。

默认情况下，训练入口会检查以下内容：

- LLaMA-Factory 的 `HEAD` 必须是上面记录的基础 commit。
- 项目补丁必须已经应用。
- `llamafactory-cli` 必须存在且可执行。
- 训练进程必须从指定的 LLaMA-Factory checkout 导入源码。

`--allow-unpatched-llamafactory` 只用于不依赖本项目补丁的实验。长上下文 DPO 不应使用这个选项。

## 维护规则

这份补丁是第三方源码和本项目训练结果之间的依赖边界。以后更新 LLaMA-Factory 时，需要同时更新基础 commit、补丁文件、本文档和统一入口的校验值，并重新做小规模数值等价和语法检查。不要只更新 `llamafactory-cli` 的安装版本，否则无法判断训练使用的是哪套实现。
