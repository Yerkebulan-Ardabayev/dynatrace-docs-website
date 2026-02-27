---
title: Google Cloud Run monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring
scraped: 2026-02-27T21:19:07.539488
---

# Google Cloud Run monitoring

# Google Cloud Run monitoring

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

The following feature sets are available for Google Cloud Run.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_run\_revision/default\_metrics | Billable Instance Time | Second | run.googleapis.com/container/billable\_instance\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Allocation | Second | run.googleapis.com/container/cpu/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container CPU Utilization | Percent | run.googleapis.com/container/cpu/utilizations |
| cloud\_run\_revision/default\_metrics | Instance Count | Count | run.googleapis.com/container/instance\_count |
| cloud\_run\_revision/default\_metrics | Max Concurrent Requests | Count | run.googleapis.com/container/max\_request\_concurrencies |
| cloud\_run\_revision/default\_metrics | Container Memory Allocation | GibiByte | run.googleapis.com/container/memory/allocation\_time |
| cloud\_run\_revision/default\_metrics | Container Memory Utilization | Percent | run.googleapis.com/container/memory/utilizations |
| cloud\_run\_revision/default\_metrics | Received Bytes | Byte | run.googleapis.com/container/network/received\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Sent Bytes | Byte | run.googleapis.com/container/network/sent\_bytes\_count |
| cloud\_run\_revision/default\_metrics | Request Count | Count | run.googleapis.com/request\_count |
| cloud\_run\_revision/default\_metrics | Request Latency | MilliSecond | run.googleapis.com/request\_latencies |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")