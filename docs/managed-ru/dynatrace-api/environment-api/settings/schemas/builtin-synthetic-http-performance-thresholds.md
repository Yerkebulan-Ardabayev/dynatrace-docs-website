---
title: Settings API - Performance thresholds schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-performance-thresholds
scraped: 2026-05-12T11:48:36.033185
---

# Settings API - Performance thresholds schema table

# Settings API - Performance thresholds schema table

* Опубликовано 05 декабря 2023 г.

### Пороги производительности (`builtin:synthetic.http.performance-thresholds)`

Dynatrace создаёт новую problem, если этот synthetic-монитор превышает любой из перечисленных ниже порогов производительности в 3 из 5 последних выполнений в данной локации, при условии что для synthetic-монитора нет открытого maintenance window. В одну problem могут быть включены несколько локаций с тремя такими нарушениями. Problem закрывается, если ни один из порогов производительности не нарушен в 5 последних выполнениях в каждой ранее затронутой локации.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.performance-thresholds` | - | `HTTP_CHECK` - HTTP monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.performance-thresholds` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Создавать problem и отправлять оповещение при нарушении порогов производительности `enabled` | boolean | - | Required |
| Пороги производительности `thresholds` | Set<[ThresholdEntry](#ThresholdEntry)> | - | Required |

##### Объект `ThresholdEntry`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Запрос `event` | text | - | Required |
| Порог (в секундах) `threshold` | float | - | Required |