---
title: Business event processing
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing
scraped: 2026-02-26T21:21:23.607886
---

# Business event processing

# Business event processing

* Latest Dynatrace
* Explanation
* 4-min read
* Published Dec 11, 2025

Business events that you ingest from various sources can be processed before analysis.

We recommend utilizing OpenPipeline as a scalable, powerful solution to manage and process business events. If you don't have access to OpenPipeline, use the classic pipeline.

## OpenPipeline

OpenPipeline is the Dynatrace Platform solution for managing and processing data from various sources. It enables effortless data handling at any scale and format on the Dynatrace platform. It provides the following benefits:

* Contextual data transformation: OpenPipeline extracts data with context and transforms it into more efficient formats.
* Unified processing language: [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") is used as a processing language, offering one syntax for all Dynatrace features and more advanced options for processing.
* Pipeline concepts: You can split business event ingest traffic into different pipelines with dedicated processing, data and metric extraction, permissions, and storage.
* Additional processors: You can use additional processors, for example, to add or remove fields.
* Enhanced data extraction: Extract business events from logs with more data extraction options.
* Improved performance and higher throughput.

To get started, see [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.").

## Classic pipeline

Business event processing via the classic pipeline is the legacy solution to process business events in Dynatrace.

Even though the classic business events processing pipeline is still available for some environments, we recommend switching to business event processing with OpenPipeline. Business event processing with the classic pipeline will be deprecated at some point in the future.

To learn more, see [Business event processing via classic pipeline](/docs/observe/business-observability/bo-event-processing/bo-processing-classic-pipeline "Process business event data in Dynatrace via the classic pipeline.").

### Classic pipeline and OpenPipeline

If you created processing rules via the classic pipeline, we recommend that you manually migrate them to OpenPipeline.

To migrate your business event processing rules to OpenPipeline

1. In OpenPipeline, [create new custom pipelines and routes](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
2. In the classic pipeline, delete your processing rules.

If you don't migrate your existing rules, it's still possible to use OpenPipeline in combination with the classic pipeline. The processing flow looks as follows:

1. In OpenPipeline, [create new custom pipelines and routes](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
2. Data is processed by [custom pipelines](/docs/platform/openpipeline/concepts/processing#types "Learn the core concepts of Dynatrace OpenPipeline processing.").
3. If data doesn't match any route, it's routed by the default route to the [classic pipeline](/docs/platform/openpipeline/concepts/processing#types "Learn the core concepts of Dynatrace OpenPipeline processing.").
4. Business events are processed as defined by the classic pipeline.

## Use cases

* Parse data to the ideal format for your use cases.
* Extract metrics.
* Specify retention periods.
* Assign security context.

## Related topics

* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [DQL matcher in OpenPipeline](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.")