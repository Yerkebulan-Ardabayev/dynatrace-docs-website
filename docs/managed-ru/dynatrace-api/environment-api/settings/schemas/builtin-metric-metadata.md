---
title: Settings API - Metric metadata schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-metric-metadata
scraped: 2026-05-12T11:49:06.700625
---

# Settings API - Metric metadata schema table

# Settings API - Metric metadata schema table

* Published Dec 05, 2023

### Метаданные метрики (`builtin:metric.metadata)`

[Custom metrics metadata](https://dt-url.net/k603stq "Custom metrics metadata") позволяет указать дополнительные сведения о метрике.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:metric.metadata` | * `group:metrics` | `metric` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.metadata` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:metric.metadata` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.metadata` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Отображаемое имя `displayName` | text | - | Optional |
| Описание `description` | text | - | Optional |
| Единица `unit` | text | - | Required |
| Формат отображения единицы `unitDisplayFormat` | enum | Сырое значение хранится в битах или байтах. Пользовательский интерфейс может отображать его в этих системах счисления:  Binary: 1 MiB = 1024 KiB = 1 048 576 байт  Decimal: 1 MB = 1000 kB = 1 000 000 байт  Если не задано, используется decimal-система. Возможные значения: * `binary` * `decimal` | Optional |
| Свойства метрики `metricProperties` | [MetricProperties](#MetricProperties) | - | Optional |
| Dimensions метрики `dimensions` | [Dimension](#Dimension)[] | Задайте метаданные для каждого dimension метрики. | Required |
| Теги `tags` | list | - | Required |
| Тип сущности-источника `sourceEntityType` | text | Указывает, какой entity dimension использовать как primary dimension. Свойство можно настроить только для метрик, принятых через Metrics API. | Optional |

##### Объект `MetricProperties`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Минимальное значение `minValue` | float | Минимально допустимое значение метрики. | Optional |
| Максимальное значение `maxValue` | float | Максимально допустимое значение метрики. | Optional |
| Релевантна для root cause `rootCauseRelevant` | boolean | Связана ли метрика (true или false) с root cause проблемы.  Метрика, релевантная для root cause, является сильным индикатором сбойного компонента. | Optional |
| Релевантна для impact `impactRelevant` | boolean | Релевантна ли метрика (true или false) для impact проблемы.  Метрика, релевантная для impact, сильно зависит от других метрик и изменяется из-за изменения нижележащей root-cause-метрики. | Optional |
| Тип значения `valueType` | enum | Тип значения метрики. Доступные варианты:  score: метрика, у которой высокие значения означают хорошую ситуацию, а низкие, проблему. Пример: success rate.  error: метрика, у которой высокие значения означают проблему, а низкие, хорошую ситуацию. Пример: счётчик ошибок. Возможные значения: * `error` * `score` * `unknown` | Required |
| Задержка `latency` | integer | Задержка метрики в минутах.  Задержка, это ожидаемая задержка передачи (например, из-за ограничений cloud-провайдеров или других сторонних источников данных) между наблюдением точки данных метрики и её доступностью в Dynatrace.  Допустимый диапазон значений, от 1 до 60 минут. | Optional |

##### Объект `Dimension`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ dimension `key` | text | - | Required |
| Отображаемое имя `displayName` | text | - | Optional |