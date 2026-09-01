"""调用 OpenAI-compatible 模型服务生成 eval 输出。

示例:

  # 评估 base 服务
  .venv-training-py311/bin/python3 training/scripts/eval/eval_generate.py \
    --model-name base_qwen25_7b \
    --api-model trip-planner-base \
    --base-url http://127.0.0.1:4396/v1

  # 评估 SFT 服务
  .venv-training-py311/bin/python3 training/scripts/eval/eval_generate.py \
    --model-name sft_qwen25_7b \
    --api-model trip-planner-sft \
    --base-url http://127.0.0.1:4396/v1
"""

from __future__ import annotations

import argparse
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from openai import OpenAI

from eval_utils import (
    DEFAULT_EVAL_RECORDS,
    append_jsonl,
    load_records_by_id,
    model_run_dir,
    planner_max_output_tokens,
    read_jsonl,
    write_json,
)
from app.agents.prompts import PLANNER_AGENT_PROMPT


def normalize_base_url(base_url: str, auto_openai_path: bool = True) -> str:
    """规范化 OpenAI-compatible base_url。

    LLaMA-Factory 的 chat API 默认挂在 /v1 下。评估时经常会手滑传
    http://127.0.0.1:4396，这里自动补成 http://127.0.0.1:4396/v1。
    """
    value = base_url.rstrip("/")
    if auto_openai_path and not value.endswith("/v1"):
        value = f"{value}/v1"
    return value


def load_done_ids(path: Path, include_failed: bool = False) -> set[str]:
    """读取已完成样本 ID。

    默认只把 ok=true 的样本视为完成。这样前一次因为 502、代理或服务未启动
    写入的失败记录，在 --resume 时会被自动重试。
    """
    done = set()
    for row in read_jsonl(path):
        if row.get("record_id") and (include_failed or row.get("ok")):
            done.add(row["record_id"])
    return done


def build_client(args: argparse.Namespace) -> OpenAI:
    """构造 OpenAI-compatible client。"""
    api_key = args.api_key or os.getenv("EVAL_API_KEY") or os.getenv("OPENAI_API_KEY") or "EMPTY"
    timeout = httpx.Timeout(args.timeout, connect=args.connect_timeout)
    http_client = httpx.Client(timeout=timeout, trust_env=args.trust_env)
    return OpenAI(
        api_key=api_key,
        base_url=normalize_base_url(args.base_url, auto_openai_path=not args.no_auto_openai_path),
        max_retries=0,
        http_client=http_client,
    )


