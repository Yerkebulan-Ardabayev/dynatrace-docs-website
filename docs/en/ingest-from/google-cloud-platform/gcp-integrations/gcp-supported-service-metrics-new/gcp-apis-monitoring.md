---
title: Google Cloud APIs monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring
scraped: 2026-02-21T21:18:40.931317
---

# Google Cloud APIs monitoring

# Google Cloud APIs monitoring

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

The following feature sets are available for Google Cloud APIs.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| api/default\_metrics | Request count | Count | serviceruntime.googleapis.com/api/request\_count |
| api/default\_metrics | Request latencies | Second | serviceruntime.googleapis.com/api/request\_latencies |
| api/default\_metrics | Request backend latencies | Second | serviceruntime.googleapis.com/api/request\_latencies\_backend |
| api/default\_metrics | Request overhead latencies | Second | serviceruntime.googleapis.com/api/request\_latencies\_overhead |
| consumer\_quota/default\_metrics | Allocation quota usage | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| consumer\_quota/default\_metrics | Quota exceeded error | Count | serviceruntime.googleapis.com/quota/exceeded |
| consumer\_quota/default\_metrics | Quota limit | Count | serviceruntime.googleapis.com/quota/limit |
| consumer\_quota/default\_metrics | Rate quota usage | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |
| consumed\_api/default\_metrics | Request count | Count | serviceruntime.googleapis.com/api/request\_count |
| consumed\_api/default\_metrics | Request latencies | Second | serviceruntime.googleapis.com/api/request\_latencies |
| consumed\_api/default\_metrics | Request sizes | Byte | serviceruntime.googleapis.com/api/request\_sizes |
| consumed\_api/default\_metrics | Response sizes | Byte | serviceruntime.googleapis.com/api/response\_sizes |
| producer\_quota/default\_metrics | Allocation quota usage | Count | serviceruntime.googleapis.com/quota/allocation/usage |
| producer\_quota/default\_metrics | Quota limit | Count | serviceruntime.googleapis.com/quota/limit |
| producer\_quota/default\_metrics | Rate quota usage | Count | serviceruntime.googleapis.com/quota/rate/net\_usage |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")