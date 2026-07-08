---
title: Services
source: https://docs.dynatrace.com/managed/observe/application-observability/services
---

# Services

# Services

* Overview
* 4-min read
* Updated on Oct 23, 2025

Services are an application's fundamental building blocks. From an observability standpoint, they provide application owners with critical metrics to monitor application health. By tracking response time, throughput, and failure rates, owners can quickly identify anomalies detected by [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.").

Dynatrace offers both health monitoring and detailed analysis of services. You can investigate traces, logs, and hotspots while also using the [Smartscape® technology](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.") to understand relationships between services and their underlying infrastructure, such as hosts or Kubernetes nodes.

## Service monitoring

Dynatrace offers a comprehensive set of capabilities to address diverse observability use cases. These range from high-level monitoring dashboards to in-depth analysis tools supporting app owners and troubleshooting use cases. You can leverage different interfaces based on their specific needs, whether monitoring service health, analyzing performance issues, or investigating complex system behaviors.

[![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") Services Classic](/managed/observe/application-observability/services-classic "Learn about Dynatrace's classic service monitoring") includes analysis capabilities such as hotspot detection, service flow visualization, and code-level profiling.

## Service monitoring vs process monitoring

A service is a logical application component that performs specific business functions and handles end-user requests. A process is an executable program running on a host or container that consumes system resources.

Service monitoring focuses on application performance from an end-user perspective. It tracks the following:

* Transaction flows and response times.
* Service endpoints and their interactions.
* Application-level errors and dependencies.

Process monitoring focuses on infrastructure resource utilization. It measures the following:

* CPU, memory, and thread consumption.
* Operating system processes on machines or in containers.
* Process availability and resource bottlenecks.

In Dynatrace, processes are organized into process groups, while services represent the logical application components. This dual approach provides visibility into both infrastructure and application performance in a connected context.

[### Service detection and naming

Learn how services are detected and named in Dynatrace and how you can customize your monitoring via service detection and naming rules.](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")[### Analysis

Explore the service monitoring details that Dynatrace can provide.](/managed/observe/application-observability/services-classic "Learn about Dynatrace's classic service monitoring")[### Request attributes

Learn what request attributes are and how you can use them across all levels of service analysis.](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")[### Settings

Find out about monitoring tuning options for services.](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-settings "Learn about service monitoring tuning options in Dynatrace.")

## Related topics

* [Service flow](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Distributed Traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")