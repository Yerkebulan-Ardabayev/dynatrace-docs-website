---
title: Install OneAgent on a server
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-02-17T21:13:34.936391
---

# Install OneAgent on a server

# Install OneAgent on a server

* Latest Dynatrace
* 3-min read
* Updated on Jan 22, 2026

Follow this guide to install Dynatrace OneAgent for the very first time.

Once you've followed this guide, you'll have OneAgent installed onto a host and can use Dynatrace to monitor that host and its processes.

The information on this page is platform-agnostic.

For OS-specific information on OneAgent installation and advanced operation, select your OS for the detailed instructions.

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

## Prerequisites

This guide assumes that you have:

* A Dynatrace environment.
* Administrator access to a Linux, Windows, or AIX host (that doesn't have any existing OneAgent installations).
* A network that supports SSL communication.

## OneAgent setup

To download and install OneAgent on a host:

1. In **Dynatrace Hub**, select **OneAgent**.
2. Select **Set up** .
   The **Install OneAgent** window opens.
3. Enter or select the appropriate parameters (see the screenshot below for an example).

   * **OS type**

     Choose **Linux**, **Windows**, or **AIX** according to your host's OS.

   * **Architecture** (Linux only)
   * **Monitoring mode**
     Options are **Full-Stack**, **Infrastructure**, or **Discovery**.
     If you are using a free Dynatrace trial, select **Full-Stack** to see everything that Dynatrace is capable of observing.
     You can always change the monitoring mode after installation.
   * For **Optional parameters**, you might want to add a **Custom host name** for easier identification.
     The rest of the parameters are out of scope for this guide.

   ![OneAgent setup parameters](https://dt-cdn.net/images/screenshot-2025-02-05-at-15-06-49-2992-637e933241.png)
4. Select **Generate token** to generate an API token that lets your Dynatrace environment access OneAgent.
   Copy the token and save it somewhere safe, because you will not be able to access it again.
   You don't need to do anything else with this token right now.

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

    ![Infrastructure & Operations view of a newly added OneAgent on host](https://dt-cdn.net/images/screenshot-2025-02-04-at-13-32-36-2598-439524d1f9.png)

OneAgent is now set up and monitoring your host. See [Get started with Dynatrace](/docs/discover-dynatrace/get-started "Learn about Dynatrace monitoring capabilities, concepts, and deployment models and find out how to get started with SaaS and Managed deployments.") to continue your first journey with Dynatrace.

## Related topics

* [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")
* [Infrastructure & Operations](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")
* [Host-level settings](/docs/observe/infrastructure-observability/hosts/configuration "Host-level settings")
* [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")