---
title: Relationship between the New RUM Experience and RUM Classic
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/relationship-to-rum-classic
scraped: 2026-02-23T21:26:20.516474
---

# Relationship between the New RUM Experience and RUM Classic

# Relationship between the New RUM Experience and RUM Classic

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 23, 2026

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

At this point, the New RUM Experience relies only on the HTTP headers and cookies already covered by the [firewall constraints for RUM Classic](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall."). If your firewalls and other infrastructure components are already configured to let these headers and cookies pass through, no further changes are required when you enable the New RUM Experience.

## Related topics

* [Capture event and session properties for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for web frontends.")
* [Capture event and session properties for mobile frontends](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for mobile frontends.")
* [Firewall constraints for RUM](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall.")