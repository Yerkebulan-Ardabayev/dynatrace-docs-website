---
title: Managed deployments
source: https://docs.dynatrace.com/managed/managed-cluster/basics/managed-deployments
---

# Managed deployments

# Managed deployments

* Explanation
* 5-min read
* Updated on May 08, 2026

Dynatrace Managed deployments can evolve from a basic internal setup to a fully integrated enterprise architecture with high availability and automatic recovery. Each stage builds on the previous one, adding components as your requirements grow. Each diagram shows the components involved and the required communication ports at that stage. Arrow direction indicates which component initiates the connection.

For a collective diagram showing all possible connections and ports, see [Supported connectivity schemes for ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").

## Stage 1: Basic internal setup

Installing Dynatrace Managed with multiple Managed Cluster nodes forms the foundation for all further deployment stages. Without further configuration, a Managed Cluster is only accessible internally and exposes port 443 for the REST API, OneAgent traffic, and web UI access ([Cluster Management Console](/managed/managed-cluster/basics/cluster-management-console "Manage your Managed Cluster infrastructure, environments, users, settings, and licensing from the Cluster Management Console.") and [monitoring environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.")). By default, remote access to [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") is enabled to provide you with proactive support. Each communication channel is secured with TLS.

![Stage 1: Basic internal Dynatrace Managed deployment with Managed Cluster nodes and Mission Control](https://dt-cdn.net/images/con-man-basic-001-1200-d2345ce291.png)

Stage 1: Basic internal Dynatrace Managed deployment with Managed Cluster nodes and Mission Control

## Stage 2: External traffic and Digital Experience Monitoring services

Extending the deployment beyond the internal network allows you to receive data from external sources, such as OneAgents, Environment ActiveGates, or Digital Experience Monitoring (DEM) services. This stage adds an Environment ActiveGate to better support multiple local OneAgents.

The DEM services may include:

* [Synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Agentless Real User Monitoring](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.")
* [Mobile Real User Monitoring](/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring "Learn how to set up real user monitoring for your mobile apps and use with Dynatrace Managed.")

To receive external traffic, expose the Managed Cluster to external networks and configure a public IP address. Exposing the Managed Cluster directly to external networks isn't recommended for security reasons. Instead, use one or more [Cluster ActiveGates](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") as mediating proxies for pre-processing of OneAgent and DEM traffic. Cluster ActiveGates are recognized by the Managed Cluster and can be configured through the Cluster Management Console, similar to Managed Cluster nodes.

![Stage 2: Dynatrace Managed deployment extended with Cluster ActiveGates for external OneAgent and DEM traffic](https://dt-cdn.net/images/con-man-pure-005-1200-f44d093c51.png)

Stage 2: Dynatrace Managed deployment extended with Cluster ActiveGates for external OneAgent and DEM traffic

The web UI is accessed using HTTPS, which requires a TLS certificate. You can use a self-signed certificate, but for secure web UI traffic and cluster administration, provide a domain name and a valid SSL certificate, or let Dynatrace generate them automatically. By default, each Managed Cluster gets a subdomain of `*.dynatrace-managed.com` with a valid certificate from Let's Encrypt.

Each Cluster ActiveGate requires:

* A publicly available IP address

  Required to accept traffic from external sources.
* A domain name with a valid [SSL certificate](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")

  External communication is only supported over HTTPS (port 443). The domain must differ from the Dynatrace web UI domain. You can provide your own domain and SSL certificate, or let Dynatrace generate them on your behalf. Cluster ActiveGates don't support proxying of web UI traffic.

For high-load installations with many external hosts, applications, sessions, and synthetic monitors, set up multiple load-balanced Cluster ActiveGates sharing the same domain name and certificate.

The Environment ActiveGate connects directly to the Managed Cluster by default (unless custom network zones are used). Configure it to connect through the Cluster ActiveGate if the Managed Cluster isn't directly reachable from the Environment ActiveGate's network.

When the Environment ActiveGate connects to the Managed Cluster through a Cluster ActiveGate, the Cluster ActiveGate must be operational, reachable, and configured with a suitable IP address (local or public) before installation begins.

## Stage 3: Integration with existing infrastructure

When embedding Dynatrace Managed into an existing IT infrastructure, you can incorporate appliances that are already in place. The diagram shows a customer-provided load balancer in front of the Cluster ActiveGate domain and a customer-provided proxy for outbound communication to Mission Control.

![Stage 3: Dynatrace Managed deployment integrated with a customer load balancer and outbound proxy](https://dt-cdn.net/images/con-man-integr-005-1200-6b2f5c5afb.png)

Stage 3: Dynatrace Managed deployment integrated with a customer load balancer and outbound proxy

## Stage 4: High availability with automatic recovery

A high-availability deployment spans distributed networks and provides near-zero downtime, continuous monitoring without data loss in failover scenarios, and cost savings by eliminating standby recovery hosts and backup transfer infrastructure. For capacity planning, treat the nodes in the additional data center as redundant rather than expanded capacity, and balance both data centers equally. For details, see [Premium high availability](/managed/managed-cluster/high-availability "Explore Dynatrace Managed high availability options, including Premium High Availability across data centers and rack-aware deployment.").

![Stage 4: Premium high-availability Dynatrace Managed deployment spanning two data centers](https://dt-cdn.net/images/con-man-global-005-1200-aa4bbfc45b.png)

Stage 4: Premium high-availability Dynatrace Managed deployment spanning two data centers

## Required configuration per traffic type

Each traffic type has different network access and certificate requirements. Although Real User Monitoring (RUM), agentless RUM, and mobile RUM typically relate to traffic from outside your network, the same requirements apply when that traffic originates inside your network.

| Traffic type | Public IP | Valid SSL certificate |
| --- | --- | --- |
| OneAgent (on-premises) |  |  |
| OneAgent (external) | required |  |
| RUM (on-premises) |  |  |
| RUM (external) |  |  |
| Agentless RUM (on-premises) |  | required |
| Agentless RUM (external) | required | required |
| Mobile RUM (on-premises) |  | required |
| Mobile RUM (external) | required | required |
| Synthetic | required |  |

[Agentless Real User Monitoring](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), [mobile-app monitoring](/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring "Learn how to set up real user monitoring for your mobile apps and use with Dynatrace Managed."), and [synthetic monitors](/managed/offline-doc/how-do-i-enable-synthetic-monitors "Learn how to enable synthetic monitors on Dynatrace Managed.") use the same endpoint to transmit monitoring data to Dynatrace Managed.