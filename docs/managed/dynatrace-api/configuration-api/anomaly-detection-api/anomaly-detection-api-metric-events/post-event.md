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

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Metric events** (`builtin:anomaly-detection.metric-events`) schema.

Creates a new metric event rule.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all JSON models that depend on the type of the model, refer to [JSON models](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models "Learn the variations of models in metric event rules via the Dynatrace API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [MetricEvent](#openapi-definition-MetricEvent) | The JSON body of the request. Contains parameters of the new metric event. | body | Optional |

### Request body objects

#### The `MetricEvent` object

The configuration of the metric event.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregationType | string | How the metric data points are aggregated for the evaluation.  The timeseries must support this aggregation. The element can hold these values * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `P90` * `SUM` * `VALUE` | Optional |
| alertingScope | [MetricEventAlertingScope[]](#openapi-definition-MetricEventAlertingScope) | Defines the scope of the metric event. Only one filter is allowed per filter type, except for tags, where up to 3 are allowed. The filters are combined by conjunction. | Optional |
| description | string | The description of the metric event. | Required |
| disabledReason | string | The reason of automatic disabling.  The `NONE` means config was not disabled automatically. The element can hold these values * `METRIC_DEFINITION_INCONSISTENCY` * `NONE` * `TOO_MANY_DIMS` | Optional |
| enabled | boolean | The metric event is enabled (`true`) or disabled (`false`). | Required |
| id | string | The ID of the metric event. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| metricDimensions | [MetricEventDimensions[]](#openapi-definition-MetricEventDimensions) | Defines the dimensions of the metric to alert on. The filters are combined by conjunction. | Optional |
| metricId | string | The ID of the metric evaluated by the metric event. | Optional |
| metricSelector | string | The metric selector that should be executed. | Optional |
| monitoringStrategy | [MetricEventMonitoringStrategy](#openapi-definition-MetricEventMonitoringStrategy) | A monitoring strategy for a metric event config.  This is the base version of the monitoring strategy, depending on the type, the actual JSON may contain additional fields. | Required |
| name | string | The name of the metric event displayed in the UI. | Required |
| primaryDimensionKey | string | Defines which dimension key should be used for the **alertingScope**. | Optional |
| queryOffset | integer | Defines the query offset to adapt the evaluation timeframe for known metric latency. | Optional |
| severity | string | The type of the event to trigger on the threshold violation.  The `CUSTOM_ALERT` type is not correlated with other alerts. The `INFO` type does not open a problem. The element can hold these values * `AVAILABILITY` * `CUSTOM_ALERT` * `ERROR` * `INFO` * `PERFORMANCE` * `RESOURCE_CONTENTION` | Optional |
| warningReason | string | The reason of a warning set on the config.  The `NONE` means config has no warnings. The element can hold these values * `NONE` | Optional |

#### The `MetricEventAlertingScope` object

A single filter for the alerting scope.

The actual set of fields depends on type of the filter. Find the list of actual objects in the description of the **filterType** field or see [Metric events anomaly detection API - JSON modelsï»¿](https://dt-url.net/ql63sap).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| filterType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `ENTITY_ID` -> EntityIdAlertingScope * `MANAGEMENT_ZONE` -> ManagementZoneAlertingScope * `TAG` -> TagFilterAlertingScope * `NAME` -> NameAlertingScope * `CUSTOM_DEVICE_GROUP_NAME` -> CustomDeviceGroupNameAlertingScope * `HOST_GROUP_NAME` -> HostGroupNameAlertingScope * `HOST_NAME` -> HostNameAlertingScope * `PROCESS_GROUP_ID` -> ProcessGroupIdAlertingScope * `PROCESS_GROUP_NAME` -> ProcessGroupNameAlertingScope The element can hold these values * `CUSTOM_DEVICE_GROUP_NAME` * `ENTITY_ID` * `HOST_GROUP_NAME` * `HOST_NAME` * `MANAGEMENT_ZONE` * `NAME` * `PROCESS_GROUP_ID` * `PROCESS_GROUP_NAME` * `TAG` | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `MetricEventDimensions` object

A single filter for the metrics dimensions.

The actual set of fields depends on type of the filter. Find the list of actual objects in the description of the **filterType** field or see [Metric events anomaly detection API - JSON modelsï»¿](https://dt-url.net/ql63sap).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| filterType | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `ENTITY` -> MetricEventEntityDimensions * `STRING` -> MetricEventStringDimensions The element can hold these values * `ENTITY` * `STRING` | Required |
| key | string | The dimensions key on the metric. | Optional |

#### The `MetricEventMonitoringStrategy` object

A monitoring strategy for a metric event config.

This is the base version of the monitoring strategy, depending on the type,
the actual JSON may contain additional fields.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `STATIC_THRESHOLD` -> MetricEventStaticThresholdMonitoringStrategy * `AUTO_ADAPTIVE_BASELINE` -> MetricEventAutoAdaptiveBaselineMonitoringStrategy The element can hold these values * `AUTO_ADAPTIVE_BASELINE` * `STATIC_THRESHOLD` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The metric event has been created. The response contains the ID and name of the newly created metric event |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/metricEvents/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
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

In this example, the request creates a **custom alert** that triggers if **free disk space** drops below **3%** in **3** out of **5** samples. The scope of the alert is **all** hosts.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own.

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

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/metricEvents
```

#### Request body

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

#### Response body

```
{



"id": "1b06b18a-82df-4e18-a4aa-d4543b227734",



"name": "Low disk space",



"description": "The available disk space is below 3%"



}
```

#### Response code

204

#### Result

The new rule looks like this in the UI:

![Metric event rule - new](https://dt-cdn.net/images/metric-events-new-1234-0b9131aee3.png)

Metric event rule - new

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")