---
title: Google Cloud supported services
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new
scraped: 2026-02-24T21:17:00.783841
---

# Google Cloud supported services

# Google Cloud supported services

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Sep 23, 2024

Dynatrace version 1.230+

This section refers to Google Cloud service metrics that are available with Google Cloud version 1.0 integration.

* For Google Cloud service metrics that are available with earlier versions of the Google Cloud integration, see [Google Cloud supported service metrics (legacy)](/docs/ingest-from/google-cloud-platform/legacy/gcp-supported-service-metrics-legacy "Supported GCP service metrics, metrics configuration, DDU consumption, and preset dashboard availability").

## Prerequisites

[Deploy Dynatrace integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Supported services for metrics

After deploying the Dynatrace integration, you can get insights into Google Cloud services metrics collected from the Google Operations API to ensure health of your cloud infrastructure.

Below, see the list of Google Cloud supported services.

1

Services might have one entity, several entities, or none. For each entity, you can see metrics, properties, logs, errors, and many more in Dynatrace [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app "Monitor all cloud platforms at once.").

## Check available metrics

To check available metrics for a service, you need to

1. Find the extension in the [Hubï»¿](https://www.dynatrace.com/hub/?query=google&filter=all) and select it to open the overview page. See example: [Google Cloud Functionsï»¿](https://www.dynatrace.com/hub/detail/google-functions/?query=cloud+function&filter=all).
2. Scroll down to the bottom of the overview page of the extension to find the **Feature sets** section.
3. In the table, select the **default\_metrics** dropdown.
4. Now, you can check all available metrics for the chosen service.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")