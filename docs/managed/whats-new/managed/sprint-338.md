---
title: What's new in Dynatrace Managed 1.338
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-338
scraped: 2026-05-12T11:07:48.166241
---

# What's new in Dynatrace Managed 1.338

# What's new in Dynatrace Managed 1.338

* Release notes
* 3-min read
* Published Apr 21, 2026
* Rollout start on May 11, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.338. It contains:

* [Feature updates](#updates): 4
* [Breaking changes](#breaking): 1
* [Fixes and maintenance](#fixes): 10 (1 vulnerability)

Platform | Dashboards

## New chart type for histogram metrics

Dynatrace Managed now supports a dedicated histogram chart in **Data Explorer** and **Dashboards** for visualizing histogram metrics.

With this new chart type, you can:

* Explore the distribution of metric values, such as response times or request sizes.
* Identify value distributions, percentiles, and outliers at a glance.

This enhancement improves observability into the shape and spread of your data, complementing existing chart types such as line and bar charts.

![Histogram chart in Dashboards](https://dt-cdn.net/images/dashboard-1260-3a410212b9.png)

Histogram chart in Dashboards

![Histogram chart in Data Explorer](https://dt-cdn.net/images/data-explorer-1590-1be3bb1b48.png)

Histogram chart in Data Explorer

## Feature updates

Platform

### Cassandra upgrade to version 4.1.11

As part of this release, the Cassandra nodes are upgraded to version 4.1.11 to provide critical bug and security fixes.

No manual user intervention or downtime is required; the upgrade occurs via rolling updates as part of normal version updates.

Platform

### Convert offline Dynatrace Managed clusters to online

You can now convert an existing offline Dynatrace Managed cluster to an online cluster without redeployment. Previously, you had to choose the connectivity mode during deployment and could not change it afterward. A conversion script is now shipped with Dynatrace Managed that allows administrators to change this connectivity mode.

For more details, see [Convert Dynatrace Managed cluster from offline to online](/managed/managed-cluster/installation/cluster-offline-to-online "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.").

Platform

### Monitored entity ID now displayed in web UI

In the Dynatrace web UI (for example, on the host, container, or service details page), select **Properties and tags** to find the monitored entity ID as the first property. This monitored entity ID is helpful when querying a specific monitored entity using the entity selector.

![Monitored entity ID in properties section](https://dt-cdn.net/images/properties-1722-c53cb871d1.png)

Monitored entity ID in properties section

Platform | Settings

### Certain Configuration API endpoints are now deprecated

Many [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.") endpoints are now covered by the [Settings endpoints](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") in the Environment API v2. Affected Configuration API endpoints now have deprecation notices.

* No immediate action is required on your part.
* Affected endpoints remain fully active.
* While we haven't set a sunset date, these endpoints may be removed in a future release.

We recommend migrating to the Environment API v2 endpoints for a more robust integration. Review the Configuration API reference to identify affected endpoints and plan your migration to Environment API v2.

## Breaking changes

Digital Experience | Synthetic

### Configuration parameter removed from new browser monitor experience schema and API

We removed the `performanceMetric` parameter from the `builtin:synthetic.browser.enablement` schema and from `EnablementDto` on the Synthetic Monitors [Environment API v2](/managed/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API."). This parameter defined which metric was used to display performance charts in the Dynatrace web UI and check performance threshold violations.

Performance alerts continue to use the `dt.synthetic.browser(.step).duration` metric with no changes in functionality.

## Fixes and maintenance

### Resolved issues in this release

* **Vulnerability**: Upgraded the Jetty third-party library to version 12.0.33 to provide critical bug and security fixes. No manual user intervention or downtime is required; the upgrade occurs via rolling updates as part of normal version updates. (MGD-10719)
* Fixed an issue where the **GET account audits** endpoint of the Account Management API would return a `500` error instead of a `504` error in case of a timeout. (LIMA-43865)
* ServiceNow notifications that fail with the `429 Too Many Requests` HTTP error code are now retried up to two times in 15-minute intervals. This reduces the likelihood of problems remaining open in ServiceNow when ServiceNow can't initially process notifications. (DI-27261)
* Fixed an issue that caused local synthetic playback to show errors on pages instrumented with a RUM JavaScript version earlier than 1.337. (DEM-25634)
* Improved the target URL detection for nested load actions. (DEM-24346)
* Fixed an incorrect ActiveGate image reference in the generated `synthetic.yaml` template for OpenShift, which was pointing to a nonexistent image (`dynatrace/activegate:<version>`) instead of the correct one (`dynatrace/dynatrace-activegate:<version>`). (DEM-24277)
* Fixed an issue in **Mobile** > **Web request error details** where filtering by `appVersion` would return `HTTP 400` errors. (DEM-23630)
* Fixed an issue where page resizes were not accounted for when replaying RUM sessions via Session Replay (moving the renderer back in time). (DEM-21951)
* Fixed formatting of the ActiveGate ID in data produced by Dynatrace extensions. (DAQ-23179)
* Fixed filtering of the **Data Forwarding** section in the **OpenPipeline usage overview** dashboard by the **Configuration** dashboard variable. (PPX-10704)

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

* [Dynatrace API changelog version 1.338](/managed/whats-new/dynatrace-api/sprint-338 "Changelog for Dynatrace API version 1.338")
* [Dynatrace API changelog version 1.337](/managed/whats-new/dynatrace-api/sprint-337 "Changelog for Dynatrace API version 1.337")