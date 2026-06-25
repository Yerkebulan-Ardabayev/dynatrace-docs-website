---
title: Service-level objectives API - PUT SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/put-slo
scraped: 2026-05-12T11:57:41.455349
---

# Service-level objectives API - PUT SLO

# Service-level objectives API - PUT SLO

* Справочник
* Опубликовано 7 сентября 2022 г.

Обновляет параметры цели уровня обслуживания (SLO).

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `slo.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого SLO. | path | Обязательный |
| body | [SloConfigItemDtoImpl](#openapi-definition-SloConfigItemDtoImpl) | JSON-тело запроса. Содержит обновлённые параметры SLO. | body | Обязательный |

### Объекты тела запроса

#### Объект `SloConfigItemDtoImpl`

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| description | string | Описание SLO. | Необязательный |
| enabled | boolean | SLO включён (`true`) или отключён (`false`).  Если не определено, SLO по умолчанию отключён. | Необязательный |
| errorBudgetBurnRate | [SloBurnRateConfig](#openapi-definition-SloBurnRateConfig) | Конфигурация скорости расходования бюджета ошибок цели уровня обслуживания (SLO). | Необязательный |
| evaluationType | string | Тип оценки SLO. Поле может принимать значения: * `AGGREGATE` | Обязательный |
| filter | string | Фильтр сущностей для оценки SLO. Общая длина строки entitySelector в SLO ограничена 1 000 символами. Используйте [синтаксис entity selector](https://dt-url.net/entityselector). | Необязательный |
| ~~metricDenominator~~ | string | УСТАРЕЛО  Метрика общего количества (знаменатель в расчёте отношения).  Обязательно, когда **useRateMetric** имеет значение `false`. | Необязательный |
| metricExpression | string | Процентное метрическое выражение для вычисления SLO. | Необязательный |
| metricName | string | Имя, используемое для создания ключей func-метрик SLO. После создания имя метрики изменить нельзя. | Необязательный |
| ~~metricNumerator~~ | string | УСТАРЕЛО  Метрика количества успехов (числитель в расчёте отношения).  Обязательно, когда **useRateMetric** имеет значение `false`. | Необязательный |
| ~~metricRate~~ | string | УСТАРЕЛО  Процентная метрика для вычисления SLO.  Обязательно, когда **useRateMetric** имеет значение `true`. | Необязательный |
| name | string | Имя SLO. | Обязательный |
| target | number | Целевое значение SLO. | Обязательный |
| timeframe | string | Временной диапазон для оценки SLO. Используйте синтаксис глобального селектора временного диапазона. | Обязательный |
| ~~useRateMetric~~ | boolean | УСТАРЕЛО  Тип метрики для вычисления SLO:  * `true`: существующая процентная метрика. * `false`: отношение двух метрик.  Список доступных метрик смотрите на [странице встроенных метрик](https://dt-url.net/be03kow) или попробуйте вызов API [GET metrics](https://dt-url.net/8e43kxf). | Необязательный |
| warning | number | Предупредительное значение SLO.  В состоянии предупреждения SLO ещё выполняется, но близко к нарушению. | Обязательный |

#### Объект `SloBurnRateConfig`

Конфигурация скорости расходования бюджета ошибок цели уровня обслуживания (SLO).

| Поле | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| burnRateVisualizationEnabled | boolean | Вычисление скорости расходования бюджета ошибок включено (`true`) или отключено (`false`).  В случае `false` вычисленные значения здесь отсутствуют.  Если не определено, вычисление скорости расходования бюджета ошибок по умолчанию отключено. | Необязательный |
| fastBurnThreshold | number | Порог между медленной и быстрой скоростью расходования. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Для реального запроса её нужно адаптировать.

```
{



"description": "Rate of successful payments per week",



"enabled": true,



"errorBudgetBurnRate": {



"burnRateVisualizationEnabled": true,



"fastBurnThreshold": 1.5



},



"evaluationType": "AGGREGATE",



"filter": "type(\"SERVICE\")",



"metricDenominator": "builtin:service.requestCount.server",



"metricExpression": "(100)*(builtin:service.errors.server.successCount:splitBy())/(builtin:service.requestCount.server:splitBy())",



"metricName": "payment_service_availability",



"metricNumerator": "builtin:service.errors.server.successCount",



"metricRate": "builtin:service.successes.server.rate",



"name": "Payment service availability",



"target": 95,



"timeframe": "-1d",



"useRateMetric": true,



"warning": 97.5



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Некорректный ввод. |
| **404** | - | Неудача. Запрошенный ресурс не существует. |
| **500** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Внутренняя ошибка сервера. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Мониторинг и алертинг по service-level objectives в Dynatrace через Service-Level Objectives Classic.")