---
title: Cisco UCS C-Series extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/cisco-ucs-c-series
scraped: 2026-03-06T21:36:04.473139
---

# Cisco UCS C-Series extension

# Cisco UCS C-Series extension

* Latest Dynatrace
* Extension
* Published Feb 21, 2025

Get insights into your Cisco UCS C-Series devices.

## Get started

### Overview

Monitor your Cisco UCS C-Series devices with data collected through the [UCS Manager XML APIï»¿](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book/b_ucs_api_book_chapter_00.html).

This extension collects infrastructure metrics and events for Cisco UCS C-Series hardware components, including CPU, fan modules, fans, memory, storage, power supplies, network adapters, and VIC interfaces.

### Use cases

* Monitor hardware health/state signals for CPUs, fan modules/fans, memory arrays/units, storage controllers, local disks, RAID batteries, power supplies, and virtual drives.
* Observe connectivity and status for adapters, external interfaces, vHBAs, and vNICs.
* Detect UCS faults and raise Dynatrace error events for faster issue triage.

### Compatibility information

* Dynatrace version 1.318+
* Cisco UCS C-Series device with access to the Cisco UCS Manager XML API.

### Requirements

* A user account with read-only privileges for UCS Manager XML API queries, provided to the extension as username/password.
* Network access from ActiveGate to the UCS endpoint.
* Ability for the configured user to perform API operations: `aaaLogin`, `configResolveClass`, `aaaLogout`.
* The specific classes queried depend on enabled feature sets:

  + C-Series Faults: `faultInst`
  + C-Series CPU: `processorUnit`
  + C-Series External Interface: `networkAdapterEthIf`
  + C-Series Fan Module / C-Series Fan Module (voltage): `equipmentFanModule`
  + C-Series Fan / C-Series Fan (voltage): `equipmentFan`
  + C-Series Local Disk / C-Series Local Disk (predictive failure count): `storageLocalDisk`
  + C-Series Memory Array: `memoryArray`
  + C-Series Memory Unit: `memoryUnit`
  + C-Series Network Adapter: `networkAdapterUnit`
  + C-Series Power Supply / C-Series Power Supply (voltage): `equipmentPsu`
  + C-Series Raid Battery: `storageRaidBattery`
  + C-Series Storage Controller: `storageController`
  + C-Series VIC Adapter: `adaptorUnit`
  + C-Series VIC External Interface: `adaptorExtEthIf`
  + C-Series VIC vHBA: `adaptorHostFcIf`
  + C-Series VIC vNIC: `adaptorHostEthIf`
  + C-Series Virtual Drive: `storageVirtualDrive`

## Activation and setup

Activate the extension in your environment from Dynatrace Hub, configure connection details for your UCS endpoint, and select the feature sets you want to collect.

## Details

The extension package contains:

* Overview dashboards (Classic & Platform)
* Analysis screens integrated with ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**
* Unified analysis pages
* Custom topology types extracted from metric dimensions:

  + Cisco UCS C-Series CPU
  + Cisco UCS C-Series External Interface
  + Cisco UCS C-Series Fan Module
  + Cisco UCS C-Series Fan
  + Cisco UCS C-Series Local Disk
  + Cisco UCS C-Series Memory Array
  + Cisco UCS C-Series Memory Unit
  + Cisco UCS C-Series Network Adapter
  + Cisco UCS C-Series Power Supply
  + Cisco UCS C-Series Raid Battery
  + Cisco UCS C-Series Storage Controller
  + Cisco UCS C-Series VIC Adapter
  + Cisco UCS C-Series VIC External Interface
  + Cisco UCS C-Series VIC vHBA
  + Cisco UCS C-Series VIC vNIC
  + Cisco UCS C-Series Virtual Drive
  + Cisco UCS C-Series Rack

### Licensing and costs

#### DPS licensing

[DPS license consumption](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") is based on metric data points ingested. The following formula provides an approximate annual ingest amount if all feature sets are enabled and the extension runs every minute:

```
((2 * # of CPUs)



+ (1 * # of External Interfaces)



+ (5 * # of Fan Modules)



+ (5 * # of Fans)



+ (5 * # of Local Disks)



+ (4 * # of Memory Arrays)



+ (2 * # of Memory Units)



+ (1 * # of Network Adapters)



+ (5 * # of Power Supplies)



+ (4 * # of Raid Batteries)



+ (1 * # of Storage Controllers)



+ (1 * # of VIC Adapters)



+ (1 * # of VIC External Interfaces)



+ (1 * # of VIC vHBAs)



+ (1 * # of VIC vNICs)



+ (2 * # of Virtual Drives))



* 525,600 metric data points/year
```

#### Classic licensing

For [Dynatrace classic licenses](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."), metric ingestion consumes Davis Data Units (DDUs) at a rate of 0.001 DDUs per metric data point.
For details, see [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

To estimate annual DDU consumption, multiply the result of the formula above by 0.001.