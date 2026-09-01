"""统一调度旅行助手的后训练流水线。

这个脚本只负责串联现有入口，不把各阶段的业务逻辑复制一份。可以重复传入
``--stage``，脚本会按依赖顺序执行所选阶段。每个阶段仍然保留自己的输出目录，
中间失败时会停在失败步骤，并打印可以单独重跑的命令。

常用示例：

  # 只看请求分布，不调用高德和强模型
  python training/scripts/run_pipeline.py \
    --stage sft-request --count 20 --request-source controlled \
    --date-mode mixed

  # 只生成 SFT records
  python training/scripts/run_pipeline.py \
    --stage sft-data --count 20 --request-source controlled \
    --date-mode mixed --workers 1 \
    --sft-dir training/data/planner/sft_runs/reader_smoke

  # 审计并导出上一条命令生成的 SFT 数据
  python training/scripts/run_pipeline.py \
    --stage sft-audit \
    --records training/data/planner/sft_runs/reader_smoke/records.jsonl \
    --sft-dir training/data/planner/sft_runs/reader_smoke \
    --sft-dataset-prefix trip_planner_sft_reader_smoke

  # 从审计后的 SFT records 接着生成通用 DPO 数据
  python training/scripts/run_pipeline.py \
    --stage dpo \
    --records training/data/planner/sft_runs/reader_smoke/export_budget_clean/records.jsonl \
    --output-dir training/data/planner/dpo/reader_smoke

这里的 ``sft-data``、``sft-audit``、``pricing``、``bestofn`` 和 ``dpo`` 是数据处理
流水线；评测和训练需要另外提供模型服务或训练配置，因此也作为显式阶段提供，
不会被默认启动。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRAINING_DIR = PROJECT_ROOT / "training"
SCRIPTS_DIR = TRAINING_DIR / "scripts"
LLAMAFACTORY_BASE_COMMIT = "9a0cfdccfa234304879f83e0c2c17b5ede8121fe"
LLAMAFACTORY_PATCH = TRAINING_DIR / "patches/llamafactory-9a0cfdcc-local.patch"
DEFAULT_LLAMAFACTORY_ROOT = PROJECT_ROOT.parent / "LLaMA-Factory"
LLAMAFACTORY_DATA_DIR = TRAINING_DIR / "data/llamafactory"
DATASET_INFO_PATH = LLAMAFACTORY_DATA_DIR / "dataset_info.json"

SFT_SCRIPT = SCRIPTS_DIR / "planner/data/generate_sft_data.py"
SFT_AUDIT_SCRIPT = SCRIPTS_DIR / "planner/audit/audit_sft_budget_fit.py"
SFT_CLASSIFY_SCRIPT = SCRIPTS_DIR / "planner/audit/classify_sft_budget_usability.py"
SFT_EXPORT_SCRIPT = SCRIPTS_DIR / "planner/data/export_sft_budget_clean_subset.py"

PRICING_COLLECT_SCRIPT = SCRIPTS_DIR / "planner/pricing/collect_attraction_candidates.py"
PRICING_BUCKET_SCRIPT = SCRIPTS_DIR / "planner/pricing/bucket_attraction_price_candidates.py"
PRICING_ESTIMATE_SCRIPT = SCRIPTS_DIR / "planner/pricing/estimate_attraction_prices_with_llm.py"

EVAL_DATA_SCRIPT = SCRIPTS_DIR / "planner/eval/build_eval_set.py"
BESTOFN_PROMPTS_SCRIPT = SCRIPTS_DIR / "planner/bestofn/build_prompts.py"
BESTOFN_CANDIDATES_SCRIPT = SCRIPTS_DIR / "planner/bestofn/generate_candidates.py"
BESTOFN_SELECT_SCRIPT = SCRIPTS_DIR / "planner/bestofn/select_best.py"

DPO_PROMPTS_SCRIPT = SCRIPTS_DIR / "eval/dpo_build_prompts.py"
DPO_CANDIDATES_SCRIPT = SCRIPTS_DIR / "eval/dpo_generate_candidates.py"
DPO_JUDGE_SCRIPT = SCRIPTS_DIR / "eval/dpo_judge_candidates.py"
DPO_PAIRS_SCRIPT = SCRIPTS_DIR / "eval/dpo_build_pairs.py"
DPO_AUDIT_SCRIPT = SCRIPTS_DIR / "eval/dpo_audit_pairs.py"

EVAL_PIPELINE_SCRIPT = SCRIPTS_DIR / "eval/eval_pipeline.py"
VALIDATION_SCRIPT = SCRIPTS_DIR / "validation/validate_trip_plan.py"

STAGE_ORDER = [
    "preflight",
    "sft-request",
    "sft-context",
    "sft-data",
    "sft-audit",
    "pricing",
    "eval-data",
    "bestofn",
    "dpo",
    "eval",
    "validate",
    "train",
]
TODAY_SLUG = date.today().strftime("%y%m%d")
DEFAULT_SFT_DIR = TRAINING_DIR / "data/planner/sft_runs" / f"{TODAY_SLUG}_pipeline"
SFT_PIPELINE_STAGES = {"sft-data", "sft-audit"}
DEFAULT_OUTPUT_DIRS = {
    "pricing": TRAINING_DIR / "data/planner/attraction_prices" / "pipeline",
    "eval-data": TRAINING_DIR / "data/planner" / f"eval_{TODAY_SLUG}",
    "bestofn": TRAINING_DIR / "data/planner/bestofn" / "pipeline",
    "dpo": TRAINING_DIR / "data/planner/dpo" / "pipeline",
    "eval": TRAINING_DIR / "outputs/eval" / "pipeline",
}
REQUIRED_PYTHON_MODULES = ["dotenv", "httpx", "openai", "pydantic", "pydantic_settings"]
# These imports are only needed when the final ``train`` stage is selected.
# Keeping them out of the data-only preflight makes it possible to inspect or
# generate requests without installing the GPU training stack first.
REQUIRED_TRAINING_MODULES = [
    "accelerate",
    "datasets",
    "deepspeed",
    "einops",
    "omegaconf",
    "peft",
    "torch",
    "torchdata",
    "transformers",
    "trl",
    "yaml",
    "matplotlib",
]


class PipelineError(RuntimeError):
    """流水线参数或前置条件不满足。"""


def project_path(value: Path | str) -> Path:
    """把相对项目路径转换成绝对路径。"""
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


def relative_or_absolute(path: Path) -> str:
    """优先用项目内相对路径显示命令，项目外路径保留绝对路径。"""
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def safe_slug(value: str) -> str:
    """生成适合作为数据集名的短标识。"""
    slug = re.sub(r"[^0-9a-zA-Z._-]+", "_", value.strip())
    return slug.strip("_") or "pipeline"


def default_python() -> str:
    """优先使用项目训练环境；没有时沿用当前解释器。"""
    project_python = PROJECT_ROOT / ".venv-training-py311/bin/python3"
    if project_python.is_file() and os.access(project_python, os.X_OK):
        return str(project_python)
    return sys.executable


def selected_python(args: argparse.Namespace) -> str:
    if args.python and "/" not in args.python:
        resolved = shutil.which(args.python)
        value = Path(resolved) if resolved else project_path(args.python)
    else:
        value = project_path(args.python) if args.python else Path(default_python())
    if not value.is_file() or not os.access(value, os.X_OK):
        raise PipelineError(f"Python 解释器不存在或不可执行：{value}")
    return str(value)


def normalize_stages(values: Sequence[str] | None) -> list[str]:
    """补上 preflight，并按依赖顺序去重。"""
    requested = list(values or ["preflight"])
    unknown = sorted(set(requested) - set(STAGE_ORDER))
    if unknown:
        raise PipelineError(f"未知阶段：{', '.join(unknown)}")
    if "preflight" not in requested:
        requested.insert(0, "preflight")
    return sorted(set(requested), key=STAGE_ORDER.index)


def stage_output_dir(args: argparse.Namespace, stage: str, stages: Sequence[str]) -> Path:
    """取得阶段输出目录。单阶段时 --output-dir 是通用快捷写法。"""
    explicit_name = {
        "pricing": "pricing_dir",
        "eval-data": "eval_data_dir",
        "bestofn": "bestofn_dir",
        "dpo": "dpo_dir",
        "eval": "eval_dir",
    }[stage]
    explicit = getattr(args, explicit_name)
    if explicit:
        return project_path(explicit)
    active_stages = [item for item in stages if item != "preflight"]
    if args.output_dir:
        if len(active_stages) != 1:
            raise PipelineError("同时运行多个阶段时，请分别使用 --sft-dir、--dpo-dir 等阶段目录参数")
        if active_stages[0] != stage:
            raise PipelineError(f"--output-dir 只能用于当前唯一阶段 {active_stages[0]}，不能用于 {stage}")
        return project_path(args.output_dir)
    return DEFAULT_OUTPUT_DIRS[stage]


def sft_output_dir(args: argparse.Namespace, stages: Sequence[str]) -> Path:
    """取得 SFT 数据 run 目录，供生成和审计阶段共用。"""
    if args.sft_dir:
        return project_path(args.sft_dir)
    active_stages = [item for item in stages if item != "preflight"]
    if args.output_dir:
        if all(item in SFT_PIPELINE_STAGES for item in active_stages):
            return project_path(args.output_dir)
        if len(active_stages) != 1:
            raise PipelineError("同时运行多个阶段时，请分别使用 --sft-dir、--dpo-dir 等阶段目录参数")
        raise PipelineError(f"--output-dir 只能用于当前唯一阶段 {active_stages[0]}，不能用于 SFT 数据目录")
    return DEFAULT_SFT_DIR


def sft_dataset_prefix(args: argparse.Namespace, stages: Sequence[str]) -> str:
    """取得当前 SFT 阶段导出的数据集前缀。"""
    output_dir = sft_output_dir(args, stages)
    prefix = args.sft_dataset_prefix or f"trip_planner_sft_{safe_slug(output_dir.name)}"
    return safe_slug(prefix)


def bestofn_dataset_prefix(args: argparse.Namespace, stages: Sequence[str]) -> str:
    """取得当前 Best-of-N 阶段导出的数据集前缀。"""
    output_dir = stage_output_dir(args, "bestofn", stages)
    prefix = args.bestofn_dataset_prefix or f"trip_planner_bestofn_{safe_slug(output_dir.name)}"
    return safe_slug(prefix)


def dpo_dataset_prefix(args: argparse.Namespace, stages: Sequence[str]) -> str:
    """取得当前 DPO 阶段导出的数据集前缀。"""
    output_dir = stage_output_dir(args, "dpo", stages)
    prefix = args.dpo_dataset_prefix or f"trip_planner_dpo_{safe_slug(output_dir.name)}"
    return safe_slug(prefix)


def generated_training_datasets(
    args: argparse.Namespace, stages: Sequence[str]
) -> tuple[str, str, str] | None:
    """返回本次流水线最后一个训练数据阶段的 train/val 数据集名和类型。

    DPO 优先于 Best-of-N，Best-of-N 优先于普通 SFT。这样同一次运行包含
    ``sft-data -> sft-audit -> bestofn -> dpo -> train`` 时，
    训练自动接到最后生成的 DPO 数据。
    """
    if "dpo" in stages:
        prefix = dpo_dataset_prefix(args, stages)
        return f"{prefix}_train", f"{prefix}_val", "dpo"
    if "bestofn" in stages:
        prefix = bestofn_dataset_prefix(args, stages)
        return f"{prefix}_sft_train", f"{prefix}_sft_val", "sft"
    if "sft-audit" in stages:
        prefix = sft_dataset_prefix(args, stages)
        return f"{prefix}_train", f"{prefix}_val", "sft"
    return None


def resolve_input_records(args: argparse.Namespace, stage: str, stages: Sequence[str]) -> Path:
    """解析需要 records.jsonl 的阶段输入，支持 SFT/评估集自动交接。"""
    if args.records:
        return project_path(args.records)
    if stage in {"pricing", "bestofn", "dpo"} and any(item in SFT_PIPELINE_STAGES for item in stages):
        return sft_output_dir(args, stages) / "records.jsonl"
    if stage == "eval" and "eval-data" in stages:
        return stage_output_dir(args, "eval-data", stages) / "records.jsonl"
    raise PipelineError(
        f"阶段 {stage} 需要输入 records.jsonl，请传 --records，或在同一次运行中先选择可自动交接的阶段"
    )


def append_option(command: list[str], flag: str, value: object | None) -> None:
    """值不为空时追加一个命令行选项。"""
    if value is None:
        return
    command.extend([flag, str(value)])


def run_step(
    args: argparse.Namespace,
    label: str,
    command: Sequence[str],
    env: dict[str, str] | None = None,
    cwd: Path | None = None,
) -> None:
    """打印并执行一个子脚本。"""
    display_command = redact_command(command)
    print(f"\n[{label}]", flush=True)
    print("$ " + shlex.join(display_command), flush=True)
    if args.dry_run:
        return
    try:
        subprocess.run(list(command), cwd=cwd or PROJECT_ROOT, check=True, env=env)
    except subprocess.CalledProcessError as exc:
        raise PipelineError(f"{label}失败，退出码={exc.returncode}") from exc


def redact_command(command: Sequence[str]) -> list[str]:
    """隐藏显式传入的密钥，避免日志把密钥打印出来。"""
    secret_flags = {"--api-key"}
    result: list[str] = []
    hide_next = False
    for item in command:
        if hide_next:
            result.append("***")
            hide_next = False
            continue
        result.append(str(item))
        if item in secret_flags:
            hide_next = True
    return result


def require_file(path: Path, description: str) -> None:
    if not path.is_file():
        raise PipelineError(f"找不到{description}：{relative_or_absolute(path)}")


def require_nonempty_file(path: Path, description: str) -> None:
    require_file(path, description)
    if path.stat().st_size == 0:
        raise PipelineError(f"{description}为空：{relative_or_absolute(path)}")


def require_nonempty_json_array(path: Path, description: str) -> None:
    """确认导出的 JSON 数组至少有一条样本。"""
    require_file(path, description)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PipelineError(f"{description}不是有效 JSON：{relative_or_absolute(path)}") from exc
    if not isinstance(data, list) or not data:
        raise PipelineError(f"{description}没有可训练样本：{relative_or_absolute(path)}")


def refuse_existing_run(path: Path, artifacts: Iterable[Path], args: argparse.Namespace) -> None:
    """避免不加 --resume 时把两个实验混写到一个目录。"""
    if args.dry_run or args.resume:
        return
    existing = [item for item in artifacts if item.exists()]
    if existing:
        names = ", ".join(relative_or_absolute(item) for item in existing[:4])
        suffix = " ..." if len(existing) > 4 else ""
        raise PipelineError(f"输出目录已有产物：{names}{suffix}。请换目录，或显式传 --resume。")


def usage_log_env(output_dir: Path) -> dict[str, str]:
    """为调用强模型的子脚本提供当前 run 的 usage 日志路径。"""
    env = os.environ.copy()
    env.setdefault("DATA_GEN_USAGE_LOG", str(output_dir / "llm_usage.jsonl"))
    return env


def write_manifest(args: argparse.Namespace, stage: str, output_dir: Path, stages: Sequence[str]) -> None:
    """记录总入口实际使用的参数，便于复现实验。"""
    if args.dry_run:
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "stage": stage,
        "stages_in_invocation": list(stages),
        "project_root": str(PROJECT_ROOT),
        "python": selected_python(args),
        "argv": redact_command(sys.argv),
        "output_dir": str(output_dir),
    }
    (output_dir / "pipeline_manifest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def build_sft_command(args: argparse.Namespace, python: str, output_dir: Path | None = None) -> list[str]:
    command = [
        python,
        str(SFT_SCRIPT),
        "--count",
        str(args.count),
        "--start-index",
        str(args.start_index),
        "--seed",
        str(args.seed),
        "--request-source",
        args.request_source,
        "--date-mode",
        args.date_mode,
        "--workers",
        str(args.workers),
        "--sample-retries",
        str(args.sample_retries),
        "--val-ratio",
        str(args.val_ratio),
        "--historical-weather-provider",
        args.historical_weather_provider,
    ]
    append_option(command, "--output-dir", output_dir)
    if args.resume:
        command.append("--resume")
    if args.target_budget_mix:
        command.extend(["--target-budget-mix", args.target_budget_mix])
    if args.disallow_budget_strictness_none:
        command.append("--disallow-budget-strictness-none")
    if args.teacher_model_provider:
        command.extend(["--teacher-model-provider", args.teacher_model_provider])
    if args.teacher_model:
        command.extend(["--teacher-model", args.teacher_model])
    append_option(command, "--amap-qps-limit", args.amap_qps_limit)
    if args.target_successes:
        command.extend(["--target-successes", str(args.target_successes)])
    append_option(command, "--budget-context-min-ratio", args.budget_context_min_ratio)
    command.extend(["--budget-context-retry-stride", str(args.budget_context_retry_stride)])
    command.extend(["--temperature", str(args.temperature)])
    if args.max_output_tokens:
        command.extend(["--max-output-tokens", str(args.max_output_tokens)])
    append_option(command, "--output-base-tokens", args.output_base_tokens)
    append_option(command, "--output-tokens-per-day", args.output_tokens_per_day)
    append_option(command, "--output-retry-tokens", args.output_retry_tokens)
    append_option(command, "--output-tokens-cap", args.output_tokens_cap)
    return command


def run_sft_request(args: argparse.Namespace, python: str) -> None:
    command = build_sft_command(args, python)
    command.extend(["--dry-run-requests", "--dry-run-summary"])
    run_step(args, "SFT 请求分布 smoke", command)


def run_sft_context(args: argparse.Namespace, python: str) -> None:
    command = build_sft_command(args, python)
    command.append("--dry-run-context")
    run_step(args, "PlannerContext smoke", command)


def resolve_sft_records(args: argparse.Namespace, stages: Sequence[str]) -> Path:
    """取得 SFT 审计输入。显式 --records 优先，否则读取当前 SFT run。"""
    if args.records:
        return project_path(args.records)
    return sft_output_dir(args, stages) / "records.jsonl"


def run_sft_data(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = sft_output_dir(args, stages)
    refuse_existing_run(output_dir, [output_dir / "records.jsonl"], args)
    write_manifest(args, "sft-data", output_dir, stages)

    run_step(args, "SFT 数据生成", build_sft_command(args, python, output_dir), env=usage_log_env(output_dir))
    records = output_dir / "records.jsonl"
    if not args.dry_run:
        require_nonempty_file(records, "SFT records.jsonl")


def run_sft_audit(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = sft_output_dir(args, stages)
    records = resolve_sft_records(args, stages)
    write_manifest(args, "sft-audit", output_dir, stages)
    if not args.dry_run:
        require_nonempty_file(records, "SFT records.jsonl")

    audit_dir = output_dir / "audit_budget"
    classification_dir = output_dir / "classification"
    export_dir = output_dir / "export_budget_clean"
    run_step(
        args,
        "SFT 预算审计",
        [
            python,
            str(SFT_AUDIT_SCRIPT),
            "--records",
            str(records),
            "--output-dir",
            str(audit_dir),
        ],
    )
    audit_rows = audit_dir / "audit_rows.jsonl"
    if not args.dry_run:
        require_file(audit_rows, "预算审计结果")

    run_step(
        args,
        "SFT 可用性分类",
        [
            python,
            str(SFT_CLASSIFY_SCRIPT),
            "--audit-rows",
            str(audit_rows),
            "--output-dir",
            str(classification_dir),
        ],
    )
    classification = classification_dir / "record_classification.jsonl"
    if not args.dry_run:
        require_file(classification, "SFT 分类结果")

    dataset_prefix = sft_dataset_prefix(args, stages)
    run_step(
        args,
        "导出预算干净 SFT 子集",
        [
            python,
            str(SFT_EXPORT_SCRIPT),
            "--records",
            str(records),
            "--classification",
            str(classification),
            "--output-dir",
            str(export_dir),
            "--category",
            args.sft_category,
            "--dataset-prefix",
            dataset_prefix,
            "--val-ratio",
            str(args.val_ratio),
        ],
    )
    lf_dir = LLAMAFACTORY_DATA_DIR / "generated"
    if not args.dry_run:
        require_nonempty_json_array(lf_dir / f"{dataset_prefix}_train.json", "导出的 SFT train")
        require_nonempty_json_array(lf_dir / f"{dataset_prefix}_val.json", "导出的 SFT val")
    run_validation_step(args, python, "sft", lf_dir / f"{dataset_prefix}_train.json", "校验 SFT train")
    run_validation_step(args, python, "sft", lf_dir / f"{dataset_prefix}_val.json", "校验 SFT val")


def run_pricing(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = stage_output_dir(args, "pricing", stages)
    if args.request_source not in {"template", "controlled"}:
        raise PipelineError("pricing 阶段的 --request-source 只能是 template 或 controlled")
    records = None if args.collect_context else resolve_input_records(args, "pricing", stages)
    candidate_path = output_dir / "generated/attraction_candidates.jsonl"
    refuse_existing_run(output_dir, [candidate_path], args)
    write_manifest(args, "pricing", output_dir, stages)

    command = [
        python,
        str(PRICING_COLLECT_SCRIPT),
        "--output-dir",
        str(output_dir),
        "--count",
        str(args.count),
        "--start-index",
        str(args.start_index),
        "--seed",
        str(args.seed),
        "--request-source",
        args.request_source,
        "--date-mode",
        args.date_mode,
        "--workers",
        str(args.workers),
        "--historical-weather-provider",
        args.historical_weather_provider,
    ]
    if args.collect_context:
        command.append("--collect-context")
    else:
        if not args.dry_run:
            require_file(records, "票价候选收集的 records.jsonl")
        command.extend(["--records", str(records)])
    run_step(args, "景点票价候选收集", command)
    bucket_path = output_dir / "generated" / f"request_count_ge{args.min_request_count}_bucketed_candidates.jsonl"
    run_step(
        args,
        "景点票价候选分桶",
        [
            python,
            str(PRICING_BUCKET_SCRIPT),
            "--input",
            str(candidate_path),
            "--output-dir",
            str(output_dir),
            "--min-request-count",
            str(args.min_request_count),
        ],
    )
    if not args.dry_run:
        require_file(bucket_path, "票价候选分桶结果")

    if args.estimate_prices:
        run_step(
            args,
            "强模型估算景点票价",
            [
                python,
                str(PRICING_ESTIMATE_SCRIPT),
                "--input",
                str(bucket_path),
                "--output-dir",
                str(output_dir),
                "--min-request-count",
                str(args.min_request_count),
                "--batch-size",
                str(args.price_batch_size),
                "--limit",
                str(args.price_limit),
                "--retries",
                str(args.price_retries),
                *(["--resume"] if args.resume else []),
            ],
            env=usage_log_env(output_dir),
        )


def run_eval_data(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = stage_output_dir(args, "eval-data", stages)
    records = output_dir / "records.jsonl"
    refuse_existing_run(output_dir, [records], args)
    write_manifest(args, "eval-data", output_dir, stages)
    request_source = args.request_source
    if request_source == "budget_supplement":
        raise PipelineError("eval-data 不支持 request-source=budget_supplement，请使用 template、llm 或 controlled")
    id_prefix = args.eval_id_prefix or safe_slug(output_dir.name)
    command = [
        python,
        str(EVAL_DATA_SCRIPT),
        "--count",
        str(args.count),
        "--start-index",
        str(args.start_index),
        "--seed",
        str(args.seed),
        "--id-prefix",
        id_prefix,
        "--output-dir",
        str(output_dir),
        "--request-source",
        request_source,
        "--date-mode",
        args.date_mode,
        "--difficulty",
        args.difficulty,
        "--workers",
        str(args.workers),
        "--historical-weather-provider",
        args.historical_weather_provider,
    ]
    if args.resume:
        command.append("--resume")
    run_step(args, "构建冻结评估集", command)
    if not args.dry_run:
        require_nonempty_file(records, "冻结评估集 records.jsonl")


def run_bestofn(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = stage_output_dir(args, "bestofn", stages)
    records = resolve_input_records(args, "bestofn", stages)
    prompts = output_dir / "prompts.jsonl"
    candidates = output_dir / "candidates.jsonl"
    refuse_existing_run(output_dir, [candidates], args)
    write_manifest(args, "bestofn", output_dir, stages)
    if not args.dry_run:
        require_file(records, "Best-of-N 输入 records.jsonl")

    prompt_command = [
        python,
        str(BESTOFN_PROMPTS_SCRIPT),
        "--records",
        str(records),
        "--output",
        str(prompts),
        "--source",
        args.bestofn_source or safe_slug(output_dir.name),
        "--seed",
        str(args.seed),
    ]
    if args.limit:
        prompt_command.extend(["--limit", str(args.limit)])
    if args.bestofn_shuffle:
        prompt_command.append("--shuffle")
    if args.bestofn_stratified_smoke20:
        prompt_command.append("--stratified-smoke20")
    if args.resume:
        prompt_command.append("--resume")
    run_step(args, "Best-of-N 构建 prompt", prompt_command)

    candidate_command = [
        python,
        str(BESTOFN_CANDIDATES_SCRIPT),
        "--prompts",
        str(prompts),
        "--output",
        str(candidates),
        "--base-url",
        args.bestofn_base_url,
        "--api-model",
        args.bestofn_api_model,
        "--workers",
        str(args.workers),
    ]
    if args.limit:
        candidate_command.extend(["--limit", str(args.limit)])
    for spec in args.bestofn_spec:
        candidate_command.extend(["--spec", spec])
    if args.api_key:
        candidate_command.extend(["--api-key", args.api_key])
    if args.resume:
        candidate_command.append("--resume")
    if args.trust_env:
        candidate_command.append("--trust-env")
    run_step(args, "Best-of-N 候选生成", candidate_command)

    prefix = bestofn_dataset_prefix(args, stages)
    lf_dir = LLAMAFACTORY_DATA_DIR / "generated"
    select_command = [
        python,
        str(BESTOFN_SELECT_SCRIPT),
        "--prompts",
        str(prompts),
        "--candidates",
        str(candidates),
        "--selected-output",
        str(output_dir / "selected.jsonl"),
        "--summary-output",
        str(output_dir / "selection_summary.json"),
        "--val-ratio",
        str(args.val_ratio),
        "--seed",
        str(args.seed),
        "--lf-sft-train",
        str(lf_dir / f"{prefix}_sft_train.json"),
        "--lf-sft-val",
        str(lf_dir / f"{prefix}_sft_val.json"),
        "--lf-pair-train",
        str(lf_dir / f"{prefix}_pair_train.json"),
        "--lf-pair-val",
        str(lf_dir / f"{prefix}_pair_val.json"),
        "--sft-train-name",
        f"{prefix}_sft_train",
        "--sft-val-name",
        f"{prefix}_sft_val",
        "--pair-train-name",
        f"{prefix}_pair_train",
        "--pair-val-name",
        f"{prefix}_pair_val",
        "--update-dataset-info",
    ]
    if args.bestofn_no_hard_gate:
        select_command.append("--no-hard-gate")
    if args.bestofn_rejected_allow_nonschema:
        select_command.append("--rejected-allow-nonschema")
    run_step(args, "Best-of-N 选择并导出", select_command)
    if not args.dry_run:
        require_nonempty_json_array(lf_dir / f"{prefix}_sft_train.json", "导出的 Best-of-N SFT train")
        require_nonempty_json_array(lf_dir / f"{prefix}_sft_val.json", "导出的 Best-of-N SFT val")
    run_validation_step(args, python, "sft", lf_dir / f"{prefix}_sft_train.json", "校验 Best-of-N SFT train")
    run_validation_step(args, python, "dpo", lf_dir / f"{prefix}_pair_train.json", "校验 Best-of-N DPO train")


def run_dpo(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = stage_output_dir(args, "dpo", stages)
    records = resolve_input_records(args, "dpo", stages)
    prompts = output_dir / "prompts.jsonl"
    candidates = output_dir / "candidates.jsonl"
    judgements = output_dir / "judgements.jsonl"
    pairs = output_dir / "pairs.jsonl"
    refuse_existing_run(output_dir, [candidates, judgements, pairs], args)
    write_manifest(args, "dpo", output_dir, stages)
    if not args.dry_run:
        require_file(records, "DPO 输入 records.jsonl")

    prompt_command = [
        python,
        str(DPO_PROMPTS_SCRIPT),
        "--records",
        str(records),
        "--output",
        str(prompts),
        "--source",
        args.dpo_source or safe_slug(output_dir.name),
        "--seed",
        str(args.seed),
    ]
    if args.limit:
        prompt_command.extend(["--limit", str(args.limit)])
    if args.dpo_shuffle:
        prompt_command.append("--shuffle")
    if args.resume:
        prompt_command.append("--resume")
    run_step(args, "DPO 构建 prompt", prompt_command)

    candidate_command = [
        python,
        str(DPO_CANDIDATES_SCRIPT),
        "--prompts",
        str(prompts),
        "--output",
        str(candidates),
        "--workers",
        str(args.dpo_workers),
        "--base-url",
        args.dpo_base_url,
        "--base-api-model",
        args.dpo_base_api_model,
        "--sft-base-url",
        args.dpo_sft_base_url,
        "--sft-api-model",
        args.dpo_sft_api_model,
    ]
    if args.limit:
        candidate_command.extend(["--limit", str(args.limit)])
    if args.dpo_no_base_low:
        candidate_command.append("--no-base-low")
    if args.dpo_no_base_high:
        candidate_command.append("--no-base-high")
    if args.dpo_no_sft_low:
        candidate_command.append("--no-sft-low")
    if args.dpo_include_strong_low:
        candidate_command.append("--include-strong-low")
    if args.dpo_include_strong_high:
        candidate_command.append("--include-strong-high")
    if args.dpo_strong_provider:
        candidate_command.extend(["--strong-provider", args.dpo_strong_provider])
    if args.dpo_strong_label:
        candidate_command.extend(["--strong-label", args.dpo_strong_label])
    if args.api_key:
        candidate_command.extend(["--api-key", args.api_key])
    if args.resume:
        candidate_command.append("--resume")
    if args.trust_env:
        candidate_command.append("--trust-env")
    run_step(args, "DPO 多候选生成", candidate_command, env=usage_log_env(output_dir))

    judge_command = [
        python,
        str(DPO_JUDGE_SCRIPT),
        "--candidates",
        str(candidates),
        "--output",
        str(judgements),
        "--workers",
        str(args.judge_workers),
    ]
    if args.resume:
        judge_command.append("--resume")
    run_step(args, "DPO 强模型 judge", judge_command, env=usage_log_env(output_dir))

    prefix = dpo_dataset_prefix(args, stages)
    lf_dir = LLAMAFACTORY_DATA_DIR / "generated"
    pair_command = [
        python,
        str(DPO_PAIRS_SCRIPT),
        "--prompts",
        str(prompts),
        "--candidates",
        str(candidates),
        "--judgements",
        str(judgements),
        "--output",
        str(pairs),
        "--train-output",
        str(output_dir / "pairs_train.jsonl"),
        "--val-output",
        str(output_dir / "pairs_val.jsonl"),
        "--lf-output-dir",
        str(lf_dir),
        "--lf-copy-dir",
        str(output_dir / "llamafactory"),
        "--lf-train-file",
        f"{prefix}_train.json",
        "--lf-val-file",
        f"{prefix}_val.json",
        "--dataset-train-name",
        f"{prefix}_train",
        "--dataset-val-name",
        f"{prefix}_val",
        "--val-ratio",
        str(args.val_ratio),
        "--seed",
        str(args.seed),
        "--min-chosen-score",
        str(args.dpo_min_chosen_score),
        "--min-score-gap",
        str(args.dpo_min_score_gap),
        "--tag-gap",
        str(args.dpo_tag_gap),
        "--max-pairs-per-prompt",
        str(args.dpo_max_pairs_per_prompt),
    ]
    run_step(args, "DPO 构造 chosen/rejected", pair_command)
    if not args.dry_run:
        require_nonempty_json_array(lf_dir / f"{prefix}_train.json", "导出的 DPO train")
        require_nonempty_json_array(lf_dir / f"{prefix}_val.json", "导出的 DPO val")
    run_validation_step(args, python, "dpo", lf_dir / f"{prefix}_train.json", "校验 DPO train")
    run_validation_step(args, python, "dpo", lf_dir / f"{prefix}_val.json", "校验 DPO val")

    run_step(
        args,
        "DPO 数据审计",
        [
            python,
            str(DPO_AUDIT_SCRIPT),
            "--prompts",
            str(prompts),
            "--candidates",
            str(candidates),
            "--judgements",
            str(judgements),
            "--pairs",
            str(pairs),
            "--output",
            str(output_dir / "audit_report.md"),
            "--sample-size",
            str(args.dpo_audit_sample_size),
        ],
    )


def run_validation_step(
    args: argparse.Namespace,
    python: str,
    kind: str,
    path: Path,
    label: str,
) -> None:
    """校验一个已经导出的 LLaMA-Factory 文件。"""
    if not args.dry_run:
        require_file(path, f"{kind} 校验输入")
    command = [python, str(VALIDATION_SCRIPT), f"--{kind}", str(path)]
    if kind == "dpo":
        command.append("--validate-rejected")
    run_step(args, label, command)


def run_validate(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    """独立校验已有的 SFT、DPO 或评估集文件。"""
    targets: list[tuple[str, Path, str]] = []
    if args.validate_sft:
        targets.append(("sft", project_path(args.validate_sft), "校验 SFT"))
    if args.validate_dpo:
        targets.append(("dpo", project_path(args.validate_dpo), "校验 DPO"))
    if args.validate_eval_gt:
        targets.append(("eval-gt", project_path(args.validate_eval_gt), "校验 Eval GT"))

    if not targets and "sft-audit" in stages:
        prefix = sft_dataset_prefix(args, stages)
        lf_dir = LLAMAFACTORY_DATA_DIR / "generated"
        targets.extend(
            [
                ("sft", lf_dir / f"{prefix}_train.json", "校验 SFT train"),
                ("sft", lf_dir / f"{prefix}_val.json", "校验 SFT val"),
            ]
        )
    if not targets and "dpo" in stages:
        prefix = dpo_dataset_prefix(args, stages)
        lf_dir = LLAMAFACTORY_DATA_DIR / "generated"
        targets.extend(
            [
                ("dpo", lf_dir / f"{prefix}_train.json", "校验 DPO train"),
                ("dpo", lf_dir / f"{prefix}_val.json", "校验 DPO val"),
            ]
        )
    if not targets:
        raise PipelineError("validate 阶段需要 --validate-sft、--validate-dpo 或 --validate-eval-gt")

    for kind, path, label in targets:
        if kind == "eval-gt":
            if not args.dry_run:
                require_file(path, "Eval GT 校验输入")
            run_step(args, label, [python, str(VALIDATION_SCRIPT), "--eval-gt", str(path)])
        else:
            run_validation_step(args, python, kind, path, label)


def run_eval(args: argparse.Namespace, python: str, stages: Sequence[str]) -> None:
    output_dir = stage_output_dir(args, "eval", stages)
    records = resolve_input_records(args, "eval", stages)
    if not args.model_name or not args.api_model:
        raise PipelineError("eval 阶段必须同时传 --model-name 和 --api-model")
    if not args.eval_skip_generate:
        refuse_existing_run(output_dir, [output_dir / safe_slug(args.model_name) / "generations.jsonl"], args)
    write_manifest(args, "eval", output_dir, stages)
    if not args.dry_run:
        require_file(records, "评测输入 records.jsonl")
    command = [
        python,
        str(EVAL_PIPELINE_SCRIPT),
        "--records",
        str(records),
        "--model-name",
        args.model_name,
        "--api-model",
        args.api_model,
        "--base-url",
        args.base_url,
        "--output-dir",
        str(output_dir),
        "--workers",
        str(args.workers),
        "--temperature",
        str(args.temperature),
        "--timeout",
        str(args.timeout),
        "--connect-timeout",
        str(args.connect_timeout),
        "--judge-workers",
        str(args.judge_workers),
    ]
    if args.api_key:
        command.extend(["--api-key", args.api_key])
    if args.limit:
        command.extend(["--limit", str(args.limit)])
    if args.resume:
        command.append("--resume")
    if args.resume_include_failed:
        command.append("--resume-include-failed")
    if args.max_tokens:
        command.extend(["--max-tokens", str(args.max_tokens)])
    if args.trust_env:
        command.append("--trust-env")
    if args.no_auto_openai_path:
        command.append("--no-auto-openai-path")
    if args.eval_skip_generate:
        command.append("--skip-generate")
    if args.eval_skip_rule:
        command.append("--skip-rule")
    if args.eval_run_judge:
        command.append("--run-judge")
    run_step(args, "单模型评测流水线", command, env=usage_log_env(output_dir))


def find_llamafactory_root(args: argparse.Namespace) -> Path:
    """找到训练使用的 LLaMA-Factory 源码目录。"""
    configured = args.llamafactory_root or os.getenv("LLAMAFACTORY_ROOT")
    root = project_path(configured) if configured else DEFAULT_LLAMAFACTORY_ROOT
    if root.is_dir():
        return root.resolve()
    if args.dry_run:
        return root
    raise PipelineError(
        f"找不到 LLaMA-Factory 源码目录：{relative_or_absolute(root)}；"
        "请传 --llamafactory-root PATH，或设置 LLAMAFACTORY_ROOT"
    )


def find_llamafactory_cli(args: argparse.Namespace, root: Path) -> Path:
    if args.llamafactory_cli:
        path = project_path(args.llamafactory_cli)
        if path.is_file() and os.access(path, os.X_OK):
            return path
        if args.dry_run:
            return path
        raise PipelineError(f"LLaMA-Factory 命令不存在或不可执行：{path}")
    candidates = [
        root / ".venv/bin/llamafactory-cli",
        PROJECT_ROOT / ".venv-training-py311/bin/llamafactory-cli",
        Path(shutil.which("llamafactory-cli") or ""),
    ]
    for path in candidates:
        if path.is_file() and os.access(path, os.X_OK):
            return path
    if args.dry_run:
        return Path("llamafactory-cli")
    raise PipelineError("找不到 llamafactory-cli，请先激活训练环境，或传 --llamafactory-cli PATH")


def verify_llamafactory_checkout(root: Path, allow_unpatched: bool = False) -> None:
    """确认源码基线和本项目记录的本地补丁一致。"""
    if allow_unpatched:
        return
    if not (root / ".git").exists():
        raise PipelineError(f"LLaMA-Factory 不是 Git checkout，无法确认补丁版本：{relative_or_absolute(root)}")
    if not LLAMAFACTORY_PATCH.is_file():
        raise PipelineError(f"找不到项目内的 LLaMA-Factory 补丁：{relative_or_absolute(LLAMAFACTORY_PATCH)}")

    try:
        revision = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise PipelineError(f"无法读取 LLaMA-Factory Git 版本：{relative_or_absolute(root)}") from exc

    if revision != LLAMAFACTORY_BASE_COMMIT:
        raise PipelineError(
            "LLaMA-Factory 基础 commit 不匹配："
            f"当前 {revision[:12] or 'unknown'}，需要 {LLAMAFACTORY_BASE_COMMIT[:12]}；"
            f"详见 {relative_or_absolute(LLAMAFACTORY_PATCH)}"
        )

    reverse_check = subprocess.run(
        ["git", "-C", str(root), "apply", "--reverse", "--check", str(LLAMAFACTORY_PATCH)],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if reverse_check.returncode == 0:
        return

    forward_check = subprocess.run(
        ["git", "-C", str(root), "apply", "--check", str(LLAMAFACTORY_PATCH)],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if forward_check.returncode == 0:
        raise PipelineError(
            "LLaMA-Factory 还没有应用项目补丁："
            f"请执行 git -C {shlex.quote(str(root))} apply {shlex.quote(str(LLAMAFACTORY_PATCH))}"
        )
    detail = (reverse_check.stderr or forward_check.stderr).strip().splitlines()
    suffix = f"；git apply 检查：{detail[0]}" if detail else ""
    raise PipelineError(f"LLaMA-Factory 当前改动与项目补丁不一致{suffix}")


def config_has_key(config: Path, key: str) -> bool:
    """检查简单 YAML 配置中是否声明了某个顶层 key。"""
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*:")
    try:
        lines = config.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise PipelineError(f"无法读取训练配置：{relative_or_absolute(config)}") from exc
    return any(pattern.match(line) and not line.lstrip().startswith("#") for line in lines)


def config_scalar(config: Path, key: str) -> str | None:
    """读取训练 YAML 中一个简单的顶层字符串值。

    这里只读取 dataset、stage、output_dir 等标量，不引入额外 YAML 依赖；
    训练时仍由 LLaMA-Factory 负责完整解析配置。
    """
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*:\s*(.*?)\s*$")
    try:
        lines = config.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise PipelineError(f"无法读取训练配置：{relative_or_absolute(config)}") from exc

    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = pattern.match(line)
        if not match:
            continue
        value = re.split(r"\s+#", match.group(1), maxsplit=1)[0].strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if value.lower() in {"", "null", "none", "~"}:
            return None
        return value
    return None


def split_dataset_names(value: str | None) -> list[str]:
    """把 LLaMA-Factory 的逗号分隔数据集参数拆成名称列表。"""
    return [item.strip() for item in (value or "").split(",") if item.strip()]


def validate_registered_datasets(dataset_dir: Path, names: Sequence[str]) -> None:
    """在训练启动前确认 dataset_info 和实际数据文件都存在。"""
    if not names:
        return
    require_file(dataset_dir / "dataset_info.json", "LLaMA-Factory dataset_info.json")
    try:
        dataset_info = json.loads((dataset_dir / "dataset_info.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PipelineError(f"LLaMA-Factory dataset_info.json 不是有效 JSON：{relative_or_absolute(dataset_dir)}") from exc

    for name in names:
        entry = dataset_info.get(name) if isinstance(dataset_info, dict) else None
        if not isinstance(entry, dict) or not entry.get("file_name"):
            raise PipelineError(
                f"dataset_info 中没有数据集 {name}；请先完成数据导出，或检查训练数据目录："
                f"{relative_or_absolute(dataset_dir)}"
            )
        file_path = Path(str(entry["file_name"]))
        if not file_path.is_absolute():
            file_path = dataset_dir / file_path
        require_nonempty_file(file_path, f"数据集 {name}")


def resolve_train_output_dir(
    args: argparse.Namespace,
    config: Path,
    generated_plan: tuple[str, str, str] | None,
    train_name: str | None,
) -> Path | None:
    """解析训练输出目录，并把项目配置中的相对路径固定到主项目根目录。"""
    if args.train_output_dir:
        return project_path(args.train_output_dir).resolve()

    if generated_plan and train_name:
        # 数据阶段的输出名带有本轮 run 标识，训练输出也按本轮隔离，避免覆盖旧实验。
        return (
            TRAINING_DIR
            / "outputs/pipeline"
            / f"{safe_slug(config.stem)}_{safe_slug(train_name)}"
        ).resolve()

    raw_output_dir = config_scalar(config, "output_dir")
    if not raw_output_dir:
        return None
    output_dir = Path(raw_output_dir)
    return (output_dir if output_dir.is_absolute() else PROJECT_ROOT / output_dir).resolve()


def build_training_overrides(
    args: argparse.Namespace,
    stages: Sequence[str],
    config: Path,
    *,
    validate_data: bool = True,
    show_summary: bool = True,
) -> tuple[list[str], tuple[str, str, str] | None, Path | None]:
    """生成传给 LLaMA-Factory 的动态覆盖参数。"""
    generated_plan = generated_training_datasets(args, stages)
    has_dataset_config = config_has_key(config, "dataset")
    has_v1_dataset = config_has_key(config, "train_dataset")

    if generated_plan and args.train_dataset:
        raise PipelineError("--train-dataset 只用于训练已有数据；同一次生成数据时无需手动指定")

    if generated_plan and not has_dataset_config:
        if has_v1_dataset:
            raise PipelineError(
                "当前自动接线只支持经典 LLaMA-Factory 配置的 dataset/eval_dataset；"
                "v1 配置使用 train_dataset 文件路径，请先准备对应 v1 数据配置。"
            )
        raise PipelineError(
            "训练配置没有 dataset 字段，无法自动接入本轮生成的数据；"
            "请使用经典 LLaMA-Factory 配置，或单独准备 v1 数据配置。"
        )

    train_name: str | None
    eval_name: str | None
    if generated_plan:
        train_name, eval_name, data_kind = generated_plan
        if args.train_dataset_dir:
            raise PipelineError(
                "本轮自动导出的数据固定写入 training/data/llamafactory；"
                "--train-dataset-dir 只用于训练已有数据集。"
            )
        config_stage = (config_scalar(config, "stage") or "").lower()
        if config_stage and config_stage != data_kind:
            raise PipelineError(
                f"训练配置 stage={config_stage} 与本轮自动接入的数据类型 {data_kind} 不一致；"
                f"请更换配置，当前数据集为 {train_name}。"
            )
    elif args.train_dataset:
        if not has_dataset_config:
            if has_v1_dataset:
                raise PipelineError(
                    "当前 --train-dataset 只支持经典 LLaMA-Factory 配置的 dataset/eval_dataset；"
                    "v1 配置使用 train_dataset 文件路径，请先准备对应 v1 数据配置。"
                )
            raise PipelineError(f"训练配置没有 dataset 字段，无法覆盖训练数据集：{relative_or_absolute(config)}")
        train_name = args.train_dataset
        eval_name = args.train_eval_dataset or config_scalar(config, "eval_dataset")
    elif has_dataset_config:
        train_name = config_scalar(config, "dataset")
        eval_name = config_scalar(config, "eval_dataset")
        if not train_name:
            raise PipelineError(f"训练配置缺少 dataset 值：{relative_or_absolute(config)}")
    else:
        train_name = None
        eval_name = None

    overrides: list[str] = []
    if has_dataset_config and train_name:
        if args.train_dataset_dir:
            dataset_dir = project_path(args.train_dataset_dir).resolve()
        elif generated_plan or args.train_dataset:
            dataset_dir = LLAMAFACTORY_DATA_DIR.resolve()
        else:
            configured_dataset_dir = config_scalar(config, "dataset_dir")
            dataset_dir = (
                project_path(configured_dataset_dir).resolve()
                if configured_dataset_dir
                else LLAMAFACTORY_DATA_DIR.resolve()
            )
        if validate_data and not args.dry_run:
            validate_registered_datasets(dataset_dir, split_dataset_names(train_name))
            validate_registered_datasets(dataset_dir, split_dataset_names(eval_name))
        overrides.append(f"dataset={train_name}")
        if eval_name:
            overrides.append(f"eval_dataset={eval_name}")
        overrides.append(f"dataset_dir={dataset_dir}")
        if show_summary:
            print(f"  训练数据目录：{relative_or_absolute(dataset_dir)}", flush=True)
            print(f"  训练数据集：{train_name}", flush=True)
            if eval_name:
                print(f"  验证数据集：{eval_name}", flush=True)

    output_dir = resolve_train_output_dir(args, config, generated_plan, train_name)
    if output_dir:
        overrides.append(f"output_dir={output_dir}")
        if show_summary:
            print(f"  训练输出目录：{relative_or_absolute(output_dir)}", flush=True)

    return overrides, generated_plan, output_dir


def llamafactory_env(root: Path) -> dict[str, str]:
    """让 console script 优先导入指定 checkout，并设置项目默认 DPO 选项。"""
    env = os.environ.copy()
    source_dir = str(root / "src")
    existing_pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        source_dir + os.pathsep + existing_pythonpath if existing_pythonpath else source_dir
    )
    env.setdefault("LLAMAFACTORY_ROOT", str(root))
    # 项目默认配置使用 DeepSpeed。LLaMA-Factory 要求 DeepSpeed 由
    # llamafactory-cli 通过 torchrun 启动，否则会在参数校验阶段停止。
    env.setdefault("FORCE_TORCHRUN", "1")
    env.setdefault("LLAMAFACTORY_DPO_LABEL_LOGITS_ONLY", "1")
    env.setdefault("LLAMAFACTORY_LOGPS_CHUNK_SIZE", "1024")
    env.setdefault("LLAMAFACTORY_LOGPS_CHECKPOINT", "1")
    env.setdefault("LLAMAFACTORY_LOGPS_UPCAST", "0")
    return env


def run_train(args: argparse.Namespace, stages: Sequence[str]) -> None:
    if not args.config:
        raise PipelineError("train 阶段必须传 --config PATH")
    config = project_path(args.config)
    require_file(config, "训练配置")
    training_overrides, _, _ = build_training_overrides(args, stages, config)
    root = find_llamafactory_root(args)
    if not args.dry_run:
        verify_llamafactory_checkout(root, allow_unpatched=args.allow_unpatched_llamafactory)
    cli = find_llamafactory_cli(args, root)
    print(f"  LLaMA-Factory 源码：{relative_or_absolute(root)}", flush=True)
    print(f"  LLaMA-Factory 工作目录：{relative_or_absolute(root)}", flush=True)
    if args.allow_unpatched_llamafactory:
        print("  补丁校验：已跳过（--allow-unpatched-llamafactory）", flush=True)
    else:
        print(f"  补丁基线：{LLAMAFACTORY_BASE_COMMIT[:12]} + 项目内补丁", flush=True)
    run_step(
        args,
        "LLaMA-Factory 训练",
        [str(cli), "train", str(config), *training_overrides],
        env=llamafactory_env(root),
        cwd=root,
    )


def env_file_has_key(path: Path, key: str) -> bool:
    """只检查 .env 是否声明非空变量，不读取或输出变量值。"""
    if not path.is_file():
        return False
    prefix = f"{key}="
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            text = line.strip()
            if not text or text.startswith("#") or not text.startswith(prefix):
                continue
            value = text[len(prefix) :].strip().strip("\"'")
            if value and not value.startswith("your_"):
                return True
    except OSError:
        return False
    return False


def has_config_key(key: str) -> bool:
    if os.getenv(key):
        return True
    return any(env_file_has_key(path, key) for path in [PROJECT_ROOT / ".env", PROJECT_ROOT / "backend/.env"])


def missing_python_modules(python: str, modules: Sequence[str]) -> list[str]:
    """检查指定解释器中缺少的 Python 模块。"""
    module_list = repr(list(modules))
    code = (
        "import importlib.util; "
        f"modules={module_list}; "
        "print(','.join(name for name in modules if importlib.util.find_spec(name) is None))"
    )
    try:
        result = subprocess.run(
            [python, "-c", code],
            cwd=PROJECT_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return list(modules)
    if result.returncode != 0:
        return list(modules)
    return [item for item in result.stdout.strip().split(",") if item]


def selected_python_version(python: str) -> str:
    """读取实际子脚本解释器的版本，避免把调度器版本误当成训练环境版本。"""
    try:
        result = subprocess.run(
            [python, "-c", "import sys; print(sys.version.split()[0])"],
            cwd=PROJECT_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return "unknown"
    version = result.stdout.strip()
    return version if result.returncode == 0 and version else "unknown"


def run_preflight(args: argparse.Namespace, stages: Sequence[str], python: str) -> None:
    required = {
        "current SFT 入口": SFT_SCRIPT,
        "SFT 预算审计": SFT_AUDIT_SCRIPT,
        "SFT 可用性分类": SFT_CLASSIFY_SCRIPT,
        "SFT 子集导出": SFT_EXPORT_SCRIPT,
        "票价候选收集": PRICING_COLLECT_SCRIPT,
        "票价候选分桶": PRICING_BUCKET_SCRIPT,
        "强模型票价估价": PRICING_ESTIMATE_SCRIPT,
        "冻结评估集构建": EVAL_DATA_SCRIPT,
        "Best-of-N prompt": BESTOFN_PROMPTS_SCRIPT,
        "Best-of-N 候选生成": BESTOFN_CANDIDATES_SCRIPT,
        "Best-of-N 选择导出": BESTOFN_SELECT_SCRIPT,
        "通用 DPO prompt": DPO_PROMPTS_SCRIPT,
        "通用 DPO 候选生成": DPO_CANDIDATES_SCRIPT,
        "通用 DPO judge": DPO_JUDGE_SCRIPT,
        "通用 DPO pair 构造": DPO_PAIRS_SCRIPT,
        "通用 DPO 审计": DPO_AUDIT_SCRIPT,
        "评测入口": EVAL_PIPELINE_SCRIPT,
        "TripPlan 校验入口": VALIDATION_SCRIPT,
        "训练依赖文件": TRAINING_DIR / "requirements-training.txt",
    }
    if "train" in stages and not args.allow_unpatched_llamafactory:
        required["LLaMA-Factory 项目补丁"] = LLAMAFACTORY_PATCH
    missing = [(label, path) for label, path in required.items() if not path.is_file()]
    print(f"项目根目录：{PROJECT_ROOT}")
    print(f"Python：{python}")
    print(f"Python 版本：{selected_python_version(python)}")
    print(f"阶段：{', '.join(stages)}")
    required_modules = list(REQUIRED_PYTHON_MODULES)
    if "train" in stages:
        required_modules.extend(REQUIRED_TRAINING_MODULES)
    missing_modules = missing_python_modules(python, required_modules)
    print(f"Python 依赖：{len(required_modules) - len(missing_modules)}/{len(required_modules)} 可导入")
    if missing_modules:
        install_command = f"{shlex.join([python, '-m', 'pip'])} install -r training/requirements-training.txt"
        print(f"  缺少：{', '.join(missing_modules)}；请执行：{install_command}")
        if args.strict_preflight or not args.dry_run:
            raise PipelineError(f"当前 Python 缺少后训练依赖，请执行：{install_command}")
    print(f"关键入口：{len(required) - len(missing)}/{len(required)} 可用")
    if missing:
        for label, path in missing:
            print(f"  缺少：{label} -> {relative_or_absolute(path)}")
        if args.strict_preflight or not args.dry_run:
            raise PipelineError("preflight 未通过")

    if "train" in stages:
        if not args.config:
            raise PipelineError("train 阶段必须传 --config PATH")
        config = project_path(args.config)
        require_file(config, "训练配置")
        # 先校验配置类型、数据阶段和路径拼接方式。实际数据尚未生成时不检查
        # dataset_info，等前面的 SFT/DPO 阶段完成后由 run_train 再检查一次。
        build_training_overrides(args, stages, config, validate_data=False, show_summary=False)

        # 训练环境必须在数据生成前检查。否则读者可能先消耗 API 配额，最后才发现
        # LLaMA-Factory checkout 或 console script 没准备好。
        root = find_llamafactory_root(args)
        if root.is_dir():
            try:
                verify_llamafactory_checkout(root, allow_unpatched=args.allow_unpatched_llamafactory)
            except PipelineError as exc:
                if not args.dry_run:
                    raise
                print(f"  训练环境警告：{exc}")
            cli = find_llamafactory_cli(args, root)
            if cli.is_file() and os.access(cli, os.X_OK):
                print(f"  llamafactory-cli：{relative_or_absolute(cli)}")
            elif args.dry_run:
                print(f"  训练环境警告：找不到可执行的 llamafactory-cli（预览不阻断）：{cli}")
        elif args.dry_run:
            print(f"  训练环境警告：找不到 LLaMA-Factory 源码目录（预览不阻断）：{relative_or_absolute(root)}")

    key_status = {
        "AMAP_API_KEY / AMAP_MAPS_API_KEY": has_config_key("AMAP_API_KEY") or has_config_key("AMAP_MAPS_API_KEY"),
        "数据生成模型 API key": any(
            has_config_key(key)
            for key in ["DATA_GEN_API_KEY", "DEEPSEEK_API_KEY", "LLM_API_KEY", "MIMO_API_KEY", "OPENAI_API_KEY"]
        ),
    }
    print("配置检查：")
    for label, present in key_status.items():
        print(f"  {'已找到' if present else '未找到'}：{label}")
    print("说明：preflight 只检查文件、依赖和配置名，不会调用 API、启动模型或修改训练数据。")
    needs_amap = any(stage in {"sft-data", "sft-context", "eval-data"} for stage in stages)
    needs_amap = needs_amap or ("pricing" in stages and args.collect_context)
    needs_data_gen = any(stage in {"sft-data", "dpo"} for stage in stages)
    needs_data_gen = needs_data_gen or ("eval-data" in stages and args.request_source == "llm")
    needs_data_gen = needs_data_gen or ("pricing" in stages and args.estimate_prices)
    needs_data_gen = needs_data_gen or ("eval" in stages and args.eval_run_judge)
    if not args.dry_run:
        if not key_status["AMAP_API_KEY / AMAP_MAPS_API_KEY"] and needs_amap:
            raise PipelineError("缺少高德 API key，请配置 AMAP_API_KEY 或 AMAP_MAPS_API_KEY")
        if not key_status["数据生成模型 API key"] and needs_data_gen:
            raise PipelineError("缺少数据生成模型 API key，请配置 DATA_GEN_API_KEY、DEEPSEEK_API_KEY 或 MIMO_API_KEY")
    elif args.strict_preflight:
        if not key_status["AMAP_API_KEY / AMAP_MAPS_API_KEY"] and needs_amap:
            raise PipelineError("严格 preflight：缺少高德 API key")
        if not key_status["数据生成模型 API key"] and needs_data_gen:
            raise PipelineError("严格 preflight：缺少数据生成模型 API key")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="统一调度旅行助手后训练的数据生成、审计、DPO、评测和训练入口。",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--stage",
        action="append",
        choices=STAGE_ORDER,
        help="要执行的阶段，可重复传入；未指定时只执行 preflight。",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只打印子命令，不执行数据生成、API 请求或训练；会保留只读的 preflight 检查。",
    )
    parser.add_argument("--strict-preflight", action="store_true", help="即使是 dry-run，也在必要入口或 API key 缺失时失败。")
    parser.add_argument("--python", help="子脚本使用的 Python 解释器；默认优先使用项目训练环境。")
    parser.add_argument("--output-dir", type=Path, help="单阶段运行时的通用输出目录。多阶段请使用阶段专用目录参数。")
    parser.add_argument("--records", type=Path, help="需要 records.jsonl 的阶段输入；多阶段时可自动接 SFT 或 eval-data 输出。")
    parser.add_argument("--resume", action="store_true", help="复用已有中间结果，并跳过已完成样本。")

    data = parser.add_argument_group("请求与 SFT 参数")
    data.add_argument("--count", type=int, default=20, help="请求或数据样本数。")
    data.add_argument("--start-index", type=int, default=0)
    data.add_argument("--seed", type=int, default=20260429)
    data.add_argument("--request-source", choices=["template", "llm", "controlled", "budget_supplement"], default="controlled")
    data.add_argument("--date-mode", choices=["future", "mixed", "past"], default="mixed")
    data.add_argument("--difficulty", choices=["standard", "hard", "harder"], default="standard", help="eval-data 的请求难度。")
    data.add_argument("--workers", type=int, default=1)
    data.add_argument("--historical-weather-provider", choices=["open-meteo", "none"], default="open-meteo")
    data.add_argument("--target-budget-mix", default="")
    data.add_argument("--disallow-budget-strictness-none", action="store_true")
    data.add_argument("--teacher-model-provider", choices=["env", "deepseek", "mimo"])
    data.add_argument("--teacher-model")
    data.add_argument("--amap-qps-limit", type=float)
    data.add_argument("--sample-retries", type=int, default=3)
    data.add_argument("--target-successes", type=int, default=0)
    data.add_argument("--budget-context-min-ratio", type=float, default=None)
    data.add_argument("--budget-context-retry-stride", type=int, default=0)
    data.add_argument("--temperature", type=float, default=0.2)
    data.add_argument("--max-output-tokens", type=int, default=0)
    data.add_argument("--output-base-tokens", type=int, default=None)
    data.add_argument("--output-tokens-per-day", type=int, default=None)
    data.add_argument("--output-retry-tokens", type=int, default=None)
    data.add_argument("--output-tokens-cap", type=int, default=None)
    data.add_argument("--val-ratio", type=float, default=0.1)
    data.add_argument("--sft-category", default="usable_budget_clean")
    data.add_argument("--sft-dataset-prefix")
    data.add_argument("--sft-dir", type=Path)

    pricing = parser.add_argument_group("票价候选参数")
    pricing.add_argument("--pricing-dir", type=Path)
    pricing.add_argument("--collect-context", action="store_true", help="pricing 阶段直接查询 PlannerContext，而不是读取 records。")
    pricing.add_argument("--min-request-count", type=int, default=5)
    pricing.add_argument("--estimate-prices", action="store_true", help="pricing 分桶后调用强模型估价；默认只收集和分桶。")
    pricing.add_argument("--price-batch-size", type=int, default=20)
    pricing.add_argument("--price-limit", type=int, default=0)
    pricing.add_argument("--price-retries", type=int, default=3)

    eval_data = parser.add_argument_group("冻结评估集参数")
    eval_data.add_argument("--eval-data-dir", type=Path)
    eval_data.add_argument("--eval-id-prefix")

    bestofn = parser.add_argument_group("Best-of-N 参数")
    bestofn.add_argument("--bestofn-dir", type=Path)
    bestofn.add_argument("--bestofn-source")
    bestofn.add_argument("--bestofn-base-url", default="http://127.0.0.1:4396/v1")
    bestofn.add_argument("--bestofn-api-model", default="trip-planner-sft")
    bestofn.add_argument("--bestofn-spec", action="append", default=[], help="候选配置 label:temperature:count，可重复。")
    bestofn.add_argument("--bestofn-shuffle", action="store_true")
    bestofn.add_argument("--bestofn-stratified-smoke20", action="store_true")
    bestofn.add_argument("--bestofn-no-hard-gate", action="store_true")
    bestofn.add_argument("--bestofn-rejected-allow-nonschema", action="store_true")
    bestofn.add_argument("--bestofn-dataset-prefix")

    dpo = parser.add_argument_group("通用 DPO 参数")
    dpo.add_argument("--dpo-dir", type=Path)
    dpo.add_argument("--dpo-source")
    dpo.add_argument("--dpo-shuffle", action="store_true")
    dpo.add_argument("--dpo-workers", type=int, default=1)
    dpo.add_argument("--dpo-base-url", default="http://127.0.0.1:4397/v1")
    dpo.add_argument("--dpo-base-api-model", default="trip-planner-base")
    dpo.add_argument("--dpo-sft-base-url", default="http://127.0.0.1:4396/v1")
    dpo.add_argument("--dpo-sft-api-model", default="trip-planner-sft")
    dpo.add_argument("--dpo-no-base-low", action="store_true")
    dpo.add_argument("--dpo-no-base-high", action="store_true")
    dpo.add_argument("--dpo-no-sft-low", action="store_true")
    dpo.add_argument("--dpo-include-strong-low", action="store_true")
    dpo.add_argument("--dpo-include-strong-high", action="store_true")
    dpo.add_argument("--dpo-strong-provider", choices=["env", "deepseek", "mimo"])
    dpo.add_argument("--dpo-strong-label", default="strong")
    dpo.add_argument("--dpo-min-chosen-score", type=float, default=4.0)
    dpo.add_argument("--dpo-min-score-gap", type=float, default=0.8)
    dpo.add_argument("--dpo-tag-gap", type=float, default=0.8)
    dpo.add_argument("--dpo-max-pairs-per-prompt", type=int, default=1)
    dpo.add_argument("--dpo-dataset-prefix")
    dpo.add_argument("--dpo-audit-sample-size", type=int, default=20)

    evaluation = parser.add_argument_group("模型评测参数")
    evaluation.add_argument("--eval-dir", type=Path)
    evaluation.add_argument("--model-name")
    evaluation.add_argument("--api-model")
    evaluation.add_argument("--base-url", default="http://127.0.0.1:4396/v1")
    evaluation.add_argument("--api-key")
    evaluation.add_argument("--limit", type=int, default=0)
    evaluation.add_argument("--timeout", type=float, default=660)
    evaluation.add_argument("--connect-timeout", type=float, default=10)
    evaluation.add_argument("--max-tokens", type=int, default=0)
    evaluation.add_argument("--trust-env", action="store_true")
    evaluation.add_argument("--no-auto-openai-path", action="store_true")
    evaluation.add_argument("--resume-include-failed", action="store_true")
    evaluation.add_argument("--eval-skip-generate", action="store_true")
    evaluation.add_argument("--eval-skip-rule", action="store_true")
    evaluation.add_argument("--eval-run-judge", action="store_true")
    evaluation.add_argument("--judge-workers", type=int, default=4)

    validation = parser.add_argument_group("格式校验参数")
    validation.add_argument("--validate-sft", type=Path, help="校验一个 SFT LLaMA-Factory JSON 文件。")
    validation.add_argument("--validate-dpo", type=Path, help="校验一个 DPO LLaMA-Factory JSON 文件。")
    validation.add_argument("--validate-eval-gt", type=Path, help="校验一个 Eval GT JSONL 文件。")

    training = parser.add_argument_group("训练参数")
    training.add_argument("--config", type=Path, help="LLaMA-Factory 训练 YAML。")
    training.add_argument("--llamafactory-cli", type=Path, help="llamafactory-cli 的完整路径。")
    training.add_argument(
        "--llamafactory-root",
        type=Path,
        help="LLaMA-Factory 源码目录；默认读取 LLAMAFACTORY_ROOT 或项目同级目录 ../LLaMA-Factory。",
    )
    training.add_argument(
        "--allow-unpatched-llamafactory",
        action="store_true",
        help="跳过项目补丁和基础 commit 校验，仅用于不需要本项目训练补丁的实验。",
    )
    training.add_argument(
        "--train-dataset-dir",
        type=Path,
        help="经典 LLaMA-Factory 数据目录；默认使用项目内 training/data/llamafactory。",
    )
    training.add_argument(
        "--train-dataset",
        help="训练已有导出数据时，指定 dataset_info.json 中的 dataset 名称。",
    )
    training.add_argument(
        "--train-eval-dataset",
        help="训练已有导出数据时，指定 dataset_info.json 中的 eval_dataset 名称；不传则沿用 YAML 配置。",
    )
    training.add_argument(
        "--train-output-dir",
        type=Path,
        help="训练输出目录；包含数据阶段时默认按本轮数据集自动生成隔离目录。",
    )
    return parser


def validate_args(args: argparse.Namespace, stages: Sequence[str]) -> None:
    if args.count < 0:
        raise PipelineError("--count 不能小于 0")
    if args.workers < 1 or args.dpo_workers < 1 or args.judge_workers < 1:
        raise PipelineError("workers 必须大于等于 1")
    if args.val_ratio < 0 or args.val_ratio >= 1:
        raise PipelineError("--val-ratio 必须在 [0, 1) 内")
    if args.resume and "preflight" in stages and len(stages) == 1:
        print("提示：单独执行 preflight 时 --resume 不会产生影响。")
    if args.train_eval_dataset and not args.train_dataset:
        raise PipelineError("--train-eval-dataset 需要和 --train-dataset 一起使用")
    if (
        "train" in stages
        and "sft-data" in stages
        and "sft-audit" not in stages
        and "dpo" not in stages
        and not args.train_dataset
    ):
        raise PipelineError("SFT 数据要先经过 sft-audit 导出后才能训练；请追加 --stage sft-audit，或单独传 --train-dataset")
    if "pricing" in stages and not args.collect_context and not args.records and not any(
        item in SFT_PIPELINE_STAGES for item in stages
    ):
        raise PipelineError("pricing 阶段需要 --records，或传 --collect-context，或同一次运行中先执行 sft-data")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        stages = normalize_stages(args.stage)
        validate_args(args, stages)
        python = selected_python(args)
        run_preflight(args, stages, python)

        if "sft-request" in stages:
            run_sft_request(args, python)
        if "sft-context" in stages:
            run_sft_context(args, python)
        if "sft-data" in stages:
            run_sft_data(args, python, stages)
        if "sft-audit" in stages:
            run_sft_audit(args, python, stages)
        if "pricing" in stages:
            run_pricing(args, python, stages)
        if "eval-data" in stages:
            run_eval_data(args, python, stages)
        if "bestofn" in stages:
            run_bestofn(args, python, stages)
        if "dpo" in stages:
            run_dpo(args, python, stages)
        if "eval" in stages:
            run_eval(args, python, stages)
        if "validate" in stages:
            run_validate(args, python, stages)
        if "train" in stages:
            run_train(args, stages)
    except PipelineError as exc:
        print(f"\n流水线停止：{exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\n流水线被用户中断。", file=sys.stderr)
        return 130

    if args.dry_run:
        print("\n检查完成：以上只是 dry-run，没有执行子脚本。")
    else:
        print("\n流水线完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
