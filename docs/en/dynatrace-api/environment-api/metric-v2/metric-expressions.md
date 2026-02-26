---
title: Metrics API - Metric expressions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-expressions
scraped: 2026-02-26T21:22:50.421665
---

# Metrics API - Metric expressions

# Metrics API - Metric expressions

* Reference
* Updated on Jul 29, 2022

Metric expressions enable you to use simple arithmetic operations right in the metric selector.

For example, this expression calculates the ratio (as a percentage) of two metrics:

```
metric1 / metric2 * 100
```

For the operands of the expression, you can use metrics or numbers.

* You need to use brackets to enforce order of operations.
* All metrics with more than 1 data point involved in a metric expression must be of the same resolution.
* You can use any metric as an operand, including metrics modified by any [transformation chain](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."), and you can apply transformations to the result of the expression.

## Limitations

* The selector must contain at least one metric key.
* You can query data points of up to 10 metrics in one query.

For the purposes of this limit, one expression (for example, `metric2 + metric2`) counts as one metric.

## Precedence

Standard mathematical precedence rules applies:

1. Parentheses, metric transformations
2. Negation
3. Multiplication, division
4. Addition, subtraction

## Aggregation

If an aggregation has been applied in a transformation chain, this aggregation is used. If no transformation has been applied, the default aggregation is used. Your metric operands can be of different aggregations. For example, `metric:max - metric:min`.

## Resolving expressions

Metric expressions are resolved as follows:

1. [Form tuple pairs](#tuples) for each pair of metrics.
2. [Align data points](#data) in every tuple.
3. Apply arithmetic operation to aligned data points.

### Tuples

Arithmetic operations use the data points of tuples (unique combinations of metricâdimensionâdimension value) of metrics. Identical tuples of each metric are paired and then their data points are aligned.

If one metric is dimensionless (has just one tuple without dimensions and dimension values), then this single tuple is paired with every tuple of other metrics. The same applies to numbers.

Non-pairable tuples are ignored by the expression and are not presented in the result.

### Data points

Once tuple pairs are formed, the data points are aligned, and then the desired arithmetical operation is applied to the aligned data points.

* If any of the aligned data points is `null`, the expression resolves to `null`.
* If a number is involved in the operation, it is aligned with every data point of the metric operand.
* If one metric is a single data point and the other is a series, the single data point is aligned with every data point of the series.
* If both metrics are a single data point, the data points are aligned and the resulting time slot covers both data points.
* If both metrics are series, the data points are aligned by timestamps.

For any unaligned data points, the expression resolves to `null`.

## Best practices

### Use only when necessary

Use a metric expression only if you cannot accomplish your goal without it. Let's say you want to calculate the average CPU usage of two hosts, `HOST-001` and `HOST-002`. You could do it with a metric expression:

```
(



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-001")):splitBy()



+



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-002")):splitBy()



)



/2
```

There are two problems with this approach. First, the expression is hard to read and therefore prone to syntax errors. Second, if one of the hosts is offline, the result of the expression is empty. Even though the second problem could be solved by a **default** transformation, usage of the [average aggregation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Configure the metric selector for the Metric v2 API.") is more effective:

```
builtin:host.cpu.usage



:filter(



or(



eq("dt.entity.host","HOST-001"),



eq("dt.entity.host","HOST-002")



)



)



:splitBy()



:avg
```

### Do not convert units

Do not use a metric expression to convert the unit of the data. Use the [**toUnit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#to-unit "Configure the metric selector for the Metric v2 API.") instead. The only exception to this rule is for units that Dynatrace does not support. Use the [GET all units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "List all metrics that are available for your monitoring environment via the Dynatrace API.") request to fetch the list of supported units.

### Limit transformation usage

Always apply the [**limit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit-transformation "Configure the metric selector for the Metric v2 API.") to the result of a calculation, not to its operands.

Consider the following query, which attempts to add top-10 CPU usage times to top-10 CPU idle times.

```
builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



+



builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
```

If you have a large environment with hundreds of hosts, it is unlikely that the 10 hosts with the highest CPU usage are among the 10 hosts with the highest CPU idle time. The operands won't have matching tuples, therefore the result of the expression will be empty. The solution is to apply the limit to the result of the expression instead:

```
(



builtin:host.cpu.usage



+



builtin:host.cpu.idle



)



:sort(value(auto,descending))



:limit(10)
```

### Cover data gaps with the default transformation

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is particularly valuable for metric expressions. Even though normally the transformation doesn't fill up `null` data points if a metric doesn't have a single data point in the query timeframe, in the metric expression context its semantic is slightly different. As long as a metric on either side of the expression has at least one data point, the transformation will fill the gaps. However, if all metrics in the expression are missing data, the transformation will return empty results.

Consider this example of a ratio expression, where we calculate the error ratio for key user actions:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os



/



builtin:apps.other.keyUserActions.requestCount.os
```

If there are many requests but not a single error in your timeframe, the result will be empty, though an error ratio of `0` would be more meaningful. You can achieve that with the `default(0)` transformation:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



/



builtin:apps.other.keyUserActions.requestCount.os
```

## Examples

Example 1. Build a ratio metric

With a metric expression, you can build your own ratio metrics. Suppose we start with the following metrics:

* **builtin:service.errors.total.count** shows the number of errors of any type in a service
* **builtin:service.errors.server.successCount** shows the number of calls without server-side errors

From them, we can build an error ratio metric:

```
builtin:service.errors.total.count:value:default(0)



/



(



builtin:service.errors.total.successCount:value:default(0)



+



builtin:service.errors.total.count:value:default(0)



)
```

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is used to replace the values of the time slots that have the value `null` with 0.

Metric 1

Metric 2

Result

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1096, 1124, 1095]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.successCount",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [46182, 77110, 76736]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0, 0, 0]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count/(builtin:service.errors.total.count+builtin:service.errors.total.successCount)",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.513592079625046, 0.513172930621934, 0.5128924549621035]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1, 1, 1]



}



]



}



]



}
```

Example 2. Contribution of a single service to total error count

The **builtin:service.errors.total.count** metric shows the number of errors across your services. The list might be lengthy, and you might be interested in each service's contribution to the error count. A combination of metric transformations and metric expressions can provide this information.

You need these transformations:

* [filter transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Configure the metric selector for the Metric v2 API.") to obtain the error count for the service that you're checking.
* [split by transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Configure the metric selector for the Metric v2 API.") to merge individual error counts of each service into one.

Then use this expression:

```
builtin:service.errors.total.count:filter(eq("dt.entity.service","SERVICE-B82BFBCB4E264A98")):value:default(0)



