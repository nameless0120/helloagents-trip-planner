# V2 PlannerContext 数据协议

更新时间：2026-04-30

这份文档定义当前线上后端和 v2 后训练数据共同使用的 Planner 输入协议。当前版本以线上已跑通代码为准，不保留历史草案。

```text
协议服从当前线上实现。
离线 SFT/DPO 数据必须和线上真实 Planner 输入同构。
```

## 当前实现位置

```text
backend/app/agents/planner_context.py
backend/app/agents/trip_planner_agent.py
backend/app/agents/planner_output.py
```

## 1. 当前线上流程

```text
TripRequest
  -> PlannerContextBuilder.collect()
      -> 并行查询 attractions / weather / hotels
      -> 生成 raw PlannerContext
  -> PlannerContextBuilder.compact_for_planner()
      -> 生成 compact PlannerContext
  -> _build_planner_query()
      -> 把 compact PlannerContext 放入 Planner prompt
  -> Planner LLM
  -> extract_json_object()
  -> TripPlan schema
  -> validate_trip_plan_shape()
```

当前存在两层上下文：

- `raw PlannerContext`：完整工具快照，用于命令行审查、日志和后置校验。
- `compact PlannerContext`：裁剪后的模型输入，用于线上 Planner 和后续 v2 训练数据。

离线训练数据应优先使用线上真实 `planner_query` 作为模型输入；`planner_query` 内部包含 `compact PlannerContext` 和 Planner 规则。同时把 `compact PlannerContext`、`raw PlannerContext` 放到 metadata 中，便于审计。

## 2. Raw PlannerContext

`raw PlannerContext` 是 `PlannerContextBuilder.collect()` 返回的结构。

```json
{
  "version": "planner_context_v2",
  "generated_at": "2026-04-29T00:00:00+00:00",
  "request": {
    "city": "北京",
    "start_date": "2026-04-29",
    "end_date": "2026-05-02",
    "travel_days": 4,
    "transportation": "公共交通",
    "accommodation": "经济型酒店",
    "preferences": ["自然风光", "艺术"],
    "free_text_input": "对海鲜过敏"
  },
  "user_profile": {
    "budget_level": "经济",
    "daily_budget": null,
    "pace": "未指定",
    "diet": "无",
    "interests": ["自然风光", "艺术"],
    "avoid": ["海鲜"],
    "free_text_input": "对海鲜过敏"
  },
  "tool_snapshot": {
    "classic_pois": [],
    "preference_pois": [],
    "scenic_pois": [],
    "experience_pois": [],
    "hotel_pois": [],
    "food_pois": [],
    "available_weather": [],
    "trip_weather": [],
    "tool_status": {}
  },
  "planner_constraints": {
    "days_count": 4,
    "expected_dates": ["2026-04-29", "2026-04-30", "2026-05-01", "2026-05-02"],
    "attractions_per_day": "2-3",
    "meals_per_day": ["breakfast", "lunch", "dinner"],
    "weather_policy": "只能使用trip_weather。天气不可用的日期必须写远期天气暂无准确预报，温度写未知，不要把短期天气平移到未来日期。",
    "grounding_policy": "景点、体验、酒店、餐饮优先来自tool_snapshot候选。确需补充常识时，要保持城市匹配并避免精确坐标编造。"
  }
}
```

当前字段说明补充：

- `user_profile.diet` 表示正向饮食偏好。
- `user_profile.avoid` 表示忌口和避雷项。
- `user_profile.companion` 当前线上暂不解析。
- `daily_budget` 当前线上不解析，固定为 `null`。
- `pace` 当前线上不解析，固定为 `未指定`。
- 天气拆为 `available_weather` 和 `trip_weather`。
- `planner_constraints` 当前是自然语言策略字段，不是布尔 flag 集合。
- 景点召回拆为 `classic_pois` 和 `preference_pois`，`scenic_pois` 是两者合并后的兼容字段。
- `classic_pois` 是城市级经典候选，默认本地缓存 60 小时。

## 3. User Profile

当前线上没有长期用户画像，因此 `user_profile` 主要从本次请求派生。

