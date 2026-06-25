---
title: ActiveGate API - GET all auto-update jobs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/get-all-jobs
scraped: 2026-05-12T11:59:58.656593
---

# ActiveGate API - GET all auto-update jobs

# ActiveGate API - GET all auto-update jobs

* Reference
* Published Jul 02, 2020

Lists all update jobs for the specified ActiveGate. The list includes completed jobs (successful or failed) and jobs in progress.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/updateJobs` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| agId | string | The ID of the required ActiveGate. | path | Required |
| from | string | The start of the requested timeframe for update jobs.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of one week is used (`now-1w`).  Maximum timeframe is 31 days. | query | Optional |
| to | string | The end of the requested timeframe for update jobs.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| startVersionCompareType | string | Filters the resulting set of update jobs by the specified initial version.  Specify the comparison operator here. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| startVersion | string | Filters the resulting set of update-jobs by the initial version (required format `<major>.<minor>.<revision>`). | query | Optional |
| updateType | string | Filters the resulting set of update-jobs by the update type. The element can hold these values * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` | query | Optional |
| targetVersionCompareType | string | Filters the resulting set of update jobs by the specified target version.  Specify the comparison operator here. The element can hold these values * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Optional |
| targetVersion | string | Filters the resulting set of update-jobs by the target version (required format `<major>.<minor>.<revision>`). | query | Optional |
| lastUpdates | boolean | If `true`, filters the resulting set of update jobs to the most recent update of each type. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UpdateJobList](#openapi-definition-UpdateJobList) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Not found. See response body for details. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UpdateJobList` object

A list of update jobs of the ActiveGate.

| Element | Type | Description |
| --- | --- | --- |
| agId | string | The ID of the ActiveGate. |
| updateJobs | [UpdateJob[]](#openapi-definition-UpdateJob) | A list of update jobs of the ActiveGate. |

#### The `UpdateJob` object

Configuration of the ActiveGate update job.

| Element | Type | Description |
| --- | --- | --- |
| agType | string | The type of the ActiveGate. The element can hold these values * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| cancelable | boolean | The job can (`true`) or can't (`false`) be cancelled at the moment. |
| duration | integer | The duration of the update, in milliseconds. |
| environments | string[] | A list of environments (specified by IDs) the ActiveGate can connect to. |
| error | string | The information about update error. |
| jobId | string | The ID of the update job. |
| jobState | string | The status of the update job. The element can hold these values * `FAILED` * `IN_PROGRESS` * `PENDING` * `ROLLBACK` * `SCHEDULED` * `SKIPPED` * `SUCCEED` |
| startVersion | string | The initial version of the ActiveGate. |
| targetVersion | string | The target version of the update.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format.  To update to the latest available version, use the `latest` value. |
| timestamp | integer | The timestamp of the update job completion.  The `null` value means the job is still running. |
| updateMethod | string | The method of updating the ActiveGate or its component. The element can hold these values * `AUTOMATIC` * `MANUAL_INSTALLATION` * `ON_DEMAND` |
| updateType | string | The component to be updated. The element can hold these values * `ACTIVE_GATE` * `REMOTE_PLUGIN_AGENT` * `SYNTHETIC` * `Z_REMOTE` |

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



"agId": "0x3efdd092",



"updateJobs": [



{



"agType": "ENVIRONMENT",



"cancelable": false,



"duration": 3608000,



"environments": [



"string"



],



"error": "string",



"jobId": "-3524498778810258605",



"jobState": "SUCCEED",



"startVersion": "1.185.0.20200201-120000",



"targetVersion": "1.190.0.20200301-130000",



"timestamp": 1582031917814,



"updateMethod": "AUTOMATIC",



"updateType": "ACTIVE_GATE"



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

## Example

In this example, the request lists all auto-update jobs of the ActiveGate with the ID of **2100855201**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2100855201/updateJobs' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates/2100855201/updateJobs
```

#### Response body

```
{



"agId": "2100855201",



"updateJobs": [



{



"jobId": "-3137933319273211278",



"jobState": "SUCCEED",



"updateMethod": "MANUAL_INSTALLATION",



"updateType": "ACTIVE_GATE",



"cancelable": false,



"startVersion": "1.198.0.20200629-221007",



"targetVersion": "1.198.0.20200630-163221",



"timestamp": 1593683526719,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": 556574



},



{



"jobId": "-6733215466838702651",



"jobState": "SUCCEED",



"updateMethod": "AUTOMATIC",



"updateType": "REMOTE_PLUGIN_AGENT",



"cancelable": false,



"startVersion": "1.198.0.20200629-123323",



"targetVersion": "1.198.0.20200630-155408",



"timestamp": 1593545522797,



"agType": "ENVIRONMENT",



"environments": [



"mySampleEnv"



],



"error": null,



"duration": 42669



}



]



}
```

#### Response code

200

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")