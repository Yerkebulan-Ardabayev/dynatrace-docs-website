---
title: Monitor Azure Functions on Plans for Windows
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions
---

# Monitor Azure Functions on Plans for Windows

# Monitor Azure Functions on Plans for Windows

* How-to guide
* 6-min read
* Updated on Jul 31, 2026

## Prerequisites

* Create a token to download and setup OneAgent:

  + [Platform tokens](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). Use Platform tokens to access the for following services:

    - fleet-management:oneagents:download
    - fleet-management:cluster-id:read
    - fleet-management:oneagent.tokens:read
  + [API Tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas "Learn the concept of an access token and its scopes.")
* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
* Determine your server URL if required.

  The server URL is required only if you use either of the following:

  + a Dynatrace Managed endpoint
  + an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint

  (For Dynatrace SaaS, the URL is automatically generated from the environment ID.)

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)
  + **Dynatrace Managed server URL:**  
    `https://{your-domain}/e/{your-environment-id}/api`

  If you're using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.

## Install Dynatrace OneAgent site extension

There are two ways to install the Dynatrace OneAgent site extension: via Azure portal or using an ARM template. Follow the steps below for instructions.

### Install Dynatrace OneAgent site extension via Azure portal

Consumption Plan

If you are on the Consumption plan you need to first stop Azure Function before running the site-extension installation process. You then need to restart Azure Functions once all steps have been completed.

1. In Azure Portal, go to **Azure Functions** and select an app service where you want to add the OneAgent extension.
2. In the left menu, go to to **Development Tools** > **Extensions**.
3. Select **Add**.
4. Select **Choose an Extension**.
5. From the list of extensions, select Dynatrace OneAgent.
6. Accept legal terms and select **Add**. It should take a moment until you see the **Dynatrace OneAgent** extension in the list.
7. In the left menu, go to to **Development Tools** > **Advanced Tools** and select **Go**. This will redirect you to the Kudu site.

   ![Kudu site](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)

   Kudu site
