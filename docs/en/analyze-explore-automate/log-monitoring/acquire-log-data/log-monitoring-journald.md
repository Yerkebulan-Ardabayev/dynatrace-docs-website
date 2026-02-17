---
title: Log Monitoring from Journald (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-journald
scraped: 2026-02-17T21:29:47.807910
---

# Log Monitoring from Journald (Logs Classic)

# Log Monitoring from Journald (Logs Classic)

* Tutorial
* 4-min read
* Published Apr 22, 2025

Log Monitoring Classic

OneAgent version 1.307+

Log module is capable of reading, processing, and uploading entries from systemd-journald, a Linux-based centralized logging system service. Events/logs are usually stored in files located in the `/var/log/journal/'machine-id'/` directory, where `machine-id` is a long string of digits identifying the machine. These files are kept in a binary, compressed format, maintained by the systemd-journald engine to manage size per file and overall, retention, rotation, etc., according to its settings.

## How Journald works

To avoid the problems of manually tracking the files, such as rotation, decompression, or parsing, Log module uses system API calls to access the entire functionality. This is achieved by opening the system library, `libsystemd.so` and its dependencies, mapping selected functions from the library, and creating a context object, to communicate with the Journald system. This way, Log module becomes a client of Journald and can use a variety of its exposed functions.

At the beginning, Log module opens a handler at the default location of the Journald context. No specific path is used, allowing the handler to open its well-known location. Then the agent reads the entries one by one, keeping track of the current position.

## Enable Journald support

To enable Journald log detection, follow the steps below:

1. Go to **Settings** > **Log Monitoring** > **Log module feature flags**.
2. Select **Enable Journald log detector**.
3. Select **Save changes**.

Enabling the feature flag is required to opt-in. Without it, even with configured ingest rules, Journald logs will not appear in Dynatrace.

## Configure log ingestion from Journald

You can enable log ingestion from Journald by either configuring the default Journald [ingest rule](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis."), or by configuring the tenant storage upload, for example `kubelet.service` as `Journald.unit` from Journald.

### Enable the default ingestion rule

For new accounts, the default Journald ingest rule is enabled by default, and the configuration described in this section is not needed.

Follow the steps below to configure the default Journald ingest rule:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Enable the **[Built-in] Ingest Journald logs** rule to ingest all Journald logs.
3. Select **Save changes**.

### Create a custom ingestion rule

Follow the steps below to configure the tenat storage upload for `kubelet.service` logs from Journad:

1. Go to **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Select **Add rule** and provide the title for your configuration.
3. Select **Add matcher**. This is the first matcher to match two specified process groups.
4. From the **Attribute** list, select **Journald Unit**.
5. Select **Add value** and type `kubelet.service`.
6. Select **Add matcher** again to match the specified log data source.
7. From the **Attribute** list, select **Log source**.
8. Select **Add value** and enter **Journald** as the value.
9. Select **Save changes**.

## Attributes selected in journald

Each entry is processed to gain the following attributes:

Semantic attribute name

Description

`Timestamp`

Retrieved by direct API call for timestamp, results in microseconds since epoch converted to agentâs timestamp domain resolution

`Content`

The extracted value of the API call for data with the **MESSAGE** field as a selector

`Journald.unit`

The extracted value of the API call for data with the **UNIT** field as a selector
As an alternative, the ***SYSTEMD\_UNIT*** field is searched. It may happen that none of the fields are found.

`LogEntryLevel`

The extracted value of the API call for data with the **PRIORITY** field as a selector, priority. Consult the table below for the definitions of the priority levels.

## Priority level

Journald priority codes are used to mark the importance of a message. The following table shows how these priorities translate into Dynatrace severity:

Value

Severity

Description

0

Emergency

System is unusable

1

Alert

Should be corrected immediately

2

Critical

Critical conditions

3

Error

Error conditions

4

Warn

May indicate that an error will occur if action is not taken

5

Notice

Events that are unusual, but not error conditions

6

Info

Normal operational messages that require no action

7

Debug

Messages which may need to be enabled first, only useful for debugging