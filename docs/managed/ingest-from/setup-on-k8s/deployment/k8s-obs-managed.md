---
title: Get started with Kubernetes observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed
scraped: 2026-05-12T11:52:50.677236
---

# Get started with Kubernetes observability

# Get started with Kubernetes observability

* Published Jul 28, 2023

This page provides instructions for deploying the Dynatrace Operator for Kubernetes observability.

To gain a more comprehensive view of your environment that includes aspects such as application observability and user experience, you should consider combining Kubernetes observability with [Application Observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") if you are on a [Dynatrace Platform Subscription (DPS)](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") or use [cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes") mode if you are on Dynatrace classic licensing.

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

## Installation options

Choose **one of the installation methods** that best suits your needs.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator version 0.8.0+

Kubernetes

OpenShift

1. Install Dynatrace Operator

The following command works for both default installations and installations using an OCI registry.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



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

Download the [DynaKube custom resource sample for Kubernetes observabilityï»¿](https://dt-url.net/sa038nu) from GitHub. In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

4. Verify deployment

Optional

Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

In this DynaKube configuration, you should see the following pods:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Install Dynatrace Operator

The following command works for both default installations and installations using an OCI registry.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "csidriver.enabled=false" \



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

If `installCRD` is set to `false`, you need to create the custom resource definition manually before starting the Helm installation:

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
```

2. Create secret for access token

Create a secret named `dynakube` for the Dynatrace Operator token obtained in [Tokens and permissions required](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

```
oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
```

3. Apply the DynaKube custom resource

Download the [DynaKube custom resource sample for Kubernetes observabilityï»¿](https://dt-url.net/sa038nu) from GitHub. In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

```
oc apply -f <your-DynaKube-CR>.yaml
```

4. Verify deployment

Optional#

Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

In this DynaKube configuration, you should see the following pods:

```
> oc get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

## Manifest

Kubernetes

OpenShift

1. Create a `dynatrace` namespace

```
kubectl create namespace dynatrace
```

2. Install Dynatrace Operator

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
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

Download the [DynaKube custom resource sample for Kubernetes observabilityï»¿](https://dt-url.net/sa038nu) from GitHub. In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

```
kubectl apply -f <your-DynaKube-CR>.yaml
```

5. Verify deployment

Optional

Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

```
> kubectl get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

In this DynaKube configuration, you should see the following pods:

```
> kubectl get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

1. Add a `dynatrace` project

```
oc adm new-project --node-selector="" dynatrace
```

2. Install Dynatrace Operator

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
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

Download the [DynaKube custom resource sample for Kubernetes observabilityï»¿](https://dt-url.net/sa038nu) from GitHub. In addition, you can review the [available parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/managed/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

```
oc apply -f <your-DynaKube-CR>.yaml
```

5. Verify deployment

Optional

Verify that your DynaKube is running and all pods in your Dynatrace namespace are running and ready.

```
> oc get dynakube -n dynatrace



NAME         APIURL                                             STATUS     AGE



dynakube     https://{your-domain}/e/{your-environment-id}/api  Running    45s
```

In this DynaKube configuration, you should see the following pods:

```
> oc get pods -n dynatrace



NAME                                  READY   STATUS    RESTARTS        AGE



dynakube-activegate-0                 1/1     Running   0               50s



dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
```

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