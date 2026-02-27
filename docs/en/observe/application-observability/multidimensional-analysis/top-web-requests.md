---
title: Top web requests
source: https://www.dynatrace.com/docs/observe/application-observability/multidimensional-analysis/top-web-requests
scraped: 2026-02-27T21:24:36.984598
---

# Top web requests

# Top web requests

* How-to guide
* 4-min read
* Updated on Sep 13, 2022

The highly flexible **Top web requests** view enables you to analyze the top web requests across all your services and to look for requests that originate from or are destined to specific URLs. This view is easily configurable and serves as a convenient entry point for in-depth analysis of your services.

To access the **Top web requests** analysis page

1. Go to **Multidimensional Analysis**.
2. Click the **Top web requests** tile.

![Top web requests page](https://dt-cdn.net/images/top-web-requests-page-3518-5c4cc7fb02.png)

## Configure view

The **Top web requests** page lists all web requests that occurred during the selected timeframe and within the selected management zone. In **Configure view**, you can set up multiple filtering capabilities. The view updates automatically as you change the parameters.

Once the view is configured, you can save it for quick access in the future. Just select **Save view** and provide a name.

You can also save the configuration as a calculated service metric and use it as any other metric in Dynatrace (for example, for [alerting](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")).

You can export the table data in a comma-separated values (CSV) file.

1. In the lower-right corner of the page, select **Show export menu** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More").

   ![Show export menu](https://dt-cdn.net/images/show-export-menu-107-2a8a76c9a2.png)
2. Select **Export visible data** or **Export table data**.

## View

* The chart on the **Top web requests** page shows the top 15 dimensions (all other dimensions are aggregated into a single dimension), and the table beneath contains up to 85 more dimensions, bringing the total number of chartable dimensions to 100. The view instantly adapts to the changes you make in the **Configure view** pane.
* The chart uses [trace and request data](/docs/observe/application-observability/multidimensional-analysis#data-source "Configure a multidimensional analysis view and save it as a calculated metric."), which has different data retention periods. For timeframes containing data older than 10 days, you can turn on the **Show data retention** toggle to better understand which data is available for which period directly from the chart.
* In the **Actions** column of the table, you can select:

  + **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") to filter the view for the specified dimension.
  + **More** (**â¦**) to access further analysis options from the [**Analyze** menu](/docs/observe/application-observability/services-classic/context-specific-drill-down#analyze-menu "Learn about easy navigation and filtering for services analysis.").

## Example use cases

Here you can find some use cases for the **Top web requests** view.

### Find a particular URL

With **Top web request** view you can focus your analysis on requests that come from or are going to a particular URL.

1. Specify `{URL:Host}{Relative-URL}` in the **Split by dimension** field to split your requests based on URLs.
2. Now filter the requests to a particular URL. In the **Filter requests** field, select the `Web request URL` filter type and provide the pattern for the URL. Note that this filter uses the **CONTAINS** operator.

### Find requests with error response codes

You can easily narrow down your requests to those that returned an error response code (that is, any error code in the range **4xx**). After you configure the dimensions that you're interested in, place your cursor into the **Filter requests** field and select the **HTTP response code** filter type (you can start typing to narrow down the suggestions). Then select the **4xx** criteria and wait for data processing to complete.

### Find POST HTTP requests

You have two options for viewing your POST (or any other HTTP method) at a glance: (1) set the HTTP method dimension or (2) filter the request by HTTP method.

#### Dimension

In this case you'll see all your requests grouped by HTTP method and by any other dimension you provide. Just specify `{HTTP-Method}` in the **Split by dimension** field.

#### Filter

In this case, all non-POST requests are filtered out, so you can focus your analysis. Just specify the `HTTP method` and select `POST` value in the **Filter requests** field.

## Related topics

* [Service metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics/service-metrics "Manage calculated service metrics via the Dynatrace configuration API.")