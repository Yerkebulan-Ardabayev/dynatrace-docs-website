---
title: Hosted self-monitoring environment
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring/hosted-self-monitoring
scraped: 2026-05-12T11:53:30.991163
---

# Hosted self-monitoring environment

# Hosted self-monitoring environment

* Published Nov 17, 2021

Each Dynatrace Managed cluster node is observed by Mission Control. Self-monitoring takes a significant role in Dynatrace pro-active support capabilities. You have control over where the self-monitoring data is stored and who has access it. All clusters have a [Local self-monitoring environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") with internal metrics. Additionally, a cluster node can be monitored by OneAgent reporting to Dynatrace or your own environment. This topic describes in detail the available self-monitoring options, configuration, and data exchange.

### Pro-active support with turnkey self-monitoring

Dynatrace Managed deployment includes Dynatrace OneAgent at each cluster node, which provides self-monitoring of cluster health. Monitoring is enabled in Full-Stack Monitoring mode.

With this capability, Dynatrace product experts can support you proactively so you can focus on monitoring your applications. Data is reported to Mission Control Support Services and stored in a self-monitoring cluster hosted by Dynatrace. Data is stored in a US region. Only Dynatrace privileged employees have access to the data.

### Premium self-monitoring environment with full access

To get detailed insights, control who has access to self-monitoring data, and set up additional alerting and dashboards, you can get premium self-monitoring.

Dynatrace offers the possibility to set up a premium self-monitoring environment on a Dynatrace SaaS cluster. This SaaS environment is hosted by Dynatrace, which monitors your Dynatrace Managed cluster. Data is reported to Mission Control Support Services and stored in a US region. Only Dynatrace privileged employees have access to the data. You will be given permission to access the environment and invite other users.

Get full access to self-monitoring data

The premium self-monitoring environment is only available and included in Enterprise Success and Support subscriptions. To learn more about setting up such an environment or subscribing to Enterprise Success and Support, please contact a Dynatrace product expert via live chat.

### Self-monitoring data exchange

On each new installation or upgrade of a Dynatrace Managed cluster node, Mission Control provides a self-monitoring OneAgent download URL. Installation sets up a pre-defined self-monitoring configuration, and data is reported to the configured environment. In addition to infrastructure and Dynatrace service metrics, the following is captured:

* User information such as IP address
* Geolocation of users
* Browser or device type
* User-action details within Dynatrace Managed such as clicks or page loads
* Dynatrace Managed processes logs

### Private self-monitoring environment

You can opt out at any time from sending self-monitoring data to Dynatrace. This setting varies depending on your licensing. If this setting is disabled and you want to adjust it - Please contact a Dynatrace product expert via live chat within your environment.

If you opt out from Dynatrace deployment health monitoring, we recommend that you set it up on your own in any other environment. You will not only gain additional visibility into your Dynatrace Managed deployment, but you will also help Dynatrace product experts troubleshoot your issues. You can also install OneAgents on your Cluster and Environment ActiveGates.

Private self-monitoring consumes your Dynatrace licenses

When you install OneAgents on your cluster nodes, they contribute to and consume your Dynatrace licenses like any other monitored hosts and applications.

Read [Private self-monitoring environment](/managed/managed-cluster/self-monitoring/private-self-monitoring "Learn how to set up and configure a private self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") to learn how to opt out and configure your self-monitoring environment.