# Документация Dynatrace: platform/openpipeline
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 18
---

## platform/openpipeline/concepts/access-control.md

---
title: Owner-based access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/access-control
scraped: 2026-02-18T21:33:44.656346
---

# Owner-based access control in OpenPipeline

# Owner-based access control in OpenPipeline

* Latest Dynatrace
* Explanation
* 1-min read
* Published Jan 09, 2026

Access control provides fine-grained permission management, balancing development team autonomy with administrator oversight for secure and sustainable ownership. It restricts who can create, edit, view, or share settings objects, while maintaining environment-level permissions.

Availability

Owner-based control is available for pipelines and ingest sources, and not routing.

## Access control and permissions

Access control and permissions are related concepts. For the settings objects where owner-based control is available

* Permissions are specific to the configuration scope setting schema.

  Permissions grant read or write permission at the environment level and are assigned to users or user groups by an administrator. If owner-based control is available for a settings object, permissions alone won't grant access to the settings object. The owner (or administrator) needs to share access for each object with the users or user groups.
* Access control is specific to the settings object.

  Owner-based access control grants view or edit access to a specific object and is defined by its owner. Access control alone doesn't grant access to a specific object if the user doesn't have sufficient permissions on the environment level. The administrator needs to grant the users or user groups sufficient permissions for the owner to share access with them.

Therefore, a settings object, such as a pipeline, can be accessed by a user who is one of the following:

* The owner of the object with sufficient permissions (`settings:objects:read` and `settings:objects:write`)
* An accessor of the object with view or edit access and sufficient permissions (`settings:objects:read` or `settings:objects:write`)
* Administrator (`settings:objects:admin`)

Show me examples

* Example 1: Grant edit access to a custom ingest source to a user.

  + The administrator assigns read and write permissions.

    ```
    ALLOW settings:objects:read, settings:objects:write WHERE settings:schemaId = "builtin:openpipeline.events.ingest-sources"
    ```
  + The owner shares view and edit access to the custom ingest source they own.

  The accessor can view and edit the custom event ingest source and view event built-in ingest sources.
* Example 2: Grant view access to all pipelines to a user group.

  + The administrator assigns read permissions.

    ```
    ALLOW settings:objects:read WHERE settings:schemaGroup IN ("group:openpipeline.all.pipelines")
    ```
  + The owners of custom pipelines share view access.

  The user group can view all built-in pipelines and the custom pipelines to which they have been given access. Because the user group lacks write permissions, the user group can't create or edit custom pipelines, even if owners share edit access.

## Owner

Owners manage settings objects and can share access with other users or transfer ownership at any time, without relying on centralized administrator intervention. The initial owner of the settings object is the user who creates it. Right after it's created, it's private, and only the owner and the administrator can see, access, and manage it.

Owners can:

* Make the settings object public by sharing view access with all users.
* Share the settings object with specific users or user groups.
* Transfer ownership to another user or user group.

## Accessor

Accessors are users who can view or edit settings objects as specified by the owner and according to their permissions.

## Administrator

Administrators maintain complete oversight at the environment level and can control settings objects created by other users, ensuring continuity if the owner is unavailable. Administrators don't need to be an owner or accessor to see settings objects.

Administrators can:

* Access in view and edit mode all settings objects in an environment.
* Manage settings objects where the owner is unavailable.
* Transfer ownership of any settings object.

## Use cases

* Empower teams with self-service configuration.
* Delegate rights, maintaining governance and compliance.

## Related topics

* [Set access control in OpenPipeline](/docs/platform/openpipeline/getting-started/set-access-control "Distribute OpenPipeline ingest source and pipeline management via owner-based access control.")

---

## platform/openpipeline/concepts/data-flow.md

---
title: Data flow in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/data-flow
scraped: 2026-02-18T21:21:11.281978
---

# Data flow in OpenPipeline

# Data flow in OpenPipeline

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Dec 10, 2025

With OpenPipeline, you can ingest data in the Dynatrace platform from a wide variety of formats and providers, through ingest sources. Data is then routed to pipelines for processing, and stored in Grail buckets.

