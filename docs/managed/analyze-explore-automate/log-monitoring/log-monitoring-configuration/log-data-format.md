---
title: Log data formats (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format
---

# Log data formats (Logs Classic)

# Log data formats (Logs Classic)

* 2-min read
* Updated on Oct 27, 2025

Log Monitoring Classic

Log Monitoring can read and analyze:

## Windows event logs

System, Security, and Application logs are automatically discovered on hosts. Other custom event-log format logs can be added [manually on the environment level](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). The timestamp is sourced from an event's attribute, `Event.System.TimeCreated.<xmlattr>.SystemTime`.

## Plain-text logs

Any plain-text log file is valid as long as it is encoded in UTF-8 or UTF-16. The timestamp is detected automatically when it is present, according to the rules described in [Supported timestamp formats (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring."). It is also possible to [configure your timestamp](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration "Define log monitoring rules that control log data timestamps."). If no timestamp is present, the log format is still valid. In such case, each line that doesn't start with a whitespace is treated as the beginning of a new log record, and is automatically assigned a timestamp that is the time of reading a log record by OneAgent.

There is no specific support for JSON. It is treated as text.

For more details, see [Supported timestamp formats](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.").

## JSON logs

OneAgent version 1.327+ supports logs in JSON format.

Logs can be provided as JSON objects or arrays. Newline characters can be used to create multi-line JSON objects.

Headers and non-JSON prefixes are allowed. These are parsed as plain text.

OneAgent accepts a header at the beginning of the file, which is parsed as plain text.

### JSON log enrichment

OneAgent extracts the `timestamp` and `loglevel` attributes from the appropriate fields within the JSON object. This is the same behavior as with the Log ingestion API. Go to [Log Monitoring API - POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#openapi-parameter-body-objects-openapienv2 "Push custom logs to Dynatrace via the Log Monitoring API v2.") to see the list of supported keys.

Additionally, it extracts the attributes from a non-JSON prefix, if present. In such a case, the values from the prefix take priority.

If there are multiple `timestamp` or `loglevel` fields within a single JSON object, only the first key is used, in alphabetical order.

OneAgent automatically extracts any string fields whose names start with `dt.` (for example, `dt.trace_id` or `dt.span_id`), if they are located at the root or first inner level of the JSON object, and adds them as attributes.

The [supported timestamp patterns](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.") for JSON logs, from fields or prefixes, are the same as for plain-text logs.

To learn more about log levels, go to [Automatic log enrichment (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

### Configuration

Automatic JSON parsing is enabled by default. If OneAgent does not recognize content in JSON format, the log file is treated as plain-text.

You can explicitly disable JSON parsing by creating a timestamp configuration rule where the JSON parsing option is disabled. To learn how to configure a timestamp rule, go to [Timestamp/splitting configuration](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration#create-rule "Define log monitoring rules that control log data timestamps.").

To disable JSON parsing for a log file:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log Monitoring** > **Timestamp/Splitting patterns**.
2. On the record of your configured timestamp rule, select ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") **Edit**.
3. Disable the **JSON format detector** option.
4. Select **Save and close**.