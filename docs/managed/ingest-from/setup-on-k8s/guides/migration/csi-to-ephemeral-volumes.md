---
title: Migrate from CSI driver to ephemeral volumes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/csi-to-ephemeral-volumes
---

# Migrate from CSI driver to ephemeral volumes

# Migrate from CSI driver to ephemeral volumes

* How-to guide
* 5-min read
* Updated on Jun 25, 2026

This guide describes the steps required to migrate your Dynatrace Operator deployment from CSI volumes to ephemeral volumes. Using the `csidriver.migrationMode` Helm value, you can complete this migration with a single pod-restart cycle instead of two, reducing disruption to your workloads.

## CSI migration mode

When migration mode is active:

* The CSI driver DaemonSet keeps the provisioner container running in cleanup-only mode. No new CSI mounts are created, and old OneAgent binaries on the node filesystem are cleaned up automatically.
* Dynatrace Operator and the webhook immediately switch to ephemeral volumes for all newly injected pods.
* The CSI driver pods continue running, so existing CSI-mounted pods can be cleanly unmounted when they restart.

## Prerequisites

* Dynatrace Operator version 1.10.0+
* You have an existing CSI-based injection setup (cloud-native full-stack or application monitoring with CSI enabled).
* You use Helm for Dynatrace Operator installation. For manifest-based installations, see [Migrate from manifests to Helm](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm "Migrate from manifests to Helm for Dynatrace Operator installation.") first.
* You have `kubectl` CLI access to the cluster.

## Migrate to ephemeral volumes

If you use `codeModulesImage` in your DynaKube, the Operator automatically switches to [node image pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")—no migration steps required. For the best update experience, enable [public registry auto-update](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") to let Dynatrace Operator resolve images automatically.

1. Enable migration mode

Upgrade Dynatrace Operator with `csidriver.migrationMode` enabled. This keeps the CSI DaemonSet running for unmounting while switching all new pod injections to ephemeral volumes.

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--namespace dynatrace \



--reset-then-reuse-values \



--set csidriver.enabled=true \



--set csidriver.migrationMode=true \



--atomic
```

After this upgrade, all newly injected pods use ephemeral-volume injection. Existing pods continue to use their current CSI mounts until they are restarted.

2. Restart injected workloads

Perform a restart of all workloads that currently use CSI-based injection. This triggers the webhook to inject them with ephemeral volumes instead of CSI volumes.

Example how to restart deployments

```
kubectl rollout restart deployment <deployment-name> -n <namespace>
```

Make sure to restart all injected workloads.

3. Verify no pods with CSI volumes remain

Verify that no pods still use CSI-based Dynatrace volumes. Run the following command to check for remaining CSI volume mounts:

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

Empty output means all pods have been migrated. If any pods are listed, restart the workload.

4. Disable the CSI driver

Ensure all workloads have been successfully migrated to ephemeral volumes before disabling the CSI driver. Any pods that still rely on CSI mounts will fail to function after the CSI driver is disabled. Verify the results from the previous verification step before proceeding.

After you confirm that no CSI volumes remain, disable the CSI driver to remove the CSI DaemonSet and all related resources.

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--namespace dynatrace \



--reset-then-reuse-values \



--set csidriver.enabled=false \



--atomic
```

This removes the CSI DaemonSet, ServiceAccount, RBAC resources, and the CSI driver object from your cluster.