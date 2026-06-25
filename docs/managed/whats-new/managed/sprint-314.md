---
title: Dynatrace Managed release notes version 1.314
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-314
scraped: 2026-05-12T11:08:02.406747
---

# Dynatrace Managed release notes version 1.314

# Dynatrace Managed release notes version 1.314

* Release notes
* Updated on Jul 28, 2025

Rollout start: May 12, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.314.

## New features and enhancements

Dynatrace Cluster

### Ensure compliance with Software Bill of Materials (SBOM) for Dynatrace Managed

You can ensure compliance with your regulations by scanning the Dynatrace Managed SBOM for vulnerabilities.

The SBOM contains all third-party libraries used by Dynatrace Managed and their versions.

* A new SBOM is provided with each version. It is part of the Managed installer and conforms to the CycloneDX standard.
* The SBOM filename is:

  `/opt/dynatrace-managed/installer/dynatrace-managed-<version>/dynatrace-managed-sbom.cdx.json`

Dynatrace Cluster

### Disk usage reduction by switching compression algorithm for timeseries data

As part of this release, the used compression format of timeseries data in Cassandra will be switched from LZ4 to ZSTD. According to load-testing, this can reduce required disk space considerably.

Note: reduction in disk usage will not be instant, but rather will happen gradually over the course of one month, as only new data will be written with the new compression algorithm.

No manual user invention or downtime is necessary. The switch happens automatically as part of normal version updates.

Dynatrace Cluster

### Faster assignment of tags, management zones, and naming rules

A new periodic worker applies tags, management zones, and naming rules to recently created monitored entities faster. This worker runs continuously and considers all monitored entities created in the last 30 minutes and seen in the last 2 hours.

It is automatically enabled by default for all Dynatrace Managed environments. No additional configuration is required.

Dynatrace Cluster

### JDK upgrade to version 21 for Dynatrace Cluster

As part of this release, Dynatrace Cluster Server nodes will be upgraded to run with JDK 21 instead of JDK 17.

No manual user-invention or downtime is necessary. The upgrade should happen via rolling updates as part of normal version updates.

Internal testing showed a considerable reduction of time spent for Java garbage collection, so the update can lead to improved performance of the Dynatrace Cluster Server process.

Digital Experience | Synthetic

### Reporting of invalid certificates enabled by default for newly created HTTP monitors

The default value for the `Accept any SSL certificate` property of the HTTP monitor request was changed to `false`, so the SSL certificate will be validated for newly created monitors.

Application Observability

### Improved management of calculated service metrics

Managing and browsing your calculated service metrics is now easier and more efficientâespecially for environments with many metrics. Hereâs whatâs new in the Calculated service metrics settings:

* **Filter by status**: Quickly identify calculated service metrics that are enabled or disabled.
* **Sort effortlessly**: Sort your metrics based on their status or Grail enablement.
* **Browse everything**: Pagination now allows you to view all calculated service metrics without limitations.

These improvements save you time, provide better visibility into your calculated service metrics, and make managing them a streamlined experience.

Platform | Davis

### Change in delay for root cause analysis

Events that don't trigger a full root cause analysis will no longer wait 3 minutes before notifying. The main cases for this are custom triggered events, such as an `AVAILABILITY_EVENT` via the REST API.

In addition, the `dt.davis.analysis_trigger_delay` is now preferred over the internally defined three-minute default for some availability-type events. If `dt.davis.analysis_trigger_delay` is set, it is the only delay considered for root cause analysis.

Digital Experience

### Browserless private Synthetic locations reduce hardware requirements to execute NAM and HTTP synthetic monitors

In general, we recommend the deployment of complete synthetic private locations to support the execution of all types synthetic monitors (HTTP, browser, NAM).

If you don't need to run browser monitors, consider deploying your location in browserless mode. This mode deploys the location (or ActiveGate belonging to it) without a browser, reducing hardware requirements. However, browser monitors can't run on a browserless location.

Consider browserless locations as an alternative to standard synthetic private locations when youâre focused purely on:

* Network and infrastructure use cases (using NAM monitors)
* API monitoring (using HTTP monitors)

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.313](/managed/whats-new/dynatrace-api/sprint-313 "Changelog for Dynatrace API version 1.313")
* [Dynatrace API changelog version 1.314](/managed/whats-new/dynatrace-api/sprint-314 "Changelog for Dynatrace API version 1.314")

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

## Resolved issues