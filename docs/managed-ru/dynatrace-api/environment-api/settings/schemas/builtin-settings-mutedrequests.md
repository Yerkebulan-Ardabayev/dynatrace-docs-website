---
title: Settings API - Muted requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-settings-mutedrequests
scraped: 2026-05-12T11:39:16.262269
---

# Settings API - Muted requests schema table

# Settings API - Muted requests schema table

* Published Dec 05, 2023

### Приглушённые запросы (`builtin:settings.mutedrequests)`

Конфигурация для указания приглушённых запросов для конкретного сервиса. У каждого сервиса может быть несколько приглушённых запросов.

Dynatrace позволяет приглушать автоматические оповещения для отдельных неважных запросов сервиса. Это также исключит их из диаграммы сервиса, чтобы вы могли сосредоточиться на производительности запросов, влияющих на клиентов. Узнайте больше о приглушённых запросах в нашей [help](https://dt-url.net/ze62t5p "Visit dynatrace.com")

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:settings.mutedrequests` | - | `SERVICE` - Service |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.mutedrequests` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:settings.mutedrequests` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.mutedrequests` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имена приглушённых запросов `mutedRequestNames` | set | - | Required |