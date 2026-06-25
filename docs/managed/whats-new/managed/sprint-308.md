---
title: Dynatrace Managed release notes version 1.308
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-308
scraped: 2026-05-12T11:07:42.627991
---

# Dynatrace Managed release notes version 1.308

# Dynatrace Managed release notes version 1.308

* Release notes
* Published Feb 13, 2025

Rollout start: Feb 17, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.308.

## Across platform

Breaking change ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform | Settings

### Settings audit log changes

We adjusted settings audit log generation to improve readability and reduce spam.

* Updates via API that donât change the value will no longer appear in the audit log. This typically happens if a script writes identical values often, which could result in many log entries without helpful content.

  Despite being a functional improvement, this is technically a breaking change.

* The classic web UI is not affected by this for most existing schemas. If a user persists the existing value again (typically changing a value, changing it back, and saving), `NO_CHANGE` entries might still occur.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Cluster

### Cassandra upgrade to version 4.1

As part of this release, the Cassandra nodes are upgraded to version 4.1.

No manual user-invention or downtime is necessary; the upgrade occurs via rolling updates as part of regular version updates.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability | Hosts

### Stability check for OneAgent Automatic Updates

The defaults for automatic updates / stable check have been reduced to 45 minutes for EC2 and non-EC2 hosts. This change improves the Automatic Updates process if maintenance windows are used.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability | Hosts

### Remote configuration management (RCM): automatic restart for host tags and properties change

OneAgent will be restarted automatically when host tags and properties are changed via RCM.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform

### Upgrade of Jetty to version 10

As part of this release, the included Jetty WebServer functionality is upgraded to version 10.0.24.

No manual user invention or downtime is necessary; the upgrade should happen via rolling updates as part of normal version updates.

In certain high-load scenarios, we have observed a slight increase in CPU and memory usage caused by implementation changes in Jetty 10. If ActiveGate instances are already at their resource limit, we recommend increasing them to avoid possible overload.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Delivery | Cluster

### Updated Dynatrace Managed installer to use Adoptium JRE version 11.0.25 / 17.0.13

The Dynatrace Managed installer has been updated to use Adoptium JRE version 11.0.25 (for Cassandra) and 17.0.13 (all other components).

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform

### Minor changes in network metrics descriptions

Minor improvements were made to network metrics descriptions visible in the web UI.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.307](/managed/whats-new/dynatrace-api/sprint-307 "Changelog for Dynatrace API version 1.307")
* [Dynatrace API changelog version 1.308](/managed/whats-new/dynatrace-api/sprint-308 "Changelog for Dynatrace API version 1.308")

## Operating systems support

### Current Dynatrace Managed operating systems support changes

##### The following operating systems will no longer be supported starting 01 February 2025

* Linux: CentOS Stream 8

  + x86-64
  + [Vendor announcementï»¿](https://www.centos.org/centos-stream/)
  + Last compatible version: 1.308
* Linux: CentOS 7.9

  + x86-64
  + [Vendor announcementï»¿](https://www.centos.org/centos-linux/)
  + Last compatible version: 1.308
* Linux: Red Hat Enterprise Linux 7.9

  + x86-64
  + [Vendor announcementï»¿](https://access.redhat.com/support/policy/updates/errata)
  + Last compatible version: 1.308

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