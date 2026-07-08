---
title: Reverse proxy or load balancer for OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent
---

# Reverse proxy or load balancer for OneAgent

# Reverse proxy or load balancer for OneAgent

* 1-min read
* Updated on Feb 24, 2026

A reverse proxy/load balancer can be placed on the path from OneAgent to ActiveGate. You need to configure the URL of the load balancer on the ActiveGate so OneAgents can use that endpoint to connect to the ActiveGate.

There is no need to configure OneAgent to use a reverse proxy. OneAgent uses a list of communication endpoints that are embedded in the installer to connect to the environment. ActiveGate reports to OneAgent the URL that is used to configure OneAgent installation.

## Configure during installation

Linux only

On Linux systems, you can configure a reverse proxy or load balancer for OneAgent by specifying the installation parameters during ActiveGate installation. For details, see [Customize ActiveGate installation on Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#load-balancer-oneagent "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

## Configure after installation

agctl

custom.properties

ActiveGate version 1.333+

You can use [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#incoming-endpoint "Learn how to use agctl to configure and manage ActiveGate from the command line") to configure a reverse proxy or load balancer for OneAgent.

#### Set a single reverse proxy endpoint:

```
agctl incoming-endpoint set https://address.of.my.lb.com:9999
```

#### Set multiple reverse proxy endpoints:

```
agctl incoming-endpoint set https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
```

After configuring the reverse proxy with `agctl`, you need to [restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") for the changes to take effect.

1. Stop the ActiveGate and edit the `custom.properties` file in the [ActiveGate configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").
2. Configure the `dnsEntryPoint` parameter in the `[connectivity]` section using the following format:

   `dnsEntryPoint = https://<DOMAIN>:<PORT>`

   where `<PORT>` is optional and defaults to `443`. For example:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb.com:9999
   ```

   To specify multiple target addresses to which the OneAgent connects, use a comma-separated list. For example:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
   ```
3. Save the `custom.properties` file and [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Verify the configuration

To verify the configuration

1. In Dynatrace, go to **Deployment Status** > **ActiveGates**.
2. Expand the row for your ActiveGate and check the **Load Balancer** property in the **Properties** section.

   You can filter the **ActiveGates** page by `Load Balancer address`.