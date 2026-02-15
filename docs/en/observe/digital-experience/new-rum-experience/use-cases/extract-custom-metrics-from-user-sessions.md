---
title: Extract a metric from user sessions
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-sessions
scraped: 2026-02-15T09:02:29.239024
---

# Extract a metric from user sessions

# Extract a metric from user sessions

* Latest Dynatrace
* Tutorial
* Published Dec 19, 2025

OpenPipeline lets you extract custom metrics from [user sessions](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-sessions "Get familiar with the data model at the heart of the New RUM Experience."), enabling long-term analyses in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** that go far beyond standard performance monitoring. By combining these metrics with [user session properties](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#event-and-session-properties "Get familiar with the data model at the heart of the New RUM Experience."), you gain the flexibility to uncover insights that are highly tailored to your business objectives.

To illustrate this process, this guide walks you through extracting a customer conversion metric from user sessions, showing the number of sessions that resulted in a customer conversion versus those that did not.

## Example scenario

In this tutorial, weâll use a web shop as our example. The shop is instrumented with the RUM JavaScript, and the captured data is mapped to a [frontend](/docs/observe/digital-experience/new-rum-experience/concepts/frontends "Learn about the frontend concept in the New RUM Experience.") named `webshop`.

Instrumentation was customized to send a user session property `successful_checkout` whenever a customer successfully completes the checkout process. The property was configured as described in [Capture event and session properties for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for web frontends.") and then sent via JavaScript API using [`sendSessionPropertyEvent`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.sendSessionPropertyEvent.html):

```
dynatrace.sendSessionPropertyEvent({



"session_properties.successful_checkout": true



});
```

With this setup, you can analyze the number of sessions with and without customer conversion by running the following DQL query:

```
fetch user.sessions



| summarize by:{session_properties.successful_checkout}, count()
```

While this query works well for short-term analysis, itâs not ideal for uncovering long-term patterns, which is much better handled by using a custom metric.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

Ensure you have the permissions described in [New RUM Experience permissions](/docs/observe/digital-experience/new-rum-experience/permissions "See what permissions you need to set up the New RUM Experience.").

## How-to

1. Create a pipeline for metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User sessions** > **Pipelines**.
2. To create a new pipeline, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** and enter a name (for example, `Webshop`).
3. To configure metric extraction, go to **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Counter metric** and define the processor by entering:

   * A descriptive **Name** (for example, `Conversion statistics`).
   * A **Matching condition** (`true`).
   * A **Metric key** (`webshop.checkout_statistics`).
   * A metric dimension Under **Dimensions**

     1. Select **Custom**.
     2. Enter a **Field name on record** (`session_properties.successful_checkout`).
     3. Enter a **Dimension name** (`successful_checkout`).
     4. Enter a **Default value** (`false`).
4. Select **Add dimension**.
5. Select **Save**.

2. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User sessions** > **Dynamic routing**.
2. To create a new route, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** and specify:

   * A descriptive **Name** (for example, `Webshop route`).
   * A **Matching condition**. In our example, the matching condition is:

     ```
     matchesValue(frontend.name, "webshop")
     ```
   * The **Pipeline** containing the processing instructions (`Webshop`).
3. Select **Save**.

## Conclusion

You have successfully extracted a custom metric from user sessions. You can now go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and view it, for example using the following query:

```
timeseries sum(easytravel.checkout_statistics), by: { successful_checkout }, interval: 15m



| fieldsAdd checkout_status = if(successful_checkout == "true", "Successful Checkout", else: "No Checkout")
```

![Custom metric extracted from user sessions showing customer conversion in a web shop](https://dt-cdn.net/images/custom-metric-extraction-from-user-sessions-example-1174-7eec1c7551.png)

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [Capture event and session properties for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for web frontends.")
* [Capture event and session properties for mobile frontends](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for mobile frontends.")