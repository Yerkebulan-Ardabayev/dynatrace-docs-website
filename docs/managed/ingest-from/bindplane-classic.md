---
title: Bindplane in Dynatrace (Dynatrace Classic)
source: https://docs.dynatrace.com/managed/ingest-from/bindplane-classic
---

# Bindplane in Dynatrace (Dynatrace Classic)

# Bindplane in Dynatrace (Dynatrace Classic)

* Explanation
* Published Sep 30, 2026

Bindplane is a telemetry pipeline management solution for centralizing collection, transformation, and routing of metrics, logs, and traces into Dynatrace and other destinations.

## Key terms

Dynatrace Bindplane OTel Collector
:   A collector that receives telemetry, applies processing, and forwards the result to one or more destinations.

Bindplane Control Plane
:   The management service that stores, deploys, and rolls out collector configurations, and reports on fleet health and throughput.

Fleet
:   A group of collectors to which a configuration is assigned. Collectors in the fleet inherit the configuration assigned to the fleet.

Open Agent Management Protocol (OpAMP)
:   The open protocol Bindplane uses to remotely manage, configure, and monitor collectors from the control plane, without SSH or manual restarts.

Edge ingest point
:   The collector's receive boundary. At this point data enters a collector, before any processing, enrichment, or transformation is applied.

## Overview

Bindplane is a unified telemetry pipeline to manage OpenTelemetry Collector fleets centrally and process telemetry at the edge by filtering, masking, enriching, and aggregating data.

Bindplane uses the Dynatrace Bindplane OTel Collector by default, or you can bring your own OpAMP-compatible OTel Collector. The **Bindplane Control Plane** configures and monitors the fleet via OpAMP, without requiring per-host access to configure individual Collectors. [Pipeline Intelligence﻿](https://docs.bindplane.com/feature-guides/pipeline-intelligence/pipeline-intelligence) is a suite of AI-powered features that help you understand your telemetry and automate your pipeline configuration.

Data from sources enters the pipeline at the edge ingest point, then it's transformed by processors, and sent to a destination.

* [Sources﻿](https://docs.bindplane.com/integrations/sources)—The origin of the telemetry, including hosts, containers, cloud services, custom log files, and any other OpenTelemetry-compatible source.
* [Processors﻿](https://docs.bindplane.com/integrations/processors)—Where transformations are applied, for example, filtering by field value, masking sensitive content, reducing volume, or enriching records with tags and attributes.
* [Destinations﻿](https://docs.bindplane.com/integrations/destinations)—Where processed telemetry is sent. Collectors can send data to multiple backends simultaneously, including Dynatrace and Splunk.

### Deployment models

Bindplane is available in two deployment models:

* **Cloud**—Cloud-hosted in Bindplane, available by region.
* **Self-hosted**—Hosted on a virtual machine (Linux), Docker, or Kubernetes.

To learn more, see [Deployment﻿](https://docs.bindplane.com/deployment).

## Use cases

* Manage large-scale fleets of OpenTelemetry collectors—Deploy, configure, and update thousands of OTel Collectors centrally from the **Bindplane Control Plane**.
* Process data and control the telemetry volume before ingestion—Mask sensitive fields, filter out low-value signals, convert high-volume log streams into summary metrics before data reaches Dynatrace, and reduce what you ingest.
* Manage multiple destinations—Send telemetry data to Dynatrace and other backends simultaneously, or send different telemetry to different destinations.
* Expand your range of telemetry sources—Send legacy syslog, third-party log files, and non-instrumented infrastructure via Bindplane into Dynatrace.

## Next

Get started by installing the Dynatrace Bindplane OTel Collector and adding Dynatrace as a Bindplane destination.

[Get started with Bindplane (Dynatrace Classic)](/managed/ingest-from/bindplane-classic/getting-started-classic "Connect your Dynatrace account to Bindplane, install the collector, configure the Enrichment Processor, and verify telemetry flows into Dynatrace.")

## Related

* [Bindplane documentation﻿](https://docs.bindplane.com)
* [OpenTelemetry in Dynatrace](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")