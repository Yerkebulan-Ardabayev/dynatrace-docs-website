---
title: Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator
---

# Dynatrace Operator

# Dynatrace Operator

* 6-min read
* Updated on Sep 05, 2025

## Operator

Dynatrace Operator manages the automated rollout, configuration, and lifecycle of Dynatrace components. It uses custom resources of kind [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") and [EdgeConnect](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Update windows currently do not apply in Kubernetes environments.

Dynatrace Operator's functionality is tied to custom resources. These resources define which features are enabled. When a custom resource is created, Dynatrace Operator triggers an initial reconciliation to ensure that the desired state is achieved. The reconciliation process regularly detects changes in the Cluster and adjusts the state accordingly. The frequency of reconciliation decreases after the initial rollout, as fewer changes are typically made.

On startup, Dynatrace Operator registers the [webhook](#webhook) with the Kubernetes API. During each reconcile loop, Dynatrace Operator checks for changes in custom resources to:

* Update status of custom resources
* Ensure that initial startup of managed components meets requirements
* Manage workloads
* Register components on the Dynatrace server

This functionality is constrained to the namespace where Dynatrace Operator is deployed.

Namespaces monitored by Dynatrace Operator should be configured as follows:

* Label namespaces according to `namespaceSelector` so the webhook can mutate Pods.
* Ensure prerequisites for injection exist in injected namespaces.

### Resource requirements

Default configuration:

* 1 replica per Cluster

A single Dynatrace Operator replica is typically sufficient due to leader election. Additional replicas will only activate when the current leader terminates and a new one is elected.

A Dynatrace Operator container has predefined CPU and memory requests and limits. To customize these values during deployment with Helm, modify the `values.yaml` file.

Resource configuration with Helm

```
operator:



requests:



cpu: 50m



memory: 64Mi



limits:



cpu: 100m



memory: 128Mi
```

### Permissions and privileges

A full list of resources accessed by Dynatrace Operator is available in the [Security documentation](/managed/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require"). Network traffic and figures are documented in the [Network traffic documentation](/managed/ingest-from/setup-on-k8s/reference/network "Network traffic requirements for the Dynatrace Operator components in a Kubernetes cluster.").

## Webhook

Dynatrace webhook modifies Pod definitions to inject Dynatrace code modules for Application observability. It also validates DynaKube definitions and converts DynaKubes with older API versions.

Webhook configurations are managed by Dynatrace Operator and are updated periodically. These updates ensure that the Kubernetes API can continue to communicate with the webhook.

### Key functions

* Pod mutation—The webhook mutates Pods by modifying their definitions to include necessary metadata for Application observability.

  + Attaches Init container to download (in case no CSI driver is used) and configure the code modules on Pod startup.
  + Attaches CSI volumes, if configured, so CSI driver can handle volume creation.
  + Modifies Pod definitions for metadata enrichment.
* Namespace mutation—The webhook mutates namespaces to enable the monitoring of Pods within those namespaces.

  + Adds labels to namespaces so the webhook can listen to Pod `CREATE` events.

  Webhook configurations only support a static namespace selector. The required label is added to newly created namespaces.
* Configuration validation

  + Check custom resources, like DynaKubes, contain valid configuration when they are created or updated

    - Different validation depending on the fields, some are required and some need to conform to more specific rules
  + Provide helpful warning/error messages if validation fails

  Check [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") and [EdgeConnect parameters](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") for more information on each field!
* Conversion between versions

  + Ensures compatibility between different versions of the custom resource definitions
  + Converts older versions of the custom resource to the storage version, that is understood by Dynatrace Operator

### Resource requirements

Default configuration:

* 2 replicas per cluster (can be scaled up to increase availability)

The Dynatrace Webhook container has default requests and limits defined. If you want to set different resource requests or limits, you can do so when deploying Dynatrace Operator with Helm.

Resource configuration with Helm

To set resource limits, modify the `values.yaml`. See the default configuration below.

```
webhook:



requests:



cpu: 300m



memory: 128Mi



limits:



cpu: 300m



memory: 128Mi
```

### Permissions and privileges

A full list of resources that are accessed by the webhook can be found in [Dynatrace Operator security](/managed/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").
Ingress and egress is documented in [Network traffic](/managed/ingest-from/setup-on-k8s/reference/network "Network traffic requirements for the Dynatrace Operator components in a Kubernetes cluster.").

## CSI driver

The Dynatrace Operator CSI driver provides Dynatrace code modules for the application Pods, while minimizing storage usage, and load on the Dynatrace environment. In addition, it provides writable volume storage for OneAgent utilizing [ephemeral local volumes﻿](https://dt-url.net/j9027w2).

* For `applicationMonitoring` configurations, it provides the necessary OneAgent binary for application monitoring to the Pods on each Node as a **read-only** mount.
* For `hostMonitoring` configurations, it provides a writable folder for the OneAgent configurations when a read-only host file system is used.
* For `cloudNativeFullStack`, it provides both of the above.

Minimizes downloads by downloading the code modules once per Node and storing them on the Node's filesystem.

* With the CSI driver, injecting 100 Pods spread across three nodes would result in just 3 Code Module downloads.
* Without the CSI driver, each Pod would need to download its own code modules, so injecting 100 Pods would result in the download of 100 code modules.

Minimizes storage usage by storing the code modules on the Node's filesystem, and creating an [OverlayFs﻿](https://dt-url.net/hf036vi) mount for each injected Pod.

* With the CSI driver, injecting 100 Pods spread across three nodes would result in the storage of only 3 code modules.
* Without the CSI driver, each Pod stores a Code Module, so injecting 100 Pods would result in the storage of 100 code modules.

For details on where the OneAgent files and logs are stored on the Kubernetes nodes (with and without CSI driver), see [Storage requirements](/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments").

### Resource requirements

Default configuration:

* 1 replica per Node (deployed via DaemonSet)

The CSI driver provisioner does not have any predefined resource limits. However, if you want to set resource limits or modify resource limits for other containers of the CSI driver, you can do so when deploying Dynatrace Operator with Helm.

Resource configuration with Helm

To set resource limits for the `provisioner` container, modify the `values.yaml`. See the example configuration below.

* Increase CPU to accelerate unpacking and installation of code modules (important for fast node startup and initialization)
* Increasing memory does not have an impact on performance

```
provisioner:



resources:



requests:



cpu: 300m



memory: 100Mi



limits:



cpu: 300m



memory: 100Mi



server:



resources:



requests:



cpu: 50m



memory: 100Mi



limits:



cpu: 50m



memory: 100Mi
```

### Permissions and privileges

The Dynatrace Operator CSI driver requires elevated permissions to create and manage mounts on the host system. Specifically, the [mountPropagation: Bidirectional﻿](https://dt-url.net/90236h3) permission is needed on the volume where the CSI driver stores the code modules. This permission is only available for privileged containers.

A full list of resources that are accessed by the CSI driver can be found in the [Security documentation](/managed/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").

Ingress and Egress is documented in the [Network traffic documentation](/managed/ingest-from/setup-on-k8s/reference/network "Network traffic requirements for the Dynatrace Operator components in a Kubernetes cluster.").