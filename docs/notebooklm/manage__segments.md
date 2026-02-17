# Dynatrace Documentation: manage/segments

Generated: 2026-02-17

Files combined: 10

---


## Source: segments-concepts-includes.md


---
title: Include data in segments
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-includes
scraped: 2026-02-17T04:54:51.954612
---

# Include data in segments

# Include data in segments

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Nov 04, 2025

Segments can logically structure and serve as convenient filters when analyzing data in different apps. Segments are constructed based on rules, called **Includes**. Learn how data of different types can be included in segments.

## Key terms

Include
:   Single rule, referencing data to be included in segment. Querying for data not explicitly referenced by any include of the selected segment, will lead to empty results.

Signal
:   Observed data point, emmitted by a monitored entity. Available signal types in Dynatrace are `logs`, `metrics`, `events`, `spans`, and others.

Monitored entity
:   Logical component monitored by Dynatrace, persisted as Smartscape node and/or classic entity.

Smartscape node
:   Node topology objects, similar to entities on the Dynatrace cluster. Nodes are a collection of all kinds of entities, regardless of their type.

Classic entity
:   Application, service, process, host, or data center entity stored on the Dynatrace cluster (such as `dt.entity.host`, `dt.entity.service`, `dt.entity.kubernetes_cluster`). Classic entities are bound to a type.

## Includes

Segments are constructed incrementally through includes, step by step, extending the scope of the segment. Includes reference a certain data type and are defined by a filter condition for data of that type.

In its initial state, logically speaking, a segment can be considered empty. To use a segment for filtering, data needs to be included.

