---
title: ActiveGate API - GET ActiveGates with auto-update jobs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-jobs/get-activegates-jobs
---

# ActiveGate API - GET ActiveGates with auto-update jobs

# ActiveGate API - GET ActiveGates with auto-update jobs

* Reference
* Published Jul 02, 2020

Lists all ActiveGates that have auto-update jobs. The list includes completed jobs (successful or failed) and jobs in progress.

You can narrow down the output by specifying filtering parameters in your request.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/updateJobs` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/updateJobs` |

## Authentication

To execute this request, you need an access token with `activeGates.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe for update jobs.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of one day is used (`now-1d`).  Maximum timeframe is 31 days. | query | Optional |
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
| **200** | [UpdateJobsAll](#openapi-definition-UpdateJobsAll) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UpdateJobsAll` object

A list of ActiveGates with update jobs.

| Element | Type | Description |
| --- | --- | --- |
| allUpdateJobs | [UpdateJobList](#openapi-definition-UpdateJobList)[] | A list of ActiveGates with update jobs. |

#### The `UpdateJobList` object

A list of update jobs of the ActiveGate.

| Element | Type | Description |
| --- | --- | --- |
| agId | string | The ID of the ActiveGate. |
| updateJobs | [UpdateJob](#openapi-definition-UpdateJob)[] | A list of update jobs of the ActiveGate. |

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



"allUpdateJobs": [



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

## Related topics

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")