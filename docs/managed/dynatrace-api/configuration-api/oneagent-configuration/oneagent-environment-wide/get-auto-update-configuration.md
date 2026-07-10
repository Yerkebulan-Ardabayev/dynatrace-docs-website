---
title: OneAgent environment-wide configuration API - GET auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide/get-auto-update-configuration
---

# OneAgent environment-wide configuration API - GET auto-update configuration

# OneAgent environment-wide configuration API - GET auto-update configuration

* Reference
* Published Oct 20, 2020

Gets the environment-wide configuration of OneAgent auto-update.

OneAgents that connect to the environment use this configuration only when their **setting** is set to `INHERITED`.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EnvironmentAutoUpdateConfig](#openapi-definition-EnvironmentAutoUpdateConfig) | Success |

### Response body objects

#### The `EnvironmentAutoUpdateConfig` object

Environment-wide configuration of OneAgents auto-updates.

Applies to all OneAgents connecting to the environment if their **setting** parameter is set to `INHERITED`. Otherwise, the host group or host level setting applies.

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| setting | string | The auto-update state of OneAgents connecting to the environment:  * `ENABLED`: OneAgents automatically update to the most recent version. * `DISABLED`: OneAgents update to the version specified in the **version** field.  OneAgents that connect to the environment use this configuration only when their **setting** parameter is set to `INHERITED`. The element can hold these values * `ENABLED` * `DISABLED` |
| targetVersion | string | Version to update a OneAgent to when automatic updates are enabled.  Supports relative versions `latest`, `previous` and `older` as well as specific version in `<major>.<minor>` format (for example `1.261`) or `<major>.<minor>.<revision>.<timestamp>` format (for example `1.261.178.20230313-090930`).  Only applicable when the **setting** parameter is set to `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Basic information about all configured update windows |
| version | string | The version to which the OneAgent must be updated.  Specify the version in the `<major>.<minor>.<revision>` format (for example `1.181.0`) or `<major>.<minor>` format (for example `1.181`). You can fetch the list of available versions with the [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m) call. If no suitable installer is found for the provided version or the value is set to `null`, OneAgent won't be updated.  Only applicable when the **setting** parameter is set to `DISABLED`. |

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
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience. |

#### The `UpdateWindow` object

Basic information about one maintenance window

| Element | Type | Description |
| --- | --- | --- |
| id | string | Identifier of maintenance window |
| name | string | The name of maintenance window |

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



"version": "1.181.0"



}
```