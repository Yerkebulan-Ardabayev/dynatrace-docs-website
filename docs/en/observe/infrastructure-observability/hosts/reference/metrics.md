---
title: Host metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/reference/metrics
scraped: 2026-02-15T21:27:15.742618
---

# Host metrics

# Host metrics

* Reference
* 7-min read
* Published Nov 04, 2024

This is a reference list of the metrics used for hosts, with details of their availability on Windows, Linux, and AIX operating systems.

You can also check if the metrics are available in the Discovery monitoring mode. For more details, refer to [Discovery mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.").

## CPU and Memory metrics

Metrics representing the usage of CPU and RAM.

### CPU

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Idle | builtin:host.cpu.idle | dt.host.cpu.idle |  |  |  |  |
| User | builtin:host.cpu.user | dt.host.cpu.user |  |  |  |  |
| IO wait | builtin:host.cpu.iowait | dt.host.cpu.iowait |  |  |  |  |
| Other | builtin:host.cpu.other | dt.host.cpu.other |  |  |  |  |
| Steal | builtin:host.cpu.steal | dt.host.cpu.steal |  |  |  |  |
| System | builtin:host.cpu.system | dt.host.cpu.system |  |  |  |  |
| System Load | builtin:host.cpu.load | dt.host.cpu.load |  |  |  |  |
| System load 5 minutes | builtin:host.cpu.load5m | dt.host.cpu.load5m |  |  |  |  |
| System load 15 minutes | builtin:host.cpu.load15m | dt.host.cpu.load15m |  |  |  |  |
| CPU Usage % | builtin:host.cpu.usage | dt.host.cpu.usage |  |  |  |  |
| Logical / Physical CPU cores |  |  |  |  |  |  |
| entc | builtin:host.cpu.entc | dt.host.cpu.entc |  |  |  |  |
| physc | builtin:host.cpu.physc | dt.host.cpu.physc |  |  |  |  |
| entConfigured | builtin:host.cpu.entConfig | dt.host.cpu.ent\_config |  |  |  |  |
| AIX Kernel threads running | builtin:host.kernelThreads.running | dt.host.kernel\_threads.running |  |  |  |  |
| AIX Kernel threads blocked | builtin:host.kernelThreads.blocked | dt.host.kernel\_threads.blocked |  |  |  |  |
| AIX Kernel threads blocked I/O message wait | builtin:host.kernelThreads.ioMessageWait | dt.host.kernel\_threads.io\_message\_wait |  |  |  |  |
| AIX Kernel threads blocked I/O event wait | builtin:host.kernelThreads.ioEventWait | dt.host.kernel\_threads.io\_event\_wait |  |  |  |  |

### Memory

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Total | builtin:host.mem.total | Unsupported |  |  |  |  |
| Used | builtin:host.mem.used | dt.host.memory.used |  |  |  |  |
| Available | builtin:host.mem.avail.bytes | dt.host.memory.avail.bytes |  |  |  |  |
| Memory available % | builtin:host.mem.avail.pct | dt.host.memory.avail.percent |  |  |  |  |
| Memory used % | builtin:host.mem.usage | dt.host.memory.usage |  |  |  |  |
| Kernel | builtin:host.mem.kernel | dt.host.memory.kernel |  |  |  |  |
| memoryReclaimable | builtin:host.mem.recl | dt.host.memory.recl |  |  |  |  |
| Page Faults | builtin:host.mem.avail.pfps | dt.host.memory.avail.pfps |  |  |  |  |
| Swap Used | builtin:host.mem.swap.used | dt.host.memory.swap.used |  |  |  |  |
| Swap Total | builtin:host.mem.swap.total | dt.host.memory.swap.total |  |  |  |  |
| Swap Available | builtin:host.mem.swap.avail | dt.host.memory.swap.avail |  |  |  |  |

### File descriptors/handles

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| File descriptors used | builtin:host.handles.fileDescriptorsUsed | dt.host.handles.file\_descriptors\_used |  |  |  |  |
| File descriptors max | builtin:host.handles.fileDescriptorsMax | dt.host.handles.file\_descriptors\_max |  |  |  |  |

## Disk metrics

Metrics representing the disk usage. Note that there's a separation between network and local drives on Linux.

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Total[1](#fn-1-1-def) |  |  |  |  | [2](#fn-1-2-def) |  |
| Disk used | builtin:host.disk.used | dt.host.disk.used |  |  | [2](#fn-1-2-def) |  |
| Disk used % | builtin:host.disk.usedPct | dt.host.disk.used.percent |  |  | [2](#fn-1-2-def) |  |
| Disk available[1](#fn-1-1-def) | builtin:host.disk.avail | dt.host.disk.avail |  |  | [2](#fn-1-2-def) |  |
| Disk available %[1](#fn-1-1-def) | builtin:host.disk.free | dt.host.disk.free |  |  | [2](#fn-1-2-def) |  |
| Read (Bytes/s) | builtin:host.disk.bytesRead | dt.host.disk.bytes\_read | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Write (Bytes/s) | builtin:host.disk.bytesWritten | dt.host.disk.bytes\_written | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Inodes total | builtin:host.disk.inodesTotal | dt.host.disk.inodes\_total |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Inodes available % | builtin:host.disk.inodesAvail | dt.host.disk.inodes\_avail |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Reads (IOPS) | builtin:host.disk.readOps | dt.host.disk.read\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Writes (IOPS) | builtin:host.disk.writeOps | dt.host.disk.write\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Disk read time | builtin:host.disk.readTime | dt.host.disk.read\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk write time | builtin:host.disk.writeTime | dt.host.disk.write\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk utilization time | builtin:host.disk.utilTime | dt.host.disk.util\_time | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |
| Disk average queue length | builtin:host.disk.queueLength | dt.host.disk.queue\_length | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |

1

OneAgent version 1.313+ The disk available and disk total metrics are not sent when the total disk size exceeds 1024 petabytes (1024 PB).

2

Local only

3

Excluding GPFS

4

Since OneAgent 1.307

5

Excluding CIFS

6

GPFS only

7

Excluding CIFS/GPFS

8

Excluding NFS/CIFS/GPFS

## Network metrics per network interface controller (NIC)

Metrics representing the usage of network interface controllers on the host. They're collected by OneAgent network module.

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Bytes Received / s | builtin:host.net.nic.bytesRx | dt.host.net.nic.bytes\_rx |  |  |  |  |
| Bytes Sent / s | builtin:host.net.nic.bytesTx | dt.host.net.nic.bytes\_tx |  |  |  |  |
| Packets Received / s | builtin:host.net.nic.packets.rx | dt.host.net.nic.packets.rx |  |  |  |  |
| Packets Sent / s | builtin:host.net.nic.packets.tx | dt.host.net.nic.packets.tx |  |  |  |  |
| Dropped Packets Out / s | builtin:host.net.nic.packets.droppedTx | dt.host.net.nic.packets.dropped\_tx |  |  |  |  |
| Dropped Packets In / s | builtin:host.net.nic.packets.droppedRx | dt.host.net.nic.packets.dropped\_rx |  |  |  |  |
| Errors Out / s | builtin:host.net.nic.packets.errorsTx | dt.host.net.nic.packets.errors\_tx |  |  |  |  |
| Errors In / s | builtin:host.net.nic.packets.errorsRx | dt.host.net.nic.packets.errors\_rx |  |  |  |  |
| Send Utilization | builtin:host.net.nic.linkUtilTx | dt.host.net.nic.link\_util\_tx |  |  |  |  |
| Received Utilization | builtin:host.net.nic.linkUtilRx | dt.host.net.nic.link\_util\_rx |  |  |  |  |

## Availability

| Metric name | Metrics classic key | Metrics on Grail key | Windows | Linux | AIX | Discovery mode |
| --- | --- | --- | --- | --- | --- | --- |
| Host availability | builtin:host.availability.state | dt.host.availability |  |  |  |  |
| Host uptime | builtin:host.uptime | builtin:host.uptime |  |  |  |  |

## Other

| Metric name | Metrics classic key | Metrics on Grail key |
| --- | --- | --- |
| Host Time Offset | builtin:host.la.to | unsupported |