# Dynatrace Documentation: whats-new/dynatrace-operator

Generated: 2026-02-16

Files combined: 7

---


## Source: dto-fix-0-10-0.md


---
title: Dynatrace Operator release notes version 0.10.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-0-10-0
scraped: 2026-02-15T09:10:04.785194
---

# Dynatrace Operator release notes version 0.10.0

# Dynatrace Operator release notes version 0.10.0

* Latest Dynatrace
* Release notes
* Published Dec 15, 2022

Release date: Nov 30, 2022

## New features and enhancements

* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change ActiveGate token support is now enabled by default.

  + An additional API token scope is required: `activeGateTokenManagement.create`
  + To disable it, set `feature.dynatrace.com/activegate-authtoken=false`
* You can [configure build label propagation from pod to environment variables](/docs/ingest-from/setup-on-k8s/guides#propagation "Detailed description of installation and configuration options for specific use-cases").
* You can [configure the CSI driver log garbage collection interval](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#limit-logs "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.").
* Recommended labels are added to the Dockerfile and release image.

### Troubleshoot subcommand

* Unless the `--dynakube` parameter is provided, all DynaKubes in the given namespace are analyzed.
* All errors detected by the `troubleshoot` subcommand are now displayed.

### Labels and annotations

* You can disable webhook injection for a pod in a monitored namespace with the following pod annotation: `dynatrace.com/inject=false`.
* Configurable labels and annotations for OneAgent and ActiveGate are added to the DynaKube custom resource.

### Feature flags

* You can configure release label propagation by setting the `feature.dynatrace.com/label-version-detection=true` feature flag in DynaKube.
* You can configure a more aggressive garbage collection on the CSI driver:

  + The `MAX_UNMOUNTED_VOLUME_AGE` environment variable on the `provisioner` container of the CSI driver pod sets the interval in days.

### Helm

* The `csidriver.maxUnmountedVolumeAge` parameter has been added to set the `MAX_UNMOUNTED_VOLUME_AGE` environment variable.

## Resolved issues

* Fixed the missing pod metadata for the enrichment file in case OneAgent injection is disabled.
* Fixed ActiveGate StatefulSet recreation when labeled externally.
* Fixed custom image handling in the `troubleshoot` subcommand.
* Fixed the missing `readOnlyRootFilesystem` for ActiveGate init container in case the feature flag is set.
* Reduced the default memory usage for Dynatrace Operator components by reducing logger instances.
* Lowered the default CSI driver OneAgent log garbage collection interval to seven days.

## References

See the [GitHub release notesï»¿](https://github.com/Dynatrace/dynatrace-operator/releases/tag/v0.10.0).


---


## Source: dto-fix-0-10-1.md


---
title: Dynatrace Operator release notes version 0.10.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-0-10-1
scraped: 2026-02-15T09:13:12.030608
---

# Dynatrace Operator release notes version 0.10.1

# Dynatrace Operator release notes version 0.10.1

* Latest Dynatrace
* Release notes
* Published Dec 15, 2022

Release date: Dec 15, 2022

## Resolved issues

* Fixed the conversion webhook in the custom resource definition by updating the namespace field correctly.

* Immutable OneAgent support: communication information is now stored both in `Secret` (`TenantToken`), and `ConfigMap` (`TenantUUID`, `CommunicationEndpoints`). This fixes the restarts on communication endpoint changes by mounting them from the configmap, instead of adding the contents of the configmap directly to the arguments.

* Fixed the missing Docker labels on the release image.

* The node-driver-registrar component is updated to version 2.6.2.

* Fixed a bug for the read-only `hostMonitoring` mode: read-only `hostMonitoring` mode needs the CSI driver, but the CSI driver didn't behave correctly, which prevents the OneAgent pod to start.

* Fixed a bug causing pods to be incorrectly unmounted due to a locked database: when there are several pods requesting a volume at the same time, the CSI driver doesn't unmount pods correctly if the database is locked at mount time.


---


## Source: dto-fix-0-10-2.md


---
title: Dynatrace Operator release notes version 0.10.2
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-0-10-2
scraped: 2026-02-15T21:27:18.616224
---

# Dynatrace Operator release notes version 0.10.2

# Dynatrace Operator release notes version 0.10.2

* Latest Dynatrace
* Release notes
* Published Jan 12, 2023

Release date: Jan 12, 2023

## Resolved issues

* Added support for code module images from public registry.

* The node-driver-registrar component is updated to version 2.7.0.
* The `livenessProbe` component is updated to version 2.9.0.
* Go is updated to version 1.19.4.


---


## Source: dto-fix-1-6-3.md


---
title: Dynatrace Operator release notes version 1.6.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-6-3
scraped: 2026-02-15T21:30:10.930960
---

# Dynatrace Operator release notes version 1.6.3

# Dynatrace Operator release notes version 1.6.3

* Latest Dynatrace
* Release notes
* Updated on Nov 20, 2025

Release date: September 20, 2025

This page provides an overview of the patches included in Dynatrace Operator version 1.6.3. For detailed information on new features and other enhancements, see the [release notes for version 1.6](/docs/whats-new/dynatrace-operator/dto-fix-1-6-0 "Release notes for Dynatrace Operator, version 1.6.0").

## Resolved issues

* Reintroduced the `mark for termination` event, which was previously removed in [Dynatrace Operator version 1.6.0](/docs/whats-new/dynatrace-operator/dto-fix-1-6-0#removal-and-deprecation-notices "Release notes for Dynatrace Operator, version 1.6.0"), to address [challenges](/docs/whats-new/dynatrace-operator/dto-fix-1-6-0#known-issues "Release notes for Dynatrace Operator, version 1.6.0") in reliably detecting node terminations in setups facilitating auto-scaler. This feature requires your API token to have the `DataExport` token scope.

## Known issues

We have identified the following known issues with Dynatrace Operator version 1.6.3

When switching from using the CSI driver without `codeModulesImage` to using it with [node image pull](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"), ensure that the CSI driverâs filesystem does not contain a code module for the specified DynaKube. If it does, the CSI driver will fail and require manual intervention to recover.

## Upgrade from Dynatrace Operator version 1.5

No breaking changes.


---


## Source: dto-fix-1-7-0.md


---
title: Dynatrace Operator release notes version 1.7.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-0
scraped: 2026-02-15T21:22:33.059648
---

# Dynatrace Operator release notes version 1.7.0

# Dynatrace Operator release notes version 1.7.0

* Latest Dynatrace
* Release notes
* Updated on Nov 28, 2025

Release date: September 8th, 2025

Important notice

If you're running Dynatrace Operator version 1.7.0, we recommend upgrading to version 1.7.1 to receive the latest important patches.

## Announcements

### Reduced volume mounts and read-only OneAgent binaries

The number of volume mounts required for injecting code modules into application pods has been reduced. Additionally, OneAgent binaries are now mounted as read-only to enhance security and stability. For more details, refer to the updated [workload mutation](/docs/ingest-from/setup-on-k8s/reference/workload-mutation "Application pod mutations when oneagent and/or metadata-enrichment is enabled.") documentation.

### Ephemeral volume size control via workload annotations

You can now limit the size of ephemeral volumes attached to injected application pods using workload annotations. For configuration details and sizing recommendations, refer to our [storage guide](/docs/ingest-from/setup-on-k8s/reference/storage#application-pod-volumes "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments").

### Permissions of ClusterRole `dynatrace-kubernetes-monitoring` have been extended

As Dynatrace extends its coverage of Kubernetes objects, the ActiveGate requires additional permissions. The following objects have been added to the `dynatrace-kubernetes-monitoring` role with `get/list/watch` permissions:

* `customresourcedefinitions`
* `ingresses`
* `networkpolicies`
* `endpointslices`
* `horizontalpodautoscalers`

## New features and enhancements

* The required scopes for the EdgeConnect OAuth client in [provisioner mode](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision "Provision EdgeConnect for a Dynatrace environment.") have been reduced.
  The scopes `settings:object:write` and `settings:object:read` are now only required if [Kubernetes automation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/kubernetes-automation/edge-connect-kubernetes-automation-operator-supported-setup "Set up the operator-supported EdgeConnect for Kubernetes Connector.") is used.

* The parameters of the `livenessProbe` of the CSI driver server container can now be configured in Helm. The following Helm switches have been added:

  + `.csidriver.server.livenessProbe.failureThreshold`
  + `.csidriver.server.livenessProbe.initialDelaySeconds`
  + `.csidriver.server.livenessProbe.periodSeconds`
  + `.csidriver.server.livenessProbe.successThreshold`
  + `.csidriver.server.livenessProbe.timeoutSeconds`

* You will now receive a warning if you enable `.spec.telemetryIngest` without specifiying `.spec.templates.openTelemetryCollector.imageRef`. The Dynatrace Operator will continue to use the `latest` image from the Dynatrace public ECR registry for the [OpenTelemetry collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace Collector."). However, using `latest` tags is an anti-pattern that should be avoided. Specifying the image will become mandatory in a future version.

* Dynatrace Operator uses an API token with a set of [scopes](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions#operatorToken "Configure tokens and permissions to monitor your Kubernetes cluster") to interact with the Dynatrace platform. With this release, the following changes have been made to the token scope requirements:

  + `entities.read` scope is no longer required
  + `settings.read` and `settings.write` become optional

Optional token scopes

The following features are limited in functionality if `settings.read` and `settings.write` are not present on the API token.

* Automatic Kubernetes API monitoring is disabled. You need to [enable it manually](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#local "Monitor the Kubernetes API using Dynatrace") for your tenant.
* The OneAgent Log module is initially deployed without a MonitoredEntityID context. As soon as the MonitoredEntityID is known, its configuration is updated and the OneAgent Log module is restarted. As a consequence, logs may initially miss the `topology:dt.entity.kubernetes_cluster` enrichment.

## Resolved issues

* The secret containing the auto-generated TLS certificate for ActiveGate is now properly removed when ActiveGate is disabled or deleted from the DynaKube configuration.

* The `.spec.templates.logMonitoring.resources` DynaKube setting now correctly applies resource requests to both the init and the main container of the LogMonitoring DaemonSet.

* A validation has been added to ensure that protocols are not included in the `.spec.apiServer` field of the EdgeConnect configuration.

* Updates to `.spec.oneAgent.(classicFullStack|cloudNativeFullStack|hostMonitoring).version` are now correctly applied if `.spec.oneAgent.(classicFullStack|cloudNativeFullStack|hostMonitoring).autoUpdate` is disabled.

* Dynatrace Operator now provides replacements for the external dependencies (binaries) used for the CSI liveness probe and the CSI node driver registrar. With mentioned replacements, increased frequency and promptness of updates will minimize vulnerabilities in the Dynatrace Operator.

  + The replacements are used by default. You can opt out of this behavior by setting by setting the Helm switches `csidriver.registrar.builtIn=false` and `csidriver.livenessprobe.builtIn=false`.
  + GKE Autopilot This configuration is not supported, since the CSI driver DaemonSet would no longer match the `WorkloadAllowlists`.

  The old binaries will remain part of the operator image for future releases. Until the final removal of binaries, vulnerability scanners might still report vulnerabilities.

* Resolved an issue in which the OpenTelemetry collector endpoint was not correctly switched from ActiveGate to the Dynatrace cluster after ActiveGate was removed from the DynaKube when `.spec.telemetryIngest` was enabled.

* Fixed an issue with duplicate container port names in the CSI driver daemonset that caused Kubernetes warnings.

* Fixed an issue where the injection init container added to application pods had a wrong value set to `.spec.securityContext.runAsNonRoot` in OpenShift environments.

* Proxy settings defined in `.spec.proxy` are now correctly applied to the LogMonitoring module. Additionally, the local ActiveGate service URL is automatically included in the `noProxy` configuration.

* The network zone specified in `.spec.networkZone` will now be correctly propagated to the `logMonitoring` DaemonSet.
  For existing deployments, where standalone `logMonitoring` and `.spec.networkZone` are already configured, the `logMonitoring` pods will be restarted to use the correct network zone configuration.

## Known issues

We have identified the following known issues with Dynatrace Operator version 1.7.0.

* In Kubernetes environments â especially those utilizing auto-scalers â there are challenges in reliably determining whether a node was intentionally removed or has failed unexpectedly. This ambiguity can lead to a high number of false-positive âHost is unavailableâ alerts, impacting monitoring accuracy and alerting quality.

* OneAgent versions earlier than `1.317` are incompatible with the reduced volume mount and read-only binary setup, as they can't read configuration files from writable locations used by the init container.

## Removal and deprecation notices

* The deprecated Dynatrace OneAgent Operator has been removed from the `operatorhub.io` catalog. Use [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/quickstart#deploy-dynatrace-operator "Deploy Dynatrace Operator on Kubernetes") instead.

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

  + `v1beta3` will be removed with Dynatrace Operator version 1.8.0

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* The DynaKube field `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` is deprecated and should no longer be used. The flag will be removed in a future version of the Dynatrace Operator. Do one of the following:

  + Pin the OneAgent version on your tenant to control all connected Kubernetes clusters at once.
  + Use the `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version` field to pin the version on a per-DynaKube basis.

* CSI sidecar binaries, located in `/usr/local/bin/csi-node-driver-registrar` and `/usr/local/bin/livenessprobe`, are now deprecated and will be removed in a future version of Dynatrace Operator.
* [Support for OpenShift 4.10 and 4.11](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") ended in March 2025. As a result, Dynatrace Operator 1.7 no longer supports these versions.

* The âMark for Terminationâ event is deprecated and will be removed in a future Operator version. This functionality is now redundant, as it has been superseded by host availability events on host shutdown and reboot introduced in OneAgent version 1.301.

## Upgrade from Dynatrace Operator version 1.6

Starting with this version, it is no longer possible to deploy a DynaKube with API versions `v1beta1` or `v1beta2`. Please update your DynaKube to the latest API version, `v1beta5`, before upgrading your Dynatrace Operator installation. For more information, see [Migration guide for DynaKube API versions](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").


---


## Source: dto-fix-1-7-2.md


---
title: Dynatrace Operator release notes version 1.7.2
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-2
scraped: 2026-02-15T21:24:25.312331
---

# Dynatrace Operator release notes version 1.7.2

# Dynatrace Operator release notes version 1.7.2

* Latest Dynatrace
* Release notes
* Updated on Jan 22, 2026

Release date: November 12th, 2025

## Resolved issues

* The OpenTelemetry Collector used for [telemetry ingest](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") now automatically includes the local ActiveGate service URL in its no-proxy configuration, ensuring that connections to the local ActiveGate bypass any configured proxies and avoiding unnecessary proxy hops or related connection issues.

## Known issues

We have identified the following known issues with Dynatrace Operator versions 1.7.0â1.7.2. For other known issues, see [Dynatrace Operator support and known issues](/docs/ingest-from/technology-support/support-model-and-issues#well-known-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

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


---


## Source: dto-fix-1-7-3.md


---
title: Dynatrace Operator release notes version 1.7.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-3
scraped: 2026-02-15T21:29:14.807134
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


---
