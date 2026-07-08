---
title: Convert Managed Cluster from offline to online
source: https://docs.dynatrace.com/managed/managed-cluster/installation/cluster-offline-to-online
---

# Convert Managed Cluster from offline to online

# Convert Managed Cluster from offline to online

* How-to guide
* 3-min read
* Updated on May 09, 2026

To convert a Managed Cluster from offline to online mode, complete the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Review requirements**](/managed/managed-cluster/installation/cluster-offline-to-online#prerequisites "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Request online license**](/managed/managed-cluster/installation/cluster-offline-to-online#request-license "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run conversion script**](/managed/managed-cluster/installation/cluster-offline-to-online#run-script "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify conversion**](/managed/managed-cluster/installation/cluster-offline-to-online#verify-conversion "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")

## Step 1 Review requirements

* Dynatrace Managed version 1.338+
* SSH access with sudo capability to all Dynatrace Managed Cluster nodes
* Cluster API token with the Service Provider API scope
* Cluster connectivity to Mission Control (the conversion script verifies this)
* Proxy (if needed, see [How to configure internet proxy for cluster](/managed/managed-cluster/configuration/configure-internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access. Supported protocols include Basic and NTLMv1."))
* Cassandra and Elasticsearch are healthy.
* All nodes are up and running.
* The cluster isn't in maintenance mode.

## Step 2 Request online license

Contact your Dynatrace sales representative and request a Dynatrace Managed license in online mode with automatic updates disabled.

## Step 3 Run conversion script

Run the script on each Managed Cluster node sequentially to convert it from offline to online mode:

```
/bin/sh /opt/dynatrace-managed/installer/convert-to-online.sh --api-token <api-token-value> --online-license <online-license-key>
```

* Required Replace `<api-token-value>` with your API token.
* Required Replace `<online-license-key>` with your online license key.
* Optional To enable or disable installation of a self-monitoring OneAgent, add parameter and value `--install-agent on` or `--install-agent off`. Default is `off`.

If the script hasn't converted all Managed Cluster nodes yet, it outputs the following message at the end:

`Not all nodes have finished the conversion to online successfully yet. IDs of nodes left to convert: [2]`

## Step 4 Verify conversion

After the script runs, it displays a message confirming that all Managed Cluster nodes are converted.

If you find the following event under **Cluster Management Console** > **Home** > **Events**, the conversion is complete.

`Your Dynatrace Managed cluster has exited maintenance mode due to the end of node conversion to online.`

## Frequently asked questions

Where can you generate an API token?

In the Cluster Management Console, go to **Home** > **Settings** > **API tokens** > **Cluster tokens** > **Generate token**.

For details, see [Cluster API authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

What happens if a conversion to online fails on a node?

A Managed Cluster stays in maintenance mode until all nodes convert to online. The script is idempotent and can be rerun.

Where can you find logs of the executed script?

By default, the script stores logs in:

`/var/opt/dynatrace-managed/logs/installer/`

What prechecks are performed at the beginning of the script?

At the beginning of the script, the following prechecks run:

1. Cassandra and Elasticsearch are healthy.
2. All nodes are up and running.
3. The cluster isn't in maintenance mode.