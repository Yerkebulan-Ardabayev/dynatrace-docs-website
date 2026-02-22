---
title: Google Cloud Composer monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-composer-monitoring
scraped: 2026-02-22T21:24:25.461459
---

# Google Cloud Composer monitoring

# Google Cloud Composer monitoring

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

The following feature sets are available for Google Cloud Composer.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_composer\_environment/default\_metrics | API Requests | Count | composer.googleapis.com/environment/api/request\_count |
| cloud\_composer\_environment/default\_metrics | API Latency | MilliSecond | composer.googleapis.com/environment/api/request\_latencies |
| cloud\_composer\_environment/default\_metrics | Parse Error Count | Count | composer.googleapis.com/environment/dag\_processing/parse\_error\_count |
| cloud\_composer\_environment/default\_metrics | DAG parsing processes | Count | composer.googleapis.com/environment/dag\_processing/processes |
| cloud\_composer\_environment/default\_metrics | Processors Timeout Count | Count | composer.googleapis.com/environment/dag\_processing/processor\_timeout\_count |
| cloud\_composer\_environment/default\_metrics | Total Parse Time | Second | composer.googleapis.com/environment/dag\_processing/total\_parse\_time |
| cloud\_composer\_environment/default\_metrics | Dag Bag Size | Count | composer.googleapis.com/environment/dagbag\_size |
| cloud\_composer\_environment/default\_metrics | Database Healthy | Unspecified | composer.googleapis.com/environment/database\_health |
| cloud\_composer\_environment/default\_metrics | Executor Open Slots | Count | composer.googleapis.com/environment/executor/open\_slots |
| cloud\_composer\_environment/default\_metrics | Executor Running Tasks | Count | composer.googleapis.com/environment/executor/running\_tasks |
| cloud\_composer\_environment/default\_metrics | Task Instance Count | Count | composer.googleapis.com/environment/finished\_task\_instance\_count |
| cloud\_composer\_environment/default\_metrics | Healthy | Unspecified | composer.googleapis.com/environment/healthy |
| cloud\_composer\_environment/default\_metrics | Celery Workers | Count | composer.googleapis.com/environment/num\_celery\_workers |
| cloud\_composer\_environment/default\_metrics | Scheduler Heartbeats | Count | composer.googleapis.com/environment/scheduler\_heartbeat\_count |
| cloud\_composer\_environment/default\_metrics | Task Queue Length | Count | composer.googleapis.com/environment/task\_queue\_length |
| cloud\_composer\_environment/default\_metrics | Worker Pod Eviction Count | Count | composer.googleapis.com/environment/worker/pod\_eviction\_count |
| cloud\_composer\_environment/default\_metrics | Zombie Tasks Killed | Count | composer.googleapis.com/environment/zombie\_task\_killed\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")