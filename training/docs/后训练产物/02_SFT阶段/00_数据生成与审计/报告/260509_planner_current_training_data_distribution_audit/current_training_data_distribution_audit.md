# 当前训练数据分布审计 2026-05-09

## 口径

- 当前训练数据按 README 的 realbudget-only 重建口径统计：`training/data/v3/sft_realbudget_runs/260508_main1000_w20_gate1_thinking_off`。
- `training/data/llamafactory/dataset_info.json` 当前为 `{}`，旧 V3 全局入口已归档；本报告统计 run-local `llamafactory_train.json` / `llamafactory_val.json`。
- 预算贴合/可用性来自同目录下重新跑出的本地审计，不调用外部模型，不修改原始 records。

## 一眼看

| 指标 | 数值 | 备注 |
|---|---|---|
| records 成功样本 | 1013 | raw records.jsonl |
| LLaMAFactory train / val | 912 / 101 | 固定 seed=20260427，val_ratio≈0.1 |
| requests / errors | 1013 / 223 | 错误率按 records+errors 估算 18.0% |
| 预算主集可用 | 86.7% (878) | teacher 预算贴合且候选预算可达 |
| 非预算 only | 12.2% (124) | strictness=none |
| 需重生成 teacher | 1.1% (11) | 请求预算 OK，但 teacher 低于目标 |
| 城市覆盖 | 35 | 城市分布见 CSV/下表 |
| 重复 record_id 组 | 0 | 应为 0 |

## 文件规模

| 文件 | 记录数 | 大小 |
|---|---|---|
| requests.jsonl | 1013 | 1.1 MB |
| records.jsonl | 1013 | 183.5 MB |
| errors.jsonl | 223 | 0.1 MB |
| llamafactory_train.json | 912 | 62.7 MB |
| llamafactory_val.json | 101 | 7.0 MB |
| llm_usage.jsonl | 1756 | 1.3 MB |

## Split 分布

| split | n | 占比 | 城市数 | 预算中位数 | 预算档 | strictness | 天数 |
|---|---|---|---|---|---|---|---|
| train | 912 | 90.0% | 35 | 5500 | limited:333, standard:267, comfortable:252, premium:44, luxury:16 | soft:689, none:115, hard:108 | 2:221, 3:373, 4:232, 5:86 |
| val | 101 | 10.0% | 30 | 5500 | comfortable:38, standard:31, limited:31, premium:1 | soft:82, hard:10, none:9 | 2:27, 3:36, 4:31, 5:7 |

## 预算可用性

| 类别 | 含义 | 数量 | 建议 |
|---|---|---|---|
| usable_budget_clean | 预算主集可用 | 86.7% (878) | 直接进预算主训练池 |
| usable_budget_candidate_tight | 预算可用但候选偏紧 | 0.0% (0) | 候选偏紧，慎用于用足预算 |
| repair_request_rebudget | 需重标请求预算 | 0.0% (0) | 需重标请求预算 |
| repair_teacher_regen | 需重生成 teacher | 1.1% (11) | 需重生成 teacher |
| nonbudget_only | 仅适合非预算 SFT | 12.2% (124) | 只进非预算/grounding 池 |
| drop_or_full_regen | 预算训练淘汰或整条重做 | 0.0% (0) | 淘汰或整条重做 |

## 预算贴合

| 指标 | 数量 |
|---|---|
| 请求预算在推荐区间 | 100.0% (1013) |
| teacher 预算在目标区间 | 86.7% (878) |
| teacher 预算低于目标 | 1.1% (11) |
| 无预算策略 | 12.2% (124) |
| 候选池高配预算可达 | 95.5% (967) |
| 请求金额分布 | min=900, p50=5500, p90=13000, max=32200 |
| teacher 总预算分布 | min=601, p50=4371, p90=10694, max=31500 |
| teacher/request 比例 | p25=0.722, p50=0.802, p75=0.949, p90=0.996 |

## 按预算档

| budget_level | n | 占比 | amount p50 | teacher p50 | clean | nonbudget | repair_teacher |
|---|---|---|---|---|---|---|---|
| limited | 364 | 35.9% | 3750 | 3022 | 92.0% (335) | 7.7% (28) | 0.3% (1) |
| standard | 298 | 29.4% | 5400 | 4170 | 80.5% (240) | 18.5% (55) | 1.0% (3) |
| comfortable | 290 | 28.6% | 7650 | 6131 | 87.9% (255) | 10.0% (29) | 2.1% (6) |
| premium | 45 | 4.4% | 12100 | 8170 | 71.1% (32) | 26.7% (12) | 2.2% (1) |
| luxury | 16 | 1.6% | 13400 | 12432 | 100.0% (16) | 0.0% (0) | 0.0% (0) |

