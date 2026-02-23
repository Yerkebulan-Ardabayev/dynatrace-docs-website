---
title: Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function
scraped: 2026-02-23T21:38:26.879428
---

# Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions

# Deploy the Dynatrace Google Cloud metric integration in Google Cloud Functions

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Sep 06, 2022
* Deprecated

Dynatrace version 1.230+

Dynatrace Google Cloud metric integration in Google Cloud Functions is **not** supported anymore.

If you're using this kind of deployment, you should switch to k8s-based Google Cloud integration as soon as possible.
See [Migrate from Google Cloud Functions 1.0 to Google Cloud k8s 1.0](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function-1-to-k8s-1 "Migrate from Google Cloud Functions v1.0 to Google Cloud k8s v1.0.").

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), that provides Google Cloud monitoring for both metrics and logs, and where the deployment takes place in a GKE cluster, you can choose to set up monitoring for metrics only, in Google Cloud Cloud Function. Note that the Google Cloud Cloud Function deployment isn't recommended for large environments and doesn't support log forwarding.
In this scenario, you will be able run the deployment script either in Google Cloud Shell or in bash. After installation, you'll get metrics, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to deploy version 1.0 of the Dynatrace Google Cloud integration in Google Cloud Cloud Function.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy "Set up monitoring for Google Cloud services using a Google Cloud Function.") of the Google Cloud Monitor installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Prerequisites

### Tools

You can deploy the Dynatrace Google Cloud integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role and use it to deploy `dynatrace-gcp-monitor`.

To create a custom role

1. Create a YAML file named `dynatrace-gcp-monitor-cloud-function-deployment-role.yaml` with the following content:

   dynatrace-gcp-monitor-cloud-function-deployment-role.yaml

   ```
   title: Dynatrace GCP Monitor cloud function deployment role



   description: Role for Dynatrace GCP Monitor cloud function deployment



   stage: GA



   includedPermissions:



   - appengine.applications.get



   - appengine.applications.create



   - cloudfunctions.functions.create



   - cloudfunctions.functions.get



   - cloudfunctions.functions.list



   - cloudfunctions.functions.sourceCodeSet



   - cloudfunctions.functions.update



   - cloudfunctions.functions.getIamPolicy



   - cloudfunctions.operations.get



   - cloudfunctions.operations.list



   - cloudscheduler.locations.list



   - cloudscheduler.jobs.list



   - cloudscheduler.jobs.create



   - cloudscheduler.jobs.get



   - cloudscheduler.jobs.delete



   - pubsub.topics.list



   - pubsub.topics.create



   - pubsub.topics.update



   - secretmanager.secrets.list



   - secretmanager.versions.add



   - secretmanager.secrets.create



   - secretmanager.versions.list



   - secretmanager.secrets.getIamPolicy



   - secretmanager.secrets.setIamPolicy



   - resourcemanager.projects.get



   - resourcemanager.projects.getIamPolicy



   - resourcemanager.projects.setIamPolicy



   - serviceusage.services.enable



   - iam.serviceAccounts.actAs



   - iam.serviceAccounts.list



   - iam.serviceAccounts.create



   - iam.serviceAccounts.getIamPolicy



   - iam.serviceAccounts.setIamPolicy



   - iam.roles.list



   - iam.roles.create



   - iam.roles.update



   - monitoring.dashboards.list



   - monitoring.dashboards.create
   ```
2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

   ```
   gcloud iam roles create dynatrace_monitor.cloud_function_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-cloud-function-deployment-role.yaml
   ```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Dynatrace permissions

