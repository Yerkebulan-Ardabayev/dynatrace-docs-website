---
title: What's new in Dynatrace Managed 1.334
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-334
scraped: 2026-05-12T11:07:40.093176
---

# What's new in Dynatrace Managed 1.334

# What's new in Dynatrace Managed 1.334

* Release notes
* 4-min read
* Updated on Mar 09, 2026
* Rollout start on Mar 16, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.334. It contains:

* [Feature updates](#updates): 6
* [Breaking changes](#breaking): 1
* [Fixes and maintenance](#fixes): 1

Platform | Dashboards

### Intuitive zoom functionality for Dashboard charts

We have added the ability to zoom in or zoom out directly on charts. To zoom in on a chart:

1. Select the desired start point.
2. Extend the range to the desired end point.

   When you release, a confirmation dialog displaying the zoom interval appears.
3. Select **Zoom in**.

You can revert the action and return to the previous timeframe.

![Dashboard zoom function](https://dt-cdn.net/images/dashboard-1616-9e090c3172.png)

Dashboard zoom function

## Feature updates

Platform

### Unified syntax highlighting for expressions

The syntax highlighting of expressions (in **Data explorer**, **Entity selector**, and **Metric selector**) has now been unified to ensure a consistent appearance and improve readability.

![Entity selector](https://dt-cdn.net/images/screenshot-2026-02-12-at-14-56-21-1932-d5730ef8f4.png)

Entity selector

Application Observability | Log Analytics

### Updated replacement strings for built-in masking rules

We introduced new replacement strings for built-in masking rules. The matching patterns are unchanged. To avoid backward compatibility problems, the previous rules are kept and renamed with `[Outdated-Built-in]` prefix. You can modify or delete the previous rules at any time.

Application Security | Vulnerabilities

### Library and Kubernetes vulnerability scanning now uses the Dynatrace Vulnerability feed

Library and Kubernetes vulnerability scanning now relies on the Dynatrace Vulnerability feed. This update delivers more accurate, transparent, and threatâaware vulnerability data while preserving strong coverage of critical risks. As part of this change, a small percentage of previously detected vulnerabilities will no longer be covered and will be marked as **Deprecated**. You can review them using the **Status** > **Deprecated** filter. For more information, see [Introducing the Dynatrace Vulnerability feed: Accurate, transparent, and threat-aware.ï»¿](https://www.dynatrace.com/news/blog/introducing-the-dynatrace-vulnerability-feed-accurate-transparent-and-threat-aware/).

Digital Experience | Synthetic

### Changed permissions in the Kubernetes template for the Synthetic Monitoring metric adapter

The Kubernetes template for the Synthetic Monitoring metric adapter has been updated to set the Cluster Role metric permissions to read-only.

Platform

### Kubernetes Workload and Pods pages display now all events

The **Kubernetes Workload** and **Pods** pages now display all events that are related to a specific workload or pod in their **Events** card.

![Events card](https://dt-cdn.net/images/events-card-1742-00eb8751d1.png)

Events card

Platform

### Configure network zones via Settings API

You can configure your network zones via the Settings API framework with the new schema `builtin:networkzones.zones`. Use the following endpoints to access the parameters

* Environment level: `GET /api/v2/settings/schemas/builtin:networkzones.zones`
* Cluster level: `GET /api/cluster/v2/settings/schemas/builtin:networkzones.zones`

For more information, see [Settings API](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework").

Note that the existing [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.") remains unchanged and continues to work alongside the new Settings API capabilities.

## Breaking changes

Account Management | Cost Management

### Switch to the new Account Management notifications endpoint

To receive a unified feed of available notifications (budget, forecast, and cost), switch to the new `NotificationsController_listNotifications` notifications endpoint. The new endpoint may return additional notification types and minor schema metadata differences.

The `SubscriptionsController_getEvents` is deprecated starting with Dynatrace version 1.333. It will continue to work until the announced sunset date, but it will not return the additional notification types available via the new endpoint.

Timing:

* Release of new `NotificationsController_listNotifications` endpoint: Dynatrace version 1.333
* Deprecation headers are planned to go live on February 23, 2026. Responses will include `deprecation: true` and `sunset: 2026-04-06`.
* Sunset date of `SubscriptionsController_getEvents` endpoint: April 6, 2026.

Links:

* Old API doc: [Dynatrace Platform Subscription API - GET events â Dynatrace Docs](/managed/dynatrace-api/account-management-api/post-notifications "List notifications for your account.")
* New API doc: [Dynatrace Platform Subscription API - POST notifications](/managed/dynatrace-api/account-management-api/post-notifications "List notifications for your account.")

## Fixes and maintenance

### Resolved issues in this release

* Fixed an edge case where an event start (start of analysis window) is not contained within a maintenance window schedule, but the analysis window end is contained within a maintenance window schedule. This mainly affected anomaly detection events (at the service- or app-level), but also custom anomaly detectors (metric events). (DI-25641)

## Operating systems support

* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.7

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

* [Dynatrace API changelog version 1.334](/managed/whats-new/dynatrace-api/sprint-334 "Changelog for Dynatrace API version 1.334")
* [Dynatrace API changelog version 1.333](/managed/whats-new/dynatrace-api/sprint-333 "Changelog for Dynatrace API version 1.333")