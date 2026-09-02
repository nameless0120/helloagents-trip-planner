# V3 SFT cp2 v2a/v2b 对比

- 评测集：`training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C_budget110/records.jsonl`
- 样本数：300
- 推理设置：vLLM，单卡单进程，`workers=10`
- 说明：本报告复用原 `A_C` generations，只刷新评测侧 `budget_fit_policy`；`standard` 和 `comfortable` 的 soft 上限为 110%，hard 预算仍 cap 到 100%。
- v2a：LoRA r16，global batch 32，lr 8e-5，ctx 24576
- v2b：LoRA r32/alpha64，global batch 32，lr 8e-5，ctx 24576

## 结论

v2b 是这轮更好的候选。新口径下餐饮 grounding 已进入 `SFT hard`，v2b 的 `SFT hard` 仍最高，`DPO soft` 也最高，餐饮多样性和预算选择贴合也略好。v2a 的 JSON/schema 稳定性稍好一点，但整体不如 v2b。

预算乘法/口径相关指标仍然不能当作 SFT 主要目标。模型可以学“选什么酒店、景点、餐厅、单价大概在哪个档位”，但最终总预算、住宿总价、餐饮总价这类确定性乘法，后续应由工程重算。

## 数据诊断

当前问题更像“数据分布和候选供给问题”，不是 teacher 样本整体脏。

- 用同一套规则评估 1000 条 SFT teacher reference，`SFT hard` 为 99.70%，`budget_selection_ok` 为 94.70%，说明进入训练集的 teacher 输出本身大体是干净的。
- 但训练集 budget strictness 明显偏软：`soft=838`、`hard=74`、`none=88`；当前 A_C eval 是 `hard=210`、`soft=90`。尤其训练集中 `comfortable+hard` 只有 7 条、`standard+hard` 只有 20 条，而 eval 分别是 90 条和 90 条。
- 训练集更偏 2-3 天：2 天 193、3 天 422、4 天 285、5 天 100；eval 是 3 天 60、4 天 120、5 天 120。模型在长行程 hard budget 上训练不足。
- 训练集 comfortable/premium teacher 虽然通过预算区间，但更贴近区间下沿：comfortable 平均只在目标区间内约 17% 位置，premium 约 18% 位置。模型容易学成“刚过 target_min 就行”，不是“宽预算主动升级酒店/餐饮/体验”。
- v2b 的 127 条预算选择失败中，88 条是低于 `target_min_total`，39 条是高于 `target_max_total`。低于目标主要集中在 comfortable/premium，超预算几乎都集中在 hard budget。
- 低于预算的 88 条里，按当前候选价格粗算有 31 条即使选择最高价酒店、景点、餐饮并沿用当前交通预算，也达不到 `target_min_total`。这说明一部分失败不是模型选择问题，而是候选 POI 价格带不够或预算目标偏高。

## 下一步调法

下一轮不建议继续只调 LoRA rank/lr。v2b 已经证明参数收益有限，应该先补数据和候选策略：

- 补一批 targeted SFT 数据，不必重做全部 1000 条。重点覆盖 `standard/comfortable hard`、`comfortable/premium soft`、4-5 天、朋友/家庭/三代、亲子酒店/高端酒店/民宿。
- 调高 hard budget 在 SFT 请求里的占比。当前非 limited 档 hard 只有 4%，建议至少提到 20%-30%；limited hard 可以提到 30%-40%。
- 对 comfortable/premium 增加“预算利用型 teacher”样本：不要只要求落入 `[target_min, target_max]`，而是优先落到区间中段，例如 80%-95% 用户预算；如果候选价格达不到，则标记为候选供给不足，不拿这类样本硬训预算贴合。
- 检索侧已增加轻量 `budget_upgrade` 候选层：预算较宽时补高端酒店/精品民宿、premium 餐厅和付费体验/演出/温泉/游船等候选；后续需要用新上下文重建 eval/SFT 数据验证覆盖率。否则 budget target 再合理，模型也没有可选项花出去。
- 评测侧把 `budget_selection_ok` 拆成三项看：hard 不超预算、soft 不明显低用、候选价格可达性。候选不可达时不应该把责任全算到模型。

v2c 补数计划当前通过 `training/scripts/run_pipeline.py --stage sft-data --request-source budget_supplement` 执行：

- 规模建议 500 条，hard 310、soft 190。
- 预算组合：`comfortable+hard=120`、`standard+hard=100`、`limited+hard=60`、`comfortable+soft=80`、`premium+soft=80`、`premium+hard=30`、`standard+soft=20`、`luxury+soft=10`。
- 天数：3 天 100、4 天 200、5 天 200。
- 同行：couple/friends/family_mixed 各 90，family_with_elders/family_with_children 各 75，business 40，solo 25，other 15。
- soft 样本统一使用预算利用目标 `target_min_ratio=0.95`、`target_max_ratio=1.05`，并在 free text 中明确“尽量用足预算，不要低配省钱”。
- 这批预算金额会比原始 1000 条更高，用于配合新 `budget_upgrade` 候选层训练模型选择更高价位酒店、餐饮和体验。

