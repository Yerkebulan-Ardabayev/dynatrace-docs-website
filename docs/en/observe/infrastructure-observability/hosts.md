---
title: Hosts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts
scraped: 2026-02-06T16:29:11.779328
---

# Hosts

# Hosts

* Latest Dynatrace
* Overview
* 3-min read
* Published Sep 25, 2018

Host performance is tracked across multiple Dynatrace pages, beginning with high-level health metrics on dashboard tiles and extending down to dedicated pages for each of your hosts. Full-stack infrastructure monitoring begins automatically as soon as Dynatrace OneAgent starts operation and begins capturing performance and event-related information on your hosts.

Brief overview

### Host groups

With many Dynatrace-monitored environments growing larger and more complex all the time, often spanning different data centers and multiple applications, [host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") are increasingly important. Host groups enable you to configure hosts per group, roll out OneAgent versions selectively per group, and track service metrics differently depending on the platform they run on.

### Virtualization performance insights

Dynatrace tells you how the virtual machines in your environment affect the performance of your applications and services. Once you include virtualization in your Dynatrace performance monitoring, you gain insight into your complete infrastructure stack and its behavior.

### Tags in a host-based configuration file

Within dynamic or large environments, manual host tagging can be impractical. For dynamic deployments that include frequently changing host instances and names (for example, AWS or MS Azure), you can [use a dedicated configuration file to programmatically apply tags to your hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.").

### Custom host names

Dynatrace generally names the detected hosts in your environment based on their DNS names, exactly as they are detected by Dynatrace OneAgent. To improve readability, you may want to [create custom host names](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.") to display instead of the detected host names.

## Basic concepts

[![Infrastructure Monitoring](https://cdn.bfldr.com/B686QPH3/at/jftqtgccnb2wt3h4ngf6z/Infrastructure_Observability.svg?auto=webp&width=72&height=72 "Infrastructure Monitoring")

### Monitoring modes

Find out what's included and how to enable Infrastructure Monitoring and Discovery modes.](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.")[### How effective is infrastructure monitoring on its own?

Learn how monitoring only the infrastructure layer of your environment can lead to an incomplete picture of the health of your applications and customer experience.](/docs/observe/infrastructure-observability/hosts/monitoring-modes/how-effective-is-infrastructure-monitoring-on-its-own "Learn how monitoring only the infrastructure layer of your environment can lead to an incomplete picture of the health of your applications and customer experience.")

## Configuration

[### Host anomaly detection

Configure host anomaly detection, including problem and event thresholds.](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.")[### Define tags and metadata for hosts

Tag and set additional properties for a monitored host.](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")[### Exclude disks and network traffic from host monitoring

Exclude selected disks and network traffic from host monitoring.](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic "Learn how to exclude selected disks and network traffic from host monitoring.")[### Organize your environment using host groups

Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.")[### Set custom host names

Change a monitored host name.](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.")

## Monitoring

[### Host monitoring with Dynatrace

Monitor hosts with Dynatrace.](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.")[### OS services monitoring

Improve the visibility of your infrastructure by monitoring the availability of operating system services.](/docs/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.")[### Classic Windows services monitoring

Improve the visibility of your infrastructure by monitoring the availability of Windows services.](/docs/observe/infrastructure-observability/hosts/monitoring/windows-services "Learn how to improve the visibility of your infrastructure by monitoring the availability of Windows services.")[### Process availability

Monitor availability and performance of the key processes on your hosts.](/docs/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.")

## Diagnostics

[![OneAgent](https://cdn.bfldr.com/B686QPH3/at/g8mmkkpfmgwbxcjz54pvfsx/OneAgent.svg?auto=webp&width=72&height=72 "OneAgent")

### OneAgent diagnostics

Learn how to run OneAgent diagnostics.](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics")