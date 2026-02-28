---
title: Unified services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service
scraped: 2026-02-28T21:25:07.667740
---

# Unified services

# Unified services

* How-to guide
* 6-min read
* Updated on Oct 13, 2025

Dynatrace version 1.274

## Overview

The **Unified service** type represents services detected using Service Detection v2 (SDv2) rules based on resource attributes.
These services were first introduced for OpenTelemetry and are now being rolled out for OneAgent in public preview (fall 2025).

Services using SDv2 detection show **Unified service** as their service type in the web UI properties, indicating that SDv2 detection rules are being applied.

Key capabilities:

* Response time, throughput, and failure rate metrics
* Automatic endpoint detection and monitoring

The term "unified services" was introduced before SDv2 existed. The underlying service, endpoint, failure, and splitting detection rules were introduced at the same time, but were hardcoded. SDv2 now makes these rules configurable. While properties still display **Unified service**, SDv2 focuses on detection rules rather than service types.

The Grail metrics `dt.service.request.response_time`, `dt.service.request.failure_count`, and `dt.service.request.count` are billable. To learn more, see [Metrics powered by Grail (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

For current detection rules and customization options, see the [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

## Legacy span:service

Legacy **span:services** were automatically migrated to SDv2 (**Unified service**) by October 1, 2025.

This affects **span:services** (OTLP API ingested services) only, not **span (default) services** detected by OneAgent with the OpenTelemetry sensor, which will remain unchanged.

For details, see the [Service Detection V2 (SDv2) Overviewï»¿](https://dt-url.net/b4030ff) post in the Dynatrace Community.