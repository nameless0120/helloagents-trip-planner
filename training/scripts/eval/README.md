# 兼容、评测与通用 DPO 脚本

这里同时保留旧 SFT 数据链路、评测脚本和通用 DPO 辅助脚本。它们不是一条默认串起来的流程，先按下面的入口区分：

如果要从头跑当前后训练流程，使用上一级的统一入口：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --output-dir training/data/planner/sft_runs/260831_smoke
```

它会把当前 SFT 的生成、预算审计、分类和导出串起来。下面的脚本保留为兼容入口、单步调试工具，以及通用 DPO/评测组件。

当前 SFT：

```text
planner/data/generate_sft_data.py
  -> planner/audit/audit_sft_budget_fit.py
  -> planner/audit/classify_sft_budget_usability.py
  -> planner/data/export_sft_budget_clean_subset.py
  -> validation/validate_trip_plan.py
  -> LLaMA-Factory SFT
```

当前 DPO 主线：

```text
planner/bestofn/prepare_*_dpo_contexts.py
  -> eval/dpo_build_prompts.py
  -> eval/dpo_generate_candidates.py
  -> planner/build_*_dpo.py 或 planner/bestofn/build_*_dpo_pairs.py
  -> LLaMA-Factory DPO 数据
  -> configs/qwen25_7b/dpo_*.yaml + planner/training/*.sh
```

旧 SFT：

```text
eval/generate_sft_data.py
  -> eval/filter_sft_data.py
  -> eval/split_sft_data.py
  -> legacy SFT train / val / eval
```

`eval/generate_sft_data.py` 只属于旧 SFT 链路。旧版本的 `controlled` 请求没有补齐当前 `TripRequest` 必填的 `party` 和 `budget_constraint`，所以会在 schema 校验处失败；现在脚本已经补上兼容字段，但它仍然只会生成 legacy 目录和 legacy 数据集。新数据不要再接旧的 filter 和 split，直接从 [`planner/data/generate_sft_data.py`](../planner/data/generate_sft_data.py) 开始，或使用上一级的 `run_pipeline.py`。

## Scripts

| Script | Purpose |
| --- | --- |
| `generate_sft_data.py` | 生成 legacy SFT 数据：模拟真实用户请求，调用真实高德工具快照，构造线上同款 Planner 输入，再用强模型蒸馏合法 `TripPlan` |
| `filter_sft_data.py` | 给旧样本补 `control_spec`，按人工确认的规则清洗脏样本，并导出 clean 版 LLaMA-Factory 训练文件 |
| `split_sft_data.py` | 把 clean 数据固定切成 train / val / eval，eval 作为独立冻结评估集 |
| `eval_generate.py` | 调用 OpenAI-compatible 模型服务，对冻结 eval 集生成候选 |
| `eval_rule_metrics.py` | 规则评估：JSON/schema/date/weather/grounding/hotel/meals/budget 等 |
| `eval_llm_judge.py` | 强模型 judge：偏好满足、可执行性、grounding、预算、连贯性、整体质量 |
| `eval_pairwise_judge.py` | 强模型 A/B 对比，例如 Base vs SFT |
| `eval_slice_report.py` | 按 `control_spec`、天气来源、天数等切片汇总评估结果 |
| `eval_pipeline.py` | 单模型评估入口：generate -> rule -> 可选 judge |
| `historical_weather.py` | 训练数据专用历史天气：用常用旅游城市坐标表调用 Open-Meteo Archive，并转换成 `trip_weather` 协议 |
| `dpo_build_prompts.py` | 通用 DPO prompt 构造工具，默认读取 legacy records；传入当前路径时也可用于当前 DPO smoke |
| `dpo_generate_candidates.py` | 通用多候选生成工具，支持 Base/SFT/Strong，并复用规则评估；默认输出仍是 legacy 路径 |
| `dpo_view_candidates.py` | 把 DPO candidates JSONL 渲染成终端/Markdown 预览，方便人工看同 prompt 多候选差异 |
| `dpo_judge_candidates.py` | 对通过硬过滤的候选做强模型 judge 多维评分 |
| `dpo_build_pairs.py` | 根据 judge 分数和阈值构造 chosen/rejected pair，并导出 LLaMA-Factory DPO 数据 |
| `dpo_audit_pairs.py` | 生成 DPO 数据审计报告，方便人工抽样检查 |

## Smoke

```bash
cd helloagents-trip-planner
.venv-training-py311/bin/python3 training/scripts/eval/generate_sft_data.py \
  --count 3 \
  --request-source template \
  --dry-run-requests
```

## Generate

```bash
.venv-training-py311/bin/python3 training/scripts/eval/generate_sft_data.py \
  --count 100 \
  --request-source llm \
  --date-mode mixed \
  --workers 32 \
  --resume
```

正式数据会写到 `training/data/legacy/sft/records.jsonl`，LLaMA-Factory 训练文件会写到 `training/data/llamafactory/trip_legacy_sft_train.json` 和 `training/data/llamafactory/trip_legacy_sft_val.json`。

正式生成是 worker 级流水线：每个 worker 独立执行“生成一条用户请求 -> 获取 PlannerContext -> 强模型生成 TripPlan -> schema 校验 -> 成功落盘”。单条失败只会重试/记录这一条，不会阻塞整批。

`--date-mode` 控制请求日期分布：

- `future`：默认值，只造未来行程，天气来自高德短期预报或远期未知占位。
- `past`：只造已经结束的历史行程，训练脚本会用 Open-Meteo Archive 改写 `trip_weather`。
- `mixed`：混合历史、近期和远期行程，用来同时覆盖“历史真实天气 / 高德短期天气 / 远期未知天气”三种行为。

历史天气只在训练数据脚本里生效，不改变线上后端。当前实现用常用旅游城市坐标表查询 Open-Meteo daily 数据，字段会转成：

```json
{
  "date": "2025-05-01",
  "day_weather": "小雨",
  "night_weather": "小雨",
  "day_temp": 30,
  "night_temp": 20,
  "wind_direction": "西",
  "wind_power": "3-4",
  "source": "open_meteo_archive"
}
```

## Filter

生成完成后先跑清洗脚本，再用 clean 版数据训练：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/filter_sft_data.py
```

当前清洗规则：

- `attractions` 每天 1-3 个都保留；如果任意一天超过 3 个景点，整条样本进入 dirty。
- 最后一天 `hotel=null` 可以保留；如果中间天 `hotel=null`，整条样本进入 dirty。
- 如果 `hotel.name` 是“无/无住宿/返程”等占位词，整条样本进入 dirty。

输出文件：

- `training/data/legacy/sft/records_with_control_spec.jsonl`
- `training/data/legacy/sft/requests_with_control_spec.jsonl`
- `training/data/legacy/sft/records_clean.jsonl`
- `training/data/legacy/sft/records_dirty.jsonl`
- `training/data/legacy/sft/records_dirty_summary.md`

`control_spec` 是请求生成时的抽样标签，例如同行类型、城市层级、预算档位、节奏、饮食和规避项。它不进入模型输入，但用于分布审计、定向补数据和切片评估。

## Split

清洗后再切分训练/验证/评估集：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/split_sft_data.py
```

默认比例为 `train=85%`、`val=5%`、`eval=10%`。脚本会按 `companion_type + city_tier + travel_days + weather_bucket` 做轻量分层，避免评估集分布太偏。

输出文件：

- `training/data/legacy/sft/records_train.jsonl`
- `training/data/legacy/sft/records_val.jsonl`
- `training/data/legacy/sft/records_eval.jsonl`
- `training/data/legacy/sft/split_summary.md`
- `training/data/llamafactory/trip_legacy_sft_clean_train.json`
- `training/data/llamafactory/trip_legacy_sft_clean_val.json`
- `training/data/llamafactory/trip_legacy_sft_clean_eval.json`

训练只使用 train/val，eval 冻结用于 SFT、DPO、SFT+DPO 的最终横向比较。

## Evaluate

先启动模型服务。SFT legacy clean 可以直接用新增的 variant：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
  --variant sft_legacy_clean \
  --cuda-visible-devices 0 \
  --api-model-name trip-planner-sft-legacy-clean
```

Base 模型服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/serve_planner_model.py \
  --variant base \
  --cuda-visible-devices 0 \
  --api-model-name trip-planner-base
```

单模型评估流水线：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_pipeline.py \
  --model-name sft_legacy_clean \
  --api-model trip-planner-sft-legacy-clean \
  --base-url http://127.0.0.1:4396/v1 \
  --workers 1 \
  --resume
```

只跑小样本 smoke：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_pipeline.py \
  --model-name sft_legacy_clean_smoke \
  --api-model trip-planner-sft-legacy-clean \
  --base-url http://127.0.0.1:4396/v1 \
  --limit 3
```

如果要接强模型 judge，在规则评估之后追加：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_pipeline.py \
  --model-name sft_legacy_clean \
  --api-model trip-planner-sft-legacy-clean \
  --base-url http://127.0.0.1:4396/v1 \
  --skip-generate \
  --skip-rule \
  --run-judge \
  --judge-workers 8 \
  --resume
```

Base vs SFT pairwise：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_pairwise_judge.py \
  --left-label base_qwen25_7b \
  --left-generations training/outputs/eval/base_qwen25_7b/generations.jsonl \
  --right-label sft_legacy_clean \
  --right-generations training/outputs/eval/sft_legacy_clean/generations.jsonl \
  --workers 8 \
  --resume
```

切片报告：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_slice_report.py \
  --model-report base_qwen25_7b=training/outputs/eval/base_qwen25_7b/rule_eval_report.json \
  --model-report sft_legacy_clean=training/outputs/eval/sft_legacy_clean/rule_eval_report.json \
  --judge sft_legacy_clean=training/outputs/eval/sft_legacy_clean/judge_scores.jsonl \
  --pairwise training/outputs/eval/comparison/pairwise_base_qwen25_7b_vs_sft_legacy_clean.jsonl \
  --pairwise-win-label right
```

评估报告默认写到：

- `training/outputs/eval/<model_name>/generations.jsonl`
- `training/outputs/eval/<model_name>/rule_eval_report.json`
- `training/outputs/eval/<model_name>/rule_eval_report.md`
- `training/outputs/eval/<model_name>/judge_scores.jsonl`
- `training/outputs/eval/<model_name>/judge_summary.md`
- `training/outputs/eval/comparison/`

## Amap Cache

PlannerContext 的高德 HTTP 入口默认启用本地缓存和进程内限速：

- 缓存目录：`training/data/cache/planner_context`
- 默认 TTL：60 小时
- 默认限速：3 QPS
- 覆盖环境变量：`PLANNER_CONTEXT_CACHE_TTL_SECONDS`、`PLANNER_CONTEXT_AMAP_CACHE_TTL_SECONDS`、`AMAP_QPS_LIMIT`

缓存命中后不会请求高德，适合大规模造数时重复城市、重复关键词、重复酒店类型的场景。正在运行的生成进程不会热更新代码；修改缓存逻辑后，需要重启生成脚本才会生效。

## 通用 DPO Data Smoke

下面是本目录提供的通用 DPO smoke 链路。默认路径和数据集名称仍是 legacy；如果传入 `training/data/planner/dpo` 下的当前数据，就要同时显式传入输入、输出和数据集名称。当前主线的 pair 构造还包括 `planner/build_*_dpo.py` 和 `planner/bestofn/build_*_dpo_pairs.py`，不能只看下面这组默认命令。

DPO 不用于修坏 JSON 或坏 schema。通用链路使用多模型自然候选、规则过滤和可选的 LLM judge 构造 chosen/rejected：

```text
dpo_build_prompts.py
  -> dpo_generate_candidates.py
  -> dpo_judge_candidates.py
  -> dpo_build_pairs.py
  -> dpo_audit_pairs.py
```

要跑这条通用链路，可以直接使用总入口：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage dpo \
  --records training/data/planner/sft_runs/<YYMMDD>_<run_slug>/records.jsonl \
  --output-dir training/data/planner/dpo/<YYMMDD>_<run_slug>
```

当前主线通常直接用候选规则指标筛选 pair，不一定调用 `dpo_judge_candidates.py`。当前公开说明见：

```text
training/docs/内部文档/DPO分块LogProb方案说明.md
```

第一轮建议先做 20 条 smoke，只验证数据链路和 pair 质量。

### 1. 构造 prompt 池

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_build_prompts.py \
  --records training/data/legacy/sft/records_train.jsonl \
  --limit 20 \
  --normalize-budget-text \
  --shuffle
```

输出：

```text
training/data/legacy/dpo/prompts.jsonl
```

`--normalize-budget-text` 用于把旧 SFT 记录里的精确随机预算改成更接近真实用户的表达：

- 低预算：按人均每天 200/300 元推导总预算
- 中等预算：按人均每天 400/500 元推导总预算
- 高预算：按人均每天 800/1000 元推导总预算
- 豪华预算：按人均每天 1200/1500/2000 元推导总预算

金额会按百元整数落地，统一表述成“总预算控制在 X 元左右”。DPO legacy 先只训练总预算语义，避免人均/每日/总额三种预算口径混杂。

### 酒店价格口径

地图 POI API 返回的是酒店候选，不是可预订 offer；高德 `hotel_pois.cost` 经常为空，因此当前版本不把 OTA 实时房价作为主线。legacy.1 的目标是先按住宿类型和城市层级生成确定性的 `estimated_cost_hint`：

- `hotel.estimated_cost` 表示单晚价格。
- 如果候选里有 `estimated_cost_hint`，模型必须复制该价格，不要自行估价。
- N 天行程默认住宿 N-1 晚，`budget.total_hotels` 必须覆盖住宿晚数。
- OTA/酒店 Shopping API 真实房价增强记录在根目录 `TODO.md`，后续作为独立工程项处理。

### 2. 生成多候选

默认生成：

- `base_t02`
- `base_t07`
- `sft_t02`

如果要加 DeepSeek/强模型候选，加 `--include-strong-low`。

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_generate_candidates.py \
  --prompts training/data/legacy/dpo/prompts.jsonl \
  --base-url http://127.0.0.1:4397/v1 \
  --base-api-model trip-planner-base \
  --sft-base-url http://127.0.0.1:4396/v1 \
  --sft-api-model trip-planner-sft-legacy-clean \
  --include-strong-low \
  --workers 8 \
  --local-workers 8 \
  --strong-workers 32 \
  --resume
```

候选生成默认带 `--json-parse-retries 5`：只有 JSON 解析失败时才重新采样，最多 5 次；如果 JSON 能解析但 schema/规则不合格，则保留该候选并交给硬过滤或 judge 处理。

并发口径：

- `--local-workers` 控制本地 vLLM/base/SFT 候选并发，建议 8。
- `--strong-workers` 控制强模型候选并发，建议 32。
- 如果不传这两个参数，脚本会退回旧行为：所有来源共用 `--workers`。

输出：

```text
training/data/legacy/dpo/candidates.jsonl
```

### 3. 查看多候选

终端查看前 3 个 prompt 的候选差异：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_view_candidates.py \
  --input training/data/legacy/dpo/candidates.jsonl \
  --limit 3
```

导出 Markdown 报告：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_view_candidates.py \
  --input training/data/legacy/dpo/candidates.jsonl \
  --limit 20 \
  --output training/data/legacy/dpo/candidates_preview.md
```

只看包含失败候选的 prompt：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_view_candidates.py \
  --input training/data/legacy/dpo/candidates.jsonl \
  --only-invalid \
  --show-output
```

### 4. Judge 打分

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_judge_candidates.py \
  --candidates training/data/legacy/dpo/candidates.jsonl \
  --workers 32 \
  --resume
```

输出：

```text
training/data/legacy/dpo/judgements.jsonl
```

### 5. 构造 DPO pair

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_build_pairs.py \
  --max-pairs-per-prompt 1 \
  --min-chosen-score 4.0 \
  --min-score-gap 0.8
```

输出：

```text
training/data/legacy/dpo/pairs.jsonl
training/data/legacy/dpo/pairs_train.jsonl
training/data/legacy/dpo/pairs_val.jsonl
training/data/llamafactory/trip_legacy_dpo_train.json
training/data/llamafactory/trip_legacy_dpo_val.json
```

同时会注册到：

```text
training/data/llamafactory/dataset_info.json
```

数据集名：

```text
trip_legacy_dpo_train
trip_legacy_dpo_val
```

### 6. 审计报告

```bash
.venv-training-py311/bin/python3 training/scripts/eval/dpo_audit_pairs.py
```

输出：

```text
training/data/legacy/dpo/audit_report.md
```

先人工看 `audit_report.md` 里的 10-20 对 pair，确认 chosen 真的比 rejected 好，再考虑扩到 100 条 prompt。
