---
title: What's new in Dynatrace Managed 1.342
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-342
---

# What's new in Dynatrace Managed 1.342

# What's new in Dynatrace Managed 1.342

* Release notes
* 5-min read
* Published Jun 18, 2026
* Rollout start on Jul 06, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.342. It contains:

* [Feature updates](#updates): 4
* [Breaking changes](#breaking): 1
* [Fixes and maintenance](#fixes): 8

## Feature updates

Infrastructure Observability | Infrastructure & Operations

### New REST API serving public URIs for Dynatrace images

We have added a new REST API to provide URIs for the images used in Dynatrace components.

Platform

### Rerun metric query with many metric dimension tuples in Data Explorer

In Data Explorer, if the limit of 100,000 dimension tuples is reached for a query, you now have the option to rerun the query with this limit removed.

The rerun option allows fetching of data for all available metric dimensions.

Other query limits, such as the maximum number of fetched data points, still apply.

Platform | Dashboards

### Selectable text in Dashboard markdown tiles

Text in Dashboard markdown tiles can now be selected and copied — making it easier to reuse content from dashboards in other documents and tools.

Software Delivery

### Updated NGINX, OpenSSL, and OpenSSL FIPS

We have updated NGINX to 1.30.x, OpenSSL to 3.5.x, and OpenSSL FIPS to 3.1.x.

## Breaking changes

Application Observability

### OneAgent end-of-life version connection enforcement

Starting with this release, Dynatrace rejects connections from OneAgent versions 1.141 and earlier.

If you’re running OneAgent version 1.141 or earlier, upgrade to a supported OneAgent version to avoid data loss and connectivity issues, and to benefit from enhanced security and features unavailable in earlier OneAgent versions.

For details, see [End-of-life announcements](/managed/whats-new/technology/end-of-life-announcements "Information about technologies, features, or integrations scheduled for end of life (EOL) in Dynatrace, including upcoming and recently retired items.").

## Fixes and maintenance

### Resolved issues in this release

* Resolved an issue where custom metric data became invisible in queries after approximately three hours. This occurred when a custom metric was deleted and then re-created with the same metric key. To resolve the issue for currently affected metrics, restart the server. However, older data can't be recovered. (MGD-12314)
* Fixed a bug on the Oracle Insights **View Statements** page. (MGD-11991)
* Fixed the Maintenance Window filter entity type lookup to avoid matching all entities for unknown entity types. (DI-28768)
* Fixed repeated `WARNING` logs from `DavisGenericEventBuilder` about `smartscape.rootcause_entity` not being part of the `davis.event` Semantic Dictionary model during problem update ingestion. (DI-28569)
* The extensions `/monitoring-configurations` endpoint now accepts only fully-formed semver version properties when creating a new monitoring configuration. (DAQ-24971)

## Operating systems support

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

* [Dynatrace API changelog version 1.341](/managed/whats-new/dynatrace-api/sprint-341 "Changelog for Dynatrace API version 1.341")