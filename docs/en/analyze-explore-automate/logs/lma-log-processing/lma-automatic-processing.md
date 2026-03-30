---
title: Automatic log processing at ingestion
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-automatic-processing
scraped: 2026-03-05T21:33:12.923279
---

# Automatic log processing at ingestion


* Latest Dynatrace
* Explanation
* 2-min read
* Published Dec 08, 2025

Automatically ingest and process logs with OneAgent, Ingest JSON and TXT logs, or Dynatrace OTLP API endpoints for seamless log management.

Dynatrace applies a unified processing approach at ingestion.
This approach ensures compatibility when switching integration mechanismsâsuch as transitioning from a log shipper integration to OneAgentâwithout requiring any additional or, in some cases, minimal configuration.

Logs are automatically prepared for processing, as the system is preconfigured to handle key attributes such as `severity` and `timestamp`.
Furthermore, log payload parsing and supported file formatsâJSON, OTLP, and TXTâare already accounted for, requiring no manual intervention.

### Overview of integrations to ingest and process logs

Depending on the log integration, the automatic processing is tailored to accommodate different formats.

#### OneAgent (recommended integration)

OneAgent is the preferred method for log ingestion.
It provides the highest observability value and eliminates the need for manual parsing configuration.
No additional configuration is required.
If you have specific needs, you have the option to customize your experience.

You can make use of the following out-of-box options:

* Support for JSON logs data format.
* Extract automatically the `severity` attribute using Automatic log enrichment for already enriched data.
* Extract automatically the [topology context](../lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa.md#autoattributes "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") to ensure logs are tied to relevant entities.
* Timestamp extraction is supported for listed Supported timestamp formats with no configuration.

For optimal automatic log processing, you can make use of the following capabilities:

* **Timestamp/Splitting patterns** for Timestamp/splitting configuration.
* Connect log data seamlessly to traces for faster problem resolution and effortless context switching.

#### Log Monitoring API - JSON and TXT endpoint

Log Monitoring API automatically process ingested logs by:

* Checking the supported **Severity** and **Timestamp** keys in [`LogMessageJson` object](../lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs.md#data-transformation-and-automatic-json-parsing "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.").
* JSON logs are processed on Log Monitoring API endpoints to preserve the original log structure.
  For more information on data models, see Ingest JSON and TXT logs.

#### Dynatrace OTLP API

Dynatrace OTLP API automatically process ingested logs by:

* Checking the supported [`severity` and `timestamp`](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md#semantic-attributes "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.") keys.
* Structured logs are processed on Dynatrace OTLP API endpoints to preserve the original log structure.
  For more information on data models, see [Ingest OTLP logs](../../../ingest-from/opentelemetry/otlp-api/ingest-logs.md#otlp-structured-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Related topics

* Log processing with OpenPipeline