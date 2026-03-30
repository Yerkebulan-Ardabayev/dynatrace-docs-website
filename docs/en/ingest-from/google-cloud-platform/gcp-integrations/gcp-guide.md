---
title: End-to-end guide for monitoring Google Cloud services integrating Operations Suite
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide
scraped: 2026-03-03T21:24:19.522416
---

# End-to-end guide for monitoring Google Cloud services integrating Operations Suite


* Latest Dynatrace
* Overview
* 2-min read
* Published Jan 17, 2022

Dynatrace perfectly integrates with Google Cloud to provide deep visibility into the workloads that are running on this platform.

## Google Cloud supported services

Dynatrace can analyze metrics from all services available in Google Operations API. To learn about monitoring the Google Cloud supported services, capabilities and configuration options, see Google Cloud supported service metrics.

## Google Cloud overview

Dynatrace provides the Google Cloud overview page. It includes views per Google Cloud project and lists of instances for VMs, SQLs, Cloud Functions, and Kubernetes.

If you are already monitoring Google Cloud and the overview is not available, you need to update the Google Cloud integration you have.

## Set up metric and log ingest

To start analyzing metrics and logs from all services available in the Google Operations API, see Set up the Dynatrace Google Cloud metric and log integration on a new GKE Autopilot cluster Recommended.

For other deployment options, see

* Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster
* Set up the Dynatrace Google Cloud metric integration on a GKE cluster
* Set up the Dynatrace Google Cloud log integration on a GKE cluster.")
* Deploy the Dynatrace Google Cloud metric integration in Google Cloud Function

The main deployment describes how to install version 1.0 of the Google Cloud integration on a GKE cluster. If you already have earlier versions installed, you need to migrate.

After deploying the integration, you can push metrics to Dynatrace from multiple Google Cloud projects.

To check if your monitoring function processes and sends logs to Dynatrace properly, see Self-monitoring for the Dynatrace Google Cloud integration.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see Extending Dynatrace (Davis data units).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See DDUs for Log Monitoring for details.

## Related topics

* Set up Dynatrace on Google Cloud