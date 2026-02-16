---
title: WMI data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions
scraped: 2026-02-16T09:30:33.898957
---

# WMI data source

# WMI data source

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 21, 2021

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your Windows Management Instrumentation (WMI) monitored devices.

We assume the following:

* You possess sufficient Windows and WMI subject matter expertise to create a WMI extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

## Prerequisites and support

Learn the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").

### Supported Dynatrace versions

* Dynatrace version 1.215+
* Windows-based Environment ActiveGate version 1.215+
* OneAgent version 1.221+ (local extensions)

### Monitored host

Local WMI extensions can be run on any OneAgent-supported Windows host without any special requirements. Make sure Extension Execution Controller (EEC) is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").

A host you want to monitor using a remote WMI extension must meet the requirements described below, including remote permissions enabled and connectivity details configured to allow your ActiveGate to access the WMI monitoring data.

#### Remote enable permission on the host

A monitored host must have the **Remote enable** permission set.

1. In the Microsoft [Server Managerï»¿](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) console, go to **Administrative Tools** > **Computer Management**.
2. Expand **Services and Applications**, right-click **WMI Control**, and select **Properties**.
3. Select the **Security** tab and then select the **Security** button.
4. Add the user you'll use to call WMI and then select **Remote Enable** in the **Allow** column.

For more information, see [Allowing Users Access to a Specific WMI Namespaceï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace) in the Microsoft documentation.

#### Configure firewall to access remote WMI

To configure the firewall to access remote WMI, issue the following commands:

```
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
```

and

```
netsh firewall set service RemoteAdmin enable
```

For more information, see [Setting up a Remote WMI Connectionï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista) in the Microsoft documentation.

#### Disable Remote UAC

Disable Remote UAC when using a local administrator account (without Active Directory).

```
New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -PropertyType DWord -Value 1 -Force
```

For more information, see [Handling Remote Connections Under UACï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac) in the Microsoft documentation.

#### Set up local user

To establish a connection to a WMI remote host, you need to use either a standard user or a user with administrator privileges, depending on the kind of data you want. You will add this user in [monitoring configuration](#monitoring-configuration). We recommend that you create a dedicated local user group or user account on the target computer specifically for remote connections.

To limit user privileges to access only a remote connection to WMI

1. In Windows, run the `DCOMCNFG` command.
2. Go to **Component Services** > **Computers**, right-click **My Computer**, and select **Properties**.
3. Select the **COM Security** tab.
4. Under **Launch and Activation Permissions**, select **Edit Limits**.
5. Select the **ANONYMOUS LOGON** name in the **Group or user names** box. Under **Permissions for ANONYMOUS LOGON**, select **Remote Launch** and **Remote Activation** in the **Allow** column.
6. Select **OK** to save.

For more information, see the Microsoft documentation:

* [Securing a Remote WMI Connectionï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)
* [Limiting access to WMI namespacesï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)
* [Access to WMI Namespacesï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)

#### Set up a fixed port for WMI

1. At the command prompt, enter:
   `winmgmt -standalonehost`
2. Stop the WMI service:  
   `net stop winmgmt`
3. Restart the WMI service in a new service host:  
   `net start winmgmt`
4. Establish a new port number for the WMI service:  
   `netsh firewall add portopening TCP 24158 WMIFixedPort`

For more information, see [Setting Up a Fixed Port for WMIï»¿](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) in the Microsoft documentation.