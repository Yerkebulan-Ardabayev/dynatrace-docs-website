---
title: Hardware and system requirements for routing/monitoring ActiveGates on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements
scraped: 2026-02-18T05:35:17.004486
---

# Hardware and system requirements for routing/monitoring ActiveGates on Windows

# Hardware and system requirements for routing/monitoring ActiveGates on Windows

* Latest Dynatrace
* 2-min read
* Published Oct 09, 2018

### Hardware and system requirements: Routing OneAgent traffic to Dynatrace, monitoring cloud environments, or monitoring remote technologies with extensions

For hardware and system requirements for other ActiveGate purposes, see:

* [Hardware and system requirements for Synthetic-enabled ActiveGates](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), which support a subset of operating systems and are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring.
* [Hardware and system requirements for the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring."). ActiveGates running the zRemote module are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring.

Run ActiveGate on dedicated system

For optimal performance and enhanced security, we recommend installing and running ActiveGate on a dedicated system.
Utilizing ActiveGate on a dedicated system not only minimizes the risk of compromising ActiveGate authentication data but also reduces the potential for malicious configuration manipulation.

## Hardware requirements

You need a machine dedicated to ActiveGate that has:

* 4 GB free disk space for ActiveGate and Extensions installation, configuration, and logs for auto update purposes.
* 4 GB for ActiveGate and OneAgent cached installers and container imagesâif such will need to be stored.
* Space for dump filesâif such will need to be stored. This functionality is turned off by default, but can be turned on in ActiveGate configuration. The maximum size of the storage space is [configurable](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.")â100 GB by default.
* 600 MB + 1.5 GB (buffer) of free disk space for Extension Execution Controller logs retransmission persistence file.
* Space for extension uploadsâdepending on extensions used.
* 2 GB RAM (4 GB recommended).
* 1 dual core processor.

For large environments, you may need to use a machine with additional CPU and memory.

## Space requirements per directory

**Space allocation per directory, for installation purposes:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater executable files, libraries, and related files  
`%PROGRAMFILES%\dynatrace\gateway`  
relative to installation parameter: `<INSTALL>\gateway`  
also configurable in GUI during installation

300 MB

ActiveGate configuration and related directories  
For Environment ActiveGate, it also contains Extensions configuration  
`%PROGRAMDATA%\dynatrace`

2 MB

For Environment ActiveGate only: Extensions executable files, libraries, and related files
`%PROGRAMFILES%\dynatrace\remotepluginmodule`  
relative to installation parameter: `<INSTALL>\remotepluginmodule`  
also configurable in GUI during installation

850 MB

**Space allocation per directory, for ActiveGate operation:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater logs  
ActiveGate packages directory for auto-update installer downloads  
`%PROGRAMDATA%\dynatrace`

1.2 GB

ActiveGate temporary files  
`%PROGRAMDATA%\dynatrace\gateway\tmp`

4 GB (including 3 GB for cached OneAgent installers and container images)

Dump files uploaded to ActiveGate by OneAgent  
`%PROGRAMDATA%\dynatrace\gateway\dump`

Functionality off by default.
When activated, can take configurable maximum size: default 100 GB.

For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  
`%PROGRAMDATA%\dynatrace\remotepluginmodule`

2 GB

For Environment ActiveGate only: ActiveGate extensions upload directory  
`%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment`

Depending on uploaded extensions

Extension Execution Controller logs retransmission persistence directory
`%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\runtime\extensions\persistence`

Up to 600 MB by default. [1](#fn-1-1-def)

1

The reliability mechanism does not work if the requirement is not met. Extra 1.5 GB required as a buffer. For more information see [Persistence details](#persistence).

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

## Supported operating systems

Supported operating systems:

| Windows OS | Versions | CPU architectures |
| --- | --- | --- |
| Windows | 10, 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## System requirements

* ActiveGate supports only operating systems running on the x86-64 architecture (64-bit Intel/AMD).
* Ensure that you have proper [network port configuration](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").
* ActiveGate installation is not supported on Windows with a disabled `NT AUTHORITY\LocalService` account.

## AWS sizing guide

The following table represents the machine instance size requirement based on number of OneAgents communicating with the ActiveGate. On each host, OneAgent is performing eight monitoring tasks:

* Infrastructure monitoring
* Log monitoring
* Full-stack monitoring of 3 Apache Tomcat instances
* Full-stack monitoring of 2 Apache HTTP Server instances
* Extension monitoring

The real number of hosts may be different depending on the monitored technologies in your environment. It is recommended that the machine on which ActiveGate is running should not exceed 50% CPU and 80% memory. Additionally, it must be assumed that ActiveGates may be inoperable during updates, restarts or short communication problems. In order to ensure high availability, operating ActiveGates should be able to takeover traffic of the unavailable ActiveGates

### x86-64 architecture

The C6i machine instances and the estimates:

Instance

vCPU

Mem (GiB)

Storage

Dedicated EBS bandwidth (Mbps)

Network performance

Estimated number of hosts

c6i.large

2

3.75

EBS-Only

500

Moderate

800

c6i.xlarge

4

7.5

EBS-Only

750

High

1800

c6i.2xlarge

8

15

EBS-Only

1,000

High

2500