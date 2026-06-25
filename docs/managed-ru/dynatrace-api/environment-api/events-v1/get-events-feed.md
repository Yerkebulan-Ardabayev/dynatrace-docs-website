---
title: Events API v1 - GET лента событий
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/get-events-feed
scraped: 2026-05-12T12:13:35.854481
---

# Events API v1 - GET лента событий

# Events API v1 - GET лента событий

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте, что можно делать с Dynatrace Events API v2.").

Перечисляет **все** события вашего окружения и их параметры. Поскольку возможное количество событий может быть большим, ответ ограничен 150 событиями. Вывод можно сузить, указав параметры фильтрации в запросе.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/events` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | integer | Начальная метка времени запроса, в миллисекундах UTC.  Если не задано, используется значение 30 дней назад от текущего момента, если не задан **relativeTime**. | query | Необязательный |
| to | integer | Конечная метка времени запроса, в миллисекундах UTC.  Если не задано, используется текущая метка времени, если не задан **relativeTime**.  Временной диапазон не должен превышать 2 года. | query | Необязательный |
| relativeTime | string | Относительный диапазон, назад от текущего времени. Элемент может принимать значения * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Необязательный |
| eventType | string | Фильтрует результирующий набор событий по типу события. Элемент может принимать значения * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` | query | Необязательный |
| entityId | string | Фильтрует результирующий набор событий до событий, связанных с указанной сущностью Dynatrace. | query | Необязательный |
| cursor | string | Ответ ограничен 150 событиями, поэтому если вы хотите получить больше, можно использовать cursor для получения следующих 150. Этот параметр должен быть пустым при первом запросе.  Ключ cursor затем можно найти в поле **nextCursor** предыдущего ответа.  При использовании строки cursor нет необходимости указывать дополнительные параметры, так как эта информация уже закодирована в cursor. | query | Необязательный |

## Ответ

Каждое событие содержит как минимум следующие элементы метаинформации и специфичные для события свойства.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EventQueryResult](#openapi-definition-EventQueryResult) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventQueryResult`

События окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| events | [EventRestEntry[]](#openapi-definition-EventRestEntry) | Список событий. |
| from | integer | Начало временного диапазона запроса. |
| nextCursor | string | Cursor для следующих 150 событий, соответствующих указанным критериям.  Задайте это значение для query-параметра **cursor**. Без него вы снова получите первые 150 событий.  Не нужно указывать дополнительные параметры, так как cursor уже содержит их все. |
| to | integer | Конец временного диапазона запроса. |
| totalEventCount | integer | Общее количество событий, соответствующих указанным критериям. |

#### Объект `EventRestEntry`

Набор параметров события.

Помимо общих свойств, упомянутых здесь, которые есть у каждого события, реальное событие имеет набор метаданных, который варьируется в зависимости от типа события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| endTime | integer | Метка времени закрытия события, в миллисекундах UTC |
| entityId | string | ID затронутой сущности Dynatrace. |
| entityName | string | Имя затронутой сущности Dynatrace. |
| eventStatus | string | Состояние события: открыто или закрыто. Элемент может принимать значения * `CLOSED` * `OPEN` |
| eventType | string | Тип события. Элемент может принимать значения * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| id | string | Закодированный ID события. Формат: *eventID\_startTime*.  Используйте значение из этого поля, когда вам нужен ID события. |
| impactLevel | string | Уровень воздействия события. Показывает, что затронуто проблемой: инфраструктура, сервис или приложение. Элемент может принимать значения * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| metadata | object | Различная метаинформация о событии. |
| resourceId | string | ID ресурса, на котором произошло событие. |
| resourceName | string | Имя ресурса, на котором произошло событие. |
| severityLevel | string | Критичность события. Элемент может принимать значения * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | Метка времени обнаружения события, в миллисекундах UTC. |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Теги сущности Dynatrace, вызвавшей событие. |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Элемент может принимать значения * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"events": [



{



"endTime": 1521542929000,



"entityId": "HOST-0000000000000007",



"entityName": "Example Host",



"eventStatus": "OPEN",



"eventType": "SLOW_DISK",



"id": "5915682011263205071_1521042929000",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "PERFORMANCE",



"source": "builtin",



"startTime": 1521042929000,



"tags": [



{



"context": "CONTEXTLESS",



"key": "exampleTag"



}



]



},



{



"endTime": 1521542929000,



"entityId": "HOST-0000000000000007",



"entityName": "Example Host",



"eventStatus": "OPEN",



"eventType": "SLOW_DISK",



"id": "5915682011263205071_1521042929000",



"impactLevel": "INFRASTRUCTURE",



"severityLevel": "PERFORMANCE",



"source": "builtin",



"startTime": 1521042929000,



"tags": [



{



"context": "CONTEXTLESS",



"key": "exampleTag"



}



]



}



],



"from": 1521042929000,



"nextCursor": "AgEBAAFn5IIFrgEAAAFofwDTrgAAAQAcMTY4N2RhYzViZTAtZmUxODEwOWQ5YTA1MTIyNQ%3D%3D",



"to": 1521542929000,



"totalEventCount": 2



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

## Пример

В этом примере запрос запрашивает все события **ERROR\_EVENT**, произошедшие за **последние 24 часа**. Результат усечён до двух событий.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/events?eventType=ERROR_EVENT&relativeTime=day' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/events?eventType=ERROR_EVENT&relativeTime=day
```

#### Содержимое ответа

```
{



"nextEventStartTms": null,



"nextEventId": null,



"nextCursor": null,



"from": 1530703635653,



"to": 1533295635653,



"totalEventCount": 25,



"events": [



{



"eventId": -8338439733889003014,



"startTime": 1532328338475,



"endTime": 1532328638475,



"entityId": "HOST-E4D1E5F46E239F21",



"entityName": "l-8.dyna.trace",



"severityLevel": "ERROR",



"impactLevel": "INFRASTRUCTURE",



"eventType": "ERROR_EVENT",



"eventStatus": "CLOSED",



"tags": [



{



"context": "CONTEXTLESS",



"key": "deploy"



},



{



"context": "CONTEXTLESS",



"key": "room23"



}



],



"id": "-8338439733889003014_1532328338475",



"annotationDescription": "testTrigger",



"correlationId": "67da0a4293956e55",



"source": "restTest"



},



{



"eventId": 3092227520312561338,



"startTime": 1531832640600,



"endTime": 1531836240600,



"entityId": "HOST-CE6A2253598EA88D",



"entityName": "q2.docker.l5",



"severityLevel": "ERROR",



"impactLevel": "INFRASTRUCTURE",



"eventType": "ERROR_EVENT",



"eventStatus": "CLOSED",



"tags": [



{



"context": "CONTEXTLESS",



"key": "ServiceNow"



}



],



"id": "3092227520312561338_1531832640600",



"customProperties": {



"Property 2": "value 2",



"Property 1": "value 1",



"Property 3": "value 3"



},



"annotationDescription": "package is damaged",



"correlationId": "1b79973c6902b486",



"source": "myAPI"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий, поддерживаемых типах событий, уровнях критичности и логике их формирования.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Понимание секции Events на странице обзора хостов, процессов и сервисов.")
* [Creating a deployment event via the Dynatrace API](https://www.youtube.com/watch?v=LDAiUMdrtvA)