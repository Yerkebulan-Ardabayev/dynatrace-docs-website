---
title: Integrate OneAgent on Azure App Service for Windows
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service
scraped: 2026-02-21T21:13:45.014063
---

# Integrate OneAgent on Azure App Service for Windows

# Integrate OneAgent on Azure App Service for Windows

* Latest Dynatrace
* How-to guide
* 9-min read
* Published Oct 16, 2018

Azure App Service provides many different hosting options for Windows, Linux, and containers with shared infrastructure ([App Service planï»¿](https://dt-url.net/f4031wl)), or fully isolated and dedicated infrastructure ([Azure App Service Environmentï»¿](https://dt-url.net/u0231c3)).

## Capabilities

The App Service integration with Dynatrace provides the following capabilities:

* [Integration for OneAgent on Windows via an extension for easy deployment](#install)
* [Integration for OneAgent on Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")
* Automatic distributed tracing and monitoring for .NET/.NET Core, Java, Node.js, PHP, and IIS
* Enhanced capturing of Azure App Service metadata, such as SKU or Website-Name
* Capturing of platform-level metrics and [additional insights into your App-Service Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Monitor Azure App Service (App Service Plan, Web App Deployment Slot) and view available metrics.") via the [Azure Monitor integration](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Capturing of logs via [log forwarding](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

**Limitations**  
Since Azure App Service is a fully managed hosting platform, applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system. The OneAgent integration for Azure App Service uses the application-only or universal injection approach, which results in some differences from the Full-Stack OneAgent installation:

* I/O monitoring requires that you enable [Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), which also provides [additional insights into your App-Service Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Monitor Azure App Service (App Service Plan, Web App Deployment Slot) and view available metrics.")
* Capturing logs requires that you enable [log forwarding](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* Automatic OneAgent updates need to be triggered via the [Dynatrace OneAgent site extension REST API](#restapi)
* Hostgroup configuration is not available

## Install Dynatrace OneAgent site extension

Windows only

Dynatrace provides a [site extensionï»¿](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) to install OneAgent on Azure App Services on Windows.

For Azure App Service on Linux or containers, see [Integration for OneAgent on Azure App Service on Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.").

Site extension is the native extension mechanism provided via [Kuduï»¿](https://github.com/projectkudu/kudu), which is the deployment management engine behind Azure App Services.

The Dynatrace OneAgent site extension doesn't include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").

There are multiple ways to install the Dynatrace OneAgent site extension:

* [Manually, via Azure Portal](#portal)
* [Automatically, using an ARM template](#arm)
* [By automating the setup with a custom PowerShell script](#script)

See below for instructions.

### Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

### Manual install via Azure Portal

1. In Azure Portal, go to the **App Services** and select an app service where you want to add the OneAgent extension.
2. In the left menu, go to to **Development Tools** > **Extensions**.
3. Select **Add**.
4. Select **Choose an Extension**.
5. From the list of extensions, select Dynatrace OneAgent.
6. Accept legal terms and select **Add**. It should take a moment until you see the **Dynatrace OneAgent** extension on the list.
7. In the left menu, go to to **Development Tools** > **Advanced Tools** and select **Go**. This will redirect you to the Kudu site.

   ![Kudu site](https://dt-cdn.net/images/screenshot-2023-08-08-at-5-41-34-pm-1046-18f975f56f.png)
8. Select **Site extensions**.
9. Select **Launch** on the Dynatrace tile.
10. On the **Start monitoring your App Service instance** page, enter your environment ID, [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes."), and server URL. See [Prerequisites](#prerequisites) section for details.
11. Optional You can select **Accept all self-signed SSL certificates** to automatically accept all self-signed TLS certificates.
12. Select **Install OneAgent**.
13. To check the deployment status, go to **Deployment Status**.
14. After installation is complete, go to **Site extension** tab in Kudu and select **Restart Site**.
15. Restart the App Service application to recycle the application's worker process

After restart, OneAgent starts monitoring your application automatically.

### Automatic install using an ARM template



As an alternative to installing via Azure Portal, you can make the Dynatrace site extension part of your ARM templates.

ARM Template

Note that the example configuration provided below is a template and some values need to be modified.

Example configuration:

dynatrace-oneagent-site-extension.json

```
{



"$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",



"contentVersion": "1.0.0.0",



"parameters": {



// WebApp Settings



"siteName": {



"type": "string",



"metadata": {



"description": "Web app name where you would like to install extension."



}



},



"location": {



"type": "string",



"metadata": {



"description": "Region of your web app."



}



},



"skuCapacity": {



"type": "int",



"defaultValue": 1,



"minValue": 1,



"metadata": {



"description": "Describes plan's instance count."



}



},



"skuName": {



"type": "string",



"defaultValue": "B1",



"allowedValues": [



"B1",



"B2",



"B3",



"D1",



"F1",



"I1",



"I1v2",



"I2",



"I2v2",



"I3",



"I3v2",



"P1V2",



"P1V3",



"P2V2",



"P2V3",



"P3V2",



"P3V3",



"PC2",



"PC3",



"PC4",



"S1",



"S2",



"S3"



],



"metadata": {



"description": "Describes plan's pricing tier and instance size. Check details at https://azure.microsoft.com/en-us/pricing/details/app-service/."



}



},



"webAppAlwaysOn": {



"type": "bool",



"metadata": {



"description": "If AlwaysOn isn't set to true, installation of OneAgent is triggered on the start-up/first request to Kudu."



},



"defaultValue": true



},



// Dynatrace OneAgent site extension settings



"environmentID": {



"type": "string",



"metadata": {



"description": "The environment ID."



}



},



"APIToken": {



"type": "string",



"metadata": {



"description": "The PaaS token."



}



},



"APIUrl": {



"type": "string",



"metadata": {



"description": "The server URL, if you want to configure an alternative communication endpoint."



}



},



"SSLMode": {



"type": "string",



"metadata": {



"description": "To automatically accept all self-signed TLS certificates, set the value to all."



},



"allowedValues": ["default", "all"],



"defaultValue": "default"



},



"monitoredCLR": {



"type": "string",



"metadata": {



"description": "Your .NET application runtime"



},



"allowedValues": ["both", "coreclr", "clr"],



"defaultValue": "both"



},



"networkZone": {



"type": "string",



"metadata": {



"description": "Your network zone. Set the value you want for your App Service instance. See network zones for more information."



},



"defaultValue": ""



}



},



"resources": [



{



"apiVersion": "2020-12-01",



"name": "[parameters('siteName')]",



"type": "Microsoft.Web/serverfarms",



"location": "[parameters('location')]",



"sku": {



"name": "[parameters('skuName')]",



"capacity": "[parameters('skuCapacity')]"



},



"properties": {



"name": "[parameters('siteName')]"



}



},



{



"apiVersion": "2020-12-01",



"name": "[parameters('siteName')]",



"type": "Microsoft.Web/sites",



"properties": {



"name": "[parameters('siteName')]",



"siteConfig": {



"alwaysOn": "[parameters('webAppAlwaysOn')]",



"appSettings": [



{ "Name": "DT_TENANT", "Value": "[parameters('environmentID')]" },



{ "Name": "DT_API_TOKEN", "Value": "[parameters('APIToken')]" },



{ "Name": "DT_API_URL", "Value": "[parameters('APIUrl')]" },



{ "Name": "DT_SSL_MODE", "Value": "[parameters('SSLMode')]" },



{ "Name": "DT_MONITORED_CLR", "Value": "[parameters('monitoredCLR')]" },



{ "Name": "DT_NETWORK_ZONE", "Value": "[parameters('networkZone')]" }



]



},



"serverFarmId": "[resourceId('Microsoft.Web/serverfarms', parameters('siteName'))]"



},



"dependsOn": ["[concat('Microsoft.Web/serverfarms/', parameters('siteName'))]"],



"location": "[parameters('location')]",



"resources": [



{



"apiVersion": "2020-12-01",



"name": "Dynatrace",



"type": "siteextensions",



"dependsOn": ["[resourceId('Microsoft.Web/sites/', parameters('siteName'))]"]



}



]



}



],



"outputs": {}



}
```

| WebApp parameter | Requirement | Description |
| --- | --- | --- |
| siteName | Required | WebApp name where you would like to install extension. |
| location | Required | Region of your WebApp. For available regions, see [Azure documentationï»¿](https://azure.microsoft.com/en-us/global-infrastructure/services/?products=app-service). |
| skuCapacity | Optional | How many instances you can run under your plan. |
| skuName | Optional | The plan's pricing tier and instance size. For pricing details, see [Azure documentationï»¿](https://azure.microsoft.com/en-us/pricing/details/app-service/). |
| webAppAlwaysOn | Optional | If `AlwaysOn` isn't set to `true`, OneAgent installation is triggered at startup (on the first request to Kudu). |

| Dynatrace parameter | Requirement | Description |
| --- | --- | --- |
| environmentID | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| APIToken | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| APIUrl | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| SSLMode | Optional | To automatically accept all self-signed TLS certificates, set the value to `all`. |
| networkZone | Optional | Your network zone. Set the value you want for your App Service instance. See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information. |
| monitoredCLR | Optional | Set the value to `clr` if your application is running on .NET, or `coreclr` if your application is running on .NET Core, default value is `both` |

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart the App Service application to recycle the application's worker process. After restart, OneAgent starts monitoring your application automatically.

### Automate the installation using a PowerShell script

You can automate the installation with a PowerShell script that uses the [Kudu REST APIï»¿](https://dt-url.net/0h031rk), [OneAgent site extension REST API](#restapi), as well as the [Azure CLIï»¿](https://dt-url.net/4j2318w). A sample implementation is available in the [Dynatrace GitHub repositoryï»¿](https://dt-url.net/9s031v4).

## Dynatrace OneAgent site extension REST API

The Dynatrace OneAgent site extension provides a REST API to automate OneAgent installation, configuration, and update.

The root URL to access the REST API is `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, where you need to replace `<Your-AppService-Subdomain>` with your own value. To authenticate, you can use either the user publishing credentials or the site-level credentials. For details, see [Accessing the Kudu serviceï»¿](https://dt-url.net/em4316d).

| Method | Endpoint | Description | Response |
| --- | --- | --- | --- |
| GET | /api/status | Returns the current status of the OneAgent installation.  The returned `state` field can be: - `NotInstalled` - `Downloading` - `Installing` - `Installed` - `Failed`  For automation purposes, use the **isAgentInstalled** and **isUpgradeAvailable** fields to check whether the OneAgent is installed and whether an upgrade is available. | `{`  `"state": "Installed",`  `"message": "OneAgent installed",`  `"version": "1.157",`  `"isAgentInstalled": true,`  `"isUpgradeAvailable": false,`  `"isFunction": false,`  `"functionAppSettings": null` `}` |
| GET | /api/settings | Returns the current settings, including Dynatrace credentials. | `{` `"apiUrl": "",` `"apiToken": "<your-api-token>",` `"environmentId": "<your-environment-id>",` `"sslMode": "Default"` `}` |
| PUT | /api/settings | Starts OneAgent installation with the given settings. These settings are stored only if the installation finishes successfully.  In the payload, you need to send the data in the same format as received by the `GET /dynatrace/api/settings` request.  If there's an update available in the status request, this `PUT` request can be used to start the upgrade. **Notes:** \* The value for `apiUrl` can be left empty for a SaaS environment. \* For `sslMode`, if you want to validate the HTTPS connection, leave it as `Default`. If you don't want to validate the HTTPS connection, set it to `AcceptAll`. | Empty response |

## Using multiple deployment slots

Because Azure App Service deployment slots are treated like full-fledged application service instances, you need to enable the site extension for OneAgent on each deployment slot you want to monitor with Dynatrace.

For details on configuring deployment slots, consult the [Microsoft documentationï»¿](https://dt-url.net/uo631ry).

If you're using application settings to additionally configure certain OneAgent options, make sure the additional settings are also applied to the deployment slots.

## Using App Service built-in authentication and authorization

If you use App Service [built-in authentication and authorization capabiltiesï»¿](https://dt-url.net/m2831x1) (also referred to as "Easy Auth"), App Service starts an additional .NET CLR instance, which makes OneAgent instrument the Easy Auth module instead of your application's instance as the leading instance.

In this case, if your application process isn't instrumented, you need to set the `DT_MONITORED_CLR` environment variable to instance that your application is running on: `clr` or `coreclr`.
You can set this variable in Azure Portal (**Settings** > **Configuration** > **Application Settings**).

## Override OneAgent configuration



To override the default configuration, you can use the following parameters.

| Parameter | Description |
| --- | --- |
| DT\_CONNECTION\_POINT | Semicolon-separated list of communication endpoints |
| DT\_MONITORED\_CLR | Variable to instrument a specific .NET/.NET Core CLR instance |

How to add the `DT_CONNECTION_POINT` parameter in Azure Portal

1. In Azure Portal, select the web application you want to monitor.
2. Select **Settings** > **Configuration** > **Application Settings**.
3. Select **New application setting**.
4. Enter the configuration key/value pair like this.

   * Name: `DT_CONNECTION_POINT`
   * Value: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` with your own value.

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)
5. Select **OK** to save the configuration.

## Using Application Insights

OneAgent may not be able to instrument your .NET/.NET Core application if you use Application Insights with runtime instrumentation enabled. This is because OneAgent and Application Insights try to use the same interface to inject at runtime.

Please review your Application Insights configuration for Asp.Net, where you can [turn off runtime instrumentationï»¿](https://dt-url.net/z1a31yy) or [Asp.Net Core auto-instrumentationï»¿](https://dt-url.net/ikc31s6).

While you may still be able to use Application Insights in basic mode or SDK in parallel with Dynatrace OneAgent, please note that this may cause other issues or significant monitoring overhead to your applications and isn't recommended.

## Update the Dynatrace OneAgent site extension

To update the Dynatrace OneAgent site extension

1. In Azure Portal, go to your Azure App Service with Dynatrace OneAgent site extension.
2. If an update is available, select **Update**.

When upgrading the extension from version 1.x to version 2.x, if you have **Always On** selected on your App Service, the upgrade of OneAgent is either triggered automatically or on the first request to the UI extension. If you don't have **Always On** selected, you must restart App Service, so that the extension process starts.

An update to the Dynatrace OneAgent site extension doesn't force a OneAgent update. To update OneAgent, see [Dynatrace OneAgent](#update-oa).

### Update OneAgent

The Dynatrace OneAgent site extension doesn't provide Dynatrace OneAgent updates automatically. To update Dynatrace OneAgent on Azure App Service

1. In Azure Portal, go to your Azure App Service with Dynatrace OneAgent site extension.
2. In the **Development Tools** section, choose **Advanced Tools** and select **Go**. This will redirect you to the KUDU website.
3. Go to **Site extensions** > **Installed** > **Dynatrace**.
4. If an update is available, select **Upgrade OneAgent**.

You can monitor the progress until the update is complete, and then restart App Service to recycle the application worker process.

## Automate OneAgent updates

To automate OneAgent update, the Dynatrace OneAgent site extension provides a REST API that can be used to trigger updates. See [REST API](#restapi) for details.

## Uninstall Dynatrace OneAgent site extension

Removing the Dynatrace OneAgent site extension also removes Dynatrace OneAgent.
If the application is running at the time of removal, the site extension recognizes the running application and, to prevent issues with the application, does not remove any Dynatrace artifacts. Instead, only the site extension, including the configuration, is removed, so that Dynatrace OneAgent is no longer active the next time the application restarts.

## Monitoring consumption

For Azure App Service, monitoring consumption is based on host units. See [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") for details.

## Troubleshooting

* [No route registered for /dynatrace/ when accessing the site extensionï»¿](https://dt-url.net/44038l8)
* [503 Service Unavailable for Web App and Kuduï»¿](https://dt-url.net/o62387e)
* [Node.js app does not get instrumentedï»¿](https://dt-url.net/n7238ds)
* [Site extension overrides JAVA\_OPTSï»¿](https://dt-url.net/rt438wk)
* [Failed to install: Could not find fileï»¿](https://dt-url.net/wr438gk)

Location of log files

* The log files for the extension are in the extensions folder: `D:\home\SiteExtensions\Dynatrace\`.
* OneAgent log files are located in `D:\home\SiteExtensions\Dynatrace.Agent\x.xxx.xxx.xxxxxxxx-xxxxxx\log`. You might have multiple `D:\home\SiteExtensions\Dynatrace.Agent\` subdirectories caused by agent updates.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")