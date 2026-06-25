---
title: Mobile app metrics API - POST a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/post-metric
scraped: 2026-05-12T11:17:33.916529
---

# Mobile app metrics API - POST a metric

# Mobile app metrics API - POST a metric

* Reference
* Published Apr 16, 2020

Создаёт новую вычисляемую метрику мобильного приложения.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [CalculatedMobileMetric](#openapi-definition-CalculatedMobileMetric) | JSON-тело запроса. Содержит определение новой вычисляемой метрики для мобильного или пользовательского приложения. | body | Optional |

### Объекты тела запроса

#### Объект `CalculatedMobileMetric`

Определение вычисляемой метрики для мобильного или пользовательского приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace приложения, которому принадлежит метрика. | Required |
| dimensions | [CalculatedMobileMetricDimension[]](#openapi-definition-CalculatedMobileMetricDimension) | Список измерений метрики. | Optional |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). | Required |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:apps`. | Required |
| metricType | string | Тип метрики. Возможные значения: * `REPORTED_ERROR_COUNT` * `USER_ACTION_DURATION` * `WEB_REQUEST_COUNT` * `WEB_REQUEST_ERROR_COUNT` | Required |
| name | string | Имя метрики, отображаемое в UI. | Required |
| userActionFilter | [CalculatedMobileMetricUserActionFilter](#openapi-definition-CalculatedMobileMetricUserActionFilter) | Фильтр пользовательских действий вычисляемой метрики для мобильного или пользовательского приложения. | Optional |

#### Объект `CalculatedMobileMetricDimension`

Измерение вычисляемой метрики мобильного приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `APP_VERSION` * `DEVICE` * `ERROR_CONTEXT` * `GEOLOCATION` * `MANUFACTURER` * `OS` | Required |
| topX | integer | Количество верхних значений для расчёта. | Required |

#### Объект `CalculatedMobileMetricUserActionFilter`

Фильтр пользовательских действий вычисляемой метрики для мобильного или пользовательского приложения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| actionDurationFromMilliseconds | integer | В расчёт метрики включаются только действия с длительностью больше или равной этому значению (в миллисекундах). | Optional |
| actionDurationToMilliseconds | integer | В расчёт метрики включаются только действия с длительностью меньше или равной этому значению (в миллисекундах). | Optional |
| apdex | string | В расчёт метрики включаются только действия с указанной оценкой Apdex. Возможные значения: * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` | Optional |
| appVersion | string | В расчёт метрики включаются только действия из этой версии приложения.  Применяется оператор EQUALS. | Optional |
| carrier | string | В расчёт метрики включаются только действия от оператора связи этого типа. | Optional |
| city | string | В расчёт метрики включаются только действия пользователей из этого города.  Укажите здесь ID геолокации. | Optional |
| connectionType | string | В расчёт метрики включаются только действия из этого типа соединения. Возможные значения: * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` | Optional |
| continent | string | В расчёт метрики включаются только действия пользователей с этого континента.  Укажите здесь ID геолокации. | Optional |
| country | string | В расчёт метрики включаются только действия пользователей из этой страны.  Укажите здесь ID геолокации. | Optional |
| device | string | В расчёт метрики включаются только действия из этой версии приложения.  Применяется оператор EQUALS. | Optional |
| hasHttpError | boolean | Статус HTTP-ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с HTTP-ошибками. * `false`: включаются все действия. | Optional |
| hasReportedError | boolean | Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с зарегистрированными ошибками. * `false`: включаются все действия. | Optional |
| isp | string | В расчёт метрики включаются только действия от этого интернет-провайдера.  Применяется оператор EQUALS. | Optional |
| manufacturer | string | В расчёт метрики включаются только действия с устройств этого производителя.  Применяется оператор EQUALS. | Optional |
| networkTechnology | string | Фильтр по сетевой технологии | Optional |
| orientation | string | В расчёт метрики включаются только действия с устройств с этой ориентацией экрана. Возможные значения: * `LANDSCAPE` * `PORTRAIT` * `UNKNOWN` | Optional |
| osFamily | string | В расчёт метрики включаются только действия из этого семейства ОС.  Укажите здесь ID ОС. | Optional |
| osVersion | string | В расчёт метрики включаются только действия из этой версии ОС.  Укажите здесь ID ОС. | Optional |
| region | string | В расчёт метрики включаются только действия пользователей из этого региона.  Укажите здесь ID геолокации. | Optional |
| resolution | string | В расчёт метрики включаются только действия с устройств с этим разрешением экрана. Возможные значения: * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` | Optional |
| userActionName | string | В расчёт метрики включаются только действия с этим именем.  Применяется оператор EQUALS. | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"applicationIdentifier": "MOBILE_APPLICATION-1234",



"dimensions": [



{



"dimension": "GEOLOCATION",



"topX": 20



}



],



"enabled": true,



"metricKey": "calc:apps.mobile.mymetric",



"metricType": "USER_ACTION_DURATION",



"name": "MyMetric",



"userActionFilter": {



"country": "GEOLOCATION-1234",



"hasHttpError": true,



"osVersion": "OS-1234"



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Вычисляемая метрика мобильного приложения создана. Тело ответа содержит её ключ и имя. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/validator` |

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

* [Создание вычисленных метрик для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших мобильных приложений.")
* [Создание вычисляемых метрик для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших пользовательских приложений.")