/



builtin:service.errors.total.count:splitBy():value:default(0) * 100
```

The [**default** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Configure the metric selector for the Metric v2 API.") is used to replace the values of the time slots that have the value `null` with 0.

Isolated service

Total count

Percentage

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:splitBy()",



"data": [



{



"dimensions": [],



"dimensionMap": {},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [49882, 82425, 81911]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))/builtin:service.errors.total.count:splitBy()*100",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [97.75670582574877, 98.61449802851077, 98.64120814054277]



}



]



}



]



}
```

Example 3. Average GC duration

The **builtin:tech.jvm.memory.gc.collectionTime** metric shows the total duration of all garbage collections in a time slot. Information about individual GC times is not available, but we can use the **builtin:tech.jvm.memory.pool.collectionCount** metric showing the number of GCs per time to obtain the average duration of a garbage collection.

Before we start the calculation, we need to align the dimensions of both metrics. To do that, we need to apply the **split by** transformation with the `dt.entity.process_group_instance` argument to the **builtin:tech.jvm.memory.pool.collectionCount** metric.

Additionally, we can sort the result in descending order by applying the [sort transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Configure the metric selector for the Metric v2 API."). The expression looks like this:

```
(



builtin:tech.jvm.memory.gc.collectionTime



/



builtin:tech.jvm.memory.pool.collectionCount:splitBy("dt.entity.process_group_instance")



):sort(value(max,descending))
```

Total GC time

Number of GCs

Average GC duration

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.gc.collectionTime",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [164670, 171630, 163044]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [6883411, 5977311, 6356225]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [163368, 162924, 170502]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1727814, 1720686, 1691604]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [31363, 30588, 31419.5]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1697262, 1703742, 1722612]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "(builtin:tech.jvm.memory.gc.collectionTime/builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")):sort(value(max,descending))",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [219.47552848898383, 195.41359356610437, 202.3019144162065]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09530539745597616, 0.09974510166294141, 0.09638426014599162]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09625384884596486, 0.09562715481569392, 0.09897876016189368]



}



]



}



]



}
```

For more examples, see the ['Metric Expressions by Example' Github pageï»¿](https://dt-url.net/metric-expressions-by-example).

## Introductory video

Note that the syntax used in this video is based on the old syntax, which required parentheses around each metric and number of an expression.

Metric Expressions