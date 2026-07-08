---
title: Configure Cluster capabilities
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-capabilities
---

# Configure Cluster capabilities

# Configure Cluster capabilities

* How-to guide
* 2-min read
* Updated on Jun 18, 2026

Certain deployments may require that specific nodes only serve UI traffic and not process OneAgent data. Or the opposite, where nodes only process OneAgent data and don't serve UI traffic. By configuring one or the other of these options, you can achieve higher stability, better cache behavior, and faster UI response times.

Web UI traffic

To improve DNS load-balancing performance, starting with Dynatrace Managed 1.214, web UI traffic is by default turned off when installing the 13th and subsequent nodes (or 7th and subsequent nodes in a data center for Premium HA). You can enable or disable web UI traffic for a node via the Cluster REST API.

To configure OneAgent or web UI traffic on a node, use the CMC or Cluster REST API.

## UI workflows

Use the CMC to configure OneAgent traffic and web UI traffic for a Managed Cluster node.

### Configure OneAgent traffic

To disable OneAgent traffic (that is, to set a Managed Cluster node to idle mode):

1. Go to **Deployment status**.
2. Expand the Managed Cluster node you want to disable and select **Configure**.
3. Select the **Browse** button (**…**) in the upper-right corner.
4. Select **Disable OneAgent traffic** to stop monitoring data processing on the node.

To enable OneAgent traffic on a node, repeat steps 1 through 3, then select **Enable OneAgent traffic** to start monitoring data processing on the node.

### Configure web UI traffic

To disable web UI traffic (that is, to set a Managed Cluster node to idle mode):

1. Go to **Deployment status**.
2. Expand the Managed Cluster node you want to disable and select **Configure**.
3. Select the **Browse** button (**…**) in the upper-right corner.
4. Select **Disable Web UI traffic** to stop monitoring data processing on the node.

To enable Web UI traffic on a node, repeat steps 1 through 3, then select **Enable Web UI traffic** to start monitoring data processing on the node.

## API workflows

Use the Cluster REST API to configure OneAgent or web UI traffic for a Managed Cluster node.

### Configure node traffic settings

You can configure this option using an API call. See [POST /cluster/configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities "Learn how to configure cluster nodes responsibilities.").

### Authentication

To run this request, you need the **Cluster token management** permission assigned to your API token. If you don't have the API token, you can generate one.

1. Go to **Access Tokens**.
2. Select **Generate token** and enter a name for your token.
3. Select the **Service Provider API** permissions and select **Generate**.

Use the generated API token to run the API calls.

### Endpoint

You can `POST` to the `/api/v1.0/onpremise/cluster/configuration` endpoint with the following parameters:

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| ID | integer | ID of the node | body | Yes |
| webUI | boolean | Sets the webUI for this node. Define if this node should be used for serving WebUI requests (`true`/`false`). | body | Yes |
| OneAgent | boolean | Sets OneAgent traffic for this node. Define if this node should receive OneAgent traffic (`true`/`false`). | body | Yes |
| datacenter | string | Not in use. | body | No |

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