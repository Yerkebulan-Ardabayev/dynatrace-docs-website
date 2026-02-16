---
title: OpenPipeline limits
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/limits
scraped: 2026-02-16T09:16:33.921309
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