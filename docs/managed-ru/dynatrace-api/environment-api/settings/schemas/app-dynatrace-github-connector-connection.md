---
title: Settings API - GitHub Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-github-connector-connection
scraped: 2026-05-12T11:46:12.955010
---

# Settings API - GitHub Connections schema table

# Settings API - GitHub Connections schema table

* Published Aug 26, 2024

### Подключения GitHub (`app:dynatrace.github.connector:connection)`

Данные аутентификации GitHub

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.github.connector:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.github.connector:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения GitHub | Required |
| Тип `type` | enum | Тип используемого метода аутентификации Возможные значения: * `pat` | Required |
| Токен `token` | secret | Токен для выбранного типа аутентификации | Required |