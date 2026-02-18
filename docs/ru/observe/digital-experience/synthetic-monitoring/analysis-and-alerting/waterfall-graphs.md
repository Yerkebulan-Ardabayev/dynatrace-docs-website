---
title: Waterfall graphs
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs
scraped: 2026-02-16T09:29:02.985102
---

# Waterfall graphs

# Waterfall graphs

* Explanation
* 11-min read
* Updated on Feb 26, 2024

Sometimes it's necessary to analyze individual browser monitor executions to understand the impact of certain locations, local CDN partners, or other variables. Waterfall analysis is a great tool for viewing detailed information about the various resources that comprise a specific load or XHR action in an execution.

A waterfall graph is a graphical display of every request and resource downloaded for an action, which can be an entire page load (load action) or the update of a specific in-page context without navigating to a new URL (XHR action). Resource- and page-level analysis is based on [W3C timings](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.").

Waterfall graphs are available on the Synthetic [**Multidimensional analysis** page](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Learn how to analyze browser-monitor data points.") for every [action](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Find out how many actions are consumed by a browser clickpath and how they differ from events.") in events with timings in browser monitor [executions](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#data-points "Learn how to analyze browser-monitor data points.") (both single URL and clickpaths).

Used in conjunction with the [scatter plot](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Learn how to analyze browser-monitor data points.") and filters on the **Multidimensional analysis** page, waterfall graphs can help you narrow down the specific resources in specific executions that are causing failures or performance violations. [Top findings](#findings) for each waterfall abstract waterfall data into accessible and actionable information.

The images below show waterfall graphs for a load and XHR action respectively.

![Load action waterfall](https://dt-cdn.net/images/waterfallloadaction1-1205-086b74aa33.png)

![XHR action waterfall](https://dt-cdn.net/images/waterfallxhraction1-1274-efc6bcbdc0.png)

Failed executions can have waterfall graphs for constituent actions up to the point when the monitor failed. Depending on the event in which failure occurs and the error type, you can find waterfall graphs even for monitors with 0% availability, and, consequently, no monitor-level performance data.

## Understand the data in waterfall graphs

The initial entry in a waterfall graph (**Loading of page** in a load action or a URL in an XHR action) shows the overall **user action duration**. The user action duration is also represented by the vertical timing line **A**.

See [Troubleshoot MV3-related issues in browser monitors](#troubleshoot-mv3) for information on the impact of transitioning the Synthetic Recorder (a Chrome browser extension) to Manifest Version 3, which is the latest iteration of the Chrome extension platform.

Hover over the entry to see additional information on the **Number of resources** downloaded or distinct **URLs** contacted. (Check [findings](#findings) for the number of first- and third-party resources.)

![First entry in a load action waterfall](https://dt-cdn.net/images/waterfallloadactionloadingofpage-1112-882a1717d2.png)

![First entry in an XHR action waterfall](https://dt-cdn.net/images/waterfallxhractionfirstentry-1174-cd6dcb60a3.png)

The waterfall graph organizes its main entries into three categories, [Document requests](#document-requests), [XHR requests](#xhr-requests), and [Resource requests](#resources). Hover over a request or resource to see the full URL.

### Document requests

For load actions, which load the entire page, this section lists the base page and any content displayed in frames. The initial request, usually the base page, is highlighted in purple. For XHR actions, this section generally shows document requests in iframes.

Base page timings are the basis of the page-level vertical timing lines displayed on the chart. For example, the start of base page load time marks the W3C Navigation start metric (the vertical timing line **N**). Load actions have a different set of [page-level timing events](#filters) compared to XHR actions.

If there's a redirect in place for the page you navigate to, the document request and resources for the page you are redirected to are shown.

Hover over the entry to see a breakdown of its load time into components. The Processing, OnDOMContentLoaded, and OnLoad components are only applicable to the base page.

Dynatrace Synthetic Monitoring includes processing time in its waterfall display and calculation. Processing time, which is time spent in JavaScript execution or simply browser overhead, is represented by the gap between the end of one resource and the start of another. Processing time is shown as a component of base page load time.

![Base page](https://dt-cdn.net/images/waterfallloadactionbasepage1-1406-9cc7f0b23f.png)

### XHR requests

Load actions as well as XHR actions can contain XHR/fetch calls, or resource requests that do not result in a complete page load. An example of generating XHRs is typing into a form field and seeing autocomplete suggestions that change dynamically as you type.

The initial XHR in an XHR action is highlighted in purple, and its timings are displayed as page-level timings in vertical lines. XHR actions have a different set of [page-level timing events](#filters) compared to load actions.

XHR entries display W3C resource timings as well as any JavaScript callback timesâin the Callback component. The Callback component is only applicable to XHRs.

![Component timings for an XHR](https://dt-cdn.net/images/waterfallxhractioninitialcomponenttimings-586-2be36bf9a7.png)

### Resource requests

Resources are listed in the order requested and indented to show the offset from the start of page navigation when each was called. Check the [top-most entry](#waterfall-data) in a waterfall graph to view the total number of resources downloaded; check [findings](#findings) to view the breakdown by first and third parties.

Each resource's download time and its components are shown in relation to that of other resources and in the context of overall page-level W3C timings. Hover over a resource to see timing details.

Resources can be [grouped and filtered](#filters).

Failed resources are marked in red. Hover over the resource for an explanation. Note that a failed resource does not necessarily result in action or monitor failure.

![Failed resource request](https://dt-cdn.net/images/waterfallfailedresource1-589-cca3366f7a.png)

If you have blocked requests to specified domains/URLs/resource types in [monitor settings](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors#advanced-setup "Learn about configuring browser monitors and clickpaths."), resources from such domains are shown without detailed timings.

![Blocked request](https://dt-cdn.net/images/waterfallblockedrequest-628-61d68bd691.png)

You can plot the performance (**HTML downloaded** / **Response end**) of any request, including document and XHR requests, across data points in the [scatter plot](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Learn how to analyze browser-monitor data points.") by selecting **Analyze over time**.

![Analyze a request over time](https://dt-cdn.net/images/scatterplotanalyzeovertime-1619-07e12cf69a.png)

## Findings

Davis, the Dynatrace AI causation engine, automatically detects top findings for each waterfall. Findings are key statistics and tips that capture how resources can impact page-level W3C timings of the initial request of an actionâthe base page in the case of load actions or the initial XHR in the case of XHR actions. Initial requests drive the first impressions of new visitors. Top findings are tools that help you identify which resources can be optimized, such as the resources impacting Visually complete (the user's above-the-fold experience), uncompressed text resources, large resources, or slow CDN resources.

Select **Show all findings** to expand the list of findings above a waterfall. Select a finding to highlight the associated resources in the waterfall graph.

![Top findings expanded](https://dt-cdn.net/images/waterfalltopfinding-1196-54e42a27e5.png)

The **Visually complete** finding compares the action timing to any configured threshold and highlights any images that impact the metric. (Thresholds and timeouts can be configured in browser monitor settings: **Advanced setup** > **Enable custom RUM JavaScript settings** > **Configure parameters for Visually complete and Speed index calculation**.)

![Visually complete finding](https://dt-cdn.net/images/waterfallvcfinding-650-f2d19da580.png)

Another finding highlights uncompressed text resources; if an uncompressed text resource is larger than 860 bytes, the hover data on compression is highlighted in red. This threshold may be configurableâ[see below](#finding-thresholds).

![Uncompressed resource](https://dt-cdn.net/images/waterfalluncompressedresource-586-e65284b928.png)

### Thresholds for waterfall findings



If Real User Monitoring (RUM) is enabled for the web applications your browser monitor runs against, you can specify thresholds for waterfall findings in application settings.

You can also find default values for findings here. For example, you can determine how to peg **Speed index** to **Visually complete** or how large is too large when it comes to being warned about the size of resources.

To configure waterfall finding thresholds

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Advanced setup**.
5. Adjust the required thresholds under **Waterfall finding thresholds**.

### PurePathÂ® distributed traces for visibility into application infrastructure

The **Traces** finding is displayed when your browser monitor runs against a web application with a [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") instance installed on the server side and that has the relevant server-side monitoring. The finding displays the linked service calls. If the monitor is associated with a web application that doesn't have the relevant server-side monitoring, the **Traces** finding is not displayed, as there are no underlying monitored services.

PurePathÂ® technology traces a web request through your application infrastructure so you can see what is driving performance behind the scenes at the application level. If you see that one or two requests are taking the majority of the time on a slow page, you can drill into the distributed trace to see, for example, if there are too many database requests or just one slow request. You can then use this information to drive performance improvements or error analysis.

When you select the finding, the associated requests and resources are highlighted in the waterfall. You can select the link provided in the top finding to access all available distributed traces or hover over an individual request to drill into a specific distributed trace. You'll probably want to analyze distributed traces for your [dynamic requests](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology."), ([document requests](#document-requests), or [XHRs](#xhr-requests)) rather than individual resources. In the image below, hovering over the document request displays the **View trace** link for that request.

![Traces top finding and single request Purepath trace](https://dt-cdn.net/images/waterfalltracesfinding-1121-556a6c6eed.png)

In the **Distributed traces** list view, select a resource/request and drill down to view **Trace**.

![Traces accessed from Synthetic waterfall](https://dt-cdn.net/images/tracesfromwaterfall-1491-340c596da0.png)

* For processes that are under heavy load, Dynatrace OneAgent automatically adjusts the data sent. Therefore, certain distributed traces may not be available. In such cases, you'll see a message about [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.") in the **Traces** finding.

* Drilling down from an individual resource (based on W3C resource timings) to a distributed trace (captured by OneAgent) is enabled by comparing URLs. If there are any rewrite rules or if parts of the URL arenât identical on the client and server sides, the **View trace** button for the resource wonât be displayed. In such cases, you can get to all your distributed traces from the **Traces** finding.

## JavaScript errors

You can analyze the details of JavaScript errors that are detected during the execution of load or XHR actions. JavaScript errors appear as red vertical markers in the waterfall graph at the point they occurred during the execution. Click a marker to analyze the details of that error. JavaScript errors do not lead to monitor failure, and monitor failure is not directly attributable to any JavaScript errors.

![Waterfall JavaScript error](https://dt-cdn.net/images/waterfalljserror-1198-234304aad2.jpg)

When you filter the [scatter plot](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#scatter-plot "Learn how to analyze browser-monitor data points.") for JavaScript errors, you can click any data point to automatically select the event and load the waterfall where a JavaScript error occurs.

The Error details page for each detected JavaScript error includes a complete stack trace that identifies the exact line of code responsible for the error. This insight can dramatically accelerate the time it takes to resolve such errors.

![JavaScript error details](https://dt-cdn.net/images/jserrordetails-1680-b4b1d8ef5d.jpg)

## Grouping, filters, and legend

Grouping and filtering tools help you focus on the waterfall requests that matter to you. You can combine grouping and filtering controls.

**Grouping by domain** organizes resources into first-party, third-party, and CDN domains. You can see the load order and timing details for specific domains.

**Grouping by type** allows you to see the main categories of first-party, third-party, and CDN resourcesâimage, script (JavaScript), CSS, and others.

![Group resources by type](https://dt-cdn.net/images/waterfallgroupbytype1-1206-c6a1a11b85.png)

Note that the group-level timings represent the end-to-end timings for loading the resources of a given type/domain; these timings are not additive, in that individual resource times do not add up to group-level timings, as resources can be loaded concurrently.

Filters allow you to focus on resources that most impact your user experience. You can view the full waterfall, or **Focus on** just those resources up until significant browser events such as DOM interactive or Visually complete.

![Filter resources by browser event](https://dt-cdn.net/images/waterfallfilterbyevent1-1203-ad6b72b76f.png)

The legend at the bottom of the waterfall lists the following with detailed descriptions below:

* W3C page-level metrics
* JavaScript errors
* Resource timing components

Select any of these to exclude/include them from the waterfall graph. The images below show the browser events and resource timing components available for load actions and XHR actions, respectively.

![Legend for load actions](https://dt-cdn.net/images/legend1loadactionwaterfall-1112-ee3b169f08.png)

![Legend for XHR actions](https://dt-cdn.net/images/legendxhractionwaterfall1-1225-a7c2e4c4e0.png)

## Troubleshooting MV3-related issues in browser monitors

The Dynatrace Synthetic Recorder, which is a Google Chrome browser extension, is transitioning to Manifest Version 3 (MV3), which is the latest iteration of the Chrome extension platform. As a result of this required transition, there are changes in the operation of the Synthetic Recorder that might require workarounds in your browser monitor configurations or application code.

Check out the following articles in the [Troubleshooting forum in the Dynatrace Communityï»¿](https://dt-url.net/dy122xtf).

* [Missing XHR actions for third-party iframesï»¿](https://dt-url.net/2zg2xr6)
* [Unable to block specific requests owing to limitations on the length of regular expressionsï»¿](https://dt-url.net/w0i2xhk)
* [`window.dispatchEvent` and `window.addEventListener` functions in application codeï»¿](https://dt-url.net/1ck2xb1)
* [401 failures on challenge-response pagesï»¿](https://dt-url.net/62m2x72)