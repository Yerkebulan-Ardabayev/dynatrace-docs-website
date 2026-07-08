---
title: Dynatrace Managed release notes version 1.306
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-306
---

# Dynatrace Managed release notes version 1.306

# Dynatrace Managed release notes version 1.306

* Release notes
* Updated on Apr 30, 2025

Rollout start: Jan 20, 2025

## Breaking changes

### AWS log forwarder EOL

As announced earlier, the Dynatrace [AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Use AWS log forwarding to ingest AWS logs.") is deprecated.

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change End of support for the Dynatrace AWS log forwarder was Dec 31, 2024.

If you are still using the deprecated AWS log forwarder, we recommend that you switch to the new [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

### Logs Classic custom attribute keys are now case-sensitive

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

This release ends the transition period for custom attribute case-sensitivity changes.

Starting with this release (Dynatrace Managed version 1.306):

* Custom attributes allow uppercase letters.
* Attributes of ingested log events are strictly matched with the attribute definitions (including uppercase or lowercase).

Custom attribute keys have to be case-sensitively unique, which means that custom attributes differing only in letter case are no longer treated as the same attributes. For example, it is now possible to define two different custom attributes named **MyAttribute** and **myattribute**.

Searches become case-sensitive (except for filter-only attributes). For example, if you define a custom attribute `MyAttribute`, then a search for `MyAttribute="SEARCH"` will return log events having this particular attribute value set to `SEARCH` but `myattribute="SEARCH"` will not.

Query values remain case-insensitive. For example, `MyAttribute="SEARCH"` is equivalent to `MyAttribute="search"`.

## New features and enhancements

### Additional attributes can be used for "Request naming" rules

Application Observability | Distributed Traces

Every attribute listed in the classic trace view, on the **Summary** tab, section **OneAgent attributes**, can be used for custom request names.

### Limit for complex event filters in Alerting Profiles

Platform | Problems

A new default limit of 1,000 unique complex event title/description filters counted over all Alerting Profiles has been introduced.

An event title/description filter is considered complex if it is either a `contains` operator with case sensitivity turned off, or a `contains regex` operator.

An Alerting Profile with only a single unique complex event title/description filter does not count toward the maximum limit.

### Kubernetes monitoring restart minimized

Infrastructure Observability | Kubernetes

Kubernetes monitoring restart has been minimized on Kubernetes settings update without actual content change.

### Kubernetes setting toggle "Monitor persistent volume claims" removed

Infrastructure Observability | Kubernetes

The toggle **Monitor persistent volume claims** has been removed, as the persistent volume claim metrics are now ingested as built-in metrics by default. For details, see [Introducing built-in Persistent Volume Claim Monitoring for Kubernetes﻿](https://community.dynatrace.com/t5/Dynatrace-tips/Introducing-built-in-Persistent-Volume-Claim-Monitoring-for/td-p/244902).

### New attributes in Windows event logs

Infrastructure Observability | Log Analytics

Added two new attributes, `User name` and `Keywords`, both from Windows event logs, to Log Viewer and as matchers in an ingest configuration.

### Unified descriptions of Infrastructure metrics

Infrastructure Observability | Hosts

The descriptions of Infrastructure metrics on the Metrics browser page and the Metric selector in the latest Dynatrace have been unified.

### OTLP (OpenTelemetry Protocol) Metrics ingest: Default resource attributes allow list extended

Metrics Ingestion Protocol

In OTLP (OpenTelemetry Protocol) metrics ingest, the default allow list for resource and scope attributes to be taken over as metrics dimensions was extended.

Several attributes in the `k8s.*` and `dt.*` namespace were added as well as `service.instance.id`.

If the new attributes are not desired, the individual toggles can be turned off under **Settings** > **Metrics** > **OpenTelemetry metrics** > **Allow list: resource and scope attributes** (or the entry can be removed altogether).

### New application parameter for user session anonymization

The [Anonymization API - PUT anonymization job](/managed/dynatrace-api/environment-api/anonymization/put-job "Start anonymization job to remove user data via Dynatrace API.") supports anonymization of user sessions based on an internal application ID via the parameter `requestId` (or `clusterRequestIds` for Premium High-Availability clusters).

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.305](/managed/whats-new/dynatrace-api/sprint-305 "Changelog for Dynatrace API version 1.305")
* [Dynatrace API changelog version 1.306](/managed/whats-new/dynatrace-api/sprint-306 "Changelog for Dynatrace API version 1.306")

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