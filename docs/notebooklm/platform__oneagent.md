# Документация Dynatrace: platform/oneagent
Язык: Русский (RU)
Сгенерировано: 2026-02-27
Файлов в разделе: 6
---

## platform/oneagent/how-one-agent-works.md

---
title: How OneAgent works
source: https://www.dynatrace.com/docs/platform/oneagent/how-one-agent-works
scraped: 2026-02-27T21:12:47.359192
---

# How OneAgent works

# How OneAgent works

* Latest Dynatrace
* 2-min read
* Published Oct 13, 2018

OneAgent comprises a set of specialized processes that run on each monitored host. It collects metrics from the operating system on which it runs, and compares the metrics to expected performance values. The most important metrics are then reported to Dynatrace.

## Processes

In addition, OneAgent detects which processes run on each host and collects performance metrics for the most important processes. OneAgent can also perform more detailed monitoring of specific technologies (such as Java, Node.js, .NET, and others) by injecting itself into those processes and monitoring their performance from within. This provides you with code-level insights into the services that your applications rely on.

## Real user monitoring

To deliver Real User Monitoring, OneAgent injects a JavaScript tag into the HTML of each application page that is rendered by your web servers. With these JavaScript tags in placeâalong with a corresponding module that is automatically installed on your web server and requires no configurationâOneAgent is able to monitor the response times and performance experienced by your customers in their mobile and desktop browsers.

## Log monitoring

OneAgent is also capable of monitoring the log files of a specific host or a specific process group. It can discover and analyze system or process-created logs. Depending on your configuration, you can store these log files, which makes the log data available independently of the log files themselves. This can be beneficial in the following situations:

* Short log-retention periods
* Volatile log storage
* Legal requirements to keep logs archived centrally

## Network

OneAgent can dig deeper and get network metrics at the process level. Thanks to process-to-process monitoring of network communications Dynatrace can:

* Ensure high-quality process communications over networks.
* Understand your network topology in dynamic environments.
* Monitor process-level network capacity.
* Perform integrated network health monitoring.

## Communication

