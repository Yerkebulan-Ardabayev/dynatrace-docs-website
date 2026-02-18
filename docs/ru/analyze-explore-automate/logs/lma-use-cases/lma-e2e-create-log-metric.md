---
title: Create log metric
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-create-log-metric
scraped: 2026-02-18T21:19:36.591495
---

# Create log metric

# Create log metric

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Apr 24, 2023

Dynatrace Log Management and Analytics gives you the ability not only to view and analyze logs but also to create metrics based on log data and use them throughout Dynatrace like any other metric. You can add them to your dashboard, include them in an analysis, and even create custom alerts.

## Create connections refused metric

You need to count how many refused connections are recorded in your log data. For that, filter the correct logs and turn the number of occurrences into a log metric. By tracking the metric, you can track possible firewall, network connectivity or server configuration issues.

### Build DQL query

To build and run your query:

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. On the **Logs and events** page, turn on **Advanced mode**.
3. Select ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **copy** for the code sample below.

   ```
   fetch logs



   | filter matchesPhrase(content, "Connection refused")



   | sort timestamp desc
   ```
4. Paste the query into the query edit box and select **Run query**.

This query performs the following actions:

* Retrieves logs with the `Connection refused` phrase found in the log content.
* Sorts the result in descending order according to the timestamp.

### Create metric

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Key**, append the metric name to the `log.` metric key: `log.conn_refused_count`.
3. Add **Matcher**.  
   Use the [DQL function](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher#lp-dql-matchesPhrase "Examine specific DQL functions and logical operators for log processing.") for matching phrases, which is part of the [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesPhrase(content, "Connection refused")
   ```

   This filters the log data containing the phrase `Connection refused`.
4. For the **Metric measurement** option, select **Occurrence of log records**.  
   The metric represents the count of occurrences of log records that contain the `Connection refused` phrase.
5. Select **Save changes** to create the log metric.

### View metric

To view the result in Data Explorer

1. Go to **Data Explorer**.
2. Select the `log.conn_refused_count` log key.
3. Select **Run query**.

## Create log attribute metric

You need to monitor an attribute of your logs, and you need to keep an eye on the error levels reported in your logs from your K8s cluster. Find the correct logs from Grail, and use the filters to create a new metric for these. Add log status (error/warning/info) to your metric, which makes it easy to track these with metrics.

### Build DQL query

To build and run your query

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. On the **Logs and events** page, turn on **Advanced mode**.
3. Select ![Copy to clipboard](https://dt-cdn.net/images/dashboards-app-tile-copy-to-clipboard-e49e92a96b.svg "Copy to clipboard") **Copy** for the code sample below.

   ```
   fetch logs



   | filter matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")



   | summarize count(), by:status
   ```
4. Paste the query into the query edit box and select **Run query**.

This query performs the following actions:

* Retrieves log records with the `dt.entity.kubernetes_cluster` attribute containing the `KUBERNETES_CLUSTER-92233333` phrase in the log content.
* Counts the number of such log records and orders them by their status attribute.

### Create metric

1. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
2. In **Key**, append the metric name to the `log.` metric key: `K8-92233333`.
3. Add **Matcher**.  
   Use the [DQL function](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-matcher#lp-dql-matchesPhrase "Examine specific DQL functions and logical operators for log processing.") for matching phrases, which is part of the [Dynatrace Query Language (DQL)](#matchesPhrase):

   ```
   matchesValue(dt.entity.kubernetes_cluster, "KUBERNETES_CLUSTER-92233333")
   ```
4. For the **Metric measurement** option, select **Occurrence of log records**.  
   The metric represents the count of occurrences of log records that contain the phrase `KUBERNETES_CLUSTER-92233333`.
5. Add a dimension `status`.
6. Select **Save changes** to create the log metric.

### View metric

To view the result in Data Explorer

1. Go to **Data Explorer**.
2. Select the `log.K8-92233333` log key and, in the **Split by**, add `status`.
3. Select **Run query**.