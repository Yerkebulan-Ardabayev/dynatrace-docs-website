---
title: Unified services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service
scraped: 2026-05-12T12:02:24.401298
---

# Unified services

# Unified services

* How-to guide
* 6-min read
* Updated on Oct 13, 2025

Dynatrace version 1.274

## Overview

The **Unified service** type represents services detected using Service Detection v2 (SDv2) rules based on resource attributes.

Services using SDv2 detection show **Unified service** as their service type in the web UI properties, indicating that SDv2 detection rules are being applied.

Key capabilities:

* Response time, throughput, and failure rate metrics
* Automatic endpoint detection and monitoring

The term "unified services" was introduced before SDv2 existed. The underlying service, endpoint, failure, and splitting detection rules were introduced at the same time, but were hardcoded. SDv2 now makes these rules configurable. While properties still display **Unified service**, SDv2 focuses on detection rules rather than service types.

For current detection rules and customization options, see the [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

## Legacy span:service

Legacy **span:services** were automatically migrated to SDv2 (**Unified service**) by October 1, 2025.

This affects **span:services** (OTLP API ingested services) only, not **span (default) services** detected by OneAgent with the OpenTelemetry sensor, which will remain unchanged.

For details, see the [Service Detection V2 (SDv2) Overviewï»¿](https://dt-url.net/b4030ff) post in the Dynatrace Community.

## Manage endpoint monitoring

You can manage endpoint metrics, such as response time, throughput, and failure rate metrics, by configuring endpoint metric collection on the environment level and overrides on the service level.

Changes to endpoint metric-collection settings have billing implications.

Metrics Classic billing

The following table lists endpoint classic metrics; metrics that [consume DDUs](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") are billed. For OneAgent-based data, these metrics aren't written.

| Metric key | Name and description | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:service.request.count | Unified service request count Number of requests received by a given service. To learn how Dynatrace detects and analyzes services, see [Services](https://dt-url.net/am-services). | Count | autovalue | DDUs |
| builtin:service.request.failure\_count | Unified service failure count Number of failed requests received by a given service. To learn how Dynatrace detects and analyzes services, see [Services](https://dt-url.net/am-services). | Count | autovalue | Host units |
| builtin:service.request.response\_time | Unified service request response time Response time of a service measured in microseconds on the server side (server side measurements do not include e.g. proxy and networking times). Response time is the time until a response is sent to a calling application, process or other service. It does not include further asynchronous processing. To learn how Dynatrace calculates service timings, see [Service analysis timings](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile | DDUs |

To manage endpoint monitoring for all unified services in your environment

1. Go to **Settings**.
2. Select **Service Detection**.
3. Select **Unified services endpoint metrics** and turn on/off **Enable endpoint metrics**.

To override endpoint monitoring for a specific unified service

1. Go to **Services**.
2. Optional On the **Services** page, in the **Service type** column, select the **Unified service** checkbox.
3. Find and select the service for which you want to configure endpoint monitoring.
4. On the service overview page, select **More** (**â¦**) > **Settings**.
5. On the **Service settings** page, select **Endpoint metrics**.
6. On the **Unified services endpoint metrics** page, turn on/off **Enable endpoint metrics**.