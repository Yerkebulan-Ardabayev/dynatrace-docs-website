---
title: Install OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows
scraped: 2026-02-26T21:19:21.087839
---

# Install OneAgent on Windows

# Install OneAgent on Windows

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Jan 22, 2026

This page describes how to download and install Dynatrace OneAgent on Windows.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements and prerequisites

* You need [administrator rights](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system") for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).
* You need permissions and credentials for restarting all your application services.
* You need to check also the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.").
* The host on which you install OneAgent needs at least 200 MB RAM.
* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").
* For OneAgent version 1.253 and earlier, we recommend that you [uninstall any existing `WinPcap` driver](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#uninstall-winpcap-driver-to-allow-npcap-installation "Learn how to download and install Dynatrace OneAgent on Windows.") to allow `Npcap` installationâdo this on all Windows versions, except for `Windows Server 2019 build 1809 without hotfix KB5066187`.
  For OneAgent version 1.255+, `Npcap` is installed by default and may cause a network disruption on `Windows Server 2016`, `Windows Server 2019 build 1809`, and `Windows Server 2019 build 1809 without hotfix KB5066187`. To prevent it, upgrade your hosts with the hotfix [KB5066187ï»¿](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5066187) or use [other documented options](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring#potential-network-disruption-during-oneagent-installation-on-windows "Learn more about troubleshooting network monitoring.").

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Uninstall WinPcap driver to allow Npcap installation

If you have the `WinPcap` driver installed, we recommend that you remove it prior to OneAgent installation and let the OneAgent installer install the appropriate packet capture driver as packaged with the OneAgent installer: `Npcap` is the recommended packet capture driver for OneAgent.

`Npcap` is the successor to `WinPcap` and is best suited for Dynatrace network analysis. The `Npcap` driver provided with the OneAgent installer is packaged in such a way that its DLL library files are seamlessly integrated with Dynatrace software, enabling unattended updates.

For more information, see:

* [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
* [Customize OneAgent installation on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.")

During the upgrade from `WinPcap` to `Npcap`, you might encounter network disruptions that can be mitigated by upgrading your Windows Server version and/or disabling `Microsoft Network Monitor Driver`. For more details, see [Potential network disruptions during OneAgent installation on Windows](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring#disruptionnetwork "Learn more about troubleshooting network monitoring.")

## Re-installation or repair of installation

OneAgent installer for Windows doesn't support the `modify` and `repair` operations. You can't reinstall OneAgent using the same installer version as was used to install the currently installed OneAgent. To reinstall OneAgent, uninstall it first or simply install a newer version.

## Installation



1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Windows**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. Download the installer. There are two options:

   * Select **Download OneAgent installer** to download the installer for Windows (EXE file) for single-server installation.
   * Download via Windows Command Prompt. Copy and run the `powershell` command. It is generated automatically when you provide the PaaS token.

     This command will only work with PowerShell 3.0 and TLS 1.2 (or later).

   Get MSI package

   If you want to use Group Policy to automatically distribute OneAgent to your Windows hosts, you'll need the MSI package along with the batch file. To get the MSI package:

   1. Download the OneAgent installer provided as an EXE file.
   2. Run it with the `--unpack-msi` parameter. This extracts the MSI package and the installation batch file. Optionally, you can specify an existing path. If you skip the path, the files are saved to a working directory. For example:

   ```
   C:\Downloads\Dynatrace-OneAgent-Windows.exe --unpack-msi "C:\installers"
   ```

   When using the `--unpack-msi` parameter, no other [installation parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.") are allowed. Add the `--quiet` parameter to run the MSI package extraction in quiet mode. Use the `--help` parameter to display a pop-up window with a list of available parameters.

   Copy and paste the MSI package and the batch file when configuring Group Policy for Dynatrace installation. The default installation should work in most cases, but if you need to customize it, you can modify the [installation parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows."). Then, you have to create a distribution point, assign a package (the OneAgent MSI package with parameters), specify a command to install the MSI package as [silent installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#silent-installation "Learn how to use the OneAgent installer for Windows."), and publish your policy.
5. Optional **Set customized options**  
   At this point, the Dynatrace UI allows you to customize your OneAgent installation: You can specify a number of customizations interactively on-screen. Based on your entries, an installation command will be generated and displayed, for use in the next step of installation (see below).  
   You can:

   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * Organize your hosts into [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."), if your environment is segmented (for example, into development and production).
   * Override automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * Apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * Disable [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

   **If further customizations are required, you can specify [additional options on the command line](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.").**
6. If you have not specified any custom options, simply run the executable file and follow the instructions as displayed.
   If you have specified custom options above, use the generated command, and run it from the download directory. The command will contain all the installation parameters reflecting the custom settings you have specified.
7. Restart all processes that you want to monitor. Youâll be prompted with a list of the processes that need to be restarted. Note that you can restart your processes at any time, even during your organizationâs next planned maintenance period. Though until all processes have been restarted, youâll only see a limited set of metrics, for example CPU or memory consumption.

What happens during installation?

OneAgent is a set of specialized services that have been configured specifically for your monitoring environment. The role of these services is to monitor various aspects of your hosts, including hardware, operating system, and application processes.

During the installation process, the installer:

* Installs executable code and libraries that are used by OneAgent.
* Creates entries in the Windows Registry that start OneAgent as a `SYSTEM` service. Additionally, the `oneagentmon` device and (optionally) `Npcap` or `WinPcap` are installed to allow better integration with the operating system and to facilitate the capture of network statistics.
* Checks the systemâs global proxy settings.
* Checks for a connection to Dynatrace Server or ActiveGate (if you installed ActiveGate and downloaded the OneAgent installer after ActiveGate was connected to Dynatrace).
* OneAgent version 1.193 and earlier Creates its own user (`dtuser`) to run OneAgent extensions. This user is a member of the **Performance Monitoring Users** group, and can only log in as a service. The password is randomly generated during installation and stored encrypted. You can't change the password. For security purposes, the `dtuser` is not allowed to:

  + Access computer from the network.
  + Log in as a batch job.
  + Log in locally.
  + Log in through Remote Desktop Services.  
    The `dtuser` is required for Dynatrace to operate properly, therefore you must not delete it. If, for some reason, the `dtuser` was deleted, next update will recreate it.
* OneAgent version 1.195+ For fresh OneAgent 1.195+ installations, the default `LocalSystem account` is used to run OneAgent extensions.
  For a summarized view of the changes made to your system by OneAgent installation, see [OneAgent security on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.