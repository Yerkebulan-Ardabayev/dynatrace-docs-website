---
title: Create a NAM monitor
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-a-nam-monitor-synthetic-app
scraped: 2026-02-16T21:20:18.956706
---

# Create a NAM monitor

# Create a NAM monitor

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Dec 05, 2025

With network availability monitors (NAM), you can check the availability of your hosts, devices, and services.

There are three types of NAM monitors: ICMP, TCP, and DNS. To learn more about them, see [NAM types](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring#NAM-types "ICMP, TCP, and DNS synthetic monitors").
You can create NAM monitors in [![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") Synthetic](#monitor-configuration) in latest Dynatrace or through [API](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-api "Learn how to set up a NAM monitor to check the performance and availability of your site.").

## NAM setup

With NAM monitors, you can include more than one step.

* Each step can contain one or multiple requests.
* Like for HTTP and browser monitors, steps are executed sequentially.
* Unlike for HTTP and browser monitors, NAM monitors can contain multiple requests within a single step. All requests assigned to a particular step are executed in parallel. If one request fails, it doesn't affect the execution of other requests within that step.
* A step is skipped if nothing matches its definition in a monitor configuration. For example, when a tag is specified in the [target filters](#target-filter) list but nothing matches the tag.
* Concept of requests executed in parallel exists for NAM monitors only

For example, if you want to monitor a group of 4 hosts with an ICMP test, you want to apply the same conditions (such as frequency, location executing test, and number of packets) for each host from your group.

NAM offers you the possibility of addressing this in multiple ways:

* You can define 4 separate tests, one per host. The benefit of this approach is that Dynatrace triggers a separate problem for each host and you can assign separate notifications for each one. You can also adjust test parameters for each host separately.
* You can define a single test with 4 requests (within 1 step). The same ICMP checks are executed, but there will be differences in reporting and alerting. The number or percentage of hosts that are down is reported with the Requests Success rate metric. You can configure a customized threshold for failing the whole monitor. For example, if it's OK that 1 out of 4 hosts is down, because of rolling out an update, you can define it on the `>=75%` level. There's always a single problem generated for a monitor, yet still, it contains detailed info about hosts that don't respond. Another benefit of this approach is easier maintenance (adjusting single setting for all 4 hosts).

  Finally, filters offer defining tests against dynamically changing structure, for example if you want to define ICMP tests against a given host group, you don't need to adjust the NAM monitor test after the host group configuration change.

You need to define constraints for each monitor. Constraints are conditions that need to be met to consider the monitorâs execution successful. It is obligatory to define the **Success rate** constraint. See [step-level constraints](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#step-level-constraints "Learn how to set up a NAM monitor to check the performance and availability of your site.") to learn more.

## Create a NAM monitor

To create a NAM monitor in latest Dynatrace

1. Go to ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** and select **Create monitor**.
2. Follow the on-screen steps as outlined in the sections below.

### Select type

The **Create synthetic monitor** page shows the types of synthetic monitor you can create.

Select **Network monitor (NAM)** to get started.

### General

* Required **Name this monitor**âThe name of the monitor as it will be displayed in the web UI (up to 500 characters).
* Required **Select a protocol**âChoose the monitor type: `DNS`, `ICMP`, or `TCP`.
* Optional **Set a description**âDescribe your monitor.
* Optional **Add tags to this monitor**âTo manually create a new tag, select **Add tag**, type the key, optionally provide a value, and select **Add**.

After you specify the general settings, select **Continue**.

### Requests

The **Requests** section has two editing modes. You can switch back and forth between these modes.

* default **Visual**âto view and configure NAM requests through web UI settings.
* **Script**âto view and edit request settings as JSON. The script you provide also serves as payload for API requests.

Settings per request (you can add multiple requests) are:

* Required **Request name**âThe name of the request.
* Required **List of targets** or **Filter expression**

  + You can provide targets for requests as an explicit list, or filter monitored hosts using a filter expression.

    - If you want to provide targets as IP or domain names, use **List of targets** to specify a comma-separated list of targets. Use this to monitor single or multiple hosts, devices, or services.
    - If you want to select some of the monitored hosts or custom devices, use **Filter expression** to specify a filter expression. This allows you to monitor a group of hosts or custom devices that meet the filter criteria. To learn more about available filters, see [target filter](#target-filter).

    You can combine both the **List of targets** and the **Filter expression** in a single monitor step. When used together, the monitor step will include the combined set of targets from both fields.
* Required **Execution attributes**âExecution attributes are essentially key/value pairs that are associated with your request. Define **Request timeout**, **Number of packets**, **Data length**, **Time to live**, **Timeout to reply**, you can also turn on or turn off **Do not fragment data**. Execution attributes are available for ICMP only.
* Required **Constraints**âConstraints are conditions that need to be met to consider monitorâs execution successful. You need to define **Constraint type**, **Operator** and **value**.

If you want to create another request, select **Add next request** and specify the above for the next request.

Use **Duplicate** ![Duplicate](https://dt-cdn.net/images/dashboards-app-tile-duplicate-f0d63fb901.svg "Duplicate") to duplicate a request and then edit it from that point instead of starting from scratch each time you add a request.

After you specify all requests, select **Continue**.

### Frequency and locations

In the **Frequency and locations** section, specify the frequency and locations.

* Required **Select frequency**âYou can choose a frequency (every `1 min`, `2 min`, `5 min`, `10 min`, `15 min`, `30 min`, or `1 h`) or select `On demand only` for manual execution.
* Required **n selected locations**âSpecify one or more locations.

After you specify the frequency and locations, select **Continue**.

### Outage and Performance

In **Outage handling**, you can enable and configure the following settings related to problem and alert generation:

* Optional "Generate a problem and send an alert when the monitor is unavailable at all configured locations (global outage)."
* Optional "Generate a problem and send an alert when the monitor is unavailable only when at least two locations are assigned." Note that this option is only possible if you selected two or more locations.
* Optional "Generate a problem and send an alert on performance threshold violations."

After you specify the outage and performance settings, select **Continue**.

### Summary

In the **Summary** section, verify your settings.

After you review the summary, select **Save** to create your monitor or **Back** to go back and adjust your monitor settings.

## Target filter

Target filter gives an option to filter **hosts monitored by Dynatrace** or **custom devices having IP addresses**. With this filter, you can select those two types of targets based on:

* type (`type`)
* tags (`tag`)
* host ID (`hostId`) (deprecated, works for hosts only, use entity ID instead)
* entity ID (`entityId`)
* host groups (`hostGroup`)
* management zones (`managementZone`)
* IP mask (`ipMask`)
* IP range (`ipRange`)
* process group instance (`processGroupInstance`)
* network interfaces of particular custom device (`interfacesOf`)
* extension name (`extensionName`)

IP range and IP mask are filters for hosts or devices known for the Dynatrace server, not an option to scan the network.

### Syntax

* Logical operators: `AND` and `OR` (case insensitive)
* Parentheses
* Expression operators: `==` and `!=`
* Tag names and values
* Negation ("not"): `!=`.
* Wildcard: `*` (selects all hosts monitored by Dynatrace)

### Examples

* `tag == tagname or hostGroup == group1`
* `(tag == tagname1:tagvalue1 or tag == tagname1:tagvalue2) and (hostGroup == group1 or managementZone == zone1)`
* `tag != tagname1 and tag != tagname2:tagvalue`
* `tag == tagname:tagvalue and (managementZone == zone1 or managementZone == zone2)`
* `tag == "[tagwithbrackets and spaces]":"value, with, commas, and, spaces"`
* `ipMask == 127.0.0.1/24`
* `hostId == HOST-000123`
* `type == CUSTOM_DEVICE and ipMask == 172.17.0.2/24`
* `entityId == HOST-045BFCDA3F507D30 or entityId == CUSTOM_DEVICE-13081D4B74B3E2C8`
* `type == HOST and processGroupInstance == PROCESS_GROUP_INSTANCE-07611353BB98908C`
* `type == CUSTOM_DEVICE and interfacesOf == CUSTOM_DEVICE-E1A88946BF04D5E7`
* `type == CUSTOM_DEVICE and extensionName == "Docker devices"`

## Performance thresholds

The performance threshold metric is compared to metric calculated for each request within monitor/step. For example, if TCP port check monitor, tests on the same host port `80` and `443` separately, Dynatrace compares threshold TCP connection establishment time twice, once for port `80` and once for port `443`.

There are three performance metrics for three types of NAM monitors:

* RTT for ICMP
* TCP connection establishment time for TCP
* DNS resolution time for DNS

Violating defined performance triggers a Problem (Slowdown).

Similarly to availability problems:

* Problems are opened per monitor
* Contains information about all requests responsible for problem

You can configure the way Dynatrace aggregates results for each packet for ICMP requests with single execution. Dynatrace supports AVG, MAX and MIN with `AVG` as the default method.

### Define thresholds

You can define performance thresholds when configuring the request for your synthetic monitor. The defined performance threshold is the same for all requests within a single step. In cases, where there's a need to build a multi-step NAM monitor, it's possible to define various thresholds for each step.

To define thresholds

1. Follow the steps described in [Create a NAM monitor](#monitor-configuration) section.
2. In the **Requests** step, scroll down the page and see **Performance thresholds alerting** section.
3. Select **Generate a problem and send an alert on performance threshold violations.** check box.
4. Turn on **Advanced performance thresholds settings** toggle.

   In this section you can set the **Number of request executions in analyzed sliding window** and the **Number of violating request executions in analyzed sliding window**. For de-alerting samples we require `n` most recent non-violating request executions.

### Violation reporting

Red color annotation over performance charts indicates the period of time during which the performance threshold is raised. Additionally, a threshold is drawn on the performance chart, and you can examine which requests are above the threshold.

You may narrow down the time range only to that for which the problem was active using zoom functionality.