---
title: Install an Environment ActiveGate on Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate
scraped: 2026-05-12T11:36:28.466208
---

# Install an Environment ActiveGate on Windows

# Install an Environment ActiveGate on Windows

* 3-min read
* Published Jul 17, 2018

Follow these steps to install an Environment ActiveGate on Windows.

## Before you begin

Decide what your ActiveGate purpose will be and review the respective hardware and system requirements. ActiveGates have different hardware and system requirements depending on the **purpose** for which they are installed:

* Purpose: [Route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies with extensions](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").  
  Hardware and system requirements for [routing/monitoring ActiveGates](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.").
* Purpose: [Run Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")  
  Synthetic-enabled ActiveGates support a subset of operating systems and are more demanding in terms of [hardware and system requirements](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") than are ActiveGates that are used for routing and monitoring.
* Purpose: [Install the zRemote module for z/OS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")  
  ActiveGates running the zRemote module are more demanding in terms of [hardware and system requirements](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring.") than are ActiveGates that are used for routing and monitoring.

In most cases, you can install an ActiveGate at any time following OneAgent installation. In some cases, however, the installation order matters, because the OneAgent installer needs to know about your ActiveGate installation before the OneAgent can be installed.

If you've already installed OneAgent

In such instances, first install the ActiveGate and then download the OneAgent installer.
For example, if you download the OneAgent installer and use it to install Dynatrace in a DMZ or network segment that has no internet access and then subsequently install an ActiveGate, youâll need to download and install OneAgent again to ensure that the installer provides the proper configuration between OneAgent and ActiveGate. This is because OneAgent needs to be automatically configured during installation to connect to your monitored environment and send monitoring data back to the Dynatrace Cluster via your ActiveGate.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given in the footer of the ActiveGate installation page.**  
ActiveGate normally listens (accepts incoming connections) on `port 9999` and talks to Dynatrace (makes outgoing connections) on `port 443`. For more information on ports usage, see [Which network ports does ActiveGate use?](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#port-usage "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")

![AG on Windows](https://dt-cdn.net/images/screenshot-2023-08-10-at-11-10-53-am-1517-967b5764b3.png)

AG on Windows

## Start installation

Sign in to Dynatrace. Go to **Deploy Dynatrace**, then select **Install ActiveGate**.

On the **Install Environment ActiveGate** page, select **Windows**.

## Download the installer

How you download your installer depends on your setup and needs. You can choose to download an installer directly to the server where you plan to install an ActiveGate or you can download an installer to a different machine and then transfer the installer to the server.

1. Select the [ActiveGate purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

   * If you want your ActiveGate to run synthetic monitors from a private location, see [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").
   * If you want your ActiveGate to route z/OS traffic to Dynatrace, see [Install the zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.").
2. Provide a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes."). This token is required to download the ActiveGate installer from your environment. If you don't have a PaaS token, you can create one right in the UI. The token is automatically appended to the download and installation commands you'll use later.
3. Download the installer. There are two options:

   * Select **Download installer** to download the Windows installer (EXE file).
   * Download via Windows Command Prompt. Copy and run the `powershell` command. It is generated automatically when you provide the PaaS token.

     This command will only work with PowerShell 3.0 and TLS 1.2 (or .later).

## Run the installer

An install parameter (determined by the ActiveGate purpose you selected) is automatically set for the command to run the installer. Make sure you use the command displayed in the Dynatrace web UI that reflects the ActiveGate purpose.

You need administrator rights to install Environment ActiveGate. **Run the executable file using administrator rights** and follow the displayed instructions.

### Customize installation

You can add additional [parameters](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Learn about the parameters that you can use with ActiveGate on Windows.") to the installation command to customize your installation. For example, to install Environment ActiveGate executable files and libraries in a different directory, use the `INSTALL=<path>` parameter (ActiveGate version 1.232+):

```
C:\ Dynatrace-ActiveGate-Windows-x86-1.0.0.exe INSTALL=D:\hosted_app\dynatrace
```

### Custom certificate for ActiveGate

We recommend using custom certificates for ActiveGates to increase security.

See [Custom SSL certificate](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#custom-ssl-certificate "Learn about the parameters that you can use with ActiveGate on Windows.").

### Default installation settings

For installation defaults, including default directories, see [ActiveGate default settings for Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Learn about the default settings with which ActiveGate is installed on Windows.").

## You've arrived

After your ActiveGate connects to Dynatrace, installation is complete and OneAgent is reconfigured to send monitoring data through ActiveGate.

* To check the status of the installation, select **Show deployment status** and switch to the **Dynatrace ActiveGates** tab.
* For troubleshooting help, see [Troubleshoot ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").