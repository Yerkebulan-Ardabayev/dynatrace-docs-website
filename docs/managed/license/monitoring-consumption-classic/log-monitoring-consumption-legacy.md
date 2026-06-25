---
title: Log Monitoring consumption for Dynatrace versions 1.207 and earlier
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/log-monitoring-consumption-legacy
scraped: 2026-05-12T12:29:00.458428
---

# Log Monitoring consumption for Dynatrace versions 1.207 and earlier

# Log Monitoring consumption for Dynatrace versions 1.207 and earlier

* 3-min read
* Published Mar 30, 2021

Dynatrace version 1.207 and earlier

Log Monitoring consumption for Dynatrace versions 1.207 and earlier is based on anticipated GiB of annual average log storage size, which is calculated as the `average annual daily ingestion of uncompressed log data multiplied by the number of days`. Once this limit is reached, you need to [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/) to arrange for additional capacity.  
`Annual average daily log storage = Actual annual storage / (# of days)`. Each Dynatrace environment comes with 5 GB of log data storage, per year at no cost to you.

## Log storage calculation example

Say, for example, that your Log Monitoring agreement is configured for 90 days and you've arranged for 450 GiB of annual daily average storage. The anticipated average daily ingestion of log data in this case would be 5 GiB.  
`450 (GiB; base quota of annual average storage) / 90 (days) = 5 (GiB; anticipated average daily ingestion)`

Once the annual equivalent of 1,825 GiB is ingested and exceeded, the annual average storage size of 450 GiB is also reached.  
`5 (GiB; anticipated average daily ingestion) Ã 365 (days) = 1,825 (GiB; anticipated average annual ingestion)`

Continuing with the example above, if after six months your actual log ingestion is only 912.5 GiB (50% of the anticipated 1,825 GiB), then you might decide to re-configure your Log Monitoring allotment down to 45 days while leaving the annual average storage capacity unchanged at 450 GiB. In this case, the anticipated average daily ingestion of log data for the subsequent six months would be 10 GiB.  
`450 (GiB; average annual capacity) / 45 (days) = 10 (GiB; anticipated average daily ingestion)`

Once the annual equivalent of 2,737.5 GiB is ingested, the annual average storage size of 450 GiB is also reached.  
`(5 Ã 182.5) + (10 Ã 182.5) = 2,737.5`

If you've arranged for annual log storage capacity, your usage will reset annually (Dynatrace SaaS only).

## Dynatrace Managed - Annual average log storage (GiB)

Log Monitoring consumption is based on anticipated GiB per day of annual average log ingestion, which is calculated as the average annual daily ingestion of uncompressed log data. Once this limit is reached, you need to [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/) to arrange for additional capacity.

For example, if during an annual period the total log data sent to your Dynatrace Managed Cluster is 730 GiB, then the "per day" rate of annual average ingestion would be 2 GiB.  
`730 (GiB; actual annual ingestion) / 365 (days) = 2 (GiB; annual average daily ingestion)`

If you've arranged for annual log storage capacity, your usage will reset annually.

### Log Monitoring overages (optional) - Dynatrace Managed deployments

If you've arranged for Log Monitoring overages so that you can exceed your agreed upon maximum limit of daily log storage, your overages will be calculated based on the difference between your daily storage limit and your actual daily storage size.
For example, if you have an agreed upon storage limit of 10 GiB/day and your actual consumption is 12 GiB/day, you'll have 2 GiB/day in overages.  
`12 (GiB; actual daily log storage) - 10 (GiB; daily log storage limit) = 2 (GiB; daily overage)`  
To add or remove overages from your account, [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/).

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Extending Dynatrace (Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")