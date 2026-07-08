---
title: Get cluster information about known cluster nodes
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-info-known-servers
---

# Get cluster information about known cluster nodes

# Get cluster information about known cluster nodes

* Published Apr 30, 2021

This API call retrieves cluster information about known nodes.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Cluster](#openapi-definition-Cluster)[] | Success |

### Response body objects

#### The `ResponseBody` object

#### The `Cluster` object

| Element | Type | Description |
| --- | --- | --- |
| buildVersion | string | Server version |
| clusterMemberAddress | string | Cluster member address |
| communicationUris | string[] | Communication URIs |
| ~~dnsEntryPointUris~~ | string[] | DEPRECATED  DNS entry point URIs |
| id | integer | Node ID |
| jvmInfo | string | JVM info |
| operationState | string | Operation state |
| osInfo | string | OS info |
| restServiceRootUris | string[] | REST service root URIs |

### Response body JSON models

```
[



{



"buildVersion": "string",



"clusterMemberAddress": "string",



"communicationUris": [



"string"



],



"dnsEntryPointUris": [



"string"



],



"id": 1,



"jvmInfo": "string",



"operationState": "string",



"osInfo": "string",



"restServiceRootUris": [



"string"



]



}



]
```

## Example

In this example, the request queries the cluster for the current deployment configuration and status. The cluster then returns information about each cluster node in an array. Each cluster node object then contains its id, status, communication addresses and host environment details.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster
```

#### Response body

```
[



{



"id": 1,



"clusterMemberAddress": "10.10.4.2:5701",



"operationState": "RUNNING",



"buildVersion": "1.216.10.20210429-124335",



"osInfo": "Platform: Linux, Version: 5.4.0-1041, Architecture: amd64, Processors: 16",



"jvmInfo": "VM: OpenJDK 64-Bit Server VM, Version: 11.0.8, Vendor: AdoptOpenJDK, Memory [maxMemory=17408M, initHeap=17408M, maxHeap=17408M, usedMeta=17M, committedMeta=17M, totalPhysicalMemory=62851M, freePhysicalMemory=14336M]",



"dnsEntryPointUris": [],



"restServiceRootUris": [



"https://ip-10-10-4-2.eu-west-1.compute.internal:8021/api/v1.0",



"https://10.10.4.2:8021/api/v1.0"



],



"communicationUris": [



"http://ip-10-10-4-2.eu-west-1.compute.internal:8020/communication",



"http://10.176.42.242:8020/communication"



]



},



...



]
```

#### Response code

`200`