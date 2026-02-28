---
title: OneAgent files and disk space requirements on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows
scraped: 2026-02-28T21:09:57.331079
---

# OneAgent files and disk space requirements on Windows

# OneAgent files and disk space requirements on Windows

* Latest Dynatrace
* 4-min read
* Updated on Jun 25, 2025

This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.

## Full-stack and Infrastructure Monitoring mode

The same disk space requirements apply to both Full-stack and Infrastructure monitoring modes.

## OneAgent directories and their sizes

|  |  | Default directory | Can be modified? |
| --- | --- | --- | --- |
| Size of installation (with temporary installation files removed) | ~775 MB | `%PROGRAMFILES%\dynatrace\oneagent` | Yes [1](#fn-1-1-def) |
| Persistent configuration | ~10 MB | `%PROGRAMDATA%\dynatrace\oneagent\agent\config` | No |
| Temporary files, runtime configuration | 200 MB | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime` | No |
| Logs | 1 GB | `%PROGRAMDATA%\dynatrace\oneagent\log` | Yes [2](#fn-1-2-def) |
| Crash reports, memory dumps | 3 GB | `%PROGRAMDATA%\dynatrace\oneagent\datastorage` | Yes [3](#fn-1-3-def) |
| Log analytics persistence | ~1 GB [4](#fn-1-4-def) | `%PROGRAMDATA%\dynatrace\oneagent\datastorage\loganalytics` | Yes [3](#fn-1-3-def) |
| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime\extensions\persistence` | Yes [5](#fn-1-5-def) [6](#fn-1-6-def) |
| Additional space required for updates | ~3.4 GB | See [Space required for installation and updates](#updates) |  |
| **Total** | **~11.5 GB** |  |  |

1

Use the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") installation parameter.

2

Use the [LOG\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#log-path "Learn how to use the OneAgent installer for Windows.") installation parameter.

3

Use the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") installation parameter.

4

The size depends on the number of ingested logs.

5

Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/docs/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.

6

The reliability mechanism does not work if the requirement is not met. For more information, see [Persistence details](#persistence).

For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").

## OneAgent files aging mechanism

OneAgent in full-stack monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").

## Space required for updates

When calculating the space required for updates, we take into account the compressed EXE installer file size, the extracted MSI package, and the size of the installation process (the space required to deploy OneAgent files).

|  | Size | Description | Removed after | Claimed by | Path |
| --- | --- | --- | --- | --- | --- |
| 1 | ~130 MB | EXE installer downloaded by AutoUpdate | OneAgent restart or next version installed [1](#fn-2-1-def) | AutoUpdate | `%PROGRAMDATA%\dynatrace\oneagent` |
| 2 | ~750 MB | Extracted MSI installer | End of the installation | OneAgent Installation | `%PROGRAMDATA%\dynatrace\oneagent` |
| 3 | ~750 MB | Extra storage for temporary installation files | End of the installation | OneAgent Installation | `%APPDATA%` |
| 4 | ~750 MB | Copy of the MSI installer saved by Windows | Next version installed | Windows installer | `%WINDIR%\Installer` |
| 5 | ~750 MB | Installed files | Next version installed | OneAgent Installation | `[Installation path]` |
| Î£ | ~3130 MB |  |  |  |  |

1

If you download the EXE installer manually, the installation process won't remove it.

Additional space required for installation and updates is calculated using the 10% safety margin:

`(size of the installation process [2+3+4+5] + installer files size [1]) * 1.1`

Required disk space for OneAgent installation and update on a single drive is ~3.4 GB calculated using this formula.

Note that the EXE installer is compressed, which explains the difference in size in comparison to the MSI installer.

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