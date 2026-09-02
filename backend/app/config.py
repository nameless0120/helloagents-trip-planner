"""应用配置和环境变量读取。"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[2]
BACKEND_ENV_FILE = PROJECT_ROOT / "backend" / ".env"
ROOT_ENV_FILE = PROJECT_ROOT / ".env"
HELLOAGENTS_ENV_FILE = PROJECT_ROOT.parent / "HelloAgents" / ".env"


def _load_env_files() -> None:
    """按项目路径加载环境变量，不依赖当前工作目录。"""
    for path in (BACKEND_ENV_FILE, ROOT_ENV_FILE, HELLOAGENTS_ENV_FILE):
        if path.is_file():
            load_dotenv(path, override=False)


_load_env_files()


class Settings(BaseSettings):
    """应用配置。环境变量名统一在字段上声明，避免各模块重复兜底。"""

    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        populate_by_name=False,
    )

    app_name: str = "HelloAgents智能旅行助手"
    app_version: str = "1.0.0"
    # 不读取通用的 DEBUG，避免被外部工具写入的 DEBUG=release 误当成布尔值。
    debug: bool = Field(default=False, validation_alias=AliasChoices("APP_DEBUG"))

    host: str = "0.0.0.0"
    port: int = 7000
    cors_origins: str = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://127.0.0.1:3000"

    amap_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("AMAP_API_KEY", "AMAP_MAPS_API_KEY"),
    )

    unsplash_access_key: str = ""
    unsplash_secret_key: str = ""

    # HelloAgents 目前读取 LLM_*；保留 OPENAI_* 作为兼容命名。
    openai_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("LLM_API_KEY", "OPENAI_API_KEY"),
    )
    openai_base_url: str = Field(
        default="https://api.openai.com/v1",
        validation_alias=AliasChoices("LLM_BASE_URL", "OPENAI_BASE_URL"),
    )
    openai_model: str = Field(
        default="gpt-4",
        validation_alias=AliasChoices("LLM_MODEL_ID", "OPENAI_MODEL"),
    )

    use_personalized_planner: bool = Field(
        default=False,
        validation_alias=AliasChoices("USE_PERSONALIZED_PLANNER"),
    )
    personalized_llm_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("PERSONALIZED_LLM_API_KEY"),
    )
    personalized_llm_base_url: str = Field(
        default="",
        validation_alias=AliasChoices("PERSONALIZED_LLM_BASE_URL"),
    )
    personalized_llm_model: str = Field(
        default="",
        validation_alias=AliasChoices("PERSONALIZED_LLM_MODEL_ID", "PERSONALIZED_LLM_MODEL"),
    )
    personalized_llm_provider: str = Field(
        default="openai",
        validation_alias=AliasChoices("PERSONALIZED_LLM_PROVIDER"),
    )

    log_level: str = "INFO"

    def get_cors_origins_list(self) -> List[str]:
        """返回去掉空白项的 CORS 来源列表。"""
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """返回进程内共享配置。测试或重载配置时可清理该缓存。"""
    return Settings()


# 保留模块级名称，兼容现有路由和服务的导入方式。
settings = get_settings()


def validate_config(current: Settings | None = None) -> bool:
    """检查启动所需配置。只在这里判断高德 key，其他模型 key 给出警告。"""
    current = current or get_settings()
    errors: list[str] = []
    warnings: list[str] = []

    if not current.amap_api_key:
        errors.append("AMAP_API_KEY 或 AMAP_MAPS_API_KEY 未配置")

    llm_api_key = current.openai_api_key or os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not llm_api_key:
        warnings.append("LLM_API_KEY 或 OPENAI_API_KEY 未配置，LLM 功能可能无法使用")

    if errors:
        error_msg = "配置错误:\n" + "\n".join(f"  - {error}" for error in errors)
        raise ValueError(error_msg)

    if warnings:
        print("\n⚠️  配置警告:")
        for warning in warnings:
            print(f"  - {warning}")

    return True


def print_config(current: Settings | None = None) -> None:
    """打印当前配置，隐藏密钥内容。"""
    current = current or get_settings()
    print(f"应用名称: {current.app_name}")
    print(f"版本: {current.app_version}")
    print(f"服务器: {current.host}:{current.port}")
    print(f"高德地图 API Key: {'已配置' if current.amap_api_key else '未配置'}")

    llm_api_key = current.openai_api_key or os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
    personalized_model = current.personalized_llm_model
    print(f"LLM API Key: {'已配置' if llm_api_key else '未配置'}")
    print(f"LLM Base URL: {current.openai_base_url}")
    print(f"LLM Model: {current.openai_model}")
    print(f"Personalized Planner: {'启用' if current.use_personalized_planner else '关闭'}")
    if current.use_personalized_planner:
        print(f"Personalized Planner Base URL: {current.personalized_llm_base_url or '未配置'}")
        print(f"Personalized Planner Model: {personalized_model or '未配置'}")
    print(f"日志级别: {current.log_level}")
