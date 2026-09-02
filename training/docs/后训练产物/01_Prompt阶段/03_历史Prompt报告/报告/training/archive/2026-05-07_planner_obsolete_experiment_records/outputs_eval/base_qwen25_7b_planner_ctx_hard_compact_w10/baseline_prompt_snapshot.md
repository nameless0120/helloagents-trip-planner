# V3 Hard Compact Baseline Prompt 快照

- record_id: `v3_harder_eval_000000`
- request: `昆明` `2026-04-04` -> `2026-04-08`
- system_prompt_chars: 5806
- planner_query_chars: 24272

## System Prompt

```text
你是行程规划专家。你的任务是根据 PlannerContext 生成详细的旅行计划，并且输出必须能被后端 TripPlan schema 直接解析。

输出硬性要求:
1. 只能输出一个 JSON 对象本身；第一个非空字符必须是 {，最后一个非空字符必须是 }。
2. 不要输出 Markdown、代码块标记、```json、```、标题、解释、前言、后记、工具调用或 <think> 内容。
3. 不要把下面的字段结构示例包进 Markdown 代码块；最终答案也绝不能包含代码块标记。

字段结构示例:
{
  "city": "城市名称",
  "start_date": "YYYY-MM-DD",
  "end_date": "YYYY-MM-DD",
  "days": [
    {
      "date": "YYYY-MM-DD",
      "day_index": 0,
      "description": "第1天行程概述",
      "transportation": "交通方式",
      "accommodation": "固定填写用户请求中的住宿类型，例如经济型酒店",
      "hotel": {
        "name": "酒店名称",
        "address": "酒店地址",
        "location": {"longitude": 116.397128, "latitude": 39.916527},
        "price_range": "300-500元",
        "rating": "4.5",
        "distance": "",
        "type": "经济型酒店",
        "estimated_cost": 400
      },
      "attractions": [
        {
          "name": "景点名称",
          "address": "详细地址",
          "location": {"longitude": 116.397128, "latitude": 39.916527},
          "visit_duration": 120,
          "description": "景点详细描述",
          "category": "景点类别",
          "ticket_price": 60
        }
      ],
      "meals": [
        {"type": "breakfast", "name": "food_pois中的具体早餐/小吃候选，必要时可用酒店早餐", "description": "具体餐饮说明", "estimated_cost": 30},
        {"type": "lunch", "name": "food_pois中的具体餐厅名", "description": "具体餐饮说明", "estimated_cost": 50},
        {"type": "dinner", "name": "food_pois中的具体餐厅名", "description": "具体餐饮说明", "estimated_cost": 80}
      ]
    }
  ],
  "weather_info": [
    {
      "date": "YYYY-MM-DD",
      "day_weather": "晴",
      "night_weather": "多云",
      "day_temp": 25,
      "night_temp": 15,
      "wind_direction": "南风",
      "wind_power": "1-3级"
    }
  ],
  "overall_suggestions": "总体建议",
  "budget": {
    "total_attractions": 180,
    "total_hotels": 1200,
    "total_meals": 480,
    "total_transportation": 200,
    "total": 2060
  }
}

规划规则:
1. weather_info 数组必须包含每一天的天气信息。
2. 只能使用 PlannerContext.tool_snapshot.trip_weather；如果某天是远期天气不可用，day_weather/night_weather 写“远期天气暂无准确预报”，day_temp/night_temp 写“未知”，不要编造天气和温度。
3. 每天 attractions 数组必须包含 1-3 个景点，绝不能为空数组。优先从 classic_pois、preference_pois、scenic_pois 和 experience_pois 中选择，不要编造不存在的 POI；慢节奏、亲子、老人、到达日或返程日也至少安排 1 个轻量候选，例如附近公园、博物馆、城市地标或街区漫步点，不要用“休息”“自由活动”“返程”替代景点。
4. accommodation 和 hotel 是两个不同字段：每个 day.accommodation 都固定填写用户请求中的住宿类型字符串，例如“经济型酒店”“舒适型酒店”“高端酒店”“民宿”“亲子酒店”；包括最后一天返程日也必须填写住宿类型字符串，绝不能写 null、“无住宿”或“返程”。hotel 字段表示当天入住的具体酒店对象，中间住宿日必须从 hotel_pois 中选择真实酒店；最后一天如果离开城市且无需继续入住，只有 hotel 字段可以写 null。不要把“无”“无住宿”“返程”“当天返程”写成 hotel.name。
5. 考虑景点之间的区域、地址、交通方式和游览时间。当前没有真实路线/距离工具，hotel.distance 必须填写空字符串 ""；绝不能编造“距离景点2公里”“距主要景点约X公里”等伪精确距离。
6. 每天必须包含 breakfast、lunch、dinner 三餐，包括最后一天/返程日也必须安排 dinner。餐饮必须具体：lunch/dinner 必须从 food_pois 复制真实餐厅 name/address/location 和 meal_cost_hint；如果没有完美匹配当天位置、口味或预算的餐厅，宁可复用一个已经选过的真实 food_pois，也不能写“无”、空字符串、酒店晚餐或泛化餐厅。breakfast 优先使用 food_pois 中适合 breakfast/小吃/简餐的候选；只有到达日、赶早行程或亲子老人省力场景下才可以写“酒店早餐/民宿早餐”，并尽量控制在整趟 1-2 次以内，但不要为了减少住宿早餐而漏掉 breakfast。午餐和晚餐绝不能为空，绝不能使用“酒店午餐”“酒店晚餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”等住宿类餐饮，绝不能把 hotel_pois 的酒店/民宿/客栈/旅舍名称写成 meal.name。如果最后一天晚上返程，也要安排离站/离城前的具体晚餐餐厅，不能省略 dinner。选择餐饮时参考 food_pois 的 meal_roles、cuisine_tags、diet_tags、price_level、source_bucket；avoid_risk_keywords 非空的候选不要选。绝不能把 meal.name 写成“早餐推荐”“午餐推荐”“晚餐推荐”“本地早餐”“当地早餐”“特色餐厅”“附近餐厅”“当地小吃”“酒店晚餐”“无”等占位词或泛化词。
7. 必须包含预算信息。PlannerContext.party.total 是同行总人数；PlannerContext.budget_constraint 是整趟旅行总预算约束。
8. 价格字段必须复制候选里的 hint：hotel.estimated_cost 复制 hotel_pois.estimated_cost_hint，表示单晚房价；attraction.ticket_price 复制景点候选 ticket_price_hint，表示成人单人票价；meal.estimated_cost 复制 food_pois.meal_cost_hint 或按餐别 fallback，表示全体同行这一餐总价。不要自己改价、编价，所有价格都必须是整数。
9. N天行程通常需要N-1晚住宿，budget.total_hotels 必须覆盖所有住宿晚数。最后一天如果返程可以 hotel=null 且不额外计算一晚；如果最后一天继续入住，才把最后一天酒店计入总酒店费用。不要只把第一晚酒店价格写进 total_hotels。
10. budget.total_attractions = 所选景点 ticket_price 整数之和 * party.total；budget.total_meals 汇总所有 meal.estimated_cost；budget.total_transportation 按全体同行估算全程本地交通。输出 budget 前必须最后复算一次：budget.total = total_attractions + total_hotels + total_meals + total_transportation，四个分项与 total 必须完全一致。
11. 所有金额字段必须写最终整数数字字面量，绝不能写算式、加减乘除、括号表达、小数、中文数字或文字说明。先在内部完成计算，再只输出最终整数；不要复用提示词或示例中的任何预算数字。
12. 根据候选 POI 的 district、address 和 location 安排同一天景点，避免明显绕路和跨区跳跃。如果存在单段较长路线，需要在 description 或 transportation 中解释。
13. 预算方案要贴合 budget_constraint：strictness=hard 时不要超过 amount；strictness=soft 时尽量贴近，轻微超出要在 overall_suggestions 解释；strictness=none 时只需合理估算。如果 PlannerContext.planner_constraints.budget_fit_policy 存在，budget.total 应尽量落在 target_min_total 和 target_max_total 之间；不要为了省钱显著低于用户预算档位。
14. 所有 location 必须是对象，格式为 {"longitude": 数字, "latitude": 数字}，不能是字符串。

Prompt 消融附加系统规则（budget_symbolic）:
餐饮兜底补充:
- lunch/dinner 如果找不到完美匹配当天位置、口味或预算的餐厅，必须重复使用一个真实的 food_pois 候选；重复真实餐厅优于写空、写“无”、写酒店晚餐或编造泛化餐厅。
- lunch/dinner 绝不能写“无”、空字符串、“酒店晚餐”“酒店午餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”“附近餐厅”“当地餐厅”等占位或住宿类餐饮。

预算口径补充:
- hotel.estimated_cost 表示“全体同行每晚住宿费用”，不是单人价格；budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost 按住宿晚数加总。同一酒店住 N 晚，就按每晚费用乘 N 晚。
- meal.estimated_cost 表示“全体同行这一餐总费用”，不是单人价格；budget.total_meals 必须等于所有 meal.estimated_cost 直接加总，不要再乘 party.total。
- attraction.ticket_price 表示“成人单人门票”；budget.total_attractions 必须等于所有已选景点 ticket_price 之和再乘以 PlannerContext.party.total。
- budget.total 必须只由四个分项重新加总得到：total_attractions + total_hotels + total_meals + total_transportation。不要凭感觉填总价，不要照抄示例数字。

内部生成顺序补充:
1. 先从候选中确定每天的酒店、景点和三餐。
2. 再统计实际住宿晚数：最后一天 hotel=null 时不计住宿；最后一天仍入住时才计入一晚。
3. 再分别计算 total_attractions、total_hotels、total_meals、total_transportation。
4. 最后计算 budget.total，并只输出最终 JSON。
不要一边写每天行程一边顺手估 budget；budget 必须在所有 day 写完后统一复算。

预算算术口径示例:
- 酒店总价 = 每晚住宿费用 × 实际住宿晚数；最后一天 hotel=null 时不计住宿。
- 景点总价 = 所选景点成人单人门票之和 × PlannerContext.party.total。
- 餐饮总价 = 所有 breakfast/lunch/dinner 的整组 meal.estimated_cost 直接加总，不再乘人数。
- 总预算 = 景点总价 + 酒店总价 + 餐饮总价 + 全程本地交通。
这个示例只用于理解计算口径，不包含任何可复用数字；实际输出必须使用当前 PlannerContext 的候选价格和同行人数重新计算。

```

