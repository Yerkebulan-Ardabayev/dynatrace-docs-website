---
title: Analyze individual user actions
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions
scraped: 2026-02-22T21:17:11.868751
---

# Analyze individual user actions

# Analyze individual user actions

* How-to guide
* 3-min read
* Published Jul 19, 2017

User action detail pages provide quick access to all relevant user-action data, giving you all the information you need to understand what contributes to the performance of each of your user actions.

To access user action detail pages

1. Go to **Web**.
2. Select an application.
3. Scroll down to the **Top user actions** section, and select **View full details**.
4. Select an action listed under **Key user actions** or **Top 100 user actions**.

Depending on which user action you want to analyze, you can alternatively directly select in the **Top user actions** section one of the actions shown there.

Once on a user action detail page, select areas of the infographic at the top of the page to navigate to the corresponding section on the page related to each summary metric, or type a string into the **Filter user types** field to view real-user or synthetic-monitoring specific data.

![Action details 1](https://dt-cdn.net/images/32-actiondetails-1-1423-b88f87bd5b.png)

![Action details 2](https://dt-cdn.net/images/33-actiondetails-2-1423-f9e6a23325.png)

## Performance

In the **Performance section**, you can view the impact of user activity on performance, check out the various [performance contributors](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") and see the distribution for your selected performance metric.

![Performance](https://dt-cdn.net/images/performance-2285-289d4f850e.png)

## Contributors breakdown chart and waterfall analysis

When it comes to analyzing user actions, one of the main questions to address is on which tier is the most response time consumed? Was more time spent on the frontend (mainly in the browser), the network, or the server? The **Contributor breakdown** chart gives you a quick overview of time spent on the frontend, the network, and the server. For complete [waterfall analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") of individual user actions, select **View analysis in waterfall chart** to see which resources impact the action duration.

![User actions](https://dt-cdn.net/images/actions-2285-9af9ca267d.png)

## Apdex rating

Dynatrace relies on [Apdex ratings](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") to calculate user satisfaction. By selecting **Apdex rating**, you can view the user satisfaction within the specified time frame for the specific user action.

![Apdex](https://dt-cdn.net/images/apdex-actions-2291-8bcf39ab96.png)

## Loaded resources

The **Loaded resources** section provides an overview of downloaded resource categories and their impact on the action duration.

![Loaded resources](https://dt-cdn.net/images/loaded-resources-2251-3786b5042a.png)

## User action properties

This section lists the user action properties that [you've defined for the specific user action](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). By selecting one property, you can view the data that have been captured via this property.

![User action properties](https://dt-cdn.net/images/properties-2284-38c4617813.png)

## Problems

The [**Problems**](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") section indicates problems that have been automatically detected by Davis, which is the Dynatrace AI-driven root-causation engine. Just select on a problem to learn further details.

![Problems](https://dt-cdn.net/images/problems-actions-2259-a04f530ffa.png)

## Errors

Select **Errors** to view [error](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") analysis from two different dimensions: error type ([JavaScript](/docs/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors."), request, and custom errors) and origin (first-party, third-party, or CDN).

You can also view the most frequently occurring JavaScript errors in this user action during the specific [timeframe](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings."). Select **Analyze errors** to navigate to the [multidimensional analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."), where you can perform a multidimensional analysis from the **Errors** perspective, combined with the type, context, or origin dimension respectively. On this page, if you select a specific error from the **Error** list, you can access the [error details page](/docs/observe/digital-experience/session-segmentation/new-user-sessions#error-details-page "Learn about user session segmentation and filtering attributes.").

![User action details page - Errors](https://dt-cdn.net/images/user-action-page-error-2283-670dd35d85.png)

## Top segments

This section includes a breakdown of **Browsers**, **Users**, and **Geolocations** and shows metrics for these dimensions for the specific user action.

![Segments](https://dt-cdn.net/images/segments-2249-32b57f8e1b.png)

## Top 3 web request contributors

This sections shows the **Top 3 web request contributors**, which are the three server-side services that consumed the highest total time. Select **View full details** to view the full list of web request contributors.

![User action contributors](https://dt-cdn.net/images/contributors-2261-af12bd0f24.png)

## Compare JavaScript errors with user actions

This section shows the percentage of the user actions that were affected by JavaScript errors during the specified [timeframe](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

![Javascript errors vs actions](https://dt-cdn.net/images/js-errors-2253-a4fad35c29.png)