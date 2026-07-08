---
title: Scrape Prometheus metrics with the OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus
---

# Scrape Prometheus metrics with the OTel Collector

# Scrape Prometheus metrics with the OTel Collector

* How-to guide
* 1-min read
* Published Jun 23, 2026

The OTel Collector can scrape Prometheus endpoints and forward the resulting metrics to Dynatrace.
Choose one of two deployment modes based on your scaling and reliability needs.

[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

## Standard (recommended)

A metric ingestion architecture that auto-scales, provides redundancy, and handles high-volume Prometheus workloads on Kubernetes. Recommended for most production environments.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

## Simplified

A single Collector for a small and static set of endpoints that don't need auto-scaling or redundancy.](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads.")

## How to choose

| Criteria | Standard | Simplified |
| --- | --- | --- |
| Best for | Production environments | Small and static target sets, demos |
| Architecture | Target Allocator, scraper, and gateway pools | A single Collector |
| Auto-scaling | Yes, with Horizontal Pod Autoscalers | No |
| Redundancy | Yes | No |
| Target discovery | Automatic via `ServiceMonitor`, `PodMonitor`, and `ScrapeConfig` CRDs | Simple service discovery or static endpoint configuration |
| Platform | Kubernetes | Any |

## Scaling

If the simplified deployment runs out of headroom but you don't yet need the standard architecture, you can run multiple independent simplified Collectors, each scraping a distinct set of targets (for example, one per namespace or team).

* This keeps the same single-Collector configuration.
* You must partition targets yourself.
* There is no shared auto-scaling.

Because of this, we recommend the [standard setup](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.") (which scales automatically) for most use cases.

For general information about scaling the Collector, see [How to scale the OTel Collector](/managed/ingest-from/opentelemetry/collector/scaling "How to scale the OpenTelemetry Collector.").