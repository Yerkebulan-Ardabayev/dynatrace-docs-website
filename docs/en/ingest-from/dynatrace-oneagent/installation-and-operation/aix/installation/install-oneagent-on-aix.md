---
title: Install OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix
scraped: 2026-02-18T21:28:19.810768
---

# Install OneAgent on AIX

# Install OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 07, 2025

This page describes how to download and install Dynatrace OneAgent on AIX.

To get started, log in to your Dynatrace SaaS environment via the [Dynatrace.comï»¿](https://www.dynatrace.com) website using the credentials provided during signup. Then continue with the installation steps below.

## Requirements

### Permissions

* You need [Download/install OneAgent](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") permissions to download and install OneAgent.
* You need administrator rights for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the internet).
* You need permissions and credentials for restarting all your application services.

### Resources

* Check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.").
* Your host requires 200 MB free memory to run OneAgent installation and update.
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Limitations

* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.
* The support for [Log management and Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") and [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") on AIX hosts is limited:

  + log detection in log module is limited only to custom log sources.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, search for **OneAgent**.
2. Select **Set up** > **AIX**.
3. Paste a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you'll use later.
4. In the **Download OneAgent** box, select  **Copy** to copy the `wget` command to the clipboard.
5. Log into your AIX host and then paste and execute the `wget` command that you just copied.

   * The `wget` command isn't installed on AIX by default. Either install it or use an alternative means of downloading OneAgent.
   * If you receive an error while downloading OneAgent, install the required certificate by downloading the root CA file from [Comodoï»¿](https://support.comodo.com/index.php?/Knowledgebase/Article/View/854/75/root-addtrustexternalcaroot) and then concatenating the content of the CRT file to `/var/ssl/cert.pem`. You can alternatively skip the certificate check by adding the parameter `--no-check-certificate`.
   * If you plan to download OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) will prevent the installer from downloading. We use encrypted connections. OpenSSL is required to enable `wget` to access the server.
6. **Verify the signature**

   After the download is complete, select  **Copy** in the **Verify signature** box to copy the `wget` command to the clipboard, then paste the provided command into your terminal window and execute it. Make sure your system is up to date, especially SSL and related certificate libraries.
7. Optional **Set customized options**

   * Enable monitoring of [Virtual I/O Server](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#vios-installation "Learn how to download and install Dynatrace OneAgent on AIX.") logical partition.
   * Set a [network zone](/docs/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.
   * If your environment is segmented (for example, into development and production), consider [organizing your hosts into host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * You can override the automatically detected [host name](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.
   * You can also apply [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") to the host to organize your monitored environments in a meaningful way.
   * Define [Properties](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.") to the host to automatically add metadata.
   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

     It is not available if the Virtual I/O Server monitoring option is enabled.

   The OneAgent command-line installer provides more options to [customize your installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. Copy the command provided in the **Run the installer with root rights** text field.
9. Run the installer.  
   Paste the command into your terminal and execute it.

   * You need root privileges. You'll need to make the script executable before you can run it as root.
   * You can use `su` or `sudo` to run the installation script. To do this, type the following command into the directory where you downloaded the installation script.  
     `sudo /bin/sh Dynatrace-OneAgent-AIX-1.0.0.sh`

   For a summary of the changes made to your system by OneAgent installation, see [OneAgent security on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").
10. On AIX, Dynatrace supports deep-code monitoring for Java, Apache, WebLogic, and Websphere applications. It's automated for OneAgent version 1.189+. For earlier releases, you need to perform some configuration on AIX, which can be easily done both for single applications as well as shell-wide.

    Automated injection of deep-code monitoring is enabled by default in Dynatrace version 1.195+ for fresh OneAgent 1.189+ installations.

    You can enable deep-code monitoring after you install OneAgent and it successfully connects to Dynatrace. On the **Hosts** page, find your host, go to **Host settings** > **Monitoring**, and select **Allow AIX kernel extension**.

## Installation on Virtual I/O Server (VIOS)

Use the generic installation steps to download the OneAgent, and then, after you have the OneAgent installer on your VIOS machine, issue the following commands.

1. Initiate the OEM installation and set up environment.

   ```
   oem_setup_env
   ```
2. Sign in to the `system` group.

   ```
   newgrp system
   ```
3. Install OneAgent.

   * The `--set-monitoring-mode=infra-only` parameter enables Infrastructure Monitoring.
   * The `--set-auto-injection-enabled=false` parameter disables automatic injection into processes.

   ```
   /bin/sh Dynatrace-OneAgent.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
   ```
4. Return to the Virtual I/O Server prompt.

   ```
   exit
   ```

## Manual OneAgent injection

If you can't use the unified monitoring approach, you can inject OneAgent manually.

Processes that have been given special privileges using AIX's Role-Based Access Control (RBAC) system can't be auto-injected. This is a safety mechanism of the operating system to restrict unknown code from being run with elevated privileges. For example, an Apache or IHS web server might have been given the `PV_NET_PORT` privilege to allow starting the server as a non-root user but still letting it bind into restricted ports like port `80`. In this case, any libraries configured for preloading, including OneAgent, will be silently ignored. In such cases, only manual OneAgent injection will work.

Manual OneAgent injection

IBM Java 1.6 â 1.8

IBM/Apache HTTP Server

Prepend your application command with the following commands:

```
export DT_HOME=/opt/dynatrace/oneagent



export LDR_PRELOAD64=$DT_HOME/agent/lib64/liboneagentproc.so



export LDR_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so
```

The `DT_HOME` variable must point to your OneAgent installation folder. If you customized your OneAgent installation directory, adjust `DT_HOME` variable accordingly. You can omit either the 32-bit or 64-bit entry, depending on your environment.

Edit your `httpd.conf` and add the following two lines at a location of your choice:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Alternatively, if you prefer to leave your `httpd.conf` unchanged, you can specify the same directives using the command line:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID` is the [environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") ID of your Dynatrace environment that should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantUUID` parameter is represented in the script as `DT_TENANT`.
* `tenantToken` is the [token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") that OneAgent uses to send data Dynatrace. It should be pulled from `dynatrace-env.sh` (or `ruxitagent.conf`, depending on your OneAgent version), which is located in the OneAgent installation root directory. The `tenantToken` parameter is represented in the script as `DT_TENANTTOKEN`.

  This token should not be confused with Dynatrace API or PaaS tokens. Those tokens can't be used here.
* `communicationEndpoints` corresponds to one or multiple HTTP addresses that represent Dynatrace Servers or ActiveGates. The `communicationEndpoints` parameter is represented in the script as `DT_CONNECTION_POINT`. For example, the `dynatrace-env.sh` (located in the OneAgent installation root directory) may contain the following:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  In this case, the parameter would be

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## You've arrived!

Great, the setup is complete! You can now take a look around your new monitoring environment.

You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.