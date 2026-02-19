---
title: OneAgent security on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows
scraped: 2026-02-19T21:31:54.130427
---

# OneAgent security on Windows

# OneAgent security on Windows

* Latest Dynatrace
* 5-min read
* Published Nov 12, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, Dynatrace requires privileged access to your operating system during both installation and operation.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

OneAgent requires admin privileges on Windows, for both installation and operation.

### Installation

OneAgent installer requires admin privileges to:

* Create the OneAgent service.
* Modify certain registry keys.
* Install packet capture driver (Npcap or WinPcap) for network metrics collection. For more information, see [Packet capture driver (pcap)](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").
* Install [oneagentmon device](/docs/discover-dynatrace/get-started/glossary#o "Get acquainted with Dynatrace terminology.").

### Operation

OneAgent requires admin privileges to:

* List all processes.
* Get memory statistics for all processes.
* Read each process command line and environment.
* View the descriptions of executable files.
* Read application configuration for Apache and IIS
* View the list of libraries loaded for each process.
* Read Windows registry keys.
* Read .NET application domain for .NET 2.0, 3.0, and 3.5.
* Start monitoring network traffic.
* Parse executables for Go Discovery.
* Gather monitoring data related to Docker containers.

## Operating system changes

OneAgent performs the following changes to your system:

### Installation

OneAgent installer modifies the following aspects of your system:

* Starting with version 1.195, no user account is created to run OneAgent extensions. Instead, the `NT AUTHORITY\SYSTEM` privileged system account is used. For more information, see [OneAgent extension user](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Learn how to use the OneAgent installer for Windows.").
* The `Dynatrace OneAgent` service is created.
* The Dynatrace OneAgent program is registered with Windows Installer.
* `oneagentmon` driver is installed and `OneAgentMon` device is created. It's required to enable automatic injection into processes.
* Registry sub-trees are created:

  + `HKEY_LOCAL_MACHINE\SOFTWARE\Dynatrace\OneAgent`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\oneagentmon`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dynatrace OneAgent`
  + `HKEY_LOCAL_MACHINE\SOFTWARE\Caphyon\Advanced Installer`
* [Troubleshooting: Network Agent initialization failure on Windowsï»¿](https://dt-url.net/7c438ee)
* The `Npcap` driver is installed with the `/admin_only` flag set, which restricts Npcap's packet reading and writing to users with Administrator privileges only. Unprivileged users can't access Npcap's functionality on a monitored host. Note that WinPcap doesn't offer this restriction. For more information, see [Customize OneAgent installation on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").

  Make sure these Npcap and WinPcap operations are permitted in your system's security settings:

  + **Npcap:** Writing registry values to `SYSTEM\CurrentControlSet\Services\npcap`
  + **Npcap:** Reading and writing registry values to `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\NpcapInst`
  + **Winpcap:** Reading and writing registry values to `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst` and `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst`
  + **Npcap and Winpcap:** Loading `wpcap.dll` and `packet.dll` located in `C:\WINDOWS\system32\Npcap` / `C:\WINDOWS\system32\WinPcap`
  + **Npcap and Winpcap:** Reading registry values regarding present network interfaces in [`SYSTEM\CurrentControlSet\Control\Network\{Network-Service-GUID}`ï»¿](https://dt-url.net/lz036sy)\*

## Files added

### Installation

OneAgents installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `%PROGRAMFILES%\dynatrace\oneagent`. Note that you can change the location using the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") parameter.
* Installer temporary files are saved in `C:\AI_RecycleBin`. The folder is deleted after the installation is complete.

### Operation

* OneAgent temporary files and runtime configuration are saved in `%PROGRAMDATA%\dynatrace\oneagent\runtime`.
* OneAgent persistent configuration is saved in `%PROGRAMDATA%\dynatrace\oneagent\config`.
* Large runtime data, such as memory dumps, is saved in `%PROGRAMDATA%\dynatrace\oneagent\datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads Security, System, and Application system logs from the last 14 days so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or automatic updates.

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The [OneAgent directory structure](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") contains globally writable directories (directories where the `Everyone` user group can write, modify, or execute). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* We leverage advanced file permissions and use the `Creator Owner` permission to limits access to files.

## Installer signing

The OneAgent installer is signed against one or more [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm). For regularly maintained systems, Windows verifies that the OneAgent installer has been published by a verified publisher.

If your Windows-based system has been offline since March 2021 or longer, Windows won't be able to verify the installer and the OneAgent installer publisher will appear as **Unknown publisher** when you attempt an installation or update. In such a case, you need to download the latest certificate from [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm) and add it to your system. Among all the DigiCert certificates, the `DigiCert Global Root G3` is mandatory for successful verification of the OneAgent installer.

* See [How to: View certificates with the MMC snap-inï»¿](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) in Microsoft docs to learn which root certificates are installed in your system.
* Download the latest root certificates from [DigiCert root certificatesï»¿](https://www.digicert.com/kb/digicert-root-certificates.htm).

### Windows 2008 R2

Starting with OneAgent version 1.225, the installer is signed using the SHA-2 algorithm. Consequently, Windows 2008 R2 hosts are required to have SHA-2 code signing support installed. If you use Windows Update, the updates were offered to you automatically (KB4474419 and KB4490628). If, however, your Windows 2008 R2 system doesn't support verifying SHA-2 signed installers, OneAgent auto-update and installation won't work if `Applocker` is configured to block unknown publishers and/or security warnings may be displayed. For more information, see the Microsoft [2019 SHA-2 Code Signing Support requirement for Windows and WSUSï»¿](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f) announcement.