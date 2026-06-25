---
title: Settings API - Enable endpoint detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-endpoint-detection-rules-opt-in
scraped: 2026-05-12T11:38:58.881074
---

# Settings API - Enable endpoint detection schema table

# Settings API - Enable endpoint detection schema table

* Published Aug 25, 2025

### Включение определения эндпоинтов (`builtin:endpoint-detection-rules-opt-in)`

Включите правила определения эндпоинтов SDv2 (`<your-dynatrace-url>/builtin:endpoint-detection-rules`) вместо жёстко закодированных. Подробнее см. [Service Detection v2 documentation](https://dt-url.net/lu030qq) и [community post](https://dt-url.net/r2230n9).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:endpoint-detection-rules-opt-in` | * `group:service-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules-opt-in` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить правила определения эндпоинтов `enabled` | boolean | Если включено, будут активны новые правила определения эндпоинтов. | Required |