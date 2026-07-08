---
title: Networks
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/networks
---

# Networks

# Networks

* Explanation
* 2-min read
* Updated on Apr 19, 2022

Dynatrace infrastructure monitoring extends beyond hosts and processes to include network communication. It provides insight into how well processes communicate, access required resources, and use network bandwidth. This helps you detect issues that aren't caused by resource limits or slow response times, but by poor connectivity or misused network capacity. By monitoring data packets exchanged between processes and hosts, you gain deeper visibility into performance and reliability across your environment.

## Network monitoring overhead

Network monitoring in Dynatrace introduces minimal overhead, which varies depending on traffic volume. Dynatrace automatically tracks this overhead and applies throttling if it exceeds 5% of available CPU. When throttling is triggered, the network module pauses for just under 3 minutes. If the threshold is still exceeded after reactivation, the pause duration doubles each time, up to a maximum of 45 minutes, until resource usage returns to acceptable levels.

## Data privacy

* Dynatrace analyzes the network packets in memory in real time.
* Dynatrace doesn't store the packets on a drive, either on monitored hosts or in the Dynatrace cluster.
* Dynatrace analyzes packet headers only, not the payload.

[#### Monitor network communications

Learn the basics of Dynatrace network monitoring, including how to analyze network health and recognize common network issues.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/how-to-monitor-network-communication)[#### Detect network errors

Learn how errors such as dropped packets and retransmissions on the network level can affect the performance and connectivity of your services.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/detect-network-errors)[#### Extended network monitoring

Extend network monitoring with network traffic metrics in containerized Linux hosts using NetTracer.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/network-monitoring-with-nettracer)[#### Troubleshooting network monitoring

Learn more about troubleshooting network monitoring.

* Troubleshooting

Read this troubleshooting guide](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring)[#### Ingest NetFlow records into Dynatrace

Learn how to ingest NetFlow records into Dynatrace.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/ingest-netflow-records)

## Related topics

* [Network monitoring﻿](https://www.dynatrace.com/platform/network-monitoring/)