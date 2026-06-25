---
title: Dynatrace Operator release notes version 1.5.1
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-5-1
scraped: 2026-05-12T12:31:27.299698
---

# Dynatrace Operator release notes version 1.5.1

# Dynatrace Operator release notes version 1.5.1

* Release notes
* Updated on Nov 20, 2025

Release date: April 25, 2025

This page provides an overview of the patches included in Dynatrace Operator version 1.5.1. For detailed information on new features and other enhancements, please refer to the [release notes for version 1.5](/managed/whats-new/dynatrace-operator/dto-fix-1-5-0 "Release notes for Dynatrace Operator, version 1.5.0").

## Resolved issues

* Fixed an issue with the webhook's certificate handling mechanism. This bug caused certificate errors in webhooks, potentially leading to deployment issues for DynaKubes.

## Known issues

* We have identified the following issues with the newly introduced [node image pull feature](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") in Dynatrace Operator version 1.5:

  + Resolved with Dynatrace Operator version 1.6.0 and OneAgent version 1.317+ When the feature is used in **cloud-native full-stack monitoring mode without the CSI driver**, it may lead to incorrect detection of hosts, containers, and services, as well as inaccurate license consumption.

  + Resolved with Dynatrace Operator version 1.6.0 Using the feature with metadata enrichment and `metadata.dynatrace.com/<key>: <value>` annotations on the injected Namespaces will lead to a panic in the Operator's webhook and prevent the injected pods from being scheduled.

  + Resolved with OneAgent version 1.315+ When the feature is used in conjunction with the **technologies annotations** for [storage optimization without CSI driver](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#storage-optimization "Configure node image pull"), it may lead to crash-loops or OneAgent misbehavior of injected Pods.

  + Resolved with OneAgent version 1.313.45+ There is a known issue with OneAgent versions >= 1.313.0 to < 1.313.45. If you upgrade to OneAgent version 1.313, make sure to use version 1.313.45+.

  When switching from using the CSI driver without `codeModulesImage` to using it with [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"), ensure that the CSI driverâs filesystem does not contain a code module for the specified DynaKube. If it does, the CSI driver will fail and require manual intervention to recover.

  Please note that all other features of Dynatrace Operator v1.5 are functioning correctly.
* GKE Marketplace Due to a change in the release process, [keyless verification](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#dynatrace-operator "Verify Dynatrace image signatures") is not supported for Dynatrace Operator version 1.5.1.

## Upgrade from Dynatrace Operator version 1.4

* Dynatrace Operator version 1.5.0 Default DynaKube version is now `v1beta4`. Make sure to update your DynaKube accordingly to use newly introduced features!

* The Dynatrace Operator now automatically generates certificates to facilitate secure communication between your in-cluster ActiveGate and other Dynatrace components. This feature is enabled by default and requires ActiveGate version 1.307.35 or higher. To use this feature, ensure your ActiveGate is updated to version 1.307.35+. If you prefer to disable this feature, set the feature flag `feature.dynatrace.com/automatic-tls-certificate: false` in your Dynakube configuration.