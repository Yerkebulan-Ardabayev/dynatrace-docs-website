---
title: Start/stop/restart ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate
---

# Start/stop/restart ActiveGate

# Start/stop/restart ActiveGate

* 1-min read
* Updated on Apr 06, 2022

To start, stop or restart an ActiveGate you need to start, stop or restart the respective [services for Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings#services "Learn about the default settings with which ActiveGate is installed on Linux") or [services for Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings#services "Learn about the default settings with which ActiveGate is installed on Windows.") that the ActiveGate is using—depending on the operating system on which the ActiveGate is installed. The actual services present also depend on the [purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") for which the ActiveGate has been installed and on the functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") that have been enabled.

Linux

Windows

You'll need root privileges to execute the commands to start, stop or restart ActiveGate services:

* Start an ActiveGate service  
  `systemctl start <service name>`

  For example:

  ```
  systemctl start dynatracegateway
  ```
* Stop an ActiveGate service  
  `systemctl stop <service name>`

  For example:

  ```
  systemctl stop dynatracegateway
  ```
* Restart an ActiveGate service  
  `systemctl restart <service name>`

  For example:

  ```
  systemctl restart dynatracegateway
  ```
* Query the current status of an ActiveGate service  
  `systemctl status <service name>`

  For example:

  ```
  systemctl status dynatracegateway
  ```

#### Services

|  |  |  |
| --- | --- | --- |
| **Component name** | **Service name** | **Description** |
| ActiveGate | `dynatracegateway` | The main ActiveGate service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| ActiveGate auto-updater | `dynatraceautoupdater` | An auto-updater service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| Extensions | `extensionsmodule` | Service for the [Extensions functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [routing-monitoring purpose](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."). This service will be active or inactive, depending on configuration—for default setting, refer to the module description. |
| zRemote | `zremote` | Service for the [zRemote functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of routing z/OS traffic to Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."). |
| Synthetic | `vuc` | Service for the [Synthetic functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of running Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations"). |

On Windows, starting and stopping ActiveGate services can be done using the Windows Task Manager, on the Services tab. You can also start and stop ActiveGate services using a command:

* Start ActiveGate  
  `net start "<service_name>"`

  For example:

  ```
  net start "Dynatrace Gateway"
  ```
* Stop ActiveGate  
  `net stop "<service_name>"`

  For example:

  ```
  net stop "Dynatrace Gateway"
  ```

#### Services

|  |  |  |
| --- | --- | --- |
| **Component name** | **Service name** | **Description** |
| ActiveGate | `Dynatrace Gateway` | The main ActiveGate service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| ActiveGate auto-updater | `Dynatrace Autoupdater` | An auto-updater service. Present for all ActiveGate [purposes](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") and functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). |
| Extensions | `Dynatrace Extensions Controller` | Service for the [Extensions functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [routing-monitoring purpose](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."). This service will be active or inactive, depending on configuration—for default setting, refer to the module description. |
| zRemote | `Dynatrace zRemote` | Service for the [zRemote functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of routing z/OS traffic to Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."). |
| Synthetic | `Dynatrace Synthetic` | Service for the [Synthetic functional module](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Present on ActiveGates installed for the [purpose of running Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations"). |