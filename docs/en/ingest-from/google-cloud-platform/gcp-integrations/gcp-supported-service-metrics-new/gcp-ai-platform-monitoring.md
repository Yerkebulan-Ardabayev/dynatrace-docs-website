---
title: Google Cloud AI Platform monitoring (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-ai-platform-monitoring
scraped: 2026-03-01T21:26:10.054224
---

# Google Cloud AI Platform monitoring (deprecated)

# Google Cloud AI Platform monitoring (deprecated)

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

The following feature sets are available for Google Cloud AI Platform.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloudml\_job/default\_metrics | Accelerator memory utilization | Percent | ml.googleapis.com/training/accelerator/memory/utilization |
| cloudml\_job/default\_metrics | Accelerator utilization | Percent | ml.googleapis.com/training/accelerator/utilization |
| cloudml\_job/default\_metrics | CPU utilization | Percent | ml.googleapis.com/training/cpu/utilization |
| cloudml\_job/default\_metrics | Memory utilization | Percent | ml.googleapis.com/training/memory/utilization |
| cloudml\_job/default\_metrics | Network bytes received | Byte | ml.googleapis.com/training/network/received\_bytes\_count |
| cloudml\_job/default\_metrics | Network bytes sent | Byte | ml.googleapis.com/training/network/sent\_bytes\_count |
| cloudml\_model\_version/default\_metrics | Error count | Count | ml.googleapis.com/prediction/error\_count |
| cloudml\_model\_version/default\_metrics | Latency | MicroSecond | ml.googleapis.com/prediction/latencies |
| cloudml\_model\_version/default\_metrics | Accelerator duty cycle | Percent | ml.googleapis.com/prediction/online/accelerator/duty\_cycle |
| cloudml\_model\_version/default\_metrics | Accelerator memory usage | Byte | ml.googleapis.com/prediction/online/accelerator/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | CPU usage | Percent | ml.googleapis.com/prediction/online/cpu/utilization |
| cloudml\_model\_version/default\_metrics | Memory usage | Byte | ml.googleapis.com/prediction/online/memory/bytes\_used |
| cloudml\_model\_version/default\_metrics | Network bytes received | Byte | ml.googleapis.com/prediction/online/network/bytes\_received |
| cloudml\_model\_version/default\_metrics | Network bytes sent | Byte | ml.googleapis.com/prediction/online/network/bytes\_sent |
| cloudml\_model\_version/default\_metrics | Replica count | Count | ml.googleapis.com/prediction/online/replicas |
| cloudml\_model\_version/default\_metrics | Replica target | Count | ml.googleapis.com/prediction/online/target\_replicas |
| cloudml\_model\_version/default\_metrics | Prediction count | Count | ml.googleapis.com/prediction/prediction\_count |
| cloudml\_model\_version/default\_metrics | Response count | Count | ml.googleapis.com/prediction/response\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")