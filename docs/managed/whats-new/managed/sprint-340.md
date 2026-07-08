---
title: What's new in Dynatrace Managed 1.340
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-340
---

# What's new in Dynatrace Managed 1.340

# What's new in Dynatrace Managed 1.340

* Release notes
* 4-min read
* Updated on Jun 10, 2026
* Rollout start on Jun 08, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.340. It contains:

* [Feature updates](#updates): 4
* [Breaking changes](#breaking): 2
* [Fixes and maintenance](#fixes): 6

Infrastructure Observability

## Modernized Network interface page for quicker insights

We’re excited to announce a completely redesigned **Network interface** page, bringing broader visibility, smoother navigation, and a more intuitive monitoring experience to your network performance workflows.

![Network Interface page](https://dt-cdn.net/images/network-interface-2038-ea340ab2a3.png)

Network Interface page

## Feature updates

Infrastructure Observability

### Modernized Disk page for quicker insights

We’re excited to announce a completely redesigned **Disk** page, bringing broader visibility, smoother navigation, and a more intuitive monitoring experience to your infrastructure performance workflows.

Platform

### Configurable log retention and storage per environment

Dynatrace Managed admins can now configure log retention and storage limits per environment directly in the CMC UI under the **Environments** setting. Log retention can be set anywhere from 1 to 90 days (in daily increments), and storage can be capped at a specific GiB value or left unlimited. Previously, log retention was fixed at 35 days with no option to adjust it. Retention changes apply to new log records going forward, with daily cleanup enforcing the configured period.

Platform

### Free-text support for non-entity filters in Data Explorer

The **Filter by** field in ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** now accepts free-text input for non-entity filters. As you type, the free-text option appears with immediate feedback.

Platform | Platform Services

### Elasticsearch upgrade to version 8.19

The Elasticsearch nodes are upgraded to version 8.19 to provide bug and security fixes and leverage performance improvements introduced by this update.  
No manual user intervention or downtime is required; the upgrade occurs via rolling updates as part of normal version updates.

## Breaking changes

Application Observability

### Upcoming OneAgent end of life version enforcement

Starting with Dynatrace Managed version 1.342, the cluster will reject connections from OneAgent versions 1.141 and earlier.

Action might be required:

If you are running OneAgent versions 1.141 or earlier, upgrade to a supported OneAgent version before upgrading to Dynatrace Managed version 1.342 to avoid data loss and connectivity issues, and to benefit from enhanced security and features unavailable in earlier OneAgent versions.

For more details, see [End-of-life announcements](/managed/whats-new/technology/end-of-life-announcements "Information about technologies, features, or integrations scheduled for end of life (EOL) in Dynatrace, including upcoming and recently retired items.").

Infrastructure Observability | Infrastructure & Operations

### Deprecation of ActiveGate auto-update API

The [ActiveGate auto-update configuration API](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.") is deprecated. Instead, use the Settings 2.0 API with the `deployment.activegate.updates` schema ID.

## Fixes and maintenance

### Resolved issues in this release

* Fixed an issue where the **Deep monitoring** / **Process group monitoring** settings that deactivated monitoring were ignored for standalone/application-only and manually injected OneAgents. (PS-42728)
* Fixed an issue where a message was being displayed stating that Python 3.14 is not supported on Linux. Message was incorrect as actual monitoring of the process works starting with OneAgent version 1.329+. (MGD-11388)
* Fixed an issue causing the RUM JavaScript to add headers to cross-origin requests if the `base` tag points to a different origin, which triggered potentially broken preflight requests. (DEM-26180)
* Fixed an issue that resulted in consecutive visit generation if cookies cannot be set. (DEM-25392)
* Fixed the issue where the infographic on the Technology & Processes custom device subpage occasionally failed to render due to missing data not being handled correctly. (DAQ-24380)

## Operating systems support

* Added support for [Ubuntu](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 26.04

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

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.340](/managed/whats-new/dynatrace-api/sprint-340 "Changelog for Dynatrace API version 1.340")