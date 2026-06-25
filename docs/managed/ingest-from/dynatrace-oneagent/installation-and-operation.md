---
title: Install OneAgent on a server
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-05-12T11:06:38.497546
---

# Install OneAgent on a server

# Install OneAgent on a server

* 3-min read
* Updated on Jan 22, 2026

Follow this guide to install Dynatrace OneAgent for the very first time.

Once you've followed this guide, you'll have OneAgent installed onto a host and can use Dynatrace to monitor that host and its processes.

The information on this page is platform-agnostic.

For OS-specific information on OneAgent installation and advanced operation, select your OS for the detailed instructions.

[Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [zOS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

## Prerequisites

This guide assumes that you have:

* A Dynatrace environment.
* Administrator access to a Linux, Windows, or AIX host (that doesn't have any existing OneAgent installations).
* A network that supports SSL communication.

## OneAgent setup

To download and install OneAgent on a host:

1. Go to **Deploy Dynatrace**.
2. Select **Start installation**. Then select your platform where you want to install OneAgent.

   ![OneAgent platform selection](https://dt-cdn.net/images/download-dynatrace-oneagent-1213-68157f2673.png)

   OneAgent platform selection
3. Paste your PaaS token in the **Download token** field or select **Create token** to generate a new Deployment API token.

   Copy the token and save it somewhere safe, because you will not be able to access it again.
4. Enter or select the appropriate parameters

   * **Architecture**

     Linux only Select one of the available options from the list.
   * **Monitoring mode**

     Options are **Full-Stack**, **Infrastructure**, or **Discovery**.
     If you are using a free Dynatrace trial, select **Full-Stack** to see everything that Dynatrace is capable of observing.
     You can always change the monitoring mode after installation.
   * For **Optional parameters**, you can add a **Custom host name** for easier identification.

     The rest of the parameters are out of scope for this guide.

   ![OneAgent deployment parameters](https://dt-cdn.net/images/oneagent-installation-1-668-edc694da5b.png)

   OneAgent deployment parameters
5. Download OneAgent.
   Either use the provided CLI command or select  **Download**.
6. Verify the signature.
   Use the provided CLI command.
   (Note: Linux and AIX only.)
7. Install OneAgent.
   Either use the provided CLI command or run the executable by selecting it in the GUI.
   Follow the steps as described in the installer.

   If you install via the GUI, you should add the following options in the **Optional: advanced command-line settings** screen:
   `--set-monitoring-mode=fullstack --set-app-log-content-access=true`
8. When the installer shows a **Congratulations! Dynatrace OneAgent was successfully installed!** message, OneAgent is installed on the host.
   Select **Finish** to exit the installer.
9. Because OneAgent can't inject itself into running processes, you'll need to restart all processes that you want OneAgent to monitor.
10. To confirm that OneAgent is monitoring your host, open Dynatrace and go to **Infrastructure & Operations** > **Host**.
    If everything is working as expected, you'll see the name of your host in the **Hosts** table.
    See the screenshot below for an example.

OneAgent is now set up and monitoring your host. See [Get started](/managed/discover-dynatrace/get-started "Learn how to get started with Dynatrace Managed.") to continue your first journey with Dynatrace.

## Related topics

* [OneAgent features](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")
* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Host-level settings](/managed/observe/infrastructure-observability/hosts/configuration "Host-level settings")
* [OneAgent monitoring modes](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")