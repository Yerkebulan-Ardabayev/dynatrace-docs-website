---
title: Delete cluster proxy configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration
---

# Delete cluster proxy configuration

# Delete cluster proxy configuration

* Published Nov 18, 2020

This API call deletes a cluster proxy configuration.

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
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Successful, previous configuration returned |
| **404** | - | Proxy was not configured |

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

In this example, you delete the proxy configuration from your Dynatrace Managed deployment (`myManaged.cluster.com`). In return, you receive a response of a previous proxy configuration.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration
```

#### Response body

```
{



"scheme": "http",



"server": "outbound-proxy.dynatrace.com",



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