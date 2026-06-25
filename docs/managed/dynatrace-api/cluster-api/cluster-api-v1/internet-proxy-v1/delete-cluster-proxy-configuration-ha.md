---
title: HA - Delete proxy configuration in specific data center
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration-ha
scraped: 2026-05-12T12:12:18.228717
---

# HA - Delete proxy configuration in specific data center

# HA - Delete proxy configuration in specific data center

* Published Nov 18, 2020

This API call deletes a proxy configuration in a specific data center.

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
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Successful, previous configuration returned |
| **404** | - | Proxy was not configured for given Data Center |

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

In this example, you delete the proxy configuration from your Dynatrace Managed deployment in a specific data center (`eu-west-1`). In return, you receive a response containing the previous proxy configuration.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1
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