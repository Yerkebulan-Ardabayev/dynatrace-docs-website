---
title: Supported timestamp formats (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format
scraped: 2026-03-01T21:26:47.406357
---

# Supported timestamp formats (Logs Classic)

# Supported timestamp formats (Logs Classic)

* 3-min read
* Updated on Sep 18, 2025

Log Monitoring Classic

Timestampâincluding date, time, timezone, and offsetâis searched for in the first 64 characters of the log content (this value is configurable via **Log Monitoring** > **Timestamp/Splitting patterns**). If an offset or timezone is not found, the local timezone of a host is used.

For the newest Dynatrace version, see [Supported timestamp formats](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Supported timestamps for the latest version of Log Management and Analytics.").

During log processing, each line where a supported timestamp is detected starts a new log record. A line without a timestamp is considered to be a continuation of an existing log record and appended to a line that contains a timestamp.  
If no timestamp is present in a log file or a timestamp is not recognized due to unsupported format, each line not starting with whitespace characters, such as `space` or `tab`, starts a new log record. Each line starting with whitespace characters, such as `space` or `tab`, is treated as a log record continuation.  
Due to multiple formats of incoming log data, Log Monitoring also enables you to define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record. For more details on defining date format, see [Log timestamp configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

The supported [timestamp formatsï»¿](https://dt-url.net/6e034iy) include:

* ISO 8601 format: `%Y-%m-%d %H:%M:%S`  
  Example: `2022-04-17 11:25:12.345`
* RFC 3339 format: `%Y-%m-%dT%H:%M:%S`  
  Example: `2022-04-17T11:25:12.345`
* Unix Epoch format, providing the number of milliseconds that have elapsed since January 1, 1970
  Example: `1652088888997`
* RFC 3164 format: `%b %d %H:%M:%S`  
  Example: `Apr 17 11:25:12`
* Db2 (IBM database 2) format: `%Y-%m-%d-%H.%M.%S`  
  Example: `2022-05-17-11.25.12.114000-300`
* IIS format: `%m/%d/%Y, %H:%M:%S`  
  Example: `04/17/2022, 11:25:12.345`
* W3C (World Wide Web Consortium) format: `%Y-%m-%d %H:%M:%S`  
  Example: `2022-04-17 11:25:12.345` specified in the UTC timezone
* Klog and Golang/glog format: `[IWEF]%m%d %H:%M:%S`
  Example: `I0408 06:40:02.634162`
* Other common formats:

  + `%d %b %Y %H:%M:%S` (example: `17 Apr 2022 11:25:12.345`)
  + `%Y %b %d %H:%M:%S` (example: `2022 Apr 17 11:25:12.345`)
  + `%d/%b/%Y:%H:%M:%S` (example: `17/Apr/2022:11:25:12.345`)

JSON files are supported for Docker only. If the `log` tag is detected in a JSON file, then the corresponding message is ingested and analyzed. Within the message, the timestamp of one of the supported formats is searched. If no supported file format is found, the `time` tag is searched. For example:

```
{



"log":"2020-11-24 11:01:36,484 CRIT Supervisor running as root (no user in config file)\n",



"stream":"stdout",



"time":"2020-11-24T11:01:36.484996713Z"



}



{



"log":"2020-11-24 11:01:36,500 INFO RPC interface 'supervisor' initialized\n",



"stream":"stdout",



"time":"2020-11-24T11:01:36.50065223Z"



}
```

### Examples of valid log file time formats

Most of the supported timestamp formats are coupled with automatic timezone format detection. The following time zone formats are recognized:

* Offset to UTC zone  
  Examples:

  `2022-04-17 11:25:12.345 +01:00`  
  `2022-04-17 11:25:12.345 +0100`  
  `2022-04-17 11:25:12.345Z -01:00`  
  `2022-04-17 11:25:12.345Z-0100`  
  `2022-04-17 11:25:12.345 UTC-01:00`  
  `2022-04-17 11:25:12.345 GMT-0100`
* Full [IANAï»¿](https://dt-url.net/jq034g6) timezone name.  
  Example:  
  `2022-04-17 11:25:12.345 Europe/Warsaw`
* Timezone name abbreviation  
  Examples:  
  `2022-04-17 11:25:12.345 CEST`  
  `2022-12-17 11:25:12.345 CET`  
  `2022-04-17 11:25:12.345Z`  
  `2022-04-17 11:25:12.345UTC+0100`

If no time zone indicator is found in the log line, the time zone used when parsing a timestamp is by default set to the one configured in
**Settings** > **Log Monitoring** > **Advanced log settings** > **Default timezone for agents**.

### Override the timezone

In case automatic timezone format detection fails, you can add a rule overriding time zone in the [Log timestamp configuration page](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration#createrule "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

## Default used timezone

When processing timestamps, OneAgent follows both local timezone patterns and UTC patterns.

### Local timezone patterns

When no timezone is specified in the log content, the following timestamp formats default to the **local timezone** of the host:

* ISO 8601 (`%Y-%m-%d %H:%M:%S`)
* RFC 3164 (`%b %d %H:%M:%S`)
* IIS (`%m/%d/%Y, %H:%M:%S`)
* Klog and Golang/glog (`[IWEF]%m%d %H:%M:%S`)
* `%d %b %Y %H:%M:%S`
* `%Y %b %d %H:%M:%S`
* `%d/%b/%Y:%H:%M:%S`

### UTC timezone patterns

When no timezone is specified in the log content, the following timestamp formats default to **UTC**:

* RFC 3339 (`%Y-%m-%dT%H:%M:%S`)
* Db2 (`%Y-%m-%d-%H.%M.%S`)
* W3C (`%Y-%m-%d %H:%M:%S`)
* Unix time

To verify which timezone was used for timestamp parsing, search the OneAgent logs (`oneagent-logmon-detailed.log`) for `Diagnostic statistics for LGI`.