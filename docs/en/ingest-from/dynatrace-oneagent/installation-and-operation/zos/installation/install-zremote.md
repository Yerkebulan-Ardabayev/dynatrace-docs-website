---
title: Install the zRemote module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote
scraped: 2026-02-22T21:20:56.555194
---

# Install the zRemote module

# Install the zRemote module

* Latest Dynatrace
* 8-min read
* Updated on Jan 22, 2026

The zRemote module processes monitoring data received from the zLocal and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the CICS, IMS, and z/OS Java code modules incurred in instrumenting subsystems and applications to an open system.

You can [customize the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Customize the zRemote module for your needs.") to enable optional features like **Host groups** and **Db2 SQL statement fetch**.

## Hardware requirements

The hardware requirements of the machine where the zRemote module runs depend on the number of anticipated CICS and IMS transactions to be monitored per second. See the hardware requirements for x86-64 and s390 architecture machines below.

* For CICS and IMS development environments: a small or medium-sized machine.
* For CICS and IMS production environments: a large or extra-large machine.
* For z/OS Java environments: a small or medium-sized machine.

Hardware requirements

Small (DEV)

Medium (DEV)

Large (PROD)

X-Large (PROD)

**Anticipated monitored CICS/IMS transactions per second**

**4,000**

**7,500**

**15,000**

**30,000**

Required CPU cores on x86-64 architecture (Xeon E5-2600 series)

2

4

8

16

Required [IFL processorsï»¿](https://www.ibm.com/products/integrated-facility-for-linux) on s390 architecture

1

1

1

2

Required memory

4GB

6GB

8GB

16GB

Required disk space

20GB

20GB

20GB

20GB

* The hardware requirements are for the case when the zRemote module and its ActiveGate are used for mainframe monitoring only.
* Multiple [zDC subsystems](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).") can be connected to a single zRemote as long as the number of monitored transactions matches the hardware requirements.

## System requirements

We recommend installing the zRemote module on an IBM Z or LinuxONE mainframe, on an supported Linux operating system for s390. The following system requirements apply:

* The zDC subsystem and the zRemote module to which it connects must be located within the same data center to avoid performance and security issues.

  + The zRemote will write a warning to its logs after a connection latency of 3 seconds.
  + The zRemote will drop the connection after a connection latency of 10 seconds.
* The zRemote only supports a [host-based ActiveGate installation](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") configured for a single environment.
* Monitoring of the host running the zRemote with OneAgent is only supported in [full-stack monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

### Supported operating systems

You can install the zRemote module on any Linux and Windows operating system listed below.

| Distribution | Versions | CPU architectures |
| --- | --- | --- |
| Oracle Linux | 8.10 | x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4 | s390, x86-64 |
| Rocky Linux | 8.10 | x86-64 |
| SUSE Enterprise Linux | 15.6 | s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | s390 |
| Windows | 10, 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## Installer overview

The overview outlines the key components of the zRemote application, the zRemote configuration, and their default installation directories. Non-persistent directories are replaced during updates and uninstallation.

### zRemote application and installation directories

Linux

Windows

Base path: `/opt/dynatrace/zremote`

Base path: `C:/Program Files/dynatrace/zremote`

All of the following directories are not retained in the event of a zRemote update or uninstallation. If you make changes here, they will be overwritten or deleted.

Directory

Component

Description

`agent/lib64`

noneagentz

The zRemote binary

`agent/lib64`

oneagentzwatchdog

A binary that provides the service capabilities for the zRemote service and controls resource limits

`agent/lib64`

oneagentdumpproc

A binary that supports creating dumps when the main application crashes

`agent/lib64/zos-s390-64/<version>`

dtzagent

A binary deployed to the UNIX part of the mainframe to support OneAget communications. For more details, see [Install the zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")

`agent/lib64/zos-s390-64/<version>`

libdtzagent.so

A binary deployed to the UNIX part of the mainframe to support agent communications. For more details, see [Install the zDC subsystem](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")

`agent/conf`

ruxitagent.conf

The default zRemote configuration file

`agent/conf`

oneagentzwatchdog.ini

The default watchdog configuration file

`agent/conf`

.pem

Application certificates

`agent`

installer.version

The installer version of the zRemote binary, which is usually the same as the zRemote version

`agent`

zremote

Linux only The service script for running the zRemote application

uninstallation.sh

Linux only The service script for uninstalling the zRemote application.

It removes everything except the persistent user configuration and log files.

### zRemote configuration and installation directories

Linux

Windows

Base path: `/var/lib/dynatrace/zremote`

Base path: `C:/Program Files/dynatrace/zremote`

All of the following directories are not retained during zRemote update or uninstallation. If you make changes here, they will be overwritten or deleted.

Directory

Component

Description

`agent`

runtime

Contains the connection details as specified by your Dynatrace environment.

`config`

instance.properties

Contains the ID of the currently registered instance.

`config`

version.properties

Contains the full version number of the zRemote module.

state

Contains the address of the last successful server connection to indicate a properly established connection.

The following directories are retained in case of update or uninstallation. You can make changes here. For more details, see [Customize the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Customize the zRemote module for your needs.").

Directory

Component

Description

`agent/conf`

zremoteagentuserconfig.conf

The configuration file for zRemote module customization

`agent/conf`

watchdoguserconfig.conf

The configuration file for watchdog customization

## Installation

The zRemote module is downloaded and installed automatically during the ActiveGate installation procedure on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Linux.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Windows.").

1. In Dynatrace Hub, select **ActiveGate** > **Set up**.
2. On the **Install Environment ActiveGate** page, select **Linux** or **Windows**.
3. Linux only Select installer type **s390** (recommended) or **x86/64**.
4. Select the purpose **Install the zRemote module for z/OS monitoring**, download the installer, and start the installation procedure.
5. Optional Customize the listening port selection.

   By default, the zRemote module listens on port 8898 for connections from the zLocal running as part of the zDC. To listen on a different port, set the `zdclistenerport` parameter to your port in the `zremoteagentuserconfig.conf` file. Make sure this port is not blocked by a firewall.

For details on the default installation settings, see ActiveGate default installation settings for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows.").

For details on customizing the installation, see customize ActiveGate installation on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Learn about the parameters that you can use with ActiveGate on Windows.").

## Logging

The zRemote logs are created on the machine where the zRemote module is installed, in the default directories for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows."). You can view the zRemote logs either directly on the machine hosting the zRemote or by requesting them from Dynatrace via the [OneAgent diagnostics](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") workflow.

The actual zRemote log should contain the following messages:

* Log messages that are sent from all CICS/IMS code modules and the zDC.
* Log messages that are sent from the zLocal.

## Update and maintenance

To stay current, you can update the zRemote module automatically to a newer version by using the [ActiveGate auto-update procedure](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.").

To manually update the zRemote module

Linux

Windows

1. If you have customized the installation, back up the `zremoteagentuserconfig.conf` file of the zRemote module and the `custom.properties` file of the ActiveGate. The installer should not overwrite these files, but we recommended backing them up for safety.
2. Uninstall the zRemote module.

   ```
   /opt/dynatrace/gateway/uninstall.sh
   ```
3. Install the zRemote module.

   ```
   ./bin/bash Dynatrace-ActiveGate-Linux-<arch>-<version>.sh --enable-zremote
   ```

1. If you have customized the installation, back up the `zremoteagentuserconfig.conf` file of the zRemote module and the `custom.properties` file of the ActiveGate. The installer should not overwrite these files, but we recommended backing them up for safety.
2. Uninstall the zRemote module via the Windows Control Panel.
3. [Install the zRemote module](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Read the step-by-step procedure for installing an Environment ActiveGate on Windows.") by executing the installer.

### Operations

To stop, start, or restart the zRemote module, you can use the following commands.

Linux

Windows

You need root privileges to execute these commands.

To query the current status of the zRemote module:

```
service zremote status
```

To stop, start, or restart the zRemote module:

```
service zremote stop|start|restart|forcestop
```

The difference between `stop` and `forcestop` is that the `stop` command instructs the process to execute its controlled shutdown routine, while `forcestop` forces the process shutdown.

You need admin privileges to execute these commands.

On Windows, the zRemote module can be maintained using the **Services** tab of the Windows Task Manager. You can also use the following command:

```
sc stop|start|restart "Dynatrace zRemote"
```

The `sc` command is asynchronous, so you need to query the status of the service, to determine when it has fully stopped:

```
sc query "Dynatrace zRemote"
```