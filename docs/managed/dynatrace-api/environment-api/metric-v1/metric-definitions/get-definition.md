---
title: Timeseries API v1 - GET definition of a metric
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-definition
scraped: 2026-05-12T11:58:36.185674
---

# Timeseries API v1 - GET definition of a metric

# Timeseries API v1 - GET definition of a metric

* Reference
* Published Nov 06, 2019

This API is deprecated. It will be removed in the future. Use [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") instead.

Gets the definition of the specified metric.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To get a definition of the metric but not its data points, set the **includeData** parameter to `false`.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| timeseriesId | string | Case-sensitive ID of the metric from which you want to read parameters.  You can execute a [GET metric definitions](/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list "View definitions of all metrics of you monitoring environment via the Timeseries v1 API.") request to obtain the list of available metrics. | path | Required |
| includeData | boolean | Flag to include data points to the response. Set to `false` to obtain just the definition of the metric. | query | Optional |

## Response

The result is a JSON object that contains metric parameters. The **TimeseriesDataPointQueryResult** object is omitted in this case.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TimeseriesQueryResult](#openapi-definition-TimeseriesQueryResult) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `TimeseriesQueryResult` object

The configuration of a metric with all its parameters and, optionally, data points.

| Element | Type | Description |
| --- | --- | --- |
| aggregationTypes | string[] | The list of allowed aggregations for this metric. The element can hold these values * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| dataResult | [TimeseriesDataPointQueryResult](#openapi-definition-TimeseriesDataPointQueryResult) | List of metric's datapoints, as well as their parameters. |
| detailedSource | string | The feature, where the metric originates. |
| dimensions | string[] | The fine metric division, for example process group and process ID for some process-related metric. |
| displayName | string | The name of the metric in the user interface. |
| filter | string | The feature, where the metric originates. The element can hold these values * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` |
| pluginId | string | The ID of the plugin, where the metric originates. |
| timeseriesId | string | The ID of the metric. |
| types | string[] | Technology type definition. Used to group metrics under a logical technology name. |
| unit | string | The unit of the metric. The element can hold these values * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (Âµs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (â°)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| warnings | string[] | The warnings that occurred while creating the metric. |

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



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"dataResult": {



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



},



"detailedSource": "Infrastructure",



"dimensions": [



"HOST"



],



"displayName": "CPU idle",



"filter": "BUILTIN",



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle",



"types": [],



"unit": "Percent"



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

In this example, the request asks for the definition of the **Actions per session** (`com.dynatrace.builtin:app.actionspersession`) metric.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=false \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=false
```

#### Response content

```
{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"displayName": "Actions per session",



"dimensions": [



"APPLICATION"



],



"unit": "PerMinute (count/min)",



"detailedSource": "Web application",



"types": [],



"aggregationTypes": [



"AVG"



],



"filter": "BUILTIN"



}
```

#### Response code

200

## Related topics

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")