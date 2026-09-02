# 餐饮 Grounding Miss 分析

- records: 300
- generations: 300
- miss records: 15
- miss meals: 27

## 分类统计

| 类别 | 次数 | 说明 |
| --- | ---: | --- |
| generic_lodging_meal | 11 | 模型写了酒店晚餐/民宿晚餐等泛化住宿餐。 |
| hotel_or_lodging_name | 6 | 模型把 hotel_pois 的酒店/宾馆/民宿名当成餐厅。 |
| empty_or_none | 5 | 模型把餐饮写成“无/空”，通常是返程日晚餐问题。 |
| generic_area_or_restaurant | 3 | 模型写了夜市/附近餐厅/美食街等区域或泛化餐饮，不是 food_pois 具体名称。 |
| unmatched_specific_name | 2 | 看起来像具体店名，但未命中 food_pois。 |

## 餐别分布

| 餐别 | 次数 |
| --- | ---: |
| dinner | 21 |
| lunch | 6 |

## 明细

### 1. v3_harder_eval_000022

- 请求：桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- 人群/预算：companion=friends, budget_level=limited, diet=海鲜过敏
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-04-05 | dinner | 民俗街夜市 | 100 | generic_area_or_restaurant |
| 2026-04-06 | dinner | 民俗街夜市 | 100 | generic_area_or_restaurant |

**可用 food_pois 候选**

- 1. 食在香乡野本地菜 | cost=160 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 2. 澳门酒家(高新店) | cost=232 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 3. 山味.本地农家菜 | cost=160 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 4. 山野间餐厅 | cost=160 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 5. 碗碗都市香米粉店(铁西店) | cost=40 | roles=breakfast/lunch/dinner | cuisine=小吃/快餐 | avoid=
- 6. 仁利米粉(施家园店) | cost=52 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 7. 海天肠粉 | cost=56 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 8. 秋福米粉(桂林市正阳路步行街店) | cost=40 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 9. 田源米粉(三多店) | cost=28 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 10. 麦当劳(桂林临桂万达餐厅) | cost=120 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 11. 麦当劳(桂林西城南路餐厅) | cost=108 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 12. 绝味鸭脖(桂林临桂花生唐店) | cost=136 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 13. 椿记烧鹅(中山店) | cost=224 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 14. 椿记烧鹅(西街店) | cost=224 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 15. 阿甘酒家(依仁店) | cost=272 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 16. 阿甘酒家(解西店) | cost=340 | roles=lunch/dinner | cuisine=老字号 | avoid=

**酒店候选名**

- 1. 桂林兴安家家福宾馆 | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店
- 2. 华夏行酒店 | cost=200 | type=住宿服务;住宿服务相关;住宿服务相关
- 3. 资源鸿福宾馆 | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店
- 4. 像云边青年旅舍(象鼻山两江四湖店) | cost=200 | type=住宿服务;旅馆招待所;青年旅舍
- 5. 宏发宾馆(桂林北站店) | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 龙脊梯田国际青年旅舍 | cost=200 | type=住宿服务;旅馆招待所;青年旅舍
- 7. 莫非青年旅舍(桂林高铁北站店) | cost=200 | type=住宿服务;旅馆招待所;青年旅舍
- 8. 福星宾馆(临桂榕山路店) | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店
- 9. 桂林华强宾馆(瓦窑批发市场) | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 灌阳联宇大酒店 | cost=200 | type=住宿服务;宾馆酒店;宾馆酒店

### 2. v3_harder_eval_000103

- 请求：扬州 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- 人群/预算：companion=family_with_elders, budget_level=standard, diet=少辣
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-05-08 | lunch | 扬州忠强旅馆 | 45 | hotel_or_lodging_name |
| 2026-05-08 | dinner | 扬州忠强旅馆 | 45 | hotel_or_lodging_name |
| 2026-05-09 | lunch | 扬州忠强旅馆 | 45 | hotel_or_lodging_name |
| 2026-05-09 | dinner | 扬州忠强旅馆 | 45 | hotel_or_lodging_name |

**可用 food_pois 候选**

- 1. 肉夹馍酸辣粉 | cost=180 | roles=lunch/dinner | cuisine= | avoid=
- 2. 多放孜然少放辣 | cost=180 | roles=lunch/dinner | cuisine= | avoid=
- 3. 扬州院子·淮扬土菜庭院餐厅(大运河博物馆何园店) | cost=372 | roles=lunch/dinner | cuisine= | avoid=
- 4. 大毛·淮扬菜(梅岭东路店) | cost=255 | roles=lunch/dinner | cuisine= | avoid=
- 5. 大毛.淮扬菜(瘦西湖店) | cost=228 | roles=lunch/dinner | cuisine= | avoid=
- 6. 打酱油百姓饭堂·淮扬菜(大运河博物馆总店顺达路) | cost=195 | roles=lunch/dinner | cuisine= | avoid=
- 7. 打酱油百姓饭堂·淮扬菜(瘦西湖梅岭店) | cost=210 | roles=lunch/dinner | cuisine= | avoid=
- 8. 市井川菜(东亚御景湾店) | cost=216 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 9. 老土灶扬州民间淮扬菜(瘦西湖店) | cost=198 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 10. 众顺和淮扬菜 | cost=174 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 11. 李氏传家菜(兴城东路店) | cost=210 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 12. 胖哥川菜馆(润扬广场3幢店) | cost=192 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 13. 西北滋味源清真特色小厨 | cost=144 | roles=lunch/dinner | cuisine=清淡餐厅/清真 | avoid=
- 14. 邗江区祥来顺小馆餐饮店 | cost=171 | roles=lunch/dinner | cuisine=清淡餐厅/清真 | avoid=
- 15. 正悦清兰州牛肉面 | cost=48 | roles=lunch/dinner | cuisine=清淡餐厅/清真 | avoid=
- 16. 大毛.淮扬菜(何园店) | cost=261 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 17. 东关街美食广场 | cost=126 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 18. 必香居茶社(兴城路店) | cost=102 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 19. 北柳酒肆(东关街店) | cost=231 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 20. 大毛·淮扬菜(兴城东路店) | cost=201 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=

**酒店候选名**

