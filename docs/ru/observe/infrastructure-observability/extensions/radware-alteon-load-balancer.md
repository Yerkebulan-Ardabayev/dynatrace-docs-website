---
title: Radware Alteon Load Balancer extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/radware-alteon-load-balancer
scraped: 2026-02-18T21:30:08.882229
---

# Radware Alteon Load Balancer extension

# Radware Alteon Load Balancer extension

* Latest Dynatrace
* Extension
* Published Dec 15, 2025

Monitor your Radware Alteon Network Load Balancers through SNMP.

## Get started

### Overview

Monitor your Radware Alteon Network Load Balancer devices and interfaces through SNMP.

This extension collects infrastructure metrics to monitor the health and performance of your Radware Alteon Load Balancer devices.

![radware-1](https://dt-cdn.net/images/radware-dashboard-resized-2107-7e41f877d2.png)

![radware-2](https://dt-cdn.net/images/radware-device-resized-2085-dbb5255a5b.png)

### Use cases

* Monitor important device metrics such as uptime, CPU and memory usage, as well as additional hardware status metrics for temperature, fan, and power supply.
* Monitor device interfaces to report metrics including bytes, discards, and errors in/out.
* Collect additional device data, including virtual server utilization, HTTP and SSL statistics, throughput, and session counts. The full list of monitored metrics can be viewed under **Feature Sets**.
* Detect device anomalies and avoid outages.

### Compatibility information

* SNMP v2c or SNMP v3
* Dynatrace version 1.318+

## Activation and setup

Activate the extension in your environment using the in-product Hub, provide the necessary device configuration, and you're all set up.

For details, see the [SNMP extension data source documentation](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.").

## Details

The extension package contains:

* SNMP Data Source configuration
* Overview dashboard (Classic & Platform)
* Unified analysis screens
* Custom topology types extracted from metric dimensions:

  + Radware Alteon Device
  + Radware Alteon Interface
* SNMP MIB files used for monitoring:

  + IF-MIB
  + ALTEON-CHEETAH-LAYER4-MIB
  + ALTEON-CHEETAH-NETWORK-MIB
  + ALTEON-CHEETAH-SWITCH-MIB
  + ALTEON-ROOT-MIB

### Licensing and costs

Calculations are based on the assumption that you monitor all metrics for every feature set every minute:

DDUs: `(60 + (8 * Interfaces)) * 525.6 DDUs/year, per device`

DPS (Metric data points): `(60 + (8 * Interfaces)) * 525,600 metric data points/year, per device`