v2c smoke50 结果：

- 当前复现命令：`DATA_GEN_THINKING=false ... training/scripts/run_pipeline.py --stage sft-data --count 50 --start-index 2000 --request-source budget_supplement --workers 20 --sample-retries 1 --sft-dir training/data/planner/sft_runs/v2c_smoke50 --resume`
- 成功 22，失败 28；失败率偏高，不建议直接跑满 500。
- 失败类型：餐饮复用 10、JSON 解析 8、预算明显低于 95% soft 目标 4、价格 hint 复制错误 2、景点数量/景点 grounding/餐饮占位/餐饮 grounding 各 1。
- 成功样本 teacher 质量：`SFT hard=100%`，`budget_selection_ok=95.45%`，`DPO soft=90.91%`。
- soft 成功样本 7 条，预算使用率大多在 95%-100% 附近，说明“能成功的样本”确实学到了 95%-105% 目标；但 premium soft 高预算样本有明显生成难度。
- 成功/失败切片文件：`training/data/v3/sft/smoke50_v2c_budget_supplement_records.jsonl`、`training/data/v3/sft/smoke50_v2c_budget_supplement_errors.jsonl`、`training/data/v3/sft/smoke50_v2c_budget_supplement_中文预览.md`。
- 结论：这批方向有效，但完整 500 条建议用 `sample_retries=3`，并考虑把 premium/luxury 预算金额略降或先做候选可达性检查，避免大量 premium soft 样本天然花不到 95%。

## 核心指标

这一组只看“这个模型版本整体值不值得继续”的指标。

| 字段 | 含义 | base | cp2_v1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| JSON 可解析率 | 输出里能抽取出合法 JSON 的比例。 | 100.00% | 100.00% | 100.00% | 99.67% |
| Schema 通过率 | JSON 能通过 `TripPlan` schema 校验的比例。 | 99.67% | 99.33% | 99.33% | 99.00% |
| SFT hard | SFT 阶段最核心硬约束通过率，包含餐饮 grounding，不含预算精确加总。 | 78.26% | 83.89% | 92.95% | 93.94% |
| DPO soft | 在 SFT hard 基础上，再看景点/餐饮多样性、预算偏好等软质量。 | 8.70% | 29.19% | 43.62% | 50.17% |
| 预算选择贴合 | 按模型选中的 POI 单价工程重算后，是否贴合预算档位。 | 50.84% | 50.67% | 55.70% | 57.24% |
| 餐饮多样性 | 同一天午晚餐不重复，整段行程餐厅不过度复用。 | 36.45% | 60.07% | 82.55% | 86.53% |

## SFT Hard

`SFT hard` 衡量模型是否学会“可交付的结构化行程骨架”。它不追求审美最优，也不要求预算乘法精确。

| 字段 | 含义 | v2a | v2b |
| --- | --- | ---: | ---: |
| SFT hard 总通过率 | 下面这些硬约束同时通过的比例。 | 92.95% | 93.94% |
| 城市/日期/天数正确 | 城市、起止日期、每日日期、天数都和用户请求一致。 | 100.00% | 100.00% |
| 住宿类型正确 | `day.accommodation` 固定等于用户要求的住宿类型。 | 100.00% | 100.00% |
| 中间日酒店不为空 | 非最后一天必须有酒店，最后一天可为空。 | 100.00% | 100.00% |
| 酒店 grounding | 输出酒店必须来自工具候选。 | 100.00% | 100.00% |
| 酒店距离不编造 | `hotel.distance` 不输出“距市中心xx公里”这类编造距离。 | 100.00% | 100.00% |
| 餐饮三餐完整 | 每天 breakfast/lunch/dinner 都存在，包括返程日 dinner。 | 100.00% | 100.00% |
| 餐饮具体性 | 不输出“早餐推荐/午餐推荐/当地美食/无”等占位名。 | 99.33% | 98.99% |
| 餐饮语义有效 | 餐厅名语义上像真实餐饮地点，不是酒店、景点或无效文本。 | 94.97% | 95.29% |
| 餐饮 grounding | 餐饮来自 `food_pois`；住宿早餐等明确合法 fallback 可接受。 | 94.97% | 94.95% |
| 景点数量正确 | 每天 1-3 个景点。 | 99.66% | 99.66% |
| 景点 grounding | 景点来自 classic/preference/scenic/experience 候选。 | 98.32% | 98.32% |
| 天气一致 | `weather_info` 日期和值和工具上下文一致。 | 100.00% | 100.00% |

## 预算相关

