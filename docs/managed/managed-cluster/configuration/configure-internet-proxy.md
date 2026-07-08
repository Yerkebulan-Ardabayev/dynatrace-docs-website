---
title: Configure internet proxy
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-internet-proxy
---

# Configure internet proxy

# Configure internet proxy

* How-to guide
* 2-min read
* Updated on Jun 18, 2026

Configure an internet connection to allow [Mission Control (MC) proactive support](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable."), receive MC updates, and use external problem notifications via tools such as ServiceNow, Jira, and webhooks.

Authentication protocols

The following authentication protocols are available:

* Basic
* NTLMv1 (Deprecated)

Configure Basic authentication together with TLS. Over TLS, transport encryption protects the credentials.

There are three different ways to configure a proxy connection for your Managed Cluster. Select the approach that best suits your needs.

[**Configure proxy during installation**](/managed/managed-cluster/configuration/configure-internet-proxy#during-installation "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1.")[**Configure proxy in the Cluster Management Console**](/managed/managed-cluster/configuration/configure-internet-proxy#cluster-management-console "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1.")[**Configure proxy with the Cluster API**](/managed/managed-cluster/configuration/configure-internet-proxy#cluster-api "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1.")

## Configure proxy during installation

Use the following command-line parameters to set up a proxy connection to MC during the Managed installation:

```
--network-proxy
```

If your machine uses a network proxy to connect to the internet, enter the address in the following format:

```
protocol://[user:password@]server-address:port
```

The default value is `none`.

```
--network-proxy-cert-file
```

If your machine uses a network HTTPS proxy with a self-signed certificate, extend the trusted certificate store. Follow this parameter with the full path to the public SSL certificate file in PEM format.

## Configure proxy in the Cluster Management Console

1. Sign in to the **Cluster Management Console**.
2. Go to **Settings** > **Internet proxy** and edit **Proxy configuration** for a particular data center.
3. Select **Connect via proxy** and enter proxy server details:

   * **Scheme**
   * **Proxy address** and **Port**
   * **Username** and **Password** if anonymous access isn't possible.

### Exclude hosts from internet proxy

To exclude hosts from the proxy—for example, when problem integrations via webhooks point to internal network hosts—add them to the exclusion list. Use a wildcard (`*`) at the beginning or end of each host entry to match all URLs within a domain.

## Configure proxy with the Cluster API

Use the [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration "Learn how to use the Dynatrace API to set or update cluster proxy configuration.") to set or update the internet proxy configuration of your Managed Cluster.

## FAQ

Can you use a transparent proxy?

Yes, Dynatrace supports transparent proxy configuration.

A transparent proxy (also known as an intercepting proxy, in-line proxy, or forced proxy) can route and intercept Managed Cluster communication to MC. A transparent proxy normally sits between the Managed Cluster and MC. With a transparent proxy, you can audit and inspect all communication payloads.

Dynatrace doesn't need to be aware of the proxy. Configure Dynatrace Managed to trust a root certificate whose private key is known to the proxy. In this setup, the proxy analyzes the contents of SSL/TLS transactions. The arrangement is a man-in-the-middle setup that Dynatrace authorizes by trusting a root certificate owned by the proxy.

How to update the SSL certificate

Run the reconfiguration script with the following parameters:

```
/opt/dynatrace-managed/installer/reconfigure.sh --update-cert --network-proxy-cert-file <proxy_cert_file>
```