---
title: Networks
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/networks
scraped: 2026-02-22T21:12:33.509962
---

# Networks

# Networks

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Network devices** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides insights into networking components and their availability, with analytics powered by [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence."). Dynatrace offers flexible network device observability, allowing you to choose the level of monitoring and onboarding process that fits your needs.

## Overview

The  **Network devices** view provides different perspectives for viewing your network devices (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Network device**: The name or identifier of the network device. Select the name for a comprehensive, full-page view with detailed metadata and metrics.
* **Network area**: The logical grouping of network devices. Network areas are configured in the [SNMP Autodiscovery extension](/docs/observe/infrastructure-observability/extensions/snmp-autodiscovery "Scan through your subnets and build an inventory of SNMP-enabled network devices.").
* **Problems**: Lists any problems detected by Dynatrace Intelligence causal AI. Select a problem to access affected entities and investigate specific issues.
* **Reachability**: Indicates whether the device is reachable and responsive over the network.
* **Uptime**: The duration the device has been operational since the last restart.
* **Interface status**: The availability status of network interfaces.
* **Saturated interfaces**: Interfaces experiencing high utilization or congestion.

## Use cases

* Monitor device health

  Monitor health status, interface availability, network utilization, and hardware metrics such as CPU and memory usage.
* Identify and resolve issues

  View all problems detected by Dynatrace Intelligence causal AI and access affected entities to investigate and resolve specific issues.
* Filter and analyze devices

  Sort and filter network devices by name, type, problems, IP address, uptime, interface status, saturated interfaces, traffic volume, and reachability.