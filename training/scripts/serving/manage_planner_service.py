#!/usr/bin/env python3
"""Start/stop/status helper for the local trip planner model service.

The LLaMA-Factory launcher can leave a child ``llamafactory-cli`` process alive
if only the wrapper process is killed.  This helper starts the service in its
own process group and records both PID and PGID, so stop/restart can reliably
clean the whole tree.
"""

from __future__ import annotations

import argparse
import getpass
import json
import os
import signal
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PYTHON = PROJECT_ROOT / ".venv-training-py311/bin/python3"
SERVE_SCRIPT = PROJECT_ROOT / "training/scripts/serving/serve_planner_model.py"
STATE_DIR = PROJECT_ROOT / "training/outputs/model_service"
PID_DIR = STATE_DIR / "pids"
DEFAULT_LOG_DIR = PROJECT_ROOT / "training/outputs/qwen25_7b"

DEFAULT_PORT = 4396
DEFAULT_VARIANT = "base"
DEFAULT_BACKEND = "vllm"
DEFAULT_DEVICES = "4,5,6,7"
DEFAULT_API_MODEL = "trip-planner-base"


@dataclass(frozen=True)
class ManagedService:
    name: str
    variant: str
    default_port: int
    default_devices: str
    default_api_model_name: str
    no_adapter: bool = False


MANAGED_SERVICES = {
    "base": ManagedService(
        name="base",
        variant="base",
        default_port=4397,
        default_devices="4,5",
        default_api_model_name="trip-planner-base",
        no_adapter=True,
    ),
    "sft": ManagedService(
        name="sft",
        variant="sft",
        default_port=4396,
        default_devices="6",
        default_api_model_name="trip-planner-sft",
    ),
    "dpo": ManagedService(
        name="dpo",
        variant="dpo",
        default_port=4398,
        default_devices="7",
        default_api_model_name="trip-planner-dpo",
    ),
}
SERVICE_ORDER = tuple(MANAGED_SERVICES)
DEFAULT_ADAPTER_PATHS = {
    "sft": PROJECT_ROOT / "training/outputs/qwen25_7b/sft",
    "dpo": PROJECT_ROOT / "training/outputs/qwen25_7b/dpo",
    "sft_dpo": PROJECT_ROOT / "training/outputs/qwen25_7b/sft_dpo",
}


def pidfile_for(port: int) -> Path:
    return PID_DIR / f"planner_model_{port}.json"


def read_state(port: int) -> dict[str, Any] | None:
    path = pidfile_for(port)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def write_state(port: int, state: dict[str, Any]) -> None:
    PID_DIR.mkdir(parents=True, exist_ok=True)
    pidfile_for(port).write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def remove_state(port: int) -> None:
    pidfile_for(port).unlink(missing_ok=True)