预算分两类看：一类是“模型报出来的预算 ledger 是否自洽”，另一类是“按模型选项工程重算后是否贴合预算”。后者更接近线上可用口径。

| 字段 | 含义 | base | cp2_v1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| 预算选择贴合 | 用模型选中的酒店/景点/餐厅单价工程重算后，是否贴合预算档位。 | 50.84% | 50.67% | 55.70% | 57.24% |
| 重算后硬预算不超 | 工程重算后的总价是否满足 hard budget。 | 87.29% | 88.26% | 88.26% | 87.21% |
| 模型上报预算加总正确 | 模型输出的四项预算和 `budget.total` 是否能加平。 | 56.19% | 73.15% | 79.19% | 72.05% |
| 模型上报预算不超 | 只看模型自己报的 `budget.total` 是否满足 hard budget。 | 96.66% | 94.97% | 94.97% | 90.57% |
| 模型上报预算偏好贴合 | 只看模型自己报的预算是否贴合预算档位。 | 23.75% | 69.13% | 66.11% | 70.71% |
| 酒店预算覆盖住宿晚数 | 模型报的酒店预算是否大致覆盖“房价 * 晚数 * 房间数”。 | 29.10% | 64.77% | 65.77% | 68.01% |
| 餐饮人均价格尺度 | 每顿餐饮 `estimated_cost` 是否像人均单餐价，而不是明显过低。 | 17.73% | 32.55% | 30.87% | 32.66% |

预算结论：110% 上限放宽后，v2b 的“预算选择贴合”提升到 57.24%，仍是最高；但模型报账本仍不可靠。预算最终口径应以工程重算为准。

`预算选择贴合` 不是只看有没有超过 hard budget，也会检查是否明显低于预算档位下限。以 v2b 为例，297 条可评估样本中 170 条通过、127 条失败；失败里 88 条是重算总价低于 `target_min_total`，39 条是高于 `target_max_total`，其中 38 条同时属于 hard budget 超支。也就是说，当前主要问题不是“都超预算”，而是 comfortable/premium 等预算较宽的请求经常被模型规划成偏省钱方案。

## DPO Soft

`DPO soft` 衡量的是行程质量倾向，不是 SFT 阶段必须完全压住的硬格式。当前它仍然依赖 `SFT hard` 先通过；餐饮 grounding 已在 hard pass 中约束，这里不再作为 DPO 增量项。

| 字段 | 含义 | base | cp2_v1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| DPO soft 总通过率 | `SFT hard` 通过后，再同时满足景点多样性、餐饮多样性、预算偏好。 | 8.70% | 29.19% | 43.62% | 50.17% |
| 重算预算版 DPO soft | 把预算偏好从“模型上报预算”换成“工程重算预算”的 DPO soft。 | 12.71% | 21.81% | 37.92% | 37.71% |
| 景点多样性 | 同一行程内同名景点不重复；计算时会忽略括号里的分店/补充信息。 | 88.63% | 69.46% | 83.89% | 81.48% |
| 餐饮多样性 | 同一天午晚餐不重复，整段行程餐厅不过度复用。 | 36.45% | 60.07% | 82.55% | 86.53% |
| 预算偏好贴合 | 模型上报预算是否贴合用户预算档位。 | 23.75% | 69.13% | 66.11% | 70.71% |

DPO 结论：v2b 的软质量收益最明显，主要来自餐饮多样性和预算偏好；景点多样性略低于 v2a，但差距不大。

## 速度

速度指标用于判断同样 `workers=10`、同样 300 条评测下，不同模型版本的推理代价。这里的延迟是单条请求从发起到返回的耗时，不是整批 wall time。

| 字段 | 含义 | base | cp2_v1 | v2a | v2b |
| --- | --- | ---: | ---: | ---: | ---: |
| 平均延迟 | 单条请求平均返回时间，越低越快。 | 69.15s | 89.87s | 90.75s | 91.05s |
| P90 延迟 | 90% 请求能在这个时间内返回，用来看尾部慢样本。 | 85.12s | 110.15s | 110.71s | 110.12s |
| 平均输出长度 | 单条输出平均字符数，间接反映回答详细程度和解码成本。 | 6831 | 6983 | 6974 | 7018 |
| P90 输出长度 | 90% 输出不超过这个字符数，用来看长输出尾部。 | 8367 | 8526 | 8451 | 8464 |

速度结论：v2a/v2b 和 cp2_v1 基本同一档，v2b 没有明显额外推理成本；base 更快主要是输出和模型行为更简单，但质量明显差。

## 输出文件

- budget110 records: `training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C_budget110/records.jsonl`
- v2a generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_A_C_w10/generations.jsonl`
- v2a budget110 report: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_A_C_w10_budget110/rule_eval_report.md`
- v2b generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2b_A_C_w10/generations.jsonl`
- v2b budget110 report: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2b_A_C_w10_budget110/rule_eval_report.md`
