---
title: Code modules delivery modes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes
---

# Code modules delivery modes

# Code modules delivery modes

* Reference
* 7-min read
* Updated on Sep 04, 2026

cloudNativeFullStack applicationMonitoring

On Kubernetes 1.35+, image volume injection is the recommended way to deliver OneAgent code modules to application pods. It requires no CSI driver, no privileged access, and the container runtime handles node-level caching natively. For clusters on older Kubernetes versions, ephemeral volume and CSI driver delivery remain available.

Notable use cases:

* Cloud-native full-stack monitoring works independently of the code modules delivery mode
* Cloud-native full-stack monitoring can be deployed via OpenShift OperatorHub.
* During a migration to image volumes, pods injected with image volumes and pods still using the CSI driver can coexist on the same cluster. See [Migrate to image volumes](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-image-volume "Step-by-step guide to migrating your Dynatrace Operator deployment to image volume injection for improved storage efficiency and security posture.").
* During a migration from CSI-based to ephemeral-volume injection, both can coexist on the same cluster. See [Enforce ephemeral-volume injection on mixed clusters](#mixed-mode).

| Delivery mode | CSI driver enabled | Storage overhead | When it applies | Notes |
| --- | --- | --- | --- | --- |
| [Image Volume](#ephemeral-node-image-pull) Recommended | No, image volume | Node-level cache (via container runtime) | Recommended for Kubernetes 1.35+. Opt-in via `feature.dynatrace.com/mount-code-modules-via-image-volume:"true"` | Best combination of storage efficiency and security posture. See [Migrate to image volume](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-image-volume "Step-by-step guide to migrating your Dynatrace Operator deployment to image volume injection for improved storage efficiency and security posture."). |
| [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) | No, ephemeral volume | Per-pod storage consumption | Default since Operator v1.10 when no CSI driver is enabled | Uses Node credentials. Image cached on each node. |
| [CSI driver image pull](#csi-image-pull) | Yes, CSI volume | Node-level cache | CSI driver enabled | Requires `customPullSecret` for private registries |
| [Node Image Pull via CSI volume](#csi-node-image-pull) | Yes, CSI volume | Node-level cache | CSI driver enabled. Opt-in via `feature.dynatrace.com/node-image-pull: "true"` | Uses Node credentials alongside the `customPullSecret` for private registries.[1](#fn-1-1-def) |

1

Because images are pulled by the Kubernetes node using node-level credentials, no `customPullSecret` is needed for private registries as long as the nodes are already configured to authenticate against the registry. For details, see [Prerequisites](#csi-node-image-pull-prerequisites).

## Volume types

Each code modules delivery mode instruments the application pod using a different volume type.

|  | Image volume | Ephemeral volume | CSI volume |
| --- | --- | --- | --- |
| **CSI driver required** | No | No | Yes |
| **Storage of Code Modules binary** | Node-level cache (managed by container runtime) | Per-pod (each pod gets its own copy) | Node-level cache (shared across pods on the same node) |
| **Credentials for private registries** | Node credentials or pod-level `imagePullSecrets` | Node credentials or pod-level `imagePullSecrets` | `customPullSecret` (or node credentials for Node Image Pull via CSI) |
| **When to use** | Kubernetes 1.35+ environment. Recommended for all new and existing deployments | Kubernetes version older than 1.35, or when image volumes are not yet available | Kubernetes version older than 1.35 with CSI driver already deployed |

## Image volume

Image volume injection is available from Kubernetes version 1.35+ and is the recommended delivery mode for new and existing deployments. The container runtime mounts the code modules image directly as a read-only volume in each injected pod. Because the runtime handles image caching at the node level, only one copy of the code modules image is stored per node regardless of how many pods are instrumented.

Image volume injection requires no CSI driver and no additional privileges, which makes it well suited for security-sensitive environments.

For setup instructions, see [Use image volumes for code modules injection](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/use-image-volumes "Configure Dynatrace Operator to deliver OneAgent code modules via image volumes for improved security and storage efficiency."). To migrate an existing deployment, see [Migrate to image volumes](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-image-volume "Step-by-step guide to migrating your Dynatrace Operator deployment to image volume injection for improved storage efficiency and security posture.").

Configuration

### Prerequisites

* Dynatrace Operator version 1.11+
* Kubernetes version 1.35+
* Container runtime with image volume support: ContainerD v2.2+ or CRI-O v1.33+
* A code modules image from a [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")

### DynaKube configuration

Add the `feature.dynatrace.com/mount-code-modules-via-image-volume` annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/mount-code-modules-via-image-volume: "true"
```

## Ephemeral volume

When the CSI driver is not enabled, code modules are copied into the application pod's ephemeral volume.

### Node Image Pull via Ephemeral Volume

Node Image Pull via Ephemeral Volume delivers OneAgent code modules by having the Kubernetes node pull the code modules image and copy the binaries into an ephemeral volume on each injected pod. No CSI driver is required, but each pod gets its own copy of the binaries, which increases per-pod storage consumption compared to node-level caching.

Since Dynatrace Operator version 1.10, Node Image Pull via ephemeral volumes is the default when no CSI driver is enabled. In previous versions, this behavior is gated by the `feature.dynatrace.com/node-image-pull: "true"` feature flag.

Configuration

#### Prerequisites

* Dynatrace OneAgent version 1.317+
* A Dynatrace code modules image sourced from a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

When using a private registry, the DynaKube `customPullSecret` does not apply to injected pods. Dynatrace Operator does not replicate pull secrets into application namespaces or add them to pods outside the `dynatrace` namespace. If the Kubernetes node is not authenticated to your private registry, the init container image pull fails. Ensure that all nodes are authenticated to the registry, or distribute a pull secret to your application namespaces, nodes, or pods. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").

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

Deprecated as of Dynatrace Operator version 1.11. Not supported on Latest Dynatrace environments. Use [Image Volume](#image-volume) or [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) instead.

Configuration

The injected init container downloads and unpacks the code module ZIP archive from your Dynatrace Environment into an ephemeral volume at pod startup. This delivery method is used when no code modules image is configured and the CSI driver is not enabled.

Drawbacks compared to image-based delivery:

* Each pod downloads the code modules ZIP from the Dynatrace Environment, which adds latency and load.
* The init container must have network access to the Environment API during pod startup.
* The binaries are not delivered as an OCI image, so image-signing and admission policies do not apply.

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

When code modules are delivered with the CSI driver, the code modules binaries are cached on the host filesystem and shared between pods, avoiding per-pod copies.

### CSI driver image pull

The CSI driver pulls the code modules image from a container image registry and exposes the code modules binaries on the host filesystem, where each injected application pod mounts them through a CSI volume.

Configuration

#### Prerequisites

* A Dynatrace code modules image sourced from a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry") or [resolved automatically](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

  + For private registries, configure a `customPullSecret`. Note that `customPullSecret` does not apply to injected pods in application namespaces. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").
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

  + For private registries, ensure all nodes are authenticated to the registry. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").
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

Deprecated as of Dynatrace Operator version 1.11. Not supported on Latest Dynatrace environments. Use [Image Volume](#image-volume) or [Node Image Pull via Ephemeral Volume](#ephemeral-node-image-pull) instead.

Configuration

The CSI driver downloads, extracts, and exposes the code modules ZIP on the host filesystem, where each injected application pod mounts them through a CSI volume. This delivery method is used when the CSI driver is enabled and no code modules image is configured.

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