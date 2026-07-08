---
title: HA - Set or update proxy configuration for specific data center
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration-ha
---

# HA - Set or update proxy configuration for specific data center

# HA - Set or update proxy configuration for specific data center

* Published Nov 18, 2020

This API call updates a proxy configuration in a specific data center.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configurations`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| dc | string | Data Center | path | Required |
| body | [InternetProxyChangeRequest](#openapi-definition-InternetProxyChangeRequest) | Configuration of proxy server for Internet connection | body | Required |

### Request body objects

#### The `InternetProxyChangeRequest` object

Configuration of proxy server for Internet connection

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| nonProxyHosts | string[] | Definition of hosts for which proxy won't be used. You can define multiple hosts. Each host can start or end with wildcard '\*' for instance to match whole domain. | Optional |
| password | string | Password of proxy server, null means do not change previous value | Optional |
| port | integer | Port of proxy server | Required |
| scheme | string | Protocol which proxy server uses The element can hold these values * `http` * `https` | Required |
| server | string | Address (either IP or Hostname) of proxy server | Required |
| user | string | User of proxy server, null means do not change previous value | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"nonProxyHosts": [



"string"



],



"password": "string",



"port": 1,



"scheme": "http",



"server": "string",



"user": "string"



}
```

## Response

### Response codes

| Code | Description |
| --- | --- |
| **201** | Successful, new configuration created |
| **204** | Successful, configuration updated |
| **400** | Given proxy configuration is invalid |

## Example

In this example, you add a proxy server (`outbound-proxy.dynatrace.com`) that uses port 8080 and requires a password to a data center `eu-west-1`, at the same time excluding an internal lab host (`*.internal.lab.company.com`).

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"scheme\":\"http\",\"server\":\"outbound-proxy-dc1.dynatrace.com\",\"port\":8080,\"nonProxyHosts\":[\"https://mycompany.com/proxy/*\",\"*.internal.lab.company.com\"],\"userOrPasswordDefined\":true}"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations/eu-west-1
```

#### Response body

```
{



"code": 201,



"message": "Successful, new configuration created."



}
```

#### Response code

`201`