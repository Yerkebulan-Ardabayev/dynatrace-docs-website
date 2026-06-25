---
title: Log Monitoring API v2 - GET aggregate logs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs
scraped: 2026-05-12T11:54:14.088419
---

# Log Monitoring API v2 - GET aggregate logs

# Log Monitoring API v2 - GET aggregate logs

* Reference
* Updated on Nov 20, 2025

Gets the aggregated log records that match the provided criteria.

Returns the aggregated number of occurrences of log values divided into time slots.

It is possible that the timeframe covered by the results exceeds the specified timeframe. In such cases, the request returns fewer timeslots than specified in the **timeBuckets** query parameter.

The request produces an `application/json` payload.

This API only works with Log Monitoring Classic.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/logs/aggregate` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/aggregate` |

## Authentication

To execute this request, you need an access token with `logs.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two weeks is used (`now-2w`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| query | string | The log search query.  The query must use the [Dynatrace search query languageï»¿](https://dt-url.net/pe03s6f). | query | Optional |
| timeBuckets | integer | The number of time slots in the result.  The query timeframe is divided equally into the specified number of slots.  The minimum length of a slot is 1 ms.  If not set, 1 is used. | query | Optional |
| maxGroupValues | integer | The maximum number of values in each group.  You can get up to 100 values per group.  If not set, 10 is used. | query | Optional |
| groupBy | string[] | The groupings to be included in the response.  You can specify several groups in the following format: `groupBy=status&groupBy=log.source`.  If not set, all possible groups are returned. You can use this option to check for possible grouping values.  Unique log data attributes (high-cardinality attributes) for example, `span_id` or `trace_id` cannot be used for grouping. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AggregatedLog](#openapi-definition-AggregatedLog) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `AggregatedLog` object

Aggregated log records.

| Element | Type | Description |
| --- | --- | --- |
| aggregationResult | object | Aggregated log records. |
| warnings | string | Optional warning messages. |

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



"aggregationResult": {



"hostId": {



"1597835271": {



"localhost": "12"



},



"1597835331": {



"remotehost": "6"



}



},



"logLevel": {



"1597835271": {



"ERROR": "1",



"INFO": "2"



},



"1597835331": {



"INFO": "17"



}



},



"logPath": {



"1597835271": {



"/var/log/messages": "15",



"/var/log/syslog": "3"



},



"1597835331": {



"/var/log/messages": "15",



"/var/log/syslog": "3"



}



},



"processId": {



"1597835271": {



"cassandra": "6"



},



"1597835331": {



"apache": "12",



"cassandra": "60"



}



}



}



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