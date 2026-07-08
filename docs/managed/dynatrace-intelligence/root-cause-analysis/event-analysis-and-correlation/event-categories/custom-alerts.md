---
title: Custom alerts
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/custom-alerts
---

# Custom alerts

# Custom alerts

* Explanation
* 1-min read
* Updated on Jan 28, 2026

This page provides information about supported custom alerts and the logic behind raising them.

Custom alerts can be defined when a specific threshold notification on a selected metric is required.

A `CUSTOM_ALERT` event type provides a simple way of defining a threshold on a given metric. Dynatrace sends out alerts when a metric breaches a user-defined threshold. You can define alerts for when actual metric values are above or below the user-defined threshold. Because a metric can be recorded by multiple components within your environment, Dynatrace always alerts with a reference to the component that shows the violating metric.

Like other event types, you can configure Davis AI functionality for custom events using well-defined event properties, such as `dt.davis.allow_merge`. For more information about properties, see [Semantic Dictionary](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

## Related topics

* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")