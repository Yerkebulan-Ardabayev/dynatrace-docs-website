---
title: OneAgent files and disk space requirements on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux
scraped: 2026-02-18T21:28:13.500462
---

# OneAgent files and disk space requirements on Linux

# OneAgent files and disk space requirements on Linux

* Latest Dynatrace
* 4-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

## Full-stack and Infrastructure Monitoring mode

The same disk space requirements apply to both Full-stack and Infrastructure monitoring modes.

## OneAgent directories and their sizes

|  | **Linux (x86)** | **Linux (ppcle)** | **Linux (s390)** | Default directory | Can be modified? |
| --- | --- | --- | --- | --- | --- |
| Size of installation | ~1.3 GB | ~500 MB | ~480 MB | `/opt/dynatrace/oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~5 MB | ~5 MB | ~5 MB | `/var/lib/dynatrace/oneagent/agent/config` | No |
| Temporary files, runtime configuration | 200 MB | 200 MB | 200 MB | `/var/lib/dynatrace/oneagent/agent/runtime` | No |
| Logs | 1 GB | 1 GB | 1 GB | `/var/log/dynatrace/oneagent` [2](#fn-1-2-def) | Yes [3](#fn-1-3-def) |
| Crash reports, memory dumps | 3 GB | 3 GB | 3 GB | `/var/lib/dynatrace/oneagent/datastorage` | Yes [4](#fn-1-4-def) |
| Log analytics persistence | ~1 GB [5](#fn-1-5-def) | ~1 GB [5](#fn-1-5-def) | ~1 GB [5](#fn-1-5-def) | `/var/lib/dynatrace/oneagent/datastorage/loganalytics` | Yes [4](#fn-1-4-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | 600 MB + 1.5 GB buffer | 600 MB + 1.5 GB buffer | `/var/lib/dynatrace/oneagent/agent/runtime/extensions/persistence` | Yes [6](#fn-1-6-def) [7](#fn-1-7-def) |
| Additional space required for updates | ~2.6 GB | ~950 MB | ~880 MB | See [Space required for updates](#updates) |  |
| **Total** | **~11.7 GB** | **~8.7 GB** | **~8.6 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.") installation parameter.

2

For OneAgent version 1.201 and earlier, the default location for log files is `/opt/dynatrace/oneagent/log`.

3

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#log-path "Learn how to use the Linux installer with command line parameters.") installation parameter.

4

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.") installation parameter.

5

The size depends on the number of ingested logs.

6

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

7

The reliability mechanism does not work if the requirement is not met. For more information see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

## OneAgent files aging mechanism

OneAgent in full-stack monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Dynatrace Managed self-monitoring

For OneAgent self-monitoring for Dynatrace Managed requirements on Linux, see [the directory structure of Dynatrace Managedï»¿](https://docs.dynatrace.com/managed/shortlink/managed-directory-structure).

## Space required for updates

When calculating the space required for updates, we take into account the installer file size and the size of the installation process, that is the space required to deploy OneAgent files.

The figures provided below are examples and should be used as a general guide. For the accurate size of installation, see the **Size of installation** in the [OneAgent directories and their sizes](#sizes) section.

|  | **Linux (x86)** | **Linux (ppcle)** | **Linux (s390)** |
| --- | --- | --- | --- |
| Installer file size | ~260 MB | ~90 MB | ~80 MB |
| Installation process size | ~2.1 GB | ~770 MB | ~720 MB |

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

**Variable**

**Description**

`persistence.reliable_mode`

`true` - reliable mode turned on; SFM logs genereted if space requirement not met
`false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism

`persistence.total_limit_kb`

Maximum volume limit for Extensions Log Persistence in kilobytes.
By default: 600 MB
Can be modified manually if the requirement can't be met on the host.