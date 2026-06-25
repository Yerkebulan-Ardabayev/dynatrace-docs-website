---
title: What's new in Dynatrace Managed 1.336
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-336
scraped: 2026-05-12T11:07:46.857126
---

# What's new in Dynatrace Managed 1.336

# What's new in Dynatrace Managed 1.336

* Release notes
* 2-min read
* Updated on Apr 13, 2026
* Rollout start on Apr 13, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.336. It contains:

* [Feature updates](#updates): 2
* [Fixes and maintenance](#fixes): 7

Platform | Settings

## Improved preview function for tagging and management zone rules

When creating tagging or management rules, it's important to review the affected monitored entities and, if there are many, filter them efficiently. We have now implemented an improved preview function in the settings, with filter options for entity name, type, and first and last seen dates.

This improved preview function is available for the following settings:

* **Tags** > **Automatically applied tags**
* **Preferences** > **Management zones**
* **Cloud Automation** > **SLO definition**

![Preview of automatically applied tags](https://dt-cdn.net/images/screenshot-2026-03-09-at-11-13-34-1760-d57c739bb9.png)

Preview of automatically applied tags

## Feature updates

Platform

### Updated Dynatrace Managed installer to use Adoptium Java version 11.0.30 / 17.0.18 / 21.0.10

The Dynatrace Managed installer has been updated to use Adoptium Java versions 11.0.30 (for Cassandra), 17.0.18 (for ActiveGate), and 21.0.10 (for all other components). No manual user intervention or downtime is required; the upgrade occurs via rolling updates as part of normal version updates.

Platform

### Progress indicator for the installation package upload

The installation packages can be quite large, so uploading them manually to the **Cluster Management Console** via the **Automatic updates** settings page may take some time. A progress indicator now displays the remaining time so that you're always informed of the current status.

## Fixes and maintenance

### Resolved issues in this release

* Improved container instrumentation rules to prevent accidental instrumentation of OpenShift 4.14+ platform components. This improves performance and reduces overhead. (OA-61720)
* Fixed an issue where multiple threads could trigger redundant reconnections to the data store after a connection reset, potentially causing unnecessary load and instability (MGD-11060)
* On the **Process group** page, the JVM metric **Garbage collection time** is now correctly displayed as a sum and not as an average. However, this change may affect the existing metric baseline. (MGD-10582)
* Improved how Data Explorer handles bad requests to provide more useful feedback when queries return a result set thatâs too large or when a user executes too many requests. (MGD-9727)
* Added `dynatrace.com/split-mounts` annotation to the synthetic pod template. This annotation was introduced in Dynatrace Operator 1.8.0 to avoid conflicts with application images that already contain a `/var/lib/dynatrace` directory, enabling correct injection into ActiveGate pods. Adding this annotation to synthetic deployments aligns the synthetic pod template with the Operator's default behavior for ActiveGate-managed pods. (DEM-22172)
* Fixed a behavior where page resizes were not accounted for when replaying RUM sessions via Session Replay (moving the renderer back in time). (DEM-21951)
* Fixed an issue where the `dt.source_entity` and `loglevel` attributes were being overwritten by Azure log processing rules. These attributes now retain their original values if set by the source. (APPOBS-33744)

## Operating systems support

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

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.336](/managed/whats-new/dynatrace-api/sprint-336 "Changelog for Dynatrace API version 1.336")
* [Dynatrace API changelog version 1.335](/managed/whats-new/dynatrace-api/sprint-335 "Changelog for Dynatrace API version 1.335")