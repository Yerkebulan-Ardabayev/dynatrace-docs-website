---
title: Context-specific drill-down
source: https://docs.dynatrace.com/managed/observe/application-observability/services-classic/context-specific-drill-down
scraped: 2026-05-12T11:21:53.053239
---

# Context-specific drill-down

# Context-specific drill-down

* Reference
* 4-min read
* Published Nov 13, 2018

Context-specific drill-down menus simplify navigation and filtering of results presented on Dynatrace service-analysis views. You can quickly slice through vast amounts of data in just a few clicks.

## Table-based layouts

Table-based layouts have this set of buttons on the right-hand side of each table row: ![Chart](https://dt-cdn.net/images/blue-chart-icon-4c5e910a12.svg "Chart") ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More")

### Context-sensitive filters

![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") Context-specific filters are available on nearly all service analysis pages that feature table-based layouts.

Selecting the filter button of a specific service instance in the service instance table filters the entire page to show only the results of that specific service instance. Have a look at the example service **Details** page below. Selecting the filter button of a specific **service instance** in the service instance table will filter the entire page to show only the results of that specific service instance.

![Context specific filter](https://dt-cdn.net/images/context-specific-filter-2994-197bdffd08.png)

Context specific filter

Similarly, selecting the filter button of a specific request attribute on the **Request attributes** tab filters the entire page to show only those results that relate to the selected request attribute.

### Create context-sensitive charts

![Chart](https://dt-cdn.net/images/blue-chart-icon-4c5e910a12.svg "Chart") Context-specific chart creation is available on nearly all service analysis pages that feature table-based layouts.

Select any row's chart button to create a chart based on the contents of the selected row. This simplifies the process of creating charts based on custom metrics or request attributes.

![Context specific charts](https://dt-cdn.net/images/context-specific-charts-2994-7b2cccd651.png)

Context specific charts

The following chart represents the response time of a `Custom Frontend` service instance. This can also be done on the **CPU** tab to display the total CPU time of an instance.

![Response time in context specific charts](https://dt-cdn.net/images/context-specific-charts-3012-2c8eaa171b.png)

Response time in context specific charts

### Context-sensitive drill-down menus

![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") The **Analyze** menus, available for results on all table-based service analysis pages, reveal all possible drill-downs and analysis options based on the current context.

Take a look to the expanded **Analyze** menu below. In this example we see options for context-sensitive analysis based on **Method hotspots**, **Outliers**, **Distributed traces**, **Response time hotspots**, **Service backtrace**, **Comparison**, **Service flow**, and **Top web requests**.

![Analyze menu](https://dt-cdn.net/images/analyze-menu-3026-03d65e04ae.png)

Analyze menu

In the example above, we've selected the `Customer Frontend` service in the **Incoming requests to this service** section and the `orange-booking-payment.jsf` request in the **Requests from** section. This drill-down combination focuses the analysis on all `orange-booking-payment.jsf` requests of the `Customer Frontend` service that call the `easyTravel-Business` database via other tree services. Additionally, filters applied via **Filter requests** are carried over to any analysis option you select from the **Analyze** menu.

## Multi-dimensional analysis

The context-specific menu for [multi-dimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.") enables you to perform context-sensitive analysis based on individual time series metrics included in your charts. This menu includes all the filtering functionality that's available on the service-analysis pages, along with advanced capabilities for charting and splitting based on multiple dimensions.

## Service flow

While **Service flow** doesn't include tables, you can still access context-sensitive drill-down menus from this view: ![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces") ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") or ![Database statements](https://dt-cdn.net/images/database-statements-icon-62baf10731.svg "Database statements") ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More")

Select any service in the service flow and you'll now see a hovering drill-down menu.

![Service flow context-specific drill-down](https://dt-cdn.net/images/service-flow-context-specific-options-3036-4afddf7a92.png)

Service flow context-specific drill-down

### Context-sensitive PurePathÂ® distributed traces

![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces") Context-specific distributed traces are available for all non-database services.

Select **Distributed traces** to view the **Distributed traces** page filtered to display only those distributed traces that trigger the depicted service flow (`easyTravel Customer Frontend` in the example below) and subsequently call the selected service (`Credit Card Verification` in the example below).

![Distributed traces from service flow](https://dt-cdn.net/images/distributed-traces-2976-2399031360.png)

Distributed traces from service flow

### Context-sensitive database statements

![Database statements](https://dt-cdn.net/images/database-statements-icon-62baf10731.svg "Database statements") Context-specific database statements are available for most of database services.

Select **Top database statements** to view the **Top database statements** page, filtered to display only those statements in the database (``` DB1`` at the picture below) executed by calls, originating in service, that triggered Service flow ( ```easyTravel Customer Frontend` at the picture below).

![ Access top database statatement from service flow](https://dt-cdn.net/images/top-database-statatement-button-3088-1104748825.png)

Access top database statatement from service flow

### Context-sensitive filters

![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") Context-specific filters are available for all services.

They filter service flow to calls originating in the service that triggered the service flow and subsequently called the selected serviceâjust like the **Filter service flow** button in the top tile of the [side pane](/managed/observe/application-observability/services-classic/service-flow/service-flow-metrics#side-pane "Learn about the service flow metrics that measure the performance of the service calls that are triggered by each service request in your environment.").

### Context-sensitive drill-down menus

![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") The **Analyze** menus, available for all services, reveal all possible drill-downs and analysis options based on the currently selected service.

## Related topics

* [Distributed Traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* [Service flow](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Multidimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")