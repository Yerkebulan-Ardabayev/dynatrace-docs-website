---
title: Self-monitoring
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring
scraped: 2026-05-12T11:11:13.823617
---

# Self-monitoring

# Self-monitoring

* Published Nov 17, 2021

To provide the highest quality pro-active support, we collect health statistics, performance metrics, and service utilization from all deployment components operated by Dynatrace ManagedâOneAgents, ActiveGates (including Extensions), and cluster nodes. Dynatrace Managed provides turnkey multi-level insights into the cluster's deployment health and cluster's performance through self-monitoring. The self-monitoring data is:

* Stored as self-monitoring metrics in all of your monitoring environments.
* Stored in a dedicated local self-monitoring environment.
* Reported to Dynatrace Mission Control to allow Dynatrace to observe and improve the product.
* Stored remotely on a dedicated Dynatrace premium self-monitoring environment (only for Enterprise Success and Support).

You can opt out anytime from sending self-monitoring data to Dynatrace. This setting varies depending on your licensing. If this setting is disabled and you want to adjust it, contact a Dynatrace product expert via live chat. Configuration and data exchange is described in details in [Hosted self-monitoring environment](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Learn how to use hosted self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.").

The following options are available for you to access self-monitoring data of a Dynatrace Managed cluster:

### Local self-monitoring

Each Dynatrace Managed cluster includes a dedicated local self-monitoring environment that collects internal deployment self-monitoring metrics. This environment is a fully working and accessible Dynatrace environment. It includes all the self-monitoring metrics collected and aggregated from the other environments on your Dynatrace Managed cluster. Data is exclusively stored on premises on your cluster.

With this type of self monitoring, you get high-level health and performance metrics, turnkey, and full control over data residency and access. See [Local self-monitoring environment](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") for details.

### Hosted self-monitoring

Dynatrace offers the possibility to set up a premium self-monitoring environment on a Dynatrace SaaS cluster. This SaaS environment is hosted by Dynatrace and then monitors your Dynatrace Managed cluster.

Support

Hosted self-monitoring is available only for Enterprise Success and Support customers.

With this type of self-monitoring, you get detailed insights and metrics, access control, data in the Dynatrace environment, and the highest personalized pro-active support. See [Hosted self-monitoring environment](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Learn how to use hosted self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") for details.

### Private self-monitoring

If you opt out from Dynatrace deployment health monitoring, you can install OneAgent on your cluster nodes on your own. They will report to the environment you select on the same or another cluster. This option will consume your Dynatrace licenses accordingly.

With this type of self-monitoring, you get detailed insights and metrics and full control over data residency and access. However, there is limited pro-active support and it is additionally licensed. See [Private self-monitoring environment](/managed/managed-cluster/self-monitoring/private-self-monitoring "Learn how to set up and configure a private self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") for details.