def process_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def process_group_alive(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def run_capture(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def port_pids(port: int) -> set[int]:
    result = run_capture(["ss", "-ltnp"])
    pids: set[int] = set()
    marker = f":{port} "
    for line in result.stdout.splitlines():
        if marker not in line:
            continue
        # Example: users:(("llamafactory-cl",pid=3016077,fd=87))
        for chunk in line.split("pid=")[1:]:
            digits = []
            for char in chunk:
                if char.isdigit():
                    digits.append(char)
                else:
                    break
            if digits:
                pids.add(int("".join(digits)))
    return pids


def proc_info(pid: int) -> tuple[str, int, str] | None:
    result = run_capture(["ps", "-p", str(pid), "-o", "user=", "-o", "pgid=", "-o", "cmd="])
    if result.returncode != 0 or not result.stdout.strip():
        return None
    line = result.stdout.strip()
    parts = line.split(None, 2)
    if len(parts) < 3:
        return None
    user, pgid, cmd = parts
    return user, int(pgid), cmd


def safe_pgid_from_port_pid(pid: int) -> int | None:
    info = proc_info(pid)
    if info is None:
        return None
    user, pgid, cmd = info
    if user != getpass.getuser():
        return None
    safe_markers = [
        "helloagents-trip-planner",
        ".serve_qwen25_7b",
        "serve_planner_model.py",
        "llamafactory-cli api",
    ]
    if not any(marker in cmd for marker in safe_markers):
        return None
    return pgid


def wait_until_port_closed(port: int, timeout: float) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not port_pids(port):
            return True
        time.sleep(0.5)
    return not port_pids(port)


def kill_pgid(pgid: int, sig: signal.Signals) -> bool:
    try:
        os.killpg(pgid, sig)
        return True
    except ProcessLookupError:
        return False
    except PermissionError as exc:
        print(f"permission denied killing pgid={pgid}: {exc}", file=sys.stderr)
        return False


def parse_service_names(value: str) -> list[str]:
    services = [item.strip() for item in value.split(",") if item.strip()]
    unknown = [item for item in services if item not in MANAGED_SERVICES]
    if unknown:
        allowed = ", ".join(SERVICE_ORDER)
        raise argparse.ArgumentTypeError(
            f"unknown service(s): {', '.join(unknown)}; allowed: {allowed}"
        )
    return services


def selected_service_specs(args: argparse.Namespace) -> list[ManagedService]:
    services = args.services if isinstance(args.services, list) else parse_service_names(args.services)
    return [MANAGED_SERVICES[name] for name in SERVICE_ORDER if name in services]


def default_adapter_path(variant: str) -> Path | None:
    return DEFAULT_ADAPTER_PATHS.get(variant)


def resolved_adapter_path(args: argparse.Namespace) -> Path | None:
    if args.no_adapter:
        return None
    adapter_path = args.adapter_path or default_adapter_path(args.variant)
    return adapter_path.expanduser().resolve() if adapter_path else None


def adapter_problem(path: Path) -> str | None:
    if not path.exists():
        return f"adapter path does not exist: {path}"
    adapter_config = path / "adapter_config.json"
    adapter_weights = [
        path / "adapter_model.safetensors",
        path / "adapter_model.bin",
    ]
    if not adapter_config.exists() or not any(item.exists() for item in adapter_weights):
        return (
            f"adapter path does not look like a finished LoRA checkpoint: {path}; "
            "expected adapter_config.json and adapter_model.safetensors or adapter_model.bin"
        )
    return None


def validate_start_inputs(args: argparse.Namespace) -> int:
    adapter_path = resolved_adapter_path(args)
    if adapter_path is None:
        return 0
    problem = adapter_problem(adapter_path)
    if not problem:
        return 0
    if getattr(args, "dry_run", False):
        print(f"warning: {problem}", file=sys.stderr)
        return 0
    print(f"Error: {problem}", file=sys.stderr)
    return 2


def status(args: argparse.Namespace) -> int:
    state = read_state(args.port)
    print(f"port: {args.port}")
    if state:
        pid = int(state.get("pid", 0))
        pgid = int(state.get("pgid", 0))
        print(f"pidfile: {pidfile_for(args.port)}")
        print(f"state pid={pid} alive={process_alive(pid)} pgid={pgid} group_alive={process_group_alive(pgid)}")
        print(f"log: {state.get('log_file')}")
        print(f"cmd: {' '.join(state.get('cmd', []))}")
    else:
        print("pidfile: missing")

    pids = sorted(port_pids(args.port))
    if pids:
        print(f"listening pids: {', '.join(map(str, pids))}")
        for pid in pids:
            info = proc_info(pid)
            if info:
                user, pgid, cmd = info
                print(f"  pid={pid} user={user} pgid={pgid} cmd={cmd}")
    else:
        print("listening pids: none")
    return 0


def stop(args: argparse.Namespace) -> int:
    pgids: set[int] = set()
    state = read_state(args.port)
    if state:
        pgid = int(state.get("pgid", 0) or 0)
        if pgid and process_group_alive(pgid):
            pgids.add(pgid)

    for pid in port_pids(args.port):
        pgid = safe_pgid_from_port_pid(pid)
        if pgid:
            pgids.add(pgid)

    if not pgids:
        print(f"no local planner service found on port {args.port}")
        remove_state(args.port)
        return 0

    for pgid in sorted(pgids):
        print(f"stopping process group pgid={pgid} with SIGTERM")
        kill_pgid(pgid, signal.SIGTERM)

    if not wait_until_port_closed(args.port, args.timeout):
        print(f"port {args.port} still busy after {args.timeout}s")
        if args.kill:
            for pgid in sorted(pgids):
                print(f"forcing process group pgid={pgid} with SIGKILL")
                kill_pgid(pgid, signal.SIGKILL)
            wait_until_port_closed(args.port, 5)
        else:
            print("rerun stop with --kill if it refuses to exit", file=sys.stderr)
            return 1

    remove_state(args.port)
    print(f"stopped planner service on port {args.port}")
    return 0


def start(args: argparse.Namespace) -> int:
    input_status = validate_start_inputs(args)
    if input_status:
        return input_status
    adapter_path = resolved_adapter_path(args)

    existing = port_pids(args.port)
    if existing and not args.force:
        print(f"port {args.port} is already in use by pid(s): {', '.join(map(str, sorted(existing)))}", file=sys.stderr)
        print("run `status`, or `stop --kill`, or pass --force if you know what you are doing", file=sys.stderr)
        return 1

    log_file = args.log_file
    if log_file is None:
        DEFAULT_LOG_DIR.mkdir(parents=True, exist_ok=True)
        log_file = DEFAULT_LOG_DIR / f"serve_{args.port}_{args.api_model_name}.log"
    log_file = log_file.expanduser().resolve()
    log_file.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        str(PYTHON),
        "-u",
        str(SERVE_SCRIPT),
        "--variant",
        args.variant,
        "--infer-backend",
        args.infer_backend,
        "--cuda-visible-devices",
        args.cuda_visible_devices,
        "--api-model-name",
        args.api_model_name,
        "--port",
        str(args.port),
    ]
    if args.model_path:
        cmd.extend(["--model-path", str(args.model_path)])
    if args.infer_backend == "vllm":
        cmd.extend(["--vllm-maxlen", str(args.vllm_maxlen), "--vllm-gpu-util", str(args.vllm_gpu_util)])
    if args.adapter_path:
        cmd.extend(["--adapter-path", str(args.adapter_path)])
    if args.no_adapter:
        cmd.append("--no-adapter")

    if getattr(args, "dry_run", False):
        print(f"would start planner service port={args.port}")
        print(f"endpoint: http://127.0.0.1:{args.port}/v1")
        print(f"api model: {args.api_model_name}")
        print(f"cmd: {' '.join(cmd)}")
        return 0

    env = os.environ.copy()
    env.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

    with log_file.open("ab", buffering=0) as log:
        proc = subprocess.Popen(
            cmd,
            cwd=str(PROJECT_ROOT),
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            env=env,
            start_new_session=True,
        )

    pgid = os.getpgid(proc.pid)
    state = {
        "pid": proc.pid,
        "pgid": pgid,
        "port": args.port,
        "variant": args.variant,
        "infer_backend": args.infer_backend,
        "cuda_visible_devices": args.cuda_visible_devices,
        "api_model_name": args.api_model_name,
        "model_path": str(args.model_path) if args.model_path else None,
        "adapter_path": str(adapter_path) if adapter_path else None,
        "log_file": str(log_file),
        "cmd": cmd,
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    write_state(args.port, state)
    print(f"started planner service pid={proc.pid} pgid={pgid} port={args.port}")
    print(f"log: {log_file}")
    print(f"endpoint: http://127.0.0.1:{args.port}/v1")
    print(f"api model: {args.api_model_name}")
    return 0


def restart(args: argparse.Namespace) -> int:
    stop_args = argparse.Namespace(port=args.port, timeout=args.timeout, kill=True)
    stop(stop_args)
    return start(args)


def service_start_args(args: argparse.Namespace, service: ManagedService) -> argparse.Namespace:
    port = getattr(args, service.name + "_port")
    api_model_name = getattr(args, service.name + "_api_model_name")
    log_file = None
    if args.log_dir:
        log_file = args.log_dir / f"serve_{port}_{api_model_name}.log"
    return argparse.Namespace(
        port=port,
        variant=service.variant,
        infer_backend=args.infer_backend,
        cuda_visible_devices=getattr(args, service.name + "_devices"),
        api_model_name=api_model_name,
        model_path=args.model_path,
        adapter_path=getattr(args, service.name + "_adapter_path", None),
        no_adapter=service.no_adapter,
        vllm_maxlen=args.vllm_maxlen,
        vllm_gpu_util=args.vllm_gpu_util,
        log_file=log_file,
        force=args.force,
        dry_run=args.dry_run,
    )


def service_stop_args(args: argparse.Namespace, service: ManagedService) -> argparse.Namespace:
    return argparse.Namespace(
        port=getattr(args, service.name + "_port"),
        timeout=args.timeout,
        kill=args.kill,
    )


def service_status_args(args: argparse.Namespace, service: ManagedService) -> argparse.Namespace:
    return argparse.Namespace(port=getattr(args, service.name + "_port"))


def status_all(args: argparse.Namespace) -> int:
    exit_code = 0
    for service in selected_service_specs(args):
        print(f"\n== {service.name} ({service.default_api_model_name}) ==")
        exit_code = max(exit_code, status(service_status_args(args, service)))
    return exit_code


def stop_all(args: argparse.Namespace) -> int:
    exit_code = 0
    for service in reversed(selected_service_specs(args)):
        print(f"\n== {service.name} ({service.default_api_model_name}) ==")
        exit_code = max(exit_code, stop(service_stop_args(args, service)))
    return exit_code


def start_all(args: argparse.Namespace) -> int:
    service_args = [(service, service_start_args(args, service)) for service in selected_service_specs(args)]
    if not args.dry_run:
        for service, start_args in service_args:
            input_status = validate_start_inputs(start_args)
            if input_status:
                print(f"failed before starting services: {service.name}", file=sys.stderr)
                return input_status
            existing = port_pids(start_args.port)
            if existing and not start_args.force:
                pids = ", ".join(map(str, sorted(existing)))
                print(
                    f"failed before starting services: port {start_args.port} "
                    f"is already in use by pid(s): {pids}",
                    file=sys.stderr,
                )
                return 1

    for service, start_args in service_args:
        print(f"\n== {service.name} ({start_args.api_model_name}) ==")
        exit_code = start(start_args)
        if exit_code:
            return exit_code
    return 0


def restart_all(args: argparse.Namespace) -> int:
    stop_code = stop_all(args)
    if stop_code:
        return stop_code
    return start_all(args)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage the local trip planner model service.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common(sub: argparse.ArgumentParser) -> None:
        sub.add_argument("--port", type=int, default=DEFAULT_PORT)

    def add_multi_common(sub: argparse.ArgumentParser) -> None:
        sub.add_argument(
            "--services",
            type=parse_service_names,
            default=list(SERVICE_ORDER),
            help=f"Comma-separated services to manage. Available: {', '.join(SERVICE_ORDER)}.",
        )
        sub.add_argument("--base-port", type=int, default=MANAGED_SERVICES["base"].default_port)
        sub.add_argument("--sft-port", type=int, default=MANAGED_SERVICES["sft"].default_port)
        sub.add_argument("--dpo-port", type=int, default=MANAGED_SERVICES["dpo"].default_port)

    def add_multi_start_options(sub: argparse.ArgumentParser) -> None:
        sub.add_argument("--infer-backend", choices=["huggingface", "vllm", "sglang", "ktransformers"], default=DEFAULT_BACKEND)
        sub.add_argument("--model-path", type=Path, default=None, help="Base model path or HF repo id passed to serve_planner_model.py.")
        sub.add_argument("--base-devices", default=MANAGED_SERVICES["base"].default_devices)
        sub.add_argument("--sft-devices", default=MANAGED_SERVICES["sft"].default_devices)
        sub.add_argument("--dpo-devices", default=MANAGED_SERVICES["dpo"].default_devices)
        sub.add_argument("--base-api-model-name", default=MANAGED_SERVICES["base"].default_api_model_name)
        sub.add_argument("--sft-api-model-name", default=MANAGED_SERVICES["sft"].default_api_model_name)
        sub.add_argument("--dpo-api-model-name", default=MANAGED_SERVICES["dpo"].default_api_model_name)
        sub.add_argument("--sft-adapter-path", type=Path, default=None)
        sub.add_argument("--dpo-adapter-path", type=Path, default=None)
        sub.add_argument("--vllm-maxlen", type=int, default=32768)
        sub.add_argument("--vllm-gpu-util", type=float, default=0.85)
        sub.add_argument("--log-dir", type=Path, default=None)
        sub.add_argument("--force", action="store_true", help="Start even if a selected port appears busy.")
        sub.add_argument("--dry-run", action="store_true", help="Print the services that would be started.")

    status_parser = subparsers.add_parser("status", help="Show service status.")
    add_common(status_parser)
    status_parser.set_defaults(func=status)

    stop_parser = subparsers.add_parser("stop", help="Stop service by pidfile and port fallback.")
    add_common(stop_parser)
    stop_parser.add_argument("--timeout", type=float, default=20)
    stop_parser.add_argument("--kill", action="store_true", help="Escalate to SIGKILL if SIGTERM does not exit.")
    stop_parser.set_defaults(func=stop)

    start_parser = subparsers.add_parser("start", help="Start service in a managed process group.")
    add_common(start_parser)
    start_parser.add_argument("--variant", default=DEFAULT_VARIANT)
    start_parser.add_argument("--infer-backend", choices=["huggingface", "vllm", "sglang", "ktransformers"], default=DEFAULT_BACKEND)
    start_parser.add_argument("--cuda-visible-devices", "--devices", default=DEFAULT_DEVICES)
    start_parser.add_argument("--api-model-name", default=DEFAULT_API_MODEL)
    start_parser.add_argument("--model-path", type=Path, default=None, help="Base model path or HF repo id passed to serve_planner_model.py.")
    start_parser.add_argument("--adapter-path", type=Path, default=None)
    start_parser.add_argument("--no-adapter", action="store_true")
    start_parser.add_argument("--vllm-maxlen", type=int, default=32768)
    start_parser.add_argument("--vllm-gpu-util", type=float, default=0.85)
    start_parser.add_argument("--log-file", type=Path, default=None)
    start_parser.add_argument("--force", action="store_true", help="Start even if the port appears busy.")
    start_parser.set_defaults(func=start)

    restart_parser = subparsers.add_parser("restart", help="Stop then start service.")
    add_common(restart_parser)
    restart_parser.add_argument("--timeout", type=float, default=20)
    restart_parser.add_argument("--variant", default=DEFAULT_VARIANT)
    restart_parser.add_argument("--infer-backend", choices=["huggingface", "vllm", "sglang", "ktransformers"], default=DEFAULT_BACKEND)
    restart_parser.add_argument("--cuda-visible-devices", "--devices", default=DEFAULT_DEVICES)
    restart_parser.add_argument("--api-model-name", default=DEFAULT_API_MODEL)
    restart_parser.add_argument("--model-path", type=Path, default=None, help="Base model path or HF repo id passed to serve_planner_model.py.")
    restart_parser.add_argument("--adapter-path", type=Path, default=None)
    restart_parser.add_argument("--no-adapter", action="store_true")
    restart_parser.add_argument("--vllm-maxlen", type=int, default=32768)
    restart_parser.add_argument("--vllm-gpu-util", type=float, default=0.85)
    restart_parser.add_argument("--log-file", type=Path, default=None)
    restart_parser.add_argument("--force", action="store_true")
    restart_parser.set_defaults(func=restart)

    status_all_parser = subparsers.add_parser("status-all", help="Show status for the base/SFT/DPO services.")
    add_multi_common(status_all_parser)
    status_all_parser.set_defaults(func=status_all)

    stop_all_parser = subparsers.add_parser("stop-all", help="Stop the selected base/SFT/DPO services.")
    add_multi_common(stop_all_parser)
    stop_all_parser.add_argument("--timeout", type=float, default=20)
    stop_all_parser.add_argument("--kill", action="store_true", help="Escalate to SIGKILL if SIGTERM does not exit.")
    stop_all_parser.set_defaults(func=stop_all)

    start_all_parser = subparsers.add_parser("start-all", help="Start the selected base/SFT/DPO services.")
    add_multi_common(start_all_parser)
    add_multi_start_options(start_all_parser)
    start_all_parser.set_defaults(func=start_all)

    restart_all_parser = subparsers.add_parser("restart-all", help="Stop then start the selected base/SFT/DPO services.")
    add_multi_common(restart_all_parser)
    restart_all_parser.add_argument("--timeout", type=float, default=20)
    restart_all_parser.add_argument("--kill", action="store_true", help="Escalate to SIGKILL if SIGTERM does not exit.")
    add_multi_start_options(restart_all_parser)
    restart_all_parser.set_defaults(func=restart_all)

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
