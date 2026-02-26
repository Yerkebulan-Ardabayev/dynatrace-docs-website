---
title: OneAgent monitoring modes
source: https://www.dynatrace.com/docs/platform/oneagent/monitoring-modes/monitoring-modes
scraped: 2026-02-26T21:14:28.804501
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