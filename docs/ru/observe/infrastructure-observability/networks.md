---
title: Networks
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks
scraped: 2026-02-06T16:29:04.150090
---

# Networks

# Networks

* Overview
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

Read this guide](/docs/observe/infrastructure-observability/networks/how-to-monitor-network-communication)[#### Detect network errors

Learn how errors such as dropped packets and retransmissions on the network level can affect the performance and connectivity of your services.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/detect-network-errors)[#### Extended network monitoring

Extend network monitoring with network traffic metrics in containerized Linux hosts using NetTracer.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/network-monitoring-with-nettracer)[#### Troubleshooting network monitoring

Learn more about troubleshooting network monitoring.

* Troubleshooting

Read this troubleshooting guide](/docs/observe/infrastructure-observability/networks/troubleshoot-network-monitoring)[#### Ingest NetFlow records into Dynatrace

Learn how to ingest NetFlow records into Dynatrace.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/networks/ingest-netflow-records)

## Related topics

* [Network monitoringï»¿](https://www.dynatrace.com/platform/network-monitoring/)