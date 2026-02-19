---
title: Google Cloud SQL monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql
scraped: 2026-02-19T21:25:49.708649
---

# Google Cloud SQL monitoring

# Google Cloud SQL monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
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

The following feature sets are available for Google Cloud SQL.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloudsql\_database/default\_metrics | Auto-failover Requests | Count | cloudsql.googleapis.com/database/auto\_failover\_request\_count |
| cloudsql\_database/default\_metrics | Available for failover | Count | cloudsql.googleapis.com/database/available\_for\_failover |
| cloudsql\_database/default\_metrics | CPU reserved cores | Count | cloudsql.googleapis.com/database/cpu/reserved\_cores |
| cloudsql\_database/default\_metrics | CPU usage | Second | cloudsql.googleapis.com/database/cpu/usage\_time |
| cloudsql\_database/default\_metrics | CPU utilization | Percent | cloudsql.googleapis.com/database/cpu/utilization |
| cloudsql\_database/default\_metrics | Bytes used | Byte | cloudsql.googleapis.com/database/disk/bytes\_used |
| cloudsql\_database/default\_metrics | Disk quota | Byte | cloudsql.googleapis.com/database/disk/quota |
| cloudsql\_database/default\_metrics | Disk read IO | Count | cloudsql.googleapis.com/database/disk/read\_ops\_count |
| cloudsql\_database/default\_metrics | Disk utilization | Count | cloudsql.googleapis.com/database/disk/utilization |
| cloudsql\_database/default\_metrics | Disk write IO | Count | cloudsql.googleapis.com/database/disk/write\_ops\_count |
| cloudsql\_database/default\_metrics | Instance state | Unspecified | cloudsql.googleapis.com/database/instance\_state |
| cloudsql\_database/default\_metrics | Memory quota | Byte | cloudsql.googleapis.com/database/memory/quota |
| cloudsql\_database/default\_metrics | Total memory usage | Byte | cloudsql.googleapis.com/database/memory/total\_usage |
| cloudsql\_database/default\_metrics | Memory usage | Byte | cloudsql.googleapis.com/database/memory/usage |
| cloudsql\_database/default\_metrics | Memory utilization | Count | cloudsql.googleapis.com/database/memory/utilization |
| cloudsql\_database/default\_metrics | InnoDB dirty pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_dirty |
| cloudsql\_database/default\_metrics | InnoDB free pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_free |
| cloudsql\_database/default\_metrics | InnoDB total pages | Count | cloudsql.googleapis.com/database/mysql/innodb\_buffer\_pool\_pages\_total |
| cloudsql\_database/default\_metrics | InnoDB fsync calls | Count | cloudsql.googleapis.com/database/mysql/innodb\_data\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB log fsync calls | Count | cloudsql.googleapis.com/database/mysql/innodb\_os\_log\_fsyncs |
| cloudsql\_database/default\_metrics | InnoDB pages read | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_read |
| cloudsql\_database/default\_metrics | InnoDB pages written | Count | cloudsql.googleapis.com/database/mysql/innodb\_pages\_written |
| cloudsql\_database/default\_metrics | Queries | Count | cloudsql.googleapis.com/database/mysql/queries |
| cloudsql\_database/default\_metrics | Questions | Count | cloudsql.googleapis.com/database/mysql/questions |
| cloudsql\_database/default\_metrics | Network bytes received by MySQL | Byte | cloudsql.googleapis.com/database/mysql/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Available for failover (Deprecated) | Count | cloudsql.googleapis.com/database/mysql/replication/available\_for\_failover |
| cloudsql\_database/default\_metrics | Last I/O thread error number | Count | cloudsql.googleapis.com/database/mysql/replication/last\_io\_errno |
| cloudsql\_database/default\_metrics | Last SQL thread error number | Count | cloudsql.googleapis.com/database/mysql/replication/last\_sql\_errno |
| cloudsql\_database/default\_metrics | Replica lag | Second | cloudsql.googleapis.com/database/mysql/replication/seconds\_behind\_master |
| cloudsql\_database/default\_metrics | Slave I/O thread running state | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_io\_running\_state |
| cloudsql\_database/default\_metrics | Slave SQL thread running state | Unspecified | cloudsql.googleapis.com/database/mysql/replication/slave\_sql\_running\_state |
| cloudsql\_database/default\_metrics | Network bytes sent by MySQL | Byte | cloudsql.googleapis.com/database/mysql/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Cloud SQL Connections | Count | cloudsql.googleapis.com/database/network/connections |
| cloudsql\_database/default\_metrics | Received bytes | Byte | cloudsql.googleapis.com/database/network/received\_bytes\_count |
| cloudsql\_database/default\_metrics | Sent bytes | Byte | cloudsql.googleapis.com/database/network/sent\_bytes\_count |
| cloudsql\_database/default\_metrics | Execution time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/execution\_time |
| cloudsql\_database/default\_metrics | IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/io\_time |
| cloudsql\_database/default\_metrics | Latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/latencies |
| cloudsql\_database/default\_metrics | Aggregated lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/aggregate/lock\_time |
| cloudsql\_database/default\_metrics | Affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/row\_count |
| cloudsql\_database/default\_metrics | Shared blocks cache access | Count | cloudsql.googleapis.com/database/postgresql/insights/aggregate/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per query execution times | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/execution\_time |
| cloudsql\_database/default\_metrics | Per query IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/io\_time |
| cloudsql\_database/default\_metrics | Per query latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/latencies |
| cloudsql\_database/default\_metrics | Per query lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/perquery/lock\_time |
| cloudsql\_database/default\_metrics | Per query affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/row\_count |
| cloudsql\_database/default\_metrics | Per query Shared blocks cache access | Count | cloudsql.googleapis.com/database/postgresql/insights/perquery/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | Per tag execution time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/execution\_time |
| cloudsql\_database/default\_metrics | Per tag IO time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/io\_time |
| cloudsql\_database/default\_metrics | Per tag latency | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/latencies |
| cloudsql\_database/default\_metrics | Per tag lock time | MicroSecond | cloudsql.googleapis.com/database/postgresql/insights/pertag/lock\_time |
| cloudsql\_database/default\_metrics | Per tag affected rows | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/row\_count |
| cloudsql\_database/default\_metrics | Per tag shared blocks cache accessed | Count | cloudsql.googleapis.com/database/postgresql/insights/pertag/shared\_blk\_access\_count |
| cloudsql\_database/default\_metrics | PostgreSQL Connections | Count | cloudsql.googleapis.com/database/postgresql/num\_backends |
| cloudsql\_database/default\_metrics | Lag bytes | Byte | cloudsql.googleapis.com/database/postgresql/replication/replica\_byte\_lag |
| cloudsql\_database/default\_metrics | Number of transactions | Count | cloudsql.googleapis.com/database/postgresql/transaction\_count |
| cloudsql\_database/default\_metrics | Replica lag | Second | cloudsql.googleapis.com/database/replication/replica\_lag |
| cloudsql\_database/default\_metrics | Server up | Count | cloudsql.googleapis.com/database/up |
| cloudsql\_database/default\_metrics | Uptime | Second | cloudsql.googleapis.com/database/uptime |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")