```json
{
  "budget_level": "经济",
  "daily_budget": null,
  "pace": "未指定",
  "diet": "无",
  "interests": ["自然风光", "艺术"],
  "avoid": ["海鲜"],
  "free_text_input": "对海鲜过敏"
}
```

饮食解析规则：

```text
想吃海鲜      -> diet="海鲜", avoid=[]
对海鲜过敏    -> diet="无", avoid=["海鲜"]
不吃辣        -> diet="无", avoid=["辣"]
少辣          -> diet="少辣", avoid=[]
```

`diet` 代表正向饮食偏好，`avoid` 代表忌口或避雷项。餐饮搜索关键词只使用正向 `diet`，不使用 `avoid`。

## 4. Raw POI 字段

raw POI 保留较多字段，主要用于审查和后置校验：

```json
{
  "id": "B000A81FY5",
  "name": "798艺术区",
  "type": "风景名胜;风景名胜;风景名胜",
  "typecode": "110200",
  "address": "酒仙桥路4号",
  "location": {"longitude": 116.494784, "latitude": 39.985063},
  "cityname": "北京市",
  "adname": "朝阳区",
  "rating": "4.8",
  "cost": "",
  "photo_count": 3,
  "source_keyword": "艺术",
  "source_role": "scenic",
  "source_bucket": "preference"
}
```

当前 POI 分层：

- `classic_pois`：城市经典候选，使用固定关键词召回，和用户偏好无关。
- `preference_pois`：用户偏好召回的传统景点、博物馆、公园、广场、纪念馆等。
- `scenic_pois`：兼容字段，是 `classic_pois + preference_pois` 合并去重后的结果。
- `experience_pois`：体验活动、展览、剧场、休闲娱乐等。
- `hotel_pois`：住宿候选。
- `food_pois`：餐饮候选。

### 酒店价格字段

高德酒店 POI 的 `cost` 经常为空，不能稳定作为预算依据。当前 v2.1 之前先采用规则估价：

- `cost`：高德返回的原始价格字段，有值则保留。
- `estimated_cost_hint`：系统根据住宿类型、城市层级、酒店 POI 类型生成的单晚估价。
- `cost_source`：价格来源。当前可取：
  - `amap_cost`：高德原始 `cost` 可用。
  - `rule_estimated`：高德缺少价格时的规则估价。
  - `ota_live_rate`：后续接入 OTA/酒店 Shopping API 后的实时房价，当前暂不作为主线。

Planner 输出时，`hotel.estimated_cost` 表示“元/晚”，应该优先复制对应候选的 `estimated_cost_hint`，不要自行改价。N 天行程默认住宿 N-1 晚，`budget.total_hotels` 必须覆盖所有住宿晚数。

经典景点召回关键词：

```text
必游景点
著名景点
热门景点
博物馆
历史文化
公园
```

当前召回控制：

- 每个关键词最多保留 `PLANNER_CONTEXT_PER_KEYWORD_LIMIT` 条，默认 `5`。
- `classic_pois` 总量默认 `PLANNER_CONTEXT_CLASSIC_LIMIT=12`。
- `preference_pois` 总量默认 `PLANNER_CONTEXT_PREFERENCE_LIMIT=16`。
- `scenic_pois` 合并后总量默认 `PLANNER_CONTEXT_POI_LIMIT=20`。
- `classic_pois` 缓存目录默认 `training/data/cache/planner_context/classic_pois/`。
- `classic_pois` 缓存 TTL 默认 `PLANNER_CONTEXT_CLASSIC_CACHE_TTL_SECONDS=216000`，即 60 小时。

当前基础过滤：

- scenic/experience 过滤培训、留学、考研、公司、产业园、批发、市场等明显噪声。
- scenic 必须命中 scenic 类型白名单。
- experience 必须命中 experience 类型白名单。
- food 必须是 `餐饮服务`。
- hotel 必须是 `住宿服务`。

## 5. Tool Status

当前 `tool_status` 按三类并行任务记录，而不是按五个候选池分别记录：

