---
title: Analyze processes
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/monitoring/analyze-processes
scraped: 2026-05-12T11:37:53.360299
---

# Analyze processes

# Analyze processes

* How-to guide
* 6-min read
* Updated on Jul 30, 2024

From any **Host** page you can view a list of the processes that contribute to each host health metric (for example, **Memory** in the image below).

![Host with consuming processes](https://dt-cdn.net/images/processes-new-810-08dd1cb78f.png)

Host with consuming processes

You can click the **Consuming processes** button to view the list of the processes that contributed to the selected health metric.

![Processes table](https://dt-cdn.net/images/processes-new-2-1173-baad2315da.png)

Processes table

Once you've displayed the contributing processes list, click any process to explore that process in detail on a dedicated **Process** page. On each process page you'll find process-specific statistics related to CPU consumption, memory consumption, network utilization (see image below), and other [infrastructure measurements](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace."). You'll also find details regarding related events, problems, and dependencies.

![Host detail - process details](https://dt-cdn.net/images/hostprocesses2-1225-b7b9608767.png)

Host detail - process details

## Vulnerabilities

The **Vulnerabilities** section on the details page of a process shows the five most severe [third-party vulnerabilities](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.") and [code-level vulnerabilities](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities "Monitor the code-level vulnerabilities in your environment.") related to this process.

To view this section, [activate and enable Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.").

If you're missing the [security permissions](/managed/secure/application-security#permissions "Access the Dynatrace Application Security functionalities.") for the management zone where the process is included, this section is not displayed.

* Select a vulnerability to view the details and understand the severity and impact of a vulnerability within your environment.
* For a complete list of the detected vulnerabilities affecting this process, select **Show all third-party vulnerabilities**/**Show all code-level vulnerabilities**.

Example third-party vulnerabilities:

![Process overview: TPV](https://dt-cdn.net/images/process-tpv-775-92fe606d07.png)

Process overview: TPV

Example code-level vulnerabilities:

![Process overview: CLV](https://dt-cdn.net/images/process-clv-774-d460fb39ba.png)

Process overview: CLV

## Process availability

Apart from recording [event-types](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them."), like process shutdowns and restarts, Dynatrace also shows [process crashes](/managed/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes."). This is especially important for service availability monitoring. Services inherit their availability from the processes they run on. Dynatrace considers a service to be offline when the entire process group it runs on is unavailable. This can occur when a process is shutdown or crashes (see image below).

![Process crashed](https://dt-cdn.net/images/process-crashed-877-1cbf72dbbc.png)

Process crashed

Dynatrace allows you to distinguish between services that are available, but receive no traffic, and services that are unavailable because the underlying processes have stopped or crashed. In the case of a crashed process, Dynatrace monitors the crash and informs you about the impact of the crash on your services and applications (see image below).

![Root cause crashed process](https://dt-cdn.net/images/root-cause-crashed-process-634-b3ccae5e57.png)

Root cause crashed process

## Process group instance availability

OneAgent version 1.291+

You can track the availability of process group instances by using the `builtin:pgi.availability.state` (`dt.process.availability` on Grail) metric.

The state is indicated by the one of these values:

* **Available**âThe process group instance is available and reported.
* **Unavailable**âThe process group instance is unavailable and not reported.
* **Unimportant**âThe process group instance is available but not reported to the cluster because it became unimportant. For more details, see [Which are the most important processes?](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.").

The metric values are sampled by OneAgent

* If the state is `available`, every minute
* If the state is `unavailable` or `unimportant`, once. After the sample containing this state is sent, OneAgent stops sending the metric for the process group instance.