![How does OpenPipeline work](https://dt-cdn.net/images/openpipeline-2500-9c90ed1772.png)

## Key terms

Pipeline
:   Collection of processing instructions to structure, separate, and store data.

## Configuration scope

Configuration scopes, such as logs and events, provide observability insights into the health, performance, and behavior of your system enabling teams to detect, diagnose, and resolve problems. Each configuration scope offers a different perspective because of its unique characteristics.

OpenPipeline provides a unified solution to configure ingestion and processing while ensuring flexibility based on the configuration scope specifics.

### Availability

The following table lists configuration scopes, summarizing availability in OpenPipeline.

| Configuration scope | Availability |
| --- | --- |
| Business events |  |
| Events (generic events) |  |
| Events - Davis events |  |
| Events - Davis problems |  |
| Events - SDLC events |  |
| Events - Security events (legacy) | Will deprecate |
| Logs |  |
| Metrics |  |
| Security events (new) |  |
| Spans |  |
| System events | Limited support[1](#fn-1-1-def) |
| Topology | Planned |
| User events |  |
| User sessions |  |

1

System events supported by OpenPipeline are limited to: App Lifecycle Notifications (`event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"`), Workflow Execution events (`event.kind == "WORKFLOW_EVENT" AND event.provider == "AUTOMATION_ENGINE"`), and ECC self-monitoring events (`event.kind == "EXTENSIONS_EVENT"`).

## Ingest sources

Data reaches the Dynatrace platform via different ingestion sources, such as API endpoints, OneAgent, and extensions, which collect data from data providers. In OpenPipeline, they are defined by a name and a path (`dt.openpipeline.source`).

Once the records reach your Dynatrace SaaS environment via ingest sources, you can route it to a pipeline.

To learn the ingest sources available in OpenPipeline, see [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.").

### Types

Ingest sources can be of a built-in, ready-made, or custom type.

| Technical point | Builtâin ingest source | Readyâmade ingest source | Custom ingest source |
| --- | --- | --- | --- |
| Owner | OpenPipeline | Extension | User or user group |
| Permissions | `settings:read` | `settings:read` | `settings:read`, `settings:write` |
| Access type | Viewâonly for all users | Viewâonly for all users | Ownerâbased access control |
| Configuration scope availability | All | Events, Logs, Metrics | Events (excluding Davis problems and Davis events) |
| Routing option | Dynamic | Dynamic, static | Dynamic, static |
| Preâprocessing | Not configurable | Not configurable | Configurable |

#### Built-in ingest source

Builtâin ingest sources represent the primary data entry points provided by Dynatrace. They are owned by OpenPipeline, allowing all users with `settings:read` permissions to view them, but not modify or delete them. This type is always present in OpenPipeline tables, it's available for all configuration scopes, and only supports dynamic routing.

#### Ready-made ingest source

A readyâmade ingest source is automatically created when an [extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") is installed. In addition to the ingest source, the installation may also generate a pipeline and an active route. Readyâmade ingest sources are owned by the installing extension and are viewâonly for all users with `settings:read` permissions. They remain unchanged through extension reactivations and are removed only when the extension is uninstalled. This type is available for the event, log, and metric configuration scopes. Typically, a ready-made ingest source routes records to the generated pipeline via static routing, however dynamic routing is supported as well.

#### Custom ingest source

Custom ingest sources are created by users, with ownership automatically assigned to them. Owners have view and edit access and can grant view access to other users or user groups, according to the user permissions. Custom ingest sources are available only within event configuration scopes, excluding Davis problems and Davis events. They support preâprocessing and allow both dynamic and static routing.

### Use cases

* Configure multiple pipelines for the same configuration scope, adopting processing instructions specific to the ingest source.

## Pre-processing

Optional data processing that occurs after ingestion and before routing. By setting pre-processing, you can transform raw data into structured formats as soon as it reaches your Dynatrace SaaS environment. Pre-processed data is then routed to a pipeline and is available for further processing before storage. Note that pre-processing is available only for custom ingest sources.

### Use cases

* Apply a unified structure to different providers' data formats.

### Best practices

Set up pre-processing to avoid creating complex matching conditions based on provider-specific data formats. This will help you streamline maintenance for routing and processing, for example, when you start ingesting data from a new provider.

## Routing

After data is ingested (and optionally pre-processed), it's routed to pipelines. The route order is relevantâthe position in the list establishes the order of execution. If no route matches the record, the record is routed via the **Default route**.

Routing is defined according to the following:

* Configuration scope: Pipelines are specific to a configuration scope. Different configuration scopes are routed to different pipelines.
* Ingest source: You can configure routing for each ingest source. Multiple ingest sources of the same configuration scope can be routed to the same pipeline.
* Routing option

  + **Dynamic routing**: Data is routed based on a matching condition. The matching condition is a DQL query that defines the data set you want to route.
  + **Static routing**: Data is routed to a specific pipeline, which remains fixed unless manually updated. Static routing is available only for [custom ingest sources](#ingest-sources).

    If a record matches a different condition but you've already configured static routing for its custom ingest source, the match is skipped and data is routed directly to the pipeline you specified.

### Use cases

* Route data of an ingest source to a dedicated pipeline.

### Best practices

* Route as much data as feasible to [custom pipelines](/docs/platform/openpipeline/concepts/processing#custom-pipeline "Learn the core concepts of Dynatrace OpenPipeline processing.") using explicit matching conditions.
* When multiple routing options are available, choose according to the data set dimension. For example, large data sets benefit more from dynamic routing.

## Processing

OpenPipeline processing occurs in pipelines containing instructions on how to structure, separate, and store your data. To learn more, see [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.").

## Storage

Dynatrace Grail database provides a single unified storage solution for all your configuration scopes. OpenPipeline target storage are [Grail buckets](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views."). You can leverage built-in buckets and, if available for the configuration scope, create new buckets with custom retention periods. Each bucket is assigned to a DQL database table. [Assign permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") to user groups or single users to provide them with access to specific buckets and tables.

By default, OpenPipeline routes data into a built-in pipeline with target storage built-in Grail bucket of the configuration scope. You can configure storage assignment

* For a custom ingest source, by directly defining its targeted storage.
* For a pipeline, based on processing matching conditions.

Exceptions for system events

Storage and retention for system events is not configurable.

---

## platform/openpipeline/concepts/processing.md

---
title: Processing in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/concepts/processing
scraped: 2026-02-18T21:18:53.805900
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

---

## platform/openpipeline/getting-started/how-to-ingestion.md

---
title: How to ingest data (events)
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/how-to-ingestion
scraped: 2026-02-18T21:21:03.607357
---

# How to ingest data (events)

# How to ingest data (events)

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Sep 16, 2025

This guide shows you how to ingest an event in Grail via the `platform/ingest/v1/events` endpoint and verify that it's persisted.

The event we will ingest is

```
{



"name": "My first ingested event"



}
```

## Who this is for

This article is intended for development teams managing data ingestion.

## Before you begin

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license that includes [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Authenticate**](/docs/platform/openpipeline/getting-started/how-to-ingestion#authenticate "How to ingest data for a configuration scope in OpenPipeline.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Copy the endpoint path**](/docs/platform/openpipeline/getting-started/how-to-ingestion#path "How to ingest data for a configuration scope in OpenPipeline.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Send an event**](/docs/platform/openpipeline/getting-started/how-to-ingestion#send "How to ingest data for a configuration scope in OpenPipeline.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Verify ingestion**](/docs/platform/openpipeline/getting-started/how-to-ingestion#verify "How to ingest data for a configuration scope in OpenPipeline.")

### Step 1 Authenticate

The `platform/ingest/v1/events` uses access token authentication. To generate an access token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a token name.
4. Find and select the **OpenPipeline â Ingest Events** (`openpipeline.events`) scope.
5. Select **Generate token**.
6. Select **Copy** and then paste the token to a secure location. It's a long string that you need to copy and paste back into Dynatrace later.

### Step 2 Copy the endpoint path

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Events** > **Ingest sources**.
2. Find the ingest source you are interested in.
3. In the **Endpoints path** column, select the endpoint name > ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy**.

### Step 3 Send an event

Run the following sample command to send an event to your environment endpoint `platform/ingest/v1/events` via `POST` request.

The sample command indicates a JSON content type and provides the JSON event data using the `-d` parameter. Make sure to substitute

* `<your-endpoint-URL>` with the URL of the endpoint you copied. It looks like `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events`.
* `<your-API-token>` with the token you generated.
* `My first ingested event` with the name of your event.

```
curl -i -X POST "<your-endpoint-URL>" \



-H "Content-Type: application/json" \



-H "Authorization: Api-Token <your-API-token>" \



-d "{\"name\":\"My first ingested event\"}"
```

Your request is successful if the output contains the 202 response code, for example

```
HTTP/2 202
```

### Step 4 optional Verify ingestion

To verify that your event has been ingested successfully, query it via DQL, for example in **Notebooks**.

1. Go to **Notebooks**.
2. Choose or create a notebook.
3. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** to add a new section with a DQL query input field.
4. Enter the following DQL query

   Make sure to substitute `My first ingested event` with your event name.

   ```
   fetch events



   | filter name == "My first ingested event"
   ```

Your query is successful if the output is a record containing a timestamp, an ingest source, and a name, for example

![Verify event ingest in Notebooks](https://dt-cdn.net/images/verify-event-ingest-1200-05f1ad9526.webp)

## Learn more

OpenPipeline is the unified ingestion component for the Dynatrace Platform. You can ingest various configuration scopes via APIs. To ingest records for a configuration scope via API, you need to

1. Authenticate.
2. Copy the endpoint path.
3. Send a record.
4. Verify ingestion.

For an overview of the available endpoints, refer to [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.").

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Ingest sources in OpenPipeline](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")

---

## platform/openpipeline/getting-started/how-to-routing.md

---
title: Route data
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/how-to-routing
scraped: 2026-02-18T21:22:53.608412
---

# Route data

# Route data

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 23, 2025

There are several use cases to split incoming records into different streams, for example, separating non-production-relevant data or enabling teams to safely format only records of the applications and services they own.

This guide shows you how to route logs of multiple production-relevant services to dedicated pipelines.

## Who this is for

This article is intended for administrators managing data streams.

## Steps

1. Determine the condition

You can use Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") to determine how many routes are needed and their matching conditions. To determine the conditions of significant production-relevant services

1. Fetch logs of all production-relevant services and summarize the records by an attribute.

   When you fetch logs via DQL in Notebooks you get an overview of the detected attributes that you can use to narrow down your results, for example, `k8s.deployment.name`.

   The following DQL query fetches logs with the Kubernetes namespace `prod` and summarizes the results by deployment name.

   ```
   fetch logs



   | filter k8s.namespace.name == "prod"



   | summarize by:{k8s.deployment.name}, count()
   ```

   Run in Playground
2. Determine the key-value pairs that identify significant services.

   The key-value pairs will be used as matching conditions. This guide focuses on four services that are identified by the following key-value pairs:

   * `k8s.deployment.name == "checkoutservice-*"`
   * `k8s.deployment.name == "currencyservice-*"`
   * `k8s.deployment.name == "emailservice-*"`
   * `k8s.deployment.name == "paymentservice-*"`

You determined how many routes you need (4) and their matching conditions (for example, `k8s.deployment.name == "checkoutservice-*`).

2. Create pipelines

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. Create a pipeline for each service.

   1. Select  **Pipeline** and enter a pipeline titleâfor example, `Checkout service pipeline` for the **checkoutservice** service.
   2. Select **Save**.

You created an empty pipeline for each service.

3. Route records to the dedicated pipeline

Create a route for each pipeline.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines** >  **Dynamic route**.
2. Define the routing condition with

   * A name
   * A matching condition
   * The target pipeline

   The following table contains example conditions based on the Kubernetes namespace and deployment to route each service's logs to the corresponding pipeline.

   Name

   Matching condition

   Target pipeline

   Checkout service

   `k8s.deployment.name == "checkoutservice-*"`

   Checkout service pipeline

   Currency service

   `k8s.deployment.name == "currencyservice-*"`

   Currency service pipeline

   Email service

   `k8s.deployment.name == "emailservice-*"`

   Email service pipeline

   Payment service

   `k8s.deployment.name == "paymentservice-*"`

   Payment service pipeline

Logs that match the routing condition are routed to the target pipeline. The routing table now includes the new routes.

## Conclusion

You routed log lines for each significant production-relevant service to a dedicated empty pipeline.

Inform teams that they can modify the pipeline content and create processing rules for their services. Once logs are ingested and routed to one of the newly created pipelines, they will be processed according to the defined rules.

Production-relevant log lines that don't match any of the newly defined conditions continue to be routed according to the Default route to the Classic pipeline. Define new conditions to route them to a different pipeline.

To change how logs are processed, you can modify the matching condition to exclude or include other log lines, or route log lines to a different processing pipeline, or change the target storage. For example, you can create a new pipeline to skip storage using the **No storage assignment** processor and route all non-production-relevant logs that match the `isNotNull(k8s.namespace.name) and k8s.namespace.name != "prod"` condition.

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")

---

## platform/openpipeline/getting-started/set-access-control.md

---
title: Set access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/set-access-control
scraped: 2026-02-18T21:35:53.942044
---

# Set access control in OpenPipeline

# Set access control in OpenPipeline

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jan 09, 2026

This guide explains how pipeline and custom ingest source owners, as well as administrators, can configure and manage access through the web UI or API.

## Prerequistes

* Dynatrace version 1.322 and earlierYou [migrated your OpenPipeline configurations to the Settings API](/docs/platform/openpipeline/migration-settings "Understand how to migrate your OpenPipeline configurations to new Settings API.").
* Verify that the user or user group permissions are sufficient for the access type you want to grant.
* To carry out the procedures via API, ensure `ownerBasedAccessControl` property is set to `true` for the OpenPipeline Settings API schema you intend to use.

  Access control default API values

  When you set the property for the first time, the following default values are added automatically.

  | Property | Description | Supported values | Default value |
  | --- | --- | --- | --- |
  | `owner` | The user who first changed the settings object. | A user, a user group, or `all-users`. | `all-users` |
  | `accessor` | The users who can access the object, depending on their permissions. | One or multiple users or user groups, or `all-users` | `all-users` |

  Available Settings API schemas

  + [builtin:openpipeline.bizevents.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-ingest-sources "View builtin:openpipeline.bizevents.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.bizevents.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-pipelines "View builtin:openpipeline.bizevents.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.bizevents.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-routing "View builtin:openpipeline.bizevents.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-ingest-sources "View builtin:openpipeline.davis.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-pipelines "View builtin:openpipeline.davis.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-routing "View builtin:openpipeline.davis.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-ingest-sources "View builtin:openpipeline.davis.problems.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-pipelines "View builtin:openpipeline.davis.problems.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.davis.problems.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-routing "View builtin:openpipeline.davis.problems.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-ingest-sources "View builtin:openpipeline.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-pipelines "View builtin:openpipeline.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-routing "View builtin:openpipeline.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-ingest-sources "View builtin:openpipeline.events.sdlc.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-pipelines "View builtin:openpipeline.events.sdlc.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-routing "View builtin:openpipeline.events.sdlc.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-ingest-sources "View builtin:openpipeline.events.security.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-pipelines "View builtin:openpipeline.events.security.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.events.security.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-routing "View builtin:openpipeline.events.security.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-ingest-sources "View builtin:openpipeline.logs.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-pipelines "View builtin:openpipeline.logs.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.logs.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-routing "View builtin:openpipeline.logs.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-ingest-sources "View builtin:openpipeline.metrics.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-pipelines "View builtin:openpipeline.metrics.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.metrics.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-routing "View builtin:openpipeline.metrics.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-ingest-sources "View builtin:openpipeline.security.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-pipelines "View builtin:openpipeline.security.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.security.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-routing "View builtin:openpipeline.security.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-ingest-sources "View builtin:openpipeline.spans.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-pipelines "View builtin:openpipeline.spans.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.spans.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-routing "View builtin:openpipeline.spans.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-ingest-sources "View builtin:openpipeline.system.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-pipelines "View builtin:openpipeline.system.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.system.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-routing "View builtin:openpipeline.system.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-ingest-sources "View builtin:openpipeline.user.events.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-pipelines "View builtin:openpipeline.user.events.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-routing "View builtin:openpipeline.user.events.routing settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-ingest-sources "View builtin:openpipeline.usersessions.ingest-sources settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-pipelines "View builtin:openpipeline.usersessions.pipelines settings schema table of your monitoring environment via the Dynatrace API.")
  + [builtin:openpipeline.user.sessions.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-routing "View builtin:openpipeline.usersessions.routing settings schema table of your monitoring environment via the Dynatrace API.")

## Share access

When you create a pipeline or custom ingest source, you're the owner, and only you and the administrator have access to it. To share access with another Dynatrace user or user group

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.
3. Open the  menu and select  **Share**.
4. Find and select the new accessor.
5. Select the access type:  **View** or  **Edit**.
6. Select **Save**.

To modify or revoke access,

1. Go to  (**Manage access**).
2. Expand the access type for the user to modify it or **Remove** it.

Set the `accessor` property value to the users or user groups that you want to share access with.

## Make public (or private)

When you create a pipeline or custom ingest source, you're the owner, and can share access with all users. To go public

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.
3. Open  and select  **Share**.
4. Go to  (**Manage access**) and turn on **Visible to anyone in your environment (Read only)**.

To return to private, do one of the following

* Turn on **Visible to anyone in your environment (Read only)** to maintain specific accessors.
* Select  **Remove all access** to remove all access types for all users and user groups.

Set the `accessor` property value to `all-users`.

## Transfer ownership

When you create a pipeline or custom ingest source, you're the owner. To transfer ownership to another Dynatrace user or user group

Via UI

Via API

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and select a configuration scope.
2. Find the custom ingest source or pipeline in the table.

1. Open the  menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   Be aware that you'll lose all access unless the new owner gives you permission.
3. After the transfer is complete, the new owner will receive an email about the ownership transfer.

Set the `owner` property value to the user or user group that you want to share access with.

Be aware that you will lose all access unless the new owner gives you permission.

## Next steps

Once administrators set permissions and owners set access, users can manage and access items accordingly. Development teams can start configuring processing for their use cases. To learn more about processing, see [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.").

## Related topics

* [Developer - Owner-based access controlï»¿](https://developer.dynatrace.com/develop/data/store-app-settings/#owner-based-access-control)

---

## platform/openpipeline/getting-started/tutorial-configure-processing.md

---
title: Configure a processing pipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/tutorial-configure-processing
scraped: 2026-02-18T21:21:06.178549
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

---

## platform/openpipeline/reference/api-ingestion-reference.md

---
title: Ingest sources in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-02-18T21:20:59.980958
---

# Ingest sources in OpenPipeline

# Ingest sources in OpenPipeline

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Dec 04, 2025

In this article, you can find reference material on OpenPipeline ingest sources, split by each configuration scope. It includes

* Availabile ingest sources and the associated `dt.openpipeline.source`
* Ingest API specification, such as the endpoint URL and the authentication method
* Prior knowledge, such as concepts, licesing compatibility, and setup

Request query parameters

Each request query parameter becomes a top-level record attribute. If there is a pre-existing attribute in the payload with the same name, the attribute from the query parameter overrides the pre-existing attribute value. An overridden original value is preserved in a new field with name syntax `overwritten<index>.<original field name>`, for example, `overwritten1.myField`.

Business events

### Prior knowledge

* [How to capture business events](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.")
* [OpenPipeline Data extraction stage](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [DDUs for business events](/docs/license/monitoring-consumption-classic/davis-data-units/ddus-for-business-events "Understand how the volume of DDU consumption is calculated for business events.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| RUM Agent | `rumagent` | Built-in |
| Business Events API | `/api/v2/bizevents/ingest` | Built-in |
| Data Extraction | `data_extraction` | Built-in |

#### Business Events API

Captures business events in Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest` |
| Method | POST |
| Authentication | [OAuth](/docs/observe/business-observability/bo-api-ingest#oauth "Set up authentication for and ingest business events via API.") [Access token](/docs/observe/business-observability/bo-api-ingest#access-token "Set up authentication for and ingest business events via API.") with **Ingest bizevents** (`bizevents.ingest`) token scope |
| Payload | `application/json` `application/cloudevent+json` `application/cloudevent-batch+json` |

To learn more, see [Ingest business events via API](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.").

Logs

### Prior knowledge

* [How to ingest logs](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")
* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [DDUs for Log Management and Analytics](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") or [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Amazon Data Firehose | `/api/v2/logs/ingest/aws_firehose` | Built-in |
| Extensions | `<extension>` | Ready-made |
| Log ingest API | `/api/v2/logs/ingest` | Built-in |
| OneAgent | `oneagent` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/logs` | Built-in |

#### Log ingest API

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest` `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Ingest logs** (`logs.ingest`) scope |
| Payload | `text/plain` `application/json` |

To learn more, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### OpenTelemetry

Pushes custom logs to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest logs** (`logs.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

Events (generic events)

### Prior knowledge

* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Default API | `/platform/ingest/v1/events` | Built-in |
| Custom API | `/platform/ingest/custom/events/<custom-endpoint-name>` | Custom |

#### Default API

Ingests generic events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events** (`openpipeline.events`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in generic events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom API

Configures custom endpoints to ingest generic events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom generic event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Configure a custom generic event endpoint via OpenPipeline Ingest API.").

Events-Davis events

### Prior knowledge

* [Davis events](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [OpenPipeline Data extraction stage](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| Classic environment API | `events/ingest` | Built-in |
| Data Extraction | `data_extraction` | Built-in |

#### Classic environment API

Ingests a custom event to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest Events** (`events.ingest`) token scope |
| Payload | `application/json` |

To learn more, see [Events API v2 - POST an event](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

Events-Davis problems

### Prior knowledge

* [Davis problems](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [Classic root cause analysis](/docs/dynatrace-intelligence/root-cause-analysis/concepts#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Classic Root Cause Analysis | *(none)* | Built-in |

Events-SDLC events

### Prior knowledge

* [How to ingest SDLC events](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources



| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Endpoint for Software Development Lifecycle events | `/platform/ingest/v1/events.SDLC` | Built-in |
| Custom endpoint for Software Development Lifecycle events | `/platform/ingest/custom/events.SDLC/<custom-endpoint-name>` | Custom |

#### Endpoint for Software Development Lifecycle events

Ingests SDLC events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.sdlc` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle** (`openpipeline.sdlc`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in SDLC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom endpoint for Software Development Lifecycle events

Configures custom endpoints to ingest SDLC events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom SDLC event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.").

Events-Security events

Migrate by December 2025

The endpoints `events.security` are planned to be deprecated. Migrate your configurations to `security.events` endpoints by **end of December 2025**. The previous endpoints will remain available **until the migration is complete**.

For a full overview of what's changing and step-by-step guidance on how to migrate, follow the instructions in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

### Prior knowledge

* [How to ingest security events](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Security events endpoint | `/platform/ingest/v1/events.security` | Built-in |
| Custom security events API | `/platform/ingest/custom/events.security/<custom-endpoint-name>` | Custom |

#### Security events endpoint (legacy)

Ingests security events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.security` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (legacy)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (legacy)

Configures custom endpoints to ingest security events. For details, see [Ingest custom security events via API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.").

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (legacy)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Metrics

### Prior knowledge

* [How to ingest metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| Classic environment API | `/api/v2/metrics/ingest` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/metrics` | Built-in |

#### Classic environment API

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `text/plain` |

To learn more, see [Metrics API - POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").

#### OpenTelemetry

Ingests OpenTelemetry metrics into Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest metrics** (`metrics.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [OpenTelemetry metrics ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-metrics "Send OpenTelemetry metrics to Dynatrace via API.").

Security events (new)

### Prior knowledge

* [How to ingest security events](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Events powered by Grail overview (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| Security events endpoint | `/platform/ingest/v1/security.events` | Built-in |
| Custom security events API | `/platform/ingest/custom/security.events/<custom-endpoint-name>` | Custom |

#### Security events endpoint (new)

Ingests security events from built-in endpoints.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/security.events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Built-in security events (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Custom security events API (new)

Configures custom endpoints to ingest security events.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) token scope |
| Payload | `application/json` |

To learn more, see [OpenPipeline Ingest API - POST Custom security event endpoint (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Spans

### Prior knowledge

* [How to ingest traces](/docs/observe/application-observability/distributed-tracing/ingest-traces "Instrument your applications with OneAgent or OpenTelemetry to start ingesting trace data into Dynatrace.")
* [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")

### Ingest sources



| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| OneAgent | `oneagent` | Built-in |
| OpenTelemetry | `/api/v2/otlp/v1/traces` | Built-in |

#### OpenTelemetry

Ingests OpenTelemetry traces to Dynatrace.

| Property | Specification |
| --- | --- |
| Endpoint URL | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces` |
| Method | POST |
| Authentication | [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`) token scope |
| Payload | `application/x-protobuf` |

To learn more, see [OpenTelemetry trace ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-traces "Send OpenTelemetry traces to Dynatrace via API..").

System events

### Prior knowledge

* [System event models](/docs/semantic-dictionary/model/dt-system-events "Get to know the Semantic Dictionary models related to system events.")
* [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* Supported system events in OpenPipeline are limited to

  + App Lifecycle Notifications

    `event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"`
  + Workflow Execution events

    `event.kind == "WORKFLOW_EVENT" AND event.provider == "AUTOMATION_ENGINE"`
  + ECC self-monitoring events

    `event.kind == "EXTENSIONS_EVENT"`

  To learn the path and type of the system events processed in your environment

  1. Go to **Notebooks**.
  2. Create a new notebook containing the following query

     ```
     fetch dt.system.events



     | filter isNotNull(dt.openpipeline.pipelines)
     ```
  3. Select **Run**.

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| System Events API[1](#fn-1-1-def) | `system_events` | Built-in |
| Extensions | `<extension>` | Ready-made |

1

Internally generated

User events & sessions

### Prior knowledge

* [User events](/docs/observe/digital-experience/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [User sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* How to capture user events and sessions on [Android](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/android/id-09-user-and-session "Identify users across sessions and devices, manage session lifecycle, and attach properties that apply to all events in a session."), [iOS](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/ios/id-09-user-and-session "Identify users, manage sessions, and report session properties in your iOS application."), [Flutter](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/flutter/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your Flutter application.") or [React Native](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/react-native/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your React Native application.")
* [Digital Experience Monitoring (DEM) overview (DPS)](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

### Ingest sources

| Ingest source | dt.openpipeline.source | Type |
| --- | --- | --- |
| RUM Agent | `rumagent` | Built-in |

## Related topics

* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [How to ingest data (events)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")

---

## platform/openpipeline/reference/dql-matcher-in-openpipeline.md

---
title: DQL matcher in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline
scraped: 2026-02-18T21:22:57.243284
---

# DQL matcher in OpenPipeline

# DQL matcher in OpenPipeline

* Latest Dynatrace
* Reference
* 8-min read
* Updated on Dec 15, 2025

With [Dynatrace powered by Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you can use [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") (DQL) functions and logical operators in matchers.

The matcher filters the ingested data and reduces the scope of data processed by the processor that you create. You can use the matcher in [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to:

* Filter records containing a specified phrase.
* Search data for a specific value in a given attribute.
* Test if a value is null.
* Use logical operators to connect two or more expressions.
* Request logs that show duration for requests longer than `1s`.

To learn about the use of logical operators in DQL, see [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.").

## Functions

### matchesPhrase

Filters records containing a specified phrase. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and the asterisk character (`*`) is a wildcard only referring to a single term, not the whole field value.

##### Validation

The `matchesPhrase` function performs case-insensitive [contains](/docs/platform/grail/dynatrace-query-language/functions#contains "A list of DQL functions.") for the whole query string and doesn't support mid-string wildcards.
For found results, additional validation takes place:

* If the query starts with a word character, the preceding character must be a non-word character.
* If the query ends with a word character, the succeeding character must be a non-word character.
* If the query starts with an asterisk, no validation of the preceding character is performed.
* If the query ends with an asterisk, no validation of the succeeding character is performed.

##### Syntax

`matchesPhrase(expression, phrase)`

##### Parameters

Parameter

Type

Description

Required

expression

string

The field name that should be checked.

Required

phrase

string

The phrase to search for. Accepts wildcard `*` at the beginning or at the end of the phrase.

Required

##### Example

In this example, you add a filter that matches log records that contain `error` phrase in their content.

```
matchesPhrase(content, "error")
```

##### Examples of event processing using DQL matchesPhrase function

Part of the input event

Processing query

Match result

Description

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "192.168.0.1")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Exact match by single term.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

`matchesPhrase(attribute, "192.168.0.1")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Non-word character is expected after character `1`.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.123"`

`matchesPhrase(attribute, "192.168.0.1*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The query would match all IPs with the last octet between `100` and `199`.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "failed to login")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Exact phrase match.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "failed to log")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

`log` is not a full word, non-word character is expected after `log`.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "failed to log*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

If the query ends with a wildcard character, the validation of the succeeding character is skipped.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "ed to login")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

`ed` is not a full word, the preceding character `l` is a part of the word.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "*ed to login")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

If the query starts with a wildcard character, the validation of the preceding character is skipped.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "*ed to log*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

If the query starts and ends with a wildcard character, the validation of the preceding and succeeding characters is skipped.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "kÃ¤Ã¤rmanÃ¼ failed")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

There should be an apostrophe (`'`) character between `kÃ¤Ã¤rmanÃ¼` and `failed`.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, "rmanÃ¼' failed")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Non-ASCII character `Ã¤` is treated as non-word character.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesPhrase(attribute, " 'kÃ¤Ã¤rmanÃ¼' failed")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

If the query starts with non-word character, the validation of the preceding character is skipped.

`attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

`matchesPhrase(attribute, "configuration for")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

There is a space in the query and a tabulator in the attribute value.

`attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

`matchesPhrase(attribute, "failed to")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

There is a single space in the query and a double space in the attribute value

`attribute="Failed to assign monitoring configuration for com.dynatrace.extension"`

`matchesPhrase(attribute, "failed to")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

It is possible to search with multiple spaces.

`attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

`matchesPhrase(attribute, "Austria")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The function handles multi-value attributes in "any-match" manner, in this case `Austria` is matched in second and third value.

`attribute=["Gdansk, Poland", "Linz, Austria", "Klagenfurt, Austria"]`

`matchesPhrase(attribute, "Pol*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Wildcard can be used also when dealing with multi-value attributes.

### matchesValue



Searches the records for a specific value in a given attribute. Returns only matching records. This function is case insensitive for ASCII characters, it works with multi-value attributes (matching any of the values), and it doesn't support mid-value wildcards.

##### Syntax

`matchesValue(expression, value)`

##### Parameters

Parameter

Type

Description

Required

expression

string, array

The field name that should be checked.

Required

value

string, array

The value (string or array of strings literal) to search for. Accepts wildcard `*` at the beginning or at the end of the value.

Required

##### Example

In this example, you add a filter record where `process.technology` attribute contains `nginx` value.

```
matchesValue(process.technology, "nginx")
```

##### Examples of event processing using DQL matchesValue function

Part of the input event

Processing query

Match result

Description

`attribute="Dynatrace"`

`matchesValue(attribute, "dynaTrace")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Case insensitive equality.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesValue(attribute, "192.168.0.1")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

The whole attribute value is considered.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesValue(attribute, "*192.168.0.1")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The value ends with `192.168.0.1`.

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesValue(attribute, "user*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The value starts with `user` (case-insensitively).

`attribute="User 'kÃ¤Ã¤rmanÃ¼' failed to login from 192.168.0.1"`

`matchesValue(attribute, "*failed to log*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The value contains the string `failed to log`.

`attribute="Ãsterreich"`

`matchesValue(attribute, "Ã¶sterreich")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

Case insensitive only for ASCII characters.

`attribute="Ãsterreich"`

`matchesValue(attribute, "Ãsterreich")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Exact match.

`attribute=["Java", "DOCKER", "k8s"]`

`matchesValue(attribute, "docker")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The function handles multi-value attributes in "any-match" manner, in this case, `docker` is matched in the second value.

`attribute=["Java11", "java17"]`

`matchesValue(attribute, "java")`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

None of the values is equal to string java.

`attribute=["Java11", "java17"]`

`matchesValue(attribute, "java*")`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Both values start with a string `java`.

`attribute="April"`

`matchesValue(attribute, {"March", "April", "May"})`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

One of the values in the array matches attribute value `April`.

`attribute="192.168.0.1"`

`matchesValue(attribute, {"127.0.0.1", "192.168.*", "172.16.*", "10.*"})`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

One of the patterns in the array matches attribute value `192.168.0.1`.

### isNotNull

Tests if a value is not NULL.

##### Syntax

`isNotNull(<value>)`

##### Example

In this example, we filter (select) data where the `host.name` field contains a value.

```
isNotNull(`host.name`)
```

timestamp

content

event.type

host.name

`2022-08-03 11:27:19`

`2022-08-03 09:27:19.836 [QueueProcessor] RemoteReporter...`

`LOG`

`HOST-AF-710319`

**Examples of event processing using DQL isNotNull function**

Part of the input event

Processing query

Match result

Description

```
{



attribute="Dynatrace"



}
```

`isNotNull(other)`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

The `other` attribute does not exists

```
{



attribute="Dynatrace"



}
```

`isNotNull(attribute)`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The `attribute` has non-null value.

```
{



attribute=null



}
```

`isNotNull(attribute)`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

The `attribute` has null value.

### isNull

Tests if a value is NULL.

##### Syntax

`isNull(<value>)`

##### Example

In this example, we filter (select) data where the `host.name` field doesn't contain a value.

```
filter isNull(`host.name`)
```

timestamp

content

event.type

host.name

`2022-08-03 12:53:26`

`2022-08-03T10:52:31Z localhost haproxy[12529]: 192.168.19.100:38440`

`LOG`

**Examples of event processing using DQL isNull function**

Part of the input event

Processing query

Match result

Description

```
{



attribute="Dynatrace"



}
```

`isNull(other)`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The `other` attribute does not exists.

```
{



attribute="Dynatrace"



}
```

`isNull(attribute)`

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

The `attribute` has non-null value.

```
{



attribute=null



}
```

`isNull(attribute)`

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

The `attribute` has null value.

## Operators

Logical operators can be used to connect two or more expressions. Check out [Logical or equality operators](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") to find out more about the behavior of logical operators in DQL.

### OR

Logical addition.

##### Syntax

`<expression_1> or <expression_2>`

##### Example

In this example, you add a matcher to filter records where the content contains either `timestamp` phrase or `trigger` phrase.

```
matchesPhrase(content, "timestamp") or matchesPhrase(content, "trigger")
```

### AND

Logical multiplication.

##### Syntax

`<expression_1> and <expression_2>`

##### Example

In this example, you add a matcher to filter records where the content contains `timestamp` phrase and `trigger` phrase.

```
matchesPhrase(content, "timestamp") and matchesPhrase(content, "trigger")
```

### NOT

Logical negation.

##### Syntax

`not <expression>`

##### Example

In this example, you add a matcher to filter records where the content doesn't contain `timestamp` phrase.

```
not matchesPhrase(content, "timestamp")
```

### Boolean literals

The matcher supports the following conditions:

* `true`â the processor (DQL query) will be applied to all records
* `false`â the processor will not be applied to any of the records in the data set

##### Literal notation

A Boolean value can be expressed using either uppercase or lowercase letters: `true`, `TRUE`, `false`, `FALSE`.

### Iterative expressions

#### iAny

Checks an iterative boolean expression and returns `true`, if the expression was true at least once, `false` if it wasn't. For example:

```
iAny(a[] > 2)
```

### Numerical operators

With DQL matcher in OpenPipeline, you can use the following numerical operators:

* `<`âLess than, for example `http.request.body.size < 1024`
* `>`âGreater than, for example `http.request.body.size > 1024`
* `<=`âLess than or equal to, for example `http.request.body.size <= 1024`
* `>=`âGreater than or equal to, for example `http.request.body.size >= 1024`
* `==`âEquals, for example `http.request.body.size == 1024`

#### Strict equality

[Logical operator](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.") (`==`) indicating an exact match.

Configuration scopes need to be identical. However, if the decimal value is `0`, floating numbers can be compared with integer data. For example, `1==1.0`.
For strings, the search is case-sensitive.

Contrary to `matchesValue` function, `strict equality` operator performs case-sensitive comparison, doesn't support wildcards and doesn't operate on elements being part of multi-value attributes.

##### Syntax

`fieldName == <expression>`

## Related topics

* [DQL Functions in OpenPipeline](/docs/platform/openpipeline/reference/openpipeline-dql-functions "A list of DQL functions available in OpenPipeline.")
* [DQL Commands](/docs/platform/openpipeline/reference/openpipeline-dql-commands "A list of DQL commands available in OpenPipeline.")
* [DQL Operators in OpenPipeline DQL processor](/docs/platform/openpipeline/reference/openpipeline-dql-operators "A list of DQL operators available in OpenPipeline DQL processor.")

---

## platform/openpipeline/reference/limits.md

---
title: OpenPipeline limits
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/limits
scraped: 2026-02-18T21:18:46.483520
---

# OpenPipeline limits

# OpenPipeline limits

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Jan 28, 2026

The following page lists the default limits of Dynatrace OpenPipeline.

## Configuration scope limits

Limitations specific to configuration scopes might override OpenPipeline generic limits. For limits specific to the configuration scope, see

* [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") and [Schema validation for logs](#schema-validation-logs)
* [Fields with limits for metrics](#fields-metrics)
* [Fields with limits for spans](#fields-spans)

## Limits specific to fields

### Fields with limits for all configuration scopes

* The following fields can be viewed-only; editing via OpenPipeline is not supported.

  + `dt.ingest.*`
  + `dt.openpipeline.*`
  + `dt.retain.*`
  + `dt.system.*`
* The following fields are added after the **Processing** stage when Dynatrace runs its entity detection. You can use them only in stages after the Processing stage, but not in pre-processing, routing, or the Processing stage.

  + `dt.entity.aws_lambda_function`
  + `dt.entity.cloud_application`
  + `dt.entity.cloud_application_instance`
  + `dt.entity.cloud_application_names`
  + `dt.entity.custom_device`
  + `dt.entity.<genericEntityType>`
  + `dt.entity.kubernetes_cluster`
  + `dt.entity.kubernetes_node`
  + `dt.entity.kubernetes_service`
  + `dt.entity.service`
  + `dt.env_vars.dt_tags`
  + `dt.kubernetes.cluster.id`
  + `dt.kubernetes.cluster.name`
  + `dt.loadtest.custom_entity.enriched_custom_device_name`
  + `dt.process.name`[1](#fn-1-1-def)
  + `dt.source_entity`
  + `k8s.cluster.name`[2](#fn-1-2-def)

  1

  To obtain equivalent results before the Processing stage, you can use `dt.process_group.detected_name` instead.

  2

  OneAgent version 1.309Dynatrace Operator version 1.4.2+The field is available before the Processing stage if [OneAgent Log module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.") is running in standalone mode.

### Fields with limits for metrics

The use of the following fields for metrics in OpenPipeline is limited.

* Fields excluded from dynamic route matching conditions and in the **Processing** stage

  + `dt.entity.*`
* Fields excluded from the **Processing** stage

  + `dt.system.monitoring_source`
  + `metric.key`
  + `metric.type`
  + `timestamp`
  + `value`

### Fields with limits for spans

The use of the following fields for spans in OpenPipeline is limited.

* Fields excluded from dynamic route matching conditions and in the **Processing** stage

  + `dt.entity.service`
  + `endpoint.name`
  + `failure_detection.*`
  + `request.is_failed`
  + `request.is_root_span`
  + `service_mesh.is_proxy`
  + `service_mesh.is_failed`
  + `supportability.*`
* Fields excluded from the **Processing** stage

  + `dt.ingest.size`
  + `dt.retain.size`
  + `duration`
  + `end_time`
  + `span.id`
  + `start_time`
  + `trace.id`

## Ingestion

### Record maximum timestamp

If the timestamp is more than 10 minutes in the future, it's adjusted to the ingest server time plus 10 minutes.

### Record minimum timestamp

Item

Earliest timestamp

Logs, Events, Business Events, System events

The ingest time minus 24 hours

Metrics, extracted metrics, and Davis events

The ingest time minus 1 hour

Records outside of these timeframes are dropped.

## Ingest API

### Timestamp value

Numerical and string timestamp values are supported. OpenPipeline parses the timestamp as follows.

* Numerical values

  + Up to `100_000_000_000` are parsed as `SECONDS`.
  + Up to `100_000_000_000_000` are parsed as `MILLISECONDS`.
  + Up to `9_999_999_999_999_999` are parsed as `MICROSECONDS`.
* String values are parsed either as

  + `UNIX epoch` milliseconds or seconds
  + `RFC3339` formats
  + `RFC3164` formats
* For other values that cannot be parsed, `timestamp` is overwritten with the ingest time.

If the record doesn't have a `timestamp` field, the field `timestamp` is set to ingest time.

## Processing

### Processing memory exhaustion

Each record can occupy maximum 16 MB of processing memory. Each change to the record (e.g. parsing a field) decreases the available processing memory. Once the available processing memory is exhausted, the record is dropped, and the metric `dt.sfm.openpipeline.not_stored.records` with dimension `reason` set to `buffer_overflow` reports it.

### Size of record after processing

The maximum size of a record after processing is 16 MB.

### Size of extracted log attributes

Log attributes can be up to 32 KB in size.
When log attributes are added to the event template, the size of each attribute is truncated to 4,096 bytes.

### Number of extractions for a single record

You can extract data on a single record in a maximum of five different pipelines (`dt. open pipeline.pipelines`). Once the threshold is exceeded, data extraction is no longer performed on the single record. The record continues to be processed and persisted.

### Schema validation for logs

A processed log is persisted if the following conditions are satisfied.

| Field | Exists | Accepted Types | Value Constraints |
| --- | --- | --- | --- |
| `timestamp` | Yes | `String`, `Numerical` | Within the [ingestion range](#ingestion) |
| `content` | Yes | `String` | Not evaluated |

If the schema is not valid the log is dropped.

### Smartscape node processor

The Smartscape ID calculation supports `string` only. The ID components must be of type `string`.

[Pre-process](/docs/platform/openpipeline/concepts/data-flow#pre-processing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.") records to convert the values you need to the `string` data type.

## Configuration

Item

Maximum limit

Early Adopter program maximum limit

Request payload size (per configuration scope)

10 MB

* Total pipeline schemas: 70 MB
* Total route schemas: 10 MB
* Total ingest source schemas: 30 MB

Pipeline number (per configuration scope)

100

2,000

Size of a stage

512 KB

512 KB

Processor number (per pipeline)

1,000

1,000

Endpoint number (per configuration scope)

100

100

Routes number (per configuration scope)

100

3,000

Ingest sources number (per configuration scope)

100

2,000

Length of a matching condition

1,000 UTF-8 encoded bytes

1,000 UTF-8 encoded bytes

Length of a DQL processor script

8,192 UTF-8 encoded bytes

8,192 UTF-8 encoded bytes

### Allowed characters in the endpoint path

The endpoint path is a unique name starting with a literal that defines the endpoint. It's case-insensitive and supports alphanumeric characters and dot (`.`). For example: `Endpoint.1`.

Endpoint path doesn't support:

* Dot (`.`) as the last character
* Whitespaces
* Consecutive dots (`..`)
* `Null` or empty input

---

## platform/openpipeline/reference/openpipeline-api.md

---
title: OpenPipeline API
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/openpipeline-api
scraped: 2026-02-18T21:21:04.875004
---

# OpenPipeline API

# OpenPipeline API

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Sep 10, 2025

### Configurations API

Replaced by Settings API

* [OpenPipeline API - GET all configurations](/docs/platform/openpipeline/reference/openpipeline-api/configurations-api/get-all "View all OpenPipeline configurations of your environment via the Dynatrace API.")
* [OpenPipeline API - GET a configuration](/docs/platform/openpipeline/reference/openpipeline-api/configurations-api/get-configuration "View an OpenPipeline configuration of your environment via the Dynatrace API.")
* [OpenPipeline API - PUT a configuration](/docs/platform/openpipeline/reference/openpipeline-api/configurations-api/put-configuration "Edit an OpenPipeline configuration of your environment via the Dynatrace API.")

### Preview API

* [OpenPipeline API - POST a processor preview](/docs/platform/openpipeline/reference/openpipeline-api/preview-api/post-processor "Create a preview of an OpenPipeline processor of your environment via the Dynatrace API.")

### Matcher API

* [OpenPipeline API - POST verify a matcher](/docs/platform/openpipeline/reference/openpipeline-api/matcher-api/post-verify "Verify an OpenPipeline matcher validity via the Dynatrace API.")
* [OpenPipeline API - POST autocomplete suggestions for a matcher](/docs/platform/openpipeline/reference/openpipeline-api/matcher-api/post-autocomplete "Create autocompletion suggestions for an OpenPipeline matcher via the Dynatrace API.")
* [OpenPipeline API - POST a DQL matcher from a LQL matcher](/docs/platform/openpipeline/reference/openpipeline-api/matcher-api/post-lqltodql "Transform a LQL matcher into a OpenPipeline DQL matcher via the Dynatrace API.")

### DQL Processor API

* [OpenPipeline API - POST verify a DQL processor](/docs/platform/openpipeline/reference/openpipeline-api/dql-processor-api/post-verify "Verify an OpenPipeline DQL processor script validity via the Dynatrace API.")
* [OpenPipeline API - POST autocomplete suggestions for a DQL processor](/docs/platform/openpipeline/reference/openpipeline-api/dql-processor-api/post-autocomplete "Create autocompletion suggestions for an OpenPipeline DQL processor via the Dynatrace API.")

### Technology API

* [OpenPipeline API - GET all technology bundles](/docs/platform/openpipeline/reference/openpipeline-api/technology-api/get-all "View all technology bundles for OpenPipeline configuration via the Dynatrace API.")
* [OpenPipeline API - GET technology processors](/docs/platform/openpipeline/reference/openpipeline-api/technology-api/get-technology "View the processors of a technology bundle for OpenPipeline configuration via the Dynatrace API.")

---

## platform/openpipeline/use-cases/processing-examples.md

---
title: OpenPipeline processing examples
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/processing-examples
scraped: 2026-02-18T21:20:57.277243
---

# OpenPipeline processing examples

# OpenPipeline processing examples

* Latest Dynatrace
* Tutorial
* 13-min read
* Updated on Jun 23, 2025

This article focuses on data processing scenarios and provides standalone examples of how to configure the OpenPipeline processors in order to achieve a result.

## Configure a new processor

To configure a new processor in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and chose a date type.
2. Find an existing pipeline or create a new one.
3. Select the stage.
4. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** and choose the processor.
5. Configure the processor by entering the required fields. Note that required fields vary based on the processor and are indicated in the user interface.
6. Save the pipeline.

## Examples

Expand the steps for the following examples to learn how to configure the processors.

### Fix unrecognized timestamp and loglevel based on a matched log source

A stored event from an application (`myLogSource`) in the log viewer is missing a proper timestamp and loglevel. You can retrieve this information from the source and parse it to achieve the following:

* Transform the unrecognized timestamp to a log event timestamp.
* Show a loglevel for the log.
* Extract the thread name from the log line into a new attribute (`thread.name`).

### Steps

1. Find the matching condition.

   1. Go to **Logs and events** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") and turn on **Advanced mode**.
   2. Enter the following DQL query to filter log data from the log source. Make sure to modify `myLogSource` with the log source.

      ```
      fetch logs



      | filter matchesValue(log.source, "myLogSource")
      ```
   3. Run the query and, when you're satisfied with the filter result, copy the `matchesValue()` function.

      ```
      matchesValue(log.source, "myLogSource")
      ```
2. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines** and select (or create) the pipeline for the log ingest source.
3. Configure a **DQL processor** in the **Processing** stage as follows.

   **Matching condition**

   The `matchesValue()` function that you copied.

   **Sample data**

   ```
   {



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "status":"NONE",



   "timestamp":"1650889391528",



   "log.source":"myLogSource",



   "loglevel":"NONE"



   }
   ```

   **DQL processor definition**

   ```
   parse content, "TIMESTAMP('MMMMM d, yyyy HH:mm:ss'):timestamp ' [' LD:'thread.name' '] ' UPPER:loglevel



   // Parses out the timestamp, thread name, and log level.



   // `TIMESTAMP` looks for the specific datetime format. The matched value is set as the existing timestamp log attribute.



   // `LD` matches any chars between literals `' ['` and `'] '`.



   // `UPPER` matches uppercase letters.



   // The remaining part of the content is not matched.
   ```
4. Save the pipeline.

Conclusion

The processed log record is displayed with metadata, including a `timestamp` and the `loglevel` attribute with proper values and the extracted attribute `thread.name`. Once new data is ingested, the processed records have a timestamp, a loglevel, and the thread name as separate attributes. You can visualize the new format, for example, in a notebook.

**Before**

```
{



"content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



"status":"NONE",



"timestamp":"1650889391528",



"log.source":"myLogSource",



"loglevel":"NONE"



}
```

**After**

```
{



"results":



[



{



"matched": true,



"record": {



"loglevel": "INFO",



"log.source": "myLogSource",



"thread.name": "myPool-thread-1",



"content": "April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



"timestamp": "2022-04-24T09:59:52.000000000Z",



"status": "NONE"



}



}



]



}
```

### Parse a field containing JSON as a raw string

A record has a field `content` (`String`) containing JSON input from which you want to parse out information. You can process specific fields, nested fields, or all fields, and treat them as plain text or bring them to top-level without knowing the schema of the JSON.

### Steps

Depending on the type of field you want to parse out, configure a **DQL** processor in the **Processing** stage with a **DQL processor definition** copied from one of the following:

Specific fields

Nested fields

All fields, without listing them

Any field from JSON, as plain text

All fields and bring them to top-level

```
parse content, "JSON{STRING:stringField:new.name}(flat=true)"



// Parses out a string field from raw record data into a standalone top-level attribute via a DPL JSON matcher.



// `flat=true` automatically creates attributes named as specified in the JSON. To rename the field, provide a new name inline after an additional `:`.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.name": "stringFieldValue"



}
```

```
parse content, "JSON{STRING:stringField, JSON {STRING:nestedStringField1}:nested}:parsedJson"



| fieldsAdd new.attribute1 = parsedJson[stringField]



| fieldsAdd new.attribute2 = parsedJson[nested][nestedStringField1]



| fieldsRemove parsedJson



// Parses out multiple string fields, including nested one, from raw record data into standalone top-level attributes, via a DPL JSON matcher.
```

Conclusion

You can process the record further; for example, you can create a top-level attribute from its nested fields.

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.attribute1": "stringFieldValue",



"new.attribute2": "NestedValue1"



}
```

```
parse content, "JSON:parsedJson"



| fieldsAdd new.field1 = parsedJson[intField],



new.field2 = parsedJson[stringField],



new.field3 = parsedJson[nested][nestedStringField1],



new.field4 = parsedJson[nested][nestedStringField2]



| fieldsRemove parsedJson



// Parses out all JSON fields without listing the attributes, via a DPL JSON matcher.
```

Conclusion

You can process the record further; for example, you can create a top-level attribute from its nested fields.

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.field1": "13",



"new.field2": "stringFieldValue",



"new.field3": "NestedValue1",



"new.field4": "NestedValue2"



}
```

```
parse content, """LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute"""



// Treats fields as plain text and renames any string that matches as specified.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"newAttribute": "stringField"



}
```

```
parse content, "JSON:parsedJson"



| fieldsFlatten parsedJson, prefix: "j"



// Parses out all fields without enumerating them and creates top-level fields from the JSON string without the need to enumerate the field names. It can be applied to multiple JSON objects.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"j.stringField": "stringFieldValue",



"j.intField": 13,



"j.nested":"{\"nestedStringField1\":\"NestedValue1\", \"nestedStringField2\":\"NestedValue2\"}"



}
```

### Parse out attributes with different formats

Applications log the user ID with different schemes (`user ID=`, `userId=`, `userId:` , `user ID =`). You can parse out attributes with different formats via a single pattern expression that uses the optional modifier (`?`) and `Alternative Groups`.

### Steps



To extract the user identifier as a standalone log attribute, configure a **DQL** processor in the **Processing** with the following **DQL processor definition**.

```
parse content, "



LD // Matches any text within a single line



('user'| 'User') // Matches specified literals



SPACE? // Matches optional punctuation



('id'|'Id'|'ID')



SPACE?



PUNCT?



SPACE?



INT:my.user.id"
```

Conclusion

With a single definition, you've extracted the user identifier from different log schemes and applied a standardized format that can be used in further stages.

**Before**

```
03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0
```

**After**

```
"my.user.id":"1234567"
```

### Use specialized DPL matchers

A JSON file contains information that you want to parse out and create new dedicate fields for it, based on the format. You can use [Dynatrace Pattern Language (DPL) matchers](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") for easier pattern building.

### Steps

To use DPL matchers to identify and create new dedicated fields for a timestamp, a loglevel, the IP address, the endpoint, and response code from the JSON file content, configure a **DQL** processor in the **Processing** stage with the following definition.

```
parse content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code"
```

Conclusion

You created new fields for the timestamp, a loglevel, IP address, endpoint, and response code, based on the format used in your JSON file.

**Before**

```
{



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"



}
```

**After**

```
{



"request": "GET /api/v2/logs/ingest HTTP/1.0",



"code": 200,



"loglevel": "INFO",



"ip": "192.168.33.1",



"timestamp": "2022-05-11T13:23:45.000000000Z",



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"



}
```

### Perform basic math on attributes

You can parse out specific values from a JSON file, perform calculations, and format the results by leveraging DQL functions and operators.

### Steps

Configure a **DQL** processor in the **Processing** stage with the following definition.

```
parse content, "LD 'total: ' INT:total '; failed: ' INT:failed" // Parses `total` and `failed` field values.



| fieldsAdd failed.percentage = 100.0 * failed / total // Calculates the failure percentage, formats the result to be a percentage, and stores it in a new attribute (`failed.percentage`).



| fieldsRemove total, failed // Removes temporary fields that are no longer needed from the JSON file.
```

Conclusion

You calculated the failure percentage based on the JSON content and created a new dedicated field.

**Before**

```
{



"content": "Lorem ipsum total: 1000; failed: 255",



}
```

**After**

```
{



"content": "Lorem ipsum total: 1000; failed: 255",



"failed.percentage": 25.5



}
```

### Add new attributes

You can add attributes that have static or dynamic values by leveraging different processors, with and without DQL queries.

### Steps

To add attributes, configure one of the following processors in the **Processing** stage.

Add fields

DQL

This processor doesn't leverage DQL queries. You can use it to add attributes with static values.

For example, you can add `company.team.name` with value `my-team` and `company.branch.name` with value `New York`. These key-value pairs will be added to all matched records.

Conclusion

You added new top-level fields that store the team name (`company.team.name`) and the branch location (`company.branch.name`) to the JSON file. The values remain static until they're manually modified.

**Before**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"company.team.name": "my-team",



"company.branch.name": "New York"



}
```

You can use it to add attributes with dynamic values. Use a definition that contains the `fieldsAdd` command, such as the following example:

```
fieldsAdd content.length = stringLength(content), content.words = arraySize(splitByPattern(content, "' '"))
```

Conclusion

You added new top-level fields that store the length (`content.length`) and number of words (`content.words`) of a JSON field. The values adapt to the content of the record.

**Before**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"content.length": "62",



"content.words": "9"



}
```

### Remove attributes

You can remove attributes by leveraging different processors, with and without DQL queries.

### Steps

To remove specific fields

* Configure a **Remove fields** processor in the **Processing** stage by providing the field names. This processor doesn't leverage DQL queries.
* Configure a **DQL** processor in the **Processing** stage by entering a definition that contains the `fieldsRemove` command, such as the following example:

  ```
  fieldsRemove redundant.attribute
  ```

Conclusion

**Before**

```
{



"redundant.attribute": "value",



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

### Rename attributes

You can rename attributes by leveraging different processors, with and without DQL queries.

### Steps

To rename an attribute of a matching record to a static value,

* Configure a **Rename fields** processor in the **Processing** stage by providing the field names that you want to be renamed and the new names. This processor doesn't leverage DQL queries.
* Configure a **DQL** processor in the **Processing** stage by entering a definition that contains the `fieldsRename` command, such as the following example:

  ```
  fieldsRename better_name = field // Renames a field to a static value
  ```

Conclusion

**Before**

```
{



"content": {"field": "Lorem ipsum"}



}
```

**After**

```
"content": {"better_name": "Lorem ipsum"}
```

### Drop records

You can drop ingested records at different stages by leveraging different processors.

### Steps

To drop an ingested record

* Before it's processed, configure a **Drop record** processor in the **Processing** stage by providing a matcher query.
* After it's processed, configure a **No storage assignment** processor in the **Storage** stage by providing a matcher query.

Conclusion

The matching records won't be stored in Grail.

### Mask data

You can mask parts of an attribute by leveraging `replacePattern` in combination with other DQL functions.

### Steps

In this scenario you want to mask part of an IP address. Configure a **DQL** processor in the **Processing** stage with one of the following definitions, depending on the part that you want to mask.

Given bits

Pattern

Repetitive patterns

Part of a field

The following example uses the [`ipMask`](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipMask "A list of DQL array functions.") function to set the last octet to the value `0`.

```
fieldsAdd ip = ipMask(ip, 24)
```

Conclusion

**Before**

```
{



"ip": "192.168.1.12"



}
```

**After**

```
{



"ip": "192.168.1.0"



}
```

The following example uses the [`replacePattern`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.") function together with DPL matchers and the [`Lookaround` behind modifier](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers#lookaround "Explore DPL syntax for optional controlling elements (modifiers).")(`<<`) to match a specific part (the last octet) of an IP address and set it to `xxx`.

```
fieldsAdd ip = replacePattern(ip, "<< (INT'.'INT'.'INT'.') INT", "xxx")
```

Conclusion

**Before**

```
{



"ip": "192.168.1.12"



}
```

**After**

```
{



"ip": "192.168.1.xxx"



}
```

The following example uses the [`replacePattern`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.") function to mask all IP addresses within a single field.

```
fieldsAdd content=replacePattern(content, "IPADDR", "xxx.xxx.xxx.xxx")
```

Conclusion

**Before**

```
{



"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194  dolor sit amet"



}
```

**After**

```
{



"content": "Lorem ipsum client_ip: xxx.xxx.xxx.xxx email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: xxx.xxx.xxx.xxx dolor sit amet"



}
```

The following example parses out the username of an email address and uses the [`replaceString`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replaceString "A list of DQL string functions.") function to replace it with a static value.

```
parse content, "LD 'email: ' LD:user '@'"



| fieldsAdd content = replaceString(content, user, "xxx")



| fieldsRemove user
```

Conclusion

**Before**

```
{



"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"



}
```

**After**

```
{



"content": "Lorem ipsum client_ip: 192.168.1.12 email: xxx@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"



}
```



## Related topics

* [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

---

## platform/openpipeline/use-cases/reduce-span-metric-cardinality.md

---
title: Reduce span-based and metric-based cardinality
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality
scraped: 2026-02-18T21:17:41.819174
---

# Reduce span-based and metric-based cardinality

# Reduce span-based and metric-based cardinality

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Feb 04, 2026

OpenPipeline processing allows you to normalize span and metric data to prevent high cardinality issues that can make aggregations and analysis unusable.

The following use cases show how to reduce cardinality in different views in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**:

* [Outbound calls](#outbound-calls)
* [Message processing](/docs/observe/application-observability/services/monitor-service-message-processing "Monitor service message processing")

## Outbound calls

### High cardinality in outbound calls

The **Outbound calls** tab displays aggregated metrics for external calls made by your service. High cardinality occurs when URLs contain unique identifiers in the path, such as `/users/12345` or `/orders/abc-def-123`, which leads to the creation of many distinct values.

Processing rules help you transform these into normalized patterns, such as `/users/*` or `/orders/*`, optimizing your outbound call data.

### Create an outbound calls normalization rule

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Go to the **Pipelines** tab. Select  **Pipeline** and enter a name (for example, `Outbound call normalization`) to create a new pipeline.
3. Go to **Processing** >  **Processor** > **DQL** and configure a new processing rule for reducing the cardinality of the URL.
4. Enter the following new DQL processor to normalize URLs:

   * **Name**: URL or any preferred name.
   * **Matching Condition**: The following condition matches all outbound HTTP calls.

     ```
     span.kind == "client" and isNotNull(url.full)
     ```
   * **DQL processor definition**

     ```
     fieldsAdd url.full.orig = url.full



     | fieldsAdd path_normalized = replacePattern(url.path, "UUIDSTRING", "[UUID]")



     | fieldsAdd path_normalized = replacePattern(path_normalized, "[/]LONG", "/[Number]")



     | fieldsAdd port = if(isNotNull(server.port), concat(":", server.port),   else:null)



     | fieldsAdd url.full = concat(url.scheme, "://", server.address, port, path_normalized)
     ```

### Enable the processor

Now that we have defined and saved a processor, we can enable the processor by connecting it to OpenPipeline via a new dynamic route so that your pipeline receives span data.

1. On the **Spans** page, go to the **Dynamic routing** tab.
2. Select  **Dynamic route**.
3. Define the dynamic route.

   * **Name**: The name you gave the processor earlier.
   * **Matching Condition**: The following matches all outbound HTTP calls.

     ```
     span.kind =="client" and isNotNull(url.full)
     ```
   * **Pipeline**: Select previously created pipeline from the list.
4. Select **Save**.

## Message processing

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** includes a **Message processing** view that aggregates metrics for messaging operations. High cardinality occurs when temporary queues are created with unique identifiers in their names (such as `amq.gen-6dggtCpu`, `async-job-2jrmsi5y`, or `orders-reply-2n68vy4g`), generating thousands of distinct queue names that make aggregations unusable.

Most instrumentations keep the cardinality of `messaging.destination.name` low by using non-standard fields like `messaging.temp.queue.hash` for high-cardinality data or by setting `messaging.destination.temporary`. However, when instrumentation doesn't follow these practices, OpenPipeline processing rules can normalize temporary queue names into patterns or flag them as temporary.

### High cardinality in message processing

Before implementing normalization rules, query your spans to identify messaging systems with high percentages of unique destination names.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and select  **Notebooks** to create a new notebook.
2. Select  **New section** > **DQL**.
3. Copy and paste the following query into the edit box and select  **Run**.

   ```
   fetch spans



   | filter isNotNull(messaging.system) and isNotNull(messaging.destination.name)



   | summarize count=count(), distinctCount=countDistinct(messaging.destination.name), by:{messaging.system, messaging.destination.temporary}



   | fieldsAdd cardinality_ratio = toDouble(distinctCount) / toDouble(count)
   ```
4. Examine the results for high cardinality ratios.

   Systems showing high cardinality ratios (above `0.5`) without `messaging.destination.temporary` set indicate queues that would:

   * Result in an excessive number of metrics with minimal analytical value.
   * Benefit from normalization as described below.

### Create a message processing normalization rule

You can use OpenPipeline processing rules to normalize temporary queue names into patterns or flag them as temporary.

To create a rule

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** and select **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Go to the **Pipelines** tab and create a new pipeline by selecting  **Pipeline** and entering a name (for example, `Queue handling`).
3. Choose whether to normalize temporary queue names into patterns or flag them as temporary.

   Flag as temporary

   Replace queue name

   On the **Processing** tab, select  **Processor** and choose **DQL**.

   To add/override the temporary queue flag, define the following new DQL processor:

   * **Name**: `Temporary queue selector` (or any name you like)
   * **Matching Condition**: The following matches all messaging spans that were detected as not temporary and match the specific destination pattern `odaRequestQueue*` that we want to override to be considered temporary.

     ```
     messaging.destination.temporary == false and



     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **DQL processor definition**: The only action to perform is to overwrite the existing value from false to true.

     ```
     fieldsAdd messaging.destination.temporary = true
     ```

   On the **Processing** tab, select  **Processor** and choose **Add fields**.

   To rename messaging destinations, define the following new DQL processor:

   * **Name**: `Destination renamer` (or any name you like)
   * **Matching Condition**: The following matches all spans that are related to messaging destinations starting with `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Add fields**: To replace the original content, you can simply add the field again with the corrected value. In this case, the original string that ends with consecutive numbers is replaced with a static string only containing the first, constant part of the destination name.

     Enter the following and then select **Add**:

     + **Name**: `messaging.destination.name`
     + **Value**: `odaRequestQueue`
4. Select **Save**.

### Enable the processor

Now that we have defined and saved a processor, we can enable the processor by connecting it to OpenPipeline via a new dynamic route, so that your pipeline receives span data.

1. Still on the **Spans** page, go to the **Dynamic routing** tab.
2. Select  **Dynamic route**.
3. Define the dynamic route.

   * **Name**: The name you gave the processor earlier.
   * **Matching Condition**: The following matches all spans that are related to messaging destinations starting with `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Pipeline**: Select from the list.
4. Select **Save**.

After applying these rules, queues with high cardinality will either have `messaging.destination.temporary` set to true or normalized names, significantly reducing metric cardinality in the message processing view. To verify this, see [How to identify high cardinality](#identify-high-cardinality) above.

---

## platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans.md

---
title: Extract metrics from spans and distributed traces
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans
scraped: 2026-02-18T21:21:10.164534
---

# Extract metrics from spans and distributed traces

# Extract metrics from spans and distributed traces

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Dec 23, 2025

This tutorial shows you how to extract metrics directly from your spans and distributed traces, via OpenPipeline, which provides flexible processing, enrichment, and routing at scale. New metrics can be calculated and derived based on any data available within the captured distributed trace, and the metrics can also be split by multiple dimensions, for example, a Kubernetes workload or a request attribute.

## Who this is for

This article is intended for app users building long-term dashboard-ready metrics from traces.

## What you will learn

How to set up OpenPipeline to extract a metric from a captured span via five examples you can adapt to your own services.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Dynatrace Platform Subscription (DPS) with [Traces powered by Grail (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.") capabilities.
* OpenPipeline permissions: `settings:objects:read` and `settings:objects:write`. To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
* [Distributed Tracing permissions](/docs/observe/application-observability/distributed-tracing/permissions#user-permissions-for-distributed-tracing "Manage permissions for Distributed Tracing powered by Grail.")

## Examples

### Requests to a workload split by Kubernetes pod

This example shows the new, recommended way to get [service instance-level insights](/docs/observe/application-observability/services-classic/analyze-individual-service-instances "Find out how you can perform a service-instance analysis."), a concept that is going away. Extract metrics from spans and split by real deployment dimensions like Kubernetes workload, pod, host, and more.

For common splits such as namespace, cluster or cloud region, use the out-of-the-box [primary Grail fields](/docs/semantic-dictionary/tags/primary-fields) already available in service metrics; you don't need a new metric.

1. Find the condition for the relevant spans in Notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **DQL**.
3. Use a DQL query to prototype your filters, fields, and groupings before you configure OpenPipeline. For example, to explore the spans that represent requests to the workload, you can use the following query:

   ```
   fetch spans



   | filter k8s.workload.name == "my-otel-demo-frontend" and span.kind == "server" and isNotNull(endpoint.name)



   | fields k8s.pod.name, dt.entity.service, endpoint.name, duration



   | limit 200
   ```

   Run in Playground

Understanding the filter conditions

* `span.kind == "server"` only keeps inbound service-handled requests and excludes client or internal spans.
* `isNotNull(endpoint.name)` ensures the span represents a request to an endpoint that Dynatrace considers in its endpoint detection rules, and that it isn't a muted request, for example.

2. Create a pipeline for metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Requests to my-otel-demo-frontend split by Kubernetes pod`
   * The matching condition:

     ```
     k8s.workload.name == "my-otel-demo-frontend"
     ```
   * The new metric keyâfor example, `span.my-otel-demo-frontend.requests_by_pod.count`
   * The metric dimensions:

     1. Select **Pre-defined** and choose `k8s.pod.name` and `k8s.pod.uid` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). These dimensions identify the pods where the workload is running. Other dimensions have also been pre-selected, such as `dt.entity.service`.
     2. Select **Save**.

You successfully created a new pipeline to extract a metric containing information about how many requests there were for the `my-otel-demo-frontend` workload and, because the metric has the pod as a dimension, you'll be able to split the requests by pod. The new pipeline is visible in the pipelines list.

3. Route spans to the pipeline

Create a dynamic route that funnels the spans you're interested in into the team's pipeline.

* One span will be routed to exactly one dynamic route. Spans can't be routed to multiple dynamic routes, so keep matching conditions precise and mutually exclusive.
* Dynamic routes are evaluated from top to bottom; as soon as a matching condition evaluates to "true", the span is routed through that dynamic route.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and specify:

   * A descriptive nameâfor example, `Spans for TeamA Cluster1 Namespace2`
   * The matching condition:

     ```
     k8s.cluster.name == "Cluster1" and k8s.namespace.name == "Namespace2"
     ```
3. Select **Add**.

You successfully created a new route. All spans of Kubernetes "Cluster1" and "Namespace2" are routed to the pipeline where a metric is extracted. The new route is visible in the routes list.

4. Query the metric

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **Metrics** > **Select a metric**.
3. Enter and select the new metric key (`span.my-otel-demo-frontend.requests_by_pod.count`).
4. Select  **Run**.

You've successfully extracted a metric to track requests to the `my-otel-demo-frontend` workload.

* You can use a Kubernetes pod dimension to split this metric.
* Spans are routed to the new pipeline; when the span belongs to the `my-otel-demo-frontend` workload (matching condition of the processor), the new pipeline extracts a metric containing the pod where the workload is running, in addition to other details.
* You can query the metric in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, or see it in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** or ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

### Number of books successfully sold per service



In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

Assumptions for the example

The number of books sold is captured as a [request attribute](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."), for example, `request_attribute.book_orders_count`. Request attributes are exposed under [`request_attribute.__attribute_name__`](/docs/semantic-dictionary/fields#request-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **System events** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Number of books successfully sold per service`
   * The matching condition:

     ```
     endpoint.name == "POST /book/{id}/checkout" and isNotNull(request_attribute.book_orders_count) and request.is_failed != true
     ```
   * For the measurement type, select **Custom**, as we're not measuring durations.
   * The field name from which to extract the value (`request_attribute.book_orders_count`).
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.books.sold.count`.
   * The metric dimensions. You can use the pre-selected dimensions, as `dt.entity.service` is selected by default.
4. Select **Save**.

You successfully created a new processor to extract a metric containing information about the number of books successfully sold, and, because the metric has the `dt.entity.service` service as a dimension, you'll be able to split the metric per service.

### Top database calls per service and query group

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

For this example metric, we want to know the top database operations or commands executed across our services. For example, the MongoDB command name, SQL keyword, Redis command name, together with the name of the target database (`db.namespace`).

We're not creating a metric for the actual `db.query.text` being executed (for example, `SELECT * FROM user_table`), as that would result in a metric with a very high cardinality.

To see a list of the actual queries being executed by your services, use the [database query performance analysis in the Services app](/docs/observe/application-observability/services/services-app#database-query-performance-analysis "Maintain centralized control over service health, performance, and resources with the Services app.").

1. Add a new query group attribute to database spans

We'll add a new attribute to our database spans that contains the query group we're interested in having in our metric: `db.operation.name +Â db.namespace`. We can then use the newly created attribute in our metric extraction step.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To add the new attribute to incoming database spans, go to **Processing** > **+ Processor** > **DQL** and define the processor by entering:

   * A descriptive nameâfor example, `Construct low cardinality db.query.group`
   * The matching condition:

     ```
     isNotNull(db.operation.name) and isNotNull(db.namespace)
     ```
   * The DQL processor definition:

     ```
     fieldsAdd db.query.group = concat(db.operation.name, " ", db.namespace)
     ```

Conclusion

You added a new `db.query.group` attribute to the database spans that you can now use to create your metric.

**Before**

```
{



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

**After**

```
{



"db.query.group": "SELECT books",



"db.namespace": "books",



"db.operation.name": "SELECT",



"db.query.text": "select b1_0.id,b1_0.author,b1_0.title from books b1_0 where b1_0.title=?"



}
```

2. Use the new attribute in the metric extraction

1. Go to **Metric extraction** >  **Processor** > **Sampling aware counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Database calls per service and query group`
   * The matching condition:

     ```
     isNotNull(db.query.group)
     ```
   * The field name from which to extract the value (`request_attribute.book_orders_count`).
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.service.db_calls_by_group.count`.
   * The metric dimensions. Select **Custom** and choose `db.query.group` as the **Field name on record**. For the service dimension, `dt.entity.service` is selected by default.
2. Select **Save**.

You successfully created a new processor to extract a metric containing information about the database calls per service and query group.

3. Query the top 10 values

In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** or ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, use [Explore interface for Metrics](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-metrics "Explore your data with our point-and-click interface.") to plot the `span.service.db_calls_by_group.count`:

* Split by `db.query.group` and `dt.entity.service`
* Sort by the `value.A` metric in a `DESC` order
* Use [**Limit**](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#metric-limit "Explore your data with our point-and-click interface.") `10` to display the top 10 results

![Explore metrics - Top 10 queries](https://dt-cdn.net/images/screenshot-2025-12-23-at-18-23-49-2414-9876a1a980.png)

### CPU time per service endpoint

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure a value metric extraction, **Metric extraction** >  **Processor** > **Sampling aware value metric** and define the processor by entering:

   * A descriptive nameâfor example, `CPU time per service endpoint`
   * The matching condition:

     ```
     request.is_root_span == true
     ```

     This condition ensures that weâll be capturing the first span of a request within a service. That is, the span where endpoint detection rules are evaluated.
   * For the measurement type, select **Custom**, as we're not measuring durations.
   * The field name from which to extract the value (`span.timing.cpu`). This attribute tracks the overall CPU time spent executing the span, including the CPU times of child spans that are running on the same thread on the same call stack.
   * The sampling options enabled (leave as is), so that the metric extraction is sampling aware.
   * The new metric keyâfor example, `span.request.cpu_time`.
   * The metric dimensions:

     1. Select **Pre-defined** and choose `endpoint.name` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). Other dimensions also get pre-selected, such as `dt.entity.service`.
     2. Select **Save**.

You successfully created a new processor to extract a metric containing information about the CPU time consumed per endpoint. The CPU-time field is measured in nanoseconds.

### Response time for outbound calls to paypal.com per service, as measured by the caller



Upcoming features

Histogram metric extraction support is coming soon.

Later in 2026, Dynatrace will provide out-of-the-box metrics for third-party calls, as part of the modernization of [Monitor third-party services](/docs/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Configure how Dynatrace should monitor third-party services.").

In this example, we describe the creation of the pipeline and the metric-extraction processor. For detailed steps, follow the approach of the [workload split by Kubernetes pod example](#workload-requests-pod), but adapt the filter queries and routing.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans** > **Pipelines**.
2. Select an existing pipeline or create a new one. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `TeamA Span metrics from Services`.
3. To configure a histogram metric extraction, go to **Metric extraction** >  **Processor** > **Sampling aware histogram metric** and define the processor by entering:

   * A descriptive nameâfor example, `Response time for outbound calls to paypal.com per service, as measured by the caller`.
   * The matching condition:

     ```
     span.kind == "client" and matchesValue(server.address, "*.paypal.com")
     ```
   * **Measurement** set to **Duration**.
   * The new metric keyâfor example, `span.outbound_paypal_requests.response_time`.
   * The metric dimensionsâyou can use the pre-selected dimensions, as `dt.entity.service` is selected by default.
4. Select **Save**.

You successfully created a new processor to extract a metric containing the response time for outbound calls to paypal.com, as measured by the caller. Also, because the metric has the calling service (`dt.entity.service`) as a dimension, you'll be able to split the metric per service.

---

## platform/openpipeline/use-cases/tutorial-log-processing-pipeline.md

---
title: Parse log lines and extract a metric
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline
scraped: 2026-02-18T21:20:58.589224
---

# Parse log lines and extract a metric

# Parse log lines and extract a metric

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Jun 23, 2025

This tutorial shows you how to parse important information from log lines into separate fields and extract a metric from it. Dedicated fields help with querying and extracting metrics, allowing you to show long-term data on a dashboard.

## Who this is for

This article is intended for administrators controlling log ingestion configuration, data storage and enrichment, and transformation policies.

## What you will learn

In this article, you will learn to narrow thousands of log lines to just the log lines of a user adding a product to their cart, transform the raw input into structured results with new dedicated fields (`userId`, `productId`, and `quantity`), and extract a metric measuring the quantity per product.

The following log line is an example of the raw data this article focuses on.

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* Dynatrace SaaS environment powered by Grail and AppEngine.
* Either [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license that includes [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capabilities or [DDUs for Log Management and Analytics](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.").

## Steps

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Find the relevant log lines in Grail**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#logs "Configure OpenPipeline processing for log lines.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure a pipeline for parsing and metric extraction**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#pipeline "Configure OpenPipeline processing for log lines.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Route data to the pipeline**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#route "Configure OpenPipeline processing for log lines.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Verify the configuration**](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline#verify "Configure OpenPipeline processing for log lines.")

### Step 1 Find the relevant log lines in Grail

1. Go to **Notebooks**.
2. Use a DQL query to narrow down to the relevant log lines.

   The following example query fetches the first 250 logs from `online-boutique` containing `AddItemAsync` that have a timestamp.

   ```
   fetch logs



   | filter k8s.namespace.name == "online-boutique"



   | filter matchesValue(content, "AddItemAsync*")



   | fields timestamp, content



   | limit 250
   ```

   ![Find relevant logs lines via DQL query](https://dt-cdn.net/images/log-processing-dql-query-1200-d1966f2ef5.png)

### Step 2 Create a pipeline for parsing and extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. To create a new pipeline, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** and enter a name (`Online Boutique`).
3. To configure parsing

   1. Go to **Processing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **DQL** and define the processor by entering:

      * A descriptive name (`Parse product, user, and quantity`).
      * A matching condition.

        In our example, the matching condition is

        ```
        matchesValue(content, "AddItemAsync*")
        ```
      * A processor definition.
        In our example, the processor definition

        ```
        parse content, "\"AddItemAsync called with userId=\"LD:userId\", productId=\"LD:productId, \"quantity=\"INT:quantity"
        ```
   2. Optional To verify the processor

      1. Enter a data sample.
         In our example, the sample data is

         ```
         {



         "content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4", "k8s.namespace.name": "online-boutique"



         }
         ```
      2. Select **Run sample data**.
      3. Observe the preview result and, if necessary, modify the matching condition and/or the processor definition.

         ![Parse log data into a structured format via OpenPiepeline](https://dt-cdn.net/images/log-processing-parsing-processor-1920-44ef93f030.png)
4. To configure metric extraction, go to **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Value metric** and define the processor by entering:

   * A descriptive name (`Extract quantity by product for AddItem`).
   * The same matching condition you used for parsing.
   * The field name from which to extract the value (`quantity`).
   * A metric key for the field (`add_item_product_quantity_by_product`).
   * A metric dimension

     1. Select **Custom** dimensions.
     2. Enter a metric dimension (`productId`).
     3. Select **Add**.

   ![Extract a metric via OpenPipeline](https://dt-cdn.net/images/log-processing-metric-extraction-1200-f4550a4cd6.png)
5. Select **Save**.

You've successfully configured a new pipeline with two processorsâone for parsing and one for metric extraction. The new pipeline is in the pipeline list.

### Step 3 Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. To create a new route, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** and specify:

   * A descriptive name (`Online Boutique`).
   * A matching condition.

     In our example, the matching condition is

     ```
     k8s.namespace.name == "online-boutique"
     ```
   * The pipeline containing the processing instructions (`Online Boutique`).

   ![Configure a dynamic route for log processing in OpenPipeline](https://dt-cdn.net/images/log-processing-dynamic-route-1200-ef7c422264.png)
3. Select **Add**.

You've successfully configured a new route. The new route is in the routes' list.

### Step 4 optional Verify the configuration

1. Generate an access token.

   1. Go to **Access Tokens** > **Generate new token** and specify:

      * A token name.
      * The token scopeâ**Ingest logs** (`logs.ingest`).
   2. Select **Generate token**.
   3. Select **Copy** and then paste the token to a secure location. It's a long string that you need to copy and paste back into Dynatrace later.
2. Send a log record.

   Run the following sample command to send a log record to your environment endpoint `/api/v2/logs/ingest` via `POST` request.

   The sample command indicates a JSON content type and provides the JSON event data using the `-d` parameter. Make sure to substitute

   * `{your-environment-id}` with your environment ID.
   * `<your-API-token>` with the token you generated.

   ```
   curl -i -X POST "https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest" \



   -H "Content-Type: application/json" \



   -H "Authorization: Api-Token <your API token>" \



   -d "{\"k8s.namespace.name\":\"online-boutique\",\"content\":\"AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4\"}"
   ```

   Your request is successful if the output contains the 204 response code.
3. Verify parsing by querying the log record and the metric in a notebook.

   1. Open an existing or new notebook in **Notebooks**.
   2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** and add two new sections with a DQL query input field.

      * To verify the log record, add a section with a DQL query input field.

        In our example, the DQL query is

        ```
        fetch logs



        | filter userId == "6517055a-9fcc-4707-8786-e33a767a90c4"
        ```
      * To verify the metric, add another section with a DQL query input field.

        In our example, the DQL query is

        ```
        timeseries avg(log.add_item_product_quantity_by_product), by:{productId}



        | fieldsAdd sum = arraySum(`avg(log.add_item_product_quantity_by_product)`)



        | fields sum, productId
        ```

      ![Verify OpenPipeline processing output](https://dt-cdn.net/images/log-processing-verification-1200-4ccb7afb6a.png)

## Conclusion



You have successfully created a pipeline to parse log data and extract a metric. The log records of the user adding a product to their cart are transformed from raw information to structured information according to your rules. They now specify dedicated fields (`userId`, `productId`, and `quantity`), from which you extracted a new metric for better analytics.

**Raw log record**

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

**Structured log record**

```
{



"k8s.namespace.name": "online-boutique",



"quantity" : 4,



"productId": "OLJCESPC7Z",



"userId": "6517055a-9fcc-4707-8786-e33a767a90c4",



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"timestamp": "2024-06-19T15:29:54.125000000Z"



}
```

---

## platform/openpipeline/use-cases/tutorial-system-events.md

---
title: Extract a metric to track system events
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-system-events
scraped: 2026-02-18T21:21:01.096721
---

# Extract a metric to track system events

# Extract a metric to track system events

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jun 23, 2025

Dynatrace produces system events for system activity in your environment, for example, when an app is installed, updated, and uninstalled. You can extract a metric via OpenPipeline and track how many app updates occurred in your environment.

## Who this is for

This article is intended for administrators and app users.

## What you will learn

In this article, you'll learn how to set up OpenPipeline to extract a metric to monitor system events frequency.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* [Latest Dynatrace](/docs/platform "Dynatrace is an all-in-one platform that's purpose-built for a wide range of use cases.") environment
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license with [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") capabilities
* `storage:system:read` user permission

## Steps

1. Find the condition for the relevant records

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **DQL**.
3. Enter a DQL query to fetch the relevant records.

   App lifecycle events are audit events produced by Dynatrace AppEngine [Registryï»¿](https://developer.dynatrace.com/develop/sdks/client-app-engine-registry/). The following example query fetches app lifecycle events and summarizes the results by event type.

   ```
   fetch dt.system.events



   | filter event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"



   | summarize by:{event.type}, count()
   ```

   Run in Playground
4. To filter only by app updates, select **app.updated** >  **Filter**.

You found the condition that identifies app updates (`event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY" AND event.type == "app.updated"`).

2. Create a pipeline for metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **System events** > **Pipelines**.
2. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `App LifeCycle-Updates`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Frequency`
   * The matching condition `event.type == "app.updated"`
   * The new metric keyâfor example, `apps.updates`
   * The metric dimensions:

     1. Select **Pre-defined** and choose `resource` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). This dimension identifies the ID of the app from which the update originates.
     2. Select **Custom** and enter:

        + **Field name on record**: A custom dimension that further defines your metricâfor example, `details.app.type`.
        + **Dimension name**: An optional field that can be used in the case of nested fields, or if you want to give the dimension an alias.
     3. Select **Add**.
4. Select **Save**.

You successfully created a new pipeline to extract a metric containing information about the event's source and further app details. The new pipeline is visible in the pipelines list.

3. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **System events** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and specify:

   * A descriptive nameâfor example, `App LifeCycle`
   * The matching condition

     ```
     event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"
     ```
   * The pipeline containing the processing instructions (`App LifeCycle-Updates`)
3. Select **Add**.

You successfully created a new route. All app lifecycle events are routed to the pipeline where a metric is extracted only for app updates. The new route is visible in the routes list.

4. Query the metric

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **Metrics** > **Select a metric**.
3. Enter and select the new metric key (`dt.system.events.apps.updates`).
4. Select  **Run**.

## Conclusion

You successfully extracted a metric to track app update frequency. All new app lifecycle events are routed to a new pipeline. When a record is an app update, the new pipeline extracts a metric containing the ID of the application from which the update originates and further app details. You can query the metric in Dashboards and Notebooks.

## Related topics

* [System event models](/docs/semantic-dictionary/model/dt-system-events "Get to know the Semantic Dictionary models related to system events.")

---

## platform/openpipeline/use-cases/tutorial-technology-processor.md

---
title: Process logs with technology bundle parsers
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-technology-processor
scraped: 2026-02-18T21:21:07.509280
---

# Process logs with technology bundle parsers

# Process logs with technology bundle parsers

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Aug 06, 2025

OpenPipeline offers pre-defined technology bundles. These are libraries of parsers (processing rules), to structure technology-specific logs according to the Dynatrace Semantic Dictionary. The parser library supports a broad range of technologiesâincluding well-known data formats, popular third-party services, and cloud providersâsuch as, AWS Lambda, Python, Cassandra, and Apache Tomcat.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

## Who this is for

This article is intended for administrators and app users.

## What you will learn

In this article, you will learn how to parse logs with technology bundle in OpenPipeline and analyze them in Notebooks.

## Before you begin

Prior knowledge

* [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* [Latest Dynatrace](/docs/platform "Dynatrace is an all-in-one platform that's purpose-built for a wide range of use cases.") environment
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license with [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") capabilities

## Steps

1. Create a pipeline for processing

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `Syslog - Pipeline`.
3. To configure processing, go to **Processing** >  **Processor** > **Technology bundle** and choose the necessary bundle. For example, the **Syslog** bundle.

   You can add multiple technology bundles on one pipeline, so you don't have to create a pipeline and a dynamic routing each time.
4. Copy the technology matching condition.

   You can customize the technology matching condition to match your needs through OpenPipeline. See [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
5. Select **Save**.

You successfully configured a new pipeline with a processor to structure syslog logs according to pre-defined rules that match Dynatrace Semantic Dictionary. The new pipeline is in the pipeline list.

2. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and enter:

   * A descriptive nameâfor example, `Syslog`
   * The matching condition you copied. This matching condition is customizable. For example, you can set it as `true` and all logs will go through that pipeline, if it's well positioned on the list.
   * The pipeline containing the processing instructions (`Syslog - Pipeline`)
3. Select **Add**.
4. Make sure to place the new route in the correct position on the list. Routes are evaluated from top to bottom. Data is dynamically routed into a pipeline according to the first applicable matching condition. Routed data is not evaluated against any subsequent conditions.
5. Select **Save**.

You successfully configured a new route. All syslog logs are routed to the pipeline for processing. The new route is in the route list.

To learn more about dynamic routing, see [Route data](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

3. Analyze structured logs

Once logs are processed according to the technology bundle, several attributes are extracted from the log content into new fields that match Dynatrace Semantic Dictionary. On top of that, technology bundles extract other attributes from logs so you can build your own [Custom alerts](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts "Learn more about custom alerts and the logic behind raising them."), [Metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis."), and [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

Log enrichment

Using parsers helps you to better structure and enrich your logs. See this comparison:

**Without parsing**

```
{



"dt.openpipeline.source": "extension:syslog",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!"



}
```

**With parsing**

```
{



"syslog.severity": 0,



"syslog.version": 1,



"syslog.priority": 24,



"syslog.facility": 3,



"syslog.message": "Critical system failure: Kernel panic detected, immediate attention required!",



"content": "<24>1 2025-08-06T14:50:30.123Z core-router-01.example.com kernel 9999 ID01 Critical system failure: Kernel panic detected, immediate attention required!",



"syslog.proc_id": "9999",



"dt.openpipeline.source": "extension:syslog",



"loglevel": "EMERGENCY",



"syslog.message_id": "ID01",



"syslog.hostname": "core-router-01.example.com",



"syslog.appname": "kernel",



"timestamp": "2025-08-06T14:50:30.123000000Z",



"status": "ERROR"



}
```

You can easily filter logs by status, application, or attributes specific to the technology, as shown in the examples below.

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open a new or existing notebook.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** and enter one of the following queries

   * Fetch syslog warn logs

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog"



     | filter status == "WARN"



     | sort timestamp desc
     ```

     Result:

     timestamp

     syslog message

     status

     syslog.appname

     syslog.priority

     `2024-10-01T11:56:27.743113056+02:00`

     `TCP: eth0: Driver has suspect GRO implementation, TCP performance may be compromised.`

     WARN

     kernel

     4

     `2024-10-01T11:56:15.248382315+02:00`

     `Network latency exceeded threshold: 250ms`

     WARN

     net-monitor

     4

     `2024-10-01T11:52:32.464416725+02:00`

     `Disk space usage exceeded 80% on /dev/sda1`

     WARN

     disk-monitor

     28
   * Group syslog logs by application

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize totalCount = count(), by: {syslog.appname}



     | sort totalCount desc
     ```

     Result:

     ![Group syslog logs by application](https://dt-cdn.net/images/syslog-byapp-1000-25aedf7940.png)
   * Sort applications by the percentage of syslog error logs

     ```
     fetch logs



     | filter dt.openpipeline.source == "extension:syslog" and isNotNull(syslog.appname)



     | summarize TotalCount = count(), Count = countIf(status == "ERROR"), by: {syslog.appname}



     | fieldsAdd Percentage = (Count * 100 / TotalCount)



     | sort Count desc



     | fieldsRemove TotalCount
     ```

     Result:

     ![Sort applications by the percentage of syslog error logs](https://dt-cdn.net/images/syslog-error-995-e3d5fe605b.png)

To see the results of the queries, you need to have everything configured correctly.

## Conclusion

You successfully structured syslog logs according to pre-defined processing rules in OpenPipeline. Incoming records that match the routing conditions are routed to the syslog pipeline, where new attributes specific to the syslog technology are extracted. The new attributes match Dynatrace Semantic Dictionary allowing for smooth analysis. You can filter syslog logs in Notebooks and get the most out of your structured logs.

## Related topics

* [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.")
* [Filter logs](/docs/secure/investigations/filter-logs "Narrow down data to relevant entries in Investigations.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

---

## platform/openpipeline.md

---
title: OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline
scraped: 2026-02-18T21:16:09.469508
---

# OpenPipeline

# OpenPipeline

* Latest Dynatrace
* Overview
* 1-min read
* Updated on Dec 19, 2025

Dynatrace version 1.295+

OpenPipeline is the Dynatrace data handling solution to seamlessly ingest and process data from different sources, at any scale, and in any format in the Dynatrace Platform.

## Use cases

* Configure ingestion and processing of different configuration scopes, such as logs and events, via a unified solution.
* Scale data management across teams by controlling access and targeted technologies.
* Ensure secure and compliant sensitive data handling.
* Enrich and contextualize data via customizable data processing.
* Optimize data quality and cost control.

## Concepts

[### Data flow

Learn how data flows from ingestion to storage via Dynatrace OpenPipeline.](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")[### Processing

Learn the core concepts of Dynatrace OpenPipeline processing.](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

## Getting started

[### How to ingest data (events)

How to ingest data for a configuration scope in OpenPipeline.](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")[### Configure processing

Configure ingest sources, routes, and processing for your data via OpenPipeline.](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

### Processing examples

* [Reduce span-based and metric-based cardinality](/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality "Reduce span- and metric-based cardinality")
* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")
* [Extract metrics from spans and distributed traces](/docs/platform/openpipeline/use-cases/tutorial-extract-metrics-from-spans "Extract metrics directly from your spans and distributed traces via OpenPipeline.")
* [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.")
* [Extract a metric to track system events](/docs/platform/openpipeline/use-cases/tutorial-system-events "Learn how to extract a metric to track system events with OpenPipeline.")
* [Extract a metric from user events](/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-events "Turn user events into actionable insights by extracting custom metrics for long-term analysis.")
* [Extract a metric from user sessions](/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-sessions "Discover how to build custom metrics from user sessions, illustrated by a customer conversion metric.")

## Reference

[### Ingest API

Reference material on ingestion APIs for the configuration scopes supported by OpenPipeline.](/docs/platform/openpipeline/reference/api-ingestion-reference "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")[### OpenPipeline API

Reference material for configurations via OpenPipeline API.](/docs/platform/openpipeline/reference/openpipeline-api "Configure OpenPipeline capabilities of ingest source, routing, and processing via API.")[### Limits

Reference material on OpenPipeline limits.](/docs/platform/openpipeline/reference/limits "Reference limits of Dynatrace OpenPipeline.")

---
