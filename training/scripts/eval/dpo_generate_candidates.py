"""为 DPO prompts 生成多模型自然候选。

示例:

  .venv-training-py311/bin/python3 training/scripts/eval/dpo_generate_candidates.py \
    --prompts training/data/planner/dpo/prompts.jsonl \
    --workers 1 \
    --resume

  # 加入强模型候选
  .venv-training-py311/bin/python3 training/scripts/eval/dpo_generate_candidates.py \
    --include-strong-low \
    --workers 2 \
    --resume
"""

from __future__ import annotations

import argparse
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import ExitStack
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from openai import OpenAI

from dpo_utils import (
    DEFAULT_DPO_CANDIDATES,
    DEFAULT_DPO_PROMPTS,
    candidate_done_prompt_ids,
    hard_filter_pass,
    normalize_base_url,
    record_from_prompt_row,
)
from eval_rule_metrics import evaluate_output
from eval_utils import append_jsonl, parse_trip_plan_output, planner_max_output_tokens, read_jsonl, write_json
from shared.common import load_project_env
from shared.llm_client import DataGenLLM


@dataclass(frozen=True)
class CandidateSpec:
    """候选生成配置。"""

    label: str
    source_type: str
    source_model: str
    temperature: float
    count: int
    base_url: str = ""
    provider: str = ""


def build_local_client(base_url: str, args: argparse.Namespace) -> OpenAI:
    """构造本地 OpenAI-compatible client。"""
    timeout = httpx.Timeout(args.timeout, connect=args.connect_timeout)
    http_client = httpx.Client(timeout=timeout, trust_env=args.trust_env)
    api_key = args.api_key or os.getenv("EVAL_API_KEY") or os.getenv("OPENAI_API_KEY") or "EMPTY"
    return OpenAI(
        api_key=api_key,
        base_url=normalize_base_url(base_url, auto_openai_path=not args.no_auto_openai_path),
        max_retries=0,
        http_client=http_client,
    )


def call_local_model(prompt_row: dict[str, Any], spec: CandidateSpec, args: argparse.Namespace) -> tuple[str, str]:
    """调用本地或 OpenAI-compatible 模型服务。"""
    client = build_local_client(spec.base_url, args)
    request = prompt_row.get("request") or {}
    max_tokens = args.max_tokens or planner_max_output_tokens(
        request,
        base=args.output_base_tokens,
        per_day=args.output_tokens_per_day,
        cap=args.output_tokens_cap,
    )
    response = client.chat.completions.create(
        model=spec.source_model,
        messages=[
            {"role": "system", "content": prompt_row.get("system_prompt", "")},
            {"role": "user", "content": prompt_row.get("prompt", "")},
        ],
        temperature=spec.temperature,
        max_tokens=max_tokens,
        stream=False,
    )
    return response.choices[0].message.content or "", response.choices[0].finish_reason or ""


