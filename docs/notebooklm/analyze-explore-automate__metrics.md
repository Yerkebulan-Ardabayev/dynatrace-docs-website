# Dynatrace Documentation: analyze-explore-automate/metrics

Generated: 2026-02-16

Files combined: 5

---


## Source: dql-examples.md


---
title: DQL timeseries examples
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/dql-examples
scraped: 2026-02-15T21:14:54.046424
---

# DQL timeseries examples

# DQL timeseries examples

* Latest Dynatrace
* 8-min read
* Updated on Oct 17, 2025

Metrics on Grail enable you to pinpoint and retrieve any metric data with the help of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). After reviewing the [fundamentals of DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide#metrics "Find out how DQL works and what are DQL key concepts.") and the [timeseries command](/docs/platform/grail/dynatrace-query-language/commands/metric-commands "DQL metric commands"), use the examples on this page to start getting answers from your metrics.

### Example 1: Average CPU usage across all hosts

In this example, you'll query the average CPU usage across all monitored hosts in your environment.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Observing the aggregate CPU usage across all hosts can help you visually confirm how your infrastructure responds to and recovers from usage spikes or slow, imperceptible growth trends over time.

```
timeseries usage=avg(dt.host.cpu.usage)
```

### Example 2: Average CPU usage by host, limit to top 3 hosts

In this example, you get every monitored host's average CPU usage and focus on the three hosts with the highest usage.

OneAgent collects CPU measurements from its host machine. These metrics are accessible through metric keys beginning with `dt.host.cpu`.

Charting individual hosts' CPU usage helps to visualize normal and outlier usage. By focusing on the three hosts with highest CPU usage, you can begin investigating under-provisioned applications. Likewise, focusing on hosts with the lowest CPU usage may reveal over-provisioning and lead to cost-saving opportunities.

1. Query the data.

   ```
   timeseries usage=avg(dt.host.cpu.usage), usage_summary=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage_summary desc



   | limit 3
   ```
2. Simplify results.

   A table can be easier to read than a line chart in some situations. Let's query data that works best with table output by focusing on the columns we most care about: `dt.entity.host` and `usage`.

   ```
   timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage desc



   | limit 3



   | fields dt.entity.host, dt.entity.host.name, usage
   ```

   This is essentially the same query as above, without the series.

### Example 3: Average CPU usage by host IP Address

In this example, you'll use an `in` condition to query hosts based on their IP address.

By using the `in` operator with `classicEntitySelector`, you can filter on `ipAddress` and other host attributes.

Using the timeseries `filter` parameter is more performant than chaining `timeseries` with the `filter` command.

```
timeseries usage=avg(dt.host.cpu.usage),



filter: {in(



dt.entity.host,



classicEntitySelector("type(host),ipAddress(\"10.102.39.126\")")



)}
```

### Example 4: Number of hosts sending CPU usage data

In this example, you'll learn how to chain `timeseries` with `summarize`. You'll first query hosts sending CPU usage data, and then count the number of hosts in the result.

Other DQL commands can also be chained with `timeseries` as demonstrated in previous examples, but unlike those examples, `summarize` further aggregates the dataset returned by `timeseries`. You'll find this two-step aggregation helpful as your questions become more complex and nuanced.

```
timeseries usage=avg(dt.host.cpu.usage), by:{dt.entity.host}



| summarize count()
```

### Example 5: Top hosts by bytes read with corresponding bytes written

In this example, you'll enrich a single result with context from another metric.

Even when focused on disk read operations, the corresponding disk writes can provide helpful context.

```
timeseries by:{dt.entity.host}, {



bytes_read=sum(dt.host.disk.bytes_read, scalar:true),



bytes_written=sum(dt.host.disk.bytes_written, scalar:true)



}



| sort bytes_read desc



| limit 3



| fields



dt.entity.host,



entityName(dt.entity.host),



bytes_read,



bytes_written
```

### Example 6: Available CPU by Kubernetes Node

In this example, you'll calculate the available CPU on all nodes of your hypothetical "openfeature" cluster.

To return a timeseries instead of a single value, we use the `[]` operator to take the difference of individual timeseries values. The result is another timeseries that you can visualize with a line chart.

The available CPU is integral for efficient resource utilization and avoiding resource contention. A timeseries visualized with a line chart is one way to show how the available CPU changes over time.

```
timeseries {



cpu_allocatable = min(dt.kubernetes.node.cpu_allocatable),



requests_cpu = max(dt.kubernetes.container.requests_cpu)



},



by:{dt.entity.kubernetes_cluster, dt.entity.kubernetes_node}



| fieldsAdd  // add friendly names



entityName(dt.entity.kubernetes_cluster),



entityName(dt.entity.kubernetes_node)



| fieldsAdd result = cpu_allocatable[] - requests_cpu[]



| fieldsRemove cpu_allocatable, requests_cpu
```

### Example 7: Average host CPU usage by host size

In this example, you'll learn how to use a [`entityAttr` command](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entity-attr "A list of DQL general functions.") to analyze host CPU usage by host size.

OneAgent collects local context from its host: information such as how many CPUs are installed and how much memory it has. You can add this information to your query with the `entityAttr` function.

Host-level information can sometimes be too fine-grained and difficult to interpret. In these situations, a well-chosen entity attribute can help you explore and analyze how individual hosts contribute to broader trends.

```
timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



| fieldsAdd cpuCores = entityAttr(dt.entity.host, "cpuCores")



| summarize by:{cpuCores}, avg(usage), count_hosts=count()
```

### Example 8: Query multiple CPU usage metrics with a single query

In this example, you'll learn how to use the [`append` command](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#append "DQL correlation and join commands") to return multiple CPU metrics with a single query.

Combining queries into one command can be useful for comparing measurements from different contexts, as they will be charted together.

As you query many metrics from a single host and perform no arithmetic, the `append` command here is preferred to querying multiple metrics with a single `timeseries` command. The `append` command is a comparatively more flexible option, as it doesn't require equivalent `by` or `filter` arguments, for example. Additionally, chaining `append` is more efficient from a DQL perspective.

```
timeseries idle=avg(dt.host.cpu.idle),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



| append [



timeseries system=avg(dt.host.cpu.system),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]



| append [



timeseries user=avg(dt.host.cpu.user),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]
```

### Example 9: Connection failure rate by host

In this example, you'll apply what you've learned from previous examples to calculate the failure rate and find hosts running processes with many failed connections.

This example uses the `default` parameter to control for the case where there are no failures. It inserts a `0` value anywhere data is missing.

Failure rate calculations are common and critical for monitoring service-level objectives. Spotting persistent or recurring high failure rates in testing environments could indicate a deployment problem before the application reaches production.

```
timeseries {



new = sum(dt.process.network.sessions.new),



reset = sum(dt.process.network.sessions.reset, default:0),



timeout = sum(dt.process.network.sessions.timeout, default:0)



},



by:{dt.entity.host}



| fieldsAdd result = 100 * (reset[] + timeout[]) / new[]



| filter arrayAvg(result) > 0



| sort arrayAvg(result) desc
```

### Example 10: Monitoring host availability

In this example you will monitor the availability of hosts and count those that are currently up.

You can use the timeseries command with the [`nonempty` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#expand--nonempty-parameter--1 "DQL metric commands") to calculate host availability. This parameter ensures that you get a result even when no data match the filterâsuch as when no hosts are up. This provides a more accurate representation of host availability.

```
timeseries availability = sum(dt.host.availability, default:0),



nonempty:true,



filter:{availability.state == "up"}
```

### Example 11: Readiness probe

In this example you'll query [log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.") to count successful and failed readiness probes by host.

You can use the [`union` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#union "DQL metric commands") to capture all hosts, including those with no failures or no successes.

```
timeseries



failure_count=sum(log.readiness_probe.failure_count, default:0),



success_count=sum(log.readiness_probe.success_count, default:0),



by:{dt.entity.host},



union:true
```

The `union:true` argument captures all hosts, even if they had no failures or no successes.

### Example 12: Failure rate

In this example, you will query the per-second failure rate for a specific endpoint ("/api/accounts"). By using the [`rate` parameter](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#rate "DQL metric commands"), you can normalize the timeseries data to a specific duration.

Monitoring request failure rates is crucial for understanding application performance, identifying bottlenecks, and ensuring optimal user experience.

Dynatrace shows the per-minute request count by default, as Dynatrace service metrics collect one-minute granularity request data.

```
timeseries sum(dt.service.request.failure_count, rate:1s),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Example 13: Capacity planning

In this example, you will query current host-disk availability and use the [`shift`](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#shift "DQL metric commands") parameter to compare it to usage 7 days ago.

Monitoring host-disk availability helps with capacity planning. If today's disk space usage is consistently higher than 7 days ago, it may signal the need for additional storage resources. Conversely, a decrease in usage might allow for resource optimization.

```
timeseries avail=avg(dt.host.disk.avail), by:{dt.entity.host}, from:-24h



| append [



timeseries avail.yesterday=avg(dt.host.disk.avail), by:{dt.entity.host}, shift:-168h



]



| filter startsWith(entityName(dt.entity.host), "prod-")
```

### Example 14: Verify host availability and redundance

In this example you'll use the [`count` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-count "DQL metric commands") to track the number of hosts monitored in each AZ of AWS region us-east-1.

Applications frequently deploy hosts across multiple availability zones (AZs) to ensure high availability. Counting hosts in each AZ helps verify that the distribution is balanced and, should one AZ experience network disruptions or other issues, the workload can fail over to another AZ.

```
timeseries num_hosts = count(dt.host.cpu.usage),



by:{aws.availability_zone},



filter:{startsWith(aws.availability_zone, "us-east-1")}
```

### Example 15: Performance optimization

In this example you'll use the [`percentile` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries-percentile "DQL metric commands") to track the 90th percentile response time of the contrived /api/accounts endpoint.

Tracking the service response time [percentilesï»¿](https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/) helps identify bottlenecks and areas for improvement. If a specific transaction consistently exceeds this threshold, you can decide if it warrants investigation and additional optimization.

```
timeseries p90 = percentile(dt.service.request.response_time, 90),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Example 16: Right-sizing deployments

In this example you'll use the [`if` function](/docs/platform/grail/dynatrace-query-language/functions/conditional-functions#if "A list of DQL conditional functions.") to label underused host-disk pairs.

Identifying overprovisioned deployments helps reduce operating costs. By removing overprovisioned infrastructure, you can determine the right size deployment for your application.

```
timeseries avail=avg(dt.host.disk.avail, scalar:true),



by:{dt.entity.disk, dt.entity.host},



filter:{startsWith(dt.entity.host, "my-app-")}



| fieldsAdd disk_usage=if(avail>450000000000, "underused", else: "optimal")



| limit 3
```

### Example 17: Split CPU usage by kubernetes annotations

In this example you'll split CPU usage by kubernetes annotation.

You can use kubernetes annotation `app.kubernetes.io/component` to evaluate the performance of your application components. Annotations are cloud application attributes and aren't typically ingested with a metric. You should split by the cloud application and look up the relevant annotation.

Many [`summarize` command functions](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") accept iterative expressions like `cpu_usage[]` to preserve the timeseries.

```
timeseries cpu_usage = sum(dt.kubernetes.container.cpu_usage, rollup:max),



by:{dt.entity.cloud_application}



| fieldsAdd annotations = entityAttr(dt.entity.cloud_application, "kubernetesAnnotations")



| fieldsAdd component = annotations[`app.kubernetes.io/component`]



| summarize cpu_usage = sum(cpu_usage[]),



by:{timeframe, interval, component}
```


---


## Source: histograms.md


---
title: Histogram metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/histograms
scraped: 2026-02-15T09:07:01.567875
---

# Histogram metrics

# Histogram metrics

* Latest Dynatrace
* Explanation
* 7-min read
* Published Jul 09, 2025

Histogram metrics are a powerful way to capture the distribution of values for a given measurement, such as response times, request sizes, or durations. Compared to a counter that measures the overall total in a single value, a histogram counts the number of occurrences at different thresholds (called buckets). It is a multi-value counter, aggregating data into buckets, allowing you to analyze percentiles, averages, and the overall shape of your data.

## Histogram metrics use cases

* Measure response time distributions for services or endpoints
* Track request or payload sizes
* Analyze latency or duration metrics in distributed systems

For a deeper dive into histograms and their advantages, see the following series of the OpenTelemetry blog posts:

* [Why histograms?ï»¿](https://opentelemetry.io/blog/2023/why-histograms/)
* [Histograms vs. summariesï»¿](https://opentelemetry.io/blog/2023/histograms-vs-summaries/)
* [Exponential histogramsï»¿](https://opentelemetry.io/blog/2023/exponential-histograms/)

## Ingest histogram metrics

No special configuration is needed to ingest histograms from OpenTelemetry (OTLP ingest API) or Prometheus sources (Dynatrace Operator). Histogram metrics are sent automatically when your environment receives OpenTelemetry or Kubernetes data.

The OpenTelemetry Exponential Histogram is not supported as a histogram: the histogram's `min|max|sum|count` are ingested but the buckets aren't.

If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.

* Cumulative histograms aren't ingested (similarly to cumulative counters).
* Histogram data points without `sum` aren't ingested. This happens when negative values are recorded.
* Histogram buckets are not sorted.
* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.

## Query percentiles using DQL

Dynatrace Query Language (DQL) allows you to analyze histogram metrics using the percentile aggregation. It calculates the requested percentile across all the buckets for each time slot.

For example:

```
timeseries percentile(http_request_duration_seconds_bucket, 99)
```

The query calculates the 99th percentile of values based on the ingested histogram buckets.

Histograms represent data as a series of buckets, each containing the count of values that fall within a specific range. For example, `http_request_duration_seconds_bucket` contains counts of request durations grouped by predefined ranges (`le` dimension).

The `percentile` function uses the bucket data to estimate the requested percentile (for example, the 99th percentile). It interpolates the value at which 99% of the observed data points fall below, based on the cumulative counts in the histogram buckets.

This query is particularly useful for analyzing latency or performance metrics, as percentiles provide insights into the worst-case scenarios experienced by users.

## Visualization examples and important warnings

You can visualize histogram metrics in Dynatrace Notebooks or Dashboards using DQL queries. However, be aware of the following limitations:

* Dynatrace currently visualizes histogram metrics **as percentiles with line charts over time** (using the `timeseries` command). Visualizing the distribution of occurrences across buckets for a given period of time (typically using a bar chart visualization) is **NOT** supported at this time.

For more information, see [Edit visualizations for Notebooks and Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Licensing and billing

The [timeseries percentile](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries_percentile "DQL metric commands") function, which is necessary to query histograms, is only available to DPS customers with the **Metrics powered by Grail** rate card. For more information, see [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").


---


## Source: metrics-security-context.md


---
title: Set up Grail permissions for Metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/metrics-security-context
scraped: 2026-02-15T21:22:25.902555
---

# Set up Grail permissions for Metrics

# Set up Grail permissions for Metrics

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as `department-A/department-AB/team-C`.

To use `dt.security_context` and other attributes for permissions, make sure these attributes are present in your telemetry data.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Set up the security context in OpenPipeline

You can define a security context based on existing resource attributes for your data within OpenPipeline. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Metrics** > **Pipelines** and after configuring your pipeline, on the **Permission** tab, use the **Set Security Context processors** option.

To define the `dt.security_context` attribute

1. Define a matching condition to filter metric records to assign the security context, such as:

   ```
   matchesValue(metric.key, "http.server.request.duration_bucket") and matchesValue(http.route, "/basket")
   ```
2. Add the `dt.security_context` for those metric records. The value of this attribute can be a literal value such as `TeamA`, or a value copied from another field present on the metric record.
3. Verify your security context is set correctly.

When new metric data arrives, the OpenPipeline security context processors add a `dt.security_context` attribute with the value `TeamA` to the matching metric records. To confirm that your security context processors handled the metric records, open ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and run a DQL query such as:

```
timeseries median(http.server.request.duration_bucket), by:{http.route, dt.security_context} | filter matchesValue(dt.security_context, "TeamA")
```

Based on the created attribute, you can enforce security-related user and group policies.

## Related topics

* [Set up Grail permissions for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent.")
* [Metadata enrichment of all telemetry originating from Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes")
* [Set up Grail permissions for logs](/docs/analyze-explore-automate/logs/lma-security-context "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")
* [Set up Grail permissions for Distributed Tracing](/docs/observe/application-observability/distributed-tracing/permissions "Manage permissions for Distributed Tracing powered by Grail.")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")


---


## Source: kubernetes-metric-migration.md


---
title: Kubernetes metrics migration guide
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/kubernetes-metric-migration
scraped: 2026-02-15T21:28:20.050229
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

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.cluster.readyz

builtin:kubernetes.cluster.readyz

dt.kubernetes.container.oom\_kills

builtin:kubernetes.container.oom\_kills

dt.kubernetes.container.restarts

builtin:kubernetes.container.restarts

dt.kubernetes.node.conditions

builtin:kubernetes.node.conditions

dt.kubernetes.node.cpu\_allocatable

builtin:kubernetes.node.cpu\_allocatable

dt.kubernetes.node.memory\_allocatable

builtin:kubernetes.node.memory\_allocatable

dt.kubernetes.node.pods\_allocatable

builtin:kubernetes.node.pods\_allocatable

dt.kubernetes.nodes

builtin:kubernetes.nodes

dt.kubernetes.persistentvolumeclaim.available

builtin:kubernetes.persistentvolumeclaim.available

dt.kubernetes.persistentvolumeclaim.capacity

builtin:kubernetes.persistentvolumeclaim.capacity

dt.kubernetes.persistentvolumeclaim.used

builtin:kubernetes.persistentvolumeclaim.used

dt.kubernetes.resourcequota.limits\_cpu

builtin:kubernetes.resourcequota.limits\_cpu

dt.kubernetes.resourcequota.limits\_cpu\_used

builtin:kubernetes.resourcequota.limits\_cpu\_used

dt.kubernetes.resourcequota.limits\_memory

builtin:kubernetes.resourcequota.limits\_memory

dt.kubernetes.resourcequota.limits\_memory\_used

builtin:kubernetes.resourcequota.limits\_memory\_used

dt.kubernetes.resourcequota.pods

builtin:kubernetes.resourcequota.pods

dt.kubernetes.resourcequota.pods\_used

builtin:kubernetes.resourcequota.pods\_used

dt.kubernetes.resourcequota.requests\_cpu

builtin:kubernetes.resourcequota.requests\_cpu

dt.kubernetes.resourcequota.requests\_cpu\_used

builtin:kubernetes.resourcequota.requests\_cpu\_used

dt.kubernetes.resourcequota.requests\_memory

builtin:kubernetes.resourcequota.requests\_memory

dt.kubernetes.resourcequota.requests\_memory\_used

builtin:kubernetes.resourcequota.requests\_memory\_used

dt.kubernetes.workload.conditions

builtin:kubernetes.workload.conditions

dt.kubernetes.workload.pods\_desired

builtin:kubernetes.workload.pods\_desired

dt.kubernetes.workloads

builtin:kubernetes.workloads

## Convergent metrics

The following metrics have been consolidated. The Grail metrics that supersede the Classic metrics offer an increased level of detail compared to the Classic metrics.

To achieve this decreased level of detail, the Grail metrics are first aggregated to the granularity of the Classic metric. From there the same set of filters can be applied and the output between Classic metrics and Grail metrics is identical.

The following list of metrics contains the pod and container count metrics and the Kubernetes event count metric that was available at a lower level of detail as Classic metric.

Kubernetes events and container/pod count metrics

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.containers

builtin:kubernetes.containers

dt.kubernetes.pod.containers\_desired

builtin:kubernetes.workload.containers\_desired

dt.kubernetes.events

builtin:kubernetes.events

dt.kubernetes.pods

builtin:kubernetes.node.pods  
builtin:kubernetes.pods

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

Metric key (Grail)

Metric key (Classic)

dt.kubernetes.container.cpu\_usage

builtin:kubernetes.node.cpu\_usage  
builtin:kubernetes.workload.cpu\_usage

dt.kubernetes.container.cpu\_throttled

builtin:kubernetes.node.cpu\_throttled  
builtin:kubernetes.workload.cpu\_throttled

dt.kubernetes.container.requests\_cpu

builtin:kubernetes.node.requests\_cpu  
builtin:kubernetes.workload.requests\_cpu

dt.kubernetes.container.limits\_cpu

builtin:kubernetes.node.limits\_cpu  
builtin:kubernetes.workload.limits\_cpu

dt.kubernetes.container.memory\_working\_set

builtin:kubernetes.node.memory\_working\_set  
builtin:kubernetes.workload.memory\_working\_set

dt.kubernetes.container.requests\_memory

builtin:kubernetes.node.requests\_memory  
builtin:kubernetes.workload.requests\_memory

dt.kubernetes.container.limits\_memory

builtin:kubernetes.node.limits\_memory  
builtin:kubernetes.workload.limits\_memory

## Replaced metrics

This group of metrics consists of Classic metric keys that have never been made available as Grail metrics.
Instead the most similar Classic metric is used to then determine the Grail metric replacement for these deprecated metrics.
The reason for the deprecation is a cleanup of duplicate metric keys. In the case of the following metrics, a complete identity of the values between the Classic Metric and Grail Metric is not feasible, but they are closely related and do not deviate very much.

Metric key (Grail)

Metric key (Classic)

Superseding Classic Metric

dt.kubernetes.container.limits\_cpu

builtin:containers.cpu.limit

n.a.

dt.kubernetes.container.oom\_kills

builtin:kubernetes.container.outOfMemoryKills

builtin:kubernetes.container.oom\_kills

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


---


## Source: rum-metric-migration.md


---
title: RUM metrics migration
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration
scraped: 2026-02-15T21:26:49.011392
---

# RUM metrics migration

# RUM metrics migration

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Jan 23, 2026

Looking for the New RUM Experience metrics documentation?

You can access the full list of available metrics and their details directly in the latest Dynatrace. Press **CTRL**/**CMD**+**K**, type `dt.frontend` and select **Show more**.

The [New RUM Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance."), which brings RUM to Grail, introduces numerous built-in metrics with the prefix `dt.frontend`. Because it uses a different data model than RUM Classic, there are no direct equivalents for [RUM Classic metrics](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#applications "Explore the complete list of built-in Dynatrace metrics."), which use the prefix `builtin:apps`. However, many metrics have replacements that serve an analogous purpose, as shown in the table below. Note that metrics with the prefix `builtin:apps` that do not appear in the table have no replacement.

Differences in metric values between the `builtin:apps` metrics and their replacements are expected and result from underlying data model changes.

RUM Classic metric

Replacement in the New RUM Experience

builtin:apps.web.actionCount.\*

builtin:apps.other.uaCount.\*

dt.frontend.user\_action.count

builtin:apps.web.actionDuration.\*

builtin:apps.other.uaDuration.\*

dt.frontend.user\_action.duration

builtin:apps.other.crashCount.\*

builtin:apps.web.countOfErrors\*

builtin:apps.web.jsErrors\*

builtin:apps.other.requestErrorCount.\*

builtin:apps.web.countOfStandaloneErrors

builtin:apps.mobile.reportedErrorCount

dt.frontend.error.count

builtin:apps.other.requestErrorRate.\*

dt.frontend.error.count

dt.frontend.request.count

builtin:apps.web.cumulativeLayoutShift.load.\*

dt.frontend.web.page.cumulative\_layout\_shift

builtin:apps.web.domInteractive.load.\*

dt.frontend.web.navigation.dom\_interactive

builtin:apps.web.firstInputDelay.load.\*

dt.frontend.web.page.first\_input\_delay

builtin:apps.web.interactionToNextPaint

dt.frontend.web.page.interaction\_to\_next\_paint

builtin:apps.web.largestContentfulPaint.load.\*

dt.frontend.web.page.largest\_contentful\_paint

builtin:apps.web.loadEventEnd.\*

dt.frontend.web.navigation.load\_event\_end

builtin:apps.other.requestCount.\*

dt.frontend.request.count

builtin:apps.other.requestTimes.\*

dt.frontend.request.duration

builtin:apps.web.activeSessions

builtin:apps.mobile.sessionCount

builtin:apps.other.sessionCount.\*

dt.frontend.session.active.estimated\_count

builtin:apps.web.firstByte.load.\*

dt.frontend.web.navigation.time\_to\_first\_byte

builtin:apps.other.userCount.\*

builtin:apps.web.activeUsersEst

dt.frontend.user.active.estimated\_count

## Related topics

* [New Real User Monitoring Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance.")


---
