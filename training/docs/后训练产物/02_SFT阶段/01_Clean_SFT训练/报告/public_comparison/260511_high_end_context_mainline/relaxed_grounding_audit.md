# Relaxed Grounding Audit

This is a side-channel audit only. It does not modify `rule_eval_report.json` or the official hard_pass numbers.

Relaxed matching applies NFKC, lowercase, a small traditional-to-simplified POI character table, bracket/space/punctuation removal, and the existing city-prefix / POI-suffix aliases.

## hard pass estimate

| Run | Records | Parsed | Strict hard_pass | Relaxed estimate | Recovered hard_pass |
| --- | ---: | ---: | ---: | ---: | ---: |
| standard/base | 200 | 198 | 178/198 (89.90%) | 178/198 (89.90%) | 0 |
| standard/legacy_b | 200 | 199 | 186/199 (93.47%) | 186/199 (93.47%) | 0 |
| standard/lr8e-5 | 200 | 198 | 191/198 (96.46%) | 191/198 (96.46%) | 0 |
| hard/base | 300 | 299 | 249/299 (83.28%) | 249/299 (83.28%) | 0 |
| hard/legacy_b | 300 | 300 | 281/300 (93.67%) | 281/300 (93.67%) | 0 |
| hard/lr8e-5 | 300 | 299 | 275/299 (91.97%) | 275/299 (91.97%) | 0 |

## item grounding

| Run | Meal strict | Meal relaxed | Meal recovered | Meal semantic strict | Meal semantic relaxed | Attraction strict | Attraction relaxed | Hotel strict | Hotel relaxed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| standard/base | 2031/2051 (99.02%) | 2031/2051 (99.02%) | 0 | 2034/2051 (99.17%) | 2034/2051 (99.17%) | 1196/1197 (99.92%) | 1196/1197 (99.92%) | 669/676 (98.96%) | 669/676 (98.96%) |
| standard/legacy_b | 2065/2067 (99.90%) | 2065/2067 (99.90%) | 0 | 2066/2067 (99.95%) | 2066/2067 (99.95%) | 1587/1591 (99.75%) | 1587/1591 (99.75%) | 490/490 (100.00%) | 490/490 (100.00%) |
| standard/lr8e-5 | 2046/2049 (99.85%) | 2046/2049 (99.85%) | 0 | 2048/2049 (99.95%) | 2048/2049 (99.95%) | 1575/1578 (99.81%) | 1575/1578 (99.81%) | 485/485 (100.00%) | 485/485 (100.00%) |
| hard/base | 3714/3762 (98.72%) | 3714/3762 (98.72%) | 0 | 3727/3762 (99.07%) | 3727/3762 (99.07%) | 1967/1971 (99.80%) | 1967/1971 (99.80%) | 1214/1228 (98.86%) | 1214/1228 (98.86%) |
| hard/legacy_b | 3770/3780 (99.74%) | 3770/3780 (99.74%) | 0 | 3775/3780 (99.87%) | 3775/3780 (99.87%) | 2861/2867 (99.79%) | 2861/2867 (99.79%) | 956/960 (99.58%) | 956/960 (99.58%) |
| hard/lr8e-5 | 3763/3771 (99.79%) | 3763/3771 (99.79%) | 0 | 3768/3771 (99.92%) | 3768/3771 (99.92%) | 2863/2877 (99.51%) | 2863/2877 (99.51%) | 954/958 (99.58%) | 954/958 (99.58%) |

## fixed metrics

| Run | Fixed metric counts | Meal miss reason counts |
| --- | --- | --- |
| standard/base | `{}` | `{"invalid:unknown_food_semantics": 8, "semantic_fallback:food_semantic_fallback": 3, "invalid:hotel_or_lodging_name": 1, "invalid:generic_lodging_meal": 1, "invalid:non_food_poi_name": 7}` |
| standard/legacy_b | `{}` | `{"invalid:unknown_food_semantics": 1, "semantic_fallback:food_semantic_fallback": 1}` |
| standard/lr8e-5 | `{}` | `{"invalid:unknown_food_semantics": 1, "semantic_fallback:food_semantic_fallback": 2}` |
| hard/base | `{}` | `{"semantic_fallback:food_semantic_fallback": 13, "invalid:non_food_poi_name": 14, "invalid:unknown_food_semantics": 18, "invalid:hotel_or_lodging_name": 2, "invalid:generic_lodging_meal": 1}` |
| hard/legacy_b | `{}` | `{"invalid:unknown_food_semantics": 5, "semantic_fallback:food_semantic_fallback": 5}` |
| hard/lr8e-5 | `{}` | `{"invalid:unknown_food_semantics": 3, "semantic_fallback:food_semantic_fallback": 5}` |

