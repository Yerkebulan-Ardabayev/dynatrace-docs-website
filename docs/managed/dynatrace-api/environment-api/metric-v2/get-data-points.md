---
title: "Metrics API - GET metric data points"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-data-points
updated: 2026-02-09
---

# Metrics API - GET metric data points

# Metrics API - GET metric data points

* Reference
* Published Jun 14, 2019

Gets data points of the specified metrics.

You can receive either one aggregated data point per tuple (unique combinations of metricâdimensionâdimension value) or a list of data points per tuple. See the description of the **resolution** parameter of the request for more information.

The following limits apply:

* The number of data points is limited to 20,000,000.
* The number of tuples is limited to 100,000.  
  If exceeded, only the first 100,000 tuples (a `:sort` transformation doesn't affect these) are processed and the rest are ignored.
* The number of data points per tuple is limited to 10,080.
* The number of monitored entities is limited to 5,000 per each [**entitySelector**](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") in the query.

These limits apply to the datapoints that the query reads in the database. The amount of datapoints in the final result might be different. For example, if the `:fold` transformation is used, the query reads multiple data points but returns just one aggregated data point per tuple.

The request produces one of the following types of payload, depending on the value of the **Accept** request header:

* `application/json`
* `text/csv; header=present`âa CSV table with header row
* `text/csv; header=absent`âa CSV table without header row

If no **Accept** header is provided with the request, an `application/json` payload is returned.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/query` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/query` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricSelector | string | Selects metrics for the query by their keys. You can select up to 10 metrics for one query.  You can specify multiple metric keys separated by commas (for example, `metrickey1,metrickey2`). To select multiple metrics belonging to the same parent, list the last part of the required metric keys in parentheses, separated by commas, while keeping the common part untouched. For example, to list the `builtin:host.cpu.idle` and `builtin:host.cpu.user` metric, write: `builtin:host.cpu.(idle,user)`.  If the metric key contains any symbols you must quote (`"`) the key. The following characters inside of a quoted metric key must be escaped with a tilde (`~`):  * Quotes (`"`) * Tildes (`~`)  For example, to query the metric with the key of **ext:selfmonitoring.jmx.Agents: Type "APACHE"** you must specify this selector:  `"ext:selfmonitoring.jmx.Agents: Type ~"APACHE~""`  You can set additional transformation operators, separated by a colon (`:`). See [Metrics selector transformationsï»¿](https://dt-url.net/metricSelector) in Dynatrace Documentation for additional information on available result transformations and syntax. | query | Optional |
| resolution | string | The desired resolution of data points.  You can use one of the following options:  * The desired amount of data points. This is the default option. This is a reference number of points, which is not necessarily equal to the number of the returned data points. * The desired timespan between data points. This is a reference timespan, which is not necessarily equal to the returned timespan. To use this option, specify the unit of the timespan.  Valid units for the timespan are:  * `m`: minutes * `h`: hours * `d`: days * `w`: weeks * `M`: months * `q`: quarters * `y`: years  If not set, the default is **120 data points**.  For example:  * Get data points which are 10 minutes apart: `resolution=10m` * Get data points which are 3 weeks apart: `resolution=3w`  You can also specify **multiple resolutions** for a single query using index-based formatting. This allows each metric expression in a multi-expression selector to have its own resolution.  Use the format: `<index>:<resolution>(,<index>:<resolution>)*` Where:  * `index` is the zero-based position of the metric expression in the `metricSelector` list. * `resolution` is either a number of data points (e.g., `120`) or a timespan with a unit (e.g., `10m`, `3w`).  If a resolution is not specified for a given index, the default of **120 data points** is applied.  **Examples:**  * `resolution=0:Inf` â First metric uses resolution `Inf`, second metric uses default (120 data points). * `resolution=0:Inf,1:10` â First metric uses `Inf`, second metric uses `10` data points. * `resolution=Inf` â All metrics use resolution `Inf`.   **Note:** If multiple resolutions are used, the resolution field in the response is the smallest resolution. | query | Optional |
| from | string | The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the relative timeframe of two hours is used (`now-2h`). | query | Optional |
| to | string | The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| entitySelector | string | Specifies the entity scope of the query. Only data points delivered by matched entities are included in response.  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity typeï»¿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selectorï»¿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters.  Use the [`GET /metrics/{metricId}`ï»¿](https://dt-url.net/6z23ifk) call to fetch the list of possible entity types for your metric.  To set a universal scope matching all entities, omit this parameter. | query | Optional |
| mzSelector | string | The management zone scope of the query. Only metrics data relating to the specified management zones are included to the response.  You can set one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used. If several values are specified, the **OR** logic applies.  * `mzId(123,456)` * `mzName("name-1","name-2")`   To set several criteria, separate them with a comma (`,`). For example, `mzName("name-1","name-2"),mzId(1234)`. Only results matching **all** of the criteria are included in the response.For example, to list metrics that have the id **123** OR **234** AND the name **name-1** OR **name-2**, use this **mzSelector**: `mzId(123,234),mzName("name-1","name-2"). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MetricData](#openapi-definition-MetricData) | Success |
| **400** | - | Syntax or validation error. From and to parameters, entitySelector or resolution are incorrect individually or in their combined meaning. |
| **404** | - | A metric has not been found. |
| **406** | - | Not acceptable. The requested media type is not supported. Check the **Accept** header of your request. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `MetricData` object

A list of metrics and their data points.

| Element | Type | Description |
| --- | --- | --- |
| nextPageKey | string | Deprecated. This field is returned for compatibility reasons. It always has the value of `null`. |
| resolution | string | The timeslot resolution in the result. |
| result | [MetricSeriesCollection[]](#openapi-definition-MetricSeriesCollection) | A list of metrics and their data points. |
| totalCount | integer | The total number of primary entities in the result.  Has the `0` value if none of the requested metrics is suitable for pagination. |
| warnings | string[] | A list of warnings |

#### The `MetricSeriesCollection` object

Data points of a metric.

| Element | Type | Description |
| --- | --- | --- |
| appliedOptionalFilters | [AppliedFilter[]](#openapi-definition-AppliedFilter) | A list of filtered metric keys along with filters that have been applied to these keys, from the `optionalFilter` parameter. |
| data | [MetricSeries[]](#openapi-definition-MetricSeries) | Data points of the metric. |
| dataPointCountRatio | number | The ratio of queried data points divided by the maximum number of data points per metric that are allowed in a single query. |
| dimensionCountRatio | number | The ratio of queried dimension tuples divided by the maximum number of dimension tuples allowed in a single query. |
| dql | [MetricQueryDQLTranslation](#openapi-definition-MetricQueryDQLTranslation) | Metric query translation to DQL. |
| metricId | string | The key of the metric.  If any transformation is applied, it is included here. |
| warnings | string[] | A list of potential warnings that affect this ID. For example deprecated feature usage etc. |

#### The `AppliedFilter` object

Optional filters that took effect.

| Element | Type | Description |
| --- | --- | --- |
| appliedTo | string[] | The keys of all metrics that this filter has been applied to.  Can contain multiple metrics for complex expressions and always at least one key. |
| filter | [Filter](#openapi-definition-Filter) | A dimensional or series filter on a metric. |

#### The `Filter` object

A dimensional or series filter on a metric.

| Element | Type | Description |
| --- | --- | --- |
| operands | [Filter[]](#openapi-definition-Filter) | If the type is `not`, `and` or `or`, then holds the contained filters. |
| referenceInvocation | [Invocation](#openapi-definition-Invocation) | Invocation of a function, e.g. the `entitySelector` function. |
| referenceString | string | For filters that match a dimension against a valkue, such as `eq` or `ne`, holds the value to compare the dimension against. |
| referenceValue | number | For the operands of `series` filters that match against a number, holds the number to compare against. |
| rollup | [Rollup](#openapi-definition-Rollup) | A way of viewing a series as a single value for the purpose of sorting or series-based filters. |
| targetDimension | string | If the type applies to a dimension, then holds the target dimension. |
| targetDimensions | string[] | If the type applies to n dimensions, then holds the target dimensions. Currently only used for the `remainder` filter. |
| type | string | Type of this filter, determines which other fields are present.Can be any of:  * `eq`, * `ne`, * `prefix`, * `in`, * `remainder`, * `suffix`, * `contains`, * `existsKey`, * `series`, * `or`, * `and`, * `not`, * `ge`, * `gt`, * `le`, * `lt`, * `otherwise`. The element can hold these values * `and` * `contains` * `eq` * `existsKey` * `ge` * `gt` * `in` * `le` * `lt` * `ne` * `not` * `or` * `otherwise` * `prefix` * `remainder` * `series` * `suffix` |

#### The `Invocation` object

Invocation of a function, e.g. the `entitySelector` function.

| Element | Type | Description |
| --- | --- | --- |
| args | string[] | Arguments to pass to the function, e.g. entity selector source code. |
| function | string | Function that is invoked, e.g. `entitySelector`. |

#### The `Rollup` object

A way of viewing a series as a single value for the purpose of sorting or series-based filters.

| Element | Type | Description |
| --- | --- | --- |
| parameter | number | - |
| type | string | -The element can hold these values * `AUTO` * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` * `VALUE` |

#### The `MetricSeries` object

Data points per dimension of a metric.

The data is represented by two arrays of the same length: **timestamps** and **values**. Entries of the same index from both arrays form a timestamped data point.

| Element | Type | Description |
| --- | --- | --- |
| dimensionMap | object | - |
| dimensions | string[] | Deprecated, refer to `dimensionMap` instead.  The ordered list of dimensions to which the data point list belongs.  Each metric can have a certain number of dimensions. Dimensions exceeding this number are aggregated into one, which is shown as `null` here. |
| timestamps | integer[] | A list of timestamps of data points.  The value of data point for each time from this array is located in **values** array at the same index. |
| values | number[] | A list of values of data points.  The timestamp of data point for each value from this array is located in **timestamps** array at the same index. |

#### The `MetricQueryDQLTranslation` object

Metric query translation to DQL.

| Element | Type | Description |
| --- | --- | --- |
| message | string | Error message - only present if the status is `not supported` |
| query | string | The DQL query corresponding to the metric query |
| status | string | The status of the DQL translation, either `success` or `not supported` The element can hold these values * `not supported` * `success` |

### Response body JSON models

```
{



"nextPageKey": "null",



"resolution": "1h",



"result": [



{



"data": [



{



"dimensionMap": {



"dt.entity.disk": "DISK-F1266E1D0AAC2C3F",



"dt.entity.host": "HOST-F1266E1D0AAC2C3C"



},



"dimensions": [



"HOST-F1266E1D0AAC2C3C",



"DISK-F1266E1D0AAC2C3F"



],



"timestamps": [



3151435100000,



3151438700000,



3151442300000



],



"values": [



11.1,



22.2,



33.3



]



},



{



"dimensions": [



"HOST-F1266E1D0AAC2C3C",



"DISK-F1266E1D0AAC2C3D"



],



"timestamps": [



3151435100000,



3151438700000,



3151442300000



],



"values": [



111.1,



222.2,



333.3



]



}



],



"dataPointCountRatio": "0.1211",



"dimensionCountRatio": "0.0322",



"metricId": "builtin:host.disk.avail"



},



{



"data": [],



"metricId": "builtin:host.cpu.idle:filter(eq(\"dt.entityhost\",HOST-123))",



"warnings": [



"The dimension key `dt.entityhost` has been referenced, but the metric has no such key."



]



}



],



"totalCount": 3,



"warnings": [



"The dimension key `dt.entityhost` has been referenced, but the metric has no such key."



]



}
```

## Timeframe note

Dynatrace stores data in time slots. The **MetricValue** object shows the *ending* timestamp of the slot. If the time, set in the **from** or **to** parameters of your query, falls within the data time slot, this time slot is included in the response.

If the timestamp of the last data slot lays outside of the specified timeframe, the last data point of the response has a *later* timestamp than the specified in **to** query parameter.

Dynatrace does not predict future data. The timestamp of the last data point may lay in the future, due to data slots principle, described above. In this case, this data slot has incomplete data.

![Timeslot scheme](https://dt-cdn.net/images/timestamp-scheme-v2-488-0b302cef3b.png)

## Examples

In these examples, the requests query the data points of the **builtin:host.cpu.usage** and **builtin:host.cpu.idle** metrics.

The timeframe is set to **last 5 minutes**. To achieve that, the **from** query parameter is set to `now-5m`.

Only data from these two hosts (**HOST-0990886B7D39FE29** and **HOST-0956C3557E9109C1**) is included in the response. To achieve this, the **entitySelector** query parameter is set to `type("dt.entity.host"),entityId("HOST-0990886B7D39FE29")`.

Because host is a dimension of the queried metrics, you can achieve the same filtering by applying the [`:filter` transformation](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Configure the metric selector for the Metric v2 API.") to the metrics themselves by setting the **metricSelector** query parameter to `builtin:host.cpu.(usage,idle):filter(or(eq("dt.entity.host","HOST-0990886B7D39FE29"),eq("dt.entity.host","HOST-0956C3557E9109C1")))` and omitting **entitySelector** as redundant.

The difference between the queries is the representation of dataâthe first shows the list of data points, while the second shows just one aggregated data point for each series (the `:fold` transformation is applied at the end).

The API token is passed in the **Authorization** header.

The response is in `application/json` format.

List of data points

Aggregated data point

#### Curl

With untransformed metrics and **entitySelector** filter:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle)&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

With transformation applied directly to the metrics:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22)))&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Request URL

With untransformed metrics and **entitySelector** filter:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle)&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m
```

With transformation applied directly to the metrics:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22)))&from=now-5m
```

#### Response body

The result is truncated to three data points per dimension.

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:host.cpu.idle",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



81.0,



81.0,



79.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



81.0,



79.0,



78.0



]



}



]



},



