---
title: Page load waterfall
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/experience-vitals/waterfall
scraped: 2026-02-16T21:30:19.977255
---

# Page load waterfall

# Page load waterfall

* Latest Dynatrace
* Reference
* 7-min read
* Published Jan 14, 2025

The page load waterfall in ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** provides powerful visualization and analysis capabilities for understanding web application performance at the [page instance](/docs/observe/digital-experience/new-rum-experience/web-frontends/concepts/pages-views-and-navigations#pages-and-page-instances "Understand how pages, views, and navigations are defined for web frontends the New RUM Experience.") level. This feature helps you analyze individual page loads, identify performance bottlenecks, and optimize the user experience by examining resource loading patterns and timing metrics.

![Example page load waterfall](https://dt-cdn.net/images/rum-page-load-waterfall-1915-f8def7fc9c.png)

## Access waterfall analysis

To access the page load waterfall

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**.
2. Select a web frontend in the **Explorer** view and select **Analyze performance**, or directly select a frontend in the **Performance** view.
3. Navigate to the **Pages** section and drill down into a specific page.
4. Select  **Perform waterfall analysis**.

## Page load instances table

The **Page load instances** table displays a list of individual page loads captured during the selected timeframe containing some metadata, counts, and metrics.

Available columns:

* Start time: The timestamp when the page load began
* Country
* Browser and browser version
* Errors: The number of errors encountered during the whole page instance (not only the page load)
* Long tasks: The count of long tasks that may have blocked the main thread during the whole page instance (not only the page load)
* Core Web Vitals and W3C navigation timings of the page

## Waterfall visualization

When you select a page load instance, the waterfall panel opens. In the waterfall you see each individual request of the page load instance with its type, name, timings, metadata, and the Gantt chart with the instance timing metric annotations and individual phases.

Clicking on any request in the waterfall reveals detailed information about the request and further drill down options. When hovering over the gantt chart entries you see the phase details.

Use cases

Drill-downs

### Identify slow resources

Use the waterfall to identify resources that are taking too long to load:

* Sort page instances by duration or specific metrics like TTFB or LCP
* Select instances with poor performance
* Examine the waterfall to find the resources contributing to slow load times
* Look for resources with long response times or render-blocking behavior

### Compare performance across conditions

Filter page load instances by:

* **Browser type and version**: Identify browser-specific performance issues
* **Geographic location**: Understand performance variations by region
* **Error conditions**: Compare successful loads with failed loads
* **Time periods**: Analyze performance trends over time

* **Session details**: Open the full session in the add-on provided by ![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions") **Users & Sessions** to see the page load in the context of the entire user journey.
* **Request trace linking**: Access detailed trace information for server-side performance analysis in the ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**.
* **Error analysis**: For failed requests you can dig deeper in the ![Error Inspector](https://dt-cdn.net/images/error-inspector-256-c849b18430.png "Error Inspector") **Error Inspector**.
* **Resource ready-mades**: For individual requests you can drill down into a provided ready-made dashboard. This enables you to dig deeper into single resources.
* **Query**: Open the waterfall query in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** for advanced queries and custom analysis using DQL.