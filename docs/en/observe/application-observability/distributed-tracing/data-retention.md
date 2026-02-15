---
title: Retain trace data for long periods
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/data-retention
scraped: 2026-02-15T08:55:07.702502
---

# Retain trace data for long periods

# Retain trace data for long periods

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jun 23, 2025

Long-term data retention provides comprehensive trend analysis and performance monitoring over extended periods. For industries with regulatory requirements for auditing and compliance purposes, storing trace data for several years can be a requirement. Additionally, it supports teams in identifing recurring issues, troubleshooting processes that take longer than expected, and investigating and resolving issues that may not be immediately apparent, especially those that develop over time.

With distributed tracing powered by Grail, you can store trace data in Grail buckets with custom retention time, from 10 days up to 10 years, shaping trace data retention and storage according to team ownership or time requirements.

## Who is this for

This article is intended for SRE and architects who want to store trace data to compare the behavior of services over long periods of time for troubleshooting or compliance purposes.

## What you will learn

In this article you will learn how to create a custom bucket with a 5-year data retention period and assign production trace data of a Kubernetes namespace to it.

## Before you begin

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

Prior knowledge

* [Organize data](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

Key terms

Pipeline
:   Collection of processing instructions to structure, separate, and store data.

Stage
:   Phase in a pipeline sequence, focused on a task and defined by processors.

Processor
:   Pre-formatted processing instruction.

Routing
:   Assignation of data to a pipeline, based either on matching conditions (dynamic routing) or directly configured (static).

## Steps

1. Create a custom bucket

To create a custom bucket with a long retention period

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Storage management** > **Bucket storage management** >  **Bucket**.
2. Define the new bucket

   * Name: `long_term_spans`
   * Retention period (days): `1825`
   * Record type: **spans**
3. Select **Create** and then refresh the list (  ).

You created a new bucket to store trace data for 5 years. The bucket will remain empty until you assign records to it via ![OpenPipeline](https://dt-cdn.net/images/openpipeline-configurations-highresolution-1025-8c07f4c78c.webp "OpenPipeline") OpenPipeline.

2. Set the bucket as storage

To assign records from a production namespace to the `long_term_spans` bucket via ![OpenPipeline](https://dt-cdn.net/images/openpipeline-configurations-highresolution-1025-8c07f4c78c.webp "OpenPipeline") OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Choose an existing pipeline or create a new one.
3. In the **Storage** stage, select  **Processor** > **Bucket assignement**.
4. Define the new processor

   * Name: `Store prod spans (5 years)`
   * Condition: `k8s.namespace.name==prod`
   * Bucket: **long\_term\_spans**
5. Select **Save**.

If an existing route points to the pipeline, the new processor will start assigning trace data from the production namespace to the `long_term_spans` bucket. If you created a new pipeline for the processor, make sure to route trace data to it.

3. Route data to the bucket

Make sure your pipeline is receiving records via a dynamic route.

1. Go to **Dynamic routing**.
2. Choose an existing dynamic route or create a new one.
3. Define the route by entering a route name, a matching condition (for example `true`), and the target pipeline name.
4. Select **Save**.

## Conclusion

You created a new bucket with a custom retention period of 5 years. The new bucket is the storage option for production-related spans. Spans are routed to the pipeline and assigned to the bucket according to matching condition.

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")