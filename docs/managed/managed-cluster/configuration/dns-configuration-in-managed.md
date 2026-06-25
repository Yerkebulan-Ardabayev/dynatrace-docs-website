---
title: DNS configuration for Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/dns-configuration-in-managed
scraped: 2026-05-12T11:53:01.709124
---

# DNS configuration for Dynatrace Managed

# DNS configuration for Dynatrace Managed

* Published Aug 06, 2020

If you need to configure your own SSL certificate (see [Install your own SSL certificate](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")), you also need to create your own domain name for the cluster domain. To do this, you need to specify your public endpoint and modify your local DNS.

Invalid configuration may lead to cluster outage

Invalid configuration of DNS might result in data mismatch or lead to cluster outage. No additional configuration is required beyond the steps outlined below.

#### Specify your public endpoint

Go to **Settings** > **Public endpoints** and enter the address you normally use to access your Dynatrace cluster UI (your own domain name).

#### Add records to your local DNS

For each Dynatrace Managed node, add a record of its IP address and your domain.
If you rely on mapping of host names to IP addresses, add `A` type records in the following format:  
`Host Type IP`

For example:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3
```

Additionally, you might want to add separate subdomains per node for the purposes of load-balancer routing.

For example:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3



n01.dynatrace.mycompany.com  A 10.176.0.1



n02.dynatrace.mycompany.com  A 10.176.0.2



n03.dynatrace.mycompany.com  A 10.176.0.3
```