---
title: Processing in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/processing
scraped: 2026-02-18T05:34:56.867105
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

Stage

Description

Processors in the stage

Executed processors

Supported data types

Processing

Prepare data for analysis and storage by parsing values into fields, transforming the schema, and filtering the data records. Fields are edited, and sensitive data is masked.

* DQL
* Add fields
* Remove fields
* Rename fields
* Drop record

All matches

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new) [1](#fn-2-1-def), Business events, Spans[1](#fn-2-1-def) , Metrics, User events, User sessions

Metric extraction

Extract metrics from the records that match the query.

* Counter metric
* Preview Histogram metric[2](#fn-2-2-def)
* Value metric

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, System events, User events, User sessions

Smartscape Node Extraction

Extract Smartscape nodes for the records that match the query.

* Smartscape node

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, System events, Spans[1](#fn-2-1-def), User events, User sessions

Smartscape Edge Extraction

Extract Smartscape edges for the records that match the query.

* Smartscape edge

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, System events, Spans[1](#fn-2-1-def), User events, User sessions

Metric extraction

Extract metrics from the records that match the query.

* Sampling aware counter metric
* Preview Sampling aware histogram metric[2](#fn-2-2-def)
* Sampling aware value metric

All matches

Spans

Data extraction

Extract a new record from a pipeline and re-ingest it as a different data type into another pipeline.

* Business event
* Software developement lifecycle event

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, System events, Spans[1](#fn-2-1-def), User events, User sessions

Davis

Extract a new record from a pipeline and re-ingest it as a Davis events into another pipeline.

* Davis event

All matches

Logs, EventsâGeneric, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, System events, Spans[1](#fn-2-1-def)

Cost allocation

Advanced option to assign cost center usage to specific records that match a query.

Make sure to review [Cost Allocation documentation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") when choosing the best approach for your environment.

* DPS Cost Allocation - Cost Center

First match only

Logs, Spans[1](#fn-2-1-def)

Product allocation

Advanced option to assign product or application usage to specific records that match a query.

Make sure to review [Cost Allocation documentation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") when choosing the best approach for your environment.

* DPS Cost Allocation - Product

First match only

Logs, Spans[1](#fn-2-1-def)

Permissions

Apply security context to the records that match the query.

* Set dt.security\_context

First match only

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, Spans[1](#fn-2-1-def), Metrics, User events, User sessions

Storage

Assign records to the best-fit bucket.

* Bucket assignment
* No storage assignment

First match only

Logs, EventsâGeneric, EventsâDavis events, EventsâDavis, EventsâSDLC events, EventsâSecurity events (legacy), Security events (new)[1](#fn-2-1-def), Business events, Spans[1](#fn-2-1-def)

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

Processor

Description

Add fields

Adds fields with name and value.

Bucket assignment

Assigns a Grail bucket.

Business event

Extracts fields into a new record and sends it to the business event table.

Counter metric

Returns the number of occurrences of a metric, from the records that match the query.

Davis event

Extracts fields into a new record and sends it to an event table.

DQL

Processes a subset of DQL. The output is formatted to string, number, bool, duration, timestamp, and respective arrays of those.

DPS Cost Allocation - Cost Center

Assigns cost center usage to a record via [`dt.cost.costcenter`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") by either copying the value from a field or setting it as a static string.

DPS Cost Allocation - Product

Assigns product or application usage to a record via [`dt.cost.product`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") by either copying the value from a field or setting it as a static string.

Drop record

Drops a record. The record is not retained.

Preview Histogram metric

Produces histogram metrics that capture a distribution. Histogram metrics can be used to calculate percentiles using the [`timeseries percentile` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands"), which are useful to analyze latencies and payload sizes.

The Histogram metric processor is currently in [Preview](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.") and only accessible to selected customers. To get started, contact a Dynatrace product expert.

To start a conversation with a Dynatrace product expert, use live chat within your Dynatrace environment.

No storage assignment

Skips storage assignment. The record is not retained.

Sampling aware counter metric

Sampling might be applied to trace data before it's processed, according to [Adaptive Traffic Management for distributed tracing](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume."). This span-specific processor supports sampling awareness when returning the number of metric occurrences, from the span records that match the query. Span aggregation and sampling awareness are configurable for all fields available in field extraction, except durationâaggregation of duration is automatically detected and handled.

Preview Sampling aware histogram metric

Sampling might be applied to trace data before it's processed, according to [Adaptive Traffic Management for distributed tracing](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume."). This span-specific processor supports sampling awareness when producing histogram metrics that capture a distribution. Span aggregation and sampling awareness are configurable for all fields available in field extraction, except durationâaggregation of duration is automatically detected and handled. Histogram metrics can be used to calculate percentiles using the [`timeseries percentile` aggregation](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands"), which are useful to analyze latencies and payload sizes.

The Sampling aware histogram metric processor is currently in [Preview](/docs/whats-new/preview-releases "Learn about our Preview releases and how you can participate in them.") and only accessible to selected customers. To get started, contact a Dynatrace product expert.

To start a conversation with a Dynatrace product expert, use live chat within your Dynatrace environment.

Sampling aware value metric

Sampling might be applied to trace data before it's processed, according to [Adaptive Traffic Management for distributed tracing](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume."). This span-specific processor supports sampling awareness when returning the aggregated values of a metric, from the span records that match the query. Span aggregation and sampling awareness are configurable for all fields available in field extraction, except durationâaggregation of duration is automatically detected and handled.

Set dt.security\_context

Sets the proper record-level access via [`dt.security_context`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") by either copying it from a field, setting it as a static string, or a static array that allows multiple values.

Smartscape node

* Calculates and enriches a Smartscape ID. The Smartscape ID is calculated based on specified ordered ID components. The ID components support the `String` type; their values are taken from reference fields and the specified node type. The Smartscape ID is then enriched on the signal. The default enriched field is `dt.smartscape.<type>` and can be renamed.
* If configured and if the signal contains details to store on the node, it creates a Smartscape event to update the Smartscape storage. This includes any fields and stable static edges extracted from the signal.
  To learn more about Smartscape nodes, see [Smartscape on Grail](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.").

Smartscape edge

Extracts Smartscape edges and assigns specified key-value pairs for the fields: source type, source ID, edge type (pre-defined or custom), target type, and target ID. To learn more about Smartscape edges, see [Smartscape on Grail](/docs/platform/grail/smartscape-on-grail "Learn about Smartscape on Grail features and how Smartscape uses the power of DQL.").

Software developement lifecycle event

Extracts fields into a new record and sends it to the SDLC event table.

Technology bundle

Matches records for the selected technology and processes them according to predefined context-sensitive processing statements.

Remove fields

Removes fields from the record.

Rename fields

Changes the name of fields.

Value metric

Returns the aggregated values of a metric from the records that match the query.

## Related topics

* [DQL Functions in OpenPipeline](/docs/platform/openpipeline/reference/openpipeline-dql-functions "A list of DQL functions available in OpenPipeline.")
* [DQL Commands](/docs/platform/openpipeline/reference/openpipeline-dql-commands "A list of DQL commands available in OpenPipeline.")