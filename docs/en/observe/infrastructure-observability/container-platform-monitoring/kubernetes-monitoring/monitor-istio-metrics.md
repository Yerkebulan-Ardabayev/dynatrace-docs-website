---
title: Istio/Envoy proxy metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics
scraped: 2026-03-06T21:21:54.871292
---

# Istio/Envoy proxy metrics

# Istio/Envoy proxy metrics

* Classic
* 1-min read
* Updated on May 08, 2023

Dynatrace version 1.255+

Istio is a platform-independent service mesh that is very popular in the Kubernetes community. Dynatrace OneAgent and ActiveGate can monitor Istio with the following observability options:

* Distributed tracing and service-level metrics: OneAgent with [code modules](../../../../ingest-from/technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* Istio metrics and topology: ActiveGate
* Istio logs: OneAgent [log module](../../../../analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa.md "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")

Alternatively, [Unified services](../../../application-observability/services/service-detection/service-detection-v1/service-types/unified-service.md "Define services on observability signals ingested via Trace ingest APIs.") provide agentless support for Istio service meshes.

## How it works

ActiveGate ingests Istio metrics and sends them to Dynatrace. Because Istio exposes metrics as Prometheus exporters, you just need to [provide annotations](monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

Based on the labels of ingested metrics, Dynatrace also detects the Istio topology without OneAgent. This is supported with ActiveGate version 1.261+.

See [Istio Service Meshï»¿](https://www.dynatrace.com/hub/detail/istio-and-envoy-service-mesh-prometheus/) in Dynatrace Hub for details on activating the Istio extension in your environment. The recommended version is 1.1.0 or later.

## Prerequisites

### ActiveGate

* See [Prometheus metrics](monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.") for ingestion prerequisites
* Topology detection: ActiveGate version 1.261+
* Sum and count extraction from histogram metrics: ActiveGate version 1.261+

### Dynatrace

* Istio metrics card on Kubernetes services, workload, and namespace pages: Dynatrace version 1.255+
* Topology (calling and called corresponding entities) on Kubernetes services, workload, and namespace pages: Dynatrace version 1.263+

Istio monitoring by OneAgent is supported for the classic full-stack, cloud-native full-stack, and application-only [deployment options](../../../../ingest-from/setup-on-k8s/how-it-works.md "In-depth description on how the deployment on Kubernetes works.") since Operator version 0.11.0+. Earlier versions support classic full-stack only.

## Related topics

* [Monitor Prometheus metrics](monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")