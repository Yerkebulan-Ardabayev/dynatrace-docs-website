---
title: Radware Alteon Load Balancer extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/radware-alteon-load-balancer
scraped: 2026-03-01T21:17:10.183401
---

# Radware Alteon Load Balancer extension

# Radware Alteon Load Balancer extension

* Latest Dynatrace
* Extension
* Updated on Feb 25, 2026

Monitor your Radware Alteon Network Load Balancer devices and interfaces through SNMP.

## Get started

### Overview

This extension collects infrastructure metrics to monitor the health and performance of your Radware Alteon Load Balancer devices.

![radware-1](https://dt-cdn.net/images/radware-dashboard-resized-2107-7e41f877d2.png)

![radware-2](https://dt-cdn.net/images/radware-device-resized-2085-dbb5255a5b.png)

### Use cases

* Monitor important device metrics such as uptime, CPU and memory usage, as well as additional hardware status metrics for temperature, fan, and power supply.
* Monitor device interfaces to report metrics including bytes, discards, and inbound and outbound errors.
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

### Licensing and cost

Calculations are based on the assumption that you monitor all metrics for every feature set every minute:

DDUs: `(60 + (8 * Interfaces)) * 525.6 DDUs/year, per device`

DPS (Metric data points): `(60 + (8 * Interfaces)) * 525,600 metric data points/year, per device`

## Feature sets

SSL\_Statistics\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| TCP sessions using SSL service | radware\_alteon.sslslbstat.cursessions | The current number of different TCP sessions using SSL service. |
| Total TCP sessions using SSL service | radware\_alteon.sslslbstat.totalsessions.count | The total number of different TCP sessions using SSL service. |
| TCP sessions using SSL service high water mark | radware\_alteon.sslslbstat.highestsessions.count | The high water mark of current sessions of different TCP sessions using SSL service. |
| SSL handshakes between clients and AAS per second | radware\_alteon.ssloff.newhandShake | New SSL handshakes between clients and AAS per second. |
| New SSL handshakes between Clients and AAS per second (sslOffPerEnhServNewhandShake) | radware\_alteon.ssloffper.enh.serv.newhandshake | Number of New SSL handshakes between Clients and AAS per second for this virtual service. |
| Number of expired SSL certificates per second for virtual service (sslOffPerEnhServExpiredCertificates) | radware\_alteon.ssloffper.enh.serv.expiredcertificates | Number of expired SSL certificates per second for virtual service. |

Hardware\_Status\_Physical

| Metric name | Metric key | Description |
| --- | --- | --- |
| Temperature sensor status | radware\_alteon.temperature.status | The status of the temperature sensor. ok(1), exceed(2) |
| Temperature warning threshold | radware\_alteon.temperature.threshold.warning | The temperature warning threshold |
| Temperature shutdown threshold | radware\_alteon.temperature.threshold.shutdown | The temperature shutdown threshold |
| Hardware fan status | radware\_alteon.fan.status | Hardware fan status. ok(1), fail(2), unplug(3) |
| Powersupply status | radware\_alteon.powersupply.status | Powersupply status. singlePowerSupplyOk(1), firstPowerSupplyFailed(2), secondPowerSupplyFailed(3), doublePowerSupplyOk(4), unknownPowerSupplyFailed(5) |

Session\_Table\_Utilization\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| Session table maximum entries | radware\_alteon.slbstat.maint.maximumsessions | The maximum number entries in the session table. |
| Ipv6 session count | radware\_alteon.slbstat.maint.ip6currsessions.count | The number of sessions for ipv6. |
| Curent sessions in session table | radware\_alteon.slbstat.maint.curbindings | The current number of sessions in the session table. |

default

| Metric name | Metric key | Description |
| --- | --- | --- |
| â | com.dynatrace.extension.network\_device.sysuptime | â |
| â | com.dynatrace.extension.network\_device.cpu\_usage | â |
| â | com.dynatrace.extension.network\_device.memory\_total | â |
| â | com.dynatrace.extension.network\_device.memory\_free | â |
| â | com.dynatrace.extension.network\_device.memory\_used | â |
| â | com.dynatrace.extension.network\_device.if.status | â |
| â | com.dynatrace.extension.network\_device.if.bytes\_in.count | â |
| â | com.dynatrace.extension.network\_device.if.bytes\_out.count | â |
| â | com.dynatrace.extension.network\_device.if.in.discards.count | â |
| â | com.dynatrace.extension.network\_device.if.out.discards.count | â |
| â | com.dynatrace.extension.network\_device.if.in.errors.count | â |
| â | com.dynatrace.extension.network\_device.if.out.errors.count | â |

Throughput\_Physical\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| Peak throughput of ports | radware\_alteon.peakthroughputusage.count | Peak throughput of ports in bits per second. |
| Current throughput of ports | radware\_alteon.curthroughputusage.count | Current throughput of ports in bits per second. |

Backend\_Server\_Utilization\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| Real-server current sessions | radware\_alteon.slbstat.enh.rserver.currsessions | Real-server current sessions. |
| Real-server total sessions | radware\_alteon.slbstat.enh.rserver.totalsessions | Real-server total sessions. |
| Real-server highest sessions | radware\_alteon.slbstat.enh.rserver.highestsessions | Real-server highest sessions. |
| Real-server total rx/tx octets | radware\_alteon.slbstat.enh.rserver.hc.octets | Real-server total rx/tx octets. |
| Real server max concurrent connections | radware\_alteon.slbcur.cfg.realserver.maxconns | The Maximum allowed number of concurrent connections per real server in the configuration. |
| SP current memory | radware\_alteon.spmemusagestats.currentmemory | The current memory of SP in kilobytes. |
| Real-server group current sessions | radware\_alteon.slbstat.enh.group.currsessions | The number of sessions that are currently handled by the real server group. |
| Real-server group total sessions | radware\_alteon.slbstat.enh.group.totalsessions | The total number of sessions that have been handled by the real server group. |
| Real-server group highest sessions | radware\_alteon.slbstat.enh.group.highestsessions | The highest sessions that have been handled by the real server group. |

Virtual\_Server\_Utilization\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| Virtual server current sessions | radware\_alteon.slbstat.enh.vserver.currsessions | The number of sessions that are currently handled by the virtual server. |
| Virtual server total sessions | radware\_alteon.slbstat.enh.vserver.totalsessions | The total number of sessions that are handled by the virtual server. |
| Virtual server highest sessions handled | radware\_alteon.slbstat.enh.vserver.highestsessions | The highest number of sessions that have been handled by the virtual server. |
| Total octets received and transmitted by the virtual server | radware\_alteon.slbstat.enh.vserver.hc.octets | The total octets received and transmitted by the virtual server. |
| Sessions handled by the virtual server | radware\_alteon.slbstat.enh.vserver.sessions | Number of Sessions handled by the virtual server per second. |
| Real server runtime status per virtual server | radware\_alteon.slbstat.enh.vserver.real.status | The runtime Real Server Status per Virtual service. (0)Up, (1)Down, (2)Admin-Down, (3)Warning, (4)Shutdown, (5)Error |
| Backend server concurrent connections for virtual service | radware\_alteon.commng.enh.perservstats.servconn | The number of concurrent backend server connections for virtual service. |
| Virtual service client requests passed to AX | radware\_alteon.commng.enh.perservstats.clireq | Number of client requests passed to AX for virtual service. |
| Virtual service security policy peak bandwidth (secPolPerServBwPeak) | radware\_alteon.secpol.perserv.bw.peak | Virtual service security policy stats - Bandwidth peak value. |
| Virtual service security policy bandwidth ( secPolPerServBwCurVal) | radware\_alteon.secpol.perserv.bw.curval | Virtual service security policy stats - Bandwidth current value. |
| Virtual service security policy PPS current (secPolPerServPPSCurVal) | radware\_alteon.secpol.perserv.pps.curval | Virtual service security policy stats - PPS current value. |
| Virtual service security policy PPS peak (secPolPerServPPSPeak) | radware\_alteon.secpol.perserv.pps.peak | Virtual service security policy stats - PPS peak value. |
| Virtual service security policy CPS current (secPolPerServCPSCurVal) | radware\_alteon.secpol.perserv.cps.curval | Virtual service security policy stats - CPS current value. |
| Virtual service security policy CPS peak (secPolPerServCPSPeak) | radware\_alteon.secpol.perserv.cps.peak | Virtual service security policy stats - CPS peak value. |
| Virtual service security policy latency current (secPolPerServLatencyCurVal) | radware\_alteon.secpol.perserv.latency.curval | Virtual service security policy stats - latency current value. |
| Virtual service security policy latency peak (secPolPerServLatencyPeak) | radware\_alteon.secpol.perserv.latency.peak | Virtual service security policy stats - latency peak value. |

Software\_Status\_SP

| Metric name | Metric key | Description |
| --- | --- | --- |
| SP CPU utilization | com.dynatrace.extension.network\_device.sp.cpu\_usage | SP CPU utilization |

Per\_Device\_HTTP\_Statistics\_Virtual

| Metric name | Metric key | Description |
| --- | --- | --- |
| HTTP 2.0 connection count | radware\_alteon.httpstatsumm.http20connection.count | HTTP 2.0 connection count. |
| HTTP 1.1 connection count | radware\_alteon.httpstatsumm.http11connection.count | HTTP 1.1 connection count. |
| HTTP 1.0 connection count | radware\_alteon.httpstatsumm.http10connection.count | HTTP 1.0 connection count. |
| HTTP 2.0 connection peak count | radware\_alteon.httpstatsumm.http20connection.peak.count | HTTP 2.0 connection peak count. |
| HTTP 1.1 connection peak count | radware\_alteon.httpstatsumm.http11connection.peak.count | HTTP 1.1 connection peak count. |
| HTTP 1.0 connection peak count | radware\_alteon.httpstatsumm.http10connection.peak.count | HTTP 1.0 connection peak count. |
| HTTP 2.0 request count | radware\_alteon.httpstatsumm.http20connection.request.count | HTTP 2.0 request count. |
| HTTP 1.1 request count | radware\_alteon.httpstatsumm.http11connection.request.count | HTTP 1.1 request count. |
| HTTP 1.0 request count | radware\_alteon.httpstatsumm.http10connection.request.count | HTTP 1.0 request count. |
| HTTP transactions per second | radware\_alteon.httptranssumm.trans.rate | HTTP transactions per second. |

High\_Availability\_Physical

| Metric name | Metric key | Description |
| --- | --- | --- |
| High availability (HA) service group state | radware\_alteon.ha.group.state | High availability (HA) service group state |
| High availability (HA) switch state | radware\_alteon.ha.switch.state | High availability (HA) switch state |
| High availability (HA) mode | radware\_alteon.ha.curcfg.mode | High availability (HA) mode |

Advanced interfaces

| Metric name | Metric key | Description |
| --- | --- | --- |
| â | com.dynatrace.extension.network\_device.if.lastchange | â |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Monitor your Radware Alteon Network Load Balancers through SNMP.](https://www.dynatrace.com/hub/detail/radware-alteon-load-balancer/)