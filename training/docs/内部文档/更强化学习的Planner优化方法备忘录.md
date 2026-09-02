# 更强化学习的 Planner 优化方法备忘录

## 当前决策

短期先继续推进 DPO。

原因是当前 `planner_soft_pass` 已经被证明可以通过 DPO 学到，且本轮 direct402 checkpoint sweep 里 `ckpt-25` 已经把 combined planner soft 从 SFT final 的 35.2% 拉到 44.7%。下一步最稳的是围绕 planner soft 继续补高质量 pair，而不是马上切到更复杂的在线强化学习训练。

后续如果要尝试更接近严格强化学习的方法，可以把下面几种方案作为备选。

## 当前任务为什么适合做 RL-style 实验

Planner 任务本质上不是单纯语言风格对齐，而是一个带约束的组合决策问题：

- 输入是一个固定的 `PlannerContext` / 用户请求。
- 输出是一整份 `TripPlan` JSON。
- 模型需要在候选酒店、餐饮、景点、天气、预算策略之间做选择。
- 结果可以被规则 evaluator 自动打分。

这很接近 contextual bandit：

```text
state   = PlannerContext / prompt
action  = generated TripPlan
reward  = rule evaluator score
policy  = planner model
```

目前的主目标是：

```text
planner_soft_pass =
  sft_hard_pass
  && attraction_diversity_ok
  && meal_diversity_ok
  && meal_cost_scale_ok
  && recomputed_budget_user_constraint_ok
  && recomputed_budget_fit_ok
```

其中 `hard_pass` 已经接近高位，后续主要难点是：在合法 TripPlan 里选择更符合预算、体验更丰富的组合。

## 推荐的后续顺序

### 1. 继续 DPO

这是当前阶段的主线。

建议继续沿用现有原则：

- chosen 必须 hard pass，尽量 planner soft pass。
- rejected 最好也 hard pass，但在一个明确 planner soft 维度失败。
- pair 差异尽量单一，避免一个 pair 同时差预算、餐饮、景点、格式。
- 不直接使用 eval / eval_hard 失败样本训练，只从 train-only contexts 构造同类压力样本。
- 从 `ckpt-25` adapter 初始化阶段二训练，低 LR、短 epoch、中间 checkpoint sweep。

### 2. Best-of-N + 规则奖励

这是 DPO 和 RL 之间最自然的一步。

流程：

```text
同一个 prompt 采样 N 个候选
-> 用 eval_rule_metrics.py 计算规则指标
-> 选最高分作为 chosen
-> 选低分但结构可用的候选作为 rejected
-> 构造 DPO / SimPO / SFT replay 数据
```

优点：

- 复用现有 evaluator，工程成本低。
- 比人工写 pair 更容易放大数据量。
- 可以直接围绕 planner soft 的失败类型采样。

风险：

- reward 权重如果写偏，模型会学习规则捷径。
- 采样温度太高会产生大量 schema/JSON 垃圾样本。
- winner 和 loser 如果差异太多，DPO 信号仍然会混。

### 3. GRPO / RLOO + 规则 reward

这是最推荐的“更强化学习一点”的实验方向。

形式：

```text
每个 prompt 在线采样 K 个 TripPlan
-> 对每个 completion 跑规则 evaluator
-> 用 reward 计算组内相对 advantage
-> 带 KL 约束更新当前策略
```

它比 DPO 更像 RL，因为候选来自当前策略的 rollout，而不是固定离线 pair。相比 PPO，它又少了 value model / critic，工程上更轻。

第一版可以用 shaped reward，不建议只用 `planner_soft_pass` 这个 0/1 值，因为太稀疏。

示例 reward：

```text
json/schema 失败：-5
finish_reason=length：-4

hard 失败：
  -2 - 0.3 * hard_failure_count

hard pass 后：
  +1.0  sft_hard_pass
  +1.2  planner_soft_pass
  +0.8  recomputed_budget_fit_ok
  +0.8  recomputed_budget_user_constraint_ok
  +0.4  attraction_diversity_ok
  +0.4  meal_diversity_ok
  +0.2  meal_cost_scale_ok
```

更好的版本应该把预算贴合做成连续分数：落在 `target_min_total ~ target_max_total` 内给满分，低于或高于范围按距离扣分。`meal_cost_scale_ok` 当前已经接近饱和，不应该继续重压，适合作为 guardrail。

建议 smoke 配置：

```text
init adapter: ckpt-25
prompts: train-only contexts
K: 4 或 8
temperature: 0.7 ~ 0.9
learning_rate: 3e-7 ~ 1e-6
max_tokens: 按 travel_days 给足
checkpoint: 每 0.25 / 0.5 epoch 保存
stop rule: hard pass 掉超过 1pp 立即停
```

### 4. PPO

PPO 最符合传统 RLHF 直觉，但不建议作为第一个实验。

原因：

- TripPlan 输出很长，token-level credit assignment 会很难。
- JSON/schema 失败会让 reward 非常稀疏。
- 需要更复杂的 value / critic 或 reward model 设计。
- 训练稳定性和工程成本都高于 GRPO / RLOO。

如果后面要做 PPO，最好先有一个稳定的 reward model 或非常可靠的规则 reward，并且先用小规模 smoke 验证不会破坏 hard pass。

## 更激进的方向：结构化动作空间

如果以后要把问题做得更像真正的规划 RL，可以考虑改输出方式：

```text
模型不直接生成完整 JSON
而是逐步选择：
  hotel_id
  meal_poi_id
  attraction_poi_id
  day assignment
  budget allocation
最后由 deterministic renderer 拼 TripPlan JSON
```

这样 action space 会更清楚，reward credit assignment 也更直接。

代价是产品和训练链路改造较大，不适合当前阶段插队做。

## 当前最务实结论

现在先继续 DPO 是合理的。

下一轮 DPO 应继续围绕 `planner_soft_pass` 做高质量、单失败维度 pair。等 DPO 的收益开始变小，最值得尝试的 RL-style 方案是：

```text
GRPO / RLOO + eval_rule_metrics.py shaped reward
```

不要一上来做 PPO。先把规则 reward 包成可在线采样、可复现实验、可 checkpoint sweep 的小闭环，再考虑更重的 RLHF 训练。
