---
title: Install OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux
scraped: 2026-02-21T21:09:45.327132
---

# Install OneAgent on Linux

# Install OneAgent on Linux

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 22, 2026

This page describes how to download and install Dynatrace OneAgent on Linux.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements

You can install OneAgent on any Linux system that's [supported by Dynatrace](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks."), regardless of the packaging system your distribution depends on.

### Permissions

* You need [Download/install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions to download and install OneAgent.
* You only need [root rights](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") to start OneAgent installation. This requires that your system meets [specific requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#system-req "Find out when Dynatrace OneAgent requires root privileges on Linux."). Otherwise, add the `NON_ROOT_MODE=0` parameter to the installation command to disable OneAgent non-privileged mode.
* You need permissions and credentials for restarting all your application services.

### Resources

* Check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.").
* Your host requires 200 MB free memory to run OneAgent installation and update.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Limitations

There are certain limitations when deploying OneAgent on a Linux host Oracle Database Server 19c and/or with mounted NFS drives. See [Troubleshoot OneAgent installation](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.").

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation



1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. **Select installer type**
   OneAgent supports the following CPU architectures:

   * `Linux ARM` - ARM64 (AARch64) including [AWS Graviton processorsï»¿](https://aws.amazon.com/ec2/graviton/)
   * `PowerPC (BE)` - 64-bit PowerPC (ppc64be) [Learn more](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.")
   * `PowerPC (LE)` - 64-bit PowerPC (ppc64le)
   * `s390` - 64-bit IBM Z mainframe (s390) [Learn more](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.")
   * `x86-64` - 64-bit Intel/AMD
5. **Download the installer**  
   Paste the provided command into your terminal window and execute it.
6. **Verify the signature**  
   After the download is complete, select  **Copy** in the **Verify signature** box to copy the `wget` command to the clipboard, then paste the provided command into your terminal window and execute it. Make sure your system is up to date, especially SSL and related certificate libraries.
7. Optional **Set customized options**

   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * If your environment is segmented (for example, into development and production), consider [organizing your hosts into host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * You can override automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * You can also apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * Disable [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

   OneAgent command-line installer provides more options to [customize your installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. **Run the installer**  
   Paste the command into your terminal window and execute it. You'll need root access only to start OneAgent installation. Elevated privileges are dropped as soon as Dynatrace OneAgent is deployed.

   If youâre on an Ubuntu Server

   ```
   sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

   If youâre using Red Hat Enterprise Linux

   ```
   su -c '/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh'
   ```

   If you start a root session

   ```
   /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

* If you plan to download Dynatrace OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) prevent the installer from downloading.
* Dynatrace uses encrypted connections. OpenSSL is required to enable `wget` to access the server. You can also download the installer by selecting **Download OneAgent installer** in the page footer and saving the installer script to any location you want, which bypasses the `wget` command altogether.

What happens during installation?

Dynatrace OneAgent is a set of specialized services configured specifically for your monitoring environment. The role of these services is to monitor various aspects of your hosts, including hardware, operating system, and application processes.

During the installation process, the installer:

* Installs executable code and libraries that are used by Dynatrace OneAgent. OneAgent binaries are installed in the `/opt/dynatrace/oneagent` directory and startup scripts are created in `/etc/init.d` (on systemd systems, startup scripts are created in `/etc/systemd/system/`). One of the Linux OneAgent components, `liboneagentproc.so`, is located in the system library directory (`/lib` or `/lib64` depending on your architecture) and is enabled at `/etc/ld.so.preload`.
* Creates its own user (`dtuser`). This user is created without a password. It's not possible to login with this user. For security purposes, services that donât require root privileges will run under this user. Installation, however, still requires root access.
* Checks the systemâs global proxy settings.
* Checks for a connection to Dynatrace Server or ActiveGate (if you installed ActiveGate and downloaded the OneAgent installer after ActiveGate was connected to Dynatrace).
* Detects all SELinux-aware applications and adjusts the SELinux security policy accordingly.
* Allows Dynatrace OneAgent to inject its own libraries into monitored processes.
* Modifies the core pattern configuration so that OneAgent can detect and report process crashes. The original core\_pattern configuration will still work following installation and will be preserved in `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, where you can define your own core settings using the format as specified in [Linux Programmer's Manualï»¿](https://man7.org/linux/man-pages/man5/core.5.html).

For a summary of the changes made to your system by OneAgent installation, see [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.