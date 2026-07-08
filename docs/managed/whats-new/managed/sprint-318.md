---
title: Dynatrace Managed release notes version 1.318
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-318
---

# Dynatrace Managed release notes version 1.318

# Dynatrace Managed release notes version 1.318

* Release notes
* 10-min read
* Updated on Aug 19, 2025
* Rollout start on Jul 7, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.318.

## New features and enhancements

Application Observability | Service detection

### Tailored services and endpoints for your applications with Service Detection v2 (SDv2)

Service Detection v2 (SDv2), an evolution of Service Detection v1, enables you to tailor services, endpoints, and failure detection to your business needs. SDv2 harmonizes OneAgent and OpenTelemetry services with the goal of providing the same functionality for all trace data.

With this initial release, OpenTelemetry services are supported, and the Adobe Experience Manager is supported as the first OneAgent technology.

![Adobe Experience Manager](https://dt-cdn.net/images/adobe-experience-manager-1737-7f7de41e91.png)

Adobe Experience Manager

SDv2 operates according to a single set of rules that are based on resource attributes. The underlying rules are customizable, and you can use any resource attribute to add context to your services.

SDv2 also introduces the endpoint concept, which represents an evolution of key requirements. Endpoints enable you to understand your application interactions and detect anomalies using baseline metrics.

![Service detection v2 settings](https://dt-cdn.net/images/sdv2-config-1609-2032994dc6.png)

Service detection v2 settings

To learn more about SDv2, see [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

Platform

### Rack-aware health status in premium HA

For Managed clusters newer than Managed version 1.302 in a Premium High Availability deployment, DC failover is triggered only if unhealthy nodes span more than one rack.

Application Observability | Distributed Traces

### Improved attribute visualisation for individual trace view

All available horizontal screen space is now utilized by attributes until either the space is fully occupied or all attributes have been displayed.

![Improved attribute visualisation for individual trace view](https://dt-cdn.net/images/solution-proposal-1-b0f77a2221.gif)

Improved attribute visualisation for individual trace view

Log Monitoring

### Collect and analyze structured data from Windows event logs

OneAgent version 1.317+

You can collect structured data from Windows Event Logs and anlyze it with Dynatrace Managed. To enable it, go to **Settings** > **Log Monitoring** > **Log module feature flags** and enable **Support for structured data in Windows Event Logs**.

When enabled, structured data is collected from Windows event logs from the "User Data" branch or, if unavailable, from the "Event Data" branch and its sub-branches. The collected data is transmitted as attributes along with the recorded content.

Attribute names are derived from available information such as tag names or the value of the name field. When tag names are repeated and the name field is empty, a sequential number is appended to the tag name.

Sub-branches without values and tags labeled as "Binary" are omitted.

Settings

### Fixed incorrect placing of buttons when configuring Java service definitions

Fixed an issue where buttons were rendered off-screen when configuring Java service definitions on certain display sizes.

Platform

### Improved Cassandra repair stability

When a Cassandra repair operation is executed manually for some reason, we now run it table by table in order to avoid causing too much overhead on the overall cluster.

Platform

### Upgrade of Cassandra to version 4.1.9

As part of this release, the Cassandra nodes are upgraded to version 4.1.9 to provide bug and security fixes.

No manual user invention or downtime is necessary. The upgrade should happen via rolling updates as part of normal version updates.

Digital Experience | Synthetic

### Deprecation and replacement of Location and Node health status metrics

We have deprecated the following Location and Node health status metrics and replaced them with the new self-monitoring metrics.

| Deprecated Metric | Replacement Metric |
| --- | --- |
| `builtin:synthetic.location.health_status` | `dsfm:synthetic.location.health_status` |
| `builtin:synthetic.location.node.component.healthStatus` | `dsfm:synthetic.location.node.component.health_status` |

Licensing

### Smoothed out a corner case in Classic Licensing

Cluster version 1.318.84+ For rare cases in classic licensing with application-only monitoring, a requirement has been changed for the benefit of customers. The host unit billing system now attempts to query the PaaS memory limit for short-lived hosts multiple times before it falls back to the host memory.

## Breaking changes

Platform | Mission Control

### Mission Control cipher update

The Mission Control ciphers have been reduced, and only the following are accepted:

```
TLS_AES_128_GCM_SHA256



TLS_AES_256_GCM_SHA384



TLS_CHACHA20_POLY1305_SHA256



ECDHE-ECDSA-AES128-GCM-SHA256



ECDHE-RSA-AES128-GCM-SHA256



ECDHE-ECDSA-AES256-GCM-SHA384



ECDHE-RSA-AES256-GCM-SHA384
```

Ensure that all connections you establish to Mission Control support these ciphers. If they don't support the listed ciphers, no connection to Mission Control can be established.

Infrastructure Observability | Hosts

### Improved splitting Oracle Net Listener processes by listener name

Fixed the issue of Oracle Net Listener processes not being split by name when OS Services are not collected on Windows. Also, now a correct listener name is used instead of Oracle home name.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.317](/managed/whats-new/dynatrace-api/sprint-317 "Changelog for Dynatrace API version 1.317")
* [Dynatrace API changelog version 1.318](/managed/whats-new/dynatrace-api/sprint-318 "Changelog for Dynatrace API version 1.318")

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