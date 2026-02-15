---
title: Google Cloud Firestore monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-firestore-monitoring
scraped: 2026-02-15T21:22:38.561379
---

# Google Cloud Firestore monitoring

# Google Cloud Firestore monitoring

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

The following feature sets are available for Google Cloud Firestore.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| firestore\_instance/default\_metrics | Document Deletes | Count | firestore.googleapis.com/document/delete\_count |
| firestore\_instance/default\_metrics | Document Reads | Count | firestore.googleapis.com/document/read\_count |
| firestore\_instance/default\_metrics | Document Writes | Count | firestore.googleapis.com/document/write\_count |
| firestore\_instance/default\_metrics | Connected Clients | Count | firestore.googleapis.com/network/active\_connections |
| firestore\_instance/default\_metrics | Snapshot Listeners | Count | firestore.googleapis.com/network/snapshot\_listeners |
| firestore\_instance/default\_metrics | Rule Evaluations | Count | firestore.googleapis.com/rules/evaluation\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")