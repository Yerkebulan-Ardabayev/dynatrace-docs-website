---
title: Waterfall analysis in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis
---

# Waterfall analysis in RUM Classic

# Waterfall analysis in RUM Classic

* How-to guide
* 7-min read
* Updated on Jan 24, 2023

Dynatrace captures user experience and performance data by monitoring individual user actions. Typically a user action begins with a click on an HTML control (for example, a button or link). The browser then loads the requested data, either by navigating to a new page or via an XHR/fetch call. JavaScript callbacks are then executed, the DOM tree is built or changed, and the web application is then once again ready for a new user action. Dynatrace **Waterfall analysis** view is the perfect tool for analyzing all such user action monitoring data in detail.

To access waterfall analysis for a user action

1. Go to **Web**.
2. Select the application that provides the user action you want to analyze.
3. Scroll down to the **Top 3 user actions section** of the application page.
4. Select a user action (or select **View full details** to access additional user actions).
5. On the **User action** page, select **View analysis in waterfall chart** to open **Waterfall analysis**.

## Data displayed in waterfall view

Waterfall analysis view is primarily built around W3C [timings](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates."). The view organizes the waterfall entries into three sections:

**Document requests** – Displays all content that is identified as the page load of the user action. This includes the initial HTML, as well as any other content that’s displayed in frames. Each entry contains the details that are captured by W3C navigation timings.

**XHR requests** – Displays all resources that were sent via XHR or fetch(). These entries contain all the details that are accessible through the W3C resource timings, in addition to the JavaScript callback execution time.

**Resources** – Displays all W3C timing details for all resources.

A user action may contain more than a single page load or XHR. Therefore, the initial request is highlighted in purple. The [timings](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") of the initial request are displayed as vertical event lines above the chart.

![Waterfall analysis](https://dt-cdn.net/images/img1-1982-cbef2f00ad.png)

Waterfall analysis

## Top findings

[Top findings](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/visually-complete-top-findings "Lean how to leverage Visually complete top findings provided in the waterfall analysis.") for waterfalls help you understand the above-the-fold user experience of your real users. Initial page loads drive the first impressions of new visitors to your web application. Further, top findings provide an easy way of understanding which web requests impact [key performance metrics](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics#kpm "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") and are therefore potential candidates for optimization.

For each user action viewed in **Waterfall analysis**, the following top findings are automatically identified and presented (see example below):

* Uncompressed text resources
* Resources larger than 100 kB
* Resources that have a browser cache rate less than 50%[1](#fn-1-1-def)
* Slow first-party, third-party, or CDN resources (> 200 ms)
* Contacted third party and CDN domains
* First-party, third-party, and CDN resources

1

To decide whether a resource was probably cached or not, we make use of the following indicator documented in the [W3C specification﻿](https://www.w3.org/TR/resource-timing-2/): "It is possible for transferSize value to be lower than encodedBodySize: when a cached response is successfully revalidated the transferSize reports the size of the response HTTP headers incurred during the revalidation, and encodedBodySize reports the size of the previously retrieved payload body."

In the example below, an uncompressed text resource has been detected. By selecting this finding tile, the affected resource is automatically highlighted below in the **Resources** list.

![Waterfall analysis](https://dt-cdn.net/images/findings1-1903-2355501843.png)

Waterfall analysis

## Aggregated view

While with the browser developer tools you always have to look at single executions, the Dynatrace aggregated waterfall allows you to get a collective view of multiple executions of the same user actions from various real users. These aggregations are calculated from the user action executions within the analysis timeframe and are bucketized into 3 aggregated waterfalls; You can select between the aggregated waterfall view displaying the slowest 10%, the fastest 10% and +-5% of the median. This helps you identify requests and patterns that relate to either high or low performance.

### Rarely occurring resources

To keep the aggregated **Waterfall analysis** view down to a reasonable and readable size, resources that occur in less than 30% of user action instances are moved to a **Rarely occurring** resource group. You can expand this group to view the rarely occurring resources. Note all the detail that’s returned in the roll-over highlight pane.

![Waterfall analysis](https://dt-cdn.net/images/img4-2000-f3ae2eef35.png)

Waterfall analysis

## Single instance view

While automated findings are a great way to get started with waterfall analysis of user actions and to discover ways of improving the customer experience of your application, sometimes you need to be able to dig deeper into the performance data of your user actions.

While the aggregated information is helpful for gaining an overview of user action processing steps and resource usage, it’s sometimes necessary to analyze individual instances of specific user actions to understand the impact of certain browsers, geolocations, or other variables. Therefore, it’s possible to view waterfall analysis of individual user-action instances. Individual user action instances are listed on the **Instances of this action** tab.

### Filter user action instances

You can filter and sort user action instances based on various criteria. Note in the example below that instances of the user action Loading of page /orange.jsf are filtered based on **Browser family**, **User type**, **Action duration**, and **Country**.

![User actions](https://dt-cdn.net/images/user-action-instances-2540-87530149fd.png)

User actions

### Analyze individual user action instances

You can select any user action instance you want to analyze. In the example below, the same user action from above is analyzed. The image below shows the waterfall analysis of just the selected instance of this user action, including:

* Resource details and timings
* User action properties and their values
* Effective connection type and network downlink, which are captured from the browser's [NetworkInformation API﻿](https://developer.mozilla.org/en-US/docs/Web/API/NetworkInformation).

![Waterfall analysis](https://dt-cdn.net/images/instances-31-1901-fe481fcceb.png)

Waterfall analysis

### End-to-end visibility and drilldown to distributed traces

A top finding called **Traces** is available when you use the **Waterfall analysis** view to analyze the performance of a single user action instance for which [distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") are available. The example below shows that `52 Traces` related to the selected user action instance are available for analysis. Select the **Traces** tile to get a link to the list of associated distributed traces. The top findings also highlight all resource entries in the waterfall analysis chart for which distributed traces are available.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-1-2000-30253b2468.png)

Waterfall analysis

Note the following limitations:

* End-to-end visibility requires a OneAgent instance running on the server side. You can only see the top findings when distributed traces are actually available.
* For processes that are under heavy load, Dynatrace OneAgent automatically adjusts how much data is sent to Dynatrace Server. Therefore, certain distributed traces may not be captured due to [Adaptive Traffic Management](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").
* The distributed traces for cross-origin XHR calls are not available in the waterfall analysis out-of-the-box. To make them available, implement one of the approaches described in [Link cross-origin XHR user actions and their distributed traces in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.").
* Dynatrace evaluates different factors to correlate waterfall resources (based on W3C resource timings) and distributed traces (captured by OneAgent). One factor is the URL. If parts of the URL aren’t identical on the client and server sides, for example, due to rewrite rules, the **View trace** button might not be displayed. In such cases, select the **Traces** tile shown in the top findings to get to all your distributed traces.

## Application settings influencing waterfall analysis

Using the application settings, you can configure the thresholds for the top findings while via the global settings, you can define resource types and URL cleanup rules.

### Configure waterfall finding thresholds

To configure waterfall finding thresholds

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Capturing** > **Advanced setup**.
5. Adjust the required thresholds under **Waterfall finding thresholds**.

### Define resource type

In Waterfall analysis view, you can group resources based on their type. Since the MIME type isn’t accessible from JavaScript, the resource type is determined based on the file extension. If certain resources don’t have a proper extension, you can configure URL matching rules to define those resource types.

To set up a URL matching rule for definition of a resource type

1. Go to **Settings**.
2. Select **Web and mobile monitoring** > **Resource types**.

![Waterfall analysis](https://dt-cdn.net/images/img3-2000-ba4f2dd61f.png)

Waterfall analysis

### Define URL cleanup rules

In the aggregated **Waterfall analysis** view, resources are aggregated based on their URLs. Often, IDs and other random numbers prevent resources from being correctly aggregated. When this happens, some important resources may unintentionally appear in the **Rarely occurring** resources list.

To define a URL cleanup rule

1. Go to **Settings** > **Web and mobile monitoring** > **Resource URL cleanup rules**.
2. Define [regular expressions](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to remove the IDs.

![Waterfall analysis](https://dt-cdn.net/images/img5-1976-f40ef20ba3.png)

Waterfall analysis