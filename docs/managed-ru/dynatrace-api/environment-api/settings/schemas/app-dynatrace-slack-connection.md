---
title: Settings API - Slack schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-slack-connection
scraped: 2026-05-12T11:43:06.709745
---

# Settings API - Slack schema table

# Settings API - Slack schema table

* Published Dec 05, 2023

### Slack (`app:dynatrace.slack:connection)`

Данные аутентификации для Slack API

(подробнее в [документации по Slack API](https://api.slack.com/authentication/basics/ "Открыть документ Slack"))

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.slack:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.slack:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.slack:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Укажите уникальное и однозначно идентифицируемое имя подключения к вашему приложению Slack. | Required |
| Токен бота `token` | secret | Токен бота, полученный из интерфейса Slack App Management.  Токен бота в формате `xoxb-******` | Required |