- 1. 全季酒店(扬州瘦西湖花园店) | cost=400 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 2. 漫居安云酒店(扬州仪征工农北路万达广场店) | cost=400 | type=住宿服务;住宿服务相关;住宿服务相关
- 3. 桔子酒店(扬州东站健民路店) | cost=400 | type=住宿服务;住宿服务相关;住宿服务相关
- 4. 宝应佳佳商务宾馆 | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店|住宿服务;旅馆招待所;旅馆招待所
- 5. 如家商旅(金标)-扬州江都金鹰广场长江路店 | cost=400 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 6. 景达酒店(仪征万达广场店) | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 7. 西苑旅馆(原西苑招待所) | cost=400 | type=住宿服务;旅馆招待所;旅馆招待所
- 8. 扬州忠强旅馆 | cost=400 | type=住宿服务;旅馆招待所;旅馆招待所
- 9. 扬州八里镇春晓宾馆 | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 扬州旅社 | cost=400 | type=住宿服务;旅馆招待所;旅馆招待所

### 3. v3_harder_eval_000135

- 请求：西安 2026-02-03->2026-02-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- 人群/预算：companion=solo, budget_level=standard, diet=无
- 正向偏好：摄影 / 自然风光 / 城市漫步 / 本地菜
- 自由文本：一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-02-07 | dinner | 西安徐北宾馆 | 30 | hotel_or_lodging_name |

**可用 food_pois 候选**

- 1. 西南夷甄选云南菜餐厅(中大国际店) | cost=110 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 2. 虎子水盆羊肉(翠华路总店) | cost=43 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 3. 吉味轩陕南菜(创汇社区C区南门店) | cost=50 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 4. 宴长安·西安菜(铂金店) | cost=81 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 5. 铭家家宴·海鲜水饺·青岛菜·院子餐厅(高新店) | cost=123 | roles=lunch/dinner | cuisine=本地菜/海鲜 | avoid=
- 6. 奔跑吧陕菜·常来长安(钟楼南大街店) | cost=70 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 7. 奔跑吧陕菜·雁塔长安(大雁塔店) | cost=61 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 8. 八百里秦川·正宗陕菜(大唐不夜城锦安坊店) | cost=98 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 9. 清真刚刚烤肉(小南门店) | cost=54 | roles=lunch/dinner | cuisine=老字号/清真 | avoid=
- 10. 西安秋林公司(秋林店) | cost=23 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 11. 清真刚刚烤肉(芙蓉街店) | cost=80 | roles=lunch/dinner | cuisine=老字号/清真 | avoid=
- 12. 爱骅裤带面馆(钟楼店) | cost=22 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 13. 蓝田印象 | cost=32 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 14. 马洪小炒泡馍馆 | cost=31 | roles=breakfast/lunch/dinner | cuisine=小吃/清真 | avoid=
- 15. 魏家凉皮(西大街店) | cost=24 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=

**酒店候选名**

- 1. 西安徐北宾馆 | cost=300 | type=住宿服务;宾馆酒店;宾馆酒店
- 2. 西安丽都民宿(长乐西苑店) | cost=300 | type=住宿服务;住宿服务相关;住宿服务相关
- 3. 西安好洁公寓 | cost=300 | type=住宿服务;住宿服务相关;住宿服务相关
- 4. 唯佳民宿(西安北辰大道店) | cost=300 | type=住宿服务;住宿服务相关;住宿服务相关
- 5. 柠檬公寓(西安长乐西苑店) | cost=300 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 枕月青年旅社(西安科技路地铁站店) | cost=300 | type=住宿服务;旅馆招待所;青年旅舍
- 7. 桂花载久露台花园青年旅舍(钟鼓楼回民街店) | cost=300 | type=住宿服务;旅馆招待所;青年旅舍
- 8. 尚俭太空舱公寓(西安大雁塔店) | cost=300 | type=住宿服务;旅馆招待所;旅馆招待所
- 9. 大雄青年旅舍(西安龙首原地铁站店) | cost=300 | type=住宿服务;旅馆招待所;青年旅舍
- 10. 十叁都赋青年旅社(西安钟鼓楼城墙店) | cost=300 | type=住宿服务;住宿服务相关;住宿服务相关

### 4. v3_harder_eval_000270

- 请求：桂林 2025-05-04->2025-05-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- 人群/预算：companion=family_mixed, budget_level=comfortable, diet=清淡饮食
- 正向偏好：亲子 / 老人友好 / 历史文化 / 城市公园 / 本地美食
- 自由文本：三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2025-05-05 | dinner | 酒店晚餐 | 200 | generic_lodging_meal |
| 2025-05-06 | dinner | 酒店晚餐 | 200 | generic_lodging_meal |
| 2025-05-07 | dinner | 酒店晚餐 | 200 | generic_lodging_meal |
| 2025-05-08 | dinner | 酒店晚餐 | 200 | generic_lodging_meal |

**可用 food_pois 候选**

- 1. 食在香乡野本地菜 | cost=200 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 2. 璞食·桂北融合菜(阳朔西街漓江店) | cost=300 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 3. 山野间餐厅 | cost=200 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 4. 山味.本地农家菜 | cost=200 | roles=lunch/dinner | cuisine= | avoid=
- 5. 阿甘酒家(中山店) | cost=365 | roles=lunch/dinner | cuisine= | avoid=
- 6. 蜜棠升明月江景餐厅 | cost=260 | roles=lunch/dinner | cuisine=亲子餐厅 | avoid=
- 7. 味道制造·桂林菜(七星店) | cost=255 | roles=lunch/dinner | cuisine= | avoid=
- 8. 桂隐厨·私房家常菜(万象城店) | cost=400 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 9. 澳门酒家(高新店) | cost=290 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 10. 椿记烧鹅(中山店) | cost=280 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 11. 椿记烧鹅(西街店) | cost=280 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 12. 阿甘酒家(依仁店) | cost=340 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 13. 阿甘酒家(解西店) | cost=425 | roles=lunch/dinner | cuisine=老字号 | avoid=

**酒店候选名**

