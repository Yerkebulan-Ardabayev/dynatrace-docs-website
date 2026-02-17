---
title: Migration of DynaKube v1beta5 to v1beta6
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6
scraped: 2026-02-17T05:09:16.821230
---

# Migration of DynaKube v1beta5 to v1beta6

# Migration of DynaKube v1beta5 to v1beta6

* Latest Dynatrace
* Reference
* 5-min read
* Published Jan 20, 2026

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta5` to `apiVersion: dynatrace.com/v1beta6` of the DynaKube.

## Support lifecycle

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

### v1beta6

**Introduced in**: Dynatrace Operator version 1.8.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Moved fields

#### `spec.extensions`

The `spec.extensions` field was moved to `spec.extensions.prometheus` to accommodate the new `spec.extensions.databases` field. The functionality remains the same.