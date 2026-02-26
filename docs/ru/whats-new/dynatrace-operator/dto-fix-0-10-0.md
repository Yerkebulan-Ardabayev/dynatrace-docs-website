---
title: Dynatrace Operator release notes version 0.10.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-0-10-0
scraped: 2026-02-26T21:23:43.718379
---

# Dynatrace Operator release notes version 0.10.0

# Dynatrace Operator release notes version 0.10.0

* Latest Dynatrace
* Release notes
* Published Dec 15, 2022

Release date: Nov 30, 2022

## New features and enhancements

* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change ActiveGate token support is now enabled by default.

  + An additional API token scope is required: `activeGateTokenManagement.create`
  + To disable it, set `feature.dynatrace.com/activegate-authtoken=false`
* You can [configure build label propagation from pod to environment variables](/docs/ingest-from/setup-on-k8s/guides#propagation "Detailed description of installation and configuration options for specific use-cases").
* You can [configure the CSI driver log garbage collection interval](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#limit-logs "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.").
* Recommended labels are added to the Dockerfile and release image.

### Troubleshoot subcommand

* Unless the `--dynakube` parameter is provided, all DynaKubes in the given namespace are analyzed.
* All errors detected by the `troubleshoot` subcommand are now displayed.

### Labels and annotations

* You can disable webhook injection for a pod in a monitored namespace with the following pod annotation: `dynatrace.com/inject=false`.
* Configurable labels and annotations for OneAgent and ActiveGate are added to the DynaKube custom resource.

### Feature flags

* You can configure release label propagation by setting the `feature.dynatrace.com/label-version-detection=true` feature flag in DynaKube.
* You can configure a more aggressive garbage collection on the CSI driver:

  + The `MAX_UNMOUNTED_VOLUME_AGE` environment variable on the `provisioner` container of the CSI driver pod sets the interval in days.

### Helm

* The `csidriver.maxUnmountedVolumeAge` parameter has been added to set the `MAX_UNMOUNTED_VOLUME_AGE` environment variable.

## Resolved issues

* Fixed the missing pod metadata for the enrichment file in case OneAgent injection is disabled.
* Fixed ActiveGate StatefulSet recreation when labeled externally.
* Fixed custom image handling in the `troubleshoot` subcommand.
* Fixed the missing `readOnlyRootFilesystem` for ActiveGate init container in case the feature flag is set.
* Reduced the default memory usage for Dynatrace Operator components by reducing logger instances.
* Lowered the default CSI driver OneAgent log garbage collection interval to seven days.

## References

See the [GitHub release notesï»¿](https://github.com/Dynatrace/dynatrace-operator/releases/tag/v0.10.0).