[Create an API tokenï»¿](https://dt-url.net/be03q3a) and [enable the following permissionsï»¿](https://dt-url.net/c023q1m):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extension monitoring configurations**
  + **Write extension monitoring configurations**
  + **Read extension environment configurations**
  + **Write extension environment configurations**

### Dynatrace URL

Determine the URL for your environment.

* For Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
* For Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

To determine `<your-environment-id>`, see [environment IDï»¿](https://dt-url.net/ej43qge).

## Install

You can deploy the Dynatrace Google Cloud integration in Google Cloud Shell or in bash. To set up integration, follow the instructions below.

For bash deployment, be sure to restart the console and [initialize Cloud SDKï»¿](https://dt-url.net/ac43q0f) before you start installation.

To initialize Cloud SDK, run

```
gcloud init
```

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the deployment package**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#dwld "Set up monitoring for Google Cloud services in Google Cloud Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure deployment**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#configure-deployment "Set up monitoring for Google Cloud services in Google Cloud Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function#script "Set up monitoring for Google Cloud services in Google Cloud Functions.")

### Step 1 Download the deployment package

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/tag/release-1.1.8/download/function-deployment-package.zip" -O function-deployment-package.zip; unzip function-deployment-package.zip; chmod a+x *.sh
```

### Step 2 Configure deployment

1. Adjust the parameters in the `activation-config.yaml` file from the deployment package.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.
2. Choose which services you want Dynatrace to monitor.

By default, the Google Cloud integration starts monitoring a series of selected services. Uncomment any additional services you want Dynatrace to monitor in the `activation-config.yaml` file.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Run the deployment script

Version upgrade of extensions is done by default. To keep the versions of existing extensions, run the script with the `--without-extensions-upgrade` parameter.

```
./setup.sh
```

The script may ask you for confirmations during deployment. For CI/CD purposes, you can add the `-d` option to make the script noninteractive.

After deploying the integration, you can see metrics from monitored services. If you want to change the monitoring scope (services & featureSets) or update the Google Cloud integration, see [Change deployment settings](#manage) below.

## Verify installation

To check whether installation was successful

1. In your Google Cloud console, go to Cloud Functions and make sure that `dynatrace-gcp-monitor` is there.
2. Select the newly deployed Google Cloud Monitor function and go to **Logs** to make sure there are no error messages.

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable custom events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for GCP alerts and turn on **On/Off** for the alerts you want to activate.

## View enabled services

To find the list of currently enabled services, go to Cloud Function in your Google Cloud console, and check the `ACTIVATION_CONFIG` environment variable.

## Update services



Adding, removing and updating versions of existing services is done by modyfing the corresponding list of services and redeploying.

1. Apply your changes to `activation-config.yaml` by commenting or uncommenting configuration blocks corresponding to specific services.
   Terminology within the file includes:

   * `service`: represents Google Cloud service name you want to monitor. Services are grouped by extensions, but you can decide what you need to monitor on a lower level (`featureSets`)
   * `featureSet`: a set of metrics for a given service. `default_metrics` is a default `featureSet` with a recommended set of metrics to be monitored. In more specific use cases, you can consider monitoring such sets as `istio featureSet` for `gae_instance service`
   * `filter_conditions`: a service-level filter that enables you to narrow the monitoring scope. It is based on the [Google Cloud Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US).  
     Example:

     ```
     filter_conditions:



     resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
     ```
2. Update monitored services by running the script below.

   Version upgrade of extensions is done by default. To keep the versions of existing extensions, run the script with the `--without-extensions-upgrade` parameter.

   ```
   ./setup.sh
   ```
3. If you removed services from monitoring, find the relevant extensions in Dynatrace Hub and delete them to remove service-specific assets (such as dashboards and alerts).

### Example

In the following example

* The `gae_instance` service is disabled.
* For the `gce_instance` service, only two feature sets are enabled: `default_metrics` and `istio`.

```
# Google App Engine Instance



#- service: gae_instance



#  featureSets:



#    - default_metrics



#  vars:



#    filter_conditions: ""



# Google VM Instance



- service: gce_instance



featureSets:



- default_metrics



#    - agent



#    - firewallinsights



- istio



#    - uptime_check



vars:



filter_conditions: ""
```

For a complete list of the Google Cloud supported services, see [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new#services "Monitor Google Cloud services with Dynatrace and view available metrics.").

## Change deployment settings

To add or remove services, or to update parameters, you need to redeploy the integration.

1. Apply your changes to `activation-config.yaml`.

   Be sure to use the same value for the `FUNCTION_NAME` parameter as before.
2. [Rerun the deployment script](#script).

## Verification

To investigate potential deployment and connectivity issues

1. [Verify installation](#verify)
2. [Enable self-monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.") Optional
3. Check the `dynatrace_gcp_<date_time>.log` log file created during the installation process.

* This file will be created each time the installation script runs.
* The debug information won't contain sensitive data such as the Dynatrace access key.
* If you are contacting a Dynatrace product expert via live chat:

  + Make sure to provide the `dynatrace_gcp_<date_time>.log` log file described in the previous step.
  + Provide version information.

    - For issues during installation, check the `version.txt` file.
    - For issues during runtime, [check function logs](#verify).

## Uninstall

1. Go to your installation directory and run the command below.

```
./uninstall.sh
```

2. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

## Monitoring consumption

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")