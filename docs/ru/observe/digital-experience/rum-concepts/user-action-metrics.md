---
title: User action metrics
source: https://www.dynatrace.com/docs/observe/digital-experience/rum-concepts/user-action-metrics
scraped: 2026-02-23T21:22:24.175994
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

Metric

Description

Applicable to

**Navigation start**

The moment when the user agent finishes prompting to unload the previous page  
If there is no previous page, this value is the same as `PerformanceTiming.fetchStart`.

Load actions

**Request start**

The time before the user agent sends the request to obtain the page from the server, relevant application caches, or a local resource  
If the transport layer fails and the connection is reopened, this metric is set to the time corresponding to the new request.

Load actions

XHR actions

**Time to first byte**

The time taken until the first byte of the response is received from the server, relevant application caches, or a local resource

Load actions

XHR actions

**HTML downloaded**

The time taken until the user agent receives the last byte of the response or the transport connection is closed, whichever comes first  
For XHR actions, this metric is known as **Response end**.

Load actions

XHR actions

**DOM interactive**

The time taken until the page's status is set to "interactive" and it's ready to receive input

Load actions

**Speed index**[1](#fn-1-1-def)

The score measuring how quickly the visible parts of the page are rendered

Load actions

**DOM content loaded**

The time taken until the user agent fires the `DOMContentLoaded` event at the page  
The `DOMContentLoaded` event is executed when the basic HTML of the page is loaded and its parsing is complete. The event doesn't wait for the loading of add-ons (for example, stylesheets, sub-frames, and images) to be complete.

Load actions

**First paint**[2](#fn-1-2-def)

The time taken to render the first non-default background element

Load actions

**First contentful paint**[3](#fn-1-3-def)

The time taken to render the first bit of content, such as text or images

Load actions

**Largest contentful paint**[4](#fn-1-4-def)

The time taken to render the largest element in the viewport

Load actions

**Visually complete**[1](#fn-1-1-def)

The time taken to fully render content in the viewport

Load actions

XHR actions

**DOM complete**

The time taken until the page's status is set to "complete"

Load actions

**Load event start**

The time taken to begin the load event of the page

Load actions

**Load event end**

The time taken to complete the load event of the page

Load actions

**User action duration**

The time taken to complete the page load  
This includes load time of XHR requests initiated before `loadEventEnd` and load time of dynamic resources and script executions triggered by DOM modifications.

Load actions

XHR actions

Custom actions

**First input start**

The moment when the user first interacts with a page, for example, clicks a UI control

Load actions

**First input delay**[5](#fn-1-5-def)

The time from the first interaction with the page to when the user agent can respond to that interaction

Load actions

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

Metric

Description

Applicable to

**Blocking**

The time between when the user agent receives a request to download a resource and when it actually starts downloading the resource  
This includes the time spent on waiting for a free TCP socket, generating disk cache entries, and proxy negotiation.

Load actions

**Application cache**

The time spent checking any relevant application caches  
This includes the time before the connection to the server is established.

Load actions

**DNS lookup**

The time taken to resolve the hostname for a target URL

Load actions

**TCP connect**

The time taken to establish a TCP connection to the server (including SSL)

Load actions

**Secure connect**

The time taken to secure the connection established to the server  
This includes the SSL handshake and SOCKS.

Load actions

**Request**

The time taken to request the page from the server until the first byte is received

Load actions

**Response**

The time taken to receive the response

Load actions

**Processing**

The time between DOM loading and Load event start

Load actions

**OnLoad**

The time taken to process the load event

Load actions

**OnDOMContentLoaded**

The time taken to execute `onDomContentLoaded` handlers

Load actions

**Callback**

The time taken to execute XHR callbacks

Load actions

**Redirect time**

The time taken to follow any HTTP redirects

Load actions

**Long tasks**[1](#fn-2-1-def)

The total time of all long JavaScript tasks (over 50 ms)  
The metric is measured from **Navigation start** for the entire user action duration.

Load actions

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