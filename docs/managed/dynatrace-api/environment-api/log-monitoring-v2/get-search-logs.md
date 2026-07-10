---
title: Log Monitoring API v2 - GET search logs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs
---

# Log Monitoring API v2 - GET search logs

# Log Monitoring API v2 - GET search logs

* Reference
* Updated on Nov 20, 2025

Gets the log records matching the provided criteria. Matching log records are sorted by the criteria specified in the **sort** query parameter, and then the first *X* records (as specified by the **limit** query parameter) are returned. To run a query without a size limit, use the [GET export logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs "Fetch log records via the Log Monitoring API v2.") request.

If the resulting log is too large, it is divided into slices. In such cases, the first response contains the **nextSliceKey** for the second slice. Use it in the **nextSliceKey** query parameter to obtain the second slice, which in turn contains the **nextSliceKey** for the third slice, and so on.

Results might be distributed unevenly between slices, and some slices might be empty.

The request produces an `application/json` payload.

This API only works with Log Monitoring Classic.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/search` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/search` |

## Authentication

To execute this request, you need an access token with `logs.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| limit | integer | The desired amount of log records.  The maximal allowed limit is 1000.  If not set, 1000 is used. | query | Optional |
| query | string | The log search query.  The query must use the [Dynatrace search query language﻿](https://dt-url.net/pe03s6f?dt=m). | query | Optional |
| sort | string | Defines the ordering of the log records.  Each field has a sign prefix (+/-) for sorting order. If no sign prefix is set, then the `+` option will be applied.  Currently, ordering is available only for the timestamp (+timestamp for the oldest records first, or -timestamp for the newest records first).  When millisecond resolution provided by the timestamp is not enough, log records are sorted based on the order in which they appear in the log source (remote process writing to REST API endpoint or remote process from which logs are collected). | query | Optional |
| nextSliceKey | string | The cursor for the next slice of results. You can find it in the **nextSliceKey** field of the previous response.  The first slice is always returned if you don't specify this parameter.  If this parameter is set, all other query parameters are ignored.  Unsupported on *Log Management and Analytics, powered by Grail*. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LogRecordsList](#openapi-definition-LogRecordsList) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `LogRecordsList` object

A list of retrieved log records.

| Element | Type | Description |
| --- | --- | --- |
| nextSliceKey | string | The cursor for the next slice of log records. Always null on *Log Management and Analytics, powered by Grail*. |
| results | [LogRecord](#openapi-definition-LogRecord)[] | A list of retrieved log records. |
| sliceSize | integer | The total number of records in a slice. |
| warnings | string | Optional warning messages. |

#### The `LogRecord` object

A single log record.

| Element | Type | Description |
| --- | --- | --- |
| additionalColumns | object | Additional columns of the log record. |
| content | string | The content of the log record. |
| eventType | string | Type of event |
| status | string | The log status (based on the log level). The element can hold these values * `ERROR` * `INFO` * `NONE` * `NOT_APPLICABLE` * `WARN` |
| timestamp | integer | The timestamp of the log record, in UTC milliseconds. |

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



"nextSliceKey": "___-2hI03q0AAAAAAAAAAAAAA-gAAAAAAAAH0P____8AAABkAAAACXRpbWVzdGFtcAD___7aEjTerQ",



"results": [



{



"additionalColumns": {



"custom.attribute": [



"value1",



"value2"



],



"loglevel": [



"SEVERE"



]



},



"content": "example log content",



"event.type": "LOG",



"status": "ERROR",



"timestamp": "1631193089000"



}



],



"sliceSize": 100



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

* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")