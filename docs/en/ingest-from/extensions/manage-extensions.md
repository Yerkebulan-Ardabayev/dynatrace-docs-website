---
title: Manage Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/manage-extensions
scraped: 2026-02-25T21:18:51.757835
---

# Manage Extensions

# Manage Extensions

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Dec 18, 2025

Manage Dynatrace extensions for hundreds of technologies.

## Prerequisites

### Permissions

hub:catalog:read

to get extensions details

storage:entities:read

read entities from storage

storage:logs:read

For reading Logs

storage:buckets:read

For reading any data

storage:system:read

Read system

storage:metrics:read

For reading metrics with DQL

settings:objects:read

Read settings objects

settings:objects:write

Write settings objects

state:user-app-states:read

For reading any data

state:user-app-states:write

Write user preferences

### Things to consider

If you can't access ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**, make sure you have the required [permissions](#permissions), specifically those starting with `extensions:configuration` and `extensions:definitions`. For additional information, refer to [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") and [IAM Policy - Read and write permissions on extensions configurationsï»¿](https://community.dynatrace.com/t5/Dynatrace-tips/IAM-Policy-Read-and-write-permissions-on-extensions/m-p/220907) in the Dynatrace Community.

## Overview

Extensions allows you to extend Dynatrace capabilities for data acquisition and domain expertise to hundreds of technologies. Extensions app is your central resource for managing and configuring Extensions 2.0.

