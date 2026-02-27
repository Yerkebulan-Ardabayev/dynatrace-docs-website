---
title: Google Cloud Firebase monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-firebase-monitoring
scraped: 2026-02-27T21:31:30.685892
---

# Google Cloud Firebase monitoring

# Google Cloud Firebase monitoring

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

The following feature sets are available for Google Cloud Firebase.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| firebase\_domain/default\_metrics | Bytes stored limit | Byte | firebasehosting.googleapis.com/storage/limit |
| firebase\_domain/default\_metrics | Bytes stored | Byte | firebasehosting.googleapis.com/storage/total\_bytes |
| firebase\_namespace/default\_metrics | Database Load | Count | firebasedatabase.googleapis.com/io/database\_load |
| firebase\_namespace/default\_metrics | Saved Bytes | Byte | firebasedatabase.googleapis.com/io/persisted\_bytes\_count |
| firebase\_namespace/default\_metrics | Responses sent | Count | firebasedatabase.googleapis.com/io/sent\_responses\_count |
| firebase\_namespace/default\_metrics | I/O utilization | Count | firebasedatabase.googleapis.com/io/utilization |
| firebase\_namespace/default\_metrics | Connections | Count | firebasedatabase.googleapis.com/network/active\_connections |
| firebase\_namespace/default\_metrics | API Hits | Count | firebasedatabase.googleapis.com/network/api\_hits\_count |
| firebase\_namespace/default\_metrics | Broadcast Load | Count | firebasedatabase.googleapis.com/network/broadcast\_load |
| firebase\_namespace/default\_metrics | Disabled for network | Unspecified | firebasedatabase.googleapis.com/network/disabled\_for\_overages |
| firebase\_namespace/default\_metrics | HTTPS Requests Received | Count | firebasedatabase.googleapis.com/network/https\_requests\_count |
| firebase\_namespace/default\_metrics | Bytes sent monthly | Byte | firebasedatabase.googleapis.com/network/monthly\_sent |
| firebase\_namespace/default\_metrics | Bytes sent limit | Byte | firebasedatabase.googleapis.com/network/monthly\_sent\_limit |
| firebase\_namespace/default\_metrics | Total billed bytes | Byte | firebasedatabase.googleapis.com/network/sent\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload and Protocol Bytes sent | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_and\_protocol\_bytes\_count |
| firebase\_namespace/default\_metrics | Payload Bytes Sent | Byte | firebasedatabase.googleapis.com/network/sent\_payload\_bytes\_count |
| firebase\_namespace/default\_metrics | Rule evaluations | Count | firebasedatabase.googleapis.com/rules/evaluation\_count |
| firebase\_namespace/default\_metrics | Bytes stored limit | Byte | firebasedatabase.googleapis.com/storage/limit |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")