{



"metricId": "builtin:host.cpu.usage",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



19.0,



19.0,



21.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589456100000,



1589456160000,



1589456220000



],



"values": [



19.0,



21.0,



22.0



]



}



]



}



]



}
```

The CSV table with header row looks like this. To obtain it, change the **Accept** header to `text/csv; header=present`.

```
metricId,dt.entity.host,time,value



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:35:00,19.0



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:36:00,19.0



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:37:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:35:00,19.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:36:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:37:00,22.0
```

#### Response code

200

#### Curl

With untransformed metrics and **entitySelector** filter:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):fold&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

With transformation applied directly to the metrics:

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22))):fold&from=now-5m' \



-H 'Authorization: Api-Token abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Request URL

With untransformed metrics and **entitySelector** filter:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):fold&entitySelector=type(%22dt.entity.host%22),entityId(%22HOST-0990886B7D39FE29%22,%22HOST-0956C3557E9109C1%22)&from=now-5m
```

With transformation applied directly to the metrics:

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/query?metricSelector=builtin:host.cpu.(usage,idle):filter(or(eq(%22dt.entity.host%22,%22HOST-0990886B7D39FE29%22),eq(%22dt.entity.host%22,%22HOST-0956C3557E9109C1%22))):fold&from=now-5m
```

#### Response body

```
{



"totalCount": 2,



"nextPageKey": null,



"resolution": "1m",



"result": [



{



"metricId": "builtin:host.cpu.idle:fold",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589455320000



],



"values": [



79.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589455320000



],



"values": [



78.0



]



}



]



},



{



"metricId": "builtin:host.cpu.usage:fold",



"dataPointCountRatio": 1.8E-5,



"dimensionCountRatio": 3.0E-5,



"data": [



{



"dimensions": [



"HOST-0990886B7D39FE29"



],



"dimensionMap": {



"dt.entity.host": "HOST-0990886B7D39FE29"



},



"timestamps": [



1589455320000



],



"values": [



21.0



]



},



{



"dimensions": [



"HOST-0956C3557E9109C1"



],



"dimensionMap": {



"dt.entity.host": "HOST-0956C3557E9109C1"



},



"timestamps": [



1589455320000



],



"values": [



22.0



]



}



]



}



]



}
```

The CSV table with header row looks like this. To obtain it, change the **Accept** header to `text/csv; header=present`.

```
metricId,dt.entity.host,time,value



builtin:host.cpu.usage,HOST-0956C3557E9109C1,2020-05-14 11:22:00,21.0



builtin:host.cpu.usage,HOST-0990886B7D39FE29,2020-05-14 11:22:00,22.00
```

#### Response code

200
