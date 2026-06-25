---
title: Web application metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/post-metric
scraped: 2026-05-12T11:17:56.258346
---

# Web application metrics API - POST a metric

# Web application metrics API - POST a metric

* Reference
* Published Feb 28, 2020

Создаёт новую вычисляемую метрику веб-приложения.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [WebApplicationMetric](#openapi-definition-WebApplicationMetric) | JSON-тело запроса. Содержит дескриптор новой вычисляемой метрики веб-приложения. | body | Required |

### Объекты тела запроса

#### Объект `WebApplicationMetric`

Дескриптор вычисляемой метрики веб-приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace приложения, которому принадлежит метрика. | Required |
| dimensions | [WebApplicationDimensionDefinition[]](#openapi-definition-WebApplicationDimensionDefinition) | Список измерений метрики. | Optional |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). | Required |
| metricDefinition | [WebApplicationMetricDefinition](#openapi-definition-WebApplicationMetricDefinition) | Определение метрики веб-приложения. | Required |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:apps`. | Required |
| name | string | Отображаемое имя метрики. | Required |
| userActionFilter | [UserActionFilter](#openapi-definition-UserActionFilter) | Фильтр пользовательских действий вычисляемой метрики веб-приложения.  Для расчёта метрики используются только пользовательские действия, соответствующие заданным критериям.  Пользовательское действие должно соответствовать **всем** критериям. | Optional |

#### Объект `WebApplicationDimensionDefinition`

Измерение вычисляемых метрик веб-приложений.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `ApdexType` * `Browser` * `ErrorContext` * `ErrorOrigin` * `ErrorType` * `GeoLocation` * `StringProperty` * `UserActionType` | Required |
| propertyKey | string | Ключ свойства пользовательского действия.  Применимо только для измерения `StringProperty`. | Optional |
| topX | integer | Количество верхних значений для расчёта. | Required |

#### Объект `WebApplicationMetricDefinition`

Определение метрики веб-приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| metric | string | Тип метрики веб-приложения. Возможные значения: * `Apdex` * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `DoubleProperty` * `ErrorCount` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongProperty` * `LongTasksTime` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `UserActionDuration` * `VisuallyComplete` | Required |
| propertyKey | string | Ключ свойства пользовательского действия.  Применимо только для метрик `DoubleProperty` и `LongProperty`. | Optional |

#### Объект `UserActionFilter`

Фильтр пользовательских действий вычисляемой метрики веб-приложения.

Для расчёта метрики используются только пользовательские действия, соответствующие заданным критериям.

Пользовательское действие должно соответствовать **всем** критериям.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionDurationFromMilliseconds | integer | В расчёт метрики включаются только действия с длительностью больше или равной этому значению (в миллисекундах). | Optional |
| actionDurationToMilliseconds | integer | В расчёт метрики включаются только действия с длительностью меньше или равной этому значению (в миллисекундах). | Optional |
| apdex | string | В расчёт метрики включаются только действия с указанной оценкой Apdex. Возможные значения: * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` | Optional |
| browserFamily | string | В расчёт метрики включаются только пользовательские действия из указанного семейства браузеров.  Применяется оператор EQUALS. | Optional |
| browserType | string | В расчёт метрики включаются только пользовательские действия из указанного типа браузера.  Применяется оператор EQUALS. | Optional |
| browserVersion | string | В расчёт метрики включаются только пользовательские действия из указанной версии браузера.  Применяется оператор EQUALS. | Optional |
| city | string | В расчёт метрики включаются только действия пользователей из этого города.  Укажите здесь ID геолокации. | Optional |
| continent | string | В расчёт метрики включаются только действия пользователей с этого континента.  Укажите здесь ID геолокации. | Optional |
| country | string | В расчёт метрики включаются только действия пользователей из этой страны.  Укажите здесь ID геолокации. | Optional |
| customAction | boolean | Статус кастомных действий в расчёте метрики:  * `true`: включаются кастомные действия. * `false`: включаются все действия. | Optional |
| customErrorName | string | Имя кастомной ошибки действий, включаемых в расчёт метрики. | Optional |
| customErrorType | string | Тип кастомной ошибки действий, включаемых в расчёт метрики. | Optional |
| domain | string | В расчёт метрики включаются только пользовательские действия из указанного домена.  Применяется оператор EQUALS. | Optional |
| hasAnyError | boolean | Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с любыми ошибками. * `false`: включаются все действия. | Optional |
| hasCustomErrors | boolean | Статус кастомных ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с кастомными ошибками. * `false`: включаются все действия. | Optional |
| hasHttpErrors | boolean | Статус ошибок запросов действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками запросов (HTTP-ошибки, неудавшиеся изображения, нарушения правил CSP). * `false`: включаются все действия. | Optional |
| hasJavascriptErrors | boolean | Статус ошибок JavaScript действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками JavaScript. * `false`: включаются все действия. | Optional |
| httpErrorCode | integer | Код статуса HTTP-ошибки действий, включаемых в расчёт метрики. | Optional |
| httpErrorCodeTo | integer | Можно использовать вместе с `httpErrorCode` для задания диапазона кодов ошибок, которые будут включены в расчёт метрики. | Optional |
| httpPath | string | Путь запроса, определённый как источник HTTP-ошибки действий, включаемых в расчёт метрики. | Optional |
| ip | string | В расчёт метрики включаются только действия с этого IP-адреса.  Применяется оператор EQUALS. | Optional |
| ipV6Traffic | boolean | Статус IPv6 действий, включаемых в расчёт метрики:  * `true`: включаются только действия по IPv6. * `false`: включаются все действия. | Optional |
| loadAction | boolean | Статус load-действий в расчёте метрики:  * `true`: включаются load-действия. * `false`: включаются все действия. | Optional |
| osFamily | string | В расчёт метрики включаются только действия из этого семейства ОС.  Укажите здесь ID ОС. | Optional |
| osVersion | string | В расчёт метрики включаются только действия из этой версии ОС.  Укажите здесь ID ОС. | Optional |
| realUser | boolean | Статус действий от реальных пользователей в расчёте метрики:  * `true`: включаются только действия реальных пользователей. * `false`: включаются все действия. | Optional |
| region | string | В расчёт метрики включаются только действия пользователей из этого региона.  Укажите здесь ID геолокации. | Optional |
| robot | boolean | Статус действий от роботов в расчёте метрики:  * `true`: включаются только действия роботов. * `false`: включаются все действия. | Optional |
| synthetic | boolean | Статус действий от synthetic monitors в расчёте метрики:  * `true`: включаются только действия от synthetic monitors. * `false`: включаются все действия. | Optional |
| targetViewGroup | string | В расчёт метрики включаются только действия на указанной группе представлений. | Optional |
| targetViewGroupNameMatchType | string | Указывает тип совпадения для фильтра группы представлений, например с помощью `Contains` или `Equals`. По умолчанию `Equals`. Возможные значения: * `Contains` * `Equals` | Optional |
| targetViewName | string | В расчёт метрики включаются только действия на указанном представлении. | Optional |
| targetViewNameMatchType | string | Указывает тип совпадения для фильтра имени представления, например с помощью `Contains` или `Equals`. По умолчанию `Equals`. Возможные значения: * `Contains` * `Equals` | Optional |
| userActionName | string | В расчёт метрики включаются только действия с этим именем.  Применяется оператор EQUALS. | Optional |
| userActionProperties | [UserActionPropertyFilter[]](#openapi-definition-UserActionPropertyFilter) | В расчёт метрики включаются только действия с указанными свойствами. | Optional |
| xhrAction | boolean | Статус XHR-действий в расчёте метрики:  * `true`: включаются XHR-действия. * `false`: включаются все действия. | Optional |
| xhrRouteChangeAction | boolean | Статус действий смены маршрута в расчёте метрики:  * `true`: включаются действия смены маршрута. * `false`: включаются все действия. | Optional |

#### Объект `UserActionPropertyFilter`

Фильтр свойств пользовательского действия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| from | number | В расчёт метрики включаются только действия со значением больше или равным этому.  Применимо только к числовым значениям. | Optional |
| key | string | Ключ проверяемого свойства действия. | Optional |
| matchType | string | Указывает тип совпадения для строкового фильтра, например с помощью `Contains` или `Equals`.  Применимо только к строковым значениям. Возможные значения: * `Contains` * `Equals` | Optional |
| to | number | В расчёт метрики включаются только действия со значением меньше или равным этому.  Применимо только к числовым значениям. | Optional |
| value | string | В расчёт метрики включаются только действия, у которых это значение в указанном свойстве.  Применимо только к строковым значениям. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"applicationIdentifier": "APPLICATION-1234",



"dimensions": [



{



"dimension": "GeoLocation",



"topX": 20



}



],



"enabled": true,



"metricDefinition": {



"metric": "UserActionDuration"



},



"metricKey": "calc:apps.web.mymetric",



"name": "MyMetric",



"userActionFilter": {



"browserType": "BROWSER-1234",



"country": "GEOLOCATION-1234",



"loadAction": true



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Метрика создана. Тело ответа содержит её ключ и имя. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная метрика валидна. Ответ без тела. |
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

* [Создание вычисляемых метрик для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших веб-приложений.")