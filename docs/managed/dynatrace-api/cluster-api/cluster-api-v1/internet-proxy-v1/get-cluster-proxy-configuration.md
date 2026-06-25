---
title: Get cluster proxy configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration
scraped: 2026-05-12T12:12:25.876559
---

# Get cluster proxy configuration

# Get cluster proxy configuration

* Published Nov 18, 2020

This API call retrieves a cluster proxy configuration.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configuration`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Success |
| **404** | - | Proxy is not configured |

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

In this example, you request proxy configuration from your Dynatrace Managed deployment (`myManaged.cluster.com`). In return you receive a response indicating that proxy server is `172.16.115.211` on port `8080` and that you require a password to use that proxy.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration
```

#### Response body

```
{



"scheme": "http",



"server": "172.16.115.211",



"port": 8080,



"userOrPasswordDefined": true



}
```

#### Response code

`200`