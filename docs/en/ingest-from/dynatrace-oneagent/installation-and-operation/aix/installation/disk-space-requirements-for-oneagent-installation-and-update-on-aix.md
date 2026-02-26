---
title: OneAgent files and disk space requirements on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix
scraped: 2026-02-26T21:19:53.218406
---

# OneAgent files and disk space requirements on AIX

# OneAgent files and disk space requirements on AIX

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

|  |  | Default directory | Can be modified? |
| --- | --- | --- | --- |
| Size of installation (with temporary installation files removed) | ~700 MB | `/opt/dynatrace/oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~5 MB | `/var/lib/dynatrace/oneagent/agent/config` | No |
| Temporary files, runtime configuration | 200 MB | `/var/lib/dynatrace/oneagent/agent/runtime` | No |
| Logs | 1 GB | `/var/log/dynatrace/oneagent` [2](#fn-1-2-def) | Yes [3](#fn-1-3-def) |
| Crash reports, memory dumps | 3 GB | `/var/lib/dynatrace/oneagent/datastorage` | Yes [4](#fn-1-4-def) |
| Log analytics persistence | ~1 GB [5](#fn-1-5-def) | `/var/lib/dynatrace/oneagent/datastorage/loganalytics` | Yes [4](#fn-1-4-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | `/var/lib/dynatrace/oneagent/agent/runtime/extensions/persistence` | Yes [5](#fn-1-5-def) [6](#fn-1-6-def) |
| Additional space required for updates | ~1.4 GB | See [Space required for updates](#updates) |  |
| **Total** | **~9.4 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#installation-path "Learn how you can use AIX installer with command line parameters.") installation parameter.

2

For OneAgent version 1.201 and earlier, the default location for log files is `/opt/dynatrace/oneagent/log`.

3

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#log-path "Learn how you can use AIX installer with command line parameters.") installation parameter.

4

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.") installation parameter.

5

The size depends on the number of ingested logs.

6

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

7

The reliability mechanism does not work if the requirement is not met. For more information see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").

## OneAgent files aging mechanism

OneAgent in Full-Stack Monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Space required for updates

When calculating the space required for updates, we take into account the installer file size and the size of the installation process, that is the space required to deploy OneAgent files.

|  |  |
| --- | --- |
| Installer file size | ~120 MB |
| Installation process size | ~1.1 GB |

Additional space required for updates is calculated using the 10% safety margin:

`(installer file size + size of the installation process) * 1.1`

### Size of the installation process

The size of the installation process is calculated as follows:

`3 * installer file size + size of the installation`

The installer size must be multiplied by 3 to account for:

* Downloaded installer file (`/var/lib/dynatrace/oneagent`)
* Archive, which is separated from the installer script (`/opt/dynatrace/oneagent`)
* Unpacked external TAR (`/opt/dynatrace/oneagent`)

In terms of space requirements, there's no real difference between manual installation of the new version (when an older version is already installed), automatic update, and updates that are triggered by restarting the OneAgent container. In all these cases, the installation process is performed exactly the same way. What differs is the method through which the update is triggered.

## Persistence details

The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.

### General information

* Persistent storage of data requires 2136 MB of free disk space:

  + 600 MB of free disk space to be used by the reliability mechanism
  + 1.5 GB of free disk space to be used as a buffer
* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.
* The volume is used proportionally to the load of logs ingest.
* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).

### Configuration

Windows configuration file: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`