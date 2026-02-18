---
title: Migration of DynaKube v1beta3 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5
scraped: 2026-02-18T05:57:50.249451
---

# Migration of DynaKube v1beta3 to v1beta5

# Migration of DynaKube v1beta3 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta3` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta3

**Introduced in**: Dynatrace Operator version 1.3.0

**Deprecated in**: Dynatrace Operator version 1.6.0

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

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