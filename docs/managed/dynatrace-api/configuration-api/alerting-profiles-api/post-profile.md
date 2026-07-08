---
title: Alerting profiles API - POST a profile
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/post-profile
---

# Alerting profiles API - POST a profile

# Alerting profiles API - POST a profile

* Reference
* Published Aug 16, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Problem alerting profiles** (`builtin:alerting.profile`) schema.

Creates a new alerting profile.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [AlertingProfile](#openapi-definition-AlertingProfile) | The JSON body of the request. Contains parameters of the new alerting profile. | body | Optional |

### Request body objects

#### The `AlertingProfile` object

Configuration of an alerting profile.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| displayName | string | The name of the alerting profile, displayed in the UI. | Required |
| eventTypeFilters | [AlertingEventTypeFilter](#openapi-definition-AlertingEventTypeFilter)[] | The list of event filters.  For all filters that are *negated* inside of these event filters, that is all "Predefined" as well as "Custom" (Title and/or Description) ones the AND logic applies. For all *non-negated* ones the OR logic applies. Between these two groups, negated and non-negated, the AND logic applies.  If you specify both severity rule and event filter, the AND logic applies. | Optional |
| id | string | The ID of the alerting profile. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| mzId | string | The ID of the management zone to which the alerting profile applies. | Optional |
| rules | [AlertingProfileSeverityRule](#openapi-definition-AlertingProfileSeverityRule)[] | A list of severity rules.  The rules are evaluated from top to bottom. The first matching rule applies and further evaluation stops.  If you specify both severity rule and event filter, the AND logic applies. | Optional |

#### The `AlertingEventTypeFilter` object

Configuration of the event filter for the alerting profile.

You have two mutually exclusive options:

* Select an event type from the list of the predefined events. Specify it in the **predefinedEventFilter** field.
* Set a rule for custom events. Specify it in the **customEventFilter** field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customEventFilter | [AlertingCustomEventFilter](#openapi-definition-AlertingCustomEventFilter) | Configuration of a custom event filter.  Filters custom events by title or description. If both specified, the AND logic applies. | Optional |
| predefinedEventFilter | [AlertingPredefinedEventFilter](#openapi-definition-AlertingPredefinedEventFilter) | Configuration of a predefined event filter. | Optional |

#### The `AlertingCustomEventFilter` object

Configuration of a custom event filter.

Filters custom events by title or description. If both specified, the AND logic applies.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customDescriptionFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Configuration of a matching filter. | Optional |
| customTitleFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Configuration of a matching filter. | Optional |

#### The `AlertingCustomTextFilter` object

Configuration of a matching filter.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| caseInsensitive | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. | Required |
| enabled | boolean | The filter is enabled (`true`) or disabled (`false`). | Required |
| negate | boolean | Reverses the comparison **operator**. For example it turns the **begins with** into **does not begin with**. | Required |
| operator | string | Operator of the comparison.  You can reverse it by setting **negate** to `true`. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `CONTAINS_REGEX` * `ENDS_WITH` * `EQUALS` | Required |
| value | string | The value to compare to. | Required |

#### The `AlertingPredefinedEventFilter` object

Configuration of a predefined event filter.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| eventType | string | The type of the predefined event. The element can hold these values * `APPLICATION_ERROR_RATE_INCREASED` * `APPLICATION_SLOWDOWN` * `APPLICATION_UNEXPECTED_HIGH_LOAD` * `APPLICATION_UNEXPECTED_LOW_LOAD` * `AWS_LAMBDA_HIGH_ERROR_RATE` * `CUSTOM_APPLICATION_ERROR_RATE_INCREASED` * `CUSTOM_APPLICATION_SLOWDOWN` * `CUSTOM_APPLICATION_UNEXPECTED_HIGH_LOAD` * `CUSTOM_APPLICATION_UNEXPECTED_LOW_LOAD` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `DATABASE_CONNECTION_FAILURE` * `EBS_VOLUME_HIGH_LATENCY` * `EC2_HIGH_CPU` * `ELB_HIGH_BACKEND_ERROR_RATE` * `ESXI_GUEST_ACTIVE_SWAP_WAIT` * `ESXI_GUEST_CPU_LIMIT_REACHED` * `ESXI_HOST_CPU_SATURATION` * `ESXI_HOST_DATASTORE_LOW_DISK_SPACE` * `ESXI_HOST_DISK_QUEUE_SLOW` * `ESXI_HOST_DISK_SLOW` * `ESXI_HOST_MEMORY_SATURATION` * `ESXI_HOST_NETWORK_PROBLEMS` * `ESXI_HOST_OVERLOADED_STORAGE` * `ESXI_VM_IMPACT_HOST_CPU_SATURATION` * `ESXI_VM_IMPACT_HOST_MEMORY_SATURATION` * `EXTERNAL_SYNTHETIC_TEST_OUTAGE` * `EXTERNAL_SYNTHETIC_TEST_SLOWDOWN` * `HOST_OF_SERVICE_UNAVAILABLE` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `MOBILE_APPLICATION_ERROR_RATE_INCREASED` * `MOBILE_APPLICATION_SLOWDOWN` * `MOBILE_APPLICATION_UNEXPECTED_HIGH_LOAD` * `MOBILE_APPLICATION_UNEXPECTED_LOW_LOAD` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OSI_DISK_LOW_INODES` * `OSI_GRACEFULLY_SHUTDOWN` * `OSI_HIGH_CPU` * `OSI_HIGH_MEMORY` * `OSI_LOW_DISK_SPACE` * `OSI_NIC_DROPPED_PACKETS_HIGH` * `OSI_NIC_ERRORS_HIGH` * `OSI_NIC_UTILIZATION_HIGH` * `OSI_SLOW_DISK` * `OSI_UNEXPECTEDLY_UNAVAILABLE` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_UNAVAILABLE` * `PG_LOW_INSTANCE_COUNT` * `PROCESS_CRASHED` * `PROCESS_HIGH_GC_ACTIVITY` * `PROCESS_MEMORY_RESOURCE_EXHAUSTED` * `PROCESS_NA_HIGH_CONN_FAIL_RATE` * `PROCESS_NA_HIGH_LOSS_RATE` * `PROCESS_THREADS_RESOURCE_EXHAUSTED` * `RDS_HIGH_CPU` * `RDS_HIGH_LATENCY` * `RDS_LOW_MEMORY` * `RDS_LOW_STORAGE_SPACE` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART_SEQUENCE` * `SERVICE_ERROR_RATE_INCREASED` * `SERVICE_SLOWDOWN` * `SERVICE_UNEXPECTED_HIGH_LOAD` * `SERVICE_UNEXPECTED_LOW_LOAD` * `SYNTHETIC_GLOBAL_OUTAGE` * `SYNTHETIC_LOCAL_OUTAGE` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_TEST_LOCATION_SLOWDOWN` | Required |
| negate | boolean | The alert triggers when the problem of specified severity arises while the specified event **is** happening (`false`) or while the specified event is **not** happening (`true`).  For example, if you chose the Slowdown (`PERFORMANCE`) severity and Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`) event with **negate** set to `true`, the alerting profile will trigger only when the slowdown problem is raised while there is no unexpected high traffic event.  Consider the following use case as an example. The Slowdown (`PERFORMANCE`) severity rule is set. Depending on the configuration of the event filter (Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`) event is used as an example), the behavior of the alerting profile is one of the following:\* **negate** is set to `false`: The alert triggers when the slowdown problem is raised while unexpected high traffic event is happening.  * **negate** is set to `true`: The alert triggers when the slowdown problem is raised while there is no unexpected high traffic event. * no event rule is set: The alert triggers when the slowdown problem is raised, regardless of any events. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `AlertingProfileSeverityRule` object

A severity rule of the alerting profile.

A severity rule defines the level of severity that must be met before an alert is sent our for a detected problem. Additionally it restricts the alerting to certain monitored entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| delayInMinutes | integer | Send a notification if a problem remains open longer than *X* minutes. | Required |
| severityLevel | string | The severity level to trigger the alert. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Required |
| tagFilter | [AlertingProfileTagFilter](#openapi-definition-AlertingProfileTagFilter) | Configuration of the tag filtering of the alerting profile. | Required |

#### The `AlertingProfileTagFilter` object

Configuration of the tag filtering of the alerting profile.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| includeMode | string | The filtering mode:  * `INCLUDE_ANY`: The rule applies to monitored entities that have at least one of the specified tags. You can specify up to 100 tags. * `INCLUDE_ALL`: The rule applies to monitored entities that have **all** of the specified tags. You can specify up to 10 tags. * `NONE`: The rule applies to all monitored entities. The element can hold these values * `INCLUDE_ALL` * `INCLUDE_ANY` * `NONE` | Required |
| tagFilters | [TagFilter](#openapi-definition-TagFilter)[] | A list of required tags. | Optional |

#### The `TagFilter` object

A tag-based filter of monitored entities.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` | Required |
| key | string | The key of the tag.  Custom tags have the tag value here. | Required |
| value | string | The value of the tag.  Not applicable to custom tags. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"displayName": "sampleAlertingProfile",



"eventTypeFilters": [



{



"predefinedEventFilter": {



"eventType": "OSI_HIGH_CPU",



"negate": true



}



},



{



"customEventFilter": {



"customDescriptionFilter": {



"caseInsensitive": false,



"enabled": false,



"negate": true,



"operator": "CONTAINS",



"value": "filterValue"



},



"customTitleFilter": {



"caseInsensitive": true,



"enabled": true,



"negate": false,



"operator": "EQUALS",



"value": "filterValue"



}



}



}



],



"id": "12345678-abcd-1234-abcd-1234567890ab",



"mzId": "1",



"rules": [



{



"delayInMinutes": 60,



"severityLevel": "AVAILABILITY",



"tagFilter": {



"includeMode": "INCLUDE_ALL",



"tagFilters": [



{



"context": "AWS",



"key": "tagKey",



"value": "tagValue"



}



]



}



}



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new alerting profile has been created. The response contains the ID of the new alerting profile. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted alerting profile is valid. Response doesn't have a body |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

In this example, the request creates a new alerting profile with the following parameters:

* Severity level: Availability, triggers after **2** minutes
* Applies to monitored entities with **MainApp** tag.
* Triggers when the **Browser monitor global outage** event is occurring.

The API token is passed in the **Authorization** header.

Because the request body is lengthy, it is truncated in this example Curl section. See the full body in the **Request body** section. You can download or copy the example request body to try it out on your own. Before using it, make sure that you're using tags that are available in your environment.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section >}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles
```

#### Request body

```
{



"displayName": "App availability",



"rules": [



{



"severityLevel": "AVAILABILITY",



"tagFilter": {



"includeMode": "INCLUDE_ANY",



"tagFilters": [



{



"context": "CONTEXTLESS",



"key": "MainApp"



}



]



},



"delayInMinutes": 2



}



],



"mzId": "9130632296508575249",



"eventTypeFilters": [



{



"predefinedEventFilter": {



"eventType": "SYNTHETIC_GLOBAL_OUTAGE",



"negate": false



}



}



]



}
```

#### Response body

```
{



"id": "19e50c27-8aed-408f-ad44-d6a1bf856f49",



"name": "App availability"



}
```

#### Response code

201

#### Result

The new alerting profile looks like this in the UI:

![POST example](https://dt-cdn.net/images/post-1340-13d1708e57.png)

POST example

## Related topics

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")