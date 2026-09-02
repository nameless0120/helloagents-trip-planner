# 餐饮 Grounding Miss 样本检查

- 评估目录：`training/outputs/eval/base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8`
- miss 样本数：33
- 说明：这里的 miss 指 `meal.name` 没命中 `food_pois.name`，且不是合法住宿早餐 fallback。

## 1. v3_harder_eval_000014

### 用户请求

- 城市/日期：成都 | 2026-06-03 -> 2026-06-05 | 3天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'business'}
- 交通/住宿：打车 / 舒适型酒店
- 预算：{'amount': 2100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 特色餐厅 / 自由活动多 / 博物馆
- 负向约束：太早起 / 过长步行 / 密集行程
- 饮食：想吃/偏好=无；避免=无
- 自由文本：出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-05 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 蛙蛙鸡冷锅鱼(金沙总店) | food_preference | lunch/dinner | 71 | 老字号 |  |
| 2 | 观锦餐厅(天府新谷店) | food_preference | lunch/dinner | 136 | 特色餐厅 |  |
| 3 | 观锦餐厅(天廊店) | food_preference | lunch/dinner | 120 | 特色餐厅 |  |
| 4 | 陶德砂锅(春熙路店) | food_preference | lunch/dinner | 61 | 老字号 |  |
| 5 | 翠孃孃老火锅(春熙路老店) | food_preference | lunch/dinner | 102 | 老字号 |  |
| 6 | 乔一乔怪味餐厅(东升店) | food_preference | lunch/dinner | 93 | 老字号 |  |
| 7 | 龙户人家串串香(奎星楼店) | food_preference | lunch/dinner | 85 | 老字号 |  |
| 8 | 马旺子·川小馆(成都太古里店) | food_preference | lunch/dinner | 133 | 特色餐厅 |  |
| 9 | 悦百味·品质川菜(悠方店) | food_companion | lunch/dinner | 160 |  |  |
| 10 | 蓉庭食府.匠心川菜.精品家宴.商务宴请 | food_companion | lunch/dinner | 97 |  |  |
| 11 | 饕林餐厅(春熙路店) | food_companion | lunch/dinner | 65 |  |  |
| 12 | 成都林恩国际俱乐部餐厅 | food_companion | lunch/dinner | 60 | 高端餐厅 |  |
| 13 | 四妹钵钵鸡(望平街店) | food_base | breakfast/lunch/dinner | 48 | 小吃 |  |

### 模型输出相关天

#### D3 2026-06-05

- 描述：参观都江堰景区，下午自由活动。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：成都青柚共享酒店(文殊院骡马市地铁站店)
- 景点：都江堰景区
- 餐饮：breakfast:酒店早餐(30元) / lunch:四妹钵钵鸡(望平街店)(48元) / dinner:酒店晚餐(60元)

### 预算摘要

- total=2285 | attractions=255 | hotels=1350 | meals=480 | transport=200

## 2. v3_harder_eval_000022

### 用户请求

- 城市/日期：桂林 | 2026-04-04 -> 2026-04-07 | 4天
- 同行：{'adults': 4, 'children': 0, 'elders': 0, 'total': 4, 'companion_type': 'friends'}
- 交通/住宿：地铁+步行 / 经济型酒店
- 预算：{'amount': 2400, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'limited', 'strictness': 'hard'}
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 负向约束：海鲜餐厅 / 购物团 / 太偏远的景点 / 高价餐厅
- 饮食：想吃/偏好=无；避免=海鲜
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-04-04 | dinner | 民俗街夜市 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 食在香乡野本地菜 | food_preference | lunch/dinner | 160 | 本地菜 |  |
| 2 | 澳门酒家(高新店) | food_preference | lunch/dinner | 232 | 本地菜 |  |
| 3 | 山味.本地农家菜 | food_preference | lunch/dinner | 160 | 本地菜 |  |
| 4 | 山野间餐厅 | food_preference | lunch/dinner | 160 | 本地菜 |  |
| 5 | 碗碗都市香米粉店(铁西店) | food_preference | breakfast/lunch/dinner | 40 | 小吃/快餐 |  |
| 6 | 仁利米粉(施家园店) | food_preference | breakfast/lunch/dinner | 52 | 小吃 |  |
| 7 | 海天肠粉 | food_preference | breakfast/lunch/dinner | 56 | 小吃 |  |
| 8 | 秋福米粉(桂林市正阳路步行街店) | food_preference | breakfast/lunch/dinner | 40 | 小吃 |  |
| 9 | 田源米粉(三多店) | food_budget | breakfast/lunch/dinner | 28 | 小吃 |  |
| 10 | 麦当劳(桂林临桂万达餐厅) | food_budget | breakfast/lunch/dinner | 120 | 快餐 |  |
| 11 | 麦当劳(桂林西城南路餐厅) | food_budget | breakfast/lunch/dinner | 108 | 快餐 |  |
| 12 | 绝味鸭脖(桂林临桂花生唐店) | food_budget | breakfast/lunch/dinner | 136 | 快餐 |  |
| 13 | 椿记烧鹅(中山店) | food_base | lunch/dinner | 224 | 老字号 |  |
| 14 | 椿记烧鹅(西街店) | food_base | lunch/dinner | 224 | 老字号 |  |
| 15 | 阿甘酒家(依仁店) | food_base | lunch/dinner | 272 | 老字号 |  |
| 16 | 阿甘酒家(解西店) | food_base | lunch/dinner | 340 | 老字号 |  |

### 模型输出相关天

#### D1 2026-04-04

- 描述：第一天游览象鼻山景区，晚上在民俗街夜市品尝桂林特色小吃。
- 交通：地铁+步行 | accommodation=经济型酒店
- 酒店：桂林兴安家家福宾馆
- 景点：象鼻山景区
- 餐饮：breakfast:酒店早餐(30元) / lunch:食在香乡野本地菜(160元) / dinner:民俗街夜市(100元)

### 预算摘要

- total=2280 | attractions=1000 | hotels=600 | meals=480 | transport=200

## 3. v3_harder_eval_000038

### 用户请求

- 城市/日期：厦门 | 2026-05-07 -> 2026-05-09 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5800, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-09 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 醉壹号海鲜大排档·老厦门特色菜(厦门美食地标店) | food_preference | lunch/dinner | 285 | 本地菜/海鲜 |  |
| 2 | 临家闽南菜(环岛路店) | food_preference | lunch/dinner | 375 | 本地菜 |  |
| 3 | 鑫坞堂 海鲜热炒(中山路总店) | food_preference | lunch/dinner | 207 | 本地菜/海鲜 |  |
| 4 | 鑫草美夫妻厦门菜(厦大白城店) | food_preference | lunch/dinner | 195 | 本地菜 |  |
| 5 | 草莓夫妇丨厦门菜(黄厝店) | food_preference | lunch/dinner | 315 | 本地菜 |  |
| 6 | 妞妞餐厅老厦门特色菜 | food_preference | lunch/dinner | 228 | 特色餐厅 |  |
| 7 | 百家春好德来姜母鸭 | food_preference | lunch/dinner | 180 | 特色餐厅 |  |
| 8 | 202特色排档(洪文分店) | food_preference | lunch/dinner | 306 | 特色餐厅 |  |
| 9 | 好食来大排档(32年美食航标店) | food_base | lunch/dinner | 285 | 老字号 |  |
| 10 | 相约厦门平价海鲜城(八市美食地标店) | food_base | lunch/dinner | 117 | 老字号/海鲜 |  |

### 模型输出相关天

#### D3 2026-05-09

- 描述：最后一天游览厦门城市广场和厦门山海健康步道，晚上返回。
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：厦门城市广场 / 厦门山海健康步道
- 餐饮：breakfast:酒店早餐(30元) / lunch:202特色排档(洪文分店)(306元) / dinner:酒店晚餐(285元)

### 预算摘要

- total=4008 | attractions=150 | hotels=2400 | meals=858 | transport=600

## 4. v3_harder_eval_000036

### 用户请求

- 城市/日期：长沙 | 2026-06-03 -> 2026-06-06 | 4天
- 同行：{'adults': 2, 'children': 1, 'elders': 0, 'total': 3, 'companion_type': 'family_with_children'}
- 交通/住宿：自驾 / 亲子酒店
- 预算：{'amount': 5000, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：亲子 / 动物园 / 海洋馆 / 城市公园 / 本地美食
- 负向约束：夜生活 / 太晚返程 / 过长步行 / 排队太久
- 饮食：想吃/偏好=无；避免=无
- 自由文本：带5岁孩子自驾，想安排亲子体验，但不要夜生活、太晚返程、过长步行或排队太久。预算是硬约束。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-03 | dinner | 酒店晚餐 |
| 2026-06-04 | dinner | 长沙海底世界 |
| 2026-06-06 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 解满嗲壹双好手 | food_preference | lunch/dinner | 189 |  |  |
| 2 | 四方坪三十栋饭店(五一广场店) | food_preference | lunch/dinner | 162 |  |  |
| 3 | 耕渔雅院·湖南鱼鲜(雨花店) | food_preference | lunch/dinner | 288 |  |  |
| 4 | 聚味瞿记·龙虾堂(国金店) | food_preference | lunch/dinner | 462 | 海鲜 |  |
| 5 | 文和友(海信广场) | food_preference | lunch/dinner | 264 |  |  |
| 6 | 湘在光脑壳家常菜馆面粉 | food_preference | lunch/dinner | 222 | 家常菜 |  |
| 7 | 我家小院开福店 | food_preference | lunch/dinner | 159 | 家常菜 |  |
| 8 | 火宫殿(东塘分店) | food_preference | lunch/dinner | 141 | 家常菜 |  |
| 9 | 映象潇湘·小瑶村(植物园店) | food_companion | lunch/dinner | 216 | 家常菜 |  |
| 10 | 胖伢子口味菜 | food_companion | lunch/dinner | 147 | 家常菜 |  |
| 11 | 长沙三景韦尔斯利酒店.OVAL全日制餐厅 | food_companion | lunch/dinner | 300 | 亲子餐厅 |  |
| 12 | 花之林人文餐厅(莲馨苑店) | food_companion | lunch/dinner | 180 | 亲子餐厅 |  |
| 13 | 夏日玛莉西餐厅(德思勤店) | food_companion | lunch/dinner | 174 | 亲子餐厅 |  |
| 14 | 喜座·湖南美食村落(总店) | food_budget | lunch/dinner | 399 | 特色餐厅 |  |
| 15 | 四方坪夜市 | food_budget | lunch/dinner | 96 | 老字号/夜市 |  |
| 16 | 鸿先阁 干煸虾 | food_budget | lunch/dinner | 300 | 老字号 |  |
| 17 | 秦皇食府(市府店) | food_budget | lunch/dinner | 240 | 老字号 |  |
| 18 | 大碗先生(悦方ID MALL店) | food_budget | lunch/dinner | 150 | 老字号 |  |
| 19 | 秦皇食府·尚馔(贺龙店) | food_budget | lunch/dinner | 339 | 老字号 |  |
| 20 | 王捌小院(红花坡店) | food_budget | lunch/dinner | 270 | 本地菜 |  |
| 21 | 渔米湘•本地农家湘菜(铜官窑店) | food_budget | lunch/dinner | 108 | 本地菜 |  |
| 22 | 天宝兄弟(长沙汇景城店) | food_base | breakfast/lunch/dinner | 525 | 小吃 |  |
| 23 | 大晴老板不在·锡纸烧烤大排档 | food_base | breakfast/lunch/dinner | 195 | 小吃 |  |

### 模型输出相关天

#### D1 2026-06-03

- 描述：入住亲子酒店，参观湖南省博物馆和五一广场，晚上在酒店享用晚餐。
- 交通：自驾 | accommodation=亲子酒店
- 酒店：长沙|庭绅·Whimsy酒店(五一广场火车站地铁站店)
- 景点：湖南省博物馆 / 五一广场
- 餐饮：breakfast:酒店早餐(30元) / lunch:解满嗲壹双好手(189元) / dinner:酒店晚餐(180元)

#### D2 2026-06-04

- 描述：参观橘子洲风景名胜区和岳麓书院，晚上在长沙海底世界享用晚餐。
- 交通：自驾 | accommodation=亲子酒店
- 酒店：长沙|庭绅·Whimsy酒店(五一广场火车站地铁站店)
- 景点：橘子洲风景名胜区 / 岳麓书院
- 餐饮：breakfast:酒店早餐(30元) / lunch:四方坪三十栋饭店(五一广场店)(162元) / dinner:长沙海底世界(120元)

#### D4 2026-06-06

- 描述：参观长沙生态动物园和返回，晚上在酒店享用晚餐。
- 交通：自驾 | accommodation=亲子酒店
- 酒店：None
- 景点：长沙生态动物园
- 餐饮：breakfast:酒店早餐(30元) / lunch:大晴老板不在·锡纸烧烤大排档(195元) / dinner:酒店晚餐(180元)

### 预算摘要

- total=3120 | attractions=120 | hotels=1500 | meals=1020 | transport=400

## 5. v3_harder_eval_000048

### 用户请求

- 城市/日期：北京 | 2026-01-04 -> 2026-01-06 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5200, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-01-06 | dinner | 不白吃有文化中心 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 紫光园·烤鸭·北京菜(前门大栅栏店) | food_preference | lunch/dinner | 180 | 本地菜 |  |
| 2 | 鸽子窝(四季青店) | food_preference | lunch/dinner | 321 | 本地菜 |  |
| 3 | 北京凯瑞御仙都皇家菜博物馆 | food_preference | lunch/dinner | 1758 | 本地菜 |  |
| 4 | 浩海火烧云傣家菜(京广店) | food_preference | lunch/dinner | 315 | 本地菜 |  |
| 5 | 浩海火烧云傣家菜(东安市场店) | food_preference | lunch/dinner | 300 | 本地菜 |  |
| 6 | 牛街清真满恒記(平安里西大街店) | food_preference | lunch/dinner | 225 | 特色餐厅/清真/清真 |  |
| 7 | 宫宴(北京店) | food_preference | lunch/dinner | 1629 | 特色餐厅 |  |
| 8 | 蘇锦宴·淮扬菜·大班徽菜·果木烤鸭(定慧寺店) | food_preference | lunch/dinner | 486 | 特色餐厅 |  |
| 9 | 胡大饭馆(簋街三店) | food_base | lunch/dinner | 411 | 老字号 |  |

### 模型输出相关天

#### D3 2026-01-06

- 描述：游览北京历史文化景点，晚上返程。
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：雍和宫 / 中国国家博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:浩海火烧云傣家菜(东安市场店)(300元) / dinner:不白吃有文化中心(304元)

### 预算摘要

- total=6220 | attractions=120 | hotels=4200 | meals=1200 | transport=600

## 6. v3_harder_eval_000056

### 用户请求

- 城市/日期：昆明 | 2026-05-05 -> 2026-05-08 | 4天
- 同行：{'adults': 2, 'children': 1, 'elders': 0, 'total': 3, 'companion_type': 'family_with_children'}
- 交通/住宿：自驾 / 亲子酒店
- 预算：{'amount': 5000, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：亲子 / 动物园 / 海洋馆 / 城市公园 / 本地美食
- 负向约束：夜生活 / 太晚返程 / 过长步行 / 排队太久
- 饮食：想吃/偏好=无；避免=无
- 自由文本：带5岁孩子自驾，想安排亲子体验，但不要夜生活、太晚返程、过长步行或排队太久。预算是硬约束。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-08 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 四方小炒·云南菜小当家(联盟店) | food_preference | lunch/dinner | 150 | 夜市/家常菜 |  |
| 2 | 从水炉·普洱生态菜馆(南强店) | food_preference | lunch/dinner | 210 |  |  |
| 3 | 外婆味道·云南经典家常菜(海埂大坝滇池海鸥岛店) | food_preference | lunch/dinner | 195 | 家常菜 |  |
| 4 | 云南荟 | food_preference | lunch/dinner | 225 |  |  |
| 5 | 学成饭店(宜良店) | food_preference | lunch/dinner | 201 |  |  |
| 6 | 旮旯食堂(南屏街店) | food_preference | lunch/dinner | 165 |  |  |
| 7 | 莱茵春天西餐厅(正义店) | food_preference | lunch/dinner | 186 | 亲子餐厅 |  |
| 8 | 莱茵春天西餐厅(美辰店) | food_preference | lunch/dinner | 195 | 亲子餐厅 |  |
| 9 | 上菌山·云南野生牛肝菌火锅(昆明老街店) | food_companion | lunch/dinner | 390 | 家常菜 |  |
| 10 | 茄子恰恰·脆皮小麻鸭(昆明老街店) | food_companion | lunch/dinner | 150 | 家常菜 |  |
| 11 | 晋府人家(滇池华夏御府店) | food_companion | lunch/dinner | 195 | 家常菜 |  |
| 12 | 莱茵春天西餐厅(青年店) | food_companion | lunch/dinner | 174 | 亲子餐厅 |  |
| 13 | 四方小炒•云南菜小当家(同德店) | food_budget | lunch/dinner | 123 | 本地菜 |  |
| 14 | 超英砂锅煲云南菜 | food_budget | lunch/dinner | 102 | 本地菜 |  |
| 15 | 临沧佤菜 | food_budget | lunch/dinner | 201 | 本地菜 |  |
| 16 | 老滇山寨·云南民族特色菜(官渡广场店) | food_budget | lunch/dinner | 198 | 本地菜 |  |
| 17 | 熙楼 | food_budget | lunch/dinner | 375 | 老字号 |  |
| 18 | 嘉华鲜花饼·现烤(昆明老街店) | food_budget | lunch/dinner | 90 | 老字号 |  |
| 19 | 晨曦豆花米线 | food_base | breakfast/lunch/dinner | 39 | 小吃 |  |

### 模型输出相关天

#### D4 2026-05-08

- 描述：返程，享受酒店早餐。
- 交通：自驾 | accommodation=无住宿
- 酒店：None
- 景点：酒店早餐
- 餐饮：breakfast:酒店早餐(30元) / lunch:超英砂锅煲云南菜(102元) / dinner:酒店晚餐(150元)

### 预算摘要

- total=2846 | attractions=576 | hotels=1500 | meals=570 | transport=200

## 7. v3_harder_eval_000058

### 用户请求

- 城市/日期：洛阳 | 2026-05-06 -> 2026-05-08 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5600, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-08 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 一记洛阳菜·糖醋小排·水席(十字街店) | food_preference | lunch/dinner | 219 | 本地菜 |  |
| 2 | 洛阳宴.洛阳菜(南昌路店) | food_preference | lunch/dinner | 306 | 本地菜 |  |
| 3 | 洛阳十字街小吃一条街 | food_preference | breakfast/lunch/dinner | 81 | 小吃 |  |
| 4 | 小街天府 | food_preference | breakfast/lunch/dinner | 75 | 小吃 |  |
| 5 | 宴愉餐茶艺术餐厅 | food_preference | lunch/dinner | 201 | 本地菜 |  |
| 6 | 光头东烙馍村·水席洛阳菜(火车站店) | food_preference | lunch/dinner | 210 | 本地菜 |  |
| 7 | 光头东烙馍村·水席洛阳菜(博物馆店) | food_preference | lunch/dinner | 210 | 本地菜 |  |
| 8 | 琥珀餐厅(洛阳宝龙广场店) | food_preference | lunch/dinner | 273 | 特色餐厅 |  |

### 模型输出相关天

#### D3 2026-05-08

- 描述：游览白马寺和隋唐洛阳城国家遗址公园，晚上返回。
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：白马寺 / 隋唐洛阳城国家遗址公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:宴愉餐茶艺术餐厅(201元) / dinner:酒店晚餐(210元)

### 预算摘要

- total=3100 | attractions=480 | hotels=1500 | meals=720 | transport=300

## 8. v3_harder_eval_000062

### 用户请求

- 城市/日期：厦门 | 2026-05-07 -> 2026-05-10 | 4天
- 同行：{'adults': 4, 'children': 0, 'elders': 0, 'total': 4, 'companion_type': 'friends'}
- 交通/住宿：地铁+步行 / 经济型酒店
- 预算：{'amount': 2900, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'limited', 'strictness': 'hard'}
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 负向约束：海鲜餐厅 / 购物团 / 太偏远的景点 / 高价餐厅
- 饮食：想吃/偏好=无；避免=海鲜
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-08 | dinner | 鼓浪屿风琴博物馆附近餐厅 |
| 2026-05-09 | dinner | 厦门园林博览苑附近餐厅 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 好食来大排档(32年美食航标店) | food_preference | lunch/dinner | 380 | 老字号 |  |
| 2 | 临家闽南菜(环岛路店) | food_preference | lunch/dinner | 500 | 本地菜 |  |
| 3 | 鑫草美夫妻厦门菜(厦大白城店) | food_preference | lunch/dinner | 260 | 本地菜 |  |
| 4 | 草莓夫妇丨厦门菜(黄厝店) | food_preference | lunch/dinner | 420 | 本地菜 |  |
| 5 | 妞妞餐厅老厦门特色菜 | food_preference | lunch/dinner | 304 | 特色餐厅 |  |
| 6 | 八市阿杰五香 | food_budget | breakfast/lunch/dinner | 36 | 小吃 |  |
| 7 | 局口拌面(中山路店) | food_budget | breakfast/lunch/dinner | 120 | 小吃 |  |
| 8 | 小田豆浆(集美店) | food_budget | breakfast/lunch/dinner | 68 | 小吃 |  |
| 9 | 芋包王闽南茶楼 | food_budget | breakfast/lunch/dinner | 180 | 小吃 |  |
| 10 | 肯德基(滨北店) | food_budget | breakfast/lunch/dinner | 144 | 快餐 |  |
| 11 | 四里沙茶面(七星园店) | food_budget | breakfast/lunch/dinner | 136 | 快餐 |  |
| 12 | 吴再添小吃店 | food_budget | breakfast/lunch/dinner | 72 | 小吃/快餐 |  |

### 模型输出相关天

#### D2 2026-05-08

- 描述：游览鼓浪屿风景名胜区和鼓浪屿管风琴艺术中心，晚上在鼓浪屿风琴博物馆附近享用晚餐。
- 交通：地铁+步行 | accommodation=经济型酒店
- 酒店：鼓浪屿晃岩36酒店
- 景点：鼓浪屿风景名胜区 / 鼓浪屿管风琴艺术中心
- 餐饮：breakfast:酒店早餐(30元) / lunch:小田豆浆(集美店)(17元) / dinner:鼓浪屿风琴博物馆附近餐厅(50元)

#### D3 2026-05-09

- 描述：游览南普陀寺和天竺山森林公园，晚上在厦门园林博览苑附近享用晚餐。
- 交通：地铁+步行 | accommodation=经济型酒店
- 酒店：厦门原宿海景公寓
- 景点：南普陀寺 / 天竺山森林公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:吴再添小吃店(18元) / dinner:厦门园林博览苑附近餐厅(180元)

### 预算摘要

- total=1760 | attractions=180 | hotels=900 | meals=480 | transport=200

## 9. v3_harder_eval_000063

### 用户请求

- 城市/日期：深圳 | 2026-05-06 -> 2026-05-10 | 5天
- 同行：{'adults': 2, 'children': 0, 'elders': 1, 'total': 3, 'companion_type': 'family_with_elders'}
- 交通/住宿：公共交通 / 舒适型酒店
- 预算：{'amount': 4700, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 负向约束：爬山 / 过长步行 / 太早起 / 太偏远的景点
- 饮食：想吃/偏好=少辣；避免=无
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-07 | dinner | 酒店晚餐 |
| 2026-05-08 | dinner | 酒店晚餐 |
| 2026-05-09 | dinner | 酒店晚餐 |
| 2026-05-10 | lunch | 酒店午餐 |
| 2026-05-10 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 辉少鱼籽鱼泡(联丰广场店) | food_diet | lunch/dinner | 186 | 少辣 |  |
| 2 | 爱辣无忧东北麻辣烫 | food_diet | lunch/dinner | 54 | 少辣 |  |
| 3 | 笨罗卜浏阳菜馆(龙华鹏润达店) | food_preference | lunch/dinner | 159 |  |  |
| 4 | 蘩楼(华强北总店) | food_preference | breakfast/lunch/dinner | 264 | 快餐 |  |
| 5 | 深圳市宝安区笨罗卜浏阳菜馆(梦想城店) | food_preference | lunch/dinner | 225 |  |  |
| 6 | 鸡叔·清远脆皮鸡火锅(华强北店) | food_preference | lunch/dinner | 195 |  |  |
| 7 | 鸡叔·清远脆皮鸡火锅(黄贝岭店) | food_preference | lunch/dinner | 255 |  |  |
| 8 | 鑫缘阁东北菜(沙井店) | food_companion | lunch/dinner | 150 | 家常菜 |  |
| 9 | 雪乡情东北菜(登良旗舰店) | food_companion | lunch/dinner | 177 | 家常菜 |  |
| 10 | 一品红川菜(皇岗分店) | food_companion | lunch/dinner | 273 | 家常菜 |  |
| 11 | 七月柿Farm House(深圳湾大地广场店) | food_companion | lunch/dinner | 372 | 家常菜 |  |
| 12 | 巴蜀风月(宝安店) | food_companion | lunch/dinner | 309 | 家常菜 |  |
| 13 | 龙帝桂林米粉 | food_companion | lunch/dinner | 57 | 清淡餐厅 |  |
| 14 | 程家逍遥镇胡辣汤(沙井和一二路店) | food_companion | lunch/dinner | 30 | 清淡餐厅 |  |
| 15 | 云妹福鼎肉片 | food_companion | lunch/dinner | 30 | 清淡餐厅 |  |
| 16 | 欧记大排档•江西景德菜(深圳首店) | food_budget | lunch/dinner | 285 | 本地菜 |  |
| 17 | 欧记大排档·江西景德菜(南山保利店) | food_budget | lunch/dinner | 264 | 本地菜 |  |
| 18 | 东江海鲜大排档.潮汕菜.砂锅粥 | food_budget | lunch/dinner | 264 | 本地菜/海鲜 |  |
| 19 | 欧记大排档·江西景德菜(罗湖东门町店) | food_budget | lunch/dinner | 288 | 本地菜 |  |
| 20 | 星店餐厅(凤凰城店) | food_budget | lunch/dinner | 144 | 特色餐厅 |  |
| 21 | 南门涮肉(深圳首店) | food_budget | lunch/dinner | 327 | 老字号 |  |
| 22 | 百草堂祖传凉茶铺 | food_budget | lunch/dinner | 84 | 老字号 |  |

### 模型输出相关天

#### D2 2026-05-07

- 描述：参观海上世界文化艺术中心，午餐在附近餐厅，晚餐在酒店。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：维也纳酒店(深圳公明天汇城店)
- 景点：海上世界文化艺术中心
- 餐饮：breakfast:酒店早餐(30元) / lunch:爱辣无忧东北麻辣烫(54元) / dinner:酒店晚餐(80元)

#### D3 2026-05-08

- 描述：参观深圳仙湖植物园，午餐在附近餐厅，晚餐在酒店。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：维也纳酒店(深圳公明天汇城店)
- 景点：深圳仙湖植物园
- 餐饮：breakfast:酒店早餐(30元) / lunch:蘩楼(华强北总店)(264元) / dinner:酒店晚餐(80元)

#### D4 2026-05-09

- 描述：参观莲花山公园，午餐在附近餐厅，晚餐在酒店。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：维也纳酒店(深圳公明天汇城店)
- 景点：莲花山公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:欧记大排档·江西景德菜(南山保利店)(88元) / dinner:酒店晚餐(80元)

#### D5 2026-05-10

- 描述：返程，早餐在酒店，午餐在酒店。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：None
- 景点：无
- 餐饮：breakfast:酒店早餐(30元) / lunch:酒店午餐(50元) / dinner:酒店晚餐(80元)

### 预算摘要

- total=2660 | attractions=180 | hotels=1800 | meals=480 | transport=200

## 10. v3_harder_eval_000075

### 用户请求

- 城市/日期：杭州 | 2025-05-04 -> 2025-05-08 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'solo'}
- 交通/住宿：公共交通 / 民宿
- 预算：{'amount': 2600, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：摄影 / 自然风光 / 城市漫步 / 本地菜
- 负向约束：密集行程 / 太偏远的景点 / 商业化打卡点
- 饮食：想吃/偏好=无；避免=无
- 自由文本：一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2025-05-08 | dinner | 无 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 传家(骆家庄西苑一区店) | food_diet | lunch/dinner | 80 | 本地菜 |  |
| 2 | 钱棠·萧山本帮菜(萧山机场大会展店) | food_diet | lunch/dinner | 106 | 本地菜 |  |
| 3 | 瓷·忆赣菜中心(杭州) | food_diet | lunch/dinner | 119 | 本地菜 |  |
| 4 | 山野之约·舌尖上的桐庐美食 | food_diet | lunch/dinner | 82 | 本地菜 |  |
| 5 | 赵府私厨·老杭帮菜(西湖老店) | food_diet | lunch/dinner | 69 | 本地菜 |  |
| 6 | 浩海火燒雲傣家菜(杭州湖滨in77店) | food_diet | lunch/dinner | 94 | 本地菜 |  |
| 7 | 赵府私厨·老杭帮菜(河坊街店) | food_diet | lunch/dinner | 66 | 本地菜 |  |
| 8 | 吴记餐厅·杭帮菜·私房菜(西湖湖滨店) | food_diet | lunch/dinner | 72 | 本地菜 |  |
| 9 | 肉本家·炭烤肉(杭州浙大总店) | food_preference | lunch/dinner | 106 | 老字号 |  |
| 10 | 老秦凉都黄牛肉馆(滨江总店) | food_preference | lunch/dinner | 78 | 老字号 |  |
| 11 | 知味观(湖滨总店) | food_preference | lunch/dinner | 68 | 老字号 |  |
| 12 | 柳来原味螺蛳粉(枫香路店) | food_base | breakfast/lunch/dinner | 31 | 小吃 |  |

### 模型输出相关天

#### D5 2025-05-08

- 描述：返程日，安排轻松的活动。
- 交通：公共交通 | accommodation=民宿
- 酒店：None
- 景点：稻乡漫步街
- 餐饮：breakfast:酒店早餐(30元) / lunch:柳来原味螺蛳粉(枫香路店)(31元) / dinner:无(0元)

### 预算摘要

- total=2070 | attractions=150 | hotels=1400 | meals=420 | transport=200

## 11. v3_harder_eval_000093

### 用户请求

- 城市/日期：贵阳 | 2026-05-07 -> 2026-05-11 | 5天
- 同行：{'adults': 2, 'children': 0, 'elders': 1, 'total': 3, 'companion_type': 'family_with_elders'}
- 交通/住宿：公共交通 / 舒适型酒店
- 预算：{'amount': 4300, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 负向约束：爬山 / 过长步行 / 太早起 / 太偏远的景点
- 饮食：想吃/偏好=少辣；避免=无
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-08 | dinner | 门黔树老贵阳家常菜(遵义路店) |
| 2026-05-10 | lunch | 门黔树老贵阳家常菜(遵义路店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 金顶山小耳朵清水烫(温馨小院店) | food_preference | lunch/dinner | 144 |  |  |
| 2 | 金顶山小耳朵清水烫(会展城店) | food_preference | lunch/dinner | 114 |  |  |
| 3 | 聚君缘烙锅 | food_preference | lunch/dinner | 159 |  |  |
| 4 | 黔渔翁豆花渎鱼(喷水池店) | food_preference | lunch/dinner | 165 |  |  |
| 5 | 大胖刘烙锅(煤矿村全国总店) | food_preference | lunch/dinner | 183 |  |  |
| 6 | 味香苑家常菜馆 | food_companion | lunch/dinner | 174 | 家常菜 |  |
| 7 | 树厨地道黔菜餐厅(青云市集店) | food_companion | lunch/dinner | 159 | 家常菜 |  |
| 8 | 小黔喜贵州家常菜(甲秀楼店) | food_companion | lunch/dinner | 210 | 家常菜 |  |
| 9 | 門黔樹老贵阳家常菜(遵义路店) | food_companion | lunch/dinner | 111 | 家常菜 |  |
| 10 | 茉莉家·家常菜 Home Cooking | food_companion | lunch/dinner | 234 | 家常菜 |  |
| 11 | 喜乐娃娃贵阳老素粉(绿苑店) | food_companion | lunch/dinner | 27 | 清淡餐厅 |  |
| 12 | 张家奇盘化红烧牛肉粉一分店 | food_companion | lunch/dinner | 39 | 清淡餐厅 |  |
| 13 | 重庆陈香火锅店(花溪花阁路店) | food_companion | lunch/dinner | 150 | 清淡餐厅 |  |
| 14 | 黔大叔大牌档(甲秀楼店) | food_budget | lunch/dinner | 180 | 本地菜 |  |
| 15 | 佳乡烟火 · 织金土烙锅(小十字店) | food_budget | lunch/dinner | 162 | 本地菜 |  |
| 16 | 好嘢·木槿树贵州菜(文创店) | food_budget | lunch/dinner | 192 | 本地菜 |  |
| 17 | 小平香辣老素粉(贵山苑B栋店) | food_budget | lunch/dinner | 36 | 老字号 |  |
| 18 | 老凯俚酸汤鱼(中天店) | food_budget | lunch/dinner | 219 | 本地菜/海鲜 |  |
| 19 | 赛维利亚中西餐厅(金阳店) | food_budget | lunch/dinner | 129 | 特色餐厅 |  |
| 20 | 一烙锅(友谊店) | food_budget | lunch/dinner | 156 | 特色餐厅 |  |
| 21 | 笔记安顺夺夺粉 | food_base | breakfast/lunch/dinner | 189 | 小吃 |  |
| 22 | 黔上姨孃老贵阳牛肉粉 | food_base | breakfast/lunch/dinner | 48 | 小吃 |  |

### 模型输出相关天

#### D2 2026-05-08

- 描述：参观历史文化景点，体验贵阳特色。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：夕宿·金融城盛佰嘉精品酒店(观山湖区会展城银行北街店)
- 景点：甲秀楼 / 贵州省博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:聚君缘烙锅(159元) / dinner:门黔树老贵阳家常菜(遵义路店)(111元)

#### D4 2026-05-10

- 描述：体验贵阳特色，享受美食。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：夕宿·金融城盛佰嘉精品酒店(观山湖区会展城银行北街店)
- 景点：贵州省地质博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:门黔树老贵阳家常菜(遵义路店)(111元) / dinner:赛维利亚中西餐厅(金阳店)(129元)

### 预算摘要

- total=2060 | attractions=180 | hotels=1200 | meals=480 | transport=200

## 12. v3_harder_eval_000103

### 用户请求

- 城市/日期：扬州 | 2026-05-05 -> 2026-05-09 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 2, 'total': 3, 'companion_type': 'family_with_elders'}
- 交通/住宿：公共交通 / 舒适型酒店
- 预算：{'amount': 4300, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 负向约束：爬山 / 过长步行 / 太早起 / 太偏远的景点
- 饮食：想吃/偏好=少辣；避免=无
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-09 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 肉夹馍酸辣粉 | food_diet | lunch/dinner | 180 | 少辣 |  |
| 2 | 多放孜然少放辣 | food_diet | lunch/dinner | 180 | 少辣 |  |
| 3 | 扬州院子·淮扬土菜庭院餐厅(大运河博物馆何园店) | food_preference | lunch/dinner | 372 |  |  |
| 4 | 大毛·淮扬菜(梅岭东路店) | food_preference | lunch/dinner | 255 |  |  |
| 5 | 大毛.淮扬菜(瘦西湖店) | food_preference | lunch/dinner | 228 |  |  |
| 6 | 打酱油百姓饭堂·淮扬菜(大运河博物馆总店顺达路) | food_preference | lunch/dinner | 195 |  |  |
| 7 | 打酱油百姓饭堂·淮扬菜(瘦西湖梅岭店) | food_preference | lunch/dinner | 210 |  |  |
| 8 | 市井川菜(东亚御景湾店) | food_companion | lunch/dinner | 216 | 家常菜 |  |
| 9 | 老土灶扬州民间淮扬菜(瘦西湖店) | food_companion | lunch/dinner | 198 | 家常菜 |  |
| 10 | 众顺和淮扬菜 | food_companion | lunch/dinner | 174 | 家常菜 |  |
| 11 | 李氏传家菜(兴城东路店) | food_companion | lunch/dinner | 210 | 家常菜 |  |
| 12 | 胖哥川菜馆(润扬广场3幢店) | food_companion | lunch/dinner | 192 | 家常菜 |  |
| 13 | 西北滋味源清真特色小厨 | food_companion | lunch/dinner | 144 | 清淡餐厅/清真/清真 |  |
| 14 | 邗江区祥来顺小馆餐饮店 | food_companion | lunch/dinner | 171 | 清淡餐厅/清真/清真 |  |
| 15 | 正悦清兰州牛肉面 | food_companion | lunch/dinner | 48 | 清淡餐厅/清真/清真 |  |
| 16 | 大毛.淮扬菜(何园店) | food_budget | lunch/dinner | 261 | 本地菜 |  |
| 17 | 东关街美食广场 | food_budget | lunch/dinner | 126 | 老字号 |  |
| 18 | 必香居茶社(兴城路店) | food_budget | lunch/dinner | 102 | 老字号 |  |
| 19 | 北柳酒肆(东关街店) | food_budget | lunch/dinner | 231 | 特色餐厅 |  |
| 20 | 大毛·淮扬菜(兴城东路店) | food_base | breakfast/lunch/dinner | 201 | 小吃 |  |

### 模型输出相关天

#### D5 2026-05-09

- 描述：返程，结束愉快的扬州之旅。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：None
- 景点：宋夹城考古遗址公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:扬州院子·淮扬土菜庭院餐厅(大运河博物馆何园店)(124元) / dinner:酒店晚餐(50元)

### 预算摘要

- total=2640 | attractions=360 | hotels=1600 | meals=480 | transport=200

## 13. v3_harder_eval_000107

### 用户请求

- 城市/日期：武汉 | 2025-05-04 -> 2025-05-08 | 5天
- 同行：{'adults': 2, 'children': 0, 'elders': 0, 'total': 2, 'companion_type': 'couple'}
- 交通/住宿：公共交通 / 民宿
- 预算：{'amount': 4800, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'soft'}
- 正向偏好：小众展馆 / 咖啡 / 艺术 / 城市漫步 / 特色餐厅
- 负向约束：过度商业化景点 / 跟团游 / 购物团
- 饮食：想吃/偏好=无；避免=无
- 自由文本：两个人想要小众、有审美的路线，喜欢展馆、咖啡和特色餐厅，但避开过度商业化景点、跟团游和购物团。预算不需要极省，要符合舒适体验。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2025-05-04 | dinner | 舂Chong coffee |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 刘聋子牛肉粉馆(汉阳龙兴东街店) | food_preference | lunch/dinner | 54 | 老字号 |  |
| 2 | 山饭子特色餐厅(汉阳国博新城店) | food_preference | lunch/dinner | 172 | 特色餐厅 |  |
| 3 | 夏氏砂锅(总店) | food_preference | lunch/dinner | 224 | 老字号 |  |
| 4 | 金马门国际美食百汇(珞喻路店) | food_preference | lunch/dinner | 320 | 老字号 |  |
| 5 | 余艳梅拌面世家 | food_preference | lunch/dinner | 44 | 老字号 |  |
| 6 | 舂Chong coffee | food_preference | breakfast/lunch/dinner | 82 | 咖啡 |  |
| 7 | 星巴克(武汉融科天城店) | food_preference | breakfast/lunch/dinner | 60 | 咖啡 |  |
| 8 | 小民大排档(江汉路店) | food_preference | lunch/dinner | 142 | 特色餐厅 |  |
| 9 | 财大小吃街(政院小区店) | food_base | breakfast/lunch/dinner | 64 | 小吃 |  |
| 10 | 刘聋子牛肉粉馆(汉阳玫瑰街店) | food_base | breakfast/lunch/dinner | 54 | 小吃/快餐 |  |
| 11 | 刘聋子牛肉粉馆(光谷新竹路店) | food_base | breakfast/lunch/dinner | 54 | 小吃 |  |

### 模型输出相关天

#### D1 2025-05-04

- 描述：抵达武汉，入住速8主题公寓(湖北大学店)，休息调整。
- 交通：公共交通 | accommodation=民宿
- 酒店：速8主题公寓(湖北大学店)
- 景点：湖北省博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:刘聋子牛肉粉馆(汉阳龙兴东街店)(54元) / dinner:舂Chong coffee(82元)

### 预算摘要

- total=2060 | attractions=210 | hotels=1200 | meals=480 | transport=200

## 14. v3_harder_eval_000125

### 用户请求

- 城市/日期：贵阳 | 2026-05-06 -> 2026-05-10 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'solo'}
- 交通/住宿：公共交通 / 民宿
- 预算：{'amount': 2300, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：摄影 / 自然风光 / 城市漫步 / 本地菜
- 负向约束：密集行程 / 太偏远的景点 / 商业化打卡点
- 饮食：想吃/偏好=无；避免=无
- 自由文本：一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-10 | dinner | 如愿青年旅舍(贵阳北站店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 黔大叔大牌档(甲秀楼店) | food_diet | lunch/dinner | 60 | 本地菜 |  |
| 2 | 佳乡烟火 · 织金土烙锅(小十字店) | food_diet | lunch/dinner | 54 | 本地菜 |  |
| 3 | 好嘢·木槿树贵州菜(文创店) | food_diet | lunch/dinner | 64 | 本地菜 |  |
| 4 | 树厨地道黔菜餐厅(青云市集店) | food_diet | lunch/dinner | 53 | 本地菜 |  |
| 5 | 老凯俚酸汤鱼(中天店) | food_diet | lunch/dinner | 73 | 本地菜/海鲜 |  |
| 6 | 滋粥楼·顺德菜(金融城店) | food_diet | lunch/dinner | 90 | 本地菜 |  |
| 7 | 小平香辣老素粉(贵山苑B栋店) | food_preference | lunch/dinner | 12 | 老字号 |  |
| 8 | 新大新豆米火锅1993(南国花锦店) | food_preference | lunch/dinner | 56 | 老字号 |  |
| 9 | 私淑蚝鲜生·鸡汤生蚝烙锅(友谊路店) | food_preference | lunch/dinner | 81 | 老字号 |  |
| 10 | 赛维利亚中西餐厅(金阳店) | food_budget | lunch/dinner | 43 | 特色餐厅 |  |
| 11 | 一烙锅(友谊店) | food_budget | lunch/dinner | 52 | 特色餐厅 |  |
| 12 | 金顶山小耳朵清水烫(温馨小院店) | food_base | breakfast/lunch/dinner | 48 | 小吃 |  |
| 13 | 笔记安顺夺夺粉 | food_base | breakfast/lunch/dinner | 63 | 小吃 |  |
| 14 | 黔上姨孃老贵阳牛肉粉 | food_base | breakfast/lunch/dinner | 16 | 小吃 |  |

### 模型输出相关天

#### D5 2026-05-10

- 描述：最后一天参观息烽集中营革命历史纪念馆，结束愉快的旅行。
- 交通：公共交通 | accommodation=民宿
- 酒店：None
- 景点：息烽集中营革命历史纪念馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:老凯俚酸汤鱼(中天店)(73元) / dinner:如愿青年旅舍(贵阳北站店)(300元)

### 预算摘要

- total=2060 | attractions=240 | hotels=1200 | meals=480 | transport=200

## 15. v3_harder_eval_000128

### 用户请求

- 城市/日期：济南 | 2026-05-08 -> 2026-05-10 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 4100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-08 | dinner | 秀宴•齐鲁文化美食剧场(高新店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 箪食巷私房菜(奥体店) | food_preference | lunch/dinner | 414 | 本地菜 |  |
| 2 | 穆得老周家牛肉烧饼 | food_preference | breakfast/lunch/dinner | 108 | 小吃/清真/清真 |  |
| 3 | 魏斯理汉堡(绿地国金天地店) | food_preference | breakfast/lunch/dinner | 120 | 小吃/快餐 |  |
| 4 | 达美乐比萨(老商埠店) | food_preference | breakfast/lunch/dinner | 150 | 小吃/快餐 |  |
| 5 | 渔家鲜·海鲜小炒·切馅煎包 | food_preference | breakfast/lunch/dinner | 207 | 小吃/海鲜 |  |
| 6 | 笨鸡小跑·临沂炒鸡(印象济南店) | food_preference | lunch/dinner | 228 | 本地菜 |  |
| 7 | 鲁西南老厨子(千佛山店) | food_preference | lunch/dinner | 237 | 本地菜 |  |
| 8 | 鲁西南老厨子(经六路延长线) | food_preference | lunch/dinner | 186 | 本地菜 |  |
| 9 | 向民炒鸡老店(济南店) | food_base | lunch/dinner | 267 | 老字号 |  |
| 10 | 鑫龙火锅城(环山路店) | food_base | lunch/dinner | 246 | 老字号 |  |

### 模型输出相关天

#### D1 2026-05-08

- 描述：第一天游览大明湖景区和趵突泉景区，晚上在秀宴•齐鲁文化美食剧场用餐。
- 交通：打车 | accommodation=高端酒店
- 酒店：卓瑞·曼兹酒店
- 景点：大明湖景区 / 趵突泉景区
- 餐饮：breakfast:酒店早餐(30元) / lunch:穆得老周家牛肉烧饼(108元) / dinner:秀宴•齐鲁文化美食剧场(高新店)(276元)

### 预算摘要

- total=3500 | attractions=240 | hotels=2250 | meals=810 | transport=300

## 16. v3_harder_eval_000131

### 用户请求

- 城市/日期：上海 | 2026-05-06 -> 2026-05-09 | 4天
- 同行：{'adults': 2, 'children': 0, 'elders': 0, 'total': 2, 'companion_type': 'couple'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 10900, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'premium', 'strictness': 'soft'}
- 正向偏好：高端酒店 / 艺术 / 特色餐厅 / 城市地标 / 休闲慢游
- 负向约束：购物团 / 打卡式景点 / 过度省钱
- 饮食：想吃/偏好=无；避免=无
- 自由文本：两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-09 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 南门涮肉(上海一店) | food_preference | lunch/dinner | 246 | 老字号 |  |
| 2 | 紫阳村地道家常菜(川沙店) | food_preference | lunch/dinner | 196 | 特色餐厅/家常菜 |  |
| 3 | 红子鸡凤凰楼 | food_preference | lunch/dinner | 274 | 老字号 |  |
| 4 | 沪西老弄堂面馆(广东路店) | food_preference | lunch/dinner | 88 | 老字号 |  |
| 5 | 莱莱小笼 | food_preference | lunch/dinner | 134 | 老字号 |  |
| 6 | 沈大成(南京东路店) | food_preference | lunch/dinner | 86 | 老字号 |  |
| 7 | 贯贯吉·清真餐厅(浙江中路店) | food_preference | lunch/dinner | 210 | 特色餐厅/清真/清真 |  |
| 8 | 3号仓库·餐厅(上海首店) | food_preference | lunch/dinner | 316 | 特色餐厅 |  |
| 9 | 宫宴(上海店) | food_budget | lunch/dinner | 946 | 精致餐厅 |  |
| 10 | Solo(衡山路店) | food_budget | lunch/dinner | 338 | 黑珍珠 |  |
| 11 | 浦江家宴 | food_budget | lunch/dinner | 512 | 精致餐厅 |  |
| 12 | 醉辉皇海鲜皇宫(118店) | food_budget | lunch/dinner | 378 | 精致餐厅/海鲜 |  |
| 13 | 上海滩餐厅(BFC外滩金融中心店) | food_budget | lunch/dinner | 1102 | 黑珍珠 |  |
| 14 | 席作·福建会馆(新天地时尚一期店) | food_budget | lunch/dinner | 962 | 黑珍珠 |  |
| 15 | 逸道(益丰·外滩源店) | food_budget | lunch/dinner | 1032 | 黑珍珠 |  |
| 16 | 东方景宴 | food_budget | lunch/dinner | 1122 | 黑珍珠 |  |
| 17 | 海福多共富海鲜面馆 | food_base | breakfast/lunch/dinner | 448 | 小吃/海鲜 |  |
| 18 | 农家菜老大(松江店) | food_base | lunch/dinner | 186 | 本地菜 |  |
| 19 | 农家菜老大(九亭店) | food_base | lunch/dinner | 230 | 本地菜 |  |
| 20 | 外滩家宴·上海菜(外滩豫园店) | food_base | lunch/dinner | 270 | 本地菜 |  |
| 21 | 浩海火烧云傣家菜(新天地广场店) | food_base | lunch/dinner | 218 | 本地菜 |  |
| 22 | 欧记大排档·景德菜(上海首店) | food_base | lunch/dinner | 188 | 本地菜 |  |

### 模型输出相关天

#### D4 2026-05-09

- 描述：参观东方明珠广播电视塔和上海世纪公园，享受特色餐厅午餐。
- 交通：打车 | accommodation=高端酒店
- 酒店：璞爵国际酒店(上海松江新桥店)
- 景点：东方明珠广播电视塔 / 上海世纪公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:浦江家宴(512元) / dinner:酒店晚餐(300元)

### 预算摘要

- total=7440 | attractions=1800 | hotels=3400 | meals=1440 | transport=800

## 17. v3_harder_eval_000134

### 用户请求

- 城市/日期：北京 | 2026-05-07 -> 2026-05-09 | 3天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'business'}
- 交通/住宿：打车 / 舒适型酒店
- 预算：{'amount': 2400, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 特色餐厅 / 自由活动多 / 博物馆
- 负向约束：太早起 / 过长步行 / 密集行程
- 饮食：想吃/偏好=无；避免=无
- 自由文本：出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-07 | dinner | 酒店晚餐 |
| 2026-05-08 | dinner | 酒店晚餐 |
| 2026-05-09 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 胡大饭馆(簋街三店) | food_preference | lunch/dinner | 137 | 老字号 |  |
| 2 | 牛街清真满恒記(平安里西大街店) | food_preference | lunch/dinner | 75 | 特色餐厅/清真/清真 |  |
| 3 | 宫宴(北京店) | food_preference | lunch/dinner | 543 | 特色餐厅 |  |
| 4 | 蘇锦宴·淮扬菜·大班徽菜·果木烤鸭(定慧寺店) | food_preference | lunch/dinner | 162 | 特色餐厅 |  |
| 5 | 南门涮肉(后海店) | food_preference | lunch/dinner | 105 | 老字号 |  |
| 6 | 胡大饭馆24h(簋街总店) | food_preference | lunch/dinner | 152 | 老字号 |  |
| 7 | 南门涮肉(东单店) | food_preference | lunch/dinner | 135 | 老字号 |  |
| 8 | ZENG餐厅剧场店(前门店) | food_preference | lunch/dinner | 88 | 特色餐厅 |  |
| 9 | 四季民福烤鸭店(双井店) | food_companion | lunch/dinner | 186 |  |  |
| 10 | 北京宴(丰台总店) | food_companion | lunch/dinner | 346 |  |  |
| 11 | 四季民福烤鸭店(望京旺角店) | food_companion | lunch/dinner | 141 |  |  |
| 12 | 北京凯瑞御仙都皇家菜博物馆 | food_companion | lunch/dinner | 586 |  |  |
| 13 | 丹江渔村·小院(四季御园店) | food_companion | lunch/dinner | 204 |  |  |
| 14 | 高端商务茶歇冷餐自助餐 | food_companion | lunch/dinner | 97 | 高端餐厅 |  |
| 15 | 大兴高端智造产业园餐厅 | food_companion | lunch/dinner | 60 | 高端餐厅 |  |
| 16 | 鮨丼屋高端日料三文鱼(月恒正大新生活广场店) | food_companion | lunch/dinner | 60 | 高端餐厅 |  |
| 17 | 紫光园·烤鸭·北京菜(前门大栅栏店) | food_base | lunch/dinner | 60 | 本地菜 |  |
| 18 | 鸽子窝(四季青店) | food_base | lunch/dinner | 107 | 本地菜 |  |
| 19 | 浩海火烧云傣家菜(京广店) | food_base | lunch/dinner | 105 | 本地菜 |  |
| 20 | 浩海火烧云傣家菜(东安市场店) | food_base | lunch/dinner | 100 | 本地菜 |  |

### 模型输出相关天

#### D1 2026-05-07

- 描述：第一天游览天坛公园和故宫博物院，晚上在胡大饭馆享用午餐。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：时光漫步酒店(北京东直门北桥地坛公园店)
- 景点：天坛公园 / 故宫博物院
- 餐饮：breakfast:酒店早餐(30元) / lunch:胡大饭馆(簋街三店)(137元) / dinner:酒店晚餐(50元)

#### D2 2026-05-08

- 描述：游览颐和园和什刹海，晚上在南门涮肉享用晚餐。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：时光漫步酒店(北京东直门北桥地坛公园店)
- 景点：颐和园 / 什刹海
- 餐饮：breakfast:酒店早餐(30元) / lunch:南门涮肉(后海店)(105元) / dinner:酒店晚餐(50元)

#### D3 2026-05-09

- 描述：游览天安门广场和中国国家博物馆，晚上在紫光园享用晚餐。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：None
- 景点：天安门广场 / 中国国家博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:紫光园·烤鸭·北京菜(前门大栅栏店)(60元) / dinner:酒店晚餐(50元)

### 预算摘要

- total=2440 | attractions=190 | hotels=1500 | meals=450 | transport=300

## 18. v3_harder_eval_000139

### 用户请求

- 城市/日期：大理 | 2026-06-18 -> 2026-06-21 | 4天
- 同行：{'adults': 2, 'children': 0, 'elders': 2, 'total': 4, 'companion_type': 'family_with_elders'}
- 交通/住宿：打车 / 亲子酒店
- 预算：{'amount': 10800, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'soft'}
- 正向偏好：亲子 / 老人友好 / 博物馆 / 城市公园 / 特色餐厅
- 负向约束：爬山 / 夜间长距离移动 / 排队太久 / 重口味餐厅
- 饮食：想吃/偏好=清淡饮食；避免=无
- 自由文本：老人和小朋友一起出行，要求清淡饮食，路线要照顾体力。不要爬山、夜间长距离移动、排队太久和重口味餐厅。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-19 | dinner | 步云山·大理白族特色餐厅 |
| 2026-06-20 | lunch | 随园食单(善德居店) |
| 2026-06-21 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 山喃集现炒云南菜·苍山露台花园餐厅(大理古城店) | food_preference | lunch/dinner | 284 | 家常菜/清真/清真 |  |
| 2 | 桃红小馆·特色云南菜·庭院花园餐厅 | food_preference | lunch/dinner | 264 | 特色餐厅 |  |
| 3 | 沐府私厨·老大理菜头牌·野生菌汤锅(人民路店) | food_preference | lunch/dinner | 332 | 老字号 |  |
| 4 | 翠麓野白族庭院私房菜 | food_preference | lunch/dinner | 260 | 特色餐厅 |  |
| 5 | 海东茄子烧烤(古城店) | food_preference | lunch/dinner | 260 | 老字号 |  |
| 6 | 金傣苑现炒云南菜·手抓饭(洋人街店) | food_preference | lunch/dinner | 236 | 家常菜/清真/清真 |  |
| 7 | 一步之肴·精选大理白族特色餐厅(三圣岛店) | food_preference | breakfast/lunch/dinner | 296 | 特色餐厅/咖啡 |  |
| 8 | 梅子井酒家 | food_preference | lunch/dinner | 324 | 特色餐厅 |  |
| 9 | 巍山家菜馆 | food_companion | lunch/dinner | 240 | 家常菜 |  |
| 10 | 茄子恰恰·脆皮小麻鸭(大理泰业店) | food_companion | lunch/dinner | 200 | 家常菜 |  |
| 11 | 安贵非遗海稍鱼(宾川店) | food_companion | lunch/dinner | 216 | 家常菜 |  |
| 12 | 隨园食单(善德居店) | food_companion | lunch/dinner | 260 | 清淡餐厅 |  |
| 13 | 南诏村·现炒云南菜 | food_base | lunch/dinner | 224 | 本地菜 |  |
| 14 | 岛七白族人家火烧猪私房菜 | food_base | lunch/dinner | 260 | 本地菜 |  |
| 15 | 老爷爷的手工鲜花饼(总店) | food_base | breakfast/lunch/dinner | 120 | 小吃 |  |

### 模型输出相关天

#### D2 2026-06-19

- 描述：参观崇圣寺三塔文化旅游区和洱海公园，晚上在洱海生态廊道散步。
- 交通：打车 | accommodation=亲子酒店
- 酒店：一山精品·亲子度假酒店(大理古城苍洱大道店)
- 景点：崇圣寺三塔文化旅游区 / 洱海公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:南诏村·现炒云南菜(224元) / dinner:步云山·大理白族特色餐厅(332元)

#### D3 2026-06-20

- 描述：参观喜洲古镇和木莲公园，晚上在木莲公园附近散步。
- 交通：打车 | accommodation=亲子酒店
- 酒店：一山精品·亲子度假酒店(大理古城苍洱大道店)
- 景点：喜洲古镇 / 木莲公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:随园食单(善德居店)(260元) / dinner:老爷爷的手工鲜花饼(总店)(120元)

#### D4 2026-06-21

- 描述：参观双廊古镇和洱海生态廊道，晚上返回酒店。
- 交通：打车 | accommodation=亲子酒店
- 酒店：None
- 景点：双廊古镇 / 洱海生态廊道
- 餐饮：breakfast:酒店早餐(30元) / lunch:翠麓野白族庭院私房菜(260元) / dinner:酒店晚餐(284元)

### 预算摘要

- total=5263 | attractions=225 | hotels=3600 | meals=1008 | transport=400

## 19. v3_harder_eval_000140

### 用户请求

- 城市/日期：杭州 | 2026-06-03 -> 2026-06-07 | 5天
- 同行：{'adults': 2, 'children': 1, 'elders': 2, 'total': 5, 'companion_type': 'family_mixed'}
- 交通/住宿：打车 / 舒适型酒店
- 预算：{'amount': 11100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：亲子 / 老人友好 / 历史文化 / 城市公园 / 本地美食
- 负向约束：爬山 / 过长步行 / 长时间排队 / 高价餐厅
- 饮食：想吃/偏好=清淡饮食；避免=无
- 自由文本：三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-07 | lunch | 心芝麻开门亲子乐园(东兴天地店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 入江南·金奖杭帮菜·浙江菜(虎跑店) | food_preference | lunch/dinner | 540 | 家常菜 |  |
| 2 | 山野之约·舌尖上的桐庐美食 | food_preference | lunch/dinner | 410 | 家常菜 |  |
| 3 | 老姑东北人(立涛园店) | food_preference | lunch/dinner | 390 | 家常菜 |  |
| 4 | 黄龙海鲜大排档(杭州总店) | food_preference | lunch/dinner | 800 | 海鲜 |  |
| 5 | 钱棠·萧山本帮菜(萧山机场大会展店) | food_preference | lunch/dinner | 530 |  |  |
| 6 | 晚酒·阿英川菜馆(一店) | food_preference | lunch/dinner | 410 | 家常菜 |  |
| 7 | 中国杭帮菜博物馆(虎玉路店) | food_preference | lunch/dinner | 675 | 家常菜 |  |
| 8 | 印湖杭味·创意杭帮菜(西湖店) | food_preference | lunch/dinner | 370 | 夜市 |  |
| 9 | 肉本家·炭烤肉(杭州浙大总店) | food_base | lunch/dinner | 530 | 老字号 |  |
| 10 | 老秦凉都黄牛肉馆(滨江总店) | food_base | lunch/dinner | 390 | 老字号 |  |
| 11 | 柳来原味螺蛳粉(枫香路店) | food_base | breakfast/lunch/dinner | 155 | 小吃 |  |
| 12 | 传家(骆家庄西苑一区店) | food_base | lunch/dinner | 400 | 本地菜 |  |
| 13 | 瓷·忆赣菜中心(杭州) | food_base | lunch/dinner | 595 | 本地菜 |  |
| 14 | 赵府私厨·老杭帮菜(西湖老店) | food_base | lunch/dinner | 345 | 本地菜 |  |

### 模型输出相关天

#### D5 2026-06-07

- 描述：返程日，安排轻松的亲子活动。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：None
- 景点：拱墅运河体育公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:心芝麻开门亲子乐园(东兴天地店)(65元) / dinner:赵府私厨·老杭帮菜(西湖老店)(345元)

### 预算摘要

- total=4450 | attractions=180 | hotels=2000 | meals=1650 | transport=1000

## 20. v3_harder_eval_000146

### 用户请求

- 城市/日期：贵阳 | 2026-06-18 -> 2026-06-21 | 4天
- 同行：{'adults': 2, 'children': 2, 'elders': 0, 'total': 4, 'companion_type': 'family_with_children'}
- 交通/住宿：自驾 / 亲子酒店
- 预算：{'amount': 5300, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：亲子 / 动物园 / 海洋馆 / 城市公园 / 本地美食
- 负向约束：夜生活 / 太晚返程 / 过长步行 / 排队太久
- 饮食：想吃/偏好=无；避免=无
- 自由文本：带5岁孩子自驾，想安排亲子体验，但不要夜生活、太晚返程、过长步行或排队太久。预算是硬约束。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-21 | lunch | 门黔樹老贵阳家常菜(遵义路店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 金顶山小耳朵清水烫(温馨小院店) | food_preference | lunch/dinner | 192 |  |  |
| 2 | 金顶山小耳朵清水烫(会展城店) | food_preference | lunch/dinner | 152 |  |  |
| 3 | 味香苑家常菜馆 | food_preference | lunch/dinner | 232 | 家常菜 |  |
| 4 | 树厨地道黔菜餐厅(青云市集店) | food_preference | lunch/dinner | 212 | 家常菜 |  |
| 5 | 聚君缘烙锅 | food_preference | lunch/dinner | 212 |  |  |
| 6 | 黔渔翁豆花渎鱼(喷水池店) | food_preference | lunch/dinner | 220 |  |  |
| 7 | 大胖刘烙锅(煤矿村全国总店) | food_preference | lunch/dinner | 244 |  |  |
| 8 | 小黔喜贵州家常菜(甲秀楼店) | food_preference | lunch/dinner | 280 | 家常菜 |  |
| 9 | 門黔樹老贵阳家常菜(遵义路店) | food_companion | lunch/dinner | 148 | 家常菜 |  |
| 10 | 茉莉家·家常菜 Home Cooking | food_companion | lunch/dinner | 312 | 家常菜 |  |
| 11 | 新山返岛餐厅 | food_companion | lunch/dinner | 304 | 亲子餐厅 |  |
| 12 | SPACELAB失重餐厅(贵阳万象城店) | food_companion | lunch/dinner | 448 | 亲子餐厅 |  |
| 13 | 港岛记·香港茶餐厅(花溪清溪云廊店) | food_companion | breakfast/lunch/dinner | 132 | 快餐/亲子餐厅 |  |
| 14 | 黔大叔大牌档(甲秀楼店) | food_budget | lunch/dinner | 240 | 本地菜 |  |
| 15 | 佳乡烟火 · 织金土烙锅(小十字店) | food_budget | lunch/dinner | 216 | 本地菜 |  |
| 16 | 好嘢·木槿树贵州菜(文创店) | food_budget | lunch/dinner | 256 | 本地菜 |  |
| 17 | 小平香辣老素粉(贵山苑B栋店) | food_budget | lunch/dinner | 48 | 老字号 |  |
| 18 | 老凯俚酸汤鱼(中天店) | food_budget | lunch/dinner | 292 | 本地菜/海鲜 |  |
| 19 | 赛维利亚中西餐厅(金阳店) | food_budget | lunch/dinner | 172 | 特色餐厅 |  |
| 20 | 一烙锅(友谊店) | food_budget | lunch/dinner | 208 | 特色餐厅 |  |
| 21 | 笔记安顺夺夺粉 | food_base | breakfast/lunch/dinner | 252 | 小吃 |  |
| 22 | 黔上姨孃老贵阳牛肉粉 | food_base | breakfast/lunch/dinner | 64 | 小吃 |  |

### 模型输出相关天

#### D4 2026-06-21

- 描述：参观黔灵山动物园-贵阳大熊猫馆和返程
- 交通：自驾 | accommodation=无住宿
- 酒店：None
- 景点：黔灵山动物园-贵阳大熊猫馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:门黔樹老贵阳家常菜(遵义路店)(37元) / dinner:港岛记·香港茶餐厅(花溪清溪云廊店)(33元)

### 预算摘要

- total=2490 | attractions=240 | hotels=1500 | meals=450 | transport=200

## 21. v3_harder_eval_000161

### 用户请求

- 城市/日期：杭州 | 2026-04-04 -> 2026-04-07 | 4天
- 同行：{'adults': 2, 'children': 0, 'elders': 0, 'total': 2, 'companion_type': 'couple'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 9600, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'premium', 'strictness': 'soft'}
- 正向偏好：高端酒店 / 艺术 / 特色餐厅 / 城市地标 / 休闲慢游
- 负向约束：购物团 / 打卡式景点 / 过度省钱
- 饮食：想吃/偏好=无；避免=无
- 自由文本：两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-04-07 | dinner | 无 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 肉本家·炭烤肉(杭州浙大总店) | food_preference | lunch/dinner | 212 | 老字号 |  |
| 2 | 老秦凉都黄牛肉馆(滨江总店) | food_preference | lunch/dinner | 156 | 老字号 |  |
| 3 | 知味观(湖滨总店) | food_preference | lunch/dinner | 136 | 老字号 |  |
| 4 | 杭州酒家(延安路店) | food_preference | lunch/dinner | 154 | 老字号 |  |
| 5 | 乔村二十八道(钱江世纪城店) | food_preference | lunch/dinner | 280 | 老字号 |  |
| 6 | 李白图书馆餐厅(西溪湿地店) | food_preference | lunch/dinner | 224 | 特色餐厅 |  |
| 7 | 李白图书馆餐厅(西湖大学店) | food_preference | lunch/dinner | 224 | 特色餐厅 |  |
| 8 | 李白图书馆餐厅(白洋桥店) | food_preference | lunch/dinner | 260 | 特色餐厅 |  |
| 9 | 杨记肴·精致浙菜(东站店) | food_budget | lunch/dinner | 300 | 精致餐厅 |  |
| 10 | 龙井御庄·精致江南菜(西湖景区店) | food_budget | lunch/dinner | 736 | 精致餐厅 |  |
| 11 | 杨记肴·精致浙菜(西湖文化广场店) | food_budget | lunch/dinner | 194 | 精致餐厅 |  |
| 12 | 杨记肴.精致浙菜(丰收时代店) | food_budget | lunch/dinner | 184 | 精致餐厅 |  |
| 13 | 桂语山房(满觉陇店) | food_budget | lunch/dinner | 1214 | 黑珍珠 |  |
| 14 | 杨记肴•精致浙菜(闸弄口黑金店) | food_budget | lunch/dinner | 300 | 精致餐厅 |  |
| 15 | 青岚(杨公堤店) | food_budget | lunch/dinner | 1282 | 黑珍珠 |  |
| 16 | 暗香·Wild Yeast | food_budget | lunch/dinner | 1828 | 黑珍珠 |  |
| 17 | 柳来原味螺蛳粉(枫香路店) | food_base | breakfast/lunch/dinner | 62 | 小吃 |  |
| 18 | 传家(骆家庄西苑一区店) | food_base | lunch/dinner | 160 | 本地菜 |  |
| 19 | 钱棠·萧山本帮菜(萧山机场大会展店) | food_base | lunch/dinner | 212 | 本地菜 |  |
| 20 | 瓷·忆赣菜中心(杭州) | food_base | lunch/dinner | 238 | 本地菜 |  |
| 21 | 山野之约·舌尖上的桐庐美食 | food_base | lunch/dinner | 164 | 本地菜 |  |
| 22 | 赵府私厨·老杭帮菜(西湖老店) | food_base | lunch/dinner | 138 | 本地菜 |  |

### 模型输出相关天

#### D4 2026-04-07

- 描述：游览城市阳台，返回。
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：城市阳台
- 餐饮：breakfast:酒店早餐(30元) / lunch:杨记肴.精致浙菜(丰收时代店)(184元) / dinner:无(0元)

### 预算摘要

- total=6820 | attractions=180 | hotels=4200 | meals=1440 | transport=800

## 22. v3_harder_eval_000164

### 用户请求

- 城市/日期：三亚 | 2025-11-05 -> 2025-11-07 | 3天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'business'}
- 交通/住宿：打车 / 舒适型酒店
- 预算：{'amount': 1800, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 特色餐厅 / 自由活动多 / 博物馆
- 负向约束：太早起 / 过长步行 / 密集行程
- 饮食：想吃/偏好=无；避免=无
- 自由文本：出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2025-11-07 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 创味·民间海南菜·海鲜(林旺店) | food_preference | lunch/dinner | 96 | 老字号/海鲜 |  |
| 2 | 椰小鸡·椰子鸡(大东海银泰店) | food_preference | lunch/dinner | 110 | 特色餐厅 |  |
| 3 | 小海鲜渔民排档·农家海南菜 | food_preference | lunch/dinner | 81 | 特色餐厅/海鲜 |  |
| 4 | 椰小鸡·椰子鸡(海天盛宴总店) | food_preference | lunch/dinner | 110 | 特色餐厅 |  |
| 5 | 不仔客海鲜270度海景餐厅 | food_preference | lunch/dinner | 134 | 特色餐厅/海鲜 |  |
| 6 | 小海豚连锁海鲜餐厅(海棠湾店) | food_preference | lunch/dinner | 111 | 特色餐厅/海鲜 |  |
| 7 | 南门涮肉(三亚店) | food_preference | lunch/dinner | 110 | 老字号 |  |
| 8 | 东海龙宫(大东海店) | food_preference | lunch/dinner | 160 | 老字号/海鲜 |  |
| 9 | 黎想•海南黎族菜(海棠湾店) | food_companion | lunch/dinner | 86 |  |  |
| 10 | 京禧1981.荔枝木烤鸭(大东海店) | food_companion | lunch/dinner | 111 |  |  |
| 11 | 黎想·传承黎族菜·海鲜·宴会厅(南山店) | food_companion | lunch/dinner | 67 | 海鲜 |  |
| 12 | 三亚海棠湾童景餐厅(青塘村) | food_companion | lunch/dinner | 129 |  |  |
| 13 | 麒麟湘粤楼 | food_companion | lunch/dinner | 74 |  |  |
| 14 | 鲜悦鲜高端刺身三文鱼 | food_companion | lunch/dinner | 87 | 高端餐厅 |  |
| 15 | 南海黎村·海南民族菜·海景餐厅(椰梦长廊店) | food_base | lunch/dinner | 100 | 本地菜 |  |
| 16 | 疍家佬味道·海南船家菜(亚龙湾店) | food_base | lunch/dinner | 97 | 本地菜 |  |
| 17 | 创味·民间海南菜(南山店) | food_base | lunch/dinner | 72 | 本地菜 |  |
| 18 | 创味·民间海南菜(藤桥·免税城店) | food_base | lunch/dinner | 84 | 本地菜 |  |

### 模型输出相关天

#### D3 2025-11-07

- 描述：上午参观南山大小洞天旅游区，下午返回酒店休息，晚上在酒店附近用餐。
- 交通：打车 | accommodation=舒适型酒店
- 酒店：如家酒店(三亚千古情海旅免税城店)
- 景点：南山大小洞天旅游区
- 餐饮：breakfast:酒店早餐(30元) / lunch:小海豚连锁海鲜餐厅(海棠湾店)(111元) / dinner:酒店晚餐(50元)

### 预算摘要

- total=2420 | attractions=240 | hotels=1500 | meals=480 | transport=200

## 23. v3_harder_eval_000188

### 用户请求

- 城市/日期：泉州 | 2026-07-03 -> 2026-07-05 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5600, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-07-05 | dinner | 港湾宾馆(南山中路店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 林松喜·姜母鸭·泉州菜 | food_preference | lunch/dinner | 264 | 本地菜 |  |
| 2 | 荔枝苑酒家 | food_preference | lunch/dinner | 237 | 本地菜 |  |
| 3 | 临家闽南菜(泉州店) | food_preference | lunch/dinner | 330 | 本地菜 |  |
| 4 | 斯丹姜母鸭(泉州总店) | food_preference | lunch/dinner | 231 | 特色餐厅/清真/清真 |  |
| 5 | 水门国仔面线糊 | food_preference | breakfast/lunch/dinner | 81 | 小吃 |  |
| 6 | 侯阿婆肉粽(东街总店) | food_preference | breakfast/lunch/dinner | 57 | 小吃 |  |
| 7 | 圆宝台湾小吃(迎津街店) | food_preference | breakfast/lunch/dinner | 84 | 小吃 |  |
| 8 | 阿姨鸡架(西街店) | food_preference | breakfast/lunch/dinner | 66 | 小吃 |  |
| 9 | 鲤酒华宴(环球城店) | food_base | lunch/dinner | 258 | 老字号 |  |
| 10 | 张林远华饭店 | food_base | lunch/dinner | 264 | 老字号 |  |
| 11 | 张林阿山姜母鸭(泉州新华北路店) | food_base | lunch/dinner | 231 | 老字号 |  |

### 模型输出相关天

#### D3 2026-07-05

- 描述：返程
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：西湖公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:水门国仔面线糊(81元) / dinner:港湾宾馆(南山中路店)(270元)

### 预算摘要

- total=3585 | attractions=240 | hotels=2250 | meals=795 | transport=300

## 24. v3_harder_eval_000193

### 用户请求

- 城市/日期：厦门 | 2026-05-07 -> 2026-05-11 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 2, 'total': 3, 'companion_type': 'family_with_elders'}
- 交通/住宿：公共交通 / 舒适型酒店
- 预算：{'amount': 5000, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 负向约束：爬山 / 过长步行 / 太早起 / 太偏远的景点
- 饮食：想吃/偏好=少辣；避免=无
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-11 | dinner | 无 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 醉壹号海鲜大排档·老厦门特色菜(厦门美食地标店) | food_preference | lunch/dinner | 285 | 海鲜 |  |
| 2 | 金家港海鲜大排档(中山路店) | food_preference | lunch/dinner | 273 | 海鲜 |  |
| 3 | 妞妞餐厅老厦门特色菜 | food_preference | lunch/dinner | 228 |  |  |
| 4 | 宴遇·福建荟馆(新景中心店) | food_preference | lunch/dinner | 1023 |  |  |
| 5 | 津品味(厦门集美区) | food_preference | lunch/dinner | 72 |  |  |
| 6 | 闹两川·老牌川菜馆(东渡店) | food_companion | lunch/dinner | 240 | 家常菜 |  |
| 7 | 草莓夫妇丨厦门菜(厦大沙坡尾店) | food_companion | lunch/dinner | 264 | 家常菜 |  |
| 8 | 闹两川.老牌川菜(同安朱子良库店) | food_companion | lunch/dinner | 150 | 家常菜 |  |
| 9 | 南山客家 | food_companion | lunch/dinner | 195 | 家常菜 |  |
| 10 | 九道菜有鸡鱼头 | food_companion | lunch/dinner | 231 | 家常菜 |  |
| 11 | 香客来砂锅小炒店(山海花园店) | food_companion | lunch/dinner | 54 | 清淡餐厅 |  |
| 12 | 橙大嘴炖汤(实验小学店) | food_companion | lunch/dinner | 144 | 清淡餐厅 |  |
| 13 | 兰記重庆小面 | food_companion | lunch/dinner | 33 | 清淡餐厅 |  |
| 14 | 好食来大排档(32年美食航标店) | food_budget | lunch/dinner | 285 | 老字号 |  |
| 15 | 相约厦门平价海鲜城(八市美食地标店) | food_budget | lunch/dinner | 117 | 老字号/海鲜 |  |
| 16 | 临家闽南菜(环岛路店) | food_budget | lunch/dinner | 375 | 本地菜 |  |
| 17 | 鑫坞堂 海鲜热炒(中山路总店) | food_budget | lunch/dinner | 207 | 本地菜/海鲜 |  |
| 18 | 鑫草美夫妻厦门菜(厦大白城店) | food_budget | lunch/dinner | 195 | 本地菜 |  |
| 19 | 草莓夫妇丨厦门菜(黄厝店) | food_budget | lunch/dinner | 315 | 本地菜 |  |

### 模型输出相关天

#### D5 2026-05-11

- 描述：返程，结束愉快的厦门之旅。
- 交通：公共交通 | accommodation=舒适型酒店
- 酒店：None
- 景点：厦门园林植物园
- 餐饮：breakfast:酒店早餐(30元) / lunch:相约厦门平价海鲜城(八市美食地标店)(117元) / dinner:无(0元)

### 预算摘要

- total=3720 | attractions=180 | hotels=1800 | meals=1440 | transport=300

## 25. v3_harder_eval_000208

### 用户请求

- 城市/日期：济南 | 2026-07-03 -> 2026-07-05 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 4100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-07-03 | dinner | 秀宴•齐鲁文化美食剧场(高新店) |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 箪食巷私房菜(奥体店) | food_preference | lunch/dinner | 414 | 本地菜 |  |
| 2 | 穆得老周家牛肉烧饼 | food_preference | breakfast/lunch/dinner | 108 | 小吃/清真/清真 |  |
| 3 | 魏斯理汉堡(绿地国金天地店) | food_preference | breakfast/lunch/dinner | 120 | 小吃/快餐 |  |
| 4 | 达美乐比萨(老商埠店) | food_preference | breakfast/lunch/dinner | 150 | 小吃/快餐 |  |
| 5 | 渔家鲜·海鲜小炒·切馅煎包 | food_preference | breakfast/lunch/dinner | 207 | 小吃/海鲜 |  |
| 6 | 笨鸡小跑·临沂炒鸡(印象济南店) | food_preference | lunch/dinner | 228 | 本地菜 |  |
| 7 | 鲁西南老厨子(千佛山店) | food_preference | lunch/dinner | 237 | 本地菜 |  |
| 8 | 鲁西南老厨子(经六路延长线) | food_preference | lunch/dinner | 186 | 本地菜 |  |
| 9 | 向民炒鸡老店(济南店) | food_base | lunch/dinner | 267 | 老字号 |  |
| 10 | 鑫龙火锅城(环山路店) | food_base | lunch/dinner | 246 | 老字号 |  |

### 模型输出相关天

#### D1 2026-07-03

- 描述：第一天游览大明湖景区和趵突泉景区，晚上在秀宴•齐鲁文化美食剧场用餐。
- 交通：打车 | accommodation=高端酒店
- 酒店：卓瑞·曼兹酒店
- 景点：大明湖景区 / 趵突泉景区
- 餐饮：breakfast:酒店早餐(30元) / lunch:穆得老周家牛肉烧饼(108元) / dinner:秀宴•齐鲁文化美食剧场(高新店)(276元)

### 预算摘要

- total=3540 | attractions=240 | hotels=2250 | meals=750 | transport=300

## 26. v3_harder_eval_000209

### 用户请求

- 城市/日期：三亚 | 2026-06-03 -> 2026-06-06 | 4天
- 同行：{'adults': 1, 'children': 0, 'elders': 2, 'total': 3, 'companion_type': 'family_with_elders'}
- 交通/住宿：打车 / 亲子酒店
- 预算：{'amount': 6100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'soft'}
- 正向偏好：亲子 / 老人友好 / 博物馆 / 城市公园 / 特色餐厅
- 负向约束：爬山 / 夜间长距离移动 / 排队太久 / 重口味餐厅
- 饮食：想吃/偏好=清淡饮食；避免=无
- 自由文本：老人和小朋友一起出行，要求清淡饮食，路线要照顾体力。不要爬山、夜间长距离移动、排队太久和重口味餐厅。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-06 | dinner | 三亚七色海民宿 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 创味·民间海南菜·海鲜(林旺店) | food_preference | lunch/dinner | 288 | 老字号/海鲜 |  |
| 2 | 渔鲜·大东海海鲜排档 | food_preference | breakfast/lunch/dinner | 180 | 快餐/家常菜/海鲜 |  |
| 3 | 椰小鸡·椰子鸡(大东海银泰店) | food_preference | lunch/dinner | 330 | 特色餐厅 |  |
| 4 | 小海鲜渔民排档·农家海南菜 | food_preference | lunch/dinner | 243 | 特色餐厅/海鲜 |  |
| 5 | 椰小鸡·椰子鸡(海天盛宴总店) | food_preference | lunch/dinner | 330 | 特色餐厅 |  |
| 6 | 不仔客海鲜270度海景餐厅 | food_preference | lunch/dinner | 402 | 特色餐厅/海鲜 |  |
| 7 | 小海豚连锁海鲜餐厅(海棠湾店) | food_preference | lunch/dinner | 333 | 特色餐厅/海鲜 |  |
| 8 | 南门涮肉(三亚店) | food_preference | lunch/dinner | 330 | 老字号 |  |
| 9 | 海纳百川川菜馆(阳光雅园店) | food_companion | lunch/dinner | 174 | 家常菜 |  |
| 10 | 老善溜肉段东北菜馆(三亚店) | food_companion | lunch/dinner | 120 | 家常菜 |  |
| 11 | 三亚东北王酒楼旗舰店 | food_companion | lunch/dinner | 150 | 家常菜 |  |
| 12 | 年味王东北菜(红沙丽景嘉园店) | food_companion | lunch/dinner | 216 | 家常菜 |  |
| 13 | 东北饺子馆 | food_companion | lunch/dinner | 162 | 清淡餐厅 |  |
| 14 | 南海黎村·海南民族菜·海景餐厅(椰梦长廊店) | food_base | lunch/dinner | 300 | 本地菜 |  |
| 15 | 疍家佬味道·海南船家菜(亚龙湾店) | food_base | lunch/dinner | 291 | 本地菜 |  |
| 16 | 创味·民间海南菜(南山店) | food_base | lunch/dinner | 216 | 本地菜 |  |
| 17 | 创味·民间海南菜(藤桥·免税城店) | food_base | lunch/dinner | 252 | 本地菜 |  |

### 模型输出相关天

#### D4 2026-06-06

- 描述：参观三亚水稻国家公园，游览三亚山海贝文化博物馆，享受酒店早餐。
- 交通：打车 | accommodation=亲子酒店
- 酒店：None
- 景点：三亚水稻国家公园 / 三亚山海贝文化博物馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:南门涮肉(三亚店)(110元) / dinner:三亚七色海民宿(60元)

### 预算摘要

- total=5760 | attractions=240 | hotels=4200 | meals=720 | transport=400

## 27. v3_harder_eval_000206

### 用户请求

- 城市/日期：北京 | 2026-04-30 -> 2026-05-03 | 4天
- 同行：{'adults': 2, 'children': 1, 'elders': 0, 'total': 3, 'companion_type': 'family_with_children'}
- 交通/住宿：自驾 / 亲子酒店
- 预算：{'amount': 5200, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：亲子 / 动物园 / 海洋馆 / 城市公园 / 本地美食
- 负向约束：夜生活 / 太晚返程 / 过长步行 / 排队太久
- 饮食：想吃/偏好=无；避免=无
- 自由文本：带5岁孩子自驾，想安排亲子体验，但不要夜生活、太晚返程、过长步行或排队太久。预算是硬约束。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-03 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 鸽子窝(四季青店) | food_preference | lunch/dinner | 321 | 家常菜 |  |
| 2 | 湘约娘家烤鸭店(角门西店) | food_preference | lunch/dinner | 249 | 家常菜 |  |
| 3 | 北京凯瑞御仙都皇家菜博物馆 | food_preference | lunch/dinner | 1758 | 家常菜 |  |
| 4 | 滩羊铺子南北疆特色汇(通州店) | food_preference | lunch/dinner | 288 |  |  |
| 5 | 沁旺达餐厅(华睦亲子生活广场店) | food_preference | lunch/dinner | 270 | 亲子餐厅/海鲜 |  |
| 6 | 蒙古大营(朝阳公园店) | food_preference | lunch/dinner | 552 | 亲子餐厅 |  |
| 7 | 基辅罗斯餐厅(翠微店) | food_preference | lunch/dinner | 489 | 亲子餐厅 |  |
| 8 | 懒人盐府人家(安贞店) | food_preference | lunch/dinner | 288 | 家常菜 |  |
| 9 | 那家小馆(798艺术区店) | food_companion | lunch/dinner | 390 | 家常菜 |  |
| 10 | 胡大饭馆(簋街三店) | food_budget | lunch/dinner | 411 | 老字号 |  |
| 11 | 紫光园·烤鸭·北京菜(前门大栅栏店) | food_budget | lunch/dinner | 180 | 本地菜 |  |
| 12 | 浩海火烧云傣家菜(京广店) | food_budget | lunch/dinner | 315 | 本地菜 |  |
| 13 | 浩海火烧云傣家菜(东安市场店) | food_budget | lunch/dinner | 300 | 本地菜 |  |
| 14 | 牛街清真满恒記(平安里西大街店) | food_budget | lunch/dinner | 225 | 特色餐厅/清真/清真 |  |
| 15 | 宫宴(北京店) | food_budget | lunch/dinner | 1629 | 特色餐厅 |  |

### 模型输出相关天

#### D4 2026-05-03

- 描述：参观北京海洋馆，返程
- 交通：自驾 | accommodation=无住宿
- 酒店：None
- 景点：北京海洋馆
- 餐饮：breakfast:酒店早餐(30元) / lunch:牛街清真满恒記(平安里西大街店)(75元) / dinner:酒店晚餐(100元)

### 预算摘要

- total=2660 | attractions=180 | hotels=1800 | meals=480 | transport=200

## 28. v3_harder_eval_000222

### 用户请求

- 城市/日期：深圳 | 2026-01-04 -> 2026-01-07 | 4天
- 同行：{'adults': 4, 'children': 0, 'elders': 0, 'total': 4, 'companion_type': 'friends'}
- 交通/住宿：地铁+步行 / 经济型酒店
- 预算：{'amount': 2500, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'limited', 'strictness': 'hard'}
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 负向约束：海鲜餐厅 / 购物团 / 太偏远的景点 / 高价餐厅
- 饮食：想吃/偏好=无；避免=海鲜
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-01-07 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 欧记大排档•江西景德菜(深圳首店) | food_preference | lunch/dinner | 380 | 本地菜 |  |
| 2 | 欧记大排档·江西景德菜(南山保利店) | food_preference | lunch/dinner | 352 | 本地菜 |  |
| 3 | 欧记大排档·江西景德菜(罗湖东门町店) | food_preference | lunch/dinner | 384 | 本地菜 |  |
| 4 | 星店餐厅(凤凰城店) | food_preference | lunch/dinner | 192 | 特色餐厅 |  |
| 5 | 洪大厨鸡煲(南山旗舰店) | food_preference | breakfast/lunch/dinner | 400 | 小吃 |  |
| 6 | 哥二广西米粉店 | food_preference | breakfast/lunch/dinner | 132 | 小吃 |  |
| 7 | 螺一一螺蛳粉 | food_preference | breakfast/lunch/dinner | 100 | 小吃 |  |
| 8 | 蘩楼(宝安南路店) | food_budget | breakfast/lunch/dinner | 300 | 小吃 |  |
| 9 | 麦当劳(光华分店餐厅) | food_budget | breakfast/lunch/dinner | 144 | 小吃/快餐 |  |
| 10 | 麦当劳(深圳中心书城餐厅) | food_budget | breakfast/lunch/dinner | 80 | 快餐 |  |
| 11 | 昌记隆江猪脚饭 | food_budget | breakfast/lunch/dinner | 96 | 简餐 |  |
| 12 | 必胜客(深圳中心书城店) | food_budget | breakfast/lunch/dinner | 244 | 快餐 |  |
| 13 | 蘩楼(华强北总店) | food_base | breakfast/lunch/dinner | 352 | 老字号/快餐 |  |
| 14 | 南门涮肉(深圳首店) | food_base | lunch/dinner | 436 | 老字号 |  |
| 15 | 百草堂祖传凉茶铺 | food_base | lunch/dinner | 112 | 老字号 |  |

### 模型输出相关天

#### D4 2026-01-07

- 描述：返程日，游览深圳人才公园和南门涮肉
- 交通：地铁+步行 | accommodation=经济型酒店
- 酒店：None
- 景点：深圳人才公园 / 南门涮肉(深圳首店)
- 餐饮：breakfast:酒店早餐(30元) / lunch:南门涮肉(深圳首店)(436元) / dinner:酒店晚餐(400元)

### 预算摘要

- total=3000 | attractions=1400 | hotels=1200 | meals=1200 | transport=200

## 29. v3_harder_eval_000235

### 用户请求

- 城市/日期：广州 | 2026-08-02 -> 2026-08-06 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'solo'}
- 交通/住宿：公共交通 / 民宿
- 预算：{'amount': 2100, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：摄影 / 自然风光 / 城市漫步 / 本地菜
- 负向约束：密集行程 / 太偏远的景点 / 商业化打卡点
- 饮食：想吃/偏好=无；避免=无
- 自由文本：一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-08-06 | dinner | 无 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 滋粥楼·顺德菜(南村万博长隆商圈店) | food_diet | lunch/dinner | 112 | 本地菜 |  |
| 2 | 欧记大排档·江西景德菜(广州首店) | food_diet | lunch/dinner | 80 | 本地菜 |  |
| 3 | 滋粥楼·顺德菜(番禺广场总店) | food_diet | lunch/dinner | 94 | 本地菜 |  |
| 4 | 松苑·浓汤广府菜(总店) | food_diet | lunch/dinner | 121 | 本地菜 |  |
| 5 | 农耕故事乡下农庄(科韵路店) | food_diet | lunch/dinner | 109 | 本地菜 |  |
| 6 | 四哥家常菜 | food_diet | lunch/dinner | 90 | 本地菜/家常菜 |  |
| 7 | 银灯食府(丽丰国际中心店) | food_preference | lunch/dinner | 94 | 老字号 |  |
| 8 | 银灯食府(文化公园店) | food_preference | breakfast/lunch/dinner | 100 | 老字号/快餐 |  |
| 9 | 大鸽饭(体育西店) | food_preference | lunch/dinner | 109 | 老字号 |  |
| 10 | 大鸽饭(棠下店) | food_preference | lunch/dinner | 106 | 老字号 |  |
| 11 | 陶陶居酒家(第十甫路店) | food_preference | lunch/dinner | 101 | 老字号 |  |
| 12 | 广州仔潮汕仔特色店(广州总店) | food_budget | lunch/dinner | 26 | 特色餐厅 |  |

### 模型输出相关天

#### D5 2026-08-06

- 描述：返程，结束广州之旅。
- 交通：公共交通 | accommodation=民宿
- 酒店：None
- 景点：流花湖公园
- 餐饮：breakfast:酒店早餐(30元) / lunch:银灯食府(丽丰国际中心店)(94元) / dinner:无(0元)

### 预算摘要

- total=2380 | attractions=500 | hotels=1200 | meals=480 | transport=200

## 30. v3_harder_eval_000238

### 用户请求

- 城市/日期：上海 | 2026-08-02 -> 2026-08-04 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5200, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-08-04 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 海福多共富海鲜面馆 | food_preference | breakfast/lunch/dinner | 672 | 小吃/海鲜 |  |
| 2 | 农家菜老大(松江店) | food_preference | lunch/dinner | 279 | 本地菜 |  |
| 3 | 农家菜老大(九亭店) | food_preference | lunch/dinner | 345 | 本地菜 |  |
| 4 | 外滩家宴·上海菜(外滩豫园店) | food_preference | lunch/dinner | 405 | 本地菜 |  |
| 5 | 浩海火烧云傣家菜(新天地广场店) | food_preference | lunch/dinner | 327 | 本地菜 |  |
| 6 | 欧记大排档·景德菜(上海首店) | food_preference | lunch/dinner | 282 | 本地菜 |  |
| 7 | 紫阳村地道家常菜(川沙店) | food_preference | lunch/dinner | 294 | 特色餐厅/家常菜 |  |
| 8 | 魏家凉皮(上海文一中心店) | food_preference | breakfast/lunch/dinner | 105 | 小吃 |  |
| 9 | 南门涮肉(上海一店) | food_base | lunch/dinner | 369 | 老字号 |  |

### 模型输出相关天

#### D3 2026-08-04

- 描述：参观上海迪士尼度假区，晚上返回。
- 交通：打车 | accommodation=高端酒店
- 酒店：None
- 景点：上海迪士尼度假区
- 餐饮：breakfast:酒店早餐(30元) / lunch:魏家凉皮(上海文一中心店)(105元) / dinner:酒店晚餐(300元)

### 预算摘要

- total=5729 | attractions=1288 | hotels=2800 | meals=1041 | transport=600

## 31. v3_harder_eval_000255

### 用户请求

- 城市/日期：厦门 | 2026-06-03 -> 2026-06-07 | 5天
- 同行：{'adults': 1, 'children': 0, 'elders': 0, 'total': 1, 'companion_type': 'solo'}
- 交通/住宿：公共交通 / 民宿
- 预算：{'amount': 2000, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'standard', 'strictness': 'hard'}
- 正向偏好：摄影 / 自然风光 / 城市漫步 / 本地菜
- 负向约束：密集行程 / 太偏远的景点 / 商业化打卡点
- 饮食：想吃/偏好=无；避免=无
- 自由文本：一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-07 | dinner | 无 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 醉壹号海鲜大排档·老厦门特色菜(厦门美食地标店) | food_diet | lunch/dinner | 95 | 本地菜/海鲜 |  |
| 2 | 临家闽南菜(环岛路店) | food_diet | lunch/dinner | 125 | 本地菜 |  |
| 3 | 鑫坞堂 海鲜热炒(中山路总店) | food_diet | lunch/dinner | 69 | 本地菜/海鲜 |  |
| 4 | 鑫草美夫妻厦门菜(厦大白城店) | food_diet | lunch/dinner | 65 | 本地菜 |  |
| 5 | 草莓夫妇丨厦门菜(黄厝店) | food_diet | lunch/dinner | 105 | 本地菜 |  |
| 6 | 妞妞餐厅老厦门特色菜 | food_diet | lunch/dinner | 76 | 本地菜 |  |
| 7 | 好食来大排档(32年美食航标店) | food_preference | lunch/dinner | 95 | 老字号 |  |
| 8 | 相约厦门平价海鲜城(八市美食地标店) | food_preference | lunch/dinner | 39 | 老字号/海鲜 |  |
| 9 | 思北特香包(厦门中山路步行街趣栗酒店店) | food_preference | lunch/dinner | 17 | 老字号 |  |

### 模型输出相关天

#### D5 2026-06-07

- 描述：返程，结束愉快的厦门之旅。
- 交通：公共交通 | accommodation=无住宿
- 酒店：None
- 景点：滨海漫步道
- 餐饮：breakfast:酒店早餐(30元) / lunch:醉壹号海鲜大排档·老厦门特色菜(厦门美食地标店)(95元) / dinner:无(0元)

### 预算摘要

- total=2020 | attractions=270 | hotels=1200 | meals=450 | transport=200

## 32. v3_harder_eval_000262

### 用户请求

- 城市/日期：长沙 | 2026-05-08 -> 2026-05-11 | 4天
- 同行：{'adults': 4, 'children': 0, 'elders': 0, 'total': 4, 'companion_type': 'friends'}
- 交通/住宿：地铁+步行 / 经济型酒店
- 预算：{'amount': 2900, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'limited', 'strictness': 'hard'}
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 负向约束：海鲜餐厅 / 购物团 / 太偏远的景点 / 高价餐厅
- 饮食：想吃/偏好=无；避免=海鲜
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-05-09 | dinner | 酒店晚餐 |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 天宝兄弟(长沙汇景城店) | food_preference | breakfast/lunch/dinner | 700 | 小吃 |  |
| 2 | 大晴老板不在·锡纸烧烤大排档 | food_preference | breakfast/lunch/dinner | 260 | 小吃 |  |
| 3 | 喜座·湖南美食村落(总店) | food_preference | lunch/dinner | 532 | 特色餐厅 |  |
| 4 | KINGLOMO金粒门(国金街一店) | food_preference | breakfast/lunch/dinner | 152 | 小吃 |  |
| 5 | 扶记小吃货(都正街店) | food_preference | breakfast/lunch/dinner | 288 | 小吃 |  |
| 6 | 四方坪夜市 | food_preference | lunch/dinner | 128 | 夜市 |  |
| 7 | 鸿先阁 干煸虾 | food_preference | lunch/dinner | 400 | 老字号 |  |
| 8 | 秦皇食府(市府店) | food_preference | lunch/dinner | 320 | 老字号 |  |
| 9 | 公交新村粉店(太平街店) | food_budget | breakfast/lunch/dinner | 92 | 小吃 |  |
| 10 | 盛香亭转转热卤(河西王府井店) | food_budget | breakfast/lunch/dinner | 172 | 快餐 |  |
| 11 | 易裕和·长沙米粉(观沙岭店) | food_budget | breakfast/lunch/dinner | 56 | 快餐 |  |
| 12 | 德元兰州纯汤牛肉面(长沙总店)清真 | food_budget | breakfast/lunch/dinner | 80 | 快餐/清真/清真 |  |
| 13 | 大碗先生(悦方ID MALL店) | food_base | lunch/dinner | 200 | 老字号 |  |
| 14 | 秦皇食府·尚馔(贺龙店) | food_base | lunch/dinner | 452 | 老字号 |  |

### 模型输出相关天

#### D2 2026-05-09

- 描述：游览湖南省博物馆和岳麓书院，晚上在大晴老板不在·锡纸烧烤大排档品尝美食。
- 交通：地铁+步行 | accommodation=经济型酒店
- 酒店：长沙假日商务宾馆(马王堆店)
- 景点：湖南省博物馆 / 岳麓书院
- 餐饮：breakfast:酒店早餐(30元) / lunch:大晴老板不在·锡纸烧烤大排档(260元) / dinner:酒店晚餐(152元)

### 预算摘要

- total=1880 | attractions=200 | hotels=600 | meals=1080 | transport=200

## 33. v3_harder_eval_000268

### 用户请求

- 城市/日期：丽江 | 2026-06-18 -> 2026-06-20 | 3天
- 同行：{'adults': 3, 'children': 0, 'elders': 0, 'total': 3, 'companion_type': 'friends'}
- 交通/住宿：打车 / 高端酒店
- 预算：{'amount': 5800, 'scope': 'total', 'currency': 'CNY', 'budget_level': 'comfortable', 'strictness': 'hard'}
- 正向偏好：城市地标 / 美食 / 夜景 / 购物
- 负向约束：猪肉餐厅 / 太偏远的景点 / 低配住宿
- 饮食：想吃/偏好=不吃猪肉；避免=无
- 自由文本：三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。

### Miss 明细

| 日期 | 餐别 | 未命中名称 |
| --- | --- | --- |
| 2026-06-19 | lunch | 兰岚·云南菜·bistro |

### 可用 food_pois 候选

| # | name | bucket | roles | cost | tags | avoid_risk |
| ---: | --- | --- | --- | ---: | --- | --- |
| 1 | 菌香时·食神餐厅 | food_preference | lunch/dinner | 240 | 本地菜 |  |
| 2 | Lan岚•云南菜•bistro | food_preference | lunch/dinner | 321 | 本地菜 |  |
| 3 | 滇西王子·山风云南菜·丽江地标品牌(古城南门店) | food_preference | lunch/dinner | 294 | 本地菜 |  |
| 4 | 则瓦米线·云南小吃集合(一中店) | food_preference | breakfast/lunch/dinner | 141 | 小吃 |  |
| 5 | 阿婆情腊排骨火锅(旗舰店) | food_preference | lunch/dinner | 180 | 本地菜 |  |
| 6 | 隔壁老王·家常云南菜(丽江旗舰店) | food_preference | lunch/dinner | 243 | 本地菜 |  |
| 7 | 樱花餐厅 | food_preference | lunch/dinner | 261 | 特色餐厅 |  |
| 8 | 渣渣米线(古城店) | food_preference | breakfast/lunch/dinner | 177 | 小吃 |  |

### 模型输出相关天

#### D2 2026-06-19

- 描述：游览玉龙雪山，体验蓝月谷，晚上欣赏丽江夜景。
- 交通：打车 | accommodation=高端酒店
- 酒店：望湖轩湖景花园客栈(古城店)
- 景点：玉龙雪山国家级风景名胜区 / 玉龙雪山国家级风景名胜区蓝月谷
- 餐饮：breakfast:酒店早餐(30元) / lunch:兰岚·云南菜·bistro(57元) / dinner:阿婆情腊排骨火锅(旗舰店)(60元)

### 预算摘要

- total=3538 | attractions=240 | hotels=2250 | meals=438 | transport=600