Communication from OneAgent to Dynatrace is outbound only and Dynatrace never initiates communication with OneAgent. Because of this, when using Dynatrace, there is no need to open ports for inbound communication.  
OneAgent can connect directly to Dynatrace Cluster or it can communicate via one or more [Dynatrace ActiveGates](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."). Simultaneous connection via multiple ActiveGates is possible. OneAgent determines which ActiveGates to communicate through based on the information it receives from Dynatrace Cluster.

OneAgent reports its collected data via HTTP/S requests to the ActiveGates or the Dynatrace Cluster. If [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") is enabled, the OneAgent will create a WebSocket session to the ActiveGates or the Cluster to allow realtime communication and reporting of its collected snapshots. WebSocket sessions are multiplexed by the ActiveGates to limit network load and are load balanced by the OneAgents.

---

## platform/oneagent/monitoring-modes/enable-monitoring-modes.md

---
title: Enable OneAgent monitoring modes
source: https://www.dynatrace.com/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes
scraped: 2026-02-27T21:12:59.143524
---

# Enable OneAgent monitoring modes

# Enable OneAgent monitoring modes

* Latest Dynatrace
* How-to guide
* 8-min read
* Published Nov 26, 2025

By default, [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") runs in Full-Stack monitoring mode, giving you complete visibility across hosts, processes, and services. If you prefer a lighter approach, you can switch to one of the two alternative modes that focus on essential infrastructure metrics:

* Infrastructure monitoring mode
* Discovery mode

## Select a default monitoring mode

You can define a default monitoring mode before installing OneAgent. This will change the default **Full-Stack** monitoring mode on the OneAgent deployment page (for Linux, Windows, and AIX operating systems) and in the ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** app (when deploying OneAgent from the **Install OneAgent** page).

To define a default monitoring mode

1. Go to **Settings** > **Preferences** > **OneAgent default mode**.
2. Select a **OneAgent default monitoring mode** from the dropdown list.
3. Select **Save changes**.

The selected value will be set as a default value for the chosen OneAgent deployment mode.

## Enable Infrastructure monitoring mode

You can turn on Infrastructure monitoring mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Infrastructure monitoring mode during OneAgent installation, use the `--set-monitoring-mode=infra-only` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Infrastructure monitoring mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
  2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
  3. Select **Host monitoring**.
  4. Go to **Monitoring Mode** and in the drop-down menu select **Infrastructure**.
  5. Select **Save changes**.
* Use the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-monitoring-mode=infra-only` parameter.
* Use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to turn on Infrastructure Monitoring mode at scale.
* To download the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring` as the schemaId and create your configuration object using [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Process injection

Process injection provides you with additional data for Infrastructure Observability. Process injection is enabled by default.

If you run your OneAgent as a container with Infrastructure monitoring mode enabled, process injection will not be performed.

Infrastructure monitoring mode enables you to monitor any infrastructure component and backing service written in Java. You can monitor backing services supported by default (for example, Kafka or ActiveMQ), and you can also build your own custom [JMX and PMI extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") for infrastructure components and use them in Infrastructure monitoring mode.

Additionally, with process injection, Infrastructure monitoring mode provides runtime metrics for:

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

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
2. Select **More** (**â¦**) > **Settings** in the upper-right corner to display the **Host settings** page.
3. Select **Host Monitoring**.
4. Go to **Advanced settings**.
5. Turn off **ProcessAgent Injection**, then select **Save changes**.
6. Restart the monitored processes on the host.

After OneAgent installation with command line

Use the [OneAgent command line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") to set the `--set-auto-injection-enabled=false` parameter.

If you use oneagentctl to turn off automatic injection, you won't be able to control auto-injection in Infrastructure monitoring mode using the Dynatrace web UI at **Settings > Monitoring > Monitored technologies** or [OneAgent monitoring configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Disable auto-injection for an environment

Define custom process monitoring rules

You can turn off process injection for particular process groups using custom process monitoring rules.

Custom process monitoring rules give you fine-grained control over which processes OneAgent injects into, with an approach that scales easily within large environments. You donât need to adjust your system configuration, and a few rules can cover thousands of processes.

For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Disable runtime metrics

You can disable the collection on JMX/PMI and runtime metrics, which will result in disabling auto-injection in Infrastructure monitoring mode.

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

   1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and find an infrastructure-monitored host. You can filter by **Monitoring mode: Infrastructure only**.
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

## Enable Discovery monitoring mode

You can turn on Discovery mode at the host level, either during or after OneAgent installation.

During OneAgent installation

To turn on Discovery mode during OneAgent installation, use the `--set-monitoring-mode=discovery` parameter.

For more information, see the [OneAgent installation](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") documentation that's specific to your environment.

After OneAgent installation

To turn on Discovery mode after OneAgent installation, use one of these options:

* In Dynatrace

  1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and open a host overview page.
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

---

## platform/oneagent/monitoring-modes/monitoring-modes.md

---
title: OneAgent monitoring modes
source: https://www.dynatrace.com/docs/platform/oneagent/monitoring-modes/monitoring-modes
scraped: 2026-02-27T21:10:49.509012
---

# OneAgent monitoring modes

# OneAgent monitoring modes

* Latest Dynatrace
* Explanation
* 5-min read
* Updated on Nov 26, 2025

Using [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") to collect performance and health data from your environment gives you deep observability across applications, services, and infrastructure. To accommodate different use cases and resource requirements, OneAgent supports multiple monitoring modes.

If you don't need full-stack monitoring, you can choose one of the two lightweight modes that focus on essential infrastructure metrics:

* Infrastructure monitoring mode
* Discovery monitoring mode

Here is an overview of available monitoring options for each monitoring mode.

| Component | Full stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| Topology discovery (hybrid cloud discovery and Smartscape) | GA | GA | GA |
| Host criticality (detection of external services and app dependencies) | GA | GA | GA |
| Basic monitoring (host health, filesystem, OS Services) | GA | GA | GA |
| Host process details | GA | GA |  |
| Detailed disk analysis | GA | GA |  |
| Network analysis | GA | GA |  |
| Memory analysis | GA | GA |  |
| Extensions | opt-in | opt-in |  |
| Custom metrics | 15 / 256 MiB | 100 / host |  |
| Log Management | opt-in | opt-in | opt-in |
| Tracing and profiling | GA |  |  |
| Process injection | GA | opt-out |  |
| Application Security[1](#fn-1-1-def) | opt-in | opt-in | opt-in |
| Live Debugger | opt-in | opt-in | opt-in |

1

For more information on Infrastructure mode and Discovery mode for Application Security, see [Monitoring modes for Application Security](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

## Infrastructure monitoring mode

OneAgent auto-injection

OneAgent in Infrastructure monitoring mode automatically injects into processes to be able to monitor backing services written in Java and runtime metrics for supported languages. Learn how to [turn off auto-injection](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes#disable-auto-injection "Learn how to enable monitoring modes when using OneAgent.").

Full-stack monitoring mode provides comprehensive application performance monitoring, including code-level visibility, in-depth process monitoring, and infrastructure monitoring (including PaaS platforms). However, if your focus is more on infrastructure health rather than in-depth application analysis, you can configure OneAgent to use Infrastructure monitoring mode, which focuses on physical and virtual infrastructure, log monitoring, and AIOps capabilities.

For more details, see [Enable Infrastructure monitoring mode](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes#enable-infrastructure-monitoring-mode "Learn how to enable monitoring modes when using OneAgent.").

## Discovery monitoring mode

OneAgent version 1.281+

Discovery monitoring mode provides basic metrics enabling you to discover your hosts and processes and learn the potential to extend your monitoring.

We recommend deploying OneAgent in Full-Stack monitoring mode to monitor your business-critical applications. Similarly, we recommend monitoring critical infrastructure, such as databases, queues, and messaging systems, with Infrastructure Observability. OneAgent in Discovery mode can be deployed across the remainder of your infrastructure for complete visibility, thanks to its relatively low cost.

Discovery mode is available only if you're using the Dynatrace Platform Subscription model. License consumption is via the **Foundation & Discovery** capability. To learn more, see [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability#discovery "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

For more details, see [Enable Discovery monitoring mode](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes#enable-discovery-mode "Learn how to enable monitoring modes when using OneAgent.").

The following built-in metrics are available in Discovery mode:

CPU

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

Memory

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available The amount of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available % The percentage of memory (RAM) available on the host. The memory that is available for allocation to new or existing processes. Available memory is an estimation of how much memory is available for use without swapping. Shows available memory as percentages. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory The memory used by the system kernel. It includes memory used by core components of OS along with any device drivers. Typically, the number will be very small. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable The memory usage for specific purposes. Reclaimable memory is calculated as available memory (estimation of how much memory is available for use without swapping) minus free memory (amount of memory that is currently not used for anything). For more information on reclaimable memory, see [this blog post](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total The amount of memory (RAM) installed on the system. | Byte | autovalue |
| builtin:host.mem.usage | Memory used % Shows percentage of memory currently used. Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. Note: Calculated by taking 100% - "Memory available %". | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used Used memory is calculated by OneAgent as follows: used = total - available. So the used memory metric displayed in Dynatrace analysis views is not equal to the used memory metric displayed by system tools. At the same time, it's important to remember that system tools report used memory the way they do due to historical reasons, and that this particular method of calculating used memory isn't really representative of how the Linux kernel manages memory in modern systems. The difference in these measurements is in fact quite significant, too. | Byte | autoavgmaxmin |

Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability.state | Host availability Host availability state metric reported in 1 minute intervals | Count | autovalue |
| builtin:host.uptime | Host uptime Time since last host boot up. Requires OneAgent 1.259+. The metric is not supported for application-only OneAgent deployments. | Second | autoavgmaxmin |

Disk

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.disk.avail | Disk available Amount of free space available for user in file system. On Linux and AIX it is free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Byte | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second Speed of read from file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second Speed of write to file system in bytes per second | Byte/second | autoavgmaxmin |
| builtin:host.disk.free | Disk available % Percentage of free space available for user in file system. On Linux and AIX it is % of free space available for unprivileged user. It doesn't contain part of free space reserved for the root. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.used | Disk used Amount of used space in file system | Byte | autoavgmaxmin |

Network

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.net.nic.bytesRx | NIC bytes received Network interface bytes received on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host Network interface bytes sent on the host | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization Network interface receive link utilization on the host | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization Network interface transmit link utilization on the host | Percent (%) | autoavgmaxmin |



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

---

## platform/oneagent/resource-attributes.md

---
title: Resource attributes
source: https://www.dynatrace.com/docs/platform/oneagent/resource-attributes
scraped: 2026-02-27T21:28:49.442702
---

# Resource attributes

# Resource attributes

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jul 23, 2025

## Host-level resource attributes

All monitoring artifacts that leave a given host, that is have the host as its resource, are enriched with the host-level resource attributes.

Host-level resource attributes are resource attributes of monitored hosts. All events raised by and measurements coming from OneAgent components running on a given host are enriched with those attributes. You can then use them in your queries to structure and filter the monitoring data.

You can also use some of the attributes to create policies to manage data access. See [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and search for fields tagged as Permission

If you have access to a host with OneAgent installed, you can inspect the `dt_host_metadata.json` and `dt_host_metadata.properties` to see the scope of resource attributes enrichment provided by OneAgent. For more information, see [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### Custom host-level attributes

You can create your own attributes by configuring key-value tags and properties set via [oneagentctl](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.") or through [Remote configuration management of OneAgents and ActiveGates](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API."). Custom tags and properties defined this way are reported as flat, first-level resource attributes.

The key tags with no value are ignored.

Tags assigned through [automated rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), [environment variables](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables."), and [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") are not included.

As the keys depend on your configuration, they aren't covered by Semantic Dictionary.

Tag names can't be prefixed with `dt.` except for the following tags that are subject to your configuration:

* `dt.security_context` - attribute to manage data access using policies. See [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").
* `dt.cost.costcenter` - attribute to assign usage to a Cost Center. See [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.").
* `dt.cost.product` - attribute to assign usage to a Product or Application ID. See [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.").

Attributes coming from custom properties and tags don't override the built-in enrichments if they have the same name. When creating your custom properties and tags, check [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") to make sure your name isn't already used.

#### Handling name clashes when merging custom properties and tags

Host-level resource attributes can be imported from host custom properties and tags. The `hostcustomproperties.conf` and `hostautotag.conf` files are the sources for these attributes. If they follow the `key=value` pattern, the same keys can exist in both files but with different values. When merged, the content from `hostautotag.conf` takes priority over the content from `hostcustomproperties.conf`, as tags take priority in case of a name clash.

If a name clash happens when merging resource attributes at different levels, the lowest level takes priority.

### General host-level attributes

All host-level resource attributes follow [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities."), unless stated otherwise.

#### AWS

#### Azure

#### Google Cloud

#### OpenStack

#### Kubernetes

#### BOSH

### Resource attributes normalization

To ensure consistent and reliable metric ingestion, resource attributes normalization is applied to all relevant internal metric keys and values. This process helps prevent metrics from being dropped due to invalid or malformed dimensions.

#### Dimension key rules

| Rule description | Details |
| --- | --- |
| **Invalid Characters** | An invalid character or a series of invalid characters is replaced with one underscore `_`. For example, `zaÃ³$%Ä` is replaced with `za_`. |
| **Empty Keys** | Dimensions with no valid characters are skipped |
| **Key Length Limit** | OneAgent version 1.317+ Max. 350 characters (previously max. 100 characters) |

#### Dimension value rules

| Rule description | Details |
| --- | --- |
| **Allowed Characters** | All non-control characters (ASCII & Unicode) |
| **Control Characters** | Not allowed. A control character (that is a character used as an instruction and is not displayed; for example, line break, tab) or a series of those characters is replaced with one underscore `_`. |
| **Value Length Limit** | OneAgent version 1.313+ Max. 2048 characters (previously max. 255 characters) |
| **Quoted Values** | If value starts and ends with `"`, it is escaped |

#### Dimension limits

To align with the current specification, a specific dimension hierarchy and defined limits are used to prevent warnings and metric drops caused by exceeding those limits.

By default, the global dimension limit is equal to `100` and the customer-defined dimension limit is 40% of the global limit.

---

## platform/oneagent/supported-monitoring-types.md

---
title: OneAgent monitoring capabilities
source: https://www.dynatrace.com/docs/platform/oneagent/supported-monitoring-types
scraped: 2026-02-27T21:12:46.295403
---

# OneAgent monitoring capabilities

# OneAgent monitoring capabilities

* Latest Dynatrace
* 3-min read
* Published Oct 12, 2018

OneAgent offers a rich set of monitoring capabilities.

## Real User Monitoring

Real User Monitoring analyzes the performance of all user interaction with your applications, whether the interactions take place in a browser or on a mobile device. Real user monitoring also enables application availability monitoring, verification of correct display of UI elements, third-party content provider performance analysis, backend service performance analysis (down to the code level), and performance analysis of all underlying infrastructure. For details, see [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.").

## Mobile app monitoring

OneAgent supports real user monitoring for mobile applications as well. The process of monitoring the user experience of your native mobile applications is fundamentally different from monitoring browser-based web applications. This is because mobile-app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package. The process of instrumenting your mobile application largely depends on the platform of your mobile application. Dynatrace supports both Android and iOS platforms. For details, see [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.").

## Server-side service monitoring

Web applications consist of web pages that are served by web servers (for example, Apache Tomcat) and web containers (for example, Docker). The web requests that are sent to a specific Tomcat server are an example of a server-side service. Server-side services may be of various types like web services, web containers, database requests, and custom services. OneAgent can provide information such as which applications or services use which other services and whether or not a service makes calls to other services or databases. For details, see [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.").

## Network, process, and host monitoring

OneAgent enables monitoring throughout your entire infrastructure including your hosts, processes, and network. You can perform log monitoring and view information such as the total traffic of your network, the CPU usage of your hosts, the response time of your processes, and more. OneAgent also provides detailed topological information so that you know, for example, which processes run on which hosts and how your processes are interconnected. For details, see [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

## Cloud and virtual machine monitoring

OneAgent monitors your entire stack, including private, public, and hybrid cloud environments. Whether you run on AWS, Azure, Cloud Foundry, or OpenStack, OneAgent auto-detects all virtualized components and keeps up with all changes. OneAgent can be integrated with your virtualized infrastructure, allowing you to connect the dots between the dependencies of the vCenters in your data center, the processes that run on them, and your applications. For details, see [Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

## Docker container monitoring

OneAgent seamlessly integrates with existing Docker environments and automatically monitors your containerized applications and services. Thereâs no need to modify your Docker images, modify run commands, or create additional containers to enable Docker monitoring. Simply install OneAgent on your hosts that serve containerized applications and services. OneAgent automatically detects the creation and termination of containers and monitors the applications and services contained within those containers. For details, see [Monitor container groups](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring").

## Root-cause analysis

A key feature of OneAgent is the ability to continuously monitor every aspect of your applications, services, and infrastructure and to automatically learn the baseline performance metrics related to these components. Dynatrace also automatically learns the baseline response times and failure rates of all requests that are vital to the success of your business. Based on these baseline values, Dynatrace determines when a detected slowdown or error-rate increase justifies the generation of a new problem event. For details, see [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.").

For a complete list of the technologies that can be monitored by OneAgent, please see [OneAgent capabilities](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

---

## platform/oneagent.md

---
title: OneAgent
source: https://www.dynatrace.com/docs/platform/oneagent
scraped: 2026-02-27T21:09:30.145118
---

# OneAgent

# OneAgent

* Latest Dynatrace
* 1-min read
* Published Mar 29, 2019

[### Capabilities

Find out the monitoring capabilities offered by OneAgent offers.](/docs/platform/oneagent/supported-monitoring-types "Read an overview of all monitoring capabilities offered by OneAgent.")[### How it works

Understand how OneAgent works.](/docs/platform/oneagent/how-one-agent-works "Understand how OneAgent works.")

[### OneAgent monitoring modes

Find out about the available monitoring modes when using OneAgent.](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")[### Enable monitoring modes

Learn how to enable monitoring modes when using OneAgent.](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes "Learn how to enable monitoring modes when using OneAgent.")

## Deploy OneAgent

Cloud platforms

Kubernetes

Other container platforms

Servers

[![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS")AWS](/docs/ingest-from/amazon-web-services) [![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure")Azure](/docs/ingest-from/microsoft-azure-services) [![Google Cloud](https://dt-cdn.net/images/gcp-512-db85a455ae.webp "Google Cloud")Google Cloud](/docs/ingest-from/google-cloud-platform)

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")Kubernetes](/docs/ingest-from/setup-on-k8s)

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry) [![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")Docker](/docs/ingest-from/setup-on-container-platforms/docker) [![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")Mesos](/docs/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon)

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

---
