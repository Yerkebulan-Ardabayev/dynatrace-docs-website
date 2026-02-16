---
title: Metrics powered by Grail overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/metrics
scraped: 2026-02-16T21:19:59.594291
---

# Metrics powered by Grail overview (DPS)

# Metrics powered by Grail overview (DPS)

* Latest Dynatrace
* Overview
* 7-min read
* Updated on Jan 26, 2026

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Metrics - Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.")
* [Metrics - Retain](/docs/license/capabilities/metrics/dps-metrics-retain "Learn how your consumption of the Metrics - Retain DPS capability is billed and charged.")
* [Metrics - Query](/docs/license/capabilities/metrics/dps-metrics-query "Learn how your consumption of the Metrics - Query DPS capability is billed and charged.")

## Metrics - Ingest & Process feature overview

Here's what's included with the Ingest & Process data-usage dimension:

Concept

Explanation

Data delivery

Delivery of metrics via OneAgent, extensions or ingest API

Topology enrichment

Enrichment of metrics with data source and topology metadata

Data transformation

* Rollup of data to reduced granularity to optimize queries for longer timeframes
* Use of efficient data structures to derive metrics from high volume spans like service response time metrics

Data-retention control

Manage data retention period of incoming metrics based on bucket assignment rules

## Metrics - Retain feature overview

Here's what's included with the Retain data-usage dimension:

Concept

Explanation

Data availability

Retained data is accessible for analysis and querying until the end of the retention period.
Metrics retention is defined at the bucket level, ensuring tailored retention periods for specific metrics.

Retention periods

Choose a desired retention period.
For the default metrics bucket, the available retention period ranges from 15 months (462 days) to 10 years (3,657 days).

## Metrics - Query feature overview

Here's what's included with the Query data-usage dimension:

| Concept | Explanation |
| --- | --- |
| DQL query execution | A [DQL query](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") scans and fetches data that is stored in Grail. Querying metrics using the `timeseries` command is always included. |
| App usage | DQL queries can be executed by:  - Apps such as Notebooks **Notebooks**, Dashboards **Dashboards**, Workflows **Workflows**, and Anomaly Detection - new **Anomaly Detection**. - Dashboard tiles that are based on metrics trigger the execution of DQL queries on refresh - Custom apps - The Dynatrace API |

## Related topics

* [Metrics](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)