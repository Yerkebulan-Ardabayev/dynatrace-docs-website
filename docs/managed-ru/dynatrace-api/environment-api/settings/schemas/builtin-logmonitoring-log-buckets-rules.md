---
title: Settings API - Log buckets schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-buckets-rules
scraped: 2026-05-12T11:48:49.995468
---

# Settings API - Log buckets schema table

# Settings API - Log buckets schema table

* Published Dec 05, 2023

### Бакеты логов (`builtin:logmonitoring.log-buckets-rules)`

Логи Dynatrace хранятся в бакетах. Каждому бакету можно задать уникальный период хранения логов (по умолчанию 35 дней). Кроме того, бакеты позволяют задавать уникальные правила доступа к разным логам или областям логов. Для создания и управления бакетами перейдите в [bucket permissions](https://dt-url.net/vc034se). Подробнее об использовании бакетов для логов см. [documentation](https://dt-url.net/ep234n2).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-buckets-rules` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-buckets-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя правила `ruleName` | text | - | Required |
| Бакет `bucketName` | text | «Бакет»: срок хранения логов. Выберите подходящий бакет. | Required |
| Сопоставитель (DQL) `matcher` | text | - | Required |