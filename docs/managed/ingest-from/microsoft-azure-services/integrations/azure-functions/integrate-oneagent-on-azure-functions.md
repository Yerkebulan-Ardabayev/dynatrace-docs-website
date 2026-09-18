---
title: Monitor Azure Functions on Plans for Windows
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions
---

# Monitor Azure Functions on Plans for Windows

# Monitor Azure Functions on Plans for Windows

* How-to guide
* 6-min read
* Updated on Aug 28, 2026

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

Dedicated Plan

Before you install the site extension, enable the Azure Functions OneAgent feature for the technology that you want to monitor:

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Filter for `azure function`.
3. Enable the feature for your technology.

## Install Dynatrace OneAgent site extension

There are two ways to install the Dynatrace OneAgent site extension: via Azure portal or using an ARM template. Follow the steps below for instructions.

### Install Dynatrace OneAgent site extension via Azure portal

Consumption Plan

If you use a Consumption Plan, stop the function app before you install the site extension. Restart the function app after you complete the installation.

1. In the Azure portal, open the function app that you want to monitor.
2. In the left menu, search for **Extensions** and select it.
3. Select **+ Add**.
4. Select **Choose an extension**, search for **Dynatrace OneAgent**, and select it.
5. Accept the legal terms and select **Add**.
6. Wait for the extension to install and refresh the extensions list.

7. In the **Browse** column for **Dynatrace OneAgent**, select the icon to open the extension configuration page in a new tab.
8. Enter your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") and [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas "Learn the concept of an access token and its scopes."), as described in [Prerequisites](#prerequisites). For Managed environments, also go to the **Optional** section and enter the **Server URL**. Ensure the URL ends with `/api`. For example, `https://{your-server-url}/api`.

9. Select the **Technology** that you want to monitor.
10. Select **Refresh versions** and choose a OneAgent version. If you don't choose one, the extension defaults to the latest version.
11. Select **Install OneAgent** and wait for the installation to finish. The page displays the required OneAgent environment variables, with an Azure CLI command at the bottom to set them. The Azure CLI command is shown for Consumption and Premium plans, but not for Dedicated plans.
12. Run the provided Azure CLI command to add the required application settings.

13. Return to the extension configuration page and verify that all configuration values are set.
14. In the Azure portal, refresh and restart the function app.

Monitoring starts automatically

After restart, OneAgent starts monitoring your application automatically.

Reduce package size

To reduce download time and package size, select only the technologies you need. By default, all technologies are included.

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

1. In the Azure portal, go to **Extensions** and select **Browse** for **Dynatrace OneAgent**. If an update is available, select **Update**. You can monitor the progress until the update is finished.
2. Restart Azure Functions to recycle the application worker process.

If you're on a **Consumption Plan**, stop Azure Functions before the update and restart them after the update.

### Update the site extension

To update the site extension on Azure Functions, go to **Extensions**, select **Browse** for **Dynatrace OneAgent**, and, if an update is available, select **Update**.

An update to the site extension doesn't force an update to OneAgent.

## Uninstall OneAgent

Removing the extension also removes OneAgent.

If the application is running at the time of removal, the extension recognizes the running application, taking care to not remove any Dynatrace artifacts to prevent issues with the application. Instead, only the extension including the configuration is removed, so that, on the next restart of the application, OneAgent is no longer active.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [Serverless compute support matrix](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).")
* [Monitor Azure Functions on Linux plans](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/azure-function-linux "Learn how to enable OneAgent monitoring for Azure Functions on Linux hosting plans, including runtime setup, environment variables, and package deployment.")