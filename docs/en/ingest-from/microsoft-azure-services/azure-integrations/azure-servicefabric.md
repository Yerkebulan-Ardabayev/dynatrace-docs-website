---
title: Monitor Azure Service Fabric
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric
scraped: 2026-02-15T08:56:38.443738
---

# Monitor Azure Service Fabric

# Monitor Azure Service Fabric

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 19, 2017

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM Metadata such as Azure regions, scale sets and more
* Automatic instrumentation including containerized applications

Note that we don't have an OOTB instrumentation for the Azure Service Fabric Programming Model (Reliable Services and Actors). Instead, use a custom instrumentation using OpenTelemetry.

## Installation

To deploy OneAgent on Azure Service Fabric, follow the same procedure as for [Azure Virtual Machines Scale Set](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.").

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")