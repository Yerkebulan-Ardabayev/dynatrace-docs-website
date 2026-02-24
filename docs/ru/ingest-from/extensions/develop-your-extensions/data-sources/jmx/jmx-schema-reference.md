---
title: JMX data source reference
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference
scraped: 2026-02-24T21:25:38.971601
---

# JMX data source reference

# JMX data source reference

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Sep 15, 2025

This is a general description of JMX data source-based extension YAML file and ways to declare metrics and dimensions you would like to collect using your extension.

## Metric values

The metric value can come from different sources.

The most common source is a numeric JMX MBean attribute:

```
metrics:



- key: com.example.somekey



value: attribute:ThreadCount
```

This will look for an attribute named `ThreadCount`. The returned value must be either numeric (any subclass of `java.lang.Number`, such as `Integer`, `Long`, `Double`) or a `boolean` (converted to `0` for `false` and `1` for `true`).

JMX allows defining attributes with complex-non numeric types. It is possible to extract a numeric value from such a non-numeric attribute value. This requires specifying which methods or fields should be accessed.

For example:

```
metrics:



- key: com.example.somekey



value:



attribute: SomeNonNumericAttribute



accessor: getSomeNumericValue()
```

See [accessor syntax](#accessor-syntax) below for a detailed syntax description.

A special case is to always use the same constant value instead of querying an attribute:

```
metrics:



- key: com.example.somekey



value: const:1
```

If the `query` matches a single MBean, this metric will always produce the value `1`. This can be used to report just the presence of a specific MBean. If the query matches multiple MBeans, this metric will produce a value corresponding to the number of matches MBeans.

## Custom dimensions

Every custom dimension consists of a constant `key` and a `value`. The value can come from different sources.

The simplest case is to set the dimension value to a constant string:

```
dimensions:



- key: k1



value: const:constant_value
```

This will produce a metric where dimension `k1` always has value `constant_value`.

MBean object name key property value can be used as a dimension value:

```
query: java.lang:type=GarbageCollector,name=*



dimensions:



- key: k1



value: property:name
```

This will produce a metric where dimension `k1` corresponds to the value of the key property `name`. For example, the MBean `java.lang:type=GarbageCollector,name=YoungGen`, will produce a metric where dimension `k1` has the value `YoungGen`.

If a process has 3 different garbage collectors, metrics with 3 different dimension values are produced and can be charted independently.

An MBean attribute can also be used as a dimension value.

```
query: java.lang:type=Compilation



dimensions:



- key: k1



value: attribute:Name
```

This will produce a metric where dimension `k1` corresponds to the value of attribute `Name`. Currently, only immutable attributes are supported. The attribute for a specific MBean is only queried once when an MBean is first discovered by OneAgent.

Similar to metric values, it is possible to extract the dimension value from a complex attribute using an accessor expression:

```
query: java.lang:type=Compilation



dimensions:



- key: k1



value:



attribute: SomeAttribute



accessor: getName()
```

This will look for an attribute called `SomeAttribute`, call `getName` on it and use the returned value as the value for dimension `k1`.

## Accessor syntax

| Accessor | Description |
| --- | --- |
| `getSomeNumericValue()` | Call a method called `getSomeNumericValue` with no parameters. |
| `getSomeNumericValue` | Parenthesis are optional methods without parameters. |
| `getA().getB()` | Call a method called `getA`, then on the return value of this call a method called `getB`. |
| `getA(1)` | Call a method called `getA` with integer argument `1`. |
| `getA("x")` | Call a method called `getA` with string argument `x`. |
| `getA(1, "x")` | Call a method called `getA` with two arguments. |
| `getA()[1]` | Call a method called `getA`, then from the return value extract value at index 1. |

## Extension variables

### Use extension variables to filter MBeans

Extension variables can be used to allow users of an extension to monitor only specific MBeans:

```
vars:



- id: gc_name_filter



displayName: Garbage Collector Name



type: text



jmx:



groups:



- group: jvm



subgroups:



- subgroup: basic



query: java.lang:type=GarbageCollector



queryFilters:



- field: name



filter: var:gc_name_filter



dimensions:



- key: k1



value: property:name



metrics:



- key: com.example.jmx.var



type: count



value: attribute:CollectionTime
```

This creates a variable called `gc_name_filter` internally and `Garbage Collector Name` in the UI. The variable value will be used to pick a specific MBean. E.g. if the variable value is `YoungGen` then the complete object name query will be `java.lang:type=GarbageCollector,name=YoungGen`

Every monitoring configuration can pick a specific value for this variable. To ensure that multiple monitoring configurations with different variable values are not mixed up in the UI, it is recommended to also add a dimension for the `name` property as demonstrated above.

### Use extension variables as dimension

Extension variables can also be used directly as the value of custom metric dimensions.

```
vars:



- id: my_variable



displayName: My Variable



type: text



jmx:



groups:



- group: jvm



subgroups:



- subgroup: variable as dimension value



query: "java.lang:type=Threading"



dimensions:



- key: my_dimension



value: var:my_variable



metrics:



- key: com.example.jmx-reference.var-dimension



type: gauge



value: attribute:ThreadCount
```

This references a variable `my_variable` and adds an additional dimension to the metric. The variable value will be used as content for the dimension. For example, if the value is `My Value`, the dimension added would be `my_dimension="My Value"`.

## Gauge value aggregation

In the example above, we retrieve the number of threads from a single MBean. But in some cases, a JMX query might return several matching beans. Collecting the results will provide us with too much information. Instead, it's more helpful to calculate the minimum, maximum, or average values to understand the range.

For that exact purpose, we provide `gauge_statcounter`, which works as a drop-in replacement for `gauge`. Unlike the regular `gauge`, which sums up the value, the `gauge_statcounter` includes distinct values such as:

* `min`: the minimum value of the metric
* `max`: the maximum value of the metric
* `sum`: the sum of metric scraping
* `count`: the number of scrape passes

Notice that average can be easily understood by dividing the sum by count.

```
- query: Catalina:type=Manager,host=*,context=*



dimensions:



- key: host



value: attribute:host



metrics:



- key: metric_activeSessions_1752841036351



value: attribute:activeSessions



type: gauge_statcounter
```