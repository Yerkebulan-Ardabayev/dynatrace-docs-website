---
title: Events API v1 - GET an event
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/get-event
scraped: 2026-05-12T12:13:42.353911
---

# Events API v1 - GET an event

# Events API v1 - GET an event

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") instead.

Lists parameters of the specified event.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/events/{eventId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events/{eventId}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| eventId | string | The ID of the required event. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventRestEntry](#openapi-definition-EventRestEntry) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventRestEntry` object

Set of parameters of the event.

Apart from the general properties mentioned here, which each event has, an actual event has a set of metadata that varies depending on the event type.

| Element | Type | Description |
| --- | --- | --- |
| endTime | integer | The timestamp of the event closure, in UTC milliseconds |
| entityId | string | The ID of the affected Dynatrace entity. |
| entityName | string | The name of the affected Dynatrace entity. |
| eventStatus | string | The state of the event: open or closed. The element can hold these values * `CLOSED` * `OPEN` |
| eventType | string | The type of the event. The element can hold these values * `APPLICATION_JS_FRAMEWORK_DETECTED` * `APPLICATION_OVERLOAD_PREVENTION` * `AVAILABILITY_EVENT` * `CONNECTION_LOST` * `CPU_SATURATED` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_APPLICATION_OVERLOAD_PREVENTION` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `DATABASE_CONNECTION_FAILURE` * `DEPLOYMENT_CHANGED_CHANGE` * `DEPLOYMENT_CHANGED_NEW` * `DEPLOYMENT_CHANGED_REMOVED` * `DYNATRACE_INTERNAL` * `EBS_VOLUME_HIGH_LATENCY` * `ELASTIC_LOAD_BALANCER_HIGH_BACKEND_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_FAILURE_RATE` * `ELASTIC_LOAD_BALANCER_HIGH_UNHEALTHY_HOST_RATE` * `ERROR_EVENT` * `ESXI_HOST_VM_MOTION_ARRIVED` * `ESXI_HOST_VM_MOTION_LEFT` * `ESXI_HOST_VM_STARTED` * `ESXI_START` * `ESXI_VM_DISCONNECTED` * `ESXI_VM_MOTION` * `ESXI_VM_POWER_OFF` * `ESXI_VM_START` * `FAILURE_RATE_INCREASED` * `HIGH_CONNECTIVITY_FAILURES` * `HIGH_DROPPED_PACKETS_RATE` * `HIGH_GC_ACTIVITY` * `HIGH_LATENCY` * `HIGH_NETWORK_ERROR_RATE` * `HIGH_NETWORK_LOSS_RATE` * `HIGH_NETWORK_UTILIZATION` * `HOST_CONNECTION_FAILED` * `HOST_CONNECTION_LOST` * `HOST_DATASTORE_LOW_DISK_SPACE` * `HOST_DISK_LOW_INODES` * `HOST_GRACEFULLY_SHUTDOWN` * `HOST_LOG_AVAILABILITY` * `HOST_LOG_ERROR` * `HOST_LOG_MATCHED` * `HOST_LOG_PERFORMANCE` * `HOST_MAINTENANCE` * `HOST_NO_CONNECTION` * `HOST_OF_SERVICE_UNAVAILABLE` * `HOST_SHUTDOWN` * `HOST_TIMEOUT` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `INSUFFICIENT_DISK_QUEUE_DEPTH` * `JAVASCRIPT_ERROR_RATE_INCREASED` * `LAMBDA_FUNCTION_HIGH_ERROR_RATE` * `LOG_AVAILABILITY` * `LOG_ERROR` * `LOG_MATCHED` * `LOG_PERFORMANCE` * `LOW_DISK_SPACE` * `LOW_STORAGE_SPACE` * `MARKED_FOR_TERMINATION` * `MEMORY_RESOURCES_EXHAUSTED` * `MEMORY_SATURATED` * `MOBILE_APPLICATION_OVERLOAD_PREVENTION` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OPENSTACK_HOST_VM_SHUTDOWN` * `OPENSTACK_HOST_VM_STARTED` * `OPENSTACK_KEYSTONE_SLOW` * `OPENSTACK_KEYSTONE_UNHEALTHY` * `OPENSTACK_VM_LAUNCH_FAILED` * `OPENSTACK_VM_MOTION` * `OSI_DOCKER_DEVICEMAPPER_LOW_DATA_SPACE` * `OSI_DOCKER_DEVICEMAPPER_LOW_METADATA_SPACE` * `OVERLOADED_STORAGE` * `PERFORMANCE_EVENT` * `PGI_CRASHED_INFO` * `PGI_HAPROXY_QUEUED_REQUESTS_HIGH` * `PGI_HAPROXY_SESSION_USAGE_HIGH` * `PGI_LOG_MATCHED` * `PGI_MEMDUMP` * `PGI_MYSQL_SLOW_QUERIES_RATE_HIGH` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_RMQ_HIGH_FILE_DESC_USAGE` * `PGI_RMQ_HIGH_MEM_USAGE` * `PGI_RMQ_HIGH_PROCESS_USAGE` * `PGI_RMQ_HIGH_SOCKETS_USAGE` * `PGI_RMQ_LOW_DISK_SPACE` * `PROCESS_CRASHED` * `PROCESS_CUSTOM_AVAILABILITY` * `PROCESS_CUSTOM_ERROR` * `PROCESS_CUSTOM_PERFORMANCE` * `PROCESS_GROUP_LOW_INSTANCE_COUNT` * `PROCESS_LOG_AVAILABILITY` * `PROCESS_LOG_ERROR` * `PROCESS_LOG_PERFORMANCE` * `PROCESS_RESTART` * `PROCESS_UNAVAILABLE` * `RDS_AZ_FAILOVER_COMPLETED` * `RDS_AZ_FAILOVER_STARTED` * `RDS_BACKUP_COMPLETED` * `RDS_BACKUP_STARTED` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART` * `RDS_RESTART_SEQUENCE` * `RESOURCE_CONTENTION` * `SERVICE_RESPONSE_TIME_DEGRADED` * `SLOW_DISK` * `SYNTHETIC_AVAILABILITY` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_SLOWDOWN` * `THREADS_RESOURCES_EXHAUSTED` * `UNEXPECTED_HIGH_LOAD` * `UNEXPECTED_LOW_LOAD` * `USER_ACTION_DURATION_DEGRADATION` * `VIRTUAL_MACHINE_SHUTDOWN` * `WARNING` * `WEB_CHECK_GLOBAL_OUTAGE` * `WEB_CHECK_LOCAL_OUTAGE` |
| id | string | The encoded ID of the event. The format is *eventID\_startTime*.  You should use the value from this field when you need an event ID. |
| impactLevel | string | The impact level of the event. It shows what is affected by the problem: infrastructure, service, or application. The element can hold these values * `APPLICATION` * `ENVIRONMENT` * `INFRASTRUCTURE` * `SERVICE` |
| metadata | object | Various metadata information about the event. |
| resourceId | string | The id of the resource the event occurred on. |
| resourceName | string | The name of the resource the event occurred on. |
| severityLevel | string | The severity of the event. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| startTime | integer | The timestamp of the event detection, in UTC milliseconds. |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | Tags of the Dynatrace entity that raised the event. |

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
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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

In this example, the request queries the parameters of the event with the ID **4166694657638834567\_1533134704285**.

This is the **CUSTOM\_DEPLOYMENT** event-affected service and is marked with the **deploy** custom tag.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/events/4166694657638834567_1533134704285 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/events/4166694657638834567_1533134704285
```

#### Response content

```
{



"eventId": 4166694657638834567,



"startTime": 1533134704285,



"endTime": 1533134704285,



"entityId": "SERVICE-0F579DCA105F190C",



"entityName": "wmqiTestingWeb",



"severityLevel": null,



"impactLevel": "SERVICE",



"eventType": "CUSTOM_DEPLOYMENT",



"eventStatus": "CLOSED",



"tags": [



{



"context": "CONTEXTLESS",



"key": "deploy"



}



],



"id": "4166694657638834567_1533134704285",



"customProperties": {



"Build Number": "1.223.23432",



"Owner": "Jason Miller (jason.miller@easytravel.com)",



"Approver": "Alice McBright (alice.mcbright@easytravel.com)",



"Git commit": "e5afbftc7eb"



},



"deploymentProject": "easyTravel service",



"remediationAction": "http://tower.local/job/RemediateJob/38/",



"deploymentVersion": "1.23.321",



"deploymentName": "easyTravel service deployment",



"source": "ServiceNow",



"ciBackLink": "http://tower.local/job/DeployJob/38/artifact/build/Deployment-v1.23.321.zip"



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
* [Creating a deployment event via the Dynatrace APIï»¿](https://www.youtube.com/watch?v=LDAiUMdrtvA)