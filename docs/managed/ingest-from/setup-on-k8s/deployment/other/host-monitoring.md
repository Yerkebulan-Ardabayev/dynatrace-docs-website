---
title: Get started with host monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring
scraped: 2026-05-12T12:04:46.293381
---

# Get started with host monitoring

# Get started with host monitoring

* 6-min read
* Updated on Sep 05, 2025

This page provides instructions for deploying the Dynatrace Operator in host monitoring configuration to a Kubernetes cluster.

If you're interested in gaining a more comprehensive view of your environment that includes aspects such as Application observability and user experience, you should consider a full Kubernetes observability approach, such as [cloud-native full-stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes") or [classic full-stack](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes").

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

The combination of `hostMonitoring` and `applicationMonitoring` in a Kubernetes cluster in the same environment is not supported.

## Installation options

Choose **one of the installation methods** that best suits your needs.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator version 0.8.0+

1. Install Dynatrace Operator

   If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

   The following command works for both default installations and installations using an OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Installation with additional configuration of the Helm chart

   Edit the [`values.yaml`ï»¿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) sample from GitHub, and then run the install command, passing the YAML file as an argument:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   If `installCRD` is set to `false`, you need to create the custom resource definition manually before starting the Helm installation:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```
2. Create secret for access token

   Create a secret named `dynakube` for the Dynatrace Operator token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for host monitoring from GitHubï»¿](https://dt-url.net/qx8363l). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
4. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with Dynatrace Operator CSI driver, you should see the following Pods:

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

   As OneAgent and CSI driver are deployed as DaemonSet you should have a OneAgent and CSI driver Pod on each node.

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

   Run the following command to see when Dynatrace Operator components finish initialization:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Create secret for access token

   Create a secret named `dynakube` for the Dynatrace Operator token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for host monitoring from GitHubï»¿](https://dt-url.net/qx8363l). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   If you want to reduce billed units, enable Infrastructure Monitoring mode in your DynaKube configuration.

   ```
   oneAgent:



   hostMonitoring:



   args:



   - --set-monitoring-mode=infra-only
   ```

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with Dynatrace Operator CSI driver, you should see the following Pods:

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

   As OneAgent and CSI driver are deployed as DaemonSet you should have a OneAgent and CSI driver Pod on each node.

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
3. Create secret for access token

   Create a secret named `dynakube` for the Dynatrace Operator token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
4. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for host monitoring from GitHubï»¿](https://dt-url.net/qx8363l). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with Dynatrace Operator CSI driver, you should see the following Pods:

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

   As OneAgent and CSI driver are deployed as DaemonSet you should have a OneAgent and CSI driver Pod on each node.

## Learn more

After you've successfully installed the Dynatrace Operator, you may find the following resources helpful for further learning and troubleshooting.

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

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")