---
title: Problems API - GET feed
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems/problems/get-feed
---

# Problems API - GET feed

# Problems API - GET feed

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

Lists the problems (and their details) observed by Dynatrace during a relative period of time.

A problem is included in the response if either the start or end timestamp of the problem is within the defined timeframe.

The output is limited to **5,000** problems. You can narrow it down by specifying filtering criteria—see the [**Parameters** section](#parameters).

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/problem/feed` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/problem/feed` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| relativeTime | string | The relative timeframe of the inquiry, back from the current time. The element can hold these values * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Optional |
| startTimestamp | integer | The start timestamp of the requested timeframe, in UTC milliseconds. | query | Optional |
| endTimestamp | integer | The end timestamp of the requested timeframe, in UTC milliseconds.  If `endTimestamp` is later than the current time, the current time is used.  The timeframe must not exceed 31 days. | query | Optional |
| status | string | Filters the result problems by the status. The element can hold these values * `CLOSED` * `OPEN` | query | Optional |
| impactLevel | string | Filters the result problems by the impact level. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` | query | Optional |
| severityLevel | string | Filters the result problems by the severity level. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` | query | Optional |
| tag | string[] | Filters the result problems by the tags of affected entities.You can specify several tags in the following format: `tag=tag1&tag=tag2`. The problem has to match *all* the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags use following format: `[context]key:value`. | query | Optional |
| expandDetails | boolean | Includes(`true`) or excludes(`false`) related events to the response.  Defaults to `false`, excluding the related events. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ProblemFeedResultWrapper](#openapi-definition-ProblemFeedResultWrapper) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ProblemFeedResultWrapper` object

| Element | Type | Description |
| --- | --- | --- |
| result | [ProblemFeedQueryResult](#openapi-definition-ProblemFeedQueryResult) | Details on open problems in your environment. |

#### The `ProblemFeedQueryResult` object

Details on open problems in your environment.

| Element | Type | Description |
| --- | --- | --- |
| monitored | object | The number of monitored entities per impact level. |
| problems | [Problem](#openapi-definition-Problem)[] | The list of problems and their details.  Contains all problems within specified timeframe, open and closed. |

#### The `Problem` object

The properties of a problem.

| Element | Type | Description |
| --- | --- | --- |
| affectedCounts | object | The number of affected entities per impact level. |
| commentCount | integer | The number of comments to the problem. |
| displayName | string | The name of the problem, displayed in the UI. |
| endTime | integer | The end timestamp of the problem, in UTC milliseconds.  Has the value `-1` if the problem is still open. |
| hasRootCause | boolean | Indicates whether Dynatrace has found at least one possible root cause for the problem. |
| id | string | The ID of the problem. |
| impactLevel | string | The impact level of the problem. It shows what is affected by the problem: infrastructure, service, or application. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| rankedEvents | [Event](#openapi-definition-Event)[] | The list of events related to the problem. |
| rankedImpacts | [EventRestImpact](#openapi-definition-EventRestImpact)[] | Provides impact information of the events in an aggregated form. For a more detailed impact analysis, see `rankedEvents`. |
| recoveredCounts | object | The number of entities that were affected, but recovered, per impact level. |
| severityLevel | string | The severity of the problem. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | The start timestamp of the problem, in UTC milliseconds. |
| status | string | The status of the problem. The element can hold these values * `CLOSED` * `OPEN` |
| tagsOfAffectedEntities | [TagInfo](#openapi-definition-TagInfo)[] | Tags of entities affected by the problem. |

#### The `Event` object

The properties of an event.

| Element | Type | Description |
| --- | --- | --- |
| activeMaintenanceWindows | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation)[] | - |
| affectedPrivateSyntheticLocations | string[] | - |
| affectedRequestsPerMinute | number | - |
| affectedSyntheticActions | string[] | If the event type is one of the synthetic event types then we may have information on which synthetic actions are affected by the event. The names of those are returned in this field. |
| affectedSyntheticLocations | string[] | - |
| affectedUserActionsPerMinute | number | - |
| annotationDescription | string | - |
| annotationType | string | - |
| artifact | string | - |
| browser | string | -The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICES` |
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
| endTime | integer | The timestamp of the event closure, in UTC milliseconds.  Has the `-1` value if the event is still open. |
| entityId | string | The ID of the affected Dynatrace entity. |
| entityName | string | The name of the affected Dynatrace entity. |
| eventType | string | The type of the event. The element can hold these values * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| geolocation | string | - |
| impactLevel | string | The impact level of the event. It shows what is affected by the problem: infrastructure, service, or application. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| isClusterWide | boolean | For events with event type `MONITORING_UNAVAILABLE`, it may be that the event is occurring on the entire Dynatrace cluster. If this is true, it could be that there are problems on the Dynatrace side. |
| isRootCause | boolean | Indicates if the event is the root cause of a problem. |
| minimumProcessGroupInstanceCountThreshold | integer | - |
| mobileAppVersion | string | - |
| operatingSystem | string | - |
| original | string | - |
| percentile | string | -The element can hold these values * `50th` * `90th` |
| referenceResponseTime50thPercentile | number | - |
| referenceResponseTime90thPercentile | number | - |
| remediationAction | string | - |
| resourceId | string | The id of the resource the event occurred on. |
| resourceName | string | The name of the resource the event occurred on. |
| service | string | - |
| serviceMethod | string | - |
| serviceMethodGroup | string | - |
| severities | [EventSeverity](#openapi-definition-EventSeverity)[] | Additional data on the event severity. |
| severityLevel | string | The severity of the event. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| source | string | - |
| startTime | integer | The timestamp of the event detection, in UTC milliseconds. |
| status | string | The status of the event. The element can hold these values * `CLOSED` * `OPEN` |
| syntheticErrorType | string[] | If the event type is one of the synthetic event types then we may have information about the error type. The names of those are returned in this field. |
| userAction | string | - |
| userDefined50thPercentileThreshold | number | - |
| userDefined90thPercentileThreshold | number | - |
| userDefinedFailureRateThreshold | number | - |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

#### The `EventSeverity` object

Additional data on the event severity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The metric used in the event severity calculation. The element can hold these values * `COMMAND_ABORT` * `CPU_READY_TIME` * `CPU_USAGE` * `CRASH_RATE` * `FAILURE_RATE` * `HYPERVISOR_PACKETS_RECEIVED_DROPPED` * `HYPERVISOR_PACKETS_TRANSMITTED_DROPPED` * `MEMORY_COMPRESSION_RATE` * `MEMORY_DECOMPRESSION_RATE` * `MEMORY_SWAP_IN_RATE` * `MEMORY_SWAP_OUT_RATE` * `MEMORY_USAGE` * `NETWORK_HIGH_RECEIVED_UTILIZATION_RATE` * `NETWORK_HIGH_TRANSMITTED_UTILIZATION_RATE` * `NETWORK_PACKETS_RECEIVED_DROPPED` * `NETWORK_PACKETS_TRANSMITTED_DROPPED` * `NETWORK_RECEIVED_ERROR_RATE` * `NETWORK_TRANSMITTED_ERROR_RATE` * `PAGE_FAULTS` * `PG_AVAILABLE` * `RESPONSE_TIME_50TH_PERCENTILE` * `RESPONSE_TIME_90TH_PERCENTILE` |
| unit | string | The unit of the severity value. The element can hold these values * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (µs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (‰)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| value | number | The value of the severity. |

#### The `EventRestImpact` object

The information about the event's impact.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The ID of the affected Dynatrace entity. |
| entityName | string | The name of the affected Dynatrace entity. |
| eventType | string | The type of the event. The element can hold these values * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| impactLevel | string | The impact level of the event. It shows what is affected by the problem: infrastructure, service, or application. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| resourceId | string | The id of the resource the event occurred on. |
| resourceName | string | The name of the resource the event occurred on. |
| severityLevel | string | The severity of the event. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

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

## Example

In this example, the request gets the problems that have occurred during the **last hour** and which are affecting **infrastructure**.

The API token is passed in the **Authorization** header.

The result is truncated to the first two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?impactLevel=INFRASTRUCTURE&relativeTime=hour' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?impactLevel=INFRASTRUCTURE&relativeTime=hour
```

#### Response body

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

#### Response code

200

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")