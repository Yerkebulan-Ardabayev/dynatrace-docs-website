---
title: Log Monitoring configuration (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration
scraped: 2026-02-19T21:34:25.597506
---

# Log Monitoring configuration (Logs Classic)

# Log Monitoring configuration (Logs Classic)

* 5-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

By default, Log Monitoring is activated in your Dynatrace environment. To start ingesting logs, depending on your use case, you need to either configure log storage rules on OneAgents or send logs to ingest APIs.

* [Log ingest rules (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.")
* [Log ingestion API (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")

You can confirm that Log Monitoring is enabled or you can enable it globally or on a host level, but checking the status and enabling or disabling Log Monitoring is optional in most cases. If you plan to use Log Monitoring, you can focus on OneAgent settings that directly affect how Log Monitoring is operating.

* [OneAgent settings](#lm-oneagent-settings).

## Check Log Monitoring status

Optional

You can check if Log Monitoring is enabled in your Dynatrace environment globally (Dynatrace web UI), or you can check if Log Monitoring is enabled on a host level (OneAgent CLI).

* To check if Dynatrace Log Monitoring is enabled globally:

  1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
  2. Find **Log Monitoring** in the list of supported technologies, and select **Edit** (pencil icon).
  3. Check if **Monitor Log Monitoring on every host** option is enabled.
* To check if Dynatrace Log Monitoring is enabled on a host level:  
  Use OneAgent CLI and execute the `oneagentctl` command with the `--get-app-log-content-access` parameter to check whether Log Monitoring is enabled:

  + Linux: `./oneagentctl --get-app-log-content-access`
  + Windows: `.\oneagentctl.exe --get-app-log-content-access`

## Enable or disable Log Monitoring

Optional

Similarly to checking Log Monitoring status, you can enable or disable Log Monitoring in your Dynatrace environment globally (Dynatrace web UI), or on a host level (OneAgent CLI).

* To activate Dynatrace Log Monitoring globally:

  1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
  2. Find **Log Monitoring** in the list of supported technologies, and select **Edit** (pencil icon).
  3. Turn on **Monitor Log Monitoring on every host**.
* To enable or disable Dynatrace Log Monitoring on a host level:  
  Use OneAgent CLI and execute the `oneagentctl` command-line interface to execute the following command at the individual host level.  
  Set the `--set-app-log-content-access` parameter to `true` or `false` to disable or enable Log Monitoring:

  + Linux: `./oneagentctl --set-app-log-content-access=true`
  + Windows: `.\oneagentctl.exe --set-app-log-content-access=true`

  Restart OneAgent service to apply changes.

## OneAgent settings

Dynatrace Log Monitoring uses the [OneAgent log module](/docs/discover-dynatrace/get-started/glossary#glossary-oneagent-log-module "Get acquainted with Dynatrace terminology.") enabled by default with all OneAgent installations. While Log Monitoring does not require any specific configuration, you can modify some of the options available for the OneAgent log module.

You can adjust:

* Enable and disable automatic log detection for different technologies.
* Define default timezone in containers.
* Enable defining the storage configuration by a configuration file on the host.
* Define specific location where the timestamp and severity occur in your incoming log data.
* Define the maximum number of log group instances per entity.

### Global OneAgent settings for Log Monitoring

1. Go to **Settings** > **Log Monitoring** > **OneAgent settings**.
2. Adjust settings and **Save changes**.

### Host-specific OneAgent settings for Log Monitoring

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **Log Monitoring** and **Advanced log settings**.
4. Adjust settings and **Save changes**.

## Default OneAgent settings

Setting

Description

Default

**Detect open log files**

This option automatically detects logs written by important processes.

enabled

**Detect IIS logs**

This option allows the detection of logs and event logs written by the Microsoft IIS server.

enabled

**Detect system logs**

Linux: Detects syslogs, and message logs.
Windows: Detects system, application, and security event logs.

enabled

**Detect logs on network file systems**

This option detects logs stored on the Network File System server. This applies for Linux only

disabled

**Allow OneAgent to monitor OneAgent logs**

This option allows OneAgent to monitor own logs.

disabled

**Detect logs of containerized applications**

This option allows the detection of log messages written to the containerized application's stdout/stderr streams. It also detects Kubernetes pod logs.

enabled

**Set UTC as default timezone in containers**

This sets the default timezone of the containers as UTC.

enabled

**Timestamp search limit**

Set the timestamp search.

`64` bytes

**Severity search chars limit**

Set the severity search characters limit.

`100` bytes

**Severity search lines limit**

Set the severity search lines limit.

`2`

**Maximum of log group instances per entity limit - count**

Set the upper limit for log group instances per entry.

`200`

## Configuration file Optional

The configuration file located on each OneAgent is used to set three options. For security reasons, these options can only be set on the host level and are available only by creating a JSON file in a specific location:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\`

The configuration file name must have the `json` extension; the file name is otherwise unrestricted.

By default, these options are set for the OneAgent log module to operate properly and to auto-detect log files on the specific host. Modifying this configuration file is not required.

### Multiple configuration files

You can have multiple JSON configuration files in the configuration folder. Files are evaluated in alphabetical order. Options from the last evaluated file takes priority.

### Preexisting configuration files

If your OneAgent installation is upgraded, you may find a `_migratedloganalytics.conf.json` file that contains your configuration migrated from the `ruxitagentloganalytics.conf` on your host.

During installation, the OneAgent installer may create `_loganalyticsconf.ctl.json`, which will contain options used during the installation. The same file will be used to store relevant options set by the OneAgentCtl tool.

### Available options

* `AppLogContentAccess`  
  Enables access to the log file content on this host. If set to `false`, the log file will be displayed in the user interface, but the content won't be accessible. Note that the OneAgent will still auto-detect log files unless the flag `AppLogAutoDetection` is set to `false`.
* `AppLogRemoteConfiguration`  
  Enables the manual configuration of logs to be accessed and monitored. If set to `false`, it won't be possible to add logs manually using the settings interface.
* `AppLogAutoDetection`  
  Enables auto-detection of log files on this host. If set to `false`, logs won't be auto-detected.

### Example

```
{



"agent-configuration": [



{



"AppLogRemoteConfiguration": true,



"AppLogContentAccess": true,



"AppLogAutoDetection": true



}



]



}
```