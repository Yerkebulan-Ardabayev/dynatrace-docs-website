---
title: Dynatrace Managed release notes version 1.322
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-322
scraped: 2026-05-12T11:07:58.627277
---

# Dynatrace Managed release notes version 1.322

# Dynatrace Managed release notes version 1.322

* Release notes
* 10-min read
* Updated on Sep 18, 2025
* Rollout start on Sep 1, 2025

Rollout start: Sep 1, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.322.

## Announcements

Platform | Metrics

### Upcoming native support for OpenTelemetry and Prometheus histograms

Starting with Cluster version 1.324, Dynatrace introduces native support for OpenTelemetry and Prometheus histograms, including automatic percentile calculation. This enhancement enables faster detection of performance outliers and simplifies observability workflows.

**Breaking change for existing histogram metrics:**

* Existing histogram metrics will no longer be updated, but they will remain available for historical visualization on dashboards, ensuring continuity and data retention. The new native histogram metrics will be exposed under distinct metric keys, each suffixed with `.histogram`.
* If an existing metric already ends with `.histogram` or `_histogram`, it will no longer receive new data points. To use the new histogram functionality under the same metric key, you must delete the existing metric using the [Metrics API - DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API."). After deletion, a new histogram metric will be automatically created under the same key.

In Dynatrace, in your [**Local-Self-Monitoring** environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health."), you can use the following query in [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to see which histogram metrics have been ingested:

```
isfm:active_gate.metrics.ingest.explicit_bucket_histogram.layout.series



:splitBy(metric_key,"dt.tenant.uuid",data_source)



:sort(value(auto,descending))



:limit(100)
```

This query requires Cluster version 1.314+ to be installed for the metric to be available.

## New features and enhancements

Application Observability | Services

### Define custom services for short-lived Go processes via web UI

You can now define a custom service for short-lived Go processes through the web UI. Similarly to Java, the **Define entry point manually** function is now available for Go.

Previously, defining a custom service for short-lived Go processes was only possible via the [Configuration API](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services#go-service-via-api "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.").

For details, see [Service detection rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.").

Digital Experience | Session Replay

### Session Replay: mobile browser UI improvement and iframe handling

A session recorded from a mobile browser shows the unrecorded gaps on the screen instead of fake UI elements (keyboard, navbar).

Sessions recorded on a desktop from a non-top iframe with a long resolution are zoomed to the interacted part.

Digital Experience | Session Replay

### Added new placeholders for frameset and canvas elements

Session Replay now has placeholders to replace the unsupported frameset and canvas elements.

We have also added legends for both placeholders on the image placeholders legends box.

Infrastructure Observability | Hosts

### Python module and script fields added to a process group

Python module and script fields are now available for Python process groups and processes.

Infrastructure Observability | Extensions

### Extension Execution Controller enabled by default

The Extension Execution Controller (EEC) is now enabled by default in new environments. There are no changes for existing environments.

Platform | Dashboards

### Share dashboards with IAM policyâbased users and groups

In addition to sharing dashboards with role-based users and groups, you can now share dashboards with IAM policyâbased users and groups through the dashboard-specific share setting.

Platform | Metrics

### Increased default metric dimensions limit for anomaly detection static threshold model

The default metric dimensions limit for static threshold configurations has been increased from `1,000` to `2,000`.

## Breaking changes

Application Observability | Services

### Service detection v2: Endpoint detection rules have been updated

With this release, only service entry points (server/consumer spans) become endpoints, excluding outbound calls to other services. Endpoint names also change to include the HTTP method.

Results:

* Focuses metrics on actual service health rather than total system activity.
* Reduces endpoint counts and improves service performance representation.

Availability:

* New environments get these new rules automatically.
* Existing environments must opt in via Settings.

To preview changes before opting in, use the dashboard attached to our [Dynatrace Communityï»¿](https://dt-url.net/lv031sg) post.

For details, see [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

Digital Experience | RUM Web

### AMP application monitoring no longer supported

Support for monitoring AMP (Accelerated Mobile Pages) applications has been discontinued. As a result, AMP applications are no longer available within your environments.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.321](/managed/whats-new/dynatrace-api/sprint-321 "Changelog for Dynatrace API version 1.321")
* [Dynatrace API changelog version 1.322](/managed/whats-new/dynatrace-api/sprint-322 "Changelog for Dynatrace API version 1.322")

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