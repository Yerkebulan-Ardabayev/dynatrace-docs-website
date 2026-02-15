---
title: Out-of-memory (OOM) and out-of-threads (OOT) events and alerting
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-02-15T09:12:24.029736
---

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

* Latest Dynatrace
* 2-min read
* Updated on Jan 10, 2024

To set up out-of-memory (OOM) and out-of-threads (OOT) events for standalone/PaaS scenarios and cloud-native Full-Stack injections, follow the instructions below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Enable the OneAgent feature**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#enable-feature "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create metric events**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#create-metrics "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")

## Step 1 Enable the OneAgent feature

To enable out-of-memory (OOM) and out-of-threads (OOT) detection

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find and turn on **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Select **Save changes**.

## Step 2 Set up high GC activity alerts

If you've already set up alerts for [high GC activity](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection#hosts "Configure host anomaly detection, including problem and event thresholds.") in your environment, alerts are automatically created for standalone/PaaS scenarios and cloud-native Full-Stack injections.

To verify your setup

1. Go to **Settings** > **Anomaly detection** and select **Hosts**.
2. Make sure that **Detect high GC activity** is turned on.

   If you're using a customized setup for [long garbage-collection times alerts](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events#long-garbage-collection-time "Learn more about resource events and the logic behind raising them."), note that, for standalone/PaaS scenarios and cloud-native Full-Stack injections, data collected in 10-second observation intervals is adjusted to one-minute observation intervals.

Alternatively, you can create alerts only for specific metric events.

1. Go to **Settings** > **Anomaly detection** and select **Metric events**.
2. Select **Add metric event**.
3. Define the following two events.

   Metric event

   Metric key

   Threshold

   Violating samples

   Sliding window

   Dealerting samples

   High GC suspension time

   `builtin:tech.jvm.memory.gc.suspensionTime`

   25 %

   3

   5

   4

   High GC total collection time

   `builtin:tech.jvm.memory.gc.collectionTime`

   24 s

   3

   5

   4
4. Select **Save changes**.

## Related topics

* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Static thresholds for infrastructure monitoring](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure "Learn about the fixed thresholds used by Dynatrace to determine when a detected slowdown or error-rate increase justifies the generation of a new problem event.")