## Recovered Hard-Pass Records

### standard/base

- none

### standard/legacy_b

- none

### standard/lr8e-5

- none

### hard/base

- none

### hard/legacy_b

- none

### hard/lr8e-5

- none

## recovered meal examples

### standard/base

- none

### standard/legacy_b

- none

### standard/lr8e-5

- none

### hard/base

- none

### hard/legacy_b

- none

### hard/lr8e-5

- none

## still invalid meal examples

### standard/base

- `planner_standard200_realbudget_eval_000040` 2026-07-07 dinner: `南京海底世界` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000040` 2026-07-08 dinner: `南京欢乐谷` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000092` 2026-08-05 dinner: `无相颂蔬食厨坊` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000092` 2026-08-09 dinner: `无相颂蔬食厨坊` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000096` 2026-05-12 lunch: `南京海底世界` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000096` 2026-05-12 dinner: `南京海底世界` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000103` 2026-05-09 lunch: `海德万顺·精致淮扬菜·宴会厅` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000103` 2026-05-12 dinner: `扬州大运河文化旅游度假区·虹桥坊酒店` reason=hotel_or_lodging_name
- `planner_standard200_realbudget_eval_000127` 2026-06-24 breakfast: `嘉华鲜花饼·甄选工坊(昆明老街店)` reason=unknown_food_semantics
- `planner_standard200_realbudget_eval_000140` 2026-06-08 dinner: `杭州开元森泊度假酒店餐厅` reason=generic_lodging_meal

### standard/legacy_b

- `planner_standard200_realbudget_eval_000092` 2026-08-06 dinner: `无相颂蔬食厨坊` reason=unknown_food_semantics

### standard/lr8e-5

- `planner_standard200_realbudget_eval_000092` 2026-08-06 lunch: `无相颂蔬食厨坊` reason=unknown_food_semantics

### hard/base

- `planner_hard_realbudget_eval_000002` 2026-05-02 dinner: `钱潮夜市(地铁东城购物中心店)` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000002` 2026-05-03 dinner: `闲林埠老街` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000012` 2025-05-09 dinner: `西工小街` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000021` 2026-06-23 dinner: `老太公海鸭·宁波菜(上海总店)` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000023` 2026-09-04 dinner: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000023` 2026-09-05 lunch: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000023` 2026-09-05 dinner: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000023` 2026-09-06 lunch: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000023` 2026-09-06 dinner: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name
- `planner_hard_realbudget_eval_000023` 2026-09-07 lunch: `洱海月湿地公园附近的餐厅` reason=non_food_poi_name

### hard/legacy_b

- `planner_hard_realbudget_eval_000008` 2026-05-11 dinner: `里白云南家常菜` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000078` 2026-09-04 lunch: `里白云南家常菜` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000148` 2025-05-08 dinner: `梅溪湖国际文化艺术中心大剧院` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000261` 2026-02-07 dinner: `虾米·闽南菜(中山路店)` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000261` 2026-02-09 lunch: `虾米·闽南菜(中山路店)` reason=unknown_food_semantics

### hard/lr8e-5

- `planner_hard_realbudget_eval_000024` 2026-05-11 lunch: `宴遇·鲁菜(山东大厦店)` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000181` 2026-05-13 dinner: `荔枝大剧院(鼓楼·荔枝广场店)` reason=unknown_food_semantics
- `planner_hard_realbudget_eval_000283` 2025-11-10 dinner: `秦湘家常菜(五一广场店)` reason=unknown_food_semantics
