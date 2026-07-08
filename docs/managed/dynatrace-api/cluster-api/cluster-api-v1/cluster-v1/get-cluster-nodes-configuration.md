---
title: Get cluster nodes configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration
---

# Get cluster nodes configuration

# Get cluster nodes configuration

* Published Apr 30, 2021

This API request retrieves the cluster nodes configuration.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Success |

## Example

This request returns all nodes with their node capability values and assignment to a datacenter.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration" -H  "accept: */*"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration
```

#### Response body

```
{



"clusterNodes": [



{



"id": 1,



"ipAddress": "10.10.4.2",



"webUI": false,



"agent": true,



"datacenter": "datacenter-1",



"kubernetesRole": ""



},



{



"id": 2,



"ipAddress": "10.10.4.6",



"webUI": true,



"agent": false,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



}
```

#### Response code

`200`