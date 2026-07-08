---
title: Self-monitoring for the Dynatrace GCP integration
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp
---

# Self-monitoring for the Dynatrace GCP integration

# Self-monitoring for the Dynatrace GCP integration

* How-to guide
* 4-min read
* Published Jul 16, 2021

Self-monitoring allows quick diagnosis to determine if a self-monitoring function is properly processing and sending logs to Dynatrace

## Enable self-monitoring

Follow the steps below according to your deployment scenario.

### Enable self-monitoring for the GKE deployment

1. Connect to the Kubernetes cluster where the GCP Monitor deployment is running.
2. Edit the configmap.

   ```
   kubectl -n dynatrace edit configmaps dynatrace-gcp-monitor-config
   ```
3. Change the value of the `SELF_MONITORING_ENABLED` parameter to `true`.
4. Restart the GKE GCP Monitor.

   ```
   kubectl -n dynatrace rollout restart deployment dynatrace-gcp-monitor
   ```

### Enable self-monitoring for the GCP Monitor deployment

1. In the Google Cloud console, go to **Cloud Functions**.
2. Select **dynatrace-gcp-monitor**.
3. Select **Edit**.
4. Under **Runtime, build and connection settings**, change the value of the `SELF_MONITORING_ENABLED` runtime environment variable to `true`.
5. Select **Next**, and then select **Deploy** to apply the new settings.

## Self-monitoring metrics

The Dynatrace GCP Monitor deployment reports self-monitoring metrics as Google Cloud metrics. See below the list of self-monitoring metrics for metric/log ingest.

### Self-monitoring metrics for the GKE deployment

**Metric ingestion**

| Metric | Description |
| --- | --- |
| MINT lines ingested | The number of data points (metrics with dimensions) ingested by Dynatrace Metrics API v2 in a given interval. |
| Dynatrace connectivity | The connectivity status (`1` = **OK**) between the monitoring function and Dynatrace. Connectivity can be broken due to an incorrect Dynatrace URL, an incorrect API token, or network connectivity issues. |
| Dynatrace failed requests count | The number of requests rejected by Dynatrace Metrics API v2. The reason for failure can be that the data point value doesn't comply with the [metric ingestion protocol syntax﻿](https://dt-url.net/0903q6o), or that the [limit for metric ingestion is exceeded﻿](https://dt-url.net/fx03vuq). |
| Dynatrace requests count | The number of requests sent to Dynatrace. |

**Log ingestion**

| Metric | Description |
| --- | --- |
| All requests | All requests sent to Dynatrace |
| Dynatrace connectivity failures | The number of failed requests to connect to Dynatrace |
| Too old records | The number of log records that were invalid because the timestamp was too old |
| Too long content size | The number of records with content exceeding the maximum content length |
| Parsing errors | The number of errors that occurred while parsing logs |
| Processing time | The total amount of time for processing logs |
| Sending time | The total amount of time for sending logs |
| Sent logs entries | The number of log entries sent to Dynatrace |
| Log ingest payload size | The size of the log payload sent to Dynatrace (in KB) |

### Self-monitoring metrics for the GCP Monitor deployment

**Metric ingestion**

| Metric | Description |
| --- | --- |
| MINT lines ingested | The number of data points (metrics with dimensions) ingested by Dynatrace Metrics API v2 in a given interval. |
| Dynatrace connectivity | The connectivity status (`1` = **OK**) between the monitoring function and Dynatrace. Connectivity can be broken due to an incorrect Dynatrace URL, an incorrect API token, or network connectivity issues. |
| Dynatrace failed requests count | The number of requests rejected by Dynatrace Metrics API v2. The reason for failure can be that the data point value doesn't comply with the [metric ingestion protocol syntax﻿](https://dt-url.net/0903q6o), or that the [limit for metric ingestion is exceeded﻿](https://dt-url.net/fx03vuq). |
| Dynatrace requests count | The number of requests sent to Dynatrace. |

## View self-monitoring metrics

The self-monitoring dashboards present multiple metrics related to Dynatrace connectivity status, the amount of data processed, and execution times.

To view the dashboards with self-monitoring metrics

1. In your GCP console, go to the GCP Monitoring service.
2. Select **Dashboards**.
3. Depending on the type of deployment selected, search for

   * The `dynatrace-gcp-monitor log self monitoring` dashboard (for logs)
   * The `dynatrace-gcp-monitor self monitoring` dashboard (for metrics)

Example dashboard:

![Self monitor](https://dt-cdn.net/images/self-monitoring-1343-1ba18f72fc.png)

Self monitor

## Related topics

* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")