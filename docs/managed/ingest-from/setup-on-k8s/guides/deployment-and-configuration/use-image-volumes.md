---
title: Use image volumes for code modules injection
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/use-image-volumes
---

# Use image volumes for code modules injection

# Use image volumes for code modules injection

* How-to guide
* 5-min read
* Published Sep 04, 2026

applicationMonitoring cloudNativeFullStack

Image volume injection is the recommended code modules delivery mode on Kubernetes 1.35+, providing secure, storage-efficient, and more reliable code modules injection into application pods. The container runtime caches a single shared copy of the code modules image per node, the same way it caches application container images. Other previously available [code modules delivery modes](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") each require a tradeoff: the [CSI driver](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-volume "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") is storage-efficient but requires a dedicated DaemonSet with [elevated privileges](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Components of Dynatrace Operator"), and [ephemeral volume injection](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-volume "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") needs no privileged access but is [storage-inefficient](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#storage-optimization "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). Image volume injection eliminates both tradeoffs.

## Prerequisites

* Dynatrace Operator version 1.11+
* Kubernetes version 1.35+
* Container runtime that supports image volumes and `subPath` mounts:

  + ContainerD v2.2+ or CRI-O v1.33+
* A code modules image from a [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")

Image volume injection is not compatible with the Dynatrace built-in tenant registry. Use a code modules image sourced from the [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), or mirrored to a [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry") from the public registry.

Verify container runtime version

Run the following command to check the container runtime version on each node:

```
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.nodeInfo.containerRuntimeVersion}{"\n"}{end}'
```

Example output:

```
ip-172-31-0-249.ec2.internal    containerd://2.2.5
```

## Enable image volume injection

### Enable image volume injection cluster-wide via DynaKube annotation

Add the `feature.dynatrace.com/mount-code-modules-via-image-volume: "true"` annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/mount-code-modules-via-image-volume: "true"
```

The `feature.dynatrace.com/mount-code-modules-via-image-volume` annotation is mutually exclusive with `feature.dynatrace.com/node-image-pull`. Enabling both results in a validation error.

### Override injection mode per pod via annotation

Before committing to a full cluster-wide migration, you can test image volume injection on a single pod. Non-annotated pods continue to use their current injection mode.

Add the `oneagent.dynatrace.com/volume-type: "image"` annotation to your workload's `spec.template.metadata.annotations`:

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "image"
```

Pod-level annotations override the injection mode set on the DynaKube. A pod annotated with `oneagent.dynatrace.com/volume-type: "image"` is injected with image volumes even if the DynaKube is configured to use CSI or ephemeral volume-based injection.

A pod restart is required for the annotation to take effect. Existing running pods are not re-injected automatically.

## Verify injection

Confirm that pods are injected with image volumes by checking the volume mounts on an injected pod:

```
kubectl describe pod <pod-name> -n <namespace>
```

In the output, look for a volume of type `image` in the `Volumes` section. Example:

```
Volumes:



oneagent-bin:



Type:        Image (a container image or OCI artifact)



Reference:   public.ecr.aws/dynatrace/dynatrace-codemodules:<version>
```

## Rollback image volume injection

### Rollback cluster-wide via DynaKube annotation

To disable image volume injection for all pods in a cluster, remove the `feature.dynatrace.com/mount-code-modules-via-image-volume: "true"` annotation from your DynaKube and re-apply it.

Then restart your workloads. Pods revert to the injection mode your DynaKube was previously configured to use. If the CSI driver is enabled, pods revert to [CSI volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-volume "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") injection. If the CSI driver is disabled, pods revert to [Node Image Pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") injection, which is the default since Dynatrace Operator version 1.10.

### Rollback individual pods via annotation

To override the injection mode for a specific pod, set the `oneagent.dynatrace.com/volume-type` annotation to `"csi"` or `"ephemeral"`:

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "csi"      # force CSI volume injection
```

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "ephemeral" # force ephemeral volume injection
```

Pod-level annotations override the DynaKube-configured injection mode. A pod annotated with `"csi"` or `"ephemeral"` uses the specified injection mode even if the DynaKube is configured for image volume injection.