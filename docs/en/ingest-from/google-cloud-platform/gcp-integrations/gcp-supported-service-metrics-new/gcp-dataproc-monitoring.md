---
title: Google Cloud Dataproc monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataproc-monitoring
scraped: 2026-02-15T21:29:58.293741
---

# Google Cloud Dataproc monitoring

# Google Cloud Dataproc monitoring

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

The following feature sets are available for Google Cloud Dataproc.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_dataproc\_cluster/default\_metrics | HDFS DataNodes | Count | dataproc.googleapis.com/cluster/hdfs/datanodes |
| cloud\_dataproc\_cluster/default\_metrics | HDFS capacity | GibiByte | dataproc.googleapis.com/cluster/hdfs/storage\_capacity |
| cloud\_dataproc\_cluster/default\_metrics | HDFS storage utilization | Count | dataproc.googleapis.com/cluster/hdfs/storage\_utilization |
| cloud\_dataproc\_cluster/default\_metrics | Unhealthy HDFS blocks by status | Count | dataproc.googleapis.com/cluster/hdfs/unhealthy\_blocks |
| cloud\_dataproc\_cluster/default\_metrics | Job duration | Second | dataproc.googleapis.com/cluster/job/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Job state duration | Second | dataproc.googleapis.com/cluster/job/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed jobs | Count | dataproc.googleapis.com/cluster/job/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running jobs | Count | dataproc.googleapis.com/cluster/job/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted jobs | Count | dataproc.googleapis.com/cluster/job/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | Operation duration | Second | dataproc.googleapis.com/cluster/operation/completion\_time |
| cloud\_dataproc\_cluster/default\_metrics | Operation state duration | Second | dataproc.googleapis.com/cluster/operation/duration |
| cloud\_dataproc\_cluster/default\_metrics | Failed operations | Count | dataproc.googleapis.com/cluster/operation/failed\_count |
| cloud\_dataproc\_cluster/default\_metrics | Running operations | Count | dataproc.googleapis.com/cluster/operation/running\_count |
| cloud\_dataproc\_cluster/default\_metrics | Submitted operations | Count | dataproc.googleapis.com/cluster/operation/submitted\_count |
| cloud\_dataproc\_cluster/default\_metrics | YARN allocated memory percentage | Count | dataproc.googleapis.com/cluster/yarn/allocated\_memory\_percentage |
| cloud\_dataproc\_cluster/default\_metrics | YARN active applications | Count | dataproc.googleapis.com/cluster/yarn/apps |
| cloud\_dataproc\_cluster/default\_metrics | YARN containers | Count | dataproc.googleapis.com/cluster/yarn/containers |
| cloud\_dataproc\_cluster/default\_metrics | YARN memory size | GibiByte | dataproc.googleapis.com/cluster/yarn/memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN NodeManagers | Count | dataproc.googleapis.com/cluster/yarn/nodemanagers |
| cloud\_dataproc\_cluster/default\_metrics | YARN pending memory size | GibiByte | dataproc.googleapis.com/cluster/yarn/pending\_memory\_size |
| cloud\_dataproc\_cluster/default\_metrics | YARN virtual cores | Count | dataproc.googleapis.com/cluster/yarn/virtual\_cores |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")