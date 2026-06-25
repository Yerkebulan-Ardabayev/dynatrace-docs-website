---
title: OneAgent on a host API - OneAgent configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-config
scraped: 2026-05-12T11:21:20.541269
---

# OneAgent on a host API - OneAgent configuration

# OneAgent on a host API - OneAgent configuration

* Reference
* Published Feb 03, 2020

Gets OneAgent configuration on the specified host. You can later change the auto-update and monitoring configuration with one of the following requests:

* [PUT auto-update configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration "Edit the auto-update configuration of a OneAgent instance via the Dynatrace API.")
* [PUT monitoring configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.")

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The Dynatrace entity ID of the required host. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [HostConfig](#openapi-definition-HostConfig) | Success |

### Response body objects

#### The `HostConfig` object

OneAgent configuration on a host.

| Element | Type | Description |
| --- | --- | --- |
| autoUpdateConfig | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Configuration of OneAgent auto-update. |
| id | string | The Dynatrace entity ID of the host where OneAgent is deployed. |
| monitoringConfig | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Monitoring configuration of OneAgent. |
| techMonitoringConfigList | [TechMonitoringConfigList](#openapi-definition-TechMonitoringConfigList) | A list of technology monitoring configurations. |

#### The `HostAutoUpdateConfig` object

Configuration of OneAgent auto-update.

| Element | Type | Description |
| --- | --- | --- |
| effectiveSetting | string | The actual state of the auto-update on the host.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case the value is taken from the host group or the environment-wide configuration. The element can hold these values * `ENABLED` * `DISABLED` |
| effectiveVersion | string | The actual version to which the OneAgent must be updated.  Applicable only if the **setting** parameter is set to `INHERITED` and the **version** parameter is set to `null`. In that case the value is taken from the host group or the environment-wide configuration. |
| id | string | The Dynatrace entity ID of the host where OneAgent is deployed. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| setting | string | The auto-update state of OneAgents on the host:  * `ENABLED`: OneAgent automatically updates to the most recent version. * `DISABLED`: OneAgent updates to the version specified in the **version** field. * `INHERITED`: The setting from the host group (if the host is a member of a host group) or the environment-wide configuration (if the host doesn't belong to a host group) is used. The element can hold these values * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Version to update a OneAgent to when automatic updates are enabled.  Supports relative versions `latest`, `previous` and `older` as well as specific version in `<major>.<minor>` format (for example `1.261`) or `<major>.<minor>.<revision>.<timestamp>` format (for example `1.261.178.20230313-090930`).  Only applicable when the **setting** parameter is set to `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows |
| version | string | The version to which the OneAgent must be updated.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format (for example `1.191.0.20200326-161115`). You can fetch the list of available versions with the [GET available versionsï»¿](https://dt-url.net/fo23rb5) call.  If no suitable installer is found for the provided version or the value is set to `null`, OneAgent won't be updated.  Only applicable when the **effectiveSetting** value is `DISABLED`.  If the **setting** parameter is set to `INHERITED` but the **version** is still set, it will result in a one-time update: OneAgent will be updated to the specified version and the **version** value will be set to `null`. For further updates the parent setting will be used. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `UpdateWindowsConfig` object

Basic information about all configured update windows

| Element | Type | Description |
| --- | --- | --- |
| windows | [UpdateWindow[]](#openapi-definition-UpdateWindow) | List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience. |

#### The `UpdateWindow` object

Basic information about one maintenance window

| Element | Type | Description |
| --- | --- | --- |
| id | string | Identifier of maintenance window |
| name | string | The name of maintenance window |

#### The `MonitoringConfig` object

Monitoring configuration of OneAgent.

| Element | Type | Description |
| --- | --- | --- |
| autoInjectionEnabled | boolean | Code modules will be injected automatically into monitored applications if this setting is enabled. This setting won't apply if auto-injection is disabled via oneagentctl (see https://dt-url.net/oneagentctl). |
| id | string | The Dynatrace entity ID of the host where OneAgent is deployed. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| monitoringEnabled | boolean | The monitoring is enabled (`true`) or disabled (`false`). |
| monitoringMode | string | The monitoring mode for the host: full stack or infrastructure only. The element can hold these values * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |

#### The `TechMonitoringConfigList` object

A list of technology monitoring configurations.

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| technologies | [Technology[]](#openapi-definition-Technology) | A list of technology monitoring configurations. |

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



"autoUpdateConfig": {



"effectiveSetting": "DISABLED",



"effectiveVersion": "1.191.0.20200326-161115",



"id": "HOST-0123456789ABCDE",



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



"setting": "DISABLED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



},



"version": "1.191.0.20200326-161115"



},



"id": "HOST-0123456789ABCDE",



"monitoringConfig": {



"autoInjectionEnabled": true,



"id": "HOST-0123456789ABCDE",



"metadata": {},



"monitoringEnabled": true,



"monitoringMode": "FULL_STACK"



},



"techMonitoringConfigList": {



"metadata": {},



"technologies": [



{



"monitoringEnabled": true,



"scope": "ENVIRONMENT",



"type": "JAVA"



}



]



}



}
```