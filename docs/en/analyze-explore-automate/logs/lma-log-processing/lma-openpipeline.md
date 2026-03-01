---
title: Log processing with OpenPipeline
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline
scraped: 2026-03-01T21:08:51.359202
---

# Log processing with OpenPipeline

# Log processing with OpenPipeline

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Oct 15, 2025

[OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") is the Dynatrace solution for processing data from various sources. It enables effortless data handling at any scale and format on the Dynatrace platform. Using OpenPipeline when processing logs in Dynatrace offers a powerful solution to manage, process, and analyze logs. This approach combines the traditional log processing capabilities with the advanced data handling features of OpenPipeline to get deeper insights into your log data.

We recommend utilizing log processing with OpenPipeline as a scalable, powerful solution to manage, process, and analyze logs. If you don't have access to OpenPipeline, use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").

## OpenPipeline advantages

OpenPipeline provides the following advantages:

* Contextual data transformation: OpenPipeline extracts data with context and transforms it into more efficient formats, for example, converting logs to business events.
* Unified processing language: [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") is used as a processing language, offering one syntax for all Dynatrace features and more advanced options for processing.
* Pipeline concepts: You can split log ingest traffic into different pipelines with dedicated processing, data and metric extraction, permissions, and storage.
* Additional processors: You can use additional processors, for example, to add or remove fields. For the complete list, see [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.").
* Enhanced data extraction: Extract business events from logs with more data extraction options.
* Increased limits: Benefit from increased default [limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics."), including content size up to 524,288 bytes, attribute size up to 2,500 bytes, and up to 250 log attributes.
* Improved performance and higher throughput.

## Stages of log processing

The stages of log processing with OpenPipeline are described below.

![logs-openpipeline](https://dt-cdn.net/images/logs-openpipeline-1566-74807e1b77.png)

Specific fields are excluded from matching and processing or restricted. To learn more, see [Limits specific to fields](/docs/platform/openpipeline/reference/limits#fields "Reference limits of Dynatrace OpenPipeline.").

1

The data remains in its original, structured form. This is important for detailed analysis and troubleshooting, as it ensures that no information is lost or altered.

2

Extracted metrics are sent to Grail only, except for the security events (new) and span configuration scopes.

Ingested logs are routed by the default route to built-in pipelines to ensure Grail storage. For log processing with OpenPipeline, the built-in pipeline is the **default** pipeline that ensures Grail storage. Create custom routes and pipelines to customize processing and storage in OpenPipeline. Processing is based on available records and doesn't take into account record enrichment from external services.

If you have created custom pipelines and your logs are routed to them by the dynamic route definition, these logs are not processed by the default pipeline. If logs aren't routed to custom pipelines, they are processed by the default pipeline.

## Enable technology bundles

OpenPipeline provides [technology bundles](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.") for common technologies and log formats. You can manually enable the required technology bundles.

To enable technology bundles in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs**.
2. Go to the **Pipelines** tab, and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Pipeline** to add a new pipeline.

   If you see **Classic pipeline** in the **Pipelines** tab, it means that you still use the [classic log processing pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation."). We recommend migrating all your log processing rules (that is, classic pipeline) to log processing with OpenPipeline by creating the required pipelines as described on this page.
3. Enter a name for your new pipeline.
4. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Processor** in the **Processing** tab, and choose **Technology bundle**.
5. Choose the required technology, and then select **Choose**.
6. Select **Run sample data** to test the configuration, and view the result.
7. Select **Save**.

To process logs, you need to enable dynamic routing. For details, see [Route data](/docs/platform/openpipeline/getting-started/how-to-routing "Learn how to route data to an OpenPipeline processing pipeline.").

## Add a custom pipeline

To create a custom pipeline in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs**.
2. Go to the **Pipelines** tab, and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Pipeline** to add a new pipeline.
3. Enter a name for your new pipeline.
4. Select one of the tabs representing stages of log processing: **Processing**, **Metric Extraction**, **Data extraction**, **Permission**, or **Storage**.
5. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Processor**, and choose from the available processors.
6. For each processor, specify the name and matching condition. Additional required fields vary based on the processor and are specified in the user interface.
7. If available, select **Run sample data** to test the configuration, and view the result.
8. Select **Save**.

You can review or edit any pipeline by selecting the record and making the necessary changes.

## Use cases

Check the following use cases to learn how to leverage log processing with OpenPipeline.

* [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")
* [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.")

## Related topics

* [OpenPipeline processing examples](/docs/platform/openpipeline/use-cases/processing-examples "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [Parse log lines and extract a metric](/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline "Configure OpenPipeline processing for log lines.")
* [DQL matcher in OpenPipeline](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.")