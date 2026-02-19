---
title: Dynatrace Operator release notes version 1.7.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-0
scraped: 2026-02-19T21:26:06.336079
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

* You will now receive a warning if you enable `.spec.telemetryIngest` without specifiying `.spec.templates.openTelemetryCollector.imageRef`. The Dynatrace Operator will continue to use the `latest` image from the Dynatrace public ECR registry for the [OpenTelemetry collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."). However, using `latest` tags is an anti-pattern that should be avoided. Specifying the image will become mandatory in a future version.

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