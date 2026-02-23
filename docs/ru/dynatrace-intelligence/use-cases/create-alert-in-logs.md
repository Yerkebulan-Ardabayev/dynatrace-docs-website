---
title: Create log alerts for a log event or summary of log data
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/create-alert-in-logs
scraped: 2026-02-23T21:32:29.197240
---

# Create log alerts for a log event or summary of log data

# Create log alerts for a log event or summary of log data

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Jan 28, 2026

One of the uses of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** is to alert users of abnormal behavior. For example, using the `makeTimeseries` DQL command, you can set up a custom alert to analyze or alert on various data such as business events or logs. In this case, the custom alert queries the raw data every minute. However, if you have infrequent log entries, or if you're interested in a specific log event, you can use alternative solutions that are more cost- and time-effective.

In this tutorial, you will learn how to

* Create a log alert for a specific log event.
* Create a log alert for a specific time period.

## Prerequisites

* Access to a Dynatrace SaaS environment
* Installed ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**

For the [Create a log alert on a summary of log data using DQL](#create-log-custom-alert-with-dql) use case, you will also need the following:

* [Configured ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** permissions](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")

## Raise a log alert based on a specific log event

If you want to monitor a specific log event and be notified when it occurs, you can create an alert based on a filtered query to avoid processing the entire raw log.

Let's assume you want to set an alert that notifies you every time NGINX logs containing the `Connection refused` error is captured. In addition, you want to extract the following information from the log content to get a quick overview of the event:

* Error number
* Client IP address
* `http_request` line that results in an error.

To save time and effort, you can set a log alert instead of an anomaly detection alert. In this case, you don't have to make a timeseries. Instead, you just need to create a filtered query that will show only the specific event, for example:

```
fetch logs



| filter matchesValue(process.technology, "nginx")



| filter matchesValue(loglevel, "ERROR")



| filter matchesPhrase(content, "Connection refused")



| fields timestamp,content, process.technology



| parse content, "LD '[error] ' INT:error_number '#' INT LD 'Connection refused' LD 'client:' SPACE? IPADDR:client_ip LD 'request:' SPACE? DQS:http_request"



| sort timestamp desc
```

Creating a log alert doesn't require you to have access to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**. You only need **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events"). To learn more about creating alerts through **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events"), see [Set up a log alert](/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events "How to create and configure Davis problems and alerts with events based on logs.").

## Raise a log alert on a summary of log data over a time period

If you want to get an overview of the log data over a specific period, for example, if the data has infrequent log entries, you can use one of the approaches:

* Create a dedicated log metric.
* Use DQL to create a log alert on a summary of log data.

### Create a dedicated log metric

Creating a dedicated log metric allows you to reuse the log metric across apps like **Dashboards** ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") and **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") and create alerts without incurring additional costs.

To learn how to create log metrics, see [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.").

Suppose you created a log metric, `log.conn_refused_count`, which collects every log entry with a `Connection refused` error.

![An example of the Analyze and alert settings for a log metric graph, with anomaly detection selected, in the Notebooks app.](https://dt-cdn.net/images/notebooks-log-metric-analyze-and-alert-1741-740d26f404.png)

Since the data in the log metric contains only the necessary logs, you can create the alert using the regular `timeseries` DQL command and the name of your log metric as a parameter.

### Create a log alert on a summary of log data using DQL

Using DQL allows you to create complex queries and apply multiple filters and sorting conditions. This approach gives you more control on what data you want to capture and what kind of information you want to see in your alerts.

To create a log alert on a summary of log data

1. Open **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Select  **Notebook** >  **New section** >  **DQL** to create a new section.
3. Fill out the field similar to the example below:

   ```
   fetch logs



   | filter dt.system.bucket == "{your bucket name}"



   | filter matchesPhrase(content, "Connection refused")



   | makeTimeseries count(), interval:1m
   ```
4. Optional Select  **Run** to test and ensure that your command works properly.
5. Select  **Options** and select  **Analyze and alert**.
6. Turn on the Dynatrace Intelligence data analyzer if it's not active.
7. Select the required analyzer and configure it. For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.").
8. Select **Run analysis**.
9. Once you're satisfied with the result, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** and select **Anomaly Detection**.  
   This action takes you to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
10. Expand **Create an event template** and configure the event triggered by the configuration. For details, see [Event template](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#event-template "How to set up an alert for missing measurements.").
11. Select **Create**.

![An example of the Analyze and alert settings for a bucket log metric graph, with anomaly detection selected, in the Notebooks app.](https://dt-cdn.net/images/notebooks-bucket-log-metric-analyze-and-alert-1744-cef4fa6326.png)

Extracting data from the `default_logs` bucket might induce additional costs. If your logs are available in a specific bucket, we recommend using `filter dt.system.bucket == "{your bucket}"` to increase efficiency.

If you don't have access to your team's or department's bucket, you can create a private one following the [bucket assignment](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.") documentation.

## Conclusion

Apart from standard Anomaly Detection alerts, Dynatrace offers other solutions, such as:

* Creating a log alert for a specific event.
* Creating an alert of log data over a period of time.

If you followed these steps, now you know how to create log alerts for specific events and a summary of the log data over a period of time.

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [[Video] Elevating Security with Anomaly Detectionï»¿](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Video] Anomaly Detection and Data Observabilityï»¿](https://www.youtube.com/watch?v=HPQi63mQg3w)