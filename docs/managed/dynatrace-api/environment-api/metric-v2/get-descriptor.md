---
title: Metrics API - GET metric descriptor
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-descriptor
scraped: 2026-05-12T11:27:55.353829
---

# Metrics API - GET metric descriptor

# Metrics API - GET metric descriptor

* Reference
* Published Jun 14, 2019

Gets the parameters of the specified metric.

The request produces one of the following types of payload, depending on the value of the **Accept** request header:

* `application/json`
* `text/csv; header=present`âa CSV table with header row
* `text/csv; header=absent`âa CSV table without header row

If no **Accept** header is provided with the request, an `application/json` payload is returned.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/{metricKey}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/{metricKey}` |

## Authentication

To execute this request, you need an access token with `metrics.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| metricKey | string | The key of the required metric.  You can set additional transformation operators, separated by a colon (`:`). See [Metrics selector transformationsï»¿](https://dt-url.net/metricSelector) in Dynatrace Documentation for additional information on available result transformations and syntax. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MetricDescriptor](#openapi-definition-MetricDescriptor) | Success |
| **404** | - | A metric has not been found. |
| **406** | - | Not acceptable. The requested media type is not supported. Check the **Accept** header of your request. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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



"dimensionCardinalities": [



{



"estimate": 20,



"key": "dt.entity.host",



"relative": 0.2



}



],



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



"latency": 1,



"metricId": "builtin:host.cpu.user:splitBy(\"dt.entity.host\"):max:fold",



"metricValueType": {



"type": "unknown"



},



"scalar": false,



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
```

## Example

In this example, the request queries the parameters of three metrics: **builtin:host.cpu.idle**, **builtin:host.cpu.usage**, and **builtin:host.disk.avail**.

The **builtin:host.cpu.idle** and **builtin:host.cpu.usage** metrics have the same parent and their selector is combined into **builtin:host.cpu.(idle,usage)**.

The response is in `application/json` format.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/builtin:host.disk.avail' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/builtin:host.disk.avail
```

#### Response body

```
{



"metricId": "builtin:host.disk.avail",



"displayName": "Disk available",



"description": "",



"unit": "Byte",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



},



{



"key": "dt.entity.disk",



"name": "Disk",



"index": 1,



"type": "ENTITY"



}



]



}
```

The CSV table with header row looks like this. To obtain it, change the **Accept** header to `text/csv; header=present`.

```
metricId,displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions



builtin:host.cpu.usage,CPU usage %,Percentage of CPU time currently utilized.,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]
```

#### Response code

200