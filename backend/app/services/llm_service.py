"""LLM服务模块"""

import os
from contextlib import contextmanager
from typing import Iterator

from hello_agents import HelloAgentsLLM
from ..config import get_settings

# 全局LLM实例
_llm_instance = None
_planner_llm_instance = None


@contextmanager
def _temporary_env(overrides: dict[str, str]) -> Iterator[None]:
    """临时覆盖环境变量，用于创建独立 LLM 实例。"""
    previous = {key: os.environ.get(key) for key in overrides}
    try:
        for key, value in overrides.items():
            if value:
                os.environ[key] = value
        yield
    finally:
        for key, value in previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def get_llm() -> HelloAgentsLLM:
    """
    获取LLM实例(单例模式)

    Returns:
        HelloAgentsLLM实例
    """
    global _llm_instance

    if _llm_instance is None:
        # HelloAgentsLLM会自动从环境变量读取配置
        # 包括OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL等
        _llm_instance = HelloAgentsLLM()

        print("✅ LLM服务初始化成功")
        print(f"   提供商: {_llm_instance.provider}")
        print(f"   模型: {_llm_instance.model}")

    return _llm_instance


def get_planner_llm() -> HelloAgentsLLM:
    """
    获取最终行程规划 LLM。

    默认返回通用 LLM；当 USE_PERSONALIZED_PLANNER=true 且配置完整时，
    仅 planner agent 使用个性化微调模型。
    """
    global _planner_llm_instance

    settings = get_settings()
    if not settings.use_personalized_planner:
        return get_llm()

    if _planner_llm_instance is None:
        model = os.getenv("PERSONALIZED_LLM_MODEL_ID") or settings.personalized_llm_model
        base_url = settings.personalized_llm_base_url
        api_key = settings.personalized_llm_api_key or "EMPTY"
        provider = settings.personalized_llm_provider or "openai"

        if not model or not base_url:
            print("⚠️  个性化 Planner 配置不完整，将使用默认 LLM")
            return get_llm()

        overrides = {
            "LLM_API_KEY": api_key,
            "OPENAI_API_KEY": api_key,
            "LLM_BASE_URL": base_url,
            "OPENAI_BASE_URL": base_url,
            "LLM_MODEL_ID": model,
            "OPENAI_MODEL": model,
            "LLM_PROVIDER": provider,
        }
        with _temporary_env(overrides):
            _planner_llm_instance = HelloAgentsLLM()

        print("✅ 个性化 Planner LLM 初始化成功")
        print(f"   提供商: {_planner_llm_instance.provider}")
        print(f"   模型: {_planner_llm_instance.model}")
        print(f"   Base URL: {base_url}")

    return _planner_llm_instance


def reset_llm():
    """重置LLM实例(用于测试或重新配置)"""
    global _llm_instance, _planner_llm_instance
    _llm_instance = None
    _planner_llm_instance = None
