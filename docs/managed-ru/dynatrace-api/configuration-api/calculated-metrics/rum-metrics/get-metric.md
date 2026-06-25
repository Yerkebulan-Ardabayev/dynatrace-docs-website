---
title: Web application metrics API - GET a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/rum-metrics/get-metric
scraped: 2026-05-12T11:17:54.466478
---

# Web application metrics API - GET a metric

# Web application metrics API - GET a metric

* Reference
* Published Feb 28, 2020

Возвращает дескриптор указанной вычисляемой метрики веб-приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/rum/{metricKey}` |

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
| **200** | [WebApplicationMetric](#openapi-definition-WebApplicationMetric) | Успех |

### Объекты тела ответа

#### Объект `WebApplicationMetric`

Дескриптор вычисляемой метрики веб-приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationIdentifier | string | ID сущности Dynatrace приложения, которому принадлежит метрика. |
| dimensions | [WebApplicationDimensionDefinition[]](#openapi-definition-WebApplicationDimensionDefinition) | Список измерений метрики. |
| enabled | boolean | Метрика включена (`true`) или отключена (`false`). |
| metricDefinition | [WebApplicationMetricDefinition](#openapi-definition-WebApplicationMetricDefinition) | Определение метрики веб-приложения. |
| metricKey | string | Уникальный ключ метрики.  Ключ должен иметь префикс `calc:apps`. |
| name | string | Отображаемое имя метрики. |
| userActionFilter | [UserActionFilter](#openapi-definition-UserActionFilter) | Фильтр пользовательских действий вычисляемой метрики веб-приложения.  Для расчёта метрики используются только пользовательские действия, соответствующие заданным критериям.  Пользовательское действие должно соответствовать **всем** критериям. |

#### Объект `WebApplicationDimensionDefinition`

Измерение вычисляемых метрик веб-приложений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimension | string | Измерение метрики. Возможные значения: * `ApdexType` * `Browser` * `ErrorContext` * `ErrorOrigin` * `ErrorType` * `GeoLocation` * `StringProperty` * `UserActionType` |
| propertyKey | string | Ключ свойства пользовательского действия.  Применимо только для измерения `StringProperty`. |
| topX | integer | Количество верхних значений для расчёта. |

#### Объект `WebApplicationMetricDefinition`

Определение метрики веб-приложения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metric | string | Тип метрики веб-приложения. Возможные значения: * `Apdex` * `ApplicationCache` * `Callback` * `CumulativeLayoutShift` * `DNSLookup` * `DOMComplete` * `DOMContentLoaded` * `DOMInteractive` * `DoubleProperty` * `ErrorCount` * `FirstContentfulPaint` * `FirstInputDelay` * `FirstInputStart` * `FirstPaint` * `HTMLDownloaded` * `LargestContentfulPaint` * `LoadEventEnd` * `LoadEventStart` * `LongProperty` * `LongTasksTime` * `NavigationStart` * `OnDOMContentLoaded` * `OnLoad` * `Processing` * `RedirectTime` * `Request` * `RequestStart` * `Response` * `SecureConnect` * `SpeedIndex` * `TCPConnect` * `TimeToFirstByte` * `UserActionDuration` * `VisuallyComplete` |
| propertyKey | string | Ключ свойства пользовательского действия.  Применимо только для метрик `DoubleProperty` и `LongProperty`. |

#### Объект `UserActionFilter`

Фильтр пользовательских действий вычисляемой метрики веб-приложения.

Для расчёта метрики используются только пользовательские действия, соответствующие заданным критериям.

Пользовательское действие должно соответствовать **всем** критериям.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actionDurationFromMilliseconds | integer | В расчёт метрики включаются только действия с длительностью больше или равной этому значению (в миллисекундах). |
| actionDurationToMilliseconds | integer | В расчёт метрики включаются только действия с длительностью меньше или равной этому значению (в миллисекундах). |
| apdex | string | В расчёт метрики включаются только действия с указанной оценкой Apdex. Возможные значения: * `Frustrated` * `Satisfied` * `Tolerating` * `Unknown` |
| browserFamily | string | В расчёт метрики включаются только пользовательские действия из указанного семейства браузеров.  Применяется оператор EQUALS. |
| browserType | string | В расчёт метрики включаются только пользовательские действия из указанного типа браузера.  Применяется оператор EQUALS. |
| browserVersion | string | В расчёт метрики включаются только пользовательские действия из указанной версии браузера.  Применяется оператор EQUALS. |
| city | string | В расчёт метрики включаются только действия пользователей из этого города.  Укажите здесь ID геолокации. |
| continent | string | В расчёт метрики включаются только действия пользователей с этого континента.  Укажите здесь ID геолокации. |
| country | string | В расчёт метрики включаются только действия пользователей из этой страны.  Укажите здесь ID геолокации. |
| customAction | boolean | Статус кастомных действий в расчёте метрики:  * `true`: включаются кастомные действия. * `false`: включаются все действия. |
| customErrorName | string | Имя кастомной ошибки действий, включаемых в расчёт метрики. |
| customErrorType | string | Тип кастомной ошибки действий, включаемых в расчёт метрики. |
| domain | string | В расчёт метрики включаются только пользовательские действия из указанного домена.  Применяется оператор EQUALS. |
| hasAnyError | boolean | Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с любыми ошибками. * `false`: включаются все действия. |
| hasCustomErrors | boolean | Статус кастомных ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с кастомными ошибками. * `false`: включаются все действия. |
| hasHttpErrors | boolean | Статус ошибок запросов действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками запросов (HTTP-ошибки, неудавшиеся изображения, нарушения правил CSP). * `false`: включаются все действия. |
| hasJavascriptErrors | boolean | Статус ошибок JavaScript действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками JavaScript. * `false`: включаются все действия. |
| httpErrorCode | integer | Код статуса HTTP-ошибки действий, включаемых в расчёт метрики. |
| httpErrorCodeTo | integer | Можно использовать вместе с `httpErrorCode` для задания диапазона кодов ошибок, которые будут включены в расчёт метрики. |
| httpPath | string | Путь запроса, определённый как источник HTTP-ошибки действий, включаемых в расчёт метрики. |
| ip | string | В расчёт метрики включаются только действия с этого IP-адреса.  Применяется оператор EQUALS. |
| ipV6Traffic | boolean | Статус IPv6 действий, включаемых в расчёт метрики:  * `true`: включаются только действия по IPv6. * `false`: включаются все действия. |
| loadAction | boolean | Статус load-действий в расчёте метрики:  * `true`: включаются load-действия. * `false`: включаются все действия. |
| osFamily | string | В расчёт метрики включаются только действия из этого семейства ОС.  Укажите здесь ID ОС. |
| osVersion | string | В расчёт метрики включаются только действия из этой версии ОС.  Укажите здесь ID ОС. |
| realUser | boolean | Статус действий от реальных пользователей в расчёте метрики:  * `true`: включаются только действия реальных пользователей. * `false`: включаются все действия. |
| region | string | В расчёт метрики включаются только действия пользователей из этого региона.  Укажите здесь ID геолокации. |
| robot | boolean | Статус действий от роботов в расчёте метрики:  * `true`: включаются только действия роботов. * `false`: включаются все действия. |
| synthetic | boolean | Статус действий от synthetic monitors в расчёте метрики:  * `true`: включаются только действия от synthetic monitors. * `false`: включаются все действия. |
| targetViewGroup | string | В расчёт метрики включаются только действия на указанной группе представлений. |
| targetViewGroupNameMatchType | string | Указывает тип совпадения для фильтра группы представлений, например с помощью `Contains` или `Equals`. По умолчанию `Equals`. Возможные значения: * `Contains` * `Equals` |
| targetViewName | string | В расчёт метрики включаются только действия на указанном представлении. |
| targetViewNameMatchType | string | Указывает тип совпадения для фильтра имени представления, например с помощью `Contains` или `Equals`. По умолчанию `Equals`. Возможные значения: * `Contains` * `Equals` |
| userActionName | string | В расчёт метрики включаются только действия с этим именем.  Применяется оператор EQUALS. |
| userActionProperties | [UserActionPropertyFilter[]](#openapi-definition-UserActionPropertyFilter) | В расчёт метрики включаются только действия с указанными свойствами. |
| xhrAction | boolean | Статус XHR-действий в расчёте метрики:  * `true`: включаются XHR-действия. * `false`: включаются все действия. |
| xhrRouteChangeAction | boolean | Статус действий смены маршрута в расчёте метрики:  * `true`: включаются действия смены маршрута. * `false`: включаются все действия. |

#### Объект `UserActionPropertyFilter`

Фильтр свойств пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| from | number | В расчёт метрики включаются только действия со значением больше или равным этому.  Применимо только к числовым значениям. |
| key | string | Ключ проверяемого свойства действия. |
| matchType | string | Указывает тип совпадения для строкового фильтра, например с помощью `Contains` или `Equals`.  Применимо только к строковым значениям. Возможные значения: * `Contains` * `Equals` |
| to | number | В расчёт метрики включаются только действия со значением меньше или равным этому.  Применимо только к числовым значениям. |
| value | string | В расчёт метрики включаются только действия, у которых это значение в указанном свойстве.  Применимо только к строковым значениям. |

### JSON-модели тела ответа

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

## Связанные темы

* [Создание вычисляемых метрик для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших веб-приложений.")