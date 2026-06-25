---
title: Timeseries API v1 - POST data points
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/read-data-points/post-data-points
scraped: 2026-05-12T11:58:33.933040
---

# Timeseries API v1 - POST data points

# Timeseries API v1 - POST data points

* Reference
* Published Nov 07, 2019

This API is deprecated. It will be removed in the future. Use [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") instead.

Fetches parameters and data points of the specified metric. In comparison to a GET request, a POST request provides less data about the metric itself.

To obtain data points, you must specify the timeframe and the aggregation type supported by the requested metric. See the **Parameters** section for more details.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To obtain data points, you must specify the timeframe and the aggregation type.

There are two mutually exclusive ways to set timeframe:

* Combination of **startTimestamp** and **endTimestamp**.
* **relativeTime**

The maximum allowed timeframe is 6 months.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| timeseriesIdentifier | string | The case-sensitive ID of the timeseries from which you want to read parameters and data points. | path | Required |
| body | [TimeseriesQueryMessage](#openapi-definition-TimeseriesQueryMessage) | The JSON body of the request, containing parameters to identify the required data points. | body | Optional |

### Request body objects

#### The `TimeseriesQueryMessage` object

Filtering parameters for a timeseries query.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregationType | string | The aggregation type for the resulting data points.  If the requested metric doesn't support the specified aggregation, the request will result in an error. The element can hold these values * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` | Optional |
| considerMaintenanceWindowsForAvailability | boolean | Exclude (`true`) or include (`false`) data points from any [maintenance windowï»¿](https://dt-url.net/b2123rg0), defined in your environment. | Optional |
| endTimestamp | integer | The start timestamp of the timeframe, in UTC milliseconds.  If later than the current time, Dynatrace automatically uses current time instead.  The timeframe must not exceed 6 months. | Optional |
| entities | string[] | Filters requested data points by entities which should deliver them. You can specify several entities at once.  Allowed values are Dynatrace entity IDs.  If the selected entity doesn't support the requested metric, the request will result in an error. | Optional |
| filters | object | A filter is an object, containing map of filter keys and its values. Valid filter keys are:  `processType`: Filters by process type. See Process types for allowed values. `osType`: Filters by operating system. See OS types for allowed values. `serviceType`: Filters by service type. See Service types for allowed values. `technology`: Filters by technology type. See Technology types for allowed values. `webServiceName`: Filters by web service name. `webServiceNamespace`: Filters by the web service namespace. `host`: Filters by entity ID of the host, for example HOST-007. | Optional |
| includeParentIds | boolean | Specifies whether the results should exposes dimension mappings between parent entities and their children.  For instance: SERVICE-0000000000000001, SERVICE\_METHOD-0000000000000001 | Optional |
| percentile | integer | Specifies which percentile of the selected response time metric should be delivered.  Only applicable to the `PERCENTILE` aggregation type.  Valid values for percentile are between 1 and 99.  Please keep in mind that percentile export is only possible for response-time based metrics such as application and service response times. | Optional |
| predict | boolean | The flag to predict future data points. | Optional |
| queryMode | string | Defines the type of result that the call should return. Valid result modes are:  `series`: returns all the data points of the metric in the specified timeframe. `total`: returns one scalar value for the specified timeframe.  By default, the `series` mode is used. The element can hold these values * `SERIES` * `TOTAL` | Optional |
| relativeTime | string | The relative timeframe, back from the current time. The element can hold these values * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | Optional |
| startTimestamp | integer | The start timestamp of the timeframe, in UTC milliseconds. | Optional |
| tags | string[] | Filters requiested data points by entity which should deliver them. Only data from entities with the specified tag is delivered.  You can specify several tags in the following format: `tags=tag1&tags=tag2`. The entity has to match *all* the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags use following format: `[context]key:value`. | Optional |
| timeseriesId | string | The case-sensitive ID of the metric, where you want to read data points.  You can execute a GET timeseries request, to obtain the list of available metrics. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"aggregationType": "AVG",



"considerMaintenanceWindowsForAvailability": "false",



"endTimestamp": 1521542929000,



"entities": [



"HOST-0000000000000007"



],



"includeParentIds": "false",



"predict": true,



"queryMode": "SERIES",



"relativeTime": "HOUR",



"startTimestamp": 1521042929000,



"tags": [



"office-linz"



],



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle"



}
```

## Response

The result is a JSON object that contains metric data points and parameters.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TimeseriesQueryResultWrapper](#openapi-definition-TimeseriesQueryResultWrapper) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `TimeseriesQueryResultWrapper` object

| Element | Type | Description |
| --- | --- | --- |
| result | [TimeseriesDataPointQueryResult](#openapi-definition-TimeseriesDataPointQueryResult) | List of metric's datapoints, as well as their parameters. |

#### The `TimeseriesDataPointQueryResult` object

List of metric's datapoints, as well as their parameters.

| Element | Type | Description |
| --- | --- | --- |
| aggregationType | string | The type of data points aggregation. The element can hold these values * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| dataPoints | object | Data points of a metric.  A JSON object that maps the ID of the entity that delivered the data points and an array, which consists of arrays of the data point float values.  May contain more than one entity ID per record (for example, a host and its network interface). In such cases, entity IDs are separated by commas.  A datapoint contains a value and a timestamp, at which the value was recorded.  Dynatrace stores data in time slots. The **dataPoints** object shows the *starting* timestamp of the slot. If the **startTimestamp** or **endTimestamp** of your query lies inside of the data time slot, this time slot is included into response. Due to the fact that the timestamp of the first data point lies outside of the specified timeframe, you will see *earlier* timestamp than the specified **startTimestamp** in the first data point of the response.  There are three versions of data points:  * Numeric datapoint: Contains a numeric value. * Enum datapoint: Contains an enum value, currently only for availability timeseries. * Prediction datapoint: Similar to the numeric datapoint, but it contains a confidence interval, within which the future values are expected to be. |
| entities | object | The list of entities where the data points originate.  A JSON object that maps the entity ID in Dynatrace and the actual name of the entity. |
| resolutionInMillisUTC | integer | The resolution of data points. |
| timeseriesId | string | The ID of the metric. |
| unit | string | The unit of data points. The element can hold these values * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (Âµs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (â°)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |

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



"result": {



"aggregationType": "AVG",



"dataPoints": {



"HOST-0000000000000007": [



[



1522220334000,



89



]



]



},



"entities": {



"HOST-0000000000000007": "Laptop-8"



},



"resolutionInMillisUTC": 300000,



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle",



"unit": "Percent"



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

## Timeframe note

Dynatrace stores data in time slots. The `dataPoints` object shows the *starting* timestamp of the slot. If the `startTimestamp` or `endTimestamp` of your query fall within the data time slot, this time slot will be included in the response. Due to the fact that the timestamp of the first data point lies outside of the specified timeframe, you will see an *earlier* timestamp than the specified `startTimestamp` in the first data point of the response.

![Timestamp scheme](https://dt-cdn.net/images/timestamp-scheme-541-8f324d62ae.png)

Timestamp scheme

## Example

In this example, the request returns values of the **Actions per session** (`com.dynatrace.builtin:app.actionspersession`) metric within the last hour for the **APPLICATION-85A7CC** and **APPLICATION-8E41C8** applications. The result returns the average numbers of user actions per application. The result is truncated to three data points per application.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries \



-H 'Authorization: abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"relativeTime": "hour",



"aggregationType": "avg",



"entities": [



"APPLICATION-85A7CCAAC7345F0B",



"APPLICATION-8E41C8C247910758"



]



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries
```

#### Request body

```
{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"relativeTime": "hour",



"aggregationType": "avg",



"entities": [



"APPLICATION-85A7CC",



"APPLICATION-8E41C8"



]



}
```

#### Response content

```
{



"result": {



"dataPoints": {



"APPLICATION-85A7CC": [



[



1534920000000,



1.6666666666666667



],



[



1534920060000,



2.5



],



[



1534920120000,



2.888888888888889



]



],



"APPLICATION-8E41C8": [



[



1534920000000,



null



],



[



1534920060000,



3



],



[



1534920120000,



null



]



]



},



"unit": "PerMinute (count/min)",



"resolutionInMillisUTC": 60000,



"aggregationType": "AVG",



"entities": {



"APPLICATION-85A7CC": "Permanent Docker",



"APPLICATION-8E41C8": "easyTravel AMP"



},



"timeseriesId": "com.dynatrace.builtin:app.actionspersession"



}



}
```

#### Response code

200