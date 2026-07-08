---
title: Digital Experience Monitoring (DEM units)
source: https://docs.dynatrace.com/managed/license/classic-licensing/digital-experience-monitoring-units
---

# Digital Experience Monitoring (DEM units)

# Digital Experience Monitoring (DEM units)

* 7-min read
* Published Mar 30, 2021

In addition to the [application and infrastructure monitoring](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") provided by OneAgent, you may also require Dynatrace Synthetic Monitoring, Real User Monitoring, and Session Replay.
These capabilities are consumed based on Digital Experience Monitoring units, otherwise known as DEM units.

## DEM units

The amount of DEM units you need depends on how many Synthetic monitors you want to run and how many user sessions you need to monitor.
The table below explains the rate at which DEM units are consumed per each capability type and unit of measure.

| Unit of measure | Capability | Consumption per unit of measure |
| --- | --- | --- |
| Synthetic action | Browser monitors, browser clickpaths | 1.0 DEM |
| Synthetic request | HTTP monitor | 0.1 DEM |
| User session per application[1](#fn-1-1-def), [2](#fn-1-2-def) | Real User Monitoring (Without Session Replay playback) | 0.25 DEM |
| User session per application[1](#fn-1-1-def), [2](#fn-1-2-def) | Real User Monitoring session captured with Session Replay | 1.0 DEM |
| Session property[3](#fn-1-3-def) | Real User Monitoring | 0.01 DEM |
| Action property[3](#fn-1-3-def) | Real User Monitoring | 0.01 DEM |
| Third-party synthetic result | Third-party synthetic API ingestion | 0.1 DEM |

1

User sessions are charged per application, even if a session spans multiple applications from the same domain.
Only user sessions from real users are counted in your consumption of user sessions.
User sessions from synthetic users and "robots" aren't counted when calculating your monitoring consumption.

2

Once a user session has about 200 user actions, a new session is created and all subsequent user actions are included in the new user session. There is no extra charge for additional user sessions that Dynatrace creates following such session splits.

3

Data types for properties are weighed differently and affect billing, monitoring, as well as consumption.
Short strings (fewer than 100 characters) and numeric (long strings, double, or dates) data types are counted as one property each.
Long string data types are counted as 1 property per 100 characters.

## Real User Monitoring

A single [Real User Monitoring](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.") session (otherwise known as a "user session") is defined as a sequence of interactions between a user with a browser-based web application or a native iOS or Android mobile app within an interval and with at least two user actions.
A user action is a mouse-button click, finger tap, or app start that triggers a web request (for example, a page load or a page-view navigation).
Interactions that include only one user action are considered “bounced” and aren't counted.
A user who interacts with more than one web application or app at the same time consumes one session for each of those web applications or apps, except when the interaction is considered “bounced”.
Interactions with hybrid mobile apps, that for technical reasons include a web application and a mobile app will only be considered as a single session.

A billed session ends when the [user session ends](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."), or after 60 minutes of continuous interaction with the web application or mobile app.

If you've set up an annual RUM sessions quota, your usage will reset annually.

### Real User Monitoring DEM consumption example

Say, for example, that a user has been interacting with a web application or mobile app for four continuous hours.
From a license perspective, a session ends after 60 minutes of continuous interaction, after which a new session is resumed for the next 60 minutes.
Therefore, a four-hour session is the equivalent of four licensed sessions:

* Without Session Replay data, this session costs `4 * 0.25 = 1 DEM unit`.
* With Session Replay data, the session costs `4 * 1 = 4 DEM units`.

## Synthetic actions and requests

* A “synthetic action” is an interaction with a synthetic browser that triggers a web request that includes a page load, navigation event, or action that triggers an XHR or Fetch request:

  + Browser monitors perform a single synthetic interaction (for example, measuring the performance and availability of a single URL)
    Browser monitors consume one synthetic action per execution.

    XHR or Fetch requests that aren't directly triggered by user input do not consume synthetic actions.
    (For example, they are made by a synthetic browser as the result of a user action like a page load.)
  + Clickpath monitors are sequences of pre-recorded synthetic actions.
    Clickpath monitors consume one synthetic action per each interaction that triggers a web request.

    Scroll downs, keystrokes, or clicks that don't trigger web requests aren't counted as actions.
* A "synthetic request" consists of one or multiple HTTP(S) requests (for example, GET, POST, HEAD requests).
  Each request executed by an HTTP(S) monitor consumes synthetic request.

A synthetic action/request is charged as soon as the action/request is made, no matter if it is successful or fails.
If an action/request fails and therefore subsequent actions/requests are not executed, these subsequent actions/requests will not be charged.

The following calculation gives you an estimate of the maximum possible consumption, assuming that all Synthetic actions/requests were executed.
Actual consumption may vary depending on if some actions/requests failed subsequent actions/requests were not executed.

`# Synthetic actions/requests consumed per monitor = (# Synthetic actions/requests included in monitor) × (# Executions per hour) × (# Locations) × # Hours`

### Synthetic actions/requests calculation example

For example, a recorded browser clickpath that navigates through two pages and clicks one button that triggers an XHR or Fetch request consumes three synthetic actions.
If such a synthetic monitor runs every 15 minutes from two locations for one day, the browser clickpath will consume 576 synthetic actions per day.

`3 (synthetic actions) × 4 (monitor executions per hour) × 2 (locations) × 24 (hours per day) = 576 (synthetic actions)`

For more details, see [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

## How consumption of Synthetic NAM Monitoring affects billing

Network availability monitoring (NAM) monitors don't have a separate line on the Dynatrace rate card. Instead, you're billed based on the [number of metric data points](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") generated during each execution of a NAM test. For more information, please contact your Dynatrace account manager.

Metric data point calculations

The following details apply to metric data points:

* Metric data points related to monitor and step execution are non-billable.
* Only the consumption of metrics produced at the request level affects your billing.
* Each request execution within ping tests generates 6 metric data points.

  + The number of packets used in a ping test does not impact the number of metrics produced or your billing.
  + The number of packets does not affect the price.
* Each request execution within TCP/DNS tests generates 3 metric data points.
* The price stays the same regardless of whether you create several tests containing a single request, or you create one test with numerous requests for the same set of hosts or devices.

## Digital Experience Monitoring overages Optional

If you've arranged for Digital Experience Monitoring overages (meaning, your account allows you to exceed the maximum limit of DEM units), the units you consume as overage are counted just as with regular DEM unit consumption.
Each additional overage session or synthetic test increases the amount of DEM units consumed by your account.
To add or remove overages from your account, [contact Dynatrace Sales﻿](https://www.dynatrace.com/contact/).

## Free tier of action and session properties

You can gain more information from a session or user action by configuring additional defined properties.
We currently offer a free tier of 20 defined properties per application.
As shown in the table, the DEM unit cost per session increases by 0.01 DEM units for each additional defined property.

For example, 100 sessions with 25 defined properties consume `100 * (25 - 20) * 0.01 = 5 DEM units` for additional defined properties.
The total DEM unit cost in this case is 30 DEM units.

`5 DEM units (additional defined properties) + 25 DEM units (100 sessions; 1 session = 0.25 DEM units) = 30 DEM units`

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)
* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")