---
title: Synthetic metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics/get-metric
scraped: 2026-05-12T11:19:22.455973
---

# Synthetic metrics API - GET a metric

# Synthetic metrics API - GET a metric

* Reference
* Published Apr 16, 2020

Возвращает дескриптор указанной вычисляемой синтетической метрики.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/synthetic/{metricKey}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ требуемой вычисляемой синтетической метрики. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CalculatedSyntheticMetric](#openapi-definition-CalculatedSyntheticMetric) | Успех |

### Объекты тела ответа

#### Объект `CalculatedSyntheticMetric`

Определение вычисляемой синтетической метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | [SyntheticMetricDimension[]](#openapi-definition-SyntheticMetricDimension) | Список измерений метрики. |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). |
| filter | [SyntheticMetricFilter](#openapi-definition-SyntheticMetricFilter) | Фильтр вычисляемой синтетической метрики. |
| metric | string | Тип синтетической метрики. Возможные значения: * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `FailedRequestsResources` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `HttpErrors` * `JavaScriptErrors` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongTasks` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `ResourceCount` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `TotalDuration` * `TransferSize` * `UserActionDuration` * `VisuallyComplete` |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:synthetic`. |
| monitorIdentifier | string | ID сущности Dynatrace synthetic monitor, которому принадлежит метрика. |
| name | string | Имя метрики, отображаемое в UI. |

#### Объект `SyntheticMetricDimension`

Измерение вычисляемой синтетической метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `Event` * `Location` * `ResourceOrigin` |
| topX | integer | Количество верхних значений для расчёта. |

#### Объект `SyntheticMetricFilter`

Фильтр вычисляемой синтетической метрики.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actionType | string | В расчёт метрики включаются только пользовательские действия указанного типа. Возможные значения: * `Custom` * `Load` * `Xhr` |
| errorCode | integer | В расчёт метрики включаются только выполнения, завершившиеся с указанным кодом ошибки. |
| event | string | В расчёт метрики включается только указанное событие browser clickpath.  Укажите здесь ID сущности Dynatrace события. Список clickpath-событий монитора можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API |
| hasError | boolean | Статус выполнения мониторов, включаемых в расчёт метрики:  * `true`: включаются только неудавшиеся выполнения. * `false`: включаются все выполнения. |
| location | string | В расчёт метрики включаются только выполнения из указанной локации.  Укажите здесь ID сущности Dynatrace локации. Список локаций, из которых работает монитор, можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API. |

### JSON-модели тела ответа

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

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")