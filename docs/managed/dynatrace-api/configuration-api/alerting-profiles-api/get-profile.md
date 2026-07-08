---
title: Alerting profiles API - GET a profile
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/alerting-profiles-api/get-profile
---

# Alerting profiles API - GET a profile

# Alerting profiles API - GET a profile

* Reference
* Published Aug 16, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Problem alerting profiles** (`builtin:alerting.profile`) schema.

Gets the parameters of the specified alerting profile.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/alertingProfiles/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required alerting profile. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AlertingProfile](#openapi-definition-AlertingProfile) | Success |

### Response body objects

#### The `AlertingProfile` object

Configuration of an alerting profile.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The name of the alerting profile, displayed in the UI. |
| eventTypeFilters | [AlertingEventTypeFilter](#openapi-definition-AlertingEventTypeFilter)[] | The list of event filters.  For all filters that are *negated* inside of these event filters, that is all "Predefined" as well as "Custom" (Title and/or Description) ones the AND logic applies. For all *non-negated* ones the OR logic applies. Between these two groups, negated and non-negated, the AND logic applies.  If you specify both severity rule and event filter, the AND logic applies. |
| id | string | The ID of the alerting profile. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| mzId | string | The ID of the management zone to which the alerting profile applies. |
| rules | [AlertingProfileSeverityRule](#openapi-definition-AlertingProfileSeverityRule)[] | A list of severity rules.  The rules are evaluated from top to bottom. The first matching rule applies and further evaluation stops.  If you specify both severity rule and event filter, the AND logic applies. |

#### The `AlertingEventTypeFilter` object

Configuration of the event filter for the alerting profile.

You have two mutually exclusive options:

* Select an event type from the list of the predefined events. Specify it in the **predefinedEventFilter** field.
* Set a rule for custom events. Specify it in the **customEventFilter** field.

| Element | Type | Description |
| --- | --- | --- |
| customEventFilter | [AlertingCustomEventFilter](#openapi-definition-AlertingCustomEventFilter) | Configuration of a custom event filter.  Filters custom events by title or description. If both specified, the AND logic applies. |
| predefinedEventFilter | [AlertingPredefinedEventFilter](#openapi-definition-AlertingPredefinedEventFilter) | Configuration of a predefined event filter. |

#### The `AlertingCustomEventFilter` object

Configuration of a custom event filter.

Filters custom events by title or description. If both specified, the AND logic applies.

| Element | Type | Description |
| --- | --- | --- |
| customDescriptionFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Configuration of a matching filter. |
| customTitleFilter | [AlertingCustomTextFilter](#openapi-definition-AlertingCustomTextFilter) | Configuration of a matching filter. |

#### The `AlertingCustomTextFilter` object

Configuration of a matching filter.

| Element | Type | Description |
| --- | --- | --- |
| caseInsensitive | boolean | The condition is case sensitive (`false`) or case insensitive (`true`).  If not set, then `false` is used, making the condition case sensitive. |
| enabled | boolean | The filter is enabled (`true`) or disabled (`false`). |
| negate | boolean | Reverses the comparison **operator**. For example it turns the **begins with** into **does not begin with**. |
| operator | string | Operator of the comparison.  You can reverse it by setting **negate** to `true`. The element can hold these values * `BEGINS_WITH` * `CONTAINS` * `CONTAINS_REGEX` * `ENDS_WITH` * `EQUALS` |
| value | string | The value to compare to. |

#### The `AlertingPredefinedEventFilter` object

Configuration of a predefined event filter.

| Element | Type | Description |
| --- | --- | --- |
| eventType | string | The type of the predefined event. The element can hold these values * `APPLICATION_ERROR_RATE_INCREASED` * `APPLICATION_SLOWDOWN` * `APPLICATION_UNEXPECTED_HIGH_LOAD` * `APPLICATION_UNEXPECTED_LOW_LOAD` * `AWS_LAMBDA_HIGH_ERROR_RATE` * `CUSTOM_APPLICATION_ERROR_RATE_INCREASED` * `CUSTOM_APPLICATION_SLOWDOWN` * `CUSTOM_APPLICATION_UNEXPECTED_HIGH_LOAD` * `CUSTOM_APPLICATION_UNEXPECTED_LOW_LOAD` * `CUSTOM_APP_CRASH_RATE_INCREASED` * `DATABASE_CONNECTION_FAILURE` * `EBS_VOLUME_HIGH_LATENCY` * `EC2_HIGH_CPU` * `ELB_HIGH_BACKEND_ERROR_RATE` * `ESXI_GUEST_ACTIVE_SWAP_WAIT` * `ESXI_GUEST_CPU_LIMIT_REACHED` * `ESXI_HOST_CPU_SATURATION` * `ESXI_HOST_DATASTORE_LOW_DISK_SPACE` * `ESXI_HOST_DISK_QUEUE_SLOW` * `ESXI_HOST_DISK_SLOW` * `ESXI_HOST_MEMORY_SATURATION` * `ESXI_HOST_NETWORK_PROBLEMS` * `ESXI_HOST_OVERLOADED_STORAGE` * `ESXI_VM_IMPACT_HOST_CPU_SATURATION` * `ESXI_VM_IMPACT_HOST_MEMORY_SATURATION` * `EXTERNAL_SYNTHETIC_TEST_OUTAGE` * `EXTERNAL_SYNTHETIC_TEST_SLOWDOWN` * `HOST_OF_SERVICE_UNAVAILABLE` * `HTTP_CHECK_GLOBAL_OUTAGE` * `HTTP_CHECK_LOCAL_OUTAGE` * `HTTP_CHECK_TEST_LOCATION_SLOWDOWN` * `MOBILE_APPLICATION_ERROR_RATE_INCREASED` * `MOBILE_APPLICATION_SLOWDOWN` * `MOBILE_APPLICATION_UNEXPECTED_HIGH_LOAD` * `MOBILE_APPLICATION_UNEXPECTED_LOW_LOAD` * `MOBILE_APP_CRASH_RATE_INCREASED` * `MONITORING_UNAVAILABLE` * `MULTI_PROTOCOL_GLOBAL_OUTAGE` * `MULTI_PROTOCOL_LOCAL_OUTAGE` * `MULTI_PROTOCOL_LOCATION_SLOWDOWN` * `OSI_DISK_LOW_INODES` * `OSI_GRACEFULLY_SHUTDOWN` * `OSI_HIGH_CPU` * `OSI_HIGH_MEMORY` * `OSI_LOW_DISK_SPACE` * `OSI_NIC_DROPPED_PACKETS_HIGH` * `OSI_NIC_ERRORS_HIGH` * `OSI_NIC_UTILIZATION_HIGH` * `OSI_SLOW_DISK` * `OSI_UNEXPECTEDLY_UNAVAILABLE` * `PGI_OF_SERVICE_UNAVAILABLE` * `PGI_UNAVAILABLE` * `PG_LOW_INSTANCE_COUNT` * `PROCESS_CRASHED` * `PROCESS_HIGH_GC_ACTIVITY` * `PROCESS_MEMORY_RESOURCE_EXHAUSTED` * `PROCESS_NA_HIGH_CONN_FAIL_RATE` * `PROCESS_NA_HIGH_LOSS_RATE` * `PROCESS_THREADS_RESOURCE_EXHAUSTED` * `RDS_HIGH_CPU` * `RDS_HIGH_LATENCY` * `RDS_LOW_MEMORY` * `RDS_LOW_STORAGE_SPACE` * `RDS_OF_SERVICE_UNAVAILABLE` * `RDS_RESTART_SEQUENCE` * `SERVICE_ERROR_RATE_INCREASED` * `SERVICE_SLOWDOWN` * `SERVICE_UNEXPECTED_HIGH_LOAD` * `SERVICE_UNEXPECTED_LOW_LOAD` * `SYNTHETIC_GLOBAL_OUTAGE` * `SYNTHETIC_LOCAL_OUTAGE` * `SYNTHETIC_NODE_OUTAGE` * `SYNTHETIC_PRIVATE_LOCATION_OUTAGE` * `SYNTHETIC_TEST_LOCATION_SLOWDOWN` |
| negate | boolean | The alert triggers when the problem of specified severity arises while the specified event **is** happening (`false`) or while the specified event is **not** happening (`true`).  For example, if you chose the Slowdown (`PERFORMANCE`) severity and Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`) event with **negate** set to `true`, the alerting profile will trigger only when the slowdown problem is raised while there is no unexpected high traffic event.  Consider the following use case as an example. The Slowdown (`PERFORMANCE`) severity rule is set. Depending on the configuration of the event filter (Unexpected high traffic (`APPLICATION_UNEXPECTED_HIGH_LOAD`) event is used as an example), the behavior of the alerting profile is one of the following:\* **negate** is set to `false`: The alert triggers when the slowdown problem is raised while unexpected high traffic event is happening.  * **negate** is set to `true`: The alert triggers when the slowdown problem is raised while there is no unexpected high traffic event. * no event rule is set: The alert triggers when the slowdown problem is raised, regardless of any events. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `AlertingProfileSeverityRule` object

A severity rule of the alerting profile.

A severity rule defines the level of severity that must be met before an alert is sent our for a detected problem. Additionally it restricts the alerting to certain monitored entities.

| Element | Type | Description |
| --- | --- | --- |
| delayInMinutes | integer | Send a notification if a problem remains open longer than *X* minutes. |
| severityLevel | string | The severity level to trigger the alert. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `MONITORING_UNAVAILABLE` * `PERFORMANCE` * `RESOURCE_CONTENTION` |
| tagFilter | [AlertingProfileTagFilter](#openapi-definition-AlertingProfileTagFilter) | Configuration of the tag filtering of the alerting profile. |

#### The `AlertingProfileTagFilter` object

Configuration of the tag filtering of the alerting profile.

| Element | Type | Description |
| --- | --- | --- |
| includeMode | string | The filtering mode:  * `INCLUDE_ANY`: The rule applies to monitored entities that have at least one of the specified tags. You can specify up to 100 tags. * `INCLUDE_ALL`: The rule applies to monitored entities that have **all** of the specified tags. You can specify up to 10 tags. * `NONE`: The rule applies to all monitored entities. The element can hold these values * `INCLUDE_ALL` * `INCLUDE_ANY` * `NONE` |
| tagFilters | [TagFilter](#openapi-definition-TagFilter)[] | A list of required tags. |

#### The `TagFilter` object

A tag-based filter of monitored entities.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. The element can hold these values * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | The key of the tag.  Custom tags have the tag value here. |
| value | string | The value of the tag.  Not applicable to custom tags. |

### Response body JSON models

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

## Example

In this example, the request lists the parameters of the **Transaction slowdown** alerting profile.

The API token is passed in the **Authorization** header.

The profile has the following parameters:

![GET example](https://dt-cdn.net/images/get-1347-c383260394.png)

GET example

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/93ac79a3-8cba-4be5-af44-50673b5e77f2 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/alertingProfiles/93ac79a3-8cba-4be5-af44-50673b5e77f2
```

#### Response body

```
{



"metadata": {



"currentConfigurationVersions": [



"7.0.0"



],



"configurationVersions": [],



"clusterVersion": "1.218.0.20210429-093737"



},



"id": "19e50c27-8aed-408f-ad44-d6a1bf856f49",



"displayName": "Transaction slowdown",



"rules": [



{



"severityLevel": "AVAILABILITY",



"tagFilter": {



"includeMode": "INCLUDE_ANY",



"tagFilters": [



{



"context": "CONTEXTLESS",



"key": "/rest",



"value": null



},



{



"context": "CONTEXTLESS",



"key": "/rest/configuration",



"value": null



}



]



},



"delayInMinutes": 1



}



],



"managementZoneId": 9130632296508575249,



"mzId": "9130632296508575249",



"eventTypeFilters": [



{



"predefinedEventFilter": {



"eventType": "APPLICATION_UNEXPECTED_HIGH_LOAD",



"negate": true



}



},



{



"predefinedEventFilter": {



"eventType": "SYNTHETIC_GLOBAL_OUTAGE",



"negate": false



}



}



]



}
```

#### Response code

200

## Related topics

* [Problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.")
* [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")