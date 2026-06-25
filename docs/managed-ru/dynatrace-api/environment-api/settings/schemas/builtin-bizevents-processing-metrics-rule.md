---
title: Settings API - Business event metric extraction schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-bizevents-processing-metrics-rule
scraped: 2026-05-12T11:39:21.108545
---

# Settings API - Business event metric extraction schema table

# Settings API - Business event metric extraction schema table

* Published Dec 05, 2023

### Извлечение метрик из Business event (`builtin:bizevents-processing-metrics.rule)`

С помощью [business event metrics](https://dt-url.net/m3034if) можно использовать запросы для создания пользовательских оповещений, представляющих конкретные вхождения business event или значения атрибутов.

Примечание:

* Вновь заданные метрики Business event могут применяться только к данным Business Event, поступившим после создания метрики.
* Метрики Business Event расходуют DDU.

Подробности о ценообразовании см. в [DDUs for custom metrics](https://dt-url.net/vg43xi8).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:bizevents-processing-metrics.rule` | * `group:business-analytics` * `group:business-analytics.ingest-pipeline` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:bizevents-processing-metrics.rule` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Ключ `key` | text | - | Required |
| Сопоставитель (DQL) `matcher` | text | [See our documentation](https://dt-url.net/bp234rv) | Required |
| Способ измерения `measure` | enum | Возможные значения: * `OCCURRENCE` * `ATTRIBUTE` | Required |
| Атрибут `measureAttribute` | text | - | Required |
| `dimensions` | set | - | Required |