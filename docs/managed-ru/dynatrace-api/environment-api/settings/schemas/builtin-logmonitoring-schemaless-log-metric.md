---
title: Settings API - Log metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric
scraped: 2026-05-12T11:39:51.853229
---

# Settings API - Log metrics schema table

# Settings API - Log metrics schema table

* Опубликовано 05 декабря 2023 г.

### Log-метрики (`builtin:logmonitoring.schemaless-log-metric)`

С log-метриками можно по запросам строить метрики из данных логов для дашбордов, аналитики и custom-алертинга. Log-метрики расходуют [DavisÂ® data units](https://dt-url.net/vg43xi8).

Учтите, что только что определённые log-метрики применяются только к данным логов, поступившим после создания метрики.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.schemaless-log-metric` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.schemaless-log-metric` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Ключ метрики `key` | text | - | Required |
| Matcher `query` | text | - | Required |
| Тип измерения метрики `measure` | enum | Возможные значения: * `OCCURRENCE` * `ATTRIBUTE` | Required |
| Атрибут `measureAttribute` | text | - | Required |
| Dimensions `dimensions` | set | Чтобы включить splitting метрики, добавьте нужные dimensions.  Имя dimension можно выбрать из списка или задать произвольное значение. Для извлечения полей из логов используйте log processing (`<your-dynatrace-url>/builtin:logmonitoring.log-dpp-rules`). | Required |