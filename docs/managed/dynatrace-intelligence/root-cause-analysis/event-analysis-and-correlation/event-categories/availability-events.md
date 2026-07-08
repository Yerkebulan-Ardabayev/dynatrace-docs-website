---
title: Availability events
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/availability-events
---

# Availability events

# Availability events

* Explanation
* 5-min read
* Updated on Jan 28, 2026

This page provides information about supported availability events and the logic behind raising them.

## Unexpected low traffic

`UNEXPECTED_LOW_LOAD`

Dynatrace collects a multidimensional baseline for application and user action traffic and therefore learns the typical traffic pattern of all your applications and user actions.

Abnormally low application traffic can indicate full application outages, so alerting on abnormally low application traffic is enabled by default.

Go to **Settings** > **Anomaly detection** > **Applications** to adapt the sensitivity of low-traffic alerting. When enabled, Dynatrace follows a time-interval comparison pattern (daily or weekly) in alerting on abnormal traffic situations. The actual monitored application traffic is compared with the previous interval and alerts if the comparison reports unusually low traffic.

A typical example of an unexpected low traffic event is shown below.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Service
* Application
* Mobile application

## Host or monitoring unavailable

`OSI_UNEXPECTEDLY_UNAVAILABLE`

This event is detected when a host is abruptly shut down or Dynatrace loses the network connection to the host’s OneAgent. If the operating system is shut down gracefully, Dynatrace won't open a problem. Dynatrace will show the host in an unavailable state.

Condition:

* Network connection to the monitored host is lost unexpectedly while OneAgent and host are still running. The connection must be lost for more than 5 minutes, before OneAgent starts sending signals again and cached metric data fills in the missing chart data.
* OneAgent isn't able to catch and send the regular operating system shutdown message.
* Decommissioning of virtual hosts (for example, in AWS auto-scaling groups) when the operating system isn't shut down and therefore Dynatrace detects this as a connection-lost event (event delayed up to 10 minutes after connection is lost).

Closing conditions:

* Event is resolved when the host is available again
* Timeout of event occurs after 12 hours.

An example host unavailable event is shown below.

## Process unavailable

`PROCESS_UNAVAILABLE`, `PROCESS_GROUP_LOW_INSTANCE_COUNT`

Dynatrace OneAgent automatically detects each running process on hosts and reports the availability state of all processes. Davis detects process and host related availability automatically, so the availability monitoring is disabled for process groups by default.

However, if a process group and its availability are of high importance you can enable availability monitoring on the process group level. You have two approaches to trigger an event on the process group level:

* If any process becomes unavailable. In that case an event is triggered immediately when any process of the group becomes unavailable for any reason.
* If number of available process is below the specified threshold. In that case you can manually specify the minimum acceptable number of process in the group. An event is triggered in number of active process is below the threshold for **2 consecutive minutes**.

If you intentionally shut down a process, an event will be triggered too, giving that condition is met. In that case just close the raised problem manually.

To configure process group availability monitoring, select **Edit** on the process group details page and select the **Availability monitoring** item.

Closing conditions:

* Event is resolved when the process is available again
* Timeout of event occurs after 5 days.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Process group (`PROCESS_GROUP_LOW_INSTANCE_COUNT`)
* Process group instance (`PROCESS_UNAVAILABLE`)

## Synthetic monitor global outage

`WEB_CHECK_GLOBAL_OUTAGE`

Synthetic monitors check your websites from multiple geographic regions on a regular schedule. Dynatrace raises a synthetic global outage event if your website stops responding from all configured geographic regions.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Synthetic monitor

## Synthetic monitor local outage

`WEB_CHECK_LOCAL_OUTAGE`

Synthetic monitors regularly check your websites from multiple geographic regions. Dynatrace raises a synthetic local outage event in case that your Website is not responding from at least one configured geographic region. Once your Web application is not responding from all configured regions, a problem will be elevated to report a global outage.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Synthetic monitor

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* External synthetic monitor

## Availability log pattern found

`HOST_LOG_AVAILABILITY`

Dynatrace Log Monitoring allows you to define log patterns that indicate availability related problems on a host. All detected pattern appearances are registered and if the number of detected pattern exceeds your critical threshold an availability log pattern event is raised.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Host

## Availability log pattern found

`PROCESS_LOG_AVAILABILITY`

Dynatrace Log Monitoring allows you to define log pattern that indicate availability related problems on a process level. Every appearance of a configured pattern is counted over time and if the number of detected pattern exceeds your critical threshold an availability log pattern event is raised.

### Applicable Dynatrace entities

The following Dynatrace entities apply to this event:

* Process group instance

## Custom availability event

`AVAILABILITY_EVENT`

This generic availability event can be used by monitoring plugins or through the [Dynatrace API](/managed/dynatrace-api/environment-api/events-v1 "Find out what you can do with the Dynatrace Events API.") to raise a customized availability event with a user-defined title (for example, `Batch process schedule outage`).

### Applicable Dynatrace entities

All Dynatrace entities apply to this event.