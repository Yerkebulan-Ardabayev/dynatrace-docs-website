---
title: OneAgent environment-wide configuration API - GET Technology monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide/get-technology-monitoring
scraped: 2026-05-12T11:15:20.826336
---

# OneAgent environment-wide configuration API - GET Technology monitoring configuration

# OneAgent environment-wide configuration API - GET Technology monitoring configuration

* Reference
* Published Feb 03, 2020

Gets the environment-wide technology monitoring configuration of OneAgent.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/technologies` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/technologies` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TechMonitoringConfigList](#openapi-definition-TechMonitoringConfigList) | Success |

### Response body objects

#### The `TechMonitoringConfigList` object

A list of technology monitoring configurations.

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| technologies | [Technology[]](#openapi-definition-Technology) | A list of technology monitoring configurations. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `Technology` object

Configuration of technology monitoring.

| Element | Type | Description |
| --- | --- | --- |
| monitoringEnabled | boolean | The monitoring of the technology is enabled (`true`) or disabled (`false`). |
| scope | string | The validity of the configuration:  * `HOST`: The setting is valid for OneAgent on host only. Other OneAgents, connected to the same Dynatrace server may have different setting. * `ENVIRONMENT`: The setting is valid for all OneAgents, connected to the Dynatrace server. The element can hold these values * `ENVIRONMENT` * `HOST` |
| type | string | The type of the technology. The element can hold these values * `AIX_KERNEL_EXT` * `APACHE` * `CIM_V2` * `DOCKER` * `DOCKER_WIN` * `DOT_NET` * `DOT_NET_CORE` * `EXTENSIONS` * `EXTENSIONS_DS_GENERIC` * `EXTENSIONS_STATSD` * `GARDEN` * `GO` * `GO_STATIC` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PHP_81` * `PHP_CGI` * `PHP_CLI` * `PHP_CLI_SERVER` * `PHP_WIN` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `VARNISH` * `Z_OS` |

### Response body JSON models

```
{



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"technologies": [



{



"monitoringEnabled": true,



"scope": "ENVIRONMENT",



"type": "JAVA"



}



]



}
```