![An example of segments missing data](https://dt-cdn.net/images/segments-includes-new-2076-89db100a5d.png)

In the following example, two include blocks were added to include logs and metrics by the given conditions. This illustrates how includes incrementally extend the scope of a segment.

![segments query](https://dt-cdn.net/images/segments-4-1478-162bffb583.png)

Include block order doesn't matter

Include blocks are ORed together.

You can drag  include blocks up and down in the web UI, but this affects only the order in which they are displayed in the UI, and does not influence which data is included in the segment.

Logical conditions within a single include can of course be more complex than simple equals-matches conditions as shown above.

![segments query](https://dt-cdn.net/images/segments-5-1498-f099426644.png)

Conditions of segment includes are evaluated at query time, directly impacting query performance. Make sure to consider [![OpenPipeline](https://cdn.bfldr.com/B686QPH3/at/rp4vgwhpjx5rv6rm53mk88cc/OpenPipeline.svg?auto=webp&width=72&height=72 "OpenPipeline") OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to process fields and simplify complex conditions.

## Data types

### Signals

Collecting observability signals is at the core of Dynatrace, so you need to understand their schema and build segments around how those signals are shaped.

Signals can be included in segments in a number of ways. For the better efficiency of resulting filter expressions, always try to reference them directly.

![Segments: data types example: three include blocks added to include logs, metrics, and events](https://dt-cdn.net/images/data-types-1-2248-556d6370c4.png)

Configurations like the one above can also be expressed more elegantly using the **All data types** option:

![Segments: data types example: using the "All data types" option as a more elegant solution](https://dt-cdn.net/images/data-types-5-2248-9558f6aca9.png)

Since context matters, and the unique monitored entity model in Dynatrace provides an alternative way to work with observability signals, there is a second option to include signals through entity-to-signal relationships.

#### Entity-to-entity relationships

Entity relationships in segments are only supported for backward compatibility with classic entities.

A further benefit of segments in regards to monitored entities is being able to leverage relationships between them.

While working with entities stored as Smartscape nodes in Grail has multiple benefits, it's sometimes necessary to construct segments for classic entities. For instance, this enables having segments that include Kubernetes workloads or other monitored entities of higher cardinality, filtered by their related Kubernetes clusters.

![segments entity relationships](https://dt-cdn.net/images/segments-entities-relationships-2842-fb9d9bec55.png)

Segments allow a single relationship traversal step only. However, multiple parallel relationships of the same originating entity can be configured.


---


## Source: segments-concepts-queries.md


---
title: Segments in DQL queries
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-queries
scraped: 2026-02-17T04:54:47.087217
---

# Segments in DQL queries

# Segments in DQL queries

* Latest Dynatrace
* Explanation
* 2-min read
* Published Mar 29, 2023

Segments are designed to act as context for DQL queries. Similar to **timeframes**, segments will directly impact how much data is scanned and returned for a given query.

## Key terms

Grail
:   Grail is the Dynatrace data lakehouse designed explicitly for observability data. It acts as a single unified storage solution for logs, metrics, traces, events, and more.

Dynatrace Query Language (DQL)
:   Dynatrace Query Language (DQL) is a powerful tool to explore your data and discover patterns, identify anomalies and outliers, create statistical modeling, and more based on data stored in Dynatrace Grail.

## Segments in DQL queries

Grail acts as the primary backend for apps on the Dynatrace platform. Data displayed in those apps is fetched from Grail using DQL queries.

* In more technical apps, such as **Notebooks** and **Dashboards**, you can directly craft and manipulate DQL queries.
* Other apps update data on the screen based on user interactions with simple web UI elements, issuing DQL queries underneath to fetch data.

Segments act as an optional context for DQL queries, injecting user-defined, preconfigured filter conditions.

During query execution, Grail evaluates only relevant conditions of segments passed based on the query's targeted data object. While a `fetch logs` query will look at filter conditions for logs only, a `timeseries` query will only evaluate filter conditions for metrics, and so on.

* Multiple conditions for the same data object in a single segment will result in OR-combined filter conditions.
* Conditions from multiple different segments will result in AND-combined filter conditions to form an intersection of parallelly selected segments.

For details on how segments are passed in the context of a DQL Query API request, see [ExecuteRequestï»¿](https://dt-url.net/6h03utf).


---


## Source: segments-concepts-variables.md


---
title: Variables in segments
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-variables
scraped: 2026-02-17T04:54:53.639114
---

# Variables in segments

# Variables in segments

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 06, 2025

Segments support variables to form dynamic conditions of include blocks. This allows deduplication of segments, covering similar instances in one single segment.

## Key terms

One-off segment
:   Segment configured with static conditions for a one-off scenario.

Dynamic segment
:   Segment configured with dynamic conditions using variables.

Variable query
:   DQL query used to populate variable values.

## Variable usage

In the following example, the variable `$bucket` is set to `default_logs`, so the include statement that follows it resolves to `dt.system.bucket = "default_logs"`.

![segments log buckets](https://dt-cdn.net/images/segments-10-2142-0d7af74bca.png)

## Variable configuration

Variable values can be configured dynamically or statically. The following example uses a DQL query to fetch a dynamic list of Grail buckets containing logs.

![segments variable configuration](https://dt-cdn.net/images/segments-11-2142-785fbf7a08.png)

A similar result can be achieved by using DQL's [data command](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#data "DQL data source commands") to form a static list of values as shown below.

```
data



record(bucket="custom_sen_high_kubernetes_istio_network_logs"),



record(bucket="custom_sen_low_logs_platform_service_shared"),



record(bucket="custom_sen_low_query_frontend_dql_logs")
```

Whether to configure variables to form dynamic or static lists of values depends on preference and specific requirements.

Avoid replicating entity lookups through segment variables filtering on entity IDs. Variables should be used to list values of a dimension that the segment is modeled around, for example, `aws-region`.

### Primary and secondary variables

Variables can be used to model a segment along a single dimension. That single dimension will be the **primary variable** and is identified by the first column of the variable query's result set. Primary variables will account for the list of suggested values when using the segment to analyze data.

On top of that, **secondary variables** can be used to account for variance of required conditions in segment includes. Think of secondary variables as further columns in the result set of a variable query. Secondary variables are strictly tied to the selection of the primary variable value when using the segment to analyze data. Think of it as selecting a full row with all its columns.

The following example will result in a primary variable `$name` and a secondary variable `$key`.

```
data



record(name = "istio_network", key="custom_sen_high_kubernetes_istio_network_logs"),



record(name = "platform_service", key="custom_sen_low_logs_platform_service_shared"),



record(name = "dql_query_frontend", key="custom_sen_low_query_frontend_dql_logs")
```

### Variables and wildcards

Neither variable names nor variable values are allowed to contain the wildcard character `*`. In conditions of segment includes, however, the wildcard character can follow a variable name to form a `starts-with` condition, such as `k8s.cluster.name = $cluster*`.

## Analyzing data using dynamic segments

Segments configured to use variables present a second selection step when being used to analyze data in apps. In our example, that second selection allows analyzing logs by selecting one or more buckets from the list.

![segment selection](https://dt-cdn.net/images/segments-12-2142-b2a14173b1.png)

### Variable query execution

When dynamic segments are used to analyze data, the variable query is executed in the context of the effective user. Users of this segment will therefore need appropriate permissions to access data queried to populate the list of values. If users lack required permissions, the list of values to select from would be empty.

Since variable queries are executed on explicit user interaction, they won't have a significant impact on license consumption. It's still advisable to avoid querying high-volume data types, such as `logs`.


---


## Source: segments-concepts-visibility.md


---
title: Visibility of segments
source: https://www.dynatrace.com/docs/manage/segments/concepts/segments-concepts-visibility
scraped: 2026-02-17T04:54:50.282105
---

# Visibility of segments

# Visibility of segments

* Latest Dynatrace
* Explanation
* 1-min read
* Published Mar 29, 2023

The **Visibility** setting determines who sees the segment in their list of segments.

* **Unlisted**âthese segments are visible only in the owner's list of segments. This prevents segment lists from becoming unnecessarily cluttered. This is the default setting.
* **Anyone in the environment**âthese segments are listed in everyone's list of segments.

![segments query](https://dt-cdn.net/images/segments-6-1000-e8d8694fe0.png)

It is important to understand that the **Visibility** setting doesn't affect general access to segments.

* Unlisted segments can still be made available to others by being referenced in apps, such as in shared notebooks and dashboards. Everyone has read-only access to all segments. This makes collaboration with segments simple.
* Permissions in IAM policies determine who can configure segments visible to anyone.
* Segments themselves don't contain any data. All queries, with or without segments, always respect data access permissions enforced by IAM policies.

## Segment permissions

Regardless of configured visibility, any segment can be accessed with `storage:filter-segments:read` permission. This guarantees that even unlisted segments that may be referenced in a shared notebook, can be used by anyone having access to that notebook.

For more information on segment permissons see [IAM policy statements](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#storage-filter-segments-read "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").


---


## Source: segments-getting-started-analyze-monitoring-data.md


---
title: Analyze monitoring data with segments
source: https://www.dynatrace.com/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data
scraped: 2026-02-17T04:46:21.460620
---

# Analyze monitoring data with segments

# Analyze monitoring data with segments

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Mar 29, 2023

Learn how to analyze monitoring data more efficiently by using segments in **Dashboards**.

## Who this is for

This article is intended for all users aiming to efficiently analyze monitoring data in different apps on the Dynatrace platform.

## What you will learn

In this article, you'll learn how to use segments to make analyzing monitoring data more efficient.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Variables in segments](/docs/manage/segments/concepts/segments-concepts-variables "Learn how variables help to form dynamic segments and reduce configuration effort and maintenance.")

Dynatrace apps supporting segments:

* [Dashboards ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards")](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* [Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks")](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Problems ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new")](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")
* Discovery & Coverage

Support for segments in further apps will follow. Watch for updates.

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have `storage:filter-segments:read` permission. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Apply a segment to filter data on your dashboard**](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data#apply-segment "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Select multiple values for more flexible filtering**](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data#multi-select "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Pin recent selections for quick access**](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data#pinning "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

### Step 1 Apply a segment to filter data on your dashboard

Segments provide quick access to predefined logical filters. Like **Dashboards**, many applications in Dynatrace feature a segment selector, giving access to the list of available segments. You can search by name the segments in the segment selector.

![Filter by segments dropdown](https://dt-cdn.net/images/segments-1-2466-b26bdc327d.png)

1. Go to **Dashboards** and select a dashboard
2. Open the segment selector  and, in **Filter by segments**, select the segment by name
3. Select one or more values for the variable in the selected segment
4. Select **Apply** to apply the selection and filter data on the dashboard

After segments are selected, apps will either automatically update data to match selected segments or require user interaction to update.

### Step 2 optional Select multiple values for more flexible filtering

While one-off segments can be selected with a single click, more advanced segments will offer a secondary selection of a dimension value, like in this example, selecting from a dynamic list of individual deployments. This secondary selection of dynamic segment values also supports multi-select.

![Filter by segments dropdown](https://dt-cdn.net/images/segments-2-2466-e23d7b3f6b.png)

1. Open the segment selector
2. Open the list of values to change your selection
3. Select multiple values to look at data matching either of those values
4. Select **Apply** to apply the selection and filter data on the dashboard

If the selected segments or a combination with other aspects (like timeframe, filters, or permissions) lead to empty query results, the app wonât show any data for that selected context.

### Step 3 optional Pin recent selections for quick access

The segment selector shows the two most recent selections, and shows up to 10 if you select **Show more**. This lets you quickly apply recent selections without having to browse the full list of available segments.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and select  **Notebook**
2. Select  **Logs**
3. Open the segment selector  and find recently used segments from previous steps
4. Select **Pin in Notebooks** to pin a specific selection for quick access
5. Select to apply the pinned entry

![Pin recent segment](https://dt-cdn.net/images/segments-recent-pin-2878-da6346e2b3.png)

Pinned segment selections are unique per app to ensure full control, as most segments won't be universally applicable.

## Conclusion

You've managed to filter data on a dashboard using segments and learned to quickly apply recent and pinned selections, increasing efficiency. Try to do the same in other apps to learn how apps choose to utilize segments for their specific use cases.


---


## Source: segments-getting-started-filter-smartscape-nodes.md


---
title: Filter Smartscape nodes with segments
source: https://www.dynatrace.com/docs/manage/segments/getting-started/segments-getting-started-filter-smartscape-nodes
scraped: 2026-02-16T21:20:03.693660
---

# Filter Smartscape nodes with segments

# Filter Smartscape nodes with segments

* Latest Dynatrace
* Tutorial
* Published Jul 03, 2025
* Preview

In Smartscape on Grail, you can filter monitored entities using the recommended `Data (all types)` include block or the type-specific include block for entities.

## Who this is for

This article is intended for all users aiming to efficiently filter Smartscape on Grail data in different apps on the Dynatrace platform.

## What you will learn

In this article, you'll learn how to use segments to filter Smartscape nodes with include blocks.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Variables in segments](/docs/manage/segments/concepts/segments-concepts-variables "Learn how variables help to form dynamic segments and reduce configuration effort and maintenance.")

Dynatrace apps supporting segments:

* [Dashboards ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards")](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* [Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks")](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* [Problems ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new")](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* [Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Distributed Tracing ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing")](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")
* Discovery & Coverage

Support for segments in further apps will follow. Watch for updates.

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have `storage:filter-segments:read` permission. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Filter Smartscape nodes with Data include blocks

To filter Smartscape nodes with include blocks for `Data (all types)`

1. Select **Settings** > **Environment segmentation** > **Segments**.
2. Select  **Segment** to create a new segment.
3. Under **All data**, provide a desired filter condition (such as `k8s.namespace.name = dynatrace`) in the filter field.
4. Select  **Preview** to preview data that matches your filter condition.
5. Select **Entities** in the list of data types available for your filter condition to preview matching Smartscape nodes.

![An example of configuring Smartscape nodes filters with segments data include blocks](https://dt-cdn.net/images/smartscape-segments-data-includes-2546-c374a90d0b.png)

## Filter Smartscape nodes with entities include blocks

To filter Smartscape nodes with include blocks for entities

1. Select **Settings** > **Environment segmentation** > **Segments**.
2. Select  **Segment** to create a new segment.
3. Select  **More** > **Entities** to create a specific include block for entities in your segment.
4. Under **Entities**, provide a desired filter condition (such as `k8s.namespace.name = dynatrace`) in the filter field.
5. Select  **Preview** to preview Smartscape nodes that match your filter condition.

![An example of configuring Smartscape nodes filters with segments entities include blocks](https://dt-cdn.net/images/smartscape-segments-entity-includes-2546-b1c7bf6b93.png)

## Conclusion

You've learned how to create Smartscape nodes filters using segment include blocks for all-type data and entities. You can now use them to filter monitored entities in Smartscape on Grail.


---


## Source: segments-reference-data-types.md


---
title: Supported data types in segments
source: https://www.dynatrace.com/docs/manage/segments/reference/segments-reference-data-types
scraped: 2026-02-17T04:54:48.713894
---

# Supported data types in segments

# Supported data types in segments

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 29, 2023

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes#data-types "Learn how data of different types can be included in segments.")

We recommend constructing segments with a single `Data (all types)` include block when possible. This gives you the most flexibility for using the segment in different scenarios.

Type

Applicable to

`Data (all types)`

Applicable to queries for any signal data type (such as `fetch logs`), entities (such as `smartscapeNodes "*"`, `fetch dt.entity.host`), or data in other Grail-tables (such as `fetch metric.series`).

`Metrics`, `Logs`, `Spans`, etc.

Applicable to any query for the specific signal data type (such as `fetch logs`).

`Entities`

Applicable to queries for entities (such as `smartscapeNodes "*"`, `fetch dt.entity.host`).

`Host (dt.entity.host)`, etc.

Applicable to queries for classic entities of specified type (such as fetch `dt.entity.host`).


---


## Source: segments-reference-limits.md


---
title: Segment limits
source: https://www.dynatrace.com/docs/manage/segments/reference/segments-reference-limits
scraped: 2026-02-17T04:54:55.317883
---

# Segment limits

# Segment limits

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 21, 2025

## General

* 10,000 segments per environment
* 20 include blocks per segment
* 1 include block per type (for example, Logs, Metrics, Spans etc.)
* 1 expression per filter condition minimum
* 10 expressions per filter condition maximum
* 10,000 values in the variable dropdown
* 10 segments per query

### Classic entities

For classic entities, various limits apply. These limits don't apply to Smartscape on Grail.

* 1 additional include per classic entity type + relationship (entity includes only)
* Conditions for related classic entities can be empty
* 100 selected variable values per segment

## Include block conditions

### All data

* Only fields and values of type `STRING`, and `ARRAY_OR_STRINGS` are supported
* Only operators `=`, and `in()` are supported

  + You can use wildcards `*` for `starts-with`, `contains`, and `ends-with` matches. For details, see [Wildcards](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field#wildcards "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").
  + Asterisks are allowed to follow variable names in conditions for `starts-with` (for example, `foo = $bar*`)

### Classic entities

For classic entities, various limits apply. These limits don't apply to Smartscape on Grail.

* Only selected properties (suggested in the filter field) are allowed
* `starts-with`, `contains`, and `ends-with` are not supported

  + The only exception is `entity.name`, which supports `starts-with`
  + Other properties only support `equals`


---


## Source: segments-use-cases-kubernetes-clusters.md


---
title: Segment data by Kubernetes clusters
source: https://www.dynatrace.com/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters
scraped: 2026-02-17T04:54:43.889738
---

# Segment data by Kubernetes clusters

# Segment data by Kubernetes clusters

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Mar 29, 2023

Configure a segment for signals and monitored entities related to multiple Kubernetes clusters in a common stack.

## Who this is for

This article is intended for administrators and Kubernetes operators who need to organize and logically structure workloads on Kubernetes clusters.

## What you will learn

In this article, you'll learn how to create a segment to conveniently filter observability signals and monitored entities in the Kubernetes domain.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Segments in DQL queries](/docs/manage/segments/concepts/segments-concepts-queries "Learn how Grail evaluates segments during query execution to return matching results only.")
* [Getting started with Kubernetes experience](/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience "Enable Kubernetes experience for existing clusters or start monitoring new clusters.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have both `storage:filter-segments:write` and `storage:filter-segments:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* You have licensed and set up [Kubernetes Platform Monitoring](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a segment for clusters of a common stack**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#create "Configure a segment for signals and monitored entities related to Kubernetes clusters")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Include observability signals and monitored entities**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#include "Configure a segment for signals and monitored entities related to Kubernetes clusters")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Analyze performance and health of entire stack**](/docs/manage/segments/use-cases/segments-use-cases-kubernetes-clusters#analyze "Configure a segment for signals and monitored entities related to Kubernetes clusters")

### Step 1 Create a segment for clusters of a common stack

In our example, a set of a few individual Kubernetes clusters make up a common stack. Together, these clusters form a stack we'll refer to as `dtp-dev3`.

1. Go to ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments") **Segments** and select  **Segment** to add a new segment
2. Give your segment a name and description

   * Select and edit **Untitled segment** to give your segment a name useful in you context  
     For this example, enter `dtp-dev3`
   * Select  **Description** and describe the segment  
     For this example, enter `Signals and entities of K8s clusters of dtp-dev3 deployment`
3. Select **Visibility** and set it to `Anyone in the environment` so others can find and use this segment
4. Select **Save**

At this point, the segment doesn't specify what data it should include. In the next section, we will reference data to be filtered with this segment.

### Step 2 Include observability signals and monitored entities

Since Kubernetes observability signals are consistently labelled with `k8s.*` dimensions and fields, our segment will make use of that by referencing them directly.

1. Select  **Add from data types** > **All data types**
2. Select **Type to filter** to include all data matching `k8s.cluster.name = dtp-dev3*`
3. Select  **Run query** to get a preview of matching data
4. Select **Save** to save your changes

   ![Signals of K8s clusters](https://dt-cdn.net/images/segments-k8s-signals-2090-2e33448917.png)

Including observability signals directly doesn't automatically include their emitting monitored entities. In the next section, we will include those entities specifically.

1. Select  **Add from entities and topology** > **Kubernetes cluster (dt.entity.kubernetes\_cluster)**
2. Select **Type to filter** to include all clusters matching `entity.name = dtp-dev3*`
3. Select  **Run query** to get a preview of matching clusters

   ![K8s clusters](https://dt-cdn.net/images/segments-k8s-clusters-2090-36fbc5501d.png)
4. Select  **Related entity** > **Kubernetes namespace**
5. Select  **Run query** for the newly added include block to get a preview of namespaces related to our clusters from above

   ![K8s namespaces of clusters](https://dt-cdn.net/images/segments-k8s-namespaces-2090-9f4067597b.png)
6. Select  **Related entity** and select all further related entities of Kubernetes clusters the segment is built around

   * Kubernetes namespace (already included)
   * Kubernetes node
   * Kubernetes pod
   * Kubernetes workload
   * Kubernetes service
   * Container group instance
   * Service
   * Host

Currently, monitored entities are included by their individual type. In future, we'll make this more flexible and allow including monitored entities of any type with a single condition.

### Step 3 Analyze health and performance of entire stack

In this step, we show how to

* Analyze general health of our stack in ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
* Analyze health and performance of services of our stack in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
* Analyze Kubernetes workloads of our stack in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

#### Problems

To analyze general health of our stack in ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**

1. Go to ![Problems](https://dt-cdn.net/images/problems-512-34e46d913e.png "Problems") **Problems**
2. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
3. Select **Apply** to finish segment selection
4. Select **Update** to refresh the problems list

   ![Problems affecting entities in dtp-dev3](https://dt-cdn.net/images/segments-k8s-problems-2140-1a51ddfe51.png)

By applying our segment, we get a filtered list of problems affecting any monitored entity of any type in our stack.

#### Services

To analyze health and performance of services of our stack in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**
2. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
3. Select **Apply** to finish segment selection

   ![Services in dtp-dev3](https://dt-cdn.net/images/segments-k8s-services-2140-f351191c33.png)

By applying our segment, we get a filtered list of services related to any cluster of our stack.

#### Dashboards

To analyze Kubernetes workloads of our stack in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**
2. Select **Ready-made dashboards**
3. Select **Search documents** and type `Kubernetes`
4. Select **Kubernetes Namespaces - Workloads** to open the ready-made dashboard
5. Open the segment selector  and, in **Filter by segments**, select the previously created segment `dtp-dev3`
6. Open the dashboard filter **Cluster** to find clusters filtered for selected segment

   ![Dashboard: Kubernetes workloads in namespaces](https://dt-cdn.net/images/segments-k8s-dashboard-workloads-2640-c406e3c410.png)

By applying our segment, we narrow the context of a dashboard, making it possible to block out all other noise with a single click.

Applying a segment to dashboards will filter for data explicitly included in segment. Some tiles may no longer show results because queried data isn't included in the applied segment.

## Conclusion

Youâve configured a segment for a set of Kubernetes clusters that form a common stack. Youâve learned how segments can be applied to conveniently filter data in different apps. You've seen an example how to analyze health and performance of a monitoring environment wihtout having to write or understand a single line of DQL yourself.

Just as for Kubernetes clusters, segments can also be built with the context of Kubernetes namespaces. Simply use `k8s.namespace.name` and select all related entities of **Kubernetes namespaces (dt.entity.cloud\_application\_namespace)** instead.


---


## Source: segments-use-cases-logs-by-bucket.md


---
title: Segment logs by bucket
source: https://www.dynatrace.com/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket
scraped: 2026-02-17T04:54:45.474329
---

# Segment logs by bucket

# Segment logs by bucket

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jul 29, 2025

Configure a segment to function as a convenient filter for logs by Grail buckets to optimize query performance and license consumption.

## Who this is for

This article is intended for administrators controlling data partitioning in Grail buckets as well as power users aiming for more efficient log queries.

## What you will learn

In this article, you'll learn how to create a new segment to function as a log bucket filter for fetching logs queries. You'll also learn the difference between one-off segments using static conditions and dynamic segments leveraging variables.

## Before you begin

Prior knowledge

* [Include data in segments](/docs/manage/segments/concepts/segments-concepts-includes "Learn how data of different types can be included in segments.")
* [Variables in segments](/docs/manage/segments/concepts/segments-concepts-variables "Learn how variables help to form dynamic segments and reduce configuration effort and maintenance.")
* [Segments in DQL queries](/docs/manage/segments/concepts/segments-concepts-queries "Learn how Grail evaluates segments during query execution to return matching results only.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have both `storage:filter-segments:write` and `storage:filter-segments:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

Key terms

Grail bucket
:   Logs can be stored in different Grail buckets. Buckets can improve query performance by reducing query execution time and the scope of data read.

One-off segment
:   Segment configured with static conditions for a one-off scenario.

Dynamic segment
:   Segment configured with dynamic conditions using variables.

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a segment for a single log bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#create-segment "Segment logs by bucket with segments")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add a variable to filter for any log bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#variable "Segment logs by bucket with segments")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Use segment to analyze logs by bucket**](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket#analyze "Segment logs by bucket with segments")

### Step 1 Create a segment for a single log bucket

Having a segment for a single bucket might be desired in some situations. The following example shows how to do that by filtering for logs of bucket `default_logs`.

![segment logs_default bucket](https://dt-cdn.net/images/segments-log-bucket1-2528-0fcb794b9b.png)

1. Go to ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments") **Segments** and select  **Segment** to add a new segment
2. Enter the segment name, such as "Log bucket"
3. Select  **Add from data types** > **Logs** to include logs in your segment
4. **Type to filter** and select `dt.system.bucket`
5. Specify a certain bucket to filter for (for example, `dt.system.bucket = default\_logs)
6. Select **Save**

Successfully configured segments are displayed in the segments list. Select  > **Edit** to modify a segment.

### Step 2 Add a variable to filter for any log bucket

Adding a variable to the segment to dynamically filter for many log buckets instead of one makes the segment universally applicable.

![segment variable logs bucket](https://dt-cdn.net/images/segments-log-bucket2-2524-201b656143.png)

1. Select  **Variable**
2. Query the list of log buckets, sorted alphabetically

   ```
   fetch dt.system.buckets



   | filter dt.system.table == "logs"



   | fields bucket=name



   | sort bucket
   ```
3. Select **Run query**
4. Select **Done** to finish variable configuration
5. Adjust the condition of the include for logs to use `$bucket` variable (`dt.system.bucket = $bucket`)
6. Select **Save**

Successfully configured variables are displayed as on top of existing include blocks of a segment. Select **Edit variable(s)** to modify variables.

### Step 3 Use segment to analyze logs by bucket

You can analyze logs in different apps. To query for logs in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and select  **Notebook**
2. Select  **Logs**
3. Open the segment selector  and, in **Filter by segments**, select the previously created segment for log buckets
4. In the **Select an option** list, select one or more log buckets to filter for
5. Select **Apply** to finish segment selection
6. Select **Run query** to query for logs of the selected buckets

![segment selection](https://dt-cdn.net/images/segments-12-2142-b2a14173b1.png)

## Conclusion

Youâve configured a segment for a single bucket statically. Youâve learned how variables help to make segments more dynamic and cover broader use cases. Lastly, youâve seen how to analyze logs of certain buckets, allowing optimization of query performance and license consumption.


---
