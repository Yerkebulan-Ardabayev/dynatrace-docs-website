---
title: Hardware and system requirements for routing/monitoring ActiveGates on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements
scraped: 2026-02-22T21:20:55.134857
---

# Hardware and system requirements for routing/monitoring ActiveGates on Linux

# Hardware and system requirements for routing/monitoring ActiveGates on Linux

* Latest Dynatrace
* 4-min read
* Updated on Nov 20, 2025

### Hardware and system requirements: Routing OneAgent traffic to Dynatrace, monitoring cloud environments, or monitoring remote technologies with extensions

For hardware and system requirements for other ActiveGate purposes, see:

* [Hardware and system requirements for Synthetic-enabled ActiveGates](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), which support a subset of operating systems and are more demanding in terms of hardware and system requirements than ActiveGates that are used for routing and monitoring.
* [Hardware and system requirements for the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring."). ActiveGates running the zRemote module are more demanding in terms of hardware and system requirements than are ActiveGates that are used for routing and monitoring purposes.

Run ActiveGate on dedicated system

For optimal performance and enhanced security, we recommend installing and running ActiveGate on a dedicated system.
Utilizing ActiveGate on a dedicated system not only minimizes the risk of compromising ActiveGate authentication data but also reduces the potential for malicious configuration manipulation.

Refer to the [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") doc page for detailed log throughput characteristics on Environmental Active Gate for logs ingest API.

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
default: `/opt/dynatrace`  
relative to installation parameter: `<INSTALL>`

300 MB

ActiveGate configuration and related directories  
For Environment ActiveGate, it also contains Extensions configuration  
default: `/var/lib/dynatrace`  
relative to installation parameter: `<CONFIG>`

2 MB

For Environment ActiveGate only: Extensions executable files, libraries, and related files
default: `/opt/dynatrace/remotepluginmodule`  
relative to installation parameter: `<INSTALL>/remotepluginmodule`

1.2 GB

**Space allocation per directory, for ActiveGate operation:**  
**(for more detailed allocation, refer to [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

**Top-level directory**

**Disk space requirements**

ActiveGate and autoupdater logs  
default: `/var/log/dynatrace`  
installation parameter: `<LOG>`

700 MB

ActiveGate packages directory for auto-update installer downloads  
default: `/var/lib/dynatrace/packages`  
installation parameter: `<PACKAGES_DIR>`

500 MB

ActiveGate temporary files  
default: `/var/tmp/dynatrace/gateway`  
path relative to installation parameter TEMP: `<TEMP>/gateway`

4 GB (including 3 GB for cached OneAgent installers and container images)

Dump files uploaded to ActiveGate by OneAgent  
`/var/lib/dynatrace/gateway/dump`

Functionality off by default, not configurable at installation time.  
When activated, can take configurable maximum size: default 100 GB.

For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  
default: `/var/lib/dynatrace/remotepluginmodule`  
path relative to installation parameter CONFIG: `<CONFIG>/remotepluginmodule`

2 GB

For Environment ActiveGate only: ActiveGate extensions upload directory  
default: `/opt/dynatrace/remotepluginmodule/plugin_deployment`  
path relative to installation parameter INSTALL: `<INSTALL>/remotepluginmodule/plugin_deployment`

Depending on uploaded extensions

Extension Execution Controller logs retransmission persistence directory
`/var/lib/dynatrace/remotepluginmodule/agent/runtime/extensions/persistence`

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

### Routing-monitoring ActiveGates

| Linux distribution | Versions | CPU architectures |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | ARM64 (AArch64), x86-64 |
| Oracle Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), s390, x86-64 |
| Rocky Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| SUSE Enterprise Linux | 15.6, 15.7 | ARM64 (AArch64), s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | ARM64 (AArch64), s390 |

1

To run ActiveGate extensions on Amazon Linux 2023, versions 315 and earlier require manual installation of the 'libcrypt.so.1' library from the 'libxcrypt-compat.rpm' package, which is not installed by default.

ActiveGate installed on the x86-64 architecture supports all functionalities. Other architectures provide only partial support. For details, see [ActiveGate purposes and functionality](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

### ActiveGates running synthetic monitors from a private location

For ActiveGates running synthetic monitors from a private location, see [Requirements for private Synthetic location: Linux: Supported operating systems](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

### ActiveGates with the zRemote module

For ActiveGates with the zRemote module, see [Install the zRemote module: System requirements: Supported operating systems](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#supported-operating-systems "Prepare and install the zRemote for z/OS monitoring.").

## System requirements

* Ensure that you have proper [network port configuration](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").
* Your operating system must handle at least 500,000 open files for the `dtuserag` user.  
  To view the system limit, execute the following command:

  ```
  [user@host]# cat /proc/sys/fs/file-max
  ```

  Also, it may be that you've checked out [too many open files in Linux](/docs/ingest-from/dynatrace-activegate#too-many-open-files-in-linux "Understand the basic concepts related to ActiveGate.").
* Your operating system must have at least 20,000 processes available to the `dtuserag` user.  
  To view the system limit, execute the following command:

  ```
  [user@host]# cat /proc/sys/kernel/pid_max
  ```
* The ActiveGate Linux installer doesn't support ACL (Access Control List). ACL rules may prohibit access to installer-created directories and files, making the ActiveGate fail to start. If you use the ACL, rules related to the installation directories defined in the following parameters should be disabled:

  ```
  INSTALL=



  CONFIG=



  LOG=



  TEMP=



  PACKAGES_DIR=
  ```

## Sizing guide

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

### ARM64 (AArch64) architecture

The C7g machine instances and the estimates:

Instance

vCPU

Mem (GiB)

Storage

Dedicated EBS bandwidth (Mbps)

Network performance

Estimated number of hosts

c7g.large

2

3.75

EBS-Only

500

Moderate

1300

c7g.xlarge

4

7.5

EBS-Only

750

High

2700

c7g.2xlarge

8

15

EBS-Only

1,000

High

5500

### s390 architecture

Machine sizes and estimates:

Machine size

CPU

Mem (GiB)

Estimated number of hosts

S

2

4

800

M

4

8

1500