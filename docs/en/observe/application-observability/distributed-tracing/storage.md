---
title: Configure data storage and retention for Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/storage
scraped: 2026-02-22T21:10:35.331916
---

# Configure data storage and retention for Distributed Tracing

# Configure data storage and retention for Distributed Tracing

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jun 23, 2025

Distributed traces are stored in Grail buckets with a retention period from 10 days up to 10 years. By default, trace data is stored for 10 days in the `default_span` bucket.

* You can store trace data in a custom bucket for specific purposes or with a longer retention period.
* You can skip storage of trace data from a specific ingest source or based on matching conditions.

## Who is this for

This article contains information on how to configure trace data retention and storage for Distributed Tracing powered by Grail via [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline."). This article is intended for administrators controlling identity and access management.

## Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Store trace data in a custom bucket

Buckets can improve query performance by reducing query execution time and the scope of data read. With this procedure, you create a new bucket with a custom retention period for trace data. Spans that match the route and the pipeline conditions are stored according to the chosen bucket retention period.

1. Create a custom bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** > **Bucket storage management** >  **Bucket**.
2. Define the new bucket

   1. Enter a bucket name and the custom retention period (days).
   2. Choose the **span** bucket table type.
3. Select **Create**.
4. Select  to refresh the bucket list.

2. Assign trace data to a bucket

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines** and choose an existing pipeline or create a new one.
2. In the **Storage** stage, select  **Processor** > **Bucket assignement** and define the new processor.

   1. Enter the processor name and the matching condition.
   2. Choose a bucket from the **Storage** dropdown list.
3. Select **Save**.
4. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

## Skip storage

With this procedure, you skip storage of spans that match the route and the pipeline conditions. Trace data is not retained.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** >**Pipelines** and choose an existing pipeline or create a new one.
2. In the **Storage** stage, select  **Processor** > **No storage assignment**.
3. Enter the processor name and matching condition.
4. Select **Save**.
5. Make sure your pipeline is receiving records via a dynamic route.

   1. Go to **Dynamic routing**.
   2. Choose an existing dynamic route or create a new one.
   3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
   4. Select **Save**.

## Related topics

* [Retain trace data for long periods](/docs/observe/application-observability/distributed-tracing/data-retention "Create and assign buckets with custom data retention for your trace data in Grail.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")