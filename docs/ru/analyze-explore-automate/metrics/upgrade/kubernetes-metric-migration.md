---
title: Kubernetes metrics migration guide
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/kubernetes-metric-migration
scraped: 2026-02-24T21:23:45.697069
---

# Kubernetes metrics migration guide

# Kubernetes metrics migration guide

* Latest Dynatrace
* 5-min read
* Updated on Jun 24, 2025

This guide provides insights into migrating Kubernetes metrics to Grail. Typically, a Grail metric is equivalent to a Metrics Classic metric. In some cases, however, there's no one-to-one relation:

* Convergent: a single Grail metric represents multiple Metrics Classic metrics of a similar scope or an increased level of detail.
* Replacement: a different Grail metric represents the Metrics Classic metric.
* Divergent/Calculated: the Classic metric is not represented 1:1 as Grail metric but can be calculated from other Grail metrics

## Identity

Classic Metrics and Grail Metrics have the same level of detail and dimensions available. The only difference is the metric key.

## Convergent metrics

The following metrics have been consolidated. The Grail metrics that supersede the Classic metrics offer an increased level of detail compared to the Classic metrics.

To achieve this decreased level of detail, the Grail metrics are first aggregated to the granularity of the Classic metric. From there the same set of filters can be applied and the output between Classic metrics and Grail metrics is identical.

The following list of metrics contains the pod and container count metrics and the Kubernetes event count metric that was available at a lower level of detail as Classic metric.

Kubernetes events and container/pod count metrics

The following table contains the workload and node resource metrics that have been available as separate workload- and node- level Classic metrics.
With Grail, there is a single metric at the container level.

**Example:** The following DQL query returns the amount of memory consumed on the workload level based on aggregated container-level data.

```
timeseries memory_working_set = sum(dt.kubernetes.container.memory_working_set)



by: {



k8s.cluster.name,



k8s.namespace.name,



k8s.workload.name



}
```

Workload- and node- level resource consumption metrics

## Replaced metrics

This group of metrics consists of Classic metric keys that have never been made available as Grail metrics.
Instead the most similar Classic metric is used to then determine the Grail metric replacement for these deprecated metrics.
The reason for the deprecation is a cleanup of duplicate metric keys. In the case of the following metrics, a complete identity of the values between the Classic Metric and Grail Metric is not feasible, but they are closely related and do not deviate very much.

## Calculated metrics

The following set of Classic container metrics is superseded by Grail container metrics.
For most of the CPU metrics in this section the Classic metrics have the unit millicores, while the Grail metrics have the unit nanoseconds/minute. To get
to the same values, the Grail metric needs to be divided by the number of nanoseconds in a minute.
(The number of nanoseconds per minute is 60 \* 1000 \* 1000 \* 1000)

This is the case for the following Grail metrics.

builtin:containers.cpu.throttledMilliCores

```
timeseries {



throttled_time = avg(dt.containers.cpu.throttled_time, rollup: sum, rate: 1m)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



throttled_milli_cores = throttled_time[] * milli_core_per_core / ns_per_min



| summarize {



throttled_milli_cores = sum(throttled_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageUserMilliCores

```
timeseries { usage_user_time = avg(dt.containers.cpu.usage_user_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_user_milli_cores = usage_user_time[] * milli_core_per_core / ns_per_min



| summarize { usage_user_milli_cores = sum(usage_user_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageSystemMilliCores

```
timeseries {



usage_system_time = avg(dt.containers.cpu.usage_system_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_system_milli_cores = usage_system_time[] * milli_core_per_core / ns_per_min



| summarize {



usage_system_milli_cores = sum(usage_system_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usageMilliCores

```
timeseries {



usage_user_time = avg(dt.containers.cpu.usage_user_time)



, usage_system_time = avg(dt.containers.cpu.usage_system_time)



}



| fieldsAdd



ns_per_min = 60 * 1000 * 1000 * 1000



, milli_core_per_core = 1000



| fieldsAdd



usage_milli_cores = (usage_user_time[] + usage_system_time[] )



* milli_core_per_core / ns_per_min



| summarize {



usage_milli_cores = sum(usage_milli_cores[] )



}, by: { timeframe, interval }
```

builtin:containers.cpu.usagePercent

```
timeseries {



// for total usage, user and system cpu usage are added



userCpuUsage = avg(dt.containers.cpu.usage_user_time)



, systemCpuUsage = avg(dt.containers.cpu.usage_system_time)



// cpu logical counts are the fallback, if the throttling ratio doesn't exist



, cpuLogicalCount = avg(dt.containers.cpu.logical_cores)



}



// filter statement ...



// leftOuter join allows the throttling ratio to be null



| join [



timeseries {



throttlingRatio = avg(dt.containers.cpu.throttling_ratio)



// same filter statement as above ...



}



], on: { interval, timeframe}, fields: { throttlingRatio}, kind:leftOuter



| fieldsAdd



// sum of system and user cpu usage



numerator = userCpuUsage[] + systemCpuUsage[]



// throttling ratio, or as a fallback cpu logical count.



, denominator = coalesce(throttlingRatio, cpuLogicalCount)



, nanoseconds_per_minute  = 60 * 1000 * 1000 * 1000



| fields



interval, timeframe



, cpuUsagePercent = 100.0 * numerator[] / ( denominator[] * nanoseconds_per_minute)
```

builtin:containers.cpu.usageTime

```
timeseries {



usageUserTime = avg(dt.containers.cpu.usage_user_time)



, usageSystemTime = avg(dt.containers.cpu.usage_system_time)



}



, by: { dt.entity.container_group_instance},



| fields



interval, timeframe



, usageTime = usageSystemTime[] + usageUserTime[]
```

builtin:containers.memory.limitPercent

```
timeseries {



limit_bytes = avg(dt.containers.memory.limit_bytes),



physical_total_bytes = avg(dt.containers.memory.physical_total_bytes)



}



| fieldsAdd



limit_percent = (limit_bytes[] / physical_total_bytes[] ) * 100



| summarize {



limit_percent = sum(limit_percent[] )



}, by: { timeframe, interval }
```

builtin:containers.memory.usagePercent

```
timeseries {



memoryLimits = avg(dt.containers.memory.limit_bytes)



, totalPhysicalMemory = avg(dt.containers.memory.physical_total_bytes)



, residentSetBytes = avg(dt.containers.memory.resident_set_bytes)



}



, by: { dt.entity.container_group_instance}



| fieldsAdd



denominator = if (



arrayFirst(memoryLimits) > 0,



then: memoryLimits,



else: totalPhysicalMemory



)



| fields



dt.entity.container_group_instance



, interval, timeframe



, memoryUsagePercent = 100 * residentSetBytes[] / denominator[]
```

## Related topics

* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")