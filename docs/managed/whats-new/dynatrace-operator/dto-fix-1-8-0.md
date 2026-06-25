---
title: Dynatrace Operator release notes version 1.8.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-8-0
scraped: 2026-05-12T12:05:26.349587
---

# Dynatrace Operator release notes version 1.8.0

# Dynatrace Operator release notes version 1.8.0

* Release notes
* Updated on Mar 31, 2026

Release date: January 27th, 2026

Upgrade to 1.8.1

If you're running Dynatrace Operator version 1.8, we recommend upgrading to version 1.8.1 to receive the latest important patches.

## Announcements

Dynatrace Operator version 1.8 introduces a new default and recommended DynaKube CRD version `v1beta6`. We encourage you to update your existing DynaKube resources to this latest version to take advantage of new features and enhancements.

### Automatic OTLP exporter configuration for applications instrumented with OpenTelemetry

Dynatrace Operator can now automatically configure applications instrumented with OpenTelemetry to export traces, metrics and logs to Dynatrace via the OTLP exporter auto-configuration feature. This simplifies configuration management and helps ensuring consistent telemetry ingest across environments.

For configuration details and examples, see the [OTLP auto-configuration guide](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

## New features and enhancements

* We introduced improvements to the [RBAC model used for Kubernetes monitoring](/managed/ingest-from/setup-on-k8s/reference/security#kubernetes-monitoring "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") via ActiveGate.

  + The `dynatrace-kubernetes-monitoring` ServiceAccount has been removed and replaced by the `dynatrace-activegate` ServiceAccount.
  + You can use [Kubernetes ClusterRole aggregationï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) to assign additional monitoring permissions to the `dynatrace-activegate` ServiceAccount during Operator installation. For details, see the [ClusterRole aggregation documentation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
  + The `dynatrace-kubernetes-monitoring` ClusterRole uses [Kubernetes ClusterRole aggregationï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) to assign the required permissions to the ServiceAccount during Operator installation.
  + The ServiceAccount token is only mounted to the ActiveGate statefulset if necessary. ActiveGates that no longer require the token (e.g. routingâonly ActiveGates) are restarted after Operator upgrade to ensure no ServiceAccount token remains mounted.
  + Setting `rbac.kspm.create: true` now requires `rbac.activeGate.create: true` and `rbac.kubernetesMonitoring.create: true`. **Be sure to adjust your Helm values if applicable before upgrading.**

* Dynatrace Operator now emits a Kubernetes warning event when the DynaKube or EdgeConnect CRD version is not the latest one supported by this Operator release. This makes it easier to identify outdated DynaKube CRD versions.

  + Dynatrace Operator RBAC permissions have been updated to include the `events.patch` permission for the `dynatrace` namespace.

* The Dynatrace Operator now uses the CA certificates provided via `.spec.caCertsRef` in requests to the Dynatrace API when rolling out EdgeConnect.

* The jobs the CSI driver creates for the [node image pull feature](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") now use the same PriorityClass as the CSI driver to ensure fast scheduling and allow preemption on congested nodes. The priority is configurable via the Helm value `csidriver.priorityClassValue`. For guidance, see [Use priorityClass for critical Dynatrace components](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Use priorityClass for critical Dynatrace components").

* Specifying an image in `.spec.templates.otelCollector.imageRef` is now mandatory when [telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") is enabled.

* Use the new pod annotation `dynatrace.com/split-mounts` to avoid conflicts with application images that already contain a `/var/lib/dynatrace` directory. This annotation is mainly intended to allow code module injection in ActiveGate pods for deep monitoring. It is enabled by default on ActiveGates managed by Dynatrace Operator.

* Dynatrace Operator components are made aware of pod memory limits by setting the environment variable [`GOMEMLIMIT`ï»¿](https://pkg.go.dev/runtime#hdr-Environment_Variables). This will make them more resilient against OOM kills, because it optimizes the Go garbage collector behaviour. Memory limits are set to 90% of the limits configured for Operator components via Helm (e.g. `csidriver.provisioner.resources.limts.memory`, `webhook.limits.memory`). The values can be provided using IEC suffixes (e.g. 123Mi).

* Namespaces selected for monitoring (matching the configured `namespaceSelectors` of `metadataEnrichment` or `oneAgent`) are written to the DynaKube conditions and to the operator log. This makes it easier to verify and troubleshoot the configured selectors.

* Kubernetes cluster and node metadata (such as cluster name, cluster UID, and node name) is now automatically added (via initContainer named `dynatrace-operator`) to OneAgent resource attributes to improve topological insights and provide a consistent set of resource attributes on all signals, regardless of origin.

* Detailed reasons for pod injection failures are now written to the `oneagent.dynatrace.com/reason`, `metadata-enrichment.dynatrace.com/reason`, and `otlp-exporter-configuration.dynatrace.com/reason` annotations on the affected pods. This makes troubleshooting pod injection issues faster and more transparent.

* Dynatrace Operator managed ActiveGate now use a liveness probe to improve detection of broken states.

* Default resource requirements for the jobs created by the CSI driver for the [node image pull feature](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") have been lowered. For guidance, see [Set resource limits for Dynatrace Operator components](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "Set resource limits for Dynatrace Operator components.")

## Resolved issues

* Handling removed API versions during Dyntrace Operator upgrade

  Kubernetes records CRD versions in `.status.storedVersions`, but doesnât remove entries when versions are deleted, so old versions accumulate and can block upgrades.

  In Dynatrace Operator 1.8.0 API versions `v1beta1` and `v1beta2` are removed from the Dynakube CRD. If you have been using Dynatrace operator < version 1.4.0 those versions are stored in the CRD in `.status.storedVersions` and require a clean up otherwise the upgrade to the new API version `v1beta6` will fail. With Dynatrace Operator version 1.7.3 we introduced a two-step solution to ensure smooth upgrades.

  1. Helm hook for CRD cleanup

     Before the actual upgrade, a Helm hook starts a Kubernetes Job that erases obsolete API versions from the DynaKube CRD's `status.storedVersions` field. The job only keeps the latest API version that is available in the Dynatrace Operator version installed **before** the upgrade. This step ensures a smooth upgrade to the new CRD during the Helm upgrade process. See [Dynatrace Operator security](/managed/ingest-from/setup-on-k8s/reference/security#upgrade-support "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for information regarding required permissions.
  2. Dynatrace Operator startup migration

     **After** the upgrade was successful and the new Dynatrace Operator version 1.8.0 is operational, it migrates all existing DynaKubes to the latest supported API version `v1beta6`. After the DynaKube migration, the `status.storedVersions` field in the DynaKube CRD is updated to hold only the latest API version `v1beta6` to ensure consistency.

  Important notice for clusters that have been running Dynatrace Operator version < 1.4.0 in the past

  + **If you have used Dynatrace Operator version <= 1.2 upgrading to Dynatrace Operator version 1.7.3 is mandatory as an intermediate step before upgrading to later releases to ensures a smooth and reliable transition.** As a general rule, skipping versions is not recommended.
  + Helm based installation

    When **using Helm** to install or upgrade from a Dynatrace Operator version >=1.3.0, no further action is required on your part. The required adjustments will be automatically handled by a Helm pre-upgrade hook during the upgrade progress.
  + Alternative installation methods

    **If you are relying on one of the alternative deployment methods listed below upgrading to Dynatrace Operator version 1.7.3 is mandatory as an intermediate step before upgrading to later releases to ensures a smooth and reliable transition.**

    - Red Hat OpenShift OperatorHub
    - OperatorHub.io
    - Google Marketplace
    - Plain Kubernetes manifests
  + Manual approach

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

* It is no longer possible to set `codeModulesImage` if the Dyntrace Operator CSI driver is disabled and neither `applicationMonitoring` nor `cloudNativeFullStack` is used. When attempting to do so, a validation error will be raised during DynaKube deployment or update.

* The `spec.templates.kspmNodeConfigurationCollector.nodeAffinity` field is now correctly applied to the KSPM Node Configuration Collector DaemonSet.

* KSPM DaemonSet now uses the built-in `privileged` SCC on OpenShift, eliminating the need for additional SCC configuration.

* The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") is now configured to skip using a proxy to connect to the in-cluster ActiveGate or the Kubernetes API.

* The cluster name used for the `k8s.cluster.name` attribute used for telemetry ingest now considers custom cluster names instead of only the DynaKube name.

* `subPath` is no longer used for `hostPath` volumes to improve compatibility across Kubernetes distributions (including RKE):

  + The underlying host path structure remains unchanged. The former `subPath` value is now appended at the end of the `hostPath`.

* There was an issue with the architecture of code modules images on ARM nodes. Default code modules images are now correctly downloaded.

* When enabled, the CSI driver is now correctly installed if Dynatrace Operator is deployed from Google Marketplace.

* Handle missing `builtin:app-transition.kubernetes` tenant settings object to support newer tenants that no longer have this object.

* Reduced maximum DynaKube name length according to enabled features to prevent issues when deploying components. The following name length limits are now enforced:

  + 32 characters if `spec.extensions` is enabled
  + 35 characters if `spec.kspm` is enabled
  + 38 characters if `spec.telemetryIngest` is enabled.
  + Existing resources that violate these new validation rules will continue to work as before, but will need to be fixed if a change or update is desired.

* Fixed an interoperability issue related to `metadataEnrichment` and `classicFullstack`. Now `metadataEnrichment` will work with `classicFullstack`. For more information, see [Dynatrace Operator support and known issues](/managed/ingest-from/technology-support/support-model-and-issues#classic-full-stack-with-metadata-enrichment "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

* Fixed a connectivity issue in Dynatrace Operator v1.7 that occurred between the OTLP exporter or CodeModules injected into application pods and the inâcluster ActiveGate when the [`automatic-tls-certificate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.") feature flag was switched from `true`to `false`. Starting with Operator v1.8.0, the TLS certificate previously created for the inâcluster ActiveGate is automatically removed from injected namespaces when `automatic-tls-certificate` is disabled.

* Changed mount point of EdgeConnect custom CA certificates to prevent overwriting well-known trusted CAs. Previous versions of the operator require including CA certs for public Dynatrace endpoints in the ConfigMap if EdgeConnect `.spec.caCertsRef` is set.

## Known issues

* Dynatrace Operator 1.8.0 is unable to establish Kubernetes monitoring when installed through OLM (Operator Lifecycle Manager) via OperatorHub. The Operator relies on aggregated ClusterRoles and their corresponding ClusterRoleBindings to set up the required permissions for Kubernetes monitoring. Since aggregated ClusterRoles are empty at build time (their rules are populated at runtime via aggregationRules), OLM incorrectly identifies them as empty and removes both the ClusterRole and ClusterRoleBinding manifests during installation. As a result, the necessary permissions are never granted, and Kubernetes monitoring cannot be established. This issue has been fixed in [Dynatrace Operator 1.8.1](/managed/whats-new/dynatrace-operator/dto-fix-1-8-1 "Release notes for Dynatrace Operator, version 1.8.1"), upgrading is strongly recommended.
* RBAC for Kubernetes monitoring requires elevated permissions to deploy the aggregated ClusterRole. This affects tooling, like ArgoCD, that manages workloads without cluster-admin permissions.

## Removal and deprecation notices

* [Support for Kubernetes 1.27](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") ended in July 2025. As a result, Dynatrace Operator 1.8.0+ will no longer support this version.
* The `dynatrace-kubernetes-monitoring` ServiceAccount will no longer exist. Instead, an aggregate ClusterRole is now bound to the `dynatrace-activegate` ServiceAccount, which will be used for Kubernetes monitoring permissions from this version onward. For more information, see the [ClusterRole aggregation documentation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
* If you have participated in the [Kubernetes Enhanced Object Visibility Preview](/managed/whats-new/preview-releases#k8s-object-visibility "Learn about our Preview releases and how you can participate in them.") and also unlocked monitoring of the sensitive Kubernetes objects ConfigMaps and Secrets, we recommend the following cleanup step, after upgrading to Operator 1.8.0:

  ```
  kubectl delete ClusterRoleBinding/dynatrace-kubernetes-monitoring-sensitive
  ```

  Details: Dynatrace Operator 1.8.0 uses `aggregationRules` to merge permissions from different ClusterRoles. This makes the ClusterRoleBinding `dynatrace-kubernetes-monitoring-sensitive` obsolete, which can safely be deleted after upgrading to Operator 1.8.0.

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* CSI sidecar binaries, located in `/usr/local/bin/csi-node-driver-registrar` and `/usr/local/bin/livenessprobe`, along with the Helm chart flags `csidriver.registrar.builtIn` and `csidriver.livenessprobe.builtIn` have been removed (deprecated in v1.7.0). The CSI driver pods will now always use the built-in implementations of livenessprobe and CSI node driver registrar. Customers who previously set these flags to `false` may observe a change in behavior. The purpose of this change is to minimize vulnerabilities in the Dynatrace Operator by ensuring prompt updates of these components.

* The OneAgent `autoUpdate` field has been removed. Automatic updates now follow your tenant's configured target version. To disable automatic updates, set either the `version` or `image` field in the DynaKube CR.

* The âMark for Terminationâ event is deprecated and will be removed in a future Operator version. This functionality is now redundant, as it has been superseded by host availability events on host shutdown and reboot introduced in OneAgent version 1.301.

## Upgrade from Dynatrace Operator version 1.7

* Specifying an image in `.spec.templates.otelCollector.imageRef` is now mandatory when [telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") is enabled.
* Deprecated DynaKube API versions `v1beta1` and `v1beta2` have been removed from the DynaKube CRD schema.
* DynaKube API version `v1beta3` is no longer served and will be removed in a future Dynatrace Operator release. See: [Migration guide for DynaKube API versions](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")
* Upgrading Dynatrace Operator may restart the ActiveGate, the OneAgent DaemonSet (host agent), and Log Monitoring DaemonSet.
* If you are monitoring Kubernetes through the public Kubernetes API from within an in-cluster ActiveGate, you will need to recreate the bearer token because the name of the used ServiceAccount changed from `dynatrace-kubernetes-monitoring` to `dynatrace-activegate`. Follow the instructions at [Connect to the public Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* Due to the aformentioned changes to the ActiveGate RBAC objects, setting `rbac.kspm.create: true` now requires `rbac.activeGate.create: true` and `rbac.kubernetesMonitoring.create: true`. **Be sure to adjust your Helm values if applicable before upgrading.**