---
title: Google Cloud Dataflow monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-dataflow-monitoring
scraped: 2026-02-28T21:28:31.479009
---

# Google Cloud Dataflow monitoring

# Google Cloud Dataflow monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
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

The following feature sets are available for Google Cloud Dataflow.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| dataflow\_job/default\_metrics | Billable shuffle data processed | Byte | dataflow.googleapis.com/job/billable\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Current number of vCPUs in use | Count | dataflow.googleapis.com/job/current\_num\_vcpus |
| dataflow\_job/default\_metrics | Current shuffle slots in use | Count | dataflow.googleapis.com/job/current\_shuffle\_slots |
| dataflow\_job/default\_metrics | Data watermark lag | Second | dataflow.googleapis.com/job/data\_watermark\_age |
| dataflow\_job/default\_metrics | Elapsed time | Second | dataflow.googleapis.com/job/elapsed\_time |
| dataflow\_job/default\_metrics | Element count | Count | dataflow.googleapis.com/job/element\_count |
| dataflow\_job/default\_metrics | Elements Produced | Count | dataflow.googleapis.com/job/elements\_produced\_count |
| dataflow\_job/default\_metrics | Estimated byte count | Byte | dataflow.googleapis.com/job/estimated\_byte\_count |
| dataflow\_job/default\_metrics | Estimated Bytes Produced | Count | dataflow.googleapis.com/job/estimated\_bytes\_produced\_count |
| dataflow\_job/default\_metrics | Failed | Count | dataflow.googleapis.com/job/is\_failed |
| dataflow\_job/default\_metrics | Per-stage data watermark lag | Second | dataflow.googleapis.com/job/per\_stage\_data\_watermark\_age |
| dataflow\_job/default\_metrics | Per-stage system lag | Second | dataflow.googleapis.com/job/per\_stage\_system\_lag |
| dataflow\_job/default\_metrics | PubsubIO.Read requests from Dataflow jobs | Count | dataflow.googleapis.com/job/pubsub/read\_count |
| dataflow\_job/default\_metrics | Pub/Sub Pull Request Latencies | MilliSecond | dataflow.googleapis.com/job/pubsub/read\_latencies |
| dataflow\_job/default\_metrics | Pub/Sub Publish Requests | Count | dataflow.googleapis.com/job/pubsub/write\_count |
| dataflow\_job/default\_metrics | Pub/Sub Publish Request Latencies | MilliSecond | dataflow.googleapis.com/job/pubsub/write\_latencies |
| dataflow\_job/default\_metrics |  |  | dataflow.googleapis.com/job/status |
| dataflow\_job/default\_metrics | System lag | Second | dataflow.googleapis.com/job/system\_lag |
| dataflow\_job/default\_metrics | Total memory usage time | GigaByte | dataflow.googleapis.com/job/total\_memory\_usage\_time |
| dataflow\_job/default\_metrics | Total PD usage time | GigaByte | dataflow.googleapis.com/job/total\_pd\_usage\_time |
| dataflow\_job/default\_metrics | Total shuffle data processed | Byte | dataflow.googleapis.com/job/total\_shuffle\_data\_processed |
| dataflow\_job/default\_metrics | Total streaming data processed | Byte | dataflow.googleapis.com/job/total\_streaming\_data\_processed |
| dataflow\_job/default\_metrics | Total vCPU time | Second | dataflow.googleapis.com/job/total\_vcpu\_time |
| dataflow\_job/default\_metrics | User Counter | Count | dataflow.googleapis.com/job/user\_counter |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")