---
title: Synthetic monitors API v2 - Update Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/put-update-monitor-definition
scraped: 2026-05-12T12:15:42.174202
---

# Synthetic monitors API v2 - Update Synthetic monitor definition

# Synthetic monitors API v2 - Update Synthetic monitor definition

* Reference
* Updated on May 05, 2026

Update Synthetic monitor definition for a given monitor ID.

The method is available only for browser and NAM monitors.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The identifier of the monitor. | path | Required |
| body | [SyntheticMultiProtocolMonitorRequest](#openapi-definition-SyntheticMultiProtocolMonitorRequest) | The JSON body of the request. Contains the parameters of the monitor. | body | Required |

### Request body objects

#### The `SyntheticMultiProtocolMonitorRequest` object

Network Availability monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | Monitor description | Optional |
| enabled | boolean | If true, the monitor is enabled. | Optional |
| frequencyMin | integer | The frequency of the monitor, in minutes. Default value depends on the monitor type (1 minute for MULTI\_PROTOCOL, 15 minutes for BROWSER). | Optional |
| locations | string[] | The locations to which the monitor is assigned. | Required |
| name | string | The name of the monitor. | Required |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. | Optional |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto[]](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto) | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. | Optional |
| steps | [SyntheticMultiProtocolMonitorStepDto[]](#openapi-definition-SyntheticMultiProtocolMonitorStepDto) | The steps of the monitor. | Required |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. | Optional |
| tags | [SyntheticTagWithSourceDto[]](#openapi-definition-SyntheticTagWithSourceDto) | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. | Optional |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` | Required |

#### The `SyntheticMonitorPerformanceThresholdsDto` object

Performance thresholds configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). | Required |
| thresholds | [SyntheticMonitorPerformanceThresholdDto[]](#openapi-definition-SyntheticMonitorPerformanceThresholdDto) | The list of performance threshold rules. | Optional |

#### The `SyntheticMonitorPerformanceThresholdDto` object

The performance threshold rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | Aggregation type The element can hold these values * `AVG` * `MAX` * `MIN` | Optional |
| dealertingSamples | integer | Number of most recent non-violating request executions that closes the problem. | Optional |
| samples | integer | Number of request executions in analyzed sliding window (sliding window size). | Optional |
| stepIndex | integer | Specify the step's index to which a threshold applies. If threshold is monitor-level, no index is needed. | Optional |
| threshold | number | Notify if monitor request takes longer than *X* time units to execute. For Network Availability monitors the time unit is milliseconds, for browser monitors - seconds. | Required |
| type | string | Type of performance threshold. The element can hold these values * `MONITOR` * `STEP` | Optional |
| violatingSamples | integer | Number of violating request executions in analyzed sliding window. | Optional |

#### The `SyntheticMonitorPrimaryGrailTagDto` object

Primary grail tag key-value pair.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | Tag key. | Required |
| value | string | Tag value. | Required |

#### The `SyntheticMultiProtocolMonitorStepDto` object

The step of a network availability monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | The list of constraints which apply to all requests in the step. | Required |
| name | string | Step name. | Required |
| properties | object | The properties which apply to all requests in the step. | Required |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto[]](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto) | Request configurations. | Required |
| requestType | string | Request type. The element can hold these values * `ICMP` * `TCP` * `DNS` | Required |
| targetFilter | string | Target filter. | Optional |
| targetList | string[] | Target list. | Optional |

#### The `SyntheticMonitorConstraintDto` object

Synthetic monitor constraint.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| properties | object | The properties of the constraint. | Required |
| type | string | Constraint type. | Required |

#### The `SyntheticMultiProtocolRequestConfigurationDto` object

The configuration of a network availability monitor request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Request constraints. | Required |

#### The `SyntheticMonitorOutageHandlingSettingsDto` object

Outage handling configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Number of consecutive failures for all locations. | Optional |
| globalOutages | boolean | Generate a problem and send an alert when the monitor is unavailable at all configured locations. | Required |
| localConsecutiveOutageCountThreshold | integer | Number of consecutive failures. | Optional |
| localLocationOutageCountThreshold | integer | Number of failing locations. | Optional |
| localOutages | boolean | Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. | Required |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Optional |
| retryOnError | boolean | Only Browser Monitor property. If set to true, execution retry will take place in case the monitor fails. | Optional |

#### The `SyntheticTagWithSourceDto` object

The tag with source of a monitored entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. | Optional |
| key | string | The key of the tag. | Required |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO. The element can hold these values * `AUTO` * `RULE_BASED` * `USER` | Optional |
| value | string | The value of the tag. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "My network availability monitor description",



"enabled": "true",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F19"



],



"name": "My network availability monitor",



"performanceThresholds": {



"enabled": "true",



"thresholds": [



{



"aggregation": "AVG",



"dealertingSamples": "5",



"samples": "5",



"stepIndex": "0",



"threshold": "200",



"violatingSamples": "3"



}



]



},



"primaryGrailTags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "another sample key",



"value": "another sample value"



}



],



"steps": [



{



"constraints": [



{



"properties": {



"operator": ">=",



"value": "95"



},



"type": "SUCCESS_RATE_PERCENT"



}



],



"name": "Step 1",



"properties": {



"ICMP_IP_VERSION": "4",



"ICMP_NUMBER_OF_PACKETS": "8",



"ICMP_TIMEOUT_FOR_REPLY": "PT1S"



},



"requestConfigurations": [



{



"constraints": [



{



"properties": {



"operator": "=",



"value": "100"



},



"type": "ICMP_SUCCESS_RATE_PERCENT"



}



]



}



],



"requestType": "ICMP",



"targetFilter": "ipMask == 127.0.0.1/24",



"targetList": [



"127.0.0.1",



"127.0.0.2"



]



}



],



"syntheticMonitorOutageHandlingSettings": {



"globalConsecutiveOutageCountThreshold": "1",



"globalOutages": "true",



"localConsecutiveOutageCountThreshold": "3",



"localLocationOutageCountThreshold": "3",



"localOutages": "true"



},



"tags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "sample key"



}



],



"type": "MULTI_PROTOCOL"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")