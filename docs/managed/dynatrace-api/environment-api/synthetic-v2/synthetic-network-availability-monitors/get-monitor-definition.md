---
title: Synthetic monitors API v2 - GET Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-monitor-definition
scraped: 2026-05-12T12:15:46.525963
---

# Synthetic monitors API v2 - GET Synthetic monitor definition

# Synthetic monitors API v2 - GET Synthetic monitor definition

* Reference
* Updated on May 05, 2026

Get a Synthetic monitor definition for the given monitor ID.

The method is available only for browser and NAM monitors.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The identifier of the monitor. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticMultiProtocolMonitorResponse](#openapi-definition-SyntheticMultiProtocolMonitorResponse) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticMultiProtocolMonitorResponse` object

Network Availability monitor.

| Element | Type | Description |
| --- | --- | --- |
| description | string | Monitor description |
| enabled | boolean | If true, the monitor is enabled. |
| entityId | string | The entity id of the monitor. |
| frequencyMin | integer | The frequency of the monitor, in minutes. |
| locations | string[] | The locations to which the monitor is assigned. |
| modificationTimestamp | integer | The timestamp of the last modification |
| name | string | The name of the monitor. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto[]](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto) | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. |
| steps | [SyntheticMultiProtocolMonitorStepDto[]](#openapi-definition-SyntheticMultiProtocolMonitorStepDto) | The steps of the monitor. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. |
| tags | [SyntheticTagWithSourceDto[]](#openapi-definition-SyntheticTagWithSourceDto) | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` |

#### The `SyntheticMonitorPerformanceThresholdsDto` object

Performance thresholds configuration.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). |
| thresholds | [SyntheticMonitorPerformanceThresholdDto[]](#openapi-definition-SyntheticMonitorPerformanceThresholdDto) | The list of performance threshold rules. |

#### The `SyntheticMonitorPerformanceThresholdDto` object

The performance threshold rule.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | Aggregation type The element can hold these values * `AVG` * `MAX` * `MIN` |
| dealertingSamples | integer | Number of most recent non-violating request executions that closes the problem. |
| samples | integer | Number of request executions in analyzed sliding window (sliding window size). |
| stepIndex | integer | Specify the step's index to which a threshold applies. If threshold is monitor-level, no index is needed. |
| threshold | number | Notify if monitor request takes longer than *X* time units to execute. For Network Availability monitors the time unit is milliseconds, for browser monitors - seconds. |
| type | string | Type of performance threshold. The element can hold these values * `MONITOR` * `STEP` |
| violatingSamples | integer | Number of violating request executions in analyzed sliding window. |

#### The `SyntheticMonitorPrimaryGrailTagDto` object

Primary grail tag key-value pair.

| Element | Type | Description |
| --- | --- | --- |
| key | string | Tag key. |
| value | string | Tag value. |

#### The `SyntheticMultiProtocolMonitorStepDto` object

The step of a network availability monitor.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | The list of constraints which apply to all requests in the step. |
| name | string | Step name. |
| properties | object | The properties which apply to all requests in the step. |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto[]](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto) | Request configurations. |
| requestType | string | Request type. The element can hold these values * `ICMP` * `TCP` * `DNS` |
| targetFilter | string | Target filter. |
| targetList | string[] | Target list. |

#### The `SyntheticMonitorConstraintDto` object

Synthetic monitor constraint.

| Element | Type | Description |
| --- | --- | --- |
| properties | object | The properties of the constraint. |
| type | string | Constraint type. |

#### The `SyntheticMultiProtocolRequestConfigurationDto` object

The configuration of a network availability monitor request.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto[]](#openapi-definition-SyntheticMonitorConstraintDto) | Request constraints. |

#### The `SyntheticMonitorOutageHandlingSettingsDto` object

Outage handling configuration.

| Element | Type | Description |
| --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Number of consecutive failures for all locations. |
| globalOutages | boolean | Generate a problem and send an alert when the monitor is unavailable at all configured locations. |
| localConsecutiveOutageCountThreshold | integer | Number of consecutive failures. |
| localLocationOutageCountThreshold | integer | Number of failing locations. |
| localOutages | boolean | Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |
| retryOnError | boolean | Only Browser Monitor property. If set to true, execution retry will take place in case the monitor fails. |

#### The `SyntheticTagWithSourceDto` object

The tag with source of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO. The element can hold these values * `AUTO` * `RULE_BASED` * `USER` |
| value | string | The value of the tag. |

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



"description": "My network availability monitor description",



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



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