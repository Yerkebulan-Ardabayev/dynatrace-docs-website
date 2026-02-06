---
title: Business Flow
source: https://www.dynatrace.com/docs/observe/business-observability/business-flow
scraped: 2026-02-06T16:27:49.743295
---

# Business Flow

# Business Flow

* Latest Dynatrace
* App
* 5-min read
* Updated on Dec 05, 2025

About the app

IT teams and business owners can use ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** to monitor and analyze critical business process flows. You can track end-to-end process delays, detect process anomalies, and report business key performance indicators (KPIs).

![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** helps with diagnosing process issues and prioritizing process optimization opportunities to improve business outcomes.

Prerequisites

Required

* Define and activate business events for each process step.
* Identify a unique identifier (correlation ID) that is common to all process steps (for example, `order_id`). The name of the correlation ID may differ between steps; the value is used to connect steps into a single flow.

Recommended

* Identify business events that indicate incidents or business exceptions, such as credit card payment errors, product outages, shipping exceptions, or other non-IT process issues.
* Identify a business KPI of your choice, such as revenue, that can be extracted from a business event attribute.

## Before you begin

* A business process is structured into steps or milestones, which are interconnected through a directional flow and branching paths.
* Each step or milestone can include business events that indicate the progression of the business flow to that specific point. Additionally, these steps can encompass business events that describe errors or exceptions impacting the business process.
* Business events, whether for step definitions or exceptions, are configured based on their `event.provider` and `event.type` values. To utilize these events within ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**, the captured business events must align with these definitions.

  Example:

  Consider a business event in EasyTrade that captures the creation of a credit card order. To use this event as part of a milestone definition, such as **Create credit card order**, it is essential to define a specific `event.type` and `event.provider` for that business event. This allows the event to be selected for the **Create credit card order** step.

  Similarly, for a business exception, the `event.type` and `event.provider` must be unique to that business event, enabling its use in a step as a business exception definition.

### Permissions

The following table describes the required permissions.

Permission

Description

app-engine:functions:run

Run Business Flow calculations

storage:bizevents:read

Read business events from GRAIL

storage:buckets:read

Read system data from GRAIL

state:app-states:read

Read and share configurations in app-states

state:app-states:write

Write configurations in app-states

state:app-states:delete

Delete configurations in app-states

app-settings:objects:read

Read configurations in app-settings

app-settings:objects:write

Write configurations in app-settings

settings:objects:read

Read settings objects

settings:objects:write

Write settings objects

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

IT teams and business owners can use ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** to monitor and analyze critical business process flows. You can track end-to-end process delays, detect process anomalies, and report business key performance indicators (KPIs).

![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** helps with diagnosing process issues and prioritizing process optimization opportunities to improve business outcomes.

![The Business Flow dashboard provides a real-time view into process and business KPI health.
Errors and business exceptions are displayed for the selected step.](https://cdn.hub.central.dynatrace.com/hub/bizflow_1.26.1_mainwindow.png)![View your business flow KPIs over time and define alerts based on anomaly detection analyzers](https://cdn.hub.central.dynatrace.com/hub/bizflow_1.26.1_kpis.png)

1 of 2The Business Flow dashboard provides a real-time view into process and business KPI health.
Errors and business exceptions are displayed for the selected step.

## Overview

The **Overview** tab serves as the landing page, where you can start discovering ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** and explore a demo business flow configuration or the last one accessed in a single view.

From here, you can:

* Analyze your configured business flows. It contains all the user interface elements for analyzing your critical business processes.
* Explore the entire tree of your processes, planning and zooming in the central main area, select steps to understand the flows, and search for specific groups of flows based on filters in the right panel.
* Drill down into the top business KPIs to see them evolving over time and create alerts based on anomaly detection.

## Business flows

Use the business flows sidebar on the left to choose which configuration you want to explore.

From here, you can:

* Find business flows classified as entities and recently modified.
  Select  to duplicate or remove any existing business flow configuration.
* Collapse that sidebar to get more screen space for navigation on the tree view.

## Filter correlation IDs

On the landing page in the right panel, you can use several filtering options to focus on the matching business flows.

* Search for specific values of the correlation IDs.
* Filter by a step to find all the business flows that may have reached or are in transit/dropped to that step and by the status of the business flow.

## Investigate problems

The Problem mode enables precise analysis of any IT problem that may affect a business process.

* This mode highlights the most relevant metrics associated with the alert, focused on the appropriate timeframe.
* Additionally, it offers quick access to the underlying problem, allowing you to efficiently diagnose and resolve issues.

## Learning modules

Go through the following processes to learn using ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**:

[01Set up Business Flow

* How-to guide
* Follow the instructions on how to successfully set up Business Flow.](/docs/observe/business-observability/business-flow/set-up-business-flow)[02Business Flow Details

* Explanation
* Explore Business Flow Details.](/docs/observe/business-observability/business-flow/business-flow-details)[03Business Flow KPIs

* Explanation
* Discover how key performance indicators can help you track performance and identify improvement opportunities within the Business Flow app.](/docs/observe/business-observability/business-flow/reported-kpis)

## Capabilities

With ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**, you can

* Report business process KPIs, including flows completed (conversions), average flow completion time, business exceptions, and a business KPI of your choice.
* Visualize and analyze individual process flows from start to finish.
* Detect and explore uncompleted or dropped process flows to determine the cause, such as an IT error, a business exception, or abnormal inter-step transit time.
* Visualize process errors and business exceptions at each step.
* Define alerting on key metrics based on ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** for short duration processes.

## Limitations

* Business processes can include no more than five branches in one step.
* Each step in a business process can be defined using no more than five different business events.
* A business process can have up to 20 nodes in total. A node is defined as a step or a branch; if a step has three branches, that counts as 3 nodes.
* Each step must have at least one active business event assigned, otherwise the configuration cannot be saved.
* The difference between timestamps on events that are in different steps must be at least one millisecond, as lower resolutions on durations are not supported, or may generate false positive alerts of disordered flows during the analysis of the business process.
* Alerting on key metrics is only possible when the average duration of a business process monitored is below 30 minutes, as ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** only analyzes a 60-minute rolling window on defined metrics. See [Sliding window](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#sliding-window "How to set up an alert for missing measurements.") for more details.
* All business KPIs in ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow** are the result of running complex DQL queries thatâdepending on the amount of data scannedâcan hit the default read data limit. If you reach this limit in any of the queries, you'll be notified and offered the option to run the DQL queries limitless on that configuration (once or by default).

  The limitless mode on a configuration can be switched off in the edit mode.

  See [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language."), to learn more about data limits.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Track your business performance indicators and results, detect problematic processes, and prioritize opportunities.](https://www.dynatrace.com/hub/detail/business-flow/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [[Blog] Business Flow: Why IT operations teams should monitor business processesï»¿](https://www.dynatrace.com/news/blog/business-flow-why-it-operations-teams-should-monitor-business-processes/)