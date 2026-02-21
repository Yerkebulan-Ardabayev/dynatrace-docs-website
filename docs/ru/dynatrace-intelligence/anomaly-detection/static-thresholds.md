---
title: Static thresholds for anomaly detection
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/static-thresholds
scraped: 2026-02-21T21:19:32.809305
---

# Static thresholds for anomaly detection

# Static thresholds for anomaly detection

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Apr 05, 2024

A static threshold represents a hard limit that a metric should not violate. Because static thresholds don't change over time, they are an important monitoring tool for defining critical boundaries of normal operation.

It's important to choose between a static and an [adaptive threshold](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "How Dynatrace adapts thresholds for multiple entities within the scope of an anomaly detection configuration."), depending on your use case.

For example, you can use a static threshold to set a limit for total memory usage by a well-known process. In this case, a static threshold is superior to an adaptive threshold because if memory consumption slowly grows over time, the adaptive threshold simply changes with it, raising no problems and eventually leading to a hidden memory leak.

In the illustrations below, memory consumption steadily increases over 30 days. A statically defined threshold of 40 MB will catch the process's abnormal behavior, while an adaptive threshold will increase along with the metric value.

![Static threshold](https://dt-cdn.net/images/static-threshold-1-1041-d8667870ee.png)

![Adaptive threshold](https://dt-cdn.net/images/static-threshold-2-1041-538cab4669.png)

Apart from the threshold value, you can specify how often the threshold must be violated within a sliding time window to raise an event (violations don't have to be successive). It helps you to avoid alerting too aggressively on single threshold violations. You can set a sliding window of up to 60 minutes.

By default, any 3 minutes out of a sliding window of 5 minutes must violate your threshold to raise an event. That is, an event would require 3 violating minutes within any 5-minute sliding window.

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")