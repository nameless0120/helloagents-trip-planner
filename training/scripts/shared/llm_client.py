"""OpenAI-compatible 数据生成客户端。"""

from __future__ import annotations

import os
import json
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from openai import OpenAI  # noqa: E402

from shared.common import extract_json, load_project_env  # noqa: E402


_usage_log_lock = threading.Lock()


def _usage_to_dict(usage: Any) -> dict[str, Any] | None:
    """把 OpenAI-compatible usage 对象转成可落盘的 dict。"""
    if usage is None:
        return None
    if isinstance(usage, dict):
        return usage
    if hasattr(usage, "model_dump"):
        return usage.model_dump()
    if hasattr(usage, "dict"):
        return usage.dict()
    try:
        return json.loads(json.dumps(usage, default=lambda obj: getattr(obj, "__dict__", str(obj))))
    except TypeError:
        return {"raw": str(usage)}


class DataGenLLM:
    """使用 OpenAI-compatible 强模型生成训练数据。"""

    def __init__(self, provider: str | None = None, model: str | None = None) -> None:
        load_project_env()
        provider = (provider or os.getenv("DATA_GEN_PROVIDER") or "env").strip().lower()
        api_key, base_url, model, timeout, reasoning_effort, enable_thinking = self._resolve_config(provider, model)

        if not api_key:
            raise RuntimeError(f"缺少 {provider} 数据生成模型 API Key 配置")
        if not base_url:
            raise RuntimeError(f"缺少 {provider} 数据生成模型 Base URL 配置")
        if not model:
            raise RuntimeError(f"缺少 {provider} 数据生成模型 model 配置")

        self.provider = provider
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
        self.base_url = base_url
        self.reasoning_effort = reasoning_effort
        self.enable_thinking = enable_thinking
        self.usage_log_path = os.getenv("DATA_GEN_USAGE_LOG")
        self.last_usage: dict[str, Any] | None = None

    @staticmethod
    def _env_truthy(name: str, default: bool = False) -> bool:
        raw = os.getenv(name)
        if raw is None:
            return default
        return raw.lower() in {"1", "true", "yes", "on"}

    @staticmethod
    def _resolve_config(
        provider: str,
        model_override: str | None,
    ) -> tuple[str | None, str, str, float, str | None, bool]:
        if provider == "env":
            api_key = os.getenv("DATA_GEN_API_KEY") or os.getenv("DEEPSEEK_API_KEY") or os.getenv("LLM_API_KEY")
            base_url = os.getenv("DATA_GEN_BASE_URL") or os.getenv("DEEPSEEK_BASE_URL") or "https://api.deepseek.com"
            model = model_override or os.getenv("DATA_GEN_MODEL") or os.getenv("DEEPSEEK_MODEL") or "deepseek-v4-pro"
            timeout = float(os.getenv("DATA_GEN_TIMEOUT") or os.getenv("DEEPSEEK_TIMEOUT") or "660")
            reasoning_effort = os.getenv("DATA_GEN_REASONING_EFFORT") or os.getenv("DEEPSEEK_REASONING_EFFORT") or "high"
            enable_thinking = DataGenLLM._env_truthy("DATA_GEN_THINKING", DataGenLLM._env_truthy("DEEPSEEK_THINKING", False))
            if not enable_thinking:
                reasoning_effort = None
            return api_key, base_url, model, timeout, reasoning_effort, enable_thinking

        if provider == "deepseek":
            api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("DATA_GEN_API_KEY") or os.getenv("LLM_API_KEY")
            base_url = os.getenv("DEEPSEEK_BASE_URL") or os.getenv("DATA_GEN_BASE_URL") or "https://api.deepseek.com"
            model = model_override or os.getenv("DATA_GEN_MODEL") or os.getenv("DEEPSEEK_MODEL") or "deepseek-v4-pro"
            timeout = float(os.getenv("DATA_GEN_TIMEOUT") or os.getenv("DEEPSEEK_TIMEOUT") or "660")
            reasoning_effort = os.getenv("DATA_GEN_REASONING_EFFORT") or os.getenv("DEEPSEEK_REASONING_EFFORT") or "high"
            enable_thinking = DataGenLLM._env_truthy("DATA_GEN_THINKING", DataGenLLM._env_truthy("DEEPSEEK_THINKING", False))
            if not enable_thinking:
                reasoning_effort = None
            return api_key, base_url, model, timeout, reasoning_effort, enable_thinking

        if provider == "mimo":
            api_key = os.getenv("MIMO_API_KEY")
            base_url = os.getenv("MIMO_OPENAI_BASE_URL") or os.getenv("MIMO_BASE_URL") or ""
            model = model_override or os.getenv("MIMO_MODEL") or "mimo-v2.5-pro"
            timeout = float(os.getenv("MIMO_TIMEOUT") or os.getenv("DATA_GEN_TIMEOUT") or "660")
            reasoning_effort = os.getenv("MIMO_REASONING_EFFORT") or None
            enable_thinking = DataGenLLM._env_truthy("MIMO_THINKING", False)
            if not enable_thinking:
                reasoning_effort = None
            return api_key, base_url, model, timeout, reasoning_effort, enable_thinking

        raise ValueError(f"不支持的数据生成模型 provider: {provider}")

    def complete_json(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        temperature: float = 0.4,
        max_tokens: int = 4096,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        """调用模型并解析 JSON。"""
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        }
        if self.enable_thinking:
            if self.reasoning_effort:
                kwargs["reasoning_effort"] = self.reasoning_effort
            kwargs["extra_body"] = {"thinking": {"type": "enabled"}}

        response = self.client.chat.completions.create(**kwargs)
        usage = _usage_to_dict(getattr(response, "usage", None))
        self.last_usage = usage
        if self.usage_log_path and usage is not None:
            row = {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "provider": self.provider,
                "model": self.model,
                "reasoning_effort": self.reasoning_effort,
                "thinking": self.enable_thinking,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "usage": usage,
                "metadata": metadata or {},
            }
            path = Path(self.usage_log_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with _usage_log_lock:
                with path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
        content = response.choices[0].message.content or ""
        return extract_json(content)