def generate_one(record: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    """生成单条输出。"""
    client = build_client(args)
    request = record.get("request") or {}
    started = time.perf_counter()
    row = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_name": args.model_name,
        "api_model": args.api_model,
        "record_id": record["record_id"],
        "request": request,
        "control_spec": record.get("control_spec", {}),
        "prompt_chars": len(record.get("planner_query", "")),
        "max_tokens": args.max_tokens or planner_max_output_tokens(
            request,
            base=args.output_base_tokens,
            per_day=args.output_tokens_per_day,
            cap=args.output_tokens_cap,
        ),
    }
    try:
        system_prompt = record.get("system_prompt") or PLANNER_AGENT_PROMPT
        response = client.chat.completions.create(
            model=args.api_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": record.get("planner_query", "")},
            ],
            temperature=args.temperature,
            max_tokens=row["max_tokens"],
            stream=False,
        )
        output = response.choices[0].message.content or ""
        row.update(
            {
                "ok": True,
                "output": output,
                "output_chars": len(output),
                "latency_seconds": round(time.perf_counter() - started, 3),
                "finish_reason": response.choices[0].finish_reason,
            }
        )
    except Exception as exc:  # noqa: BLE001
        row.update(
            {
                "ok": False,
                "output": "",
                "output_chars": 0,
                "latency_seconds": round(time.perf_counter() - started, 3),
                "error_type": type(exc).__name__,
                "error": str(exc),
            }
        )
    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 Planner 评测输出。")
    parser.add_argument("--records", type=Path, default=DEFAULT_EVAL_RECORDS)
    parser.add_argument("--model-name", required=True, help="评估运行名称，例如 base_qwen25_7b / sft_qwen25_7b")
    parser.add_argument("--api-model", required=True, help="OpenAI API model 参数")
    parser.add_argument("--base-url", default="http://127.0.0.1:4396/v1")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--output-file", type=Path, default=None)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--timeout", type=float, default=660)
    parser.add_argument("--connect-timeout", type=float, default=10)
    parser.add_argument("--max-tokens", type=int, default=0)
    parser.add_argument("--output-base-tokens", type=int, default=3000)
    parser.add_argument("--output-tokens-per-day", type=int, default=1800)
    parser.add_argument("--output-tokens-cap", type=int, default=16000)
    parser.add_argument("--trust-env", action="store_true", help="允许 httpx 读取 HTTP_PROXY/HTTPS_PROXY 等环境代理")
    parser.add_argument("--no-auto-openai-path", action="store_true", help="不要自动给 base_url 补 /v1")
    parser.add_argument("--resume-include-failed", action="store_true", help="resume 时重新纳入此前失败的样本")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records_by_id = load_records_by_id(args.records)
    records = list(records_by_id.values())
    if args.limit > 0:
        records = records[: args.limit]

    run_dir = model_run_dir(args.model_name, args.output_dir)
    output_file = args.output_file or (run_dir / "generations.jsonl")
    metadata_file = run_dir / "generation_config.json"

    done_ids = load_done_ids(output_file, include_failed=args.resume_include_failed) if args.resume else set()
    todo = [record for record in records if record["record_id"] not in done_ids]
    effective_base_url = normalize_base_url(args.base_url, auto_openai_path=not args.no_auto_openai_path)

    write_json(
        metadata_file,
        {
            "model_name": args.model_name,
            "api_model": args.api_model,
            "base_url": effective_base_url,
            "records": str(args.records),
            "total_records": len(records),
            "todo": len(todo),
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "workers": args.workers,
            "timeout": args.timeout,
            "connect_timeout": args.connect_timeout,
            "system_prompt_source": "backend/app/agents/prompts.py:PLANNER_AGENT_PROMPT",
            "system_prompt_policy": "prefer records[].system_prompt, fallback to backend/app/agents/prompts.py",
            "trust_env": args.trust_env,
            "resume_include_failed": args.resume_include_failed,
        },
    )

    print(
        f"生成 eval 输出: model={args.model_name}, total={len(records)}, todo={len(todo)}, "
        f"workers={args.workers}, base_url={effective_base_url}",
        flush=True,
    )
    ok = 0
    failed = 0
    try:
        if args.workers <= 1:
            for index, record in enumerate(todo, start=1):
                row = generate_one(record, args)
                append_jsonl(output_file, row)
                ok += int(row.get("ok", False))
                failed += int(not row.get("ok", False))
                status = "ok" if row.get("ok") else f"{row.get('error_type')}: {row.get('error', '')[:160]}"
                print(f"progress {index}/{len(todo)} ok={ok} failed={failed} last={record['record_id']} {status}", flush=True)
        else:
            with ThreadPoolExecutor(max_workers=args.workers) as executor:
                futures = {executor.submit(generate_one, record, args): record["record_id"] for record in todo}
                for index, future in enumerate(as_completed(futures), start=1):
                    row = future.result()
                    append_jsonl(output_file, row)
                    ok += int(row.get("ok", False))
                    failed += int(not row.get("ok", False))
                    status = "ok" if row.get("ok") else f"{row.get('error_type')}: {row.get('error', '')[:160]}"
                    print(f"progress {index}/{len(todo)} ok={ok} failed={failed} last={row['record_id']} {status}", flush=True)
    except KeyboardInterrupt:
        print(f"\n用户中断: 已写入 ok={ok}, failed={failed}, output={output_file}", flush=True)
        raise SystemExit(130)

    print(f"完成: ok={ok}, failed={failed}, output={output_file}")


if __name__ == "__main__":
    main()
