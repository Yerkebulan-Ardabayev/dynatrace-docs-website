---
title: Dynatrace Operator release notes version 1.8.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-8-1
scraped: 2026-02-22T21:28:09.782333
---

# Dynatrace Operator release notes version 1.8.1

# Dynatrace Operator release notes version 1.8.1

* Latest Dynatrace
* Release notes
* Updated on Feb 09, 2026

Release date: February 9th, 2026

This page provides an overview of the patches included in Dynatrace Operator version 1.8.1. For detailed information on new features and other enhancements, please refer to the [release notes for version 1.8](/docs/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0").

## Resolved issues

* ActiveGate permissions on OperatorHub marketplace

  Dynatrace Operator 1.8.1 now includes the RBAC resources that were previously missing for ClusterServiceVersion (CSV) based installations. The Dynatrace Operator bundle build process has been modified to overcome the CSV limitations regarding aggregated roles that caused this issue.

* Log monitoring allowlist on GKE Autopilot

  Fixed an issue with log monitoring on GKE Autopilot where the tenant suffix added to the HostPath for RKE support caused validation failures.

## Removal and deprecation notices

* The Helm repository located in `dynatrace/helm-charts` is deprecated and will stop receiving updates in a future release! If you are still using it,
  please update the URL to `dynatrace/dynatrace-operator` or switch to the OCI registry-based approach. Update the Helm repository URL with the following commands:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* To prevent potential disruptions, we strongly advise keeping your DynaKube API version up to date. Once a version is deprecated and removed, updates may become significantly more complex and time-sensitive.

  + More information about the deprecation process of the DynaKube API versions can be found in the [migration guide](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

## Upgrade from Dynatrace Operator version 1.7

* Specifying an image in `.spec.templates.otelCollector.imageRef` is now mandatory when [telemetry ingest](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") is enabled.
* Deprecated DynaKube API versions `v1beta1` and `v1beta2` have been removed from the DynaKube CRD schema.
* DynaKube API version `v1beta3` is no longer served and will be removed in a future Dynatrace Operator release. See: [Migration guide for DynaKube API versions](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")
* Upgrading Dynatrace Operator may restart the ActiveGate, the OneAgent DaemonSet (host agent), and Log Monitoring DaemonSet.
* If you are monitoring Kubernetes through the public Kubernetes API from within an in-cluster ActiveGate, you will need to recreate the bearer token because the name of the used ServiceAccount changed from `dynatrace-kubernetes-monitoring` to `dynatrace-activegate`. Follow the instructions at [Connect to the public Kubernetes API](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* Due to the aformentioned changes to the ActiveGate RBAC objects, setting `rbac.kspm.create: true` now requires `rbac.activeGate.create: true` and `rbac.kubernetesMonitoring.create: true`. **Be sure to adjust your Helm values if applicable before upgrading.**