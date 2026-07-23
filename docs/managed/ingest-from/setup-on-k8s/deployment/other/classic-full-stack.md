---
title: Get started with Full observability (classic full-stack deployment)
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack
---

# Get started with Full observability (classic full-stack deployment)

# Get started with Full observability (classic full-stack deployment)

* 8-min read
* Updated on Sep 05, 2025

This deployment mode is supported by Dynatrace but is no longer recommended for most environments.

Classic Full-Stack mode is not supported when using a [platform token](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

This page provides instructions for deploying the Dynatrace Operator in classic full-stack configuration to a Kubernetes cluster.

Prerequisites

Before installing Dynatrace on your Kubernetes cluster, ensure that you meet the following requirements:

* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to monitor.
* You have sufficient privileges on the monitored cluster to run `kubectl` or `oc` commands. If you don't use the `cluster-admin` cluster role, see [deployment permissions](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for the required permissions.

### Cluster setup and configuration

* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to your Dynatrace environment URL.

  + For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.
* For OpenShift Dedicated, you need the [cluster-admin role﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Helm installation Use [Helm version 3﻿](https://dt-url.net/n5036j1).

### Supported versions

See supported Kubernetes/OpenShift [platform versions](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") and [distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Installation options

Choose **one of the installation methods** that best suits your needs.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator version 0.8.0+

New Helm installation and upgrade instructions use our Helm chart available from an OCI registry. Therefore, if the Dynatrace repository is currently added to your local Helm repositories, it can be safely removed.

```
helm repo remove dynatrace
```

The installation process is independent of whether you are using Kubernetes or OpenShift. The platform is auto-detected during the installation.

1. Install Dynatrace Operator

   If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

   The following command works for both default installations and installations using an OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --set csidriver.enabled="false" \



   --create-namespace \



   --namespace dynatrace \



   --atomic \
   ```

   Installation with additional configuration of the Helm chart

   Edit the [`values.yaml`﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/config/helm/chart/default/values.yaml) sample from GitHub, and then run the install command, passing the YAML file as an argument:

   Make sure to disable Dynatrace Operator CSI driver from being rolled out, as it's not used in classic full-stack.

   ```
   csidriver:



   enabled: false
   ```

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   If `installCRD` is set to `false`, you need to create the custom resource definition manually before starting the Helm installation:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```
2. Create secret for access token

   Create a secret named `dynakube` for the Dynatrace Operator token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```
3. Apply the DynaKube custom resource

   Download the [DynaKube custom resource sample for classic full-stack from GitHub﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/dynakube/v1beta5/classicFullStack.yaml). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

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

   In a default DynaKube configuration, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   As OneAgent is deployed as DaemonSet, you should have a OneAgent Pod on each node.

## Manifest

Kubernetes

OpenShift

1. Create a `dynatrace` namespace

   ```
   kubectl create namespace dynatrace
   ```
2. Install Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
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

   Download the [DynaKube custom resource sample for classic full-stack from GitHub﻿](https://dt-url.net/ei436pt). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

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

   In a default DynaKube configuration, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   As OneAgent is deployed as DaemonSet, you should have a OneAgent Pod on each node.

1. Add a `dynatrace` project

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Install Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
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

   Download the [DynaKube custom resource sample for classic full-stack from GitHub﻿](https://dt-url.net/ei436pt). In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
5. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace project are running and ready.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following Pods:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-2wnbb               1/1     Running   0               50s



   dynakube-oneagent-wp2bt               1/1     Running   0               50s



   dynakube-oneagent-pxdv4               1/1     Running   0               50s



   dynatrace-operator-8445c87f87-qhc5t   1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-ws7gg    1/1     Running   0               3m02s



   dynatrace-webhook-56644487df-xkxkd    1/1     Running   0               3m02s
   ```

   As OneAgent is deployed as DaemonSet, you should have a OneAgent Pod on each node.

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

Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.

Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator)[#### Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

Set resource limits for Dynatrace ActiveGates

Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits)

## Related topics

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")