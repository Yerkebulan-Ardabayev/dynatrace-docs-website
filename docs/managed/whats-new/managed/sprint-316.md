---
title: Dynatrace Managed release notes version 1.316
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-316
---

# Dynatrace Managed release notes version 1.316

# Dynatrace Managed release notes version 1.316

* Release notes
* Updated on Jul 04, 2025
* Rollout start on Jun 10, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.316.

## New features and enhancements

Digital Experience | RUM Web

### Customize the RUM monitoring code filename prefix

You can now specify a custom prefix for the RUM monitoring code filename, which helps prevent it from being blocked by ad blockers.

For more information, see [Configure the Real User Monitoring Classic code source](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source#configure-custom-monitoring-code-filename-prefix "Configure the Real User Monitoring Classic code source for your specific requirements.").

Dynatrace Cluster

### New warning for multiple `:rollup` operators in metric selectors

While previously allowed, multiple `:rollup` operators on the same transformation chain can lead to unintended behavior.

To help prevent that, we’re introducing a new warning mechanism that detects when multiple `:rollup` operators are applied within the same transformation chain. The system will now issue a warning if it detects multiple `:rollup` operators, giving you clearer insights and helping ensure more predictable outcomes.

Dynatrace Cluster

### Upgraded third-party Jetty WebServer functionality

As part of this release, the included Jetty WebServer functionality is upgraded to version 10.0.25 in Dynatrace Server and ActiveGate.

No manual user intervention or downtime is necessary; the upgrade should happen via rolling updates as part of normal version updates.

Dynatrace Cluster

### Improved performance of Metrics API v2 for listing metrics

We have optimized the [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."), which lists all available metrics. It now requires significantly less data reading to provide the information, and if called frequently, it may now be returned more quickly. No changes to the returned information are expected.

## Breaking changes

Dynatrace Cluster

### Fixed missing Content Security Policy (CSP) headers in SAML sign-in process

We have fixed an issue with missing Content Security Policy (CSP) headers in the SAML sign-in process.

However, if the sign-in process involves redirects to URLs other than those defined in **XML metadata of a SAML 2.0 Identity Provider** (see [Manage users and groups with SAML in Dynatrace Managed](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.")), the CSP rule `form-action` could be violated, causing sign-in failure.

Any additional URLs must be added as described in [Manage users and groups with SAML in Dynatrace Managed](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.").

![User group attribute setting for SSO IdP redirect.](https://dt-cdn.net/images/man-sso-idp-923-ff2e96b558.png)

User group attribute setting for SSO IdP redirect.

Digital Experience | Synthetic

### Browser monitor autologin is deprecated

Autologin is now deprecated in browser monitors:

* Browser monitors containing autologin/web form authentication can no longer be saved via API v1 or the web UI.
* 'Web form' authentication is no longer available when creating a browser monitor or on the **Advanced setup** page.

Infrastructure Observability | Kubernetes

### Anomaly Detection: Improved "High CPU throttling" alert

We have improved the "High CPU throttling" alert by adjusting the calculation from throttling/usage to throttling/limits. This enhancement ensures more accurate alerts, particularly in scenarios involving idle pods, thereby reducing false positives.

With this update, you can now trust the "High CPU throttling" alert to provide more reliable and actionable insights. If you have customized the thresholds for this alert, please revisit them to ensure they align with the new calculation method.

Dynatrace Cluster

### Assigning management zones from security context is deprecated

Assigning management zones from the security context is deprecated and will be removed with Dynatrace Managed version 1.322.

With this change, **Settings** > **Preferences** > **Management zones** > **Security context settings** will no longer be available.

Use [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") instead.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see [Dynatrace API changelog version 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316").

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