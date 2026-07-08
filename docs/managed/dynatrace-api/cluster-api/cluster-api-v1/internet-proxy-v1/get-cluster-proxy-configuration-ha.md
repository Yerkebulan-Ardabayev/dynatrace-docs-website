---
title: HA - Get proxy configuration for specific data center
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha
---

# HA - Get proxy configuration for specific data center

# HA - Get proxy configuration for specific data center

* Published Nov 18, 2020

This API call retrieves a proxy configuration for a specific data center in premium high availability deployments.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configurations`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| dc | string | Data Center | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Success |
| **404** | - | Proxy is not configured for given Data Center |

### Response body objects

#### The `InternetProxy` object

Configuration of proxy server for Internet connection

| Element | Type | Description |
| --- | --- | --- |
| nonProxyHosts | string[] | Definition of hosts for which proxy won't be used. |
| port | integer | Port of proxy server |
| scheme | string | Protocol which proxy server uses |
| server | string | Address (either IP or Hostname) of proxy server |
| userOrPasswordDefined | boolean | Indicates if user/password for proxy is configured |

### Response body JSON models

```
{



"nonProxyHosts": [



"string"



],



"port": 1,



"scheme": "string",



"server": "string",



"userOrPasswordDefined": true



}
```

## Example

In this example, you request to receive proxy configurations for a specific data center (`eu-west-1`). In return you receive JSON response listing of proxy configurations only for `eu-west-1`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1
```

#### Response body

```
{



"scheme": "http",



"server": "outbound-proxy-dc1.dynatrace.com",



"port": 8080,



"nonProxyHosts": [



"https://mycompany.com/proxy/*",



"*.internal.lab.company.com"



],



"userOrPasswordDefined": true



}
```

#### Response code

`200`