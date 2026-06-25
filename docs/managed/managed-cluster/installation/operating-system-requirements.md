---
title: Operating system requirements
source: https://docs.dynatrace.com/managed/managed-cluster/installation/operating-system-requirements
scraped: 2026-05-12T11:25:10.427673
---

# Operating system requirements

# Operating system requirements

* Reference
* 2-min read
* Updated on May 08, 2026

Review the operating system requirements before installing Dynatrace Managed.

* Dynatrace Managed requires a **dedicated host**. The host must not run other services that are central processing unit (CPU)- or memory-intensive, or that use [ports required by Dynatrace Managed](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.").
* Dynatrace Managed runs on a **64-bit Linux distribution** (see supported distributions below). It supports installation on physical and virtualized hosts but not in containers.
* Dynatrace Managed requires a fixed IPv4 address. It supports only IPv4 address spaces.
* Configure your [firewall settings](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.") before installation.
* The libraries installed with Dynatrace Managed are locale-aware. Set the system locale to an English option, for example `LANG=en_US.UTF-8`, to ensure correct display of text and symbols.

## Supported operating systems

| Linux distribution | Versions | CPU architectures |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | x86-64 |
| Debian | 11, 12 | x86-64 |
| Oracle Linux | 8.8, 8.10, 9.2, 9.4, 9.6, 10.1[1](#fn-linux-distribution-1-def) | x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 10.0[1](#fn-linux-distribution-1-def) | x86-64 |
| Rocky Linux | 9.2, 9.4, 9.6, 10.0[1](#fn-linux-distribution-1-def) | x86-64 |
| SUSE Enterprise Linux | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |

1

Dynatrace Managed requires manual installation of the 'libcrypt.so.1' library from the 'libxcrypt-compat.rpm' package, which is not installed by default.

## Support changes

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