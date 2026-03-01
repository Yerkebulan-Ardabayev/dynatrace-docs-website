---
title: Host availability
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability
scraped: 2026-03-01T21:18:20.039426
---

# Host availability

# Host availability

* How-to guide
* 5-min read
* Updated on Nov 26, 2024

You can track host availability on the overview page for a selected host. The **Host availability** tile displays the percentage of the selected time range in which the host was online and responsive to requests.

## Check host availability state

To check a host's availability state

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** to list all the machines (physical and virtual) in your environment that have OneAgent installed.
2. Select a host to go to the host overview page, where you can view host details, including all available metrics for the host.
3. On the notifications bar, **Availability** indicates the percentage of time that the host was online and responsive to requests. Dynatrace detects and shows operating system shutdowns (including reboots) and periods when a host is offline (for example, if the host is down unexpectedly).

   When the connection to the host is lost, OneAgent caches all the collected data in a 55-minute buffer. Once the connection is reestablished, the data for the host is collected from the buffer's content and updated.

   In this example, the notifications bar displays an availability rate of 99.74% for the selected host during the selected timeframe.

   ![Host availability on the notifications bar](https://dt-cdn.net/images/notifications-bar-availability-854-e927dcebcb.png)
4. Select **Availability** on the notifications bar to display the **Host availability** panel, which charts host availability over time.

   In this example, the legend indicates the three different host availability states that occurred during the selected timeframe.

   ![Host page detail - online availability](https://dt-cdn.net/images/image-3-757-d2642a2b5d.png)

## Host availability states

### Check OneAgent monitoring settings per host

To check or change the monitoring settings per host:

1. Go to **Settings** > **Monitoring** > **Monitoring overview**.
2. Select the **Hosts** tab.
3. Find the host and check the **Summary** column to see if it's being monitored.
4. Select the edit button ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") and check the settings in the **Monitoring** tab.

## Host availability events

When the availability state changes (for example, when the host is shut down), OneAgent sends availability events. To check all events for a specific host, go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**, select the desired host, and then go to the **Events** tile.

The event types are:

* Reboot graceful
* Reboot ungraceful
* Graceful shutdown

  + K8s node termination (a subelement of Graceful shutdown, specific to Kubernetes environments)

### Reboot graceful/ungraceful

After a system restart, OneAgent checks system-specific log files or events to determine if the host was shut down gracefully or ungracefully.

* Graceful reboot indicates that the host is rebooted following an expected operating system shutdown.

  ![Host availability event - graceful reboot](https://dt-cdn.net/images/host-availability-graceful-reboot-1027-9c5a256356.png)
* Ungraceful reboot indicates that the host is rebooted following an unexpected operating system shutdown caused by events, such as power loss or a system crash.

  ![Host availability event - ungraceful reboot](https://dt-cdn.net/images/host-availability-ungraceful-reboot-1007-a3958d05f4.png)

The reboot graceful and reboot ungraceful events are supported on Linux, AIX, and Windows operating systems.

### Graceful shutdown

When the host is about to shut down, OneAgent sends the appropriate host shutdown event.

![Host availability event - graceful shutdown](https://dt-cdn.net/images/host-availability-graceful-shutdown-compact-1450-1488a61897.png)

The graceful shutdown event is supported on Linux, AIX, and Windows operating systems.

### K8s node termination

K8s node termination is supported on the Linux operating system. This event is generated on hosts where the Kubernetes engine is detected. OneAgent creates an inhibitor lock to get more time during shutdown.

Make sure OneAgent has sufficient rights to register the inhibitor lock.

If your Linux distribution experiences connections problems or the network manager is turned off faster than the event is sent, the shutdown event might not be sent on time.

![Host availability event - Kubernetes node shutdown](https://dt-cdn.net/images/host-availability-k8s-node-shutdown-969-3fd821c153.png)

## Maintenance windows

Maintenance windows are periods of time during which maintenance activities are scheduled to be performed in monitored environments. These maintenance windows can be used to prevent alerting, log file collection, system profiling, and other activities from taking place. For details, see [Maintenance windows](/docs/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.").

Maintenance windows are displayed as gray bars at the top of the **Host availability** and **Host performance** tiles on the host overview page.

![Availability tile maintenance window](https://dt-cdn.net/images/image-938-c6ad83866e.png)

![Host performance maintenance window](https://dt-cdn.net/images/image-1923-d376018fd7.png)