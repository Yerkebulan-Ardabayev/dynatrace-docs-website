---
title: Monitor multiple Google Cloud projects
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects
scraped: 2026-05-12T11:51:51.977809
---

# Monitor multiple Google Cloud projects

# Monitor multiple Google Cloud projects

* How-to guide
* 3-min read
* Published Mar 12, 2021

You can push metrics to Dynatrace from multiple Google Cloud projects. For example, you can run `dynatrace-gcp-monitor` in a project dedicated to monitoring, and get metrics from production, stage, or development projects.

There are two methods for monitoring multiple Google Cloud projects, depending on the size of the environment you want to monitor:

* Large environmentsâsuggested multiproject method
* Standard environmentsâalternative method

## Large environments

To monitor large environments, you can make use of Google's metrics scope feature. You need to select the main scoping project (where the Google Cloud integration will be deployed) and configure the rest of the projects as monitored projects. See below for instructions.

To modify a metrics scope, you need to have the Monitoring Admin (roles/monitoring.admin) role's permissions for all projects involved.

1. In your Google Cloud console, select the main scoping project and go to the Monitoring service.
2. Select **Metrics Scope** settings from the left menu.
3. Select **Add Cloud projects to metrics scope**.
4. Select all the desired projects to be monitored by the main scoping project and add them.

Basically, you extend the metrics visibility from the main scoping project to all the monitored projects from your Google Cloud console. For details, see [Viewing metrics for multiple projectsï»¿](https://cloud.google.com/monitoring/settings).

The next step is to deploy the Google Cloud Monitor integration with the parameter `scopingProjectSupportEnabled` set to `true` in your configuration file. See [Main deployment](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.") or [Alternative deployment scenarios](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This approach should work up to roughly 375 moderately sized projects. If you want to monitor more projects, you'll have to set up multiple Google Cloud Monitor integrations in different main scoping projects, assigning each monitored project to one of them.

## Standard environments

There are two ways you can set up the standard monitoring: using the gcloud CLI or in the Google Cloud console. See below for instructions.

Prerequisites

Deploy Dynatrace integration in a [Kubernetes container](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

### Set up monitoring using the gcloud CLI

To add projects to monitoring using the gcloud CLI

1. Create IAM roles.

Be sure to replace `<your-desired-project-ID>` with the ID of your desired project.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/gcp_iam_roles/dynatrace-gcp-monitor-metrics-role.yaml



gcloud iam roles create dynatrace_monitor.metrics --project=<your-desired-project-ID> --file=dynatrace-gcp-monitor-metrics-role.yaml
```

2. Grant required IAM policies to the IAM service account for your desired projects.

Be sure to replace `<your-desired-project-ID>` with the ID of your desired project, and `<your-GCP-project-ID>` with the ID of the project where the IAM service account was created.

Kubernetes container deployment

Google Cloud Function deployment

```
gcloud projects add-iam-policy-binding <your-desired-project-ID> --member="serviceAccount:dynatrace-gcp-monitor-sa@<your-GCP-project-ID>.iam.gserviceaccount.com" --role=projects/<your-desired-project-ID>/roles/dynatrace_monitor.metrics
```

```
gcloud projects add-iam-policy-binding <your-desired-project-ID> --member="serviceAccount:dynatrace-gcp-service-custom@<your-GCP-project-ID>.iam.gserviceaccount.com" --role=projects/<your-desired-project-ID>/roles/dynatrace_monitor.metrics
```

3. Repeat step 1 and 2 for all the other projects you want to monitor.
4. Enable permission for service usage booking. Optional

If you want to set up service usage booking, you need to enable the [**serviceusage.services.use** permission for your IAM service accountï»¿](https://cloud.google.com/service-usage/docs/access-control#permissions).
For details about configuring `serviceUsageBooking` see [Parameters](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#param "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

It takes about a minute for the metrics from the newly configured projects to appear in Dynatrace.

For GKE deployment, you must restart your Kubernetes container after adding projects to monitoring.

### Set up monitoring in the Google Cloud console

Alternatively, you can grant access for all desired projects in the Google Cloud console.

To add projects to monitoring in the Google Cloud console

1. On your Google Cloud console, go to **IAM & Admin**.
2. Select a project you want to monitor, and add permissions for the IAM service account attached to the function.
3. Repeat step 2 for all the other projects you want to monitor.

For GKE deployment, you must restart your Kubernetes container after adding projects to monitoring.

## Related topics

* [Google Cloud integrations](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")