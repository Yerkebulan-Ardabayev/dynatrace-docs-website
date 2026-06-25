---
title: Events API v1 - POST an event
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/post-event
scraped: 2026-05-12T12:13:40.104293
---

# Events API v1 - POST an event

# Events API v1 - POST an event

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") instead.

Pushes custom events from third-party integrations to one or more monitored entities.

This endpoint enables third-party systems such as CI platforms (Jenkins, Bamboo, Electric Cloud, etc.) to provide additional details for Dynatrace automated root cause analysis.

You can use this endpoint to:

* Push information-only events from third-party systems to provide additional information for Dynatrace automated root cause analysis. The time of event closure is already known and the event IDs are returned instantly. You can push these events for up to **30 days** into the past. The information-only event types are:

  + `CUSTOM_ANNOTATION`
  + `CUSTOM_CONFIGURATION`
  + `CUSTOM_DEPLOYMENT`
  + `CUSTOM_INFO`
  + `MARKED_FOR_TERMINATION`
* Push problem-opening events (for example, an error rate increase) to trigger the Dynatrace automated root cause analysis engine. Correlation IDs are returned instead of event IDs. These events stay open until the specified timeout expires. To prevent expiration, you can refresh these events by sending the same payload again. You can push these events for up to **60 minutes** into the past. The problem-opening event types (sorted by highest to lowest severity) are:

  + `AVAILABILITY_EVENT`
  + `ERROR_EVENT`
  + `PERFORMANCE_EVENT`
  + `RESOURCE_CONTENTION`

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/events` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The set of parameters depends on the event type. See [**Parameters mapping**](#parameters-mapping) below for details.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [EventCreation](#openapi-definition-EventCreation) | The JSON body of the request, containing parameters of the event. | body | Optional |

### Request body objects

#### The `EventCreation` object

Configuration of the custom event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| allowDavisMerge | boolean | Allow Davis AI to merge this event into existing problems (true) or force creating a new problem (false).  This only applies to problem-opening event types. | Optional |
| annotationDescription | string | A detailed description of the custom annotation, for example `DNS route has been changed to x.mydomain.com`. | Optional |
| annotationType | string | The type of the custom annotation, for example `DNS route has been changed`. | Optional |
| attachRules | [PushEventAttachRules](#openapi-definition-PushEventAttachRules) | The set of rules defining Dynatrace entities to be associated with the event.  You can specify tags to dynamically match Dynatrace entities or IDs of specific entities.  At least one entity ID or tag is required. | Required |
| changed | string | The new value of the configuration that has been set by the event. | Optional |
| ciBackLink | string | The link to the deployed artifact within the 3rd party system. | Optional |
| configuration | string | The ID or the name of the configuration that has been changed by the event. | Optional |
| customProperties | object | The set of any properties related to the event, in the *"key" : "value"* format. | Optional |
| deploymentName | string | The ID of the triggered deployment. | Optional |
| deploymentProject | string | The project name of the deployed package. | Optional |
| deploymentVersion | string | The version of the triggered deployment. | Optional |
| description | string | The textual description of the configuration change. | Optional |
| end | integer | The end timestamp of the event, in UTC milliseconds.  If not set, the current time is used for information-only events.  Not applicable to problem-opening events. Such an event stays open until it times out depending on the **timeoutMinutes** parameter. | Optional |
| eventType | string | The type of the event. The element can hold these values * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION` | Required |
| original | string | The previous value of the configuration. | Optional |
| remediationAction | string | The link to the deployment related remediation action within the external tool. | Optional |
| source | string | The name or ID of the external source of the event. | Required |
| start | integer | The start timestamp of the event, in UTC milliseconds.  If not set, the current timestamp is used.  You can report information-only events up to **30 days** into the past.  You can report problem-opening events up to **60 minutes** into the past. | Optional |
| timeoutMinutes | integer | The timeout for problem-opening events in minutes. Not applicable to information-only events.  If not set, 15 minutes is used. The maximum allowed value is 120 minutes.  You can refresh the event by sending the same payload again. | Optional |
| timeseriesIds | string[] | A list of timeseries IDs, related to the event. | Optional |
| title | string | The title of the configuration that has been set by the event. | Optional |

#### The `PushEventAttachRules` object

The set of rules defining Dynatrace entities to be associated with the event.