- 1. 华夏行酒店 | cost=400 | type=住宿服务;住宿服务相关;住宿服务相关
- 2. 像云边青年旅舍(象鼻山两江四湖店) | cost=400 | type=住宿服务;旅馆招待所;青年旅舍
- 3. 维也纳酒店(桂林兴安店) | cost=400 | type=住宿服务;住宿服务相关;住宿服务相关
- 4. 太子酒店 | cost=400 | type=住宿服务;宾馆酒店;四星级宾馆
- 5. 龙脊梯田蓝影主题民宿(金佛顶缆车索道店) | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 桂林北桂酒店(桂林火车站南溪山公园店) | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 7. 宏发宾馆(桂林北站店) | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 雅斯特酒店(桂林资源县政府店) | cost=400 | type=住宿服务;宾馆酒店;宾馆酒店
- 9. 龙脊梯田国际青年旅舍 | cost=400 | type=住宿服务;旅馆招待所;青年旅舍
- 10. 莫非青年旅舍(桂林高铁北站店) | cost=400 | type=住宿服务;旅馆招待所;青年旅舍

### 5. v3_harder_eval_000039

- 请求：深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- 人群/预算：companion=family_with_elders, budget_level=comfortable, diet=清淡饮食
- 正向偏好：亲子 / 老人友好 / 博物馆 / 城市公园 / 特色餐厅
- 自由文本：老人和小朋友一起出行，要求清淡饮食，路线要照顾体力。不要爬山、夜间长距离移动、排队太久和重口味餐厅。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2025-11-08 | dinner | 无 | 0 | empty_or_none |

**可用 food_pois 候选**

- 1. 星店餐厅(凤凰城店) | cost=96 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 2. 蘩楼(华强北总店) | cost=176 | roles=breakfast/lunch/dinner | cuisine=老字号/快餐 | avoid=
- 3. 南门涮肉(深圳首店) | cost=218 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 4. 百草堂祖传凉茶铺 | cost=56 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 5. 东江海鲜大排档.潮汕菜.砂锅粥 | cost=176 | roles=lunch/dinner | cuisine=老字号/海鲜 | avoid=
- 6. 鑫缘阁东北菜(沙井店) | cost=100 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 7. 点都德(岗厦北店) | cost=172 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 8. 潮香四海·家传潮汕菜(南山店) | cost=176 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 雪乡情东北菜(登良旗舰店) | cost=118 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 10. 一品红川菜(皇岗分店) | cost=182 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 11. 七月柿Farm House(深圳湾大地广场店) | cost=248 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 12. 巴蜀风月(宝安店) | cost=206 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 13. 龙帝桂林米粉 | cost=38 | roles=lunch/dinner | cuisine=清淡餐厅 | avoid=
- 14. 程家逍遥镇胡辣汤(沙井和一二路店) | cost=20 | roles=lunch/dinner | cuisine=清淡餐厅 | avoid=
- 15. 云妹福鼎肉片 | cost=20 | roles=lunch/dinner | cuisine=清淡餐厅 | avoid=
- 16. 欧记大排档•江西景德菜(深圳首店) | cost=190 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 17. 欧记大排档·江西景德菜(南山保利店) | cost=176 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 18. 欧记大排档·江西景德菜(罗湖东门町店) | cost=192 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 深圳时光小屋青年旅舍 | cost=550 | type=住宿服务;旅馆招待所;青年旅舍
- 2. 深圳光明温德姆至尊酒店 | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 七月居青年旅舍(宝安上川地铁站店) | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 4. 深圳浪骑瞻云度假酒店 | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 5. 深圳国际会展中心洲际酒店 | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 深圳前海华侨城艾美酒店 | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 7. 深圳前海华侨城瑞吉酒店 | cost=550 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 青朴旅居公寓(深圳世界之窗店) | cost=550 | type=住宿服务;旅馆招待所;旅馆招待所
- 9. 万发住宿 | cost=550 | type=住宿服务;旅馆招待所;旅馆招待所
- 10. 深圳暖心青年旅社(深大科技园店) | cost=550 | type=住宿服务;旅馆招待所;青年旅舍

### 6. v3_harder_eval_000104

- 请求：杭州 2026-08-02->2026-08-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- 人群/预算：companion=business, budget_level=comfortable, diet=无
- 正向偏好：城市地标 / 特色餐厅 / 自由活动多 / 博物馆
- 自由文本：出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-08-04 | dinner | 杭州牵手驿家酒店 | 500 | hotel_or_lodging_name |

**可用 food_pois 候选**

