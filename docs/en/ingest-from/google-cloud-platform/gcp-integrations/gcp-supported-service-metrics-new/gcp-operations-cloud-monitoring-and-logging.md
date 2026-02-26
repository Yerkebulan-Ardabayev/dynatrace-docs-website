---
title: Operations: Cloud Monitoring & Logging
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-operations-cloud-monitoring-and-logging
scraped: 2026-02-26T21:26:10.432338
---

# Operations: Cloud Monitoring & Logging

# Operations: Cloud Monitoring & Logging

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Operations suite.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| uptime\_url/default\_metrics | Check passed | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| uptime\_url/default\_metrics | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| uptime\_url/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| uptime\_url/default\_metrics | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| uptime\_url/default\_metrics | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gce\_instance/uptime\_check | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gce\_instance/uptime\_check |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gce\_instance/uptime\_check | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gce\_instance/uptime\_check | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| gae\_app\_uptime\_check/default\_metrics | Check passed | Unspecified | monitoring.googleapis.com/uptime\_check/check\_passed |
| gae\_app\_uptime\_check/default\_metrics | Content mismatch | Unspecified | monitoring.googleapis.com/uptime\_check/content\_mismatch |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/error\_code |
| gae\_app\_uptime\_check/default\_metrics |  |  | monitoring.googleapis.com/uptime\_check/http\_status |
| gae\_app\_uptime\_check/default\_metrics | Request latency | MilliSecond | monitoring.googleapis.com/uptime\_check/request\_latency |
| gae\_app\_uptime\_check/default\_metrics | Time until SSL certificate expires | Day | monitoring.googleapis.com/uptime\_check/time\_until\_ssl\_cert\_expires |
| logging\_sink/default\_metrics | Exported log bytes | Byte | logging.googleapis.com/exports/byte\_count |
| logging\_sink/default\_metrics | Exported log entries failures | Count | logging.googleapis.com/exports/error\_count |
| logging\_sink/default\_metrics | Exported log entries | Count | logging.googleapis.com/exports/log\_entry\_count |
| cloudtrace\_googleapis\_com\_CloudtraceProject/default\_metrics | Spans Exported to BigQuery | Count | cloudtrace.googleapis.com/bigquery\_export/exported\_span\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")