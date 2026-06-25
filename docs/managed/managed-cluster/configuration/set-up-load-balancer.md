---
title: Set up a load balancer for Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/set-up-load-balancer
scraped: 2026-05-12T11:53:06.779160
---

# Set up a load balancer for Dynatrace Managed

# Set up a load balancer for Dynatrace Managed

* Published May 19, 2022

A Dynatrace Managed cluster includes NGINX, an all-in-one, open-source, high-performance HTTP server and reverse proxy. NGINX, which is installed on each cluster node, performs load balancing and routing of traffic between nodes. NGINX is configured specifically to perform the following tasks:

* **Session persistence and affinity**

  Once a web UI session is opened on a given cluster node, requests are forwarded to that cluster node until the user closes the session (signs out).
* **Node health checks**

  If a node is unreachable, that node is marked as unhealthy, and traffic is forwarded only to healthy nodes.
* **DNS resolution** Optional

  DNS records are managed for the cluster; the DNS resolves to the IP addresses of all the cluster nodes. This provides additional load balancing based on DNS (the order of IP addresses is randomized in DNS resolution). Automatic DNS management for the cluster is optionalâyou can opt out and use your DNS instead.

Additional cluster load balancing

NGINX is an integral part of a Dynatrace Managed deployment. If you need an additional tier of load balancing to achieve a single point of access, you can set up your load balancer in front of the Dynatrace Managed cluster.

## Setup considerations

* **Compliance**

  Your organization might have strict rules regarding TLS certificate management and access control. For example, a policy might require that all incoming traffic traverse an organization-approved central load balancer or proxy server.
* **Extended failover**

  In the event of a node's hardware or network failure, the node IP may still be part of the domain record. This can result in connection timeouts if the unhealthy IP address is selected in DNS resolution. An external load balancer can automatically exclude the unhealthy node, which improves the user experience.
* **Geographically distributed load balancing**

  For clusters deployed in two datacenters (using the Premium HA feature), we recommend having an additional load balancer that can optimize user access and handle cross-datacenter failover. See [Premium HA for multi-data centers](/managed/managed-cluster/high-availability/premium-high-availability "Learn how Dynatrace Premium High Availability provides near-zero downtime and data resilience through multi-data-center deployments for Managed Clusters.").

## Load balancer configuration guidelines

Load balancer configuration depends on how the particular load balancer will be used. The following are general guidelines.

### Target configuration

The list of target nodes should contain IP addresses of Dynatrace Managed nodes intended to receive the web traffic, including user-generated traffic and REST API calls. Typically the list should contain all cluster nodes. This list has to be updated after node join or removal.

In the Cluster Management Console, you can exclude a node from web UI traffic. This feature affects the NGINX configuration and the automatically provisioned domain (`xyz.dynatrace-managed.com`). When you use an external load balancer, cluster nodes need to be excluded from the list of target nodes; otherwise, they will still receive network traffic. See [Cluster node capabilities](/managed/managed-cluster/configuration/cluster-node-capabilities "Find out how to enable/disable a cluster node via the Web UI or API call").

Traffic must be forwarded to HTTPS port 443 of NGINX. The request path/parameters must not be altered in any way; custom path suffixes are not supported.

### Timeouts

We recommend setting the timeout value for the target response to no less than what is configured in NGINX by default (120 seconds).

### Health checks

We recommend configuring health checks for all of the target nodes. If you do not configure health checks for all of the target nodes, the load balancer may attempt to forward traffic to a node that is not monitored by the health check and that may be down due to failure.

Use the `/rest/health` URL for the health check with an expected response code of `HTTP 200`.

### Session persistence and affinity

Session persistence and affinity are configured and realized by the Dynatrace Managed cluster. No configuration is required.

### Domain and SSL certificates

Optional

Configuration of a domain name pointing to the load balancer and a TLS certificate is optional. You can disable the automatic domain and certificate handling option of Dynatrace. See [DNS configuration for Dynatrace Managed](/managed/managed-cluster/configuration/dns-configuration-in-managed "Learn how to configure DNS entries for Dynatrace Managed.").

## Web UI traffic

If you plan to use the load balancer for web UI traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

### Public endpoint configuration

1. In the Cluster Management Console (CMC), go to **Settings** and select **Public endpoints**.
2. Adjust **Dynatrace Web UI URL** to point to your load balancer.

Chat not available

If you changed the Dynatrace Web UI URL you normally use to access your Dynatrace Cluster UI or use more than one domain to access your Dynatrace Cluster, it might affect the in-product chat assistance. However, you can still access it via REST API:

1. Repeat step 1 mentioned above.
2. See the **Public endpoints** redirection from the UI instructions on the right.
3. Use the following API Token to create an **Additional address**.

   POST `/endpoint/webUiAddress`
4. Use the following API Token to access the in-product chat assistance.

   POST `/endpoint/additionalWebUiAddresses`

## OneAgent traffic

Load balancing is less needed for OneAgent traffic because OneAgent is capable of switching between endpoints and effectively performing client-side load balancing. If you plan to use the load balancer for OneAgent traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

### OneAgent endpoint configuration

1. In the Cluster Management Console (CMC), go to **Deployment Status** and select **Cluster nodes**.
2. On each node's details page, select **Configure** and, in **Customize node endpoints**, adjust **IP address and port for OneAgent traffic** to point to the load balancer and not to the node directly.

## RUM/Mobile/Synthetic traffic

If you plan to use the load balancer where agentless RUM or mobile app monitoring is used, we highly recommended that you configure a load balancer, either in front of cluster ActiveGates or directly in front of the cluster. Due to the possibility of high-volume TLS connection and request spikes, offloading TLS termination to a load balancer is beneficial, particularly if the load balancer has hardware-accelerated TLS handling and/or autoscaling capabilities. This can shield the cluster from overload and separate the access path between beacon traffic and web UI/OneAgent traffic.

If you plan to use the load balancer for RUM/Mobile/Synthetic traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

### Public endpoint configuration

1. In the Cluster Management Console (CMC), go to **Settings** and select **Public endpoints**.
2. Adjust **Cluster ActiveGate URL** to point to your load balancer.  
   You can do it even if you don't have any cluster ActiveGates and/or the load balancer points directly to the Managed cluster.