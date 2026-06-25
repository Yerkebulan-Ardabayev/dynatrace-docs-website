---
title: Get started with Full Kubernetes observability (cloud-native full-stack deployment)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed
scraped: 2026-05-12T11:52:52.580162
---

# Get started with Full Kubernetes observability (cloud-native full-stack deployment)

# Get started with Full Kubernetes observability (cloud-native full-stack deployment)

* Updated on Nov 06, 2023

This page provides instructions on installing Dynatrace Operator with cloud-native full-stack configuration to a Kubernetes cluster.

Prerequisites

Before installing Dynatrace on your Kubernetes cluster, ensure that you meet the following requirements:

* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to monitor.
* You have sufficient privileges on the monitored cluster to run `kubectl` or `oc` commands.

### Cluster setup and configuration

* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to your Dynatrace environment URL.

  + For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.
* For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Helm installation Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).

### Supported versions

See supported Kubernetes/OpenShift [platform versions](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") and [distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

By default, Dynatrace Operator injects OneAgent in all namespaces, but you can configure it to monitor only specific namespaces and exclude others. For details, see [Configure monitoring for namespaces and pods](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#monitor-only-specific-namespaces "Configure monitoring for namespaces and pods").

[Configuring SCC](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.") is required for OpenShift for `cloudNativeFullStack` and `applicationMonitoring` with CSI driver deployments.

## Installation options

Choose **one of the installation methods** that best suits your needs.

[![Dynatrace UI](https://dt-cdn.net/images/search-color-945bb8b42a.svg "Dynatrace UI")

**Guided (Dynatrace UI)**](#guided)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Guided (Dynatrace UI)

Dynatrace version 1.290+

1. Go to **Kubernetes**.
2. Select **Connect automatically via Dynatrace Operator** in the header of the Kubernetes cluster page.

![Quickstart](https://dt-cdn.net/images/quickstart-3574-833bd4c27b.png)

Quickstart

1. Enter the following details.

   * **Name**: Defines the display name of your Kubernetes cluster within Dynatrace. Additionally, this name will be used as a prefix for naming Dynatrace-specific resources inside your Kubernetes cluster, such as DynaKube (custom resource), ActiveGate (pod), OneAgents (pods), and as a name for the secret holding your tokens.
   * Recommended **Group**: Defines a group used by various Dynatrace settings, including network zone, ActiveGate group, and host group. If not set, defaults or empty values are used.
   * **Dynatrace Operator token**: Select **Create token** or enter the **API token** you previously created. For more information, see [Access tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
   * Optional**Data ingest token**: Select **Create token** or enter the **API token** you previously created. For more information, see [Access tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
2. Optional Decide whether you want the Dynatrace Operator to disable the verification of the Dynatrace SSL certificate.

   This is relevant if you are using Dynatrace Managed with self-signed certificates.
3. Select **Download dynakube.yaml**. Copy the code block created by Dynatrace created and **run it in your terminal**. Ensure you execute the commands in the same directory where you downloaded the YAML or adapt the command to link to the location of the YAML manifest.

   The downloaded YAML file is a basic version of the DynaKube custom resource definition. To adjust values to your specific needs, refer to the [DynaKube custom resource samples for cloud-native full-stack from GitHubï»¿](https://dt-url.net/9n636jg). For more information about all configuration options, see [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
4. Optional Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   As OneAgent and CSI-driver are deployed as DaemonSet you should have a OneAgent and CSI-driver pod on each node.

## Helm

Dynatrace Operator version 0.8.0+

New Helm installation and upgrade instructions use our Helm chart available from an OCI registry. Therefore, if the Dynatrace repository is currently added to your local Helm repositories, it can be safely removed.

```
helm repo remove dynatrace
```

The installation process is independent of whether you are using Kubernetes or OpenShift. The platform is auto-detected during the installation.

1. Install Dynatrace Operator

   The following command works for both default installations and installations using an OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Installation with additional configuration of the Helm chart

   Edit the [`values.yaml`ï»¿](https://dt-url.net/helm-values) sample from GitHub, and then run the install command, passing the YAML file as an argument:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   For cloud native, full stack deployments, a CSI driver is mandatory. If `installCRD` is set to `false`, you need to create the custom resource definition manually before starting the Helm installation:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) and IBM Kubernetes Service (IKS) require [additional configuration](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").
2. Create secret for access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for cloud-native full-stack from GitHubï»¿](https://dt-url.net/9n636jg). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to-guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Optional Verify deployment

   Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   As OneAgent and CSI-driver are deployed as DaemonSet you should have a OneAgent and CSI-driver pod on each node.

## Manifest

Kubernetes

OpenShift

1. Create a `dynatrace` namespace

   ```
   kubectl create namespace dynatrace
   ```
2. Install Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) and IBM Kubernetes Service (IKS) require [additional configuration](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

   Run the following command to see when Dynatrace Operator components finish initialization:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Create secret for Access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for cloud-native full-stack from GitHubï»¿](https://dt-url.net/9n636jg). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to-guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Verify deployment

   Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   As OneAgent and CSI-driver are deployed as DaemonSet you should have a OneAgent and CSI-driver pod on each node.

1. Add a `dynatrace` project

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Install Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
   ```

   Run the following command to see when Dynatrace Operator components finish initialization:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Create secret for Access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for cloud-native full-stack from GitHubï»¿](https://dt-url.net/9n636jg). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to-guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Verify deployment

   Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<CLUSTER_DOMAIN>/e/<ENVIRONMENT_ID>/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following pods:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   As OneAgent and CSI-driver are deployed as DaemonSet you should have a OneAgent and CSI-driver pod on each node.

## Learn more

After you've successfully installed Dynatrace Operator, you may find the following resources helpful for further learning and troubleshooting.

[#### Guides

Detailed description of installation and configuration options for specific use-cases

Guides](/managed/ingest-from/setup-on-k8s/guides)[#### Troubleshooting

This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.

Troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting)

[#### How it works

In-depth description on how the deployment on Kubernetes works.

How it works](/managed/ingest-from/setup-on-k8s/how-it-works)[#### Reference

Contains a reference page with configuration options for each Dynatrace component

Reference](/managed/ingest-from/setup-on-k8s/reference)[#### Dynatrace Operator release notes

Release notes for Dynatrace Operator

Dynatrace Operator release notes](/managed/whats-new/dynatrace-operator)[#### Update or uninstall Dynatrace Operator

Upgrade and uninstallation procedures for Dynatrace Operator

Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

Set resource limits for Dynatrace ActiveGates

Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Related topics

* [Flexible, scalable, self-service Kubernetes native observability now in General Availabilityï»¿](https://www.dynatrace.com/news/blog/flexible-scalable-self-service-kubernetes-native-observability/)