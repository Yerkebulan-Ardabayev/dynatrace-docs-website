---
title: Configure a processing pipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/tutorial-configure-processing
scraped: 2026-02-15T21:12:21.857605
---

# Configure a processing pipeline

# Configure a processing pipeline

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Sep 16, 2025

Manage configuration of ingestion endpoints, dynamic routes, and pipelines via OpenPipeline.

## Who this is for

This article is intended for administrators controlling ingestion configuration, data storage and enrichment, and transformation policies.

## What you will learn

In this article, you'll learn how to create a new configuration for data records via OpenPipeline, from ingestion configuration to Grail storage.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* You have both `openpipeline:configurations:write` and `openpipeline:configurations:read` permissions. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* If you already use the log processing pipeline, ensure the [matching conditions are converted to DQL](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.").

Key terms

Ingest sources
:   Source of ingestion for a configuration scope, collecting data from the provider into Dynatrace Platform, for example, API endpoints or OneAgent.

Routing
:   Assignation of data to a pipeline, based either on matching conditions (dynamic routing) or directly configured (static).

Pipeline
:   Collection of processing instructions to structure, separate, and store data.

Stage
:   Phase in a pipeline sequence, focused on a task and defined by processors.

Processor
:   Pre-formatted processing instruction.

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configure a pipeline**](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Configure custom ingest sources**](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#ingest "Configure ingest sources, routes, and processing for your data in OpenPipeline.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Route data to a pipeline**](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

### Step 1 Configure a pipeline

OpenPipeline stores data in Grail buckets. If you need a bucket with specific permissions or custom data retention, [create a custom bucket](/docs/platform/grail/organize-data#custom-grail-buckets "Insights on the Grail data model consisting of buckets, tables, and views.").

**Pipelines** lists built-in and custom pipelines for a configuration scope in your environment. To configure your own pipelines to group processing and extraction by technology or team

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: and select a configuration scope.
2. Select **Pipelines** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** to add a new pipeline.
3. Required Enter the pipeline name.
4. For each stage, configure the processors.

   1. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** and choose a processor.
   2. For each processor, specify the name and matching condition. Additional required fields vary based on the processor and are specified in the user interface.
5. Select **Save**.

Successfully configured pipelines are displayed in the pipelines list. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Edit** to modify a custom pipeline.

### Step 2 optional Configure custom ingest sources

**Ingest sources** lists built-in and custom ingest sources for a configuration scope in your environment. To configure your own ingest sources, such as API endpoints for a service, technology, or team,

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: and select a configuration scope.
2. Select **Ingest sources** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Source**.
3. Enter a source name and the path URI, and choose a routing option.

   * To route data statically to a pipeline, specify the pipeline name, then proceed with the **Ingest sources** setup.
   * To route data dynamically, complete the **Ingest sources** setup and then [specify the matching conditions](#route).
4. Optional To configure storage for an ingest source, expand **Advanced options** and choose an existing Grail bucket.
5. Optional To pre-process data before it's routed to a pipeline, go to **Pre-processing** and set the processors. For each processor, specify a name and a matching condition. Additional required fields vary based on the processor and are specified in the user interface.
6. Select **Save**.

Successfully configured custom ingest sources are displayed in the ingest sources list. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Edit** to modify a custom ingest source.

### Step 3 Dynamically route data to a pipeline

You can route incoming data to pipelines based on any field value or the ingest source. To route data dynamically

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: and select a configuration scope.
2. Select **Dynamic routing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route**.
3. Enter a matching condition.
4. Select **Save**.

Successfully configured routes are displayed in the dynamic routing list. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Edit** to modify a routing configuration.

## Conclusion

You have configured ingest sources, routing, and processing for records of a configuration scope via OpenPipeline. Once you [start ingesting](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline."), your data is processed as configured, stored in a Grail bucket, and available for analysis via Grail capabilities.

## Related topics

* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")