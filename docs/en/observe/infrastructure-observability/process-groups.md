---
title: Process groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups
scraped: 2026-02-16T21:22:28.106087
---

# Process groups

# Process groups

* Explanation
* 3-min read
* Published Jan 08, 2019

Dynatrace automatically merges related processes into process groups. A âprocess groupâ is a logical cluster of processes that belong to the same application or deployment unit and perform the same function across multiple hosts. Process groups are key building blocks of most modern web-based applications.

Show moreâ¦

Dynatrace automatically [detects application types](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process") such as Tomcat, JBoss, Apache HTTP Server, MongoDB, and many others technologies. To create process groups, Dynatrace uses specific process properties. For Tomcat, Dynatrace uses `CATALINA_HOME` and `CATALINA_BASE` to distinguish between different Tomcat clusters. For JBoss, Dynatrace uses `JBOSS_HOME` and the JBoss cluster configuration. For generic Java processes, Dynatrace uses the JAR file or the main class used to start the process. There are also many specialized detection mechanisms. For example, Dynatrace can detect:

* IBM WebSphere clusters and domains
* Oracle WebLogic clusters and domains
* Cassandra clusters
* Tibco BusinessWorks engines
* Kubernetes apps
* OpenShift apps
* Cloud Foundry apps
* Azure Web Apps
* And moreâ¦

On each process overview page you'll find the properties if you expand **Properties and tags**.

### What does this mean for services?

Process groups are the basis for service detection, because each process group is considered to be a logical cluster or single deployment. When Dynatrace detects the "same" service in separate process groups, it treats them as separate services (for example, one process might be used in staging and the other in production).

If you instruct Dynatrace to merge two separate process groups into a single process group, this will result in the services running on those processes to also be merged.

### Customize process groups

To serve your particular needs when monitoring your processes, Dynatrace allows you to:

* [Customize the name of process groups](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming").
* [Adapt the composition of default process groups](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").
* [Create new process groups in cases where the technology of processes isn't recognized by Dynatrace](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Basic concepts

[![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies")

### What technologies underlie individual processes?

Technologies and versions behind a process.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process")[### Which are the most important processes?

Display the most important processes for monitoring and process grouping.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.")

## Configuration

[### Cloud application and workload detection

Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.](/docs/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection "Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.")[### Define your own process group metadata

Configure your own process-related metadata based on the unique needs of your organization or environment.](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")[### Process group detection

Customize process-group detection.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")[### Process deep monitoring

Customize process-group monitoring.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring")[### Process group naming

Customize process-group naming.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming")

## Monitoring

[### Analyze process responsiveness

Leverage responsiveness to assess process performance.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-process-responsiveness "Use responsiveness to assess process performance.")[### Analyze processes

Analyze processes, including information on process metrics, vulnerabilities, and availability.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-processes "The Dynatrace approach to process monitoring and process grouping")[### Monitor process-specific network connections

Analyze process-specific network connections.](/docs/observe/infrastructure-observability/process-groups/monitoring/monitor-process-specific-network-connections "Analyze process-specific network connections.")[### Overview of all technologies running in your environment

Get a performance summary of all the technologies in your environment.](/docs/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.")[### Process group availability monitoring and alerting

Enable process-group availability monitoring to get alerts if processes go offline or crash.](/docs/observe/infrastructure-observability/process-groups/monitoring/process-group-availability-monitoring-and-alerting "Enable process-group availability monitoring to get alerts if processes go offline or crash.")