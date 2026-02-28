---
title: Google Cloud Filestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring
scraped: 2026-02-28T21:30:59.855385
---

# Google Cloud Filestore monitoring

# Google Cloud Filestore monitoring

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

The following feature sets are available for Google Cloud Filestore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| filestore\_instance/default\_metrics | Average read latency | MilliSecond | file.googleapis.com/nfs/server/average\_read\_latency |
| filestore\_instance/default\_metrics | Average write latency | MilliSecond | file.googleapis.com/nfs/server/average\_write\_latency |
| filestore\_instance/default\_metrics | Free disk bytes | Byte | file.googleapis.com/nfs/server/free\_bytes |
| filestore\_instance/default\_metrics | Free disk space percent | Percent | file.googleapis.com/nfs/server/free\_bytes\_percent |
| filestore\_instance/default\_metrics | Metadata operation count | Count | file.googleapis.com/nfs/server/metadata\_ops\_count |
| filestore\_instance/default\_metrics | Procedure call count | Count | file.googleapis.com/nfs/server/procedure\_call\_count |
| filestore\_instance/default\_metrics | Bytes read | Byte | file.googleapis.com/nfs/server/read\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on read operations | MilliSecond | file.googleapis.com/nfs/server/read\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk read operation count | Count | file.googleapis.com/nfs/server/read\_ops\_count |
| filestore\_instance/default\_metrics | Used disk bytes | Byte | file.googleapis.com/nfs/server/used\_bytes |
| filestore\_instance/default\_metrics | Used disk space percent | Percent | file.googleapis.com/nfs/server/used\_bytes\_percent |
| filestore\_instance/default\_metrics | Bytes written | Byte | file.googleapis.com/nfs/server/write\_bytes\_count |
| filestore\_instance/default\_metrics | Time (in milliseconds) spent on write operations | MilliSecond | file.googleapis.com/nfs/server/write\_milliseconds\_count |
| filestore\_instance/default\_metrics | Disk write operation count | Count | file.googleapis.com/nfs/server/write\_ops\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")