---
title: Extended network monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer
scraped: 2026-02-21T21:09:12.539556
---

# Extended network monitoring

# Extended network monitoring

* How-to guide
* 5-min read
* Updated on Oct 03, 2025

Extend network monitoring with network traffic metrics in containerized Linux hosts.

With network metrics added to your containerized hosts, DavisÂ® root cause analysis will leverage them and extend analysis to provide visibility into network-related issues. Extensive network traffic on particular nodes is a sign that you should consider scaling up the cluster.

## NetTracer

NetTracer is an open source tool for tracing TCP events and collecting network connection metrics on Linux. It consists of two parts:

* BPF program used for collecting data
* Binary that presents the data in a structured or semi-structured format

Advantages:

* It can trace TCP events: **connect**, **accept**, and **close**
* It can collect metrics about each traced connection
* It's a high performance applicaton (written in C and C++)
* It's independent from kernel version and configuration (Linux kernel 4.15 and higher)
* It's an open source project ([NetTracerï»¿](https://github.com/dynatrace-oss/nettracer-bpf))

NetTracer defines an IPv4 and IPv6 TCP connection by source address and port, destination address and port, PID of the communicating process, and network namespace.

Using this TCP connection definition, it collects the following metrics:

* Bytes sent
* Bytes received
* Packets sent
* Packets received
* Packets retransmitted
* Round-Trip Time (in microseconds)
* Round-Trip Time variance (not used in Dynatrace analysis)

By default, NetTracer is included as the binary `oneagentnettracer` with every OneAgent installation, and it can be enabled via the Dynatrace web UI.

## NetTracer supported platforms

NetTracer officially supports Linux kernel versions 4.15 and higher, but other Dynatrace components that coexist with NetTracer on a particular host have specific requirements and are supported on particular Linux distributions. The following table lists the tested and safest Linux distributions to use when planning to use NetTracer with Dynatrace.

Distribution

Architecture

Release

RedHat Enterprise Linux

x86\_64

8.0 and higher

CentOS

x86\_64

8.0 and higher

Ubuntu

x86\_64

18.04 LTS and higher

## Enable NetTracer

When enabled, OneAgent will use NetTracer to collect network data from containers, but only for Linux hosts.

To enable NetTracer on a specific Linux host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your Linux host.
2. On the host overview page, select **More** (**â¦**) > **Settings** in the upper-right corner of the page.
3. On the **Host settings** page, select **NetTracer traffic** and turn on **Enable NetTracer traffic network monitoring**.

To enable NetTracer globally on all your Linux hosts

1. Go to **Settings** > **Network & Discovery** > **NetTracer traffic**.
2. Turn on **Enable NetTracer traffic network monitoring**.

To ensure NetTracer works correctly, OneAgent must be installed in either Full-Stack or Infrastructure monitoring mode, as these modes enable the network monitoring feature. If OneAgent is installed in a limited mode (for example, Discovery monitoring mode), NetTracer may not function as intended. For more details, see [OneAgent monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

## Built-in metrics for NetTracer

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.nettracer.bytes\_rx | Bytes received Number of bytes received | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.bytes\_tx | Bytes transmitted Number of bytes transmitted | Byte | autoavgcountmaxminsum |
| builtin:tech.nettracer.pkts\_retr | Retransmitted packets Number of retransmitted packets | Count | autovalue |
| builtin:tech.nettracer.pkts\_rx | Packets received Number of packets received | Count | autovalue |
| builtin:tech.nettracer.pkts\_tx | Packets transmitted Number of packets transmitted | Count | autovalue |
| builtin:tech.nettracer.retr\_percentage | Retransmission Percentage of retransmitted packets | Percent (%) | autoavgmaxmin |
| builtin:tech.nettracer.rtt | Round trip time Round trip time in milliseconds. Aggregates data from active sessions | Millisecond | autoavgcountmaxminsum |
| builtin:tech.nettracer.traffic | Network traffic Summary of incoming and outgoing network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_rx | Incoming traffic Incoming network traffic in bits per second | bit/s | autovalue |
| builtin:tech.nettracer.traffic\_tx | Outgoing traffic Outgoing network traffic in bits per second | bit/s | autovalue |

### Calculated metrics for NetTracer

The following metrics available for NetTracer are calculated:

* `builtin:tech.nettracer.retr_percentage` (Retransmission)

  Retransmission = retransmitted packets / (retransmitted packets + packets transmitted) Ã 100
* `builtin:tech.nettracer.traffic_rx` (Incoming traffic)

  Incoming traffic = (sum of bytes received \* 8) per second
* `builtin:tech.nettracer.traffic_tx` (Outgoing traffic)

  Outgoing traffic = (sum of bytes transmitted:sum \* 8) per second
* `builtin:tech.nettracer.traffic` (Network traffic)

  Network traffic = ((sum of bytes received + sum of bytes transmitted) \* 8) per second

## Dimensions for NetTracer

Metric key

Dimension

Value

Unit

`builtin:tech.nettracer.bytes_rx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge, where:

sum = number of bytes from all sessions in the given timeframe

avg/min/max = average/minimal/maximal bytes per session in the given timeframe

count = number of sessions in the given timeframe

Bytes

`builtin:tech.nettracer.bytes_tx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge, where:

sum = number of bytes from all sessions in the given timeframe

avg/min/max = average/minimal/maximal bytes per session in the given timeframe

count = number of sessions in the given timeframe

Bytes

`builtin:tech.nettracer.pkts_rx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.pkts_tx`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.pkts_retr`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Count, sending deltas/resetting counter

Count

`builtin:tech.nettracer.rtt`

`dt.entity.process_group_instance`  
`dt.entity.process_group`  
`dt.entity.host`

Gauge

Miliseconds

### Container dimensions for NetTracer

If the process is running in a container, the following dimensions are added:

* `dt.entity.container_group_instance`
* `dt.entity.container_group`

Additional container dimensions are added depending on the deployment type.

Kubernetes

Docker (no Kubernetes)

`container.image.name` (if it's available)  
`k8s.container.name`  
`k8s.namespace.name`  
`k8s.pod.name`  
`k8s.pod.uid`

`container.image.name`  
`container.name`

## Where can I see NetTracer data?

After it's collected, NetTracer data is available as metrics throughout Dynatrace.

* **Data Explorer**: You can use the metrics in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to create charts and dashboards that display data that interests you.
* **Process group instance page**: Go to process group instance page and select **Networking** tab.

  ![Process group instance page - Networking details](https://dt-cdn.net/images/pgi-page-networking-details-2172-bcb6d64191.png)
* **Host overview**: Go to host overview page and scroll down to the **Network analysis** section.

  ![Network analysis](https://dt-cdn.net/images/lde68092-dev-apps-dynatracelabs-com-ui-apps-dynatrace-classic-hosts-ui-entity-host-b8ec70b7dc022ec8-gtf-2h-gf-all-sessionid-4aquod8c7d1hqbf8-2-2913-bca5600276.png)

**Networking** and **Network analysis** sections contain NetTracer data combined with other network data analysed for this host. NetTracer gathers data for containerized processes, meanwhile Network Agent for native (i.e., non-containerized) processes.

## NetTracer characteristics

* Only 4096 TCP connections are tracked from the NetTracer `ebpf` module.
* Information about listen ports requires an active TCP connection.