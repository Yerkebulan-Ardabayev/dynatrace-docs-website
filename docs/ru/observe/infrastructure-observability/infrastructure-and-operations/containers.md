---
title: Containers
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/containers
scraped: 2026-02-27T21:14:38.758973
---

# Containers

# Containers

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 25, 2025

The  **Containers** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** provides a dedicated inventory for viewing, filtering, and inspecting containers independently or in relation to hosts and processes. Navigate between entities to see how they are interconnected.

This view supports containerized workloads orchestrated by ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** or running on a standalone host. Each container displays detailed information, including metadata, logs, events, and time-series charts for CPU, memory, and network traffic.

## Overview

The  **Containers** view provides different perspectives for viewing your containers (**Health**, **Utilization**, and **Metadata**).

The **Health** perspective includes the following default columns:

* **Container**: The container's unique name or identifier. Select the name for a comprehensive, full-page view with detailed metadata, logs, events, and time-series charts.
* **Container group name**: The group or deployment to which the container is assigned.
* **Custom alerts**: Lists any active custom alerts associated with the container.

Other perspectives provide additional columns, including **Containerization type** (the containerization technology in use) and **Container host name** (the host machine on which the container operates).

## Use cases

* View containers within a host

  Navigate from a host to see all containers running on it and the containerized workload distribution.
* Access detailed container information

  Select a container to access a full-page view with detailed metadata, logs, events, and time-series charts (for example, CPU, memory, network traffic) for deeper analysis and troubleshooting.
* Navigate between related entities

  Navigate between hosts, containers, and processes to see how they are interconnected and view the full infrastructure context.
* Group and filter containers

  Filter containers by container group, containerization type, and other metadata to organize and analyze containers based on operational or logical groupings.
* Identify critical issues

  Use the **Custom alerts** column and the **Critical alert** filter to quickly identify containers with problems. Select an alert to investigate it.
* Monitor resource usage

  Analyze and compare CPU and memory usage metrics across containers to optimize resource allocation.
* Drill down into container details

  Select a container name to view detailed graphs, processes, logs, and events for troubleshooting.
* Analyze trends

  Use the time selector and resource usage graphs to identify patterns or anomalies over time.