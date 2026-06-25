---
title: Dynatrace Managed release notes version 1.302
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-302
scraped: 2026-05-12T11:07:57.374620
---

# Dynatrace Managed release notes version 1.302

# Dynatrace Managed release notes version 1.302

* Release notes
* Updated on Dec 05, 2024

Rollout start: Oct 14, 2024

## New features and enhancements

### Premium HA multi-datacenter failover

The new Premium High Availability (HA) multi-datacenter failover mechanism automatically detects Elasticsearch or Cassandra node outages. After the nodes are operational again, it automatically triggers a repair on all nodes that were not available during the outage.

For details, see [managed-auto-repair](/managed/managed-cluster/high-availability/auto-repair).

### Improved Cassandra CPU in some deployments

Adjusted Cassandra tuning to resolve high Cassandra CPU issues in some Dynatrace Managed deployments.

### IPv6 support for Network Availability Monitors

Digital Experience | Synthetic

ActiveGate version 1.301+ Dynatrace version 1.302+

NAM has been improved by adding support for IPv6. Now you can use NAM to check network and device availability in IPv6 networks.

### Kubernetes cluster page improved

Infrastructure Observability | Kubernetes

The ActiveGate product version (instead of the build version) is now displayed on the Kubernetes cluster page, to be consistent with the **Deployment status** page.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.302](/managed/whats-new/dynatrace-api/sprint-302 "Changelog for Dynatrace API version 1.302")

## Operating systems support

* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5
* Added support for [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5
* Added support for [Rocky Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5

### Current Dynatrace Managed operating systems support changes

##### The following operating systems will no longer be supported starting 01 November 2024

* Linux: Oracle Linux 9.0, 9.3

  + x86-64
  + [Vendor announcementï»¿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
  + Last compatible version: 1.302
* Linux: Rocky Linux 9.0, 9.3

  + x86-64
  + [Vendor announcementï»¿](https://endoflife.date/rocky-linux)
  + Last compatible version: 1.302

### Future Dynatrace Managed operating systems support changes

##### The following operating systems will no longer be supported starting 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Vendor announcementï»¿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Vendor announcementï»¿](https://endoflife.date/rocky-linux)

##### The following operating systems will no longer be supported starting 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Vendor announcementï»¿](https://www.suse.com/lifecycle/)

##### The following operating systems will no longer be supported starting 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Vendor announcementï»¿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Vendor announcementï»¿](https://ubuntu.com/about/release-cycle)

##### The following operating systems will no longer be supported starting 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Vendor announcementï»¿](https://aws.amazon.com/linux/)

### Past Dynatrace Managed operating systems support changes

##### The following operating systems are no longer supported since 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Vendor announcementï»¿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Vendor announcementï»¿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Vendor announcementï»¿](https://endoflife.date/rocky-linux)

##### The following operating systems are no longer supported since 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Vendor announcementï»¿](https://wiki.debian.org/DebianReleases)

## Resolved issues

* [General Availability (Build version\_1.302.76)](#managed-sprint-302-ga)
* [Update 102 (Build 1.302.102)](#managed-sprint-302-102)

### General Availability (Build version\_1.302.76)

The version\_1.302 GA release contains 12 resolved issues.

| Component | Resolved issues |
| --- | --- |
| [Cluster](#managed-sprint-302-ga-Cluster) | 10 |
| [Session Replay](#managed-sprint-302-ga-Session Replay) | 2 |

#### Cluster

* Aggregation conversion to MDA has been improved for built-in and calculated service metrics. (TI-14032)
* Permissions checks for service extraction is fixed. (TI-14133)
* Fixed authentication inconsistencies for workflow event triggers when triggering with events other than bizevents. Check your workflow actor's permissions if you experience different trigger behavior. (PPX-2982)
* The Process Agent executables blocklist for Windows has been extended with: `"SEARCHINDEXER.EXE", "LSM.EXE", "WINLOGO.EXE", "SPOOLSV.EXE", "TASKHOST.EXE", "SPPSVC.EXE", "SEARCHFILTERHOST.EXE", "MMC.EXE", "MQSVC.EXE", "WMIPRVSE.EXE", "WININIT.EXE", "SERVICES.EXE", "EXPLORER.EXE", "SEARCHPROTOCOLHOST.EXE", "POWERSHELL.EXE", "SDIAGNHOST.EXE", "TASKHOSTW.EXE", "SIHOST.EXE", "TASKMGR.EXE"`. (OA-35354)
* Fixed an issue where an IAM policy denying write access to schema group `group:privacy-settings` prevented the creation of RUM mobile apps. (RUM-21513)
* The throughput chart for calling/called services is fixed on the service overview page. (TI-14156)
* Scrolling sensitivity in the single trace view of distributed traces has been improved. (TI-13794)
* A client IP hint is no longer shown if no client IP is available. (TI-13978)
* On Davis events in Grail triggered by service anomaly detection, `endpoint.name` is now written as an array. (DI-16285)
* Fixed missing VictorOps configuration in offline clusters. (CLD-12248)

#### Session Replay

* Added a minimum height for the player container to avoid sessions being rendered too small. (SR-5941)
* Some long split sessions were taking too long to load, so to improve the load time, we are skipping the operations that can be skipped until the time to start the replay. (SR-6017)

### Update 102 (Build 1.302.102)

This cumulative update contains 1 resolved issue and all previously released updates for the 1.302 release.

|
|  |
|
|  |

#### Cluster

* Resolved an issue caused by new default settings in Firewalld in Red Hat Enterprise Linux 9.5 that blocked Dynatrace firewall rules. (MGD-1220)