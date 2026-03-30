---
title: SNMP generic server extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/snmp-generic-server
scraped: 2026-03-04T21:39:18.259271
---

# SNMP generic server extension


* Latest Dynatrace
* Extension
* Published Feb 19, 2026

Monitor server infrastructure health and performance using SNMP protocol in environments where you can't deploy OneAgent.

## Get Started

### Overview

This extension collects generally supported SNMP infrastructure metrics to monitor the health and resource usage of servers. Metrics are collected through SNMP get polling.

### Use cases

* Monitoring of server infrastructure where a OneAgent isn't feasible to install.
* Unix Servers: As an alternative to: [Remote Unixï»¿](https://www.dynatrace.com/hub/detail/remote-unix-monitoring-20/)
* Windows Servers: As an alternative to WMI: [Remote Windowsï»¿](https://www.dynatrace.com/hub/detail/remote-windows-host-monitoring/)

### Compatibility information

* Any device which supports SNMP polling and one or more of the following MIBs:

  + HOST-RESOURCES-MIB
  + UCD-SNMP-MIB
  + ENTITY-SENSOR-MIB
* Unix: Net-SNMP software agent running. [Red Hat documentation exampleï»¿](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/sect-system_monitoring_tools-net-snmp)
* Windows: the SNMP service needs to be enabled and configured. [Microsoft documentationï»¿](https://learn.microsoft.com/en-us/windows/win32/snmp/snmp-start-page)

## Activation and setup

Simply activate the extension in your environment using the in-product Hub and provide the required device connection configurations.
This extension uses the Dynatrace SNMP Data source.

## Details

This extension collects SNMP OID metrics from commonly supported MIBs. Most feature sets map to general entries or tables within the MIB files.

* **SNMPv2-MIB**: System properties such as `sysname` and the `sysuptime` metric.
* **HOST-RESOURCES-MIB**: Monitoring basic system resources such as CPU, memory, storage, and running processes on a host.
* **UCD-SNMP-MIB**: Monitoring detailed system metrics such as load averages, disk I/O
* **ENTITY-SENSOR-MIB**: Monitoring of physical sensors such as temperature, voltage, fan speed, and others.

### FAQ

What is the Custom Metric Usage of this extension?

The custom metric usage can be managed through which feature sets you choose to enable. `sysuptime` is the only enforced metric as part of the 'default' feature set. You can also use filter variables to restrict collection of specific paths and sensor types [Dimension Filtersï»¿](https://community.dynatrace.com/t5/Dynatrace-tips/Extensions-2-0-How-to-use-dimension-filters/m-p/230904)
All other feature sets are based on an Object Entry or Table within the SNMP Mib. e.g., `hr-storage fs` = [HR hrStorageStableï»¿](https://mibs.observium.org/mib/HOST-RESOURCES-MIB/#hrStorageTable). Sometimes this is split into multiple for even more granular selection such as `ucd-system-cpu-basic`, `ucd-system-cpu-detailed` and `ucd-system-swap` which all come from: [UCD systemStatsï»¿](https://mibs.observium.org/mib/UCD-SNMP-MIB/#systemStats).

To estimate the metrics ingested you can use a formula such as:

```
Scalar OIDs: 1 metric per OID


#metric_keys_in_fs


Table OIDs: 1 metric per each table entry (e.g., sensor, disk, process, file):


#metric_keys_in_fs * #entries_in_table
```