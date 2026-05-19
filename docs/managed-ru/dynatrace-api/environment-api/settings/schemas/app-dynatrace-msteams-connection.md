---
title: Settings API - Microsoft Teams schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-msteams-connection
scraped: 2026-05-12T11:46:35.324481
---

# Settings API - Microsoft Teams schema table

# Settings API - Microsoft Teams schema table

* Published Dec 05, 2023

### Microsoft Teams (`app:dynatrace.msteams:connection)`

Данные аутентификации для приложения Microsoft Teams

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.msteams:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.msteams:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.msteams:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.msteams:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения Microsoft Teams | Required |
| Целевая команда Microsoft Team `teamName` | text | Необязательно | Optional |
| Имя целевого канала `channelName` | text | Необязательно | Optional |
| URL вебхука `webhook` | secret | URL вебхука, ведущий на канал  URL создаётся с помощью приложения `Incoming Webhook` в Teams | Required |