#!/usr/bin/env python3
"""Launch an OpenAI-compatible LLaMA-Factory API for the trip planner model.

Qwen2.5 does not have an 8B text instruct checkpoint. The closest <=8B
checkpoint is Qwen2.5-7B-Instruct, which is what this launcher uses by default.

Examples:
    cd .

    # Serve the base Qwen2.5-7B-Instruct model for DPO generation.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --variant base \
      --port 4397 \
      --api-model-name trip-planner-base \
      --cuda-visible-devices 4,5

    # Serve the SFT LoRA result after training finishes.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --variant sft \
      --cuda-visible-devices 6 \
      --api-model-name trip-planner-sft

    # Serve the DPO-only result.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --variant dpo \
      --port 4398 \
      --api-model-name trip-planner-dpo \
      --cuda-visible-devices 6

    # Serve the SFT+DPO result.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --variant sft_dpo \
      --cuda-visible-devices 6

    # Serve a specific checkpoint or experiment output.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --adapter-path training/outputs/qwen25_7b/sft/checkpoint-39 \
      --cuda-visible-devices 6

    # Only write the generated LLaMA-Factory inference yaml and exit.
    .venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
      --variant base \
      --write-config-only
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
WORKSPACE_ROOT = PROJECT_ROOT.parent
LLAMA_FACTORY_ROOT = WORKSPACE_ROOT / "LLaMA-Factory"

DEFAULTS = {
    "model_path": "Qwen/Qwen2.5-7B-Instruct",
    "template": "qwen",
    "host": "0.0.0.0",
    "port": 4396,
    "backend": "huggingface",
    "infer_dtype": "bfloat16",
    "api_model_prefix": "trip-planner",
}

VARIANTS = {
    "base": None,
    "sft": PROJECT_ROOT / "training/outputs/qwen25_7b/sft",
    "dpo": PROJECT_ROOT / "training/outputs/qwen25_7b/dpo",
    "sft_dpo": PROJECT_ROOT / "training/outputs/qwen25_7b/sft_dpo",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve Qwen2.5 planner checkpoints through LLaMA-Factory OpenAI-style API.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--variant",
        choices=sorted(VARIANTS),
        default="sft",
        help="Which planner result to serve.",
    )
    parser.add_argument(
        "--adapter-path",
        type=Path,
        default=None,
        help="Override the LoRA adapter path. Use this for a new experiment output.",
    )
    parser.add_argument(
        "--no-adapter",
        action="store_true",
        help="Serve the base model even if --variant points to an adapter.",
    )
    parser.add_argument("--model-path", default=DEFAULTS["model_path"], help="Base model path or HF repo id.")
    parser.add_argument("--template", default=DEFAULTS["template"], help="LLaMA-Factory chat template.")
    parser.add_argument(
        "--infer-backend",
        choices=["huggingface", "vllm", "sglang", "ktransformers"],
        default=DEFAULTS["backend"],
        help="LLaMA-Factory inference backend.",
    )
    parser.add_argument(
        "--infer-dtype",
        choices=["auto", "float16", "bfloat16", "float32"],
        default=DEFAULTS["infer_dtype"],
        help="Inference dtype.",
    )
    parser.add_argument("--host", default=DEFAULTS["host"], help="API bind host.")
    parser.add_argument("--port", type=int, default=DEFAULTS["port"], help="API port.")
    parser.add_argument(
        "--api-model-name",
        default=None,
        help="Model id shown by /v1/models. Requests are OpenAI-compatible.",
    )
    parser.add_argument(
        "--cuda-visible-devices",
        default=None,
        help="Set CUDA_VISIBLE_DEVICES for this server process, e.g. 6 or 6,7.",
    )
    parser.add_argument(
        "--llamafactory-cli",
        default=os.getenv("LLAMAFACTORY_CLI"),
        help="Path to llamafactory-cli. Defaults to PATH lookup.",
    )
    parser.add_argument(
        "--llamafactory-root",
        type=Path,
        default=LLAMA_FACTORY_ROOT,
        help="LLaMA-Factory repository root used as the working directory.",
    )
    parser.add_argument(
        "--config-out",
        type=Path,
        default=None,
        help="Write the generated inference yaml here. Defaults to training/configs/qwen25_7b/.serve_qwen25_7b_<variant>.yaml.",
    )
    parser.add_argument(
        "--write-config-only",
        action="store_true",
        help="Only write the generated yaml and exit.",
    )
    parser.add_argument("--vllm-maxlen", type=int, default=32768, help="Only used when --infer-backend vllm.")
    parser.add_argument("--vllm-gpu-util", type=float, default=0.85, help="Only used when --infer-backend vllm.")
    parser.add_argument("--vllm-max-lora-rank", type=int, default=32, help="Only used when --infer-backend vllm.")
    return parser.parse_args()


def resolve_adapter(args: argparse.Namespace) -> Path | None:
    if args.no_adapter:
        return None

    adapter = args.adapter_path if args.adapter_path is not None else VARIANTS[args.variant]
    if adapter is None:
        return None

    adapter = adapter.expanduser().resolve()
    if not adapter.exists():
        raise FileNotFoundError(
            f"Adapter path does not exist: {adapter}\n"
            f"Train it first or pass --adapter-path to another checkpoint."
        )

    adapter_config = adapter / "adapter_config.json"
    adapter_weights = [
        adapter / "adapter_model.safetensors",
        adapter / "adapter_model.bin",
    ]
    if not adapter_config.exists() or not any(path.exists() for path in adapter_weights):
        raise FileNotFoundError(
            f"Adapter path exists but does not look like a finished LoRA checkpoint: {adapter}\n"
            "Expected adapter_config.json and adapter_model.safetensors or adapter_model.bin.\n"
            "If you want to serve an intermediate checkpoint, pass --adapter-path to that checkpoint directory."
        )

    return adapter


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def build_config(args: argparse.Namespace, adapter: Path | None) -> str:
    lines = [
        f"model_name_or_path: {args.model_path}",
        f"template: {args.template}",
        f"infer_backend: {args.infer_backend}",
        f"infer_dtype: {args.infer_dtype}",
        "trust_remote_code: true",
    ]

    if adapter is not None:
        lines.insert(1, f"adapter_name_or_path: {adapter}")

    if args.infer_backend == "vllm":
        lines.extend(
            [
                f"vllm_maxlen: {args.vllm_maxlen}",
                f"vllm_gpu_util: {args.vllm_gpu_util}",
                f"vllm_max_lora_rank: {args.vllm_max_lora_rank}",
            ]
        )

    return "\n".join(lines) + "\n"


def find_cli(args: argparse.Namespace) -> str:
    if args.llamafactory_cli:
        cli = Path(args.llamafactory_cli).expanduser()
        if cli.exists():
            return str(cli)
        found = shutil.which(str(args.llamafactory_cli))
        if found:
            return found
        raise FileNotFoundError(f"llamafactory-cli not found: {args.llamafactory_cli}")

    candidates = [
        PROJECT_ROOT / ".venv-training-py311/bin/llamafactory-cli",
        shutil.which("llamafactory-cli"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)

    raise FileNotFoundError(
        "llamafactory-cli was not found. Activate the training env or pass --llamafactory-cli."
    )


def main() -> int:
    args = parse_args()
    try:
        adapter = resolve_adapter(args)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    config_out = args.config_out
    if config_out is None:
        config_out = PROJECT_ROOT / f"training/configs/qwen25_7b/.serve_qwen25_7b_{args.variant}.yaml"
    config_out = config_out.expanduser().resolve()
    config_out.parent.mkdir(parents=True, exist_ok=True)
    config_out.write_text(build_config(args, adapter), encoding="utf-8")

    api_model_name = args.api_model_name or f"{DEFAULTS['api_model_prefix']}-{args.variant}"

    print("Planner model server config")
    print(f"  variant: {args.variant}")
    print(f"  model: {args.model_path}")
    print(f"  adapter: {adapter or '(none)'}")
    print(f"  template: {args.template}")
    print(f"  backend: {args.infer_backend}")
    print(f"  endpoint: http://{args.host}:{args.port}/v1")
    print(f"  API_MODEL_NAME: {api_model_name}")
    print(f"  config: {config_out}")

    if args.write_config_only:
        return 0

    try:
        cli = find_cli(args)
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    env = os.environ.copy()
    env["API_HOST"] = args.host
    env["API_PORT"] = str(args.port)
    env["API_MODEL_NAME"] = api_model_name
    if args.cuda_visible_devices:
        env["CUDA_VISIBLE_DEVICES"] = args.cuda_visible_devices

    cmd = [cli, "api", str(config_out)]
    try:
        return subprocess.call(cmd, cwd=str(args.llamafactory_root), env=env)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
