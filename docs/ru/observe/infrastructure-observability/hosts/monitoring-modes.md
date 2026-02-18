---
title: Infrastructure and Discovery monitoring modes
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring-modes
scraped: 2026-02-06T16:20:45.488376
---

# Infrastructure and Discovery monitoring modes

# Infrastructure and Discovery monitoring modes

* Explanation
* 12-min read
* Updated on Oct 16, 2025

If you don't need your OneAgent to run in the full-stack monitoring mode, you can also use one of the two lightweight modes that provide you with the subset of OneAgent metrics, focusing on your host infrastructure:

* Infrastructure Monitoring mode
* Discovery mode

The table below shows an overview of available monitoring options for each of the monitoring modes.

|  | Discovery | Infrastructure | Full stack |
| --- | --- | --- | --- |
| Topology discovery (hybrid cloud discovery and Smartscape) | GA | GA | GA |
| Host criticality (detection of external services and app dependencies) | GA | GA | GA |
| Basic monitoring (host health, filesystem, OS Services) | GA | GA | GA |
| Host process details |  | GA | GA |
| Detailed disk analysis |  | GA | GA |
| Network analysis |  | GA | GA |
| Memory analysis |  | GA | GA |
| Extensions |  | opt-in | opt-in |
| Custom metrics |  | 100 / host | 15 / 256 MiB |
| Log Management | opt-in | opt-in | opt-in |
| Tracing and profiling |  |  | GA |
| Process injection |  | opt-out | GA |
| Application Security[1](#fn-1-1-def) | opt-in | opt-in | opt-in |
| Live Debugger | opt-in | opt-in | opt-in |

1

For more information on Infrastructure Monitoring and Discovery modes for Application Security, see [Monitoring modes for Application Security](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

## Default monitoring mode

You can define a default monitoring mode before installing OneAgent. This will change the default **Full-Stack** monitoring mode on the OneAgent deployment page (for Linux, Windows, and AIX operating systems) and in the **Discovery & Coverage** app (when deploying OneAgent from the **Install OneAgent** page).

To define a default monitoring mode

1. Go to **Settings** > **Preferences** > **OneAgent default mode**.
2. Select a **OneAgent default monitoring mode** from the dropdown list.
3. Select **Save changes**.

The selected value will be set as a default value for the chosen OneAgent deployment mode.

## Discovery mode

OneAgent version 1.281+

OneAgent Discovery mode provides basic metrics enabling you to discover your hosts and processes and learn the potential to extend your monitoring.

We recommend that you deploy OneAgent in Full-Stack Monitoring mode to monitor your business-critical applications. Similarly, we recommend that you monitor critical infrastructure, like databases, queues, and messaging systems with Infrastructure Monitoring. OneAgent in Discovery mode can be deployed across the remainder of your infrastructure for full visibility thanks to its relatively low cost.

Discovery mode is available only if you're using the Dynatrace Platform Subscription model. License consumption is via the **Foundation & Discovery** capability. To learn more, see [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability#discovery "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

The following built-in metrics are available in Discovery mode:

### CPU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.cpu.entConfig | AIX Entitlement configured Capacity Entitlement is the number of virtual processors assigned to the AIX partition. It's measured in fractions of processor equal to 0.1 or 0.01. For more information about entitlement, see [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) in official IBM documentation. | Ratio | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used Percentage of entitlement used. Capacity Entitlement is the number of virtual cores assigned to the AIX partition. See for more information about entitlement, see [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) in official IBM documentation. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.idle | CPU idle Average CPU time, when the CPU didn't have anything to do | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | CPU I/O wait Percentage of time when CPU was idle during which the system had an outstanding I/O request. It is not available on Windows. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.load | System load The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last minute | Ratio | autoavgmaxmin |
| builtin:host.cpu.load15m | System load15m The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 15 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.load5m | System load5m The average number of processes that are being executed by CPU or waiting to be executed by CPU over the last 5 minutes | Ratio | autoavgmaxmin |
| builtin:host.cpu.other | CPU other Average CPU time spent on other tasks: servicing interrupt requests (IRQ), running virtual machines under the control of the host's kernel (meaning the host is a hypervisor for VMs). It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed Total CPUs consumed by the AIX partition | Ratio | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal Average CPU time, when a virtual machine waits to get CPU cycles from the hypervisor. In a virtual environment, CPU cycles are shared across virtual machines on the hypervisor server. If your virtualized host displays a high CPU steal, it means CPU cycles are being taken away from your virtual machine to serve other purposes. It may indicate an overloaded hypervisor. It's available only for Linux hosts | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.system | CPU system Average CPU time when CPU was running in kernel mode | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.usage | CPU usage % Percentage of CPU time when CPU was utilized. A value close to 100% means most host processing resources are in use, and host CPUs can't handle additional work | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.user | CPU user Average CPU time when CPU was running in user mode | Percent (%) | autoavgmaxmin |
| builtin:host.kernelThreads.blocked | AIX Kernel threads blocked Length of the swap queue. The swap queue contains the threads ready to run but swapped out with the currently running threads | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Kernel threads I/O event wait Number of threads that are waiting for file system direct (cio) + Number of processes that are asleep waiting for buffered I/O | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioMessageWait | AIX Kernel threads I/O message wait Number of threads that are sleeping and waiting for raw I/O operations at a particular time. Raw I/O operation allows applications to direct write to the Logical Volume Manager (LVM) layer | Count | autoavgmaxmin |
| builtin:host.kernelThreads.running | AIX Kernel threads runnable Number of runnable threads (running or waiting for run time) (threads ready). The average number of runnable threads is seen in the first column of the vmstat command output | Count | autoavgmaxmin |

### Memory



| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available The amount of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available % The percentage of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. Shows available memory as percentages. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory The memory used by the system kernel. It includes memory used by core components of OS along with any device drivers. Typically, the number will be very small. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable The memory usage for specific purposes. Reclaimable memory is calculated as available memory (estimation of how much memory is available for use without swapping) minus free memory (amount of memory that is currently not used for anything). For more information on reclaimable memory, see [this blog post](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total The amount of memory (RAM) installed on the system. | Byte | autovalue |
| builtin:host.mem.usage | Memory used % Shows percentage of memory currently used. Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. Note: Calculated by taking 100% - "Memory available %". | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. | Byte | autoavgmaxmin |

### Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability.state | Host availability Host availability state metric reported in 1 minute intervals | Count | autovalue |
| builtin:host.uptime | Host uptime Time since last host boot up. Requires OneAgent 1.259+. The metric is not supported for application-only OneAgent deployments. | Second | autoavgmaxmin |

### Disk

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.disk.avail | Disk available Amount of free space available for user in file system. On Linux and AIX it is free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Byte | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second Speed of read from file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second Speed of write to file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.free | Disk available % Percentage of free space available for user in file system. On Linux and AIX it is % of free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.used | Disk used Amount of used space in file system | Byte | autoavgmaxmin |

### Network

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.net.nic.bytesRx | NIC bytes received Network interface bytes received on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host Network interface bytes sent on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization Network interface receive link utilization on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization Network interface transmit link utilization on the host | Percent (%) | autoavgmaxmin |

### Enable Discovery mode

You turn on Discovery mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Discovery mode during OneAgent installation, use the `--set-monitoring-mode=discovery` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Discovery mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Discovery**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=discovery` parameter.

### Code-module injection

For [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") and [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") to work in Discovery mode, code-module injection is required. Code-module injection is disabled by default.

After [turning on Discovery mode](#enable-discovery-mode), you can turn on the code-module injection for a single host.

1. Go to the settings page of the desired host and select **Host monitoring**.
2. Go to **Advanced settings**.
3. Turn on **CodeModule Injection**, then select **Save changes**.
4. Restart the monitored processes on the host.

For details on how Application Security works in Discovery mode, see [Application Security: Discovery mode](/docs/secure/application-security#discovery "Access the Dynatrace Application Security functionalities.").

## Infrastructure Monitoring mode

OneAgent auto-injection

OneAgent in Infrastructure Monitoring mode automatically injects into processes to be able to monitor backing services written in Java and runtime metrics for supported languages. Learn how to [turn off auto-injection](#disable-auto-injection).

While Full-Stack mode provides complete application performance monitoring, code-level visibility, deep process monitoring, and Infrastructure Monitoring (including PaaS platforms) for use cases where less visibility is required, OneAgent can be configured for Infrastructure Monitoring mode, which provides physical and virtual infrastructure-centric monitoring, along with log monitoring and AIOps.

### Enable Infrastructure Monitoring mode



You turn on Infrastructure Monitoring mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Infrastructure Monitoring mode during OneAgent installation, use the `--set-monitoring-mode=infra-only` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Infrastructure Monitoring mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Infrastructure**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=infra-only` parameter.
* Use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to turn on Infrastructure Monitoring mode at scale.
* To download the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring` as the schemaId and create your configuration object using [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Process injection

Process injection provides you with additional data for Infrastructure Monitoring. Process injection is enabled by default.

If you run your OneAgent as a container with Infrastructure Monitoring mode enabled, process injection will not be performed.

Infrastructure Monitoring mode enables you to monitor any infrastructure component and backing service written in Java. You can monitor backing services supported by default (for example, Kafka or ActiveMQ), and you can also build your own custom [JMX and PMI extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") for infrastructure components and use them in Infrastructure Monitoring mode.

Additionally, with process injection, Infrastructure Monitoring mode provides runtime metrics for:

* Java
* .NET
* Node.js
* Golang
* PHP
* Web servers such as Apache HTTP, NGINX, or Microsoft IIS.

### Disable process auto-injection

We don't recommend turning off auto-injection, but if you're required to do so due to strict security requirements, you can choose among various options. Turning off auto-injection also prevents Dynatrace from discovering vulnerabilities or live debugging in your environment, even if you enable [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") or [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace."). You can turn off automatic injection at the host or environment level.

#### Disable auto-injection for a single host

After OneAgent installation with UI

1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
3. Select **Host Monitoring**.
4. Go to **Advanced settings**.
5. Turn off **ProcessAgent Injection**, then select **Save changes**.
6. Restart the monitored processes on the host.

After OneAgent installation with command line

Use the [OneAgent command line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-auto-injection-enabled=false` parameter.

If you use oneagentctl to turn off automatic injection, you won't be able to control auto-injection in Infrastructure Monitoring mode using the Dynatrace web UI at **Settings > Monitoring > Monitored technologies** or [OneAgent monitoring configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Disable auto-injection for an environment

Define custom process monitoring rules

You can turn off process injection for particular process groups using custom process monitoring rules.

Custom process monitoring rules give you fine-grained control over which processes OneAgent injects into, with an approach that scales easily within large environments. You donât need to adjust your system configuration, and a few rules can cover thousands of processes.

For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Disable runtime metrics

You can disable the collection on JMX/PMI and runtime metrics, which will result in disabling auto-injection in Infrastructure Monitoring mode.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. In the list of supported technologies, search for the **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode** entry.
3. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit it and then disable it.
4. Restart all processes on your infrastructure-monitored hosts.

Disable selected extensions

You can also turn off selected extensions collecting the metrics at the environment level.

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Supported technologies

   Custom extensions

   1. In the list of supported technologies, search for technologies marked as **JMX monitoring** in the **Type** column.
   2. Select the pencil icon ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") to edit an extension of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. In the list of custom extensions, search for extensions marked as **JMX** or **PMI** in the **Extension type** column.
   2. Select the extension name of your choice.
   3. Turn off **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   The setting at the host level takes precedence over environment settings. If a host is configured to **Use host configuration** for the extension and the extension isn't activated on this host, the environment configuration won't be applied. To make sure an extension is active on a single host level:

   1. Go to **Hosts** (previous Dynatrace) or ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and find an infrastructure-monitored host. You can filter by **Monitoring mode: Infrastructure only**.
   2. Open the host page.
   3. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
   4. In the **Monitored technologies** table, search for extensions of type **JMX extension**, **JMX monitoring**, or **PMI extension**.
   5. Select **Edit**. Use the **Activate `<extension name>` on this host** control.

### Filter hosts by injection status

When you turn off auto-injection, you can find such hosts using the **Auto-injection** filter on the **Deployment Status** page or [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Use Dynatrace web UI

1. Go to **Deployment Status** and then select the **OneAgents** tab.
2. Select the **Filter by** box, select **Auto-injection**, and select **Disabled manually**. You can also use one of the filters below to check other reasons. Note that a filter appears only if a host with a respective status is available in your deployment.

* **Enabled**  
  Auto-injection was successfully enabled.
* **Disabled manually**  
  Auto-injection was disabled [after OneAgent installation](#after-install), either using the Dynatrace web UI or `oneagentctl`.
* **Disabled on installation**  
  Auto-injection was disabled [during OneAgent installation](#during-install).
* **Disabled on sanity check**  
  Auto-injection wasn't enabled due to a failed test performed by the OneAgent installer before OneAgent installation started. Check the OneAgent installer log for details.
* **Failed on installation**  
  Auto-injection failed due to an error during OneAgent installation. Check the OneAgent installer log for details.

Use Dynatrace API

Run the [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") call with the `autoInjection` parameter set to `DISABLED_MANUAL`. The returned payload contains the list of OneAgents with auto-injection disabled [after OneAgent installation](#after-install) via either the Dynatrace web UI or `oneagentctl`.

## Virtualization monitoring



Dynatrace supports [virtualization monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). To monitor the virtual components in your environment, you need to complete an extra step beyond the initial setup. For full details, see [Set up virtualization monitoring](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.").

## FAQ

What happens when OneAgent injects itself into the monitored technology?

Along with injection, the injected module becomes dynamically linked to the monitored technology. Consequently, it becomes an integral part of the monitored process and can only be removed with a process restart. Depending on the OS (Windows/Linux/AIX), injection is performed in slightly different ways, but the outcome is quite similar.

I have turned off injection, but I can see that the Dynatrace deep code modules are still injected into monitored technologies.

The injection rules refer to the point in time when the process of a supported technology is started. After it is started, the deep-code monitoring module of OneAgent remains dynamically linked to the monitored technology and can be unloaded only by restarting the monitored process.

I have restarted/disabled/stopped OneAgent, but the injected modules remain active. What's going on?

With injection, the injected module becomes dynamically linked to the monitored technology. Consequently, it becomes an integral part of the monitored process and can be removed only by restarting the monitored process.

How does OneAgent monitor processes?

OneAgent injects into a process each time a new process is started in the system. OneAgent identifies the launched process (by name, location, user space, and so on) and, if it's supported for injection and if the injection rules don't exclude it, OneAgent sets up a dynamic link between the monitored process and one of the OneAgent deep-code monitoring modules.

I have disabled OneAgent in the web UI, but I still see the process active on the host and some form of network traffic is still going on between OneAgent and the Dynatrace cluster. I thought that disabled OneAgents would stop all activity.

Disabled OneAgents effectively stop monitoring your environment. However, the core of OneAgent, which is responsible for communication with the Dynatrace cluster, remains active. Because communication between OneAgent and Dynatrace clusters is always invoked on the OneAgent side, OneAgent needs to keep sending its status and asking the cluster if it needs to start monitoring again.