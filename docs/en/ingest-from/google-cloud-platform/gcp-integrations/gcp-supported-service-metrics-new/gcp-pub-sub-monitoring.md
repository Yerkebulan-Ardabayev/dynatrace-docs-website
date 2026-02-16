---
title: Google Cloud Pub/Sub monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring
scraped: 2026-02-16T09:34:01.352217
---

# Google Cloud Pub/Sub monitoring

# Google Cloud Pub/Sub monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
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

The following feature sets are available for Google Cloud Pub/Sub.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes |
| pubsub\_snapshot/default\_metrics | Snapshot backlog bytes by region | Byte | pubsub.googleapis.com/snapshot/backlog\_bytes\_by\_region |
| pubsub\_snapshot/default\_metrics | Snapshot updates | Count | pubsub.googleapis.com/snapshot/config\_updates\_count |
| pubsub\_snapshot/default\_metrics | Snapshot messages | Count | pubsub.googleapis.com/snapshot/num\_messages |
| pubsub\_snapshot/default\_metrics | Snapshot messages by region | Count | pubsub.googleapis.com/snapshot/num\_messages\_by\_region |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age |
| pubsub\_snapshot/default\_metrics | Oldest snapshot message age by region | Second | pubsub.googleapis.com/snapshot/oldest\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Ack message count | Count | pubsub.googleapis.com/subscription/ack\_message\_count |
| pubsub\_subscription/default\_metrics | Backlog size | Byte | pubsub.googleapis.com/subscription/backlog\_bytes |
| pubsub\_subscription/default\_metrics | Subscription byte cost | Byte | pubsub.googleapis.com/subscription/byte\_cost |
| pubsub\_subscription/default\_metrics | Subscription updates | Count | pubsub.googleapis.com/subscription/config\_updates\_count |
| pubsub\_subscription/default\_metrics | Dead letter message count | Count | pubsub.googleapis.com/subscription/dead\_letter\_message\_count |
| pubsub\_subscription/default\_metrics | Mod ack deadline message count | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | Outstanding push messages | Count | pubsub.googleapis.com/subscription/num\_outstanding\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages |
| pubsub\_subscription/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/subscription/num\_retained\_acked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/subscription/num\_unacked\_messages\_by\_region |
| pubsub\_subscription/default\_metrics | Unacked messages | Count | pubsub.googleapis.com/subscription/num\_undelivered\_messages |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Oldest unacked message age | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age |
| pubsub\_subscription/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/subscription/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_subscription/default\_metrics | Acknowledge message operations | Count | pubsub.googleapis.com/subscription/pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Acknowledge requests | Count | pubsub.googleapis.com/subscription/pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | Pull operations | Count | pubsub.googleapis.com/subscription/pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | Pull requests | Count | pubsub.googleapis.com/subscription/pull\_request\_count |
| pubsub\_subscription/default\_metrics | Push requests | Count | pubsub.googleapis.com/subscription/push\_request\_count |
| pubsub\_subscription/default\_metrics | Push latency | MicroSecond | pubsub.googleapis.com/subscription/push\_request\_latencies |
| pubsub\_subscription/default\_metrics | Retained acked bytes | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes |
| pubsub\_subscription/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/subscription/retained\_acked\_bytes\_by\_region |
| pubsub\_subscription/default\_metrics | Seek requests | Count | pubsub.googleapis.com/subscription/seek\_request\_count |
| pubsub\_subscription/default\_metrics | Sent message count | Count | pubsub.googleapis.com/subscription/sent\_message\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull Acknowledge requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_ack\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline message operations | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_message\_operation\_count |
| pubsub\_subscription/default\_metrics | StreamingPull ModifyAckDeadline requests | Count | pubsub.googleapis.com/subscription/streaming\_pull\_mod\_ack\_deadline\_request\_count |
| pubsub\_subscription/default\_metrics | StreamingPull responses | Count | pubsub.googleapis.com/subscription/streaming\_pull\_response\_count |
| pubsub\_subscription/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/subscription/unacked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Topic byte cost | Byte | pubsub.googleapis.com/topic/byte\_cost |
| pubsub\_topic/default\_metrics | Topic updates | Count | pubsub.googleapis.com/topic/config\_updates\_count |
| pubsub\_topic/default\_metrics | Publish message size | Byte | pubsub.googleapis.com/topic/message\_sizes |
| pubsub\_topic/default\_metrics | Retained acked messages by region | Count | pubsub.googleapis.com/topic/num\_retained\_acked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Unacked messages by region | Count | pubsub.googleapis.com/topic/num\_unacked\_messages\_by\_region |
| pubsub\_topic/default\_metrics | Oldest retained acked message age by region | Second | pubsub.googleapis.com/topic/oldest\_retained\_acked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Oldest unacked message age by region | Second | pubsub.googleapis.com/topic/oldest\_unacked\_message\_age\_by\_region |
| pubsub\_topic/default\_metrics | Retained acked bytes by region | Byte | pubsub.googleapis.com/topic/retained\_acked\_bytes\_by\_region |
| pubsub\_topic/default\_metrics | Publish message operations | Count | pubsub.googleapis.com/topic/send\_message\_operation\_count |
| pubsub\_topic/default\_metrics | Publish requests | Count | pubsub.googleapis.com/topic/send\_request\_count |
| pubsub\_topic/default\_metrics | Unacked bytes by region | Byte | pubsub.googleapis.com/topic/unacked\_bytes\_by\_region |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")