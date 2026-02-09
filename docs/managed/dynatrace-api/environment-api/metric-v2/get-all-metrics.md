---
title: "Metrics API - GET metrics"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics
updated: 2026-02-09
---

# Metrics API - GET metrics

# Metrics API - GET metrics

* Reference
* Published Jun 14, 2019

Lists all available metrics.

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces one of the following types of payload, depending on the value of the **Accept** request header:

* `application/json`
* `text/csv; header=present`âa CSV table with header row
* `text/csv; header=absent`âa CSV table without header row

If no **Accept** header is provided with the request, an `application/json` payload is returned.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of metric schemata in a single response payload.  The maximal allowed page size is 500.  If not set, 100 is used.  If a value higher than 500 is used, only 500 results per page are returned. | query | Optional |
| metricSelector | string | Selects metrics for the query by their keys.  You can specify multiple metric keys separated by commas (for example, `metrickey1,metrickey2`). To select multiple metrics belonging to the same parent, list the last part of the required metric keys in parentheses, separated by commas, while keeping the common part untouched. For example, to list the `builtin:host.cpu.idle` and `builtin:host.cpu.user` metric, write: `builtin:host.cpu.(idle,user)`.  You can select a full set of related metrics by using a trailing asterisk (`*`) wildcard. For example, `builtin:host.*` selects all host-based metrics and `builtin:*` selects all Dynatrace-provided metrics.  You can set additional transformation operators, separated by a colon (`:`). See [Metrics selector transformationsï»¿](https://dt-url.net/metricSelector) in Dynatrace Documentation for additional information on available result transformations and syntax.  Only `aggregation`, `merge`, `parents`, and `splitBy` transformations are supported by this endpoint.  If the metric key contains any symbols you must quote (`"`) the key. The following characters inside of a quoted metric key must be escaped with a tilde (`~`):  * Quotes (`"`) * Tildes (`~`)  For example, to query the metric with the key of **ext:selfmonitoring.jmx.Agents: Type "APACHE"** you must specify this selector:  `"ext:selfmonitoring.jmx.Agents: Type ~"APACHE~""`  To find metrics based on a search term, rather than metricId, use the **text** query parameter instead of this one. | query | Optional |
| text | string | Metric registry search term. Only show metrics that contain the term in their key, display name, or description. Use the `metricSelector` parameter instead of this one to select a complete metric hierarchy instead of doing a text-based search. | query | Optional |
| fields | string | Defines the list of metric properties included in the response.  `metricId` is **always** included in the result. The following additional properties are available:  * `displayName`: The name of the metric in the user interface. Enabled by default. * `description`: A short description of the metric. Enabled by default. * `unit`: The unit of the metric. Enabled by default. * `tags`: The tags of the metric.  * `dduBillable`: An indicator whether the usage of metric consumes [Davis data unitsï»¿](https://dt-url.net/ddu). Deprecated and always `false` for Dynatrace Platform Subscription. Superseded by `billable`. * `billable`: An indicator whether the usage of metric is billable.  * `created`: The timestamp (UTC milliseconds) when the metrics has been created. * `lastWritten`: The timestamp (UTC milliseconds) when metric data points have been written for the last time. * `aggregationTypes`: The list of allowed aggregations for the metric. Note that it may be different after a [transformationï»¿](https://dt-url.net/metricSelector) is applied. * `defaultAggregation`: The default aggregation of the metric. It is used when no aggregation is specified or the `:auto` transformation is set. * `dimensionDefinitions`: The fine metric division (for example, process group and process ID for some process-related metric). * `transformations`: A list of [transformationsï»¿](https://dt-url.net/metricSelector) that can be applied to the metric. * `entityType`: A list of entity types supported by the metric. * `minimumValue`: The minimum allowed value of the metric. * `maximumValue`: The maximum allowed value of the metric. * `rootCauseRelevant`: Whether (true or false) the metric is related to a root cause of a problem. A root-cause relevant metric represents a strong indicator for a faulty component. * `impactRelevant`: Whether (true or false) the metric is relevant to a problem's impact. An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed. * `metricValueType`: The type of the metric's value. You have these options: + `score`: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.   + `error`: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count. * `latency`: The latency of the metric, in minutes. The latency is the expected reporting delay (for example, caused by constraints of cloud vendors or other third-party data sources) between the observation of a metric data point and its availability in Dynatrace. The allowed value range is from `1` to `60` minutes. * `metricSelector`: The underlying metric selector used by a func: metric. * `scalar`: Indicates whether the metric expression resolves to a scalar (`true`) or to a series (`false`).   A scalar result always contains one data point. The amount of data points in a series result depends on the resolution you're using. * `resolutionInfSupported`: If `true`, resolution=Inf can be applied to the metric query.  To add properties, list them with leading plus `+`. To exclude default properties, list them with leading minus `-`.  To specify several properties, join them with a comma (for example `fields=+aggregationTypes,-description`).  If you specify just one property, the response contains the metric key and the specified property. To return metric keys only, specify `metricId` here. | query | Optional |
| writtenSince | string | Filters the resulted set of metrics to those that have data points within the specified timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years | query | Optional |
| writtenSinceMode | string | Controls how the writtenSince filter is applied.  * `INCLUDE`: Includes only metrics that have been written since the specified writtenSince timestamp (filters out metrics not written since then). * `EXCLUDE`: Excludes metrics that have been written since the specified writtenSince timestamp (only returns metrics not written since then).  If not specified, the default is `INCLUDE`. | query | Optional |
| metadataSelector | string | The metadata scope of the query. Only metrics with specified properties are included to the response.  You can set one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used. If several values are specified, the **OR** logic applies.  * `unit("unit-1","unit-2")` * `tags("tag-1","tag-2")` * `dimensionKey("dimkey-1","dimkey-2")`. The filtering applies only to dimensions that were written within the last 14 days. * `custom("true")`. "true" to include only user-defined metrics metrics (without namespace or with `ext:`, `calc:`, `func:`, `appmon:`), "false" to filter them out. * `exported("true")`. "true" to include only exported metrics, "false" to filter them out.  To set several criteria, separate them with a comma (`,`). For example, `tags("feature","cloud"),unit("Percent"),dimensionKey("location"),custom("true")`. Only results matching **all** criteria are included in response.  For example, to list metrics that have the tags **feature** AND **cloud** with a unit of **Percent** OR **MegaByte** AND a dimension with a dimension key **location**, use this **metadataSelector**: `tags("feature"),unit("Percent","MegaByte"),tags("cloud"),dimensionKey("location")`. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MetricDescriptorCollection](#openapi-definition-MetricDescriptorCollection) | Success |
| **400** | - | Syntax or validation error. **metricSelector** or **fields** have syntactic or semantic errors. |
| **404** | - | A metric has not been found. |
| **406** | - | Not acceptable. The requested media type is not supported. Check the **Accept** header of your request. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `MetricDescriptorCollection` object

A list of metrics along with their descriptors.

| Element | Type | Description |
| --- | --- | --- |
| metrics | [MetricDescriptor[]](#openapi-definition-MetricDescriptor) | A list of metric along with their descriptors |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| totalCount | integer | The estimated number of metrics in the result. |
| warnings | string[] | A list of potential warnings about the query. For example deprecated feature usage etc. |

#### The `MetricDescriptor` object

The descriptor of a metric.

| Element | Type | Description |
| --- | --- | --- |
| aggregationTypes | string[] | The list of allowed aggregations for this metric. The element can hold these values * `auto` * `avg` * `count` * `max` * `median` * `min` * `percentile` * `sum` * `value` |
| billable | boolean | If `true`the usage of metric is billable.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| created | integer | The timestamp of metric creation.  Built-in metrics and metric expressions have the value of `null`. |
| dduBillable | boolean | If `true` the usage of metric consumes [Davis data unitsï»¿](https://dt-url.net/ddu). Deprecated and always `false` for Dynatrace Platform Subscription. Superseded by `isBillable`.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| defaultAggregation | [MetricDefaultAggregation](#openapi-definition-MetricDefaultAggregation) | The default aggregation of a metric. |
| description | string | A short description of the metric. |
| dimensionCardinalities | [MetricDimensionCardinality[]](#openapi-definition-MetricDimensionCardinality) | The cardinalities of MINT metric dimensions. |
| dimensionDefinitions | [MetricDimensionDefinition[]](#openapi-definition-MetricDimensionDefinition) | The fine metric division (for example, process group and process ID for some process-related metric).  For [ingested metricsï»¿](https://dt-url.net/5d63ic1), dimensions that doesn't have have any data within the last 15 days are omitted. |
| displayName | string | The name of the metric in the user interface. |
| entityType | string[] | List of admissible primary entity types for this metric. Can be used for the `type` predicate in the `entitySelector`. |
| impactRelevant | boolean | The metric is (`true`) or is not (`false`) impact relevant.  An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| lastWritten | integer | The timestamp when the metric was last written.  Has the value of `null` for metric expressions or if the data has never been written. |
| latency | integer | The latency of the metric, in minutes.  The latency is the expected reporting delay (for example, caused by constraints of cloud vendors or other third-party data sources) between the observation of a metric data point and its availability in Dynatrace.  The allowed value range is from 1 to 60 minutes.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| maximumValue | number | The maximum allowed value of the metric.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| metricId | string | The fully qualified key of the metric.  If a transformation has been used it is reflected in the metric key. |
| metricSelector | string | The metric selector that is used when querying a func: metric. |
| metricValueType | [MetricValueType](#openapi-definition-MetricValueType) | The value type for the metric. |
| minimumValue | number | The minimum allowed value of the metric.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| resolutionInfSupported | boolean | If 'true', resolution=Inf can be applied to the metric query. |
| rootCauseRelevant | boolean | The metric is (`true`) or is not (`false`) root cause relevant.  A root-cause relevant metric represents a strong indicator for a faulty component.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| scalar | boolean | Indicates whether the metric expression resolves to a scalar (`true`) or to a series (`false`). A scalar result always contains one data point. The amount of data points in a series result depends on the resolution you're using. |
| tags | string[] | The tags applied to the metric.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. |
| transformations | string[] | Transform operators that could be appended to the current transformation list. The element can hold these values * `asGauge` * `default` * `delta` * `evaluateModel` * `filter` * `fold` * `histogram` * `last` * `lastReal` * `limit` * `merge` * `names` * `parents` * `partition` * `rate` * `rollup` * `setUnit` * `smooth` * `sort` * `splitBy` * `timeshift` * `toUnit` |
| unit | string | The unit of the metric. |
| unitDisplayFormat | string | The raw value is stored in bits or bytes. The user interface can display it in these numeral systems:  Binary: 1 MiB = 1024 KiB = 1,048,576 bytes  Decimal: 1 MB = 1000 kB = 1,000,000 bytes  If not set, the decimal system is used.  [Metric expressionsï»¿](https://dt-url.net/metricExpression) don't return this field. The element can hold these values * `binary` * `decimal` |
| warnings | string[] | A list of potential warnings that affect this ID. For example deprecated feature usage etc. |

#### The `MetricDefaultAggregation` object

The default aggregation of a metric.

| Element | Type | Description |
| --- | --- | --- |
| parameter | number | The percentile to be delivered. Valid values are between `0` and `100`.  Applicable only to the `percentile` aggregation type. |
| type | string | The type of default aggregation. The element can hold these values * `auto` * `avg` * `count` * `max` * `median` * `min` * `percentile` * `sum` * `value` |

#### The `MetricDimensionCardinality` object

The dimension cardinalities of a metric.

| Element | Type | Description |
| --- | --- | --- |
| estimate | integer | The cardinality estimate of the dimension. |
| key | string | The key of the dimension.  It must be unique within the metric. |
| relative | number | The relative cardinality of the dimension expressed as percentage |

#### The `MetricDimensionDefinition` object

The dimension of a metric.

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The display name of the dimension. |
| index | integer | The unique 0-based index of the dimension.  Appending transformations such as :names or :parents may change the indexes of dimensions. `null` is used for the dimensions of a metric with flexible dimensions, which can be referenced with their dimension key, but do not have an intrinsic order that could be used for the index. |
| key | string | The key of the dimension.  It must be unique within the metric. |
| name | string | The name of the dimension. |
| type | string | The type of the dimension. The element can hold these values * `ENTITY` * `NUMBER` * `OTHER` * `STRING` * `VOID` |

#### The `MetricValueType` object

The value type for the metric.

| Element | Type | Description |
| --- | --- | --- |
| type | string | The metric value type The element can hold these values * `error` * `score` * `unknown` |

### Response body JSON models

```
{



"metrics": [



{



"aggregationTypes": [



"auto",



"value"



],



"created": 1597400123451,



"dduBillable": false,



"defaultAggregation": {



"type": "value"



},



"description": "Percentage of user-space CPU time currently utilized, per host.",



"dimensionDefinitions": [



{



"displayName": "Host",



"index": 0,



"key": "dt.entity.host",



"name": "Host",



"type": "ENTITY"



}



],



"displayName": "CPU user",



"entityType": [



"HOST"



],



"lastWritten": 1597400717783,



"metricId": "builtin:host.cpu.user:splitBy(\"dt.entity.host\"):max:fold",



"metricValueType": {



"type": "unknown"



},



"tags": [],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"rate",



"sort",



"last",



"splitBy"



],



"unit": "Percent"



},



{



"aggregationTypes": [



"auto",



"value"



],



"created": 1597400123451,



"dduBillable": false,



"defaultAggregation": {



"type": "value"



},



"description": "Percentage of user-space CPU time currently utilized, per host.",



"dimensionDefinitions": [



{



"displayName": "Host",



"index": 0,



"key": "dt.entity.host",



"name": "Host",



"type": "ENTITY"



}



],



"displayName": "CPU user",



"entityType": [



"HOST"



],



"lastWritten": 1597400717783,



"metricId": "builtin:host.cpu.user:splitBy()",



"metricValueType": {



"type": "unknown"



},



"tags": [],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"rate",



"sort",



"last",



"splitBy"



],



"unit": "Percent"



}



],



"nextPageKey": "ABCDEFABCDEFABCDEF_",



"totalCount": 3



}
```

## Example

In this example, the request queries all built-in metrics (**metricSelector** is set to `builtin:*`) available in the **mySampleEnv** environment. The following fields are included in the response:

* metricId
* unit
* aggregationTypes

To achieve that, the **fields** query parameter is set to `unit,aggregationTypes`.

The API token is passed in the **Authorization** header.

The response is in `application/json` format and is truncated to four entries.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&metricSelector=builtin:*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&metricSelector=builtin:*
```

#### Response body

```
{



"totalCount": 1808,



"nextPageKey": "___a7acX3q0AAAAGAQAJYnVpbHRpbjoqAQA",



"metrics": [



{



"metricId": "builtin:host.cpu.idle",



"unit": "Percent",



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



]



},



{



"metricId": "builtin:host.cpu.load",



"unit": "Ratio",



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



]



},



{



"metricId": "builtin:service.errors.server.count",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:service.keyRequest.count.client",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



}



]



}
```

The CSV table with header row looks like this. To obtain it, change the **Accept** header to `text/csv; header=present`.

```
metricId,unit,aggregationTypes



builtin:host.cpu.idle,Percent,"[auto, avg, max, min]"



builtin:host.cpu.load,Ratio,"[auto, avg, max, min]"



builtin:service.errors.server.count,Count,"[auto, value]"



builtin:service.keyRequest.count.client,Count,"[auto, value]"
```

#### Response code

200