![The Monitoring configurations tab lists the configurations that are available for each extension. Includes the extension version used by each configuration and the status of each configuration.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.42.png)![The Health tab shows the extension health per monitoring configuration.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.49.57.png)![Explore the logs related to the health of each extension.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.18.png)![Start monitoring new data sources.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.50.46.png)![Manage all Extensions 2.0 installed in your environment.](https://dt-cdn.net/hub/Screenshot_2025-07-07_at_14.51.26.png)

1 of 5The Monitoring configurations tab lists the configurations that are available for each extension. Includes the extension version used by each configuration and the status of each configuration.

## Dynatrace Hub

### Upload a custom extension from Dynatrace Hub

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** >  **Upload custom extension**.
2. Select your extension archive and upload it to Dynatrace.

Dynatrace Hub verifies the extension archive and structure and automatically enables it after a successful upload.

Most fields are pre-filled based on the extension YAML file. You can provide release notes information explaining why the extension version changed.

### Deploy an extension from Dynatrace Hub

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Discover**.
2. Find the extension from the list or use the search bar. All extensions already in your environment are marked with  **Installed**.
3. Select the tile of the extension you want to add, then select **Add to environment**.

You can now check the **Product information**, **Extension content**, **Available versions**, **Monitoring configurations**, and **Health** of your extension by selecting each of the tabs.

#### Define devices

Select **Add device** to define the devices from which you want to pull data and provide the device connection details:

* IP address or device name
* Port
* SNMP version and related authentication details

#### Start monitoring

Your extension appears in Dynatrace Hub. The next step is to provide the monitoring configuration for your extension. The detailed steps depend on your extension data source. For more information, see:

* [SNMP extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#activate-extension "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")
* [WMI extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#activate-extension "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")
* [Prometheus extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions#activate-extension "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")
* [Oracle SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#activate-extension "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")
* [Microsoft SQL extensions](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")

### Update an extension from Dynatrace Hub

To update an extension, simply upload a new version. Dynatrace Hub will automatically activate the new extension version.

Each update of the extension will overwrite the metric event configuration that may come with the extension. This means that any customizations made to the metric events settings will be reset to their default values upon updating the extension. It is advisable to take note of any custom configurations and reapply them after the update if necessary.

### Delete an extension from Dynatrace Hub

You can uninstall an extension or remove a version of that extension.

To uninstall an extension

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Manage**.
2. Find the extension you want to remove and select  >  **Uninstall**.

To delete extension versions

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** > **Manage**.
2. Select the extension tile to open the details.
3. Select **Available versions** >  **Uninstall**.

When you delete a version, Dynatrace Hub activates the latest available version.

## Dynatrace API

### API permissions

* You need an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the following permissions to manage the extension lifecycle:

  + API v2

    - Read extensions
    - Write extensions
    - Read extension environment configurations
    - Write extension environment configurations
    - Read extension monitoring configurations
    - Write extension monitoring configurations
  + API v1

    - Read configuration
    - Write configuration

### Upload an extension with Dynatrace API

Run the following command to upload the extension package to your environment. For this example, we use the Dynatrace SaaS URL:

```
curl -X POST "https://{env-id}.live.dynatrace.com/api/v2/extensions" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: multipart/form-data" \



-F "file=@MyCustomExtension.zip;type=application/zip"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `MyCustomExtension.zip` with the actual name of your extension package.

After a successful upload, the Dynatrace API returns basic extension details, including the extension name, version, and minimum Dynatrace version required to run the extension:

```
{



"extensionName":"custom:my.company.extension",



"version":"1.0.0",



"author":{



"name":"My Company"



},



"dataSources":[



],



"variables":[



],



"featureSets":[



],



"minDynatraceVersion":"1.213.0"



}
```

### Enable an extension with Dynatrace API

After you upload the extension to your environment, you need to enable the environment configuration. This step is necessary because you can upload up to 10 extension versions but you can use only one extension version at the time. When you activate the extension, you specify which extension version to use.

Run the following command to activate the extension in your environment. For this example, we use the Dynatrace SaaS URL.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



-d "{\"version\":\"{version}\"}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.

To determine the extension name, extract the extension package, extract the `extensions.zip` file from the package, and open the `extension.yaml` file.

After a successful activation, the Dynatrace API returns the version of the activated extension. For example:

```
{"version":"1.0.0"}
```

### Start monitoring with Dynatrace API

To start monitoring, you need to add at least one version of the monitoring configuration. The format of the JSON payload depends on the monitored data source.

```
curl -X POST "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName>/monitoringConfigurations" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



--data @{monitoring-configuration} -i
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.
* `{monitoring-configuration}` with the filename containing the JSON payload with the monitoring configuration. For details on the format, see [SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#monitoring-configuration "Learn how to create an SNMP extension using the Extensions framework.").

After a successful call, the Dynatrace API returns the `MonitoringConfigurationResponse` object. For example:

```
[



{ "objectId": "vu9U3hXa3q0AAAABACVleHQ6Y29tLmR5bmF0cmFjZS5zY2hlbWEtc25tcC1nZW5lcmljAAhhZ19ncm91cAAHRTJFVEVTVAAkMWMxZTlhMDctNzVkYi0zZjI0LWI4OGUtZmIxYWRiNGNjYTY4vu9U3hXa3q0", "code": 200 }



]
```

After a few minutes, go to [Metric browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") and search for the metrics you defined for your extension.

### Update extension with Dynatrace API

To update an extension, you need to upload the new extension package and enable the new environment configuration.

#### Upload updated extension package with API

To upload the package, use the same command you used to upload the initial version of the extension. You need to use the new extension package filename if it changed.

#### Enable new configuration version with API

To enable the environment configuration version, you need to add the version parameter to the API call. Use one of these methods to determine the version:

* After a successful upload, the Dynatrace API returns basic extension details, including the version.
* Find the version in the `extension.yaml` file inside the extension package.
* Run the [Get extension versions](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-extension-versions "Use the Dynatrace Extensions 2.0 API to view all available versions of an extension.") API call.

Run the following command to activate the new version. For this example, we use the Dynatrace SaaS URL.

```
curl -X PUT "https://{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token  {api-token}" \



-H "Content-Type: application/json; charset=utf-8" \



-d "{\"version\":\"{version}\"}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to activate.

After a successful activation, the Dynatrace API returns the version of the activated extension. For example:

```
{"version":"1.1.0"}
```

If you need to revert activation to an earlier version, run the command above with a different version parameter.

### Delete extension with Dynatrace API

If you uploaded a number of extension versions, you need to delete all the versions to completely remove the extension from your environment. You can use [GET extension versions](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-extension-versions "Use the Dynatrace Extensions 2.0 API to view all available versions of an extension.") to list all the extension versions available in your environment.

#### Delete environment configuration with API

To delete the currently active environment configuration, use [DELETE environment configuration](/docs/dynatrace-api/environment-api/extensions-20/environment-configurations/del-deactivate-env-config "Delete currently active environment configuration of an extension via the Dynatrace Extensions 2.0 API."). For this example, we use the Dynatrace SaaS URL.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/environmentConfiguration" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.

After a successful deactivation, the Dynatrace API returns the version of the deactivated extension. For example:

```
{"version":"1.1.0"}
```

#### Delete extension version with API

To delete an extension version, use [DELETE an extension version](/docs/dynatrace-api/environment-api/extensions-20/extensions/del-version "Delete an extension from your environment via the Dynatrace Extensions 2.0 API."). In this example, we use the Dynatrace SaaS URL.

```
curl -X DELETE "{env-id}.live.dynatrace.com/api/v2/extensions/{extensionName}/{version}" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Replace:

* `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](#prerequisites).
* `{extensionName}` with the actual extension name.
* `{version}` with the extension version you want to delete.

After a successful version deletion, the Dynatrace API returns the following response:

```
{



"extensionName":"custom:my.company.extension",



"version":"1.0.0",



"author":{



"name":"My Company"



},



"dataSources":[



],



"variables":[



],



"featureSets":[



],



"minDynatraceVersion":"1.213.0"



}
```

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Explore ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions** in Dynatrace Hub.](https://www.dynatrace.com/hub/detail/extension-manager/)