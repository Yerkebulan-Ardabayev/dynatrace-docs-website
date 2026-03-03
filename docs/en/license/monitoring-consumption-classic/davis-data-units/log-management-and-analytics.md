---
title: DDUs for Log Management and Analytics
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics
scraped: 2026-03-03T21:30:32.117251
---

# DDUs for Log Management and Analytics

# DDUs for Log Management and Analytics

* 12-min read
* Updated on Apr 07, 2025

The DDU consumption model outlined here for Log Management and Analytics only affects Dynatrace SaaS environments that are activated for Dynatrace Grail for log data management. DDU consumption for all other DDU capability types, including [Log Monitoring for Dynatrace SaaS & Managed](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic."), remains unchanged. For details about activating Log Management and Analytics for your Dynatrace environment, contact a Dynatrace product expert via live chat within your Dynatrace environment.

This page explains how DDUs are consumed by Dynatrace Log Management and Analytics and how you can estimate and track your environmentâs DDU consumption.

## DDU consumption model for Log Management and Analytics

The DDU consumption model for Log Management and Analytics is based on three dimensions of data usage (Ingest & Process, Retain, and Query). The unit of measure for consumed data volume is gigabytes (GB). Each of the three data usage dimensions consumes DDUs based on a different weight (see the "DDU consumption" row in the table below for details).

Total DDU consumption for Log Management and Analytics is calculated by multiplying the DDU weight of each of the three data-usage dimensions with the data volume in GB.

## Ingest & Process

Whatâs included with the Ingest & Process data-usage dimension?

Apply the following calculation to determine your DDU consumption for the Ingest & Process data-usage dimension:  
`(number of GBs ingested) Ã (100.00 DDU weight) = DDUs consumed`

Be aware that data enrichment and processing can increase your data volume significantly. Depending on the source of the data, the technology, the attributes, and metadata added during processing, the total data volume after processing can increase by a factor of 2 or more.

## Retain

Whatâs included with the Retain data-usage dimension?

Apply the following calculation to determine your DDU consumption for the Retain data-usage dimension:  
`(number of GB of processed data ingested) Ã (retention period in days) Ã (0.30 DDU weight) Ã (number of days that data is stored) = DDUs consumed`

## Query

Query data usage occurs when:

* Running the query in the Log & Events viewer.
* Submitting custom DQL queries in the Logs & Events viewer in advanced mode.
* Unified analysis pages show the log data of a specific entity.
* Dashboard tiles that are based on log data trigger the execution of DQL queries on refresh and include sampled data.
* Executing DQL queries via API.

Dynatrace Query Language (DQL) queries consume Davis data units (DDUs) while they are active, even when the results of such queries are not returned. To avoid unnecessary consumption of DDUs, cancel ongoing queries for logs and aggregations that are no longer necessary. Otherwise, you might be billed for incomplete queries.

Whatâs included with the Query data-usage dimension?

Apply the following calculation to determine your DDU consumption for the Query data-usage dimension:  
`(number of GB of uncompressed data read during query execution) Ã (1.70 DDU weight) = DDUs consumed`

## Calculate DDU consumption across data-usage dimensions

Following are example DDU calculations which show how each data-usage dimension contributes to overall DDU consumption.

### Step 1 â Ingest & Process

For example, say that you produce 500 GB of log data per day which you ingest into Log Management and Analytics for processing. The monthly DDU consumption for Ingest & Process in this case would be 1,500,000 DDUs:

### Step 2 - Retain

Following the Ingest & Process step, your data is retained and enriched on an on-going basis. If you ingested 500 GB of raw data in step 1, 900 GB of enriched data (`500 GB Ã 1.8 for enrichment`) is added to your storage daily. In this example, your enriched data is retained for 35 days. The monthly DDU consumption (after a ramp-up period of 35 days) for Retain in this case is 283,500 DDUs:

If the same amount of processed data is to be retained for a year, the monthly DDU consumption (after a ramp-up of 365 days in this case) for Retain is 2,956,500 DDUs.

### Step 3 - Query

Letâs assume that to resolve incidents and analyze performance issues your team executes DQL queries with a total of 25 TB of data read per day. The monthly DDU consumption for Query in this case is 1,275,000 DDUs.

### Step 4 â Total DDU consumption

The total monthly DDU consumption for this example scenario of 35 days of data retention is 3,058,500 DDUs.

## FAQ

### Can I change the retention period for Log Management and Analytics?

Yes. The following retention periods apply to log buckets:

* 10 days (10 days)
* 2 weeks (15 days)
* 1 month (35 days) default
* 3 months (95 days)
* 1 year (372 days)

* 15 months (462 days)
* 3 years (1,102 days)
* 5 years (1,832 days)
* 7 years (2,562 days)
* 10 years (3,657 days)

### Where can I check my environmentâs DDU consumption for logs and events?

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**. Youâll need the change monitoring settings permission or an admin account to access this page.
2. On the **Davis data units (DDU)** page:  
   a. In the **Consumption by DDU pool** table, see the **Log Monitoring** row.  
   b. In the **DDU consumption details** section, go to the **Log Monitoring** tab.

### What is the DDU weight of one log or event record?

For Log Management and Analytics, volume of data in gigabytes (GB) is the unit of measure. Consumption is based on three data-usage dimensions. The weight of DDU consumption per dimension is as follows:

* Ingest & Process: 100.00 DDUs per GB of data ingested and processed
* Retain: 0.30 DDUs per GB per day for data stored
* Query: 1.70 DDUs per GB for data read from storage during query execution

### What is the size of one log or event record?

The number and size of individual log records isnât relevant for DDU consumption. For Log Management and Analytics, DDU consumption for a given period is calculated based on volume of data ingested and processed, volume of data stored per day, and volume of data read from storage during query execution.

### Are there any host-included DDUs available for Log Management and Analytics?

No. Log Management and Analytics always consumes DDUs for Ingest & Process, Retain, and Query. Note that you can choose to only ingest and process data without storing it or querying it. Each Dynatrace environment includes a free tier of 200,000 DDUs per year, which can be used for Ingest & Process, Retain, and Query.

### Iâm currently using my DDUs for Log Monitoring for Dynatrace SaaS & Managed, custom metrics, custom traces, custom events, and serverless functions and I donât plan to migrate. Will anything change for me?

No. The DDU consumption model outlined here for Log Management and Analytics only affects Dynatrace SaaS environments that are activated for and connected to a Dynatrace GrailTM cluster for log data management. DDU consumption for all other DDU capability types, including Log Monitoring for Dynatrace SaaS & Managed, remains unchanged.

### Iâm considering migrating to Log Management and Analytics. What will change for me?

If Log Management and Analytics is activated for your environment, the DDU consumption model that uses gigabytes as the unit of measure will replace the event-based consumption model thatâs used for Log Monitoring for Dynatrace SaaS & Managed. Consumption of other DDU-based capability types, including Log Monitoring for Dynatrace SaaS & Managed (if you continue to use it in parallel) will remain unchanged.

### Does the Dynatrace platform consume DDUs for fractional GBs? Would 0.5 GB of Ingest & Process consume only 50 DDUs?

Yes. Every ingested GB (or fraction thereof, before enrichment and processing) is added together and then multiplied by the DDU weight of 100.00 DDUs. For example, DDU consumption for Ingest & Process of 10.50 GB equates to 1,050 DDUs.

`10.50 (GB log data) Ã 100.00 (DDU weight) = 1,050 DDUs`

### I want to convert my log messages into metrics. How will this affect my environmentâs DDU consumption?

While writing ingested logs to time series is a cost-effective way of visualizing log-based metrics, this approach consumes additional DDUs for creating custom metrics in addition to the DDUs consumed for Ingest & Process.

### Do failed query executions consume DDUs?

No, when internal failures occur while executing a query (for example, a time-out) no DDUs are consumed.

### Do canceled query executions consume DDUs?

If you cancel a query execution, all data read before the cancellation will be factored into your DDU consumption.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")