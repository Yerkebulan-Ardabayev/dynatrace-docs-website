---
title: Settings API - Ingest routing configuration (events.security) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-routing
scraped: 2026-05-12T11:42:52.645530
---

# Settings API - Ingest routing configuration (events.security) schema table

# Settings API - Ingest routing configuration (events.security) schema table

* Published Aug 25, 2025

### Конфигурация маршрутизации ingest (events.security) (`builtin:openpipeline.events.security.routing)`

Содержит конфигурацию маршрутизации

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:openpipeline.events.security.routing` | * `group:openpipeline.all.routing` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.events.security.routing` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.events.security.routing` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.events.security.routing` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Маршрутизация для pipeline `routingEntries` | [RoutingEntry](#RoutingEntry)[] | - | Required |

##### Объект `RoutingEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Тип pipeline `pipelineType` | enum | Возможные значения: * `custom` * `builtin` | Required |
| ID pipeline `pipelineId` | setting | - | Required |
| ID встроенного pipeline `builtinPipelineId` | text | - | Required |
| Запрос, определяющий, должна ли запись быть направлена в целевой pipeline этого правила. `matcher` | text | - | Required |
| Описание `description` | text | - | Required |