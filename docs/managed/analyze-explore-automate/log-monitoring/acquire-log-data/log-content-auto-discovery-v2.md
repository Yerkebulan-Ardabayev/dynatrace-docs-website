---
title: Log content autodiscovery (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2
---

# Log content autodiscovery (Logs Classic)

# Log content autodiscovery (Logs Classic)

* Explanation
* 3-min read
* Updated on Mar 25, 2026

Log Monitoring Classic

By default, Dynatrace automatically discovers all new log files that meet the requirements described below.

## Default autodiscovery

Dynatrace automatically discovers, analyzes, and stores (if [selected for storage](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.")) logs every 60 seconds.

Whether your autodiscovered files are stored in Dynatrace depends on the log ingest rules.

By default, the OneAgent log module autodiscovers the following categories of log files:

* **System logs**  
  On Windows:

  + `Windows Security Log`
  + `Windows Application Log`
  + `Windows System Log`

  On Linux:

  + `/var/log/messages`
  + `/var/log/syslog`

  On AIX:

  + `/var/log/messages` (supported by OneAgent version 1.335+)
  + `/var/log/syslog` (supported by all OneAgent versions)
* **Log files** opened by running processes. For details, see [Log content autodiscovery (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2#autodiscoveryrequirements "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")
* **IIS Logs** (Windows only) - both event logs and plain log files
* **Container logs** (Linux only) in Kubernetes, Openshift, and non-instrumented Docker. For details, see [Log Monitoring in Kubernetes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes#autodiscovery_requirements "Learn how to monitor logs in Kubernetes.")

### Attributes selected in Windows event logs

For Windows event logs, Log Monitoring detects the following fields and sends them as custom attributes:

| Semantic attribute name | Event property |
| --- | --- |
| `winlog.keywords` | `Event.RenderingInfo.Keywords` |
| `winlog.username` | `Event.System.Security.<xmlattr>.UserID` |
| `winlog.level` | `Event.RenderingInfo.Level` |
| `winlog.eventid` | `Event.System.EventID` |
| `winlog.provider` | `Event.System.Provider.<xmlattr>.Name` |
| `winlog.task` | `Event.System.Task` |
| `winlog.opcode` | `Event.RenderingInfo.Opcode` |

## Autodiscovery requirements

A log file must meet all of the following requirements in order to be autodiscovered:

* The log file must be opened by an [important process](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.").
* The log file must exist for a minimum of one minute.

  Unsupported timestamps

  Files with an unsupported timestamp are automatically timestamped with the time the file was read.
* The logs must have a supported character encoding.
  By default, the supported encoding is UTF-8. Other supported types include UTF-8 BOM and, if the files contain the byte-order mark (BOM), UTF-16LE and UTF-16BE.

  Binary logs

  Binary log files are not detected automatically. You can use custom log sources with **Allow binary format** option set to ingest Binary log files.
* The log file must be at least 0.5 KB in size.
* The log file must have been updated (written to) in the last 7 days.  
  Log files that have not been updated in the past 7 days while Log Monitoring is active will not be visible on dashboards.
* The log file must be in the actual `log` or `logs` folder or in its subfolders:

  + Valid path examples:  
    `c:\log\log_file.txt`  
    `c:\logs\NewFolder\log_file.txt`
  + Invalid path example:  
    `c:\log\NewFolder\NewFolder\log_file.txt`

  or the log filename must contain a `log` string preceded or followed by the period (`.`) or underscore (`_`) character:

  + Valid filename examples:  
    `c:\NewFolder\abc.log`  
    `c:\NewFolder\0865842.log.txt`
  + Invalid filename example:  
    `c:\NewFolder\logfile.txt`

## Turn off log autodiscovery

If you don't want Dynatrace to automatically discover new log files on a specific monitored host, you can turn off log autodiscovery.

1. On the host, open the log analytics configuration file for editing.

   * **On Linux**:  
     `/var/lib/dynatrace/oneagent/agent/config/ruxitagentloganalytics.conf`
   * **On Windows**:  
     `%PROGRAMDATA%\dynatrace\oneagent\agent\config\ruxitagentloganalytics.conf`
2. Set the following:  
   `AppLogAutoDetection = false`

OneAgent restart is not required.

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

## Unsupported autodiscovery scenarios

Scenarios that are not supported in the rotated log autodiscovery process include:

* Rotated log generation with a directory change. This process could lead to the creation of numerous non-aggregated and/or incomplete logs, as well as to resource overuse.
* Rotated log generation with immediate compression, where the application addresses a file with the same name. If a rotation criterion is met (for example, the required file size is reached), the file is moved to another location and immediately compressed.
  Example: `/var/log/application.log -> /var/log/application.log.1.gz -> /var/log/application.log.2.gz -> /var/log/application.log.3.gz`. This process might again lead to incomplete log creation.

## Related topics

* [Troubleshooting Log Monitoring (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.")