```json
{
  "weather": {
    "ok": true,
    "message": "available=4, covered_trip_days=4/4"
  },
  "hotels": {
    "ok": true,
    "message": "hotels=10"
  },
  "attractions": {
    "ok": true,
    "message": "classic=12, preference=16, scenic=20, experience=4, food=12"
  }
}
```

## 6. Weather 协议

当前天气包含两组：

- `available_weather`：可用天气来源。线上通常是高德短期预报；训练数据的历史行程可使用 Open-Meteo Archive。
- `trip_weather`：按行程日期对齐后的天气，是 Planner 唯一允许使用的天气。

可用天气：

```json
{
  "date": "2026-04-29",
  "day_weather": "晴",
  "night_weather": "晴",
  "day_temp": 24,
  "night_temp": 9,
  "wind_direction": "西南",
  "wind_power": "1-3",
  "source": "amap_forecast"
}
```

训练数据历史天气：

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

远期天气不可用：

```json
{
  "date": "2026-07-14",
  "day_weather": "远期天气暂无准确预报",
  "night_weather": "远期天气暂无准确预报",
  "day_temp": "未知",
  "night_temp": "未知",
  "wind_direction": "未知",
  "wind_power": "未知",
  "source": "unavailable_future_weather"
}
```

后端 schema 已允许 `day_temp/night_temp` 为 `int` 或 `str`，不会把 `"未知"` 强行转成 `0`。

## 7. Compact PlannerContext

`compact PlannerContext` 是最终发给 Planner LLM 的核心结构化上下文。线上真实模型输入不是裸 compact JSON，而是 `_build_planner_query()` 生成的完整用户消息。

生成位置：

```text
PlannerContextBuilder.compact_for_planner()
```

结构：

```json
{
  "version": "planner_context_v2",
  "request": {},
  "user_profile": {},
  "tool_snapshot": {
    "trip_weather": [],
    "classic_pois": [],
    "preference_pois": [],
    "scenic_pois": [],
    "experience_pois": [],
    "hotel_pois": [],
    "food_pois": [],
    "candidate_counts": {
      "classic_pois": 12,
      "preference_pois": 16,
      "scenic_pois": 20,
      "experience_pois": 4,
      "hotel_pois": 10,
      "food_pois": 12
    }
  },
  "planner_constraints": {}
}
```

compact 和 raw 的区别：

- 删除 `generated_at`。
- 删除 `available_weather`。
- 删除 `tool_status`。
- 删除 POI 的 `id/typecode/cityname/photo_count/source_role`。
- 保留 POI 的 `source_bucket`，让 Planner 区分经典、偏好、体验、餐饮、酒店来源。
- 保留所有候选条数，不默认裁剪候选数量。
- 只裁字段，不裁候选。

compact POI 字段：

```json
{
  "name": "798艺术区",
  "type": "风景名胜;风景名胜",
  "district": "朝阳区",
  "address": "酒仙桥路4号",
  "location": {"longitude": 116.494784, "latitude": 39.985063},
  "rating": "4.8",
  "cost": "127.00",
  "matched_keyword": "艺术",
  "source_bucket": "preference"
}
```

规则：

- `type` 会压缩成长类型的后两段。
- `district` 来自 raw `adname`。
- `address` 最多保留 48 个字符，超长会省略。
- 空值字段会被删除。
- `cost` 有值则保留，无值则删除。
- 酒店候选如果存在 `estimated_cost_hint` 和 `cost_source`，必须保留。
- `matched_keyword` 来自 raw `source_keyword`。
- `source_bucket` 来自 raw `source_bucket`，常见值包括 `classic`、`preference`、`experience`、`food`、`hotel`。

## 8. Planner Query

当前 `_build_planner_query()` 把 compact PlannerContext 嵌入用户消息：

