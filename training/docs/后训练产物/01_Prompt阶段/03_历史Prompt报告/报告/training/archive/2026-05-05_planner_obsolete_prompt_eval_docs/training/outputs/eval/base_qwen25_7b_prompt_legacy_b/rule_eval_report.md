# Rule Eval Report: base_qwen25_7b_prompt_v2

- records: 91
- generations: `training/outputs/eval/base_qwen25_7b_prompt_v2/generations.jsonl`
- records_path: `training/data/v2/sft/records_eval.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 16 | 16 | 100.00% |
| budget_arithmetic_consistent | 16 | 16 | 100.00% |
| budget_consistent | 16 | 16 | 100.00% |
| budget_level_aligned | 14 | 16 | 87.50% |
| budget_preference_aligned | 14 | 16 | 87.50% |
| budget_within_user_budget | 16 | 16 | 100.00% |
| city_ok | 16 | 16 | 100.00% |
| date_range_ok | 16 | 16 | 100.00% |
| day_dates_ok | 16 | 16 | 100.00% |
| day_index_ok | 16 | 16 | 100.00% |
| days_len_ok | 16 | 16 | 100.00% |
| hard_pass | 16 | 16 | 100.00% |
| invalid_hotel_name_ok | 16 | 16 | 100.00% |
| json_extract_ok | 91 | 91 | 100.00% |
| location_object_ok | 16 | 16 | 100.00% |
| meal_complete | 16 | 16 | 100.00% |
| middle_hotel_ok | 16 | 16 | 100.00% |
| schema_ok | 16 | 91 | 17.58% |
| weather_dates_ok | 16 | 16 | 100.00% |
| weather_match | 16 | 16 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "schema": 75,
  "budget_preference_mismatch": 2
}
```

## Failure Examples

### v2_request_000314
- request: 青岛 2026-08-29->2026-09-01 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '历史文化']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000064
- request: 杭州 2025-05-01->2025-05-04 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['博物馆', '自然风光']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000927
- request: 长沙 2026-04-26->2026-04-29 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['城市公园', '历史文化', '城市地标']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000866
- request: 南京 2026-04-24->2026-04-28 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '主题乐园', '摄影', '历史文化']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000565
- request: 深圳 2026-06-30->2026-07-03 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '历史文化', '海滨度假', '美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000655
- request: 上海 2026-05-31->2026-06-03 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['第一次来', '海滨度假', '美食', '历史文化']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000662
- request: 厦门 2026-07-30->2026-07-31 days=2 transport=公共交通 hotel=经济型酒店 prefs=['历史文化', '购物商圈', '自然风光']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000234
- request: 青岛 2026-04-17->2026-04-21 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['主题乐园', '自然风光', '户外轻徒步']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000183
- request: 南京 2026-05-03->2026-05-05 days=3 transport=打车 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '城市公园']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000381
- request: 北京 2026-04-27->2026-04-29 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['第一次来', '城市地标', '休闲慢游']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000992
- request: 洛阳 2026-06-30->2026-07-03 days=4 transport=公共交通 hotel=经济型酒店 prefs=['艺术', '海滨度假', '美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000514
- request: 珠海 2026-05-04->2026-05-06 days=3 transport=自驾 hotel=舒适型酒店 prefs=['主题乐园', '美食', '历史文化', '素食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000770
- request: 三亚 2025-11-02->2025-11-03 days=2 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '购物商圈', '美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.1.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000599
- request: 哈尔滨 2026-04-01->2026-04-03 days=3 transport=打车 hotel=经济型酒店 prefs=['购物商圈', '城市地标', '城市漫步', '摄影']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000661
- request: 宁波 2026-07-30->2026-08-02 days=4 transport=自驾 hotel=民宿 prefs=['夜市夜景', '历史文化']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000832
- request: 昆明 2026-05-31->2026-06-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '主题乐园', '历史文化', '博物馆']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000175
- request: 北京 2026-06-15->2026-06-18 days=4 transport=打车 hotel=民宿 prefs=['历史文化', '休闲慢游', '美食', '摄影']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000414
- request: 青岛 2026-05-03->2026-05-07 days=5 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '自然风光', '摄影']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000323
- request: 成都 2026-04-01->2026-04-03 days=3 transport=打车 hotel=经济型酒店 prefs=['美食', '博物馆', '小众展览']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v2_request_000102
- request: 上海 2026-07-30->2026-08-01 days=3 transport=自驾 hotel=经济型酒店 prefs=['亲子', '自然风光', '博物馆', '城市漫步']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`
