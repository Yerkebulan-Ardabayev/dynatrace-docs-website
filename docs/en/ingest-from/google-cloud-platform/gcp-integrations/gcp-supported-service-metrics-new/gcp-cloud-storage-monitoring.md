---
title: Google Cloud Storage monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring
scraped: 2026-02-20T21:21:18.827797
---

# Google Cloud Storage monitoring

# Google Cloud Storage monitoring

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

The following feature sets are available for Google Cloud Storage.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gcs\_bucket/default\_metrics | Rule evaluations | Count | firebasestorage.googleapis.com/rules/evaluation\_count |
| gcs\_bucket/default\_metrics | Request count | Count | storage.googleapis.com/api/request\_count |
| gcs\_bucket/default\_metrics | Authentication count | Count | storage.googleapis.com/authn/authentication\_count |
| gcs\_bucket/default\_metrics | Object-ACL based access count | Count | storage.googleapis.com/authz/acl\_based\_object\_access\_count |
| gcs\_bucket/default\_metrics | ACLs usage | Count | storage.googleapis.com/authz/acl\_operations\_count |
| gcs\_bucket/default\_metrics | Object ACL changes | Count | storage.googleapis.com/authz/object\_specific\_acl\_mutation\_count |
| gcs\_bucket/default\_metrics | Received bytes | Byte | storage.googleapis.com/network/received\_bytes\_count |
| gcs\_bucket/default\_metrics | Sent bytes | Byte | storage.googleapis.com/network/sent\_bytes\_count |
| gcs\_bucket/default\_metrics | Object count | Count | storage.googleapis.com/storage/object\_count |
| gcs\_bucket/default\_metrics | Total byte seconds | Byte | storage.googleapis.com/storage/total\_byte\_seconds |
| gcs\_bucket/default\_metrics | Total bytes | Byte | storage.googleapis.com/storage/total\_bytes |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")