You can specify tags to dynamically match Dynatrace entities or IDs of specific entities.

At least one entity ID or tag is required.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| entityIds | string[] | A list of entity IDs to which the event should be attached. | Optional |
| tagRule | [TagMatchRule[]](#openapi-definition-TagMatchRule) | A set of matching rules to dynamically pick up entities based on tags.  Only entities seen within the last **24 hours** are taken into account for tag-based matching rules. | Optional |

#### The `TagMatchRule` object

The list of tags to be used for matching Dynatrace entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| meTypes | string[] | The list of types of the Dynatrace entities (for example hosts or services) you want to pick up by matching. The element can hold these values * `APM_SECURITY_GATEWAY` * `APPLICATION` * `APPLICATION_METHOD` * `APPLICATION_METHOD_GROUP` * `APPMON_SERVER` * `APPMON_SYSTEM_PROFILE` * `AUTO_SCALING_GROUP` * `AUXILIARY_SYNTHETIC_TEST` * `AWS_APPLICATION_LOAD_BALANCER` * `AWS_AVAILABILITY_ZONE` * `AWS_CREDENTIALS` * `AWS_LAMBDA_FUNCTION` * `AWS_NETWORK_LOAD_BALANCER` * `AZURE_API_MANAGEMENT_SERVICE` * `AZURE_APPLICATION_GATEWAY` * `AZURE_APP_SERVICE_PLAN` * `AZURE_COSMOS_DB` * `AZURE_CREDENTIALS` * `AZURE_EVENT_HUB` * `AZURE_EVENT_HUB_NAMESPACE` * `AZURE_FUNCTION_APP` * `AZURE_IOT_HUB` * `AZURE_LOAD_BALANCER` * `AZURE_MGMT_GROUP` * `AZURE_REDIS_CACHE` * `AZURE_REGION` * `AZURE_SERVICE_BUS_NAMESPACE` * `AZURE_SERVICE_BUS_QUEUE` * `AZURE_SERVICE_BUS_TOPIC` * `AZURE_SQL_DATABASE` * `AZURE_SQL_ELASTIC_POOL` * `AZURE_SQL_SERVER` * `AZURE_STORAGE_ACCOUNT` * `AZURE_SUBSCRIPTION` * `AZURE_TENANT` * `AZURE_VM` * `AZURE_VM_SCALE_SET` * `AZURE_WEB_APP` * `BROWSER` * `CF_APPLICATION` * `CF_FOUNDATION` * `CINDER_VOLUME` * `CLOUD_APPLICATION` * `CLOUD_APPLICATION_INSTANCE` * `CLOUD_APPLICATION_NAMESPACE` * `CLOUD_NETWORK_INGRESS` * `CLOUD_NETWORK_POLICY` * `CONTAINER_GROUP` * `CONTAINER_GROUP_INSTANCE` * `CUSTOM_APPLICATION` * `CUSTOM_DEVICE` * `CUSTOM_DEVICE_GROUP` * `DCRUM_APPLICATION` * `DCRUM_SERVICE` * `DCRUM_SERVICE_INSTANCE` * `DEVICE_APPLICATION_METHOD` * `DEVICE_APPLICATION_METHOD_GROUP` * `DISK` * `DOCKER_CONTAINER_GROUP` * `DOCKER_CONTAINER_GROUP_INSTANCE` * `DYNAMO_DB_TABLE` * `EBS_VOLUME` * `EC2_INSTANCE` * `ELASTIC_LOAD_BALANCER` * `ENVIRONMENT` * `EXTERNAL_SYNTHETIC_TEST_STEP` * `GCP_ZONE` * `GEOLOCATION` * `GEOLOC_SITE` * `GOOGLE_COMPUTE_ENGINE` * `HOST` * `HOST_GROUP` * `HTTP_CHECK` * `HTTP_CHECK_STEP` * `HYPERVISOR` * `HYPERVISOR_CLUSTER` * `HYPERVISOR_DISK` * `KUBERNETES_CLUSTER` * `KUBERNETES_NODE` * `KUBERNETES_SERVICE` * `MOBILE_APPLICATION` * `MULTIPROTOCOL_MONITOR` * `NETWORK_INTERFACE` * `NEUTRON_SUBNET` * `OPENSTACK_PROJECT` * `OPENSTACK_REGION` * `OPENSTACK_VM` * `OS` * `PROCESS_GROUP` * `PROCESS_GROUP_INSTANCE` * `QUEUE` * `QUEUE_INSTANCE` * `RELATIONAL_DATABASE_SERVICE` * `S3BUCKET` * `SERVICE` * `SERVICE_INSTANCE` * `SERVICE_METHOD` * `SERVICE_METHOD_GROUP` * `SWIFT_CONTAINER` * `SYNTHETIC_LOCATION` * `SYNTHETIC_TEST` * `SYNTHETIC_TEST_STEP` * `VCENTER` * `VIRTUALMACHINE` * `VMWARE_DATACENTER` | Required |
| tags | [TagInfo[]](#openapi-definition-TagInfo) | The list of tags you want to use for matching. At least one tag is required.  You can use custom tags from the UI, imported tags, and tags based on environment variables. | Required |

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



"annotationDescription": "The coffee machine is broken",



"annotationType": "defect",



"attachRules": {



"entityIds": [



"CUSTOM_DEVICE-0000000000000007"



],



"tagRule": [



{



"meTypes": [



"HOST"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "customTag"



}



]



}



]



},



"end": 1521542929000,



"eventType": "CUSTOM_ANNOTATION",



"source": "OpsControl",



"start": 1521042929000



}
```

### Parameters mapping

|  | Availability event | Custom annotation | Custom config | Custom deployment | Custom info | Error event | Performance event | Resource contention | Marked for termination |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| description | req | opt | req | n/a | req | req | req | req | req |
| title | req | n/a | n/a | n/a | opt | req | req | req | opt |
| source | req | req | req | req | req | req | req | req | req |
| annotationType | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| annotationDescription | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| deploymentName | n/a | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a |
| deploymentVersion | n/a | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a |
| deploymentProject | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a |
| ciBackLink | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | opt |
| remediationAction | n/a | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a |
| original | n/a | n/a | opt | n/a | n/a | n/a | n/a | n/a | n/a |
| configuration | n/a | n/a | req | n/a | n/a | n/a | n/a | n/a | n/a |
| customProperties | opt | opt | opt | opt | opt | opt | opt | opt | opt |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EventStoreResult](#openapi-definition-EventStoreResult) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EventStoreResult` object

