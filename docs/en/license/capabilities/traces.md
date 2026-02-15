---
title: Traces powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/traces
scraped: 2026-02-15T08:57:26.222116
---

# Traces powered by Grail overview (DPS)

# Traces powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 9-min read
* Updated on Jun 23, 2025

The Traces powered by Grail DPS capability gives customers access to:

* Distributed trace ingestion for OpenTelemetry via the OTLP API.
* Distributed trace ingestion for serverless functions.
* Extended trace ingestion for [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.") beyond the [included trace data volume](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-traces "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").
* Extended trace data retention for up to 10 years.
* Advanced tracing analytics in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, and via API.

This page describes the different tracing capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Traces - Ingest & Process](/docs/license/capabilities/traces/dps-traces-ingest "Learn how your consumption of the Traces - Ingest & Process DPS capability is billed and charged.")
* [Traces - Retain](/docs/license/capabilities/traces/dps-traces-retain "Learn how your consumption of the Traces - Retain DPS capability is billed and charged.")
* [Traces - Query](/docs/license/capabilities/traces/dps-traces-query "Learn how your consumption of the Traces - Query DPS capability is billed and charged.")

## Traces - Ingest feature overview

Ingest & Process replaces the platform extensions [Custom Traces Classic](/docs/license/capabilities/platform-extensions/custom-traces-classic "Learn how your consumption of the Dynatrace Custom Traces Classic DPS capability is billed and charged.") and [Serverless Functions Classic](/docs/license/capabilities/platform-extensions/serverless-functions-classic "Learn how your consumption of the Dynatrace Serverless Functions Classic DPS capability is billed and charged.").
They cannot be used simultaneously.

Ingest & Process usage occurs when:

| Concept | Explanation |
| --- | --- |
| Data ingest | Distributed trace data ingested from the following sources is charged as [Ingest & Process](#trace-ingest-usage):  - Via the OpenTelemetry [OTLP Trace Ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") from non-Full-Stack sources. - Via [serverless functions](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace"). - Extended trace ingest for [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") (if the customer [explicitly requests extended trace ingest](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#extend-trace-ingest "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")).  Enrichment of spans with additional metadata at the source, such as [Kubernetes metadata](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"), increase the size of ingested data that is charged as [Ingest & Process](#trace-ingest-usage). |
| Data processing via OpenPipeline | - Data processing via OpenPipeline is included in [Traces â Ingest & Process](#trace-ingest-usage). However, it increases the size of span data that is charged as [Traces â Retain](#trace-retain-usage). - Topology enrichment based on Dynatrace entities (`dt.entity.*` entity types) does not increase the billable span size or [Traces â Ingest & Process](#trace-ingest-usage) consumption. - Custom metrics are created from span data and are charged as [Metrics - Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged."). These are Grail metric keys and therefore are available only in latest Dynatrace. |

Dynatrace reserves the right to work with customers to adjust or disable parsing rules, processors, or pipelines that experience service degradation.

## Traces - Retain feature overview

Retain usage occurs when:

| Concept | Explanation |
| --- | --- |
| Data availability | Retained data is accessible for analysis and querying until the end of the retention period (with limitations described in the note below this table). |
| Retention period | Choose the desired retention period. For trace data, the available [retention period](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") ranges from 10 days to 10 years. Trace retention is defined at the bucket level, allowing tailored retention periods for specific traces. Retain calculation is independent of the trace ingestion source, whether Full-Stack, Mainframe, or Ingest & Process. The first 10 days of retention are always included. |
| Topology enrichment | Spans are enriched and processed in OpenPipeline. Enriched data (including Topology enrichment and Data processing as described in [Ingest & Process](#trace-ingest-usage)) is the basis for Retain usage for data that is stored longer than the included 10 days. |
| Data processing | Services, endpoints, and failures are detected based on span data. |
| Data storage control | Spans are filtered or excluded based on content, topology, or metadata. They are routed to a dedicated bucket. |

For Traces - Retain, data availability in certain apps is limited:

* ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** provides access to only the first 10 days of retained data.
  This app is superseded by ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
* ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** provides access only to the first 10 days of retained data.
  This app will be superseded by ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.
* ![Multidimensional Analysis](https://dt-cdn.net/images/multidimensional-analysis-512-3aed148cfe.png "Multidimensional Analysis") **Multidimensional Analysis** provides access only to the first 35 days of retained data.
  This app will be superseded by ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

## Traces - Query feature overview

Query usage occurs when:

| Concept | Explanation |
| --- | --- |
| DQL query execution | A [DQL query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") scans and fetches data that is stored in Grail. Spans can be joined and analyzed in context with other signals on the Dynatrace platform, such as logs, events, or metrics. |
| App usage | DQL queries can be executed by:  - Apps such as Notebooks **Notebooks**, Dashboards **Dashboards**, Workflows **Workflows**, and Anomaly Detection - new **Anomaly Detection**. (Note: Distributed Tracing **Distributed Tracing** and Services **Services** don't consume any Query usage.) - Dashboard tiles that are based on span data trigger the execution of DQL queries on refresh - Custom apps - The Dynatrace API |

The usage of ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** and ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is included with Dynatrace.
No query consumption is generated by these apps.

When other data types are also read in a query, this can result in consumption of the corresponding capability, such as [Log - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").

## Related topics

* [Distributed Tracing](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.")
* [Traces](/docs/semantic-dictionary/model/trace "Get to know the Semantic Dictionary models related to traces.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)