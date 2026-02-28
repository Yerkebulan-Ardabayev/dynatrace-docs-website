---
title: Filter Smartscape nodes with segments
source: https://www.dynatrace.com/docs/manage/segments/getting-started/segments-getting-started-filter-smartscape-nodes
scraped: 2026-02-28T21:19:45.169040
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