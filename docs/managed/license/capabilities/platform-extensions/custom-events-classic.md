---
title: Custom Events Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/custom-events-classic
---

# Custom Events Classic (DPS)

# Custom Events Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

Custom Events Classic feature overview

This page describes how the Custom Events Classic DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Custom Events Classic](/managed/license/capabilities/platform-extensions#events "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: custom events

The unit of measure for calculating your environment's consumption of custom events is custom events.

While there are no additional costs or licensing involved in the default monitoring and reporting of built-in event types via OneAgent or cloud integrations, such event-related customizations do result in additional consumption because they require significantly more processing and analytical power than the built-in event ingestion via OneAgent of cloud integrations.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Custom Events Classic.

To use them in Data Explorer, enter DPS into the **Search** field.
These metrics are also available via the Environment API and linked in Account Management (**Usage summary** > **Custom Events Classic** > **Actions** > **View details**).
The table below shows the list of metrics you can use to monitor your organization's consumption of Custom Events Classic.

(DPS) Total Custom Events Classic billing usage
:   Key: `builtin:billing.custom_events_classic.usage`

    Dimension: count

    Resolution: 1 min

    Description: Number of billable ingested events aggregated over all monitored entities.

(DPS) Custom Events Classic billing usage by event info
:   Key: `builtin:billing.custom_events_classic.usage_by_event_info`

    Dimension: count

    Resolution: 1 min

    Description: Number of billable ingested events split by entity type.

(DPS) Custom Events Classic billing usage by monitored entity
:   Key: `builtin:billing.custom_events_classic.usage_by_entity`

    Dimension: count

    Resolution: 1 min

    Description: Number of billable ingested events split by monitored entity.

You can monitor the total number of billable classic events ingested for various intervals for any selected timeframe using the metric "(DPS) Total Custom Events Classic billing usage."
The example below shows the consumption aggregated in 1-hour intervals.
Between 11:00 and 14:00, around 1,600 custom events classic were ingested every 1 hour.

![Custom Events Classic (DPS)](https://dt-cdn.net/images/image061-828-61035cf7a2.png)

Custom Events Classic (DPS)

## Related topics

* [Platform extensions overview (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)