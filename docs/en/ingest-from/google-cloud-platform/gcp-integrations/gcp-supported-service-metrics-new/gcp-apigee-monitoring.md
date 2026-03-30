---
title: Google Cloud Apigee monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apigee-monitoring
scraped: 2026-03-05T21:38:15.589538
---

# Google Cloud Apigee monitoring


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

The following feature sets are available for Google Cloud Apigee.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| apigee\_googleapis\_com\_Environment/default\_metrics | Apigee anomaly event count | Count | apigee.googleapis.com/environment/anomaly\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee policy response latencies | MilliSecond | apigee.googleapis.com/policy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response latencies | MilliSecond | apigee.googleapis.com/proxy/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy request cumulative count | Count | apigee.googleapis.com/proxy/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee proxy response cumulative count | Count | apigee.googleapis.com/proxy/response\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response latencies | MilliSecond | apigee.googleapis.com/target/latencies |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target request cumulative count | Count | apigee.googleapis.com/target/request\_count |
| apigee\_googleapis\_com\_Proxy/default\_metrics | Apigee target response cumulative count | Count | apigee.googleapis.com/target/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee policy response latencies | MilliSecond | apigee.googleapis.com/policyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Percentile of Apigee proxy response latencies | MilliSecond | apigee.googleapis.com/proxyv2/latencies\_percentile |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy request cumulative count | Count | apigee.googleapis.com/proxyv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee proxy response cumulative count | Count | apigee.googleapis.com/proxyv2/response\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target request cumulative count | Count | apigee.googleapis.com/targetv2/request\_count |
| Deprecated apigee\_googleapis\_com\_ProxyV2/default\_metrics | Apigee target response cumulative count | Count | apigee.googleapis.com/targetv2/response\_count |

## Related topics

* Google Cloud integrations