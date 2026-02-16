---
title: Anomaly Detection status types
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types
scraped: 2026-02-16T21:26:53.359318
---

# Anomaly Detection status types

# Anomaly Detection status types

* Latest Dynatrace
* Explanation
* 3-min read
* Published Jan 20, 2025

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** provides a **Status** column that represents the health status of the custom alert and contains information about the success rate of custom alert executions that ran in the background over the last 24 hours. This means that, if an error or warning occurs, the custom alert will send a warning or error event. These events are then compared to the success events from the last 24 hours.

The status of the custom alert can change from warning to error if success rate falls under 95% over time.

In addition, the **Status** column contains information about the inaccessibility of the success rate data that can be divided into three types:

* **Pending**. This status indicates that the custom alert has not been executed yet, or that the query doesn't have any executable events.
* **Unavailable**. This status indicates that you might not have the permissions necessary to access the status information.
* **Inactive**. This status indicates that the custom alert is currently disabled.

## Anomaly Detection status list

A custom alert can have any of the following status types:

Status

Description

**Success**

The success rate for the last 24 hours is over 99%.

**Error**

The success rate for the last 24 hours is under 95%.

**Warning**

The success rate for the last 24 hours is between 95% and 99%.

**Unavailable**

Status currently unavailable. Check if you have the following permissions:

* `storage:system:read`

**Pending**

Can't calculate the success rate. The custom alert has not yet been executed, or the query does not contain any execution events.

**Inactive**

The custom alert is not enabled.

## Troubleshooting

If the status of your custom alert shows an error, select  **Error** > **View more details** to see the error message.

Some of the error messages might be more complicated than others. Here are some of the common ones to help you resolve the issue faster.

* `Query failed because the response time exceeded 10000 ms`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** sets a 10-second execution limit on queries. This safety limit helps to prevent other custom alert configurations from being delayed or stuck in the queue.

* `Anomaly detector failed with an unauthorized request. Fix the required permissions in the authorization settings`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** lacks the necessary permissions and is unable to read the data on your behalf. For more information about required permissions and editing authorization settings, see [Prerequisites](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#prerequisites "Explore anomaly detection configurations using the Anomaly Detection app.") and [Enable or edit Anomaly Detection authorization settings](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#edit-authorization-settings "Explore anomaly detection configurations using the Anomaly Detection app.").
* `Query does not result in a valid timeseries: No valid time series records found. A valid time series record contains a single duration field, a single timeframe and one or multiple numeric arrays. Consider using the 'timeseries' or 'makeTimeseries' DQL command`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** requires a timeseries to automatically check the alert condition. For more information and examples of a valid query, see [Examples of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** on Grail](/docs/dynatrace-intelligence/use-cases/anomaly-detection-examples "Use the power of Grail and DQL to convert any data into time series for anomaly detection analyzers.").

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Examples of anomaly detection on Grail](/docs/dynatrace-intelligence/use-cases/anomaly-detection-examples "Use the power of Grail and DQL to convert any data into time series for anomaly detection analyzers.")