---
title: Dynatrace Operator release notes version 1.6.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-6-3
scraped: 2026-03-06T21:34:29.094701
---

# Dynatrace Operator release notes version 1.6.3


* Latest Dynatrace
* Release notes
* Updated on Nov 20, 2025

Release date: September 20, 2025

This page provides an overview of the patches included in Dynatrace Operator version 1.6.3. For detailed information on new features and other enhancements, see the release notes for version 1.6.

## Resolved issues

* Reintroduced the `mark for termination` event, which was previously removed in Dynatrace Operator version 1.6.0, to address challenges in reliably detecting node terminations in setups facilitating auto-scaler. This feature requires your API token to have the `DataExport` token scope.

## Known issues

We have identified the following known issues with Dynatrace Operator version 1.6.3

When switching from using the CSI driver without `codeModulesImage` to using it with node image pull, ensure that the CSI driverâs filesystem does not contain a code module for the specified DynaKube. If it does, the CSI driver will fail and require manual intervention to recover.

## Upgrade from Dynatrace Operator version 1.5

No breaking changes.