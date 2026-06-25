---
title: Dynatrace Managed release notes version 1.310
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-310
scraped: 2026-05-12T11:07:50.714448
---

# Dynatrace Managed release notes version 1.310

# Dynatrace Managed release notes version 1.310

* Release notes
* Updated on Apr 10, 2025

Rollout start: Mar 18, 2025

This page showcases new features, changes, and bug fixes in Dynatrace Managed version 1.310.

## Breaking changes

Breaking change ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability | OS services monitoring

### OS services monitoring policy now requires detection rule

New or modified OS services monitoring policies require defining at least one detection rule. Preexisting policies will be honored without changes.

In addition, detection rules support the `$match()` operator.

Breaking change ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform | Settings

### Settings audit log changes

We adjusted settings audit log generation to improve readability and reduce spam.

Changes to the rank of objects due to reordering them in a ranked list will now be reflected as follows:

* In the audit log API: `REORDER` (from `UPDATE`) if the value itself was not changed, or `UPDATE` (as before) if the value itself was changed.

## New features and enhancements

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability | Application Observability | Vulnerability Analytics

### Observe and protect your Python stacks

Starting with Dynatrace Managed version 1.310+ and OneAgent version 1.309+, you can monitor your Python processes, trace your Python applications and services end-to-end, and analyze your Python runtime and third-party libraries for vulnerabilities.

For a complete list of all supported Python technologies, see [Technology support](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Python code module](/managed/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.").

#### Infrastructure Observability

Observe the health and availability of your Python processes and identify Python garbage collection bottlenecks across all generations and thread misbehavior. The following Python process metrics are available:

* Python GC collections count (gen0, gen1, gen2)
* Python GC collected objects (gen0, gen1, gen2)
* Python GC uncollectable objects (gen0, gen1, gen2)
* Python GC time (gen0, gen1, gen2)
* Number of active Python threads
* Number of allocated memory (heap) blocks

To get started

1. Go to **Settings** > **Monitoring** > **Monitoring technologies**.
2. Find Python and enable **Monitor Python**.
3. [Create a process monitoring rule](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring") to enable deep monitoring of the selected processes.

#### Application Observability

Automatically detect your Python applications across every tier and diagnose anomalies with Davis AI to determine the root cause down to the broken code. End-to-end service observability combined with code-level insights and exception analysis will help you ensure the robustness of your production environment.

For a complete list of all supported Python technologies, see [Technology support](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To get started

1. Ensure that Python monitoring is enabled (see [Infrastructure Observability](#infrastructure-observability) above).
2. Go to **Settings** > **Preferences** > **OneAgent features**, find and enable all Python sensors of interest, and then restart your processes.

#### Vulnerability Analytics

Automatically detect Python runtime and third-party vulnerabilities in your Python applications, quickly assess their impact on your monitored environment, and prioritize remediation efforts.

To get started

1. Ensure that Python monitoring is enabled (see [Infrastructure Observability](#infrastructure-observability) above).
2. Go to **Settings** > **Preferences** > **OneAgent features**, find and enable Python software component reporting, and then restart your processes.
3. Go to **Settings** > **Application Security** > **Vulnerability Analytics** > **General settings**, and then enable Python.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform | Davis

### Problem merging: `is same as` generic relationship now taken into account

Problem merging now takes the `is same as` generic relationship into account, which can be defined in the topology model, generic relationship settings.

Two events on different entities will merge into the same problem if:

* The two events are connected via `is same as`
* The two events do not explicitly disable merging
* The start times of the two events are close to each other

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Platform | Platform Services

### Network zone environment limit

There is now a network zone environment limit of `10,000` by default.

Feature update ![Dot](https://dt-cdn.net/images/dot-a32314f261.svg "Dot") Infrastructure Observability

### Resilient updates for Environment ActiveGates

We're excited to announce enhancements to the ActiveGate auto-update mechanism. The new update process ensures that updates within network zones, ActiveGate groups, and Synthetic private locations are performed in a rolling fashion. These improvements brings several benefits:

* **Minimized downtime**: By updating ActiveGates sequentially, we reduce the risk of service interruptions.
* **Enhanced stability**: Rolling updates ensure that only a subset of ActiveGates is updated at any given time, maintaining overall system stability.
* **Improved reliability**: This method allows for better monitoring and quick interruption if any issues arise during the update process.

These changes will significantly enhance the performance and reliability of ActiveGate deployments.

## Dynatrace API

To learn about changes to the Dynatrace API in this release, see:

* [Dynatrace API changelog version 1.309](/managed/whats-new/dynatrace-api/sprint-309 "Changelog for Dynatrace API version 1.309")
* [Dynatrace API changelog version 1.310](/managed/whats-new/dynatrace-api/sprint-310 "Changelog for Dynatrace API version 1.310")

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