---
title: Migration guide for DynaKube API versions
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/dynakube
scraped: 2026-02-24T21:29:50.490627
---

# Migration guide for DynaKube API versions

# Migration guide for DynaKube API versions

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Jan 22, 2026

## Overview

Depending on your Dynatrace Operator Version, different `apiVersion`'s of the `DynaKube` are supported. This page collects the migration guides for each `apiVersion` considering the version of the Operator.

Starting with Dynatrace Operator version 1.8.0+, Dynatrace Operator emits a Kubernetes warning event if the installed DynaKube CRD version doesnât match the version expected by this Operator release.

### API Version Overview

| DynaKube API version | Introduced | Deprecated | Removed [1](#fn-1-1-def) | Migration guides |
| --- | --- | --- | --- | --- |
| v1beta5 | 1.6.0 |  |  |  |
| v1beta4 | 1.5.0 |  |  | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |
| v1beta3 | 1.3.0 | 1.7.0 |  | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |

1

The respective API version is no longer served with the stated Dynatrace Operator version. It will get deleted from the CRD in a subsequent version.

## Conversion strategies

### Automatic conversion

Each version of the Dynatrace Operator converts the deployed `DynaKubes` with an older `apiVersion` to the latest `apiVersion` supported by that Dynatrace Operator version.

* Example: Dynatrace Operator v1.6.x will always convert `DynaKubes` to `v1beta5`.

So when you are checking, using `kubectl` what `apiVersion` you are using, you will always see the latest `apiVersion` that is supported by that Dynatrace Operator version. You can facilitate this mechanism instead of doing a manual conversion.

1. Download the converted version of your DynaKube. The following command will give you the DynaKube converted to the latest supported `apiVersion`:

   ```
   kubectl get dynakubes -n <namespace> <dynakube-name> -o yaml
   ```
2. Cleanup the downloaded DynaKube, only keep this sections

   * relevant parts of `.metadata` section
   * complete `.spec` section

### Manual conversion

1. First, check the version of the Operator that is currently deployed. If you don't know which version you're running, here are some ways to find out.

   Using Helm:

   * Use the `helm list` command, the `APP VERSION` field tells you the version of the installed Dynatrace Operator.

     + Example:

   ```
   > helm list -n dynatrace -o json | jq -r '.[].app_version'`



   1.6.2
   ```

   Using `kubectl`:

   * There is an `app.kubernetes.io/version` label on the Dynatrace Operator Deployment that shows the version used.

     + Example:

   ```
   > kubectl get deployment dynatrace-operator -n dynatrace -o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'



   1.6.2
   ```
2. Then check the `apiVersion` of the `DynaKube` used and follow the matching migration guide in the [overview above](#overview).

## Removal process

The Dynatrace Operator follows a structured deprecation process that follows the [official Kubernetes guidanceï»¿](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning) to ensure smooth transitions between DynaKube API versions while providing adequate time for migration.

### Phase 1: Deprecation announcement

**Pre-deprecation notice**: An announcement is made in the release notes at least one Dynatrace Operator release before the deprecation takes effect.

**Deprecation marking**: The API version is officially marked as deprecated in the subsequent release, but remains fully functional and supported.

### Phase 2: Supported deprecation period

**Continued support**: The deprecated API version continues to be fully supported and functional during the deprecation period.

**Migration encouragement**: Users are strongly encouraged to migrate to the newer API version during this time using the provided migration guides.

**Automatic conversion**: The Operator automatically converts deprecated API versions to the latest supported version in the background, ensuring compatibility.

### Phase 3: Removal preparation

**API serving disabled**: After the support period ends, the deprecated API version is marked as `served: false` in the Custom Resource Definition (CRD).

**Conversion-only mode**: The API version schema is retained in the CRD for conversion purposes only, allowing existing resources to be read and converted.

**Migration deadline**: Users must complete their migration to the newer API version before this phase to ensure continued functionality of their DynaKube resources.

### Phase 4: Complete removal

**Schema removal**: The deprecated API version schema is completely removed from the CRD in a future Operator release.

**No conversion support**: After removal, no conversion or compatibility support is available for the deprecated API version.

### Migration timeline recommendations

* **Immediate action**: Plan your migration as soon as a deprecation notice is announced
* **Testing period**: Use the deprecation period to test the migration in non-production environments
* **Production migration**: Complete production migration well before the API serving is disabled
* **Validation**: Verify that all DynaKube resources are using the current API version after migration