---
title: Data Explorer FAQ
source: https://www.dynatrace.com/docs/analyze-explore-automate/explorer/explorer-troubleshooting
scraped: 2026-02-23T21:36:29.943603
---

# Data Explorer FAQ

# Data Explorer FAQ

* 1-min read
* Published Mar 10, 2022

Why am I not seeing all series of my metric?

* The *default* number of displayed series per metric is `20`. Consequently, some series might be missing in Data Explorer. To ensure the series data you're looking for is displayed, provide more specific filters such as a management zone or an entity name filter.
* The *maximum* number of displayed series per metric is `100`. Note that this limit applies even if you remove the [**limit** transformation](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit "Configure the metric selector for the Metric v2 API.") from the metric selector on the [**Code** tab](/docs/analyze-explore-automate/explorer/explorer-advanced-query-editor "Build advanced queries using the Data Explorer advanced mode.").

If series data is absent for a metric expression, see [Why is the result of my metric expression empty?](/docs/dynatrace-api/environment-api/metric-v2/metric-faq#empty-result-metric-expression "Frequently asked questions about the Metrics API v2.").

Why are some table cells empty when they should have values?

The root cause of this issue is often the same as for [Why am I not seeing all series of my metric?](#missing-series)

The metric series are limited to a certain number.

Suppose you query `builtin:host.cpu.usage` and `builtin:host.cpu.idle` split by `dt.entity.host`. For both metrics, the top 100 hosts are requested per default. But the top 100 hosts of the `builtin:host.cpu.usage` metric probably diverges from the top 100 hosts of the `builtin:host.cpu.idle` metric, leading to empty cells in the table for some hosts.

Why do I see different availability values in Data Explorer than on the Host and Process pages?

The metrics `builtin:host.availability` and `builtin:pgi.availability` are based on timeseries data provided by the OneAgents, whereas the availability values shown on the Host and Process pages are calculated by dedicated events. Thus, the values may diverge.

In the future, the availability shown in the Host and Process pages will be based on the availability metrics as well.

Why do chart values dip at the current (now) time?

If your charts show a misleading drop in values at the end (current time), you can manually adjust the timeframe to subtract the last one or two time buckets.

To temporarily adjust the timeframe

1. Open the timeframe selector.
2. Subtract one or two buckets from the end of the timeframe. For example, change `-2h` to `-2h-2m`.

To set the adjusted timeframe as the default timeframe for the dashboard

1. Edit the dashboard.
2. Under **Edit dashboard**, select the **Settings** tab.
3. Turn on **Default timeframe**.
4. Select and edit the timeframe. For example, change `-2h` to `-2h-2m`.
5. Select **Done**.

For a discussion of this issue, see [Correction required on Dashboard Charts showing dip at current timeï»¿](https://community.dynatrace.com/t5/Dynatrace-product-ideas/RFE-Correction-required-onDashboard-Charts-showing-dip-at/idi-p/144070) in the Dynatrace Community.

For more about timeframes, see [Dynatrace dashboard timeframe and management zone settings](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Related topics

* [Metrics API - FAQ](/docs/dynatrace-api/environment-api/metric-v2/metric-faq "Frequently asked questions about the Metrics API v2.")