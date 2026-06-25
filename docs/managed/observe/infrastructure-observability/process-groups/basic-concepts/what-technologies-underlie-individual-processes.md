---
title: What technologies underlie individual processes?
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes
scraped: 2026-05-12T11:37:47.698559
---

# What technologies underlie individual processes?

# What technologies underlie individual processes?

* Reference
* 1-min read
* Published Jul 19, 2017

More than simply knowing the types of processes in your environment (for example, Java or .NET), Dynatrace understands the technologies that underlie those processes. For example, Dynatrace understands when a Java process is comprised of a Tomcat or a Jettyâin many cases it even knows the versions of these technologies. This information available to you on each **Process** page.

With detailed analysis of the technologies and versions underlying specific processes, you'll no longer have to wonder where varying versions have been deployed. This is a vital first step in troubleshooting problems.

To view the technology properties underlying a process:

1. Go to **Hosts**.
2. Select that host that runs the process you're interested in.
3. From the **Processes** section on the **Host** page, select the process you're interested in.
4. On the **Process** page, expand the **Properties** pane near the top of the page.

The **Type** property indicates the main technology underlying a process. Ancillary technologies are provided in the **Technologies** property. In the **Technologies** property, you'll typically find additional details, like CLR or Java version, but you may also find details like SOLR or MongoDB-client version. See the examples below to better understand the types of information that Dynatrace can provide.

![Example 1](https://dt-cdn.net/images/2016-08-31-14-56-14-photos-822-1fdc8f7618.png)

Example 1

![Example 2](https://dt-cdn.net/images/2016-09-01-08-56-57-process-deve2e-ruxitlabs-com-deve2e-dynatrace-671-aa158da1b5.png)

Example 2

![Example 3](https://dt-cdn.net/images/2016-08-31-14-56-26-photos-824-77d5e9af35.png)

Example 3

![Example 4](https://dt-cdn.net/images/2016-08-31-14-56-41-photos-824-ccb8f73c23.png)

Example 4