def call_strong_model(prompt_row: dict[str, Any], spec: CandidateSpec, args: argparse.Namespace) -> tuple[str, str]:
    """调用强模型生成候选。"""
    llm = DataGenLLM(provider=spec.provider or None)
    max_tokens = args.max_tokens or planner_max_output_tokens(
        prompt_row.get("request") or {},
        base=args.output_base_tokens,
        per_day=args.output_tokens_per_day,
        cap=args.output_tokens_cap,
    )
    kwargs: dict[str, Any] = {
        "model": llm.model,
        "messages": [
            {"role": "system", "content": prompt_row.get("system_prompt", "")},
            {"role": "user", "content": prompt_row.get("prompt", "")},
        ],
        "temperature": spec.temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    if llm.enable_thinking and llm.reasoning_effort:
        kwargs["reasoning_effort"] = llm.reasoning_effort
    if llm.enable_thinking:
        kwargs["extra_body"] = {"thinking": {"type": "enabled"}}
    response = llm.client.chat.completions.create(**kwargs)
    return response.choices[0].message.content or "", response.choices[0].finish_reason or ""


def make_candidate(prompt_row: dict[str, Any], spec: CandidateSpec, index: int, args: argparse.Namespace) -> dict[str, Any]:
    """生成并规则评估单个候选。"""
    candidate_id = f"{prompt_row['prompt_id']}__{spec.label}__{index}"
    started = time.perf_counter()
    candidate: dict[str, Any] = {
        "candidate_id": candidate_id,
        "source_model": spec.source_model,
        "source_type": spec.source_type,
        "temperature": spec.temperature,
        "output_text": "",
        "parsed_ok": False,
        "schema_ok": False,
        "trip_plan": None,
        "rule_metrics": {},
        "rule_errors": [],
        "generation_meta": {},
    }
    try:
        # JSON 解析失败通常只是一次采样废样本，尤其强模型高温输出更容易夹杂解释、
        # 截断或不完整 JSON。这里只对 json_extract 失败做短重试；如果 JSON 能解析
        # 但 schema/规则不合格，则保留该候选交给硬过滤和后续 judge 处理。
        max_attempts = max(1, args.json_parse_retries)
        retry_errors: list[dict[str, Any]] = []
        for attempt in range(1, max_attempts + 1):
            attempt_started = time.perf_counter()
            if spec.source_type == "strong":
                output, finish_reason = call_strong_model(prompt_row, spec, args)
            else:
                output, finish_reason = call_local_model(prompt_row, spec, args)

            generation = {
                "ok": True,
                "output": output,
                "latency_seconds": round(time.perf_counter() - attempt_started, 3),
                "output_chars": len(output),
            }
            rule_result = evaluate_output(record_from_prompt_row(prompt_row), generation)
            trip_plan, _, error_stage, error = parse_trip_plan_output(output)
            parsed_ok = error_stage != "json_extract"
            candidate.update(
                {
                    "output_text": output,
                    "parsed_ok": parsed_ok,
                    "schema_ok": trip_plan is not None,
                    "trip_plan": trip_plan.model_dump() if trip_plan else None,
                    "rule_metrics": rule_result.get("metrics", {}),
                    "rule_errors": rule_result.get("errors", []),
                    "generation_meta": {
                        "ok": True,
                        "latency_seconds": round(time.perf_counter() - started, 3),
                        "last_attempt_latency_seconds": generation["latency_seconds"],
                        "finish_reason": finish_reason,
                        "output_chars": len(output),
                        "attempts": attempt,
                        "max_json_parse_attempts": max_attempts,
                        "json_parse_retry_count": attempt - 1,
                        "json_parse_retry_errors": retry_errors,
                    },
                }
            )
            if parsed_ok:
                break

            retry_errors.append(
                {
                    "attempt": attempt,
                    "error_stage": error_stage,
                    "message": error,
                    "finish_reason": finish_reason,
                    "output_chars": len(output),
                }
            )
            if attempt < max_attempts:
                print(
                    f"  - {candidate_id} JSON解析失败，重试 {attempt + 1}/{max_attempts}",
                    flush=True,
                )

        passed, reasons = hard_filter_pass(candidate)
        candidate["hard_filter_pass"] = passed
        candidate["hard_filter_reasons"] = reasons
    except Exception as exc:  # noqa: BLE001
        candidate.update(
            {
                "generation_meta": {
                    "ok": False,
                    "latency_seconds": round(time.perf_counter() - started, 3),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                },
                "hard_filter_pass": False,
                "hard_filter_reasons": ["generation_failed"],
            }
        )
    return candidate


def generate_prompt_candidates(prompt_row: dict[str, Any], specs: list[CandidateSpec], args: argparse.Namespace) -> dict[str, Any]:
    """生成一个 prompt 下所有候选。"""
    candidates = []
    for spec in specs:
        for index in range(spec.count):
            candidates.append(make_candidate(prompt_row, spec, index, args))
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "prompt_id": prompt_row["prompt_id"],
        "record_id": prompt_row["record_id"],
        "request": prompt_row.get("request") or {},
        "control_spec": prompt_row.get("control_spec") or {},
        "metadata": prompt_row.get("metadata") or {},
        "candidates": candidates,
    }


def empty_candidate_row(prompt_row: dict[str, Any]) -> dict[str, Any]:
    """构造一个 prompt 的候选输出骨架。"""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "prompt_id": prompt_row["prompt_id"],
        "record_id": prompt_row["record_id"],
        "request": prompt_row.get("request") or {},
        "control_spec": prompt_row.get("control_spec") or {},
        "metadata": prompt_row.get("metadata") or {},
        "candidates": [],
    }


