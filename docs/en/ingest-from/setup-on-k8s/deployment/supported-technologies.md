---
title: Supported distributions
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/supported-technologies
scraped: 2026-02-28T21:15:44.613617
---

# Supported distributions

# Supported distributions

* Latest Dynatrace
* 6-min read
* Updated on Sep 07, 2023

This page gives an overview and documents the different configurations for all major Kubernetes distributions.

For the overall Dynatrace support lifecycle for Kubernetes and Red Hat OpenShift, including the currently supported versions, see [Dynatrace support lifecycle for Kubernetes and Red Hat OpenShift full stack Monitoring](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

## AWS Elastic Kubernetes Service (EKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for EKS.

Dynatrace supports a variety of different flavors of AWS EKS. For EKS on EC2 or bare metal, you can install Dynatrace in [any available deployment option](#installation-k8s) without any additional configuration changes. For EKS on Fargate, you can [install Dynatrace for App Observability](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.").

### AWS Bottlerocket OS

applicationMonitoring

Additional configuration is required for AWS Bottlerocket OS on EKS nodes.
You can deploy Dynatrace for Application Observability and configure Platform Observability via ActiveGate (Kubernetes API Monitoring). Platform Observability via Dynatrace OneAgent is not supported. Starting with Dynatrace Operator version 0.12.0 and before Dynatrace Operator version 1.7.0, the CSI driver is supported and needs to be configured in [read-only mode for Bottlerocket OS](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume "Configure read-only CSI volumes for OneAgent injection to enhance data security."):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



feature.dynatrace.com/injection-readonly-volume: "true"



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- kubernetes-monitoring



- dynatrace-api



...
```

## Azure Kubernetes Service (AKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for AKS.

## Google Kubernetes Engine (GKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for GKE.

### GKE Standard & Anthos

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without Dynatrace Operator CSI driver, additional configuration is required. Enable volume storage for the OneAgent by setting the `ONEAGENT_ENABLE_VOLUME_STORAGE` environment variable:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



...
```

### GKE Autopilot

applicationMonitoring

For GKE Autopilot, you can [install Dynatrace for App Observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"). Dynatrace Operator CSI driver is supported for all GKE Autopilot clusters running Kubernetes version 1.26+. Additionally, only images from the following repositories are supported and must be set during installation:

* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`
* `docker.io/dynatrace/dynatrace-operator`
* `public.ecr.aws/dynatrace/dynatrace-operator`

Standalone LogMonitoring on GKE Autopilot is fully supported since Dynatrace Operator version 1.4.2 with the following repository source support:

* `docker.io/dynatrace/dynatrace-logmodule`
* `public.ecr.aws/dynatrace/dynatrace-logmodule`

#### Allowlisting Dynatrace workloads

CSI driver Standalone LogMonitoring

Starting with GKE Autopilot version 1.32.1-gke.1376000 a `WorkloadAllowlist` explicitly permits security exceptions (for example, allowing the Dynatrace Operator CSI driver to run privileged workloads).
Dynatrace is working with Google to roll out these `WorkloadAllowlists` in a timely manner for each release.

Further details on the process can be found on the official [Google Cloud docsï»¿](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

Deploying and managing the AllowlistSynchronizer will be automated in Dynatrace Operator version 1.5.0+. For versions 1.4.1 - 1.4.X you will have to apply such manifest yourself.

##### AllowlistSynchronizer for version 1.4.2:

```
apiVersion: auto.gke.io/v1



kind: AllowlistSynchronizer



metadata:



name: allowlist-synchronizer-dynatrace



spec:



allowlistPaths:



- Dynatrace/csidriver/1.4.2/*



- Dynatrace/logmonitoring/1.4.2/*
```

Apply the `AllowlistSynchronizer`:

```
kubectl apply -f allowlist-synchronizer-dynatrace.yaml
```

v1.3.2 and earlier versions

CSI driver

Depending on the deployment option, the image can be set in different ways.

#### Helm

Set the `image` value in your helm `values.yaml` to one of the supported repositories during installation.

```
--set image=gcr.io/dynatrace-marketplace-prod/dynatrace-operator:v1.3.2
```

```
--set image=docker.io/dynatrace/dynatrace-operator:v1.3.2
```

#### Manifests

1. Instead of applying the manifest, the manifests (`kubernetes-csi.yaml`) have to be downloaded from the [release pageï»¿](https://github.com/Dynatrace/dynatrace-operator/releases).
2. Replace the value `public.ecr.aws/dynatrace/dynatrace-operator` in the image fields with `docker.io/dynatrace/dynatrace-operator`.
3. Apply the changed manifest. Use the appropriate one depending on if you want to use the CSI driver or not.

   ```
   kubectl apply -f kubernetes-csi.yaml
   ```

## Red Hat OpenShift

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Classic full-stack is supported only on Kubernetes nodes that use Red Hat Enterprise Linux (RHEL) as their operating system.

For OpenShift, you need to [configure Security Context Constraints (SCC)](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.") for all deployments using the Dynatrace Operator CSI driver (`cloudNativeFullStack`, `applicationMonitoring`/`hostMonitoring` with CSI). In addition, starting with Openshift 4.13, you need to [configure the CSI Inline Ephemeral Volume Admissing plugin](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.").

For managed OpenShift implementations such as AWS ROSA and Azure Red Hat OpenShift (ARO), Dynatrace supports the same features as dedicated OpenShift.

For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://dt-url.net/a2038v8).

## Rancher Kubernetes Engine 1 (RKE1)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for RKE1.

## Rancher Kubernetes Engine 2 (RKE2)

applicationMonitoring

No specific configuration is required for RKE2 when `applicationMonitoring` mode is used. Due to SELinux policies on Red Hat Enterprise Linux derivatives, `hostMonitoring`, `cloudNativeFullStack` and `classicFullStack` modes are not supported.

## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

For TKGI, additional environment configurations are required for all deployment modes except `applicationMonitoring` without Dynatrace Operator CSI driver.

### `cloudNativeFullStack`, `applicationMonitoring` (with CSI driver), and `hostMonitoring`

In the `values.yaml`, additional configuration is required for these modes to configure the CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/vcap/data/kubelet"
```

### `classicFullStack`

Requires images from the Dynatrace built-in registry and not from the public registry. Use the following configuration:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /var/vcap/store
```

## IBM Kubernetes Service (IKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

For IKS, additional environment configurations are required for all deployment modes except `applicationMonitoring` without the CSI driver.

### `cloudNativeFullStack`, `applicationMonitoring` (with CSI driver), and `hostMonitoring`

Additional configuration is required for these modes to configure the CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/data/kubelet"
```

### `classicFullStack`

Requires images from the Dynatrace built-in registry and not from the public registry. Use the following configuration:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /opt
```

## SUSE Container as a Service (CaaS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without the CSI driver, be sure to configure volume storage for OneAgent:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack: # change to `hostMonitoring` if needed



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"
```

## Nutanix Kubernetes Platform (NKP, former D2iQ Konvoy)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.

## Oracle Kubernetes Engine (OKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.

## Mirantis Kubernetes Engine

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.