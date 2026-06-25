---
title: Log Monitoring API v2 - GET export logs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/get-export-logs
scraped: 2026-05-12T11:54:15.310165
---

# Log Monitoring API v2 - GET export logs

# Log Monitoring API v2 - GET export logs

* Reference
* Updated on Nov 20, 2025

Gets the log records matching the provided criteria. Matching log records are sorted by the criteria specified in the **sort** query parameter.

Unlike the [GET search logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/get-search-logs "Fetch log records via the Log Monitoring API v2.") request, this one does not impose a limit on the total number of resulting log records. However, if the resulting log is too large, pagination is applied. You can set the page size in the **pageSize** query parameter. In such cases, the first response contains the **nextPageKey** for the second page. Use it in the **nextPageKey** query parameter to obtain the second page, which in turn contains the **nextPageKey** for the third page, and so on.

The request produces an `application/json` payload.

This API only works with Log Monitoring Classic.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/export` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/export` |

## Authentication

To execute this request, you need an access token with `logs.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The number of results per result page. | query | Optional |
| query | string | The log search query.  The query must use the [Dynatrace search query languageï»¿](https://dt-url.net/pe03s6f). | query | Optional |
| sort | string | Defines the ordering of the log records.  Each field has a sign prefix (+/-) for sorting order. If no sign prefix is set, then the `+` option will be applied.  Currently, ordering is available only for the timestamp (+timestamp for the oldest records first, or -timestamp for the newest records first).  When millisecond resolution provided by the timestamp is not enough, log records are sorted based on the order in which they appear in the log source (remote process writing to REST API endpoint or remote process from which logs are collected). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExportedLogRecordList](#openapi-definition-ExportedLogRecordList) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **501** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The server either does not recognize the request method, or it lacks the ability to fulfill the request. May happen when Grail log storage is enabled. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ExportedLogRecordList` object

A list of exported log records.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| results | [LogRecord[]](#openapi-definition-LogRecord) | A list of retrieved log records. |
| totalCount | integer | The total number of entries in the result. |
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



"nextPageKey": "___-2lZ43q0AAAAdeJxjYAAC1sLS1KJKBhjggtIijFCGHEwCAFiHAoP___7aVnjerQ",



"pageSize": 100,



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



"totalCount": 150



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