---
title: Out-of-memory (OOM) and out-of-threads (OOT) events and alerting
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-03-06T21:29:46.503655
---

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting


* Latest Dynatrace
* 2-min read
* Updated on Jan 10, 2024

To set up out-of-memory (OOM) and out-of-threads (OOT) events for standalone/PaaS scenarios and cloud-native Full-Stack injections, follow the instructions below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Enable the OneAgent feature**](set-up-event-and-memory-alerting.md#enable-feature "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create metric events**](set-up-event-and-memory-alerting.md#create-metrics "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")

## Step 1 Enable the OneAgent feature

To enable out-of-memory (OOM) and out-of-threads (OOT) detection

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find and turn on **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Select **Save changes**.

## Step 2 Set up high GC activity alerts

If you've already set up alerts for high GC activity in your environment, alerts are automatically created for standalone/PaaS scenarios and cloud-native Full-Stack injections.

To verify your setup

1. Go to **Settings** > **Anomaly detection** and select **Hosts**.
2. Make sure that **Detect high GC activity** is turned on.

   If you're using a customized setup for long garbage-collection times alerts, note that, for standalone/PaaS scenarios and cloud-native Full-Stack injections, data collected in 10-second observation intervals is adjusted to one-minute observation intervals.

Alternatively, you can create alerts only for specific metric events.

1. Go to **Settings** > **Anomaly detection** and select **Metric events**.
2. Select **Add metric event**.
3. Define the following two events.
4. Select **Save changes**.

## Related topics

* Metric events
* Static thresholds for infrastructure monitoring