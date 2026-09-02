# LLM Judge Summary

```json
{
  "total": 100,
  "judged": 97,
  "skipped": 3,
  "judge_coverage": 0.97,
  "skip_reason_counts": {
    "schema": 2,
    "judge_failed": 1
  },
  "scores_avg": {
    "preference_satisfaction": 2.8763,
    "practicality": 2.6495,
    "grounding_faithfulness": 3.5567,
    "budget_reasonableness": 1.6082,
    "coherence": 2.3608,
    "overall_quality": 2.1753
  }
}
```

## Low Score Examples

### v3_harder_eval_000106
- overall: 0
- request: 杭州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- issues: ['8 validation errors for TripPlan\ndays.0.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=97.2, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.0.meals.2.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=87.6, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.1.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=82.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.1.meals.2.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=160.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.2.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=78.6, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.2.meals.2.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=61.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.3.meals.1.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=31.8, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float\ndays.3.meals.2.estimated_cost\n  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=68.4, input_type=float]\n    For further information visit https://errors.pydantic.dev/2.12/v/int_from_float']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000119
- overall: 0
- request: 哈尔滨 2026-07-03->2026-07-06 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- issues: ['1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000036
- overall: 0
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000027
- overall: 1.0
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ['全程未安排任何咖啡体验，未满足“咖啡”偏好', '晚餐“杭州酒家”连续在D1/D2/D3/D4晚餐及D5午餐重复出现，严重缺乏餐饮多样性', 'D5景点“南宋德寿宫遗址博物馆”和“杭州植物园”与D2、D3完全重复，且D5无酒店却安排两个景点，不合理', 'D1描述“晚上在酒店享用早餐”自相矛盾', 'D4景点“杭州国家版本馆”和“全山石艺术中心”分处余杭和转塘，一天内跨区远距离跳跃，公共交通不可行', '预算计算严重错误：餐饮实际约792元而计划仅468元；总预算2278元远低于舒适档下限3250元，且未安排咖啡、交通等消费', '缺少城市漫步类专项安排或咖啡馆小坐等体现审美的内容，整体偏常规景点']
- rationale: 计划虽命中多数工具候选，但出现景点重复、餐厅大量复用、预算自相矛盾、缺少咖啡与城市漫步等致命问题，整体质量很差。

### v3_harder_eval_000033
- overall: 1.0
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ['酒店选在常熟市，距离所有景点极远，大幅增加通勤时间和体力消耗，违背“避免太偏远景点”和“老年友好”约束，行程完全不现实', '连续5天午餐、晚餐均使用同一家餐厅，严重缺乏餐饮多样性，违反旅游餐饮原则，导致体验单调', '预算分项计算严重错误：景点总价1400元远超实际（约340元），餐饮总价474元远低于按两人计算的1700元，且总额3874元与分项不符，预算可信度极低', '早餐连续5天同一家小吃店，每日安排几乎完全相同，缺乏变化和具体描述，整体行程呆板']
- rationale: 计划在景点选择上勉强符合偏好，但酒店选址在常熟导致极长通勤，完全无法执行；餐饮极度重复且预算计算多处矛盾，整体质量非常低，无法满足家庭带老人舒适慢游的要求。

### v3_harder_eval_000010
- overall: 1.0
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['每天更换酒店且包含青年旅舍等非舒适型住宿，违反住宿偏好且极不现实', '晚餐多次重复使用同一家餐厅（清真刚刚烤肉芙蓉街店）和同品牌连锁，严重缺乏餐饮多样性', '餐饮成本估算严重错误，未按5人全队计算，导致预算总额严重偏离舒适型预算区间', "乐班Le’ban·农场餐厅为人均119元的高价餐厅，违反'避高价餐厅'约束", '21日中雨天气未做任何室内替代或调整，安排钟楼、大雁塔等户外活动，对老人和儿童不友好', '青龙寺遗址博物馆门票价格错误（应为免费），且预算合计远低于实际应发生费用']
- rationale: 计划在住宿、餐饮约束和预算合理性上存在多重严重失误：住宿几乎每天换且多数不符合舒适型定位；餐饮成本计算脱离per person单位，总预算仅5200元，远低于7200-11100的目标区间；高价餐厅、单一餐厅重复出现直接违反用户避高价和多样化需求；雨天未做调整，实际可行性极差。

### v3_harder_eval_000085
- overall: 1.0
- request: 北京 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['总预算3000元严重超过用户硬限额2100元，且门票虚报为1200元，实际仅约140元', '第5天午餐与晚餐均为同一家北京凯瑞御仙都皇家菜博物馆，单顿586元，两顿共1172元，预算失控且缺乏餐饮多样性', '第4天八达岭长城（延庆）与南苑森林湿地公园（丰台）距离极远，公共交通一日游极不现实', '第1天描述出现“晚上在酒店享用早餐”明显矛盾', '紫光园·烤鸭·北京菜在第1天午餐和第4天午餐重复使用，违反餐饮多样性要求', '第3天午餐和晚餐虽为不同分店，但均为浩海火烧云傣家菜，品牌重复，且该品牌非本地菜，不符合偏好']
- rationale: 行程偏好基本覆盖自然风光与城市漫步，但预算完全失控，门票价格严重高估，餐饮重复昂贵，且包含不可执行的远距离景区组合，整体质量低。

### v3_harder_eval_000072
- overall: 1.0
- request: 哈尔滨 2026-05-05->2026-05-08 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['总预算2963元严重超出2400元硬上限，与用户穷游约束冲突', '5月冰雪大世界已闭园，计划中两日安排冰雪大世界完全无法执行', "酒店选在阿城区，偏离市区景点，通勤荒谬，与'地铁+步行'及城市漫步不匹配", '第四天重复游览冰雪大世界，且波塞冬海底世界为高价偏远景点，违背避偏远和高价餐厅/景点的要求', 'Day3与Day4午晚餐均使用同一餐厅，餐饮缺乏多样性，且部分餐费过高（如老厨家304元、金刚山272元、福成厚304元/餐）', '交通预算仅200元，在酒店偏远的情况下完全不现实，预算计算与门票总额（1155元）也对不上实际门票之和']
- rationale: 计划存在致命硬伤：预算大幅超支、5月开放不可行的冰雪大世界被两次安排、酒店偏僻破坏整个行程的可执行性，且餐饮重复、费用虚高，无法通过任何修正实现合格旅行。

### v3_harder_eval_000120
- overall: 1.0
- request: 珠海 2026-07-03->2026-07-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['景点和餐饮严重重复：情侣路出现三次，珠海大剧院出现两次，粤禧顺·广东顺德菜(情侣中路店)作为午餐或晚餐反复使用五次，缺乏多样性，不符合慢节奏但应丰富体验的要求。', '预算计算严重混乱：total_attractions、total_meals与各日明细明显矛盾，总预算5500远低于实际累计餐费约3900元、门票约1700元（按5人计）以及住宿和交通，无法满足硬性预算约束且未提供可信计算。']
- rationale: 计划名义上覆盖了要求的大部分偏好景点和餐厅，但高度重复的安排使行程单调到不现实。预算表完全失实，无法作为执行参考。虽然使用了工具候选，接地性尚可，但整体质量极低。

### v3_harder_eval_000175
- overall: 1.0
- request: 北京 2026-02-03->2026-02-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['预算计算严重错误：住宿只算3晚（1050）实际4晚（1400）；餐饮总额420与实际1487严重不符；总花费远超2100元硬约束。', '餐饮位置严重不合理：天坛公园与鸽子窝(海淀)、颐和园与浩海火烧云京广店(朝阳)等跨度大，毫无顺路性。', '最后一天晚餐为“无”，安排不完整。', '两天重复使用浩海火烧云傣家菜品牌，且菜系非北京本地菜，与偏好冲突。']
- rationale: 景点选择尚可，但餐饮安排混乱、位置跳跃、预算严重超标，完全无法满足2100元硬约束，整体质量极差。

### v3_harder_eval_000185
- overall: 1.0
- request: 广州 2025-08-07->2025-08-11 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['餐饮严重违反多样性与 grounding 规则：整趟行程反复使用同一品牌‘大鸽饭’（体育西店出现3次晚餐+1次午餐；棠下店出现2次午餐），lunch/dinner 几乎被‘大鸽饭’垄断，完全没有体现本地菜多样性，明显违背‘不应多天反复使用同一家真实餐厅或同一品牌’的要求。', '景点安排存在重复、节奏不佳：广州动物园出现在第3天和第5天两次，广州塔与广州塔-空中漫步本质上是同一地标，分别出现在不同天，造成重复与行程碎片化；且同一天安排广州塔（海珠）后远赴长隆野生动物世界（番禺），公共交通耗时过长，不现实。', '酒店位置偏远且缺乏换宿合理性：连续4天选用白云区‘广州好运来公寓’，而行程大量活动在海珠、天河、越秀、番禺，每天往返交通时长极高，对 solo 摄影旅行者既不省力也不合理；酒店 breakfast 统一为‘酒店早餐’，但未说明民宿是否含早，grounding 弱。', '最后一天酒店为 null 且当天仍有完整活动安排（烈士陵园+动物园+午晚餐），未交代行李寄存与去程安排；同时 budget 内酒店成本仅按 4 晚×300 计算，与需求不符。', '预算计算明显偏小：合计 2000 元勉强进入 budget 区间但分项粗糙，总交通费仅 200 元（5 天全公共交通）明显低估，且二沙岛门票 80 元在候选 hint 为‘免费/0’类公园中偏高，餐饮费用均按单人次饭贴但未含早的真实花费构成。']
- rationale: 计划严重缺乏餐饮多样性、景点重复、酒店位置偏、最后一天缺失住宿、交通耗时与预算均不合理。餐厅几乎只反复用‘大鸽饭’，完全背离本地菜偏好和 grounding 要求，导致实用性和整体评分极低。

### v3_harder_eval_000238
- overall: 1.0
- request: 上海 2026-08-02->2026-08-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['严重预算超支：计划总预算5820元，超出用户5200元的硬性上限，且未遵守comfortable档位及65%-100%目标区间。', '餐饮grounding严重不足：多日午餐/晚餐使用未被food_pois收录的餐厅或占位名称（如dinner描述含糊），且多日重复使用完全相同的单一早餐（魏家凉皮），缺乏多样性。', '酒店位置极度偏远：选择松江区的璞爵国际酒店，与黄浦区、浦东新区的主要景点距离过远，每日行程需长时间跨区打车，不符合“适中节奏”和“不要太偏远”的约束。']
- rationale: 计划在景点选择上部分匹配了用户的城市地标和夜景偏好，但存在多项致命缺陷。预算硬超支且未合理分配；酒店选址严重偏离市区，导致行程不切实际；餐饮几乎脱离工具提供的候选池，lunch/dinner缺乏真实具体内容且重复单一早餐。整体计划需要彻底重构以满足约束。

### v3_harder_eval_000045
- overall: 2.0
- request: 济南 2026-04-04->2026-04-08 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['预算严重不实：总餐费实际约1168元，计划仅列480元；门票应总计400元却标320元；分项相加不等于总价2000元', '最后一天安排莱芜战役纪念馆，位于莱芜区，距离市区极远，明确违反“不要太偏远”约束，且当天中雨，不适合户外远行', '多日午餐与晚餐重复同一家餐厅（day0箪食巷私房菜奥体店早晚重复；day1向民炒鸡老店早晚重复；箪食巷玉函店在day2午餐和day3午餐重复），严重缺乏餐饮多样性', '住宿选在历城区东部（聚满佳住房、舒心小憩公寓），距离主要景点区较远，公共交通便利性不足，影响现实执行', '缺少真正的城市漫步内容和街道穿行体验，仅以景点替代，行程描述单薄']
- rationale: 用户偏好基本被回应，但计划存在严重预算自洽错误、极度远距离景点反约束、餐饮大量重复使用、住宿偏远、最后一天恶劣天气下户外远行等问题，整体可执行性和质量较低。

### v3_harder_eval_000039
- overall: 2.0
- request: 深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- issues: ['酒店位于光明区，每日往返南山、罗湖、福田，长距离移动严重违背老人与儿童体力照顾需求，安排不现实', '午餐和晚餐连续4天分别固定为同一家餐厅（蘩楼、南门涮肉），严重缺乏餐饮多样性，与用户特色餐厅偏好和清淡饮食要求部分不匹配', '预算计算错误：实际餐饮总费用约为908元，但预算中仅列468元，导致总价自洽性差', '行程描述过于简略，每日仅一个景点且顺序重复，缺乏具体时间安排和衔接细节，连贯性极差']
- rationale: 计划虽选用了部分符合条件的景点和餐饮，但酒店选址偏远导致每日通勤疲劳，不符合老人儿童出行核心诉求；餐饮完全重复且预算严重错算，整体实用性、连贯性和自洽性很低，基本不可行。

### v3_harder_eval_000048
- overall: 2.0
- request: 北京 2026-01-04->2026-01-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['预算严重超限：总预算6350元超过hard上限5200元，且住宿按3晚850元计算，实际只需2晚，餐饮总成本远超预算中3000元的估计', '未覆盖用户明确偏好的夜景和购物：行程描述提到晚上欣赏夜景却没有任何夜景地点，完全缺失购物安排', '酒店位置偏远：华北宾馆位于石景山区，距离市中心核心景点较远，不符合紧凑高效节奏，增加通勤成本', '每日描述与内容矛盾：宣称晚上欣赏夜景但无对应景点，整体建议空泛，缺乏具体细节']
- rationale: 计划在景点和餐饮选择上较好地使用了PlannerContext候选，但预算严重不合理且多项偏好未满足，导致整体质量很差。

### v3_harder_eval_000008
- overall: 2.0
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['预算严重不一致：总住宿写2250元但仅住两晚应为1500元；总餐饮写720元但各餐累加约1206元，且总预算3875元与分项加总矛盾，实际花费可能低于严格预算下限，硬约束未满足', '第二天晚餐仅“老爷爷的手工鲜花饼”，作为朋友聚餐正餐过于单薄，缺乏菜品多样性且不符合“吃得好”的偏好', '旅行计划完全没有涉及夜景和购物活动，未体现用户偏好的“夜景”“购物”等要求，偏好覆盖不完整', '午餐和晚餐选择的云南菜餐厅（如桃红小馆）未明确标注清真或无猪肉，存在与“不吃猪肉”约束冲突的风险，虽然部分餐厅可能可提供无猪肉菜，但未给予足够保证']
- rationale: 景点和餐厅基本来自候选集，天气处理正确，但预算严重不自洽、总价计算错误且可能不达标，同时餐饮安排欠缺合理性、缺失夜景与购物，整体质量较低。

### v3_harder_eval_000025
- overall: 2.0
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['包含上海迪士尼度假区，属于典型商业化打卡点，明确违背用户“尽量避开商业化打卡点”的负面约束', '每日景点与餐饮地理跨区严重不协调：Day3位于静安的自然博物馆搭配松江区的两顿农家菜，Day4迪士尼搭配长宁午餐和浦东世博晚餐，Day5世纪公园搭配宝山区同一面馆的两顿，公共交通极难实现', '预算极度不自洽：门票实际合计约838元，餐饮合计约1527元，住宿1400元，粗估总支出超3700元，远超2300元硬上限；计划所列分项与合计相互矛盾', '餐饮严重违反多样性：Day1与Day4晚餐重复使用“南门涮肉(上海一店)”，Day5午餐与晚餐均为“海福多共富海鲜面馆”，同天同店重复使用', '第5天午餐与晚餐均使用同一家高单价面馆（224元/人），明显不合理，且无必要重复']
- rationale: 计划引入迪士尼已破坏偏好，每日路线跨区跳跃根本不可执行，预算计算错误且严重超支，餐饮大量重复，整体为低质量方案。

### v3_harder_eval_000014
- overall: 2.0
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- issues: ['预算分项计算严重错误：景点门票总计180元与实际115元不符；酒店总计1350元应为900元（仅住2晚）；餐饮总计429元与实际约722元不符；总预算2259元超出hard上限2100元。', '第一天午餐和晚餐均选择观锦餐厅（不同分店），同一天餐饮主题重复，缺乏多样性。', '第三天再次安排宽窄巷子景区，与第一天重复，浪费有限半天时间，未充分利用其他候选景点。', '行程描述未体现‘自由活动多’，每日具体安排较满，自由时间不明确。']
- rationale: 计划选取的景点和餐厅大多符合偏好，且交通和体力安排合理。但预算部分存在致命错误，各项加总混乱，总价超标；同时重复安排宽窄巷子，第一天午晚餐品牌重复，降低了整体方案的严谨性和体验感。

### v3_harder_eval_000007
- overall: 2.0
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ['预算严重自洽失败：餐饮总额仅列480元，实际估算超2000元，总额2800元远低于7000元舒适档位，不符合软约束要求。', '第四天都江堰行程极不现实：午餐设在春熙路翠孃孃老火锅，与都江堰景区地理跨越过大，公共交通无法衔接。', '餐饮多样性严重不足：翠孃孃老火锅重复3次、马旺子重复2次，又无咖啡或小众餐厅补充，损害审美体验。', "未满足用户关键偏好：完全缺失'小众展馆'和'咖啡'相关安排，也未体现城市漫步路线设计。", '住宿选址不妥：成都希望旅馆位于龙泉驿，与大部分景点距离过远，每日长距离通勤降低舒适度与可执行性。']
- rationale: 行程选用了工具中的真实POI，grounding基本合格。但偏好被忽视、餐饮高频率重复、都江堰当天午餐选址错误、预算严重失真，整体质量很低，勉强可用但不推荐。

### v3_harder_eval_000023
- overall: 2.0
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ['预算计算严重错误：total_attractions 凭空出现180元，实际无门票支出；total_meals 仅1152元，但按给定估算实际应为约2618元，导致总预算失真。', '第三天双廊古镇和第四天喜洲古镇的午餐、晚餐均安排在距离景点一小时车程的大理古城，对老人极不现实，实用性差。', "最后一天晚餐选择糕饼店'老爷爷的手工鲜花饼(总店)'，不适合作为四人正餐，且费用使用 per-person hint 但计划中当作总价，同时破坏饮食结构和连贯性。", '第二天午餐和晚餐都在下关区域，但与当天景点洱海公园勉强可接受，但整体每日餐饮地点缺乏与景点的就近匹配。']
- rationale: 计划满足不爬山、少辣、慢节奏等偏好，但餐饮地点与景点严重不匹配，导致实用性低；预算分项严重错漏，虚构门票且餐饮低估，完全不具参考性。整体质量差。
