---
title: Dynatrace Managed release notes version 1.312
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-312
---

# Dynatrace Managed release notes version 1.312

# Dynatrace Managed release notes version 1.312

* Release notes
* Updated on Apr 24, 2025

Rollout start: Apr 14, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.312.

## New features and enhancements

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability | Log monitoring

### Updated log ingestion limits

* Log analytics: Enhanced log ingestion characteristics with improved support for log records containing large payload sizes.
* All log settings: Updated log ingestion limits to reflect new thresholds and capabilities.

See [Log Monitoring default limits (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.") for detailed information.

Digital Experience | RUM Web

### Assess website's overall responsiveness with Interaction to Next Paint

Interaction to Next Paint (INP) has replaced First Input Delay (FID) in Google’s Core Web Vitals. Dynatrace now offers the ability to monitor and analyze INP for your monitored websites. While FID was used to measure the responsiveness of the initial interaction on a website, INP allows to assess the latency across interactions on a website during a visit.

You can put our [INP metric](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#web-applications "Explore the complete list of built-in Dynatrace metrics.") (`builtin:apps.web.interactionToNextPaint`) on dashboards across various dimensions, such as frontend applications, browsers, and locations.

Additionally, you can assess INP values via the **Frontend** page and other analysis pages and filter for websites with the worst INP values to initiate improvements.

![Frontend application overview including Interaction to Next Paint](https://dt-cdn.net/images/screenshot-2025-04-07-at-14-44-27-1733-c8a57e770e.png)

Frontend application overview including Interaction to Next Paint

Application Security | Vulnerabilities

### Go support for Runtime Vulnerability Analytics and Runtime Application Protection

Go technology is now available for Runtime Vulnerability Analytics (code-level vulnerability detection) and Runtime Application Protection (attack protection).

* To enable Runtime Vulnerability Analytics monitoring for Go code-level vulnerabilities

  1. [Configure the code-level vulnerability detection control for Go](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
  2. [Enable OneAgent monitoring for Go](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* To enable Runtime Application Protection monitoring for attacks in Go technology

  1. [Configure the attack control for Go](/managed/secure/application-security/application-protection#config "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
  2. [Enable OneAgent monitoring for Go](/managed/secure/application-security/application-protection#enable-oneagent-feature "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

Action required

With this release, preview customers for Go technology need to upgrade to OneAgent version 1.311 to reactivate this functionality. After that, no further configuration is necessary.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Logs

### Log ingestion warnings update

With this release, EEC, Log Analysis, and ActiveGate will start setting the `attr_key_trimmed` value in the `dt.ingest.warnings` attribute of log events having at least one attribute key exceeding the limit of `100` bytes in UTF-8 representation. This is documented in:

* [Log ingestion warnings (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings "List of log ingestion warnings")

Digital Experience | RUM Web

### Subresource integrity for the RUM monitoring code

You can now leverage the subresource integrity browser feature to ensure the integrity of the RUM monitoring code that is automatically injected or manually inserted into your web application.

For more information, see [Use Subresource Integrity (SRI) for Real User Monitoring Classic code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring Classic code.").

Digital Experience | Synthetic

### Additional Kerberos authentication support for browser monitors

Negotiate (Kerberos) is now supported for browser monitors executed in private locations with:

* Cluster version 1.312
* ActiveGate version 1.311+ Linux
* ActiveGate version 1.311+ Containerized

Digital Experience | Synthetic

### Added ephemeral storage limits to containerized location template

The Containerized Synthetic location template now includes ephemeral storage requests and limits for each container.

Platform | Davis

### Support for dt.source\_entity resolving in event reports for classic properties mode

`dt.source_entity` can now be overwritten on events for classic configs supporting an event template (for example, log events, metric events). It is also possible to extract a value from another property via `{property}`.

Cluster

### Upgrade of Cassandra to version 4.1.8

As part of this release, the Cassandra nodes are upgraded to version 4.1.8 to provide bug and security fixes.

No manual user invention or downtime is necessary. The upgrade should happen via rolling updates as part of normal version updates.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.311](/managed/whats-new/dynatrace-api/sprint-311 "Changelog for Dynatrace API version 1.311")
* [Dynatrace API changelog version 1.312](/managed/whats-new/dynatrace-api/sprint-312 "Changelog for Dynatrace API version 1.312")

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

## Resolved issues

#### Cluster

* Fixed a bug where certain regions in India were missing on the world map for tenants with country set to India. (DEM-5641)

* Fixed an issue where, in premium HA environments, the connection to Elasticsearch was initialized with the wrong IP addresses. (MGD-3242)
* "Calculated service metrics" page: Unsupported units are no longer displayed in the "Unit" selection list. (APPOBS-5161)
* Fixed processing of invalid Split dimensions passed through URLs. (APPOBS-4744)
* Fixed distributed trace view share linking. (APPOBS-5276)
* Fixed an issue in the Calculated Service Metrics API that allowed the creation of unsupported metric "Capture full service call" (`CAPTURED_FULL_SERVICE_CALLS`). (APPOBS-5311)

#### Session Replay

* Fixed skip inactivity for sessions with long inactivity. (DEM-6209)