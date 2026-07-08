---
title: Configure Cluster DNS entries
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-dns-entries
---

# Configure Cluster DNS entries

# Configure Cluster DNS entries

* How-to guide
* 1-min read
* Updated on Jun 18, 2026

If you need to configure your own SSL certificate (see [Install your own SSL certificate](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")), you also need to create your own domain name for the Managed Cluster domain. Specify your public endpoint and update your local Domain Name System (DNS).

Invalid configuration may lead to a Managed Cluster outage

Invalid configuration of DNS might result in data mismatch or lead to a Managed Cluster outage. No configuration beyond the steps below is needed.

## Specify your public endpoint

Go to **Settings** > **Public endpoints** and enter the address you normally use to access your Dynatrace web UI (your own domain name).

## Add records to your local DNS

For each Dynatrace Managed node, add a record of its IP address and your domain.
If you rely on mapping of host names to IP addresses, create `A` records in the following format:
`Host Type IP`

For example:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3
```

To allow per-node load-balancer routing, add separate subdomains for each node.

For example:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3



n01.dynatrace.mycompany.com  A 10.176.0.1



n02.dynatrace.mycompany.com  A 10.176.0.2



n03.dynatrace.mycompany.com  A 10.176.0.3
```