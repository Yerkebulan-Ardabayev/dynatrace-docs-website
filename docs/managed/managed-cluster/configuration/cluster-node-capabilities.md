---
title: Cluster node capabilities
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/cluster-node-capabilities
scraped: 2026-05-12T11:53:08.149709
---

# Cluster node capabilities

# Cluster node capabilities

* Published Jul 17, 2018

Certain deployments may require that specific nodes only serve UI traffic and not process OneAgent data. Or the opposite, where nodes only process OneAgent data and don't serve UI traffic. By configuring one or the other of these options, you can achieve higher stability, better cache behavior, and faster UI response times.

Web UI traffic

To improve DNS load-balancing performance, starting with Dynatrace Managed 1.214, web UI traffic is by default disabled when installing the 13th and subsequent nodes (or 7th and subsequent nodes in a data center for Premium HA). You can enable/disable web UI traffic for a node via the Cluster REST API.

To enable or disable OneAgent traffic on a node, you can use the Web UI, the command line, or an API call.

## Enable/Disable OneAgent traffic via the Cluster Management Console UI

To disable OneAgent traffic (i.e., to set a cluster node to idle mode)

1. Go to **Deployment Status**.
2. Expand the cluster node you want to disable and click **Configure**.
3. Click the Browse button (**â¦**) in the top right corner.
4. Select **Disable OneAgent traffic** to stop monitoring data processing on the node.

To enable OneAgent traffic on a node, repeat the first three steps above, then select **Enable OneAgent traffic** to start monitoring data processing on the node.

## Enable/Disable Web UI traffic via the Cluster Management Console UI

To disable Web UI traffic (i.e., to set a cluster node to idle mode)

1. Go to **Deployment Status**.
2. Expand the cluster node you want to disable and click **Configure**.
3. Click the Browse button (**â¦**) in the top right corner.
4. Select **Disable Web UI traffic** to stop monitoring data processing on the node.

To enable Web UI traffic on a node, repeat the first three steps above, then select **Enable Web UI traffic** to start monitoring data processing on the node.

## Enable/Disable OneAgent or Web UI traffic using an API call

You can configure this option using an API call. See [Configure cluster nodes responsibilities](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities "Learn how to configure cluster nodes responsibilities.")

### Authentication

To execute this request, you need the **Cluster token management** permission assigned to your API token. If you do not have the API token, you can generate one.

1. Go to **Access Tokens**.
2. Select **Generate token** and enter a name for your token.
3. Select the **Service Provider API** permissions and click **Generate**.

Use the generated API token to execute the API calls.

### Endpoint

You can `POST` to the `/api/v1.0/onpremise/cluster/configuration` endpoint with the following parameters:

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| ID | integer | ID of the node | body | required |
| webUI | boolean | Sets the webUI for this node. Define if this node should be used for serving WebUI requests (`true`/`false`). | body | required |
| OneAgent | boolean | Sets OneAgent traffic for this node. Define if this node should receive OneAgent traffic (`true`/`false`). | body | required |
| datacenter | string | not in use. | body | not required |

An example of a JSON payload for the API call:

```
{



"clusterNodes": [



{



"id": 1,



"webUI": true,



"agent": true,



"datacenter": "dc-1"



},



{



"id": 2,



"webUI": true,



"agent": true,



"datacenter": "dc-1"



}



]



}
```