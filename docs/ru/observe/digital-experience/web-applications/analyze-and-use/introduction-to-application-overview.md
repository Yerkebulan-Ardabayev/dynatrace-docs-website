---
title: Introduction to application overview page
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview
scraped: 2026-02-18T21:25:14.739680
---

# Introduction to application overview page

# Introduction to application overview page

* Explanation
* 2-min read
* Published Jul 11, 2019

The application overview page, which is organized into meaningful and intuitive sections, allows you to perform a thorough analysis of both the performance of your application as well as the user behavior.

To access the application overview page

1. Go to **Web**.
2. Select an application.

## Filtering

You can perform your analysis based on a specific dimension selected from the filter at the top of the application overview page. If you choose **User type** for example, you can specify whether you want to perform your analysis based on data gathered from **Synthetic**, **Real users**, or **Robots**.

## Tags and JavaScript frameworks

Right beneath the name of your application, you can view the assigned [tags](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") and [JavaScript frameworks](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions."), which are displayed within the expandable **Tags and JavaScript frameworks** area. It's easy to add new tags hereâjust select **Add tag**. There's also a **Framework settings** button that takes you to the settings related to [JavaScript frameworks](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

## Performance analysis

The [**Performance analysis** section](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.") displays a number of performance metrics for your application. To view the sections pertaining to performance analysis, expand the **Performance analysis** part of the infographic.

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

## User behavior

The [**User behavior** section](/docs/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Understand the user behavior analysis options that are provided by Dynatrace.") displays a number of user behavior metrics for your application. To view the sections related to user behavior, expand the **User behavior** part of the infographic.

![User behavior](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

## Analyze user sessions

Select **Analyze user sessions** in the upper-right corner to thoroughly [analyze a user session from different dimensions](/docs/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

## Pin to dashboard

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

Select **Pin to dashboard** in the upper-right corner to add a tile for performance or user behavior analysis (based on which part has been expanded) to the classic dashboard of your preference for a quick analysis view. For details, see [Pin tiles to your dashboard](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Application settings

Select **More** (**â¦**) in the upper-right corner of the page, and then select **Edit** to access the application settings.

## Top findings

To access the [Hyperlyzer](/docs/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions."), select **More** (**â¦**) > **Show top findings**. Here you can see top findings regarding where your users are located, what browser version they're using, their operating system, and the user actions the application has received, sorted by action duration in a descending order (the slowest actions are regarded top findings, as these are the problematic ones that need to capture your attention).

## Smartscape view

To access [Smartscape view](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment."), select **More** (**â¦**) > **Smartscape view**. Smartscape offers a quick but at the same time detailed overview of all the topological dependencies of your application.