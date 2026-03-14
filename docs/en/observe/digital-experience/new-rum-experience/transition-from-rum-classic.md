---
title: Transition from RUM Classic to the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/transition-from-rum-classic
scraped: 2026-03-06T21:25:59.818788
---

# Transition from RUM Classic to the New RUM Experience


* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Feb 20, 2026

If you already monitor your web and mobile frontends with RUM Classic, upgrading to the New RUM Experience is straightforward. Learn how the New RUM Experience relates to RUM Classic and how to enable it.

## Enable the New RUM Experience

Upgrading from RUM Classic to the New RUM Experience requires only a configuration change. The following guides outline the necessary steps.

[Web](web-frontends/initial-setup/enable-new-rum-for-web-apps.md) [Android](mobile-frontends/android/id-01-initial-setup.md) [iOS](mobile-frontends/ios/id-01-initial-setup.md) [React Native](mobile-frontends/react-native/id-01-initial-setup.md) [Flutter](mobile-frontends/flutter/id-01-initial-setup.md) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](mobile-frontends/maui/id-01-initial-setup.md) 

## Relationship between the New RUM Experience and RUM Classic

The New RUM Experience currently relies on certain RUM Classic functionalities. Hereâs what this means for you.

#### Enabling the New RUM Experience

You can currently enable the New RUM Experience only if RUM Classic is active. At this time, disabling data ingestion into RUM Classic and fully migrating is not possible.

#### Configuration

Most configuration settings for the New RUM Experience are based on those already used by RUM Classic. This means that:

* Changes made in the New RUM Experience also apply to RUM Classic.
* Conversely, if you modify settings in RUM Classic that are also available in the New RUM Experience, those changes will apply there as well.

Event and session properties are an exceptionâthey have a separate configuration from user action and session properties in RUM Classic.

#### Monitoring traffic

When the New RUM Experience is enabled, RUM beacons in a new format are sent alongside RUM Classic beacons to the same endpoint.

#### Infrastructure requirements

At this point, the New RUM Experience relies only on the HTTP headers and cookies already covered by the [firewall constraints for RUM Classic](../web-applications/initial-setup/firewall-constraints-for-rum.md "Find out how to make sure that Real User Monitoring data passes through your firewall."). If your firewalls and other infrastructure components are already configured to let these headers and cookies pass through, no further changes are required when you enable the New RUM Experience.

#### Built-in metrics

The New RUM Experience provides numerous builtâin metrics. Due to its different underlying data model, these are not direct equivalents of the [RUM Classic metrics](../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#applications "Explore the complete list of built-in Dynatrace metrics."). Still, many metrics have functional replacements, which are listed in [RUM metrics migration](../../../analyze-explore-automate/metrics/upgrade/rum-metric-migration.md "See how RUM Classic metrics map to their logical equivalents in Grail.").

## Related topics

* [Capture event and session properties for web frontends](web-frontends/additional-configuration/event-and-session-properties.md "Learn how to capture event and session properties for web frontends.")
* [Capture event and session properties for mobile frontends](mobile-frontends/additional-configuration/event-and-session-properties.md "Learn how to capture event and session properties for mobile frontends.")
* [Firewall constraints for RUM](../web-applications/initial-setup/firewall-constraints-for-rum.md "Find out how to make sure that Real User Monitoring data passes through your firewall.")
* [RUM metrics migration](../../../analyze-explore-automate/metrics/upgrade/rum-metric-migration.md "See how RUM Classic metrics map to their logical equivalents in Grail.")