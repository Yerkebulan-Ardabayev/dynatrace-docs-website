---
title: Settings API - OneAgent Business events capturing variants schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-http-capturing-variants
scraped: 2026-05-12T11:46:36.501591
---

# Settings API - OneAgent Business events capturing variants schema table

# Settings API - OneAgent Business events capturing variants schema table

* Published Mar 17, 2025

### Варианты захвата Business events для OneAgent (`builtin:bizevents.http.capturing-variants)`

Варианты захвата OneAgent.

Правила захвата указывают OneAgent захватывать обобщённые content-type; варианты захвата добавьте ниже.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents.http.capturing-variants` | * `group:business-analytics.business-events-sources` * `group:business-analytics` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents.http.capturing-variants` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставитель Content-type `contentTypeMatcher` | enum | Возможные значения: * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Значение сопоставления Content-type `contentTypeValue` | text | - | Required |
| Парсер `parser` | enum | Возможные значения: * `JSON` * `XML` * `URL encoded` * `Text` * `Raw` | Required |