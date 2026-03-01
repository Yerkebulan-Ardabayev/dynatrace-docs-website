---
title: Performance analysis
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis
scraped: 2026-03-01T21:08:18.016037
---

# Performance analysis

# Performance analysis

* How-to guide
* 6-min read
* Published Jul 19, 2017

The **Performance analysis** section displays a number of performance metrics for your application. Just expand the **Performance analysis** section of the infographic on the [application overview page](/docs/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.") to view the performance analysis options.

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

## Working with the infographic

Each area of the infographic appearing at the top is clickable, offering access to deeper detail regarding each metric. Whenever you select a part of the infographic, the left section right below the infographic shows different data that reflect the selected part.

The left-hand portion of the performance analysis infographic shows dimensional breakdowns of your application traffic based on browser type, user type, and geographic region. In the middle, you can see the different action types, the Apdex rating and the errors section, while on the right-hand side, the resources and the services sections are displayed. The top finding for each dimension is displayed by default in each section. The discrete infographic sections are briefly described below.

Top browsers

If you select the **Top browser** section of the infographic, you see the **Browser breakdown** on the left under the infographic. This shows the traffic per desktop browser, mobile browser, [synthetic](/docs/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."), and more.

By selecting **Analyze performance** in the bottom right corner of the **Browser breakdown** section, you navigate to the [multidimensional analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."), where you can perform a multidimensional analysis from the **Browsers** perspective.

![Browsers](https://dt-cdn.net/images/browsers-2278-df044b9e0a.png)

Top user type

By selecting **Top user type**, in the **User type** section under the infographic, you can see the number of actions per minute, Load and XHR actions, and JavaScript errors of **Real users** versus **Robots** (for example, Googlebot), and [**Synthetic**](/docs/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."). The bar appearing at the top of the **User type** section, is a visual representation of this breakdown.

By selecting **Analyze performance** in the bottom right corner of the **Browser breakdown** section, you navigate to the [multidimensional analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."), where you can perform a multidimensional analysis from the **User type** perspective.

![User types](https://dt-cdn.net/images/user-types-2289-a96765e8cd.png)

Geolocation breakdown

By selecting **Geolocation breakdown** you can view the geographical locations that have the highest traffic. You can view further details on the [world map](/docs/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.") that you can access by selecting **View full world map**.

By selecting **Analyze performance** in the bottom right corner of this section, you navigate to the [multidimensional analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions."), where you can perform a multidimensional analysis from the **Geolocations** perspective.

![Geolocations](https://dt-cdn.net/images/geolocations-2335-e51f88186e.png)

Load, XHR, and custom user actions

[User actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") are divided into **Load** actions and **XHR** actions (or custom actions if available).

If you select the user actions part of the infographic, you can view the **Impact of user actions on performance**. The charts displayed show among other things, the [Visually complete](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") metric for load actions and the [Response end](/docs/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") for XHR actions.

You can also use the metric selector to display either the **Slowest 10%**, **Median**, or **Fastest 10%** of user actions.

By selecting **Analyze performance** in the bottom right corner of this section, you can [analyze your applicationâs performance and user actions across multiple dimensions](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Performance analysis](https://dt-cdn.net/images/performance-analysis-marked-2346-a63d69b1ca.png)

Apdex rating

Dynatrace relies on [Apdex ratings](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") to calculate user satisfaction with specific applications. By selecting **Apdex rating**, you can view the user satisfaction within the specified time frame.

![Apdex](https://dt-cdn.net/images/apdex-2275-4f37729a71.png)

Resources

Select **Resources** in the infographic to view details regarding the resources that your application relies on. Dynatrace uses the provider host names of downloaded resources to categorize content resources into either **3rd party resources**, **CDN resources**, or **1st party resources**. You can examine the action duration by resource type and also compare it to a previous time frame.

In the **1st party resources** tab, you can also look for trends in your internal resourcesâ**Scripts**, **Images**, and **CSS** resources are tracked and reported separately.

From this section, you can also navigate to the [provider detection settings](/docs/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.") where you can manually add a provider.

![Resources](https://dt-cdn.net/images/resources-2279-8542dfb13e.png)

Services

Select the **Services** portion of the infographic to view the services that support your application in the **Called services** section. If you select **View service flow** at the bottom right corner of this section, you can [view the sequence of service calls that are triggered by each service](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment."). Dynatrace allows you to [access the service flow for an application as well as a user action](/docs/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Learn how to access service flows for applications and user actions.").

![Services](https://dt-cdn.net/images/services-2255-23e1ba2133.png)

### Application availability

If you have one or more [synthetic monitors](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.") set up to test the availability of your application, you can see the availability of your application directly on the application overview page within the **Availability** section. The availability chart shows you an aggregate view of all of the selected application's synthetic monitors. You can select **View full details** to view details related to outages and navigate directly to synthetic monitor details (your [analysis timeframe](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") settings will remain intact) to perform further analysis.

![Availability](https://dt-cdn.net/images/availability-2274-52399f442d.png)

## Composite metrics across response times



This section helps you figure out from a high level perspective where your performance focus should lie. You can identify, for example, whether the duration up to the time to first byte is an issue for your application or you should focus on user perceived loading performance, indicated by Speed index and Visually complete.

If you select **Analyze performance** in the bottom right corner of this section, you can [analyze your applicationâs performance and user actions across multiple dimensions](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Composite metrics](https://dt-cdn.net/images/metrics-2309-defde297c9.png)

## Top 3 included domains

At a glance, you can see the **Top 3 included domains**, which are the domains that contain the largest number of actions that have been automatically detected by [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") in your environment. You can select **View full details** to view more details on the traffic coming from these domains and to [define new applications](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

![Domains](https://dt-cdn.net/images/domains-2296-117bbe4967.png)

## Problems

The [Problems](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") section indicates problems that have been automatically detected by Davis, the Dynatrace AI engine. Just select a problem to learn further details.

![Problems](https://dt-cdn.net/images/problems-2300-47780cd400.png)

## Top errors

The **Top errors** list displays the most frequently occurring [errors](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") by error type: **JavaScript**, **Request**, or **Custom**. You can [configure errors](/docs/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.") by type or individually.

To view **Top errors**

1. Go to **Web**.
2. Select the application that you want to analyze and scroll down to **Top errors**.

![Top errors infographic](https://dt-cdn.net/images/top-errors-921-5efd41aa51.png)

## Top 3 user actions

The **Top 3 user actions** list shows you the three slowest user actions. Actions are sorted based on **priority** (high priority actions are listed first) and **total time consumed** (duration multiplied by number of actions). The **total time consumed** measure is valuable because it factors in how frequently an action is called. For example, a slow action that is called often has more significant impact on performance than a slow action that isn't called often.

If you select a user action, you'll be directed to the [user action overview page](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions "Understand how you can access user action detail pages and analyze user actions.") where you can further analyze the specific user action.

If you select **View full details** in the bottom right corner of the section, you can [analyze your applicationâs performance and user actions across multiple dimensions](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![User actions](https://dt-cdn.net/images/user-actions-2260-8e1d88bb09.png)

## Events

Events represent system incidents that might be of interest to you. Such events include errors, new version deployments of your application, configuration changes, and more. The events shown in the image below were generated because the [maximum number of user actions per minute was exceededï»¿](https://dt-url.net/h92389d).

![Events](https://dt-cdn.net/images/image-2240-9cc2b49e51.png)