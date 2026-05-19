---
title: Settings API - Amazon GuardDuty schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-amazon-guardduty-connections
scraped: 2026-05-12T11:42:29.918296
---

# Settings API - Amazon GuardDuty schema table

# Settings API - Amazon GuardDuty schema table

* Published Sep 25, 2025

### Amazon GuardDuty (`app:dynatrace.amazon.guardduty:connections)`

Приём данных о безопасности из Amazon GuardDuty.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.amazon.guardduty:connections` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Укажите уникальное отображаемое имя для вашего подключения. | Required |
| ID токена приёма `ingest_token_id` | text | ID токена приёма Grail, используемого в этом подключении | Optional |