def generate_candidates_split_workers(
    todo: list[dict[str, Any]],
    specs: list[CandidateSpec],
    args: argparse.Namespace,
) -> None:
    """按来源拆分并发池：本地模型低并发，强模型高并发。"""
    local_specs = [spec for spec in specs if spec.source_type != "strong"]
    strong_specs = [spec for spec in specs if spec.source_type == "strong"]
    local_workers = max(1, args.local_workers or args.workers)
    strong_workers = max(1, args.strong_workers or args.workers)

    print(
        f"split workers: local={local_workers} strong={strong_workers} "
        f"local_specs={len(local_specs)} strong_specs={len(strong_specs)}",
        flush=True,
    )

    rows_by_prompt = {row["prompt_id"]: empty_candidate_row(row) for row in todo}
    pending_by_prompt = {row["prompt_id"]: 0 for row in todo}
    futures = {}
    completed_prompts = 0
    total_valid = 0

    with ExitStack() as stack:
        local_executor = stack.enter_context(ThreadPoolExecutor(max_workers=local_workers)) if local_specs else None
        strong_executor = stack.enter_context(ThreadPoolExecutor(max_workers=strong_workers)) if strong_specs else None

        for prompt_row in todo:
            prompt_id = prompt_row["prompt_id"]
            for spec in specs:
                executor = strong_executor if spec.source_type == "strong" else local_executor
                if executor is None:
                    continue
                for index in range(spec.count):
                    future = executor.submit(make_candidate, prompt_row, spec, index, args)
                    futures[future] = prompt_id
                    pending_by_prompt[prompt_id] += 1

        for future in as_completed(futures):
            prompt_id = futures[future]
            candidate = future.result()
            rows_by_prompt[prompt_id]["candidates"].append(candidate)
            pending_by_prompt[prompt_id] -= 1

            if pending_by_prompt[prompt_id] == 0:
                row = rows_by_prompt[prompt_id]
                row["candidates"].sort(key=lambda item: item.get("candidate_id", ""))
                append_jsonl(args.output, row)
                valid = sum(1 for item in row["candidates"] if item.get("hard_filter_pass"))
                total_valid += valid
                completed_prompts += 1
                print(
                    f"progress {completed_prompts}/{len(todo)} "
                    f"valid_candidates={valid} total_valid={total_valid} last={prompt_id}",
                    flush=True,
                )


