---
title: Metric events anomaly detection API - POST an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/post-event
scraped: 2026-05-12T12:15:40.054695
---

# Metric events anomaly detection API - POST an event

# Metric events anomaly detection API - POST an event

* Reference
* Updated on Apr 26, 2023
* Deprecated

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Metric events** (`builtin:anomaly-detection.metric-events`).

Создаёт новое правило metric event.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все JSON-модели, зависящие от типа модели, смотрите в [JSON models](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models "Изучите вариации моделей в правилах metric event через Dynatrace API.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [MetricEvent](#openapi-definition-MetricEvent) | JSON-тело запроса. Содержит параметры нового metric event. | body | Optional |

### Объекты тела запроса

#### Объект `MetricEvent`

Конфигурация metric event.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregationType | string | Как точки метрики агрегируются для оценки.  Временной ряд должен поддерживать эту агрегацию. Возможные значения: * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `P90` * `SUM` * `VALUE` | Optional |
| alertingScope | [MetricEventAlertingScope[]](#openapi-definition-MetricEventAlertingScope) | Определяет область действия metric event. Допускается только один фильтр на каждый тип фильтра, кроме тегов, где допускается до 3. Фильтры объединяются по конъюнкции. | Optional |
| description | string | Описание metric event. | Required |
| disabledReason | string | Причина автоматического отключения.  `NONE` означает, что конфигурация не была отключена автоматически. Возможные значения: * `METRIC_DEFINITION_INCONSISTENCY` * `NONE` * `TOO_MANY_DIMS` | Optional |
| enabled | boolean | Metric event включён (`true`) или отключён (`false`). | Required |
| id | string | ID metric event. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| metricDimensions | [MetricEventDimensions[]](#openapi-definition-MetricEventDimensions) | Определяет измерения метрики, по которым оповещать. Фильтры объединяются по конъюнкции. | Optional |
| metricId | string | ID метрики, оцениваемой metric event. | Optional |
| metricSelector | string | Селектор метрики, который должен быть выполнен. | Optional |
| monitoringStrategy | [MetricEventMonitoringStrategy](#openapi-definition-MetricEventMonitoringStrategy) | Стратегия мониторинга для конфигурации metric event.  Это базовая версия стратегии мониторинга, в зависимости от типа фактический JSON может содержать дополнительные поля. | Required |
| name | string | Имя metric event, отображаемое в UI. | Required |
| primaryDimensionKey | string | Определяет, какой ключ измерения использовать для **alertingScope**. | Optional |
| queryOffset | integer | Определяет смещение запроса для адаптации интервала оценки под известную задержку метрики. | Optional |
| severity | string | Тип события для срабатывания при нарушении порога.  Тип `CUSTOM_ALERT` не коррелируется с другими оповещениями. Тип `INFO` не открывает проблему. Возможные значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Optional |
| warningReason | string | Причина предупреждения, установленного на конфигурацию.  `NONE` означает, что у конфигурации нет предупреждений. Возможные значения: * `NONE` | Optional |

#### Объект `MetricEventAlertingScope`

Одиночный фильтр области действия оповещения.

Фактический набор полей зависит от типа фильтра. Список фактических объектов смотрите в описании поля **filterType** или в [Metric events anomaly detection API - JSON models](https://dt-url.net/ql63sap).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filterType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `ENTITY_ID` -> EntityIdAlertingScope * `MANAGEMENT_ZONE` -> ManagementZoneAlertingScope * `TAG` -> TagFilterAlertingScope * `NAME` -> NameAlertingScope * `CUSTOM_DEVICE_GROUP_NAME` -> CustomDeviceGroupNameAlertingScope * `HOST_GROUP_NAME` -> HostGroupNameAlertingScope * `HOST_NAME` -> HostNameAlertingScope * `PROCESS_GROUP_ID` -> ProcessGroupIdAlertingScope * `PROCESS_GROUP_NAME` -> ProcessGroupNameAlertingScope Возможные значения: * `CUSTOM_DEVICE_GROUP_NAME` * `ENTITY_ID` * `HOST_GROUP_NAME` * `HOST_NAME` * `MANAGEMENT_ZONE` * `NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_NAME` * `TAG` | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `MetricEventDimensions`

Одиночный фильтр измерений метрик.

Фактический набор полей зависит от типа фильтра. Список фактических объектов смотрите в описании поля **filterType** или в [Metric events anomaly detection API - JSON models](https://dt-url.net/ql63sap).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| filterType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `ENTITY` -> MetricEventEntityDimensions * `STRING` -> MetricEventStringDimensions Возможные значения: * `ENTITY` * `STRING` | Required |
| key | string | Ключ измерений метрики. | Optional |

#### Объект `MetricEventMonitoringStrategy`

Стратегия мониторинга для конфигурации metric event.

Это базовая версия стратегии мониторинга, в зависимости от типа
фактический JSON может содержать дополнительные поля.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STATIC_THRESHOLD` -> MetricEventStaticThresholdMonitoringStrategy * `AUTO_ADAPTIVE_BASELINE` -> MetricEventAutoAdaptiveBaselineMonitoringStrategy Возможные значения: * `AUTO_ADAPTIVE_BASELINE` * `STATIC_THRESHOLD` | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Metric event создан. Ответ содержит ID и имя только что созданного metric event |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
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

## Пример

В этом примере запрос создаёт **custom alert**, который срабатывает, если **free disk space** падает ниже **3%** в **3** из **5** замеров. Область действия оповещения это **все** хосты.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

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

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")