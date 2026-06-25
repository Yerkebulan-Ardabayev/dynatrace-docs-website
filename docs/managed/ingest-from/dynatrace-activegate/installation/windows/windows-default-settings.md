---
title: ActiveGate default installation settings for Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings
scraped: 2026-05-12T11:36:29.629318
---

# ActiveGate default installation settings for Windows

# ActiveGate default installation settings for Windows

* 1-min read
* Updated on Apr 21, 2026

If you do not specify any parameters during ActiveGate installation to customize settings, the following default settings will be used. To modify defaults settings during installation, see [Customize ActiveGate installation on Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Learn about the parameters that you can use with ActiveGate on Windows.")

## Directories

On Windows, the `%PROGRAMDATA%` directory is usually hidden for non-privileged users. Therefore you cannot select it by browsing through folders. Instead, to access the folder, paste the folder path directly into a Windows Explorer address box.

| **Purpose of directory** | **Default path** | **Path relative to installation parameter** | **Disk space requirements**  **(if size not given, assume less than 1 MB)** |
| --- | --- | --- | --- |
| ActiveGate executable files, libraries,and related files | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | 600 MB |
| ActiveGate configuration | `%PROGRAMDATA%\dynatrace\gateway\config` |  |  |
| ActiveGate SSL folder | `%PROGRAMDATA%\dynatrace\gateway\ssl` |  |  |
| ActiveGate temporary files | `%PROGRAMDATA%\dynatrace\gateway\tmp` |  | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| ActiveGate logs | `%PROGRAMDATA%\dynatrace\gateway\log` |  | 500 MB |
| Dump files uploaded to ActiveGate by OneAgent | `%PROGRAMDATA%\dynatrace\gateway\dump` |  | Functionality off by default. When activated, can take configurable maximum size: default 100 GB. |
| ActiveGate packages directory for auto-update installer downloads | `%PROGRAMDATA%\dynatrace\packages` |  | 500 MB |
| ActiveGate extensions executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\remotepluginmodule` | `<INSTALL>\remotepluginmodule` | 350 MB |
| ActiveGate extensions configuration, logs, cache, run-time work area | `%PROGRAMDATA%\dynatrace\remotepluginmodule` |  | 2 GB (for logs and crash dumps) |
| ActiveGate extensions upload directory | `%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` | `<INSTALL>\remotepluginmodule\plugin_deployment` | Depending on uploaded extensions |
| zRemote executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\zremote` | `<INSTALL>\zremote` | 50 MB |
| zRemote user-modifiable persistent configuration,  zRemote runtime work area, crash reports | `%PROGRAMDATA%\dynatrace\zremote\agent` |  | 50 MB |
| zRemote logs | `%PROGRAMDATA%\dynatrace\zremote\log` |  | 200 MB |
| Private Synthetic executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\synthetic` | `<INSTALL>\synthetic` | 270 MB |
| Private synthetic logs | `%PROGRAMDATA%\dynatrace\synthetic\log` |  | 1 GB |
| Private synthetic temporary files | `%PROGRAMDATA%\dynatrace\synthetic` |  | 20 GB, including 1 GB for the `%PROGRAMDATA%\dynatrace\synthetic\cache` and 1 GB for `%PROGRAMDATA%\dynatrace\synthetic\screenshots` |
| Autoupdater | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | Included in estimate for ActiveGate executable files |
| Autoupdater logs | `%PROGRAMDATA%\dynatrace\autoupdater\log` |  | 200 MB |

## Services

|  |  |  |
| --- | --- | --- |
| **Component name** | **Service name** | **Description** |
| ActiveGate | `Dynatrace Gateway` | The main ActiveGate service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| ActiveGate auto-updater | `Dynatrace Autoupdater` | An auto-updater service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| Extensions | `Dynatrace Extensions Controller` | Service for the [Extensions functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [routing-monitoring purpose](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."). This service will be active or inactive, depending on configurationâfor default setting, refer to the module description. |
| zRemote | `Dynatrace zRemote` | Service for the [zRemote functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of routing z/OS traffic to Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."). |
| Synthetic | `Dynatrace Synthetic` | Service for the [Synthetic functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of running Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations"). |

## Service account

All ActiveGate services are running as unprivileged `Local Service` account. The only exception is `Dynatrace Autoupdater` which is running as `Local System`.

## Port usage

By default, ActiveGate:

* receives connections from OneAgents or other ActiveGates on port 9999
* receives Dynatrace API on port 9999
* connects to Dynatrace SaaS or Managed cluster on port 443

For more information about possible ActiveGate connectivity schemes, see [Supported connectivity schemes for ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").