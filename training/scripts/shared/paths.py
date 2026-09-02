"""当前后训练目录的唯一来源。

脚本可以从不同工作目录直接启动，因此不要在各个入口里重复拼接路径。
这里只定义当前主线使用的目录，不保留已经移除的旧版目录别名。
"""

from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
TRAINING_DIR = PROJECT_ROOT / "training"
SCRIPTS_DIR = TRAINING_DIR / "scripts"
CONFIGS_DIR = TRAINING_DIR / "configs"
PATCHES_DIR = TRAINING_DIR / "patches"

DATA_DIR = TRAINING_DIR / "data"
PLANNER_DATA_DIR = DATA_DIR / "planner"
SFT_RUNS_DIR = PLANNER_DATA_DIR / "sft_runs"
BESTOFN_DIR = PLANNER_DATA_DIR / "bestofn"
DPO_DIR = PLANNER_DATA_DIR / "dpo"
EVAL_DATA_DIR = PLANNER_DATA_DIR / "eval"
EVAL_HARD_DATA_DIR = PLANNER_DATA_DIR / "eval_hard"
ATTRACTION_PRICES_DIR = PLANNER_DATA_DIR / "attraction_prices"

LLAMAFACTORY_DIR = DATA_DIR / "llamafactory"
LLAMAFACTORY_GENERATED_DIR = LLAMAFACTORY_DIR / "generated"

OUTPUTS_DIR = TRAINING_DIR / "outputs"
EVAL_OUTPUT_DIR = OUTPUTS_DIR / "eval"
