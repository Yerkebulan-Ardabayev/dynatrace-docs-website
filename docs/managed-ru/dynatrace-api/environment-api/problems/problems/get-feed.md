---
title: Problems API - GET лента
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/get-feed
scraped: 2026-05-12T12:08:07.912666
---

# Problems API - GET лента

# Problems API - GET лента

* Справочник
* Обновлено 13 июня 2022 г.

Этот API устарел. Используйте вместо него [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте о возможностях Dynatrace Problems API v2.").

Возвращает список проблем (и их детали), обнаруженных Dynatrace за относительный период времени.

Проблема включается в ответ, если метка времени начала или окончания проблемы попадает в заданный временной диапазон.

Вывод ограничен **5 000** проблемами. Сузить его можно, указав критерии фильтрации, смотрите [раздел **Параметры**](#parameters).

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/feed` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/feed` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| relativeTime | string | Относительный временной диапазон запроса, отсчитываемый назад от текущего времени. Поле может принимать значения: * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Необязательный |
| startTimestamp | integer | Метка времени начала запрашиваемого диапазона, в UTC миллисекундах. | query | Необязательный |
| endTimestamp | integer | Метка времени окончания запрашиваемого диапазона, в UTC миллисекундах.  Если `endTimestamp` позже текущего времени, используется текущее время.  Диапазон не должен превышать 31 день. | query | Необязательный |
| status | string | Фильтрует проблемы в результате по статусу. Поле может принимать значения: * `CLOSED` * `OPEN` | query | Необязательный |
| impactLevel | string | Фильтрует проблемы в результате по уровню воздействия. Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` | query | Необязательный |
| severityLevel | string | Фильтрует проблемы в результате по уровню серьёзности. Поле может принимать значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` | query | Необязательный |
| tag | string[] | Фильтрует проблемы в результате по тегам затронутых сущностей.Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Проблема должна соответствовать *всем* указанным тегам.  Для тегов вида ключ-значение, например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `[context]key:value`. | query | Необязательный |
| expandDetails | boolean | Включает (`true`) или исключает (`false`) связанные события в ответе.  По умолчанию `false`, связанные события исключаются. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ProblemFeedResultWrapper](#openapi-definition-ProblemFeedResultWrapper) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ProblemFeedResultWrapper`

| Поле | Тип | Описание |
| --- | --- | --- |
| result | [ProblemFeedQueryResult](#openapi-definition-ProblemFeedQueryResult) | Детали открытых проблем в вашем окружении. |

#### Объект `ProblemFeedQueryResult`

Детали открытых проблем в вашем окружении.

| Поле | Тип | Описание |
| --- | --- | --- |
| monitored | object | Количество отслеживаемых сущностей по уровням воздействия. |
| problems | [Problem[]](#openapi-definition-Problem) | Список проблем и их деталей.  Содержит все проблемы за указанный диапазон, открытые и закрытые. |

#### Объект `Problem`

Свойства проблемы.

| Поле | Тип | Описание |
| --- | --- | --- |
| affectedCounts | object | Количество затронутых сущностей по уровням воздействия. |
| commentCount | integer | Количество комментариев к проблеме. |
| displayName | string | Имя проблемы, отображаемое в UI. |
| endTime | integer | Метка времени окончания проблемы, в UTC миллисекундах.  Имеет значение `-1`, если проблема ещё открыта. |
| hasRootCause | boolean | Указывает, нашёл ли Dynatrace хотя бы одну возможную первопричину проблемы. |
| id | string | ID проблемы. |
| impactLevel | string | Уровень воздействия проблемы. Показывает, что затронуто проблемой: инфраструктура, сервис или приложение. Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| rankedEvents | [Event[]](#openapi-definition-Event) | Список событий, связанных с проблемой. |
| rankedImpacts | [EventRestImpact[]](#openapi-definition-EventRestImpact) | Предоставляет информацию о воздействии событий в агрегированном виде. Для более детального анализа воздействия смотрите `rankedEvents`. |
| recoveredCounts | object | Количество сущностей, которые были затронуты, но восстановились, по уровням воздействия. |
| severityLevel | string | Серьёзность проблемы. Поле может принимать значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | Метка времени начала проблемы, в UTC миллисекундах. |
| status | string | Статус проблемы. Поле может принимать значения: * `CLOSED` * `OPEN` |
| tagsOfAffectedEntities | [TagInfo[]](#openapi-definition-TagInfo) | Теги сущностей, затронутых проблемой. |

#### Объект `Event`

Свойства события.

| Поле | Тип | Описание |
| --- | --- | --- |
| activeMaintenanceWindows | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | - |
| affectedPrivateSyntheticLocations | string[] | - |
| affectedRequestsPerMinute | number | - |
| affectedSyntheticActions | string[] | Если тип события является одним из синтетических типов событий, может быть доступна информация о том, какие синтетические действия затронуты событием. Их имена возвращаются в этом поле. |
| affectedSyntheticLocations | string[] | - |
| affectedUserActionsPerMinute | number | - |
| annotationDescription | string | - |
| annotationType | string | - |
| artifact | string | - |
| browser | string | Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICES` |
| changed | string | - |
| ciBackLink | string | - |
| correlationId | string | - |
| cpuLimitInMHz | integer | - |
| cpuLoad | number | - |
| customProperties | object | - |
| deploymentName | string | - |
| deploymentParamAdded | string | - |
| deploymentParamRemoved | string | - |
| deploymentProject | string | - |
| deploymentVersion | string | - |
| effectiveEntity | string | - |
| endTime | integer | Метка времени закрытия события, в UTC миллисекундах.  Имеет значение `-1`, если событие ещё открыто. |
| entityId | string | ID затронутой сущности Dynatrace. |
| entityName | string | Имя затронутой сущности Dynatrace. |
| eventType | string | Тип события. Поле может принимать значения: * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| geolocation | string | - |
| impactLevel | string | Уровень воздействия события. Показывает, что затронуто проблемой: инфраструктура, сервис или приложение. Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| isClusterWide | boolean | Для событий с типом `MONITORING_UNAVAILABLE` событие может происходить на всём кластере Dynatrace. Если это так, возможны проблемы на стороне Dynatrace. |
| isRootCause | boolean | Указывает, является ли событие первопричиной проблемы. |
| metadata | object | Метаданные события. |
| minimumProcessGroupInstanceCountThreshold | integer | - |
| mobileAppVersion | string | - |
| operatingSystem | string | - |
| original | string | - |
| percentile | string | Поле может принимать значения: * `50th` * `90th` |
| referenceResponseTime50thPercentile | number | - |
| referenceResponseTime90thPercentile | number | - |
| remediationAction | string | - |
| resourceId | string | ID ресурса, на котором произошло событие. |
| resourceName | string | Имя ресурса, на котором произошло событие. |
| service | string | - |
| serviceMethod | string | - |
| serviceMethodGroup | string | - |
| severities | [EventSeverity[]](#openapi-definition-EventSeverity) | Дополнительные данные о серьёзности события. |
| severityLevel | string | Серьёзность события. Поле может принимать значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| source | string | - |
| startTime | integer | Метка времени обнаружения события, в UTC миллисекундах. |
| status | string | Статус события. Поле может принимать значения: * `CLOSED` * `OPEN` |
| syntheticErrorType | string[] | Если тип события является одним из синтетических типов событий, может быть доступна информация о типе ошибки. Их имена возвращаются в этом поле. |
| userAction | string | - |
| userDefined50thPercentileThreshold | number | - |
| userDefined90thPercentileThreshold | number | - |
| userDefinedFailureRateThreshold | number | - |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Поле | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `AnyValue`

Схема, представляющая произвольный тип значения.

#### Объект `EventSeverity`

Дополнительные данные о серьёзности события.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Метрика, используемая при расчёте серьёзности события. Поле может принимать значения: * `COMMAND_ABORT` * `CPU_READY_TIME` * `CPU_USAGE` * `CRASH_RATE` * `FAILURE_RATE` * `HYPERVISOR_PACKETS_RECEIVED_DROPPED` * `HYPERVISOR_PACKETS_TRANSMITTED_DROPPED` * `MEMORY_COMPRESSION_RATE` * `MEMORY_DECOMPRESSION_RATE` * `MEMORY_SWAP_IN_RATE` * `MEMORY_SWAP_OUT_RATE` * `MEMORY_USAGE` * `NETWORK_HIGH_RECEIVED_UTILIZATION_RATE` * `NETWORK_HIGH_TRANSMITTED_UTILIZATION_RATE` * `NETWORK_PACKETS_RECEIVED_DROPPED` * `NETWORK_PACKETS_TRANSMITTED_DROPPED` * `NETWORK_RECEIVED_ERROR_RATE` * `NETWORK_TRANSMITTED_ERROR_RATE` * `PAGE_FAULTS` * `PG_AVAILABLE` * `RESPONSE_TIME_50TH_PERCENTILE` * `RESPONSE_TIME_90TH_PERCENTILE` |
| unit | string | Единица измерения значения серьёзности. Поле может принимать значения: * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (Âµs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (â°)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| value | number | Значение серьёзности. |

#### Объект `EventRestImpact`

Информация о воздействии события.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | ID затронутой сущности Dynatrace. |
| entityName | string | Имя затронутой сущности Dynatrace. |
| eventType | string | Тип события. Поле может принимать значения: * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| impactLevel | string | Уровень воздействия события. Показывает, что затронуто проблемой: инфраструктура, сервис или приложение. Поле может принимать значения: * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| resourceId | string | ID ресурса, на котором произошло событие. |
| resourceName | string | Имя ресурса, на котором произошло событие. |
| severityLevel | string | Серьёзность события. Поле может принимать значения: * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |

#### Объект `TagInfo`

Тег сущности Dynatrace.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Поле может принимать значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  Пользовательские теги содержат здесь значение тега. |
| value | string | Значение тега.  Неприменимо к пользовательским тегам. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"result": {



"monitored": {



"APPLICATION": 1,



"ENVIRONMENT": 1,



"INFRASTRUCTURE": 1,



"SERVICE": 1



},



"problems": [



{



"affectedCounts": {



"APPLICATION": 1,



"ENVIRONMENT": 1,



"INFRASTRUCTURE": 1,



"SERVICE": 1



},



"commentCount": 1,



"displayName": "string",



"endTime": 1,



"hasRootCause": true,



"id": "string",



"impactLevel": "APPLICATION",



"rankedEvents": [



{



"activeMaintenanceWindows": [



{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}



],



"affectedPrivateSyntheticLocations": [



"string"



],



"affectedRequestsPerMinute": 1,



"affectedSyntheticActions": [



"string"



],



"affectedSyntheticLocations": [



"string"



],



"affectedUserActionsPerMinute": 1,



"annotationDescription": "string",



"annotationType": "string",



"artifact": "string",



"browser": "APPLICATION",



"changed": "string",



"ciBackLink": "string",



"correlationId": "string",



"cpuLimitInMHz": 1,



"cpuLoad": 1,



"customProperties": {},



"deploymentName": "string",



"deploymentParamAdded": "string",



"deploymentParamRemoved": "string",



"deploymentProject": "string",



"deploymentVersion": "string",



"effectiveEntity": "string",



"endTime": 1,



"entityId": "string",



"entityName": "string",



"eventType": "APPLICATION_JS_FRAMEWORK_DETECTED",



"geolocation": "string",



"impactLevel": "APPLICATION",



"isClusterWide": true,



"isRootCause": true,



"metadata": {



"empty": true



},



"minimumProcessGroupInstanceCountThreshold": 1,



"mobileAppVersion": "string",



"operatingSystem": "string",



"original": "string",



"percentile": "50th",



"referenceResponseTime50thPercentile": 1,



"referenceResponseTime90thPercentile": 1,



"remediationAction": "string",



"resourceId": "string",



"resourceName": "string",



"service": "string",



"serviceMethod": "string",



"serviceMethodGroup": "string",



"severities": [



{



"context": "COMMAND_ABORT",



"unit": "Ampere (A)",



"value": 1



}



],



"severityLevel": "AVAILABILITY",



"source": "string",



"startTime": 1,



"status": "CLOSED",



"syntheticErrorType": [



"string"



],



"userAction": "string",



"userDefined50thPercentileThreshold": 1,



"userDefined90thPercentileThreshold": 1,



"userDefinedFailureRateThreshold": 1



}



],



"rankedImpacts": [



{



"entityId": "string",



"entityName": "string",



"eventType": "APPLICATION_JS_FRAMEWORK_DETECTED",



"impactLevel": "APPLICATION",



"resourceId": "string",



"resourceName": "string",



"severityLevel": "AVAILABILITY"



}



],



"recoveredCounts": {



"APPLICATION": 1,



"ENVIRONMENT": 1,



"INFRASTRUCTURE": 1,



"SERVICE": 1



},



"severityLevel": "AVAILABILITY",



"startTime": 1,



"status": "CLOSED",



"tagsOfAffectedEntities": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



]



}



]



}



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

В этом примере запрос получает проблемы, возникшие за **последний час** и затрагивающие **инфраструктуру**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до первых двух записей.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?impactLevel=INFRASTRUCTURE&relativeTime=hour' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?impactLevel=INFRASTRUCTURE&relativeTime=hour
```

#### Тело ответа

```
{



"result": {



"problems": [



{



"id": "-1024851378335816085_1538553240000V2",



"startTime": 1538553240000,



"endTime": 7258118400000,



"displayName": "85",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "ERROR",



"commentCount": 0,



"tagsOfAffectedEntities": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



}



],



"rankedImpacts": [



{



"entityId": "PROCESS_GROUP_INSTANCE-DE765F657721AF59",



"entityName": "IIS app pool dotNetBackend_easyTravel_x64",



"severityLevel": "ERROR",



"impactLevel": "INFRASTRUCTURE",



"eventType": "PROCESS_LOG_ERROR"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 0,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": true



},



{



"id": "2307087411653364173_1538400720000V2",



"startTime": 1538400720000,



"endTime": 7258118400000,



"displayName": "173",



"impactLevel": "INFRASTRUCTURE",



"status": "OPEN",



"severityLevel": "AVAILABILITY",



"commentCount": 0,



"tagsOfAffectedEntities": [



{



"context": "CONTEXTLESS",



"key": "loadtest"



},



{



"context": "CONTEXTLESS",



"key": "ServiceNow"



},



{



"context": "CONTEXTLESS",



"key": "host tag"



}



],



"rankedImpacts": [



{



"entityId": "PROCESS_GROUP-09875E82E2FB98FD",



"entityName": "Windows System",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "PROCESS_GROUP_LOW_INSTANCE_COUNT"



},



{



"entityId": "HOST-ED6BC51DEBA8093A",



"entityName": "ZID",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "CONNECTION_LOST"



}



],



"affectedCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"recoveredCounts": {



"INFRASTRUCTURE": 1,



"SERVICE": 0,



"APPLICATION": 0,



"ENVIRONMENT": 0



},



"hasRootCause": true



}



],



"monitored": {



"INFRASTRUCTURE": 2474,



"SERVICE": 85,



"APPLICATION": 503,



"ENVIRONMENT": 1



}



}



}
```

#### Код ответа

200

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")