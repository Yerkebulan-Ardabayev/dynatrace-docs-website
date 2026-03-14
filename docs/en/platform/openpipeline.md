---
title: OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline
scraped: 2026-03-06T21:10:24.659240
---

# OpenPipeline


* Latest Dynatrace
* Overview
* 1-min read
* Updated on Dec 19, 2025

Dynatrace version 1.295+

OpenPipeline is the Dynatrace data handling solution to seamlessly ingest and process data from different sources, at any scale, and in any format in the Dynatrace Platform.

## Use cases

* Configure ingestion and processing of different configuration scopes, such as logs and events, via a unified solution.
* Scale data management across teams by controlling access and targeted technologies.
* Ensure secure and compliant sensitive data handling.
* Enrich and contextualize data via customizable data processing.
* Optimize data quality and cost control.

## Concepts

[### Data flow

Learn how data flows from ingestion to storage via Dynatrace OpenPipeline.](openpipeline/concepts/data-flow.md "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")[### Processing

Learn the core concepts of Dynatrace OpenPipeline processing.](openpipeline/concepts/processing.md "Learn the core concepts of Dynatrace OpenPipeline processing.")

## Getting started

[### How to ingest data (events)

How to ingest data for a configuration scope in OpenPipeline.](openpipeline/getting-started/how-to-ingestion.md "How to ingest data for a configuration scope in OpenPipeline.")[### Configure processing

Configure ingest sources, routes, and processing for your data via OpenPipeline.](openpipeline/getting-started/tutorial-configure-processing.md "Configure ingest sources, routes, and processing for your data in OpenPipeline.")

### Processing examples

* [Reduce span-based and metric-based cardinality](openpipeline/use-cases/reduce-span-metric-cardinality.md "Leverage three different views in the Services app to normalize span and metric data, ensuring aggregations and analysis remain reliable and usable.")
* [OpenPipeline processing examples](openpipeline/use-cases/processing-examples.md "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [Parse log lines and extract a metric](openpipeline/use-cases/tutorial-log-processing-pipeline.md "Configure OpenPipeline processing for log lines.")
* [Extract metrics from spans and distributed traces](openpipeline/use-cases/tutorial-extract-metrics-from-spans.md "Extract metrics directly from your spans and distributed traces via OpenPipeline.")
* [Process logs with technology bundle parsers](openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.")
* [Extract a metric to track system events](openpipeline/use-cases/tutorial-system-events.md "Learn how to extract a metric to track system events with OpenPipeline.")
* [Configure multi-cloud ingest governance with pipeline groups](openpipeline/use-cases/pipeline-groups-multicloud.md "Configure pipeline groups via the Settings API to ensure consistent governance across multiâcloud deployments, restrict sensitive stages, and structure team responsibilities through mandatory and restricted pipelines.")
* [Extract a metric from user events](../observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-events.md "Turn user events into actionable insights by extracting custom metrics for long-term analysis.")
* [Extract a metric from user sessions](../observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-sessions.md "Discover how to build custom metrics from user sessions, illustrated by a customer conversion metric.")

## Reference

[### Ingest API

Reference material on ingestion APIs for the configuration scopes supported by OpenPipeline.](openpipeline/reference/api-ingestion-reference.md "Reference ingest sources and APIs for the configuration scopes supported in OpenPipeline.")[### OpenPipeline API

Reference material for configurations via OpenPipeline API.](openpipeline/reference/openpipeline-api.md "Configure OpenPipeline capabilities of ingest source, routing, and processing via API.")[### Limits

Reference material on OpenPipeline limits.](openpipeline/reference/limits.md "Reference limits of Dynatrace OpenPipeline.")