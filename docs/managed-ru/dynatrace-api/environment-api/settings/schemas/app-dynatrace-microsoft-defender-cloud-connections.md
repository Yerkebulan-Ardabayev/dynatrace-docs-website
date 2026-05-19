---
title: Settings API - Microsoft Defender for Cloud schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-microsoft-defender-cloud-connections
scraped: 2026-05-12T11:45:42.812298
---

# Settings API - Microsoft Defender for Cloud schema table

# Settings API - Microsoft Defender for Cloud schema table

* Published Jun 30, 2025

### Microsoft Defender for Cloud (`app:dynatrace.microsoft.defender.cloud:connections)`

Приём данных об уязвимостях и событий сканирования из Microsoft Defender for Cloud.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.microsoft.defender.cloud:connections` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Укажите уникальное отображаемое имя для вашего подключения. | Required |
| Использовать доверенный сервис? `use_trusted_service` | enum | Экспортировать как доверенный сервис? Возможные значения: * `true` * `false` | Required |
| ID токена приёма `ingest_token_id` | text | ID токена приёма Grail, используемого в этом подключении | Optional |