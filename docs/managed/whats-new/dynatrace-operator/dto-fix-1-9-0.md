---
title: Dynatrace Operator release notes version 1.9.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-9-0
---

# Dynatrace Operator release notes version 1.9.0

# Dynatrace Operator release notes version 1.9.0

* Release notes
* Updated on Jul 16, 2026

Release date: April 13, 2026

On this page, you’ll find an overview of what’s new and improved in Dynatrace Operator version 1.9.0.

## New features and enhancements

* Metadata enrichment for OneAgent code modules:  
  When using `applicationMonitoring` or `cloudNativeFullstack`, `metadataEnrichment` is enabled automatically and does not need to be added explicitly. This ensures Kubernetes metadata is automatically added to all signals, giving full observability context without additional configuration.

* The SecurityContexts of Dynatrace OpenTelemetry Collector, EdgeConnect, NodeConfigCollector, and CSI driver containers have been updated to align with the latest [CIS Kubernetes Benchmark﻿](https://www.cisecurity.org/benchmark/kubernetes) and [Pod Security Standards (PSS)﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

* When Kubernetes monitoring is first enabled (for example, when onboarding a new cluster), KSPM settings are automatically configured. New clusters no longer require manual configuration. Existing clusters and their configurations are not affected. For details, see [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

* Legacy `dt.kubernetes.*` metadata enrichment attributes have been fully replaced by `k8s.*` attributes. For backward compatibility, the legacy attributes are still emitted by default. If you've migrated your dashboards, alerts, and queries to use `k8s.*`, you can disable the legacy attributes by setting `feature.dynatrace.com/enable-attributes-dt.kubernetes="false"` on the DynaKube. For the full list of feature flags, see [DynaKube feature flags for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.").

  + Affected attributes (with replacement from [Semantic dictionary](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")):

    - `dt.kubernetes.cluster.id` (replaced by `k8s.cluster.uid`)
    - `dt.kubernetes.workload.kind` (replaced by `k8s.workload.kind`)
    - `dt.kubernetes.workload.name` (replaced by `k8s.workload.name`)

* To improve startup times, the image pull policy now follows the Kubernetes default (`IfNotPresent` for tagged images, `Always` for `:latest` or untagged images) instead of being explicitly set to `Always`. You can configure the image pull policy in the DynaKube for operator managed components or the Helm chart for the operator itself. For configuration options, see [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* Following changes in Kubernetes 1.31+, AppArmor profiles are now configured directly in the pod or container `securityContext` instead of using annotations. No action is required — the Dynatrace Operator automatically applies the correct method based on your cluster version. If you're on Kubernetes 1.30 or earlier, the existing Helm chart-based AppArmor configuration continues to work but is deprecated and will be removed after Kubernetes 1.30 reaches end of life. For details, see [Enable AppArmor for enhanced security](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.").

* You can now control rolling update behavior directly in the DynaKube individually for OneAgent, ActiveGate, and LogMonitoring using the new `rollingUpdate` field. For details, see [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* The support archive now includes a `kubernetes-version.txt` file with the Kubernetes server version of the cluster.

## Resolved issues

* Fixed an issue where the Dynatrace Operator reset the replica count of ActiveGate, EdgeConnect, OpenTelemetry Collector, and databases extension reconcilers to default values on every reconciliation, interfering with horizontal pod autoscaling (HPA). The Operator no longer writes the `replicas` field, unless explicitly specified in the DynaKube.

* Fixed an issue where a secret creation failure for Dynatrace injection in one namespace aborted secret creation for all remaining namespaces.

* The Helm value `customPullSecret` is now applied to all components deployed in the Dynatrace namespace.

* Injection behavior controlled by `dynatrace.com/inject`, `otlp-exporter-configuration.dynatrace.com/inject`, and the DynaKube feature flag `feature.dynatrace.com/automatic-injection` is now aligned with the OneAgent and metadata enrichment injection mechanisms. For details about the available settings for these flags, see [Pod and container annotations](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config#annotations "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

* Namespace validation now also covers OTLP-exporter auto-configuration. Applying a DynaKube fails with an error if its `namespaceSelector` for OneAgent injection, metadata enrichment, or OTLP-exporter configuration overlaps with another DynaKube. Ensure that each namespace is assigned to only one DynaKube for injection.

* Resolved an issue where CSI volumes could stop working after a node restart due to faulty backoff logic. Mount availability is now verified before backing off.

* Fixed an issue where the ActiveGate TLS secret was not cleaned up correctly due to an incorrect deletion name. The correct `<dynakube>-activegate-tls` name is now used.

* Fixed a connectivity issue between in-cluster ActiveGate and CodeModules agents. TLS certificate secrets in monitored namespaces are now correctly removed when no longer needed — for example, when a user disables the `automatic-tls-certificate` feature flag. Previously, stale secrets were still being mounted into application pods, causing connectivity failures due to an expired ActiveGate TLS certificate.

* The `app.kubernetes.io/version` label on deployed Extensions Execution Controller (EEC) pods now reflects the version specified in the DynaKube. Previously, the label incorrectly contained the operator version or was empty.

* The EdgeConnect AppArmor annotation that was previously set by the Operator has been removed, as it was never enforced and had no effect. Note that the annotation approach only works on Kubernetes 1.30 and earlier — on Kubernetes 1.31+, the `securityContext`-based AppArmor configuration is not yet supported for EdgeConnect. To set an AppArmor profile on Kubernetes 1.30 or earlier, use the EdgeConnect `spec.annotations` field. For details, see [Enable AppArmor for enhanced security](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.").

* Fixed an issue where the node-image-pull job for downloading Dynatrace code modules used a node name instead of a node selector, causing suboptimal interaction with the Kubernetes scheduler.

* Fixed an issue where deleting a DynaKube and recreating it with a different name caused the Kubernetes cluster connection settings in Dynatrace to be overwritten, changing the cluster name visible in the Dynatrace UI. The Operator now reconciles the Kubernetes cluster entity before modifying settings, ensuring existing configuration is preserved.

* Fixed an issue where the ActiveGate entered an initial `Error` phase during deployment before reconciling successfully.

* Aggregated ClusterRoles are no longer used. This resolves a known incompatibility with OperatorHub and aligns with least-privilege principles, as their use requires additional permissions during Dynatrace Operator installation. The Dynatrace Operator deployment now uses standard ClusterRoles exclusively. For details, see [ClusterRole aggregation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

## Known issues

* If Dynatrace Operator injects a seccomp profile into an application pod in OpenShift, [SecurityContextConstraints (SCCs)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies) that prevent seccomp profile usage — such as `anyuid`, `restricted`, or `nonroot` — will no longer apply. The system will instead fall back to another SCC (for example `restricted-v2`), which may render pods unschedulable or cause workload degradation.

  [Disable seccomp profile for Dynatrace init containers](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Overview of seccomp profile configuration for Dynatrace components.") if you are affected.

## Removal and deprecation notices

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* The `operator.apparmor`, `webhook.apparmor`, and `csidriver.apparmor` Helm values are deprecated. On Kubernetes version 1.31+, set AppArmor using `appArmorProfile` in the `podSecurityContext` instead. These values will continue to work until Kubernetes version 1.30 reaches end of life (August 2026). See [Enable AppArmor for enhanced security](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor "Apply AppArmor profiles on Dynatrace components for enhanced security.") for details.

* The `feature.dynatrace.com/oneagent-max-unavailable` flag is deprecated. Use the `rollingUpdate` field in the DynaKube instead. For details, see [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

## Upgrade from Dynatrace Operator version 1.8

In Dynatrace Operator version 1.9, the DynaKube API version `v1beta3` is removed from the CRD. Applying DynaKube resources using this version will fail. Additionally, `v1beta4` is now deprecated. Update your DynaKube manifests to `v1beta6` before upgrading the Dynatrace Operator. For more information, see [Migration guide for DynaKube API versions](/managed/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

Pods injected via `applicationMonitoring` or `cloudNativeFullStack` now automatically receive metadata enrichment. If `metadataEnrichment` in the DynaKube was enabled only to support OneAgent injection, it can be removed.

The [feature flag](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Overview of seccomp profile configuration for Dynatrace components.") `feature.dynatrace.com/init-container-seccomp-profile` is now enabled by default. If you relied on the unspecified seccomp profile on injected init containers, set the flag to `false` on your DynaKube.