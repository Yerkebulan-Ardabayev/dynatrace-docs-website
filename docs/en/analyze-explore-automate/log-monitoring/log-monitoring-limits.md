---
title: Log Monitoring default limits (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits
scraped: 2026-02-19T21:20:44.683553
---

# Log Monitoring default limits (Logs Classic)

# Log Monitoring default limits (Logs Classic)

* 1-min read
* Updated on Feb 02, 2026

Log Monitoring Classic

This page lists default limits for the latest version of Dynatrace Log Monitoring.

The current limitations apply to both log file ingestion and generic log ingestion via API.

## Log ingestion limits

The table below summarizes the most important default limits related to log ingest. All presented limits refer to UTF-8 encoded data.

| Type | Limit | Description |
| --- | --- | --- |
| Content | 8 kB | The maximum size of log entry body |
| Attribute key | 100 bytes | The key of an attribute value |
| Attribute value length | 250 bytes | The maximum length of an attribute value |
| Number of log attributes | 50 | The maximum number of attributes a log can contain |
| Log events per minute | 1M/min | The maximum number of log events in a minute |
| Log age | 24 hours | The maximum age of log entries when ingested |
| Logs with future dates | No restriction[1](#fn-1-1-def) | How far into the future log entries can reach |
| Values per attribute | 32 values | The maximum number of individual values an attribute can contain |
| Request size | 10 MB | The maximum size of the payload data |
| Number of log records | 50,000 records | The maximum number of log records per request |
| Nested objects | 5 levels | The maximum number of levels ingested with nested objects |

1

There is no ingestion limitation on log entries with future timestamps, but entries with timestamps further than 10 minutes into the future have their timestamps set to the moment of ingestion.

## Unsupported autodiscovery scenarios

Scenarios that are not supported in the rotated log autodiscovery process include:

* Rotated log generation with a directory change. This process could lead to the creation of numerous non-aggregated and/or incomplete logs, as well as to resource overuse.
* Rotated log generation with immediate compression, where the application addresses a file with the same name. If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed.
  Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log creation.

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

Type

Description

Rotated log generation with a directory change

The potential consequence is the creation of duplicates and/or incomplete logs.

Rotated log generation with immediate compression

If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed. Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log ingest. There should be at least one uncompressed rotated file.

Rotated log generation with queue logic

The oldest log records are removed whenever new content is added to a file, resulting in a relatively constant log file size. This scenario can be easily replaced with a supported rotation scheme by, for example, starting a new file when the current file reaches a predefined size.

## Log record accepted time range

The following rules apply to all log event sources, such as OneAgent and the generic log ingestion API.

Log record timestamp

Description

The current time minus 24 hours for log records.

The event is dropped if the log event contains a timestamp before the current time minus 24 hours.
If the record is ingested via the generic Log Ingestion API, it can return the following:

`400` - if all log events in the payload have timestamps earlier than the current time minus 24 hours.
Message in response: `All logs are out of correct time range.`

`200` - in case some of the events in the payload have timestamps earlier than the current time minus 24 hours.
Example message in response: `2 events were not ingested because of timestamp out of correct time range`.

`204` - (No Content) in case of success.

The current time minus two hours for log metrics and events.

The data point is dropped if the log metric data point timestamp is before the current time minus two hours.

Current time plus ten minutes

The time stamp is reset to current time.

## High-cardinality attributes

Unique log data attributes (high-cardinality attributes) such as `span_id` and `trace_id` generate unnecessarily excessive facet lists that may impact log viewer performance. Because of this, they aren't listed in log viewer facets. You can still use them in a log viewer advanced search query.

## Log ingestion API request objects

In addition to generic Dynatrace API limitations ([Dynatrace API - Access limit](/docs/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API.")) the following log ingestion API specific limits apply:

* `LogMessagePlain plain` text object.  
  The length of the message is limited to 8,192 characters. Any content exceeding the limit is trimmed.
* `LogMessageJson` JSON object.  
  The object might contain the following types of keys (the possible key values are listed below):

  + Timestamp. The following formats are supported: UTC milliseconds, RFC3339, and RFC3164. If not set, the current timestamp is used.
  + Severity. If not set, NONE is used.
  + Content. If the content key is not set, the whole JSON is parsed as the content.
  + Semantic attribute. Only values of the String type are supported. Semantic attributes are indexed and can be used in queries. These are also displayed in aggregations (facets). If an unsupported key occurs it is not indexed and cannot be used in indexing and aggregations.

  The length of the value is limited. Any content exceeding the limit is trimmed. Default limits:

  + Content: 8,192 characters.
  + Semantic attribute value: 250 characters.

## Sensitive data masking limits

Be aware of the following limitations to sensitive data masking:

* If the masking process takes too much time, the log file affected is blocked until the restart of OneAgent or any configuration change, and then you get the `File not monitored - incorrect sensitive data masking rule` message.

## Active Gate throughput

If you are using the SaaS endpoint, you don't have to worry about the Active Gate throughput. The throughput is the same as for Grail.
If you use Environmental Active Gate, the throughput is 3.3GB/min with RTT <= 200 ms.