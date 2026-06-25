---
title: ActiveGate default installation settings for Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings
scraped: 2026-05-12T11:25:11.792721
---

# ActiveGate default installation settings for Linux

# ActiveGate default installation settings for Linux

* 1-min read
* Updated on Apr 21, 2026

If you do not specify any parameters during ActiveGate installation to customize settings, the following default settings will be applied. To modify defaults settings during installation, see [Customize ActiveGate installation on Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

## Directories

| **Purpose of directory** | **Default path** | **Path relative to installation parameter** | **Disk space requirements**  **(if size is not given, assume less than 1 MB)** |
| --- | --- | --- | --- |
| ActiveGate executable files, libraries, and related files | `/opt/dynatrace/gateway` | `<INSTALL>/gateway` | 600 MB |
| [ActiveGate configuration](#ag-config) | `/var/lib/dynatrace/gateway/config` | `<CONFIG>/gateway/config` |  |
| ActiveGate SSL folder | `/var/lib/dynatrace/gateway/ssl` | `<CONFIG>/gateway/ssl` |  |
| ActiveGate temporary files | `/var/tmp/dynatrace/gateway` | `<TEMP>/gateway` | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| ActiveGate logs | `/var/log/dynatrace/gateway` | `<LOG>/gateway` | 500 MB |
| Dump files uploaded to ActiveGate by OneAgent | `/var/lib/dynatrace/gateway/dump` | `<CONFIG>/gateway/dump` | Functionality off by default. When activated, can take configurable maximum size: default 100 GB. |
| ActiveGate packages directory for auto-update installer downloads | `/var/lib/dynatrace/packages` | `<PACKAGES_DIR>` | 500 MB. |
| ActiveGate extensions executable files, libraries, and related files[1](#fn-1-1-def) | `/opt/dynatrace/remotepluginmodule` | `<INSTALL>/remotepluginmodule` | 350 MB |
| ActiveGate extensions configuration, logs, cache, run-time work area | `/var/lib/dynatrace/remotepluginmodule` | `<CONFIG>/remotepluginmodule` | 2 GB (for logs and crash dumps) |
| ActiveGate extensions upload directory | `/opt/dynatrace/remotepluginmodule/plugin_deployment/` | `<INSTALL>/remotepluginmodule/plugin_deployment/` | Depending on uploaded extensions |
| zRemote executable files, libraries, and related files | `/opt/dynatrace/zremote` | `<INSTALL>/zremote` | 50 MB |
| zRemote user-modifiable persistent configuration,  zRemote runtime work area, crash reports | `/var/lib/dynatrace/zremote/agent` | `<CONFIG>/zremote/agent` | 50 MB |
| zRemote logs | `/var/log/dynatrace/zremote` | `<LOG>/zremote` | 200 MB |
| Private Synthetic executable files, libraries, and related files | `/opt/dynatrace/synthetic` | `<INSTALL>/synthetic` | 270 MB |
| Private synthetic logs | `/var/log/dynatrace/synthetic` | `<LOG>/synthetic/log` | 1 GB |
| Private Synthetic temporary files | `/var/tmp/dynatrace/synthetic` | `<TEMP>/synthetic` | 20 GB, including 1 GB for the `/var/tmp/dynatrace/synthetic/cache` and 1 GB for `/var/tmp/dynatrace/synthetic/screenshots`  You can [use `TEMP` to customize this location](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#temporary "Learn about the command-line parameters that you can use with ActiveGate on Linux."); however, for Synthetic-enabled ActiveGate installed on Ubuntu 20.04 LTS and 22.04 LTS earlier than 1.331, the path must begin with `/var/tmp`, for example, `TEMP=/var/tmp/syn`. Dynatrace requires write access to `/var/tmp` for the installation of Chromium snap packages. |
| Autoupdater | `/opt/dynatrace/autoupdater` | `<INSTALL>/autoupdater` | Included in estimate for ActiveGate executable files |
| Autoupdater logs | `/var/log/dynatrace/autoupdater` | `<LOG>/autoupdater` | 200 MB |

1

To ensure that extensions run correctly, the filesystem flag must be set to `exec` and not `noexec`. This configuration is crucial because it allows the execution of binaries and scripts within the specified filesystem. Without this setting, the extension will not be able to execute properly, leading to potential errors and failures.

## Access ActiveGate `config` directory

The config directory has specific permissions set for the `dtuserag` user. Access to this directory requires root privileges, as direct login to the `dtuserag` account is not allowed.

## Services

|  |  |  |
| --- | --- | --- |
| **Component name** | **Service name** | **Description** |
| ActiveGate | `dynatracegateway` | The main ActiveGate service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| ActiveGate auto-updater | `dynatraceautoupdater` | An auto-updater service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| Extensions | `extensionsmodule` | Service for the [Extensions functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [routing-monitoring purpose](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."). This service will be active or inactive, depending on configurationâfor default setting, refer to the module description. |
| zRemote | `zremote` | Service for the [zRemote functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of routing z/OS traffic to Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."). |
| Synthetic | `vuc` | Service for the [Synthetic functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of running Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations"). |

## Service account

All ActiveGate services are by default running as dedicated unprivileged user `dtuserag`. The only exception is `dynatraceautoupdater` which requires root privileges.

If the user `dtuserag` does not already exist in the system, the installer will create it.

## Port usage

By default, ActiveGate:

* receives connections from OneAgents or other ActiveGates on port 9999
* receives Dynatrace API on port 9999
* connects to Dynatrace SaaS or Managed cluster on port 443

For more information about possible ActiveGate connectivity schemes, see [Supported connectivity schemes for ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").