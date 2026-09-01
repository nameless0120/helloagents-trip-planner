"""Planner 评估流水线入口。

该脚本负责串联：

1. eval_generate.py
2. eval_rule_metrics.py
3. 可选 eval_llm_judge.py

pairwise 和 slice 报告通常需要多个模型输出，单独用对应脚本执行。
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from eval_utils import DEFAULT_EVAL_OUTPUT_DIR, DEFAULT_EVAL_RECORDS, model_run_dir


SCRIPT_DIR = Path(__file__).resolve().parent


def run_step(cmd: list[str], dry_run: bool = False) -> None:
    """执行一个步骤。"""
    print("\n$ " + " ".join(cmd), flush=True)
    if dry_run:
        return
    subprocess.run(cmd, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="运行 Planner 单模型评估流水线。")
    parser.add_argument("--records", type=Path, default=DEFAULT_EVAL_RECORDS)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--api-model", required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:4396/v1")
    parser.add_argument("--api-key", default=None)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_EVAL_OUTPUT_DIR)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--timeout", type=float, default=660)
    parser.add_argument("--connect-timeout", type=float, default=10)
    parser.add_argument("--max-tokens", type=int, default=0)
    parser.add_argument("--trust-env", action="store_true", help="允许本地模型请求读取 HTTP_PROXY/HTTPS_PROXY 等环境代理")
    parser.add_argument("--no-auto-openai-path", action="store_true", help="不要自动给 base_url 补 /v1")
    parser.add_argument("--resume-include-failed", action="store_true", help="resume 时重新纳入此前失败的样本")
    parser.add_argument("--skip-generate", action="store_true")
    parser.add_argument("--skip-rule", action="store_true")
    parser.add_argument("--run-judge", action="store_true")
    parser.add_argument("--judge-workers", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_dir = model_run_dir(args.model_name, args.output_dir)
    generations = run_dir / "generations.jsonl"

    if not args.skip_generate:
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "eval_generate.py"),
            "--records",
            str(args.records),
            "--model-name",
            args.model_name,
            "--api-model",
            args.api_model,
            "--base-url",
            args.base_url,
            "--output-dir",
            str(args.output_dir),
            "--workers",
            str(args.workers),
            "--temperature",
            str(args.temperature),
            "--timeout",
            str(args.timeout),
            "--connect-timeout",
            str(args.connect_timeout),
        ]
        if args.max_tokens:
            cmd.extend(["--max-tokens", str(args.max_tokens)])
        if args.trust_env:
            cmd.append("--trust-env")
        if args.no_auto_openai_path:
            cmd.append("--no-auto-openai-path")
        if args.resume_include_failed:
            cmd.append("--resume-include-failed")
        if args.api_key:
            cmd.extend(["--api-key", args.api_key])
        if args.limit:
            cmd.extend(["--limit", str(args.limit)])
        if args.resume:
            cmd.append("--resume")
        run_step(cmd, dry_run=args.dry_run)

    if not args.skip_rule:
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "eval_rule_metrics.py"),
            "--records",
            str(args.records),
            "--generations",
            str(generations),
            "--model-name",
            args.model_name,
            "--output-dir",
            str(args.output_dir),
        ]
        run_step(cmd, dry_run=args.dry_run)

    if args.run_judge:
        cmd = [
            sys.executable,
            str(SCRIPT_DIR / "eval_llm_judge.py"),
            "--records",
            str(args.records),
            "--generations",
            str(generations),
            "--model-name",
            args.model_name,
            "--output-dir",
            str(args.output_dir),
            "--workers",
            str(args.judge_workers),
        ]
        if args.limit:
            cmd.extend(["--limit", str(args.limit)])
        if args.resume:
            cmd.append("--resume")
        run_step(cmd, dry_run=args.dry_run)

    print(f"\n评估目录: {run_dir}")


if __name__ == "__main__":
    main()
