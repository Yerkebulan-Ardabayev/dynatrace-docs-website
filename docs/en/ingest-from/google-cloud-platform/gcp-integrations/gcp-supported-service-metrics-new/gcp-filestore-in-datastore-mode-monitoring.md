---
title: Google Cloud Firestore in Datastore mode monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring
scraped: 2026-03-06T21:36:25.334800
---

# Google Cloud Firestore in Datastore mode monitoring


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

Set up integration

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](../gcp-guide/deploy-k8.md#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the Metrics browser, Data Explorer, and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Firestore in Datastore mode.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| datastore\_request/default\_metrics | Requests | Count | datastore.googleapis.com/api/request\_count |
| datastore\_request/default\_metrics | Sizes of read entities | Byte | datastore.googleapis.com/entity/read\_sizes |
| datastore\_request/default\_metrics | Sizes of written entities | Byte | datastore.googleapis.com/entity/write\_sizes |
| datastore\_request/default\_metrics | Index writes | Count | datastore.googleapis.com/index/write\_count |
| datastore\_request/default\_metrics | Requests | Count | firestore.googleapis.com/api/request\_count |

## Related topics

* Google Cloud integrations