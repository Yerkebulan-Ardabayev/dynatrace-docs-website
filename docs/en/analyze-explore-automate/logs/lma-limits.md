---
title: Log Management and Analytics default limits
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-limits
scraped: 2026-02-28T21:20:14.580386
---

# Log Management and Analytics default limits

# Log Management and Analytics default limits

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Feb 02, 2026

This page lists default limits for the latest version of Dynatrace Log Management and Analytics. The current limitations apply to both log file ingestion and log ingestion via the Log ingestion API.

## Log ingestion limits

The table below summarizes the most important default limits related to log ingest. All presented limits refer to UTF-8 encoded data.

| Type | Limit | Description |
| --- | --- | --- |
| Content | 10 MB[1](#fn-1-1-def) | The maximum size of log entry body |
| Attribute key | 100 bytes | The key of an attribute value |
| Attribute value length | 32 kB | The maximum length of an attribute value |
| Number of log attributes | 500 | The maximum number of attributes a log can contain |
| Log events per minute | No limit | The maximum number of log events in a minute |
| Log age | 24 hours | The maximum age of log entries when ingested |
| Logs with future dates | No restriction[2](#fn-1-2-def) | How far into the future log entries can reach |
| Values per attribute | 32 values | The maximum number of individual values an attribute can contain |
| Request size [3](#fn-1-3-def) | 10 MB | The maximum size of the payload data |
| Number of log records | 50,000 records | The maximum number of log records per request |
| Nested objects | 5 levels | The maximum number of levels ingested with nested objects |
| Extracted log attribute | 4,096 bytes | When logs are added to the event template, log attributes are truncated to 4096 bytes |

1

The content limit is lower (512 kB) for logs routed to the **Classic pipeline**.

2

There is no ingestion limitation on log entries with future timestamps, but entries with timestamps further than 10 minutes into the future have their timestamps set to the moment of ingestion.

3

When it comes to request size, the Log Ingestion API endpoints accept requests up to 10 MB. However, after the initial processing, the batch may grow in size. If it exceeds 16 MB after processing, it will be rejected with the following 413 error: `Message size limit exceeded after preprocessing on ingest endpoint`. To avoid this issue, ingest smaller batches of log records to stay within the size limits.

A log request may increase in size due to the following reasons:

* Missing content attributes in ingested log records: If a log ingested through the Log Ingestion API endpoint does not have a content-like attribute, this attribute will be added after ingestion.
* For logs ingested via the OTLP endpoint, resource and scope attributes are copied to each individual log record.

Check your access to OpenPipeline in [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

## Log ingestion latency

Logs ingested via OneAgent are typically ready for analysis between a few seconds and 90 seconds (30 seconds on average).

Logs ingested by API are available for analysis in Dynatrace after 10 seconds on average.

Occasionally, a higher latency might occur by data loss prevention mechanisms like retransmissions, buffering, or other factors that can introduce delays.

## Log record accepted time range

The following rules apply to all log event sources, such as OneAgent and the generic log ingestion API.

## Log metrics

Number of metrics is limited to:

* `100,000` (`1000` per pipeline x `100` pipelines) for Log Management and Analytics powered by Grail with OpenPipeline
* `1000` for Log Management and Analytics powered by Grail without enabled OpenPipeline
* `50` in other cases.

## Log ingestion API request objects

In addition to generic Dynatrace API limitations ([Dynatrace API - Access limit](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")) the following log ingestion API specific limits apply:

* `LogMessageJson` JSON object. See [Ingest JSON and TXT logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Understand how JSON and TXT logs are processed, whether in flattened or raw mode.") for the complete list of keys and their descriptions.
* `LogMessageOTLP` OpenTelemetry Protocol object. See [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

## Limits for your log autodiscovery when using OneAgent

Log files in OneAgent:

* cannot be deleted earlier than a minute after creation.
* must be appended (old content is not updated).
* must have text content.
* must be opened constantly (not just for short periods of adding log entries).
* must be opened in write mode.
* must not be smaller than the configured size threshold (default: 500 bytes) to be checked for binary content.

The default maximum number of log sources per process group instance is 200. This value is configurable via the **Maximum number of log sources per process group instance** option in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log Monitoring** > **Advanced log settings**.

In standard environments, OneAgent log module supports up to 10,000 files in one directory with logs and 200 MB of new log content per minute. If you have more data, especially a higher level of magnitude, there's a high chance that the OneAgent log module supports it. Contact the Dynatrace support team to review your setup beforehand.

In special cases, such as very poor hardware performance, the OneAgent log module's limitations might be more strict.

## Log rotation limits

Scenarios that are not supported in the rotated log monitoring process include:

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Active Gate throughput

If you are using the SaaS endpoint, you don't have to worry about the Active Gate throughput. The throughput is the same as for Grail.
If you use Environmental Active Gate, the throughput is 3.3GB/min with RTT <= 200 ms.