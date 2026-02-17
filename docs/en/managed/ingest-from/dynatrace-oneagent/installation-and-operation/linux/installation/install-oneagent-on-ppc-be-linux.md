---
title: Install OneAgent on PPC BE Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux
scraped: 2026-02-17T21:22:50.611004
---

# Install OneAgent on PPC BE Linux

# Install OneAgent on PPC BE Linux

* Latest Dynatrace
* 3-min read
* Updated on Jan 22, 2026

To install Dynatrace OneAgent when you have a Dynatrace SaaS deployment, go to [Dynatrace.comï»¿](https://www.dynatrace.com) and **Login** using the username and password you received from Dynatrace in your signup confirmation email. If you have a Dynatrace Managed deployment, [access the Cluster Management Console and choose the environmentï»¿](https://docs.dynatrace.com/managed/shortlink/managed-monitoring-environment) you want to monitor. Then continue with the installation steps provided below.

## Requirements

* You need the [permissions](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") for the following actions:

  + To create a directory where you want to install OneAgent
  + To change firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).
  + To restart your application services
* You also need to check the [disk space requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.").
* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on whether your Dynatrace deployment is SaaS or Managed, and depending on your network layout and security settings, you may choose to either provide direct access to the Dynatrace cluster, or you can [set up an ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

* On PPC BE Linux, OneAgent supports only Java and Apache/IHS.
* You don't need root access to install OneAgent on PPC BE Linux.
* You can install OneAgent in any directory.

### Allow connections through firewall

Ensure that your firewall settings allow communication to Dynatrace.  
Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**

## Installation

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.
3. Choose the **PowerPC (BE)** installer type from the list. Copy the command provided in the **Use this command on the target host to download OneAgent for Linux PowerPC (BE)** text field
4. Login to your PPC BE Linux host and execute the command you copied from Dynatrace.

   * If you plan to download Dynatrace OneAgent directly to a server, note that outdated or missing libraries (for example, CA certificates or OpenSSL) will prevent the download.
   * Dynatrace uses encrypted connections. OpenSSL is required to enable `wget` to access the server. You can also download the ZIP archive of OneAgent by clicking the **Download OneAgent installer** link in the page footer and saving the installer script to any location; this bypasses the `wget` command altogether.
5. In your file system, create a folder for OneAgent installation. For example, `/opt/dynatrace/oneagent`.
6. Unzip the ZIP archive of OneAgent into the newly created folder.

   All monitored applications must to be able to read the OneAgent library. Ensure that the permissions allow this.
7. You have two options now: either monitor every application on your host or just a single application.

   All applications

   Single application

   To automatically monitor every application on your host, enable the `liboneagentproc.so` component of OneAgent. This is located in the system library directory (`/lib` or `/lib64` depending on your architecture), at `/etc/ld.so.preload`.

   ## You've arrived!

   Great, the setup is complete! You can now take a look around your new monitoring environment.

   You can access your monitoring environment anytime by going to Dynatrace website and selecting **Login** in the upper-right corner.

   One last thing: to monitor your processes, you need to restart them. At any time, you can check which processes aren't monitored and need to be restarted. Just go to **Deployment Status**, switch to the **All hosts** or **Recently connected hosts** tab, and expand the host you are interested in.

   To monitor a single application, you need to restart it first. Prepend the application start command with the following commands:

   ```
   DT_HOME=<installation directory>



   export DT_HOME



   LD_PRELOAD=$DT_HOME/agent/<system library>/liboneagentproc.so



   export LD_PRELOAD
   ```

   Where:

   * `<installation directory>` is the directory where OneAgent is installed
   * `<system library>` is `/lib` or `/lib64` depending on your architecture

   ## You've arrived!

   Great, setup is complete! You can now take a look around your new monitoring environment. If you have a SaaS deployment, you can access your monitoring environment anytime by going to [Dynatrace.comï»¿](https://www.dynatrace.com) and clicking the **Login** button in the upper-right corner. If you have a Dynatrace Managed deployment, you can [access your monitoring environment through the Cluster Management Consoleï»¿](https://docs.dynatrace.com/managed/shortlink/managed-monitoring-environment).