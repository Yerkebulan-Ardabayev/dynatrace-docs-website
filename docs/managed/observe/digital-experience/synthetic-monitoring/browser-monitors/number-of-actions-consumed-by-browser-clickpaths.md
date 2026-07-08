---
title: Number of actions consumed by browser clickpaths in Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths
---

# Number of actions consumed by browser clickpaths in Classic

# Number of actions consumed by browser clickpaths in Classic

* How-to guide
* 2-min read
* Published May 16, 2018

Dynatrace Synthetic Monitoring Classic creates a separate synthetic action for each page interaction that triggers a web request, including a page load, navigation event, or an XHR. Synthetic actions (similar to user actions for Real User Monitoring) hold the performance data that's collected during the playback of clickpath events.

To find out how many synthetic actions a specific browser clickpath consumes:

1. Go to **Synthetic Classic**.
2. Select a browser clickpath.
3. On the Synthetic details page, the **Properties** section displays the count of synthetic actions (versus events) for the clickpath.

   ![Actions on Synthetic details page](https://dt-cdn.net/images/syntheticdetailsactions-1656-e9e2013dc3.png)

   Actions on Synthetic details page

   The number of actions and events, frequency, locations, and current consumption for the selected time frame are displayed. The number of actions consumed daily for this clickpath is calculated as follows.

   `4 executions per hour (runs every 15 minutes) × 24 x 2 locations × 5 actions = 960 synthetic actions`

   On the **Synthetic events and actions** card, you can switch between viewing all events (default) or actions only (turn on **Show events with timings only**).

   ![KPM events](https://dt-cdn.net/images/kpm-events-948-247a3b2545.png)

   KPM events

When recording or editing a clickpath, you'll notice that your interaction with your web application is captured in terms of [events](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Learn about the event types created when recording a browser clickpath."). The screenshots below show events captured during [script recording](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") and in [edit mode](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.").

![Browser clickpath events during recording workflow](https://dt-cdn.net/images/clickpatheventsinitial-2150-8146d11425.png)

Browser clickpath events during recording workflow

![Clickpath events in edit mode](https://dt-cdn.net/images/recordedclickpath2-2127-04b0b07f47.png)

Clickpath events in edit mode

An event isn't the same thing as an action—only events that trigger web requests are actions, so your script might not have as many actions as events. Events such as clicking an input field or entering text into a form don't trigger network requests. These events are important from a functional perspective but don’t generate any performance data. When first [setting up a clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application."), the Summary page clearly outlines the number of events versus actions in your clickpath.

![Clickpath summary](https://dt-cdn.net/images/summaryclickpath1-1676-5c00606bdd.png)

Clickpath summary

You can access and edit your event list at any time: Select your monitor in **Synthetic Classic** > **Edit** > **Recorded clickpath**.

## Related topics

* [Real User and Synthetic Monitoring overview (DPS)](/managed/license/capabilities/real-user-synthetic-monitoring "Learn how Dynatrace Real User and Synthetic Monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Digital Experience Monitoring (DEM units)](/managed/license/classic-licensing/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.")