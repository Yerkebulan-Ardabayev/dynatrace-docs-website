---
title: Settings API - PagerDuty Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-pagerduty-connection
scraped: 2026-05-12T11:45:26.969248
---

# Settings API - PagerDuty Connections schema table

# Settings API - PagerDuty Connections schema table

* Published Dec 05, 2023

### Подключения PagerDuty (`app:dynatrace.pagerduty:connection)`

Учётные данные для приложения PagerDuty

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.pagerduty:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.pagerduty:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения PagerDuty | Required |
| URL API PagerDuty `url` | text | URL эндпоинта API PagerDuty | Required |
| Токен API `token` | secret | Токен для эндпоинта API PagerDuty | Required |