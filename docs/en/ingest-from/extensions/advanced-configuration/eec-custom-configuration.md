---
title: Extension Execution Controller custom configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/eec-custom-configuration
scraped: 2026-02-23T21:27:13.071316
---

# Extension Execution Controller custom configuration

# Extension Execution Controller custom configuration

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Sep 22, 2025

The Extension Execution Controller (EEC) can be used standalone, out of the box. This topic explains how to modify your EEC.

## Modify the EEC configuration

To modify the EEC configuration, edit the `extensionsuser.conf` file, which is located at:

* Using ActiveGate (for installation in the default location):

  + Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Using OneAgent:

  + Windows: `%PROGRAMDATA%C\dynatrace\oneagent\agent\config\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/oneagent/agent/config/extensionsuser.conf`

## Restart the EEC service

After modifying the `extensionsuser.conf`, you need to restart the EEC service:

Linux

Windows

To restart the EEC service on a Linux system, run the following commands:

* For systems with SystemV:

  ```
  service extensionsmodule stop



  service extensionsmodule start
  ```
* For systems with systemd:

  ```
  systemctl stop extensionsmodule



  systemctl start extensionsmodule
  ```

To restart the EEC service on a Windows system, either start **Task Manager** and restart the `Dynatrace Extensions Controller` service or run the following commands:

```
net stop "Dynatrace Extensions Controller"



net start "Dynatrace Extensions Controller"
```

## Change port used to communicate with ActiveGate

By default, the EEC sends data via port 9999, which is used by ActiveGate.

If you modify the port using the ActiveGate `custom.properties` file, you also have to modify the port that's used by the EEC. To do so, edit the `extensionsuser.conf` file to replace `PORT` with the target port and then restart the EEC service.

```
Server=https://127.0.0.1:PORT/communication
```

The port needs to be configured for the ActiveGate plugin module and the EEC.

## Change EEC port used to communicate with the extension

This port is used for communication between the EEC and existing extension (data source) processes.

To add it, edit the `extensionsuser.conf` file and insert

```
ingestport=<new_port>
```

## Enable/disable custom code extensions for data sources

Extensions leveraging sensitive data sources can significantly enhance the functionality and flexibility of your custom monitoring. However, they can also introduce potential vulnerabilities. Disabling custom extensions for these sensitive data sources can significantly reduce the risk of unauthorized access or data leakage.

To enable or disable custom code extensions for a data source

1. [Modify the EEC configuration](#modify-eec) to replace `<DSID>` with the data source ID for which you want to enable or disable custom code extensions.

   ```
   custom_code_<DSID>_allowed=[True|False]
   ```
2. [Restart the EEC service](#restart-eec).

## Elevate privileges for local extensions on Windows

By default, all local extensions on Windows (except WMI ones running on OneAgent) are executed with a LOCAL SERVICE account, which has lower privileges than the LOCAL SYSTEM account that is the default one for OneAgent and EEC.

In case an extension requires elevated privileges, you can configure it to run as LOCAL SYSTEM manually.

Open the `extensionsuser.conf` file and add the `elevated_privileges_extensions` parameter as follows:

```
elevated_privileges_extensions=[<extensionName>:<extensionVersion>]
```

The `extensionVersion` can either be a specific version in the format `<major>.<minor>.<patch>`, for example `1.0.1`, or a wildcard character `*` that can be used to specify that all versions of a particular extension will have elevated privileges.

When adding more than one extension, use a comma-separated list.

```
elevated_privileges_extensions=[com.dynatrace.filesystem:*, com.dynatrace.ibm-mq:1.0.1]
```

Only Dynatrace extensions can be elevated, while custom ones cannot. In case an extension was configured to run with elevated privileges but was already executed (the process is running), itâs necessary to force the process to restart by either restarting the OneAgent service or temporarily disabling and re-enabling the extension monitoring configuration.

## Related topics

* [Develop your own Extensions](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")