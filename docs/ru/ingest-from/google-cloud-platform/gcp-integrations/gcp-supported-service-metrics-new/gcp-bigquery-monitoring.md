---
title: Google BigQuery monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring
scraped: 2026-02-18T05:52:48.796818
---

# Google BigQuery monitoring

# Google BigQuery monitoring

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

The following feature sets are available for Google BigQuery.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| bigquery\_biengine\_model/default\_metrics | Inflight requests | Count | bigquerybiengine.googleapis.com/model/inflight\_requests |
| bigquery\_biengine\_model/default\_metrics | Request count | Count | bigquerybiengine.googleapis.com/model/request\_count |
| bigquery\_biengine\_model/default\_metrics | Request execution times | MilliSecond | bigquerybiengine.googleapis.com/model/request\_latencies |
| bigquery\_project/default\_metrics | Job count | Count | bigquery.googleapis.com/job/num\_in\_flight |
| bigquery\_project/default\_metrics | Query count | Count | bigquery.googleapis.com/query/count |
| bigquery\_project/default\_metrics | Query execution times | Second | bigquery.googleapis.com/query/execution\_times |
| bigquery\_project/default\_metrics | Slots used by project, reservation, and job type | Count | bigquery.googleapis.com/slots/allocated |
| bigquery\_project/default\_metrics | Slots assigned | Count | bigquery.googleapis.com/slots/assigned |
| bigquery\_project/default\_metrics | Slots capacity committed | Count | bigquery.googleapis.com/slots/capacity\_committed |
| bigquery\_project/default\_metrics | Slots max assigned | Count | bigquery.googleapis.com/slots/max\_assigned |
| bigquery\_project/default\_metrics | Slots used across projects in reservation | Count | bigquery.googleapis.com/slots/total\_allocated\_for\_reservation |
| bigquery\_project/default\_metrics | Total slots | Count | bigquery.googleapis.com/slots/total\_available |
| bigquery\_project/default\_metrics | Reservation total bytes | Byte | bigquerybiengine.googleapis.com/reservation/total\_bytes |
| bigquery\_project/default\_metrics | Reservation used bytes | Byte | bigquerybiengine.googleapis.com/reservation/used\_bytes |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")