Contains IDs of all custom events, created by an event push call.

| Element | Type | Description |
| --- | --- | --- |
| storedCorrelationIds | string[] | List of correlation IDs for problem-opening-events. |
| storedEventIds | integer[] | List of event IDs for information-only-events.  This field is provided for compatibility reasons. You should use the values from the **storedIds** field instead. |
| storedIds | string[] | List of **encoded** event IDs for information-only-events. |

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



"storedCorrelationIds": [



"string"



],



"storedEventIds": [



1



],



"storedIds": [



"string"



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

In this example, the request pushes the **CUSTOM\_ANNOTATION** event, which applies to all custom devices with the **Coffee-2nd-floor** tag. This annotation is a notification that these coffee machines are broken.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/events \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"eventType": "CUSTOM_ANNOTATION",



"timeoutMinutes": 0,



"attachRules": {



"tagRule": [



{



"meTypes": [



"CUSTOM_DEVICE"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "IG-test"



}



]



}



]



},



"source": "OpsControl",



"annotationType": "defect",



"annotationDescription": "coffee machine is defective"



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/events
```

#### Request body

```
{



"eventType": "CUSTOM_ANNOTATION",



"timeoutMinutes": 0,



"attachRules": {



"tagRule": [



{



"meTypes": ["CUSTOM_DEVICE"],



"tags": [



{



"context": "CONTEXTLESS",



"key": "IG-test"



}



]



}



]



},



"source": "OpsControl",



"annotationType": "defect",



"annotationDescription": "coffee machine is defective"



}
```

#### Response body

```
{



"storedEventIds": [



-6153476110846051426



],



"storedIds": [



"-6153476110846051426_1533300519291"



],



"storedCorrelationIds": []



}
```

#### Response code

200

## Related topics

* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")
* [Event analysis and correlation](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Gain an understanding of the Events section on each host, process, and service overview page.")
* [Creating a deployment event via the Dynatrace APIï»¿](https://www.youtube.com/watch?v=LDAiUMdrtvA)