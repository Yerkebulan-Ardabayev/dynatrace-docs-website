---
title: What's new in Dynatrace Managed version 1.326
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-326
---

# What's new in Dynatrace Managed version 1.326

# What's new in Dynatrace Managed version 1.326

* Release notes
* Updated on Oct 20, 2025
* Rollout start on Oct 27, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.326. It contains:

* [Feature updates](#updates): 2
* [Breaking changes](#breaking): 2
* [Fixes and maintenance](#fixes): 8

## Feature updates

Platform | Davis

### Holiday-aware baseline modification

Public holidays have a significant impact on the usage behavior of services and applications. These deviations also affect the accuracy of the service and application baseline. To minimize the risk of false positive alerts, specific public holidays are systematically excluded from the service baseline and application baseline. Excluded public holidays are: New Year, Easter, Thanksgiving, Black Friday and Christmas.

This setting is enabled by default. To disable the feature, go to **Settings** > **Anomaly Detection** > **Holiday-aware baseline modification**.

Classic licensing

### Track your cluster license usage via API

You can now track the license usage of your host units, Davis data units (DDU), and Digital Experience Monitoring (DEM) units in Dynatrace classic licensing via the [Cluster API v2 – Cluster license](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage "Use the API to get cluster license details and billed usage.").

For Dynatrace Managed in **online mode**:

* `GET api/cluster/v2/clusterLicense` Gets the cluster license and billed usage
* `GET api/cluster/v2/clusterLicense/environment/total` Gets the billed usage per environment, including usage from past contracts
* `POST api/cluster/v2/clusterLicense/key` Changes the license key of the cluster

For Dynatrace Managed in **offline mode**:

* `GET api/cluster/v2/clusterLicense` Gets the cluster license and billed usage
* `POST api/cluster/v2/clusterLicense/upload` Uploads the license key the cluster

## Breaking changes

Application Observability | Services

### Automatic migration of span:services to SDv2

The legacy `span:services` (OTLP API ingested services) will be automatically migrated to the Unified Services type. The new service type automatically enables Davis AI anomaly detection, endpoint detection, and advanced monitoring capabilities. If your environment already migrated from `span:services` to Unified Services in 2023, this change will not affect you.

### Simplified in-product search

The in-product search no longer includes Dynatrace documentation and community content in the search results. Instead, this content has been replaced with a static link to [search.dynatrace.com﻿](https://search.dynatrace.com).

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.326](/managed/whats-new/dynatrace-api/sprint-326 "Changelog for Dynatrace API version 1.326")
* [Dynatrace API changelog version 1.325](/managed/whats-new/dynatrace-api/sprint-325 "Changelog for Dynatrace API version 1.325")

## Fixes and maintenance

Platform

### Cassandra upgrade to version 4.1.10

As part of this release, the Cassandra nodes are upgraded to version 4.1.10 to provide critical bug and security fixes.

No manual user-invention or downtime is necessary, the upgrade should happen via rolling updates as part of normal version updates.

### Resolved issues in this release

* Resolved an issue with referential integrity checks between settings that prevented saving of settings changes if the settings value contained unchanged secrets as well as a reference to another setting. (PS-36658)
* The new Warning event type can be set in the classic event template. (DI-23143)
* Fixed an issue where Problem A got linked to Problem B as a duplicate, but Problem B did not contain the events from Problem A, which happened when Problem B reached the max evidence limit. (DI-23018)
* Fixed an issue introduced in Dynatrace version 1.322, where problem notifications with a textual (text/html/markdown) problem details format show the problem start/end in UTC instead of the timezone configured for the Dynatrace Server. (DI-23006)
* Fixed Session Replay rendering issues related to CSS @import handling (importing other CSS with combination of absolute and relative paths being used by them). (DEM-15898)
* Fixed deployment guidance by providing the appropriate version of the new OneAgent Lambda releases. (MGD-7064)
* Adapted exception handling logic so that the PersistenceUnavailableException is logged as INFO. (DI-22667)

Cluster version (1.326.67.20251107-122142)

* Fixed a bug in monitored entities storage that could lead to empty query results when the number of built in types exceeds 2.5 million during recreation of the monitored entities attribute index. (MGD-8002)

## Operating systems support

* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.0
* Added support for [SUSE Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 15.7

### Future Dynatrace Managed operating systems support changes

##### The following operating systems will no longer be supported starting 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Vendor announcement﻿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Vendor announcement﻿](https://ubuntu.com/about/release-cycle)

##### The following operating systems will no longer be supported starting 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Vendor announcement﻿](https://aws.amazon.com/linux/)

### Past Dynatrace Managed operating systems support changes

##### The following operating systems are no longer supported since 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Vendor announcement﻿](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Vendor announcement﻿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Vendor announcement﻿](https://endoflife.date/rocky-linux)

##### The following operating systems are no longer supported since 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Vendor announcement﻿](https://wiki.debian.org/DebianReleases)

##### The following operating systems are no longer supported since 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Vendor announcement﻿](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Vendor announcement﻿](https://endoflife.date/rocky-linux)

##### The following operating systems are no longer supported since 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Vendor announcement﻿](https://www.suse.com/lifecycle/)