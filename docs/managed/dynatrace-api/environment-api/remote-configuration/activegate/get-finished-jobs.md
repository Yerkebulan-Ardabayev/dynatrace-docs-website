---
title: ActiveGate remote configuration management API - GET finished jobs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/remote-configuration/activegate/get-finished-jobs
scraped: 2026-05-12T11:55:43.490190
---

# ActiveGate remote configuration management API - GET finished jobs

# ActiveGate remote configuration management API - GET finished jobs

* Reference
* Published Oct 06, 2022

Lists completed configuration job for ActiveGates.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/remoteConfigurationManagement` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/remoteConfigurationManagement` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe for a remote configuration management job.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years | query | Optional |
| to | string | The end of the requested timeframe for a remote configuration management job.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RemoteConfigurationManagementJobList](#openapi-definition-RemoteConfigurationManagementJobList) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `RemoteConfigurationManagementJobList` object

A list of remote configuration management jobs.

| Element | Type | Description |
| --- | --- | --- |
| jobs | [RemoteConfigurationManagementJobSummary[]](#openapi-definition-RemoteConfigurationManagementJobSummary) | A list of remote configuration management jobs. |

#### The `RemoteConfigurationManagementJobSummary` object

Remote configuration management job with basic data.

| Element | Type | Description |
| --- | --- | --- |
| endTime | string | Date (in ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') when the remote configuration management job was finished. This field is present only for finished jobs. |
| entityType | string | Type of entities modified by remote configuration management. The element can hold these values * `ACTIVE_GATE` * `ONE_AGENT` |
| id | string | The ID of the remote configuration management job. |
| startTime | string | Date (in ISO 8601 format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z') when the remote configuration management job was started. |

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



"jobs": [



{



"endTime": "2020-11-05T08:15:30.144Z",



"entityType": "ACTIVE_GATE or ONE_AGENT",



"id": "7974003406714390819",



"startTime": "2020-11-05T08:15:30.144Z"



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