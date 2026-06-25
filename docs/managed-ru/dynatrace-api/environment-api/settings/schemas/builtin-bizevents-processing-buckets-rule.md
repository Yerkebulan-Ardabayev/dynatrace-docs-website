---
title: Settings API - Business event bucket assignment schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-buckets-rule
scraped: 2026-05-12T11:47:23.219520
---

# Settings API - Business event bucket assignment schema table

# Settings API - Business event bucket assignment schema table

* Published Dec 05, 2023

### Назначение бакетов для Business events (`builtin:bizevents-processing-buckets.rule)`

Business events можно хранить в разных бакетах. Первое пользовательское правило, которое совпадёт, определит назначение бакета. Если ни одно правило не совпадёт, будет использован бакет по умолчанию.

О создании пользовательских бакетов и других возможностях см. [our documentation](https://dt-url.net/4c034xt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-buckets.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-buckets.rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя правила `ruleName` | text | - | Required |
| Бакет `bucketName` | text | События сохраняются в выбранном бакете. Содержимое бакета можно анализировать в log & event viewer. (`<your-dynatrace-url>//ui/logs-events?advancedQueryMode=true&query=fetch+bizevents`) | Required |
| Сопоставитель (DQL) `matcher` | text | [See our documentation](https://dt-url.net/bp234rv) | Required |