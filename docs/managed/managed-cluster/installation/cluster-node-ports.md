---
title: Cluster node ports
source: https://docs.dynatrace.com/managed/managed-cluster/installation/cluster-node-ports
scraped: 2026-05-12T11:22:21.997232
---

# Cluster node ports

# Cluster node ports

* Reference
* 3-min read
* Updated on May 08, 2026

Dynatrace Managed requires specific network ports for operation. Configure your firewall so that all ports listed below are open for bi-directional communication. For a typical Managed deployment, all ports should be open between cluster nodes.

| Port | Used by | Notes |
| --- | --- | --- |
| 443 | Dynatrace web UI, OneAgent, and REST API | Routed to local port 8022 via an iptables prerouting rule. **This port must remain open** to allow incoming traffic from your data center. All cluster communication uses HTTPS with strong encryption. |
| 5701-5710 | Hazelcast In-memory data grid platform | Distributes data evenly across cluster nodes and enables horizontal scaling. Required for cluster-internal communication only. Ports can be blocked for traffic from outside the cluster. |
| 5711, 8018 | Nodekeeper | Required for cluster-internal communication only. Ports can be blocked for traffic from outside the cluster. |
| 7000, 7001, 9042 | Cassandra-based Hypercube storage | Required for cluster-internal communication only. Ports can be blocked for traffic from outside the cluster. |
| 7199 | Cassandra JMX | Required for cluster-internal communication only. Port can be blocked for traffic from outside the cluster. |
| 8019 | Upgrade UI | Required for cluster-internal communication only. Port can be blocked for traffic from outside the cluster. |
| 8020, 8021 | Dynatrace Managed UI and REST API | Required for cluster-internal communication only. Ports can be blocked for traffic from outside the cluster. |
| 8022 | Dynatrace Managed UI and REST API (NGINX) | Can be used in place of port 443 when a non-privileged port is required. Ports can be blocked for traffic from outside the cluster. |
| 8443[1](#fn-1-1-def) | Monitoring data from OneAgent, nodes within Dynatrace Managed cluster | OneAgent sends data outbound to Dynatrace Cluster onlyâno listening port is opened on the monitored host. Each host with OneAgent must have access to this port, which must also remain open for inter-node communication. |
| 9200, 9300 | Elasticsearch-based search engine | Required for cluster-internal communication only. Ports can be blocked for traffic from outside the cluster. |
| 9998 | Embedded ActiveGate | For cluster-internal communication only. |

1

Environments running a cluster version earlier than 1.166 use port `8443`. New environments still use port `8443`, but it doesn't need to be exposed outside the cluster nodes. Upgraded environments preserve the port settings from the previous version.

## Outbound communication to Mission Control

All cluster nodes must be able to communicate with Mission Control to receive software updates and exchange data. Allow outbound traffic to the following IPv4 addresses:

* `13.228.109.33`
* `46.137.81.205`
* `52.5.224.56`
* `52.48.91.146`
* `52.200.165.10`
* `52.221.165.63`

Domains used:

* `mcsvc.dynatrace.com`
* `mcsvc-us.dynatrace.com`
* `mcsvc-eu.dynatrace.com`
* `mcsvc-ap.dynatrace.com`

All cluster data received by Mission Control via the domains above is hosted in the U.S. regions.

To ensure compliance with United States export restrictions[2](#fn-2-2-def), if you plan to host a Managed Cluster or monitor Huawei Cloud services (or any Huawei affiliate), contact Dynatrace Support to configure a Europe or Asia/Pacific endpoint.

2

The Dynatrace Software may not be exported or re-exported from the U.S. to (a) any Group E country listed in SUPPLEMENT NO. 1 TO PART 740âCOUNTRY GROUPS (Currently Syria, North Korea, Iran and Cuba) or the Crimea Region of Ukraine, or (b) any company, entity or person listed as a party of concern found [hereï»¿](https://2016.export.gov/ecr/eg_main_023148.asp) (currently including Huawei Technologies and its affiliates worldwide), or (3) for any end-use related to the development, production or use of nuclear, chemical or biological weapons or missiles. Our contracts with our customers require compliance with these and other export control laws.

Mission Control communication uses HTTPS and WSS over port `443` with TLS v1.2. The TLS/SSL certificate is provided by Amazon and renewed automatically each year.

Mission Control communication can be routed through a proxy. The proxy must support WebSockets and the SNI TLS extension.