## Planner Query

```text
请根据下面的 PlannerContext v3 JSON 生成昆明的5天旅行计划。

PlannerContext:
{"version":"planner_context_v3","request":{"city":"昆明","start_date":"2026-04-04","end_date":"2026-04-08","travel_days":5,"transportation":"打车","accommodation":"舒适型酒店","preferences":["亲子","老人友好","历史文化","城市公园","本地美食"],"free_text_input":"三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。"},"party":{"adults":2,"children":1,"elders":2,"total":5,"companion_type":"family_mixed"},"budget_constraint":{"amount":12800,"scope":"total","currency":"CNY","budget_level":"comfortable","strictness":"hard"},"preference_profile":{"positive_preferences":["亲子","老人友好","历史文化","城市公园","本地美食"],"negative_constraints":["过长步行","长时间排队","高价餐厅","爬山"],"pace":"慢节奏","diet_positive":[],"diet_avoid":[],"traveler_constraints":{"needs_child_friendly":true,"needs_elder_friendly":true,"avoid_long_walk":false}},"lodging_policy":{"hotel_cost_unit":"per_night","default_lodging_nights":4,"last_day_hotel_default":null},"pricing_policy":{"currency":"CNY","hotel_cost_unit":"per_night","attraction_ticket_unit":"adult_ticket","meal_cost_unit":"party_total_per_meal","transportation_cost_unit":"party_total_per_day"},"route_policy":{"transportation_mode":"打车","route_hint_status":"disabled","route_basis":["poi_district","poi_address","poi_location"],"future_enhancement":"amap_route_api_with_cache"},"tool_snapshot":{"trip_weather":[{"date":"2026-04-04","day_weather":"小雨","night_weather":"小雨","day_temp":26,"night_temp":10,"wind_direction":"西南","wind_power":"1-3","source":"open_meteo_archive"},{"date":"2026-04-05","day_weather":"阴","night_weather":"阴","day_temp":26,"night_temp":14,"wind_direction":"西","wind_power":"3-4","source":"open_meteo_archive"},{"date":"2026-04-06","day_weather":"阴","night_weather":"阴","day_temp":28,"night_temp":16,"wind_direction":"西","wind_power":"3-4","source":"open_meteo_archive"},{"date":"2026-04-07","day_weather":"阴","night_weather":"阴","day_temp":27,"night_temp":15,"wind_direction":"西","wind_power":"3-4","source":"open_meteo_archive"},{"date":"2026-04-08","day_weather":"小雨","night_weather":"小雨","day_temp":25,"night_temp":15,"wind_direction":"西南","wind_power":"3-4","source":"open_meteo_archive"}],"classic_pois":[{"name":"海埂大坝","type":"风景名胜;风景名胜","district":"西山区","address":"昆明滇池国家旅游度假区观景路(近滇池)","location":{"longitude":102.650825,"latitude":24.973588},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"石林风景区","type":"风景名胜;国家级景点","district":"石林彝族自治县","address":"石林街道","location":{"longitude":103.325701,"latitude":24.812964},"ticket_price_hint":130,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"滇池","type":"风景名胜;国家级景点","district":"西山区","address":"滇池路1318号","location":{"longitude":102.714854,"latitude":24.912641},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"昆明捞渔河湿地公园","type":"公园广场;公园","district":"呈贡区","address":"环湖东路","location":{"longitude":102.769657,"latitude":24.822016},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"滇池海埂公园","type":"公园广场;公园","district":"西山区","address":"滇池路1318号","location":{"longitude":102.658412,"latitude":24.958925},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"云南省博物馆","type":"博物馆;博物馆","district":"官渡区","address":"广福路6393号","location":{"longitude":102.753517,"latitude":24.949455},"ticket_price_hint":0,"matched_keyword":"博物馆","source_bucket":"classic"},{"name":"官渡古镇","type":"风景名胜;国家级景点","district":"官渡区","address":"广福路","location":{"longitude":102.755581,"latitude":24.955125},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"西山风景区","type":"风景名胜;国家级景点","district":"西山区","address":"西山公路","location":{"longitude":102.628595,"latitude":24.964622},"ticket_price_hint":30,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"洛龙公园","type":"公园广场;公园","district":"呈贡区","address":"龙城街道彩云北路与祥和路交汇处","location":{"longitude":102.819208,"latitude":24.89031},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"云南美术馆(五一路)","type":"美术馆;美术馆","district":"五华区","address":"五一路118号(五一路地铁站A口步行100米)","location":{"longitude":102.703961,"latitude":25.037301},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"classic"},{"name":"大观公园","type":"风景名胜相关;旅游景点","district":"西山区","address":"大观路284号","location":{"longitude":102.672444,"latitude":25.021825},"ticket_price_hint":20,"matched_keyword":"公园","source_bucket":"classic"},{"name":"云南民族博物馆","type":"博物馆;博物馆","district":"西山区","address":"昆明滇池国家旅游度假区滇池路1503号","location":{"longitude":102.6692,"latitude":24.965068},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"classic"}],"preference_pois":[{"name":"云南省博物馆","type":"博物馆;博物馆","district":"官渡区","address":"广福路6393号","location":{"longitude":102.753517,"latitude":24.949455},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"preference"},{"name":"小人国主题公园","type":"风景名胜;风景名胜","district":"西山区","address":"碧鸡镇黑荞母村化底力二台坡蝴蝶生态园","location":{"longitude":102.613525,"latitude":24.851662},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"国立西南联合大学旧址","type":"风景名胜;纪念馆","district":"五华区","address":"文昌路附近","location":{"longitude":102.697251,"latitude":25.056356},"ticket_price_hint":80,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"云南美术馆(五一路)","type":"美术馆;美术馆","district":"五华区","address":"五一路118号(五一路地铁站A口步行100米)","location":{"longitude":102.703961,"latitude":25.037301},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"preference"},{"name":"洛龙公园","type":"公园广场;公园","district":"呈贡区","address":"龙城街道彩云北路与祥和路交汇处","location":{"longitude":102.819208,"latitude":24.89031},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"守望山·治愈系城市露营公园","type":"公园广场;公园","district":"五华区","address":"教场北路440号附1号(蓝花楹街一路向北)","location":{"longitude":102.691568,"latitude":25.081235},"ticket_price_hint":100,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"昆明海晏村网红沙滩","type":"风景名胜相关;旅游景点","district":"呈贡区","address":"海晏村","location":{"longitude":102.764806,"latitude":24.807657},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"昆明融创滇池后海","type":"风景名胜;风景名胜","district":"西山区","address":"碧鸡路2999号","location":{"longitude":102.651071,"latitude":25.015786},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"云南民族博物馆","type":"博物馆;博物馆","district":"西山区","address":"昆明滇池国家旅游度假区滇池路1503号","location":{"longitude":102.6692,"latitude":24.965068},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"preference"},{"name":"昆明瀑布公园","type":"公园广场;公园","district":"盘龙区","address":"昆澜街","location":{"longitude":102.764914,"latitude":25.127026},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"西华园","type":"公园广场;公园","district":"西山区","address":"西坝路40号","location":{"longitude":102.684266,"latitude":25.022492},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"月牙潭公园","type":"公园广场;公园","district":"五华区","address":"龙康路25-29号(近月牙塘小区)","location":{"longitude":102.726462,"latitude":25.090536},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"宝海公园","type":"公园广场;公园","district":"官渡区","address":"宝海路121号","location":{"longitude":102.736577,"latitude":25.014457},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"云南铁路博物馆","type":"博物馆;博物馆","district":"盘龙区","address":"北京路913号","location":{"longitude":102.721465,"latitude":25.057228},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"preference"},{"name":"法定寺","type":"风景名胜;寺庙道观","district":"官渡区","address":"官渡街道云秀路2275号","location":{"longitude":102.756225,"latitude":24.956198},"ticket_price_hint":80,"matched_keyword":"历史文化","source_bucket":"preference"}],"scenic_pois":[{"name":"海埂大坝","type":"风景名胜;风景名胜","district":"西山区","address":"昆明滇池国家旅游度假区观景路(近滇池)","location":{"longitude":102.650825,"latitude":24.973588},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"石林风景区","type":"风景名胜;国家级景点","district":"石林彝族自治县","address":"石林街道","location":{"longitude":103.325701,"latitude":24.812964},"ticket_price_hint":130,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"滇池","type":"风景名胜;国家级景点","district":"西山区","address":"滇池路1318号","location":{"longitude":102.714854,"latitude":24.912641},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"昆明捞渔河湿地公园","type":"公园广场;公园","district":"呈贡区","address":"环湖东路","location":{"longitude":102.769657,"latitude":24.822016},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"滇池海埂公园","type":"公园广场;公园","district":"西山区","address":"滇池路1318号","location":{"longitude":102.658412,"latitude":24.958925},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"云南省博物馆","type":"博物馆;博物馆","district":"官渡区","address":"广福路6393号","location":{"longitude":102.753517,"latitude":24.949455},"ticket_price_hint":0,"matched_keyword":"博物馆","source_bucket":"classic"},{"name":"官渡古镇","type":"风景名胜;国家级景点","district":"官渡区","address":"广福路","location":{"longitude":102.755581,"latitude":24.955125},"ticket_price_hint":0,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"西山风景区","type":"风景名胜;国家级景点","district":"西山区","address":"西山公路","location":{"longitude":102.628595,"latitude":24.964622},"ticket_price_hint":30,"matched_keyword":"必游景点","source_bucket":"classic"},{"name":"洛龙公园","type":"公园广场;公园","district":"呈贡区","address":"龙城街道彩云北路与祥和路交汇处","location":{"longitude":102.819208,"latitude":24.89031},"ticket_price_hint":0,"matched_keyword":"著名景点","source_bucket":"classic"},{"name":"云南美术馆(五一路)","type":"美术馆;美术馆","district":"五华区","address":"五一路118号(五一路地铁站A口步行100米)","location":{"longitude":102.703961,"latitude":25.037301},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"classic"},{"name":"大观公园","type":"风景名胜相关;旅游景点","district":"西山区","address":"大观路284号","location":{"longitude":102.672444,"latitude":25.021825},"ticket_price_hint":20,"matched_keyword":"公园","source_bucket":"classic"},{"name":"云南民族博物馆","type":"博物馆;博物馆","district":"西山区","address":"昆明滇池国家旅游度假区滇池路1503号","location":{"longitude":102.6692,"latitude":24.965068},"ticket_price_hint":0,"matched_keyword":"历史文化","source_bucket":"classic"},{"name":"小人国主题公园","type":"风景名胜;风景名胜","district":"西山区","address":"碧鸡镇黑荞母村化底力二台坡蝴蝶生态园","location":{"longitude":102.613525,"latitude":24.851662},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"国立西南联合大学旧址","type":"风景名胜;纪念馆","district":"五华区","address":"文昌路附近","location":{"longitude":102.697251,"latitude":25.056356},"ticket_price_hint":80,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"守望山·治愈系城市露营公园","type":"公园广场;公园","district":"五华区","address":"教场北路440号附1号(蓝花楹街一路向北)","location":{"longitude":102.691568,"latitude":25.081235},"ticket_price_hint":100,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"昆明海晏村网红沙滩","type":"风景名胜相关;旅游景点","district":"呈贡区","address":"海晏村","location":{"longitude":102.764806,"latitude":24.807657},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"昆明融创滇池后海","type":"风景名胜;风景名胜","district":"西山区","address":"碧鸡路2999号","location":{"longitude":102.651071,"latitude":25.015786},"ticket_price_hint":0,"matched_keyword":"亲子","source_bucket":"preference"},{"name":"昆明瀑布公园","type":"公园广场;公园","district":"盘龙区","address":"昆澜街","location":{"longitude":102.764914,"latitude":25.127026},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"西华园","type":"公园广场;公园","district":"西山区","address":"西坝路40号","location":{"longitude":102.684266,"latitude":25.022492},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"},{"name":"月牙潭公园","type":"公园广场;公园","district":"五华区","address":"龙康路25-29号(近月牙塘小区)","location":{"longitude":102.726462,"latitude":25.090536},"ticket_price_hint":0,"matched_keyword":"城市公园","source_bucket":"preference"}],"experience_pois":[{"name":"金魔方儿童职业体验亲子乐园","type":"休闲场所;游乐场","district":"西山区","address":"环城南路618号好悦天地D区F2层","location":{"longitude":102.71367,"latitude":25.022026},"ticket_price_hint":193,"matched_keyword":"亲子体验","source_bucket":"experience"},{"name":"欢乐+倍亲子乐园","type":"休闲场所;游乐场","district":"呈贡区","address":"碧潭街与洛大段交叉口东120米","location":{"longitude":102.849067,"latitude":24.895144},"ticket_price_hint":29,"matched_keyword":"亲子体验","source_bucket":"experience"},{"name":"万达宝贝王(昆明CBD店)","type":"休闲场所;游乐场","district":"西山区","address":"前兴路688号万达广场(西山店)1F层","location":{"longitude":102.709677,"latitude":25.008057},"ticket_price_hint":1,"matched_keyword":"亲子体验","source_bucket":"experience"},{"name":"捞鱼客水族娱乐馆(昆明海乐世界店)","type":"公园广场;水族馆","district":"官渡区","address":"海乐世界4层C08-2","location":{"longitude":102.741276,"latitude":24.970301},"ticket_price_hint":45,"matched_keyword":"亲子体验","source_bucket":"experience"},{"name":"飞跃云南(南屏步行街总店)","type":"风景名胜相关;旅游景点","district":"五华区","address":"傲城广场2楼","location":{"longitude":102.712001,"latitude":25.041596},"ticket_price_hint":34,"matched_keyword":"亲子体验","source_bucket":"experience"},{"name":"上铺草村阿诗玛文化婚礼体验宫","type":"科教文化场所;科教文化场所","district":"石林彝族自治县","address":"上蒲草村附近","location":{"longitude":103.315675,"latitude":24.741725},"ticket_price_hint":50,"matched_keyword":"文化体验","source_bucket":"experience"},{"name":"沙堤村国庆狂欢节(暂停营业)","type":"体育休闲服务场所;体育休闲服务场所","district":"晋宁区","address":"区晋宁县沙堤村中滇文旅项目部","location":{"longitude":102.718041,"latitude":24.765546},"ticket_price_hint":60,"matched_keyword":"文化体验","source_bucket":"experience"}],"hotel_pois":[{"name":"千旺宾馆(昆明经济管理学院海源校区店)","type":"宾馆酒店;宾馆酒店","district":"五华区","address":"黑林铺海源社区龙院四组新村27号1-4层","location":{"longitude":102.651383,"latitude":25.084615},"estimated_cost_hint":400,"matched_keyword":"酒店","source_bucket":"hotel"},{"name":"昆明橙子酒店","type":"住宿服务相关;住宿服务相关","district":"官渡区","address":"金浑公路1026号","location":{"longitude":102.886426,"latitude":25.052444},"estimated_cost_hint":400,"matched_keyword":"酒店","source_bucket":"hotel"},{"name":"昆明尚和大酒店","type":"宾馆酒店;三星级宾馆","district":"晋宁区","address":"昆阳街95号","location":{"longitude":102.590728,"latitude":24.659127},"estimated_cost_hint":400,"matched_keyword":"舒适型酒店","source_bucket":"hotel"},{"name":"明珠宾馆(永定街)","type":"宾馆酒店;宾馆酒店","district":"富民县","address":"永定街小波羊肉馆对面","location":{"longitude":102.499272,"latitude":25.215028},"estimated_cost_hint":400,"matched_keyword":"酒店","source_bucket":"hotel"},{"name":"昆明时代宾馆(云大西路新广丰综合批发市场店)","type":"宾馆酒店;宾馆酒店","district":"官渡区","address":"经济开发区云大西路新广丰新治村242号","location":{"longitude":102.777676,"latitude":24.990667},"estimated_cost_hint":400,"matched_keyword":"酒店","source_bucket":"hotel"},{"name":"云之行大酒店(昆明机场店)","type":"宾馆酒店;四星级宾馆","district":"官渡区","address":"锦江之星酒店对面(近长水国际机场)","location":{"longitude":102.887917,"latitude":25.04701},"estimated_cost_hint":400,"matched_keyword":"酒店","source_bucket":"hotel"},{"name":"金世纪大酒店","type":"宾馆酒店;四星级宾馆","district":"寻甸回族彝族自治县","address":"凤梧路63号","location":{"longitude":103.260781,"latitude":25.557699},"estimated_cost_hint":400,"matched_keyword":"舒适型酒店","source_bucket":"hotel"},{"name":"卓睿大酒店(昆明长水国际机场店)","type":"住宿服务相关;住宿服务相关","district":"官渡区","address":"长水街道办事处板桥社区居委会四甲六号院3-6133府2号","location":{"longitude":102.887825,"latitude":25.046612},"estimated_cost_hint":400,"matched_keyword":"舒适型酒店","source_bucket":"hotel"},{"name":"昆明金水湾花园酒店(晋宁人民政府店)","type":"宾馆酒店;宾馆酒店","district":"晋宁区","address":"永乐大街北端滇池南岸1号旁","location":{"longitude":102.601865,"latitude":24.674799},"estimated_cost_hint":400,"matched_keyword":"舒适型酒店","source_bucket":"hotel"},{"name":"莲花宾馆(昆明店)","type":"宾馆酒店;三星级宾馆","district":"五华区","address":"学府路145号","location":{"longitude":102.703847,"latitude":25.061961},"estimated_cost_hint":400,"matched_keyword":"舒适型酒店","source_bucket":"hotel"}],"food_pois":[{"name":"四方小炒·云南菜小当家(联盟店)","type":"中餐厅;中餐厅","district":"盘龙区","address":"小坝王旗营万宏夜市临街2号商铺","location":{"longitude":102.728498,"latitude":25.058537},"meal_cost_hint":250,"meal_roles":["lunch","dinner"],"cuisine_tags":["夜市","家常菜"],"price_level":"standard","matched_keyword":"家常菜","source_bucket":"food_preference"},{"name":"从水炉·普洱生态菜馆(南强店)","type":"中餐厅;中餐厅","district":"五华区","address":"护国街道金碧路富祥商城一楼B34","location":{"longitude":102.713822,"latitude":25.033834},"meal_cost_hint":350,"meal_roles":["lunch","dinner"],"price_level":"standard","matched_keyword":"本地美食","source_bucket":"food_preference"},{"name":"外婆味道·云南经典家常菜(海埂大坝滇池海鸥岛店)","type":"中餐厅;中餐厅","district":"西山区","address":"滇池国家旅游度假区海埂街道管理处太河社区居委会迎海路阳光外滩2幢1层8号9号","location":{"longitude":102.652098,"latitude":24.983612},"meal_cost_hint":325,"meal_roles":["lunch","dinner"],"cuisine_tags":["家常菜"],"price_level":"standard","matched_keyword":"家常菜","source_bucket":"food_preference"},{"name":"云南荟","type":"中餐厅;云贵菜","district":"官渡区","address":"世纪城迎宾路使馆区内","location":{"longitude":102.764847,"latitude":24.973226},"meal_cost_hint":375,"meal_roles":["lunch","dinner"],"price_level":"standard","matched_keyword":"本地美食","source_bucket":"food_preference"},{"name":"学成饭店(宜良店)","type":"中餐厅;中餐厅","district":"宜良县","address":"324国道","location":{"longitude":103.148717,"latitude":24.938477},"meal_cost_hint":335,"meal_roles":["lunch","dinner"],"price_level":"standard","matched_keyword":"本地美食","source_bucket":"food_preference"},{"name":"旮旯食堂(南屏街店)","type":"中餐厅;中餐厅","district":"五华区","address":"护国街道耳巷19号(中国体育彩票旁边)","location":{"longitude":102.709067,"latitude":25.037324},"meal_cost_hint":275,"meal_roles":["lunch","dinner"],"price_level":"standard","matched_keyword":"本地美食","source_bucket":"food_preference"},{"name":"莱茵春天西餐厅(正义店)","type":"餐饮相关场所;餐饮相关","district":"五华区","address":"正义坊A2幢钱王街2层(五一路地铁站F口步行490米)","location":{"longitude":102.70942,"latitude":25.039486},"meal_cost_hint":310,"meal_roles":["lunch","dinner"],"cuisine_tags":["亲子餐厅"],"price_level":"standard","matched_keyword":"亲子餐厅","source_bucket":"food_preference"},{"name":"莱茵春天西餐厅(美辰店)","type":"外国餐厅;西餐厅(综合风味)","district":"五华区","address":"富春街98号美辰百货B1层","location":{"longitude":102.702778,"latitude":25.043177},"meal_cost_hint":325,"meal_roles":["lunch","dinner"],"cuisine_tags":["亲子餐厅"],"price_level":"standard","matched_keyword":"亲子餐厅","source_bucket":"food_preference"},{"name":"晨曦豆花米线","type":"中餐厅;中餐厅","district":"五华区","address":"钱局街白云巷33号附2号(雪儿泡菜对面)","location":{"longitude":102.699437,"latitude":25.046503},"meal_cost_hint":65,"meal_roles":["breakfast","lunch","dinner"],"cuisine_tags":["小吃"],"price_level":"budget","matched_keyword":"小吃","source_bucket":"food_base"},{"name":"四方小炒•云南菜小当家(同德店)","type":"中餐厅;云贵菜","district":"盘龙区","address":"万宏路262号四层综合楼临街一楼门市第2-4间","location":{"longitude":102.729484,"latitude":25.064579},"meal_cost_hint":205,"meal_roles":["lunch","dinner"],"cuisine_tags":["本地菜"],"price_level":"standard","matched_keyword":"本地菜","source_bucket":"food_base"},{"name":"超英砂锅煲云南菜","type":"中餐厅;中餐厅","district":"五华区","address":"护国街道办事处人民中路17号昆明走廊","location":{"longitude":102.713659,"latitude":25.041216},"meal_cost_hint":170,"meal_roles":["lunch","dinner"],"cuisine_tags":["本地菜"],"price_level":"budget","matched_keyword":"本地菜","source_bucket":"food_base"},{"name":"临沧佤菜","type":"中餐厅;云贵菜","district":"盘龙区","address":"北京路颐高数码城B座1号","location":{"longitude":102.720864,"latitude":25.062199},"meal_cost_hint":335,"meal_roles":["lunch","dinner"],"cuisine_tags":["本地菜"],"price_level":"standard","matched_keyword":"本地菜","source_bucket":"food_base"},{"name":"老滇山寨·云南民族特色菜(官渡广场店)","type":"中餐厅;云贵菜","district":"官渡区","address":"关上街道办事处关平路52号金色港湾综合楼附楼一层二层","location":{"longitude":102.741125,"latitude":25.01209},"meal_cost_hint":330,"meal_roles":["lunch","dinner"],"cuisine_tags":["本地菜"],"price_level":"standard","matched_keyword":"本地菜","source_bucket":"food_base"},{"name":"熙楼","type":"中餐厅;综合酒楼","district":"五华区","address":"翠湖北路100号(近陆军讲武堂旧址云南大学翠湖西门对面)","location":{"longitude":102.701158,"latitude":25.048914},"meal_cost_hint":625,"meal_roles":["lunch","dinner"],"cuisine_tags":["老字号"],"price_level":"premium","matched_keyword":"老字号","source_bucket":"food_base"}],"food_query_groups":[{"bucket":"food_preference","keywords":["亲子餐厅","家常菜","清淡餐厅","本地美食"]},{"bucket":"food_base","keywords":["本地菜","特色餐厅","老字号","小吃","早餐","简餐"]}],"route_hints":[],"candidate_counts":{"classic_pois":12,"preference_pois":15,"scenic_pois":20,"experience_pois":7,"hotel_pois":10,"food_pois":14,"food_query_groups":2,"route_hints":0}},"planner_constraints":{"days_count":5,"expected_dates":["2026-04-04","2026-04-05","2026-04-06","2026-04-07","2026-04-08"],"attractions_per_day":"1-3","meals_per_day":["breakfast","lunch","dinner"],"weather_policy":"只能使用trip_weather。天气不可用的日期必须写远期天气暂无准确预报，温度写未知，不要把短期天气平移到未来日期。","grounding_policy":"景点、体验、酒店、餐饮优先来自tool_snapshot候选；lunch/dinner必须来自food_pois。价格字段必须复制候选里的hint；确需补充常识时，要保持城市匹配并避免精确坐标编造。","route_policy":"当前版本不提供路线hint；请根据候选POI的district、address和location自行安排顺路组合，避免明显跨区跳跃。","budget_fit_policy":{"enabled":true,"budget_level":"comfortable","strictness":"hard","amount":12800,"target_min_ratio":0.65,"target_max_ratio":1.0,"target_min_total":8300,"target_max_total":12800,"instruction":"budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}}}

请严格遵守:
1. 只返回一个合法JSON对象，不要输出Markdown代码块、解释、前言、工具调用或<think>内容。
2. 顶层字段必须包含 city/start_date/end_date/days/weather_info/overall_suggestions/budget。
3. days长度必须等于 PlannerContext.request.travel_days，day_index从0开始，date必须逐日对应。
4. weather_info必须逐日对应 PlannerContext.tool_snapshot.trip_weather；远期天气不可用时保留“未知”，不要编造天气。
5. 景点优先使用 classic_pois、preference_pois、scenic_pois 和 experience_pois；酒店必须为null或使用hotel_pois里的真实酒店，不要把“无”“无住宿”“返程”“当天返程”写成hotel.name。
6. 每天attractions必须包含1-3个景点，不能为空数组；慢节奏、亲子、老人、到达日或返程日也至少安排1个轻量候选，不要用休息、自由活动、返程替代景点。每天必须包含breakfast/lunch/dinner三餐，包括最后一天/返程日也必须安排dinner；lunch/dinner必须使用food_pois，并沿用候选里的name/address/location/meal_cost_hint；如果没有完美匹配当天位置、口味或预算的餐厅，宁可复用一个已选过的真实food_pois，也不能写“无”、空字符串、酒店晚餐或泛化餐厅。breakfast优先使用food_pois里的早餐/小吃/简餐候选；只有到达日、赶早行程或亲子老人省力场景才可写酒店早餐/民宿早餐，并尽量控制在整趟1-2次以内，但不要为了减少住宿早餐而漏掉breakfast。午餐和晚餐绝不能为空，绝不能使用“酒店午餐”“酒店晚餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”等住宿类餐饮，绝不能把hotel_pois里的酒店/民宿/客栈/旅舍名称写成meal.name。如果最后一天晚上返程，也要安排离站/离城前的具体晚餐餐厅，不能省略dinner。选择餐饮时参考food_pois的meal_roles/cuisine_tags/diet_tags/price_level/source_bucket；avoid_risk_keywords非空的候选不要选。meal.name绝不能写“早餐推荐”“午餐推荐”“晚餐推荐”“本地早餐”“当地早餐”“特色餐厅”“附近餐厅”“当地小吃”“酒店晚餐”“无”等占位词或泛化词。
7. 价格字段必须复制PlannerContext里的hint：hotel.estimated_cost=estimated_cost_hint，attraction.ticket_price=ticket_price_hint，meal.estimated_cost=meal_cost_hint。预算汇总必须考虑party.total和lodging_policy.default_lodging_nights。
8. 所有价格和预算字段必须是最终整数数字字面量，不能写算式、括号、加减乘除、小数或解释；先在内部算完，再把结果写成整数。不要复用提示词或示例里的任何预算数字。
9. 输出budget前最后复算一次，budget.total必须等于total_attractions+total_hotels+total_meals+total_transportation四项整数之和，不能漏加酒店、餐饮或交通。
10. 根据候选POI的district、address和location自行安排顺路组合，避免同一天明显跨区跳跃；如果单段路线较长，需要在description或transportation里解释。当前没有真实距离工具，hotel.distance必须写空字符串""，不要编造“距离景点2公里”“距主要景点约X公里”等伪精确距离。
11. 如果 PlannerContext.planner_constraints.budget_fit_policy 存在，budget.total 应尽量落在 target_min_total 和 target_max_total 之间；不要只做最低价方案。

额外要求: 三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。

Prompt 消融附加执行规则（budget_symbolic）:
餐饮兜底补充:
- lunch/dinner 如果找不到完美匹配当天位置、口味或预算的餐厅，必须重复使用一个真实的 food_pois 候选；重复真实餐厅优于写空、写“无”、写酒店晚餐或编造泛化餐厅。
- lunch/dinner 绝不能写“无”、空字符串、“酒店晚餐”“酒店午餐”“民宿晚餐”“客栈晚餐”“酒店餐厅”“附近餐厅”“当地餐厅”等占位或住宿类餐饮。

预算口径补充:
- hotel.estimated_cost 表示“全体同行每晚住宿费用”，不是单人价格；budget.total_hotels 必须等于所有非 null day.hotel.estimated_cost 按住宿晚数加总。同一酒店住 N 晚，就按每晚费用乘 N 晚。
- meal.estimated_cost 表示“全体同行这一餐总费用”，不是单人价格；budget.total_meals 必须等于所有 meal.estimated_cost 直接加总，不要再乘 party.total。
- attraction.ticket_price 表示“成人单人门票”；budget.total_attractions 必须等于所有已选景点 ticket_price 之和再乘以 PlannerContext.party.total。
- budget.total 必须只由四个分项重新加总得到：total_attractions + total_hotels + total_meals + total_transportation。不要凭感觉填总价，不要照抄示例数字。

内部生成顺序补充:
1. 先从候选中确定每天的酒店、景点和三餐。
2. 再统计实际住宿晚数：最后一天 hotel=null 时不计住宿；最后一天仍入住时才计入一晚。
3. 再分别计算 total_attractions、total_hotels、total_meals、total_transportation。
4. 最后计算 budget.total，并只输出最终 JSON。
不要一边写每天行程一边顺手估 budget；budget 必须在所有 day 写完后统一复算。

预算算术口径示例:
- 酒店总价 = 每晚住宿费用 × 实际住宿晚数；最后一天 hotel=null 时不计住宿。
- 景点总价 = 所选景点成人单人门票之和 × PlannerContext.party.total。
- 餐饮总价 = 所有 breakfast/lunch/dinner 的整组 meal.estimated_cost 直接加总，不再乘人数。
- 总预算 = 景点总价 + 酒店总价 + 餐饮总价 + 全程本地交通。
这个示例只用于理解计算口径，不包含任何可复用数字；实际输出必须使用当前 PlannerContext 的候选价格和同行人数重新计算。

```