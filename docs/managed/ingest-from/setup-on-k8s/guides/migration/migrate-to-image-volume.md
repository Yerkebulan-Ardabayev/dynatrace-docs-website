---
title: Migrate to image volumes for code modules injection
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-image-volume
---

# Migrate to image volumes for code modules injection

# Migrate to image volumes for code modules injection

* How-to guide
* 5-min read
* Published Sep 01, 2026

Image volume injection is the recommended way to deliver OneAgent code modules on Kubernetes 1.35+. The container runtime mounts the code modules image directly as a read-only volume in each injected pod. Because the container runtime caches image at the node level, the image is pulled once per node and shared across all pods running on the same node.

Use this guide if you have an existing deployment using CSI driver or ephemeral volume injection and want to migrate to image volume injection.

## Prerequisites

* Dynatrace Operator version 1.11+
* Kubernetes version 1.35+
* Container runtime that supports image volumes and `subPath` mounts:

  + ContainerD v2.2+ or CRI-O v1.33+
* A code modules image from a [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") or [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")

Verify container runtime version

```
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.nodeInfo.containerRuntimeVersion}{"\n"}{end}'
```

Example output:

```
ip-172-31-0-249.ec2.internal    containerd://2.2.5
```

## Migrate individual workloads

To migrate specific pods before committing to a full cluster-wide migration, annotate individual pods. Non-annotated pods continue to use their current injection mode.

Add the `oneagent.dynatrace.com/volume-type: "image"` annotation to your pod definition:

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "image"
```

Pod-level annotations override the DynaKube-configured injection mode. A pod annotated with `oneagent.dynatrace.com/volume-type: "image"` is injected with image volumes even if the DynaKube is configured for CSI or ephemeral volume injection.

A pod restart is required for the annotation to take effect. Existing running pods are not re-injected automatically.

To verify injection, see [Verify injection](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-image-volume#expand--Verify-image-volume-injection--4 "Step-by-step guide to migrating your Dynatrace Operator deployment to image volume injection for improved storage efficiency and security posture.").
Once pod-level migration is validated, cluster-wide migration can be performed by enabling image volume injection on the DynaKube and restarting all injected workloads.

## Migrate all workloads cluster-wide

A full migration requires a rolling restart of all injected workloads.

1. Enable image volume injection on the DynaKube

Add the `feature.dynatrace.com/mount-code-modules-via-image-volume` annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/mount-code-modules-via-image-volume: "true"
```

The `feature.dynatrace.com/mount-code-modules-via-image-volume` annotation is mutually exclusive with `feature.dynatrace.com/node-image-pull`. Enabling both results in a validation error.

2. Restart injected workloads

Restart all workloads that are not yet using image volumes. The webhook re-injects them with image volumes on the next pod start.

```
kubectl rollout restart deployment <deployment-name> -n <namespace>
```

3. Verify image volume injection

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

## Rollback

To revert, remove the `feature.dynatrace.com/mount-code-modules-via-image-volume: "true"` annotation from your DynaKube, re-apply it, then restart your workloads. Pods revert to their previous injection mode.