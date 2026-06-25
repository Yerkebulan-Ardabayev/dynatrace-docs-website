---
title: Settings API - Limit outbound connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dt-javascript-runtime-allowed-outbound-connections
scraped: 2026-05-12T11:43:19.870451
---

# Settings API - Limit outbound connections schema table

# Settings API - Limit outbound connections schema table

* Published Dec 05, 2023

### Ограничение исходящих соединений (`builtin:dt-javascript-runtime.allowed-outbound-connections)`

Можно ограничить доступ к публичным эндпоинтам из функций, запущенных в Dynatrace JavaScript Runtime, например к backend'ам приложений и функций, написанных в Dashboards, Notebooks и Automations app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dt-javascript-runtime.allowed-outbound-connections` | * `group:dt-javascript-runtime` * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dt-javascript-runtime.allowed-outbound-connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `allowedOutboundConnections` | [AllowedHostsList](#AllowedHostsList) | - | Required |

##### Объект `AllowedHostsList`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ограничить исходящие соединения эндпоинтами в allowlist `enforced` | boolean | Если включено, Dynatrace JavaScript Runtime сможет подключаться только к указанным хостам. | Required |
| Allowlist `hostList` | set | Хост, к которому должны подключаться backend'ы приложений. | Required |