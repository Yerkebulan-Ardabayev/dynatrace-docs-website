---
title: Synthetic metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/post-metric
---

# Synthetic metrics API - POST a metric

# Synthetic metrics API - POST a metric

* Справка
* Опубликовано 16 апр. 2020 г.

Создаёт новую расчётную синтетическую метрику.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CalculatedSyntheticMetric](#openapi-definition-CalculatedSyntheticMetric) | Тело JSON запроса. Содержит определение новой расчётной синтетической метрики. | body | Опционально |

### Объекты тела запроса

#### Объект `CalculatedSyntheticMetric`

Определение расчётной синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | [SyntheticMetricDimension](#openapi-definition-SyntheticMetricDimension)[] | Список измерений метрики. | Опционально |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). | Обязательный |
| filter | [SyntheticMetricFilter](#openapi-definition-SyntheticMetricFilter) | Фильтр расчётной синтетической метрики. | Опционально |
| metric | string | Тип синтетической метрики. Элемент может принимать следующие значения * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `FailedRequestsResources` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `HttpErrors` * `JavaScriptErrors` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongTasks` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `ResourceCount` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `TotalDuration` * `TransferSize` * `UserActionDuration` * `VisuallyComplete` | Обязательный |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:synthetic`. | Обязательный |
| monitorIdentifier | string | ID Dynatrace сущности синтетического монитора, к которому относится метрика. | Обязательный |
| name | string | Название метрики, отображаемое в UI. | Обязательный |

#### Объект `SyntheticMetricDimension`

Измерение расчётной синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimension | string | Измерение метрики. Элемент может принимать следующие значения * `Event` * `Location` * `ResourceOrigin` | Обязательный |
| topX | integer | Количество топовых значений для расчёта. | Опционально |

#### Объект `SyntheticMetricFilter`

Фильтр расчётной синтетической метрики.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionType | string | В расчёт метрики включаются только пользовательские действия указанного типа. Элемент может принимать следующие значения * `Custom` * `Load` * `Xhr` | Опционально |
| errorCode | integer | В расчёт метрики включаются только выполнения, завершившиеся с указанным кодом ошибки. | Опционально |
| event | string | В расчёт метрики включается только указанное событие браузерного clickpath.  Здесь нужно указать ID Dynatrace сущности события. Список событий clickpath монитора можно получить запросом [GET a synthetic monitor﻿](https://dt-url.net/4oe3kka?dt=m) из Environment API | Опционально |
| hasError | boolean | Статус выполнения мониторов, включаемых в расчёт метрики:  * `true`: включаются только неудачные выполнения. * `false`: включаются все выполнения. | Опционально |
| location | string | В расчёт метрики включаются только выполнения из указанной локации.  Здесь нужно указать ID Dynatrace сущности локации. Список локаций, из которых запускается монитор, можно получить запросом [GET a synthetic monitor﻿](https://dt-url.net/4oe3kka?dt=m) из Environment API. | Опционально |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Расчётная синтетическая метрика создана. Ответ содержит её ключ и название. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление Dynatrace сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание Dynatrace сущности. |
| id | string | ID Dynatrace сущности. |
| name | string | Название Dynatrace сущности. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой в реальном запросе. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная расчётная синтетическая метрика корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела JSON ответа

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

## Похожие темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор с одним URL, браузерный clickpath или HTTP-монитор.")