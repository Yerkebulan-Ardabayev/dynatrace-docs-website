---
title: General limitations for RUM mobile applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/general-limitations
scraped: 2026-05-12T11:33:20.884124
---

# General limitations for RUM mobile applications

# General limitations for RUM mobile applications

* Troubleshooting
* 1-min read
* Updated on Jan 13, 2026

This page outlines important limitations related to mobile application monitoring.

## Event limitations

These restrictions do not apply to monitoring data captured within the web views of hybrid apps.

Be aware of the following limitations:

* **Events per minute**: There is a restriction on the number of events that can be generated within a single minute. Exceeding this limit may result in events being dropped or not processed. The default limit is 1,000 events per minute.
* **Children per action**: Each action can only contain a limited number of child actions. If this limit is exceeded, additional child actions may not be recorded. The default limit is 200.