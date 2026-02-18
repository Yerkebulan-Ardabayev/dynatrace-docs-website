---
title: Dynatrace Operator release notes version 1.7.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-3
scraped: 2026-02-18T21:33:31.147965
---

# Dynatrace Operator release notes version 1.7.3

# Dynatrace Operator release notes version 1.7.3

* Latest Dynatrace
* Release notes
* Updated on Jan 15, 2026

Release date: January 19th, 2025

## Resolved issues

### Handling removed API versions during Dyntrace Operator upgrade

Kubernetes records CRD versions in `.status.storedVersions`, but doesnât remove entries when versions are deleted, so old versions accumulate and can block upgrades.

In Dynatrace Operator versions < 1.4, deprecated `v1beta1` and `v1beta2` were automatically added to `.status.storedVersions` and never cleaned up. Thus, any cluster that had been running versions before 1.4 is affected. If these versions remain during a future upgrade, CRD installation will fail. This release introduces a two-step solution to ensure smooth upgrades:

1. Helm hook for CRD cleanup

   During upgrade, a Helm hook starts a Kubernetes Job that erases obsolete API versions from the DynaKube CRD's `status.storedVersions` field. The job only keeps the latest API version that is available in the Dynatrace Operator version installed **before** the upgrade. This step ensures a smooth upgrade to the new CRD during the Helm upgrade process. See [Dynatrace Operator security](/docs/ingest-from/setup-on-k8s/reference/security#upgrade-support "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for information regarding required permissions.
2. Dynatrace Operator startup migration

   **After** the upgrade was successful and the new Dynatrace Operator version 1.7.3 is operational, it migrates all existing DynaKubes to the latest supported API version `v1beta5`. After the DynaKube migration, the `status.storedVersions` field in the DynaKube CRD is updated to hold only the latest API version `v1beta5` to ensure consistency.

Important notice for clusters that have been running Dynatrace Operator version < 1.4.0 in the past

* **If you have used Dynatrace Operator version <= 1.2 upgrading to Dynatrace Operator version 1.7.3 is mandatory as an intermediate step before upgrading to later releases to ensures a smooth and reliable transition.** As a general rule, skipping versions is not recommended.
* Helm based installation

  When **using Helm** to install or upgrade from a Dynatrace Operator version >=1.3.0, no further action is required on your part. The required adjustments will be automatically handled by a Helm pre-upgrade hook during the upgrade progress.
* Alternative installation methods

  **If you are relying on one of the alternative deployment methods listed below upgrading to Dynatrace Operator version 1.7.3 is mandatory as an intermediate step before upgrading to later releases to ensures a smooth and reliable transition.**

  + Red Hat OpenShift OperatorHub
  + OperatorHub.io
  + Google Marketplace
  + Plain Kubernetes manifests
* Manual approach

  Instead of upgrading to version 1.7.3, you can manually perform the required adjustments to the CRD

  1. Run the following command to list stored versions in the CRD of your cluster.

     ```
     kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
     ```
  2. Continue the procedure if `v1beta1` or `v1beta2` are listed in the stored versions of the CRD in your cluster.
  3. Identify the currently active version:

     ```
     storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
     ```
  4. Convert all DynaKubes to the active version:

     ```
     kubectl get dynakube -n dynatrace -o yaml | kubectl apply -f -
     ```
  5. Remove all previous versions while keeping the active version:

     ```
     kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
     ```

Ensuring that the CRD's `.status.storedVersions` field is properly cleaned up is crucial to avoid issues with future upgrades.

ArgoCD may display resources that are still using an old API version as "out-of-sync".

## Known issues

We have identified the following known issues with Dynatrace Operator versions 1.7.0â1.7.3. For other known issues, see [Dynatrace Operator support and known issues](/docs/ingest-from/technology-support/support-model-and-issues#well-known-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

* Due to optimization of the injected mounts (combining them under `/var/lib/dynatrace`), Dynatrace components can no longer be injected with the OneAgent.

* Classic full-stack and metadata enrichment are not compatible and cannot be used to inject the same application pods.

## Removal and deprecation notices

* The deprecated Dynatrace OneAgent Operator has been removed from the operatorhub.io catalog. Please use our [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/quickstart#deploy-dynatrace-operator "Deploy Dynatrace Operator on Kubernetes") instead.

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* The following API versions of the DynaKube CustomResourceDefinition have been removed in Dynatrace Operator version 1.7.0:

  + `v1beta1`
  + `v1beta2`
* The following API versions of the DynaKube CustomResourceDefinition are marked for deprecation and will be removed in the specified Dynatrace Operator versions:

  + `v1beta3` will be removed with Dynatrace Operator version 1.8

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* The DynaKube field `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` is deprecated and should no longer be used. The flag will be removed in a future version of the Dynatrace Operator. Do one of the following:

  + Pin the OneAgent version on your tenant to control all connected Kubernetes clusters at once.
  + Use the `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version` field to pin the version on a per-DynaKube basis.

* CSI sidecar binaries, located in `/usr/local/bin/csi-node-driver-registrar` and `/usr/local/bin/livenessprobe`, are now deprecated and will be removed in a future version of Dynatrace Operator.
* [Support for OpenShift 4.10 and 4.11](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") ended in March 2025. As a result, Dynatrace Operator 1.7.0 will no longer support these versions.

## Upgrade from Dynatrace Operator version 1.6

In Dynatrace Operator version 1.7, the DynaKube API versions `v1beta1` and `v1beta2` are no longer served. Applying DynaKube resources using these versions will fail. Update your DynaKube manifests to `v1beta5` before upgrading the Dynatrace Operator. For more information, see [Migration guide for DynaKube API versions](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").