---
title: Migrate from Google Cloud Functions 1.0 to Google Cloud k8s 1.0
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function-1-to-k8s-1
scraped: 2026-05-12T12:08:51.547330
---

# Migrate from Google Cloud Functions 1.0 to Google Cloud k8s 1.0

# Migrate from Google Cloud Functions 1.0 to Google Cloud k8s 1.0

* How-to guide
* 2-min read
* Published Nov 29, 2022

Dynatrace version 1.230+

Since function-based Google Cloud integration (v1.0) is being deprecated, users are expected to migrate to k8s-based Google Cloud integration (v1.0).

Both kinds of integration have the same features. Only the deployed components change. Data continuity is preserved, except for the time elapsed between deployments. You don't need to change anything in your dashboard or alerts as metric keys stay the same.

## Before you begin

It is recommended that you have the `activation-config.yaml` file that you used during the function deployment. Most of the parameters you need for a new deployment can be reused based on this file.

The `activation-config.yaml` file specifies the monitoring scope (services and feature sets). You need to specify the same monitoring scope in your new deployment to confirm that monitoring coverage does not change.

If you don't have the file, you can check the current monitoring scope in function deployment:

1. Find your monitoring function in Google Cloud. By default, its name is `dynatrace-gcp-monitor`.
2. Go to **Variables** tab.
3. Copy `ACTIVATION_CONFIG` variable and save it. You can use it as reference when setting monitoring scope (services and feature sets) for new deployment.

## Migration guide

1. Remove function-based Google Cloud integration.

   Rolling upgrade (deploying a new integration before removing the old one) is not recommended, as the metrics would be reported twice, which might affect your data.

   See [Uninstall](/managed/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy#uninstall "Set up monitoring for Google Cloud services using a Google Cloud Function.").

   Make sure that you have disabled all Google Cloud extensions in Dynatrace UI. Alternatively, you can add `--upgrade-extensions` option during deployment in step 3 when running `./deploy-helm.sh` deployment script.
2. Deploy k8s-based Google Cloud integration from scratch.

   See [Set up the Dynatrace Google Cloud metric and log integration on a new GKE Autopilot cluster](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").
3. Verify that k8s-based Google Cloud integration is working.

   See [Verify installation](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#verify "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

## Related topics

* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")