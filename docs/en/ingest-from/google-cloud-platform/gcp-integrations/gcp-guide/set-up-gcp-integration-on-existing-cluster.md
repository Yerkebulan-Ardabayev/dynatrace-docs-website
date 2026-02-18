---
title: Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster
scraped: 2026-02-18T05:43:24.156174
---

# Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster

# Set up the Dynatrace Google Cloud log and metric integration on an existing GKE cluster

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), where the deployment script runs in a new automatically created GKE Autopilot cluster, you can choose to run the deployment script on an existing standard GKE or GKE Autopilot cluster. In this scenario, you will set up Google Cloud monitoring for metrics and logs in Google Cloud Shell. During setup, a new Pub/Sub subscription will be created. GKE will run two containers: a metric forwarder and a log forwarder. After installation, you'll get metrics, logs, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

Dynatrace version 1.230+

This page describes how to install version 1.0 of the Google Cloud integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace Google Cloud log integration supports up to 8 GB of data processing per hour (with base resourcesâwithout scaling). With bigger loads, messages will start to be retained in the PubSub Subscription. To measure latency, look for these metrics: `Oldest unacked message age` and `Unacked messages`. For scaling recommendations, see the [scaling guide](#scalingguide) below.

Dynatrace Google Cloud metric integration supports up to 50 Google Cloud projects with the standard deployment. To monitor larger environments, you need to enable metrics scope. See [Monitor multiple Google Cloud projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

## Prerequisites

To deploy the integration, you need to make sure the following requirements are met on the machine where you are running the installation.

* Linux OS only
* Internet access
* GKE Cluster access
* Dynatrace environment access

  You need to configure the Dynatrace endpoint (environment, cluster or ActiveGate URL) to which the GKE cluster should send metrics and logs. Make sure that you have direct network access or, if there is a proxy or any other component present in between, that communication is not affected.

### Tools

You can deploy the Dynatrace GCP integration in Google Cloud Shell or in bash.

If you use bash, you need to install:

* [Google Cloud SDKï»¿](https://dt-url.net/e8110336)
* [kubectlï»¿](https://kubernetes.io/docs/tasks/tools/)
* [helmï»¿](https://helm.sh/docs/intro/install/)
* [jq (version 1.6)ï»¿](https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64)
* [yq (version 4.9.x+)ï»¿](https://github.com/mikefarah/yq/releases/download/v4.9.8/yq_linux_amd64)
* curl
* unzip

### Google Cloud permissions

Running the deployment script requires a list of permissions. You need to create a custom role (see below) and use it to deploy `dynatrace-gcp-monitor`.

1. Create a YAML file named `dynatrace-gcp-monitor-helm-deployment-role.yaml` with the following content:

dynatrace-gcp-monitor-helm-deployment-role.yaml

```
title: Dynatrace GCP Monitor helm deployment role



description: Role for Dynatrace GCP Monitor helm and pubsub deployment



stage: GA



includedPermissions:



- container.clusters.get



- container.configMaps.create



- container.configMaps.delete



- container.configMaps.get



- container.configMaps.update



- container.deployments.create



- container.deployments.delete



- container.deployments.get



- container.deployments.update



- container.namespaces.create



- container.namespaces.get



- container.pods.get



- container.pods.list



- container.secrets.create



- container.secrets.delete



- container.secrets.get



- container.secrets.list



- container.secrets.update



- container.serviceAccounts.create



- container.serviceAccounts.delete



- container.serviceAccounts.get



- iam.roles.create



- iam.roles.list



- iam.roles.update



- iam.serviceAccounts.actAs



- iam.serviceAccounts.create



- iam.serviceAccounts.getIamPolicy



- iam.serviceAccounts.list



- iam.serviceAccounts.setIamPolicy



- pubsub.subscriptions.create



- pubsub.subscriptions.get



- pubsub.subscriptions.list



- pubsub.topics.attachSubscription



- pubsub.topics.create



- pubsub.topics.getIamPolicy



- pubsub.topics.list



- pubsub.topics.setIamPolicy



- pubsub.topics.update



- resourcemanager.projects.get



- resourcemanager.projects.getIamPolicy



- resourcemanager.projects.setIamPolicy



- serviceusage.services.enable



- serviceusage.services.get



- serviceusage.services.list



- serviceusage.services.use
```

Each group of permissions is used to handle the different resources included in the integration. Creation and access are for new resources, update is for reusing existing resources, and deletion is for uninstalling.

* container.configMaps: for mapping secrets and other variables used by the containers.
* container.deployments: for the K8s' deployment within the cluster (which includes the pods, containers, etc.).
* container.namespaces: for the K8s namespace in which we are deploying the resources.
* container.pods: for the K8s pods.
* container.secrets: for the K8s secrets in which to store the data-sensitive variables.
* container.serviceAccounts: for the SA to be taken in the K8s context.
* iam.roles: for the necessary permissions for data collection.
* iam.serviceAccounts: for the general context SA.
* resourcemanager.projects: for handling the project in which we are deploying our integration.
* serviceusage.services: for handling the services' APIs.
* pubsub.subscriptions: for the PubSub subscription we are using to collect and ingest logs.
* pubsub.topics: for the PubSub topic we are using to collect and ingest logs.

2. Run the command below, replacing `<your_project_ID>` with the project ID where you want to deploy the Dynatrace integration.

```
gcloud iam roles create dynatrace_monitor.helm_deployment --project=<your_project_ID> --file=dynatrace-gcp-monitor-helm-deployment-role.yaml
```

Be sure to add this role to your Google Cloud user. For details, see [Grant or revoke a single roleï»¿](https://dt-url.net/vx03vid).

### Google Cloud settings

The location where you deploy the integration determines whether you need make any additional settings.

#### Deploy on an existing GKE Autopilot cluster

If you deploy the integration on an existing GKE Autopilot cluster, you don't need to make any additional settings.

#### Deploy on an existing GKE standard cluster

If you deploy the integration on an existing GKE standard cluster, you need to

* [Enable Workload Identity on a clusterï»¿](https://dt-url.net/2j23qqv)
* [Enable `GKE_METADATA` on the GKE node poolsï»¿](https://dt-url.net/an43q2s)

### Configure log export

1. Run the following shell script in the Google Cloud project you've selected for deployment.

Be sure to replace `<your-subscription-name>` and `<your-topic-name>` with your own values.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Configure [log exportï»¿](https://dt-url.net/4743r02) to send the desired logs to the Google Cloud Pub/Sub topic created above.

### Dynatrace permissions

You need to create a token with a set of permissions.

1. Go to **Access tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Under **Template**, select `GCP Services Monitoring`.
5. Select **Generate**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

Alternatively, you can create the token and add permissions manually.

Add manually

[Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permissions](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."):

* API v1:

  + **Read configuration**
  + **Write configuration**
* API v2:

  + **Ingest metrics**
  + **Read extensions**
  + **Write extensions**
  + **Read extensions monitoring configuration**
  + **Write extensions monitoring configuration**
  + **Read extensions environment configuration**
  + **Write extensions environment configuration**
  + **Ingest logs**
  + **Manage metadata of Hub items**
  + **Read Hub related data**
  + **Install and update Hub items**

To monitor logs from multiple projects, you need to create **Log Routing Sinks** in each source project selecting as a destination for your main project (in which you also deployed the integration and the PubSub Topic and Subscription).
For more information, see [Route logs to supported destinationsï»¿](https://dt-url.net/cl038gj).

### Log ingestion

* Determine where log ingestion will be performed, according to your deployment. This distinction is important when configuring the [parameters](#param) for this integration.

  + **For SaaS deployments:** SaaS log ingest, where log ingestion is performed directly through the Cluster API. Recommended
  + **For Managed deployments:** You can use an existing ActiveGate for log ingestion. For information on how to deploy it, see [ActiveGate installation](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

Because of GCP's implementation of Cloud Function 2nd gen, logs from those resources will be linked to the underlying Cloud Run instances. Both extensions will have to be enabled.

To learn more, visit [Google Cloud Functions version comparisonï»¿](https://dt-url.net/b6038q5).

## Install

Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#dwld "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#param "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect your Kubernetes cluster**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#connect "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-on-existing-cluster#script "Deploy log and metric monitoring for Google Cloud services on an existing standard GKE or GKE Autopilot cluster")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

1. The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor`and edit the `values.yaml` file, setting the required and optional parameter values as follows.

   You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

   **Parameter name**

   **Description**

   **Default value**

   `parallelProcesses`

   Optional Number of parallel processes to run the whole log monitoring loop

   `1`

   `numberOfConcurrentLogForwardingLoops`

   Optional Number of workers pulling logs from pubsub concurrently and pushing them to Dynatrace

   `5`

   `numberOfConcurrentMessagePullCoroutines`

   Optional Number of concurrent coroutines to pull messages from pub/sub

   `10`

   `numberOfConcurrentPushCoroutines`

   Optional Number of concurrent coroutines to push messages to Dynatrace

   `5`

   `gcpProjectId`

   Required The ID of the GCP project you've selected for deployment.

   Your current project ID

   `deploymentType`

   Required Leave to `all`.

   `all`

   `dynatraceAccessKey`

   Required Your [Dynatrace API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the [required permissions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#api "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

   `dynatraceUrl`

   Required For SaaS log/metric ingestion, it's your environment URL (`https://<your-environment-id>.live.dynatrace.com`).

   `logsSubscriptionId`

   Required The ID of your log Sink Pub/Sub subscription. For details, see [Configure log export](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#pubsub "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

   `dynatraceLogIngestUrl`

   Optional You can set it if you want to ingest logs separately from metrics.For SaaS log ingestion, it's your environment URL (`https://<your_environment_ID>.live.dynatrace.com`).

   `dynatraceAccessKeySecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceAccessKey`.

   `dynatraceUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceUrl`.

   `dtSecurityContext`

   Optional Assign the attribute value used for data segmentation, analysis, and permission mapping within the Dynatrace platform. Refer to [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") for more information. If left empty, the value of `gcpProjectId` will be assigned automatically.

   Value of `gcpProjectId`

   `dynatraceLogIngestUrlSecretName`

   Optional You can specify the key to fetch the endpoint from GCP Secret Manager, instead of using `dynatraceLogIngestUrl`.

   `requireValidCertificate`

   Optional If set to `true`, Dynatrace requires the SSL certificate of your Dynatrace environment.For SaaS log ingestion, we recommend leaving the default value.

   `true`

   `selfMonitoringEnabled`

   Optional Send custom metrics to GCP to quickly diagnose if `dynatrace-gcp-monitor` processes and sends metrics/logs to Dynatrace properly.For details, see [Self-monitoring metrics for the Dynatrace GCP integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

   `false`

   `serviceAccount`

   Optional Name of the service account to be created.

   `dockerImage`

   OptionalDynatrace GCP Monitor docker image. We recommend using the default value, but you can adapt it if needed.

   `dynatrace/dynatrace-gcp-monitor:v1-latest`

   `logIngestContentMaxLength`

   Optional The maximum content length of a log event. Should be less than or equal to the setting on your Dynatrace environment.

   `8192`

   `logIngestAttributeValueMaxLength`

   Optional The maximum length of the log event attribute value. If it exceeds the server limit, content will be truncated.

   `250`

   `logIngestRequestMaxEvents`

   Optional The maximum number of log events in a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `5000`

   `logIngestRequestMaxSize`

   Optional The maximum size in bytes of a single payload to the logs ingestion endpoint. If it exceeds the server limit, payload will be rejected with code `413`.

   `1048576`

   `logIngestEventMaxAgeSeconds`

   Optional Determines the maximum age of a forwarded log event. Should be less than or equal to the setting on your Dynatrace environment.

   `86400`

   `printMetricIngestInput`

   Optional If set to `true`, the GCP Monitor outputs the lines of metrics to stdout.

   `false`

   `serviceUsageBooking`

   Optional Service usage booking is used for metrics and determines a caller-specified project for quota and billing purposes. If set to `source`, monitoring API calls are booked in the project where the Kubernetes container is running. If set to `destination`, monitoring API calls are booked in the project that is monitored. For details, see [Monitor multiple GCP projects - Standard environments - Step 4](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `source`

   `useProxy`

   Optional Depending on the value you set for this flag, the GCP Monitor will use the following proxy settings: Dynatrace (set to `DT_ONLY`), GCP API (set to `GCP_ONLY`), or both (set to `ALL`).

   By default, proxy settings are not used.

   `httpProxy`

   Optional The proxy HTTP address; use this flag in conjunction with `USE_PROXY`.

   `httpsProxy`

   Optional The proxy HTTPS address; use this flag in conjunction with `USE_PROXY`.

   `gcpServicesYaml`

   Optional Configuration file for GCP services.

   `queryInterval`

   Optional Metrics polling interval in minutes. Allowed values: `1` - `6`

   `3`

   `scopingProjectSupportEnabled`

   Optional Set to `true` when metrics scope is configured, so metrics will be collected from all projects added to the metrics scope.For details, see [Monitor multiple GCP projects - Large environments](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/monitor-multiple-projects "Push metrics to Dynatrace from multiple Google Cloud projects.").

   `false`

   `excludedProjects`

   Optional Comma-separated list of projects to be excluded from monitoring (for example, `<project_A>,<project_B>`)

   `excludedMetricsAndDimensions`

   Optional Yaml formatted list of metrics and their dimensions to be excluded for monitoring.

   `metricAutodiscovery`

   Optional If set to `true`, the GCP Monitor will run metric auto-discovery mode, expanding your options for selecting metrics to monitor. For more information, see [Monitor GCP projects using auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.").

   `false`
2. Choose which services you want Dynatrace to monitor.

   By default, the Dynatrace Google Cloud integration starts monitoring a set of selected services. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services.

For DDU consumption information, see [Monitoring consumption](#ddu).

### Step 3 Connect your Kubernetes cluster

To connect to your existing GKE standard cluster or existing GKE Autopilot cluster, run the command below, making sure to replace

* `<cluster>` with your cluster name
* `<region>` with the region where your cluster is running
* `<project>` with the project ID where your cluster is running

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

For details, see [Configuring cluster access for kubectlï»¿](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Step 4 Run the deployment script

The deployment script will create an IAM service account with the necessary roles and deploy `dynatrace-gcp-monitor` to your GKE cluster. The latest versions of Google Cloud extensions will be uploaded.

You have two options:

* Run the deployment script without parameters if you want to use the default values provided (`dynatrace-gcp-monitor-sa` for the IAM service account name and `dynatrace_monitor` for the IAM role name prefix):

```
cd helm-deployment-package



./deploy-helm.sh
```

* Run the deployment script with parameters if you want to set your own values (be sure to replace the placeholders with your desired values):

```
cd helm-deployment-package



./deploy-helm.sh [--role-name <role-to-be-created/updated>]
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --without-extensions-upgrade
```

## Verify installation

To check whether installation was successful

1. Check if the container is running.

   After the installation, it may take couple of minutes until the container is up and running.

   ```
   kubectl -n dynatrace get pods
   ```
2. Check the container logs for errors or exceptions. You have two options:

In the Kubernetes CLI

In your Google Cloud console

Run the following commands.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-metrics



kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

To check the container logs for errors in your Google Cloud console

1. Go to **Logs explorer**.
2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-metrics"` (for metric ingest logs)
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"` (for log ingest logs)

3. Check if dashboards are imported.

   Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Choose services for metrics monitoring

### Services enabled by default

Monitoring of following services will be enabled during deployment of Google Cloud Monitor:

* [Google APIs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-apis-monitoring "Monitor Google Cloud APIs and view available metrics.")
* [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine/app-engine-monitoring "Monitor Google App Engine and view available metrics.")
* [Google BigQuery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-bigquery-monitoring "Monitor Google BigQuery and view available metrics.")
* [Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/cloud-functions-monitoring "Monitor Google Cloud Functions and view available metrics.")
* [Google Cloud Run](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun/cloud-run-monitoring "Monitor Google Cloud Run and view available metrics.")
* [Google Cloud Storage](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-storage-monitoring "Monitor Google Cloud Storage and view available metrics.")
* [Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine/compute-engine-monitoring "Monitor Google Compute Engine and view available metrics.")
* [Google Firestore in Datastore mode](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-in-datastore-mode-monitoring "Monitor Google Cloud Firestore in Datastore mode and view available metrics.")
* [Google Filestore](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-filestore-monitoring "Monitor Google Filestore and view available metrics.")
* [Google Kubernetes Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke/google-kubernetes-engine-monitoring "Monitor Google Kubernetes Engine and view available metrics.")
* [Google Cloud Load Balancing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-load-balancing-monitoring "Monitor Google Cloud Load Balancing and view available metrics.")
* [Google Cloud Pub/Sub](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-monitoring "Monitor Google Cloud Pub/Sub and view available metrics.")
* [Google Cloud Pub/Sub Lite](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-pub-sub-lite-monitoring "Monitor Google Cloud Pub/Sub Lite and view available metrics.")
* [Google Cloud SQL](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-cloud-sql "Monitor Google Cloud SQL and view available metrics.")

There are more service integrations available, but need to be enabled. Go to [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.") for a list of supported services. Next section describes how to manage them. For an alternative approach, consider leveraging [auto-discovery](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/gcp-autodiscovery "Push any metrics to Dynatrace from Google Cloud projects.") to extend your metric coverage.

### Manage enabled services

You can manage enabled services via Dynatrace Hub.

Filter for "gcp"âyou'll find annotations in the results for items that are already available in your environment.

To enable a new service, select it in Hub and then install it.

You can also disable a service via Dynatrace Hub.

To see if the services need updating, open them in Hub and check release notes. The updates can include new metrics, new assets like dashboards, or other changes.

All changes to enabled services are applied to Google Cloud Monitor within few minutes.

#### Feature sets & available metrics

To see what metrics are included for specific service, check [Google Cloud supported services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics."). By default, only `defaultMetrics` feature set is enabled. To enable additional feature sets, you have to uncomment them in `values.yaml` file and redeploy whole Google Cloud Monitor.

Current configuration of feature sets can be found in cluster's ConfigMap named `dynatrace-gcp-function-config`.

#### Advanced scope management

To further refine monitoring scope, you can use `filter_conditions` field in `values.yaml` file. This requires Google Cloud Monitor to be redeployed. See [Google Cloud Monitoring filtersï»¿](https://cloud.google.com/monitoring/api/v3/filters?hl=en_US) for syntax.

Example:

```
filter_conditions:



resource.labels.location = "us-central1-c" AND resource.labels.namespace_name = "dynatrace"
```

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. Select **Anomaly detection** > **Metric events**.
3. Filter for Google Cloud alerts and turn on **On/Off** for the alerts you want to activate.

## View metrics and logs

After deploying the integration, depending on your deployment type, you can:

* See metrics from monitored services: go to **Metrics** and filter by `gcp`.
* View and analyze Google Cloud logs: in Dynatrace, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and, to look for Google Cloud logs, filter by `cloud.provider: gcp`.

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Run the command below, making sure to replace `<your-helm-release>` with the value from the previous step.

   ```
   helm upgrade <your-helm-release> dynatrace-gcp-monitor -n dynatrace
   ```

For details, see [Helm upgradeï»¿](https://helm.sh/docs/helm/helm_upgrade/).

### Change deployment type

To change the deployment type (`all`, `metrics`, or `logs`)

1. Find out what Helm release version you're using.

   ```
   helm ls -n dynatrace
   ```
2. Uninstall the release.

   Be sure to replace `<your-helm-release>` with the release name from the previous output.

   ```
   helm uninstall <your-helm-release> -n dynatrace
   ```
3. Edit `deploymentType` in `values.yaml` with the new value and save the file.
4. Run the deployment command again. For details, see [Run the deployment script](#script).

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
    - For issues during runtime, [check container logs](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp "Determine if your self-monitoring function is properly processing and sending logs to Dynatrace.").

## Scaling guide for logs

The default container with 1.25vCPU and 1Gi (with default configuration) can handle 8 GB of log throughput per hour. Achieving more throughput requires allocating more resources to the container (scale up), increasing the number of container replicas (scale out), and changing configuration numbers to use allocated resources efficiently. All config variables can be found and changed in `dynatrace-gcp-monitor-config`.

The following table presents tested configuration and achieved throughput with scaled up&out containers:

Achieved throughput

Machine resources

Replica sets

Config variable values

~8MB/s => ~480MB/min

4vCPU 4Gi RAM

1

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~25MB/s => ~1.5GB/min => ~2TB/day

4vCPU 4Gi RAM

4

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

~46MB/s => ~2.7GB/min => ~4TB/day

4vCPU 4Gi RAM

6

`PARALLEL_PROCESSES=4`,  
 `NUMBER_OF_CONCURRENT_MESSAGE_PULL_COROUTINES = 30`,  
 `NUMBER_OF_CONCURRENT_PUSH_COROUTINES=20`

## Autoscaling guide for logs

Autoscaling works only for `logs` type of deployment, not `all`.

We recommend manually scaling the container to have a 4vCPU 4Gi machine and then enabling autoscaling.

GCP provides autoscaling of containers in both directions: **horizontal** and **vertical**. However, Dynatrace recommends only **horizontal** scaling.

If you have a 4vCPU 4Gi machine, you can enable autoscaling **horizontally**. However, we **don't** recommend scaling horizontally with the base resources of the container (1.25vCPU, 1Gi). It hasn't been proven to be efficient during testing. One 4vCPU machine does better than four 1vCPU machines. To enable autoscaling horizontally, use the horizontal autoscaling command:

```
kubectl autoscale deployment dynatrace-gcp-monitor --namespace dynatrace --cpu-percent=90 --min=1 --max=6
```

Autoscaling is recommended only when you have a minimum of 450 MB/min throughput and can provide a 4vCPU 4Gi RAM machine. Autoscaling is only scaling out, not scaling the machine up.

We **don't** recommend scaling **vertically** because every time a machine is scaled up, an environment variable needs to be changed to create more processes corresponding to machine cores.

## Uninstall

1. Find out what Helm release version you're using.

```
helm ls -n dynatrace
```

2. Uninstall the release.

Be sure to replace `<your-helm-release>` with the release name from the previous output.

```
helm uninstall <your-helm-release> -n dynatrace
```

Alternatively, you can delete the namespace.

```
kubectl delete namespace dynatrace
```

3. To remove all monitoring assets (such as dashboards and alerts) from Dynatrace, you need to remove all Google Cloud extensions.

You can find and delete relevant extensions via Dynatrace Hub.

Make sure to uninstall the following resources manually:

* The initial Role created and attached to the Service Account that you used to deploy the integration.
* The PubSub Topic.
* The PubSub Subscription.
* The LogRoute Sink.

## Monitoring consumption

### Metric ingestion

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs). For details, see [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

### Log ingestion

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)