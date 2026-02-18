# Dynatrace Documentation: managed/analyze-explore-automate

Generated: 2026-02-18

Files combined: 2

---


## Source: log-monitoring.md


---
title: Log Monitoring Classic
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring
scraped: 2026-02-16T21:30:46.193948
---

# Log Monitoring Classic

# Log Monitoring Classic

* 2-min read
* Updated on Nov 20, 2025

With Log Monitoring as a part of the Dynatrace platform, you gain direct access to the log content of all your mission-critical applications, infrastructure and cloud platforms. You can create custom log metrics for smarter and faster troubleshooting. You will be able to understand log data in the context of your full stack, including real user impacts.

Log Monitoring Classic end-of-life

Log Monitoring Classic, which is available for SaaS and Managed deployments, will reach end-of-life by 2027. For details, see the [Log Monitoring Classic end-of-life](/docs/whats-new/saas/sprint-328#log-monitoring-classic-end-of-life "Release notes for Dynatrace SaaS, version 1.328") announcement in our release notes.

We recommend [upgrading to Log Management and Analytics](/docs/analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.") well in advance.

![LMC - Ingestion channel overview](https://dt-cdn.net/images/lmc-ingestion-channel-overview-2500-abfee3614c.png)

[### Ingest & Processing

Set up automatic log collection, and extract value with Log Processing.](/docs/analyze-explore-automate/log-monitoring/acquire-log-data "Learn how to acquire log data in Dynatrace Log Monitoring.")[### Analysis

Analyze significant log events across multiple logs, across parts of the environment (production), and potentially over a longer timeframe.](/docs/analyze-explore-automate/log-monitoring/analyze-log-data "Learn how to analyze log data in Dynatrace Log Monitoring.")[### Alerting

Define patterns, events, and custom log metrics to receive proactive notifications.](/docs/analyze-explore-automate/log-monitoring/alert-log-data "Create, or let Dynatrace create, alerts-based log data in Dynatrace log monitoring")[### API

Use the Dynatrace API to send log data to Dynatrace and quickly search, aggregate, or export the log content.](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

#### Configuration

[Get the latest Log Monitoring](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.")

[Tweak your setup](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration "Learn how to configure Dynatrace Log Monitoring.")

[Default limits](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.")

[Supported log data format](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format "This topic lists all the log formats supported by Log Monitoring.")

[Connect log data to traces](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.")

[Log ingest rules](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.")

[Log Monitoring FAQ](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.")

#### Log data acquisition

[Autodiscovery](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")

[Add log files manually](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Learn how to manually add log files for analysis.")

[Generic log ingestion](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")

[Cloud log forwarding](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Learn how to configure AWS, Azure and Google Cloud log forwarding to ingest logs.")

[Logs from Kubernetes](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.")

[Add log sources](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Learn how to include and exclude log sources for analysis.")

[Log processing](/docs/analyze-explore-automate/log-monitoring/log-processing "Create log processing rules that reshape your incoming log data for better analysis or further processing.")

#### Log data analysis

[Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.")

[Log events](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.")

[Log metrics](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")

[Log custom attributes](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Learn how to create and use custom attributes during log data ingestion.")

[Management zones](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")

## Related topics

* [Log monitoringï»¿](https://www.dynatrace.com/platform/log-monitoring/)
* [DDUs for Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")


---


## Source: self-monitoring-metrics.md


---
title: Self-monitoring metrics
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics
scraped: 2026-02-17T21:29:00.317715
---

# Self-monitoring metrics

# Self-monitoring metrics

* 4-min read
* Published Dec 03, 2021

Dynatrace offers a special self-monitoring category of metrics to provide observability into the operation and health of Dynatrace components and features. These metrics are available in every Dynatrace Managed and SaaS environment and can be identified by the `dsfm:` metric prefix.

To review the currently implemented self-monitoring metrics

1. Go to **Metrics**.
2. Filter the table by `dsfm:`.
3. Expand any row to review metric details.

The examples that follow show how you can use these self-monitoring metrics to get insights into the operation and health of your Dynatrace ActiveGate and Dynatrace environment over time.

## Environment insights

In this example, we use self-monitoring metrics to get insights into the operation and health of a Dynatrace environment over time.

1. Go to **Data Explorer**.
2. Check the metrics listed below.

To view the self-monitoring data use the following metrics:

* `dsfm:cluster.oneagent.agent_modules` (number of monitored hosts)  
  Data Explorer query example:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(and(eq("dt.oneagent.agent_type",os))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:sort(value(max,descending)):limit(10)
  ```
* `dsfm:cluster.oneagent.agent_modules` (number of monitored code modules)  
  Data Explorer query example:

  ```
  dsfm:cluster.oneagent.agent_modules:filter(not(or(eq("dt.oneagent.agent_type",os),eq("dt.oneagent.agent_type",log_analytics),eq("dt.oneagent.agent_type",remote_plugin)))):merge("dt.entity.apm_tenant","dt.tenant.uuid"):avg:splitBy():sum:auto:limit(10)
  ```
* `dsfm:server.service_calls.received` (number of service calls received)  
  Data Explorer query example:

  ```
  dsfm:server.service_calls.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.spans.received` (number of spans received)  
  Data Explorer query example:

  ```
  dsfm:server.spans.received:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.user_session_count` (number of user sessions)  
  Data Explorer query example:

  ```
  dsfm:server.rum.user_session_count:default(0):splitBy():sum:rate(1m)
  ```
* `dsfm:server.rum.action_count` (number of user actions)  
  Data Explorer query example:

  ```
  dsfm:server.rum.action_count:default(0):splitBy():sum:rate(1m)
  ```

### Example environment insights dashboard

You can create a Dynatrace dashboard for quick, focused access to the self-monitoring data. Create tiles by selecting the self-monitoring metrics in Data Explorer, configuring a visualization for each of them, and pinning them to your dashboards. For more information, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

The following screenshot shows a dashboard that uses the above metrics to monitor the operation of a Dynatrace environment over time.

* A steady number of monitored hosts and modules, service calls received, and user sessions/actions per minute together indicate a healthy Dynatrace environment.
* A significant drop in these metrics might indicate a problem, in which case you should contact a Dynatrace product expert via live chat to determine the root cause.

![Example of dashboard page with self-monitoring metrics.](https://dt-cdn.net/images/3dashboard-1107-58988f1958.png)

## Log and event monitoring insights

In this example, we use self-monitoring metrics to get insights into the operation of [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") over time.

1. Go to **Data Explorer**.
2. Check the metrics listed below.

To view the self-monitoring data use the following metrics:

* `dsfm:server.log_and_events_monitoring.events_rejected_count` (Count of log events that are rejected due to ingestion limit)  
  This metric can be used to verify if any log events were rejected due to the ingest/minute limit for a given timeframe. If the metric is frequently above `0`, then it may suggest that limits should be increased for that tenant.  
  Data Explorer query example:

  ```
  dsfm:server.log_and_events_monitoring.events_rejected_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```
* `dsfm:server.log_and_events_monitoring.events_incoming_count` (The count of incoming log events)  
  This metric can be used to to verify how many log events are incoming to the server for a given timeframe. It can include duplicates due to retransmissions. This metric contains additional dimensions: `event.sender` to identify the source of the incoming log event and `event.type` to identify the event type of the incoming log event.  
  Data Explorer query example:

  ```
  dsfm:server.log_and_events_monitoring.events_incoming_count:splitBy():sum:auto:sort(value(sum,descending)):rate(1m)
  ```

## ActiveGate insights

In this example, we use the self-monitoring metrics to get insights into the operation of an ActiveGate.

1. Go to **Metrics**.
2. Filter the table by `dsfm:active_gate`.
3. Check metrics for ActiveGate JVM CPU usage and heap memory, which are a good first indicator of the health and utilization of an ActiveGate:

   * **ActiveGate - JVM - CPU Usage**
   * **ActiveGate - JVM - Heap Memory Used**
   * **ActiveGate - JVM - Heap Memory Available**

The following screenshots show the JVM memory usage and JVM CPU usage of one ActiveGate in the cluster.

![Example of Data Explorer page with self-monitoring metric.](https://dt-cdn.net/images/1explorer-f-1565-6576341d6c.png)

Notice that the memory usage and availability over time does not indicate any abnormal utilization, but CPU usage shows an interesting peak.

![Example of Data Explorer page with self-monitoring metric graph.](https://dt-cdn.net/images/2explorer-f-1565-80ae3f684e.png)

Further investigation reveals that this peak was caused by an increased number of OneAgents reporting via this ActiveGate, which resulted from the execution of a test on this cluster.


---
