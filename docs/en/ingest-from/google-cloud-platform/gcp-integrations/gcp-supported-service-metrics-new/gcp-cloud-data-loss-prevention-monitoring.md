---
title: Google Cloud Data Loss Prevention monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-data-loss-prevention-monitoring
scraped: 2026-02-25T21:25:32.337850
---

# Google Cloud Data Loss Prevention monitoring

# Google Cloud Data Loss Prevention monitoring

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

The following feature sets are available for Google Cloud Data Loss Prevention.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| cloud\_dlp\_project/default\_metrics | Content bytes inspected | Byte | dlp.googleapis.com/content\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Content bytes transformed | Byte | dlp.googleapis.com/content\_bytes\_transformed\_count |
| cloud\_dlp\_project/default\_metrics | Findings | Count | dlp.googleapis.com/finding\_count |
| cloud\_dlp\_project/default\_metrics | Job results | Count | dlp.googleapis.com/job\_result\_count |
| cloud\_dlp\_project/default\_metrics | Job trigger runs | Count | dlp.googleapis.com/job\_trigger\_run\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes inspected | Byte | dlp.googleapis.com/storage\_bytes\_inspected\_count |
| cloud\_dlp\_project/default\_metrics | Storage bytes transformed | Byte | dlp.googleapis.com/storage\_bytes\_transformed\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")