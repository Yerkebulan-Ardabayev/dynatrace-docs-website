---
title: Google Cloud AlloyDB monitoring
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-alloydb-monitoring
scraped: 2026-05-12T11:51:04.946605
---

# Google Cloud AlloyDB monitoring

# Google Cloud AlloyDB monitoring

* How-to guide
* 2-min read
* Published May 17, 2023

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud AlloyDB.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| alloydb\_database/insights\_metrics | Execution time | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.execution\_time |
| alloydb\_database/insights\_metrics | IO time | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.io\_time |
| alloydb\_database/insights\_metrics | Latency | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.latencies |
| alloydb\_database/insights\_metrics | Lock time | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache access | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.aggregate.shared\_blk\_access\_count |
| alloydb\_database/insights\_metrics | Execution time per query | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.execution\_time |
| alloydb\_database/insights\_metrics | IO time per query | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.io\_time |
| alloydb\_database/insights\_metrics | Latency per query | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.latencies |
| alloydb\_database/insights\_metrics | Lock time per query | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows per query | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache access per query | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.perquery.shared\_blk\_access\_count |
| alloydb\_database/insights\_metrics | Execution time per tag | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.execution\_time |
| alloydb\_database/insights\_metrics | IO time per tag | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.io\_time |
| alloydb\_database/insights\_metrics | Latency per tag | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.latencies |
| alloydb\_database/insights\_metrics | Lock time per tag | MicroSecond | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.lock\_time |
| alloydb\_database/insights\_metrics | Affected rows per tag | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.row\_count |
| alloydb\_database/insights\_metrics | Shared blocks cache accessed per tag | Count | cloud.gcp.alloydb\_googleapis\_com.database.postgresql.insights.pertag.shared\_blk\_access\_count |
| alloydb\_instance/default\_metrics | Mean CPU utilization | Percent | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.average\_utilization |
| alloydb\_instance/default\_metrics | Maximum CPU utilization | Percent | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.maximum\_utilization |
| alloydb\_instance/default\_metrics | vCPUs allocated per node | Count | cloud.gcp.alloydb\_googleapis\_com.instance.cpu.vcpus |
| alloydb\_instance/default\_metrics | Minimum available memory | Byte | cloud.gcp.alloydb\_googleapis\_com.instance.memory.min\_available\_memory |
| alloydb\_instance/default\_metrics | Instance abort count | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.abort\_count |
| alloydb\_instance/default\_metrics | Mean connections per node | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.average\_connections |
| alloydb\_instance/default\_metrics | Instance commit count | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.commit\_count |
| alloydb\_instance/default\_metrics | Limit on connections per node | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.connections\_limit |
| alloydb\_instance/default\_metrics | Number and status of nodes | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.instances |
| alloydb\_instance/default\_metrics | Maximum replication lag | MilliSecond | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.replication.maximum\_lag |
| alloydb\_instance/default\_metrics | AlloyDB replica count | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.replication.replicas |
| alloydb\_instance/default\_metrics | Total connections per instance | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.total\_connections |
| alloydb\_instance/default\_metrics | Instance transaction count | Count | cloud.gcp.alloydb\_googleapis\_com.instance.postgres.transaction\_count |

## Related topics

* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")