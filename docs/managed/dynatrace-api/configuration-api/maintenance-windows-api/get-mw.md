---
title: Maintenance windows API - GET a maintenance window
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-mw
scraped: 2026-05-12T12:06:27.832585
---

# Maintenance windows API - GET a maintenance window

# Maintenance windows API - GET a maintenance window

* Reference
* Updated on Apr 28, 2020

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema instead.

Gets the parameters of the specified maintenance window.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required maintenance window. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MaintenanceWindow](#openapi-definition-MaintenanceWindow) | Success |

### Response body objects

#### The `MaintenanceWindow` object

Configuration of a maintenance window.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the maintenance purpose. |
| id | string | The ID of the maintenance window. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| name | string | The name of the maintenance window, displayed in the UI. |
| schedule | [Schedule](#openapi-definition-Schedule) | The schedule of the maintenance window. |
| scope | [Scope](#openapi-definition-Scope) | The scope of the maintenance window.  The scope restricts the alert/problem detection suppression to certain Dynatrace entities. It can contain a list of entities and/or matching rules for dynamic formation of the scope.  If no scope is specified, the alert/problem detection suppression applies to the entire environment. |
| suppressSyntheticMonitorsExecution | boolean | Suppress execution of synthetic monitors during the maintenance. |
| suppression | string | The type of suppression of alerting and problem detection during the maintenance. The element can hold these values * `DETECT_PROBLEMS_AND_ALERT` * `DETECT_PROBLEMS_DONT_ALERT` * `DONT_DETECT_PROBLEMS` |
| type | string | The type of the maintenance: planned or unplanned. The element can hold these values * `PLANNED` * `UNPLANNED` |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `Schedule` object

The schedule of the maintenance window.

| Element | Type | Description |
| --- | --- | --- |
| end | string | The end date and time of the maintenance window validity period in yyyy-mm-dd HH:mm format. |
| recurrence | [Recurrence](#openapi-definition-Recurrence) | The recurrence of the maintenance window. |
| recurrenceType | string | The type of the schedule recurrence. The element can hold these values * `DAILY` * `MONTHLY` * `ONCE` * `WEEKLY` |
| start | string | The start date and time of the maintenance window validity period in yyyy-mm-dd HH:mm format. |
| zoneId | string | The time zone of the start and end time. Default time zone is UTC.  You can use either UTC offset `UTC+01:00` format or the IANA Time Zone Database format (for example, `Europe/Vienna`). |

#### The `Recurrence` object

The recurrence of the maintenance window.

| Element | Type | Description |
| --- | --- | --- |
| dayOfMonth | integer | The day of the month for monthly maintenance.  The value of `31` is treated as the last day of the month for months that don't have a 31st day. The value of `30` is also treated as the last day of the month for February. |
| dayOfWeek | string | The day of the week for weekly maintenance.  The format is the full name of the day in upper case, for example `THURSDAY`. The element can hold these values * `FRIDAY` * `MONDAY` * `SATURDAY` * `SUNDAY` * `THURSDAY` * `TUESDAY` * `WEDNESDAY` |
| durationMinutes | integer | The duration of the maintenance window in minutes. |
| startTime | string | The start time of the maintenance window in HH:mm format. |

#### The `Scope` object

The scope of the maintenance window.

The scope restricts the alert/problem detection suppression to certain Dynatrace entities. It can contain a list of entities and/or matching rules for dynamic formation of the scope.

If no scope is specified, the alert/problem detection suppression applies to the entire environment.

| Element | Type | Description |
| --- | --- | --- |
| entities | string[] | A list of Dynatrace entities (for example, hosts or services) to be included in the scope.  Allowed values are Dynatrace entity IDs. |
| matches | [MonitoredEntityFilter[]](#openapi-definition-MonitoredEntityFilter) | A list of matching rules for dynamic scope formation.  If several rules are set, the OR logic applies. |

#### The `MonitoredEntityFilter` object

A matching rule for Dynatrace entities.

| Element | Type | Description |
| --- | --- | --- |
| mzId | string | The ID of a management zone to which the matched entities must belong. |
| tagCombination | string | The logic that applies when several tags are specified: AND/OR.  If not set, the OR logic is used. The element can hold these values * `AND` * `OR` |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The tag you want to use for matching.  You can use custom tags from the UI, AWS tags, Cloud Foundry tags, OpenShift/Kubernetes, and tags based on environment variables. |
| type | string | The type of the Dynatrace entities (for example, hosts or services) you want to pick up by matching. The element can hold these values * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` |

#### The `TagInfo` object

Tag of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

### Response body JSON models

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

## Example

In this example, the request inquires about the properties of the **infrastructure maintenance** maintenance window, which has the ID **0b989446-e56f-4837-a521-96f4d39a9b76**.

The configuration has the following settings:

![GET example](https://dt-cdn.net/images/get-example-980-48060ed670.png)

GET example

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/0b989446-e56f-4837-a521-96f4d39a9b76" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows/0b989446-e56f-4837-a521-96f4d39a9b76
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.175.0.20190731-075319"



},



"id": "0b989446-e56f-4837-a521-96f4d39a9b76",



"name": "infrastructure maintenance",



"description": "Monthly check-up of infrastructure",



"type": "PLANNED",



"suppression": "DETECT_PROBLEMS_DONT_ALERT",



"scope": {



"entities": [],



"matches": [



{



"type": "HOST",



"managementZoneId": null,



"tags": [



{



"context": "CONTEXTLESS",



"key": "InfWindows"



},



{



"context": "CONTEXTLESS",



"key": "InfLinux"



}



],



"tagCombination": "OR"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfWeek": null,



"dayOfMonth": 31,



"startTime": "19:00",



"durationMinutes": 60



},



"start": "2019-07-01 00:00",



"end": "2020-07-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

#### Response code

200

## Related topics

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.")