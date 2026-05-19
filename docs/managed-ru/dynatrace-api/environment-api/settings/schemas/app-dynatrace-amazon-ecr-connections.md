---
title: Settings API - Amazon ECR schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-amazon-ecr-connections
scraped: 2026-05-12T11:39:30.210890
---

# Settings API - Amazon ECR schema table

# Settings API - Amazon ECR schema table

* Published Mar 17, 2025

### Amazon ECR (`app:dynatrace.amazon.ecr:connections)`

Приём данных об уязвимостях и событий сканирования из Amazon Elastic Container Registry.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.amazon.ecr:connections` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.ecr:connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Укажите уникальное отображаемое имя для вашего подключения. | Required |
| Тип сканирования Amazon ECR `scan_type` | enum | Тип сканирования, которое будет выполнено Возможные значения: * `basic` * `enhanced` | Required |
| ID токена приёма `ingest_token_id` | text | ID токена приёма Grail, используемого в этом подключении | Optional |