---
title: Dynatrace Operator release notes version 1.5.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-5-0
scraped: 2026-05-12T12:34:43.716211
---

# Dynatrace Operator release notes version 1.5.0

# Dynatrace Operator release notes version 1.5.0

* Release notes
* Published Apr 01, 2025

Release date: April 24, 2025

Important notice

If you're running Dynatrace Operator version 1.5.0, we recommend upgrading to version 1.5.1 to receive the latest important patches.

## Upcoming changes

### Kubernetes dimension names change

The Kubernetes dimension names (`dt.kubernetes.cluster.id`, `dt.kubernetes.workload.kind`, `dt.kubernetes.workload.name`) won't be available starting with Dynatrace Operator version 1.8.0.

If you're still using them, update your configuration, queries, and other references to the new names as soon as possible.

| Deprecated name | New name |
| --- | --- |
| `dt.kubernetes.cluster.id` | `k8s.cluster.uid` |
| `dt.kubernetes.workload.kind` | `k8s.workload.kind` |
| `dt.kubernetes.workload.name` | `k8s.workload.name` |

## New features and enhancements

* The new node image pull feature introduces new capabilities for image pulling, along with enhanced performance, security and flexibility in the Dynatrace Operator. For more information on the feature, see our guide for configuring [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull").

* For `cloudNativeFullStack` and `hostMonitoring`, OneAgent (host module) no longer depends on the CSI driver. If the CSI driver is not deployed, a `hostPath` volume is utilized instead. The default path (`/var/opt/dynatrace`) can be overriden via the `storageHostPath` field.

* You can now add a PersistentVolumeClaim (PVC) to your containerized ActiveGate to avoid data loss across unexpected restarts. We recommend to add a PVC when using [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."). Learn how to configure a PVC in our [guide](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") and protect yourself from losing log data.

* [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") can now be enabled by adding `debugging` to [`.spec.activeGate.capabilities`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#active-gate "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* [OneAgent log module](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") and the CSI driver are now supported on GKE Autopilot.

## Resolved issues

* The log module was unable to retrieve metadata from the Kubernetes API. This issue was resolved by providing the service account token with the appropriate permissions to the OneAgent pod.

* Tenant tokens can be manually rotated using the [Dynatrace API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens."). This process has been simplified, as the restart of ActiveGate and OneAgent to utilize the new token is now handled automatically, eliminating the need for manual restarts.

* The issue where stray operator logs were inadvertently included in the binary zip output during support archive generation, causing the zip file to become corrupted on non-Linux systems, has been resolved.

* Providing custom arguments to the OneAgent ([.spec.oneagent.\*.args](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#one-agent "List the available parameters for setting up Dynatrace Operator on Kubernetes.")) could potentially result in duplications. To prevent unforeseen side effects, duplicates are now avoided, except for arguments `--set-host-property` and `--set-host-tag`.

  *Note:* Providing `--set-host-tag` multiple times with the same tag value is not allowed. Such a DynaKube configuration will be rejected.

* Host properties are typically provided to the OneAgent in `key=value` pairs using `--set-host-property` arguments. An issue that caused DynaKube configurations to be rejected has now been resolved, allowing the desired host properties to be set successfully.

* The Helm `.debug` switch now accepts string values, which are correctly interpreted.

* The `/var/logs` host directory mount is now read-only to ensure access to journald and kubelet logs.

## Removal and deprecation notices

* The âMark for Terminationâ event is deprecated and will be removed in a future Operator version. This functionality is now redundant, as it has been superseded by host availability events on host shutdown and reboot introduced in OneAgent version 1.301.

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

## Upgrade from Dynatrace Operator version 1.4

* Dynatrace Operator version 1.5.0 Default DynaKube version is now `v1beta4`. Make sure to update your DynaKube accordingly to use newly introduced features!

* The Dynatrace Operator now automatically generates certificates to facilitate secure communication between your in-cluster ActiveGate and other Dynatrace components. This feature is enabled by default and requires ActiveGate version 1.307.35 or higher. To use this feature, ensure your ActiveGate is updated to version 1.307.35+. If you prefer to disable this feature, set the feature flag `feature.dynatrace.com/automatic-tls-certificate: false` in your Dynakube configuration.