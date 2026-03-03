---
title: Cisco UCS M-Series extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/cisco-ucs-m-series
scraped: 2026-03-03T21:29:29.779660
---

# Cisco UCS M-Series extension

# Cisco UCS M-Series extension

* Latest Dynatrace
* Extension
* Published Feb 21, 2025

Get insights into your Cisco UCS M-Series devices.

## Get started

### Overview

Monitor your Cisco UCS M-Series devices with data collected through the [UCS Manager APIï»¿](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book/b_ucs_api_book_chapter_00.html).

This extension collects infrastructure metrics to monitor the health and performance of your Cisco UCS M-Series devices and their components including CPU, fans, power supplies, interfaces and more.

### Use cases

* Monitor chassis and hardware health signals, including CPU temperature/current, fan, fan module, PSU, memory array, storage controller, local disk, and switch card properties.
* Track Ethernet traffic and error counters for UCS ports, including receive/transmit bytes/packets, pause/error/collision counters, and utilization/headroom metrics.
* Observe Fabric Interconnect environmental and system metrics.
* Analyze uplink and pool-level behavior through metrics for Ethernet, server, and network port pools.
* Detect device anomalies and avoid outages.

### Compatibility information

* Dynatrace version 1.318+
* Cisco UCS M-Series device with access to the Cisco UCS Manager XML API.

### Requirements

* A user account with read-only privileges for UCS Manager XML API queries, provided to the extension as username/password.
* Network access from ActiveGate to the UCS endpoint.
* Ability for the configured user to perform API operations: `aaaLogin`, `configResolveClass`, `aaaLogout`.
* The specific classes queried depend on enabled feature sets:

  + M-Series CPU: `processorUnit`, `processorEnvStats`
  + M-Series Fan Module: `equipmentFanModule`, `equipmentFan`
  + M-Series Fan: `equipmentFan`
  + M-Series Local Disk: `storageLocalDisk`
  + M-Series Memory Array: `memoryArray`
  + M-Series Power Supply: `equipmentPsu`
  + M-Series Storage Controller: `storageController`
  + M-Series Ethernet Port: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series EthPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series NetworkPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series ServerPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Fabric Interconnect: `networkElement`, `swEnvStats`, `swSystemStats`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Fabric Ethernet LAN Port Channel: `fabricEthLanPc`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Host Ethernet Interface: `adaptorHostEthIf`, `adaptorEthPortStats`, `adaptorVnicStats`
  + M-Series Organization: `orgOrg`
  + M-Series Rack Server: `computeRackUnit`
  + M-Series Service Profile: `lsServer`, `adaptorEthPortStats`, `adaptorVnicStats`
  + M-Series Switch Card: `equipmentSwitchCard`

## Activation and setup

Activate the extension in your environment from Dynatrace Hub, configure connection details for your UCS endpoint, and select the feature sets you want to collect.

## Details

The extension package contains:

* Overview dashboards (Classic & Platform)
* Analysis screens integrated with ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**
* Unified analysis pages
* Custom topology types extracted from metric dimensions:

  + Cisco UCS M-Series CPU
  + Cisco UCS M-Series Fan Module
  + Cisco UCS M-Series Fan
  + Cisco UCS M-Series Local Disk
  + Cisco UCS M-Series Memory Array
  + Cisco UCS M-Series Power Supply
  + Cisco UCS M-Series Storage Controller
  + Cisco UCS M-Series Ethernet Port
  + Cisco UCS M-Series Ethernet Port Pool
  + Cisco UCS M-Series Network Port Pool
  + Cisco UCS M-Series Server Port Pool
  + Cisco UCS M-Series Fabric Interconnect
  + Cisco UCS M-Series Fabric Ethernet LAN PC
  + Cisco UCS M-Series Host Ethernet Interface
  + Cisco UCS M-Series Organization
  + Cisco UCS M-Series Rack
  + Cisco UCS M-Series Service Profile
  + Cisco UCS M-Series Switch Card

### Licensing and costs

#### DPS licensing

[DPS license consumption](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") is based on metric data points ingested. The following formula provides an approximate annual ingest amount if all feature sets are enabled and the extension runs every minute:

```
(2 * # of CPUs)



+ (1 * # of Fan Modules)



+ (1 * # of Fans)



+ (1 * # of Local Disks)



+ (1 * # of Memory Arrays)



+ (1 * # of Power Supplies)



+ (1 * # of Storage Controllers)



+ (38 * # of Ethernet Ports)



+ (12 * # of Ethernet Port Pools)



+ (12 * # of Network Port Pools)



+ (12 * # of Server Port Pools)



+ (45 * # of Fabric Interconnects)



+ (34 * # of Fabric Ethernet LAN PCs)



+ (20 * # of Host Ethernet Interfaces)



+ (1 * # of Organizations)



+ (1 * # of Racks)



+ (20 * # of Service Profiles)



+ (1 * # of Switch Cards)



* 525,600 metric data points/year
```

#### Classic licensing

For [Dynatrace classic licenses](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."), metric ingestion consumes Davis Data Units (DDUs) at the rate of 0.001 DDUs per metric data point.
For details, see [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

To estimate annual DDU consumption, multiply the result of the formula above by 0.001.