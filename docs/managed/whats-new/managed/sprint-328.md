---
title: What's new in Dynatrace Managed version 1.328
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-328
scraped: 2026-05-12T11:07:49.394800
---

# What's new in Dynatrace Managed version 1.328

# What's new in Dynatrace Managed version 1.328

* Release notes
* Published Nov 20, 2025
* Rollout start on Dec 02, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.328. It contains:

* [Breaking changes](#breakingchanges): 2
* [Fixes and maintenance](#fixes): 1

## Breaking changes

Application Observability

### Consistent data in Kubernetes observability now ensured

To avoid inconsistent data in Kubernetes observability, both OneAgent OS module and OneAgent code modules are now rejected if the OS module is outdated in the cloud-native full-stack mode configuration. The affected workloads will lose observability until all module versions are synchronized.

**Action required:**

Update the OneAgent OS module to a version that is at least equal to the latest version of any code module running on the Kubernetes cluster.

Platform

### SAML HTTP-redirect message signing added

Added support for message signing in SAML HTTP-Redirect binding.

* If `wantsAuthnRequestsSigned=true` is specified in `XML metadata of a SAML 2.0 Identity Provider`, **AuthnRequests** are now signed. Previously, this setting was ignored.
* **LogoutRequests** and **LogoutResponses** are now signed by default.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.328](/managed/whats-new/dynatrace-api/sprint-328 "Changelog for Dynatrace API version 1.328")
* [Dynatrace API changelog version 1.327](/managed/whats-new/dynatrace-api/sprint-327 "Changelog for Dynatrace API version 1.327")

## Fixes and maintenance

### Resolved issues in this release

* Disabled sharing based on the IAM policy. (PAPA-29450)

### Resolved issues (update 1.328.87.20251229-091620)

* Fixed a problem with the NGINX health check module, which is responsible for redirecting traffic between cluster nodes. (MGD-9000)