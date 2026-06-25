---
title: What's new in Dynatrace Managed version 1.330
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-330
scraped: 2026-05-12T11:08:03.789275
---

# What's new in Dynatrace Managed version 1.330

# What's new in Dynatrace Managed version 1.330

* Release notes
* Published Jan 09, 2026
* Rollout start on Jan 19, 2026

New versions are rolled out within configurable [maintenance windows](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.").

|  | Rollout start | Currently supported |
| --- | --- | --- |
| [Version 1.338](/managed/whats-new/managed/sprint-338 "New features, changes, and resolved issues in Dynatrace Managed 1.338") | May 11, 2026 | Yes |
| [Version 1.336](/managed/whats-new/managed/sprint-336 "New features, changes, and resolved issues in Dynatrace Managed 1.336") | Apr 13, 2026 | Yes |
| [Version 1.334](/managed/whats-new/managed/sprint-334 "New features, changes, and resolved issues in Dynatrace Managed 1.334") | Mar 16, 2026 | Yes |
| [Version 1.332](/managed/whats-new/managed/sprint-332 "Release notes for Dynatrace Managed, version 1.332") | Feb 16, 2026 | Only with [Enterprise Success and Supportï»¿](https://dt-url.net/qt03zwg) |

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.330. It contains:

* [Feature updates](#updates): 8
* [Breaking changes](#breaking): 3
* [Fixes and maintenance](#fixes): 5

## Feature updates

Account Management

### Monitor your cluster license usage

We have added a dashboard to your cluster's local self-monitoring environment, which allows you to track the license usage of your host units, Davis data units (DD), and Digital Experience Monitoring (DEM) units under classic licensing.

We have also added specific billing metrics for each license unit, so you can alert on license events (for example, when units are about to run out) using metric events. For details on billing metrics and how to define license events, see [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

![Cluster license usage dashboard](https://dt-cdn.net/images/managed330-cluster-license-usage-2335-1d3ae4be6a.png)

Cluster license usage dashboard

Application Observability | Distributed Tracing

### Set and override OneAgent masking at the host group level

[OneAgent masking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") can mask data at first contact before it leaves a monitored process. To allow you to configure it in multiteam and multidepartment environments, we made it possible to set and override it at the host group level in addition to the already existing environment, Kubernetes cluster/namespace, and process group levels. This is especially convenient when managing hundreds of applications.

Platform

### Intuitive zoom functionality for Data Explorer charts

We have added the ability to zoom in or out directly on charts in the Data Explorer. To zoom in on a chart, select the desired start point, hold down the mouse button, and drag to the desired endpoint. Release the mouse button; a confirmation dialog for the zoom interval should appear.

Once you have zoomed in, you can use the revert button to return to the previous timeframe.

![Zoom functionality on Data Explorer charts](https://dt-cdn.net/images/screenshot-2026-01-16-at-15-20-42-1617-0a636a5632.png)

Zoom functionality on Data Explorer charts

Platform

### Improved accuracy in dimension limit monitoring for metrics

Usage of custom metrics with a steady flow of new dimension values (such as Kubernetes pod UIDs) could display incorrect patterns in self-monitoring, including sudden increases followed by drops.

With this update, dimension limits are now calculated accurately, providing clearer and more reliable insights into your metric usage.

Platform

### Suggestions for entity selectors in Settings

Automatically applied tags, management zones, and SLO definitions now support entity selector suggestions. Instead of manually typing out entity selectors, you can use this auto-complete feature, which suggests available filters, operators, and values.

![entity selector suggestions](https://dt-cdn.net/images/auto-complete-1337-525ba3065b.png)

entity selector suggestions

Platform

### New Metrics API v2 endpoint for deleting outdated metrics

The [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") now includes a new endpoint that allows you to delete metrics that haven't been written in a given number of days. Hereâs what you can do:

* Use `DELETE /api/v2/metrics` to delete ingested metrics.
* Use the `metricSelector` parameter to choose specific metrics.
* Use wildcards to delete metrics with a prefix or all metrics by specifying `*`.
* Use the `minUnusedDays` parameter to define how many days a metric must go unused before itâs deleted.

Example: To delete all metrics not written in the last 60 days:

`DELETE /api/v2/metrics?metricSelector=<your-selector>&minUnusedDays=60`

Platform | OneAgent

### OneAgent version compatibility check

[OneAgent Health](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.") now displays the lowest and highest compatible OneAgent versions with this Managed cluster. Additionally, a warning message is issued if a OneAgent version is too low or too high, allowing you to react and quickly connect a OneAgent with a compatible version.

## Breaking changes

Infrastructure Observability | Extensions

### Event related endpoints have been removed from the Extensions Environment API v2

The following deprecated endpoints have been removed from the Environment API v2:

* `/extensions/{extensionName}/environmentConfiguration/events`
* `/extensions/{extensionName}/monitoringConfigurations/{configurationId}/events`.

Platform

### Replaced in-product live chat with external link

The in-product live chat has been replaced by an external link to the [Dynatrace Support Centerï»¿](https://support.dynatrace.com). In the Dynatrace Support Center, you can contact our product specialists at any time with questions about Dynatrace.

Platform

### Metric fileDescriptorsPercentUsed is no longer split by PID

For performance reasons, the PID dimension was removed from the fileDescriptorsPercentUsed metric. This means the metric can't be split by PID anymore.

Metric key: `builtin:tech.generic.handles.fileDescriptorsPercentUsed`

## Fixes and maintenance

### Resolved issues in this release

* In the case of [classic K8s log monitoring](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes."), the log monitoring modules are not included in the host Units license and are also not billed. However, they were incorrectly included in the host unit quota check, potentially leading to misleading information about quota usage. Therefore, we excluded the log monitoring modules from the host unit quota check (MGD-8983)
* Fixed installer packages that weren't synchronized correctly between nodes if a script file without a semantic version in the filename was present in the Dynatrace Managed server installer folder. (MGD-8354)
* Resolved an issue with application-only deployments when multiple code modules could overwrite each other's OneAgent version on the same host. (MGD-6868)
* Reliable browser monitor auto-login: Fixed a bug in the JavaScript step of the auto-login browser monitor, preventing crashes when the monitor fails, for a smoother monitoring experience. (DEM-18430)
* Consistent handling of whitespace endpoints: Service detection v2 spans now treat endpoints consisting of all whitespace characters the same as empty endpoints, resulting in no `endpoint.name` being assigned. This update ensures consistent span behavior, with no impact on metric generation. (APPOBS-30130)

### Resolved issues (update 1.330.29.20251229-0916101)

* Fixed a problem with the NGINX health check module, which is responsible for redirecting traffic between cluster nodes. (MGD-9000)

## Operating systems support

* Added support for [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.1

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

* [Dynatrace API changelog version 1.330](/managed/whats-new/dynatrace-api/sprint-330 "Changelog for Dynatrace API version 1.330")
* [Dynatrace API changelog version 1.329](/managed/whats-new/dynatrace-api/sprint-329 "Changelog for Dynatrace API version 1.329")