- 1. 肉本家·炭烤肉(杭州浙大总店) | cost=106 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 2. 老秦凉都黄牛肉馆(滨江总店) | cost=78 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 3. 知味观(湖滨总店) | cost=68 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 4. 杭州酒家(延安路店) | cost=77 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 5. 乔村二十八道(钱江世纪城店) | cost=140 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 6. 李白图书馆餐厅(西溪湿地店) | cost=112 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 7. 李白图书馆餐厅(西湖大学店) | cost=112 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 8. 李白图书馆餐厅(白洋桥店) | cost=130 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 乔村二十八道(未来科技城店) | cost=152 | roles=lunch/dinner | cuisine= | avoid=
- 10. 宫宴(杭州店) | cost=521 | roles=lunch/dinner | cuisine= | avoid=
- 11. 新周记·巷子里的江南味(平海路店) | cost=103 | roles=lunch/dinner | cuisine= | avoid=
- 12. 锦禾堂·高端定制餐厅(大浒街店) | cost=319 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 13. 鮨·鱼小喵(高端日料宅配旗舰店) | cost=65 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 14. Missblue生日蛋糕高端定制(回龙庙前店) | cost=110 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 15. 柳来原味螺蛳粉(枫香路店) | cost=31 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 16. 传家(骆家庄西苑一区店) | cost=80 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 17. 钱棠·萧山本帮菜(萧山机场大会展店) | cost=106 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 18. 瓷·忆赣菜中心(杭州) | cost=119 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 19. 山野之约·舌尖上的桐庐美食 | cost=82 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 20. 赵府私厨·老杭帮菜(西湖老店) | cost=69 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 杭州云慢民宿(宋城店) | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 2. 永利活禅酒店(人民广场地铁恒隆店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 杭州大家小院·碳先生智能健康民宿 | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 4. 杭州西湖陇上山居璞玉客栈 | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 5. 韶华卿卿青年旅舍(滨康路地铁站店) | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 6. 杭州拣枝而栖青年旅舍(龙湖滨江天街江陵路地铁站店) | cost=500 | type=住宿服务;旅馆招待所;青年旅舍
- 7. 旅小二青年酒店(金地广场店) | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 8. 杭州拣枝而栖青年旅舍(杭州武林广场宝善桥地铁站店) | cost=500 | type=住宿服务;旅馆招待所;青年旅舍
- 9. 杭州牵手驿家酒店 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 富阳鸿鑫宾馆 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店

### 7. v3_harder_eval_000251

- 请求：济南 2026-07-03->2026-07-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- 人群/预算：companion=couple, budget_level=premium, diet=无
- 正向偏好：高端酒店 / 艺术 / 特色餐厅 / 城市地标 / 休闲慢游
- 自由文本：两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-07-06 | dinner | 无 | 0 | empty_or_none |

**可用 food_pois 候选**

- 1. 穆得老周家牛肉烧饼 | cost=72 | roles=lunch/dinner | cuisine=老字号/清真 | avoid=
- 2. 向民炒鸡老店(济南店) | cost=178 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 3. 鑫龙火锅城(环山路店) | cost=164 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 4. 箪食巷私房菜(奥体店) | cost=276 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 5. 老济南济南菜(大明湖店) | cost=150 | roles=lunch/dinner | cuisine=老字号/海鲜 | avoid=
- 6. 澜锦·鸽厨主题餐厅(开元府店) | cost=252 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 7. 鑫悦诚府·新鲁菜·餐厅(趵突泉店) | cost=128 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 8. 醉得意·山茶油炒土鸡(济南芙蓉街店) | cost=90 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 鲁海湾·渔家菜(龙鼎大道店) | cost=170 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 10. 7号院·精品湘菜羊汤(奥体中路CBD店) | cost=282 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 11. 西棠食久记 | cost=186 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 12. 东舜赶海•渔家菜(经十路店) | cost=202 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 13. 鼎煮高端和牛放题(国华广场店) | cost=974 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 14. 泉客厅Spring Pavilion中餐厅(济南绿地中心店) | cost=1782 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 15. 长安道高端火锅 | cost=1394 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 16. 魏斯理汉堡(绿地国金天地店) | cost=80 | roles=breakfast/lunch/dinner | cuisine=小吃/快餐 | avoid=
- 17. 达美乐比萨(老商埠店) | cost=100 | roles=breakfast/lunch/dinner | cuisine=小吃/快餐 | avoid=
- 18. 渔家鲜·海鲜小炒·切馅煎包 | cost=138 | roles=breakfast/lunch/dinner | cuisine=小吃/海鲜 | avoid=
- 19. 笨鸡小跑·临沂炒鸡(印象济南店) | cost=152 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. IU酒店(济南山东艺术设计学院店) | cost=750 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 2. 卓瑞·曼兹酒店 | cost=750 | type=住宿服务;宾馆酒店;四星级宾馆
- 3. 九如山不二木居民宿 | cost=750 | type=住宿服务;宾馆酒店;宾馆酒店
- 4. 济南聚满佳住房 | cost=750 | type=住宿服务;旅馆招待所;旅馆招待所|餐饮服务;中餐厅;中餐厅
- 5. 济南南郊宾馆 | cost=750 | type=住宿服务;宾馆酒店;四星级宾馆
- 6. 济南舜耕会展中心六里山南路亚朵酒店 | cost=750 | type=住宿服务;宾馆酒店;宾馆酒店
- 7. 泉城大酒店 | cost=750 | type=住宿服务;宾馆酒店;四星级宾馆|餐饮服务;餐饮相关场所;餐饮相关
- 8. 济南舒心小憩公寓 | cost=750 | type=住宿服务;宾馆酒店;宾馆酒店
- 9. 丰豪宾馆(济南英雄山风景区店) | cost=750 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 昌源大酒店(济微公路店) | cost=750 | type=住宿服务;宾馆酒店;宾馆酒店

### 8. v3_harder_eval_000030

- 请求：三亚 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- 人群/预算：companion=family_mixed, budget_level=comfortable, diet=清淡饮食
- 正向偏好：亲子 / 老人友好 / 历史文化 / 城市公园 / 本地美食
- 自由文本：三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-05-12 | dinner | 南梦园电子游艺厅(金润广场店) | 46 | unmatched_specific_name |

**可用 food_pois 候选**

- 1. 南海黎村·海南民族菜·海景餐厅(椰梦长廊店) | cost=500 | roles=lunch/dinner | cuisine= | avoid=
- 2. 椰小鸡·椰子鸡(海棠68环球美食店) | cost=575 | roles=lunch/dinner | cuisine= | avoid=
- 3. 创味·民间海南菜·海鲜(林旺店) | cost=480 | roles=lunch/dinner | cuisine=海鲜 | avoid=
- 4. 渔鲜·大东海海鲜排档 | cost=300 | roles=breakfast/lunch/dinner | cuisine=快餐/家常菜/海鲜 | avoid=
- 5. 嗲嗲的椰子鸡(椰梦长廊店) | cost=635 | roles=lunch/dinner | cuisine= | avoid=
- 6. 嗲嗲的椰子鸡(三亚湾店) | cost=500 | roles=lunch/dinner | cuisine= | avoid=
- 7. 海纳百川川菜馆(阳光雅园店) | cost=290 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 8. 老善溜肉段东北菜馆(三亚店) | cost=200 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 9. 疍家佬味道·海南船家菜(亚龙湾店) | cost=485 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 10. 创味·民间海南菜(南山店) | cost=360 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 11. 创味·民间海南菜(藤桥·免税城店) | cost=420 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 12. 椰小鸡·椰子鸡(大东海银泰店) | cost=550 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 13. 小海鲜渔民排档·农家海南菜 | cost=405 | roles=lunch/dinner | cuisine=特色餐厅/海鲜 | avoid=
- 14. 椰小鸡·椰子鸡(海天盛宴总店) | cost=550 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=

**酒店候选名**

- 1. 如家酒店(三亚千古情海旅免税城店) | cost=500 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 2. 佳和酒店(海棠湾免税城店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 三亚金的精品酒店公寓(三亚湾凤凰机场店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 4. 猪小弟海景度假公寓 | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 5. 三亚三夏光年客栈 | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 6. 速8精选酒店(三亚湾椰梦长廊店) | cost=500 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 7. 三亚七色海民宿 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 三亚得居圣岛旅租 | cost=500 | type=住宿服务;旅馆招待所;青年旅舍
- 9. 云合十里青年旅舍 | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 10. 哪里那里海岸精品客栈(三亚亚龙湾店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店|住宿服务;旅馆招待所;旅馆招待所

### 9. v3_harder_eval_000060

- 请求：厦门 2026-06-03->2026-06-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- 人群/预算：companion=family_mixed, budget_level=comfortable, diet=清淡饮食
- 正向偏好：亲子 / 老人友好 / 历史文化 / 城市公园 / 本地美食
- 自由文本：三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-06-07 | dinner | 无 | 0 | empty_or_none |

**可用 food_pois 候选**

- 1. 醉壹号海鲜大排档·老厦门特色菜(厦门美食地标店) | cost=475 | roles=lunch/dinner | cuisine=海鲜 | avoid=
- 2. 海渔家餐厅 | cost=300 | roles=lunch/dinner | cuisine=亲子餐厅/海鲜 | avoid=
- 3. 闹两川·老牌川菜馆(东渡店) | cost=400 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 4. 草莓夫妇丨厦门菜(厦大沙坡尾店) | cost=440 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 5. 闹两川.老牌川菜(同安朱子良库店) | cost=250 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 6. 金家港海鲜大排档(中山路店) | cost=455 | roles=lunch/dinner | cuisine=海鲜 | avoid=
- 7. 妞妞餐厅老厦门特色菜 | cost=380 | roles=lunch/dinner | cuisine= | avoid=
- 8. 宴遇·福建荟馆(新景中心店) | cost=1705 | roles=lunch/dinner | cuisine= | avoid=
- 9. 好食来大排档(32年美食航标店) | cost=475 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 10. 相约厦门平价海鲜城(八市美食地标店) | cost=195 | roles=lunch/dinner | cuisine=老字号/海鲜 | avoid=
- 11. 临家闽南菜(环岛路店) | cost=625 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 12. 鑫坞堂 海鲜热炒(中山路总店) | cost=345 | roles=lunch/dinner | cuisine=本地菜/海鲜 | avoid=
- 13. 鑫草美夫妻厦门菜(厦大白城店) | cost=325 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 14. 草莓夫妇丨厦门菜(黄厝店) | cost=525 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 厦门屿海民宿 | cost=450 | type=住宿服务;住宿服务相关;住宿服务相关
- 2. 厦门原宿海景公寓 | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 他·城·壹·海海景酒店 | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店|住宿服务;旅馆招待所;旅馆招待所
- 4. 聆感·安屿192O侘寂美学酒店(鼓浪屿三丘田码头店) | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店
- 5. 七庆美居酒店(彩虹沙滩店) | cost=450 | type=商务住宅;住宅区;住宅小区|住宿服务;住宿服务相关;住宿服务相关
- 6. 鼓浪屿晃岩36酒店 | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店
- 7. 鼓浪屿海岸花旅馆(三丘田码头龙头路小吃街店) | cost=450 | type=住宿服务;旅馆招待所;旅馆招待所
- 8. 厦门屿上别厝·甄选酒店 | cost=450 | type=住宿服务;住宿服务相关;住宿服务相关
- 9. 拾末·鼓浪屿1931海景影音天台别墅酒店(三丘田码头店) | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 一尚锦苑酒店(翔安马巷店) | cost=450 | type=住宿服务;宾馆酒店;宾馆酒店

### 10. v3_harder_eval_000082

- 请求：西安 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- 人群/预算：companion=friends, budget_level=limited, diet=海鲜过敏
- 正向偏好：美食 / 夜市 / 老字号 / 城市漫步
- 自由文本：四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-04-05 | dinner | 文体中心夜市 | 128 | generic_area_or_restaurant |

**可用 food_pois 候选**

- 1. 虎子水盆羊肉(翠华路总店) | cost=172 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 2. 蓝田印象 | cost=128 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 3. 爱骅裤带面馆(钟楼店) | cost=88 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 4. 马洪小炒泡馍馆 | cost=124 | roles=breakfast/lunch/dinner | cuisine=小吃/清真 | avoid=
- 5. 魏家凉皮(西大街店) | cost=96 | roles=breakfast/lunch/dinner | cuisine=小吃 | avoid=
- 6. 魏斯理汉堡(凤城十二路店) | cost=192 | roles=breakfast/lunch/dinner | cuisine=小吃/快餐 | avoid=
- 7. 清真刚刚烤肉(小南门店) | cost=216 | roles=lunch/dinner | cuisine=老字号/清真 | avoid=
- 8. 西安秋林公司(秋林店) | cost=92 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 9. 魏斯理汉堡(博乐里店) | cost=176 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 10. 必胜客(文景餐厅) | cost=164 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 11. 魏家凉皮(西安凤八博乐里凉皮店) | cost=136 | roles=breakfast/lunch/dinner | cuisine=快餐 | avoid=
- 12. 清真刚刚烤肉(芙蓉街店) | cost=320 | roles=lunch/dinner | cuisine=老字号/清真 | avoid=

**酒店候选名**

- 1. 西安好客宾馆(唐兴路店) | cost=250 | type=住宿服务;住宿服务相关;住宿服务相关
- 2. 西安拾玥宾馆 | cost=250 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 百影汇酒店(航空学院阎良校区店) | cost=250 | type=住宿服务;住宿服务相关;住宿服务相关
- 4. 迎宾宾馆(西安付村花园店) | cost=250 | type=住宿服务;宾馆酒店;宾馆酒店|住宿服务;旅馆招待所;旅馆招待所
- 5. 睿泊影咖酒店(比亚迪二厂店) | cost=250 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 枕月青年旅社(西安科技路地铁站店) | cost=250 | type=住宿服务;旅馆招待所;青年旅舍
- 7. 桂花载久露台花园青年旅舍(钟鼓楼回民街店) | cost=250 | type=住宿服务;旅馆招待所;青年旅舍
- 8. 尚俭太空舱公寓(西安大雁塔店) | cost=250 | type=住宿服务;旅馆招待所;旅馆招待所
- 9. 大雄青年旅舍(西安龙首原地铁站店) | cost=250 | type=住宿服务;旅馆招待所;青年旅舍
- 10. 十叁都赋青年旅社(西安钟鼓楼城墙店) | cost=250 | type=住宿服务;住宿服务相关;住宿服务相关

### 11. v3_harder_eval_000081

- 请求：青岛 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- 人群/预算：companion=couple, budget_level=premium, diet=无
- 正向偏好：高端酒店 / 艺术 / 特色餐厅 / 城市地标 / 休闲慢游
- 自由文本：两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-05-08 | dinner | 酒店晚餐 | 114 | generic_lodging_meal |
| 2026-05-09 | lunch | 酒店午餐 | 114 | generic_lodging_meal |
| 2026-05-10 | lunch | 酒店午餐 | 114 | generic_lodging_meal |

**可用 food_pois 候选**

- 1. 前海沿·青岛菜(五四广场永旺店) | cost=114 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 2. 众品老方子锅贴甜沫(总店) | cost=36 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 3. 前海沿·青岛菜(中山路天主教堂店) | cost=134 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 4. 西镇臭豆腐·电烤肉(汶上路店) | cost=52 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 5. 33号大院·青岛本帮菜(青岛旗舰店) | cost=130 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 6. 开海·红岛海鲜虾水饺店(八大关店) | cost=230 | roles=lunch/dinner | cuisine=特色餐厅/海鲜 | avoid=
- 7. 船歌·鱼水饺青岛菜(青岛万象城店) | cost=172 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 8. 柏海餐厅 | cost=186 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 双合园·海鲜水饺青岛菜(九水东店) | cost=190 | roles=lunch/dinner | cuisine=精致餐厅/海鲜 | avoid=
- 10. 升海·本源海鲜海胆水饺(西海岸店) | cost=240 | roles=lunch/dinner | cuisine=精致餐厅/海鲜 | avoid=
- 11. 吕氏焗小鲜•花园餐厅(八大关店) | cost=144 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 12. 铭宴·东方合院·园林餐厅 | cost=178 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 13. 味语膳房(石老人) | cost=632 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 14. 我很牛·高端自助火锅(东李鞋城店) | cost=170 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 15. 石源高端日料三文鱼 | cost=178 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 16. 陈文鼎·黑糖珍珠奶茶(台东姿儿街店) | cost=26 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 17. 等俺船靠岸·老船蒸鲜·渔家菜(全球创始店) | cost=146 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 18. 众品老方子锅贴甜沫(栈桥店) | cost=40 | roles=breakfast/lunch/dinner | cuisine=小吃/快餐 | avoid=
- 19. 良友青岛菜(五四广场店) | cost=182 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 都市118连锁酒店(青岛山东科技大学北门店) | cost=800 | type=住宿服务;住宿服务相关;住宿服务相关
- 2. 青岛智胜锦钰酒店(海尔工业园山东科技大学店) | cost=800 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 青岛世界博览城润生大酒店 | cost=1250 | type=住宿服务;宾馆酒店;五星级宾馆
- 4. 青岛五四广场海信广场亚朵酒店 | cost=1250 | type=住宿服务;宾馆酒店;五星级宾馆
- 5. 青岛五四广场云霄路亚朵酒店 | cost=800 | type=住宿服务;宾馆酒店;四星级宾馆
- 6. 青岛锦里酒店(青岛火车站栈桥店) | cost=800 | type=住宿服务;住宿服务相关;住宿服务相关
- 7. 青岛金叶宾馆 | cost=800 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 海畔之家宾馆 | cost=800 | type=住宿服务;宾馆酒店;宾馆酒店
- 9. 升级商务宾馆 | cost=800 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 香江之星商务酒店 | cost=800 | type=住宿服务;宾馆酒店;宾馆酒店

### 12. v3_harder_eval_000131

- 请求：上海 2026-05-06->2026-05-09 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- 人群/预算：companion=couple, budget_level=premium, diet=无
- 正向偏好：高端酒店 / 艺术 / 特色餐厅 / 城市地标 / 休闲慢游
- 自由文本：两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-05-06 | lunch | 上海城隍庙小吃 | 50 | unmatched_specific_name |
| 2026-05-07 | dinner | 酒店晚餐 | 246 | generic_lodging_meal |
| 2026-05-08 | dinner | 酒店晚餐 | 246 | generic_lodging_meal |
| 2026-05-09 | lunch | 酒店午餐 | 246 | generic_lodging_meal |

**可用 food_pois 候选**

- 1. 南门涮肉(上海一店) | cost=246 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 2. 紫阳村地道家常菜(川沙店) | cost=196 | roles=lunch/dinner | cuisine=特色餐厅/家常菜 | avoid=
- 3. 红子鸡凤凰楼 | cost=274 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 4. 沪西老弄堂面馆(广东路店) | cost=88 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 5. 莱莱小笼 | cost=134 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 6. 沈大成(南京东路店) | cost=86 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 7. 贯贯吉·清真餐厅(浙江中路店) | cost=210 | roles=lunch/dinner | cuisine=特色餐厅/清真 | avoid=
- 8. 3号仓库·餐厅(上海首店) | cost=316 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 宫宴(上海店) | cost=946 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 10. Solo(衡山路店) | cost=338 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 11. 浦江家宴 | cost=512 | roles=lunch/dinner | cuisine=精致餐厅 | avoid=
- 12. 醉辉皇海鲜皇宫(118店) | cost=378 | roles=lunch/dinner | cuisine=精致餐厅/海鲜 | avoid=
- 13. 上海滩餐厅(BFC外滩金融中心店) | cost=1102 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 14. 席作·福建会馆(新天地时尚一期店) | cost=962 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 15. 逸道(益丰·外滩源店) | cost=1032 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 16. 东方景宴 | cost=1122 | roles=lunch/dinner | cuisine=黑珍珠 | avoid=
- 17. 海福多共富海鲜面馆 | cost=448 | roles=breakfast/lunch/dinner | cuisine=小吃/海鲜 | avoid=
- 18. 农家菜老大(松江店) | cost=186 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 19. 农家菜老大(九亭店) | cost=230 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 20. 外滩家宴·上海菜(外滩豫园店) | cost=270 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 璞爵国际酒店(上海松江新桥店) | cost=850 | type=住宿服务;宾馆酒店;宾馆酒店
- 2. 東禾九谷悦泊鄉乡村酒店 | cost=850 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 青旅瑞华酒店(上海大宁店) | cost=850 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 4. 一间森林青年旅舍(上海同济大学四平路地铁站店) | cost=850 | type=住宿服务;旅馆招待所;青年旅舍|住宿服务;宾馆酒店;宾馆酒店
- 5. 上海左庭上院酒店 | cost=850 | type=住宿服务;宾馆酒店;宾馆酒店
- 6. 上海也山花园民宿(崇明森林公园店) | cost=850 | type=住宿服务;旅馆招待所;旅馆招待所
- 7. 际庭青旅(北外滩平凉路地铁站店) | cost=850 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 上海船长五号青年酒店(莘庄地铁站店) | cost=850 | type=住宿服务;宾馆酒店;宾馆酒店
- 9. 布丁严选酒店(上海顾村公园华山医院店) | cost=850 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 10. 上海宝格丽酒店 | cost=1400 | type=住宿服务;宾馆酒店;五星级宾馆

### 13. v3_harder_eval_000134

- 请求：北京 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- 人群/预算：companion=business, budget_level=comfortable, diet=无
- 正向偏好：城市地标 / 特色餐厅 / 自由活动多 / 博物馆
- 自由文本：出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-05-09 | dinner | 酒店晚餐 | 50 | generic_lodging_meal |

**可用 food_pois 候选**

- 1. 胡大饭馆(簋街三店) | cost=137 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 2. 牛街清真满恒記(平安里西大街店) | cost=75 | roles=lunch/dinner | cuisine=特色餐厅/清真 | avoid=
- 3. 宫宴(北京店) | cost=543 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 4. 蘇锦宴·淮扬菜·大班徽菜·果木烤鸭(定慧寺店) | cost=162 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 5. 南门涮肉(后海店) | cost=105 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 6. 胡大饭馆24h(簋街总店) | cost=152 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 7. 南门涮肉(东单店) | cost=135 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 8. ZENG餐厅剧场店(前门店) | cost=88 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 9. 四季民福烤鸭店(双井店) | cost=186 | roles=lunch/dinner | cuisine= | avoid=
- 10. 北京宴(丰台总店) | cost=346 | roles=lunch/dinner | cuisine= | avoid=
- 11. 四季民福烤鸭店(望京旺角店) | cost=141 | roles=lunch/dinner | cuisine= | avoid=
- 12. 北京凯瑞御仙都皇家菜博物馆 | cost=586 | roles=lunch/dinner | cuisine= | avoid=
- 13. 丹江渔村·小院(四季御园店) | cost=204 | roles=lunch/dinner | cuisine= | avoid=
- 14. 高端商务茶歇冷餐自助餐 | cost=97 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 15. 大兴高端智造产业园餐厅 | cost=60 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 16. 鮨丼屋高端日料三文鱼(月恒正大新生活广场店) | cost=60 | roles=lunch/dinner | cuisine=高端餐厅 | avoid=
- 17. 紫光园·烤鸭·北京菜(前门大栅栏店) | cost=60 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 18. 鸽子窝(四季青店) | cost=107 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 19. 浩海火烧云傣家菜(京广店) | cost=105 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 20. 浩海火烧云傣家菜(东安市场店) | cost=100 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 时光漫步酒店(北京东直门北桥地坛公园店) | cost=500 | type=住宿服务;宾馆酒店;四星级宾馆
- 2. 郁金香温泉花园度假村 | cost=500 | type=体育休闲服务;度假疗养场所;度假村|体育休闲服务;休闲场所;采摘园|住宿服务;住宿服务相关;住宿服务相关
- 3. 北京赛福特饭店 | cost=500 | type=住宿服务;宾馆酒店;三星级宾馆
- 4. 速8精选酒店(北京首钢园金安桥地铁站店) | cost=500 | type=住宿服务;宾馆酒店;经济型连锁酒店
- 5. 北京悦居·中国(原宏悦商务酒店北京望京SOHO店) | cost=500 | type=住宿服务;宾馆酒店;三星级宾馆
- 6. 北京宝格丽酒店 | cost=1400 | type=住宿服务;宾馆酒店;五星级宾馆
- 7. 北京艺栈青年酒店(燕莎亮马桥地铁站店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 米家青年HOSTEL(北京酒仙桥798艺术区店) | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 9. 北京悉昙酒店 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 北京王府井文华东方酒店 | cost=1400 | type=住宿服务;宾馆酒店;五星级宾馆|体育休闲服务;娱乐场所;酒吧

### 14. v3_harder_eval_000263

- 请求：杭州 2025-11-05->2025-11-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- 人群/预算：companion=family_with_elders, budget_level=standard, diet=少辣
- 正向偏好：自然风光 / 历史文化 / 公园 / 本地美食
- 自由文本：带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2025-11-09 | dinner | 无 | 0 | empty_or_none |

**可用 food_pois 候选**

- 1. 和为贵·路哥东北烧烤 | cost=152 | roles=lunch/dinner | cuisine= | avoid=
- 2. 村夫烤鱼·烤蛙(五常大道店) | cost=160 | roles=lunch/dinner | cuisine= | avoid=
- 3. 牛少侠东北烤肉(富阳店) | cost=110 | roles=lunch/dinner | cuisine= | avoid=
- 4. 黄龙海鲜大排档(杭州总店) | cost=320 | roles=lunch/dinner | cuisine=海鲜 | avoid=
- 5. 钱棠·萧山本帮菜(萧山机场大会展店) | cost=212 | roles=lunch/dinner | cuisine= | avoid=
- 6. 印湖杭味·创意杭帮菜(西湖店) | cost=148 | roles=lunch/dinner | cuisine=夜市 | avoid=
- 7. 一席地·本地鸡窝(邮电路店) | cost=136 | roles=lunch/dinner | cuisine= | avoid=
- 8. 江南忆味主题餐厅 | cost=128 | roles=lunch/dinner | cuisine= | avoid=
- 9. 入江南·金奖杭帮菜·浙江菜(虎跑店) | cost=216 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 10. 山野之约·舌尖上的桐庐美食 | cost=164 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 11. 老姑东北人(立涛园店) | cost=156 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 12. 晚酒·阿英川菜馆(一店) | cost=164 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 13. 中国杭帮菜博物馆(虎玉路店) | cost=270 | roles=lunch/dinner | cuisine=家常菜 | avoid=
- 14. 李家小宴家宴(佳源名城店) | cost=186 | roles=lunch/dinner | cuisine=清淡餐厅 | avoid=
- 15. 鱼笑面食(嘉绿名苑东区店) | cost=30 | roles=lunch/dinner | cuisine=清淡餐厅 | avoid=
- 16. 浆小白豆浆夜市(东站店) | cost=38 | roles=lunch/dinner | cuisine=夜市/清淡餐厅 | avoid=
- 17. 肉本家·炭烤肉(杭州浙大总店) | cost=212 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 18. 老秦凉都黄牛肉馆(滨江总店) | cost=156 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 19. 传家(骆家庄西苑一区店) | cost=160 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 20. 瓷·忆赣菜中心(杭州) | cost=238 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 杭州云慢民宿(宋城店) | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 2. 永利活禅酒店(人民广场地铁恒隆店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 3. 杭州大家小院·碳先生智能健康民宿 | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 4. 杭州西湖陇上山居璞玉客栈 | cost=500 | type=住宿服务;旅馆招待所;旅馆招待所
- 5. 韶华卿卿青年旅舍(滨康路地铁站店) | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 6. 杭州拣枝而栖青年旅舍(龙湖滨江天街江陵路地铁站店) | cost=500 | type=住宿服务;旅馆招待所;青年旅舍
- 7. 旅小二青年酒店(金地广场店) | cost=500 | type=住宿服务;住宿服务相关;住宿服务相关
- 8. 杭州拣枝而栖青年旅舍(杭州武林广场宝善桥地铁站店) | cost=500 | type=住宿服务;旅馆招待所;青年旅舍
- 9. 杭州牵手驿家酒店 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店
- 10. 富阳鸿鑫宾馆 | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店

### 15. v3_harder_eval_000297

- 请求：三亚 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- 人群/预算：companion=couple, budget_level=comfortable, diet=无
- 正向偏好：小众展馆 / 咖啡 / 艺术 / 城市漫步 / 特色餐厅
- 自由文本：两个人想要小众、有审美的路线，喜欢展馆、咖啡和特色餐厅，但避开过度商业化景点、跟团游和购物团。预算不需要极省，要符合舒适体验。

**未命中餐饮**

| 日期 | 餐别 | 模型 name | 费用 | 分类 |
| --- | --- | --- | ---: | --- |
| 2026-08-06 | dinner | 无 | 0 | empty_or_none |

**可用 food_pois 候选**

- 1. 创味·民间海南菜·海鲜(林旺店) | cost=192 | roles=lunch/dinner | cuisine=老字号/海鲜 | avoid=
- 2. 椰小鸡·椰子鸡(大东海银泰店) | cost=220 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 3. 小海鲜渔民排档·农家海南菜 | cost=162 | roles=lunch/dinner | cuisine=特色餐厅/海鲜 | avoid=
- 4. 椰小鸡·椰子鸡(海天盛宴总店) | cost=220 | roles=lunch/dinner | cuisine=特色餐厅 | avoid=
- 5. 不仔客海鲜270度海景餐厅 | cost=268 | roles=lunch/dinner | cuisine=特色餐厅/海鲜 | avoid=
- 6. 小海豚连锁海鲜餐厅(海棠湾店) | cost=222 | roles=lunch/dinner | cuisine=特色餐厅/海鲜 | avoid=
- 7. 南门涮肉(三亚店) | cost=220 | roles=lunch/dinner | cuisine=老字号 | avoid=
- 8. 东海龙宫(大东海店) | cost=320 | roles=lunch/dinner | cuisine=老字号/海鲜 | avoid=
- 9. 南海黎村·海南民族菜·海景餐厅(椰梦长廊店) | cost=200 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 10. 疍家佬味道·海南船家菜(亚龙湾店) | cost=194 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 11. 创味·民间海南菜(南山店) | cost=144 | roles=lunch/dinner | cuisine=本地菜 | avoid=
- 12. 创味·民间海南菜(藤桥·免税城店) | cost=168 | roles=lunch/dinner | cuisine=本地菜 | avoid=

**酒店候选名**

- 1. 忆游尤近精致体验客栈 | cost=350 | type=住宿服务;旅馆招待所;旅馆招待所
- 2. 三亚万吉度假公寓 | cost=350 | type=住宿服务;旅馆招待所;旅馆招待所
- 3. 三亚亚特兰蒂斯·棠岸公寓 | cost=350 | type=住宿服务;旅馆招待所;旅馆招待所
- 4. 海云间海景度假酒店公寓(海棠湾保利店) | cost=350 | type=住宿服务;宾馆酒店;宾馆酒店
- 5. 三亚盘云水和民宿(亚龙湾热带森林公园店) | cost=350 | type=住宿服务;住宿服务相关;住宿服务相关
- 6. 猪小弟海景度假公寓 | cost=350 | type=住宿服务;旅馆招待所;旅馆招待所
- 7. 三亚七色海民宿 | cost=350 | type=住宿服务;宾馆酒店;宾馆酒店
- 8. 三亚得居圣岛旅租 | cost=350 | type=住宿服务;旅馆招待所;青年旅舍
- 9. 云合十里青年旅舍 | cost=350 | type=住宿服务;住宿服务相关;住宿服务相关
- 10. 哪里那里海岸精品客栈(三亚亚龙湾店) | cost=500 | type=住宿服务;宾馆酒店;宾馆酒店|住宿服务;旅馆招待所;旅馆招待所
