---
title: Differences between containerized and host-based ActiveGates
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/differences
scraped: 2026-03-05T21:37:14.955623
---

# Differences between containerized and host-based ActiveGates


* Latest Dynatrace
* 1-min read
* Published Sep 01, 2023

ActiveGate deployed on a host using an installerâdepending on a selected [purpose](../capabilities.md "Learn the capabilities and uses of ActiveGate.")âconsists of multiple processes delivering several functionalities. The container image covers only a subset of that, provided by the core ActiveGate process.

## Purposes

An ActiveGate container image currently supports only a subset of [routing and monitoring](../capabilities.md#functional_tbl "Learn the capabilities and uses of ActiveGate.") as well as [private synthetic](../capabilities.md#synthetic "Learn the capabilities and uses of ActiveGate.").

For a complete overview, see [ActiveGate purposes and functionality](../capabilities.md "Learn the capabilities and uses of ActiveGate.").

## Auto-update

[ActiveGate auto-update](../operation/update-activegate.md "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.") is supported only for host-based ActiveGates deployed using an installer.

In Kubernetes environments, ActiveGate updates are managed by the container runtime.

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image already specifies a certain version.

## Remote configuration management

[Remote configuration management](../../bulk-configuration.md "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") doesn't support containerized ActiveGates.

A containerized ActiveGate configuration is not persistently stored. It is declarative, using the Kubernetes native means of configuration, so any changes triggered by the remote configuration management mechanism would be lost upon container restart.