---
title: OTel Collector for ingesting telemetry into Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector
---

# OTel Collector for ingesting telemetry into Dynatrace

# OTel Collector for ingesting telemetry into Dynatrace

* Overview
* 5-min read
* Updated on Apr 28, 2026

The OTel Collector (or just "Collector") is a network service application that you can use to batch and transform telemetry data. It acts as a proxy and can receive OTLP requests as well as data from other sources, transform these requests according to defined rules, and forward them to the backend.

The following diagram shows different components that the Collector can use to receive, process, and export telemetry data to Dynatrace.

![The OTel Collector can receive, process, and export telemetry data to Dynatrace](https://cdn.bfldr.com/B686QPH3/as/5b86f3jgqb7frz6rtb85hjc/OpenTelemetry_-_Dynatrace_Collector_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector pipeline

## Advantages of using the Collector

In general, using the Collector alongside your service can be an advantage, since it allows your service to offload data quickly and takes care of additional handling such as retries, batching, encryption, or sensitive data filtering. It centralizes common processing tasks instead of duplicating them in each application.

You should use the Collector if:

* You need to collect data from different data sources in different formats and you need an easy way to make them all deliver their data to a backend that would otherwise be incompatible.
* You need to have common processing of attributes on your telemetry data.

The Collector is a relatively lightweight component, so teams can deploy their own to avoid sharing the same configuration.

The Collector is configured in a single YAML file. This eliminates the need to browse through multiple files and reduces maintenance. You can find more information on the configuration at [Configure the OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Distributions

The Collector comes in different distribution flavors and with different setup and deployment options.

| Type | When should I use it? |
| --- | --- |
| Dynatrace OTel Collector Recommended | The preferred choice for most use cases. It ships with a set of verified and stable Collector components, typically used with Dynatrace setups. |
| Core | When you primarily want to convert between OTLP protocols (such as converting between HTTP and gRPC, see [Transform OTLP gRPC to HTTP with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")), enforce memory usage constraints, or apply request batching. |
| Contrib | Ideal for test setups, as it contains all third-party components and doesn't require a custom build. It's generally not recommended for production systems, as it typically consumes more resources and may be less stable than an optimized Builder instance. |
| Collector Builder | When you need to fully customize the Collector instance and only run the components required for your use case. |

### Dynatrace OTel Collector

The Dynatrace distribution of the OpenTelemetry (OTel) Collector is a customized Collector build provided by Dynatrace. It is tailored for typical use cases in a Dynatrace context, and ships with an optimized and verified set of Collector components.

#### Dynatrace OTel Collector advantages

The Dynatrace OTel Collector offers the following advantages compared to other Collector distributions.

* Covered by Dynatrace support, see [Dynatrace OTel Collector support](#support).
* Collector components verified by Dynatrace.
* Security patches independent of OTel Collector releases.

The Dynatrace OTel Collector preserves the standard configuration model and component semantics.
By avoiding proprietary abstractions or hidden defaults, it enables both humans and AI agents to reliably reuse standard OpenTelemetry references and examples with fewer errors.

#### Dynatrace OTel Collector support

The x86‑64 and ARM64 builds of the Dynatrace OTel Collector distribution are supported by the Dynatrace Support team, in accordance with the [Dynatrace support policy﻿](https://support.dynatrace.com/).

For full support coverage, contact Dynatrace through the official support channels.
Issues reported via GitHub are handled on a best‑effort basis; support contracts and SLAs don't apply.

Each minor version is supported for three months.
Fixes are provided either as a patch release for the latest supported minor version or as part of a subsequent minor version release.

#### Dynatrace OTel Collector components

For the full list of provided components, see [Components﻿](https://github.com/Dynatrace/dynatrace-otel-collector#components).

#### Dynatrace OTel Collector use cases

For concrete use-case and configuration examples for the individual components, see [OTel Collector use cases](/managed/ingest-from/opentelemetry/collector/use-cases "Configure your OpenTelemetry Collector instance for different use cases.").

#### Deploy the Dynatrace OTel Collector

To deploy the Dynatrace OTel Collector, follow the steps as described in [Deploy the Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.").

The Dynatrace OTel Collector ships with specific components, which are described in the [Dynatrace OTel Collector's GitHub repo﻿](https://github.com/Dynatrace/dynatrace-otel-collector/).

### OpenTelemetry distributions

Dynatrace provides limited support for Core, Contrib, and Builder setups.
This support covers only the components and their versions that are included in the Dynatrace OTel Collector.

For a fully supported Collector distribution, see [Dynatrace OTel Collector](#dt-collector-dist).

#### Collector Core

The [Core distribution﻿](https://github.com/open-telemetry/opentelemetry-collector) contains the basic proxy service and a few fundamental service components.
This includes:

* A receiver for OpenTelemetry protocol (OTLP) data over HTTP and gRPC.
* Processors for batching requests and ensuring memory usage constraints.
* Exporters for console logging and OTLP over HTTP and gRPC.

#### Collector Contrib

The [Contrib distribution﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib) builds on top of Core and enhances its functionality by shipping with a large number of additional receivers, processors, and exporters, contributed by third parties.

Given that the Contrib distribution is an all-in-one package and comes with all service components pre-compiled, it may use more system resources (storage and memory) than an optimized Collector build.

Dynatrace recommends using the Contrib distribution only for testing purposes.
It shouldn't be used for production environments.

#### Collector Builder

In addition to the two distributions, OpenTelemetry also offers the [OpenTelemetry Collector Builder (OCB)﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/cmd/builder), a command line tool that allows you to build your own customized version of the Collector.

## Components

### Receiver

A receiver is a component that allows data to come into the Collector. It can receive data from multiple sources. Many receivers come with default settings and don't need much configuration.

For a list of available receivers and their basic configuration, see the official [OpenTelemetry documentation on receivers﻿](https://opentelemetry.io/docs/collector/configuration/#receivers).

### Processor Optional

A processor is an optional component that transforms, filters, or enriches data before export.

For a list of available processors and their basic configuration, see the official [OpenTelemetry documentation on processors﻿](https://opentelemetry.io/docs/collector/configuration/#processors). OpenTelemetry has a list of [recommended processors﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/processor#recommended-processors), but these are optional.

### Exporter

An exporter is a component that sends processed data to one or more backends. Exporters can support more than one data source.

Because many exporters require additional configuration (for example, an endpoint), be sure to check the official [OpenTelemetry documentation on exporters﻿](https://opentelemetry.io/docs/collector/configuration/#exporters) for a list of available exporters and their configurations.

### Services

Services define pipelines that channel data through the Collector. They define which components work together to process OpenTelemetry data.