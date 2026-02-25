---
title: Extract a metric from user events
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-events
scraped: 2026-02-25T21:17:40.906181
---

# Extract a metric from user events

# Extract a metric from user events

* Latest Dynatrace
* Tutorial
* Published Dec 19, 2025

OpenPipeline makes it straightforward to turn [user events](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-events "Get familiar with the data model at the heart of the New RUM Experience.") into custom metrics, giving you the power to analyze patterns that impact your goals in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") while ensuring your data remains useful for long-term analysis. Its ability to parse data from standard user event attributes into dedicated fields facilitates metric extraction.

To illustrate the process, this guide uses a travel booking site as an exampleâthe number of views per journey is extracted into a custom metric to help identify trends.

## Example scenario

In this tutorial, weâll use the [Dynatrace demo application easyTravelï»¿](https://dt-url.net/rj034fg) as an example. easyTravel lists available journeys, and when a user selects a journey, its details are displayed.

The application is instrumented with the RUM JavaScript, and the captured data is mapped to a [frontend](/docs/observe/digital-experience/new-rum-experience/concepts/frontends "Learn about the frontend concept in the New RUM Experience.") named `easytravel`. Each time a user navigates from one page to anotherâfor example, from the home page to a specific journeyâa [navigation event](/docs/observe/digital-experience/new-rum-experience/web-frontends/concepts/pages-views-and-navigations#navigations "Understand how pages, views, and navigations are defined for web frontends the New RUM Experience.") is captured.

Navigation events provide the information needed to analyze the number of views per journey. Each journey has a unique ID. When a soft navigation to a specific journey occurs, the URL path updates to include that journey IDâfor example, `/easytravel/journeys/24859438`. This value is captured in the `view.url.path` field of the navigation event.

Therefore, you can analyze the number of views per journey by running the following DQL query:

```
fetch user.events



| filter matchesPhrase(frontend.name, "easytravel") AND



characteristics.has_navigation == true AND



matchesPhrase(view.url.path, "/easytravel/journeys/*") AND



not matchesPhrase(view.url.path, "*book")



| parse view.url.path, "'/'LD'/'LD'/'LD:journey_id"



| summarize by: {journey_id}, count()



| sort `count()` desc
```

While this query works well for short-term analysis, itâs not ideal for monitoring long-term trends. For that purpose, creating a custom metric derived from the query using OpenPipeline is a more suitable approach.

## Before you begin

Prior knowledge

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")

Prerequisites

Ensure you have the permissions described in [New RUM Experience permissions](/docs/observe/digital-experience/new-rum-experience/permissions "See what permissions you need to set up the New RUM Experience.").

## How-to

1. Create a pipeline for parsing and metric extraction

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User events** > **Pipelines**.
2. To create a new pipeline, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** and enter a name (for example, `easyTravel`).
3. To configure the parsing of the journey ID into a separate field, go to **Processing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **DQL** and define the processor by entering:

   * A descriptive name (for example, `Add journey_id`).
   * A matching condition. In our example, the matching condition is:

     ```
     characteristics.has_navigation == true AND



     matchesPhrase(view.url.path, "/easytravel/journeys/*") AND



     not matchesPhrase(view.url.path, "*book")
     ```
   * A processor definition. In our example, the processor definition is:

     ```
     parse view.url.path, "'/'LD'/'LD'/'LD:journey_id"



     | fieldsAdd journey_id
     ```
4. To configure metric extraction, go to **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Counter metric** and define the processor by entering:

   * A descriptive **Name** (for example, `Viewed journeys`).
   * A **Matching condition** (`isNotNull(journey_id)`).
   * A **Metric key** (`easytravel.journey_view_count`).
   * A metric dimension. Under **Dimensions**

     1. Select **Custom**.
     2. Enter a **Field name on record** (`journey_id`).
     3. Enter a **Dimension name** (`journey_id`).
5. Select **Add dimension**.
6. Select **Save**.

2. Route data to the pipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User events** > **Dynamic routing**.
2. To create a new route, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** and specify:

   * A descriptive **Name** (for example, `easyTravel route`).
   * A **Matching condition**. In our example, the matching condition is:

     ```
     matchesValue(frontend.name, "easytravel")
     ```
   * The **Pipeline** containing the processing instructions (`easyTravel`).
3. Select **Save**.

## Conclusion

You have successfully created a pipeline to parse user events and extract a metric. You can now go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and view it, for example using the following query:

```
timeseries count = sum(easytravel.journey_view_count), by: {journey_id}, interval: 3h



| sort arraysum(count) desc



| limit 5
```

![Custom metric extracted from user events showing the top viewed journeys in easyTravel](https://dt-cdn.net/images/custom-metric-extraction-from-user-events-example-1292-7c0ae97470.png)

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")