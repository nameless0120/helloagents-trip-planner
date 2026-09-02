# few-shot 示例数字与工具 hint 一致性审查

| 字段 | 示例值 | 命中数 | 工具一致 | 工具不一致 | 工具匹配不完整 |
| --- | ---: | ---: | ---: | ---: | ---: |
| total_hotels | 800 | 10 | 8 | 2 | 0 |
| total_attractions | 200 | 23 | 0 | 22 | 1 |
| total_meals | 520 | 21 | 0 | 18 | 3 |

## 命中样本明细

| record_id | 命中判断 | 输出示例字段 | 工具hint重算 | 工具未匹配 |
| --- | --- | --- | --- | --- |
| v3_harder_eval_000004 | total_hotels:tool_consistent; total_meals:tool_mismatch(expected=467) | {'total_hotels': 800, 'total_attractions': 160, 'total_meals': 520} | {'total_hotels': 800, 'total_attractions': 80, 'total_meals': 467} |  |
| v3_harder_eval_000006 | total_attractions:tool_mismatch(expected=30) | {'total_hotels': 1650, 'total_attractions': 200, 'total_meals': 525} | {'total_hotels': 1650, 'total_attractions': 30, 'total_meals': 1371} |  |
| v3_harder_eval_000005 | total_meals:tool_incomplete | {'total_hotels': 1200, 'total_attractions': 1100, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 685, 'total_meals': 996} | {'total_meals': ['无']} |
| v3_harder_eval_000002 | total_meals:tool_mismatch(expected=1568) | {'total_hotels': 1000, 'total_attractions': 510, 'total_meals': 520} | {'total_hotels': 750, 'total_attractions': 1320, 'total_meals': 1568} |  |
| v3_harder_eval_000012 | total_hotels:tool_mismatch(expected=700) | {'total_hotels': 800, 'total_attractions': 960, 'total_meals': 1296} | {'total_hotels': 700, 'total_attractions': 1280, 'total_meals': 1584} |  |
| v3_harder_eval_000013 | total_attractions:tool_mismatch(expected=420) | {'total_hotels': 1600, 'total_attractions': 200, 'total_meals': 654} | {'total_hotels': 1600, 'total_attractions': 420, 'total_meals': 670} |  |
| v3_harder_eval_000024 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 480, 'total_meals': 480} | {'total_hotels': 800, 'total_attractions': 320, 'total_meals': 453} |  |
| v3_harder_eval_000034 | total_attractions:tool_mismatch(expected=130) | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 324} | {'total_hotels': 800, 'total_attractions': 130, 'total_meals': 498} |  |
| v3_harder_eval_000029 | total_attractions:tool_mismatch(expected=80) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 1020} | {'total_hotels': 1500, 'total_attractions': 80, 'total_meals': 2096} |  |
| v3_harder_eval_000042 | total_meals:tool_incomplete | {'total_hotels': 600, 'total_attractions': 1020, 'total_meals': 520} | {'total_hotels': 600, 'total_attractions': 2460, 'total_meals': 560} | {'total_meals': ['正阳楼学府店特色东北菜', '金刚山烧烤', '金刚山烧烤']} |
| v3_harder_eval_000045 | total_meals:tool_mismatch(expected=1530) | {'total_hotels': 1200, 'total_attractions': 1200, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 240, 'total_meals': 1530} | {'total_attractions': ['济南泉城公园', '济南泉城公园']} |
| v3_harder_eval_000052 | total_attractions:tool_mismatch(expected=780) | {'total_hotels': 1000, 'total_attractions': 200, 'total_meals': 1008} | {'total_hotels': 750, 'total_attractions': 780, 'total_meals': 1572} |  |
| v3_harder_eval_000072 | total_meals:tool_mismatch(expected=1992) | {'total_hotels': 600, 'total_attractions': 1130, 'total_meals': 520} | {'total_hotels': 600, 'total_attractions': 1860, 'total_meals': 1992} |  |
| v3_harder_eval_000076 | total_attractions:tool_mismatch(expected=480) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 486} | {'total_hotels': 1500, 'total_attractions': 480, 'total_meals': 1443} |  |
| v3_harder_eval_000082 | total_meals:tool_incomplete | {'total_hotels': 750, 'total_attractions': 1200, 'total_meals': 520} | {'total_hotels': 750, 'total_attractions': 1288, 'total_meals': 1180} | {'total_meals': ['文体中心夜市']} |
| v3_harder_eval_000094 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 240, 'total_meals': 240} | {'total_hotels': 800, 'total_attractions': 320, 'total_meals': 546} |  |
| v3_harder_eval_000084 | total_attractions:tool_mismatch(expected=105) | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 800, 'total_attractions': 105, 'total_meals': 349} |  |
| v3_harder_eval_000095 | total_meals:tool_mismatch(expected=1163) | {'total_hotels': 1200, 'total_attractions': 1100, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 175, 'total_meals': 1163} |  |
| v3_harder_eval_000100 | total_attractions:tool_mismatch(expected=400) | {'total_hotels': 1800, 'total_attractions': 200, 'total_meals': 510} | {'total_hotels': 1800, 'total_attractions': 400, 'total_meals': 4000} |  |
| v3_harder_eval_000105 | total_attractions:tool_incomplete | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 1200, 'total_attractions': 45, 'total_meals': 739} | {'total_attractions': ['南京大牌档(1912总统府店)']} |
| v3_harder_eval_000114 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 480, 'total_meals': 261} | {'total_hotels': 800, 'total_attractions': 400, 'total_meals': 702} |  |
| v3_harder_eval_000115 | total_meals:tool_mismatch(expected=690) | {'total_hotels': 1200, 'total_attractions': 210, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 185, 'total_meals': 690} |  |
| v3_harder_eval_000123 | total_attractions:tool_mismatch(expected=390) | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 1600, 'total_attractions': 390, 'total_meals': 1005} |  |
| v3_harder_eval_000137 | total_meals:tool_mismatch(expected=3040) | {'total_hotels': 1200, 'total_attractions': 300, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 280, 'total_meals': 3040} |  |
| v3_harder_eval_000153 | total_meals:tool_mismatch(expected=1934) | {'total_hotels': 1800, 'total_attractions': 120, 'total_meals': 520} | {'total_hotels': 1800, 'total_attractions': 40, 'total_meals': 1934} |  |
| v3_harder_eval_000152 | total_attractions:tool_mismatch(expected=208) | {'total_hotels': 600, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 600, 'total_attractions': 208, 'total_meals': 1992} |  |
| v3_harder_eval_000175 | total_attractions:tool_mismatch(expected=105); total_meals:tool_mismatch(expected=1135) | {'total_hotels': 1400, 'total_attractions': 200, 'total_meals': 520} | {'total_hotels': 1400, 'total_attractions': 105, 'total_meals': 1135} |  |
| v3_harder_eval_000184 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 240, 'total_meals': 334} | {'total_hotels': 800, 'total_attractions': 160, 'total_meals': 578} |  |
| v3_harder_eval_000187 | total_meals:tool_mismatch(expected=1042) | {'total_hotels': 1200, 'total_attractions': 400, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 580, 'total_meals': 1042} |  |
| v3_harder_eval_000186 | total_attractions:tool_mismatch(expected=480) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 720} | {'total_hotels': 1500, 'total_attractions': 480, 'total_meals': 1416} |  |
| v3_harder_eval_000204 | total_meals:tool_mismatch(expected=531) | {'total_hotels': 1000, 'total_attractions': 240, 'total_meals': 520} | {'total_hotels': 1000, 'total_attractions': 30, 'total_meals': 531} |  |
| v3_harder_eval_000203 | total_attractions:tool_mismatch(expected=150) | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 1600, 'total_attractions': 150, 'total_meals': 1929} | {'total_meals': ['曙光烧烤·20年老牌烤串(吴井店)', '四方小炒·云南菜小当家(同德店)']} |
| v3_harder_eval_000207 | total_meals:tool_mismatch(expected=1550) | {'total_hotels': 1200, 'total_attractions': 400, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 480, 'total_meals': 1550} |  |
| v3_harder_eval_000211 | total_attractions:tool_mismatch(expected=104) | {'total_hotels': 2250, 'total_attractions': 200, 'total_meals': 1026} | {'total_hotels': 2250, 'total_attractions': 104, 'total_meals': 2436} |  |
| v3_harder_eval_000214 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 240, 'total_meals': 330} | {'total_hotels': 800, 'total_attractions': 240, 'total_meals': 693} |  |
| v3_harder_eval_000215 | total_meals:tool_mismatch(expected=708) | {'total_hotels': 1200, 'total_attractions': 1050, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 245, 'total_meals': 708} |  |
| v3_harder_eval_000218 | total_attractions:tool_mismatch(expected=315) | {'total_hotels': 2250, 'total_attractions': 200, 'total_meals': 729} | {'total_hotels': 1500, 'total_attractions': 315, 'total_meals': 1260} |  |
| v3_harder_eval_000232 | total_hotels:tool_mismatch(expected=600) | {'total_hotels': 800, 'total_attractions': 0, 'total_meals': 768} | {'total_hotels': 600, 'total_attractions': 0, 'total_meals': 1912} |  |
| v3_harder_eval_000235 | total_meals:tool_mismatch(expected=1175) | {'total_hotels': 1200, 'total_attractions': 520, 'total_meals': 520} | {'total_hotels': 1200, 'total_attractions': 305, 'total_meals': 1175} |  |
| v3_harder_eval_000241 | total_attractions:tool_mismatch(expected=80) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 1020} | {'total_hotels': 2250, 'total_attractions': 80, 'total_meals': 1706} |  |
| v3_harder_eval_000249 | total_meals:tool_mismatch(expected=1256) | {'total_hotels': 1650, 'total_attractions': 440, 'total_meals': 520} | {'total_hotels': 1650, 'total_attractions': 440, 'total_meals': 1256} |  |
| v3_harder_eval_000245 | total_attractions:tool_mismatch(expected=52) | {'total_hotels': 1200, 'total_attractions': 200, 'total_meals': 480} | {'total_hotels': 1200, 'total_attractions': 52, 'total_meals': 438} | {'total_meals': ['老细屋里私房菜馆']} |
| v3_harder_eval_000254 | total_meals:tool_mismatch(expected=712) | {'total_hotels': 900, 'total_attractions': 480, 'total_meals': 520} | {'total_hotels': 900, 'total_attractions': 240, 'total_meals': 712} |  |
| v3_harder_eval_000258 | total_attractions:tool_mismatch(expected=156) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 1200} | {'total_hotels': 1500, 'total_attractions': 156, 'total_meals': 1680} |  |
| v3_harder_eval_000262 | total_attractions:tool_mismatch(expected=208) | {'total_hotels': 600, 'total_attractions': 200, 'total_meals': 1080} | {'total_hotels': 600, 'total_attractions': 208, 'total_meals': 1832} |  |
| v3_harder_eval_000274 | total_hotels:tool_consistent | {'total_hotels': 800, 'total_attractions': 480, 'total_meals': 493} | {'total_hotels': 800, 'total_attractions': 240, 'total_meals': 465} | {'total_meals': ['黄山老妈·土菜馆(老街店)', '黄山老妈·土菜馆(老街店)', '黄山老妈·土菜馆(老街店)']} |
| v3_harder_eval_000276 | total_attractions:tool_mismatch(expected=1059) | {'total_hotels': 1650, 'total_attractions': 200, 'total_meals': 1440} | {'total_hotels': 1650, 'total_attractions': 1059, 'total_meals': 2325} |  |
| v3_harder_eval_000284 | total_hotels:tool_consistent; total_meals:tool_mismatch(expected=1422) | {'total_hotels': 800, 'total_attractions': 540, 'total_meals': 520} | {'total_hotels': 800, 'total_attractions': 320, 'total_meals': 1422} |  |
| v3_harder_eval_000283 | total_attractions:tool_mismatch(expected=80); total_meals:tool_mismatch(expected=2458) | {'total_hotels': 1600, 'total_attractions': 200, 'total_meals': 520} | {'total_hotels': 1600, 'total_attractions': 80, 'total_meals': 2458} |  |
| v3_harder_eval_000299 | total_attractions:tool_mismatch(expected=370) | {'total_hotels': 1500, 'total_attractions': 200, 'total_meals': 498} | {'total_hotels': 1500, 'total_attractions': 370, 'total_meals': 1992} |  |