## 预算档 x Strictness

| level/strictness | n | 占比 |
|---|---|---|
| comfortable/hard | 12 | 1.2% |
| comfortable/none | 29 | 2.9% |
| comfortable/soft | 249 | 24.6% |
| limited/hard | 88 | 8.7% |
| limited/none | 28 | 2.8% |
| limited/soft | 248 | 24.5% |
| luxury/hard | 1 | 0.1% |
| luxury/soft | 15 | 1.5% |
| premium/hard | 3 | 0.3% |
| premium/none | 12 | 1.2% |
| premium/soft | 30 | 3.0% |
| standard/hard | 14 | 1.4% |
| standard/none | 55 | 5.4% |
| standard/soft | 229 | 22.6% |

## 金额与行程

| 分布 | 明细 |
|---|---|
| budget amount bucket | 2001-4000:269, 4001-6000:229, 6001-8000:156, 8001-12000:163, <=2000:67, >12000:129 |
| travel_days | 2:248, 3:409, 4:263, 5:93 |
| party_total | 1:175, 2:311, 3:296, 4:176, 5:42, 6:13 |
| companion_type | friends:220, family_with_children:184, couple:181, solo:145, family_with_elders:117, family_mixed:77, business:45, other:44 |
| accommodation | 舒适型酒店:390, 经济型酒店:331, 民宿:148, 高端酒店:75, 亲子酒店:69 |
| transportation | 地铁+步行:368, 打车:314, 公共交通:216, 自驾:115 |
| season | spring:473, summer:341, autumn:124, winter:75 |
| month | 01:39, 02:36, 03:24, 04:58, 05:391, 06:148, 07:83, 08:110, 09:94, 11:30 |

## 城市分布

| 城市 | n | 占比 |
|---|---|---|
| 北京 | 94 | 9.3% |
| 上海 | 57 | 5.6% |
| 成都 | 57 | 5.6% |
| 苏州 | 46 | 4.5% |
| 广州 | 46 | 4.5% |
| 深圳 | 46 | 4.5% |
| 长沙 | 42 | 4.1% |
| 南京 | 41 | 4.0% |
| 西安 | 41 | 4.0% |
| 青岛 | 38 | 3.8% |
| 三亚 | 38 | 3.8% |
| 杭州 | 38 | 3.8% |
| 厦门 | 35 | 3.5% |
| 武汉 | 30 | 3.0% |
| 宁波 | 27 | 2.7% |
| 昆明 | 26 | 2.6% |
| 桂林 | 25 | 2.5% |
| 哈尔滨 | 25 | 2.5% |
| 沈阳 | 24 | 2.4% |
| 天津 | 23 | 2.3% |
| 丽江 | 23 | 2.3% |
| 福州 | 21 | 2.1% |
| 珠海 | 18 | 1.8% |
| 大连 | 17 | 1.7% |
| 郑州 | 17 | 1.7% |
| 济南 | 15 | 1.5% |
| 重庆 | 15 | 1.5% |
| 扬州 | 14 | 1.4% |
| 大理 | 12 | 1.2% |
| 洛阳 | 12 | 1.2% |
| 泉州 | 11 | 1.1% |
| 贵阳 | 11 | 1.1% |
| 张家界 | 10 | 1.0% |
| 呼和浩特 | 10 | 1.0% |
| 黄山 | 8 | 0.8% |

## 城市层级

| city_tier | n | 占比 |
|---|---|---|
| major | 394 | 38.9% |
| popular | 381 | 37.6% |
| long_tail | 238 | 23.5% |

## 偏好 Top 20

