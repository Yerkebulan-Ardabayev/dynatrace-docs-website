---
title: Timestamp/splitting configuration (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration
scraped: 2026-02-20T21:12:07.052863
---

# Timestamp/splitting configuration (Logs Classic)

# Timestamp/splitting configuration (Logs Classic)

* 7-min read
* Updated on Sep 18, 2025

Log Monitoring Classic

Dynatrace allows you to define rules that control log data timestamps.

For the newest Dynatrace version, see [Timestamp/splitting configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.").

## Timestamp detection

By default, Log Monitoring automatically detects only the most common and unambiguous subset of date formats supported. For details, see [Supported timestamp formats (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.").

### No timestamp detected

When Log Monitoring is unable to determine the time format, it treats each log line as a separate log entry with an automatically assigned timestamp (observation timestamp) using a one-minute time resolution, except for lines starting with whitespaces (space, tab), which are treated as a continuation of an entry.

### Timestamp search limit

Regardless of format, the timestamp typically occurs within the first 64 characters of a log entry. However, the timestamp can occur elsewhere, in which case you can raise this limit on the OneAgent configuration page: **Log Monitoring** > **Timestamp/Splitting patterns**.

### Timestamp rules

Regardless of where it occurs in a log entry, a timestamp may be written in multiple formats. Dynatrace supports some timestamp formats by default, but sometimes multiple formats may fit the incoming log data and match the timestamp to an incorrect timestamp pattern.

Because of this, Log Monitoring also enables you to define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record. These rules contain a timestamp pattern, time zone, and matchers.

* **Pattern**âDefines what should be considered a timestamp in your logline.
* **Timestamp search limit**âspecifies the count of characters in each log line, measured from the beginning of the line, where the timestamp is searched.
* **Timestamps in indented lines**âEnable this option if you don't want to parse timestamps in lines that start with whitespace characters.
* **Time zone**âDefines the timestamp time zone. Optional if your timestamp pattern includes the timezone indicator (`%z`).
* **Matcher**âNarrows down the range for the rule and applies the timestamp pattern only to matched log entries. Because you can't use the `log.content` attribute in the timestamp pattern matchers, the highest granularity is a log source. Granularity is at this level because the timestamp pattern is used to split the contents of a log source into separate log records, so it is used before the `log.content` attribute's value (or any other attributes set on an individual log record's level) is determined.

  + If you create multiple rules matching the same log data, all defined time formats are searched for.
  + If you have at least one rule matching a given log, predefined formats are not applied to it.

### Multiple timestamp patterns in the same log source

When ingesting log entries, OneAgent parses the log entry for a timestamp.
To do this, it uses a list of matcher patterns.

* When the log entry contains one timestamp, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the first pattern in the list. If the entryâs timestamp matches one of the patterns, OneAgent uses that timestamp as the beginning of the log entry.
* When the log entry contains two or more timestamps, OneAgent evaluates the timestamp against the list of matcher patterns, starting with the pattern that was matched in the previous log entry.

Therefore, it is possible that even if the log entryâs first timestamp matches the first pattern in the list of matching patterns, OneAgent will actually match the second timestampâbecause the previous log entry matched the second pattern.
See the code block below for an example.

```
Log entry 1: Pattern 1, Pattern 2



Log entry 2: Pattern 2



Log entry 3: Pattern 1, Pattern 2
```

For log entry 3, even if "Pattern 1" appears first in the list of matcher patterns, OneAgent will actually match "Pattern 2".

To ensure OneAgent evaluates only your desired timestamp patterns, carefully select which patterns are in your matching list. In the example above, to guarantee Pattern 1 is always used, remove Pattern 2 from your list. This may result in messages that only contain Pattern 2 timestamps to be dropped.

For example, if your log file contains both `%FT%T` (2024-01-01T12:30:01) and `%F %T %Z` (2024-01-01 12:30:01 UTC) patterns, and OneAgent successfully matches the first pattern in a line, it will prioritize that pattern for subsequent lines.

## Supported scopes

Three hierarchy scopes are supported: host, host group, and environment.

The hierarchy scopes are merged into one list in the following order:

1. Host rules
2. Host group rules
3. Environment rules

![Diagram showing the rule priority for timestamp configuration rules.](https://dt-cdn.net/images/timestamp-sopes-955-9292323a57.png)

The OneAgent receives the merged list (merged lists from its respective hosts, host groups, and environments) with no indication of which scopes are defined.

### Host scope

The host scope can be accessed through the **Host settings** for a specific host.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
5. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Host group scope

The host group scope can be accessed via the **Host** page.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Timestamp/Splitting patterns**.
7. Configure data masking by adding rules with a set of matchers that specify what should be considered a timestamp in the log record.

### Environment scope

The environment scope is available in the settings menu.

1. Go to **Settings** > **Log Monitoring** > **Timestamp/Splitting patterns**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.

## Create rule

To add a rule (on the host, host group, or environment level) that interprets the incoming log data timestamps

1. Select **Add rule** to start configuring your rule.
2. **Rule name**

   The name to display for your configuration.
3. **Pattern**

   Enter the pattern to be read as a date from the logs. For details on timestamp formats, see [Supported timestamp formats (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Supported timestamps for the latest version of Dynatrace Log Monitoring.") and the [Date libraryï»¿](https://dt-url.net/o8034wt).

   You need to specify at least the year, month, day, hours, minutes, and seconds, although you can use alternative formats for them. You can include the time zone indicator (`%z`) or specify the time zone separately in the rule definition.

   Rules without a pattern can override the timezone only for default supported timestamps.
4. **Timestamp search limit**

   Use this field to define the number of characters in every log line where timestamp is searched. If you want to ignore timestamps and split logs using the [default rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-one-agent-log-data-format#plain-text-logs "This topic lists all the log formats supported by Log Management and Analytics"), set this value to `0`. Use this field to overwrite the global [timestamp search limit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration#timestamp-search-limit "Define a specific date format using timestamp rules that specify what should be considered a timestamp in a log record.") (default 64 bytes).
5. **Time zone**

   Select the time zone to apply to this pattern.  
   This setting is not enabled if you have already specified the timezone in the timestamp pattern (`%z`).

   You can select `Local time zone` to use the time zone of the host on which the OneAgent is running.
6. Select **Add matcher** to create a specific match for this rule and narrow down the scope for that rule.

   You can include multiple matchers in one rule. For example, the timestamp configuration rule can be applied to logs from a specific container, namespace, or log source. Multiple matchers with the same attribute use AND logic between matchers, while matchers with multiple values assigned to them use OR logic.

   Matcher attribute

   Matching is based on

   **Process group**

   The process group ID.

   **Log source**

   A log path; wildcards are supported in form of an asterisk.

   **K8s container name**

   The name of the Kubernetes container.

   **K8s namespace name**

   The name of the Kubernetes namespace.

   **K8s deployment name**

   The name of the Kubernetes deployment.

   **Container name**

   The name of the container.

   **DT entity container group ID**

   The DT entity container group ID.

   **Process technology**

   The technology name.
7. Select the matching attribute.
8. Select **Value** and, from the **Value** list, select the detected log data items.

   You can add multiple values to the selected attribute. You can have one matcher that indicates the `Log source` and matches values `/var/log/syslog` and `Windows Application Log`. Use asterisks (`*`) as wildcards to get a partial match.
9. Select **Save changes**.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

Rule reorder propagation delay

When you change the rule order (to change the order in which they are executed), allow for two or three minutes of propagation time between when you save the change and when the change takes effect.

The **Active** toggle

Starting with OneAgent version 1.249, you can activate/inactivate your rules by turning on/off the **Active** toggle. To manage your rules effectively, we recommend that you upgrade your OneAgent to version 1.249. If you have any rules set on the host with OneAgent version earlier than 249, you will not be able to inactivate them, in which case you need to remove such rules by selecting **Delete** on the rule level or via the REST API.

Rules are executed in the order in which they appear on the **Timestamp/Splitting patterns** page.

## REST API

You can use the Settings API to manage your timestamp configuration:

* View schema
* List stored configuration objects
* View single configuration object
* Create new, edit, or remove existing configuration object

To check the current schema version for timestamp configuration, list all available schemas and look for the `builtin:logmonitoring.timestamp-configuration` schema identifier.

Timestamp configuration objects are available for configuration on the following scopes:

* `environment`âconfiguration object affects all hosts in a given environment.
* `host_group`âconfiguration object affects all hosts assigned to a given host group.
* `host`âconfiguration object affects only the given host.

To create a timestamp configuration using the API

1. [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the **Write settings** (`settings.write`) and **Read settings** (`settings.read`) permissions.
2. Use the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint to learn the JSON format required to post your configuration. The timestamp configuration schema identifier (`schemaId`) is `builtin:logmonitoring.timestamp-configuration`. Here is an example JSON payload with the timestamp configuration:

   ```
   [



   {



   "insertAfter":"uAAZ0ZW5hbnQABnRlbmFudAAkMGUzYmY2ZmYtMDc2ZC0zNzFmLhXaq0",



   "schemaId": "builtin:logmonitoring.timestamp-configuration",



   "schemaVersion": "0.1.0",



   "scope": "tenant",



   "value": {



   "config-item-title": "Added from REST API",



   "date-time-pattern": "%Y-%m-%d %H:%M:%S",



   "timezone": "CET",



   "matchers": [



   {



   "attribute": "dt.entity.process_group",



   "operator": "MATCHES",



   "values": [



   "PROCESS_GROUP-05F00CBACF39EBD1"



   ]



   },



   {



   "attribute": "log.source",



   "operator": "MATCHES",



   "values": [



   "Windows System Log",



   "Windows Security Log"



   ]



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.