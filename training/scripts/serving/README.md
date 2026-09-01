# Planner Model Services

`manage_planner_service.py` is the service entry point for post-training.
It can start, stop and inspect the base, SFT and DPO OpenAI-compatible model
servers from one script.

Start the services needed for DPO data generation:

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft \
  --base-devices 4,5 \
  --sft-devices 6 \
  --sft-adapter-path training/outputs/qwen25_7b/sft
```

Start base, SFT and DPO together:

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft,dpo \
  --base-devices 4,5 \
  --sft-devices 6 \
  --dpo-devices 7 \
  --sft-adapter-path training/outputs/qwen25_7b/sft \
  --dpo-adapter-path training/outputs/qwen25_7b/dpo
```

Defaults:

```text
base -> http://127.0.0.1:4397/v1 -> trip-planner-base
sft  -> http://127.0.0.1:4396/v1 -> trip-planner-sft
dpo  -> http://127.0.0.1:4398/v1 -> trip-planner-dpo
```

Inspect and stop services:

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py status-all
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py stop-all --kill
```

Use `--dry-run` with `start-all` to print commands without starting vLLM.
