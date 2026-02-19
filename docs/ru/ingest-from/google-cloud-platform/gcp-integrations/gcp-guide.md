---
title: End-to-end guide for monitoring Google Cloud services integrating Operations Suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide
scraped: 2026-02-19T21:28:19.508598
---

# End-to-end guide for monitoring Google Cloud services integrating Operations Suite

# End-to-end guide for monitoring Google Cloud services integrating Operations Suite

* Latest Dynatrace
* Overview
* 2-min read
* Published Jan 17, 2022

Dynatrace perfectly integrates with Google Cloud to provide deep visibility into the workloads that are running on this platform.

## Google Cloud supported services

Dynatrace can analyze metrics from all services available in Google Operations API. To learn about monitoring the Google Cloud supported services, capabilities and configuration options, see [Google Cloud supported service metrics](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.").

## Google Cloud overview

Dynatrace provides the Google Cloud overview page. It includes views per Google Cloud project and lists of instances for VMs, SQLs, Cloud Functions, and Kubernetes.

If you are already monitoring Google Cloud and the overview is not available, you need to update the Google Cloud integration you have.

## Set up metric and log ingest

To start analyzing metrics and logs from all services available in the Google Operations API, see [Set up the Dynatrace Google Cloud metric and log integration on a new GKE Autopilot cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") Recommended.

For other deployment options, see

* [Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")
* [Set up the Dynatrace Google Cloud metric integration on a GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-metrics-only "Set up metric monitoring for Google Cloud services on a GKE cluster.")
* [Set up the Dynatrace Google Cloud log integration on a GKE cluster](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")
* [Deploy the Dynatrace Google Cloud metric integration in Google Cloud Function](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Set up monitoring for Google Cloud services in Google Cloud Functions.")

The [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") describes how to install version 1.0 of the Google Cloud integration on a GKE cluster. If you already have earlier versions installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

After deploying the integration, [you can push metrics to Dynatrace from multiple Google Cloud projects](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

To check if your monitoring function processes and sends logs to Dynatrace properly, see [Self-monitoring for the Dynatrace Google Cloud integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")