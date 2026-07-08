---
title: Set up load balancer
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/set-up-load-balancer
---

# Set up load balancer

# Set up load balancer

* How-to guide
* 5-min read
* Updated on Jun 18, 2026

Set up an external load balancer when you need an additional load-balancing tier in front of your Managed Cluster.

## Plan load balancer setup

The Dynatrace Managed Cluster includes NGINX, an all-in-one, open-source, high-performance HTTP server and reverse proxy. NGINX, which is installed on each Managed Cluster node, performs load balancing and routing of traffic between nodes. NGINX is configured specifically to perform the following tasks:

* **Session persistence and affinity**

  After a user starts a web UI session on a given Managed Cluster node, requests go to that node until the user closes the session.
* **Node health checks**

  If a node is unreachable, that node is marked as unhealthy, and traffic is forwarded only to healthy nodes.
* **DNS resolution** Optional

  DNS records are managed for the Managed Cluster; the DNS resolves to the IP addresses of all the nodes. DNS-based resolution provides additional load balancing (the order of IP addresses is randomized in DNS resolution). Automatic DNS management for the Managed Cluster is optional—you can opt out and use your DNS instead.

Additional cluster load balancing

NGINX is an integral part of a Dynatrace Managed deployment. If you need an additional tier of load balancing to achieve a single point of access, set up your load balancer in front of the Dynatrace Managed Cluster.

### Setup considerations

* **Compliance**

  Your organization might have strict rules regarding TLS certificate management and access control. For example, a policy might require that all incoming traffic traverse an organization-approved central load balancer or proxy server.
* **Extended failover**

  In the event of a node's hardware or network failure, the node IP may still be part of the domain record. Stale DNS records can result in connection timeouts if the unhealthy IP address is selected in DNS resolution. An external load balancer can automatically exclude the unhealthy node, which improves the user experience.
* **Geographically distributed load balancing**

  For clusters deployed in two data centers (using the Premium High Availability feature), Dynatrace recommends adding an additional load balancer that can optimize user access and handle cross-data-center failover. See [Premium High Availability for multi-data centers](/managed/managed-cluster/high-availability/multi-data-centers "Understand how Dynatrace Managed Premium High Availability provides failover, data resilience, and data routing across data centers.").

### Configuration guidelines

Load balancer configuration depends on how the particular load balancer will be used. The following are general guidelines.

#### Target configuration

The list of target nodes should contain IP addresses of Dynatrace Managed nodes intended to receive the web traffic, including user-generated traffic and REST API calls. Typically the list should contain all Managed Cluster nodes. This list has to be updated after node join or removal.

In the Cluster Management Console (CMC), you can exclude a node from web UI traffic. This feature affects the NGINX configuration and the automatically provisioned domain (`xyz.dynatrace-managed.com`). When you use an external load balancer, nodes need to be excluded from the list of target nodes; otherwise, they will still receive network traffic. See [cluster node capabilities](/managed/managed-cluster/configuration/configure-cluster-capabilities "Configure OneAgent data processing and web UI traffic on individual Managed Cluster nodes using the Cluster Management Console or REST API.").

Traffic must be forwarded to HTTPS port 443 of NGINX. The request path/parameters must not be altered in any way; custom path suffixes aren't supported.

#### Timeouts

Set the timeout value for the target response to no less than what's configured in NGINX by default (120 seconds).

#### Health checks

Configure health checks for all of the target nodes. If you don't configure health checks for all of the target nodes, the load balancer may attempt to forward traffic to a node that isn't monitored by the health check and that may be down due to failure.

Use the `/rest/health` URL for the health check with an expected response code of `HTTP 200`.

#### Session persistence and affinity

Session persistence and affinity are configured and realized by the Dynatrace Managed Cluster. No configuration is required.

#### Domain and SSL certificates

Optional

Configuration of a domain name pointing to the load balancer and a TLS certificate is optional. You can disable the automatic domain and certificate handling option of Dynatrace. See [DNS configuration in Dynatrace Managed](/managed/managed-cluster/configuration/configure-cluster-dns-entries "Configure DNS entries for your Dynatrace Managed deployment by creating a domain name, setting a public endpoint, and adding DNS A records for each node.").

## Configure load balancer

Configure the endpoint settings that match the traffic types you want to route through the external load balancer.

[**Configure web UI traffic**](/managed/managed-cluster/configuration/set-up-load-balancer#configure-web-ui-traffic "Learn how to set up an external load balancer in front of your Dynatrace Managed Cluster to handle web UI, OneAgent, and RUM/Mobile/Synthetic traffic.")[**Configure OneAgent traffic**](/managed/managed-cluster/configuration/set-up-load-balancer#configure-one-agent-traffic "Learn how to set up an external load balancer in front of your Dynatrace Managed Cluster to handle web UI, OneAgent, and RUM/Mobile/Synthetic traffic.")[**Configure RUM, mobile, and Synthetic traffic**](/managed/managed-cluster/configuration/set-up-load-balancer#configure-rum-mobile-synthetic-traffic "Learn how to set up an external load balancer in front of your Dynatrace Managed Cluster to handle web UI, OneAgent, and RUM/Mobile/Synthetic traffic.")

### Configure web UI traffic

If you plan to use the load balancer for web UI traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

#### Public endpoint configuration

1. In the CMC, go to **Settings** and select **Public endpoints**.
2. Adjust **Dynatrace Web UI URL** to point to your load balancer.

Chat not available

If you changed the Dynatrace Web UI URL that opens your Dynatrace web UI, or if more than one domain points to your Managed Cluster, it might affect in-product chat assistance. However, you can still access it via REST API:

1. Repeat step 1 mentioned above.
2. See the **Public endpoints** redirection from the UI instructions on the right.
3. Use the following API Token to create an **Additional address**.

   POST `/endpoint/webUiAddress`
4. Use the following API Token to access the in-product chat assistance.

   POST `/endpoint/additionalWebUiAddresses`

### Configure OneAgent traffic

Load balancing is less needed for OneAgent traffic because OneAgent is capable of switching between endpoints and performing client-side load balancing. If you plan to use the load balancer for OneAgent traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

#### OneAgent endpoint configuration

1. In the CMC, go to **Deployment Status** and select **Cluster nodes**.
2. On each node's details page, select **Configure** and, in **Customize node endpoints**, adjust **IP address and port for OneAgent traffic** to point to the load balancer and not to the node directly.

### Configure RUM, mobile, and Synthetic traffic

If you plan to use the load balancer where agentless RUM or mobile app monitoring is used, Dynatrace recommends configuring a load balancer, either in front of cluster ActiveGates or directly in front of the Managed Cluster. Due to the possibility of high-volume TLS connection and request spikes, offloading TLS termination to a load balancer is beneficial, particularly if the load balancer has hardware-accelerated TLS handling or autoscaling capabilities. TLS offloading can shield the Managed Cluster from overload and separate the access path between beacon traffic and web UI/OneAgent traffic.

If you plan to use the load balancer for RUM/Mobile/Synthetic traffic, in addition to the [general guidelines](#general-guidelines) for configuring the load balancer, the following setting should be configured.

#### Public endpoint configuration

1. In the CMC, go to **Settings** and select **Public endpoints**.
2. Adjust **Cluster ActiveGate URL** to point to your load balancer.  
   You can do it even if you don't have any cluster ActiveGates or the load balancer points directly to the Managed Cluster.