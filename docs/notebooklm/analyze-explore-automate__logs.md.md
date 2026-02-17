# Dynatrace Documentation: analyze-explore-automate/logs.md

Generated: 2026-02-17

Files combined: 1

---


## Source: logs.md


---
title: Log Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs
scraped: 2026-02-17T04:47:10.783872
---

# Log Analytics

# Log Analytics

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Jan 28, 2026

Log Management and Analytics powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") provides a unified approach to unlocking the value of log data in the Dynatrace platform.

Hassle-free management of your log data lets you [ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") petabytes of data without schemas, indexing, or rehydration. All of that data is usable at any time for any analytics task. Thanks to schema on-read and the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."), there's no need to decide what you want to query during data ingestion. Select the retention period for your data that suits your business and compliance needs, whether for debugging or audit purposes.

Put Dynatrace Log Management and Analytics into use:

* **Enhance unified observability**: Integrate logs with traces and metrics for comprehensive observability in Kubernetes and cloud. Use Grail, DQL, and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** for unified exploration and visualization with dashboards.
* **Accelerate problem resolution**: Utilize logs for detailed troubleshooting, leveraging Dynatrace Intelligence to pinpoint relevant logs and reduce mean time to repair. Perform instant queries with Grail and DQL for rapid issue resolution.
* **Close monitoring gaps**: Track metrics, health, performance, and business indicators from hybrid cloud and mainframe deployments. Automate log collection with OneAgent, parse and process logs at scale with OpenPipeline, and transform logs into metrics with Grail and DQL.

## Get started

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Quick start guide**

Take the first steps to onboard and explore your logs.](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql "Explore the Log Management and Analytics use case for real-time observability with logs.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Ingest logs**

Set up log collection to automatically bring logs from different sources.](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Set up buckets and permissions**

Configure storage and define retention and access controls.](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Configure processing in OpenPipeline**

Define how ingested logs are processed and stored.](/docs/analyze-explore-automate/logs/lma-log-processing "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** **app**

Learn how to leverage ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Alerting, Problems, and automations**

Create anomaly detection and alerts, as well as automate the detection process.](/docs/analyze-explore-automate/logs/alerting-on-logs "Create, or let Dynatrace create, alerts-based log data in Dynatrace log monitoring")

Log data can come from diverse sources, including Kubernetes, technology stacks, cloud services, hyperscalers, custom API integrations, or Dynatrace extensions. Dynatrace employs OneAgent and API as key methods for ingesting logs from these sources.

The ingested logs are channeled to Dynatrace OpenPipeline for processing, analysis, and storage.

![Dynatrace Platform Overview](https://dt-cdn.net/images/logs-overview-2678-9573941b3e.png)

The Grail data lakehouse serves as a single unified storage solution where log data is interconnected within a real-time model that reflects the topology and dependencies within a monitored environment.

You can analyze the ingested data in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, run queries in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to gather a comprehensive understanding of your log data, or use ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** for real-time visualization and monitoring.

## Consumption model

The consumption model for Log Management and Analytics is based on three dimensions of data usage (Ingest & Process, Retain, and Query). The unit of measure for consumed data volume is gibibytes (GiB). In addition, **Retain with Included queries** is an available option combining the dimensions of Query and Retention. For details, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

## Availability and previous versions

Log Management and Analytics is the latest log offering available in Dynatrace SaaS with Grail.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Make smarter, faster decisions when troubleshooting and measuring the health of your environments: automatically unify logs, traces, and metrics of events in real time, monitor Kubernetes, optimize storage costs by extracting metrics from logs at ingest or read time, and resolve incidents faster.](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [Upgrade to Log Management and Analytics](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.")
* [Log Management and Analytics use cases](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.")
* [Log on Grail examples](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")


---