| preference | n | 占比(按标签出现次数) |
|---|---|---|
| 美食 | 360 | 10.8% |
| 休闲慢游 | 298 | 8.9% |
| 历史文化 | 276 | 8.3% |
| 亲子 | 261 | 7.8% |
| 自然风光 | 247 | 7.4% |
| 城市地标 | 218 | 6.5% |
| 老人友好 | 194 | 5.8% |
| 博物馆 | 182 | 5.5% |
| 城市漫步 | 162 | 4.9% |
| 第一次来 | 158 | 4.7% |
| 摄影 | 157 | 4.7% |
| 城市公园 | 146 | 4.4% |
| 购物商圈 | 111 | 3.3% |
| 主题乐园 | 108 | 3.2% |
| 户外轻徒步 | 102 | 3.1% |
| 夜市夜景 | 84 | 2.5% |
| 艺术 | 81 | 2.4% |
| 小众展览 | 75 | 2.2% |
| 海滨度假 | 66 | 2.0% |
| 素食 | 26 | 0.8% |

## 正向/负向约束 Top 20

| positive_preference | n | 占比 |
|---|---|---|
| 美食 | 360 | 10.8% |
| 休闲慢游 | 298 | 8.9% |
| 历史文化 | 276 | 8.3% |
| 亲子 | 261 | 7.8% |
| 自然风光 | 247 | 7.4% |
| 城市地标 | 218 | 6.5% |
| 老人友好 | 194 | 5.8% |
| 博物馆 | 182 | 5.5% |
| 城市漫步 | 162 | 4.9% |
| 第一次来 | 158 | 4.7% |
| 摄影 | 157 | 4.7% |
| 城市公园 | 146 | 4.4% |
| 购物商圈 | 111 | 3.3% |
| 主题乐园 | 108 | 3.2% |
| 户外轻徒步 | 102 | 3.1% |
| 夜市夜景 | 84 | 2.5% |
| 艺术 | 81 | 2.4% |
| 小众展览 | 75 | 2.2% |
| 海滨度假 | 66 | 2.0% |
| 素食 | 26 | 0.8% |

| negative_constraint | n | 占比 |
|---|---|---|
| 太偏远的景点 | 223 | 14.4% |
| 购物团 | 217 | 14.1% |
| 过度商业化景点 | 211 | 13.7% |
| 人挤人的网红店 | 203 | 13.1% |
| 高价餐厅 | 195 | 12.6% |
| 太累的路线 | 193 | 12.5% |
| 重辣 | 95 | 6.2% |
| 重口味 | 81 | 5.2% |
| 海鲜 | 50 | 3.2% |
| 荤菜 | 26 | 1.7% |
| 猪肉 | 25 | 1.6% |
| 酒 | 25 | 1.6% |

## 结构质量检查

| 检查项 | 数量 | 备注 |
|---|---|---|
| 重复 record_id 组 | 0 | 应为 0 |
| 缺 request.budget_constraint | 0 | 应为 0 |
| 缺 request.party | 0 | 应为 0 |
| 缺 planner_context | 0 | 应为 0 |
| 缺 compact_planner_context | 0 | 可为 0 更好 |
| 缺 trip_plan.budget | 0 | 应为 0 |
| 缺 trip_plan.days | 0 | 应为 0 |
| travel_days 与 days 数不一致 | 0 | 应为 0 |
| 空 attractions 的日程 | 0 | 按 day 计数 |
| 空 meals 的日程 | 0 | 按 day 计数 |
| hotel=null 的日程 | 999 | schema 可选，按 day 计数 |
| budget 分项求和不等于 total | 0 | 容差 5 元 |
| output 非合法 JSON | 0 | 应为 0 |

## 失败样本

| 维度 | 明细 |
|---|---|
| error_type | RuntimeError:223 |
| error_kind | other_runtime:174, context_budget_unreachable:49 |
| 预算不可达 ratio | min=0.498, p50=0.846, p90=0.973, max=0.992 |
| 失败请求 amount | min=1500, p50=6850, p90=18350, max=26800 |

## LLM Usage

| 指标 | 数值 |
|---|---|
| usage rows | 1756 |
| model | deepseek-v4-pro:1756 |
| call_type | planner:1756 |
| prompt_tokens | 27652261 |
| completion_tokens | 18448575 |
| reasoning_tokens | 14144734 |
| total_tokens | 46100836 |
| prompt_cache_hit/miss | 11422720 / 16229541 |
| tokens_per_record | 45509.2 |

## 输出文件

- summary: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/summary.json`
- city_distribution: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/city_distribution.csv`
- preference_distribution: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/preference_distribution.csv`
- split_record_ids: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/split_record_ids.csv`
- budget_fit: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/budget_fit/sft_budget_fit_audit.md`
- usability: `training/outputs/eval/audits/260509_v3_current_training_data_distribution_audit/usability/sft_budget_usability_audit.md`
