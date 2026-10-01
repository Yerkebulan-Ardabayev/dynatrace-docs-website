---
title: Dynatrace Operator release notes version 1.8.1
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-8-1
---

# Dynatrace Operator release notes version 1.8.1

# Dynatrace Operator release notes version 1.8.1

* Release notes
* Updated on Sep 16, 2026

**Release date:** February 9, 2026

**Minimum operator version required for direct upgrade:** 1.4.0—see [Upgrade from older versions](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#upgrade-path "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator."). Review the release notes for each intermediate version and pay attention to breaking changes before upgrading.

This page provides an overview of the patches included in Dynatrace Operator version 1.8.1. For detailed information on new features and other enhancements, please refer to the [release notes for version 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0").

## Resolved issues

* ActiveGate permissions on OperatorHub marketplace

  Dynatrace Operator 1.8.1 now includes the RBAC resources that were previously missing for ClusterServiceVersion (CSV) based installations. The Dynatrace Operator bundle build process has been modified to overcome the CSV limitations regarding aggregated roles that caused this issue.

  **Limitation:** The ClusterRoleBinding included in this fix is hard-coded to reference the `dynatrace-activegate` ServiceAccount in the `dynatrace` namespace. If you deploy the Dynatrace Operator in a different namespace, the required permissions for Kubernetes monitoring are not granted, resulting in the same behavior as version 1.8.0.

* Log monitoring allowlist on GKE Autopilot

  Fixed an issue with log monitoring on GKE Autopilot where the tenant suffix added to the HostPath for RKE support caused validation failures.

## Known issues

* RBAC for Kubernetes monitoring requires elevated permissions to deploy the aggregated ClusterRole. This affects tooling, like ArgoCD, that manages workloads without cluster-admin permissions.

## Removal and deprecation notices

* Removed Rancher Kubernetes Engine 1 (RKE1) from supported distributions.
* The Helm repository located in `dynatrace/helm-charts` is archived and no longer receives updates. If you still install or upgrade Dynatrace Operator from it, switch to the OCI registry:

  ```
  helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



  --version <version> \



  --namespace dynatrace \



  --reset-then-reuse-values \



  --install
  ```

  If you can't use OCI, point your Helm repository to `dynatrace/dynatrace-operator` instead:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

  For details, see [Migrate from the legacy Helm repository](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#helm-repo-migrate "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.").

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

## Upgrade from Dynatrace Operator version 1.7

* Specifying an image in `.spec.templates.otelCollector.imageRef` is now mandatory when [telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") is enabled.
* Deprecated DynaKube API versions `v1beta1` and `v1beta2` have been removed from the DynaKube CRD schema.
* DynaKube API version `v1beta3` is no longer served and will be removed in a future Dynatrace Operator release. See: [Migration guide for DynaKube API versions](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")
* Upgrading Dynatrace Operator may restart the ActiveGate, the OneAgent DaemonSet (host agent), and Log Monitoring DaemonSet.
* If you are monitoring Kubernetes through the public Kubernetes API from within an in-cluster ActiveGate, you will need to recreate the bearer token because the name of the used ServiceAccount changed from `dynatrace-kubernetes-monitoring` to `dynatrace-activegate`. Follow the instructions at [Connect to the public Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* Due to the aformentioned changes to the ActiveGate RBAC objects, setting `rbac.kspm.create: true` now requires `rbac.activeGate.create: true` and `rbac.kubernetesMonitoring.create: true`. **Be sure to adjust your Helm values if applicable before upgrading.**

Important notice for clusters that have been running Dynatrace Operator version 1.3 and earlier in the past

Clusters that have previously run Dynatrace Operator version 1.3 and earlier may have obsolete `v1beta1` or `v1beta2` entries in the DynaKube CRD's `.status.storedVersions`. These must be removed before upgrading to this release, or the CRD upgrade will fail.

Whether you need to stop at Dynatrace Operator version 1.7.3 first depends on your installation method:

* **Helm-based installation**

  + **Current version 1.4.0 and later**—No action required. The Helm pre-upgrade hook automatically removes obsolete `.status.storedVersions` entries during the upgrade.
  + **Current version 1.3 and earlier**—You must upgrade to Dynatrace Operator 1.7.3 before upgrading to the next release.
* **Alternative installation methods** (Red Hat OpenShift OperatorHub, OperatorHub.io, Google Marketplace, or plain Kubernetes manifests)

  + **Never ran version 1.3 and earlier**—No action required.
  + **Previously ran version 1.3 and earlier**—You must upgrade to Dynatrace Operator 1.7.3 before upgrading to the next release.

Manually remove obsolete entries from `.status.storedVersions`

Instead of upgrading to version 1.7.3, you can manually remove the obsolete entries from `.status.storedVersions`:

1. List the stored versions in the CRD:

   ```
   kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
   ```
2. Continue only if multiple versions are listed in the output. If only one version is listed, no action is required.
3. Identify the currently active version:

   ```
   storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
   ```
4. Convert all DynaKubes to the active version:

   ```
   kubectl get dynakube -n dynatrace -o yaml | kubectl replace -f -
   ```
5. Remove all previous versions while keeping the active version:

   ```
   kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
   ```

Ensuring that `.status.storedVersions` is clean is crucial to avoid issues with future upgrades.

ArgoCD may display resources that are still using an old API version as "out-of-sync".