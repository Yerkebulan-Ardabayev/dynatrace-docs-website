---
title: Deploy the Dynatrace Google Cloud metric integration using a Google Cloud Function (legacy)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/legacy/deploy-with-google-cloud-function-legacy
scraped: 2026-05-12T12:08:49.693134
---

# Deploy the Dynatrace Google Cloud metric integration using a Google Cloud Function (legacy)

# Deploy the Dynatrace Google Cloud metric integration using a Google Cloud Function (legacy)

* How-to guide
* 5-min read
* Published Mar 12, 2021
* Deprecated

This page describes how to install Google Cloud Function version 0.1, which is scheduled for deprecation.

* If you are making a fresh installation, you should [deploy Google Cloud Function version 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-with-google-cloud-function "Set up monitoring for Google Cloud services in Google Cloud Functions.").
* If you already have version 0.1 of the Google Cloud Function installed, you should [migrate to Google Cloud Function version 1.0](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Install

To set up the Dynatrace integration as a Google Cloud Function, follow the instructions below.

Deploy in Google Cloud Shell

Deploy in bash

### Prerequisites

* [Install yq version 4.9.8ï»¿](https://dt-url.net/411p0nlq)  
  **Example command to install yq:**

  ```
  sudo wget https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64 -O /usr/bin/yq && sudo chmod +x /usr/bin/yq
  ```
* [Install jqï»¿](https://dt-url.net/cl1203zc)
* [Create an API tokenï»¿](https://dt-url.net/be03q3a)
* [Enable the following permissions for the API tokenï»¿](https://dt-url.net/c023q1m): `Ingest metrics` (API v2), `Read configuration` (API v1), and `Write configuration` (API v1)
* Determine the URL for your environment.

  + For Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/`
  + For Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/`

  To determine `<your-environment-id>`, see [environment IDï»¿](https://dt-url.net/ej43qge).
* Running the deployment script requires a list of permissions. You can create a custom role (instruction below) and use it to deploy `dynatrace-gcp-monitor`.

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

Be sure to add this role to your GCP user.

To deploy the Dynatrace GCP function in Google Cloud Shell, download and run the installation script below, making sure to replace `<VERSION>` with the release version you want to download, for example `0.1.19`.

Be sure to choose one of the versions before `release-1.0.0`, as the newer versions require [different installation instructions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

The Dynatrace GCP Monitor uses [Cloud Schedulerï»¿](https://dt-url.net/n483qgj), which requires the App Engine application. If you don't have App Engine installed, the installer script will prompt you to create App Engine and select the region where you want the installer script to run.

The installation script will prompt for the following parameters:

* **GCP project ID** - The ID of the Google Cloud project where you want to deploy the Dynatrace GCP Monitor. The default is set to the current project ID, for the gcloud CLI.
* **Function size** - The amount of memory that you want to allocate to the function. You can select one of the following:

  + `[s]` - Small (allocates 256 MB memory to the function). Select this option if you have up to 500 GCP service instances.
  + `[m]` - Medium (allocates 512 MB memory to the function). Select this option if you have up to 1,000 GCP service instances.
  + `[l]` - Large (allocates 2,048 MB memory to the function). Select this option if you have up to 5,000 GCP service instances.

    You can adjust the amount of memory after installation.
* **Dynatrace tenant URI** - Your Dynatrace environment URL. See **Prerequisites** for details.
* **Dynatrace API token** - Your Dynatrace API token. See **Prerequisites** for details.

### Prerequisites

* [Install jqï»¿](https://dt-url.net/cl1203zc)
* [Install yq 4.9.xï»¿](https://dt-url.net/411p0nlq)  
  **Example command to install yq:**

  ```
  sudo wget https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64 -O /usr/bin/yq && sudo chmod +x /usr/bin/yq
  ```
* [Install Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [Create an API tokenï»¿](https://dt-url.net/be03q3a)
* [Enable the `Ingest metrics`, `Read configuration`, and `Write configuration` permissions for the API tokenï»¿](https://dt-url.net/c023q1m)
* Determine the URL for your environment.

**For SaaS:**  
`https://<your-environment-id>.live.dynatrace.com/`

**For Managed:**  
`https://<your-domain>/e/<your-environment-id>/`

To determine `<your-environment-id>`, see [environment IDï»¿](https://dt-url.net/ej43qge).

* Running the deployment script requires a list of permissions. You can create a custom role (instruction below) and use it to deploy `dynatrace-gcp-monitor`.

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

Be sure to add this role to your GCP user.

To deploy the Dynatrace GCP function in bash

1. Restart the console and [initialize Cloud SDKï»¿](https://dt-url.net/ac43q0f).

```
gcloud init
```

2. Download and run the installation script below.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

The Dynatrace GCP Monitor uses [Cloud Schedulerï»¿](https://dt-url.net/n483qgj), which requires the App Engine application. If you don't have App Engine installed, the installer script will prompt you to create App Engine and select the region where you want the installer script to run.

The installation script will prompt for the following parameters:

* **GCP project ID** - The ID of the Google Cloud project where you want to deploy the Dynatrace GCP Monitor. The default is set to the current project ID, for the gcloud CLI.
* **Function size** - The amount of memory that you want to allocate to the function. You can select one of the following:

  + `[s]` - Small (allocates 256 MB memory to the function). Select this option if you have up to 500 GCP service instances.
  + `[m]` - Medium (allocates 512 MB memory to the function). Select this option if you have up to 1,000 GCP service instances.
  + `[l]` - Large (allocates 2,048 MB memory to the function). Select this option if you have up to 5,000 GCP service instances.

    You can adjust the amount of memory after installation.
* **Dynatrace tenant URI** - Your Dynatrace environment URL. See **Prerequisites** for details.
* **Dynatrace API token** - Your Dynatrace API token. See **Prerequisites** for details.

After deploying the integration, you can see metrics from monitored services. If you want to add services to monitoring, see [Expand monitoring](#expand) below.

## Verify installation

To check whether installation was successful

1. In your Google Cloud console, go to Cloud Functions and make sure that `dynatrace-gcp-monitor` is there.
2. Select the newly deployed function and go to **Logs** to make sure there are no error messages.

## Expand monitoring

There are two ways to add services to Dynatrace monitoring when using a Google Cloud Function: via the service configuration file or using the GCP console. See below for instructions.

In the service configuration file

In the Google Cloud console

To add services in the service configuration file

1. Download the `activation-config.yaml` service configuration file, making sure to replace `<VERSION>` with your function release version.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/dynatrace-gcp-monitor.zip" -O dynatrace-gcp-monitor.zip; unzip -p dynatrace-gcp-monitor.zip activation-config.yaml >activation-config.yaml
```

2. Edit the `activation.metrics.services` section in `activation-config.yaml` by uncommenting the services you want to monitor.
3. Download and run the `dynatrace-gcp-monitor` installation script in the same folder where you downloaded `activation-config.yaml`.

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/download/release-<VERSION>/setup.sh" -O setup.sh; chmod a+x *.sh; ./setup.sh
```

To add services in the Google Cloud console

1. Go to **Cloud Functions**
2. Select **dynatrace-gcp-monitor**
3. Select **Edit**
4. Under **Variables, networking and advanced settings**, select **Environment variables**
5. Select **Runtime environment variables**
6. Modify the value for **GCP services** to include the services or configurations you want to monitor (for example, `cloud_function`, `gce_instance/agent`).
7. Select **Next**, then select **Deploy**

## Related topics

* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")