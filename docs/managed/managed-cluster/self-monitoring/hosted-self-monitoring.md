---
title: Hosted self-monitoring
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring/hosted-self-monitoring
---

# Hosted self-monitoring

# Hosted self-monitoring

* Explanation
* 1-min read
* Updated on Jun 11, 2026

Mission Control (MC) observes each Managed Cluster node, and this self-monitoring underpins Dynatrace proactive support. You control where the self-monitoring data resides and who can access it. All Managed Clusters have a [local self-monitoring environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn about the local self-monitoring environment that collects internal Dynatrace Managed Cluster health metrics and stores all data exclusively on-premises.") with internal metrics. Additionally, OneAgent can monitor a Managed Cluster node and report to Dynatrace or to your own environment.

The premium self-monitoring environment is only available and included in **Enterprise Success and Support** subscriptions.

## Proactive support with turnkey self-monitoring

Dynatrace Managed deployment includes Dynatrace OneAgent at each Managed Cluster node, which provides self-monitoring of Managed Cluster health. OneAgent runs in Full-Stack Monitoring mode.

With this capability, Dynatrace product experts provide proactive support, so you can focus on monitoring your applications. MC Support Services receives the data and stores it in a self-monitoring environment hosted on a Dynatrace SaaS cluster in the United States region. Only privileged Dynatrace employees have access to the data.

## Self-monitoring data exchange

On each new installation or upgrade of a Dynatrace Managed Cluster node, MC provides a self-monitoring OneAgent download address. Installation sets up a predefined self-monitoring configuration, and OneAgent reports data to the configured environment. Beyond infrastructure and Dynatrace service metrics, OneAgent also captures the following:

* User information such as IP address.
* Geolocation of users.
* Browser or device type.
* User-action details within Dynatrace Managed such as clicks or page loads.
* Dynatrace Managed process logs.