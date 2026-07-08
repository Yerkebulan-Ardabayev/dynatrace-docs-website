---
title: Maintenance windows API - POST a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/post-mw
---

# Maintenance windows API - POST a maintenance window

# Maintenance windows API - POST a maintenance window

* Reference
* Updated on Apr 28, 2020

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema instead.

Creates a new maintenance window.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [MaintenanceWindow](#openapi-definition-MaintenanceWindow) | The JSON body of the request. Contains parameters of the new maintenance window. | body | Optional |

### Request body objects

#### The `MaintenanceWindow` object

Configuration of a maintenance window.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | A short description of the maintenance purpose. | Required |
| id | string | The ID of the maintenance window. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| name | string | The name of the maintenance window, displayed in the UI. | Required |
| schedule | [Schedule](#openapi-definition-Schedule) | The schedule of the maintenance window. | Required |
| scope | [Scope](#openapi-definition-Scope) | The scope of the maintenance window.  The scope restricts the alert/problem detection suppression to certain Dynatrace entities. It can contain a list of entities and/or matching rules for dynamic formation of the scope.  If no scope is specified, the alert/problem detection suppression applies to the entire environment. | Optional |
| suppressSyntheticMonitorsExecution | boolean | Suppress execution of synthetic monitors during the maintenance. | Optional |
| suppression | string | The type of suppression of alerting and problem detection during the maintenance. The element can hold these values * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` | Required |
| type | string | The type of the maintenance: planned or unplanned. The element can hold these values * `PLANNED` * `UNPLANNED` | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `Schedule` object

The schedule of the maintenance window.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| end | string | The end date and time of the maintenance window validity period in yyyy-mm-dd HH:mm format. | Required |
| recurrence | [Recurrence](#openapi-definition-Recurrence) | The recurrence of the maintenance window. | Optional |
| recurrenceType | string | The type of the schedule recurrence. The element can hold these values * `DAILY` * `MONTHLY` * `ONCE` * `WEEKLY` | Required |
| start | string | The start date and time of the maintenance window validity period in yyyy-mm-dd HH:mm format. | Required |
| zoneId | string | The time zone of the start and end time. Default time zone is UTC.  You can use either UTC offset `UTC+01:00` format or the IANA Time Zone Database format (for example, `Europe/Vienna`). | Required |

#### The `Recurrence` object

The recurrence of the maintenance window.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dayOfMonth | integer | The day of the month for monthly maintenance.  The value of `31` is treated as the last day of the month for months that don't have a 31st day. The value of `30` is also treated as the last day of the month for February. | Optional |
| dayOfWeek | string | The day of the week for weekly maintenance.  The format is the full name of the day in upper case, for example `THURSDAY`. The element can hold these values * `FRIDAY` * `MONDAY` * `SATURDAY` * `SUNDAY` * `THURSDAY` * `TUESDAY` * `WEDNESDAY` | Optional |
| durationMinutes | integer | The duration of the maintenance window in minutes. | Required |
| startTime | string | The start time of the maintenance window in HH:mm format. | Required |

#### The `Scope` object

The scope of the maintenance window.

The scope restricts the alert/problem detection suppression to certain Dynatrace entities. It can contain a list of entities and/or matching rules for dynamic formation of the scope.

If no scope is specified, the alert/problem detection suppression applies to the entire environment.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| entities | string[] | A list of Dynatrace entities (for example, hosts or services) to be included in the scope.  Allowed values are Dynatrace entity IDs. | Required |
| matches | [MonitoredEntityFilter](#openapi-definition-MonitoredEntityFilter)[] | A list of matching rules for dynamic scope formation.  If several rules are set, the OR logic applies. | Required |

#### The `MonitoredEntityFilter` object

A matching rule for Dynatrace entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| mzId | string | The ID of a management zone to which the matched entities must belong. | Optional |
| tagCombination | string | The logic that applies when several tags are specified: AND/OR.  If not set, the OR logic is used. The element can hold these values * `AND` * `OR` | Optional |
| tags | [TagInfo](#openapi-definition-TagInfo)[] | The tag you want to use for matching.  You can use custom tags from the UI, AWS tags, Cloud Foundry tags, OpenShift/Kubernetes, and tags based on environment variables. | Required |
| type | string | The type of the Dynatrace entities (for example, hosts or services) you want to pick up by matching. The element can hold these values * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` | Optional |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Required |
| key | string | The key of the tag.  Custom tags have the tag value here. | Required |
| value | string | The value of the tag.  Not applicable to custom tags. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "An example Maintenance window",



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"name": "Example Window",



"schedule": {



"end": "2019-02-27 00:00",



"recurrence": {



"dayOfMonth": "23",



"durationMinutes": "60",



"startTime": "16:28"



},



"recurrenceType": "MONTHLY",



"start": "2018-08-02 00:00",



"zoneId": "Europe/Vienna"



},



"scope": {



"entities": [



"HOST-0000000000123456"



],



"matches": [



{



"mzId": "123456789",



"tagCombination": "AND",



"tags": [



{



"context": "AWS",



"key": "testkey",



"value": "testvalue"



}



],



"type": "HOST"



}



]



},



"suppressSyntheticMonitorsExecution": "true",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"type": "UNPLANNED"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new maintenance window has been created. The response body contains its ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

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

#### Response body JSON models

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

In this example, the request creates a new maintenance window for a **one-time planned** maintenance. The maintenance window begins at **8:00 am** and ends at **1:00 pm** on July 31st, 2019. It affects the application with the ID of **APPLICATION-61A89B82DF26BCFC** and all the hosts that have the **MainApp** custom tag. Problem detection is suppressed during this maintenance.

The API token is passed in the **Authorization** header.

The request body is lengthy, so it is truncated in the **Curl** section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own. Be sure to use the entity IDs and tags that are available in your environment. You can retrieve the list of monitored entities with the [**Topology and Smartscape API**](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") and the list of tags with the [**Automatically applied tags API**](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api "Learn what the Dynatrace automatically applied tags API offers.").

#### Curl

```
curl -X POST \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{ <truncated - see the Request body section > }'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows
```

#### Request body

```
{



"name": "Main app update",



"description": "Deployment of a new version of the main application",



"type": "PLANNED",



"suppression": "DONT_DETECT_PROBLEMS",



"scope": {



"entities": ["APPLICATION-61A89B82DF26BCFC"],



"matches": [



{



"type": "HOST",



"mzId": null,



"tags": [



{



"context": "CONTEXTLESS",



"key": "MainApp"



}



],



"tagCombination": "OR"



}



]



},



"schedule": {



"recurrenceType": "ONCE",



"start": "2019-07-31 08:00",



"end": "2019-07-31 13:00",



"zoneId": "Europe/Vienna"



}



}
```

#### Response body

```
{



"id": "ac6f245d-e945-4e0c-85b1-8c134d0b05ad",



"name": "Main app update",



"description": "Deployment of a new version of the main app"



}
```

#### Response code

201

#### Result

The new maintenance window looks like this in the UI:

![POST example](https://dt-cdn.net/images/post-example-971-3dd3f9b318.png)

POST example

## Related topics

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.")