---
title: Settings API - User action custom metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-user-action-custom-metrics
scraped: 2026-05-12T11:45:51.581289
---

# Settings API - User action custom metrics schema table

# Settings API - User action custom metrics schema table

* Published Dec 05, 2023

### Пользовательские метрики на основе user-действий (`builtin:user-action-custom-metrics)`

С помощью пользовательских метрик user-действий (см. [documentation](https://dt-url.net/3i03u3s)) можно извлекать business-level KPI-метрики из данных user-действий. Метрики затем можно сохранять как timeseries и потреблять (без интерполяции) в пользовательских графиках, механизмах оповещений или Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).

Для изучения собранных метрик перейдите в Data explorer (`<your-dynatrace-url>//ui/data-explorer`).

Чтобы создать пользовательское событие на основе пользовательской метрики, перейдите в Custom events for alerting (`<your-dynatrace-url>//#settings/anomalydetection/metricevents`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:user-action-custom-metrics` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.usql-custom-metrics` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:user-action-custom-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:user-action-custom-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:user-action-custom-metrics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить пользовательскую метрику `enabled` | boolean | - | Required |
| Ключ метрики `metricKey` | text | - | Required |
| Тип извлекаемого значения `value` | [MetricValue](#MetricValue) | Задаёт тип значения, извлекаемого из user-действия. При использовании **user action counter** подсчитывается число user-действий (аналогично count(\*) в USQL). При использовании **user action field value** извлекается значение поля user-действия. | Required |
| Добавить dimension `dimensions` | list | Задаёт поля, используемые как dimensions. Dimension, это набор справочной информации о точке данных метрики, представляющий интерес для бизнеса. Dimensions, это параметры вроде "application", "type", "apdexCategory". Например, использование "type" в качестве dimension позволяет разбивать данные графика по типу user-действия. | Required |
| Добавить фильтр `filters` | [Filter](#Filter)[] | Задаёт фильтры для user-действия. Фильтры применяются в момент извлечения данных, и для извлечения пользовательских метрик используются только сессии, удовлетворяющие критериям фильтрации. Эти фильтры нельзя изменить в metric data explorer. Например, "type equals Xhr" даст данные только от xhr-действий, исключая user-действия других типов. | Required |

##### Объект `MetricValue`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `type` | enum | Возможные значения: * `COUNTER` * `FIELD` | Required |
| Имя поля `fieldName` | text | - | Required |

##### Объект `Filter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя поля `fieldName` | text | - | Required |
| Оператор `operator` | enum | Возможные значения: * `EQUALS` * `NOT_EQUAL` * `IS_NULL` * `IS_NOT_NULL` * `LIKE` * `NOT_LIKE` * `LESS_THAN` * `LESS_THAN_OR_EQUAL_TO` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL_TO` * `IN` * `STARTS_WITH` | Required |
| Значение `value` | text | - | Required |
| Значения `valueIn` | list | - | Required |