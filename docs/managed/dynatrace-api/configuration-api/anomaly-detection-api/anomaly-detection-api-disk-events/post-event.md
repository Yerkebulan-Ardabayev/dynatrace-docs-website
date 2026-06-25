---
title: Disk events anomaly detection API - POST an event
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-disk-events/post-event
scraped: 2026-05-12T11:20:25.705361
---

# Disk events anomaly detection API - POST an event

# Disk events anomaly detection API - POST an event

* Reference
* Published Aug 29, 2019

Creates a new disk event rule.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [DiskEventAnomalyDetectionConfig](#openapi-definition-DiskEventAnomalyDetectionConfig) | JSON body of the request. Contains parameters of the new disk event rule. | body | Optional |

### Request body objects

#### The `DiskEventAnomalyDetectionConfig` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| diskNameFilter | [DiskNameFilter](#openapi-definition-DiskNameFilter) | Narrows the rule usage down to disks, matching the specified criteria. | Optional |
| enabled | boolean | Disk event rule enabled/disabled. | Required |
| hostGroupId | string | Narrows the rule usage down to disks that run on hosts that themselves run on the specified host group. | Optional |
| id | string | The ID of the disk event rule. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| metric | string | The metric to monitor. The element can hold these values * `LOW_DISK_SPACE` * `LOW_INODES` * `READ_TIME_EXCEEDING` * `WRITE_TIME_EXCEEDING` | Required |
| name | string | The name of the disk event rule. | Required |
| samples | integer | The number of samples to evaluate. | Required |
| tagFilters | [TagFilter[]](#openapi-definition-TagFilter) | Narrows the rule usage down to the hosts matching the specified tags. | Optional |
| threshold | number | The threshold to trigger disk event.  * A percentage for `LowDiskSpace` or `LowInodes` metrics. * In milliseconds for `ReadTimeExceeding` or `WriteTimeExceeding` metrics. | Required |
| violatingSamples | integer | The number of samples that must violate the threshold to trigger an event. Must not exceed the number of evaluated samples. | Required |

#### The `DiskNameFilter` object

Narrows the rule usage down to disks, matching the specified criteria.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| operator | string | Comparison operator. The element can hold these values * `CONTAINS` * `DOES_NOT_CONTAIN` * `DOES_NOT_EQUAL` * `DOES_NOT_START_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| value | string | Value to compare to. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

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



"diskNameFilter": {



"operator": "CONTAINS",



"value": "string"



},



"enabled": true,



"hostGroupId": "string",



"id": "string",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"metric": "LOW_DISK_SPACE",



"name": "string",



"samples": 10,



"tagFilters": [



{



"context": "AWS",



"key": "string",



"value": "string"



}



],



"threshold": 1,



"violatingSamples": 8



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new disk event rule has been created. The ID of the new disk event rule is returned. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/diskEvents/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted disk event rule is valid. Response doesn't have a body. |
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

In this example, the request creates a new custom disk event rule named **very slow disk**. The rule triggers an alert for any disk whose name **starts with `C`** and whose read time exceeds **200** milliseconds in **8** out of **10** samples.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"name": "very slow disk",



"enabled": true,



"metric": "READ_TIME_EXCEEDING",



"threshold": 200,



"samples": 10,



"violatingSamples": 8,



"diskNameFilter": {



"operator": "STARTS_WITH",



"value": "C"



},



"tagFilters": []



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/diskEvents
```

#### Request body

```
{



"name": "very slow disk",



"enabled": true,



"metric": "READ_TIME_EXCEEDING",



"threshold": 200,



"samples": 10,



"violatingSamples": 8,



"diskNameFilter": {



"operator": "STARTS_WITH",



"value": "C"



},



"tagFilters": []



}
```

#### Response body

```
{



"id": "fdd83212-9c08-44ba-a0cf-dbb471cd819a",



"name": "very slow disk"



}
```

#### Response code

204

#### Result

The new rule looks like this in the UI:

![Custom disk events rule - new](https://dt-cdn.net/images/disk-events-new-1324-3559d560ae.png)

Custom disk events rule - new

## Related topics

* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")