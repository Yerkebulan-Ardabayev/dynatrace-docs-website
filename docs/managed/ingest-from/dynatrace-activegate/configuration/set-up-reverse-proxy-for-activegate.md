---
title: Reverse proxy or load balancer for ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate
scraped: 2026-05-12T11:36:22.648753
---

# Reverse proxy or load balancer for ActiveGate

# Reverse proxy or load balancer for ActiveGate

* 1-min read
* Updated on Feb 24, 2026

A reverse proxy or a load balancer can be placed on the path from an ActiveGate to the Dynatrace Cluster. This allows your ActiveGate to connect to any available node of the Cluster, spreading the load between the nodes.  
To do this, you need to:

* Provide the address of the reverse proxy/load balancer.
* Ensure that ActiveGate will ignore any further target address information sent from the Dynatrace Cluster, and will thus connect only to the address you have specified.

![ActiveGate connecting to Dynatrace Cluster via reverse proxy/load balancer](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

ActiveGate connecting to Dynatrace Cluster via reverse proxy/load balancer

### Option to configure during installation

This configurationâto use a reverse proxy or a load balancerâcan also be applied during ActiveGate installation, by specifying installation parameters to the ActiveGate installer for [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#reverse-proxy-or-load-balancer-configuration "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#reverse-proxy-or-load-balancer-configuration "Learn about the parameters that you can use with ActiveGate on Windows.") or it can be configured later, after ActiveGate installation, as shown in the following procedure.

A load balancer should not be placed between ActiveGate and OneAgent, as it can disrupt memory dump transmission and processing.

## Configure after installation

agctl

custom.properties

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#outgoing-endpoint "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure a reverse proxy or load balancer for ActiveGate.

#### Set a single reverse proxy endpoint:

```
agctl outgoing-endpoint set https://my.reverse-proxy.com:443/communication
```

#### Set multiple reverse proxy endpoints:

```
agctl outgoing-endpoint set https://my.reverse-proxy-1.com:443/communication,https://my.reverse-proxy-2.com:443/communication
```

After configuring the reverse proxy with `agctl`, you need to [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

1. Stop the ActiveGate and edit the `custom.properties` file in the [ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").
2. To tell the ActiveGate to ignore connectivity information received from the Dynatrace cluster, add or modify the `ignoreClusterRuntimeInfo` parameter in the `[connectivity]` section of the `custom.properties` file:

   ```
   [connectivity]



   ignoreClusterRuntimeInfo = true
   ```
3. Specify the address of the reverse proxy: Add the `seedServerUrl` parameter in the `[collector]` section of the `custom.properties` file in the following format:  
   `seedServerUrl = https://<REVERSE_PROXY>:<REVERSE_PROXY_PORT>/communication`  
   For example:

   ```
   [collector]



   seedServerUrl = https://my.reverse-proxy.com:443/communication
   ```

   **Specify multiple addresses:**  
   The parameter can be a single value or it can be a comma-separated list of target addresses to which the ActiveGate connects.  
   For example:

   ```
   [collector]



   seedServerUrl = https://my.reverse-proxy-1.com:443/communication,https://my.reverse-proxy-2.com:443/communication
   ```
4. Save the `custom.properties` file and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").