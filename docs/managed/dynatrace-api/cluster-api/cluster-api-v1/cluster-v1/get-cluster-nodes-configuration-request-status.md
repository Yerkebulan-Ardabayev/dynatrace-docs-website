---
title: Get cluster nodes configuration request status
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-request-status
scraped: 2026-05-12T12:12:21.416593
---

# Get cluster nodes configuration request status

# Get cluster nodes configuration request status

* Published Apr 30, 2021

This API call retrieves the status of cluster node configuration requests.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration/status/{requestedAt}`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| requestedAt | integer | - | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Success |

## Example

This request provides information on the given operation status. You can identify a request by its requested timestamp and pass it as a `requestedAt` path parameter.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration/status/1" -H  "accept: */*"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration/status/1
```

#### Response body

```
{



"id": 1619771074449,



"request": {



"clusterNodes": [



{



"id": 1,



"ipAddress": "10.10.4.2",



"webUI": false,



"agent": true,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



]



},



"state": "SUCCESS",



"details": "",



"requestedAt": "2021/04/30 08:24:34 Etc/UTC",



"finishedAt": "2021/04/30 08:25:50 Etc/UTC",



"states": {



"DOMAIN_UPDATE": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "",



"requestedAt": "2021/04/30 08:25:13 Etc/UTC",



"finishedAt": "2021/04/30 08:25:41 Etc/UTC",



"states": {}



},



"OPERATION_STATE": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update operation state step finished",



"requestedAt": "2021/04/30 08:25:41 Etc/UTC",



"finishedAt": "2021/04/30 08:25:41 Etc/UTC",



"states": {}



},



"AGENT_TRAFFIC": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update agent traffic step finished",



"requestedAt": "2021/04/30 08:25:41 Etc/UTC",



"finishedAt": "2021/04/30 08:25:50 Etc/UTC",



"states": {}



},



"WEB_UI": {



"id": 0,



"request": null,



"state": "SUCCESS",



"details": "Update web step finished",



"requestedAt": "2021/04/30 08:24:36 Etc/UTC",



"finishedAt": "2021/04/30 08:25:13 Etc/UTC",



"states": {}



}



}



}
```

#### Response code

`200`