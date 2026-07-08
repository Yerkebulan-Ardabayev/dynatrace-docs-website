---
title: Azure Service Fabric
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-fabric
---

# Azure Service Fabric

# Azure Service Fabric

* How-to guide
* 1-min read
* Published Mar 28, 2024

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM Metadata such as Azure regions, scale sets and more
* Automatic instrumentation including containerized applications

Note that we don't have an OOTB instrumentation for the Azure Service Fabric Programming Model (Reliable Services and Actors). Instead, use a custom instrumentation using OpenTelemetry.

## Installation

To deploy OneAgent on Azure Service Fabric, follow the same procedure as for [Azure Virtual Machines Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.").