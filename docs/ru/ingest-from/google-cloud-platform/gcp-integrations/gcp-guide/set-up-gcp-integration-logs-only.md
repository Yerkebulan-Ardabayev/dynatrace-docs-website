---
title: Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only
scraped: 2026-02-28T21:22:32.169375
---

# Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)

# Set up the Dynatrace Google Cloud log integration in a Kubernetes container (GKE)

* Latest Dynatrace
* How-to guide
* 12-min read
* Updated on Oct 08, 2024

Dynatrace version 1.230+

As an alternative to the [main deployment](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster."), that provides Google Cloud monitoring for both metrics and logs, you can choose to set up monitoring for logs only. In this scenario, you'll run the deployment script in Google Cloud Shell. Instructions will depend on the location where you want the deployment script to run:

* On a new GKE Autopilot cluster created automatically Recommended
* On an existing GKE standard or GKE Autopilot cluster

During setup, a new Pub/Sub subscription will be created. GKE will run a log forwarder container. After installation, you'll get logs, dashboards, and alerts for your configured services in Dynatrace.

For other deployment options, see [Alternative deployment scenarios](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide "Other options to set up log and/or metric monitoring for Google Cloud services").

This page describes how to install version 1.0 of the Google Cloud integration on a GKE cluster.

* If you already have an [earlier version](/docs/ingest-from/google-cloud-platform/legacy/deployment-k8s-container-legacy "Set up log and metric monitoring for GCP services in a Kubernetes container.") installed, you need to [migrate](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/migrate-gcp-function "Migrate from Google Cloud integration version 0.1 to version 1.0 on Kubernetes and as a Google Cloud Function.").

## Limitations

Dynatrace Google Cloud log integration supports up to 8 GB of data processing per hour (with base resourcesâwithout scaling). With bigger loads, messages will start to be retained in the PubSub Subscription. To measure latency, look for these metrics: `Oldest unacked message age` and `Unacked messages`. For scaling recommendations, see the [scaling guide](#scalingguide) below.

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

### Configure log export

1. Run the following shell script in the Google Cloud project you've selected for deployment.

Be sure to replace `<your-subscription-name>` and `<your-topic-name>` with your own values.

```
wget https://raw.githubusercontent.com/dynatrace-oss/dynatrace-gcp-monitor/master/scripts/deploy-pubsub.sh



chmod +x deploy-pubsub.sh



./deploy-pubsub.sh --topic-name <your-topic-name> --subscription-name <your-subscription-name>
```

2. Configure [log exportï»¿](https://dt-url.net/4743r02) to send the desired logs to the Google Cloud Pub/Sub topic created above.

To monitor logs from multiple projects, you need to create **Log Routing Sinks** in each source project selecting as a destination for your main project (in which you also deployed the integration and the PubSub Topic and Subscription).
For more information, see [Route logs to supported destinationsï»¿](https://dt-url.net/cl038gj).

### Dynatrace permissions

* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and [enable the following permission](/docs/dynatrace-api/basics/dynatrace-api-authentication#token-permissions "Find out how to get authenticated to use the Dynatrace API."): **Ingest logs** (API v2).

### Log ingestion

* Determine where log ingestion will be performed, according to your deployment. This distinction is important when configuring the [parameters](#param) for this integration.

  + **For SaaS deployments:** SaaS log ingest, where log ingestion is performed directly through the Cluster API. Recommended
  + **For Managed deployments:** You can use an existing ActiveGate for log ingestion. For information on how to deploy it, see [ActiveGate installation](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate").

Because of GCP's implementation of Cloud Function 2nd gen, logs from those resources will be linked to the underlying Cloud Run instances. Both extensions will have to be enabled.

To learn more, visit [Google Cloud Functions version comparisonï»¿](https://dt-url.net/b6038q5).

## Install



Complete the steps below to finish your setup.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download the Helm deployment package in Google Cloud Shell**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#dwld "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure parameter values**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#param "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect your Kubernetes cluster**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#connect "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Run the deployment script**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/set-up-gcp-integration-logs-only#script "Set up log monitoring for Google Cloud services in a Kubernetes container (GKE).")

### Step 1 Download the Helm deployment package in Google Cloud Shell

```
wget -q "https://github.com/dynatrace-oss/dynatrace-gcp-monitor/releases/latest/download/helm-deployment-package.tar"; tar -xvf helm-deployment-package.tar; chmod +x helm-deployment-package/deploy-helm.sh
```

### Step 2 Configure parameter values

The Helm deployment package contains a `values.yaml` file with the necessary configuration for this deployment. Go to `helm-deployment-package/dynatrace-gcp-monitor`and edit the `values.yaml` file, setting the required and optional parameter values as follows.

You might want to store this file somewhere for future updates, since it will be needed in case of redeployments. Also, keep in mind that its schema can change. In such case, you should use the new file and only copy over the parameter values.

For DDU consumptiom information, see [Monitoring consumption](#ddu).

### Step 3 Connect your Kubernetes cluster

* If you want to have a new GKE Autopilot cluster created by the deployment script, add `--create-autopilot-cluster` to the script. Setting up the connection to the cluster will happen automatically in this case and you can proceed to [step 4](#script).
* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, you can connect to your cluster from the Google Cloud console or via terminal. Follow the instructions below.

From the Google Cloud console

Via terminal

1. In your Google Cloud console, go to your Kubernetes Engine.
2. Select **Clusters**, and then select **Connect**.
3. Select **Run in Cloud Shell**.

Run the command below, making sure to replace

* `<cluster>` with your cluster name
* `<region>` with the region where your cluster is running
* `<project>` with the project ID where your cluster is running

```
gcloud container clusters get-credentials <cluster> --region <region> --project <project>
```

For details, see [Configuring cluster access for kubectlï»¿](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

### Step 4 Run the deployment script

* If you run the deployment script on an existing standard GKE or GKE Autopilot cluster, the deployment script will create an IAM service account with the necessary roles and deploy `dynatrace-gcp-monitor` to your Kubernetes cluster.
* If you run the deployment script with the `--create-autopilot-cluster` option, the deployment script will automatically create the new GKE Autopilot cluster and deploy `dynatrace-gcp-monitor` to it.

To run the deployment script, follow the instructions below.

Run on existing cluster

Run on new cluster

The latest versions of Google Cloud extensions will be uploaded. You have two options:

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

Run the command below. The latest versions of extensions will be uploaded.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster
```

To set a different name for the new cluster, run the command below instead, making sure to replace the placeholder (`<name-of-new-cluster>`) with your preferred name.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --autopilot-cluster-name <name-of-new-cluster>
```

To keep the existing versions of present extensions and install the latest versions for the rest of the selected extensions, if they are not present, run the command below instead.

```
cd helm-deployment-package



./deploy-helm.sh --create-autopilot-cluster --without-extensions-upgrade
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

Run the following command.

```
kubectl -n dynatrace logs -l app=dynatrace-gcp-monitor -c dynatrace-gcp-monitor-logs
```

To check the container logs for errors in your Google Cloud console

1. Go to **Logs explorer**.
2. Use the filters below to get metric and/or log ingest logs from the Kubernetes container:

   * `resource.type="k8s_container"`
   * `resource.labels.container_name="dynatrace-gcp-monitor-logs"`

3. Check if dashboards are imported.

   In Dynatrace, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and filter by **Tag** for `Google Cloud`. A number of dashboards for Google Cloud Services should be available.

## Enable alerting

To activate alerting, you need to enable metric events for alerting in Dynatrace.

To enable metric events

1. Go to **Settings**.
2. In **Anomaly detection**, select **Metric events**.
3. Filter for Google Cloud alerts and turn on **On/Off** for the alerts you want to activate.

## View logs

After deploying the integration, you can view and analyze Google Cloud logs in Dynatrace if you go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and filter by `cloud.provider: gcp`.

## Change deployment settings

### Change parameters from `values.yaml`

To load a new `values.yaml` file, you need to upgrade your Helm release.

To update your Helm release

1. Find out what Helm release version you're using.

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

DDU consumption applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)