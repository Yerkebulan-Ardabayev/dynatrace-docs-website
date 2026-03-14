---
title: Digital Experience Monitoring (DEM) overview (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/digital-experience-monitoring
scraped: 2026-03-04T21:27:41.938129
---

# Digital Experience Monitoring (DEM) overview (DPS)


* Latest Dynatrace
* Overview
* 7-min read
* Updated on May 16, 2025

Dynatrace Digital Experience Monitoring (DEM) provides availability and performance monitoring to help ensure that your applications and services are available, functional, fast, and efficient across all channels, including mobile, web, IoT, and APIs.

This page describes the different Digital Experience Monitoring capabilities and the features that they provide with a DPS subscription.

For information about how usage of a specific DEM capability translates to consumption of your DPS license commit, see

* [Real User Monitoring (RUM)](digital-experience-monitoring/real-user-monitoring.md "Learn how your consumption of the Dynatrace Real User Monitoring (RUM) DPS capability is billed and charged.")
* [Real User Monitoring with Session Replay](digital-experience-monitoring/real-user-monitoring-session-replay.md "Learn how your consumption of the Dynatrace Real User Monitoring with Session Replay DPS capability is billed and charged.")
* [Real User Monitoring Property](digital-experience-monitoring/real-user-monitoring-property.md "Learn how your consumption of the Dynatrace Real User Monitoring Property DPS capability is billed and charged.")
* [Browser Monitor or Clickpath](digital-experience-monitoring/browser-monitor-clickpath.md "Learn how your consumption of the Browser Monitor or Clickpath DPS capability is billed and charged.")
* [Third-Party Synthetic API Ingestion](digital-experience-monitoring/third-party-api.md "Learn how your consumption of the the Dynatrace Third-Party Synthetic API Integration DPS capability is billed and charged.")
* [HTTP Monitor](digital-experience-monitoring/http-monitor.md "Learn how your consumption of the Dynatrace HTTP Monitor DPS capability is billed and charged.")

## Real User Monitoring (RUM)

Dynatrace RUM is a performance monitoring process that collects detailed data about each user's interactions with your application, whether it be a browser-based application or a mobile app deployed on Android or iOS.
Real User Monitoring collects data on a variety of metrics.
For example, data collected on load actions can include navigation start, request start, and speed index metrics.

## Real User Monitoring with Session Replay

Session Replay helps capture and visually replay the complete digital experience of your end users.
User interactions with your application are recorded and can be replayed in a movie-like experience.
Session Replay makes it easy to reproduce production issues and errors, and to understand problems such as malformed pages and infinite spinners.

## Real User Monitoring Property

Dynatrace captures extensive performance information about your applications. This information can be enriched with valuable metadata and converted into user action and user session properties. These properties enable powerful queries, segmentation, and aggregations on the captured metadata.

Any RUM property can be configured for an application.

## Browser Monitor or Clickpath

A browser monitor simulates a user visiting your application using a modern, updated web browser to monitor your application's business-critical workflows.
Browser monitors can be configured to run from any Dynatrace public or private locations at frequencies of up to every five minutes and sends alerts when the application becomes inaccessible or when performance degrades significantly.
In addition, they can be used to check the availability of internal resources that are inaccessible from outside your network.

The Dynatrace recorder is used to capture an exact sequence of clicks and user inputs, availability, and performance.
Alternatively, a defined sequence can be scripted to accomplish the same goal.

## Third-Party Synthetic API Ingestion

The third-party endpoints of the Synthetic API enable the pushing of third-party synthetic data and events to Dynatrace.
The API also facilitates adjustments of results which were previously pushed to Dynatrace.

## HTTP Monitor

Synthetic HTTP monitors can be created to check the availability of resourcesâwebsites or API endpoints.
In addition, they can be used to check the availability of internal resources that are inaccessible from outside your network.

## Synthetic NAM Monitoring

Network availability monitoring (NAM) monitors don't have a separate line on the Dynatrace rate card. Instead, you're billed based on the [number of metric data points](metrics.md "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") generated during each execution of a NAM test. For more information, please contact your Dynatrace account manager.

Metric data point calculations

The following details apply to metric data points:

* Metric data points related to monitor and step execution are non-billable.
* Only the consumption of metrics produced at the request level affects your billing.
* Each request execution within ping tests generates 6 metric data points.

  + The number of packets used in a ping test does not impact the number of metrics produced or your billing.
  + The number of packets does not affect the price.
* Each request execution within TCP/DNS tests generates 3 metric data points.
* The price stays the same regardless of whether you create several tests containing a single request, or you create one test with numerous requests for the same set of hosts or devices.

## Related topics

* [Real User Monitoring](../../observe/digital-experience/rum-concepts/rum-overview.md "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Session Replay](../../observe/digital-experience/session-replay.md "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Synthetic Monitoring](../../observe/digital-experience/synthetic-monitoring.md "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [License Dynatrace](../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)