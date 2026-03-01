---
title: Google Cloud Spanner monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-spanner-monitoring
scraped: 2026-03-01T21:20:25.961869
---

# Google Cloud Spanner monitoring

# Google Cloud Spanner monitoring

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

The following feature sets are available for Google Cloud Spanner.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| spanner\_instance/default\_metrics | API requests | Count | spanner.googleapis.com/api/api\_request\_count |
| spanner\_instance/default\_metrics | Bytes received by Cloud Spanner. | Byte | spanner.googleapis.com/api/received\_bytes\_count |
| spanner\_instance/default\_metrics | API request rate | PerSecond | spanner.googleapis.com/api/request\_count |
| spanner\_instance/default\_metrics | Request latencies | Second | spanner.googleapis.com/api/request\_latencies |
| spanner\_instance/default\_metrics | Bytes sent by Cloud Spanner. | Byte | spanner.googleapis.com/api/sent\_bytes\_count |
| spanner\_instance/default\_metrics | Backup storage used. | Byte | spanner.googleapis.com/instance/backup/used\_bytes |
| spanner\_instance/default\_metrics | Smoothed CPU utilization | Percent | spanner.googleapis.com/instance/cpu/smoothed\_utilization |
| spanner\_instance/default\_metrics | CPU utilization | Percent | spanner.googleapis.com/instance/cpu/utilization |
| spanner\_instance/default\_metrics | CPU utilization by priority | Percent | spanner.googleapis.com/instance/cpu/utilization\_by\_priority |
| spanner\_instance/default\_metrics | Nodes | Count | spanner.googleapis.com/instance/node\_count |
| spanner\_instance/default\_metrics | Sessions | Count | spanner.googleapis.com/instance/session\_count |
| spanner\_instance/default\_metrics | Storage limit | Byte | spanner.googleapis.com/instance/storage/limit\_bytes |
| spanner\_instance/default\_metrics | Storage used. | Byte | spanner.googleapis.com/instance/storage/used\_bytes |
| spanner\_instance/default\_metrics | Storage utilization | Percent | spanner.googleapis.com/instance/storage/utilization |
| spanner\_instance/default\_metrics | Count of queries | Count | spanner.googleapis.com/query\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")