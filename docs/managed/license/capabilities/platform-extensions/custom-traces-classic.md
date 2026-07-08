---
title: Custom Traces Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/custom-traces-classic
---

# Custom Traces Classic (DPS)

# Custom Traces Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

Custom Traces Classic feature overview

This page describes how the Custom Traces Classic DPS capability is consumed and billed.
For an overview of the capability, including its main features, see [Custom Traces Classic](/managed/license/capabilities/platform-extensions#traces "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## How consumption is calculated: ingested spans

The unit of measure for Custom Traces Classic is in an ingested span.
A span is a single operation within a distributed trace.
To calculate the total consumption, multiply the number of ingested spans by the [price per span﻿](https://www.dynatrace.com/pricing/rate-card/).

Traces, including OpenTelemetry spans captured by OneAgent code modules or sent via the OneAgent local Trace API, are included with [Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged."), and therefore are not consumed as Custom Traces Classic.

## Track your consumption

This section describes the different Dynatrace tools that you can use to track consumption and costs.

### Track your consumption with metrics

Dynatrace provides built-in usage metrics that help you understand and analyze your organization's consumption of Custom Traces Classic.
To use them in Data Explorer, enter DPS into the **Search** field.
These metrics are also available via the Environment API and linked in Account Management (**Usage summary** > **Custom Traces Classic** > **Actions** > **View details**).
The table below shows the list of metrics you can use to monitor your organization's consumption of Custom Traces Classic.

(DPS) Total Custom Traces Classic billing usage
:   Key: `builtin:billing.custom_traces_classic.usage`

    Dimension: count

    Resolution: 1 min

    Description: The number of billable ingested spans aggregated over all monitored entities.

(DPS) Custom Traces Classic billing usage by monitored entity
:   Key: `builtin:billing.custom_traces_classic.usage_by_entity`

    Dimension: `dt.entity.monitored_entity\[ME:MONITORED_ENTITY]`

    Resolution: 1 min

    Description: The number of billable ingested spans split by monitored entity.

(DPS) Custom Traces Classic billing usage by span type
:   Key: `builtin:billing.custom_traces_classic.usage_by_span_type`

    Dimension: `span_type\[STRING]`

    Resolution: 1 min

    Description: The number of billable ingested spans split by span type. |

You can monitor the total number of billable custom traces for various intervals for any selected timeframe using the metric "(DPS) Total Custom Traces Classic billing usage."
The example below shows consumption aggregated in 1-hour intervals.
Between 11:00 and 14:00, around 58,000 custom traces were consumed each 1 hour.

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image056-906-0fd3d122fa.png)

Custom Traces Classic (DPS)

You can monitor the consumption of metric data points by any filtered entity using the metric "(DPS) Billed metric data points reported and split by other entities."
The example below shows that all billable custom traces between 13:00 and 14:00 came from the entity collector-trace-exporter.

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image058-908-ecba7294a8.png)

Custom Traces Classic (DPS)

If you are interested in the split by span type, use the metric "(DPS) Custom Traces Classic billing usage by span type."

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image060-906-1a6b019225.png)

Custom Traces Classic (DPS)

## Related topics

* [Platform extensions overview (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)