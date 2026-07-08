---
title: Timeseries API v1 - GET list of metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list
---

# Timeseries API v1 - GET list of metrics

# Timeseries API v1 - GET list of metrics

* Reference
* Published Nov 06, 2019

This API is deprecated. It will be removed in the future. Use [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") instead.

Lists all metric definitions, along with parameters of each metric available within your environment.

The full list can be lengthy, but you can narrow it down by specifying filter parameters such as the source of the metric. See the **Parameters** expandable section for more details.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries` |

## Authentication

To execute this request, you need an access token with `DataExport` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| source | string | The type of the metric, such as BUILTIN or CUSTOM. The element can hold these values * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` | query | Optional |
| detailedSource | string | The feature where metrics originates, such as Synthetic or RUM. | query | Optional |

### Possible values for the `detailedSource` element:

You can find allowed values for the `detailedSource` element in the subheadings of the **Built-in metrics** and **Plugin metrics** sections of the available metrics pages for [SaaS](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.") and [Managed](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics."). Use them exactly as in headings—spaces included.

## Response

The result is JSON containing the array of objects, with each object representing a metric.

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TimeseriesDefinition](#openapi-definition-TimeseriesDefinition)[] | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `TimeseriesDefinition` object

The configuration of a metric with all its parameters.

| Element | Type | Description |
| --- | --- | --- |
| aggregationTypes | string[] | The list of allowed aggregations for this metric. The element can hold these values * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| detailedSource | string | The feature, where the metric originates. |
| dimensions | string[] | The fine metric division, for example process group and process ID for some process-related metric. |
| displayName | string | The name of the metric in the user interface. |
| filter | string | The feature, where the metric originates. The element can hold these values * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` |
| pluginId | string | The ID of the plugin, where the metric originates. |
| timeseriesId | string | The ID of the metric. |
| types | string[] | Technology type definition. Used to group metrics under a logical technology name. |
| unit | string | The unit of the metric. The element can hold these values * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (µs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (‰)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| warnings | string[] | The warnings that occurred while creating the metric. |

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
[



{



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"detailedSource": "Infrastructure",



"dimensions": [



"HOST"



],



"displayName": "CPU idle",



"filter": "BUILTIN",



"timeseriesId": "com.dynatrace.builting:host.cpu.idle",



"types": [



"Test"



],



"unit": "Percent",



"warnings": []



}



]
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

In this example, the request lists the metric of the **PLUGIN** type, where the detailed source is **PHP-FPM**.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/timeseries?source=plugin&detailedsource=PHP-FPM' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries?api-token&source=plugin&detailedsource=PHP-FPM
```

#### Response content

```
[



{



"timeseriesId": "beta.python.phpfpm.dev:accepted conn",



"displayName": "accepted conn",



"dimensions": [



"PROCESS_GROUP_INSTANCE",



"pool"



],



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"unit": "Count (count)",



"filter": "PLUGIN",



"detailedSource": "PHP-FPM",



"pluginId": "beta.python.phpfpm.dev",



"types": []



},



{



"timeseriesId": "beta.python.phpfpm.dev:active processes",



"displayName": "active processes",



"dimensions": [



"PROCESS_GROUP_INSTANCE",



"pool"



],



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"unit": "Count (count)",



"filter": "PLUGIN",



"detailedSource": "PHP-FPM",



"pluginId": "beta.python.phpfpm.dev",



"types": []



}



]
```

#### Response code

200

## Process types

The list of known process types we monitor with Dynatrace is continuously growing. If you don't see the process type you want in the list below, please refer to the Dynatrace processes page to see whether the process is included there.

Click to view process types list

|  |  |  |  |
| --- | --- | --- | --- |
| * apachehttp * apmng * awsrds * cassandra * couchdb * db2 * dockerdaemon * dotnet * erlang * glassfish | * haproxy * iis * iisapppool * java * jboss * linuxsystem * memcached * mongodb * mongodbrouter | * mssql * mysql * nginx * nodejs * oracledb * perl * php * postgres * python | * redis * ruby * tomcat * unknown * varnishcache * weblogic * websphere * windowsservice * windowssystem |

## OS types

The list of known operating systems that we monitor with Dynatrace is continuously growing. If you don't see the OS type you want listed below, please refer to the Dynatrace hosts page to see whether the OS type is included there.

Click to view the OS list

|  |  |
| --- | --- |
| * aix * darwin * hpux * linux | * solaris * unknown * windows * zos |

## Service types

Click to view the services list

|  |  |
| --- | --- |
| * database * messaging * method * mobile * process | * rmi * unknown * webrequest * webservice * website |

## Technology types

Click to view the technology list

|  |  |
| --- | --- |
| * apache * dotnet * iis * java * loganalytics * net * nginx * nodejs | * os * php * ruby * sdk * unknown * varnish * wsmb * z |

## Aggregation types

Click to view aggregation type list

|  |  |
| --- | --- |
| * max * min * sum * count | * avg * median * percentile |

## Related topics

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")