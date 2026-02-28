---
title: Extract a metric to track system events
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-system-events
scraped: 2026-02-28T21:12:35.858162
---

# Extract a metric to track system events

# Extract a metric to track system events

* Latest Dynatrace
* Tutorial
* 3-min read
* Updated on Jun 23, 2025

Dynatrace produces system events for system activity in your environment, for example, when an app is installed, updated, and uninstalled. You can extract a metric via OpenPipeline and track how many app updates occurred in your environment.

## Who this is for

This article is intended for administrators and app users.

## What you will learn

In this article, you'll learn how to set up OpenPipeline to extract a metric to monitor system events frequency.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

* [Latest Dynatrace](/docs/platform "Dynatrace is an all-in-one platform that's purpose-built for a wide range of use cases.") environment
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license with [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") capabilities
* `storage:system:read` user permission

## Steps

1. Find the condition for the relevant records

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **DQL**.
3. Enter a DQL query to fetch the relevant records.

   App lifecycle events are audit events produced by Dynatrace AppEngine [Registryï»¿](https://developer.dynatrace.com/develop/sdks/client-app-engine-registry/). The following example query fetches app lifecycle events and summarizes the results by event type.

   ```
   fetch dt.system.events



   | filter event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"



   | summarize by:{event.type}, count()
   ```

   Run in Playground
4. To filter only by app updates, select **app.updated** >  **Filter**.

You found the condition that identifies app updates (`event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY" AND event.type == "app.updated"`).

2. Create a pipeline for metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **System events** > **Pipelines**.
2. To create a new pipeline, select  **Pipeline** and enter a nameâfor example, `App LifeCycle-Updates`.
3. To configure metric extraction, go to **Metric extraction** >  **Processor** > **Counter metric** and define the processor by entering:

   * A descriptive nameâfor example, `Frequency`
   * The matching condition `event.type == "app.updated"`
   * The new metric keyâfor example, `apps.updates`
   * The metric dimensions:

     1. Select **Pre-defined** and choose `resource` from the [pre-defined dimensions](/docs/semantic-dictionary/model/dt-system-events#audit-event "Get to know the Semantic Dictionary models related to system events."). This dimension identifies the ID of the app from which the update originates.
     2. Select **Custom** and enter:

        + **Field name on record**: A custom dimension that further defines your metricâfor example, `details.app.type`.
        + **Dimension name**: An optional field that can be used in the case of nested fields, or if you want to give the dimension an alias.
     3. Select **Add**.
4. Select **Save**.

You successfully created a new pipeline to extract a metric containing information about the event's source and further app details. The new pipeline is visible in the pipelines list.

3. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **System events** > **Dynamic routing**.
2. To create a new route, select  **Dynamic route** and specify:

   * A descriptive nameâfor example, `App LifeCycle`
   * The matching condition

     ```
     event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"
     ```
   * The pipeline containing the processing instructions (`App LifeCycle-Updates`)
3. Select **Add**.

You successfully created a new route. All app lifecycle events are routed to the pipeline where a metric is extracted only for app updates. The new route is visible in the routes list.

4. Query the metric

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open an existing or new notebook.
2. Select  > **Metrics** > **Select a metric**.
3. Enter and select the new metric key (`dt.system.events.apps.updates`).
4. Select  **Run**.

## Conclusion

You successfully extracted a metric to track app update frequency. All new app lifecycle events are routed to a new pipeline. When a record is an app update, the new pipeline extracts a metric containing the ID of the application from which the update originates and further app details. You can query the metric in Dashboards and Notebooks.

## Related topics

* [System event models](/docs/semantic-dictionary/model/dt-system-events "Get to know the Semantic Dictionary models related to system events.")