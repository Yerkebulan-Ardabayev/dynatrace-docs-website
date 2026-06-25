---
title: Process group availability monitoring and alerting
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/monitoring/process-group-availability-monitoring-and-alerting
scraped: 2026-05-12T11:37:55.200409
---

# Process group availability monitoring and alerting

# Process group availability monitoring and alerting

* How-to guide
* Published May 12, 2018

If you have critically-important processes that you want to monitor for availability, or if you want to ensure that the number of processes of a cluster never drops below a certain limit, Dynatrace allows you to select the availability alerting strategy that best meets your needs. This means that you can configure Dynatrace to proactively alert you if any process or number of processes within a specific [process group](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") goes offline or crashes. Alerts include links to related Dynatrace [problem pages](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI."), making it easy for you to access all the details related to an unavailable process so that you can quickly resolve the issue.

## Enable process-group availability monitoring

Instead of reporting process availability events of service-hosting process groups by default, you have the option to receive alerts when a process becomes unavailable or when minimum threshold isn't met.

1. Go to **Hosts**.
2. Select the host youâre interested in.
3. Scroll down and select **Consuming processes**.
4. From the **Process** list, select the process group (or individual process) youâre interested in.
5. From the browse menu (**â¦**), select **Settings** to access **Process group settings**.
6. Select **Availability monitoring**.
7. Alerting is disabled by default. **Enable process group availability monitoring** must be toggled on in order to enable alerting.

## When to activate this setting

Once the **Enable process group availability monitoring** is toggled on, you have two options.

Receive alerts only for the most important process-group availability issues

This option triggers an availability event when any process in the selected process group becomes unavailable.

![Pg settings](https://dt-cdn.net/images/2021-03-12-11-53-24-1127-df5e27dbf8.png)

Pg settings

Raise an alert when any process in a selected process group becomes unavailable

This option triggers an availability event when a user-defined threshold for the minimum number of running processes within a selected process group isnât met.

In the example below, the required minimum number of running processes is set to `2`. This means that whenever this process group has fewer than two running processes, Dynatrace will trigger an availability-level event for the process group.

![Min thresh](https://dt-cdn.net/images/2021-03-12-11-55-20-1090-5020e55d24.png)

Min thresh