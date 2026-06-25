---
title: Mobile app metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-metric
scraped: 2026-05-12T11:17:28.090113
---

# Mobile app metrics API - GET a metric

# Mobile app metrics API - GET a metric

* Reference
* Published Apr 16, 2020

Возвращает дескриптор указанной вычисляемой метрики мобильного приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile/{metricKey}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ требуемой метрики. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CalculatedMobileMetric](#openapi-definition-CalculatedMobileMetric) | Успех |

### Объекты тела ответа

#### Объект `CalculatedMobileMetric`

Определение вычисляемой метрики для мобильного или пользовательского приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace приложения, которому принадлежит метрика. |
| dimensions | [CalculatedMobileMetricDimension[]](#openapi-definition-CalculatedMobileMetricDimension) | Список измерений метрики. |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:apps`. |
| metricType | string | Тип метрики. Возможные значения: * `REPORTED_ERROR_COUNT` * `USER_ACTION_DURATION` * `WEB_REQUEST_COUNT` * `WEB_REQUEST_ERROR_COUNT` |
| name | string | Имя метрики, отображаемое в UI. |
| userActionFilter | [CalculatedMobileMetricUserActionFilter](#openapi-definition-CalculatedMobileMetricUserActionFilter) | Фильтр пользовательских действий вычисляемой метрики для мобильного или пользовательского приложения. |

#### Объект `CalculatedMobileMetricDimension`

Измерение вычисляемой метрики мобильного приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `APP_VERSION` * `DEVICE` * `ERROR_CONTEXT` * `GEOLOCATION` * `MANUFACTURER` * `OS` |
| topX | integer | Количество верхних значений для расчёта. |

#### Объект `CalculatedMobileMetricUserActionFilter`

Фильтр пользовательских действий вычисляемой метрики для мобильного или пользовательского приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actionDurationFromMilliseconds | integer | В расчёт метрики включаются только действия с длительностью больше или равной этому значению (в миллисекундах). |
| actionDurationToMilliseconds | integer | В расчёт метрики включаются только действия с длительностью меньше или равной этому значению (в миллисекундах). |
| apdex | string | В расчёт метрики включаются только действия с указанной оценкой Apdex. Возможные значения: * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` |
| appVersion | string | В расчёт метрики включаются только действия из этой версии приложения.  Применяется оператор EQUALS. |
| carrier | string | В расчёт метрики включаются только действия от оператора связи этого типа. |
| city | string | В расчёт метрики включаются только действия пользователей из этого города.  Укажите здесь ID геолокации. |
| connectionType | string | В расчёт метрики включаются только действия из этого типа соединения. Возможные значения: * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |
| continent | string | В расчёт метрики включаются только действия пользователей с этого континента.  Укажите здесь ID геолокации. |
| country | string | В расчёт метрики включаются только действия пользователей из этой страны.  Укажите здесь ID геолокации. |
| device | string | В расчёт метрики включаются только действия из этой версии приложения.  Применяется оператор EQUALS. |
| hasHttpError | boolean | Статус HTTP-ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с HTTP-ошибками. * `false`: включаются все действия. |
| hasReportedError | boolean | Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с зарегистрированными ошибками. * `false`: включаются все действия. |
| isp | string | В расчёт метрики включаются только действия от этого интернет-провайдера.  Применяется оператор EQUALS. |
| manufacturer | string | В расчёт метрики включаются только действия с устройств этого производителя.  Применяется оператор EQUALS. |
| networkTechnology | string | Фильтр по сетевой технологии |
| orientation | string | В расчёт метрики включаются только действия с устройств с этой ориентацией экрана. Возможные значения: * `LANDSCAPE` * `PORTRAIT` * `UNKNOWN` |
| osFamily | string | В расчёт метрики включаются только действия из этого семейства ОС.  Укажите здесь ID ОС. |
| osVersion | string | В расчёт метрики включаются только действия из этой версии ОС.  Укажите здесь ID ОС. |
| region | string | В расчёт метрики включаются только действия пользователей из этого региона.  Укажите здесь ID геолокации. |
| resolution | string | В расчёт метрики включаются только действия с устройств с этим разрешением экрана. Возможные значения: * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` |
| userActionName | string | В расчёт метрики включаются только действия с этим именем.  Применяется оператор EQUALS. |

### JSON-модели тела ответа

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

## Связанные темы

* [Создание вычисленных метрик для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших мобильных приложений.")
* [Создание вычисляемых метрик для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших пользовательских приложений.")