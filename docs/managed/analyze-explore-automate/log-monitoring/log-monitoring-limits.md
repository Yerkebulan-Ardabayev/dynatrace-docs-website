---
title: Log Monitoring default limits (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits
---

# Log Monitoring default limits (Logs Classic)

# Log Monitoring default limits (Logs Classic)

* 1-min read
* Updated on Mar 04, 2026

Log Monitoring Classic

This page lists default limits for the latest version of Dynatrace Log Monitoring.

The current limitations apply to both log file ingestion and generic log ingestion via API.

## Log ingestion limits

The table below summarizes the most important default limits related to log ingest. All presented limits refer to UTF-8 encoded data.

| Type | Limit | Description |
| --- | --- | --- |
| Content | 8 kB | The maximum size of log entry body |
| Attribute key | 100 bytes | The key of an attribute value |
| Attribute value length | 250 bytes | The maximum length of an attribute value |
| Number of log attributes | 50 | The maximum number of attributes a log can contain |
| Log events per minute | 1k/minute per cluster by default | The maximum number of log events in a minute |
| Log age | 24 hours | The maximum age of log entries when ingested |
| Logs with future dates | No restriction[1](#fn-1-1-def) | How far into the future log entries can reach |
| Values per attribute | 32 values | The maximum number of individual values an attribute can contain |
| Request size | 10 MB | The maximum size of the payload data |
| Number of log records | 50,000 records | The maximum number of log records per request |
| Nested objects | 5 levels | The maximum number of levels ingested with nested objects |

1

There is no ingestion limitation on log entries with future timestamps, but entries with timestamps further than 10 minutes into the future have their timestamps set to the moment of ingestion.

When it comes to log events per minute, if your log data stream within your cluster exceeds the limit, all log events above the limit are ignored. If you increase the resources (RAM) in your nodes, you can increase the limit based on the cluster resource size using an API call or the Cluster Management Console (CMC).

There are two ways to refresh the cluster limit:

* Using the API call. See [Update log events per cluster for Log Monitoring](/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring "Learn how to update the total log events per cluster limit based on the cluster resources size using API.") for details.
* Refreshing the cluster limit using the Cluster Management Console (CMC):

  1. In the CMC, select **Environments** and the environment for which you wish to update the total log events per cluster.
  2. On the environment details page, in the **Cluster overload prevention settings** section, select **Refresh cluster limit**.

## Log events per minute

Log data ingestion is limited by default to 1,000 log events per minute per cluster.

* If your log data stream within your cluster exceeds the limit, all log events above the limit are ignored.
* If you increase resources (RAM) in your nodes, you can increase the limit based on the cluster resources size using an API call or Cluster Management Console (CMC).

This applies to all event sources (OneAgent and generic log ingestion). You can use self-monitoring metrics to get a count of incoming log events and log events rejected because this limit was exceeded. For details, see [Self-monitoring metrics](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#log-self-monitoring-metrics "Explore the complete list of self-monitoring Dynatrace metrics.").

**Refresh cluster limit using the API call**  
See [Update log events per cluster for Log Monitoring](/managed/dynatrace-api/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring "Learn how to update the total log events per cluster limit based on the cluster resources size using API.").

**Refresh cluster limit using Cluster Management Console (CMC)**

1. In the CMC, select **Environments** and the environment for which you wish to update the total log events per cluster.
2. On the environment details page, in the **Cluster overload prevention settings** section, select the **Refresh cluster limit**.