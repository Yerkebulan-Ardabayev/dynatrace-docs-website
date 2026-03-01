---
title: Processing in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/processing
scraped: 2026-03-01T21:11:38.838134
---

# Processing in OpenPipeline

# Processing in OpenPipeline

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Jan 28, 2026

Dynatrace OpenPipeline can reshape incoming data for better understanding, processing, and analysis. OpenPipeline processing is based on rules that you create and offers a flexible way of extracting value from raw records.

## Key terms

Ingest sources
:   Source of ingestion for a configuration scope, collecting data from the provider into Dynatrace Platform, for example, API endpoints or OneAgent.

Routing
:   Assignation of data to a pipeline, based either on matching conditions (dynamic) or direct assignation (static).

## Pipeline

Once data is ingested and routed, OpenPipeline processing occurs in pipelines. Each pipeline contains a set of processing instructions (processors) that are executed in an ordered sequence of stages and define how Dynatrace should structure, separate, and store your data. After a record is processed, it's sent to storage and is available for further analysis.

Record enrichment

Processing is based on available records and doesn't take into account record enrichment from external services.

### Types

Pipelines can be of a custom or built-in type.

#### Custom pipeline

You can create new custom pipelines and modify them to group processing and extraction according to the relevant technology or team. By adding custom pipelines per team, you can manage them via owner-based access control.

#### Built-in pipeline

Built-in pipelines are provided out of the box. They are essential for OpenPipeline operation and generally cannot be modified within OpenPipeline. Access to these pipelines is intentionally restricted to preserve their configuration.

##### Default pipeline

The **default** pipeline is a built-in pipeline that processes unassigned incoming data for storage. It's unique to the configuration scope and ensures that records are assigned to the default bucket and not unintentionally dropped. It's available to all users in view-only mode. It's not available for log and business event configuration scopes where the **Classic pipeline** is available.

Route as much data as feasible to custom pipelines using explicit matching conditions; limit the use of the default pipeline to monitoring unassigned incoming data.

##### Classic pipeline

The **Classic pipeline** is a built-in pipeline specific to the log and business event configuration scopes. It represents and serves as an entry point to the rules you set in **Settings Classic** for [log](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.") or [business event](/docs/observe/business-observability/bo-event-processing "Utilize business event processing rules to reshape incoming business event data for better understanding, analysis, or further transformation.") processing via the classic pipeline.

If you use log processing via the classic pipeline, migrate your rules to OpenPipeline custom pipelines.

Processing via classic pipeline vs OpenPipeline

Processing via OpenPipeline offers higher limits and flexibility. The following table summarizes the key technical differences of processing logs via the log classic pipeline and OpenPipeline.

| Technical point | Log classic pipeline | OpenPipeline |
| --- | --- | --- |
| Data type support | `String` | `String`, `Number`, and `Boolean` |
| Content field limit | 512 kB | 10 MB |
| Field name case sensitivity | Case-insensitive | Case-sensitive[1](#fn-1-1-def) |
| Connect log data to traces | Built-in rules | Automatic[2](#fn-1-2-def) |
| Technology parsers | Built-in rules | Preset bundles with broader technology support |
| Query language | LQL, DQL | DQL[3](#fn-1-3-def) |
| Metric dimension naming | No | Yes |
| Metric-key `log` prefix | Mandatory | Optional |

1

If logs are ingested via [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2."), the field names are automatically lowercased after data is routed to the **Classic pipeline**.

2

The enrichment is done automatically, without requiring any user interaction.

3

See also [Conversion to DQL for Logs](/docs/analyze-explore-automate/logs/logs-upgrade/lma-dql-conversion "Convert your current log monitoring rules to DQL.").

### Use cases

* Prepare, transform, and store data in Grail.
* Grant access to specific records.

## Stage

A stage is a phase in a pipeline sequence that focuses on a task, such as masking, filtering, processing, or extraction. Stages contain a predefined list of configurable processors, which define the task of the stage.

![Stages in a pipeline](https://dt-cdn.net/images/stages-2497-7cb2c914ee.png)

The following table is a comprehensive list of stages, ordered in the pipeline sequence of execution, specifying which processors are available and executed for each stage, for the supported configuration scopes.

Specific fields are excluded from matching and processing or restricted. To learn more, see [Limits specific to fields](/docs/platform/openpipeline/reference/limits#fields "Reference limits of Dynatrace OpenPipeline.").

1

The data remains in its original, structured form. This is important for detailed analysis and troubleshooting, as it ensures that no information is lost or altered.

2

Extracted metrics are sent to Grail only, except for the security events (new) and span configuration scopes.

## Processor

A processor is a pre-formatted processing instruction that focuses either on modifying (for example, by renaming or adding a new field) or extracting data (for example, by creating an event from a log line or extracting metrics).

While the processor format is predefined, it contains a configurable matcher and processing definition.

* The matcher defines the target of a processor via a DQL query. It narrows down the available data to the specific set you want to process.
* The processing definition instructs Dynatrace on how to transform or modify the data filtered by the matcher.

The following table lists alphabetically all available processors in a pipeline.

## Related topics

* [DQL Functions in OpenPipeline](/docs/platform/openpipeline/reference/openpipeline-dql-functions "A list of DQL functions available in OpenPipeline.")
* [DQL Commands](/docs/platform/openpipeline/reference/openpipeline-dql-commands "A list of DQL commands available in OpenPipeline.")