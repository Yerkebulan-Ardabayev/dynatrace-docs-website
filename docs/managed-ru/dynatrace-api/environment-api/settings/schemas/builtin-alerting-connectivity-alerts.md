---
title: Settings API - Connectivity alerts schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-alerting-connectivity-alerts
scraped: 2026-05-12T11:41:43.753922
---

# Settings API - Connectivity alerts schema table

# Settings API - Connectivity alerts schema table

* Published Dec 05, 2023

### Оповещения о связности (`builtin:alerting.connectivity-alerts)`

Включите или отключите проблемы TCP-связности для процессов этой группы процессов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:alerting.connectivity-alerts` | - | `PROCESS_GROUP` - Process Group |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:alerting.connectivity-alerts` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Проблемы TCP-связности `connectivityAlerts` | boolean | - | Required |