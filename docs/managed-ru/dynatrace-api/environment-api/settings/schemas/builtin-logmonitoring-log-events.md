---
title: Settings API - Log events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events
scraped: 2026-05-12T11:49:23.296096
---

# Settings API - Log events schema table

# Settings API - Log events schema table

* Published Dec 05, 2023

### События лога (`builtin:logmonitoring.log-events)`

Настройте паттерны логов, запускающие события для оповещений и анализа DavisÂ®. Учтите: обнаружение событий лога влечёт [billing costs](https://dt-url.net/hk03ulj).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-events` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-events` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-events` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-events` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Сводка `summary` | text | Текстовая сводка записи log event | Required |
| Сопоставитель `query` | text | - | Required |
| Шаблон события `eventTemplate` | [EventTemplate](#EventTemplate) | - | Required |

##### Объект `EventTemplate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Заголовок `title` | text | Заголовок события, которое надо запустить. Введите '{' для подсказок по placeholder. | Required |
| Описание `description` | text | Описание события, которое надо запустить. Введите '{' для подсказок по placeholder. | Required |
| Тип события `eventType` | enum | Тип события, которое надо запустить. Возможные значения: * `INFO` * `ERROR` * `AVAILABILITY` * `SLOWDOWN` * `RESOURCE` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `MARKED_FOR_TERMINATION` * `WARNING` | Required |
| Разрешить merge `davisMerge` | boolean | DavisÂ® AI попытается слить это событие в существующие проблемы, иначе всегда будет создаваться новая проблема. | Required |
| Свойства `metadata` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value-свойств, прикрепляемых к запущенному событию. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок по ключам. | Required |
| Значение `metadataValue` | text | Введите '{' для подсказок по placeholder. | Required |