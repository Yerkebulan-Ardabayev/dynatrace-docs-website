---
title: End-of-life announcements
source: https://www.dynatrace.com/docs/whats-new/technology/end-of-life-announcements
scraped: 2026-02-22T21:29:15.079292
---

# End-of-life announcements

# End-of-life announcements

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jan 15, 2026

## General policy

To deliver a premium experience, Dynatrace evolves in step with the technology stacks we build on. When our partner vendors retire older components, we also phase them out so you receive the most secure and fully supported innovations.

We communicate these changes through two milestones that help you plan ahead:

### End of Support (EoS)

* Last date on which Dynatrace provides bug fixes or security updates.
* After EoS, the component keeps running, but maintenance stops and support is best-effort only. Features will no longer be maintained, and no critical fixes will be deployed.
* Ongoing operation, and associated risk, becomes the customerâs responsibility.

### End of Life (EoL)

* Latest date when Dynatrace disables, removes, or blocks the component, ending its useful operation.
* Upgrade paths remain open so you can migrate and continue getting full value from Dynatrace.
* Support tickets related to the component are no longer accepted.

## Scheduled EOL for unsupported OneAgent versions

If you are running any of the OneAgent versions listed below, upgrade to a supported version before the EOL date to ensure uninterrupted monitoring.

| OneAgent versions | Standard EoS [1](#fn-1-1-def) | EoL |
| --- | --- | --- |
| 1.141 and earlier | 2018 | Aug 1, 2025 |
| 1.215 and earlier | April 29, 2022 | Oct 1, 2025 |
| 1.241 and earlier | June 8, 2023 | Jan 1, 2026 |
| 1.299 and earlier | Sep 30, 2025 | Sep 1, 2026 |

1

[Support policyï»¿](https://www.dynatrace.com/company/trust-center/support-policy/)

## Python Extension Framework 1.0

Weâre moving away from the retired Python 3.5/3.8 runtimes to a current, fully supported Python version so your extensions stay secure and future-ready. This extension framework upgrade closes unpatched security gaps, gives you access to the latest libraries and performance gains, and ensures continued compatibility with upcoming Dynatrace features.

### OneAgent extensions

OneAgent version 1.299 is the last release that support the Python Extensions 1.0 framework.

* EoS: Support (that is bug fixes, security updates) ended on Sep 30, 2025.
* Python Extension Framework 1.0 is EoS since Sep 1, 2024.
* To continue using extensions after the OneAgent version 1.299 EoL date, migrate to the new [Extensions framework](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and [update OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") to a supported version. See [Migration guides for custom extensions 1.0](#migration)

### ActiveGate extensions

ActiveGate version 1.299 is the latest release that supports Python Extensions 1.0.

* EoS: Support (that is bug fixes, security updates) ended Sep 30, 2025.
* Python Extension framework 1.0 is EoS since Sep 1, 2024.

### Migration guides for custom extensions 1.0

Migrate all Python extensions 1.0 to the new Extensions to maintain a secure, supported environment.

* [Migrate Python extensionsï»¿](https://developer.dynatrace.com/develop/extensions/dynatrace-extensions-vscode/guides/migrate/python-migrate/)
* [Video: A Practical Guide to Building Python Based Extensions with Dynatraceï»¿](https://www.youtube.com/watch?v=g-lPIZx66BA)

To remain supported, [update your OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") to the latest version.

## Native mobile applications for iOS and Android

As part of our ongoing commitment to delivering a streamlined and consistent user experience, Dynatrace is retiring its [native mobile applications for iOS and Android](/docs/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Learn how you can connect your Dynatrace environments with the Dynatrace mobile app to receive problem alerts."). This change aligns with our strategy to provide a unified, responsive web interface and leverage modern, flexible notification channels.

### Key dates

* **Last app update**: End of 2025
* **Sunset date**: June 30, 2026
* **Support ends**: June 30, 2026

### Whatâs changing?

The Dynatrace native mobile apps will no longer be available for download or supported after the sunset date.

We encourage you to access Dynatrace via the responsive web interface, which offers full functionality across all device types and screen sizes.

Push notifications will now be delivered through third-party integrations such as Slack, Teams, PagerDuty, email, and ntfy.

### Why this change?

* **Unified experience**: A single responsive web platform ensures consistent functionality across all devices.
* **Flexibility**: You can choose your preferred communication tools for alerts and updates.

### Recommended actions

* Begin using the responsive web interface.
* Set up your preferred notification integrations via:

  + Dynatrace SaaS: [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
  + Dynatrace Managed: [Problem notifications](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.")
* Remove the native app from your devices after the sunset date.

### Need help?

For assistance with transitioning or setting up integrations, please see the Documentation links above or contact Support.