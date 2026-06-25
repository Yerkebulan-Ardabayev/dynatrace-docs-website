---
title: Settings API - Metric query schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-metric-query
scraped: 2026-05-12T11:43:08.488192
---

# Settings API - Metric query schema table

# Settings API - Metric query schema table

* Published Dec 05, 2023

### Метрический запрос (`builtin:metric.query)`

Сохранённый метрический запрос позволяет вычислять значения метрик через метрическое выражение.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:metric.query` | * `group:metrics` | `metric` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.query` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:metric.query` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.query` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Запрос `metricSelector` | text | - | Required |