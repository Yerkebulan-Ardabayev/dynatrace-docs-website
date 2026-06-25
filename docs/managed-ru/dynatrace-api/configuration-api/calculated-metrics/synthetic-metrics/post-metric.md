---
title: Synthetic metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/post-metric
scraped: 2026-05-12T11:19:24.203234
---

# Synthetic metrics API - POST a metric

# Synthetic metrics API - POST a metric

* Reference
* Published Apr 16, 2020

Создаёт новую вычисляемую синтетическую метрику.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CalculatedSyntheticMetric](#openapi-definition-CalculatedSyntheticMetric) | JSON-тело запроса. Содержит определение новой вычисляемой синтетической метрики. | body | Optional |

### Объекты тела запроса

#### Объект `CalculatedSyntheticMetric`

Определение вычисляемой синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | [SyntheticMetricDimension[]](#openapi-definition-SyntheticMetricDimension) | Список измерений метрики. | Optional |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). | Required |
| filter | [SyntheticMetricFilter](#openapi-definition-SyntheticMetricFilter) | Фильтр вычисляемой синтетической метрики. | Optional |
| metric | string | Тип синтетической метрики. Возможные значения: * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `FailedRequestsResources` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `HttpErrors` * `JavaScriptErrors` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongTasks` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `ResourceCount` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `TotalDuration` * `TransferSize` * `UserActionDuration` * `VisuallyComplete` | Required |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:synthetic`. | Required |
| monitorIdentifier | string | ID сущности Dynatrace synthetic monitor, которому принадлежит метрика. | Required |
| name | string | Имя метрики, отображаемое в UI. | Required |

#### Объект `SyntheticMetricDimension`

Измерение вычисляемой синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `Event` * `Location` * `ResourceOrigin` | Required |
| topX | integer | Количество верхних значений для расчёта. | Optional |

#### Объект `SyntheticMetricFilter`

Фильтр вычисляемой синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionType | string | В расчёт метрики включаются только пользовательские действия указанного типа. Возможные значения: * `Custom` * `Load` * `Xhr` | Optional |
| errorCode | integer | В расчёт метрики включаются только выполнения, завершившиеся с указанным кодом ошибки. | Optional |
| event | string | В расчёт метрики включается только указанное событие browser clickpath.  Укажите здесь ID сущности Dynatrace события. Список clickpath-событий монитора можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API | Optional |
| hasError | boolean | Статус выполнения мониторов, включаемых в расчёт метрики:  * `true`: включаются только неудавшиеся выполнения. * `false`: включаются все выполнения. | Optional |
| location | string | В расчёт метрики включаются только выполнения из указанной локации.  Укажите здесь ID сущности Dynatrace локации. Список локаций, из которых работает монитор, можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"dimensions": [



{



"dimension": "Location"



}



],



"enabled": true,



"filter": {



"event": "SYNTHETIC_TEST_STEP-1234",



"hasError": true



},



"metric": "UserActionDuration",



"metricKey": "calc:synthetic.browser.mymetric",



"monitorIdentifier": "SYNTHETIC_TEST-1234",



"name": "MyMetric"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Вычисляемая синтетическая метрика создана. Тело ответа содержит её ключ и имя. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная вычисляемая синтетическая метрика валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")