---
title: OpenTelemetry and Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry
---

# OpenTelemetry and Dynatrace

# OpenTelemetry and Dynatrace

* Overview
* 2-min read
* Updated on Oct 08, 2026

[OpenTelemetry (OTel)﻿](https://www.opentelemetry.io) provides a standardized way of collecting and exporting telemetry data.
It allows applications and infrastructure to transmit telemetry to backends (such as Dynatrace) using vendor-agnostic formats.
These backends can then aggregate and analyze the data.

You can implement this service by service, adopting the open standards of OpenTelemetry where openness matters most, while leveraging enhanced OneAgent features available where you need them.
Dynatrace supports this flexible approach, ensuring you experience industry-leading analytics regardless of how you mix your instrumentation choices.

## Ingest methods

There are two different ways you can export your OTLP data to Dynatrace.
Choose the deployment option that best aligns with your observability strategy.

![Dynatrace supports OTLP ingest via API or an OTel Collector](https://dt-cdn.net/images/opentelemetry-ingest-methods-light-mode-2-3840-ea266b8d61.png)

OTLP: Send data to Dynatrace

Send OTLP traces, metrics, and logs to Dynatrace directly from your applications over OTLP/HTTP, or route them through an OpenTelemetry Collector that exports to the Dynatrace OTLP API. For more information about OpenTelemetry Collectors, see [OTel Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.").

## Why use OpenTelemetry with Dynatrace?

Dynatrace provides end-to-end observability for all your application telemetry while embracing OpenTelemetry standards.
With its unified observability approach, Dynatrace offers a comprehensive platform for viewing, storing, and correlating all OpenTelemetry signals in one place.
This solution empowers you to simplify complexity and innovate faster by extracting maximum value from your data, regardless of origin.

Dynatrace provides you with:

* Powerful analytics at scale.
  Execute massive queries at lightning speed, turning telemetry data into actionable and intelligent insights for faster problem resolution.
* Intelligence beyond instrumentation.
  Dynatrace enriches OpenTelemetry data with business context and advanced analytics to deliver actionable intelligence, rather than just data collection.
* Accelerated innovation.
  Navigate OpenTelemetry data with out-of-the-box analysis, dynamic visualizations, and instant performance insights that foster collaboration between development and operations teams.
* Seamless integration.
  Enable easier integration of data into the Dynatrace Platform.

## How is Dynatrace involved with OpenTelemetry?

Dynatrace is deeply committed to the OpenTelemetry ecosystem through multiple avenues of involvement:

* Dynatrace is one of the top contributors to the OpenTelemetry project with key maintainer roles, helping shape its core functionality and direction.
* Dynatrace is actively involved through leadership positions on multiple OpenTelemetry special interest groups (SIGs) and on the OpenTelemetry Technical Committee.
  This helps to shape the future direction of OpenTelemetry standards and practices.
* Dynatrace supports over 30 open-source projects and contributes to multiple open-source offerings, reflecting its deep commitment to community-driven innovation.

## Multiple pathways to leverage your OpenTelemetry data

Dynatrace meets customers where they are in their observability journey, offering multiple ingestion options for getting OpenTelemetry signals into the platform including:

* OTLP API
* OTel Collector
* Dynatrace OTel Collector

## Licensing

Licensing for OpenTelemetry data is fully integrated into the Dynatrace Platform Subscription model, ensuring that all telemetry types (traces and spans, metrics, logs) are billed transparently and consistently.

## Related topics

* [Use OneAgent with OpenTelemetry data](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")