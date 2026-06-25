---
title: Visually complete top findings
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings
scraped: 2026-05-12T11:34:57.375404
---

# Visually complete top findings

# Visually complete top findings

* Overview
* 2-min read
* Published Jul 05, 2019

Dynatrace has made it easy for you and your web performance-optimization engineers to access Visually complete metric findings for each page-load that is captured with Dynatrace Real User Monitoring. Visually complete measurements are easy to understandâthey measure the amount of time it takes for the visible portion of a web application to fully render on your end-usersâ device screens. Analyzing the Visually complete user experience metric helps you understand what can be done to improve your applicationâs end usersâ above-the-fold experience. Optimizing your application for Visually complete, however, requires an in-depth understanding of web-page loading behavior. This is where Dynatrace [Waterfall analysis](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") is indispensable.

## Visually complete findings

The **Visually complete** top findings tile helps you focus your waterfall analysis on those page resources that impact the above-the-fold user experience. It also gives you a quick indication as to whether or not any performance thresholds have been breached. On top you get the last DOM element (and a DOM-element identifier) impacting Visually complete timing for the waterfall captured on a given real device and display size. As you can see from the image below, CSS files and JavaScript files are not highlighted as impacting resources as this canât be determined for sure. When youâre optimizing the above-the-fold area, you have to take a look at these resources as well as they can visibly change DOM elements that aren't bound to a resource request. In the example below, a simple SPAN tag, not a resource, is causing the final trigger for Visually complete.

As you can see in the example below, top findings may also include warnings. Two warnings are displayed in this example. Explanations of these two finding types are detailed below the image.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-with-visually-complete-top-finding-1968-796ce96ee6.png)

Waterfall analysis

## Top finding #1: Visually complete (Apdex and Key performance metric violation)

The first warning is driven by the threshold youâve set for your applicationâs [key performance metric](/managed/observe/digital-experience/rum-concepts/user-action-metrics#kpm "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") and [Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."). You can [change this setting](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") by navigating to the settings of this monitored application (see example below). Changing the threshold directly impacts not only the top findings but also the Apdex score calculation for the application across all Dynatrace views, including the [World map](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), [application overview](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page."), and elsewhere.

![Waterfall analysis](https://dt-cdn.net/images/application-apdex-settings-2019-e830c18ed8.png)

Waterfall analysis

## Top finding #2: Speed index exceeds a percentage of Visually complete timing

The second threshold is related to the [Speed index and Visually complete metrics](/managed/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.") and how they relate to each other. Visually complete indicates when the area above-the-fold is fully rendered, whereas Speed index helps you to understand how quickly the largest areas of the screen are loading. The larger the difference between Speed index and Visually complete timing the better. To provide you with an easy indicator, Dynatrace warns you if Speed index is 50% or more of Visually complete. You can change this threshold as your performance improves and you need tighter restrictions.