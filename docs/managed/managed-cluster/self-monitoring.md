---
title: Self-monitoring
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring
---

# Self-monitoring

# Self-monitoring

* 1-min read
* Updated on Jun 11, 2026

Dynatrace Managed tracks the health and performance of your Managed Cluster through self-monitoring, collecting data from all deployment components—OneAgents, ActiveGates (including Extensions), and Managed Cluster nodes. Depending on your configuration, it stores data locally, sends it to Mission Control (MC), or forwards it to a dedicated self-monitoring environment.

[### Local self-monitoring

Each Managed Cluster includes a dedicated local self-monitoring environment that keeps all data on-premises.](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn about the local self-monitoring environment that collects internal Dynatrace Managed Cluster health metrics and stores all data exclusively on-premises.")[### Hosted self-monitoring

Set up a premium self-monitoring environment on a Dynatrace SaaS cluster to get detailed insights with personalized proactive support (Enterprise Success and Support only).](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Understand how Mission Control uses OneAgent to monitor Dynatrace Managed Cluster health and how Mission Control collects and stores self-monitoring data.")[### Private self-monitoring

Install OneAgent on your nodes and report to an environment you select for full control over data residency and access.](/managed/managed-cluster/self-monitoring/private-self-monitoring "Learn how to set up and configure a private self-monitoring environment to gain additional insights into your Dynatrace Managed Cluster health.")