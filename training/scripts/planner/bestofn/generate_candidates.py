#!/usr/bin/env python3
"""Generate Best-of-N candidates for planner prompts."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from openai import OpenAI


PROJECT_ROOT = Path(__file__).resolve().parents[4]
EVAL_SCRIPTS_DIR = PROJECT_ROOT / "training/scripts/eval"
SHARED_SCRIPTS_DIR = PROJECT_ROOT / "training/scripts"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(BACKEND_DIR))
sys.path.insert(0, str(EVAL_SCRIPTS_DIR))
sys.path.insert(0, str(SHARED_SCRIPTS_DIR))

from eval_rule_metrics import evaluate_output  # noqa: E402
from eval_utils import append_jsonl, planner_max_output_tokens, read_jsonl, write_json  # noqa: E402
from shared.common import load_project_env  # noqa: E402


DEFAULT_PROMPTS = PROJECT_ROOT / "training/data/planner/bestofn/prompts.jsonl"
DEFAULT_OUTPUT = PROJECT_ROOT / "training/data/planner/bestofn/candidates.jsonl"


@dataclass(frozen=True)
class CandidateSpec:
    label: str
    temperature: float
    count: int


def normalize_base_url(base_url: str, auto_openai_path: bool = True) -> str:
    value = base_url.rstrip("/")
    if auto_openai_path and not value.endswith("/v1"):
        value = f"{value}/v1"
    return value


def parse_spec(value: str) -> CandidateSpec:
    """Parse label:temperature:count."""
    parts = value.split(":")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("--spec must look like label:temperature:count")
    label, temperature, count = parts
    try:
        return CandidateSpec(label=label, temperature=float(temperature), count=int(count))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def done_prompt_ids(path: Path) -> set[str]:
    return {row.get("prompt_id", "") for row in read_jsonl(path) if row.get("prompt_id")}


def record_from_prompt_row(row: dict[str, Any]) -> dict[str, Any]:
    """Shape prompt rows back into evaluate_output records."""
    return {
        "record_id": row["record_id"],
        "request": row.get("request") or {},
        "control_spec": row.get("control_spec") or {},
        "planner_context": row.get("planner_context") or {},
        "compact_planner_context": row.get("compact_planner_context") or {},
        "planner_query": row.get("prompt") or "",
    }


def build_client(args: argparse.Namespace) -> OpenAI:
    timeout = httpx.Timeout(args.timeout, connect=args.connect_timeout)
    http_client = httpx.Client(timeout=timeout, trust_env=args.trust_env)
    return OpenAI(
        api_key=args.api_key or os.getenv("EVAL_API_KEY") or os.getenv("OPENAI_API_KEY") or "EMPTY",
        base_url=normalize_base_url(args.base_url, auto_openai_path=not args.no_auto_openai_path),
        max_retries=0,
        http_client=http_client,
    )


def call_model(prompt_row: dict[str, Any], spec: CandidateSpec, args: argparse.Namespace) -> tuple[str, str]:
    client = build_client(args)
    max_tokens = args.max_tokens or planner_max_output_tokens(
        prompt_row.get("request") or {},
        base=args.output_base_tokens,
        per_day=args.output_tokens_per_day,
        cap=args.output_tokens_cap,
    )
    response = client.chat.completions.create(
        model=args.api_model,
        messages=[
            {"role": "system", "content": prompt_row.get("system_prompt", "")},
            {"role": "user", "content": prompt_row.get("prompt", "")},
        ],
        temperature=spec.temperature,
        max_tokens=max_tokens,
        stream=False,
    )
    return response.choices[0].message.content or "", response.choices[0].finish_reason or ""


def make_candidate(prompt_row: dict[str, Any], spec: CandidateSpec, index: int, args: argparse.Namespace) -> dict[str, Any]:
    candidate_id = f"{prompt_row['prompt_id']}__{spec.label}__{index}"
    started = time.perf_counter()
    candidate: dict[str, Any] = {
        "candidate_id": candidate_id,
        "source_model": args.api_model,
        "source_type": "bestofn",
        "temperature": spec.temperature,
        "output_text": "",
        "rule_metrics": {},
        "rule_errors": [],
        "generation_meta": {},
    }
    try:
        output, finish_reason = call_model(prompt_row, spec, args)
        generation = {
            "ok": True,
            "output": output,
            "latency_seconds": round(time.perf_counter() - started, 3),
            "output_chars": len(output),
        }
        rule_result = evaluate_output(record_from_prompt_row(prompt_row), generation)
        metrics = rule_result.get("metrics", {})
        candidate.update(
            {
                "output_text": output,
                "parsed_ok": metrics.get("json_extract_ok") is True,
                "schema_ok": metrics.get("schema_ok") is True,
                "rule_metrics": metrics,
                "rule_errors": rule_result.get("errors", []),
                "generation_meta": {
                    **generation,
                    "finish_reason": finish_reason,
                    "label": spec.label,
                },
            }
        )
    except Exception as exc:  # noqa: BLE001
        candidate["generation_meta"] = {
            "ok": False,
            "latency_seconds": round(time.perf_counter() - started, 3),
            "error_type": type(exc).__name__,
            "error": str(exc),
            "label": spec.label,
        }
    return candidate


def generate_one(prompt_row: dict[str, Any], specs: list[CandidateSpec], args: argparse.Namespace) -> dict[str, Any]:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Best-of-N candidates.")
    parser.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--base-url", default="http://127.0.0.1:4396/v1")
    parser.add_argument("--api-model", default="trip-planner-sft")
    parser.add_argument(
        "--spec",
        type=parse_spec,
        action="append",
        default=None,
        help="Candidate spec label:temperature:count. Can be repeated.",
    )
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--timeout", type=float, default=660)
    parser.add_argument("--connect-timeout", type=float, default=10)
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
    specs = args.spec or [
        CandidateSpec("t02", 0.2, 1),
        CandidateSpec("t05", 0.5, 2),
        CandidateSpec("t08", 0.8, 1),
    ]
    done_ids = done_prompt_ids(args.output) if args.resume else set()
    todo = [row for row in prompts if row.get("prompt_id") not in done_ids]

    config = {
        "prompts": str(args.prompts),
        "output": str(args.output),
        "base_url": args.base_url,
        "api_model": args.api_model,
        "total_prompts": len(prompts),
        "todo": len(todo),
        "workers": args.workers,
        "specs": [spec.__dict__ for spec in specs],
    }
    write_json(args.output.parent / "candidate_generation_config.json", config)
    print(json.dumps(config, ensure_ascii=False, indent=2), flush=True)

    completed = 0
    hardpass = 0
    if args.workers <= 1:
        for prompt_row in todo:
            row = generate_one(prompt_row, specs, args)
            append_jsonl(args.output, row)
            completed += 1
            hardpass += sum(1 for item in row["candidates"] if item.get("rule_metrics", {}).get("sft_hard_pass"))
            print(f"progress {completed}/{len(todo)} hardpass_candidates={hardpass} last={row['prompt_id']}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_one, row, specs, args): row["prompt_id"] for row in todo}
            for future in as_completed(futures):
                row = future.result()
                append_jsonl(args.output, row)
                completed += 1
                hardpass += sum(1 for item in row["candidates"] if item.get("rule_metrics", {}).get("sft_hard_pass"))
                print(f"progress {completed}/{len(todo)} hardpass_candidates={hardpass} last={row['prompt_id']}", flush=True)

    print(f"done: {args.output}")


if __name__ == "__main__":
    main()
