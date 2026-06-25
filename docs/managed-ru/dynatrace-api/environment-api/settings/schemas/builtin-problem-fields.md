---
title: Settings API - Problem fields schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-problem-fields
scraped: 2026-05-12T11:41:02.842604
---

# Settings API - Problem fields schema table

# Settings API - Problem fields schema table

* Published Mar 17, 2025

### Поля проблемы (`builtin:problem.fields)`

Поля проблемы позволяют задавать правила извлечения определённых полей из событий в проблемы. События хранятся в dt.davis.events, проблемы хранятся в dt.davis.problems. Каждая настройка представляет собой уникальное правило, указывающее, какие поля события должны быть извлечены в проблему, чтобы критически важная информация переносилась и оставалась легкодоступной.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:problem.fields` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.fields` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:problem.fields` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:problem.fields` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если true, поле извлекается из событий в проблемы. | Required |
| Поле события `eventField` | text | Поле события, которое будет извлечено. | Required |
| Поле проблемы `problemField` | text | Поле, под которым извлечённые данные события будут сохранены в проблеме. | Required |