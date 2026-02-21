---
title: Hosts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/hosts
scraped: 2026-02-21T21:10:20.660403
---

# Hosts

# Hosts

* Latest Dynatrace
* Explanation
* 3-min read
* Published Nov 25, 2025

The  **Hosts** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides comprehensive monitoring of your infrastructure hosts across physical machines, virtual machines, and cloud instances. Use this tool to track host health, performance metrics, and resource utilization to ensure optimal infrastructure operation.

Full-stack infrastructure monitoring begins automatically as soon as Dynatrace OneAgent starts operation and begins capturing performance and event-related information on your hosts.

## Overview

Here's what each column in the  **Hosts** view stands for.

* **Host**: The host's unique name or identifier. Select the name for a comprehensive, full-page view with in-depth details.
* **Monitoring mode**: The OneAgent monitoring mode configured for the host (Full-Stack, Infrastructure, or Discovery).
* **Health status**: Current health state of the host based on detected anomalies and alerts.
* **Custom alerts**: Lists any active custom alerts associated with the host.
* **Resource usage**: Provides metrics on CPU, memory, disk, and network consumption.
* **Host groups**: The logical grouping assigned to organize hosts across data centers and applications.

## Use cases

* Identify critical issues

  Use the **Custom alerts** column and health status filters to quickly identify hosts with problems. Selecting the alert takes you directly to the investigation view.
* Monitor resource utilization

  Analyze and compare CPU, memory, disk, and network usage metrics across hosts to optimize resource allocation.
* Organize environments

  Use [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to configure hosts per group, roll out OneAgent versions selectively, and track service metrics differently depending on the platform they run on.
* Drill down into host details

  Select a host name to view detailed graphs, processes, logs, events, and connected services for troubleshooting.

## Host monitoring with OneAgent

[#### OneAgent monitoring modes

Find out more about the available monitoring modes when using OneAgent.

* Explanation

Read this explanation](/docs/platform/oneagent/monitoring-modes/monitoring-modes)[#### Enable OneAgent monitoring modes

Learn how to enable monitoring modes when using OneAgent.

* How-to guide

Read this guide](/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes)