---
title: Google Cloud Bigtable monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigtable-monitoring
scraped: 2026-02-24T21:27:37.373734
---

# Google Cloud Bigtable monitoring

# Google Cloud Bigtable monitoring

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

The following feature sets are available for Google Cloud Bigtable.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| bigtable\_cluster/default\_metrics | CPU load | Count | bigtable.googleapis.com/cluster/cpu\_load |
| bigtable\_cluster/default\_metrics | CPU load (hottest node) | Count | bigtable.googleapis.com/cluster/cpu\_load\_hottest\_node |
| bigtable\_cluster/default\_metrics | Disk load | Count | bigtable.googleapis.com/cluster/disk\_load |
| bigtable\_cluster/default\_metrics | Nodes | Count | bigtable.googleapis.com/cluster/node\_count |
| bigtable\_cluster/default\_metrics | Storage utilization | Count | bigtable.googleapis.com/cluster/storage\_utilization |
| bigtable\_cluster/default\_metrics | Data stored | Byte | bigtable.googleapis.com/disk/bytes\_used |
| bigtable\_cluster/default\_metrics | Storage capacity per node | Byte | bigtable.googleapis.com/disk/per\_node\_storage\_capacity |
| bigtable\_cluster/default\_metrics | Storage capacity | Byte | bigtable.googleapis.com/disk/storage\_capacity |
| bigtable\_table/default\_metrics | Replication latencies | MilliSecond | bigtable.googleapis.com/replication/latency |
| bigtable\_table/default\_metrics | Replication maximum delay | Second | bigtable.googleapis.com/replication/max\_delay |
| bigtable\_table/default\_metrics | Error count | Count | bigtable.googleapis.com/server/error\_count |
| bigtable\_table/default\_metrics | Server Latencies | MilliSecond | bigtable.googleapis.com/server/latencies |
| bigtable\_table/default\_metrics | Modified rows | Count | bigtable.googleapis.com/server/modified\_rows\_count |
| bigtable\_table/default\_metrics | Multi-cluster failovers | Count | bigtable.googleapis.com/server/multi\_cluster\_failovers\_count |
| bigtable\_table/default\_metrics | Received bytes | Byte | bigtable.googleapis.com/server/received\_bytes\_count |
| bigtable\_table/default\_metrics | Request count | Count | bigtable.googleapis.com/server/request\_count |
| bigtable\_table/default\_metrics | Returned rows | Count | bigtable.googleapis.com/server/returned\_rows\_count |
| bigtable\_table/default\_metrics | Sent bytes | Byte | bigtable.googleapis.com/server/sent\_bytes\_count |
| bigtable\_table/default\_metrics | Data stored | Byte | bigtable.googleapis.com/table/bytes\_used |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")