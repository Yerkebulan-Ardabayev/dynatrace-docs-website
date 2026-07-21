---
title: Metric events anomaly detection API - POST an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/post-event
---

# Metric events anomaly detection API - POST an event

# Metric events anomaly detection API - POST an event

* Справка
* Обновлено 26 апр. 2023 г.
* Устарело

Этот API устарел. Вместо него используй [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). Ищи схему **Metric events** (`builtin:anomaly-detection.metric-events`).

Создаёт новое правило метрик-события.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все модели JSON, зависящие от типа модели, перечислены в разделе [JSON models](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models "Learn the variations of models in metric event rules via the Dynatrace API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [MetricEvent](#openapi-definition-MetricEvent) | Тело JSON запроса. Содержит параметры нового метрик-события. | body | Опционально |

### Объекты тела запроса

#### Объект `MetricEvent`

Конфигурация метрик-события.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregationType | string | Способ агрегации точек данных метрики для оценки. Временной ряд должен поддерживать эту агрегацию. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `P90` * `SUM` * `VALUE` | Опционально |
| alertingScope | [MetricEventAlertingScope](#openapi-definition-MetricEventAlertingScope)[] | Определяет область действия метрик-события. Допустим только один фильтр на тип фильтра, кроме тегов, где допускается до 3. Фильтры комбинируются через конъюнкцию. | Опционально |
| description | string | Описание метрик-события. | Обязательно |
| disabledReason | string | Причина автоматического отключения. Значение `NONE` означает, что конфигурация не была отключена автоматически. Элемент может принимать значения * `METRIC_DEFINITION_INCONSISTENCY` * `NONE` * `TOO_MANY_DIMS` | Опционально |
| enabled | boolean | Метрик-событие включено (`true`) или отключено (`false`). | Обязательно |
| id | string | ID метрик-события. | Опционально |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опционально |
| metricDimensions | [MetricEventDimensions](#openapi-definition-MetricEventDimensions)[] | Определяет измерения метрики, по которым срабатывает оповещение. Фильтры комбинируются через конъюнкцию. | Опционально |
| metricId | string | ID метрики, оцениваемой метрик-событием. | Опционально |
| metricSelector | string | Селектор метрики, который нужно выполнить. | Опционально |
| monitoringStrategy | [MetricEventMonitoringStrategy](#openapi-definition-MetricEventMonitoringStrategy) | Стратегия мониторинга для конфигурации метрик-события. Это базовая версия стратегии мониторинга, в зависимости от типа фактическая модель JSON может содержать дополнительные поля. | Обязательно |
| name | string | Название метрик-события, отображаемое в интерфейсе. | Обязательно |
| primaryDimensionKey | string | Определяет, какой ключ измерения нужно использовать для **alertingScope**. | Опционально |
| queryOffset | integer | Определяет смещение запроса для адаптации периода оценки под известную задержку метрики. | Опционально |
| severity | string | Тип события, срабатывающего при нарушении порога. Тип `CUSTOM_ALERT` не коррелирует с другими оповещениями. Тип `INFO` не открывает проблему. Элемент может принимать значения * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Опционально |
| warningReason | string | Причина предупреждения, установленного для конфигурации. Значение `NONE` означает, что у конфигурации нет предупреждений. Элемент может принимать значения * `NONE` | Опционально |

#### Объект `MetricEventAlertingScope`

Один фильтр для области действия оповещения.

Фактический набор полей зависит от типа фильтра. Список фактических объектов см. в описании поля **filterType** или в разделе [Metric events anomaly detection API - JSON models﻿](https://dt-url.net/ql63sap?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filterType | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `ENTITY_ID` -> EntityIdAlertingScope * `MANAGEMENT_ZONE` -> ManagementZoneAlertingScope * `TAG` -> TagFilterAlertingScope * `NAME` -> NameAlertingScope * `CUSTOM_DEVICE_GROUP_NAME` -> CustomDeviceGroupNameAlertingScope * `HOST_GROUP_NAME` -> HostGroupNameAlertingScope * `HOST_NAME` -> HostNameAlertingScope * `PROCESS_GROUP_ID` -> ProcessGroupIdAlertingScope * `PROCESS_GROUP_NAME` -> ProcessGroupNameAlertingScope Элемент может принимать значения * `CUSTOM_DEVICE_GROUP_NAME` * `ENTITY_ID` * `HOST_GROUP_NAME` * `HOST_NAME` * `MANAGEMENT_ZONE` * `NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_NAME` * `TAG` | Обязательно |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опционально |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опционально |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опционально |

#### Объект `MetricEventDimensions`

Один фильтр для измерений метрики.

Фактический набор полей зависит от типа фильтра. Список фактических объектов см. в описании поля **filterType** или в разделе [Metric events anomaly detection API - JSON models﻿](https://dt-url.net/ql63sap?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filterType | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `ENTITY` -> MetricEventEntityDimensions * `STRING` -> MetricEventStringDimensions Элемент может принимать значения * `ENTITY` * `STRING` | Обязательно |
| key | string | Ключ измерения на метрике. | Опционально |

#### Объект `MetricEventMonitoringStrategy`

Стратегия мониторинга для конфигурации метрик-события.

Это базовая версия стратегии мониторинга, в зависимости от типа
фактическая модель JSON может содержать дополнительные поля.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STATIC_THRESHOLD` -> MetricEventStaticThresholdMonitoringStrategy * `AUTO_ADAPTIVE_BASELINE` -> MetricEventAutoAdaptiveBaselineMonitoringStrategy Элемент может принимать значения * `AUTO_ADAPTIVE_BASELINE` * `STATIC_THRESHOLD` | Обязательно |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"aggregationType": "AVG",



"alertingScope": [



{



"entityId": "HOST-000000000001E240",



"filterType": "ENTITY_ID"



},



{



"filterType": "TAG",



"tagFilter": {



"context": "CONTEXTLESS",



"key": "someKey",



"value": "someValue"



}



}



],



"description": "This is the description for my metric event.",



"disabledReason": "NONE",



"enabled": true,



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"metricDimensions": [



{



"filterType": "ENTITY",



"key": "dt.entity.disk",



"nameFilter": {



"operator": "EQUALS",



"value": "diskName"



}



}



],



"metricId": "com.dynatrace.builtin:host.disk.bytesread",



"monitoringStrategy": {



"alertCondition": "ABOVE",



"dealertingSamples": 5,



"samples": 5,



"threshold": 80,



"type": "STATIC_THRESHOLD",



"unit": "KILO_BYTE_PER_SECOND",



"violatingSamples": 3



},



"name": "My metric event",



"severity": "CUSTOM_ALERT",



"warningReason": "NONE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Метрик-событие создано. Ответ содержит ID и название только что созданного метрик-события |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

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

### Модели тела ответа JSON

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

## Проверка payload

Рекомендуется проверить payload перед отправкой с фактическим запросом. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, читай в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

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

#### Модели тела ответа JSON

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

## Пример

В этом примере запрос создаёт **пользовательское оповещение** (custom alert), которое срабатывает, если **свободное место на диске** опускается ниже **3%** в **3** из **5** выборок. Область действия оповещения, все хосты.

Токен API передаётся в заголовке **Authorization**.

Можно скачать или скопировать тело примера запроса, чтобы опробовать его самостоятельно.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/metricEvents \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"metricId": "com.dynatrace.builtin:host.disk.freespacepercentage",



"name": "Low disk space",



"description": "The available disk space is below 3%",



"aggregationType": "AVG",



"eventType": "CUSTOM_ALERT",



"alertCondition": "BELOW",



"samples": 5,



"violatingSamples": 3,



"dealertingSamples": 5,



"threshold": 3,



"enabled": true,



"tagFilters": []



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/metricEvents
```

#### Тело запроса

```
{



"metricId": "com.dynatrace.builtin:host.disk.freespacepercentage",



"name": "Low disk space",



"description": "The available disk space is below 3%",



"aggregationType": "AVG",



"eventType": "CUSTOM_ALERT",



"alertCondition": "BELOW",



"samples": 5,



"violatingSamples": 3,



"dealertingSamples": 5,



"threshold": 3,



"enabled": true,



"tagFilters": []



}
```

#### Тело ответа

```
{



"id": "1b06b18a-82df-4e18-a4aa-d4543b227734",



"name": "Low disk space",



"description": "The available disk space is below 3%"



}
```

#### Код ответа

204

#### Результат

Новое правило выглядит в UI так:

![Metric event rule - new](https://dt-cdn.net/images/metric-events-new-1234-0b9131aee3.png)

Metric event rule - new

## Похожие темы

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")