---
title: What's new in Dynatrace Managed 1.348
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-348
---

# What's new in Dynatrace Managed 1.348

# What's new in Dynatrace Managed 1.348

* Release notes
* 7-min read
* Published Sep 23, 2026
* Rollout start on Sep 28, 2026 (planned)

Pre-release information

This is an ongoing summary of changes in this planned release. Check back here at GA for the final version.

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.348. It contains:

* [Feature updates](#updates): 10
* [Breaking changes](#breaking): 3
* [Fixes and maintenance](#fixes): 12

## Feature updates

Account Management | Cost Management

### Billing report no longer shows the current day in the booked-costs chart

The **Billing report** no longer displays the current day in the **Booked costs to date** chart. Previously, today's cumulative cost appeared identical to yesterday's because no costs had been booked yet for the current day, which could suggest that monitoring had stopped. The chart now ends at the previous day, showing only complete, accurate data.

Account Management | Subscriptions and Licensing

### CSV Download for DPS prior 2023

For customers who have a Dynatrace Platform Subscription (DPS) license signed prior to April, 2023, you can now export your consumption history CSV directly in **Account Management**. Go to **History**, find the subscription labeled **DPS** (not **DPS: Regular**), select **Details**, and request your usage report. You'll receive a download link by email.

The export covers the full duration of your consumption for DPS licenses prior to 2023, with daily consumption data per SKU and environment, giving you a reliable record for auditing, reporting, and contractual purposes.

Digital Experience | Synthetic

### Optimized presentation of Synthetic test executions

Querying Synthetic test executions is now optimized by excluding locations that are no longer monitored, and reducing the default time range for queries. This provides quicker responses to certain queries on Synthetic tests and eases the load from availability checks for alerting.

Infrastructure Observability | Kubernetes

### New default triggering values for Kubernetes ready-made alerts

Kubernetes ready-made alerts now have updated default values for triggering updates. Only new deployments use these new defaults, while existing deployments retain their current settings.

Platform

### Sign in with a modern, accessible experience

You can now sign in to Dynatrace Managed through refreshed authentication pages—the login, forgot password, session expired, and welcome pages—that follow the current Dynatrace design language and improve accessibility and usability. Your existing sign-in methods and authentication workflow remain unchanged.

Platform

### Identify your Dynatrace Managed license files by name

If you run Dynatrace Managed in offline mode, the license files you receive from Dynatrace are now named after the license they contain, such as `license-<license-name>.lic`. When you keep license files for several Managed Clusters on the same disk, you can see which license each file holds and assign it to the correct Managed Cluster.

Previously, every license file was named `license.lic`. Licenses issued before this change retain that filename, as do licenses with no defined name.

Platform

### Extend retention for RUM user sessions and Session Replay up to 90 days

You can now configure retention periods of up to 90 days for RUM user sessions and Session Replay directly in **Cluster Management Console** > **Environments**. Longer retention gives you access to a broader history of user behavior and session recordings, which helps with troubleshooting and experience optimization.

Default retention periods remain unchanged. Cluster Management Console (CMC) enforces that user sessions are retained at least as long as Session Replay recordings. Retention changes apply to new records going forward and do not affect existing data.

You can also manage these settings via the Cluster API v2 environments endpoints (`api/cluster/v2/environments`).

Depending on the number of nodes in the Dynatrace Managed installation and the use of longer log retention periods, the retention period may only be extended for a limited number of environments. The CMC UI will indicate whether the retention period can be extended for a specific environment.

Platform

### Scale out your Managed Cluster to more nodes

You can now scale out your Managed Cluster to 42 nodes (21 nodes per data center with Premium High Availability), so you can monitor more hosts, services, and applications as your monitoring footprint grows.

Previously, a Managed Cluster was limited to 30 nodes (15 nodes per data center with Premium High Availability). Existing Managed Clusters receive the higher limits automatically after you upgrade.

Software Delivery

### ActiveGate modules are now protected from exclusion in CMC

When an ActiveGate target version is configured, the corresponding Synthetic and OneAgent installation packages can no longer be manually excluded in CMC Batch Management. The matching module version is automatically selected as the highest compatible revision for the configured ActiveGate target version. This safeguard helps prevent installation failures that occur when required modules are excluded for new ActiveGate deployments.

Software Delivery

### Standard NGINX instrumentation in your Dynatrace Managed cluster

The Dynatrace Managed Cluster NGINX update from 1.28.X to 1.30.X required enabling "runtime instrumentation" for self monitoring One Agents. With Dynatrace Managed version 1.348 we have reverted this to the standard NGINX instrumentation.

## Breaking changes

Application Observability

### OneAgent end-of-life version connection enforcement

Starting with this release, Dynatrace rejects connections from OneAgent versions 1.241 and earlier.

**Action plan:** If you’re running OneAgent versions 1.241 or earlier, upgrade to a supported OneAgent version to avoid data loss and connectivity issues, and to benefit from enhanced security and features unavailable in earlier OneAgent versions.

For details, see [End-of-life announcements](/managed/whats-new/technology/end-of-life-announcements "Information about technologies, features, or integrations scheduled for end of life (EOL) in Dynatrace, including upcoming and recently retired items.").

Application Observability

### URL path pattern matching conditions now consider calculated `http.route` values

URL path pattern matching conditions now also consider calculated `HTTP.route` values, correcting a previous inconsistency where these values were ignored.  
Because the matching behavior changes, rules that relied on the previous behavior might match differently.

**Action plan:** Review your URL path pattern conditions and confirm they still match as intended now that calculated `HTTP.route` values are included.

Platform

### Monitor your Managed Cluster with the built-in self-monitoring dashboard

Starting with Dynatrace Managed version 1.348, a preset dashboard for Managed Cluster self-monitoring is built into your local self-monitoring environment. This dashboard replaces the [Dynatrace Self-Monitoring (Managed)﻿](https://www.dynatrace.com/hub/detail/dynatrace-self-monitoring-managed/) extension, which is now end-of-life, and includes updated performance indicators that reflect current Managed Cluster scalability.

The **Dynatrace Self-Monitoring (Managed)** extension will be removed from ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") **Hub** in an upcoming release. If you have this extension installed, disable it before it is removed.

**Action plan:** Disable the Dynatrace Self-Monitoring (Managed) extension in your local self-monitoring environment.

## Fixes and maintenance

### Resolved issues in this release

* Fixed vulnerability feed downloads for Dynatrace Managed Clusters without an Application Security license entitlement. (SIA-26144)
* Fixed an issue where a mission control cluster event incorrectly reported a Snyk vulnerability feed download failure when only the DTV app feed download had actually failed. Managed no longer downloads the Snyk feed, and DTV app feed failures are now reported correctly. (SIA-26130)
* Fixed an error that could occur when rendering charts on the Browser Monitoring and Synthetic pages. (PRISM-14616)
* Fixed two issues on Dynatrace Classic dashboards supporting remote environments. Management zones for cluster-local tenants are now resolved in-process instead of calling the disabled loopback HTTP port, and global and default dashboard aliases are now replaced with the resolved dashboard UUID before requesting remote tile data, preventing the initial 403 response. (PRISM-14154)
* Fixed an issue where Dashboards Classic dynamic filters did not suggest custom dimension names for ordinary metric string dimensions (like `thread_pool_name` in the original finding), returning an empty suggestion list. Now the suggestion list is correctly resolved for the given metric's custom dimension. (PRISM-13961)
* Fixed an unhandled error on Dashboards Classic when a remote-link tile configuration could not be parsed; the tile now shows the setup error message instead of failing silently. Added a null guard after deserialization in `generateUrlAndOpenDexpRemoteLink` method. If the config can't be parsed, fire `TileSetupErrorEvent` with the existing clipboard error message and return early. (PRISM-13086)
* Fixed a missing limit on the number of directories scanned when a wildcard pattern is used in a log path configuration (`maxDirsMatchingLogPattern`). Without this limit, an overly broad pattern could cause excessive resource consumption on the host. The limit is now enforced. (OA-71411)
* Fixed platform problem closing for classic problem IDs: the Grail snapshot lookup now uses the FDI2-normalized form of the ID; IDs without a start timestamp are discarded rather than emitting an unverifiable close. (DI-31295)
* Fixed a rendering bug where the visual viewport was positioned incorrectly during replay when the recorded session contained zoom or pan interactions. The replayed content would appear at the wrong offset due to the translation and page scroll not being correctly coordinated. (DEM-32904)
* Fixed a bug that caused Synthetic private node creation to fail for Alibaba Cloud environments. Nodes can now be created and configured for Alibaba Cloud without errors. (DEM-29065)
* Fixed an issue in hybrid mobile sessions with WebView correlation enabled where JavaScript errors were not recognized correctly. The Analyze JavaScript errors option is now available for WebView JavaScript errors, restoring access to detailed error analysis, including stack traces and source maps. (DEM-28346)
* Fixed an issue where a malfunctioning primary tags selection was shown when creating or modifying the monitoring configuration of a JMX or PMI-based extension. The selection is now hidden. (DAQ-28744)

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

* [Dynatrace API changelog version 1.348](/managed/whats-new/dynatrace-api/sprint-348 "Changelog for Dynatrace API version 1.348")
* [Dynatrace API changelog version 1.347](/managed/whats-new/dynatrace-api/sprint-347 "Changelog for Dynatrace API version 1.347")