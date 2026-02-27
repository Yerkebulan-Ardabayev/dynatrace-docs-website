---
title: Google Cloud Router monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-router-monitoring
scraped: 2026-02-27T21:31:02.700485
---

# Google Cloud Router monitoring

# Google Cloud Router monitoring

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

The following feature sets are available for Google Cloud Router.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| nat\_gateway/default\_metrics | Allocated ports | Unspecified | router.googleapis.com/nat/allocated\_ports |
| nat\_gateway/default\_metrics | Closed connections count | Unspecified | router.googleapis.com/nat/closed\_connections\_count |
| nat\_gateway/default\_metrics | Received packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_received\_packets\_count |
| nat\_gateway/default\_metrics | Sent packets dropped count | Unspecified | router.googleapis.com/nat/dropped\_sent\_packets\_count |
| nat\_gateway/default\_metrics | NAT allocation failed | Unspecified | router.googleapis.com/nat/nat\_allocation\_failed |
| nat\_gateway/default\_metrics | New connections count | Unspecified | router.googleapis.com/nat/new\_connections\_count |
| nat\_gateway/default\_metrics | Open connections | Unspecified | router.googleapis.com/nat/open\_connections |
| nat\_gateway/default\_metrics | Port usage | Unspecified | router.googleapis.com/nat/port\_usage |
| nat\_gateway/default\_metrics | Received bytes count | Byte | router.googleapis.com/nat/received\_bytes\_count |
| nat\_gateway/default\_metrics | Received packets count | Unspecified | router.googleapis.com/nat/received\_packets\_count |
| nat\_gateway/default\_metrics | Sent bytes count | Byte | router.googleapis.com/nat/sent\_bytes\_count |
| nat\_gateway/default\_metrics | Sent packets count | Unspecified | router.googleapis.com/nat/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")