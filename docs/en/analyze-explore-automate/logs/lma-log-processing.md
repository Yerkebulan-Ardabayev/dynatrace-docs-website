---
title: Log processing
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing
scraped: 2026-02-16T21:21:32.533955
---

# Log processing

# Log processing

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Dec 11, 2025

Dynatrace can reshape incoming log data for better understanding, analysis, or further transformation.

Information can be logged in a very wide variety of formats depending on the application, process, operating system, or other factors. Log pre-processing and processing with OpenPipeline offers a central and flexible way of extracting value from those raw log lines.

![Diagram - Steps of log processing](https://dt-cdn.net/images/lma-log-processing-with-openpipeline-v2-2500-0a3f3308e5.png)

Log processing comprises the following steps.

### 1. Automatic log processing on ingest

Dynatrace processes logs upon ingestion to ensure that your log lines are ready for automation, troubleshooting, and analysis. This unified approach allows you to switch between different [log ingest strategies](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") with zero or minimum configuration.

Automatic log processing on ingest includes timestamp extraction, severity extraction, and log payload parsing.

For more details, see [Automatic log processing at ingestion](/docs/analyze-explore-automate/logs/lma-log-processing/lma-automatic-processing "Ingest and process logs automatically with OneAgent, Log Monitoring API v2, or Dynatrace OTLP API.").

### 2. Pre-processing with OpenPipeline

Dynatrace applies log pre-processing to enrich, normalize, and prepare log data for analysis. Thanks to this structured approach, logs from supported technologies are enriched without manual configuration, have better structure and metadata, and are connected with their traces.

Pre-processing with OpenPipeline ensures consistent log structure, improved queryability, and seamless integration with Dynatrace observability features.

For more information, see [Log pre-processing with OpenPipeline with ready-made bundles](/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing "Streamline log analysis by enriching and normalizing data using ready-made technology bundles for popular technologies before it enters OpenPipeline.").

### 3. Log processing with OpenPipeline

Log processing with OpenPipeline involves using the [OpenPipeline solution](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to handle logs before they are stored in Grail. This step includes different stages, such as processing, metric and data extraction, permissions, and storage. See [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.") for the detailed overview of all the stages.

We recommend utilizing log processing with OpenPipeline as a scalable, powerful solution to manage, process, and analyze logs. If you don't have access to OpenPipeline, use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Data flow in OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")