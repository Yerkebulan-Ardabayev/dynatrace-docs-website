---
title: Network availability monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring
scraped: 2026-02-16T21:27:10.788972
---

# Network availability monitoring

# Network availability monitoring

* Explanation
* 4-min read
* Updated on Aug 08, 2024

Dynatrace version 1.296+ ActiveGate version 1.295+

Network availability monitoring (NAM) allows you to monitor the availability of remote hosts or services over the network when an HTTP/HTTPS endpoint isn't available.

You can use NAM for infrastructure-related use cases or to deepen the root cause analysis for [HTTP](/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic "Learn about HTTP monitors.") and [browser](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors "Learn about browser monitors.") monitors.

You can create synthetic network availability monitors of **ICMP**, **TCP**, or **DNS** [type](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring#nam-types "ICMP, TCP, and DNS synthetic monitors").

You can configure NAM monitors and access their performance results in [Synthetic](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.") in latest Dynatrace.
See [create a NAM monitor](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor "Learn how to set up a NAM monitor to check the performance and availability of your site.") to learn how to set up your monitor in [Synthetic](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.") or via [API](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-api "Learn how to set up a NAM monitor to check the performance and availability of your site.").

## NAM types

There are three types of network availability monitors.

* ICMPâSends pings with a configurable number of packets or size to validate if there's a network connection to the host or device. It also checks the quality of that connection.
* TCPâEstablishes a TCP connection to a particular port. It validates if a port is open and if it accepts TCP connections. It also checks if a host is available through the network.
* DNSâValidates if a hostname can be resolved to an IP address.

To find out more about NAM types, see [available script configuration properties](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#script-properties "Learn how to set up a NAM monitor to check the performance and availability of your site.").

## Problems

Problems are created on the monitor level.

To receive alerts when problems are generated

1. Edit the monitor.
2. Go to [Outage and Performance](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#monitor-configuration "Learn how to set up a NAM monitor to check the performance and availability of your site.").
3. Configure the problems and alerts you want to generate.

To analyze a problem

1. In the **Problems** section of the preview panel, select **Open in Problems app**.
2. In the **Problems app**, you'll see monitors affected by problems, where each problem consists of:

   * Affected stepsâExpand the **Step Id** to see at least one of the following details request id, request type, failure reason and status message.
   * Affected requestsâExpand the **Request target** you'll see request target address, request id, request type and failure reasons.
   * Affected locations.
   * Date of first failed execution.

## Limitations

There are certain limitations when using network availability monitors. You can find out more about them below.

### Number of requests

The maximum number of network activities executed per network availability monitor is 1,000. Network activity is a single DNS request, single TCP request, or single ICMP packet. Dynatrace may use multiple packets within a single ICMP request, if configured.

If a monitor uses a [target filter](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#target-filter "Learn how to set up a NAM monitor to check the performance and availability of your site."), it might not be possible to precisely predict the number of requests in advance of execution (for example, when monitoring an entire host group or a subnet with a wide IP range). In such cases, the limit is applied when the target filter is resolved before the monitor's execution into the actual list of addresses.

The number of requests depends on the number of hosts matching the filter. For example, when monitoring an entire host group or **filtering the monitored hosts** using a subnet with a wide IP range.

### Number of monitors

You can have up to 5,000 NAM monitors per environment. Other types of monitors don't contribute to this limit.

### Deployment type

Network availability monitors are supported only on [private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

Containerized locations

Network availability monitors are supported on [containerized](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations#nam-monitors-on-containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.") Synthetic-enabled ActiveGate deployments, but additional permissions are required for ICMP tests.

To enable ICMP request type for NAM execution

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Settings**.
2. In **Settings**, select and expand **Web and mobile monitoring**.
3. In the **Web and mobile monitoring** section, select **Private Synthetic Locations**.
4. Select **Add Kubernetes location**.
5. Configure your location and make sure to turn on **Enable ICMP request type for Network Availability Monitors execution**.

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

### Use of proxy

Network availability monitors do not support the use of [proxy servers](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#proxy-connection-scenarios "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring."). Ensure that your network configuration allows direct access to the monitored endpoints without routing through a proxy.