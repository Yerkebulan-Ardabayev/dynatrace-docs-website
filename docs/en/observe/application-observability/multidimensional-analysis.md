---
title: Multidimensional analysis
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis
scraped: 2026-02-28T21:15:01.201692
---

# Multidimensional analysis

# Multidimensional analysis

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The **Multidimensional analysis** view enables you to analyze web requests of your services with fine-tuned filtering, so you can focus your analysis on the dimensions that matter most. This view is easily configurable and serves as a convenient entry point for in-depth analysis of your services.

With multidimensional analysis, you can investigate custom views: **Top web requests**, **Database statements**, and **Exception analysis**.

To access the **Multidimensional analysis** page

1. Go to **Multidimensional Analysis**.
2. Choose one of the analysis options that you want to investigate, or **Create analysis view**.

## Pre-defined views

[### Top web requests

Analyze the most frequent and most expensive web requests.](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")[### Top database statements

Analyze the most frequent and most expensive database statements.](/docs/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")[### Exception analysis

Understand and analyze all code-level exceptions.](/docs/observe/application-observability/multidimensional-analysis/exception-analysis "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")

## Data source

Multidimensional analysis uses trace and request data as its data source, which includes information on [distributed traces](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#traces-grail "Check retention times for various data types.") and [requests](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#request-attributes "Check retention times for various data types.").

* For timeframes shorter than two hours, a higher resolution (below 1 minute) is used.
* For larger amounts of data, especially for longer timeframes or unfiltered analysis, sampling is applied: only a fraction of trace and request data is used.
* To view the information about the data used for analysis and suggestions on how to improve accuracy, hover over **Refine**.
* To include more data to the analysis, select **Refine**.

Multidimensional analysis vs charts

Unlike [Data Explorer](/docs/analyze-explore-automate/explorer#limitations "Query for metrics and transform results to gain desired insights."), multidimensional analysis uses trace and request data, not metric data, so values on multidimensional analysis charts might differ from values on custom charts.

## Configure view

In **Configure view**, you can set up multiple filtering capabilities. The view updates automatically as you change the parameters.

You can export the table data in a comma-separated values (CSV) file.

1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
2. Select **Export visible data** or **Export table data**.

## View

![Top database statements page](https://dt-cdn.net/images/top-database-statements-3564-3bd08ea1b1.png)

The chart shows the top 15 dimensions (all other dimensions are aggregated into a single dimension) and the table beneath contains up to 85 more dimensions, bringing the total number of chartable dimensions to 100. The view instantly adapts to the changes you make in the **Configure view** pane.

In the **Actions** column of the table, you can select:

* **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") to filter the view for the specified dimension.
* **More** (**â¦**) to access further analysis options from the [**Analyze** menu](/docs/observe/application-observability/services-classic/context-specific-drill-down#analyze-menu "Learn about easy navigation and filtering for services analysis.").

For timeframes containing data older than 10 days, you can turn on **Show data retention** to better understand which data is available for which period directly from the chart.

### Save view

Once the view is configured, you can save it for quick access in the future. Just select **Save** view and provide a name.

Dynatrace provides several views out of the box:

* [Exception analysis](/docs/observe/application-observability/multidimensional-analysis/exception-analysis "Learn how Dynatrace can help you see which exceptions occurred in your environment during a selected analysis timeframe.")
* [Top database statements](/docs/observe/application-observability/multidimensional-analysis/top-database-statements "Understand the database activity across your environment with Dynatrace.")
* [Top web requests](/docs/observe/application-observability/multidimensional-analysis/top-web-requests "Learn how to analyze all web requests across all of your services using Dynatrace.")

## Calculated service metric

You can save the configured view as a calculated service metric, which you can use just like any other Dynatrace metric, for example for [charting](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [data export via API](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.").

Only new data is written to calculated metrics; retrospective data is not included.

Limits

* Only new data is written to calculated metrics; retrospective data is not included.
* You can have up to 500 enabled calculated metrics per environment and up to 100 enabled calculated metrics per service.
* Classic calculated metrics support at most 100 dimension values. This is referred to as the "top X" rule, as you can select fewer depending on your configuration. However you choose the top 100 dimension values, the remaining dimensions are aggregated into a single timeseries and the dimension value is accessible through a special `remainder` dimension. The [remainder](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Configure the metric selector for the Metric v2 API.") filter condition allowing you to filter on this `remainder` dimension.

* Grail calculated service metrics with cardinality higher than 2000 within any 5-minute window in the past 2 weeks or since the last metric change are automatically disabled in Grail. Enabling such metrics on Grail is not allowed. If the metric is already enabled on Grail, you are informed of the metric rejection via the [**Metric & Dimensions Usage + Rejections**](/docs/dynatrace-api/environment-api/metric-v2/best-practices#identify-high-cardinality-situations "Best practices for metrics.") ready-made dashboard. To enable a Classic metric on Grail and keep collecting incoming data on Grail, make sure cardinality stays below the limit.

To create a calculated service metric from a multidimensional analysis view

1. Go to **Multidimensional Analysis**.
2. Select **Create analysis view**.
3. Optional Select the management zone. The new metric will be restricted to data from this zone.
4. Configure the view. Find the description of available options in the [**Configure view**](#configure) section above.
5. In the **View** pane, select **Create metric**.

   ![Create calculated metric](https://dt-cdn.net/images/service-calculated-metric-create-328-e5859c1ea9.png)
6. Specify the name for the metric. The name is added to the metric key automatically.
7. Optional If needed, customize the metric key.

   Once a metric is created, you can't change its key.
8. Optional If you want to fine-tune your metric, select **Advanced options** to configure additional parameters of the metric. For details, see [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.").
9. Select **Create metric**.

## Related topics

* [Service metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")
* [Calculated metrics for services](/docs/observe/application-observability/services/calculated-service-metric "Learn how to create a calculated metric based on web requests.")