---
title: Dynatrace Managed release notes version 1.320
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-320
---

# Dynatrace Managed release notes version 1.320

# Dynatrace Managed release notes version 1.320

* Release notes
* 10-min read
* Updated on Sep 18, 2025
* Rollout start on Aug 4, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.320.

## Announcements

Platform | Metrics

### Upcoming native support for OpenTelemetry and Prometheus histograms

Starting with Cluster version 1.324, Dynatrace introduces native support for OpenTelemetry and Prometheus histograms, including automatic percentile calculation. This enhancement enables faster detection of performance outliers and simplifies observability workflows.

**Breaking change for existing histogram metrics:**

* Existing histogram metrics will no longer be updated, but they will remain available for historical visualization on dashboards, ensuring continuity and data retention. The new native histogram metrics will be exposed under distinct metric keys, each suffixed with `.histogram`.
* If an existing metric already ends with `.histogram` or `_histogram`, it will no longer receive new data points. To use the new histogram functionality under the same metric key, you must delete the existing metric using the [Metrics API - DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API."). After deletion, a new histogram metric will be automatically created under the same key.

In Dynatrace, in your [**Local-Self-Monitoring** environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn about the local self-monitoring environment that collects internal Dynatrace Managed Cluster health metrics and stores all data exclusively on-premises."), you can use the following query in [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to see which histogram metrics have been ingested:

```
isfm:active_gate.metrics.ingest.explicit_bucket_histogram.layout.series



:splitBy(metric_key,"dt.tenant.uuid",data_source)



:sort(value(auto,descending))



:limit(100)
```

This query requires Cluster version 1.314+ to be installed for the metric to be available.

## New features and enhancements

Platform | Deployment

### Bulk migration of OneAgents between Managed environments

We have simplified the process of migrating multiple OneAgents across environments, enabling centralized control and reducing manual effort.

This feature supports both web UI–based workflows and REST API integration, offering flexibility for manual and automated operations.

For details, see [Web UI procedures](/managed/ingest-from/bulk-configuration#web-ui-procedures "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") and [API procedures](/managed/ingest-from/bulk-configuration#api-procedures "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.").

Platform | Deployment

### Reconfigure IP address of cluster node without full redeployment

Administrators can now update the IP address of individual nodes within a cluster without requiring a full redeployment. This simplifies network reconfiguration and enhances flexibility in dynamic infrastructure environments.

For details, see [Reconfigure the IP address of a cluster node](/managed/managed-cluster/operation/ip-reconfiguration "Learn how to reconfigure your node's IP address.").

Platform | Tags

### Understand which rule applied a tag to a monitored entity

We have updated the web UI and Monitored entities API to provide information about which specific rule caused a tag being applied to a monitored entity.

In the web UI, you can select a tag to go directly to the source rule in Settings UI for [Automatically applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") or [Manually applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically."). See for example this web UI display:

![Example of tagging info displayed in web UI](https://dt-cdn.net/images/screenshot-2025-07-31-at-15-23-13-914-d2778ef664.png)

Example of tagging info displayed in web UI

The [Monitored entities API v2](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") includes additional fields `source` and `sourceSetting` as part of the tag-information. The `source` field indicates how the tag was applied, and `sourceSetting` specifies the associated Settings object. You can use the [Settings API](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") to retrieve the object (source rule).

**Example Monitored entities API v2 response**

```
{



"context": "CONTEXTLESS",



"key": "conditional-load-test",



"stringRepresentation": "conditional-load-test",



"source": "Auto tags",



"sourceSetting": "api/v2/settings/objects/...."



},
```

Platform | Data Explorer

### Sort dimensions alphanumerically in the metric selector

A new optional parameter is available for dimension sorting in the metric selector. The default is `lexical`, which is the default value and sorts dimension values in lexicographic order; the other available option is `natural`, which detects digits in a dimension and sorts according to their numeric value.

For details, see [Metrics API - Metric selector: Sort transformation](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Configure the metric selector for the Metric v2 API.").

Platform | Data Explorer

### Fetching metric-key suggestions optimized

We’ve optimized filtering for metric-key suggestions in the Data Explorer, so suggestions now appear much faster when you start typing. This ensures a smooth experience, even when working with large datasets.

Platform | Davis

### Problem close time metadata now shown in classic problem details

The classic problem details page now shows the time when a problem was closed in Dynatrace, next to the other lifetime data. This allows you to quickly see the maximum time that was used for alerting profile duration filters when the problem was still in the open state.

Digital Experience | Session Replay

### Firefox browser extension added for Session Replay

A Firefox browser extension has been added for Session Replay. A link to the Firefox store will now appear when replaying a session and we identify that the extension is not installed (as was done with Chrome and Edge).

Digital Experience | RUM Web

### Control loading and execution of the RUM JavaScript with `defer` and `async`

To reduce parse-blocking JavaScript, you can now manage how the RUM monitoring code is loaded and executed by using the `async` or `defer` attributes. These attributes can be applied to the following snippet formats:

* [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [OneAgent JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case")

Platform

### Upgrade of third-party Jetty WebServer functionality to version 12

As part of this release, the included Jetty WebServer functionality is upgraded to version 12.0.22 in Dynatrace Server and ActiveGate.

No manual user-invention or downtime is necessary, the upgrade should happen via rolling updates as part of normal version updates.

Note: In certain high-load scenarios, we experienced a slight increase in CPU and memory usage caused by implementation changes in Jetty 12. If ActiveGate instances are very short on resources, we advise a slight increase to avoid potential overload.

OneAgent

### Additional code module download options via Deployment API

The `multidistro` flavor can now be combined with ARM architecture when downloading code modules via the Deployment API.

Extensions

### Warning status support

The Extensions 2.0 framework now understands and can produce both `WARNING` and `PENDING` status. Those statuses have been added to the already present `OK` and `ERROR`.

## Breaking changes

Log Monitoring

### Log ingest via REST API strictly validates request payload size for compressed payloads

Log ingest via REST API now strictly validates the request payload size for compressed payloads.

* Previously, some requests that contained compressed payloads below the size limit of 10 MB, with an uncompressed payload size that exceeded 10 MB, were accepted.
* Now, such requests are rejected with HTTP status code 431. Whether compressed or uncompressed, the payload size must now be below 10 MB.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.319](/managed/whats-new/dynatrace-api/sprint-319 "Changelog for Dynatrace API version 1.319")
* [Dynatrace API changelog version 1.320](/managed/whats-new/dynatrace-api/sprint-320 "Changelog for Dynatrace API version 1.320")

## Operating systems support

* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6
* Added support for [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6
* Added support for [Rocky Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6

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