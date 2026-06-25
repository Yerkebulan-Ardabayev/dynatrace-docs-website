---
title: Network availability monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/nam-for-managed
scraped: 2026-05-12T12:05:20.590724
---

# Network availability monitoring

# Network availability monitoring

* Updated on Aug 23, 2024

Dynatrace Managed version 1.296+ ActiveGate version 1.295+

Network availability monitoring (NAM) allows you to monitor the availability of remote hosts or services over the network when an HTTP/HTTPS endpoint isn't available.

You can use NAM for infrastructure-related use cases or to deepen the root cause analysis for HTTP and browser monitors.

You can create synthetic network availability monitors of **ICMP**, **TCP**, or **DNS** type. To learn how to create NAM monitors, see [Create NAM monitors](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed "Learn how to set up and manage a NAM monitor to check the performance and availability of your site.").

## NAM types

There are three types of network availability monitors.

* ICMPâSends pings with a configurable number of packets or size to validate if there's a network connection to the host or device. It also checks the quality of that connection.
* TCPâEstablishes a TCP connection to a particular port. It validates if a port is open and if it accepts TCP connections. It also checks if a host is available through the network.
* DNSâValidates if a hostname can be resolved to an IP address.

To find out more about NAM types, see [available script configuration properties](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed#script-properties "Learn how to set up and manage a NAM monitor to check the performance and availability of your site.").

## Reporting

On-demand monitor execution

Monitor execution is possible via [API](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution "View the results of Synthetic monitor executions via the Synthetic v2 API."). The retention period for data from monitor execution is 6 hours.

To display an overview of your monitor, select **Network availability monitors** in **Synthetic Classic**. You'll see a list of all your NAM monitors, select the monitor name to open the overview (reporting) page.

The default reporting pages consist of:

* Metrics
* Request metrics
* TCP, ICMP or DNS metrics
* Monitored hosts (these are only visible if your monitor has been defined with a filter expression)
* Events

### Metrics

In the **Metrics** section, you can see

* a bar chart showing the number of monitor executions.
* a line chart showing the average monitor execution time.
* a line chart showing the average monitor availability.

For each of the above, you can select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") to **Show in data explorer**, **Create metric event**, **Pin to dashboard**.

### Request metrics

In the **Request metrics** section, you can see

* a bar chart showing the average number of requests executions.
* a line chart showing the average requests availability.

For each of the above, you can select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") to **Show in data explorer**, **Create metric event**, **Pin to dashboard**.

### TCP, ICMP and DNS metrics

In this section, you can see a chart showing one of the following metrics depending on your monitor type

* TCP - showing a chart for the connection time by request.
* ICMP - showing charts for success rate by request, packets sent by request, packets received by request and Round trip time by request.
* DNS - showing a chart for the resolution time.

For each of the above, you can select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") to **Show in data explorer**, **Create metric event**, **Pin to dashboard**.

### Monitored hosts

This section shows a list of your monitored hosts. You can sort them by name. Selecting a particular hostname will show a detailed view of it in **Hosts**.

### Events

This section shows a bar chart of events. If an outage is listed you need to select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row"), to see its details.

## Problems

Problems are created on the monitor level.

If your monitor

1. If there's a problem with your monitor you'll see **Problems** under the monitor name. Select **Problems**, then select **Go to Problems**.
2. In **Problems**, you'll see monitors affected by problems, where each problem consists of at least one of the follwoing

   * Affected stepsâExpand the **Step Id** to see at least one of the following details request id, request type, failure reason and status message.
   * Affected requestsâExpand the **Request target** you'll see request target address, request id, request type and failure reasons.
   * Affected locations.
   * Date of first failed execution.

## Limitations

There are certain limitations when using network availability monitors. You can find out more about them below.

### Number of requests

The maximum number of network activities executed per network availability monitor is 1,000. Network activity is a single DNS request, single TCP request, or single ICMP packet. Dynatrace may use multiple packets within a single ICMP request, if configured.

If a monitor uses a [target filter](/managed/observe/digital-experience/synthetic-monitoring/network-availability-monitors/configure-nam-managed#target-filter-managed "Learn how to set up and manage a NAM monitor to check the performance and availability of your site."), it might not be possible to precisely predict the number of requests in advance of execution (for example, when monitoring an entire host group or a subnet with a wide IP range). In such cases, the limit is applied when the target filter is resolved before the monitor's execution into the actual list of addresses.

The number of requests depends on the number of hosts matching the filter. For example, when monitoring an entire host group or **filtering the monitored hosts** using a subnet with a wide IP range.

### Number of monitors

You can have up to 5,000 NAM monitors per environment. Other types of monitors don't contribute to this limit.

### Deployment type

Network availability monitors are supported only on [private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

Containerized locations

Network availability monitors are supported on [containerized](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations#nam-monitors-on-containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.") Synthetic-enabled ActiveGate deployments, but additional permissions are required for ICMP tests.

To enable ICMP request type for NAM execution

1. In **Settings**, select and expand **Web and mobile monitoring**.
2. In the **Web and mobile monitoring** section, select **Private Synthetic Locations**.
3. Select **Add Kubernetes location**.
4. Configure your location and make sure to turn on **Enable ICMP request type for Network Availability Monitors execution**.

ICMP monitors use the `ping` executable, which requires the `CAP_NET_RAW` capability set for the container executing the requests (`synthetic-vuc`). Additionally, the `allowPrivilegeEscalation` property of `securityContext` for this container has to be set to `true`, because the process that launches the `ping` executable doesn't have the required privileges set by default.

The entire `securityContext` for the `synthetic-vuc` container with enabled network availability monitors should look as follows.

```
securityContext:



readOnlyRootFilesystem: true



privileged: false



allowPrivilegeEscalation: true



runAsNonRoot: true



capabilities:



drop: ["all"]



add: ["NET_RAW"]
```