def build_specs(args: argparse.Namespace) -> list[CandidateSpec]:
    """根据参数生成候选配置。"""
    specs: list[CandidateSpec] = []
    if not args.no_base_low:
        specs.append(
            CandidateSpec(
                label="base_t02",
                source_type="base",
                source_model=args.base_api_model,
                base_url=args.base_url,
                temperature=args.base_low_temperature,
                count=args.base_low_count,
            )
        )
    if not args.no_base_high:
        specs.append(
            CandidateSpec(
                label="base_t07",
                source_type="base",
                source_model=args.base_api_model,
                base_url=args.base_url,
                temperature=args.base_high_temperature,
                count=args.base_high_count,
            )
        )
    if not args.no_sft_low:
        specs.append(
            CandidateSpec(
                label="sft_t02",
                source_type="sft",
                source_model=args.sft_api_model,
                base_url=args.sft_base_url,
                temperature=args.sft_low_temperature,
                count=args.sft_low_count,
            )
        )
    if args.include_strong_low:
        specs.append(
            CandidateSpec(
                label="strong_t02",
                source_type="strong",
                source_model=args.strong_label,
                temperature=args.strong_low_temperature,
                count=args.strong_low_count,
                provider=args.strong_provider,
            )
        )
    if args.include_strong_high:
        specs.append(
            CandidateSpec(
                label="strong_t07",
                source_type="strong",
                source_model=args.strong_label,
                temperature=args.strong_high_temperature,
                count=args.strong_high_count,
                provider=args.strong_provider,
            )
        )
    if not specs:
        raise ValueError("至少保留一个候选来源")
    return specs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="为 DPO prompt 生成多候选。")
    parser.add_argument("--prompts", type=Path, default=DEFAULT_DPO_PROMPTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_DPO_CANDIDATES)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--local-workers", type=int, default=0, help="本地 vLLM/base/SFT 候选并发；默认沿用 --workers。")
    parser.add_argument("--strong-workers", type=int, default=0, help="强模型候选并发；默认沿用 --workers。")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")

    parser.add_argument("--base-url", default="http://127.0.0.1:4397/v1")
    parser.add_argument("--base-api-model", default="trip-planner-base")
    parser.add_argument("--base-low-temperature", type=float, default=0.2)
    parser.add_argument("--base-high-temperature", type=float, default=0.7)
    parser.add_argument("--base-low-count", type=int, default=1)
    parser.add_argument("--base-high-count", type=int, default=1)
    parser.add_argument("--no-base-low", action="store_true")
    parser.add_argument("--no-base-high", action="store_true")

    parser.add_argument("--sft-base-url", default="http://127.0.0.1:4396/v1")
    parser.add_argument("--sft-api-model", default="trip-planner-sft")
    parser.add_argument("--sft-low-temperature", type=float, default=0.2)
    parser.add_argument("--sft-low-count", type=int, default=1)
    parser.add_argument("--no-sft-low", action="store_true")

    parser.add_argument("--include-strong-low", action="store_true")
    parser.add_argument("--include-strong-high", action="store_true")
    parser.add_argument(
        "--strong-provider",
        choices=["env", "deepseek", "mimo"],
        default=None,
        help="强模型 provider；不填时沿用 DATA_GEN_PROVIDER/env。调用 MIMO 时必须显式传 mimo。",
    )
    parser.add_argument("--strong-label", default="strong")
    parser.add_argument("--strong-low-temperature", type=float, default=0.2)
    parser.add_argument("--strong-high-temperature", type=float, default=0.7)
    parser.add_argument("--strong-low-count", type=int, default=1)
    parser.add_argument("--strong-high-count", type=int, default=1)

    parser.add_argument("--api-key", default=None)
    parser.add_argument("--timeout", type=float, default=660)
    parser.add_argument("--connect-timeout", type=float, default=10)
    parser.add_argument(
        "--json-parse-retries",
        type=int,
        default=5,
        help="JSON解析失败时最多尝试几次；只重试 json_extract 失败，不重试 schema/规则失败。",
    )
    parser.add_argument("--max-tokens", type=int, default=0)
    parser.add_argument("--output-base-tokens", type=int, default=3000)
    parser.add_argument("--output-tokens-per-day", type=int, default=1800)
    parser.add_argument("--output-tokens-cap", type=int, default=16000)
    parser.add_argument("--trust-env", action="store_true")
    parser.add_argument("--no-auto-openai-path", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_project_env()
    prompts = read_jsonl(args.prompts)
    if args.limit > 0:
        prompts = prompts[: args.limit]
    done_ids = candidate_done_prompt_ids(args.output) if args.resume else set()
    todo = [row for row in prompts if row.get("prompt_id") not in done_ids]
    specs = build_specs(args)
    config_path = args.output.parent / "candidate_generation_config.json"
    write_json(
        config_path,
        {
            "prompts": str(args.prompts),
            "output": str(args.output),
            "total_prompts": len(prompts),
            "todo": len(todo),
            "workers": args.workers,
            "local_workers": args.local_workers or args.workers,
            "strong_workers": args.strong_workers or args.workers,
            "specs": [spec.__dict__ for spec in specs],
        },
    )

    print(f"DPO candidates: prompts={len(prompts)}, todo={len(todo)}, workers={args.workers}")
    print("specs:", ", ".join(f"{spec.label}:{spec.source_type}@{spec.temperature}x{spec.count}" for spec in specs))

    ok = 0
    if args.local_workers or args.strong_workers:
        generate_candidates_split_workers(todo, specs, args)
    elif args.workers <= 1:
        for index, prompt_row in enumerate(todo, start=1):
            row = generate_prompt_candidates(prompt_row, specs, args)
            append_jsonl(args.output, row)
            valid = sum(1 for item in row["candidates"] if item.get("hard_filter_pass"))
            ok += valid
            print(f"progress {index}/{len(todo)} valid_candidates={valid} total_valid={ok} last={row['prompt_id']}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_prompt_candidates, row, specs, args): row["prompt_id"] for row in todo}
            for index, future in enumerate(as_completed(futures), start=1):
                row = future.result()
                append_jsonl(args.output, row)
                valid = sum(1 for item in row["candidates"] if item.get("hard_filter_pass"))
                ok += valid
                print(f"progress {index}/{len(todo)} valid_candidates={valid} total_valid={ok} last={row['prompt_id']}", flush=True)

    print(f"完成: candidates={args.output}")


if __name__ == "__main__":
    main()
