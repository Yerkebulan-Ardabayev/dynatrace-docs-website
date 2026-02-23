---
title: Analyze monitoring data with segments
source: https://www.dynatrace.com/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data
scraped: 2026-02-23T21:19:54.541865
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