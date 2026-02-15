---
title: Migration of DynaKube v1beta2 to v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4
scraped: 2026-02-15T21:25:27.203240
---

# Migration of DynaKube v1beta2 to v1beta4

# Migration of DynaKube v1beta2 to v1beta4

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta2` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta2

**Introduced in**: Dynatrace Operator version 1.2.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta4

**Introduced in**: Dynatrace Operator version 1.5.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Replaced feature flags

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack: {} # same as autoUpdate: true



  # ...
  ```
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  image: ... # same effect as autoUpdate: false



  codeModulesImage: # same effect as autoUpdate: false



  # ...



  ---



  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  version: ... # replaces autoUpdate: false



  # ...
  ```

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.