8. Select **Site extensions**.
9. Select **Launch** on the Dynatrace tile.
10. On the **Start monitoring your App Functions instance** page, enter the relevant configuration details. See the [Prerequisites](#prerequisites) section for details.
11. Select **Install OneAgent**.
12. Restart the application to recycle the application's worker process
13. To check the deployment status, go to the **Fleet Management app in Dynatrace**.

After restart, OneAgent starts monitoring your application automatically.

Select only the technologies you need to reduce download time and package size. By default, all technologies are included, which increases the package size.

### Install Dynatrace OneAgent site extension using an ARM template

Alternatively to the main installation method via Azure portal, you can make the Dynatrace site extension part of your ARM templates.  
Example configuration:

```
{



"apiVersion": "2016-08-01",



"name": "[parameters('resourceName')]",



"type": "Microsoft.Web/sites",



"properties": {



"name": "[parameters('resourceName')]",



"siteConfig": {



"alwaysOn": true,



"appSettings": [



{ "Name": "DT_TENANT", "Value": "<Environment-ID>" },



{ "Name": "DT_API_TOKEN", "Value": "<PaaS-Token>" },



{ "Name": "DT_API_URL", "Value": "<Server-Url>" },



{ "Name": "DT_SSL_MODE", "Value": "default" }



]



},



"serverFarmId": "[resourceId('Microsoft.Web/serverfarms', parameters('resourceName'))]"



},



"dependsOn": [



"[concat('Microsoft.Web/serverfarms/', parameters('resourceName'))]"



],



"location": "[parameters('location')]",



"resources": [



{



"apiVersion": "2016-08-01",



"name": "Dynatrace",



"type": "siteextensions",



"dependsOn": [



"[resourceId('Microsoft.Web/sites', parameters('resourceName'))]"



],



"properties": { }



}



]



}
```

| Parameter | Requirement | Description |
| --- | --- | --- |
| `DT_TENANT` | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| `DT_API_TOKEN` | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| `DT_API_URL` | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| `DT_SSL_MODE` | Optional | To automatically accept all self-signed TLS certificates, set the value to `all`. |
| `DT_TECH` | Optional | The OneAgent technology to install. By default, all technologies are installed. |
| `DT_AGENT_VERSION` | Optional | The OneAgent version to install. By default, the latest version is installed. |

If `AlwaysOn` isn't set to `true`, the installation of OneAgent is triggered on the start-up/first request to Kudu.

To check the deployment status, go to **Deployment Status**.

After installation is complete, go to Azure portal and restart the App Function application to recycle the application's worker process. Immediately after restart, OneAgent will begin monitoring your application.

## Automate the installation and update of Dynatrace OneAgent site extension with Kudu REST API

After you install the Dynatrace OneAgent site extension, you can use the **Kudu REST API** to automate installation and update of the Dynatrace OneAgent site extension.

The root URL to access the REST API is `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, where you need to replace `<Your-AppService-Subdomain>` with your own value. To authenticate, you can use either the user publishing credentials or the site-level credentials.

### Kudu REST API endpoints

| Method | Endpoint | Parameters/Response | Example |
| --- | --- | --- | --- |
| GET | `/api/status`  Returns the current status of the OneAgent installation. | **Response:**  The `state` field can be:  * `NotInstalled` * `Downloading` * `Installing` * `Installed` * `Failed`  For automation, use `isAgentInstalled` and `isUpgradeAvailable` to determine whether OneAgent is installed and whether an upgrade is available. | ```  {  "state": "Installed",  "message": "OneAgent installed",  "version": "1.157",  "latestVersion": "1.343.77.20260727-122922",  "isAgentInstalled": true,  "isUpgradeAvailable": false  } ``` |
| GET | `/api/settings`  Returns the current settings, including Dynatrace credentials. | **Response:**  The value for `apiUrl` can be left empty for a SaaS environment. | ```  {  "apiUrl": "",  "apiToken": "<your-api-token>",  "environmentId": "<your-environment-id>",  "sslMode": "Default",  "tech": "All",  "agentVersion": "1.343.77.20260727-122922",  "monitoredCLR": "Both"  } ``` |
| PUT | `/api/settings`  Starts OneAgent installation with the given settings. These settings are stored only if the installation finishes successfully.  If an update is available in the status request, this `PUT` request can be used to start the upgrade. | **Parameters:**  Send the data in the format received by the `GET /dynatrace/api/settings` request.  * `apiUrl` * `tech` * `agentVersion` * `monitoredCLR`  To check all available versions, use the [Deployment API - List available versions of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.").  **Response:** Empty response | ```  {  "apiUrl": "string",  "apiToken": "string",  "environmentId": "string",  "sslMode": "Default",  "monitoredCLR": "Both",  "tech": "string",  "agentVersion": "string"  } ``` |

### Accepted values for each field

| Field | Accepted values |
| --- | --- |
| `tech` | * `All` * `Java` * `NodeJS` |
| `monitoredCLR` | * `Both` * `Clr` * `CoreClr` |
| `sslMode` | * `Default` * `AcceptAll` |

## Override OneAgent configuration

To override the default configuration, you can use the following parameters.

| Parameter | Description |
| --- | --- |
| `DT_CONNECTION_POINT` | Semicolon-separated list of communication endpoints |

How to add the DT\_CONNECTION\_POINT parameter in the Azure portal

1. In the Azure portal, select the web function you want to monitor.
2. Select **Settings** > **Configuration** > **Application Settings**.
3. Select **New application setting**.
4. Enter the following key/value pair:

   * Name: `DT_CONNECTION_POINT`
   * Value: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` with your own value.

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)

   DT connection
5. Select **OK** to save the configuration.

## Update OneAgent

Dynatrace doesn't provide OneAgent updates on Azure Functions automatically. To update OneAgent on Azure Functions:

1. Go to Azure portal, browse to your site extension, and, if an update is available, select **Update**. You can monitor the progress until the update is finished.
2. Restart Azure Functions to recycle the application worker process.

If you're on a **Consumption Plan**, stop Azure Functions before the update and restart them after the update.

The extension provides its own REST API for automating OneAgent updates. For details, see the Kudu REST API section above.

### Update the site extension

To update the site extension on Azure Functions, go to the Azure portal, browse to your site extension, and, if an update is available, select **Update**.

An update to the site extension doesn't force an update to OneAgent.

## Uninstall OneAgent

Removing the extension also removes OneAgent.

If the application is running at the time of removal, the extension recognizes the running application, taking care to not remove any Dynatrace artifacts to prevent issues with the application. Instead, only the extension including the configuration is removed, so that, on the next restart of the application, OneAgent is no longer active.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [Serverless compute support matrix](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).")
* [Monitor Azure Functions on Plans for Linux](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/azure-function-linux "Learn how to enable OneAgent monitoring for Azure Functions running on Linux plans.")