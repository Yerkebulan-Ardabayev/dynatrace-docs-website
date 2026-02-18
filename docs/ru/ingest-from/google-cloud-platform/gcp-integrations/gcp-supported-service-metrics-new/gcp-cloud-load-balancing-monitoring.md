---
title: Google Cloud Load Balancing monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring
scraped: 2026-02-16T09:35:45.918996
---

# Google Cloud Load Balancing monitoring

# Google Cloud Load Balancing monitoring

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

The following feature sets are available for Google Cloud Load Balancing.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| https\_lb\_rule/default\_metrics | Backend latency | MilliSecond | loadbalancing.googleapis.com/https/backend\_latencies |
| https\_lb\_rule/default\_metrics | Backend Request Bytes | Byte | loadbalancing.googleapis.com/https/backend\_request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Backend Request Count | Count | loadbalancing.googleapis.com/https/backend\_request\_count |
| https\_lb\_rule/default\_metrics | Backend Response Bytes | Byte | loadbalancing.googleapis.com/https/backend\_response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Frontend RTT | MilliSecond | loadbalancing.googleapis.com/https/frontend\_tcp\_rtt |
| https\_lb\_rule/default\_metrics | Request bytes | Byte | loadbalancing.googleapis.com/https/request\_bytes\_count |
| https\_lb\_rule/default\_metrics | Request count | Count | loadbalancing.googleapis.com/https/request\_count |
| https\_lb\_rule/default\_metrics | Response bytes | Byte | loadbalancing.googleapis.com/https/response\_bytes\_count |
| https\_lb\_rule/default\_metrics | Total latency | MilliSecond | loadbalancing.googleapis.com/https/total\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Backend latencies | MilliSecond | loadbalancing.googleapis.com/https/internal/backend\_latencies |
| internal\_http\_lb\_rule/default\_metrics | Request bytes | Byte | loadbalancing.googleapis.com/https/internal/request\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Request count | Count | loadbalancing.googleapis.com/https/internal/request\_count |
| internal\_http\_lb\_rule/default\_metrics | Response bytes | Byte | loadbalancing.googleapis.com/https/internal/response\_bytes\_count |
| internal\_http\_lb\_rule/default\_metrics | Total latencies | MilliSecond | loadbalancing.googleapis.com/https/internal/total\_latencies |
| internal\_tcp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_tcp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| internal\_tcp\_lb\_rule/default\_metrics | RTT latencies | MilliSecond | loadbalancing.googleapis.com/l3/internal/rtt\_latencies |
| internal\_udp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/internal/egress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/internal/egress\_packets\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/internal/ingress\_bytes\_count |
| internal\_udp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/internal/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| tcp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_lb\_rule/default\_metrics | RTT latencies | MilliSecond | loadbalancing.googleapis.com/l3/external/rtt\_latencies |
| udp\_lb\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/l3/external/egress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Egress packets | Count | loadbalancing.googleapis.com/l3/external/egress\_packets\_count |
| udp\_lb\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/l3/external/ingress\_bytes\_count |
| udp\_lb\_rule/default\_metrics | Ingress packets | Count | loadbalancing.googleapis.com/l3/external/ingress\_packets\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Closed connections | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/closed\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Egress bytes | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/egress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | Frontend RTT | MilliSecond | loadbalancing.googleapis.com/tcp\_ssl\_proxy/frontend\_tcp\_rtt |
| tcp\_ssl\_proxy\_rule/default\_metrics | Ingress bytes | Byte | loadbalancing.googleapis.com/tcp\_ssl\_proxy/ingress\_bytes\_count |
| tcp\_ssl\_proxy\_rule/default\_metrics | New connections opened | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/new\_connections |
| tcp\_ssl\_proxy\_rule/default\_metrics | Open Connections | Count | loadbalancing.googleapis.com/tcp\_ssl\_proxy/open\_connections |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")