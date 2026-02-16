---
title: Log Analytics (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/log-analytics
scraped: 2026-02-16T21:19:56.895128
---

# Log Analytics (DPS)

# Log Analytics (DPS)

* Latest Dynatrace
* Overview
* 10-min read
* Updated on Nov 25, 2025

This page describes log observability capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific capability translates to consumption of your DPS license commit, see

* [Log - Ingest & Process](/docs/license/capabilities/log-analytics/dps-log-ingest "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.")
* [Log - Retain](/docs/license/capabilities/log-analytics/dps-log-retain "Learn how your consumption of the Log Management & Analytics - Retain DPS capability is billed and charged.")
* [Log - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.")
* [Log - Retain with Included Queries](/docs/license/capabilities/log-analytics/dps-log-retain-included "Learn how your consumption of the Log Management & Analytics - Retain with Included Queries DPS capability is billed and charged.")

Dynatrace offers

* A usage-based model, with Log - Retain and Log - Query charged separately.
* Retain with Included Queries.

## Usage-based model

In the usage-based model, Log - Retain and Log - Query are charged separately.

In this case, you pay for each query.
This is ideal if you have historical data that you do not access frequently.

## Log - Ingest & Process feature overview

What's included with the Ingest & Process data-usage dimension?

| Concept | Explanation |
| --- | --- |
| Data delivery | Delivery of log data via OneAgent or Log ingestion API (via ActiveGate) |
| Topology enrichment | Enrichment of log events with data source and topology metadata |
| Data transformation | - Add, edit, or drop any log attribute - Perform mathematical transformations on numerical values (for example, creating new attributes based on calculations of existing attributes) - Mask sensitive data by replacing either the whole log record, one specific log record attribute, or certain text with a masked string - Extract business, infrastructure, application, or other data from raw logs. This can be a single character, string, number, array of values, or other. Extracted data can be turned into a new attribute allowing additional querying and filtering. Metrics can be created from newly extracted attributes (see Conversion to time series below) |
| Data-retention control | - Filter and exclude incoming logs based on content, topology, or metadata (filtering generates usage for Ingest & Process, but not for Retain) - Manage data retention periods of incoming logs based on data-retention rules |
| Conversion to time series | Create metrics from log records or attributes (note that creating custom metrics generates additional consumption as described here) |

Apply the following calculation to determine your consumption for the Ingest & Process data-usage dimension:

`consumption = (number of GiBs ingested) Ã (GiB price as per your rate card)`

Data enrichment and processing can increase your data volume significantly.
Depending on the source of the data, the technology, the attributes, and metadata added during processing, the total data volume after processing can increase by a factor of 2 or more.

Dynatrace reserves the right to work with customers to adjust or disable parsing rules, processors, or pipelines that are experiencing service degradation.

## Log - Retain feature overview

Here's what's included with the Retain data-usage dimension:

| Concept | Explanation |
| --- | --- |
| Data availability | Retained data is accessible for analysis and querying until the end of the retention period. |
| Retention periods | Choose a desired retention period. For log buckets, the available retention period ranges from 1 day to 10 years.  Metrics retention is defined at the bucket level, ensuring tailored retention periods for specific metrics. |

## Log - Query feature overview

Query data usage occurs when:

* Executing DQL queries in Notebooks, Workflows, Custom Apps and via API
* Dashboard tiles that are based on log data trigger the execution of DQL queries on refresh and include sampled data
* Submitting DQL queries by clicking the âRun queryâ button (for example, in the Logs & Events viewer in simple and advanced mode or on unified analysis pages)

What's included with the Query data-usage dimension?

| Concept | Explanation |
| --- | --- |
| On-read parsing | Use DQL to query historical logs in storage and extract business, infrastructure, or other data across any timeframe, and use extracted data for follow-up analysis |
| Aggregation | Perform aggregation, summarization, or statistical analysis of data in logs across specific timeframes or time patterns (for example, data occurrences in 30-second or 10-minute intervals) |
| Reporting | Create reports or summaries with customized fields (columns) by adding, modifying, or dropping existing log attributes |
| Context | Use DQL to analyze log data in context with relevant data on the Dynatrace platform, for example, user sessions or distributed traces |

## Log - Retain with Included Queries feature overview

Dynatrace version 1.316+

In the Retain with Included Queries model, retained log data within a configured time period can be queried free of charge, as often as you want.
This is ideal if you frequently access recent data, or look at highly predictable consumption patterns.

Customers can split a log bucketâs retention period into two parts:

* An Included Queries retention period (10â35 days of data retention).
* The overall retention period (up to 10 years) that follows the usage-based [Retain](#retain) and [Query](#query) model.

With the Retain with Included Queries model, Log - Ingest & Process consumption continues to be calculated separately and is charged only once for the initial ingestion into your tenant.

Customers who select the Retain with Included Queries option in the bucket configuration are not charged for those queries executed within the scope of the **Included Queries** retention period. (The retention period is defined on a log bucket within the Dynatrace Platform.)
For queries that are executed and include a scope outside of the Included Queries period, only these logs outside of the Retain with Included Queries are billed individually with the usage based [Log - Query](#query) model.

`Included query usage per day = (GiB of logs within the defined Included Queries retention period) Ã 15`

In any 24-hour period, customers with this licensing option activated are entitled to run queries with an aggregate scanned-GiB volume of up to 15 times the volume of log data that is retained within the **Included Queries** timeframe at that time.
Example: You ingest and retain 1 GiB per day, and set the Included Queries retention period to 10 days. Your query quota is 150 GiB per 24 hours (1 GiB x 10 Days x 15 Multiplier = 150 GiB).

Using this formula, we have included sufficient queries for the majority of customers.
In case you exceed the included query volume, the Dynatrace team will reach out and help you to evaluate and optimize query consumption.
Alternatively, if the Retain with Included Query option does not meet your use case and requirements, you can reconfigure a bucket at any time to use individually billed on-demand queries without losing data.

## Related topics

* [Log Analytics](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")
* [What is Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)