---
title: What's new in Dynatrace Managed 1.346
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-346
---

# What's new in Dynatrace Managed 1.346

# What's new in Dynatrace Managed 1.346

* Release notes
* 5-min read
* Published Aug 25, 2026
* Rollout start on Aug 31, 2026

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.346. It contains:

* [Feature updates](#updates): 9
* [Breaking changes](#breaking): 3
* [Fixes and maintenance](#fixes): 5

## Feature updates

Digital Experience | Synthetic

### Screenshots now sent directly from your cluster to Amazon S3

Screenshots captured in your Dynatrace environments are now uploaded to Amazon S3 directly from the cluster, replacing the previous flow where the upload was handled by VUC. This change eliminates the need to pass AWS credentials to VUC, reducing the credential exposure surface and improving overall security.

Infrastructure Observability

### Redesigned Azure page for quicker insights

We’re excited to announce a redesigned **Azure** page, bringing broader visibility, smoother navigation, and a more intuitive monitoring experience to your infrastructure performance workflows.

Platform

### Cassandra nodes upgrade to version 4.1.12

The Cassandra nodes are upgraded to version 4.1.12, delivering critical bug and security fixes. No manual user intervention or downtime is required—the upgrade happens via rolling updates as a part of normal version updates.

Platform

### Track tenant token rotation status and receive daily alerts

You can now query the current status of a tenant token rotation in your Dynatrace Managed environment using the new `api/v2/tenantTokenRotation/status` endpoint. While a rotation is in progress, a severe Cluster event is raised daily for the duration of the rotation, so cluster administrators stay informed until the rotation completes.

Previously, there was no way to check whether a rotation was in progress. An incomplete rotation persisted undetected and directly affected monitoring continuity.

Platform

### Redesigned user authentication pages in the Cluster Management Console

You can now manage user authentication in the Cluster Management Console through a redesigned experience. Across the **User authentication** pages, the filters, data tables, and actions look and behave consistently, and when you save or discard a change, it takes effect immediately, just like your environment settings.

Platform

### Simplified local self-monitoring environment

Local self-monitoring environments now show only the relevant capabilities that are available in the environment. This affects the environment’s ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**, main menu, and preset dashboards.

Platform

### Stay informed about unsupported Dynatrace Managed product versions

When you're using an unsupported version of Dynatrace Managed, you will be informed with a notification and a special tag on the **Licensing** page.

Platform | Dashboards

### Keep your management zone filter when you drill into remote dashboards

You can now drill down from an aggregated dashboard to a dashboard in a remote environment and keep your management-zone filter in place. The filter is applied automatically when you open the remote dashboard, so your monitoring context stays consistent as you navigate across environments. You can keep filters for multiple management zones simultaneously.

Previously, the filter was lost in the remote environment, and you had to select the same management zone again in each remote environment. The filter now carries over only when a management-zone name matches exactly between the source and remote environments.

Platform | Problems

### Send problem notifications to IPv6 webhook endpoints

You can now target IPv6 endpoints with problem notification webhooks, so your notification pipeline works in environments that run IPv6-only networks. The webhook URL field in **Settings** > **Integrations** > **Problem notifications** accepts IPv6 bracket notation alongside standard IPv4 addresses. Existing IPv4 webhook configurations continue to work without changes. Dynatrace itself continues to operate in an IPv4 setup. To enable IPv6 webhook support, run the installer with `--enable-ipv6-webhooks on`. For existing installations, use `--enable-ipv6-webhooks off` to revert to IPv4-only webhooks.

## Breaking changes

Application Observability

### Connections from OneAgent version 1.215 and earlier are rejected

Dynatrace now rejects connections from OneAgent version 1.215 and earlier. **Action plan:** If you're running OneAgent version 1.215 and earlier, upgrade to a supported OneAgent version to avoid data loss and connectivity issues, and to benefit from enhanced security and features unavailable in earlier OneAgent versions.

For details, see [End-of-life announcements](/managed/whats-new/technology/end-of-life-announcements "Information about technologies, features, or integrations scheduled for end of life (EOL) in Dynatrace, including upcoming and recently retired items.").

Application Observability | Distributed Tracing

### HTTP failure detection extended to FaaS services

HTTP failure detection now applies to FaaS services (AWS Lambda, Azure Functions, and GCP Cloud Functions) with HTTP data. After this update, you may see a higher failure rate in your environment. This is expected—issues with these services are now detected and reported for the first time.

Software Delivery

### Select a container registry in the Kubernetes deployment form

When configuring Kubernetes or OpenShift monitoring in the Managed deployment form, you can now select the container registry from a dropdown.

* **Amazon ECR** (new default)
* **Docker Hub**
* **Private container registry**
* **Built-in registry** (deprecated)

Based on your selection, Dynatrace automatically generates a ready-to-use `dynakube.yaml` and matching Helm install command with the correct image locations. For **Amazon ECR** and **Docker Hub**, no manual registry configuration is required, simplifying deployments and activating ARM-based environments. For private container registry, image locations must still be configured manually, as before.

The built-in cluster container registry will be shut down on January 1, 2028, and will no longer function because it doesn't support ARM architectures. **Action plan**: Migrate to Amazon ECR or Docker Hub.

## Fixes and maintenance

### Resolved issues in this release

* Fixed an issue where an unstable connection to Mission Control could leave the Managed server installer stuck in a downloading state indefinitely. (PRISM-13852)
* Fixed an issue where audit log entries for user removals from user groups and alert notifications showed an empty value instead of the affected user's username. (PRISM-13761)
* Fixed a pin-to-dashboard issue that caused HTTP 400 errors. (PRISM-13091)
* Fixed an error that occurred when filtering problems using a search string that contained many special characters. (DI-30187)
* Fixed an issue where named-target `POST` forms failed to submit when the target window was already open, causing the action to time out. If you applied the `disableNewWindowPostFormsHandling` experimental property as a workaround, you can now remove it. (DEM-28422)

## Operating systems support

* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.8
* Added support for [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.2

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

* [Dynatrace API changelog version 1.346](/managed/whats-new/dynatrace-api/sprint-346 "Changelog for Dynatrace API version 1.346")
* [Dynatrace API changelog version 1.345](/managed/whats-new/dynatrace-api/sprint-345 "Changelog for Dynatrace API version 1.345")