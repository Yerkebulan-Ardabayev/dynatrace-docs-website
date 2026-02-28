---
title: User action metrics
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-action-metrics
scraped: 2026-02-28T21:15:19.128347
---

# User action metrics

# User action metrics

* Explanation
* 8-min read
* Updated on Mar 20, 2023

For web applications, Dynatrace calculates a host of [user action](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") metrics.

Core web vitals

The following metrics are core web vitals and are available only for load actions:

* **Largest contentful paint**
* **Cumulative layout shift**
* **First input delay**

## Milestone metrics

Milestone metrics represent events that occur at a specific point in time during a user action. However, these metrics are measured in seconds or milliseconds because they are calculated relative to the user action start time. In other words, user action start time serves as a reference point from which the time for the milestone metrics is measured. For example, a value of 47 ms for **Navigation start** indicates that this event occurred 47 ms after the action start time.

1

**Speed index** and **Visually complete** are only available on browsers that support [mutation observersï»¿](https://developers.google.com/web/updates/2012/02/Detect-DOM-changes-with-Mutation-Observers): Microsoft Internet Explorer 11, Microsoft Edge 15+, Firefox 57+, and Google Chrome 61+.

2

**First paint** is supported on all browsers except Internet Explorer.

3

**First contentful paint** is available only for [Chromium-based browsersï»¿](https://www.chromium.org/Home).

4

**Largest contentful paint** is available for Chromium-based browsers. Measured using [Google-provided APIsï»¿](https://web.dev/lcp/#measure-lcp-in-javascript).

5

For Chromium-based browsers, **First input delay** is measured using [Google-provided APIsï»¿](https://web.dev/fid/#measure-fid-in-javascript). For Firefox, Safari, and Internet Explorer 9+, the metric is measured using a Dynatrace implementation that listens for events of type `click`, `mousedown`, `keydown`, or `touchstart` and calculates the delay from when the RUM JavaScript registers such events to when the events are triggered.

## Phase metrics

As opposed to milestone metrics, phase metrics imply a duration.

1

You can use the **Long tasks** metric instead of the [**Total blocking time**ï»¿](https://web.dev/tbt/) metric, which we decided not to introduce due to certain technical limitations. Also note that the **Blocking** metric shown in the waterfall isn't related to **Total blocking time** and is only available for specific requests.

## Key performance metrics

From the metrics listed above, Dynatrace has specified some as key metrics. Key performance metrics enable you to select the ideal user experience metric for each of your applications. These key metrics provide you with valuable performance insights that promote success in your digital business. The key performance metrics include:

* User action duration
* Visually complete
* Speed index
* DOM interactive
* Load event end
* Load event start

* HTML downloaded / Response end
* Time to first byte
* Largest contentful paint
* Cumulative layout shift[1](#fn-3-1-def)
* First input delay (RUM web only)

1

**Cumulative layout shift** is the score measuring the unexpected shifting of visible webpage elements. It is available for [Chromium-based browsersï»¿](https://www.chromium.org/Home) and measured using [Google-provided APIsï»¿](https://web.dev/cls/#measure-cls-in-javascript).

Dynatrace allows you to [choose the right performance metric for each application condition](/docs/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.").

## Missing metric measurements

Metric measurements might be missing in the following cases:

#### Visually complete

* During a load action, the user selects another link that triggers a new load action before the original page load event is completed. The second load action interrupts the **Visually complete** calculation of the first load action, so no measurement is available.  
  In the earlier version of **Visually complete**, Dynatrace used the user action duration as a fallback measurement. This skewed the timeseries, so such cases are now excluded to ensure more accurate aggregates.
* A late redirect is triggered immediately following a load action.
* The [Visually complete time-out](/docs/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics#config-enhanced-vc "Learn how to use 'Visually complete' and 'Speed index' metrics.") is reached during the calculation.

#### Core web vitals

* The browser API doesn't trigger and provide a metric measurement before the user action ends (see the **User action duration** metric).  
  In earlier versions of Dynatrace Real User Monitoring, these values were sent after the completion of the user action. Such values were not meaningful and often not representative. For example, **First input delay (FID)** measures page load responsiveness. The primary driver for a high FID value is JavaScript execution. So if a user waited a minute following a page load before selecting a new link, most if not all JavaScript processing would already have taken place and the resulting small FID measurement wouldn't be a representative value of a true page load. Such measurements skewed the overall metric aggregate.
* The user's browser doesn't support the APIs that are used to measure core web vitals. See details under [Milestone metrics](#milestone-metrics) to learn which browsers support Core web vitals.
* The page is loaded or reloaded in an inactive tab, and the browser API does not report values.
* The browser API provides negative values.