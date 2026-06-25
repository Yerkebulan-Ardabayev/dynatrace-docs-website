---
title: Dynatrace Operator release notes version 1.4.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-4-0
scraped: 2026-05-12T12:31:17.659711
---

# Dynatrace Operator release notes version 1.4.0

# Dynatrace Operator release notes version 1.4.0

* Release notes
* Published Dec 10, 2024

Release date: Dec 9, 2024

## Announcements

* [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") is now available via the Dynatrace Operator. For more information, visit [Security Posture Management](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

* Dynatrace version 1.310+ OneAgent version 1.309+ Dynatrace Operator version 1.4.2+ A new `logMonitoring` section in DynaKube enables easy configuration of log collection
  for OneAgent and the new OneAgent Log Module. The `logMonitoring` section can be used in combination with any deployment mode like `cloudNativeFullStack` or `applicationMonitoring`.

* Available with a future Dynatrace version (CQ2/2025) Leverage Dynatrace extensions in Kubernetes to integrate and monitor technologies with Dynatrace.
  Explore and onboard technologies by activating extensions via Dynatrace Hub or selected in-product screens. By configuring the `extensions` field in DynaKube,
  the Dynatrace Operator will rollout and manage the extension components including Dynatrace OpenTelemetry Collector and Extension Execution Controller in your Kubernetes environment.

## New features and enhancements

* In DynaKube version `v1beta3`, the `useCSIDriver` field is removed from in the `spec` section. The operator now derives this setting from the Dynatrace Operator deployment configuration. Existing DynaKubes will continue to function, disregarding this field.

* The init container has been renamed from `install-oneagent` to `dynatrace-operator` to reflect its broader functionality and purpose.

* Using the ActiveGate API is now simpler, as services for both HTTP and HTTPS ports are always created.

* The experimental feature flag `feature.dynatrace.com/multiple-osagents-on-node` has been removed.

* If the `image` field for ActiveGate or OneAgent is left unspecified, images from the Dynatrace built-in registry are used, which only support the x86-64 CPU architecture. Consequently, the node affinity for ActiveGate and OneAgent defaults to x86-64 when the `image` field is not set.
  Requiring other CPU architectures or multi-arch images? Please consult our [public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Use a public registry") documentation.

* The `version` field now affects the versions used for OneAgent and OneAgent Code Modules in cloud-native full-stack and application monitoring mode. The `image` fields take precedence over the `version` field.

* The `apiUrl` field of a DynaKube is now immutable. To change it, delete the existing DynaKube and create a new one.

* Dynatrace adheres to the principle of least privilege. To avoid granting unnecessary permissions, the Dynatrace Operator Helm chart allows configuration of Kubernetes RBAC permissions via the `rbac` section in the Helm values file. Please refer to this section in the Helm chart to manage the RBAC resources.

## Resolved issues

* Resolved an issue in DynaKube validation where the OneAgent version field was incorrectly rejecting standard version strings (e.g., 1.200.0.20240501-085142).

* Resolved an issue with the `highAvailability` field in the Helm chart that caused a PodDisruptionBudget to be created for the Dynatrace Operator Webhook even when `highAvailability` was set to `false`.

* Resolved an issue where the labels and annotations of the EdgeConnect custom resource were not propagated to EdgeConnect pods.

* Resolved an issue where the EdgeConnect status in the custom resource did not accurately reflect the Podâs failure state.

## Removal and deprecation notices

* The âMark for Terminationâ event is deprecated and will be removed in a future Operator version. This functionality is now redundant, as it has been superseded by host availability events on host shutdown and reboot introduced in OneAgent version 1.301.

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* As the Dynatrace OneAgent Operator reached its end-of-life on April 1, 2023, we are deprecating its listing in several OLM marketplaces. This includes certified-operators, redhat-marketplace-operators, community-operators, and community-operators-prod. For migration, please visit [Migrating from OneAgent Operator to Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc").

## Upgrade from Dynatrace Operator version 1.3

* Manifests When installing Dynatrace Operator using manifests, the `kubernetes-csi.yaml` file now includes all Operator components, including the CSI driver. This makes the use of `kubernetes.yaml` redundant and it **must no longer be applied**. Previously, `kubernetes-csi.yaml` contained only the CSI driver component. Applying both manifests sequentially as was required before will result in an error. The Dynatrace webhook will reject DynaKubes that require a CSI driver (even if the CSI driver is running correctly).