---
title: Differences between containerized and host-based ActiveGates
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences
scraped: 2026-05-12T12:34:14.179709
---

# Differences between containerized and host-based ActiveGates

# Differences between containerized and host-based ActiveGates

* 1-min read
* Published Sep 01, 2023

ActiveGate deployed on a host using an installerâdepending on a selected [purpose](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.")âconsists of multiple processes delivering several functionalities. The container image covers only a subset of that, provided by the core ActiveGate process.

## Purposes

An ActiveGate container image currently supports only a subset of [routing and monitoring](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.") as well as [private synthetic](/managed/ingest-from/dynatrace-activegate/capabilities#synthetic "Learn the capabilities and uses of ActiveGate.").

For a complete overview, see [ActiveGate purposes and functionality](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

|  | **Installer** | **Container** |
| --- | --- | --- |
| OneAgent routing | Applicable | Applicable |
| API | Applicable | Applicable Not applicable Logs |
| Infrastructure Monitoring (VMware, CloudFoundry, DBInsights, Kubernetes) | Applicable | Applicable |
| Cloud monitoring | Applicable | Applicable Azure Not applicable AWS |
| Extensions | Applicable | Not applicable |
| Synthetic monitors | Applicable | Applicable |
| ZRemote | Applicable | Not applicable |

## Auto-update

[ActiveGate auto-update](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.") is supported only for host-based ActiveGates deployed using an installer.

In Kubernetes environments, ActiveGate updates are managed by the container runtime.

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image already specifies a certain version.

## Remote configuration management

[Remote configuration management](/managed/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") doesn't support containerized ActiveGates.

A containerized ActiveGate configuration is not persistently stored. It is declarative, using the Kubernetes native means of configuration, so any changes triggered by the remote configuration management mechanism would be lost upon container restart.