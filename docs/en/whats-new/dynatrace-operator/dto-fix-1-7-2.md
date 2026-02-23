---
title: Dynatrace Operator release notes version 1.7.2
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-2
scraped: 2026-02-23T21:29:57.315181
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