---
title: Code modules delivery modes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes
---

# Code modules delivery modes

# Code modules delivery modes

* Reference
* 7-min read
* Updated on Jul 10, 2026

cloudNativeFullStack applicationMonitoring

Dynatrace Operator can deliver OneAgent code modules to application pods in several ways. Which one applies depends on whether the CSI driver is enabled, the Dynatrace Operator version, and how you configure the DynaKube.

Notable use cases:

* Cloud-native full-stack monitoring works independently of the CSI driver.
* Cloud-native full-stack monitoring can be deployed via OpenShift OperatorHub.
* Non-CSI and CSI-based code module injection can be combined — for details, see [Enforce ephemeral-volume injection on mixed clusters](#mixed-mode).

| Delivery mode | CSI driver enabled | Storage overhead | When it applies | Notes |
| --- | --- | --- | --- | --- |
| [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) | No, ephemeral volume | Per-pod storage consumption | Code modules image configured. Default since Operator v1.10 | Uses Node credentials. Image cached on each node. |
| [CSI driver image pull](#csi-image-pull) | Yes, CSI volume | Node-level cache | Code modules image configured, and CSI driver enabled | Requires `customPullSecret` for private registries |
| [Node Image Pull via CSI volume](#csi-node-image-pull) | Yes, CSI volume | Node-level cache | Code modules image configured and CSI driver enabled. Opt-in via `feature.dynatrace.com/node-image-pull: "true"` | Uses Node credentials alongside the `customPullSecret` for private registries.[1](#fn-1-1-def) |
| [CSI driver ZIP download](#csi-zip) | Yes, CSI volume | Node-level cache | No code modules image configured | Not supported on Latest Dynatrace environments. Use [CSI driver image pull](#csi-image-pull) instead. |
| [ZIP download](#zip-download) | No, ephemeral volume | Per-pod storage consumption | No code modules image configured | Adds latency on every pod start. ZIP downloaded and extracted to each pod’s ephemeral volume. Not supported on the Latest Dynatrace environments. Use [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) instead. |

1

Because images are pulled by the Kubernetes node using its own credentials, no `customPullSecret` is needed for private registries as long as the nodes are already configured to authenticate against the registry. For details, see [Prerequisites](#csi-node-image-pull-prerequisites).

## Volume types

The delivery mode depends on which volume type is used to expose code module binaries to the application pod.

|  | Ephemeral volume | CSI volume |
| --- | --- | --- |
| **CSI driver required** | No | Yes |
| **Storage** | Per-pod (each pod gets its own copy) | Node-level cache (shared across pods on the same node) |
| **Credentials for private registries** | Node credentials or pod-level `imagePullSecrets` | `customPullSecret` (or node credentials for Node Image Pull via CSI) |
| **When to use** | No CSI driver available, or ephemeral injection is preferred for specific workloads | CSI driver is available and node-level caching is preferred |

## Ephemeral volume

When the CSI driver is not enabled, code modules are copied into the application pod's ephemeral volume.

### Node Image Pull via Ephemeral Volume

With Node Image Pull via ephemeral volumes, the injected init container image is the code modules image instead of the Operator's image. The Kubernetes node pulls it directly and the init container copies the OneAgent binaries into an ephemeral volume on the application pod.

Since Dynatrace Operator version 1.10, Node Image Pull to ephemeral volumes is used when a code modules image is configured.
In previous versions, this behavior is gated by the `feature.dynatrace.com/node-image-pull: "true"` feature flag.

Configuration

#### Prerequisites

* Dynatrace OneAgent version 1.317+
* A Dynatrace code modules image sourced from a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

With this mode, the Kubernetes node pulls the code modules image for your injected application pods. When using a private registry, the DynaKube `customPullSecret` does **not** apply to these pods—Dynatrace Operator does not replicate pull secrets into application namespaces or add them to pods outside the `dynatrace` namespace.

Ensure that all nodes are authenticated to the registry, or distribute a pull secret to your application namespaces, nodes, or pods. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").

#### DynaKube configuration

Enable automatic image resolution via the `feature.dynatrace.com/use-public-registry` annotation, or set the `codeModulesImage` field directly. For image sources and tag format, see [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

### ZIP download

The injected init container downloads and unpacks the code module ZIP archive from your Dynatrace Environment into an ephemeral volume at pod startup.

This delivery method is used when no code modules image is configured or it cannot be auto resolved and the CSI driver is not enabled.

Drawbacks:

* Each pod downloads the code modules ZIP from the Dynatrace Environment, which adds latency and load.
* The init container must have network access to the Environment API during pod startup.
* No Kubernetes-native supply chain integration—the binaries are not delivered as an OCI image, so image-signing and admission policies do not apply.

For these reasons, node image pull via ephemeral volume delivery is recommended over ZIP download whenever possible.

Configuration

#### Prerequisites

* CSI driver not enabled on the cluster.
* No code modules image configured.
* The injected pods must have network access to the Dynatrace Environment API at startup.

#### DynaKube configuration

Dynatrace Operator uses this mode automatically when no code modules image is set and the CSI driver is not enabled. Ensure that `codeModulesImage` is absent from your DynaKube, and that the [automatic resolution](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") does not apply:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack: {}
```

### Storage optimization

OneAgent version 1.315+

When code modules are delivered via ephemeral volumes, each injected pod receives its own copy of the code module binaries. To reduce storage consumption, you can scope injection to specific application technologies (for example, Java), preventing unnecessary binaries from being copied.

If storage optimization is not configured (that is, the `oneagent.dynatrace.com/technologies` annotation is missing), storage consumption follows the guidelines outlined in the [storage requirements](/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments").

The technologies specified are copied into a shared volume, consuming ephemeral storage.

#### Technology identifiers

The following identifiers are available per technology:

| Technology | Identifier |
| --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | `java` |
| [.NET, .NET Core and .NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | `dotnet` |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | `nodejs` |
| [Python](/managed/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.") | `python` |
| [PHP](/managed/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.") | `php` |
| [Go](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") | `go` |
| Apache, IBM HTTP Server | `apache` |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.") | `nginx` |

#### Annotate the application pod

To reduce the data copied into application pods, you can specify which OneAgent technologies are relevant for your application. Annotate your application pods as shown in the pod snippet below:

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"
```

When specifying a comma-separated list of technology identifiers, ensure there are no whitespace characters within the annotation value.

Annotation values must use the exact technology identifiers listed in the table above.

If no `oneagent.dynatrace.com/technologies` annotation is provided, all technologies are copied to application pods.

If a single technology is used across your cluster, or if you want to set a default technology for Dynatrace code module injection, you can configure it at the DynaKube level to apply to all injected application pods.

Configure on DynaKube-level

Modify your DynaKube configuration by restricting code module injection to a specific technology or a set of multiple technologies:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



oneagent.dynatrace.com/technologies: "java"



spec:



...
```

When specifying a comma-separated list of technology identifiers, ensure there are no whitespace characters within the annotation value.

## CSI volume

When code modules are delivered with the CSI driver, the code modules binaries are shared between pods, avoiding per-pod copies.

### CSI driver image pull

The CSI driver pulls the code modules image and exposes the code modules binaries on the host filesystem, where each injected application pod mounts them through a CSI volume.

Configuration

#### Prerequisites

* A Dynatrace code modules image sourced from a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry") or [resolved automatically](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

  + For private registries, configure a `customPullSecret`. For details, see [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").
* CSI driver enabled on the cluster.

#### DynaKube configuration

Enable automatic image resolution via the `feature.dynatrace.com/use-public-registry` annotation, or set the `codeModulesImage` field directly. For image sources and tag format, see [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

### Node Image Pull via CSI volume

Dynatrace Operator version 1.5

The CSI driver schedules a pull job on each node where the container runtime pulls the code modules image directly. The code modules binaries are then exposed on the host filesystem, where each injected application pod mounts them through a CSI volume.

This approach simplifies Kubernetes-native integration with supply chain security tooling and reduces the need for a `customPullSecret` when sourcing images from private registries.[2](#fn-2-2-def) Because the node pulls the image, ensure that the node is authenticated to the private registry. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").

Since Dynatrace Operator version 1.10, the `node-image-pull` feature flag only affects the CSI driver. For ephemeral-volume deployments, [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) is the default.

2

Starting from [Dynatrace Operator version 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0"), the download jobs inherit the same `PriorityClass` as the CSI driver to ensure fast scheduling and preemption on congested clusters. You can configure the value through `csidriver.priorityClassValue` in the Helm values file. For guidance, see [Use priorityClass for critical Dynatrace components](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Use priorityClass for critical Dynatrace components").

Configuration

#### Prerequisites

* Dynatrace OneAgent version 1.317+
* A Dynatrace code modules image sourced from a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").
* CSI driver enabled on the cluster.

#### DynaKube configuration

Enable the `node-image-pull` feature flag and the `use-public-registry` annotation for automatic image resolution, or set the `codeModulesImage` field directly. For image sources and tag format, see [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



feature.dynatrace.com/use-public-registry: "true" # enables automatic image resolution; omit if setting codeModulesImage manually



spec:



oneAgent:



# example, can also be used with `cloudNativeFullStack`



applicationMonitoring:



codeModulesImage: <dynatrace-codemodules-image> # optional if resolved automatically
```

#### Limitations

GKE Autopilot dynamically provisions nodes and their sizes based on the aggregated resource requests of pods. This makes GKE Autopilot unsuitable for the node image pull feature in combination with the CSI driver. Dynatrace recommends either disabling node image pull on GKE Autopilot with the CSI driver, or using ephemeral-volume delivery instead—see [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull).

### CSI driver ZIP download

The CSI driver downloads, extracts and exposes the code modules ZIP on the host filesystem, where each injected application pod mounts them through a CSI volume.

Configuration

#### Prerequisites

* CSI driver enabled on the cluster.
* No code modules image configured.

#### DynaKube configuration

Dynatrace Operator uses this mode automatically when the CSI driver is enabled and no code modules image is set. Ensure that `codeModulesImage` is absent from your DynaKube, and that the [automatic resolution](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") does not apply:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack: {}
```

## Enforce ephemeral-volume injection on mixed clusters

applicationMonitoring cloudNativeFullStack OneAgent version 1.315+

You can selectively configure Dynatrace code module injection to use ephemeral volumes, even when the CSI driver is available on the node. In this case, code module injection behaves as described in [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) and [Storage optimization](#storage-optimization).

To do this, use the `oneagent.dynatrace.com/volume-type: "ephemeral"` annotation on the Pod, as shown in the code block below. The `oneagent.dynatrace.com/technologies` annotation is an additional optimization—see [Annotate the application pod](#technologies).

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "ephemeral" # no CSI driver involved



oneagent.dynatrace.com/technologies: "nginx"    # minimize storage consumption
```

This approach combines the storage optimizations provided by the CSI driver with the performance gains and enhanced resiliency of ephemeral-volume injection for selected pods and applications.

Example scenarios:

* [NGINX instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") and prior injection are recommended with an ephemeral volume for higher resiliency, while other workloads can be injected using the CSI driver, eliminating the need for any vendor-specific annotations.
* Mixed setups with and without node access, such as AWS Elastic Kubernetes Service (EKS) with EC2 nodes and Fargate. Ensure the CSI driver is available on all nodes where CSI-based code module injection can occur.