```text
请根据下面的 PlannerContext JSON 生成{city}的{travel_days}天旅行计划。

PlannerContext:
{compact_context_json}

请严格遵守:
1. 只返回一个合法JSON对象，不要输出Markdown代码块、解释、前言、工具调用或<think>内容。
2. 顶层字段必须包含 city/start_date/end_date/days/weather_info/overall_suggestions/budget。
3. days长度必须等于 PlannerContext.request.travel_days，day_index从0开始，date必须逐日对应。
4. weather_info必须逐日对应 PlannerContext.tool_snapshot.trip_weather；远期天气不可用时保留“未知”，不要编造天气。
5. 景点优先使用 classic_pois、preference_pois、scenic_pois 和 experience_pois；酒店必须为 null 或使用 hotel_pois 里的真实酒店，不要把“无”“无住宿”“返程”“当天返程”写成 hotel.name；餐饮优先使用对应候选，并沿用候选里的 name/address/location。
6. 每天安排2-3个景点，每天必须包含breakfast/lunch/dinner三餐。
7. 预算要和住宿、餐饮、景点门票、交通方式大致一致。酒店如果有 estimated_cost_hint，hotel.estimated_cost 必须复制该单晚价格；N天行程默认住宿N-1晚，budget.total_hotels 必须覆盖住宿晚数。无法从工具获得价格时用系统给出的规则估价，不要让模型自由编价。
```

如果 `request.free_text_input` 非空，会追加：

```text
额外要求: {free_text_input}
```

## 9. Runtime Validator

当前 runtime validator 不是完整质量评估器，只做轻量结构校验和 grounding warning。

当前硬校验：

- `city` 必须等于请求城市。
- `start_date/end_date` 必须等于请求日期。
- `days` 长度必须等于 `request.travel_days`。
- 每天 `day_index` 从 0 连续。
- 每天 `date` 必须和请求日期逐日对应。
- 如果存在 `hotel`，`hotel.name` 不能是“无”“无住宿”“返程”等占位词；无住宿只能用 `hotel: null` 表达。
- 每天必须有 `attractions`。
- 每天 `meals` 至少 3 项。
- `weather_info` 日期必须和请求日期完全一致。

当前软校验：

- 景点是否大致来自 `classic_pois + preference_pois + scenic_pois + experience_pois`；名称匹配允许“锦里古街”与“锦里”这类弱命中。
- 酒店是否大致来自 `hotel_pois`。

软校验只打印 warning，不拦截。这样可以避免高德召回缺口导致线上不可用。

## 10. Retry / Fallback

当前 Planner retry 是干净重试：

```text
同一个 planner_query
  -> 第1次生成
  -> 解析失败
  -> 第2次仍使用同一个 planner_query
```

不会把以下内容拼回下一次 prompt：

- 上一次错误信息。
- 上一次失败输出。
- 修复提示。
- 本地 Planner 失败详情。

失败只用于：

- 写入 `training/data/online_feedback/planner_failures.jsonl`。
- 如果后续成功，可构造离线 DPO 候选。

如果个性化 Planner 失败，会切到默认 Planner，但默认 Planner 仍然接收干净 `planner_query`。

## 11. v2 数据生成对齐

离线 v2 SFT/DPO 数据必须和线上协议同构。训练时的 human/input 文本应尽量等于线上真实 `planner_query`。

建议 SFT 样本结构：

```json
{
  "instruction": "根据 PlannerContext 生成严格符合 TripPlan schema 的旅行计划 JSON。",
  "input": "{...线上真实 planner_query...}",
  "output": "{...TripPlan...}",
  "metadata": {
    "compact_planner_context": "{...compact PlannerContext...}",
    "raw_planner_context": "{...raw PlannerContext...}",
    "request": {}
  }
}
```

保存条件：

- `TripPlan` schema 可解析。
- `validate_trip_plan_shape()` 通过。
- 无严重饮食冲突。
- 天气日期和请求日期一致。

v2 DPO 应基于同一个 compact PlannerContext 生成多个自然候选：

```text
base model candidate
SFT model candidate
strong low-temp candidate
strong high-temp candidate
```

chosen/rejected 选择：

```text
chosen = 高分候选
rejected = 低分但结构合法、自然、无显式模板痕迹的候选
```

不要再使用带显式负面标签的模板化坏样本。
