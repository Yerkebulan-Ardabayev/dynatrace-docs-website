# Dynatrace Documentation: ingest-from/microsoft-azure-services

Generated: 2026-02-18

Files combined: 121

---


## Source: azure-aks.md


---
title: Azure Kubernetes Service (AKS)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks
scraped: 2026-02-18T05:39:52.748181
---

# Azure Kubernetes Service (AKS)

# Azure Kubernetes Service (AKS)

* Latest Dynatrace
* Overview
* 1-min read
* Published May 04, 2020

Dynatrace OneAgent provides extensive monitoring of **Azure Kubernetes Service** pods, nodes, and clusters. The OneAgent deployment process is consistent with other distributions.

In addition you can enable capturing AKS specific metrics from Azure Monitor

## Integration

[Enable Kubernetes monitoring](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")

[Azure Monitor AKS metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service "Monitor Azure Kubernetes Service and view available metrics.")

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")


---


## Source: integrate-oneagent-on-azure-app-service.md


---
title: Integrate OneAgent on Azure App Service for Windows
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service
scraped: 2026-02-17T04:51:38.309392
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

## Troubleshoot

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


---


## Source: integrate-oneagent-on-web-app-for-containers.md


---
title: Integrate OneAgent on Azure App Service for Linux and containers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers
scraped: 2026-02-18T05:49:16.586606
---

# Integrate OneAgent on Azure App Service for Linux and containers

# Integrate OneAgent on Azure App Service for Linux and containers

* Latest Dynatrace
* How-to guide
* 11-min read
* Updated on Dec 17, 2025

Linux only

App Service on Linux supports two scenarios.

* **Bring your own code**

  In the code scenario, App Service provides a base container that is maintained by the platform.

  This container targets:

  + A development framework, such as .NET Core, PHP, or Node.js.
  + A version of that framework, such as .NET Core 3.0 or .NET Core 3.1.

  Follow the procedure on the **Built-in image** tab.
* **Bring your own container**

  In the container scenario, App Service provides a host where a custom container provided by the customer can execute.

  For details on the differences between the two scenarios, see [Things you should know: Web Apps on Linuxï»¿](https://dt-url.net/jm039gu).

  To monitor App Services on Linux, you need to integrate OneAgent within your containerized application.

  Follow the procedure on the **Custom image** tab.

Built-in image

Custom image

## Integrate Dynatrace on built-in image

Azure App Service for Linux allows you to customize its base container at runtime using a [startup script or script commandï»¿](https://dt-url.net/z2234qa) that must be executed in a bash shell or [Azure Cloud Shellï»¿](https://dt-url.net/at034yy). The script can be configured in multiple ways.

### Set startup script command/file at creation time using Azure CLI

```
az webapp create -n <my-app> -g <my-resourcegroup> -p <my-appservice-plan> --runtime <runtime-tag> --startup-file <startup-script/command>
```

### Set script command/file at creation time for an existing App Service

```
az webapp config set -n <my-app> -g <my-resourcegroup> --startup-file <startup-script/command>
```

### Set script command/file using ARM template

Use the [appCommandLineï»¿](https://docs.microsoft.com/en-us/azure/templates/microsoft.web/sites/config-web?pivots=deployment-language-arm-template#siteconfig-1) property of your ARM template to set the startup script/command.

```
{



"acrUseManagedIdentityCreds": false,



"acrUserManagedIdentityId": null,



"alwaysOn": false,



"apiDefinition": null,



"apiManagementConfig": null,



"appCommandLine": "<startup-script/command>",



"appSettings": null,



"autoHealEnabled": false,



"autoHealRules": null,



"autoSwapSlotName": null,



...
```

### Set startup script command/file in the Azure portal

![AppService Linux Portal Startup](https://dt-cdn.net/images/screenshot-2022-12-13-at-13-42-44-1109-8955530cdd.png)

### Script or command?

A startup script is the same as a startup command: it's a command that executes the script (remember to use the path of the script). However, this requires that you package the script along with your application. If you don't want to have this dependency, use startup commands.

The script/command is executed within the container init script, which is implemented differently on each technology stack.

For details on startup commands, see the Azure App Service for Linux documentation on [What are the expected values for the Startup File section when I configure the runtime stack?ï»¿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

### Integrate Dynatrace using a startup script/command

To integrate Dynatrace, the startup script/command needs to have access to a few variables.

Parameter

Description

`$DT_ENDPOINT`

Your Dynatrace API server endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

`$DT_API_TOKEN`

API Token to access the Dynatrace REST APIâ[create an API Token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the **InstallerDownload** scope.

`$DT_INCLUDE`

Configure required code modules, depending on the used technology stack.

* `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
* Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

For details, see [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").

`$START_APP_CMD`

The command to start your application

[What are the expected values for the Startup File section when I configure the runtime stack?ï»¿](https://docs.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#what-are-the-expected-values-for-the-startup-file-section-when-i-configure-the-runtime-stack-)

If you use a shell other than bash, make sure to adapt the script appropriately to the shell's character escape requirements.

You can do this in two ways.

* App service settings Recommended
* Setting the values inline

#### Monitoring PHP on NGINX

To monitor both PHP-FPM and NGINX

1. Set `DT_INCLUDE` to `all`.
2. Use the startup script with two additional commands at the end.

   ```
   echo '/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so' >> /etc/ld.so.preload



   /etc/init.d/nginx restart
   ```

#### App service settings

Set the values of the above parameters using [App Settingsï»¿](https://dt-url.net/da239ts)âthis is equivalent to setting environment variablesâand then run this command.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && sh /tmp/installer-wrapper.sh
```

Java Runtime stack

For apps running on the Java Runtime stack in Azure App Service, this installation method may not work as expected in some cases. For example, customers have reported issues with Alpine-based images, where the above command was interpreted as a single string rather than executed as a shell command. This caused the `&&` operator to be treated as part of the `wget` input instead of chaining commands.

If you encounter this behavior, consider using an alternative approach to execute the script (such as a custom startup script or modifying a [custom image](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#install--custom-image "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")).

Alternatively, you can use the calling-only script below, which works for all Linux images.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



sh $installerWrapperInstallationPath
```

#### Setting the values inline

You can set the needed variables only for the command that runs the OneAgent installer.

To do this, you need to set the values before the command as shown below.

```
wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh
```

Alternatively, you can use the startup file as shown below.

```
#!/bin/sh



readonly installerWrapperInstallationPath=/tmp/installer-wrapper.sh



readonly installerWrapperURL=https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh



wget -O $installerWrapperInstallationPath -q $installerWrapperURL



DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh $installerWrapperInstallationPath
```

### Example: Integrate into a node.js application using Azure CLI within a bash shell

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configure the startup command**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-1 "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Restart the web application twice**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers#step-2 "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

#### Step 1 Configure the startup command

```
RESOURCE_GROUP="my-appservice-test"



APPSVC="my-linux-webapp"



DT_ENDPOINT="https://XXXXXX.live.dynatrace.com"



DT_API_TOKEN="XXXXXX"



DT_INCLUDE="nodejs"



START_APP_CMD="pm2 start index.js --no-daemon"



STARTUP_CMD="wget -O /tmp/installer-wrapper.sh -q https://raw.githubusercontent.com/dynatrace-oss/cloud-snippets/main/azure/linux-app-service/oneagent-installer.sh && DT_ENDPOINT=$DT_ENDPOINT DT_API_TOKEN=$DT_API_TOKEN DT_INCLUDE=$DT_INCLUDE START_APP_CMD=$START_APP_CMD sh /tmp/installer-wrapper.sh"



az webapp config set --resource-group $RESOURCE_GROUP --name $APPSVC --startup-file "$STARTUP_CMD"
```

#### Step 2 Restart the web application twice

After you configure the startup command, restart the web application **twice**.

* Restart once to initialize OneAgent installation.
* Restart again to start OneAgent instrumenting your application.

## Integrate Dynatrace on custom image

To integrate OneAgent with the application image, you have two options:

* [Integrate the OneAgent image layer provided by Dynatrace](#layer)
* [Download OneAgent artifacts at image build-time from Dynatrace REST API](#api)

### Option 1: Integrate using Dynatrace offered OneAgent image layer

This option requires that you have Docker v17.05+ installed on your computer.

1. Sign in to Docker with your Dynatrace environment ID as the username and your PaaS token as the password.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Add the following lines to your application image Dockerfile, after the last `FROM` command.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Replace the following placeholders in the template.

   Parameter

   Description

   `<ADDRESS>`

   Your Dynatrace registry endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

   `<TECHNOLOGY>`

   Configure required code modules, depending on the used technology stack.

   * `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
   * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

   For details, see the [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").

   **What if my Docker image is based on Alpine Linux?**

   Dynatrace OneAgent supports Alpine Linuxâbased environments. To use an Alpine Linux compatible OneAgent, use image name `oneagent-codemodules-musl` (as shown in the adapted template below) instead of `oneagent-codemodules`.

   ```
   COPY --from=<ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
3. Build your application image.

   Build the Docker image from your Dockerfile to use it in your Kubernetes environment.

   ```
   docker build -t yourapp .
   ```
4. Restart the web application **twice**.

   * Restart once to initialize the OneAgent install script.
   * Restart again to start OneAgent on the host.

### Option 2: Integrate using installer script from Dynatrace REST API

1. Add the following two lines to your Dockerfile.

   ```
   RUN wget -O /tmp/installer.sh -q "<DT_ENDPOINT>/api/v1/deployment/installer/agent/unix/paas-sh/latest?Api-Token=<DT_API_TOKEN>&flavor=<DT_FLAVOR>&include=<DT_INCLUDE>" && sh /tmp/installer.sh



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   Replace the following parameters in the template above.

   Parameter

   Description

   `<DT_ENDPOINT>`

   Your Dynatrace API endpointâuse either your environment [cluster endpoint](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") or an [ActiveGate address](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

   `<DT_API_TOKEN>`

   API Token to access the Dynatrace REST APIâ[create an API Token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the **InstallerDownload** scope.

   `<DT_FLAVOR>`

   Configure the required architecture.

   * `default` for standard, glibc-based Linux images
   * `musl` for Alpine Linuxâbased images

   `<DT_INCLUDE>`

   Configure required code modules, depending on the used technology stack.

   * `all` includes all available OneAgent code modules (`java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, `sdk`), but it increases download package size.
   * Alternatively, choose identifiers appropriate to your application stack, such as `java`, `dotnet`, `nodejs`, or `php`.

   For details, see the [API documentation](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API.").
2. Build your application image.

   Build the Docker image from your Dockerfile to use it in your Kubernetes environment.

   ```
   docker build -t yourapp .
   ```
3. Restart the web application **twice**.

   * Restart once to initialize the OneAgent install script.
   * Restart again to start OneAgent on the host.

## Additional configuration Optional

Use additional environment variables to configure OneAgent for troubleshooting or advanced networking. You can either set them via your App Service Application settings or, when using a custom container image, configure them within your application image Dockerfile.

### Networking variables

Parameter

Description

`DT_NETWORK_ZONE`

Specifies to use a network zone. For more information, see [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

`DT_PROXY`

When using a proxy, use this environment variable to pass proxy credentials. For more information, see [Set up OneAgent on containers for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

### Additional metadata for process grouping and service detection

When listing multiple tags, you need to put them in double quotes, for example: DT\_TAGS="Tag1=Value1 Tag2=Value2".

Parameter

Description

`DT_LOCALTOVIRTUALHOSTNAME`

Multiple containers are sometimes detected as a single instance (localhost), leading to various problems in, for example, service detection or availability alerts. Use this environment variable to define a unique name for your container instance. For details, see [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Find out how Dynatrace Service Detection v1 detects and names different types of services.")

`DT_APPLICATIONID`

Some technologies don't provide unique application names. In such cases, use this environment variable to provide a unique name. For more information, see [Web server naming issues](/docs/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Find out how Dynatrace Service Detection v1 detects and names different types of services.").

`DT_TAGS`

Applies [custom tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") to your process group.

`DT_CUSTOM_PROP`

Applies [custom metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") to your process group.

`DT_CLUSTER_ID`

If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use case, use this environment variable to **group all processes with the same value**.

`DT_NODE_ID`

If the [process group detection rules](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") won't work for your use case, use this environment variable to **separate process group instances**.

### Validating variables

Parameter

Description

`DT_LOGSTREAM`

Set this variable with `stdout` to configure the OneAgent to log errors to the console. To see additional OneAgent logs, set the log level with `DT_LOGLEVELCON` as follows.

`DT_LOGLEVELCON`

Use this environment variable to define the console log level. Valid options are: `NONE`, `SEVERE`, and `INFO`.

`DT_AGENTACTIVE`

Set to `true` or `false` to enable or disable OneAgent.

## Update OneAgent

Built-in image

Custom image

When an update is available, restart your application to update OneAgent.

Each time you want to leverage a new version of Dynatrace OneAgent, you need to rebuild your local OneAgent code modules and application image. Any newly started pods from this application image will be monitored with the latest version of OneAgent.

If you've specified a default OneAgent installation version for new hosts and applications using [OneAgent update settings](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), your web apps will be automatically monitored by the defined default version of OneAgent.

## Uninstall OneAgent

Built-in image

Custom image

To uninstall OneAgent

1. In Azure portal, go to your web application > **Configuration** > **General settings**.
2. Remove your startup command (leave **Startup Command** empty).
3. Select **Save**.

To uninstall OneAgent, remove references from above described Dynatrace integration from your application image and redeploy the application.

## Potential conflict with Application Insights

OneAgent may conflict with Azure Application Insights agents already instrumenting the application. If you don't see any monitoring data coming in, check if you have turned on Application Insights and re-try with Application Insights turned off.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: monitor-app-service.md


---
title: Monitor Azure App Service Plan metrics
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service
scraped: 2026-02-18T05:58:15.861194
---

# Monitor Azure App Service Plan metrics

# Monitor Azure App Service Plan metrics

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for **Azure App Service Plan** used by your deployed App Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![App service plan](https://dt-cdn.net/images/dashboard-87-873-b330e8b901.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BytesReceived | Data in | Instance | Byte | âï¸ |
| BytesSent | Data out | Instance | Byte | âï¸ |
| CpuPercentage | CPU percentage | Instance | Percent | âï¸ |
| DiskQueueLength | Disk queue length | Instance | Count | âï¸ |
| HttpQueueLength | HTTP queue length | Instance | Count | âï¸ |
| MemoryPercentage | Memory percentage | Instance | Percent | âï¸ |
| SocketInboundAll | Socket inbound all |  | Count |  |
| SocketLoopback | Socket loopback | Instance | Count |  |
| SocketOutboundAll | Socket Outbound All |  | Count |  |
| SocketOutboundEstablished | Socket outbound established | Instance | Count |  |
| SocketOutboundTimeWait | Socket outbound time wait | Instance | Count |  |
| TcpCloseWait | TCP close wait | Instance | Count |  |
| TcpClosing | TCP closing | Instance | Count |  |
| TcpEstablished | TCP established | Instance | Count |  |
| TcpFinWait1 | TCP fin wait 1 | Instance | Count |  |
| TcpFinWait2 | TCP fin wait 2 | Instance | Count |  |
| TcpLastAck | TCP last ack | Instance | Count |  |
| TcpSynReceived | TCP syn received | Instance | Count |  |
| TcpSynSent | TCP syn sent | Instance | Count |  |
| TcpTimeWait | TCP time wait | Instance | Count |  |


---


## Source: azure-appservice.md


---
title: Monitor Azure App Service
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice
scraped: 2026-02-18T05:39:49.167762
---

# Monitor Azure App Service

# Monitor Azure App Service

* Latest Dynatrace
* Overview
* 1-min read
* Published Jan 16, 2023

Azure App Service provides many different hosting options for Windows, Linux, and containers with shared infrastructure ([App Service planï»¿](https://dt-url.net/f4031wl)), or fully isolated and dedicated infrastructure ([Azure App Service Environmentï»¿](https://dt-url.net/u0231c3)).

## Capabilities

The App Service integration with Dynatrace provides the following capabilities:

* [Integration for OneAgent on Windows via an extension for easy deployment](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service#install "Install, configure, update, uninstall, and troubleshoot OneAgent for monitoring Azure App Service on Windows using an Azure site extension.")
* [Integration for OneAgent on Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")
* Automatic distributed tracing and monitoring for .NET/.NET Core, Java, Node.js, PHP, and IIS
* Enhanced capturing of Azure App Service metadata, such as SKU or Website-Name
* Capturing of platform-level metrics and [additional insights into your App-Service Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service "Monitor Azure App Service (App Service Plan, Web App Deployment Slot) and view available metrics.") via the [Azure Monitor integration](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Capturing of logs via [log forwarding](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

## Related topics

* [Serverless monitoring](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")


---


## Source: azure-arc-enabled-servers.md


---
title: Microsoft Azure Arc-enabled servers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers
scraped: 2026-02-17T21:28:10.737984
---

# Microsoft Azure Arc-enabled servers

# Microsoft Azure Arc-enabled servers

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 10, 2024

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more
* [Classic Virtual Machines](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Install Dynatrace OneAgent VM extension

There are several ways to install the Dynatrace OneAgent VM extension: through Azure Portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.

Azure Portal

Azure CLI 2.0

ARM template

### Add the extension to an existing VM

1. In Azure Portal, go to an existing Azure Arc Machine resource.
2. In the left menu, go to **Settings** > **Extensions**.
3. Select **Add**.
4. From the list of extensions, select **Dynatrace OneAgent**.
5. Select **Next** to add the extension.
6. On the **Configure Dynatrace OneAgent Extension** page, enter your **Environment ID**, your **API Token**, and your **Server URL**. See [Prerequisites](#prerequisites) for details.
7. Optional Define additional OneAgent settings (such as proxy, port).
8. Select **Review + create**.
9. To check the deployment status, in your Dynatrace environment, go to **Deployment Status**.

```
az connectedmachine extension create



--publisher "Dynatrace.Ruxit"



--type "<Extension-Type>"



--name â<Extension-Type>â



--resource-group "<Resource-Group>"



--machine-name "<Azure Arc Server Name>"



--location <Azure Region>



--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the VM is deployed. |
| Azure Arc Server Name | Required | Name of the machine extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| Extension-name | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| Azure Region | Required | Azure Region of the resource |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |

Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.

The [JSON fileï»¿](https://dt-url.net/9f03wr8) for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. The placement of the JSON file affects the value of the resource name and type.

Example

The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the `"resources": []` object of the virtual machine.'

```
{



â¯ â¯ "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",



â¯ â¯ "contentVersion": "1.0.0.0",



â¯ â¯ "parameters": {



â¯ â¯ â¯ â¯ "vmName": {



â¯ â¯ â¯ â¯ â¯ â¯ "type": "string"



â¯ â¯ â¯ â¯ },



â¯ â¯ â¯ â¯ "location": {



â¯ â¯ â¯ â¯ â¯ â¯ "type": "string"



â¯ â¯ â¯ â¯ },



â¯ â¯ â¯ â¯ "tenant": {



â¯ â¯ â¯ â¯ â¯ â¯ "type": "string"



â¯ â¯ â¯ â¯ },



â¯ â¯ â¯ â¯ "token": {



â¯ â¯ â¯ â¯ â¯ â¯ "type": "securestring"



â¯ â¯ â¯ â¯ },



â¯ â¯ â¯ â¯ "server": {



â¯ â¯ â¯ â¯ â¯ â¯ "type": "string",



â¯ â¯ â¯ â¯ â¯ â¯ "defaultValue": ""



â¯ â¯ â¯ â¯ }



â¯ â¯ },



â¯ â¯ "resources": [



â¯ â¯ â¯ â¯ {



â¯ â¯ â¯ â¯ â¯ â¯ "name": "[concat(parameters('vmName'),'/<Extension-Type>')]",



â¯ â¯ â¯ â¯ â¯ â¯ "type": "Microsoft.HybridCompute/machines/extensions",



â¯ â¯ â¯ â¯ â¯ â¯ "location": "[parameters('location')]",



â¯ â¯ â¯ â¯ â¯ â¯ "apiVersion": "2022-03-10",



â¯ â¯ â¯ â¯ â¯ â¯ "properties": {



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "publisher": "dynatrace.ruxit",



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "type": " <Extension-Type>",



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "autoUpgradeMinorVersion": true,



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "settings": {



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "tenantId": "[parameters('tenant')]",



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "server": "[parameters('server')]"



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ },



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "protectedSettings": {



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ "token": "[parameters('token')]"



â¯ â¯ â¯ â¯ â¯ â¯ â¯ â¯ }



â¯ â¯ â¯ â¯ â¯ â¯ }



â¯ â¯ â¯ â¯ }



â¯ â¯ ]



}
```

| Parameter | Required | Description |
| --- | --- | --- |
| Parent-Arc Machine-Resource | Required | Name of the Azure Arc Machine resource where you want to install the extension. Not applicable when using nested resource. |
| Arc Machine Name | Required | Name of the Azure Arc Machine where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). From Microsoft Azure Arc version 2.200.0.0, it's recommended to pass it in `protectedSettings`. |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |

To check the deployment status, in your Dynatrace environment, go to **Manage** > **Deployment status**.

After installation is complete, OneAgent will begin monitoring.


---


## Source: monitor-azure-ai-all-in-one.md


---
title: Azure AI - All In One monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-all-in-one
scraped: 2026-02-18T05:44:39.332110
---

# Azure AI - All In One monitoring

# Azure AI - All In One monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for All In One. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| CharactersTrained | Total number of characters trained | ApiName, OperationName, Region | Count |  |
| CharactersTranslated | Total number of characters in incoming text request | ApiName, OperationName, Region | Count |  |
| ClientErrors | Number of calls with client side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code 5xx) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| TotalTokenCalls | Total number of token calls | ApiName, OperationName, Region | Count |  |
| TotalTransactions | Total number of transactions |  | Count |  |


---


## Source: monitor-azure-ai-anomaly-detector.md


---
title: Azure AI - Anomaly Detector monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-anomaly-detector
scraped: 2026-02-18T05:49:56.720073
---

# Azure AI - Anomaly Detector monitoring

# Azure AI - Anomaly Detector monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Anomaly Detector. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-bing-autosuggest.md


---
title: Azure AI - Bing Autosuggest monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-autosuggest
scraped: 2026-02-18T05:51:13.815725
---

# Azure AI - Bing Autosuggest monitoring

# Azure AI - Bing Autosuggest monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Bing Autosuggest. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-bing-custom-search.md


---
title: Azure AI - Bing Custom Search monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-custom-search
scraped: 2026-02-17T05:05:03.297668
---

# Azure AI - Bing Custom Search monitoring

# Azure AI - Bing Custom Search monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Bing Custom Search. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-bing-entity-search.md


---
title: Azure AI - Bing Entity Search monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-entity-search
scraped: 2026-02-18T05:44:03.563864
---

# Azure AI - Bing Entity Search monitoring

# Azure AI - Bing Entity Search monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Bing Entity Search. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-bing-search.md


---
title: Azure AI - Bing Search monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-search
scraped: 2026-02-18T05:49:49.799168
---

# Azure AI - Bing Search monitoring

# Azure AI - Bing Search monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Bing Search. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-bing-spell-check.md


---
title: Azure AI - Bing Spell Check monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-spell-check
scraped: 2026-02-18T05:45:41.293439
---

# Azure AI - Bing Spell Check monitoring

# Azure AI - Bing Spell Check monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Bing Spell Check. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-computer-vision.md


---
title: Azure AI - Computer Vision monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-computer-vision
scraped: 2026-02-17T21:33:37.019457
---

# Azure AI - Computer Vision monitoring

# Azure AI - Computer Vision monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Computer Vision. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-content-moderator.md


---
title: Azure AI Content Moderator monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-content-moderator
scraped: 2026-02-16T21:28:48.725054
---

# Azure AI Content Moderator monitoring

# Azure AI Content Moderator monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Content Moderator. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-custom-vision-prediction.md


---
title: Azure AI - Custom Vision Prediction monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-prediction
scraped: 2026-02-18T05:46:15.124057
---

# Azure AI - Custom Vision Prediction monitoring

# Azure AI - Custom Vision Prediction monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Custom Vision Prediction. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-custom-vision-training.md


---
title: Azure AI - Custom Vision monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-training
scraped: 2026-02-16T09:33:10.253387
---

# Azure AI - Custom Vision monitoring

# Azure AI - Custom Vision monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Custom Vision. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-face.md


---
title: Azure AI - Face monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-face
scraped: 2026-02-18T05:45:39.609852
---

# Azure AI - Face monitoring

# Azure AI - Face monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Face. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-immersive-reader.md


---
title: Azure AI - Immersive Reader monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-immersive-reader
scraped: 2026-02-17T05:04:32.347215
---

# Azure AI - Immersive Reader monitoring

# Azure AI - Immersive Reader monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Immersive Reader. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-language-understanding-authoring.md


---
title: Azure AI - Language Understanding (LUIS) Authoring monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding-authoring
scraped: 2026-02-18T05:56:28.297213
---

# Azure AI - Language Understanding (LUIS) Authoring monitoring

# Azure AI - Language Understanding (LUIS) Authoring monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Language Understanding (LUIS) Authoring. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-language-understanding.md


---
title: Azure AI - Language Understanding (LUIS) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding
scraped: 2026-02-18T05:56:41.760866
---

# Azure AI - Language Understanding (LUIS) monitoring

# Azure AI - Language Understanding (LUIS) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Language Understanding (LUIS). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| TotalTokenCalls | Total number of token calls | ApiName, OperationName, Region | Count |  |


---


## Source: monitor-azure-ai-openai.md


---
title: Azure OpenAI
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-openai
scraped: 2026-02-18T05:47:57.413184
---

# Azure OpenAI

# Azure OpenAI

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Mar 25, 2024

Dynatrace version 1.272+Environment ActiveGate version 1.195+

Dynatrace ingests metrics from Azure Metrics API for OpenAI. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| SuccessRate | Availability rate | API name, Operation name, Ratelimit key, Region | Percent | Applicable |
| BlockedCalls | Blocked calls | API name, Operation name, Ratelimit key, Region | Count | Applicable |
| ClientErrors | Client errors | API name, Operation name, Ratelimit key, Region | Count | Applicable |
| DataIn | Data in | API name, Operation name, Region | Byte | Applicable |
| DataOut | Data out | API name, Operation name, Region | Byte | Applicable |
| GeneratedTokens | Number of generated completion tokens | API name, Model deployment name, Model name, Region, Usage channel | Count | Applicable |
| Latency | Latency | API name, Operation name, Ratelimit key, Region | MilliSecond | Applicable |
| FineTunedTrainingHours | Processed fine tuned training hours | API name, Model deployment name, Model name, Region, Usage channel | Count | Applicable |
| TokenTransaction | Processed inference tokens | API name, Model deployment name, Model name, Region, Usage channel | Count | Applicable |
| ProcessedPromptTokens | Processed prompt tokens | API name, Model deployment name, Model name, Region, Usage channel | Count | Applicable |
| Ratelimit | Ratelimit | Ratelimit key, Region | Count | Applicable |
| ServerErrors | Number of server errors | API name, Operation name, Ratelimit key, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | API name, Operation name, Ratelimit key, Region | Count | Applicable |
| TotalCalls | Number of calls | API name, Operation name, Ratelimit key, Region | Count | Applicable |
| TotalErrors | Number of errors | API name, Operation name, Ratelimit key, Region | Count | Applicable |


---


## Source: monitor-azure-ai-personalizer.md


---
title: Azure AI - Personalizer monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-personalizer
scraped: 2026-02-18T05:44:59.524544
---

# Azure AI - Personalizer monitoring

# Azure AI - Personalizer monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Personalizer. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-qna-maker.md


---
title: Azure AI - QnA Maker monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-qna-maker
scraped: 2026-02-18T05:54:37.788879
---

# Azure AI - QnA Maker monitoring

# Azure AI - QnA Maker monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for QnA Maker. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-ai-speech.md


---
title: Azure AI - Speech monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-speech
scraped: 2026-02-17T21:28:16.174311
---

# Azure AI - Speech monitoring

# Azure AI - Speech monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Speech. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| TotalTokenCalls | Total number of token calls | ApiName, OperationName, Region | Count |  |


---


## Source: monitor-azure-ai-text-analytics.md


---
title: Azure AI - Text Analytics monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-text-analytics
scraped: 2026-02-18T05:56:19.738709
---

# Azure AI - Text Analytics monitoring

# Azure AI - Text Analytics monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Text Analytics. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| TotalTransactions | Total number of transactions |  | Count |  |


---


## Source: monitor-azure-ai-translator.md


---
title: Azure AI - Translator monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-translator
scraped: 2026-02-18T05:47:35.790965
---

# Azure AI - Translator monitoring

# Azure AI - Translator monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Translator. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| CharactersTrained | Total number of characters trained | ApiName, OperationName, Region | Count |  |
| CharactersTranslated | Total number of characters in incoming text request | ApiName, OperationName, Region | Count |  |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| TotalTokenCalls | Total number of token calls | ApiName, OperationName, Region | Count |  |


---


## Source: monitor-azure-api-management-service.md


---
title: Azure API Management Service monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service
scraped: 2026-02-18T05:48:02.821632
---

# Azure API Management Service monitoring

# Azure API Management Service monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure API Management Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure API Management (Microsoft.ApiManagement/service). While you have this service configured, you can't have Azure Application Service (built-in) (depracated) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Overall duration of gateway requests | Overall Duration of Gateway Requests in milliseconds | Location, Hostname | MilliSecond |  |
| Duration of backend requests | Duration of Backend Requests in milliseconds | Location, Hostname | MilliSecond |  |
| Capacity | Utilization metric for ApiManagement service. Note: For skus other than Premium, 'Max' aggregation will show the value as 0. | Location | Percent | Applicable |
| Total event hub events | Number of events sent to EventHub | Location | Count | Applicable |
| Successful event hub events | Number of successful EventHub events | Location | Count | Applicable |
| Failed event hub events | Number of failed EventHub events | Location | Count | Applicable |
| Rejected event hub events | Number of rejected EventHub events (wrong configuration or unauthorized) | Location | Count |  |
| Throttled event hub events | Number of throttled EventHub events | Location | Count |  |
| Timed out event hub events | Number of timed out EventHub events | Location | Count |  |
| Dropped event hub events | Number of events skipped because of queue size limit reached | Location | Count |  |
| Size of event hub events | Total size of EventHub events in bytes | Location | Byte |  |
| Requests | Gateway request metrics with multiple dimensions | Location, Hostname, Last error reason, Backend response code, Gateway response code, Backend response code category, Gateway response code category | Count | Applicable |
| Network connectivity status of resources (preview) | Network Connectivity status of dependent resource types from API Management service | Location, Resource type | Count |  |
| Web socket messages (preview) | Count of WebSocket messages based on selected source and destination | Location, Source, Destination | Count |  |
| Web socket connection attempts (preview) | Count of WebSocket connection attempts based on selected source and destination | Location, Source, Destination, State | Count |  |


---


## Source: monitor-azure-app-configuration.md


---
title: Azure App Configuration monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-configuration
scraped: 2026-02-17T21:31:29.003450
---

# Azure App Configuration monitoring

# Azure App Configuration monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 10, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure App Configuration. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![App config](https://dt-cdn.net/images/dashboard-57-1361-d768c55692.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| HttpIncomingRequestCount | Total number of incoming HTTP requests | StatusCode, Authentication | Count | Applicable |
| HttpIncomingRequestDuration | Latency on an HTTP request | StatusCode, Authentication | MilliSecond |  |
| ThrottledHttpRequestCount | Throttled HTTP requests |  | Count | Applicable |


---


## Source: monitor-azure-application-gateway.md


---
title: Azure Application Gateway monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway
scraped: 2026-02-18T05:45:02.351134
---

# Azure Application Gateway monitoring

# Azure Application Gateway monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Application Gateway. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure Application Gateway (Microsoft.Network/applicationGateways). While you have this service configured, you can't have Azure Application Gateway service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Throughput | Number of bytes per second the Application Gateway has served |  | BytePerSecond | Applicable |
| Unhealthy host count | Number of unhealthy backend hosts | Backend pool HTTP settings | Count | Applicable |
| Healthy host count | Number of healthy backend hosts | Backend pool HTTP settings | Count | Applicable |
| Total requests | Count of successful requests that Application Gateway has served | Backend pool HTTP settings | Count |  |
| Requests per minute per healthy host | Average request count per minute per healthy backend host in a pool | Backend pool HTTP settings | Count |  |
| Failed requests | Count of failed requests that Application Gateway has served | Backend pool HTTP settings | Count | Applicable |
| Response status | Http response status returned by Application Gateway | HTTP status | Count | Applicable |
| Current connections | Count of current connections established with Application Gateway |  | Count | Applicable |
| CPU utilization | Current CPU utilization of the Application Gateway |  | Percent |  |
| New connections per second | New connections per second established with Application Gateway |  | PerSecond |  |
| Current capacity units | Capacity Units consumed |  | Count |  |
| Fixed billable capacity units | Minimum capacity units that will be charged |  | Count |  |
| Estimated billed capacity units | Estimated capacity units that will be charged |  | Count |  |
| Current compute units | Compute Units consumed |  | Count |  |
| Backend response status | The number of HTTP response codes generated by the backend members. This does not include any response codes generated by the Application Gateway. | Backend server, Backend pool, Backend HTTP setting, HTTP status | Count |  |
| Client TLS protocol | The number of TLS and non-TLS requests initiated by the client that established connection with the Application Gateway. To view TLS protocol distribution, filter by the dimension TLS Protocol. | Listener, TLS protocol | Count |  |
| Bytes sent | The total number of bytes sent by the Application Gateway to the clients | Listener | Byte |  |
| Bytes received | The total number of bytes received by the Application Gateway from the clients | Listener | Byte |  |
| Client RTT | Round trip time between clients and Application Gateway. This metric indicates how long it takes to establish connections and return acknowledgements | Listener | MilliSecond |  |
| Application gateway total time | Time that it takes for a request to be processed and its response to be sent. This is the interval from the time when Application Gateway receives the first byte of an HTTP request to the time when the response send operation finishes. It's important to note that this usually includes the Application Gateway processing time, time that the request and response packets are traveling over the network and the time the backend server took to respond. | Listener | MilliSecond |  |
| Backend connect time | Time spent establishing a connection with a backend server | Listener, Backend server, Backend pool, Backend HTTP setting | MilliSecond |  |
| Backend first byte response time | Time interval between start of establishing a connection to backend server and receiving the first byte of the response header, approximating processing time of backend server | Listener, Backend server, Backend pool, Backend HTTP setting | MilliSecond |  |
| Backend last byte response time | Time interval between start of establishing a connection to backend server and receiving the last byte of the response body | Listener, Backend server, Backend pool, Backend HTTP setting | MilliSecond |  |
| Matched count | Web Application Firewall Total Rule Distribution for the incoming traffic | Rule group, Rule ID | Count |  |
| Blocked count | Web Application Firewall blocked requests rule distribution | Rule group, Rule ID | Count |  |


---


## Source: monitor-azure-application-insights.md


---
title: Azure Application Insights monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-insights
scraped: 2026-02-17T21:27:06.681526
---

# Azure Application Insights monitoring

# Azure Application Insights monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Application Insights. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.198+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Insights](https://dt-cdn.net/images/2021-03-12-11-44-29-1661-92088ffd2d.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| requests/duration | The time between receiving an HTTP request and finishing sending the response | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | MilliSecond | Applicable |
| requests/count | The count of completed HTTP requests | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | Count | Applicable |
| requests/failed | The count of failed HTTP requests | Request performance, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Applicable |
| availabilityResults/availabilityPercentage | The percentage of successfully completed availability tests | Test name, Run location, | Percent | Applicable |
| availabilityResults/count | The count of availability tests | Test name, Run location, Test result | Count |  |
| availabilityResults/duration | Availability test duration | Test name, Run location, Test result | MilliSecond |  |
| browserTimings/networkDuration | The time between user request and network connection |  | MilliSecond | Applicable |
| browserTimings/processingDuration | The time between receiving the last byte of a document until the DOM is loaded |  | MilliSecond | Applicable |
| browserTimings/receiveDuration | The receiving response time |  | MilliSecond | Applicable |
| browserTimings/sendDuration | The send request time |  | MilliSecond | Applicable |
| browserTimings/totalDuration | The browser page load time |  | MilliSecond |  |
| dependencies/count | The number of dependency calls | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Applicable |
| dependencies/duration | The dependency duration | Dependency type, Dependency performance, Successful call, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | MilliSecond |  |
| dependencies/failed | The number of dependency call failures | Dependency type, Dependency performance, Target of a dependency call, Result code, Is traffic synthetic, Cloud role instance, Cloud role name | Count | Applicable |
| pageViews/count | The number of page views | Is traffic synthetic, Cloud role name, | Count | Applicable |
| pageViews/duration | The page view load time | Is traffic synthetic, Cloud role name | MilliSecond |  |
| performanceCounters/requestExecutionTime | The HTTP request execution time | Cloud role instance | MilliSecond |  |
| performanceCounters/requestsInQueue | The HTTP requests in application queue | Cloud role instance | Count |  |
| performanceCounters/requestsPerSecond | The HTTP request rate | Cloud role instance | PerSecond | Applicable |
| performanceCounters/exceptionsPerSecond | The exception rate | Cloud role instance | PerSecond |  |
| performanceCounters/processIOBytesPerSecond | The process IO rate | Cloud role instance | BytePerSecond | Applicable |
| performanceCounters/processCpuPercentage | The processor time | Cloud role instance | Percent | Applicable |
| performanceCounters/processorCpuPercentage |  | Cloud role instance | Percent | Applicable |
| performanceCounters/memoryAvailableBytes | The available memory | Cloud role instance | Byte | Applicable |
| performanceCounters/processPrivateBytes | The process private bytes | Cloud role instance | Byte |  |
| requests/rate | The server request rate | Request performance, Result code, Is traffic synthetic, Cloud role instance, Successful request, Cloud role name | PerSecond | Applicable |
| exceptions/count | The number of exceptions | Cloud role name, Cloud role instance, Device type | Count |  |
| exceptions/browser | The browser exceptions | Cloud role name | Count | Applicable |
| exceptions/server | The server exceptions | Cloud role name, Cloud role instance | Count | Applicable |
| traces/count | The number of traces | Severity level, Is traffic synthetic, Cloud role name, Cloud role instance | Count |  |

## Limitations

Running the Azure App Service extension at the same time with Azure Application Insights is not supported.


---


## Source: monitor-azure-arc.md


---
title: Azure Machine - Azure Arc
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-arc
scraped: 2026-02-18T05:50:32.088379
---

# Azure Machine - Azure Arc

# Azure Machine - Azure Arc

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Mar 07, 2024

Dynatrace version 1.281+ Environment ActiveGate version 1.195+

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").


---


## Source: monitor-azure-automation-account.md


---
title: Azure Automation Account monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-automation-account
scraped: 2026-02-18T05:51:44.162427
---

# Azure Automation Account monitoring

# Azure Automation Account monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Automation Account. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Auto acc](https://dt-cdn.net/images/2021-03-12-10-49-47-1713-cab240a4fe.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| TotalJob | Total number of jobs | Runbook, Status | Count | Applicable |
| TotalUpdateDeploymentMachineRuns | Total software update deployment machine runs in a software update deployment run | SoftwareUpdateConfigurationNam, Status, TargetComputer | Count | Applicable |
| TotalUpdateDeploymentRuns | Total software update deployment runs | SoftwareUpdateConfigurationName, Status, TotalUpdateDeploymentRuns | Count | Applicable |


---


## Source: monitor-azure-basic-load-balancer.md


---
title: Azure Basic Load Balancer monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer
scraped: 2026-02-18T05:46:08.177183
---

# Azure Basic Load Balancer monitoring

# Azure Basic Load Balancer monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").


---


## Source: monitor-azure-batch.md


---
title: Azure Batch monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-batch
scraped: 2026-02-18T05:51:47.638353
---

# Azure Batch monitoring

# Azure Batch monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jun 25, 2020

The Azure Batch overview page gives you a comprehensive view of how many jobs and tasks were completed over a period of time. You can also track nodes in different states, such as running, idle, or offline.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Azure batch dash](https://dt-cdn.net/images/azurebatchaccounts-2385-9e18eb64a6.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CoreCount | Total number of dedicated cores in the batch account | None | Count | Applicable |
| CreatingNodeCount | Number of nodes being created | None | Count |  |
| IdleNodeCount | Number of idle nodes | None | Count | Applicable |
| JobDeleteCompleteEvent | Total number of jobs that have been successfully deleted | jobId | Count |  |
| JobDeleteStartEvent | Total number of jobs that have been requested to be deleted | jobId | Count |  |
| JobDisableCompleteEvent | Total number of jobs that have been successfully disabled | jobId | Count |  |
| JobDisableStartEvent | Total number of jobs that have been requested to be disabled | jobId | Count |  |
| JobStartEvent | Total number of jobs that have been successfully started | jobId | Count | Applicable |
| JobTerminateCompleteEvent | Total number of jobs that have been successfully terminated | jobId | Count |  |
| JobTerminateStartEvent | Total number of jobs that have been requested to be terminated | jobId | Count |  |
| LeavingPoolNodeCount | Number of nodes leaving the pool | None | Count |  |
| LowPriorityCoreCount | Total number of low-priority cores in the batch account | None | Count | Applicable |
| LowPriorityNodeCount | Total number of low-priority nodes in the batch account | None | Count | Applicable |
| OfflineNodeCount | Number of offline nodes | None | Count |  |
| PoolCreateEvent | Total number of pools that have been created | poolId | Count |  |
| PoolDeleteCompleteEvent | Total number of pool deletes that have completed | poolId | Count |  |
| PoolDeleteStartEvent | Total number of pool deletes that have started | poolId | Count |  |
| PoolResizeCompleteEvent | Total number of pool resizes that have completed | poolId | Count |  |
| PoolResizeStartEvent | Total number of pool resizes that have started | poolId | Count |  |
| PreemptedNodeCount | Number of preempted nodes | None | Count |  |
| RebootingNodeCount | Number of rebooting nodes | None | Count | Applicable |
| ReimagingNodeCount | Number of reimaging nodes | None | Count |  |
| RunningNodeCount | Number of running nodes | None | Count | Applicable |
| StartTaskFailedNodeCount | Number of nodes where the Start Task has failed | None | Count |  |
| StartingNodeCount | Number of nodes starting | None | Count | Applicable |
| TaskCompleteEvent | Total number of tasks that have completed | poolId,jobId | Count | Applicable |
| TaskFailEvent | Total number of tasks that have completed in a failed state | poolId,jobId | Count | Applicable |
| TaskStartEvent | Total number of tasks that have started | poolId,jobId | Count | Applicable |
| TotalNodeCount | Total number of dedicated nodes in the batch account | None | Count | Applicable |
| UnusableNodeCount | Number of unusable nodes | None | Count |  |
| WaitingForStartTaskNodeCount | Number of nodes waiting for the Start Task to complete | None | Count |  |


---


## Source: monitor-azure-blockchain-service.md


---
title: Azure Blockchain monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-blockchain-service
scraped: 2026-02-17T21:29:30.734401
---

# Azure Blockchain monitoring

# Azure Blockchain monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 17, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Blockchain. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Blockchain](https://dt-cdn.net/images/dashboard-76-1896-1212e3c01c.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ConnectionAccepted | The number of accepted connections | Node | Count | Applicable |
| ConnectionActive | The number of active connections | Node | Count | Applicable |
| ConnectionHandled | The number of handled connections | Node | Count | Applicable |
| CpuUsagePercentageInDouble | The block number of the latest block committed | Node | Percent | Applicable |
| IOReadBytes | The number of IO read bytes | Node | Byte | Applicable |
| IOWriteBytes | The number of IO write bytes | Node | Byte | Applicable |
| MemoryLimit | Memory limit | Node | Byte | Applicable |
| MemoryUsage | Memory usage | Node | Byte | Applicable |
| MemoryUsagePercentageInDouble | The percentage of memory usage | Node | Percent |  |
| PendingTransactions | The number of pending transactions | Node | Count | Applicable |
| ProcessedBlocks | The number of processed blocks | Node | Count | Applicable |
| ProcessedTransactions | The number of processed transactions | Node | Count | Applicable |
| QueuedTransactions | The number of queued transactions | Node | Count | Applicable |
| RequestHandled | The number of handled requests | Node | Count | Applicable |
| StorageUsage | Storage usage | Node | Byte | Applicable |


---


## Source: monitor-azure-cache-for-redis.md


---
title: Azure Cache for Redis monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis
scraped: 2026-02-18T05:56:40.045586
---

# Azure Cache for Redis monitoring

# Azure Cache for Redis monitoring

* Latest Dynatrace
* How-to guide
* 23-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Cache for Redis. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

This service monitors a part of Azure Cache for Redis (`Microsoft.Cache/redis`).

While you have this service configured, you **can't** have Azure Redis Cache (built-in) service turned on.

Enterprise Azure Cache for Redis service (`Microsoft.Cache/redisEnterprise`) currently cannot be monitored; to request this type of monitoring, please create an RFE (Request for Enhancement).

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Connected clients | The number of client connections to the cache. | Shard ID | Count | Applicable |
| Total operations | The total number of commands processed by the cache server. | Shard ID | Count | Applicable |
| Cache hits | The number of successful key lookups. | Shard ID | Count | Applicable |
| Cache misses | The number of failed key lookups. | Shard ID | Count | Applicable |
| Cache miss rate | The % of get requests that miss. | Shard ID | Percent | Applicable |
| Gets | The number of get operations from the cache. | Shard ID | Count |  |
| Sets | The number of set operations to the cache. | Shard ID | Count |  |
| Operations per second | The number of instantaneous operations per second executed on the cache. | Shard ID | Count |  |
| Evicted keys | The number of items evicted from the cache. | Shard ID | Count |  |
| Total keys | The total number of items in the cache. | Shard ID | Count |  |
| Expired keys | The number of items expired from the cache. | Shard ID | Count |  |
| Used memory | The amount of cache memory used for key/value pairs in the cache in MB. | Shard ID | Byte |  |
| Used memory percentage | The percentage of cache memory used for key/value pairs. | Shard ID | Percent | Applicable |
| Used memory RSS | The amount of cache memory used in MB, including fragmentation and metadata. | Shard ID | Byte |  |
| Server load | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. | Shard ID | Percent |  |
| Cache write | The amount of data written to the cache in bytes per second. | Shard ID | BytePerSecond |  |
| Cache read | The amount of data read from the cache in bytes per second. | Shard ID | BytePerSecond |  |
| Connections created per second (instance based) | The number of instantaneous connections created per second on the cache via port 6379 or 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connections closed per second (instance based) | The number of instantaneous connections closed per second on the cache via port 6379 or 6380 (SSL). | Shard ID, Primary, SSL | PerSecond |  |
| Connected clients (instance based) | The number of client connections to the cache. | Shard ID, Port, Primary | Count |  |
| Total operations (instance based) | The total number of commands processed by the cache server. | Shard ID, Port, Primary | Count |  |
| Cache hits (instance based) | The number of successful key lookups. | Shard ID, Port, Primary | Count |  |
| Cache misses (instance based) | The number of failed key lookups. | Shard ID, Port, Primary | Count |  |
| Gets (instance based) | The number of get operations from the cache. | Shard ID, Port, Primary | Count |  |
| Sets (instance based) | The number of set operations to the cache. | Shard ID, Port, Primary | Count |  |
| Operations per second (instance based) | The number of instantaneous operations per second executed on the cache. | Shard ID, Port, Primary | Count |  |
| Evicted keys (instance based) | The number of items evicted from the cache. | Shard ID, Port, Primary | Count |  |
| Total keys (instance based) | The total number of items in the cache. | Shard ID, Port, Primary | Count |  |
| Expired keys (instance based) | The number of items expired from the cache. | Shard ID, Port, Primary | Count |  |
| Used memory (instance based) | The amount of cache memory used for key/value pairs in the cache in MB. | Shard ID, Port, Primary | Byte |  |
| Used memory percentage (instance based) | The percentage of cache memory used for key/value pairs. | Shard ID, Port, Primary | Percent |  |
| Used memory RSS (instance based) | The amount of cache memory used in MB, including fragmentation and metadata. | Shard ID, Port, Primary | Byte |  |
| Server load (instance based) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. | Shard ID, Port, Primary | Percent |  |
| Cache write (instance based) | The amount of data written to the cache in bytes per second. | Shard ID, Port, Primary | BytePerSecond |  |
| Cache read (instance based) | The amount of data read from the cache in bytes per second. | Shard ID, Port, Primary | BytePerSecond |  |
| CPU (instance based) | The CPU utilization of the Azure Redis Cache server as a percentage. | Shard ID, Port, Primary | Percent |  |
| CPU | The CPU utilization of the Azure Redis Cache server as a percentage. | Shard ID | Percent | Applicable |
| Cache latency microseconds (preview) | The latency to the cache in microseconds. | Shard ID | Count |  |
| Errors | The number errors that occurred on the cache. | Shard ID, Error type | Count |  |
| Connected clients (shard 0) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 0) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 0) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 0) | The number of failed key lookups. |  | Count |  |
| Gets (shard 0) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 0) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 0) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 0) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 0) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 0) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 0) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 0) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 0) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 0) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 0) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 0) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 1) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 1) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 1) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 1) | The number of failed key lookups. |  | Count |  |
| Gets (shard 1) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 1) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 1) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 1) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 1) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 1) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 1) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 1) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 1) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 1) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 1) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 1) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 2) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 2) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 2) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 2) | The number of failed key lookups. |  | Count |  |
| Gets (shard 2) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 2) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 2) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 2) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 2) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 2) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 2) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 2) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 2) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 2) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 2) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 2) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 3) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 3) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 3) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 3) | The number of failed key lookups. |  | Count |  |
| Gets (shard 3) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 3) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 3) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 3) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 3) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 3) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 3) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 3) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 3) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 3) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 3) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 3) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 4) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 4) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 4) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 4) | The number of failed key lookups. |  | Count |  |
| Gets (shard 4) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 4) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 4) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 4) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 4) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 4) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 4) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 4) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 4) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 4) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 4) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 4) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 5) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 5) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 5) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 5) | The number of failed key lookups. |  | Count |  |
| Gets (shard 5) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 5) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 5) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 5) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 5) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 5) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 5) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 5) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 5) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 5) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 5) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 5) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 6) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 6) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 6) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 6) | The number of failed key lookups. |  | Count |  |
| Gets (shard 6) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 6) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 6) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 6) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 6) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 6) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 6) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 6) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 6) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 6) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 6) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 6) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 7) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 7) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 7) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 7) | The number of failed key lookups. |  | Count |  |
| Gets (shard 7) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 7) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 7) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 7) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 7) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 7) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 7) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 7) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 7) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 7) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 7) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 7) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 8) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 8) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 8) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 8) | The number of failed key lookups. |  | Count |  |
| Gets (shard 8) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 8) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 8) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 8) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 8) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 8) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 8) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 8) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 8) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 8) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 8) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 8) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Connected clients (shard 9) | The number of client connections to the cache. |  | Count |  |
| Total operations (shard 9) | The total number of commands processed by the cache server. |  | Count |  |
| Cache hits (shard 9) | The number of successful key lookups. |  | Count |  |
| Cache misses (shard 9) | The number of failed key lookups. |  | Count |  |
| Gets (shard 9) | The number of get operations from the cache. |  | Count |  |
| Sets (shard 9) | The number of set operations to the cache. |  | Count |  |
| Operations per second (shard 9) | The number of instantaneous operations per second executed on the cache. |  | Count |  |
| Evicted keys (shard 9) | The number of items evicted from the cache. |  | Count |  |
| Total keys (shard 9) | The total number of items in the cache. |  | Count |  |
| Expired keys (shard 9) | The number of items expired from the cache. |  | Count |  |
| Used memory (shard 9) | The amount of cache memory used for key/value pairs in the cache in MB. |  | Byte |  |
| Used memory RSS (shard 9) | The amount of cache memory used in MB, including fragmentation and metadata. |  | Byte |  |
| Server load (shard 9) | The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages. |  | Percent |  |
| Cache write (shard 9) | The amount of data written to the cache in bytes per second. |  | BytePerSecond |  |
| Cache read (shard 9) | The amount of data read from the cache in bytes per second. |  | BytePerSecond |  |
| CPU (shard 9) | The CPU utilization of the Azure Redis Cache server as a percentage. |  | Percent |  |
| Geo - replication healthy | The health status of geo-replication link. 1 if healthy and 0 if disconnected or unhealthy. | Shard ID | Count |  |
| Geo - replication data sync offset | Approximate amount of data in bytes that needs to be synchronized to geo-secondary cache. | Shard ID | Byte |  |
| Geo - replication connectivity lag | Time in seconds since last successful data synchronization with geo-primary cache. Value will continue to increase if the link status is down. | Shard ID | Second |  |
| Geo - replication full sync event started | Fired on initiation of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization. | Shard ID | Count |  |
| Geo - replication full sync event finished | Fired on completion of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization. | Shard ID | Count |  |


---


## Source: monitor-azure-cognitive-services-ink-recognizer.md


---
title: Azure Cognitive Services - Ink Recognizer monitoring (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cognitive-services-ink-recognizer
scraped: 2026-02-18T05:45:21.118422
---

# Azure Cognitive Services - Ink Recognizer monitoring (deprecated)

# Azure Cognitive Services - Ink Recognizer monitoring (deprecated)

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Ink Recognizer. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cognitive services](https://dt-cdn.net/images/dashboard-79-1423-6e181ef360.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BlockedCalls | Number of calls that exceeded rate or quota limit | ApiName, OperationName, Region | Count | Applicable |
| ClientErrors | Number of calls with client-side error (HTTP response code `4xx`) | ApiName, OperationName, Region | Count | Applicable |
| DataIn | Size of incoming data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| DataOut | Size of outgoing data in bytes | ApiName, OperationName, Region | Byte | Applicable |
| Latency | Latency in milliseconds | ApiName, OperationName, Region | MilliSecond | Applicable |
| ServerErrors | Number of calls with service internal error (HTTP response code `5xx`) | ApiName, OperationName, Region | Count | Applicable |
| SuccessfulCalls | Number of successful calls | ApiName, OperationName, Region | Count | Applicable |
| TotalCalls | Total number of calls | ApiName, OperationName, Region | Count |  |
| TotalErrors | Total number of calls with error response (HTTP response code `4xx` or `5xx`) | ApiName, OperationName, Region | Count | Applicable |


---


## Source: monitor-azure-container-app.md


---
title: Azure Container App monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-app
scraped: 2026-02-17T05:05:48.852159
---

# Azure Container App monitoring

# Azure Container App monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 31, 2023

Dynatrace ingests metrics from Azure Metrics API for Azure Container App. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Reserved cores | Number of reserved cores for container app revisions | Revision | Count | Applicable |
| Replica count | Number of replicas count of container app | Revision | Count | Applicable |
| Requests | Requests processed | Replica, Revision, Status code, Status code category | Count | Applicable |
| Replica restart count | Restart count of container app replicas | Replica, Revision | Count | Applicable |
| Network in bytes | Network received bytes | Replica, Revision | Byte | Applicable |
| Total reserved cores | Number of total reserved cores for the container app |  | Count | Applicable |
| Network out bytes | Network transmitted bytes | Replica, Revision | Byte | Applicable |
| CPU usage | CPU consumed by the container app, in nano cores. 1,000,000,000 nano cores = 1 core | Replica, Revision | Count | Applicable |
| Memory working set bytes | Container App working set memory used in bytes. | Replica, Revision | Byte | Applicable |


---


## Source: monitor-azure-container-apps-environment.md


---
title: Azure Container Apps Environment monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-apps-environment
scraped: 2026-02-17T21:31:59.085679
---

# Azure Container Apps Environment monitoring

# Azure Container Apps Environment monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 31, 2023

Dynatrace ingests metrics from Azure Metrics API for Azure Container Apps Environment. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Cores quota limit | The cores quota limit of managed environment |  | Count |  |
| Percentage cores used out of limit | The cores quota utilization of managed environment |  | Percent |  |


---


## Source: monitor-azure-container-instances.md


---
title: Monitor Azure Container Instances
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-instances
scraped: 2026-02-18T05:54:26.898778
---

# Monitor Azure Container Instances

# Monitor Azure Container Instances

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Container Instances. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Cont inst](https://dt-cdn.net/images/2021-03-12-10-53-35-1600-bdea730964.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CpuUsage | CPU usage on all cores in millicores | containerName | Count | Applicable |
| MemoryUsage | Total memory usage in byte | containerName | Bytes | Applicable |
| NetworkBytesReceivedPerSecond | The network bytes received per second |  | Bytes | Applicable |
| NetworkBytesTransmittedPerSecond | The network bytes transmitted per second |  | Bytes | Applicable |


---


## Source: monitor-azure-container-registry.md


---
title: Azure Container Registry monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-registry
scraped: 2026-02-17T21:28:22.248489
---

# Azure Container Registry monitoring

# Azure Container Registry monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Container Registry. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Container reg](https://dt-cdn.net/images/dashboard-58-2151-e99629b75c.png)

## Available metrics

| Name | Description | Unit |  | Recommended |
| --- | --- | --- | --- | --- |
| AgentPoolCPUTime | AgentPool CPU time in seconds | Second |  |  |
| RunDuration | Run duration in milliseconds | MilliSecond | Applicable |  |
| SuccessfulPullCount | Number of successful image pulls | Count | Applicable |  |
| SuccessfulPushCount | Number of successful image pushes | Count | Applicable |  |
| TotalPullCount | Number of image pulls in total | Count | Applicable |  |
| TotalPushCount | Number of image pushes in total | Count | Applicable |  |


---


## Source: monitor-azure-cosmos-db-account-globaldocumentdb.md


---
title: Azure Cosmos DB Account (GlobalDocumentDB) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb
scraped: 2026-02-17T21:27:00.294674
---

# Azure Cosmos DB Account (GlobalDocumentDB) monitoring

# Azure Cosmos DB Account (GlobalDocumentDB) monitoring

* Latest Dynatrace
* How-to guide
* 9-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Cosmos DB Account (GlobalDocumentDB). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). While you have this service configured, you can't have Azure Cosmos Database (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Region added | Region Added | Region | Count |  |
| Autoscale max throughput | Autoscale Max Throughput | Collection name, Database name | Count | Applicable |
| Cassandra connection closures | Number of Cassandra connections that were closed, reported at a 1 minute granularity | Closure reason, Region | Count |  |
| Cassandra connector average replication latency | Cassandra Connector Average ReplicationLatency |  | MilliSecond |  |
| Cassandra connector replication health status | Cassandra Connector Replication Health Status | Replication in error, Replication not started, Replication in progress | Count |  |
| Cassandra keyspace created | Cassandra Keyspace Created | Keyspace name | Count |  |
| Cassandra keyspace deleted | Cassandra Keyspace Deleted | Keyspace name | Count |  |
| Cassandra keyspace throughput updated | Cassandra Keyspace Throughput Updated | Keyspace name | Count |  |
| Cassandra keyspace updated | Cassandra Keyspace Updated | Keyspace name | Count |  |
| Cassandra request charges | RUs consumed for Cassandra requests made | Collection name, Database name, Operation type, Region, Resource type | Count |  |
| Cassandra requests | Number of Cassandra requests made | Collection name, Database name, Error code, Operation type, Region, Resource type | Count |  |
| Cassandra table created | Cassandra Table Created | Table name, Keyspace name | Count |  |
| Cassandra table deleted | Cassandra Table Deleted | Table name, Keyspace name | Count |  |
| Cassandra table throughput updated | Cassandra Table Throughput Updated | Table name, Keyspace name | Count |  |
| Cassandra table updated | Cassandra Table Updated | Table name, Keyspace name | Count |  |
| Account created | Account Created |  | Count |  |
| Data usage | Total data usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| Dedicated gateway average CPU usage | Average CPU usage across dedicated gateway instances | Region | Percent |  |
| Dedicated gateway average memory usage | Average memory usage across dedicated gateway instances, which is used for both routing requests and caching data | Region | Byte |  |
| Dedicated gateway CPU usage | CPU usage across dedicated gateway instances | Region | Percent |  |
| Dedicated gateway maximum CPU usage | Average Maximum CPU usage across dedicated gateway instances | Region | Percent |  |
| Dedicated gateway memory usage | Memory usage across dedicated gateway instances | Region | Byte |  |
| Dedicated gateway requests | Requests at the dedicated gateway | Cache exercised, Cache hit, Collection name, Database name, Operation name, Region | Count |  |
| Account deleted | Account Deleted |  | Count |  |
| Document count | Total document count reported at 5 minutes, 1 hour and 1 day granularity | Collection name, Database name, Region | Count | Applicable |
| Document quota | Total storage quota reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| Gremlin database created | Gremlin Database Created | Database name | Count |  |
| Gremlin database deleted | Gremlin Database Deleted | Database name | Count |  |
| Gremlin database throughput updated | Gremlin Database Throughput Updated | Database name | Count |  |
| Gremlin database updated | Gremlin Database Updated | Database name | Count |  |
| Gremlin graph created | Gremlin Graph Created | Graph name, Database name | Count |  |
| Gremlin graph deleted | Gremlin Graph Deleted | Graph name, Database name | Count |  |
| Gremlin graph throughput updated | Gremlin Graph Throughput Updated | Graph name, Database name | Count |  |
| Gremlin graph updated | Gremlin Graph Updated | Graph name, Database name | Count |  |
| Gremlin request charges | Request Units consumed for Gremlin requests made | Collection name, Database name, Region | Count |  |
| Gremlin requests | Number of Gremlin requests made | Collection name, Database name, Error code, Region | Count |  |
| Index usage | Total index usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| Integrated cache evicted entries size | Size of the entries evicted from the integrated cache | Region | Byte |  |
| Integrated cache item expiration count | Number of items evicted from the integrated cache due to TTL expiration | Region | Count |  |
| Integrated cache item hit rate | Number of point reads that used the integrated cache divided by number of point reads routed through the dedicated gateway with eventual consistency | Region | Percent |  |
| Integrated cache query expiration count | Number of queries evicted from the integrated cache due to TTL expiration | Region | Count |  |
| Integrated cache query hit rate | Number of queries that used the integrated cache divided by number of queries routed through the dedicated gateway with eventual consistency | Region | Percent |  |
| Materialized view catchup gap in minutes | Maximum time difference in minutes between data in source container and data propagated to materialized view | Region, Materialized view name | Count |  |
| Materialized views builder average CPU usage | Average CPU usage across materialized view builder instances, which are used for populating data in materialized views | Region | Percent |  |
| Materialized views builder average memory usage | Average memory usage across materialized view builder instances, which are used for populating data in materialized views | Region | Byte |  |
| Materialized views builder maximum CPU usage | Average Maximum CPU usage across materialized view builder instances, which are used for populating data in materialized views | Region | Percent |  |
| Metadata requests | Count of metadata requests. Cosmos DB maintains system metadata collection for each account, that allows you to enumerate collections, databases, etc, and their configurations, free of charge. | Collection name, Database name, Region, Status code | Count | Applicable |
| Normalized ru consumption | Max RU consumption percentage per minute | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Percent | Applicable |
| Region offlined | Region Offlined | Region, Status code | Count |  |
| Region onlined | Region Onlined | Region, Status code | Count |  |
| Physical partition size | Physical Partition Size in bytes | Collection name, Database name, Resource ID, Physical partition ID, Region | Byte |  |
| Physical partition throughput | Physical Partition Throughput | Collection name, Database name, Resource ID, Physical partition ID, Region | Count |  |
| Provisioned throughput | Provisioned Throughput | Collection name, Database name | Count | Applicable |
| Region failed over | Region Failed Over |  | Count |  |
| Region removed | Region Removed | Region | Count |  |
| P99 replication latency | P99 Replication Latency across source and target regions for geo-enabled account | Source region, Target region | MilliSecond |  |
| Server side latency | Server Side Latency | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | MilliSecond | Applicable |
| Server side latency direct | Server Side Latency in Direct Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| Server side latency gateway | Server Side Latency in Gateway Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| Service availability | Account requests availability at one hour, day or month granularity |  | Percent | Applicable |
| SQL container created | Sql Container Created | Container name, Database name | Count |  |
| SQL container deleted | Sql Container Deleted | Container name, Database name | Count |  |
| SQL container throughput updated | Sql Container Throughput Updated | Container name, Database name | Count |  |
| SQL container updated | Sql Container Updated | Container name, Database name | Count |  |
| SQL database created | Sql Database Created | Database name | Count |  |
| SQL database deleted | Sql Database Deleted | Database name | Count |  |
| SQL database throughput updated | Sql Database Throughput Updated | Database name | Count |  |
| SQL database updated | Sql Database Updated | Database name | Count |  |
| Azure table table created | AzureTable Table Created | Table name | Count |  |
| Azure table table deleted | AzureTable Table Deleted | Table name | Count |  |
| Azure table table throughput updated | AzureTable Table Throughput Updated | Table name | Count |  |
| Azure table table updated | AzureTable Table Updated | Table name | Count |  |
| Total requests | Number of requests made | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| Total requests (preview) | Number of SQL requests | Collection name, Database name, Operation type, Region, Status, Status code | Count |  |
| Total request units | SQL Request Units consumed | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| Total request units (preview) | Request Units consumed with CapacityType | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count |  |
| Account keys updated | Account Keys Updated | Key type | Count |  |
| Account network settings updated | Account Network Settings Updated |  | Count |  |
| Account replication settings updated | Account Replication Settings Updated |  | Count |  |
| Account diagnostic settings updated | Account Diagnostic Settings Updated | Diagnostic settings name, Resource group name | Count |  |


---


## Source: monitor-azure-cosmos-db-account-mongodb.md


---
title: Azure Cosmos DB Account (MongoDB) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb
scraped: 2026-02-17T04:57:34.414291
---

# Azure Cosmos DB Account (MongoDB) monitoring

# Azure Cosmos DB Account (MongoDB) monitoring

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Cosmos DB Account (MongoDB). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure Cosmos DB Account (Microsoft.DocumentDB/databaseAccounts). While you have this service configured, you can't have Azure Cosmos Database (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| AddRegion | Region Added | Region | Count |  |
| AutoscaleMaxThroughput | Autoscale Max Throughput | Collection name, Database name | Count | Applicable |
| CreateAccount | Account Created |  | Count |  |
| DataUsage | Total data usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| DeleteAccount | Account Deleted |  | Count |  |
| DocumentCount | Total document count reported at 5 minutes, 1 hour and 1 day granularity | Collection name, Database name, Region | Count | Applicable |
| DocumentQuota | Total storage quota reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| IndexUsage | Total index usage reported at 5 minutes granularity | Collection name, Database name, Region | Byte | Applicable |
| MetadataRequests | Count of metadata requests. Cosmos DB maintains system metadata collection for each account, that allows you to enumerate collections, databases, etc, and their configurations, free of charge. | Collection name, Database name, Region, Status code | Count | Applicable |
| MongoCollectionCreate | Mongo Collection Created | Collection name, Database name | Count |  |
| MongoCollectionDelete | Mongo Collection Deleted | Collection name, Database name | Count |  |
| MongoCollectionThroughputUpdate | Mongo Collection Throughput Updated | Collection name, Database name | Count |  |
| MongoCollectionUpdate | Mongo Collection Updated | Collection name, Database name | Count |  |
| MongoDBDatabaseCreate | Mongo Database Created | Database name | Count |  |
| MongoDBDatabaseUpdate | Mongo Database Updated | Database name | Count |  |
| MongoDatabaseDelete | Mongo Database Deleted | Database name | Count |  |
| MongoDatabaseThroughputUpdate | Mongo Database Throughput Updated | Database name | Count |  |
| MongoRequestCharge | Mongo Request Units Consumed | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| MongoRequests | Number of Mongo Requests Made | Collection name, Command name, Database name, Error code, Region, Status | Count |  |
| NormalizedRUConsumption | Max RU consumption percentage per minute | Collection name, Collection rid, Database name, Partition key range ID, Physical partition ID, Region | Percent | Applicable |
| OfflineRegion | Region Offlined | Region, Status code | Count |  |
| OnlineRegion | Region Onlined | Region, Status code | Count |  |
| PhysicalPartitionSizeInfo | Physical Partition Size in bytes | Collection name, Database name, Physical partition ID, Region, Resource ID | Byte |  |
| PhysicalPartitionThroughputInfo | Physical Partition Throughput | Collection name, Database name, Physical partition ID, Region, Resource ID | Count |  |
| ProvisionedThroughput | Provisioned Throughput | Collection name, Database name | Count | Applicable |
| RegionFailover | Region Failed Over |  | Count |  |
| RemoveRegion | Region Removed | Region | Count |  |
| ReplicationLatency | P99 Replication Latency across source and target regions for geo-enabled account | Source region, Target region | MilliSecond |  |
| ServerSideLatency | Server Side Latency | Collection name, Connection mode, Database name, Operation type, Publicapi type, Region | MilliSecond | Applicable |
| ServerSideLatencyDirect | Server Side Latency in Direct Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServerSideLatencyGateway | Server Side Latency in Gateway Connection Mode | Collection name, Database name, Operation type, Publicapi type, Region | MilliSecond |  |
| ServiceAvailability | Account requests availability at one hour, day or month granularity |  | Percent | Applicable |
| TotalRequestUnits | SQL Request Units consumed | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| TotalRequests | Number of requests made | Capacity type, Collection name, Database name, Operation type, Region, Status, Status code | Count | Applicable |
| UpdateAccountKeys | Account Keys Updated | Key type | Count |  |
| UpdateAccountNetworkSettings | Account Network Settings Updated |  | Count |  |
| UpdateAccountReplicationSettings | Account Replication Settings Updated |  | Count |  |
| UpdateDiagnosticsSettings | Account Diagnostic Settings Updated | Diagnostic settings name, Resource group name | Count |  |


---


## Source: monitor-azure-data-explorer-cluster.md


---
title: Azure Data Explorer monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-explorer-cluster
scraped: 2026-02-18T05:52:42.318508
---

# Azure Data Explorer monitoring

# Azure Data Explorer monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Data Explorer. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Data expl](https://dt-cdn.net/images/dashboard-81-3840-6b01ea9389.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| BatchBlobCount | The number of data sources in an aggregated batch for ingestion | Count | Database | Applicable |
| BatchDuration | The duration of the aggregation phase in the ingestion flow | Second | Database |  |
| BatchSize | The uncompressed, expected data size in an aggregated batch for ingestion | Byte | Database | Applicable |
| BatchesProcessed | The number of batches aggregated for ingestion | Count | Database, SealReason |  |
| CPU | The CPU utilization level | Percent |  | Applicable |
| CacheUtilization | The utilization level in the cluster scope | Percent |  | Applicable |
| ContinuousExportMaxLatenessMinutes | The lateness (in minutes) reported by the continuous export jobs in the cluster | Count |  | Applicable |
| ContinuousExportNumOfRecordsExported | The number of records exported, fired for every storage artifact written during the export operation | Count |  | Applicable |
| ContinuousExportPendingCount | The number of pending continuous export jobs ready for execution | Count |  | Applicable |
| ContinuousExportResult | Indicates whether continuous export succeeded or failed | Count | ContinuousExportName, Result, Database | Applicable |
| EventsProcessedForEventHubs | The number of events processed by the cluster when ingesting from Event/IoT Hub | Count | EventStatus |  |
| ExportUtilization | The export utilization | Percent |  | Applicable |
| IngestionLatencyInSeconds | The ingestion time from the source (for example, if message is in EventHub) to the cluster in seconds | Second |  | Applicable |
| IngestionResult | The number of ingestion operations | Count | IngestionResultDetails |  |
| IngestionUtilization | The ratio of used ingestion slots in the cluster | Percent |  | Applicable |
| IngestionVolumeInMB | The overall volume of ingested data to the cluster (in MB) | MegaByte |  | Applicable |
| InstanceCount | The total instance count | Count |  |  |
| KeepAlive | Sanity check, indicating how the cluster responds to queries | Count |  | Applicable |
| QueryDuration | The queries duration in seconds | MilliSecond | QueryStatus | Applicable |
| SteamingIngestRequestRate | The streaming ingest request rate (requests per second) | Count |  |  |
| StreamingIngestDataRate | The streaming ingest data rate (MB per second) | Count |  |  |
| StreamingIngestDuration | The streaming ingest duration in milliseconds | MilliSecond |  |  |
| StreamingIngestResults | The streaming ingest result | Count | Result |  |
| TotalNumberOfConcurrentQueries | The total number of concurrent queries | Count |  | Applicable |
| TotalNumberOfExtents | The total number of data extents | Count |  | Applicable |
| TotalNumberOfThrottledCommands | The total number of throttled commands | Count | CommandType |  |
| TotalNumberOfThrottledQueries | The total number of throttled queries | Count |  | Applicable |


---


## Source: monitor-azure-data-factory.md


---
title: Azure Data Factory (V1, V2) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-factory
scraped: 2026-02-18T05:50:27.051532
---

# Azure Data Factory (V1, V2) monitoring

# Azure Data Factory (V1, V2) monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Data Factory (V1, V2). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Data fact 1](https://dt-cdn.net/images/2021-03-12-10-56-34-1618-f4f03adbc4.png)

![Data fact 2](https://dt-cdn.net/images/2021-03-12-11-01-37-1813-741106667f.png)

## Available metrics

### Azure Data Factory V1

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| FailedRuns | The total number of runs that failed within a minute window | pipelineName, activityName | Count | Applicable |
| SuccessfulRuns | The total number of runs that succeeded within a minute window | pipelineName, activityName | Count | Applicable |

### Azure Data Factory V2

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ActivityCancelledRuns | The total number of activity runs that were cancelled within a minute window | ActivityType, PipelineName, FailureType, Name | Count |  |
| ActivityFailedRuns | The total number of activity runs that failed within a minute window | ActivityType, PipelineName, FailureType, Name | Count | Applicable |
| ActivitySucceededRuns | The total number of activity runs that succeeded within a minute window | ActivityType, PipelineName, FailureType, Name | Count | Applicable |
| FactorySizeInGbUnits | Total factory size (GB unit) |  | GigaByte |  |
| IntegrationRuntimeAvailableMemory | Integration runtime available memory | IntegrationRuntimeName, NodeName | Byte | Applicable |
| IntegrationRuntimeAvailableNodeNumber | Integration runtime available node count | IntegrationRuntimeName | Count |  |
| IntegrationRuntimeAverageTaskPickupDelay | Integration runtime queue duration | IntegrationRuntimeName | Second |  |
| IntegrationRuntimeCpuPercentage | Integration runtime CPU utilization | IntegrationRuntimeName, NodeName | Percent | Applicable |
| IntegrationRuntimeQueueLength | Integration runtime queue length | IntegrationRuntimeName | Count |  |
| MaxAllowedFactorySizeInGbUnits | Maximum allowed factory size (GB unit) |  | GigaByte |  |
| MaxAllowedResourceCount | Maximum allowed entities count |  | Count |  |
| PipelineCancelledRuns | Cancelled pipeline runs metrics | FailureType, Name | Count |  |
| PipelineFailedRuns | Failed pipeline runs metrics | FailureType, Name | Count | Applicable |
| PipelineSucceededRuns | Succeeded pipeline runs metrics | FailureType, Name | Count | Applicable |
| ResourceCount | Total entities count |  | Count |  |
| SSISIntegrationRuntimeStartCancel | The total number of SSIS IR starts that were cancelled within a minute window | IntegrationRuntimeName | Count |  |
| SSISIntegrationRuntimeStartFailed | The total number of SSIS IR starts that failed within a minute window | IntegrationRuntimeName | Count |  |
| SSISIntegrationRuntimeStartSucceeded | The total number of SSIS IR starts that succeeded within a minute window | IntegrationRuntimeName | Count |  |
| SSISIntegrationRuntimeStopStuck | The total number of SSIS IR stops that were stuck within a minute window | IntegrationRuntimeName | Count |  |
| SSISIntegrationRuntimeStopSucceeded | The total number of SSIS IR stops that succeeded within a minute window | IntegrationRuntimeName | Count |  |
| SSISPackageExecutionCancel | The total number of SSIS package executions that were cancelled within a minute window | IntegrationRuntimeName | Count |  |
| SSISPackageExecutionFailed | The total number of SSIS package executions that failed within a minute window | IntegrationRuntimeName | Count |  |
| SSISPackageExecutionSucceeded | The total number of SSIS package executions that succeeded within a minute window | IntegrationRuntimeName | Count |  |
| TriggerCancelledRuns | The total number of trigger runs that were cancelled within a minute window | Name, FailureType | Count |  |
| TriggerFailedRuns | The total number of trigger runs that failed within a minute window | Name, FailureType | Count | Applicable |
| TriggerSucceededRuns | The total number of trigger runs that succeeded within a minute window | Name, FailureType | Count | Applicable |


---


## Source: monitor-azure-data-lake-analytics.md


---
title: Azure Data Lake Analytics monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-analytics
scraped: 2026-02-17T21:26:47.681657
---

# Azure Data Lake Analytics monitoring

# Azure Data Lake Analytics monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Data Lake Analytics. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Lake analyt](https://dt-cdn.net/images/2021-03-12-11-03-26-861-0d68610484.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| JobEndedSuccess | Count of successful jobs | containerName | Count | Applicable |
| JobEndedFailure | Count of failed jobs | containerName | Count | Applicable |
| JobEndedCancelled | Count of cancelled jobs |  | Count | Applicable |
| JobAUEndedSuccess | Total AU time for successful jobs |  | Second | Applicable |
| JobAUEndedFailure | Total AU time for failed jobs |  | Second | Applicable |
| JobAUEndedCancelled | Total AU time for cancelled jobs |  | Second | Applicable |
| JobStage | Progress of jobs |  | Count |  |


---


## Source: monitor-azure-data-lake-storage-gen1.md


---
title: Azure Data Lake Storage Gen1 monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-storage-gen1
scraped: 2026-02-18T05:50:54.360993
---

# Azure Data Lake Storage Gen1 monitoring

# Azure Data Lake Storage Gen1 monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Data Lake Storage Gen1. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Datalake stor](https://dt-cdn.net/images/2021-03-12-11-05-12-1836-18b60d158c.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| TotalStorage | Total amount of data stored in the account | Byte | Applicable |
| ReadRequests | Count of data read requests to the account | Count | Applicable |
| DataRead | Total amount of data read from the account | Byte | Applicable |
| WriteRequests | Count of data write requests to the account | Count | Applicable |
| DataWritten | Total amount of data written from the account | Byte | Applicable |


---


## Source: monitor-azure-data-share.md


---
title: Azure Data Share monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-share
scraped: 2026-02-15T09:11:51.205877
---

# Azure Data Share monitoring

# Azure Data Share monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Data Share. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Data share](https://dt-cdn.net/images/dashboard-80-1920-72f664b28a.png)

## Available metrics

| Name | Dimensions | Unit | Recommended |
| --- | --- | --- | --- |
| FailedShareSubscriptionSynchronizations |  | Count | Applicable |
| FailedShareSynchronizations |  | Count | Applicable |
| ShareCount | ShareName | Count | Applicable |
| ShareSubscriptionCount |  | Count | Applicable |
| SucceededShareSubscriptionSynchronizations |  | Count | Applicable |
| SucceededShareSynchronizations |  | Count | Applicable |


---


## Source: monitor-azure-db-mariadb.md


---
title: Azure Database for MariaDB monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mariadb
scraped: 2026-02-18T05:57:02.329371
---

# Azure Database for MariaDB monitoring

# Azure Database for MariaDB monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 25, 2020

On the Azure Database for MariaDB overview page you can see if youâre running out of CPU or facing a high I/O percentage, so you always know which queries need to be optimized.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

Optionally, for OneAgent integration, see [how database activity is monitored](/docs/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Learn about automatic detection and monitoring of database services in your application environment.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Mariadb dash](https://dt-cdn.net/images/azuredbformariadb-3481-86c2844045.png)

### Set up a management zone

To import a dashboard for Azure Database for MariaDB, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to those relevant to this service.

When you create a management zone for this dashboard:

1. Create a rule that identifies services based on a common property:

   * Service type: `Database`
   * Technology: `MariaDB`
   * Service topology: `Opaque service`
2. Add a condition for the database name to contain the `mariadb` string (case sensitive.)

Example

![Azure management zone](https://dt-cdn.net/images/azuredbformariadbmanagementzone-2686-28aa52c965.png)

After you create the management zone, select it from your dashboard (**Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | Active connections | Count | Applicable |
| backup\_storage\_used | Backup storage used | Bytes |  |
| cpu\_percent | CPU percent | Percent | Applicable |
| connections\_failed | Failed connections | Count | Applicable |
| io\_consumption\_percent | IO percent | Percent | Applicable |
| memory\_percent | Memory percent | Percent | Applicable |
| network\_bytes\_ingress | Network In across active connections | Bytes | Applicable |
| network\_bytes\_egress | Network Out across active connections | Bytes | Applicable |
| seconds\_behind\_master | Replication lag in seconds | Count | Applicable |
| serverlog\_storage\_limit | Server log storage limit | Bytes |  |
| serverlog\_storage\_percent | Server log storage percent | Percent | Applicable |
| serverlog\_storage\_usage | Server log storage used | Bytes |  |
| storage\_limit | Storage limit | Bytes |  |
| storage\_percent | Storage percent | Percent | Applicable |
| storage\_used | Storage used | Bytes |  |


---


## Source: monitor-azure-db-mysql.md


---
title: Azure Database for MySQL monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql
scraped: 2026-02-17T21:31:50.555767
---

# Azure Database for MySQL monitoring

# Azure Database for MySQL monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 25, 2020

Deprecation notice

On 16 September 2024, Azure Database for MySQL will be retired. Azure introduced a new service, see [Azure Database for MySQL Flexible Servers monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers "Monitor Azure DB for Database for MySQL Flexible Servers and view available metrics.").

The Azure Database for MySQL overview page serves as a comprehensive overview of your MySQL servers and database instances. From here you can gain full visibility and check if your database is healthy, under-performing, or if there are any failed connections.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

Optionally, for OneAgent integration, see [how database activity is monitored](/docs/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Learn about automatic detection and monitoring of database services in your application environment.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Mysql dash](https://dt-cdn.net/images/azuredbformysql-1920-eef37d7ad6.png)

### Set up a management zone

To import a dashboard for Azure Database for MySQL, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to those relevant to this service.

When you create a management zone for this dashboard:

1. Create a rule that identifies services based on a common property:

   * Service type equals `Database`
   * Service topology equals `Opaque service`
2. Add a condition for the database name to contain the `mysql` string (case sensitive.)

Example

![Azure management zone](https://dt-cdn.net/images/azuredbformysqlmanagementzone-2662-467d58e129.webp)

After you create the management zone, assign it to your dashboard (from the dashboard, select **Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | Active connections | Count | Applicable |
| backup\_storage\_used | Backup storage used | Bytes |  |
| cpu\_percent | CPU percent | Percent | Applicable |
| connections\_failed | Failed connections | Count | Applicable |
| io\_consumption\_percent | IO percent | Percent | Applicable |
| memory\_percent | Memory percent | Percent | Applicable |
| network\_bytes\_ingress | Network In across active connections | Bytes | Applicable |
| network\_bytes\_egress | Network Out across active connections | Bytes | Applicable |
| seconds\_behind\_master | Replication lag in seconds | Count | Applicable |
| serverlog\_storage\_limit | Server log storage limit | Bytes |  |
| serverlog\_storage\_percent | Server log storage percent | Percent | Applicable |
| serverlog\_storage\_usage | Server log storage used | Bytes |  |
| storage\_limit | Storage limit | Bytes |  |
| storage\_percent | Storage percent | Percent | Applicable |
| storage\_used | Storage used | Bytes |  |


---


## Source: monitor-azure-db-postgresql.md


---
title: Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-postgresql
scraped: 2026-02-18T05:47:42.861477
---

# Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring

# Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) monitoring

* Latest Dynatrace
* How-to guide
* 6-min read
* Published Jun 25, 2020

On the Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) overview pages you get insights into various aspects of database performance, including CPU and memory usage, active connections, storage space, and much more.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

Optionally, for OneAgent integration, see [how database activity is monitored](/docs/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Learn about automatic detection and monitoring of database services in your application environment.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Postgres dash](https://dt-cdn.net/images/azuredbforpostgresql-2976-bc0290ba6d.png)

![Hyper](https://dt-cdn.net/images/azuredbforpostgresqlhyperscale-3017-95194857cf.png)

### Set up a management zone

To import a dashboard for Azure Database for PostgreSQL, you need to [set up a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") to limit the entities displayed on the dashboard to those relevant to this service.

When you create a management zone for this dashboard:

1. Create a rule that identifies services based on a common property:

   * Service topology: `Opaque service`
   * Service type: `Database`
2. Add a condition for the database name to contain the `postgres` string (case sensitive.)

Example

![Azure management zone](https://dt-cdn.net/images/azuredbforpostgresqlmanagementzone-2700-c85a5f89c0.webp)

You can see whether a dashboard requires a management zone in the rules setup.

After you create the management zone, assign it to your dashboard (from the dashboard, select **Edit** > **Settings** > **Default management zone**). For more information, see [Dashboard timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## Available metrics

### Azure Database for PostgreSQL (Single Server)

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | The number of active connections to the server | Count | Applicable |
| backup\_storage\_used | The amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server. | Bytes |  |
| cpu\_percent | The percentage of CPU in use | Percent | Applicable |
| connections\_failed | The number of established connections that failed | Count | Applicable |
| io\_consumption\_percent | The percentage of IO in use | Percent | Applicable |
| pg\_replica\_log\_delay\_in\_bytes | Lag in bytes of the most lagging replica | Bytes |  |
| memory\_percent | The percentage of memory in use | Percent | Applicable |
| network\_bytes\_ingress | Network in across active connections | Bytes | Applicable |
| network\_bytes\_egress | Network out across active connections | Bytes | Applicable |
| pg\_replica\_log\_delay\_in\_seconds | The time since the last replayed transaction. This metric is available for replica servers only. | Seconds | Applicable |
| serverlog\_storage\_limit | The maximum server log storage for this server | Bytes |  |
| serverlog\_storage\_percent | The percentage of server log storage used out of the server's maximum server log storage | Percent | Applicable |
| serverlog\_storage\_usage | The amount of server log storage in use | Bytes |  |
| storage\_limit | The maximum storage for this server | Bytes |  |
| storage\_percent | The percentage of storage used out of the server's maximum | Percent | Applicable |
| storage\_used | The amount of storage in use. The storage used by the service may include the database files, transaction logs, and the server logs. | Bytes |  |

### Azure Database for PostgreSQL Hyperscale

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | The number of active connections to the server | Count | Applicable |
| cpu\_percent | The percentage of CPU in use | Percent | Applicable |
| iops | The number of requests that your application is sending to the storage disks in one second | Count | Applicable |
| memory\_percent | The percentage of memory in use | Percent | Applicable |
| network\_bytes\_egress | Network out across active connections | Byte | Applicable |
| network\_bytes\_ingress | Network in across active connections | Byte | Applicable |
| storage\_percent | The percentage of storage used out of the server's maximum | Percent | Applicable |
| storage\_used | The amount of storage in use. The storage used by the service may include the database files, transaction logs, and the server logs. | Byte |  |

### Azure Database for PostgreSQL - Flexible Server

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| active\_connections | Number of connections to your server. | Count | Applicable |
| backup\_storage\_used | Amount of backup storage used. This metric represents the sum of storage consumed by all the full database backups, differential backups, and log backups retained based on the backup retention period set for the server. The frequency of the backups is service managed. For geo-redundant storage, backup storage usage is twice that of the locally redundant storage. | Byte |  |
| connections\_failed | Failed connections. | Count | Applicable |
| connections\_succeeded | Succeeded connections. | Count |  |
| cpu\_credits\_consumed | Number of credits used by the flexible server. Applicable to Burstable tier. | Count |  |
| cpu\_credits\_remaining | Number of credits available to burst. Applicable to Burstable tier. | Count |  |
| cpu\_percent | Percentage of CPU in use. | Percent | Applicable |
| disk\_queue\_depth | Number of outstanding I/O operations to the data disk. | Count |  |
| iops | Number of I/O operations to disk per second. | Count | Applicable |
| maximum\_used\_transactionIDs | Maximum transaction ID in use. | Count |  |
| memory\_percent | Percentage of memory in use. | Percent | Applicable |
| network\_bytes\_ingress | Amount of incoming network traffic. | Byte | Applicable |
| network\_bytes\_egress | Amount of outgoing network traffic. | Byte | Applicable |
| read\_iops | Number of data disk I/O read operations per second. | Count |  |
| read\_throughput | Bytes read per second from disk. | Count | Applicable |
| storage\_free | Amount of storage space available. | Byte |  |
| storage\_percent | Percent of storage space used. The storage used by the service may include the database files, transaction logs, and the server logs. | Percent | Applicable |
| storage\_used | The storage used by the service may include the database files, transaction logs, and the server logs. | Byte |  |
| txlogs\_storage\_used | Amount of storage space used by the transaction logs. | Byte |  |
| write\_iops | Number of data disk I/O write operations per second. | Count |  |
| write\_throughput | Bytes written per second to disk. | Count | Applicable |


---


## Source: monitor-azure-device-provisioning-service.md


---
title: Azure Device Provisioning Service monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-device-provisioning-service
scraped: 2026-02-18T05:49:58.393847
---

# Azure Device Provisioning Service monitoring

# Azure Device Provisioning Service monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Device Provisioning Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

The Device Provisioning Service instance needs to be linked to IoT Hubs in order to be able to create group and individual enrollments.

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Device provisioning](https://dt-cdn.net/images/dashboard-82-1920-1723ded01c.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| AttestationAttempts | The number of device attestations attempted | ProvisioningServiceName, Status, Protocol | Count | Applicable |
| DeviceAssignments | The number of devices assigned to an IoT hub | ProvisioningServiceName, IotHubName | Count | Applicable |
| RegistrationAttempts | The number of device registrations attempted | ProvisioningServiceName, IotHubName, Status | Count | Applicable |


---


## Source: monitor-azure-dns-zone.md


---
title: Azure DNS Zone monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-dns-zone
scraped: 2026-02-17T21:30:33.388254
---

# Azure DNS Zone monitoring

# Azure DNS Zone monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 22, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure DNS Zone. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.201+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![DNS zone](https://dt-cdn.net/images/dashboard-83-2495-4e32820d60.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| QueryVolume | The volume of DNS queries | Count | Applicable |
| RecordSetCapacityUtilization | The percentage utilization of the maximum limit of record sets for your DNS zone | Percent | Applicable |
| RecordSetCount | The count of DNS record sets within your DNS zone | Count | Applicable |


---


## Source: monitor-azure-event-grid.md


---
title: Azure Event Grid (Domain Topics, Topics, System Topics) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid
scraped: 2026-02-18T05:47:01.016739
---

# Azure Event Grid (Domain Topics, Topics, System Topics) monitoring

# Azure Event Grid (Domain Topics, Topics, System Topics) monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Event Grid (Domain Topics, Topics, System Topics). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Eventgrid dash](https://dt-cdn.net/images/domain-dashboard-2831-82aa7e47f2.png)

![Topics](https://dt-cdn.net/images/topic-dashboard-1850-f3c283d392.png)

![System](https://dt-cdn.net/images/system-dashboard-1805-f6d8b147c2.png)

## Available metrics

### Azure Event Grid Domain Topics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, DeadLetterReason | Count |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, Error, ErrorType | Count | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | Topic, EventSubscriptionName, DomainEventSubscriptionName | MilliSecond | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName, DropReason | Count | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Topic, ErrorType, Error | Count | Applicable |
| PublishSuccessCount | Total events published to this topic | Topic | Count | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds |  | MilliSecond | Applicable |

### Azure Event Grid Topics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Total events published to this topic | Count |  | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds | MilliSecond |  | Applicable |
| UnmatchedEventCount | Total events not matching any of the event subscriptions for this topic | Count |  | Applicable |

### Azure Event Grid System Topics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Total dead-lettered events matching to this event subscription | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Total events failed to deliver to this event subscription | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Total events delivered to this event subscription | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Destination processing duration in milliseconds | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Total dropped events matching to this event subscription | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Total events matched to this event subscription | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Total events failed to publish to this topic | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Total events published to this topic | Count |  | Applicable |
| PublishSuccessLatencyInMs | Publish success latency in milliseconds | MilliSecond |  | Applicable |
| UnmatchedEventCount | Total events not matching any of the event subscriptions for this topic | Count |  | Applicable |


---


## Source: monitor-azure-event-hubs.md


---
title: Azure Event Hubs (Clusters) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hubs
scraped: 2026-02-16T21:30:17.283935
---

# Azure Event Hubs (Clusters) monitoring

# Azure Event Hubs (Clusters) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Event Hubs (Clusters). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Eventhub](https://dt-cdn.net/images/2021-03-12-11-08-56-1665-d814b13d6b.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ActiveConnections | Total active connections for Microsoft.EventHub |  | Count |  |
| AvailableMemory | Available memory for the Event Hub Cluster as a percentage of total memory | Role | Percent | Applicable |
| CPU | CPU utilization for the Event Hub Cluster as a percentage | Role | Percent | Applicable |
| CaptureBacklog | Captured backlog for Microsoft.EventHub |  | Count |  |
| CapturedBytes | Captured bytes for Microsoft.EventHub |  | Byte |  |
| CapturedMessages | Captured messages for Microsoft.EventHub |  | Count |  |
| ConnectionsClosed | Connections closed for Microsoft.EventHub |  | Count |  |
| ConnectionsOpened | Connections opened for Microsoft.EventHub |  | Count |  |
| IncomingBytes | Incoming bytes for Microsoft.EventHub |  | Byte | Applicable |
| IncomingMessages | Incoming messages for Microsoft.EventHub |  | Count | Applicable |
| IncomingRequests | Incoming requests for Microsoft.EventHub |  | Count | Applicable |
| OutgoingBytes | Outgoing bytes for Microsoft.EventHub |  | Byte | Applicable |
| OutgoingMessages | Outgoing messages for Microsoft.EventHub |  | Count | Applicable |
| QuotaExceededErrors | Quota exceeded errors for Microsoft.EventHub |  | Count | Applicable |
| ServerErrors | Server errors for Microsoft.EventHub. |  | Count | Applicable |
| Size | Size of an EventHub in Bytes. | Role | Byte |  |
| SuccessfulRequests | Successful requests for Microsoft.EventHub |  | Count |  |
| ThrottledRequests | Throttled requests for Microsoft.EventHub |  | Count | Applicable |
| UserErrors | User errors for Microsoft.EventHub |  | Count | Applicable |


---


## Source: monitor-azure-expressroute-circuit.md


---
title: Azure ExpressRoute Circuit monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-expressroute-circuit
scraped: 2026-02-16T21:30:24.027099
---

# Azure ExpressRoute Circuit monitoring

# Azure ExpressRoute Circuit monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure ExpressRoute Circuit. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Express dash](https://dt-cdn.net/images/dashboard-36-1699-420811ae56.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ArpAvailability | ARP availability from MSEE towards all peers | PeeringType, Peer | Percent | Applicable |
| BgpAvailability | BGP availability from MSEE towards all peers | PeeringType, Peer | Percent | Applicable |
| BitsInPerSecond | Bits ingressing Azure per second | PeeringType | PerSecond | Applicable |
| BitsOutPerSecond | Bits egressing Azure per second | PeeringType | PerSecond | Applicable |
| QosDropBitsInPerSecond | Ingress bits of data dropped per second |  | PerSecond | Applicable |
| QosDropBitsOutPerSecond | Egress bits of data dropped per second |  | PerSecond | Applicable |


---


## Source: monitor-azure-firewall.md


---
title: Azure Firewall monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-firewall
scraped: 2026-02-18T05:45:43.011366
---

# Azure Firewall monitoring

# Azure Firewall monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Firewall. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Firewall](https://dt-cdn.net/images/2021-03-12-11-11-35-1340-4fd1a156f8.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ApplicationRuleHit | Number of times application rules were hit | Status, Reason, Protocol, Protocol | Count | Applicable |
| DataProcessed | Total amount of data processed by this firewall |  | Byte | Applicable |
| FirewallHealth | Indicates the overall health of this firewall | Status, Reason | Percent | Applicable |
| NetworkRuleHit | Number of times network rules were hit | Status, Reason | Count | Applicable |
| SNATPortUtilization | Percentage of outbound SNAT ports currently in use | Protocol | Percent |  |


---


## Source: monitor-azure-front-door.md


---
title: Azure Front Door (classic) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door
scraped: 2026-02-17T21:31:09.161905
---

# Azure Front Door (classic) monitoring

# Azure Front Door (classic) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Sep 27, 2023

The Azure Front Door (classic) overview page gives you visibility into the number of served client requests, latency, and the efficiency of your routing.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

This service monitors previous (classic) offering of [Azure Front Doorï»¿](https://dt-url.net/rz0390g).

For information regarding the latest Microsoft [Azure Front Door Standard and Premiumï»¿](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview) service, `Front Door and CDN profile`, see [Azure Front Door Standard/Premium and CDN profiles monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles "Monitor Azure Front Door Standard/Premium and CDN profiles and view available metrics.").

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Frontdoor dash](https://dt-cdn.net/images/frontdoor-1600-ab764051bd.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| BackendHealthPercentage | Percentage of successful health probes from the HTTP/S proxy to backends | Percent | Applicable |
| BackendRequestCount | Number of requests sent from the HTTP/S proxy to backends | Count | Applicable |
| BackendRequestLatency | Time from when the request was sent by the HTTP/S proxyMySQL to the backend until the HTTP/S proxy received the last response byte from the backend | MilliSeconds | Applicable |
| BillableResponseSize | Number of billable bytes (minimum 2KB per request) sent as responses from HTTP/S proxy to clients | Bytes |  |
| RequestCount | Number of client requests served by the HTTP/S proxy | Count | Applicable |
| RequestSize | Number of bytes sent as requests from clients to the HTTP/S proxy | Bytes | Applicable |
| ResponseSize | Number of bytes sent as responses from HTTP/S proxy to clients | Bytes | Applicable |
| TotalLatency | Time calculated from when the client request was received by the HTTP/S proxy until the client acknowledged the last response byte from the HTTP/S proxy | MilliSeconds | Applicable |
| WebApplicationFirewallRequestCount | Number of client requests processed by the Web Application Firewall | Count | Applicable |


---


## Source: monitor-azure-gateway-load-balancer.md


---
title: Azure Gateway Load Balancer monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer
scraped: 2026-02-18T05:52:19.582116
---

# Azure Gateway Load Balancer monitoring

# Azure Gateway Load Balancer monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Gateway Load Balancer. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure Load Balancer (Microsoft.Network/loadBalancers). While you have this service configured, you can't have Azure Load Balancers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Data path availability | Average Load Balancer data path availability per time duration | Frontend IP address, Frontend port | Count | Applicable |
| Health probe status | Average Load Balancer health probe status per time duration | Protocol type, Backend port, Frontend IP address, Frontend port, Backend IP address | Count | Applicable |
| Byte count | Total number of Bytes transmitted within time period | Frontend IP address, Frontend port, Direction | Byte |  |
| Packet count | Total number of Packets transmitted within time period | Frontend IP address, Frontend port, Direction | Count | Applicable |
| SYN count | Total number of SYN Packets transmitted within time period | Frontend IP address, Frontend port, Direction | Count |  |


---


## Source: monitor-azure-integration-service-environment.md


---
title: Azure Integration Service Environment monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-integration-service-environment
scraped: 2026-02-18T05:48:15.401939
---

# Azure Integration Service Environment monitoring

# Azure Integration Service Environment monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Integration Service Environment. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.198+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Azure Integration Service Environment](https://dt-cdn.net/images/2021-03-12-11-14-12-1724-951bced50f.png)

Azure Integration Service Environment can be connected with Azure Logic Apps. For more information, see [Connect to Azure virtual networks from Azure Logic Apps by using an integration service environmentï»¿](https://docs.microsoft.com/en-us/azure/logic-apps/connect-virtual-network-vnet-isolated-environment).

**Dashboard for Azure Integration Service Environment with Azure Logic Apps**

![Azure Integration Service Environment + Logic Apps](https://dt-cdn.net/images/2021-03-12-11-15-54-1718-17950831c6.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| ActionLatency | Latency of completed workflow actions | Second | Applicable |
| ActionSuccessLatency | Latency of succeeded workflow actions | Second | Applicable |
| ActionThrottledEvents | Number of workflow action throttled events | Count | Applicable |
| ActionsCompleted | Number of workflow actions completed | Count | Applicable |
| ActionsFailed | Number of workflow actions failed | Count | Applicable |
| ActionsSkipped | Number of workflow actions skipped | Count | Applicable |
| ActionsStarted | Number of workflow actions started | Count | Applicable |
| ActionsSucceeded | Number of workflow actions succeeded | Count | Applicable |
| IntegrationServiceEnvironmentWorkflowMemoryUsage | Workflow memory usage for integration service environment | Percent | Applicable |
| IntegrationServiceEnvironmentWorkflowProcessorUsage | Workflow processor usage for integration service environment | Percent | Applicable |
| RunFailurePercentage | Percentage of workflow runs failed | Percent |  |
| RunLatency | Latency of completed workflow runs | Second | Applicable |
| RunStartThrottledEvents | Number of workflow run start throttled events | Count | Applicable |
| RunSuccessLatency | Latency of succeeded workflow runs | Second | Applicable |
| RunThrottledEvents | Number of workflow action or trigger throttled events | Count | Applicable |
| RunsCancelled | Number of workflow runs cancelled | Count | Applicable |
| RunsCompleted | Number of workflow runs completed | Count | Applicable |
| RunsFailed | Number of workflow runs failed | Count | Applicable |
| RunsStarted | Number of workflow runs started | Count | Applicable |
| RunsSucceeded | Number of workflow runs succeeded | Count | Applicable |
| TriggerFireLatency | Latency of fired workflow triggers | Second | Applicable |
| TriggerLatency | Latency of completed workflow triggers | Second | Applicable |
| TriggerSuccessLatency | Latency of succeeded workflow triggers | Second | Applicable |
| TriggerThrottledEvents | Number of workflow trigger throttled events | Count | Applicable |
| TriggersCompleted | Number of workflow triggers completed | Count | Applicable |
| TriggersFailed | Number of workflow triggers failed | Count | Applicable |
| TriggersFired | Number of workflow triggers fired | Count | Applicable |
| TriggersSkipped | Number of workflow triggers skipped | Count | Applicable |
| TriggersStarted | Number of workflow triggers started | Count | Applicable |
| TriggersSucceeded | Number of workflow triggers succeeded | Count | Applicable |


---


## Source: monitor-azure-iot-central-applications.md


---
title: Azure IoT Central Applications monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-central-applications
scraped: 2026-02-18T05:54:18.563523
---

# Azure IoT Central Applications monitoring

# Azure IoT Central Applications monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 10, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure IoT Central Applications. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.198+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![IoT](https://dt-cdn.net/images/readme-md-11-1920-72bad88b14.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| c2d.property.read.failure | The count of all failed property reads initiated from IoT Central | Count | Applicable |
| c2d.property.read.success | The count of all successful property reads initiated from IoT Central | Count | Applicable |
| c2d.property.update.failure | The count of all failed property updates initiated from IoT Central | Count | Applicable |
| c2d.property.update.success | The count of all successful property updates initiated from IoT Central | Count | Applicable |
| connectedDeviceCount | Number of devices connected to IoT Central | Count | Applicable |
| d2c.property.read.failure | The count of all failed property reads initiated from devices | Count | Applicable |
| d2c.property.read.success | The count of all successful property reads initiated from devices | Count | Applicable |
| d2c.property.update.failure | The count of all failed property updates initiated from devices | Count | Applicable |
| d2c.property.update.success | The count of all successful property updates initiated from devices | Count | Applicable |


---


## Source: monitor-azure-iot-hub.md


---
title: Azure IoT Hub monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub
scraped: 2026-02-18T05:58:42.482181
---

# Azure IoT Hub monitoring

# Azure IoT Hub monitoring

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure IoT Hub. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure IoT Hub (Microsoft.Devices/IotHubs). While you have this service configured, you can't have Azure Iot Hub (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Telemetry message send attempts | Number of device-to-cloud telemetry messages attempted to be sent to your IoT hub |  | Count | Applicable |
| Telemetry messages sent | Number of device-to-cloud telemetry messages sent successfully to your IoT hub |  | Count | Applicable |
| C2D message deliveries completed | Number of cloud-to-device message deliveries completed successfully by the device |  | Count |  |
| C2D messages abandoned | Number of cloud-to-device messages abandoned by the device |  | Count |  |
| C2D messages rejected | Number of cloud-to-device messages rejected by the device |  | Count |  |
| C2D messages expired | Number of expired cloud-to-device messages |  | Count |  |
| Total devices (deprecated) | Number of devices registered to your IoT hub |  | Count |  |
| Connected devices (deprecated) | Number of devices connected to your IoT hub |  | Count |  |
| Routing - telemetry messages delivered | The number of times messages were successfully delivered to all endpoints using IoT Hub routing. If a message is routed to multiple endpoints, this value increases by one for each successful delivery. If a message is delivered to the same endpoint multiple times, this value increases by one for each successful delivery. |  | Count | Applicable |
| Routing - telemetry messages dropped | The number of times messages were dropped by IoT Hub routing due to dead endpoints. This value does not count messages delivered to fallback route as dropped messages are not delivered there. |  | Count | Applicable |
| Routing - telemetry messages orphaned | The number of times messages were orphaned by IoT Hub routing because they didn't match any routing rules (including the fallback rule). |  | Count | Applicable |
| Routing - telemetry messages incompatible | The number of times IoT Hub routing failed to deliver messages due to an incompatibility with the endpoint. This value does not include retries. |  | Count | Applicable |
| Routing - messages delivered to fallback | The number of times IoT Hub routing delivered messages to the endpoint associated with the fallback route. |  | Count | Applicable |
| Routing - messages delivered to event hub | The number of times IoT Hub routing successfully delivered messages to Event Hub endpoints. |  | Count |  |
| Routing - message latency for event hub | The average latency (milliseconds) between message ingress to IoT Hub and message ingress into an Event Hub endpoint. |  | MilliSecond |  |
| Routing - messages delivered to service bus queue | The number of times IoT Hub routing successfully delivered messages to Service Bus queue endpoints. |  | Count |  |
| Routing - message latency for service bus queue | The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a Service Bus queue endpoint. |  | MilliSecond |  |
| Routing - messages delivered to service bus topic | The number of times IoT Hub routing successfully delivered messages to Service Bus topic endpoints. |  | Count |  |
| Routing - message latency for service bus topic | The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a Service Bus topic endpoint. |  | MilliSecond |  |
| Routing - messages delivered to messages/events | The number of times IoT Hub routing successfully delivered messages to the built-in endpoint (messages/events). |  | Count |  |
| Routing - message latency for messages/events | The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into the built-in endpoint (messages/events). |  | MilliSecond |  |
| Routing - messages delivered to storage | The number of times IoT Hub routing successfully delivered messages to storage endpoints. |  | Count |  |
| Routing - message latency for storage | The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a storage endpoint. |  | MilliSecond |  |
| Routing - data delivered to storage | The amount of data (bytes) IoT Hub routing delivered to storage endpoints. |  | Byte |  |
| Routing - blobs delivered to storage | The number of times IoT Hub routing delivered blobs to storage endpoints. |  | Count |  |
| Event grid deliveries | The number of IoT Hub events published to Event Grid. Use the Result dimension for the number of successful and failed requests. | Routing result, Event type | Count |  |
| Event grid latency | The average latency (milliseconds) from when the Iot Hub event was generated to when the event was published to Event Grid. This number is an average between all event types. Use the EventType dimension to see latency of a specific type of event. | Event type | MilliSecond |  |
| Routing deliveries (preview) | The number of times IoT Hub attempted to deliver messages to all endpoints using routing. To see the number of successful or failed attempts, use the Result dimension. To see the reason of failure, like invalid, dropped, or orphaned, use the FailureReasonCategory dimension. You can also use the EndpointName and EndpointType dimensions to understand how many messages were delivered to your different endpoints. The metric value increases by one for each delivery attempt, including if the message is delivered to multiple endpoints or if the message is delivered to the same endpoint multiple times. | Endpoint type, Endpoint name, Failure reason category, Result, Routing source | Count |  |
| Routing delivery latency (preview) | The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into an endpoint. You can use the EndpointName and EndpointType dimensions to understand the latency to your different endpoints. | Endpoint type, Endpoint name, Routing source | MilliSecond |  |
| Routing delivery message size in bytes (preview) | The total size in bytes of messages delivered by IoT hub to an endpoint. You can use the EndpointName and EndpointType dimensions to view the size of the messages in bytes delivered to your different endpoints. The metric value increases for every message delivered, including if the message is delivered to multiple endpoints or if the message is delivered to the same endpoint multiple times. | Endpoint type, Endpoint name, Routing source | Byte |  |
| Successful twin reads from devices | The count of all successful device-initiated twin reads. |  | Count |  |
| Failed twin reads from devices | The count of all failed device-initiated twin reads. |  | Count |  |
| Response size of twin reads from devices | The average, min, and max of all successful device-initiated twin reads. |  | Byte |  |
| Successful twin updates from devices | The count of all successful device-initiated twin updates. |  | Count |  |
| Failed twin updates from devices | The count of all failed device-initiated twin updates. |  | Count |  |
| Size of twin updates from devices | The average, min, and max size of all successful device-initiated twin updates. |  | Byte |  |
| Successful direct method invocations | The count of all successful direct method calls. |  | Count |  |
| Failed direct method invocations | The count of all failed direct method calls. |  | Count |  |
| Request size of direct method invocations | The average, min, and max of all successful direct method requests. |  | Byte |  |
| Response size of direct method invocations | The average, min, and max of all successful direct method responses. |  | Byte |  |
| Successful twin reads from back end | The count of all successful back-end-initiated twin reads. |  | Count |  |
| Failed twin reads from back end | The count of all failed back-end-initiated twin reads. |  | Count |  |
| Response size of twin reads from back end | The average, min, and max of all successful back-end-initiated twin reads. |  | Byte |  |
| Successful twin updates from back end | The count of all successful back-end-initiated twin updates. |  | Count |  |
| Failed twin updates from back end | The count of all failed back-end-initiated twin updates. |  | Count |  |
| Size of twin updates from back end | The average, min, and max size of all successful back-end-initiated twin updates. |  | Byte |  |
| Successful twin queries | The count of all successful twin queries. |  | Count |  |
| Failed twin queries | The count of all failed twin queries. |  | Count |  |
| Twin queries result size | The average, min, and max of the result size of all successful twin queries. |  | Byte |  |
| Successful creations of twin update jobs | The count of all successful creation of twin update jobs. |  | Count |  |
| Failed creations of twin update jobs | The count of all failed creation of twin update jobs. |  | Count |  |
| Successful creations of method invocation jobs | The count of all successful creation of direct method invocation jobs. |  | Count |  |
| Failed creations of method invocation jobs | The count of all failed creation of direct method invocation jobs. |  | Count |  |
| Successful calls to list jobs | The count of all successful calls to list jobs. |  | Count |  |
| Failed calls to list jobs | The count of all failed calls to list jobs. |  | Count |  |
| Successful job cancellations | The count of all successful calls to cancel a job. |  | Count |  |
| Failed job cancellations | The count of all failed calls to cancel a job. |  | Count |  |
| Successful job queries | The count of all successful calls to query jobs. |  | Count |  |
| Failed job queries | The count of all failed calls to query jobs. |  | Count |  |
| Completed jobs | The count of all completed jobs. |  | Count |  |
| Failed jobs | The count of all failed jobs. |  | Count |  |
| Number of throttling errors | Number of throttling errors due to device throughput throttles |  | Count | Applicable |
| Total number of messages used | Number of total messages used today |  | Count |  |
| Total device data usage | Bytes transferred to and from any devices connected to IotHub |  | Byte | Applicable |
| Total device data usage (preview) | Bytes transferred to and from any devices connected to IotHub |  | Byte |  |
| Total devices | Number of devices registered to your IoT hub |  | Count | Applicable |
| Connected devices | Number of devices connected to your IoT hub |  | Count | Applicable |
| Configuration metrics | Metrics for Configuration Operations |  | Count |  |


---


## Source: monitor-azure-key-vault.md


---
title: Azure Key Vault monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-key-vault
scraped: 2026-02-17T05:12:41.483586
---

# Azure Key Vault monitoring

# Azure Key Vault monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Key Vault. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Key vault](https://dt-cdn.net/images/key-vault-dashboard-1920-537bfb50e1.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | Vault requests availability | Percent | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiHit | Total number of service API hits | Count | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiLatency | Overall latency of service API | MilliSecond | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| ServiceApiResult | Total number of service API results | Count | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |
| SaturationShoebox | Vault capacity used | Percent | ActivityType, ActivityName, StatusCode, StatusCodeClass | Applicable |


---


## Source: monitor-azure-logic-apps.md


---
title: Azure Logic Apps monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-logic-apps
scraped: 2026-02-18T05:55:12.065436
---

# Azure Logic Apps monitoring

# Azure Logic Apps monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Logic Apps. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.198+

Logic Apps created on the Standard Plan are supported using the Azure App Services (built-in) service, **not** the Logic App service. You can find it on the Azure overview page, **Functions** view.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Logic apps](https://dt-cdn.net/images/2021-03-12-11-18-46-1890-1b4aa49e05.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| ActionLatency | Latency of completed workflow actions | Second | Applicable |
| ActionSuccessLatency | Latency of successful workflow actions | Second | Applicable |
| ActionThrottledEvents | Number of workflow action throttled events | Count | Applicable |
| ActionsCompleted | Number of completed workflow actions | Count | Applicable |
| ActionsFailed | Number of failed workflow actions | Count | Applicable |
| ActionsSkipped | Number of skipped workflow actions | Count | Applicable |
| ActionsStarted | Number of started workflow actions | Count | Applicable |
| ActionsSucceeded | Number of successful workflow actions | Count | Applicable |
| BillableActionExecutions | Number of billed workflow action executions | Count | Applicable |
| BillableTriggerExecutions | Number of billed workflow trigger executions | Count | Applicable |
| BillingUsageNativeOperation | Number of billed native operation executions | Count | Applicable |
| BillingUsageStandardConnector | Number of billed standard connector executions | Count | Applicable |
| BillingUsageStorageConsumption | Number of billed storage consumption executions | Count | Applicable |
| RunFailurePercentage | Percentage of failed workflow runs | Percent | Applicable |
| RunLatency | Latency of completed workflow runs | Second | Applicable |
| RunStartThrottledEvents | Number of workflow run start throttled events | Count | Applicable |
| RunSuccessLatency | Latency of successful workflow runs | Second | Applicable |
| RunThrottledEvents | Number of workflow action or trigger throttled events | Count | Applicable |
| RunsCancelled | Number of cancelled workflow runs | Count | Applicable |
| RunsCompleted | Number of completed workflow runs | Count | Applicable |
| RunsFailed | Number of failed workflow runs | Count | Applicable |
| RunsStarted | Number of started workflow runs | Count | Applicable |
| RunsSucceeded | Number of successful workflow runs | Count | Applicable |
| TotalBillableExecutions | Number of billed workflow executions | Count | Applicable |
| TriggerFireLatency | Latency of fired workflow triggers | Second | Applicable |
| TriggerLatency | Latency of completed workflow triggers | Second | Applicable |
| TriggerSuccessLatency | Latency of successful workflow triggers | Second | Applicable |
| TriggerThrottledEvents | Number of workflow trigger throttled events | Count | Applicable |
| TriggersCompleted | Number of completed workflow triggers | Count | Applicable |
| TriggersFailed | Number of failed workflow triggers | Count | Applicable |
| TriggersFired | Number of fired workflow triggers | Count | Applicable |
| TriggersSkipped | Number of skipped workflow triggers | Count | Applicable |
| TriggersStarted | Number of started workflow triggers | Count | Applicable |
| TriggersSucceeded | Number of successful workflow triggers | Count | Applicable |


---


## Source: monitor-azure-machine-learning.md


---
title: Azure Machine Learning monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-machine-learning
scraped: 2026-02-18T05:50:50.904087
---

# Azure Machine Learning monitoring

# Azure Machine Learning monitoring

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Machine Learning. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Machine](https://dt-cdn.net/images/2021-03-12-11-20-31-1643-cae1bee39c.png)

![Learning](https://dt-cdn.net/images/2021-03-12-11-22-14-1652-be57e72c22.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Active Cores | Number of active cores. | Scenario, ClusterName | Count | Applicable |
| Active Nodes | Number of active nodes. These are the nodes which are actively running a job. | Scenario, ClusterName | Count | Applicable |
| Cancel Requested Runs | Number of runs where cancel was requested for this workspace. Count is updated when cancellation request has been received for a run. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count |  |
| Cancelled Runs | Number of runs cancelled for this workspace. Count is updated when a run is successfully cancelled. | Scenario, RunType, PublishedPipelineI, ComputeType, PipelineStepType | Count |  |
| Completed Runs | Number of runs completed successfully for this workspace. Count is updated when a run has completed and output has been collected. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| CpuUtilization | Percentage of memory utilization on a CPU node. Utilization is reported at one minute intervals. | Scenario, runId, NodeId, ClusterName | Percent | Applicable |
| Errors | Number of run errors in this workspace. Count is updated whenever run encounters an error. | Scenario | Count | Applicable |
| Failed Runs | Number of runs failed for this workspace. Count is updated when a run fails. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Finalizing Runs | Number of runs entered finalizing state for this workspace. Count is updated when a run has completed but output collection still in progress. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| GpuUtilization | Percentage of memory utilization on a GPU node. Utilization is reported at one-minute intervals. | Scenario, runId, NodeId, DeviceId, ClusterName | Percent | Applicable |
| Idle Cores | Number of idle cores. | Scenario, ClusterName | Count | Applicable |
| Idle Nodes | Number of idle nodes. Idle nodes are the nodes which are not running any jobs but can accept new job if available. | Scenario, ClusterName | Count | Applicable |
| Leaving Cores | Number of leaving cores | Scenario, ClusterName | Count | Applicable |
| Leaving Nodes | Number of leaving nodes. Leaving nodes are the nodes which just finished processing a job and will go to Idle state. | Scenario, ClusterName | Count | Applicable |
| Model Deploy Failed | Number of model deployments that failed in this workspace. | Scenario, StatusCode | Count | Applicable |
| Model Deploy Started | Number of model deployments started in this workspace. | Scenario | Count | Applicable |
| Model Deploy Succeeded | Number of model deployments that succeeded in this workspace. | Scenario | Count | Applicable |
| Model Register Failed | Number of model registrations that failed in this workspace. | Scenario, StatusCode | Count | Applicable |
| Model Register Succeeded | Number of model registrations that succeeded in this workspace. | Scenario | Count | Applicable |
| Not Responding Runs | Number of runs not responding for this workspace. Count is updated when a run enters Not Responding state. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Not Started Runs | Number of runs in Not Started state for this workspace. Count is updated when a request is received to create a run but run information has not yet been populated. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Preempted Cores | Number of preempted cores | Scenario, ClusterName | Count | Applicable |
| Preempted Nodes | Number of preempted nodes. These nodes are the low priority nodes which are taken away from the available node pool. | Scenario, ClusterName | Count | Applicable |
| Preparing Runs | Number of runs that are preparing for this workspace. Count is updated when a run enters Preparing state while the run environment is being prepared. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count |  |
| Provisioning Runs | Number of runs that are provisioning for this workspace. Count is updated when a run is waiting on compute target creation or provisioning. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count |  |
| Queued Runs | Number of runs that are queued for this workspace. Count is updated when a run is queued in compute target. Can occur when waiting for required compute nodes to be ready. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Quota Utilization Percentage | Percent of quota utilized. | Scenario, ClusterName, VmFamilyName, VmPriority | Percent | Applicable |
| Started Runs | Number of runs running for this workspace. Count is updated when a run starts running on required resources. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Starting Runs | Number of runs started for this workspace. Count is updated after request to create run and run info, such as the Run Id, has been populated. | Scenario, RunType, PublishedPipelineId, ComputeType, PipelineStepType | Count | Applicable |
| Total Cores | Number of total cores. | Scenario, ClusterName | Count | Applicable |
| Total Nodes | Number of total nodes. This total includes some of Active Nodes, Idle Nodes, Unusable Nodes, Preempted Nodes, Leaving Nodes. | Scenario, ClusterName | Count | Applicable |
| Unusable Cores | Number of unusable cores. | Scenario, ClusterName | Count | Applicable |
| Unusable Nodes | Number of unusable nodes. Unusable nodes are not functional due to some unresolvable issue. Azure will recycle these nodes. | Scenario, ClusterName | Count | Applicable |
| Warnings | Number of run warnings in this workspace. Count is updated whenever a run encounters a warning. | Scenario | Count | Applicable |


---


## Source: monitor-azure-media-service.md


---
title: Azure Media Services monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-media-service
scraped: 2026-02-17T21:28:51.612472
---

# Azure Media Services monitoring

# Azure Media Services monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Media Services. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.201+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Media serv](https://dt-cdn.net/images/2021-03-12-11-25-06-1565-f7f3707c6b.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| AssetCount | The number of assets already created in current media service account | Count | Applicable |
| AssetQuota | The number of assets allowed for current media service account | Count | Applicable |
| AssetQuotaUsedPercentage | Asset used percentage in current media service account | Percent | Applicable |
| ContentKeyPolicyCount | The number of content key policies already created in current media service account | Count | Applicable |
| ContentKeyPolicyQuota | The number of content key polices allowed for current media service account | Count | Applicable |
| ContentKeyPolicyQuotaUsedPercentage | Content key policy used percentage in current media service account | Percent | Applicable |
| StreamingPolicyCount | The number of streaming policies already created in current media service account | Count | Applicable |
| StreamingPolicyQuota | The number of streaming policies allowed for current media service account | Count | Applicable |
| StreamingPolicyQuotaUsedPercentage | Streaming policy used percentage in current media service account | Percent | Applicable |


---


## Source: monitor-azure-mesh-application.md


---
title: Azure Mesh Application monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-mesh-application
scraped: 2026-02-17T04:57:14.476419
---

# Azure Mesh Application monitoring

# Azure Mesh Application monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 10, 2020

This service has been retired by Microsoft. For more information, see the [Microsoft announcementï»¿](https://azure.microsoft.com/en-us/updates/azure-service-fabric-mesh-preview-retirement/).

Dynatrace ingests metrics from Azure Metrics API for Azure Mesh Application. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Mesh](https://dt-cdn.net/images/dashboard-63-2674-12efdf4c98.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| AllocatedCpu | CPU allocated as per Azure Resource Manager template | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Count | Applicable |
| AllocatedMemory | Memory allocated as per Azure Resource Manager template | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Byte | Applicable |
| ActualCpu | CPU usage | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Count | Applicable |
| ActualMemory | Memory usage | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Byte | Applicable |
| CpuUtilization | Percentage of actual/allocated CPU | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Percent | Applicable |
| MemoryUtilization | Percentage of actual/allocated memory | ApplicationName, ServiceName, CodePackageName, ServiceReplicaName | Percent | Applicable |


---


## Source: monitor-azure-netapp-files.md


---
title: Azure NetApp Files monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-netapp-files
scraped: 2026-02-18T05:44:20.062758
---

# Azure NetApp Files monitoring

# Azure NetApp Files monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure NetApp Files. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Netapp](https://dt-cdn.net/images/image-9-2557-4d14b532da.png)

## Available metrics

## Azure NetApp Files

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| VolumePoolAllocatedSize | Provisioned size of the pool | Byte | Applicable |
| VolumePoolAllocatedUsed | Allocated used size of the pool | Byte | Applicable |
| VolumePoolTotalLogicalSize | Sum of the logical size of all the volumes belonging to the pool | Byte | Applicable |
| VolumePoolTotalSnapshotSize | Sum of snapshot size of all volumes in this pool | Byte | Applicable |

## Azure NetApp Files - Volumes

| Name | Description | Unit |  |
| --- | --- | --- | --- |
| AverageReadLatency | The average time for reads from the volume in milliseconds | MilliSecond | Applicable |
| AverageWriteLatency | The average time for writes from the volume in milliseconds | MilliSecond | Applicable |
| CbsVolumeBackupActive | Volume backup active state | Count |  |
| CbsVolumeLogicalBackupBytes | Logical bytes backed up | Byte |  |
| CbsVolumeOperationComplete | Operation state | Count |  |
| CbsVolumeOperationTransferredBytes | Bytes transferred for operation | Byte |  |
| CbsVolumeProtected | Volume protected state | Count |  |
| ReadIops | Read IOPS | PerSecond | Applicable |
| VolumeAllocatedSize | Volume allocated size | Byte | Applicable |
| VolumeLogicalSize | Volume consumed size | Byte | Applicable |
| VolumeSnapshotSize | Volume snapshot size | Byte |  |
| WriteIops | Write IOPS | PerSecond | Applicable |
| XregionReplicationHealthy | Checks if volume replication status is healthy | Count |  |
| XregionReplicationLagTime | Volume replication lag time | Second |  |
| XregionReplicationLastTransferDuration | Volume replication last transfer duration | Second |  |
| XregionReplicationLastTransferSize | Volume replication last transfer size | Byte |  |
| XregionReplicationRelationshipProgress | Volume replication progress | Byte |  |
| XregionReplicationRelationshipTransferring | Checks if volume replication is transferring | Count |  |
| XregionReplicationTotalTransferBytes | Volume replication total transfer | Byte |  |


---


## Source: monitor-azure-network-interface.md


---
title: Azure Network Interface monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-interface
scraped: 2026-02-18T05:50:05.192401
---

# Azure Network Interface monitoring

# Azure Network Interface monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Network Interface. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Netint](https://dt-cdn.net/images/2021-03-12-11-27-12-1526-0c4e059b90.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| BytesReceivedRate | Number of bytes received by the network interface | Byte | Applicable |
| BytesSentRate | Number of bytes sent by the network interface | Byte | Applicable |
| PacketsReceivedRate | Number of packets received by the network interface | Count | Applicable |
| PacketsSentRate | Number of packets sent by the network interface | Count | Applicable |


---


## Source: monitor-azure-network-watcher.md


---
title: Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher
scraped: 2026-02-18T05:58:33.201962
---

# Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring

# Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Network Watcher (Connection Monitor, Connection Monitor Preview). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Conn monitor](https://dt-cdn.net/images/cm-dashboard-1-3137-226998a645.png)

![Conn monitor preview](https://dt-cdn.net/images/cm-dashboard-1414-d3238a9386.png)

## Available metrics

**Connection Monitor**

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| AverageRoundtripMs | The average network round-trip time (ms) for connectivity monitoring probes sent between source and destination | MilliSecond | Applicable |
| ProbesFailedPercent | The percentage of connectivity monitoring probes failed | Percent | Applicable |

**Connection Monitor Preview**

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| AverageRoundtripMs | The average network RTT for connectivity monitoring probes sent between source and destination | MilliSecond |  |  |
| ChecksFailedPercent | The percentage of failed checks for a test | Percent | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Applicable |
| ProbesFailedPercent | The percentage of connectivity monitoring probes failed | Percent |  |  |
| RoundTripTimeMs | The RTT for checks sent between source and destination | MilliSecond | Source address, Source endpoint name, Source resource ID, Destination address, Destination endpoint name, Destination resource ID, Destination port, Test group name, Test configuration name | Applicable |


---


## Source: monitor-azure-notification-hub.md


---
title: Azure Notification Hub monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-notification-hub
scraped: 2026-02-18T05:58:56.068172
---

# Azure Notification Hub monitoring

# Azure Notification Hub monitoring

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Sep 10, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Notification Hub. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Notification hub](https://dt-cdn.net/images/dashboard-60-1408-5577f14a52.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| incoming | The count of all successful send API calls | Count | Applicable |
| incoming.all.failedrequests | Total incoming failed requests for a notification hub | Count | Applicable |
| incoming.all.requests | Total incoming requests for a notification hub | Count | Applicable |
| incoming.scheduled | Scheduled push notifications sent | Count |  |
| incoming.scheduled.cancel | Scheduled push notifications cancelled | Count |  |
| installation.all | Installation management operations | Count |  |
| installation.delete | Delete installation operations | Count |  |
| installation.get | Get installation operations | Count |  |
| installation.patch | Patch installation operations | Count |  |
| installation.upsert | Create or update installation operations | Count |  |
| notificationhub.pushes | All outgoing notifications of the notification hub | Count | Applicable |
| outgoing.allpns.badorexpiredchannel | The count of pushes that failed because the channel/token/registrationId in the registration was expired or invalid | Count |  |
| outgoing.allpns.channelerror | The count of pushes that failed because the channel was invalid, not associated with the correct app, throttled, or expired | Count |  |
| outgoing.allpns.invalidpayload | The count of pushes that failed because the PNS returned a bad payload error | Count |  |
| outgoing.allpns.pnserror | The count of pushes that failed because there was a problem communicating with the PNS (excludes authentication problems) | Count |  |
| outgoing.allpns.success | The count of all successful notifications | Count |  |
| outgoing.apns.badchannel | The count of pushes that failed because the token is invalid (APNS status code: 8) | Count |  |
| outgoing.apns.expiredchannel | The count of token that were invalidated by the APNS feedback channel | Count |  |
| outgoing.apns.invalidcredentials | The count of pushes that failed because the PNS did not accept the provided credentials, or the credentials are blocked | Count |  |
| outgoing.apns.invalidnotificationsize | The count of pushes that failed because the payload was too large (APNS status code: `7`) | Count |  |
| outgoing.apns.pnserror | The count of pushes that failed because of errors communicating with APNS | Count |  |
| outgoing.apns.success | The count of all successful notifications | Count |  |
| outgoing.gcm.authenticationerror | The count of pushes that failed because the PNS didn't accept the provided credentials, the credentials are blocked, or the `SenderId` isn't correctly configured in the app (GCM result: `MismatchedSenderId`) | Count |  |
| outgoing.gcm.badchannel | The count of pushes that failed because the `registrationId` in the registration wasn't recognized (GCM result: `Invalid Registration`) | Count |  |
| outgoing.gcm.expiredchannel | The count of pushes that failed because the `registrationId` in the registration was expired (GCM result: `NotRegistered`) | Count |  |
| outgoing.gcm.invalidcredentials | The count of pushes that failed because the PNS didn't accept the provided credentials, or the credentials are blocked | Count |  |
| outgoing.gcm.invalidnotificationformat | The count of pushes that failed because the payload wasn't formatted correctly (GCM result: `InvalidDataKey` or `InvalidTtl`) | Count |  |
| outgoing.gcm.invalidnotificationsize | The count of pushes that failed because the payload was too large (GCM result: `MessageTooBig`) | Count |  |
| outgoing.gcm.pnserror | The count of pushes that failed because of errors communicating with GCM | Count |  |
| outgoing.gcm.success | The count of all successful notifications | Count |  |
| outgoing.gcm.throttled | The count of pushes that failed because GCM throttled this app (GCM status code: `501`-`599` or `result:Unavailable`) | Count |  |
| outgoing.gcm.wrongchannel | The count of pushes that failed because the `registrationId` in the registration isn't associated to the current app (GCM result: `InvalidPackageName`) | Count |  |
| outgoing.mpns.authenticationerror | The count of pushes that failed because the PNS didn't accept the provided credentials, or the credentials are blocked | Count |  |
| outgoing.mpns.badchannel | The count of pushes that failed because the `ChannelURI` in the registration wasn't recognized (MPNS status: `404 not found`) | Count |  |
| outgoing.mpns.channeldisconnected | The count of pushes that failed because the `ChannelURI` in the registration was disconnected (MPNS status: `412 not found`) | Count |  |
| outgoing.mpns.dropped | The count of pushes that were dropped by MPNS (MPNS response header: X-NotificationStatus: `QueueFull or Suppressed`) | Count |  |
| outgoing.mpns.invalidcredentials | The count of pushes that failed because the PNS didn't accept the provided credentials, or the credentials are blocked | Count |  |
| outgoing.mpns.invalidnotificationformat | The count of pushes that failed because the payload of the notification was too large | Count |  |
| outgoing.mpns.pnserror | The count of pushes that failed because of errors communicating with MPNS | Count |  |
| outgoing.mpns.success | The count of all successful notifications | Count |  |
| outgoing.mpns.throttled | The count of pushes that failed because MPNS is throttling this app (WNS MPNS: `406 Not Acceptable`) | Count |  |
| outgoing.wns.authenticationerror | Notification not delivered because of errors communicating with Windows Live, invalid credentials, or wrong token | Count |  |
| outgoing.wns.badchannel | The count of pushes that failed because the ChannelURI in the registration was not recognized (WNS status: 404 not found) | Count |  |
| outgoing.wns.channeldisconnected | The notification was dropped because the `ChannelURI` in the registration is throttled (WNS response header: X-WNS-DeviceConnectionStatus: `Disconnected`) | Count |  |
| outgoing.wns.channelthrottled | The notification was dropped because the `ChannelURI` in the registration is throttled (WNS response header: X-WNS-NotificationStatus: `ChannelThrottled`) | Count |  |
| outgoing.wns.dropped | The notification was dropped because the `ChannelURI` in the registration is throttled (X-WNS-NotificationStatus: dropped but not X-WNS-DeviceConnectionStatus: `Disconnected`) | Count |  |
| outgoing.wns.expiredchannel | The count of pushes that failed because the `ChannelURI` is expired (WNS status: `410 Gone`) | Count |  |
| outgoing.wns.invalidcredentials | The count of pushes that failed because the PNS didn't accept the provided credentials, the credentials are blocked, or Windows Live doesn't recognize the credentials | Count |  |
| outgoing.wns.invalidnotificationformat | The format of the notification is invalid (WNS status: `400`). Note that WNS doesn't reject all invalid payloads | Count |  |
| outgoing.wns.invalidnotificationsize | The notification payload is too large (WNS status: `413`) | Count |  |
| outgoing.wns.invalidtoken | The token provided to WNS isn't valid (WNS status: `401 Unauthorized`) | Count |  |
| outgoing.wns.pnserror | Notification not delivered because of errors communicating with WNS | Count |  |
| outgoing.wns.success | The count of all successful notifications | Count |  |
| outgoing.wns.throttled | The count of pushes that failed because WNS is throttling this app (WNS status: `406 Not Acceptable`) | Count |  |
| outgoing.wns.tokenproviderunreachable | Windows Live isn't reachable | Count |  |
| outgoing.wns.wrongtoken | The token provided to WNS is valid, but for another application (WNS status: `403 Forbidden`). This can happen if the `ChannelURI` in the registration is associated with another app. | Count |  |
| registration.all | The count of all successful registration operations (creations, updates, queries, and deletions) | Count |  |
| registration.create | The count of all successful registration creations | Count |  |
| registration.delete | The count of all successful registration deletions | Count |  |
| registration.get | The count of all successful registration queries | Count |  |
| registration.update | The count of all successful registration updates | Count |  |
| scheduled.pending | Pending scheduled notifications | Count |  |


---


## Source: monitor-azure-power-bi.md


---
title: Azure Power BI Embedded monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-power-bi
scraped: 2026-02-16T21:27:57.743476
---

# Azure Power BI Embedded monitoring

# Azure Power BI Embedded monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 10, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Power BI Embedded. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Power bi](https://dt-cdn.net/images/dashboard-61-1468-85d8a9b03d.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| QueryDuration | DAX query duration in last interval | MilliSecond |  | Applicable |
| QueryPoolJobQueueLength | Number of jobs in the queue of the query thread pool | Count |  | Applicable |
| memory\_metric | Memory ranging 0-3 GB for A1, 0-5 GB for A2, 0-10 GB for A3, 0-20 GB for A4, 0-50 GB for A5, and 0-100 GB for A6 | Byte |  | Applicable |
| memory\_thrashing\_metric | Average memory thrashing | Percent |  |  |
| qpu\_high\_utilization\_metric | QPU high utilization in last minute, `1` for high QPU utilization, otherwise `0` | Count |  |  |
| qpu\_metric | QPU ranging 0-100 for S1, 0-200 for S2, and 0-400 for S4 | Count |  | Applicable |
| workload\_memory\_metric | The usage of memory in your capacity resource per workload | Byte | Workload | Applicable |
| workload\_qpu\_metric | The query processing unit (QPU) load on your capacity, per workload | Count | Workload | Applicable |


---


## Source: monitor-azure-private-dns-zone.md


---
title: Azure Private DNS Zone monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-private-dns-zone
scraped: 2026-02-18T05:50:03.480634
---

# Azure Private DNS Zone monitoring

# Azure Private DNS Zone monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Private DNS Zone. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Private dns dash](https://dt-cdn.net/images/privatedns-dashboard-1626-bd25c5d19d.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| QueryVolume | Number of queries served for a DNS zone | Count | Applicable |
| RecordSetCount | Number of Record Sets in a DNS zone | Count | Applicable |
| RecordSetCapacityUtilization | Percentage of Record Set capacity utilized by a DNS zone | Percent | Applicable |
| VirtualNetworkLinkCount | Number of virtual networks associated with a private DNS zone | Count | Applicable |
| VirtualNetworkLinkCapacityUtilization | Percentage of virtual network capacity utilized by a private DNS zone | Percent | Applicable |
| VirtualNetworkWithRegistrationCapacityUtilization | Percentage of capacity utilization for a virtual network with automatic registration that is utilized by a private DNS zone | Percent |  |
| VirtualNetworkWithRegistrationLinkCount | Number of virtual networks that are linked to a private DNS zone and for which automatic registration is activated | Count |  |


---


## Source: monitor-azure-public-ip-addresses.md


---
title: Azure Public IP Address monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-public-ip-addresses
scraped: 2026-02-17T04:57:57.305474
---

# Azure Public IP Address monitoring

# Azure Public IP Address monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Public IP Address. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![IP-dash](https://dt-cdn.net/images/dashboard-21-1352-94948a295c.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| ByteCount | Total number of bytes transmitted within time period | Byte, Port, Direction | Applicable |
| BytesDroppedDDoS | Inbound bytes dropped DDoS | BytePerSecond |  |
| BytesForwardedDDoS | Inbound bytes forwarded DDoS | BytePerSecond |  |
| BytesInDDoS | Inbound bytes DDoS | BytePerSecond |  |
| DDoSTriggerSYNPackets | Inbound SYN packets to trigger DDoS mitigation | PerSecond |  |
| DDoSTriggerTCPPackets | Inbound TCP packets to trigger DDoS mitigation | PerSecond |  |
| DDoSTriggerUDPPackets | Inbound UDP packets to trigger DDoS mitigation | PerSecond |  |
| IfUnderDDoSAttack | Under DDoS attack or not | Count |  |
| PacketCount | Total number of packets transmitted within time period | Count, Port, Direction | Applicable |
| PacketsDroppedDDoS | Inbound packets dropped DDoS | PerSecond |  |
| PacketsForwardedDDoS | Inbound packets forwarded DDoS | PerSecond |  |
| PacketsInDDoS | Inbound packets DDoS | PerSecond |  |
| SynCount | Total number of SYN Packets transmitted within time period | Count, Port, Direction | Applicable |
| TCPBytesDroppedDDoS | Inbound TCP bytes dropped DDoS | BytePerSecond |  |
| TCPBytesForwardedDDoS | Inbound TCP bytes forwarded DDoS | BytePerSecond |  |
| TCPBytesInDDoS | Inbound TCP bytes DDoS | BytePerSecond |  |
| TCPPacketsDroppedDDoS | Inbound TCP packets dropped DDoS | PerSecond |  |
| TCPPacketsForwardedDDoS | Inbound TCP packets forwarded DDoS | PerSecond |  |
| TCPPacketsInDDoS | Inbound TCP packets DDoS | PerSecond |  |
| UDPBytesDroppedDDoS | Inbound UDP bytes dropped DDoS | BytePerSecond |  |
| UDPBytesForwardedDDoS | Inbound UDP bytes forwarded DDoS | BytePerSecond |  |
| UDPBytesInDDoS | Inbound UDP bytes DDoS | BytePerSecond |  |
| UDPPacketsDroppedDDoS | Inbound UDP packets dropped DDoS | PerSecond |  |
| UDPPacketsForwardedDDoS | Inbound UDP packets forwarded DDoS | PerSecond |  |
| UDPPacketsInDDoS | Inbound UDP packets DDoS | PerSecond |  |
| VipAvailability | Average IP address availability per time duration | Percent, Port | Applicable |


---


## Source: monitor-azure-recovery-services-vault.md


---
title: Azure Recovery Services Vault
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-recovery-services-vault
scraped: 2026-02-18T05:44:42.660850
---

# Azure Recovery Services Vault

# Azure Recovery Services Vault

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Mar 07, 2024

Dynatrace version 1.281+ Environment ActiveGate version 1.195+

Dynatrace ingests metrics from Azure Metrics API for Azure Recovery Services Vault. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BackupHealthEvent |  | Backup instance ID, Backup instance name, Datasource ID, Datasource type, Health status | Count | Applicable |
| RestoreHealthEvent |  | Backup instance ID, Backup instance name, Datasource ID, Datasource type, Health status | Count | Applicable |


---


## Source: monitor-azure-relay.md


---
title: Azure Relay monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-relay
scraped: 2026-02-17T21:26:30.872491
---

# Azure Relay monitoring

# Azure Relay monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Relay. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.201+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Relay](https://dt-cdn.net/images/dashboard-62-966-f8f2704383.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ActiveConnections | Total active connections for Azure Relay | EntityName | Count | Applicable |
| ActiveListeners | Total active listeners for Azure Relay | EntityName | Count | Applicable |
| BytesTransferred | Total bytes transferred for Azure Relay | EntityName | Count | Applicable |
| ListenerConnections-ClientError | Client error on listener connections for Azure Relay | EntityName | Count | Applicable |
| ListenerConnections-ServerError | Server error on listener connections for Azure Relay | EntityName | Count | Applicable |
| ListenerConnections-Success | Successful listener connections for Azure Relay | EntityName | Count |  |
| ListenerConnections-TotalRequests | Total listener connections for Azure Relay | EntityName | Count | Applicable |
| ListenerDisconnects | Total listener disconnects for Azure Relay | EntityName | Count |  |
| SenderConnections-ClientError | Client error on sender connection for Azure Relay | EntityName | Count | Applicable |
| SenderConnections-ServerError | Server error on sender connection for Azure Relay | EntityName | Count | Applicable |
| SenderConnections-Success | Successful sender connections for Azure Relay | EntityName | Count |  |
| SenderConnections-TotalRequests | Total sender connections requests for Azure Relay | EntityName | Count | Applicable |
| SenderDisconnects | Total sender disconnects for Azure Relay | EntityName | Count |  |

## Limitations

Metrics are only supported for the Hybrid Connections feature in Azure Relay.


---


## Source: monitor-azure-search.md


---
title: Azure Search Service monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-search
scraped: 2026-02-17T21:32:58.186034
---

# Azure Search Service monitoring

# Azure Search Service monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Search Service. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Search](https://dt-cdn.net/images/2021-03-12-11-30-05-1118-9ee9ae86dc.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| SearchLatency | Average search latency for the search service | Second | Applicable |
| SearchQueriesPerSecond | Search queries per second for the search service | PerSecond | Applicable |
| ThrottledSearchQueriesPercentage | Percentage of search queries that were throttled for the search service | Percent | Applicable |


---


## Source: monitor-azure-signalr.md


---
title: Monitor Azure SignalR
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-signalr
scraped: 2026-02-18T05:51:23.918617
---

# Monitor Azure SignalR

# Monitor Azure SignalR

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure SignalR. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Signalr](https://dt-cdn.net/images/2021-03-12-11-31-44-1700-536213ca69.png)

## Available metrics

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| ConnectionCount | The amount of user connection | Count | Endpoint | Applicable |
| InboundTraffic | The inbound traffic of service | Byte |  | Applicable |
| MessageCount | The total amount of messages | Count |  | Applicable |
| OutboundTraffic | The outbound traffic of service | Byte |  | Applicable |
| SystemErrors | The percentage of system errors | Percent |  | Applicable |
| UserErrors | The percentage of user errors | Percent |  | Applicable |


---


## Source: monitor-azure-sql-data-warehouse.md


---
title: Azure SQL Data Warehouse (legacy)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-data-warehouse
scraped: 2026-02-17T05:02:36.946591
---

# Azure SQL Data Warehouse (legacy)

# Azure SQL Data Warehouse (legacy)

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Aug 12, 2021

The Azure SQL Data Warehouse overview page gives you a comprehensive view of how many jobs and tasks were completed over a period of time. You can also track nodes in different states, such as running, idle, or offline.

## Prerequisites

* Dynatrace version 1.224+
* Environment ActiveGate version 1.205+

This service monitors the data warehouse type of SQL Databases. You can find the already monitored resources on the Azure overview page in the **Cloud services** section.

To monitor the SQL Databases user kind, check Azure SQL Servers and the **Databases components** sections on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Active queries | Active queries. Using this metric unfiltered and unsplit displays all active queries running on the system. |  | Count | Applicable |
| Blocked by firewall | The number of logins to the data warehouse from the database application that the firewall blocks. |  | Count | Applicable |
| CPU percentage | The percentage of CPU that all nodes utilize for the data warehouse. |  | Percent | Applicable |
| Cache hit percentage | The sum of all columnstore segments hits in the local SSD cache. |  | Percent |  |
| Cache used percentage | The sum of all bytes in the local SSD cache across all nodes. |  | Percent |  |
| DWU limit | The Data Warehouse Unit, which is the service-level objective of the data warehouse. |  | Count | Applicable |
| DWU percentage | The maximum value when compared between CPU percentage and Data IO percentage. |  | Percent | Applicable |
| DWU used | DWU limit \* DWU percentage |  | Count | Applicable |
| Data IO percentage | The percentage of IO that all nodes utilize for the data warehouse. |  | Percent | Applicable |
| Effective cap resource percent | The effective cap resource percent for the workload group. If there are other workload groups with the effective min resource percent higher than `0`, the effective cap resource percent is lowered proportionally. | Is user defined, workload group | Percent |  |
| Effective min resource percent | The effective minimum resource percentage setting allowed, considering the service level and the workload group settings. | Is user defined, workload group | Percent |  |
| Failed connections | The number of failed connections to the data warehouse from the database application. |  | Count | Applicable |
| Local tempdb percentage | The percentage of the local tempdb that all compute nodes utilize. |  | Percent |  |
| Memory percentage | The percentage of memory of the SQL Server utilized across all nodes for the data warehouse. |  | Percent | Applicable |
| Queued queries | Cumulative count of requests queued after the maximum concurrency limit was reached. |  | Count | Applicable |
| Successful connections | The number of successful connections to the data from the database application. |  | Count | Applicable |
| Workload group active queries | The active queries within the workload group. Using this metric unfiltered and unsplit displays all active queries running on the system. | Is user defined, workload group | Count |  |
| Workload group allocation by cap resource percent |  |  |  |  |
| The percentage allocation of resources relative to the effective cap resource percent per workload group. This metric provides the effective utilization of the workload group. | Is user defined, Workload group. | Percent |  |  |
| Workload group allocation by system percent | The percentage allocation of resources relative to the entire system. | Is user defined, workload group | Percent |  |
| Workload group query timeouts | Queries for the workload group that have timed out. | Is user defined, workload group | Count |  |
| Workload group queued queries | Cumulative count of requests queued after the maximum concurrency limit was reached. | Is user defined, workload group | Count |  |


---


## Source: monitor-azure-sql-database-dtu.md


---
title: Azure SQL Database (DTU) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu
scraped: 2026-02-15T09:10:56.316650
---

# Azure SQL Database (DTU) monitoring

# Azure SQL Database (DTU) monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure SQL Database (DTU). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure SQL (Microsoft.Sql/servers/databases). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CPU percentage | CPU percentage |  | Percent | Applicable |
| Data IO percentage | Data IO percentage |  | Percent | Applicable |
| Log IO percentage | Log IO percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| DTU percentage | DTU Percentage. Applies to DTU-based databases. |  | Percent | Applicable |
| Data space used | Data space used. Not applicable to data warehouses. |  | Byte | Applicable |
| Successful connections | Successful Connections | TLS version | Count | Applicable |
| Failed connections - system errors | Failed Connections | Error | Count | Applicable |
| Failed connections - user errors | Failed Connections : User Errors | Error | Count |  |
| Blocked by firewall | Blocked by Firewall |  | Count | Applicable |
| Deadlocks | Deadlocks. Not applicable to data warehouses. |  | Count | Applicable |
| Data space used percent | Data space used percent. Not applicable to data warehouses or hyperscale databases. |  | Percent | Applicable |
| In - memory OLTP storage percent | In-Memory OLTP storage percent. Not applicable to data warehouses. |  | Percent | Applicable |
| Workers percentage | Workers percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| Sessions percentage | Sessions percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| Sessions count | Number of active sessions. Not applicable to Synapse DW Analytics. |  | Count |  |
| DTU limit | DTU Limit. Applies to DTU-based databases. |  | Count | Applicable |
| DTU used | DTU used. Applies to DTU-based databases. |  | Count | Applicable |
| SQL server process core percent | CPU usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\_instance\_cpu\_percent, and will be removed in the future.) |  | Percent |  |
| SQL server process memory percent | Memory usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\_instance\_memory\_percent, and will be removed in the future.) |  | Percent |  |
| Tempdb data file size kB | Space used in tempdb data files in kilobytes. Not applicable to data warehouses. |  | Count |  |
| Tempdb log file size kB | Space used in tempdb transaction log file in kilobytes. Not applicable to data warehouses. |  | Count |  |
| Tempdb percent log used | Space used percentage in tempdb transaction log file. Not applicable to data warehouses. |  | Percent |  |
| Data space allocated | Allocated data storage. Not applicable to data warehouses. |  | Byte |  |
| Successful ledger digest uploads | Ledger digests that were successfully uploaded. |  | Count |  |
| Failed ledger digest uploads | Ledger digests that failed to be uploaded. |  | Count |  |


---


## Source: monitor-azure-sql-database-hyperscale.md


---
title: Azure SQL Database Hyperscale monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-hyperscale
scraped: 2026-02-16T09:29:06.302001
---

# Azure SQL Database Hyperscale monitoring

# Azure SQL Database Hyperscale monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 13, 2021

Dynatrace ingests metrics from Azure Metrics API for Azure SQL Database Hyperscale. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.215+
* Environment ActiveGate version 1.205+

This service monitors the hyperscale type of SQL Databases. You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset. To monitor the SQL Databases user kind, check Azure SQL Servers and the **Databases components** sections on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Hyperscale](https://dt-cdn.net/images/azi-2615-eba6f59034.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| allocated\_data\_storage | Data space allocated | Byte | Applicable |
| base\_blob\_size\_bytes | Base blob storage size | Byte |  |
| blocked\_by\_firewall | Blocked by firewall | Count | Applicable |
| connection\_failed | Failed connections | Count | Applicable |
| connection\_successful | Successful connections | Count | Applicable |
| cpu\_limit | CPU limit | Count | Applicable |
| cpu\_percent | CPU percentage | Percent | Applicable |
| cpu\_used | CPU used | Count | Applicable |
| deadlock | Deadlocks | Count | Applicable |
| log\_backup\_size\_bytes | Log backup storage size | Byte | Applicable |
| log\_write\_percent | Log IO percentage | Percent |  |
| physical\_data\_read\_percent | Data IO percentage | Percent | Applicable |
| sessions\_percent | Sessions percentage | Percent | Applicable |
| snapshot\_backup\_size\_bytes | Snapshot backup storage size | Byte |  |
| sqlserver\_process\_core\_percent | SQL server process core percent | Percent |  |
| sqlserver\_process\_memory\_percent | SQL server process memory percent | Percent |  |
| tempdb\_data\_size | Tempdb data file size kb | Count |  |
| tempdb\_log\_size | Tempdb log file size kb | Count |  |
| tempdb\_log\_used\_percent | Tempdb percent log used | Percent | Applicable |
| workers\_percent | Workers percentage | Percent | Applicable |
| xtp\_storage\_percent | In-memory OLTP storage percent | Percent |  |


---


## Source: monitor-azure-sql-database-vcore.md


---
title: Azure SQL Database (vCore) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore
scraped: 2026-02-17T04:58:00.205544
---

# Azure SQL Database (vCore) monitoring

# Azure SQL Database (vCore) monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure SQL Database (vCore). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure SQL (Microsoft.Sql/servers/databases). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CPU percentage | CPU percentage |  | Percent | Applicable |
| Data IO percentage | Data IO percentage |  | Percent | Applicable |
| Log IO percentage | Log IO percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| Data space used | Data space used. Not applicable to data warehouses. |  | Byte | Applicable |
| Successful connections | Successful Connections | TLS version | Count | Applicable |
| Failed connections - system errors | Failed Connections | Error | Count | Applicable |
| Failed connections - user errors | Failed Connections : User Errors | Error | Count |  |
| Blocked by firewall | Blocked by Firewall |  | Count | Applicable |
| Deadlocks | Deadlocks. Not applicable to data warehouses. |  | Count | Applicable |
| Data space used percent | Data space used percent. Not applicable to data warehouses or hyperscale databases. |  | Percent | Applicable |
| In - memory OLTP storage percent | In-Memory OLTP storage percent. Not applicable to data warehouses. |  | Percent | Applicable |
| Workers percentage | Workers percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| Sessions percentage | Sessions percentage. Not applicable to data warehouses. |  | Percent | Applicable |
| Sessions count | Number of active sessions. Not applicable to Synapse DW Analytics. |  | Count |  |
| CPU limit | CPU limit. Applies to vCore-based databases. |  | Count | Applicable |
| CPU used | CPU used. Applies to vCore-based databases. |  | Count | Applicable |
| SQL server process core percent | CPU usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\_instance\_cpu\_percent, and will be removed in the future.) |  | Percent |  |
| SQL server process memory percent | Memory usage as a percentage of the SQL DB process. Not applicable to data warehouses. (This metric is equivalent to sql\_instance\_memory\_percent, and will be removed in the future.) |  | Percent |  |
| Tempdb data file size kB | Space used in tempdb data files in kilobytes. Not applicable to data warehouses. |  | Count |  |
| Tempdb log file size kB | Space used in tempdb transaction log file in kilobytes. Not applicable to data warehouses. |  | Count |  |
| Tempdb percent log used | Space used percentage in tempdb transaction log file. Not applicable to data warehouses. |  | Percent |  |
| App CPU billed | App CPU billed. Applies to serverless databases. |  | Count |  |
| App CPU percentage | App CPU percentage. Applies to serverless databases. |  | Percent |  |
| App memory percentage | App memory percentage. Applies to serverless databases. |  | Percent |  |
| Data space allocated | Allocated data storage. Not applicable to data warehouses. |  | Byte |  |
| Full backup storage size | Cumulative full backup storage size. Applies to vCore-based databases. Not applicable to Hyperscale databases. |  | Byte |  |
| Differential backup storage size | Cumulative differential backup storage size. Applies to vCore-based databases. Not applicable to Hyperscale databases. |  | Byte |  |
| Log backup storage size | Cumulative log backup storage size. Applies to vCore-based and Hyperscale databases. |  | Byte |  |
| Successful ledger digest uploads | Ledger digests that were successfully uploaded. |  | Count |  |
| Failed ledger digest uploads | Ledger digests that failed to be uploaded. |  | Count |  |


---


## Source: monitor-azure-sql-elastic-pool-dtu.md


---
title: Azure SQL elastic pool (DTU) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu
scraped: 2026-02-16T21:26:02.683177
---

# Azure SQL elastic pool (DTU) monitoring

# Azure SQL elastic pool (DTU) monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure SQL elastic pool (DTU). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure SQL (Microsoft.Sql/servers/elasticpools). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CPU percentage | CPU percentage | Database arm resource ID | Percent | Applicable |
| Data IO percentage | Data IO percentage | Database arm resource ID | Percent | Applicable |
| Log IO percentage | Log IO percentage | Database arm resource ID | Percent | Applicable |
| DTU percentage | DTU Percentage. Applies to DTU-based elastic pools. | Database arm resource ID | Percent | Applicable |
| Data space used percent | Data space used percent. Not applicable to hyperscale |  | Percent | Applicable |
| Workers percentage | Workers percentage | Database arm resource ID | Percent | Applicable |
| Sessions percentage | Sessions percentage | Database arm resource ID | Percent |  |
| Sessions count | Number of active sessions |  | Count | Applicable |
| EDTU limit | eDTU limit. Applies to DTU-based elastic pools. |  | Count | Applicable |
| Data max size | Data max size. Not applicable to hyperscale |  | Byte |  |
| EDTU used | eDTU used. Applies to DTU-based elastic pools. | Database arm resource ID | Count | Applicable |
| Data space used | Data space used. Not applicable to hyperscale | Database arm resource ID | Byte |  |
| In - memory OLTP storage percent | In-Memory OLTP storage percent. Not applicable to hyperscale |  | Percent |  |
| SQL server process core percent | CPU usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\_instance\_cpu\_percent, and will be removed in the future.) |  | Percent |  |
| SQL server process memory percent | Memory usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\_instance\_memory\_percent, and will be removed in the future.) |  | Percent |  |
| Tempdb data file size kB | Space used in tempdb data files in kilobytes. |  | Count |  |
| Tempdb log file size kB | Space used in tempdb transaction log file in kilobytes. |  | Count |  |
| Tempdb percent log used | Space used percentage in tempdb transaction log file |  | Percent |  |
| Data space allocated | Data space allocated. Not applicable to hyperscale | Database arm resource ID | Byte |  |
| Data space allocated percent | Data space allocated percent. Not applicable to hyperscale |  | Percent |  |


---


## Source: monitor-azure-sql-elastic-pool-vcore.md


---
title: Azure SQL elastic pool (vCore) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore
scraped: 2026-02-17T05:03:22.767179
---

# Azure SQL elastic pool (vCore) monitoring

# Azure SQL elastic pool (vCore) monitoring

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure SQL elastic pool (vCore). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure SQL (Microsoft.Sql/servers/elasticpools). While you have this service configured, you can't have Azure Sql Servers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| CPU percentage | CPU percentage | Database arm resource ID | Percent | Applicable |
| Data IO percentage | Data IO percentage | Database arm resource ID | Percent | Applicable |
| Log IO percentage | Log IO percentage | Database arm resource ID | Percent | Applicable |
| Data space used percent | Data space used percent. Not applicable to hyperscale |  | Percent |  |
| Workers percentage | Workers percentage | Database arm resource ID | Percent |  |
| Sessions percentage | Sessions percentage | Database arm resource ID | Percent | Applicable |
| Sessions count | Number of active sessions |  | Count | Applicable |
| Data max size | Data max size. Not applicable to hyperscale |  | Byte |  |
| Data space used | Data space used. Not applicable to hyperscale | Database arm resource ID | Byte |  |
| In - memory OLTP storage percent | In-Memory OLTP storage percent. Not applicable to hyperscale |  | Percent |  |
| CPU limit | CPU limit. Applies to vCore-based elastic pools. | Database arm resource ID | Count | Applicable |
| CPU used | CPU used. Applies to vCore-based elastic pools. | Database arm resource ID | Count | Applicable |
| SQL server process core percent | CPU usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\_instance\_cpu\_percent, and will be removed in the future.) |  | Percent |  |
| SQL server process memory percent | Memory usage as a percentage of the SQL DB process. Applies to elastic pools. (This metric is equivalent to sql\_instance\_memory\_percent, and will be removed in the future.) |  | Percent |  |
| Tempdb data file size kB | Space used in tempdb data files in kilobytes. |  | Count |  |
| Tempdb log file size kB | Space used in tempdb transaction log file in kilobytes. |  | Count |  |
| Tempdb percent log used | Space used percentage in tempdb transaction log file |  | Percent |  |
| Data space allocated | Data space allocated. Not applicable to hyperscale | Database arm resource ID | Byte |  |
| Data space allocated percent | Data space allocated percent. Not applicable to hyperscale |  | Percent |  |


---


## Source: monitor-azure-sql-server.md


---
title: Azure SQL Server monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server
scraped: 2026-02-18T05:44:32.805953
---

# Azure SQL Server monitoring

# Azure SQL Server monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").


---


## Source: monitor-azure-standard-load-balancer.md


---
title: Azure Standard Load Balancer monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer
scraped: 2026-02-17T21:30:02.201084
---

# Azure Standard Load Balancer monitoring

# Azure Standard Load Balancer monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

Dynatrace ingests metrics from Azure Metrics API for Azure Standard Load Balancer. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

## Available metrics

This service monitors a part of Azure Load Balancer (Microsoft.Network/loadBalancers). While you have this service configured, you can't have Azure Load Balancers (built-in) service turned on.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Data path availability | Average Load Balancer data path availability per time duration | Frontend IP address, Frontend port | Count | Applicable |
| Health probe status | Average Load Balancer health probe status per time duration | Protocol type, Backend port, Frontend IP address, Frontend port, Backend IP address | Count | Applicable |
| Byte count | Total number of Bytes transmitted within time period | Frontend IP address, Frontend port, Direction | Byte |  |
| Packet count | Total number of Packets transmitted within time period | Frontend IP address, Frontend port, Direction | Count |  |
| SYN count | Total number of SYN Packets transmitted within time period | Frontend IP address, Frontend port, Direction | Count |  |
| SNAT connection count | Total number of new SNAT connections created within time period | Frontend IP address, Backend IP address, Connection state | Count |  |
| Allocated SNAT ports | Total number of SNAT ports allocated within time period | Frontend IP address, Backend IP address, Protocol type | Count |  |
| Used SNAT ports | Total number of SNAT ports used within time period | Frontend IP address, Backend IP address, Protocol type | Count |  |
| Health probe status | Azure Cross-region Load Balancer backend health and status per time duration | Frontend IP address, Frontend port, Backend IP address, Protocol type, Frontend region, Backend region | Count |  |


---


## Source: monitor-azure-storage-account-classic.md


---
title: Azure Storage Account Classic (Blob, File, Queue, Table) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-classic
scraped: 2026-02-18T05:56:07.660323
---

# Azure Storage Account Classic (Blob, File, Queue, Table) monitoring

# Azure Storage Account Classic (Blob, File, Queue, Table) monitoring

* Latest Dynatrace
* How-to guide
* 11-min read
* Updated on Nov 15, 2023

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Storage Account Classic. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

This service monitors a part of Storage Account Classic (`Microsoft.ClassicStorage/storageAccounts`). You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset.

To monitor resources of the `Microsoft.Storage/storageAccounts` (including Storage, StorageV2 and BlobStorage) type, check Storage Accounts and the **Storage accounts** section on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Storage Account Classic](https://dt-cdn.net/images/storageaccountnew-2908-6a758a1c35.png)

## Available metrics

**Storage Account (Classic)**

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |
| UsedCapacity | Account used capacity. | Byte |  | Applicable |

**Azure Storage Blob Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources on the Azure overview page in the `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| BlobCapacity | The amount of storage used by the storage accountâs Blob service in bytes. | Byte | BlobType | Applicable |
| BlobCount | The number of Blob in the storage accountâs Blob service. | Count | BlobType | Applicable |
| ContainerCount | The number of containers in the storage accountâs Blob service. | Count |  | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| IndexCapacity | The amount of storage used by ADLS Gen2 (Hierarchical) Index in bytes. | Byte |  |  |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage File Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, FileShare, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| FileCapacity | The amount of storage used by the storage accountâs File service in bytes. | Byte | FileShare | Applicable |
| FileCount | The number of file in the storage accountâs File service. | Count | FileShare | Applicable |
| FileShareCount | The number of file shares in the storage accountâs File service. | Count |  | Applicable |
| FileShareQuota | The upper limit on the amount of storage that can be used by Azure Files Service in bytes. | Byte | FileShare | Applicable |
| FileShareSnapshotCount | The number of snapshots present on the share in storage accountâs Files Service. | Count | FileShare |  |
| FileShareSnapshotSize | The amount of storage used by the snapshots in storage accountâs File service in bytes. | Byte | FileShare |  |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, FileShare, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, FileShare, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, FileShare, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Queue Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of type Microsoft.Storage/storageAccounts (including Storage, StorageV2 and BlobStorage), check Storage Accounts and Azure overview section `Storage accounts`.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| QueueCapacity | The amount of storage used by the storage accountâs Queue service in bytes. | Byte |  | Applicable |
| QueueCount | The number of queue in the storage accountâs Queue service. | Count |  | Applicable |
| QueueMessageCount | The approximate number of queue messages in the storage accountâs Queue service. | Count |  | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |

**Azure Storage Table Services (Classic)**

This service monitors a part of Storage Account Classic (Microsoft.ClassicStorage/storageAccounts). You can find the already monitored resources in Azure overview page in `Cloud services` section or use a dashboard preset. To monitor resources of the Microsoft.Storage/storageAccounts type (including Storage, StorageV2 and BlobStorage), check Storage Accounts and the `Storage accounts` section on the Azure overview page.

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| Availability | The percentage of availability for the storage service or the specified API operation. Availability is calculated by taking the TotalBillableRequests value and dividing it by the number of applicable requests, including those that produced unexpected errors. All unexpected errors result in reduced availability for the storage service or the specified API operation. | Percent | Authentication, GeoType, ApiName | Applicable |
| Egress | The amount of egress data, in bytes. This number includes egress from an external client into Azure Storage as well as egress within Azure. As a result, this number does not reflect billable egress. | Byte | Authentication, GeoType, ApiName | Applicable |
| Ingress | The amount of ingress data, in bytes. This number includes ingress from an external client into Azure Storage as well as ingress within Azure. | Byte | Authentication, GeoType, ApiName | Applicable |
| SuccessE2ELatency | The end-to-end latency of successful requests made to a storage service or the specified API operation, in milliseconds. This value includes the required processing time within Azure Storage to read the request, send the response, and receive acknowledgment of the response. | MilliSecond | Authentication, GeoType, ApiName | Applicable |
| SuccessServerLatency | The latency used by Azure Storage to process a successful request, in milliseconds. This value does not include the network latency specified in SuccessE2ELatency. | MilliSecond | Authentication, GeoType, ApiName |  |
| TableCapacity | The amount of storage used by the storage accountâs Table service in bytes. | Byte |  | Applicable |
| TableCount | The number of table in the storage accountâs Table service. | Count |  | Applicable |
| TableEntityCount | The number of table entities in the storage accountâs Table service. | Count |  | Applicable |
| Transactions | The number of requests made to a storage service or the specified API operation. This number includes successful and failed requests, as well as requests which produced errors. Use ResponseType dimension for the number of different type of response. | Count | Authentication, GeoType, ResponseType, ApiName | Applicable |


---


## Source: monitor-azure-storage-sync.md


---
title: Azure Storage Sync monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-sync
scraped: 2026-02-17T05:06:45.478103
---

# Azure Storage Sync monitoring

# Azure Storage Sync monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Storage Sync. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Stor sync](https://dt-cdn.net/images/2021-03-12-11-36-41-1570-b719e71510.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| ServerSyncSessionResult | Logs a value of `1` each time the server endpoint successfully completes a sync session with the cloud endpoint | Sync group name, Server endpoint name, Sync direction | Count | Applicable |
| StorageSyncSyncSessionAppliedFilesCount | The number of files synced | Sync group name, Server endpoint name, Sync direction | Count | Applicable |
| StorageSyncSyncSessionPerItemErrorsCount | The number of files that failed to sync | Sync group name, Server endpoint name, Sync direction | Count | Applicable |
| StorageSyncBatchTransferredFileBytes | The total file size transferred for sync sessions | Sync group name, Server endpoint name, Sync direction | Byte | Applicable |
| StorageSyncServerHeartbeat | Logs a value of `1` each time the registered server successfully records a heartbeat with the cloud endpoint | Server name | Count | Applicable |
| StorageSyncRecallIOTotalSizeBytes | The total size of data recalled by the server | Server name | Byte |  |
| StorageSyncRecalledTotalNetworkBytes | The size of data recalled | Sync group name, Server name | Byte |  |
| StorageSyncRecallThroughputBytesPerSecond | The size of data recall throughput | Sync group name, Server name | BytePerSecond |  |
| StorageSyncRecalledNetworkBytesByApplication | The size of data recalled by application | Sync group name, Server name, Application name | Byte |  |


---


## Source: monitor-azure-stream-analytics.md


---
title: Azure Stream Analytics monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics
scraped: 2026-02-18T05:46:34.884170
---

# Azure Stream Analytics monitoring

# Azure Stream Analytics monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Stream Analytics. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Stream](https://dt-cdn.net/images/2021-03-12-11-39-16-1056-7bb7a37cb2.png)

## Available metrics

| Name | Dimensions | Description | Unit | Recommended |
| --- | --- | --- | --- | --- |
| AMLCalloutFailedRequests | Failed function requests | Logical name, Partition ID | Count | Applicable |
| AMLCalloutInputEvents | Function events | Logical name, Partition ID | Count |  |
| AMLCalloutRequests | Function requests | Logical name, Partition ID | Count | Applicable |
| ConversionErrors | Data conversion errors | Logical name, Partition ID | Count | Applicable |
| DeserializationError | Input deserialization errors | Logical name, Partition ID | Count | Applicable |
| DroppedOrAdjustedEvents | Out-of-order events | Logical name, Partition ID | Count | Applicable |
| EarlyInputEvents | Early input events | Logical name, Partition ID | Count | Applicable |
| Errors | Runtime errors | Logical name, Partition ID | Count | Applicable |
| InputEventBytes | Input event bytes | Logical name, Partition ID | Byte |  |
| InputEvents | Input events | Logical name, Partition ID | Count | Applicable |
| InputEventsSourcesBacklogged | Backlogged input events | Logical name, Partition ID | Count | Applicable |
| InputEventsSourcesPerSecond | Input sources received | Logical name, Partition ID | PerSecond | Applicable |
| LateInputEvents | Late input events | Logical name, Partition ID | Count | Applicable |
| OutputEvents | Output events | Logical name, Partition ID | Count | Applicable |
| OutputWatermarkDelaySeconds | Watermark delay | Logical name, Partition ID | Second | Applicable |
| ResourceUtilization | Percentage of resource utilization | Logical name, Partition ID | Percent | Applicable |


---


## Source: monitor-azure-synapse-analytics.md


---
title: Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-synapse-analytics
scraped: 2026-02-18T05:55:46.663282
---

# Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool) monitoring

# Azure Synapse Analytics (Synapse Workspace, Apache Spark pool, SQL pool) monitoring

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Analytics (Synapse Workspace, Apache Spark pool, SQL pool). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Synapse workspace](https://dt-cdn.net/images/dashboard-86-1365-48045e63d7.png)

## Available metrics

**Synapse Workspace**

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| IntegrationActivityRunsEnded | The number of orchestration activities that succeeded, failed, or were cancelled | Result, Failure type, Activity, Activity type, Pipeline | Count | Applicable |
| IntegrationPipelineRunsEnded | The number of orchestration pipeline runs that succeeded, failed, or were cancelled | Result, Failure type, Pipeline | Count | Applicable |
| IntegrationTriggerRunsEnded | The number of orchestration triggers that succeeded, failed, or were cancelled | Result, Failure type, Trigger | Count | Applicable |
| BuiltinSqlPoolLoginAttempts | The number of login attempts that succeeded or failed | Result, Failure type | Count |  |
| BuiltinSqlPoolRequestsEnded | The number of queries that succeeded, failed, or were cancelled | Result, Failure type | Count | Applicable |
| BuiltinSqlPoolDataProcessedBytes | The amount of data processed by queries |  | Byte | Applicable |

**Apache Spark pool**

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| BigDataPoolApplicationsActive | Active Apache Spark applications | Job state | Count | Applicable |
| BigDataPoolApplicationsEnded | Ended Apache Spark applications | Job result, Job type | Count | Applicable |
| BigDataPoolAllocatedMemory | Memory allocated (in GB) | Submitter ID | Count | Applicable |
| BigDataPoolAllocatedCores | V cores allocated | Submitter ID | Count | Applicable |

**SQL pool**

| Name | Description | Unit | Dimensions | Recommended |
| --- | --- | --- | --- | --- |
| AdaptiveCacheHitPercent | Measures how well workloads are utilizing the adaptive cache. Use this metric with the cache hit percentage metric to determine whether to scale for additional capacity or rerun workloads to hydrate the cache. | Percent |  | Applicable |
| AdaptiveCacheUsedPercent | Measures how well workloads are utilizing the adaptive cache. Use this metric with the cache used percentage metric to determine whether to scale for additional capacity or rerun workloads to hydrate the cache. | Percent |  | Applicable |
| Connections | The number of total logins to the SQL pool | Count | Result | Applicable |
| ConnectionsBlockedByFirewall | The number of connections blocked by firewall rules | Count |  |  |
| DWULimit | The service-level objective of the SQL pool | Count |  | Applicable |
| DWUUsed | The usage across the SQL pool, measured by DWU limit \* DWU percentage. | Count |  | Applicable |
| DWUUsedPercent | The usage across the SQL pool, measured by taking the maximum between CPU percentage and Data IO percentage | Percent |  | Applicable |
| LocalTempDBUsedPercent | The local tempdb utilization across all compute nodes. Values are emitted every five minutes. | Percent |  | Applicable |
| MemoryUsedPercent | The memory utilization across all nodes in the SQL pool | Percent |  | Applicable |
| WLGActiveQueries | The active queries within the workload group | Count | Is user defined, Workload group | Applicable |
| WLGActiveQueriesTimeouts | The queries for the workload group that have timed out | Count | Is user defined, Workload group | Applicable |
| WLGAllocationByMaxResourcePercent | The percentage allocation of resources relative to the effective cap resource percent per workload group | Percent | Is user defined, Workload group |  |
| WLGAllocationBySystemPercent | The percentage allocation of resources relative to the entire system | Percent | Is user defined, Workload group |  |
| WLGEffectiveCapResourcePercent | The effective cap resource percent for the workload group | Percent | Is user defined, Workload group |  |
| WLGQueuedQueries | The cumulative number of requests queued after the max concurrency limit was reached | Count | Is user defined, Workload group |  |
| wlg\_effective\_min\_resource\_percent | The effective minimum resource percentage setting allowed, considering the service level and the workload group settings | Percent | Is user defined, Workload group |  |


---


## Source: monitor-azure-time-series-insights.md


---
title: Azure Time Series Insights (Environment, Event Source) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-time-series-insights
scraped: 2026-02-16T21:30:36.748292
---

# Azure Time Series Insights (Environment, Event Source) monitoring

# Azure Time Series Insights (Environment, Event Source) monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 23, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Time Series Insights (Environment, Event Source). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Timeseries](https://dt-cdn.net/images/2021-03-12-11-41-03-1622-e3c1ff7533.png)

![Time series event sources](https://dt-cdn.net/images/azure-time-series-insights-event-sources-dashboard-1920-7ec38ddb3d.png)

## Available metrics

| Name | Description | Unit | Recommended (Environment) | Recommended (Event Source) |
| --- | --- | --- | --- | --- |
| IngressReceivedMessages | The number of messages read from all Event Hub or IoT Hub event sources | Count | Applicable | Applicable |
| IngressReceivedInvalidMessages | The number of invalid messages read from the event source | Count | Applicable | Applicable |
| IngressStoredBytes | The total size of events successfully processed and available for query | Byte | Applicable | Applicable |
| IngressReceivedBytes | The number of bytes read from all event sources | Byte | Applicable | Applicable |
| IngressStoredEvents | The number of flattened events successfully processed and available for query | Count | Applicable | Applicable |
| IngressReceivedMessagesTimeLag | The difference between the time that the message is enqueued in the event source and the time it is processed in ingress | Second | Applicable | Applicable |
| IngressReceivedMessagesCountLag | The difference between the sequence number of the last enqueued message in the event source partition and the sequence number of messages being processed in ingress | Count | Applicable | Applicable |
| WarmStorageMaxProperties | The maximum number of properties used allowed by the environment for S1/S2 SKU and the maximum number of properties allowed by warm store for PAYG SKU | Count | Applicable |  |
| WarmStorageUsedProperties | The number of properties used by the environment for S1/S2 SKU and number of properties used by warm store for PAYG SKU | Count | Applicable |  |


---


## Source: monitor-azure-traffic-manager.md


---
title: Azure Traffic Manager monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-traffic-manager
scraped: 2026-02-18T05:55:51.810457
---

# Azure Traffic Manager monitoring

# Azure Traffic Manager monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Traffic Manager. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Traffic manager 3](https://dt-cdn.net/images/traffic-manager-3-1674-a6b32b5038.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| QpsByEndpoint | Number of times a Traffic Manager endpoint was returned in the given time frame. | EndpointName | Count | Applicable |
| ProbeAgentCurrentEndpointStateByProfileResourceId | `1` if endpoint probe status is `Enabled`, otherwise `0`. | EndpointName | Count | Applicable |


---


## Source: monitor-azure-virtual-network-gateways.md


---
title: Azure Virtual Network Gateway monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-virtual-network-gateways
scraped: 2026-02-18T05:51:32.830274
---

# Azure Virtual Network Gateway monitoring

# Azure Virtual Network Gateway monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jun 25, 2020

On the Azure Virtual Network Gateway overview page you can monitor connected workloads and performance to ensure that Azure Virtual Network Gateway is successfully connected.

Only the VPN gateway type can be monitored by Dynatrace. The ExpressRoute gateway type is not monitored.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Vng dash](https://dt-cdn.net/images/virtualnetworkgateway-1257-ccba37a0d0.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| AverageBandwidth | Average site-to-site bandwidth of a gateway in bytes per second |  | BytesPerSecond |  |
| P2SBandwidth | Average point-to-site bandwidth of a gateway in bytes per second |  | BytesPerSecond |  |
| P2SConnectionCount | Point-to-site connection count of a gateway | Protocol | Count |  |
| TunnelAverageBandwidth | Average bandwidth of a tunnel in bytes per second | ConnectionName,RemoteIP | BytesPerSecond | Applicable |
| TunnelEgressBytes | Outgoing bytes of a tunnel | ConnectionName,RemoteIP | Bytes | Applicable |
| TunnelEgressPacketDropTSMismatch | Outgoing packet drop count from traffic selector mismatch of a tunnel | ConnectionName,RemoteIP | Count | Applicable |
| TunnelEgressPackets | Outgoing packet count of a tunnel | ConnectionName,RemoteIP | Count |  |
| TunnelIngressBytes | Incoming bytes of a tunnel | ConnectionName,RemoteIP | Bytes | Applicable |
| TunnelIngressPacketDropTSMismatch | Incoming packet drop count from traffic selector mismatch of a tunnel | ConnectionName,RemoteIP | Count | Applicable |
| TunnelIngressPackets | Incoming packet count of a tunnel | ConnectionName,RemoteIP | Count |  |


---


## Source: monitor-azure-web-application-firewall-policies.md


---
title: Azure Web Application Firewall (WAF) Policy on Azure CDN monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-web-application-firewall-policies
scraped: 2026-02-18T05:56:55.116532
---

# Azure Web Application Firewall (WAF) Policy on Azure CDN monitoring

# Azure Web Application Firewall (WAF) Policy on Azure CDN monitoring

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 18, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Web Application Firewall (WAF) Policy on Azure CDN. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.203+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Webapp](https://dt-cdn.net/images/2021-03-12-11-42-49-1338-4713f92c56.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| WebApplicationFirewallRequestCount | The number of client requests processed by Web Application Firewall | PolicyName, RuleName, Action | Count | Applicable |


---


## Source: azure-cloud-services-metrics.md


---
title: All Azure cloud services
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics
scraped: 2026-02-18T05:39:54.074204
---

# All Azure cloud services

# All Azure cloud services

* Latest Dynatrace
* Overview
* 19-min read
* Updated on Feb 12, 2024

Dynatrace can receive Azure Monitor metrics for multiple preselected services.

* You can view graphs per service instance, with a set of dimensions, and create custom graphs that you can pin to your dashboards.
* You can reduce your Azure Monitor costs and throttling by selecting which additional services to monitor.
* For non-classic (formerly "non-built-in") services, you can choose which metrics to monitor.

## Azure cloud services monitored by default

As a result of [Azure monitoring integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), some services are monitored out-of-the-box.

[Azure API Management Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service) [Azure Application Gateways classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin) [Azure Application Service classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-builtin) [Azure Cosmos Database classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin) [Azure Events Hub classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hub-builtin) [Azure Iot Hub classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin) [Azure Load Balancers classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin) [Azure Redis Cache classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin) [Azure Service Bus classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-bus-builtin) [Azure SQL Servers classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin) [Azure Virtual Machines classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin) [Azure Storage Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account) 

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

## Other Azure cloud services

Apart from cloud services monitored by default, you can also monitor other Azure services that affect the performance of your Azure-hosted applications.

[Azure AI - All In One](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-all-in-one) [Azure AI - Anomaly Detector](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-anomaly-detector) [Azure AI - Bing Autosuggest](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-autosuggest) [Azure AI - Bing Custom Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-custom-search) [Azure AI - Bing Entity Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-entity-search) [Azure AI - Bing Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-search) [Azure AI - Bing Spell Check](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-spell-check) [Azure AI - Computer Vision](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-computer-vision) [Azure AI - Content Moderator](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-content-moderator) [Azure AI - Custom Vision Prediction](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-prediction) [Azure AI - Custom Vision Training](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-training) [Azure AI - Face](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-face) [Azure AI - Immersive Reader](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-immersive-reader) [Azure AI - Ink Recognizer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cognitive-services-ink-recognizer) [Azure AI - Language Understanding (LUIS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding) [Azure AI - Language Understanding (LUIS) Authoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding-authoring) [Azure AI - OpenAI](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-openai) [Azure AI - Personalizer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-personalizer) [Azure AI - QnA Maker](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-qna-maker) [Azure AI - Speech](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-speech) [Azure AI - Text Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-text-analytics) [Azure AI - Translator](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-translator) [Azure API Management Services classic (deprecated)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin) [Azure App Configuration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-configuration) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service) [![Azure App Env v2](https://dt-cdn.net/images/azure-app-service-environment-v2-5888da78cc.svg "Azure App Env v2")Azure App Service Environment](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-environment) [Azure Application Gateway](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway) [Azure Application Insights](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-insights) [Azure Automation Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-automation-account) [Azure Basic Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer) [Azure Batch](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-batch) [Azure Blockchain](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-blockchain-service) [Azure Cache for Redis](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis) [Azure Container App](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-app) [Azure Container Apps Environment](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-apps-environment) [Azure Container Instances](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-instances) [Azure Container Registry](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-registry) [Azure Cosmos DB Account (GlobalDocumentDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb) [Azure Cosmos DB Account (MongoDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb) [Azure Data Explorer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-explorer-cluster) [Azure Data Factory](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-factory) [Azure Data Lake Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-analytics) [Azure Data Lake Storage](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-storage-gen1) [Azure Data Share](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-share) [Azure Database for MariaDB](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mariadb) [Azure Database for MySQL Flexible Servers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers) [Azure Database for MySQL](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql) [Azure Database for PostgreSQL](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-postgresql) [Azure Device Provisioning Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-device-provisioning-service) [Azure DNS Zone](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-dns-zone) [Azure Event Grid](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid) [Azure Event Hubs](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hubs) [Azure ExpressRoute Circuit](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-expressroute-circuit) [Azure Firewall](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-firewall) [Azure Front Door (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door) [Azure Front Door Standard/Premium and CDN profiles](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles) [Azure Gateway Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer) [Azure HDInsight](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight) [Azure Integration Service Environment](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-integration-service-environment) [Azure IoT Central Applications](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-central-applications) [Azure IoT Hub](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub) [Azure Key Vault](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-key-vault) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service) [Azure Logic Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-logic-apps) [Azure Machine - Azure Arc](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-arc) [Azure Machine Learning](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-machine-learning) [Azure Maps Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-maps-account) [Azure Media Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-media-service) [Azure Mesh Application](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-mesh-application) [Azure NetApp Files](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-netapp-files) [Azure Network Interface](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-interface) [Azure Network Watcher](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher) [Azure Notification Hub](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-notification-hub) [Azure Power BI](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-power-bi) [Azure Private DNS Zone](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-private-dns-zone) [Azure Public IP Address](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-public-ip-addresses) [Azure Recovery Services Vault](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-recovery-services-vault) [Azure Relay](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-relay) [Azure Search Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-search) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-fabric) [Azure SignalR](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-signalr) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps) [Azure SQL Database (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu) [Azure SQL Database Hyperscale](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-hyperscale) [Azure SQL Database (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore) [Azure SQL Data Warehouse](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-data-warehouse) [Azure SQL Elastic Pool (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu) [Azure SQL Elastic Pool (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore) [Azure SQL Managed Instance](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-managed-instance) [Azure SQL Server](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server) [Azure Standard Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer) [Azure Storage Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account) [Azure Storage Accounts classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin) [Azure Storage Account Classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-classic) [Azure Storage Sync](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-sync) [Azure Stream Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics)  [Azure Synapse Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-synapse-analytics) [Azure Time Series Insights](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-time-series-insights) [Azure Traffic Manager](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-traffic-manager) [Azure Virtual Machines Classic](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic) [Azure Virtual Network Gateway](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-virtual-network-gateways) [Azure Web Application Firewall (WAF) Policy on Azure CDN](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-web-application-firewall-policies) 

## Cloud services with their respective Dynatrace entity types

Not all cloud services have Dynatrace entities created for them and can have tags imported from the cloud. Expand the table below to see cloud services with their respective Dynatrace entity types and to check if they have tags imported from the cloud provider.

### List of Azure services with entities and tags

| Service | Cloud type | Tag monitoring and filtering | Dynatrace entity type |
| --- | --- | --- | --- |
| Azure API Management services (built-in) (deprecated) | Microsoft.ApiManagement/service | Applicable | AZURE\_API\_MANAGEMENT\_SERVICE |
| Azure API Management Service | Microsoft.ApiManagement/service | Applicable | cloud:azure:apimanagement:service, CUSTOM\_DEVICE |
| Azure Container App | Microsoft.App/containerApps | Applicable | cloud:azure:app:containerapps, CUSTOM\_DEVICE |
| Azure Container Apps Environment | Microsoft.App/managedEnvironments | Applicable | cloud:azure:app:managedenvironments, CUSTOM\_DEVICE |
| Azure App Configuration | Microsoft.AppConfiguration/configurationStores | Applicable | cloud:azure:appconfiguration:configurationstores, CUSTOM\_DEVICE |
| Azure Spring Apps | Microsoft.AppPlatform/Spring | Applicable | cloud:azure:appplatform:spring, CUSTOM\_DEVICE |
| Azure Automation Account | Microsoft.Automation/automationAccounts | Applicable | cloud:azure:automation:automationaccounts, CUSTOM\_DEVICE |
| Azure Batch Account | Microsoft.Batch/batchAccounts | Applicable | cloud:azure:batch:account, CUSTOM\_DEVICE |
| Azure Blockchain Service | Microsoft.Blockchain/blockchainMembers | Applicable | cloud:azure:blockchain:blockchainmembers, CUSTOM\_DEVICE |
| Azure Cache for Redis | Microsoft.Cache/redis | Applicable | cloud:azure:cache:redis, CUSTOM\_DEVICE |
| Azure Redis (built-in) | Microsoft.Cache/redis | Applicable | AZURE\_REDIS\_CACHE |
| Azure CDN WAF Policy | Microsoft.Cdn/cdnwebapplicationfirewallpolicies | Applicable | cloud:azure:cdn:cdnwebapplicationfirewallpolicies, CUSTOM\_DEVICE |
| Azure Virtual Machine (classic) | Microsoft.ClassicCompute/virtualMachines | Applicable | cloud:azure:classic\_virtual\_machine, CUSTOM\_DEVICE |
| Azure Storage Account (classic) | Microsoft.ClassicStorage/storageAccounts | Applicable | cloud:azure:classic\_storage\_account, CUSTOM\_DEVICE |
| Azure Storage Blob Services (classic) | Microsoft.ClassicStorage/storageAccounts | Applicable | cloud:azure:classic\_storage\_account:blob, CUSTOM\_DEVICE |
| Azure Storage File Services (classic) | Microsoft.ClassicStorage/storageAccounts | Applicable | cloud:azure:classic\_storage\_account:file, CUSTOM\_DEVICE |
| Azure Storage Queue Services (classic) | Microsoft.ClassicStorage/storageAccounts | Applicable | cloud:azure:classic\_storage\_account:queue, CUSTOM\_DEVICE |
| Azure Storage Table Services (classic) | Microsoft.ClassicStorage/storageAccounts | Applicable | cloud:azure:classic\_storage\_account:table, CUSTOM\_DEVICE |
| Azure Anomaly Detector | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:anomalydetector, CUSTOM\_DEVICE |
| Azure Bing Autosuggest | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:bingautosuggest, CUSTOM\_DEVICE |
| Azure Bing Custom Search | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:bingcustomsearch, CUSTOM\_DEVICE |
| Azure Bing Entity Search | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:bingentitysearch, CUSTOM\_DEVICE |
| Azure Bing Search | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:bingsearch, CUSTOM\_DEVICE |
| Azure Bing Spell Check | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:bingspellcheck, CUSTOM\_DEVICE |
| Azure AI All in One | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:allinone, CUSTOM\_DEVICE |
| Azure Computer Vision | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:computervision, CUSTOM\_DEVICE |
| Azure AI Content Moderator | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:contentmoderator, CUSTOM\_DEVICE |
| Azure Custom Vision Prediction | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:customvisionprediction, CUSTOM\_DEVICE |
| Azure Custom Vision Training | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:customvisiontraining, CUSTOM\_DEVICE |
| Azure Face | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:face, CUSTOM\_DEVICE |
| Azure Immersive Reader | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:immersivereader, CUSTOM\_DEVICE |
| Azure Ink Recognizer | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:inkrecognizer, CUSTOM\_DEVICE |
| Azure Language Understanding (LUIS) | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:luis, CUSTOM\_DEVICE |
| Azure Language Understanding Authoring (LUIS) | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:luisauthoring, CUSTOM\_DEVICE |
| Azure Machine Azure Arc | Microsoft.Hybridcompute/machines | Applicable | cloud:azure:hybridcompute:machines, CUSTOM\_DEVICE |
| Azure OpenAI | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:openai, CUSTOM\_DEVICE |
| Azure Personalizer | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:personalizer, CUSTOM\_DEVICE |
| Azure QnA Maker | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:qnamaker, CUSTOM\_DEVICE |
| Azure Recovery Services Vault | Microsoft.RecoveryServices/Vaults | Applicable | cloud:azure:recoveryservices:vaults, CUSTOM\_DEVICE |
| Azure Speech | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:speech, CUSTOM\_DEVICE |
| Azure Text Analytics | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:textanalytics, CUSTOM\_DEVICE |
| Azure Translator | Microsoft.CognitiveServices/accounts | Applicable | cloud:azure:cognitiveservices:translator, CUSTOM\_DEVICE |
| Azure Virtual machines (built-in) | Microsoft.Compute/virtualMachines | Applicable | AZURE\_VM |
| Azure Virtual machines (built-in) | Microsoft.Compute/virtualMachineScaleSets | Applicable | AZURE\_VM\_SCALE\_SET |
| Azure Container Instance | Microsoft.ContainerInstance/containerGroups | Applicable | cloud:azure:containerinstance:containergroup, CUSTOM\_DEVICE |
| Azure Container Registry | Microsoft.ContainerRegistry/registries | Applicable | cloud:azure:containerregistry:registries, CUSTOM\_DEVICE |
| Azure Kubernetes Service (AKS) | Microsoft.ContainerService/managedClusters | Applicable | cloud:azure:containerservice:managedcluster, CUSTOM\_DEVICE |
| Azure Data Factory v1 | Microsoft.DataFactory/dataFactories | Applicable | cloud:azure:datafactory:v1, CUSTOM\_DEVICE |
| Azure Data Factory v2 | Microsoft.DataFactory/factories | Applicable | cloud:azure:datafactory:v2, CUSTOM\_DEVICE |
| Azure Data Lake Analytics | Microsoft.DataLakeAnalytics/accounts | Applicable | cloud:azure:datalakeanalytics:accounts, CUSTOM\_DEVICE |
| Azure Data Lake Storage Gen1 | Microsoft.DataLakeStore/accounts | Applicable | cloud:azure:datalakestore:accounts, CUSTOM\_DEVICE |
| Azure Data Share | Microsoft.DataShare/accounts | Applicable | cloud:azure:datashare:accounts, CUSTOM\_DEVICE |
| Azure DB for MariaDB | Microsoft.DBforMariaDB/servers | Applicable | cloud:azure:mariadb:server, CUSTOM\_DEVICE |
| Azure DB for MySQL Flexible Servers | Microsoft.DBforMySQL/flexibleServers | Applicable | cloud:azure:mysql:flexibleservers, CUSTOM\_DEVICE |
| Azure DB for MySQL | Microsoft.DBforMySQL/servers | Applicable | cloud:azure:mysql:server, CUSTOM\_DEVICE |
| Azure DB for PostgreSQL Flexible Server | Microsoft.DBforPostgreSQL/flexibleServers | Applicable | cloud:azure:postgresql:flexibleservers, CUSTOM\_DEVICE |
| Azure DB for PostgreSQL Server | Microsoft.DBforPostgreSQL/servers | Applicable | cloud:azure:postgresql:server, CUSTOM\_DEVICE |
| Azure DB for PostgreSQL Hyperscale | Microsoft.DBforPostgreSQL/serversv2 | Applicable | cloud:azure:postgresql:serverv2, CUSTOM\_DEVICE |
| Azure IoT Hubs (built-in) | Microsoft.Devices/IotHubs | Applicable | AZURE\_IOT\_HUB |
| Azure IoT Hub | Microsoft.Devices/IotHubs | Applicable | cloud:azure:devices:iothubs, CUSTOM\_DEVICE |
| Azure Device Provisioning Service | Microsoft.Devices/provisioningServices | Applicable | cloud:azure:devices:provisioningservices, CUSTOM\_DEVICE |
| Azure Cosmos DB Account (GlobalDocumentDB) | Microsoft.DocumentDB/databaseAccounts | Applicable | cloud:azure:documentdb:databaseaccounts:global, CUSTOM\_DEVICE |
| Azure Cosmos DB Account (MongoDB) | Microsoft.DocumentDB/databaseAccounts | Applicable | cloud:azure:documentdb:databaseaccounts:mongo, CUSTOM\_DEVICE |
| Azure Cosmos DB (built-in) | Microsoft.DocumentDB/databaseAccounts | Applicable | AZURE\_COSMOS\_DB |
| Azure Event Grid Domain | Microsoft.EventGrid/domains | Applicable | cloud:azure:eventgrid:domains, CUSTOM\_DEVICE |
| Azure Event Grid System Topic | Microsoft.EventGrid/systemTopics | Applicable | cloud:azure:eventgrid:systemtopics, CUSTOM\_DEVICE |
| Azure Event Grid Topic | Microsoft.EventGrid/topics | Applicable | cloud:azure:eventgrid:topics, CUSTOM\_DEVICE |
| Azure Event Hubs Cluster | Microsoft.EventHub/clusters | Applicable | cloud:azure:eventhub:clusters, CUSTOM\_DEVICE |
| Azure Event Hubs (built-in) | Microsoft.EventHub/namespaces | Applicable | AZURE\_EVENT\_HUB\_NAMESPACE |
| Azure Event Hubs (built-in) | Microsoft.EventHub/namespaces/eventhubs | Not applicable | AZURE\_EVENT\_HUB |
| Azure HDInsight Cluster | Microsoft.HDInsight/clusters | Applicable | cloud:azure:hdinsight:cluster, CUSTOM\_DEVICE |
| Azure Machine Azure Arc | Microsoft.hybridcompute/machines | Applicable | cloud:azure:hybridcompute:machines, CUSTOM\_DEVICE |
| Azure Application Insights | Microsoft.Insights/components | Applicable | cloud:azure:insights:components, CUSTOM\_DEVICE |
| Azure IoT Central Application | Microsoft.IoTCentral/IoTApps | Applicable | cloud:azure:iotcentral:iotapps, CUSTOM\_DEVICE |
| Azure Key Vault | Microsoft.KeyVault/vaults | Applicable | cloud:azure:keyvault:vaults, CUSTOM\_DEVICE |
| Azure Data Explorer Cluster | Microsoft.Kusto/Clusters | Applicable | cloud:azure:kusto:clusters, CUSTOM\_DEVICE |
| Azure Integration Service Environment | Microsoft.Logic/integrationServiceEnvironments | Applicable | cloud:azure:logic:integrationserviceenvironments, CUSTOM\_DEVICE |
| Azure Logic Apps | Microsoft.Logic/workflows | Applicable | cloud:azure:logic:workflows, CUSTOM\_DEVICE |
| Azure Machine Learning Workspace | Microsoft.MachineLearningServices/workspaces | Applicable | cloud:azure:machinelearningservices:workspaces, CUSTOM\_DEVICE |
| Azure Maps Account | Microsoft.Maps/accounts | Applicable | cloud:azure:maps:accounts, CUSTOM\_DEVICE |
| Azure Media Service | Microsoft.Media/mediaservices | Applicable | cloud:azure:media:mediaservices, CUSTOM\_DEVICE |
| Azure Streaming Endpoint | Microsoft.Media/mediaservices/streamingEndpoints | Applicable | cloud:azure:media:mediaservices:streamingendpoints, CUSTOM\_DEVICE |
| Azure NetApp Capacity Pool | Microsoft.NetApp/netAppAccounts/capacityPools | Applicable | cloud:azure:netapp:netappaccounts:capacitypools, CUSTOM\_DEVICE |
| Azure NetApp Volume | Microsoft.NetApp/netAppAccounts/capacityPools/volumes | Applicable | cloud:azure:netapp:netappaccounts:capacitypools:volumes, CUSTOM\_DEVICE |
| Azure Application Gateway | Microsoft.Network/applicationGateways | Applicable | cloud:azure:network:applicationgateways, CUSTOM\_DEVICE |
| Azure Application Gateway (built-in) | Microsoft.Network/applicationGateways | Applicable | AZURE\_APPLICATION\_GATEWAY |
| Azure Firewall | Microsoft.Network/azurefirewalls | Applicable | cloud:azure:network:azurefirewalls, CUSTOM\_DEVICE |
| Azure DNS Zone | Microsoft.Network/dnszones | Applicable | cloud:azure:network:dnszones, CUSTOM\_DEVICE |
| Azure ExpressRoute Circuit | Microsoft.Network/expressRouteCircuits | Applicable | cloud:azure:network:expressroutecircuits, CUSTOM\_DEVICE |
| Azure Front Door | Microsoft.Network/frontdoors | Applicable | cloud:azure:frontdoor, CUSTOM\_DEVICE |
| Azure Front Door and CDN profiles | Microsoft.Cdn/Profiles | Applicable | cloud:azure:cdn:profiles, CUSTOM\_DEVICE |
| Azure Basic Load Balancer | Microsoft.Network/loadBalancers | Applicable | cloud:azure:network:loadbalancers:basic, CUSTOM\_DEVICE |
| Azure Gateway Load Balancer | Microsoft.Network/loadBalancers | Applicable | cloud:azure:network:loadbalancers:gateway, CUSTOM\_DEVICE |
| Azure Standard Load Balancer | Microsoft.Network/loadBalancers | Applicable | cloud:azure:network:loadbalancers:standard, CUSTOM\_DEVICE |
| Azure Load Balancer (built-in) | Microsoft.Network/loadBalancers | Applicable | AZURE\_LOAD\_BALANCER |
| Azure Network Interface | Microsoft.Network/networkInterfaces | Applicable | cloud:azure:network:networkinterfaces, CUSTOM\_DEVICE |
| Azure Connection Monitors | Microsoft.Network/networkWatchers/connectionMonitors | Applicable | cloud:azure:network:networkwatchers:connectionmonitors, CUSTOM\_DEVICE |
| Azure Connection Monitors Preview | Microsoft.Network/networkWatchers/connectionMonitors | Applicable | cloud:azure:network:networkwatchers:connectionmonitors:preview, CUSTOM\_DEVICE |
| Azure Private DNS Zone | Microsoft.Network/privateDnsZones | Applicable | cloud:azure:network:privatednszones, CUSTOM\_DEVICE |
| Azure Public IP Address | Microsoft.Network/publicIPAddresses | Applicable | cloud:azure:network:publicipaddresses, CUSTOM\_DEVICE |
| Azure Traffic Manager Profile | Microsoft.Network/trafficManagerProfiles | Applicable | cloud:azure:traffic\_manager\_profile, CUSTOM\_DEVICE |
| Azure Virtual Network Gateway | Microsoft.Network/virtualNetworkGateways | Applicable | cloud:azure:virtual\_network\_gateway, CUSTOM\_DEVICE |
| Azure Notification Hub | Microsoft.NotificationHubs/namespaces/notificationHubs | Applicable | cloud:azure:notificationhubs:namespaces:notificationhubs, CUSTOM\_DEVICE |
| Azure Power BI Embedded | Microsoft.PowerBIDedicated/capacities | Applicable | cloud:azure:powerbidedicated:capacities, CUSTOM\_DEVICE |
| Azure Recovery Services Vault | Microsoft.RecoveryServices/Vaults | Applicable | cloud:azure:recoveryservices:vaults, CUSTOM\_DEVICE |
| Azure Relay | Microsoft.Relay/namespaces | Applicable | cloud:azure:relay:namespaces, CUSTOM\_DEVICE |
| Azure Search Service | Microsoft.Search/searchServices | Applicable | cloud:azure:search:searchservices, CUSTOM\_DEVICE |
| Azure Service Bus (built-in) | Microsoft.ServiceBus/namespaces | Applicable | AZURE\_SERVICE\_BUS\_NAMESPACE |
| Azure Service Bus (built-in) | Microsoft.ServiceBus/namespaces/topics | Not applicable | AZURE\_SERVICE\_BUS\_TOPIC |
| Azure Service Bus (built-in) | Microsoft.ServiceBus/namespaces/queues | Not applicable | AZURE\_SERVICE\_BUS\_QUEUE |
| Azure Mesh Application | Microsoft.ServiceFabricMesh/applications | Applicable | cloud:azure:servicefabricmesh:applications, CUSTOM\_DEVICE |
| Azure SignalR | Microsoft.SignalRService/SignalR | Applicable | cloud:azure:signalrservice:signalr, CUSTOM\_DEVICE |
| Azure SQL (built-in) | Microsoft.Sql/servers | Applicable | AZURE\_SQL\_SERVER |
| Azure SQL (built-in) | Microsoft.Sql/servers/databases | Applicable | AZURE\_SQL\_DATABASE |
| Azure SQL (built-in) | Microsoft.Sql/servers/elasticPools | Applicable | AZURE\_SQL\_ELASTIC\_POOL |
| Azure SQL Managed Instance | Microsoft.Sql/managedInstances | Applicable | cloud:azure:sql:managed, CUSTOM\_DEVICE |
| Azure SQL Server | Microsoft.Sql/servers | Applicable | cloud:azure:sql:servers, CUSTOM\_DEVICE |
| Azure SQL Data Warehouse (legacy) | Microsoft.Sql/servers/databases | Applicable | cloud:azure:sql:servers:databases:datawarehouse, CUSTOM\_DEVICE |
| Azure SQL Database (DTU) | Microsoft.Sql/servers/databases | Applicable | cloud:azure:sql:servers:databases:dtu, CUSTOM\_DEVICE |
| Azure SQL Database Hyperscale | Microsoft.Sql/servers/databases | Applicable | cloud:azure:sql:servers:databases:hyperscale, CUSTOM\_DEVICE |
| Azure SQL Database (vCore) | Microsoft.Sql/servers/databases | Applicable | cloud:azure:sql:servers:databases:vcore, CUSTOM\_DEVICE |
| Azure SQL elastic pool (DTU) | Microsoft.Sql/servers/elasticpools | Applicable | cloud:azure:sql:servers:elasticpools:dtu, CUSTOM\_DEVICE |
| Azure SQL elastic pool (vCore) | Microsoft.Sql/servers/elasticpools | Applicable | cloud:azure:sql:servers:elasticpools:vcore, CUSTOM\_DEVICE |
| Azure Storage Sync Service | Microsoft.StorageSync/storageSyncServices | Applicable | cloud:azure:storagesync:storagesyncservices, CUSTOM\_DEVICE |
| Azure Storage Account | Microsoft.Storage/storageAccounts | Applicable | cloud:azure:storage:storageaccounts, CUSTOM\_DEVICE |
| Azure Storage Blob Services | Microsoft.Storage/storageAccounts | Applicable | cloud:azure:storage:storageaccounts:blob, CUSTOM\_DEVICE |
| Azure Storage File Services | Microsoft.Storage/storageAccounts | Applicable | cloud:azure:storage:storageaccounts:file, CUSTOM\_DEVICE |
| Azure Storage Queue Services | Microsoft.Storage/storageAccounts | Applicable | cloud:azure:storage:storageaccounts:queue, CUSTOM\_DEVICE |
| Azure Storage Table Services | Microsoft.Storage/storageAccounts | Applicable | cloud:azure:storage:storageaccounts:table, CUSTOM\_DEVICE |
| Azure Storage accounts (built-in) | Microsoft.Storage/storageAccounts | Applicable | AZURE\_STORAGE\_ACCOUNT |
| Azure Stream Analytics Job | Microsoft.StreamAnalytics/streamingjobs | Applicable | cloud:azure:streamanalytics:streamingjobs, CUSTOM\_DEVICE |
| Azure Synapse Workspace | Microsoft.Synapse/workspaces | Applicable | cloud:azure:synapse:workspaces, CUSTOM\_DEVICE |
| Azure Apache Spark Pool | Microsoft.Synapse/workspaces/bigDataPools | Applicable | cloud:azure:synapse:workspaces:bigdatapools, CUSTOM\_DEVICE |
| Azure SQL Pool | Microsoft.Synapse/workspaces/sqlPools | Applicable | cloud:azure:synapse:workspaces:sqlpools, CUSTOM\_DEVICE |
| Azure Time Series Insights Environment | Microsoft.TimeSeriesInsights/environments | Applicable | cloud:azure:timeseriesinsights:environments, CUSTOM\_DEVICE |
| Azure Time Series Insights Event Source | Microsoft.TimeSeriesInsights/environments/eventsources | Applicable | cloud:azure:timeseriesinsights:eventsources, CUSTOM\_DEVICE |
| Azure App Service Environment v2 | Microsoft.Web/hostingEnvironments | Applicable | cloud:azure:web:hostingenvironments:v2, CUSTOM\_DEVICE |
| Azure App Service Plan | Microsoft.Web/serverfarms | Applicable | cloud:azure:web:serverfarms, CUSTOM\_DEVICE |
| Azure App Services (built-in) | Microsoft.Web/sites | Applicable | AZURE\_WEB\_APP |
| Azure App Services (built-in) | Microsoft.Web/sites | Applicable | AZURE\_FUNCTION\_APP |
| Azure Web App Deployment Slot | Microsoft.Web/sites/slots | Applicable | cloud:azure:web:appslots, CUSTOM\_DEVICE |
| Azure Function App Deployment Slot | Microsoft.Web/sites/slots | Applicable | cloud:azure:web:functionslots, CUSTOM\_DEVICE |

## Configuration API

To list all Azure-supported services on your cluster by the current version, use the [Azure-supported services API](/docs/dynatrace-api/configuration-api/azure-supported-services "Fetch a list of Azure supported services via the Dynatrace API.").

## Monitoring consumption

All cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions.

* Each metric dimension results in the ingestion of 1 data point
* 1 data point consumes 0.001 DDUs

## Related topics

* [Monitor Azure services with Azure Monitor metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")


---


## Source: opentelemetry-on-azure-functions-dotnet.md


---
title: Trace Azure Functions written in .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet
scraped: 2026-02-18T05:51:12.097479
---

# Trace Azure Functions written in .NET

# Trace Azure Functions written in .NET

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Jul 31, 2024

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

.NET version 8 or earlier

## Installation

1. Add the following dependencies to your project.

   * Required `Dynatrace.OpenTelemetry`âprovides integration of Dynatrace-specific components (for activity export and propagation) into OpenTelemetry .NET.
   * Optional [`OpenTelemetry.Extensions.Hosting`ï»¿](https://dt-url.net/w603yxv)âuses a `TracerProvider` with a dependency injection. While the latest release is supported for worker functions, in-process functions require OpenTelemetry.Extensions.Hosting version 1.0.0-rc9.5 or earlier. For details, see [Compatibility with `dotnet` (in-process) runtime](#compatibility-with-dotnet-in-process-runtime) below.

   Example commands to add dependencies

   ```
   dotnet add package Dynatrace.OpenTelemetry



   dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Extensions.Hosting
   ```
2. Additionally, depending on the runtime you use, we recommend that you use the following Azure-functions helper packages:

   * Recommended For in-process (library) functions (`dotnet` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions`
     + `OpenTelemetry.Instrumentation.AspNetCore`

     To add the packages, run the command below.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions



     dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Instrumentation.AspNetCore
     ```
   * Recommended For isolated aka worker functions (`dotnet-isolated` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker`

     To add the package, run the command below.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker
     ```
   * Optional Alternatively, on both runtimes you can use a Dynatrace package called `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` with the following functions:

     + [`AzureFunctionsCoreInstrumentation.Trace`](#manual-trace-instrumentation)
     + [`AzureFunctionsCoreInstrumentation.TraceAsync`](#manual-trace-instrumentation)

## Compatibility with OpenTelemetry and `System.Diagnostics.DiagnosticSource` versions

Periodically, we need to upgrade the minimum version of the `OpenTelemetry` NuGet package
our components depend on, and consequently, the minimum version of the `System.Diagnostics.DiagnosticSource` library.
This table lists the compatibility between `Dynatrace.OpenTelemetry`, `OpenTelemetry`, and `System.Diagnostics.DiagnosticSource` versions.

| `Dynatrace.OpenTelemetry` version | Minimum `OpenTelemetry` version | Minimum `System.Diagnostics.DiagnosticSource` version |
| --- | --- | --- |
| 1.273 and earlier | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

You don't usually need to worry about these dependencies as they're defined for you in our NuGet package. This
means that when you upgrade `Dynatrace.OpenTelemetry`, NuGet might implicitly upgrade your `OpenTelemetry` or
`System.Diagnostics.DiagnosticSource` version if you are currently on an earlier one.

## Compatibility with `dotnet` (in-process) runtime

For the `dotnet` (in-process) runtime, only certain versions of OpenTelemetry are compatible with certain versions of the Azure runtime:

* Azure Functions `dotnet` runtime v3 is not compatible with OpenTelemetry.
* Azure Functions `dotnet` runtime v4 is compatible with OpenTelemetry 1.3.x (`System.Diagnostics.DiagnosticSource` 6).

When using the `dotnet` (in-process) runtime, functions are loaded into the same CLR as the runtime. For instrumentation to work properly, the same `System.Diagnostics.DiagnosticSource` assembly needs to be used in the runtime and by the OpenTelemetry dependencies of the function. Symptoms of incompatible combinations may include your function failing to build, failing to load at runtime, or producing incomplete traces.

## Example using the dotnet (in-process) runtime

Your `Startup.cs` could look as follows:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Microsoft.Azure.Functions.Extensions.DependencyInjection;



using Microsoft.Extensions.DependencyInjection;



using OpenTelemetry.Trace;



[assembly: FunctionsStartup(typeof(Examples.AzureFunctionApp.Startup))]



namespace Examples.AzureFunctionApp



{



internal class Startup : FunctionsStartup



{



public override void Configure(IFunctionsHostBuilder builder)



{



builder.Services.AddOpenTelemetryTracing(sdk => sdk



.AddAzureFunctionsInstrumentation()



.AddAspNetCoreInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace & call AddTelemetrySdk (see below)



);



}



}



}
```

An instrumented in-process function could look like this:

```
using System.Diagnostics;



using System.Threading.Tasks;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Microsoft.AspNetCore.Http;



using Microsoft.AspNetCore.Mvc;



using Microsoft.Azure.WebJobs;



using Microsoft.Azure.WebJobs.Extensions.Http;



using Microsoft.Extensions.Logging;



namespace Examples.AzureFunctionApp



{



public class Function



{



public Function(ILoggerFactory loggerFactory)



{



// This is needed in every function in your app.



DynatraceSetup.InitializeLogging(loggerFactory);



}



[FunctionName("MyFunction")]



public async Task<IActionResult> Run(



[HttpTrigger(AuthorizationLevel.Function, "get", Route = null)] HttpRequest request,



Microsoft.Azure.WebJobs.ExecutionContext ctx)



{



// This adds the required attributes to make the activity recognizable as an Azure function invocation.



// Put this line first - there should be minimal time elapsing between the Activity being created



// by the ASP.NET core instrumentation and the call to this method.



AzureFunctionsInstrumentation.AddIncomingHttpAzureFunctionCallInfo(Activity.Current, ctx);



// Your handler code...



}



}



}
```

Additionally, you need to modify `host.json` to allow logging for `Dynatrace.OpenTelemetry`.
Note that this does not enable logging unless [explicitly configured](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace."). See [InitializeLogging](#initializelogging).

```
{



"version": "2.0",



"logging": {



// ...



"logLevel": {



"Dynatrace.OpenTelemetry": "Debug"



}



}



}
```

## Example using the dotnet-isolated runtime

The following examples use the [built-in HTTP modelï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model) of Azure functions and do **not** apply to functions using the [ASP.NET core integrationï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) of isolated Azure functions. See the chapter about [`ASP.NET core integration`](#asp-net-core-integration) below.

Your `Program.cs` could look as follows:

OpenTelemetry versions earlier than 1.4

OpenTelemetry version 1.4+

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWorkerDefaults(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetryTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWorkerDefaults(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

No additional code is needed to instrument functions; everything is handled by the middleware.

## ASP.NET core integration (isolated runtime)

If you create a new project for Azure function .NET8 or laterâfor example, using Visual Studio templateâthen, it'll add [ASP.NET core integrationï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) in Azure Function by default.

To enable function tracing, you need to use only the `ConfigureFunctionsWebApplication` method instead of `ConfigureFunctionsWorkerDefaults` in your initialization code given in [`ASP.NET core integration`](#asp-net-core-integration). The initialization code may look as follows:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWebApplication(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

## Technical details

### `InitializeLogging`

* Calling `InitializeLogging` is required even if you don't plan to enable logging, and the actual log messages won't be logged even after calling this method, unless [configured](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.").
* If you use the [`dotnet-isolated` runtimeï»¿](https://dt-url.net/2i23yrm) (out-of-process, worker functions), you need to call `InitializeLogging` in your `Main` method before calling `AddDynatrace`. You can pass `null` as `loggerFactory`, so that, if enabled, logging can use `Console.Out`/`Console.Error`. This is automatically forwarded to AppInsights for the `dotnet-isolated` runtime.
* If you have specific requirements, you can also pass any custom `LoggingFactory`.
* For the [`dotnet` runtimeï»¿](https://dt-url.net/2r43yf7) (in-process, class-library), sending logs to AppInsights requires using an `ILogger` or `ILoggerFactory` injected into the function with a dependency injection. Thus, you shouldn't use `null` as an argument for the `loggerFactory` parameter, but call `InitializeLogging` the first time any function in your Function App is invoked. To get the `ILoggerFactory`, simply add a parameter of that type.
* If you use the `ILoggerFactory` provided by Azure Functions, you also need to modify `host.json` to enable logging there. We recommend that you always use the `debug` log-level in `host.json`, as the actual log messages handed to the ILogger are separately configured in the Dynatrace configuration.

  ```
  {



  "version": "2.0",



  "logging": {



  // ...



  "logLevel": {



  "Dynatrace.OpenTelemetry": "Debug"



  }



  }



  }
  ```

### `AddDynatrace`

* `AddDynatrace` is an extension method to OpenTelemetry's `TracerProvider`. It requires `using Dynatrace.OpenTelemetry`. Currently, there aren't any additional parameters for this function, as configuration is read from environment variables and a `dtconfig.json` file. For details, see [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.").
* `AddDynatrace` mainly adds an `ActivityProcessor` to the `TracerProvider` that will send all activities to Dynatrace. This extension:

  + Sets the resources required by Dynatrace. Due to [an issue with the OpenTelemetry .NET SDKï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/issues/2909), this will override any existing resources. If you need custom resources, you need to call `SetResourceBuilder` on the `TracerProvider` *after* `AddDynatrace`. Be aware that this will override the resources configured by `AddDynatrace` and you need to readd them as part of the same `SetResourceBuilder` call. You can do this by calling the OpenTelemetry SDK's `AddTelemetrySdk` extension method on the `ResourceBuilder`.
  + Exchanges the global `Propagators.DefaultTextMapPropagator` with a custom one that is based on the default W3C-format, but does additional processing of `tracestate` and additional Dynatrace-specific HTTP headers. The baggage propagator is also enabled, as is default for OpenTelemetry .NET. There's currently no way to disable it. Using another propagator isn't supported and will lead to missing links in the distributed traces.

The following minimal snippet might be used to initialize a `TracerProvider` with `AddDynatrace`:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using OpenTelemetry.Trace;



// ...



// (call DynatraceSetup.InitializeLogging before or after AddDynatrace depending on runtime)



// ...



TracerProvider tracerProvider = Sdk.CreateTracerProviderBuilder().AddDynatrace().Build();
```

### `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync`

This is the low-level instrumentation function provided in the `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` package. You usually shouldn't use these, but instead use the runtime-specific helpers, as in the [examples above](#helper-usage-examples).

This function creates and starts a `System.Diagnostics.Activity`. It runs the handler function argument, then stops `Activity` and records any exception on it. An example usage could look like this:

```
public class HttpExample {



private readonly TracerProvider _tracerProvider;



public HttpExample(TracerProvider tracerProvider) {



_tracerProvider = tracerProvider;



}



[Function("HttpExample")]



public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequestData req, FunctionContext ctx)



{



var parent = ExtractParentContext(req, ctx); // See further below after this code snippet



return AzureFunctionsCoreInstrumentation.Trace(_tracerProvider, ctx.FunctionDefinition.Name, () => RunInternal(req), parent);



}



public IActionResult RunInternal(HttpRequestData req)



{



// ... your actual handler code ...



return new OkObjectResult("Your result");



}



}
```

The parent `ActivityContext` must be extracted from the HTTP headers using the `Propagators.DefaultTextMapPropagator`, which `AddDynatrace` initializes. If you don't pass any parent, a trace root span will be created (`Activity.Current` won't be used).

This is how a parent could be manually extracted with in-process functions for use with `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync` when not using the ASP.NET core instrumentation:

```
private static ActivityContext ExtractParentContext(HttpRequest request)



{



var context = Propagators.DefaultTextMapPropagator.Extract(default, request, HeaderValuesGetter);



return context.ActivityContext;



}



private static IEnumerable<string> HeaderValuesGetter(HttpRequest request, string name) =>



request.Headers.TryGetValue(name, out var values) ? values : (IEnumerable<string>)null;
```

For worker functions, the code can become more complex because in addition to HTTP headers, you may want to
(but don't have to) use the W3C TraceContext provided in the `FunctionContext`:

```
private static ActivityContext ExtractParentContext(HttpRequestData request, FunctionContext context) {



ActivityContext parent = default;



PropagationContext ctx = Propagators.DefaultTextMapPropagator.Extract(



default,



request.Headers,



(c, k) => c.TryGetValues(k, out var value) ? value : null);



parent = ctx.ActivityContext;



if (parent == default)



{



PropagationContext ctx2 = Propagators.DefaultTextMapPropagator.Extract(



default,



context.TraceContext,



(c, k) =>



{



string? result =



k.Equals("traceparent", StringComparison.OrdinalIgnoreCase) ? c.TraceParent :



k.Equals("tracestate", StringComparison.OrdinalIgnoreCase) ? c.TraceState :



null;



return result == null ? null : new[] { result };



});



parent = ctx2.ActivityContext;



}



return parent;



}
```

## Instrumenting `HttpClient` calls (outgoing HTTP requests)

A very common need is to trace outgoing HTTP requests. This can be achieved by using the [`OpenTelemetry.Instrumentation.Http` NuGet packageï»¿](https://www.nuget.org/packages/OpenTelemetry.Instrumentation.Http).

The instrumentation then has to be added to your `TracerProvider` setup by calling `AddHttpClientInstrumentation`, for example, in `Program.cs`:

OpenTelemetry versions earlier than 1.4

OpenTelemetry version 1.4+

```
// ...



using OpenTelemetry.Trace;



// ...



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



// ...



.ConfigureServices(services => services



.AddOpenTelemetryTracing(tracing => tracing



// ...



.AddHttpClientInstrumentation(op =>



{



// Exclude outgoing calls to external telemetry endpoints



op.Filter = AzureFunctionsCoreInstrumentation.FilterExternalTelemetry;



})))



.Build();



// ...
```

```
// ...



using OpenTelemetry.Trace;



// ...



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



// ...



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddHttpClientInstrumentation(op =>



{



// Exclude irrelevant outgoing calls (e.g. AppInsights QuickPulse pings)



op.FilterHttpRequestMessage = AzureFunctionsCoreInstrumentation.FilterExternalTelemetry;



})))



.Build();



host.Run();
```

Using a request filter as in the example above is highly recommended, as otherwise, depending on your Function Apps configuration, you might observe a large number of periodic requests to `https://rt.services.visualstudio.com/QuickPulseService.svc/ping` or similar URLs.

Alternatively, you can [disable telemetry dynamicallyï»¿](https://dt-url.net/95038ca).

We recommend to use the helper function `AzureFunctionsCoreInstrumentation.FilterExternalTelemetry` which is available in package `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` since version 1.267. In earlier versions, you can use the following filter instead:

```
op.FilterHttpRequestMessage = req => Activity.Current?.Parent != null;
```

Because of an [Azure Functions runtime issueï»¿](https://github.com/Azure/azure-functions-host/issues/7278), the HTTP instrumentation won't work on Azure Functions in-process version 3.x.

The underlying issue can also affect other instrumentations. Therefore, we do not recommend using in-process version 3 functions.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")


---


## Source: opentelemetry-on-azure-functions-nodejs.md


---
title: Trace Azure Functions written in Node.js
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs
scraped: 2026-02-18T05:51:52.406284
---

# Trace Azure Functions written in Node.js

# Trace Azure Functions written in Node.js

* Latest Dynatrace
* How-to guide
* 6-min read
* Updated on Nov 04, 2025

The [`@dynatrace/opentelemetry-azure-functions` moduleï»¿](https://dt-url.net/9603x96) provides APIs for tracing Node.js on Azure Functions.

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

* @dynatrace/opentelemetry-azure-functions version 1.243+

## Installation

To set up OpenTelemetry Node.js integration on Azure Functions, run the following command.

```
npm install --save @dynatrace/opentelemetry-azure-functions
```

## Trace export

Azure Functions can be developed by using either of two different [programming modelsï»¿](https://dt-url.net/9p03lmb), v3 and v4. To accommodate differences between the two models, Dynatrace provides two different ways of trace export:

* For programming model v3, the Azure Functions handler is wrapped (with the `wrapHandler` API) to generate and export traces.
* For programming model v4, [Azure Functions Hooksï»¿](https://dt-url.net/v323l3e) are used to achieve the same. Note that hooks are available only for the programming model v4.

For details, see below.

### Programming model v3

To export traces to Dynatrace from Azure Functions developed with [programming model v3ï»¿](https://dt-url.net/n443lxw)

1. Select one of the two ways below to initialize tracing.

   * `NodeTracerProvider`âmore lightweight than `NodeSDK`
   * `NodeSDK`âtypically used if you're interested in additional OpenTelemetry signals such as metrics

   It is possible to bundle several Azure Functions into a single Azure Function app. It's therefore important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put a tracing setup code into a shared file as described in the [Azure Functions JavaScript developer guideï»¿](https://dt-url.net/t223xf2) and require it at the top of all functions.

   The tracing setup code should be implemented to set up tracing only once before any other third-party module is required.

   NodeTracerProvider example (recommended)

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



   // tracing setup



   const exporter = new DtSpanExporter();



   const processor = new DtSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



   spanProcessors: [processor]



   // ...other configurations



   });



   provider.register({



   propagator: new DtTextMapPropagator(),



   // ...other configurations



   });
   ```

   NodeSDK example

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeSDK } from "@opentelemetry/sdk-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



   const sdk = new NodeSDK({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   spanProcessor: new DtSpanProcessor(new DtSpanExporter()),



   textMapPropagator: new DtTextMapPropagator(),



   // ...other configurations



   });



   sdk.start().then(() => {



   // Resources have been detected and SDK is started



   });
   ```
2. Wrap your function handler as below and export the wrapped handler.

   ```
   import type { AzureFunction, Context, HttpRequest } from "@azure/functions"



   // Import the wrapHandler function.



   import { wrapHandler } from "@dynatrace/opentelemetry-azure-functions";



   const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {



   // The created span is set as active by the OpenTelemetry ContextManager here



   context.log("HTTP trigger function processed a request.");



   const name = (req.query.name || (req.body && req.body.name));



   const responseMessage = name



   ? "Hello, " + name + ". This HTTP triggered function executed successfully."



   : "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.";



   context.res = {



   status: 200,



   body: responseMessage



   };



   };



   // Export the wrapped handler function.



   export default wrapHandler(httpTrigger);
   ```

### Programming model v4

There are two ways to export traces to Dynatrace from Azure Functions developed with [programming model v4ï»¿](https://dt-url.net/7t03lem).

* Use the `initDynatrace` API.
* Initialize tracing by registering Azure Function hooks manually.

Regardless of the instrumentation approach you choose, always implement the tracing setup code to set up tracing only once before any other third-party module is required.

#### Use the `initDynatrace` API

The `initDynatrace` API registers Azure Function hooks required for tracing and optionally registers required tracing components.

You can do this either with or without the OpenTelemetry setup:

* initDynatrace with OpenTelemetry setup (recommended)

  Pass `true` as the first argument to the `initDynatrace` to set up tracing and return the registered NodeTracerProvider. Resource attributes for the provider can be passed as the second optional argument.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // initialize instrumentation with tracing setup



  const provider = initDynatrace(true, {



  "my.resource.attribute": "My Resource"



  });



  // azure functions registration goes here
  ```
* initDynatrace without OpenTelemetry setup

  Call `initDynatrace` without parameters to register required Azure Function hooks only and set up tracing manually. This is convenient if customizations are required in the tracing setup.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  import { Resource } from "@opentelemetry/resources";



  import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



  import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const exporter = new DtSpanExporter();



  const processor = new DtSpanProcessor(exporter);



  const provider = new NodeTracerProvider({



  resource: new Resource({



  "my.resource.attribute": "My Resource"



  }),



  sampler: new DtSampler(),



  // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



  spanProcessors: [processor]



  // ...other configurations



  });



  provider.register({



  propagator: new DtTextMapPropagator(),



  // ...other configurations



  });



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

  Note that the tracing setup code is the same as for programming model v3 and the example with NodeSDK (from the model v3 above) would work here as well. To make it more convenient, there is the `configureDynatrace` API, which does the same as the above.

  ```
  import { configureDynatrace, initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const provider = configureDynatrace({



  "my.resource.attribute": "My Resource"



  });



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

#### Initializing tracing by registering Azure Function hooks manually.

In cases where you need to register additional Azure Functions hooks, the `initDynatrace` API might not be suitable.

Because Azure Function hooks are executed in the same order they are registered, it's important to:

* Register the Dynatrace Trace Start hook as the first pre-invocation hook
* Register the Dynatrace Trace End hook as the last post-invocation hook

Hook execution times are included in the total function execution time. If the order of the registered hooks is incorrect, the function execution time reported by our instrumentation won't be accurate either.

To find out more about Azure Function hooks, see the [Azure Functions Node.js developer guideï»¿](https://dt-url.net/uo23lv1).

To order hooks as needed, you can use the `registerTraceStartHook` and `registerTraceEndHook` APIs as shown below.

```
import { app, PreInvocationContext, PostInvocationContext } from "@azure/functions";



import { configureDynatrace, registerTraceStartHook, registerTraceEndHook } from "@dynatrace/opentelemetry-azure-functions";



// setup tracing with configureDynatrace or manually



const provider = configureDynatrace();



// register Dynatrace Trace Start hook



registerTraceStartHook();



// register other user's pre-invocation hooks



app.hook.preInvocation(async (context: PreInvocationContext) => {



// hook code



});



// register other user's post-invocation hooks



app.hook.postInvocation(async (context: PostInvocationContext) => {



// hook code



});



// register Dynatrace Trace End hook



registerTraceEndHook();



// azure functions registration goes here
```

## Compatibility

| OneAgent version | OpenTelemetry API | OpenTelemetry SDK |
| --- | --- | --- |
| 1.243 - 1.255 | 1.x.y | 1.0.x |
| 1.257+ | 1.x.y | 1.0.x - 1.7.x |
| 1.259+ | 1.x.y | 1.0.x - 1.8.x |
| 1.261+ | 1.x.y | 1.0.x - 1.9.x |
| 1.265+ | 1.x.y | 1.0.x - 1.10.x |
| 1.273+ | 1.x.y | 1.0.x - 1.15.x |
| 1.279+ | 1.x.y | 1.0.x - 1.17.x |
| 1.283+ | 1.x.y | 1.0.x - 1.18.x |
| 1.285+ | 1.x.y | 1.0.x - 1.20.x |
| 1.289+ | 1.x.y | 1.0.x - 1.22.x |
| 1.293+ | 1.x.y | 1.0.x - 1.24.x |
| 1.297+ | 1.x.y | 1.0.x - 1.25.x |
| 1.303+ | 1.x.y | 1.0.x - 1.26.x |
| 1.307+ | 1.x.y | 1.0.x - 1.29.x |
| 1.313+ | 1.x.y | 1.0.x - 1.30.x |
| 1.327+ | 1.x.y | 1.0.x - 2.0.x |
| 1.331+ | 1.x.y | 1.0.x - 2.2.x |

Dynatrace version 1.327+ The `@dynatrace/opentelemetry-azure-functions` module supports OpenTelemetry SDK V2. To use V2 (instead of V1), override the version of `@dynatrace/opentelemetry-core` module (required by `@dynatrace/opentelemetry-azure-functions`) with a version that supports OpenTelemetry SDK V2.

1. From the table above, choose a version that supports OpenTelemetry SDK V2.
2. In your `package.json` file, add the `overrides` section and specify one of the versions of the `@dynatrace/opentelemetry-core` module to enforce.
3. Run `npm install` to apply the changes.

Example:

```
{



"dependencies": {



"@dynatrace/opentelemetry-azure-functions": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Once `@dynatrace/opentelemetry-azure-functions` is changed to use OpenTelemetry SDK V2 by default, this override won't be needed anymore.

Supported [Azure Functions runtimeï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):

* 4.x

Supported [Azure Functions programming modelï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):

* 3.x
* 4.x @dynatrace/opentelemetry-azure-functions version 1.289+

## Limitations

* Only `async` function handlers are supported.

  + This follows the Azure recommendation to use [`async` and `await`ï»¿](https://dt-url.net/be03x31).
  + `wrapHandler` returns any non-`async` function unwrapped, so the function itself will work but no span will be created.
  + Note that async functions were introduced in ECMAScript 2017. No span will be created if an earlier version of ECMAScript is used. In case TypeScript is used, make sure [compilation targetï»¿](https://dt-url.net/df02zbc) is set to ECMAScript 2017 or higher.
* The package supports only the [Consumption planï»¿](https://dt-url.net/ck022yx). While it may work on other plans, we cannot guarantee compatibility or performance.
* Signaling function completion using the deprecated [`context.done()`ï»¿](https://dt-url.net/0l23xfy) or [`context.res.send()`ï»¿](https://dt-url.net/dj43xgq) calls is not supported. Either use a `$return` binding and return the result from the function handler, or use a named `out` binding and set `context.binding.<name>`. For HTTP triggers, setting `context.res` is also supported.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")


---


## Source: opentelemetry-on-azure-functions-python.md


---
title: Trace Azure Functions written in Python
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python
scraped: 2026-02-17T04:56:27.351489
---

# Trace Azure Functions written in Python

# Trace Azure Functions written in Python

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 13, 2022

The [`dynatrace-opentelemetry-azure-functions` packageï»¿](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) provides APIs for tracing Python Azure Functions.

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

* dynatrace-opentelemetry-azure-functions version 1.245+

## Installation

To set up OpenTelemetry Python integration on Azure Functions, add the following line to the `requirements.txt` file of your function app:

```
dynatrace-opentelemetry-azure-functions
```

This adds the latest version of the `dynatrace-opentelemetry-azure-functions` package as a dependency to your function app. For more information about managing dependencies, consult the [Azure Functions Python developer guideï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).

## Trace export

To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler functions](#instrument).

### Initialize tracing

Select one of the two ways below to initialize tracing.

* `configure_dynatrace` functionâThis is the recommended option unless you need to manually set up the tracing components.
* Manual tracing setupâThis allows for a more fine-grained setup of tracing components.

Because it's possible to bundle several Azure Functions into a single Azure Function app, it's important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put the tracing setup code into a shared file as described in the [Azure Functions Python developer guideï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure) and import it at the top of the files that define a function.

Example with `configure_dynatrace` (recommended)

```
from opentelemetry.sdk.resources import Resource



from opentelemetry.semconv.resource import ResourceAttributes



from dynatrace.opentelemetry.tracing.api import configure_dynatrace



tracer_provider = configure_dynatrace(



resource=Resource.create({"my.resource.attribute": "My Resource"})



)
```

Example with manual tracing setup

```
from opentelemetry.propagate import set_global_textmap



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider



from opentelemetry.semconv.resource import ResourceAttributes



from opentelemetry.trace import set_tracer_provider



from dynatrace.opentelemetry.tracing.api import (



DtSampler,



DtSpanProcessor,



DtTextMapPropagator,



)



span_processor = DtSpanProcessor()



tracer_provider = TracerProvider(



sampler=DtSampler(),



resource=Resource.create({"my.resource.attribute": "My Resource"}),



)



tracer_provider.add_span_processor(span_processor)



set_global_textmap(DtTextMapPropagator())



set_tracer_provider(tracer_provider)
```

The tracing setup code should be implemented to set up tracing only once before any other third-party module is imported. If you use `isort` to sort your imports, we suggest that you [deactivate itï»¿](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) while importing the tracing setup module, as shown in the following example:

```
# isort: off



import setup_tracing  # import the module containing your setup code



# isort: on



# import other modules
```

### Instrument a handler function

#### Programming model v1

Use the `wrap_handler` decorator to instrument your handler function, as shown in the example below:

```
from azure import functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



@wrap_handler



def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:



# From here the created span is available in the OpenTelemetry context as the current span.



# do something ...



return  func.HttpResponse(f"Hello world.", status_code=200)
```

The [contextï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) parameter is optional and can be omitted from the handler's signature.

If your HTTP function handler doesn't return an explicit result and uses multiple `Out` bindings, you should provide the name of the response binding as a binding hint to the decorator, so that result attributes can be properly set on the span.

Example:

```
from azure import functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



@wrap_handler(http_result_param_name="res")



def main(req: func.HttpRequest, other: func.Out[str], res: func.Out[func.HttpResponse]):



# do something ...



res.set(func.HttpResponse(f"Hello world.", status_code=200))
```

#### Programming model v2

Functions implemented using the [v2 programming modelï»¿](https://dt-url.net/ix03806) can also be instrumented using the `wrap_handler` decorator.

Because the Azure functions framework for programming model V2 uses decorators to mark handler functions, the order in which the `wrap_handler` and the Azure decorators are applied is important.
The snippet below shows the correct order: the handler needs to be decorated with `wrap_handler` before the `app.route` decorator.

```
import azure.functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



app = func.FunctionApp()



@app.function_name("MyHttpFunc")



@app.route(route="hello")



@wrap_handler # Note: wrap_handler must be located after the app.route decorator, so it's executed first.



def main(req: func.HttpRequest) -> func.HttpResponse:



# do something ...



return func.HttpResponse("Hello world", status_code=200)
```

## Limitations

* The Azure runtime dynamically passes the [invocation contextï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) argument to your handler function if the handler's signature contains a parameter with name `context`. However, if there's also a binding with the name `context` in your `function.json` file, the invocation context is ignored by the binding and the binding is passed instead. The `wrap_handler` decorator won't work in this case, since it requires the invocation context to extract certain span attributes. Be sure not to use the name `context` for any binding in your `function.json` file.
* HTTP handler functions with multiple `Out` bindings and no explicit return result should provide the name of the response output binding to the function decorator, so that result span attributes can be properly set.
* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.
* Instrumentation of [WSGI and ASGIï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) web frameworks is currently not supported for the v2 programming model because of the handler's different signature.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [Azure monitoringï»¿](https://www.dynatrace.com/technologies/azure-monitoring/)


---


## Source: opentelemetry-on-azure-functions.md


---
title: Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions
scraped: 2026-02-18T05:50:01.819888
---

# Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan

# Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Mar 31, 2025

Dynatrace version 1.240+ OneAgent version 1.193+

Dynatrace uses [OpenTelemetryï»¿](https://dt-url.net/y903u4j) to monitor Azure Functions invocations.
For that purpose, Dynatrace provides language-specific packages, such as [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` for .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace."), that can be used in combination with default OpenTelemetry SDKs and APIs.

## Installation

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Activate the OneAgent feature**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#oneagent-feature "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Select a configuration method**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#choose-config-method "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Specify a Dynatrace API endpoint**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#specify-endpoint "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Apply the configuration to your function app**](#apply-config)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Instrument the function code**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#instrument-code "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")

### Step 1 Activate the OneAgent feature

Go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.

### Step 2 Select a configuration method

1. In Dynatrace,  **Search** for **Deploy OneAgent** app and select it.
2. Under **Download Dynatrace OneAgent**, select **Set up** > **Azure Functions**.
3. On the **Enable Monitoring for Azure Functions** page, under **How will you configure your Azure Functions?**, select your preferred configuration method from the dropdown menu.

### Step 3 optional Specify a Dynatrace API endpoint Optional

If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.

To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the Azure Function that you want to monitor.

### Step 4 Apply the configuration to your function app

To apply the configuration, select one of the options below, depending on your configuration method.

Configure with JSON file

Configure with environment variables

Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your Azure Functions deployment.

On **Enable Monitoring for Azure Functions**, under **Use the following values to configure your monitored Azure Functions**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your function app configuration:

1. In Azure Portal, go to your function app.
2. In **Settings**, select **Configuration**.
3. Edit any existing environment variables so that the names and values match those in [Dynatrace](#variables-dynatrace), or, if your function app doesn't have any existing variables, select **New application setting** and add the names and values for all the variables in [Dynatrace](#variables-dynatrace).

Leave the settings not listed by Dynatrace unchanged.

### Step 5 Instrument the function code

Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution:

* **.NET (C#):** [Trace Azure Functions written in .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")
* **Node.js (Javascript):** [Trace Azure Functions written in Node.js](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")
* **Python:** [Trace Azure Functions written in Python](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")

## Known limitations

The Dynatrace Azure Functions integration doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace OneAgent, this results in **unmonitored hosts**.

## Related topics

* [Monitor Azure Functions on App Service Plan for Windows](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.")
* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: otel-native-dotnet-azure.md


---
title: Trace Azure Functions with OpenTelemetry .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure
scraped: 2026-02-18T05:51:40.792782
---

# Trace Azure Functions with OpenTelemetry .NET

# Trace Azure Functions with OpenTelemetry .NET

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Mar 09, 2022

The OpenTelemetry Protocol (OTLP) exporters for .NET currently support [gRPC and HTTP 1.1 with binary Protocol Buffers (Protobuf) payloadï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#exporters) transports. Supported corresponding protocol values are `grpc` and `http/protobuf`. [Configuration optionsï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options) can be set either via environment variables or explicitly in code.

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Instrument Azure Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Azure Functions.

To instrument your Azure Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Set up export**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#export "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add dependencies**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#dependencies "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument code**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#instrument "Learn how to use OpenTelemetry .NET to trace Azure Functions.")

### Step 1 Set up export

gRPC export

HTTP export

To ingest **gRPC** via the Dynatrace Trace API, you need to use an [OpenTelemetry collectorï»¿](https://dt-url.net/vf23sfn) between Dynatrace and the exporter.

If you use environment variables for setup, you need to set the following value:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `grpc`

#### Configure the OpenTelemetry Collector

To ingest **gRPC** via the Dynatrace Trace API, you need to use an [OpenTelemetry collectorï»¿](https://dt-url.net/vf23sfn) between Dynatrace and the exporter.

The OpenTelemetry Collector is available as a [Docker imageï»¿](https://hub.docker.com/r/otel/opentelemetry-collector).
To use this collector to export trace data to Dynatrace, you need to customize the [configurationï»¿](https://opentelemetry.io/docs/collector/configuration/) using the OpenTelemetry OTLP exporter.

Here is a sample configuration file:

```
receivers:



otlp:



protocols:



grpc:



exporters:



otlp_http:



endpoint: "https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp"



headers: {"Authorization": "Api-Token <YOUR-DYNATRACE-API-TOKEN}"}



service:



pipelines:



traces:



receivers: [otlp]



exporters: [otlp_http]
```

For further details on configuration, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

To ingest **HTTP** via the Dynatrace Trace API, you need to [configure the exporterï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options). The exporter will then directly send traces to the configured endpoint.

If you use environment variables for setup, you need to set the following values:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `http/protobuf`
* For `OTEL_EXPORTER_OTLP_ENDPOINT`: the URL for export endpoint

  + If you set the endpoint URL via environment variables, the export endpoints for traces and metrics are automatically appended by `v1/traces` for traces and `v1/metrics` for metrics. For example, if the endpoint is set to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp`, traces will be exported to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp/v1/traces`.
  + If you set the endpoint explicitly in code, it will be used as is.

  For details, see [Endpoint URLs for OTLP/HTTPï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#endpoint-urls-for-otlphttp).
* For `OTEL_EXPORTER_OTLP_HEADERS`: the authorization API token value in the following format: `Authorization=Api-Token <TOKEN>`.

### Step 2 Add dependencies

Add the following dependencies via NuGet to your project:

```
OpenTelemetry.Exporter.OpenTelemetryProtocol
```

OpenTelemetry also provides other [auto-instrumentation libraries available as NuGet packagesï»¿](https://www.nuget.org/packages?q=opentelemetry.instrumentation).

### Step 3 Instrument code with OpenTelemetry

Intrument using gRPC export

Instrument using HTTP export

If you don't set the `Protocol` property of the `OtlpExporterOptions` class via environment variables or in code, it will be initialized as [`OtlpExportProtocol.Grpc` by defaultï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry.Exporter.OpenTelemetryProtocol/OtlpExporterOptions.cs#L99).

```
public class Startup : FunctionsStartup



{



public override void Configure(IFunctionsHostBuilder builder)



{



string activitySource = "[activitySource]";



string serviceName = "[serviceName]";



string collectorUrl = "[collectorUrl]"  // Points to the running collector, configured before.



builder.Services.AddSingleton((builder) =>



{



return Sdk.CreateTracerProviderBuilder()



.SetSampler(new AlwaysOnSampler())



.AddSource(activitySource)



.SetResourceBuilder(ResourceBuilder.CreateDefault().AddService(serviceName))



.AddHttpClientInstrumentation(op =>



{



// Exclude frequent calls generated by Azure Application Insights



op.FilterHttpRequestMessage = (req) => !req.RequestUri.AbsoluteUri.Contains("visualstudio");



})



.AddOtlpExporter(otlpOptions =>



{



otlpOptions.Endpoint = new Uri(collectorUrl);



})



.Build();



});



}



}
```

The code sample using **HTTP exporter** is similar to the **gRPC exporter** sample; the only difference is in the configuration of `OtlpExporterOptions`:

```
return Sdk.CreateTracerProviderBuilder()



// ...



// ... other initialization code (see the code snippet for the gRPC case)



// ...



.AddOtlpExporter(otlpOptions =>



{



otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;



otlpOptions.Headers = "Authorization=Api-Token <TOKEN>";



//Use an explicitly set endpoint for export



//or an endpoint configured via environment variable.



otlpOptions.Endpoint = new Uri("https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp");



})



.Build();
```

If the configuration is done via environment variables, the code for adding an OTLP/HTTP exporter is even simpler:

```
return Sdk.CreateTracerProviderBuilder()



// ...



// ... other initialization code (see the code snippet for the gRPC case)



// ...



.AddOtlpExporter()



.Build();
```


---


## Source: func-dynamic-plans.md


---
title: Monitor Azure Functions on Consumption Plans
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-02-16T09:31:33.797276
---

# Monitor Azure Functions on Consumption Plans

# Monitor Azure Functions on Consumption Plans

* Latest Dynatrace
* Overview
* 1-min read
* Published Apr 20, 2022

Azure Functions let you run code without provisioning or managing servers.
This deployment model is sometimes referred to as "serverless" or "Function as a Service" (FaaS).

* An Azure Function runs in an application on a container managed by Azure. This lets you focus on writing code without worrying about the underlying application or infrastructure.
* Azure Functions are ephemeral. This means that the underlying container can be suspended or recycled when thereâs no request pending.

## Integration

[Trace Azure Functions written in .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")

[Trace Azure Functions written in Node.js](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")

[Trace Azure Functions written in Python](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")

## Monitoring Consumption

For Azure Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")


---


## Source: integrate-oneagent-on-azure-functions.md


---
title: Monitor Azure Functions on App Service Plan for Windows
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions
scraped: 2026-02-17T04:52:00.376987
---

# Monitor Azure Functions on App Service Plan for Windows

# Monitor Azure Functions on App Service Plan for Windows

* Latest Dynatrace
* How-to guide
* 6-min read
* Published Oct 16, 2018

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extension for easy deployment of OneAgent](#install-dynatrace-oneagent-site-extension-via-azure-portal)
* Support for Azure Functions that are written in .NET (in-process) and hosted on an **App Service Plan on Windows**
* Enhanced support for Azure App Service metadata such as compute mode, SKU, and more
* Automatic service detection for functions written in any language for Azure Function Runtime v2+
* Automatic tracing and code-profiling for .NET/.NET Core based functions
* End-to-end tracing across multiple functions for http-based triggers and other instrumented services and applications. Other triggers such as QueueTriggers require custom trace propagation.

Dynatrace provides an [Azure Site Extensionï»¿](https://github.com/projectkudu/kudu/wiki/Azure-Site-Extensions) to install OneAgent on Azure Functions. Azure Site Extensions are the native extension mechanism provided via [Kuduï»¿](https://github.com/projectkudu/kudu), which is the deployment management engine behind Azure App Services.

The Dynatrace OneAgent site extension doesn't include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").

Limitations

Since Azure Functions are a fully managed hosting platform built on top of Azure App Services, functions/applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system. This results in some restrictions for OneAgent:

* Enhanced I/O monitoring requires [Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.").
* Dynatrace Log Monitoring isn't supported for Azure Functions.
* Network zones aren't supported.

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Install Dynatrace OneAgent site extension

There are two ways to install the Dynatrace OneAgent site extension: via Azure Portal or using an ARM template. Follow the steps below for instructions.

### Install Dynatrace OneAgent site extension via Azure Portal

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

### Install Dynatrace OneAgent site extension using an ARM template

Alternatively to the main installation method via Azure Portal, you can make the Dynatrace site extension part of your ARM templates.  
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
| DT\_TENANT | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| DT\_API\_TOKEN | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| DT\_API\_URL | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| DT\_SSL\_MODE | Optional | To automatically accept all self-signed TLS certificates, set the value to `all`. |

If `AlwaysOn` isn't set to `true`, the installation of OneAgent is triggered on the start-up/first request to Kudu.

To check the deployment status, go to **Deployment Status**.

After installation is complete, go to Azure Portal and restart the App Function application to recycle the application's worker process. Immediately after restart, OneAgent will begin monitoring your application.

## Automate the installation and update of Dynatrace OneAgent site extension with Kudu REST API

After you install the Dynatrace OneAgent site extension, you can use the **Kudu REST API** to automate installation and update of the Dynatrace OneAgent site extension. See the [automation setup page on GitHubï»¿](https://github.com/Dynatrace/snippets/tree/master/technologies/azure/automate-appservice-siteextension-setup) for details.

The root URL to access the REST API is `https://<Your-AppService-Subdomain>.scm.azurewebsites.net/dynatrace/`, where you need to replace `<Your-AppService-Subdomain>` with your own value. To authenticate, you can use either the user publishing credentials or the site-level credentials. See [Accessing the Kudu serviceï»¿](https://github.com/projectkudu/kudu/wiki/Accessing-the-kudu-service) for details.

Method

Endpoint

Description

Response

GET

`/api/status`

Returns the current status of the OneAgent installation.

The returned "state" field can be:

* `NotInstalled`
* `Downloading`
* `Installing`
* `Installed`
* `Failed`

For automation, use **isAgentInstalled** and **isUpgradeAvailable** to determine whether OneAgent is installed and whether an upgrade is available.

```
{



"state": "Installed",



"message": "OneAgent installed",



"version": "1.157",



"isAgentInstalled": true,



"isUpgradeAvailable": false,



"isFunction": false,



"functionAppSettings": null



}
```

GET

`/api/settings`

Returns the current settings, including Dynatrace credentials.

The value for `apiUrl` can be left empty for a SaaS environment.

```
{



"apiUrl": "",



"apiToken": "<your-api-token>",



"environmentId": "<your-environment-id>",



"sslMode": "Default"



}
```

PUT

`/api/settings`

Starts OneAgent installation with the given settings. These settings are stored only if the installation finishes successfully.

In the payload, you need to send the data in the format received by the `GET /dynatrace/api/settings` request.

If an update is available in the status request, this `PUT` request can be used to start the upgrade.

Empty response

## Override OneAgent configuration

To override the default configuration, you can use the following parameters.

| Parameter | Description |
| --- | --- |
| DT\_CONNECTION\_POINT | Semicolon-separated list of communication-endpoints |

How to add the DT\_CONNECTION\_POINT parameter in Azure Portal

To add the DT\_CONNECTION\_POINT parameter

1. In Azure Portal, select the web function you want to monitor.
2. Select **Settings** > **Configuration** > **Application Settings**.
3. Select **New application setting**.
4. Enter the following key/value pair:

   * Name: `DT_CONNECTION_POINT`
   * Value: `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/communication`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` with your own value.

   ![DT connection](https://dt-cdn.net/images/2020-11-18-16-07-38-1030-8f03d116e4.png)
5. Select **OK** to save the configuration.

## Update OneAgent

Dynatrace doesn't provide OneAgent updates on Azure Functions automatically. To update OneAgent on Azure Functions, go to Azure Portal, browse to your site extension, and, if an update is available, select **Update**. You can monitor the progress until the update is finished.  
Then restart Azure Functions to recycle the application worker process.

The extension provides its own REST API for automating OneAgent updates. See [REST API](#restapi) for details.

### Update the site extension

To update the site extension on Azure App Service, go to the Azure Portal, browse to your site extension, and, if an update is available, select **Update**.

An update to the site extension doesn't force an update to OneAgent.

When upgrading the extension from version 1.x to version 2.x, if you have **Always On** selected on your App Service, the upgrade of OneAgent is either triggered automatically, or on the first request to the UI extension. If you don't have **Always On** selected, you must restart App Service, so that the extension process starts.

## Uninstall OneAgent

Removing the extension also removes OneAgent.

If the application is running at the time of removal, the extension recognizes the running application, taking care to not remove any Dynatrace artifacts to prevent issues with the application. Instead, only the extension including the configuration is removed, so that, on the next restart of the application, OneAgent is no longer active.

## Monitoring consumption

See [Serverless monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details on monitoring consumption for Azure Functions.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")


---


## Source: azure-functions.md


---
title: Monitor Azure Functions using Azure App Service (built-in)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions
scraped: 2026-02-18T05:40:15.085872
---

# Monitor Azure Functions using Azure App Service (built-in)

# Monitor Azure Functions using Azure App Service (built-in)

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Apr 20, 2022

Azure Functions offers a wide range of options to address various Azure Functions [scenarios and use-casesï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios):

* Use your preferred language
* Automate deployment
* Take advantage of flexible [hostingï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)

## Distributed Tracing

With the different options for hosting your functions, Dynatrace provides you with the best options to enable distributed tracing.

* Dynatrace offers an easy integration for **Azure Functions running on Appservice- (Dedicated) plan** using a [site extension](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.").
* Tracing Azure Functions on a **Consumption- or Premium-Plan** comes with additional restrictions by the nature of a serverless service, such as using instrumentation agents to fully automatically instrument your code at runtime.

Dynatrace provides distributed tracing for these sandboxed environments based on [OpenTelemetryï»¿](https://opentelemetry.io/). If you already use OpenTelemetry to instrument your functions, you can ingest the trace data using [Dynatrace Trace Ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), but we recommend that you use the [Dynatrace exporter](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans"), which adds additional benefits to fully leverage the automatic AI-based analysis capabilities of Dynatrace.

To make using OpenTelemetry easier, Dynatrace provides [library packages for Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans") to reduce necessary OpenTelemetry boiler-plate code for trace-propagation, applying resource attributes and initialization code as well as aligning with semantic conventions.

By using advanced concepts such as [aspect-oriented programming (AOP)ï»¿](https://en.wikipedia.org/wiki/Aspect-oriented_programming), it is even possible to add fully automatic instrumentation without changing a single line of code, as demonstrated within this community github-project for [Azure Functions .NETï»¿](https://github.com/dtPaTh/Azure.Functions.Tracing).

## Additional visibility using logs and platform metrics

To enhance visibility for monitoring your Azure Functions health, we recommend that you [enable capturing service metrics from Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/monitor-func-service-builtin "Monitor Azure Function Services and view available metrics.") as well as [ingesting logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.").

![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)

## Related topics

* [Serverless monitoring](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")


---


## Source: azure-migration-guide.md


---
title: Migrate from Azure classic (formerly 'built-in') services to cloud services
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide
scraped: 2026-02-18T05:52:32.298221
---

# Migrate from Azure classic (formerly 'built-in') services to cloud services

# Migrate from Azure classic (formerly 'built-in') services to cloud services

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Jun 27, 2024

From the Azure overview page, you can access Dynatrace classic services and cloud services for Azure monitoring. Both types of services share the same Azure resources. However, classic services use a predefined set of metrics, so configuring which metrics to monitor, or determining which ones are already monitored, is not supported.

## Classic services vs cloud services

As previously mentioned, classic services and cloud services share the same Azure resources. However, cloud services support a wider range of configuration options, such as new metrics and customizable monitored metrics. To give you more customization options, weâve started the following:

* Adding more services to the **Cloud services** section so you can customize which metrics and dimensions you want to monitor.
* Adding more metrics for cloud services; not only are they configurable, but you can now monitor much more than before.
* Replacing the classic services with cloud services that have more configuration options regarding metrics and dimensions.

![public-cloud-services-section-infographic](https://dt-cdn.net/images/public-cloud-services-section-infographic-950-ccb7323d99.png)

If you're using classic services, we recommend migrating to cloud services to take advantage of the wider range of customizable configuration options.

## Impact of the migration

Even though classic and cloud services monitor the same Azure resources on Dynatrace side, they are monitored as two different entities.

* They have different entity IDs and metric keys.
* Data for each Dynatrace entity type is collected and stored separately.
* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change You need to adapt the configuration of dashboards, alerts, and management zones based on entity ID or [metric keys with the monitored service type](#metrics).

You do have the option to choose from a classic or cloud service to preserve historical data, for now. But be aware of the following:

* Historical data is persisted on the classic services. If you switch back, monitored data will present gaps for the period in which the resources were monitored via the cloud service.
* You canât have both of them turned on simultaneously. Even though on Dynatrace side theyâre two different services, the legacy and new versions monitor the same Azure resource. If you had two versions switched on simultaneously, you would be charged double for polling the same data twice.
* If you turn on the new version, the classic version is turned off automatically, and vice versa.
* There is no direct link between entities containing historical and new data.
* Logs from [Azure log forwarder](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.") are still linked to historical data and entities.

To monitor cloud services, you need to have [Environment ActiveGateï»¿](https://dt-url.net/sc0396g) configured.

## Changes in the UI

Your Azure overview page changes after configuring a new version of a service.

For example, letâs look at **Azure Storage Account**.

* If the legacy **Azure Storage Accounts** service is configured, this is what the **Storage accounts** section of the Azure overview looks like.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1449-46980fd72d.png)

* Select **Cloud services** to find new overview pages for the services.

![azure-public-cloud-vct-dev1-services](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-services-1112-707a41c03e.png)

* After configuring **Azure Storage Account**, **Azure Storage Blob**, **Azure Storage File**, **Azure Storage Queue**, and **Azure Storage Table** services, this is what the **Storage accounts** section of the Azure overview looks like.

![azure-public-cloud-vct-dev1-storage](https://dt-cdn.net/images/azure-public-cloud-vct-dev1-storage-1452-a16425bb86.png)

* Additionally, you can configure metrics for cloud services via UI.

![azure-settings-manage-services](https://dt-cdn.net/images/azure-settings-manage-services-1297-d00845930c.png)

![azure-settings-storage-blob-services](https://dt-cdn.net/images/azure-settings-storage-blob-services-1311-5b78cf0ab1.png)

## Cloud services and their corresponding classic services

| new Cloud service | old Classic service |
| --- | --- |
| [Azure API Management Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service "Monitor Azure API Management Service and view available metrics.") | [Azure API Management services (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin "Monitor Azure API Management Services and view available metrics.") Deprecated |
| [Azure Application Gateway](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway "Monitor Azure Application Gateway and view available metrics.") | [Azure Application Gateway (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin "Monitor Azure Application Gateways and view available metrics.") |
| [Azure Basic Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer "Monitor Azure Basic Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Gateway Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer "Monitor Azure Gateway Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Standard Load Balancer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer "Monitor Azure Standard Load Balancer and view available metrics.") | [Azure Load Balancer (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin "Monitor Azure Load Balancers and view available metrics.") |
| [Azure Cache for Redis](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis "Monitor Azure Cache for Redis and view available metrics.") | [Azure Redis (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin "Monitor Azure Redis Cache and view available metrics.") |
| [Azure Cosmos DB Account (GlobalDocumentDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb "Monitor Azure Cosmos DB Account (GlobalDocumentDB) and view available metrics.") | [Azure Cosmos DB (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Monitor Azure Cosmos DB and view available metrics.") |
| [Azure Cosmos DB Account (MongoDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb "Monitor Azure Cosmos DB Account (MongoDB) and view available metrics.") | [Azure Cosmos DB (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin "Monitor Azure Cosmos DB and view available metrics.") |
| [Azure IoT Hub](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub "Monitor Azure IoT Hub and view available metrics.") | [Azure IoT Hubs (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin "Monitor Azure IoT Hub and view available metrics.") |
| [Azure SQL Server](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server "Monitor Azure SQL Server and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL Database (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu "Monitor Azure SQL Database (DTU) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL Database (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore "Monitor Azure SQL Database (vCore) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL elastic pool (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu "Monitor Azure SQL elastic pool (DTU) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure SQL elastic pool (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore "Monitor Azure SQL elastic pool (vCore) and view available metrics.") | [Azure SQL (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin "Monitor Azure SQL Servers and view available metrics.") |
| [Azure Storage Account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Blob Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage File Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Queue Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |
| [Azure Storage Table Services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account "Monitor Azure Storage Account and view available metrics.") | [Azure Storage accounts (classic)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin "Monitor Azure Storage Accounts and view available metrics.") |

## Metrics migration

Below you can find tables with classic services metrics and their corresponding cloud services metrics. Empty cells indicate the lack of an identical corresponding metric.

### Azure API Management Service

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Failed requests | builtin:cloud.azure.apiMgmt.requests.failed | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "400"), eq("Gateway response code category", "5xx"))) |
| Other requests | builtin:cloud.azure.apiMgmt.requests.other | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(and(ne("Gateway response code category", "1xx"), ne("Gateway response code category", "2xx"), ne("Gateway response code", "300"), ne("Gateway response code", "301"), ne("Gateway response code", "304"), ne("Gateway response code", "307"), ne("Gateway response code", "400"), ne("Gateway response code", "401"), ne("Gateway response code", "403"), ne("Gateway response code", "429"), ne("Gateway response code category", "5xx"))) |
| Successful requests | builtin:cloud.azure.apiMgmt.requests.successful | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code category", "1xx"), eq("Gateway response code category", "2xx"), eq("Gateway response code", "300"), eq("Gateway response code", "301"), eq("Gateway response code", "304"), eq("Gateway response code", "307"))) |
| Total requests | builtin:cloud.azure.apiMgmt.requests.total | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests |
| Unauthorized requests | builtin:cloud.azure.apiMgmt.requests.unauth | Requests | ext:cloud.azure.microsoft\_apimanagement.service.requests:filter(or(eq("Gateway response code", "401"), eq("Gateway response code", "403"), eq("Gateway response code", "429"))) |
| Capacity | builtin:cloud.azure.apiMgmt.capacity | Capacity | ext:cloud.azure.microsoft\_apimanagement.service.capacity |
| Duration | builtin:cloud.azure.apiMgmt.duration | Overall duration of gateway requests | ext:cloud.azure.microsoft\_apimanagement.service.duration |

### Azure Application Gateway

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Healthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.healthyhostcount |
| Unhealthy host count | builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | ext:cloud.azure.microsoft\_network.applicationgateways.unhealthyhostcount |
| Requests failed | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Failed requests | ext:cloud.azure.microsoft\_network.applicationgateways.failedrequests |
| Requests total | builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Total requests | ext:cloud.azure.microsoft\_network.applicationgateways.totalrequests |
| Response status | builtin:cloud.azure.appGateway.http.status.response | Response status | ext:cloud.azure.microsoft\_network.applicationgateways.responsestatus |
| Current connections count | builtin:cloud.azure.appGateway.network.connections.count | Current connections | ext:cloud.azure.microsoft\_network.applicationgateways.currentconnections |
| Network throughput | builtin:cloud.azure.appGateway.network.throughput | Throughput | ext:cloud.azure.microsoft\_network.applicationgateways.throughput |

### Azure Load Balancers

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Load balancer DIP TCP availability | builtin:cloud.azure.loadbalancer.availability.dipTcp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Tcp")) / 100 |
| Load balancer DIP UDP availability | builtin:cloud.azure.loadbalancer.availability.dipUdp | Health probe status | ext:cloud.azure.microsoft\_network.loadbalancers.dipavailability:filter(eq("ProtocolType", "Udp")) / 100 |
| Load Balancer VIP availability | builtin:cloud.azure.loadbalancer.availability.vip | Data path availability | ext:cloud.azure.microsoft\_network.loadbalancers.vipavailability / 100 |
| SNAT connections successful | builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Successful")) |
| SNAT connections pending | builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Pending")) |
| SNAT connections failed | builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connection count | ext:cloud.azure.microsoft\_network.loadbalancers.snatconnectioncount:filter(eq("ConnectionState" ,"Failed")) |
| Bytes received | builtin:cloud.azure.loadbalancer.traffic.byteIn | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "In")) |
| Bytes sent | builtin:cloud.azure.loadbalancer.traffic.byteOut | Byte count | ext:cloud.azure.microsoft\_network.loadbalancers.bytecount:filter(eq("Direction", "Out")) |
| Packets received | builtin:cloud.azure.loadbalancer.traffic.packetIn | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "In")) |
| Packets sent | builtin:cloud.azure.loadbalancer.traffic.packetOut | Packet count | ext:cloud.azure.microsoft\_network.loadbalancers.packetcount:filter(eq("Direction", "Out")) |
| SYN packets received | builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "In")) |
| SYN packets sent | builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN count | ext:cloud.azure.microsoft\_network.loadbalancers.syncount:filter(eq("Direction", "Out")) |

### Azure Cache for Redis

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Cache hits | builtin:cloud.azure.redis.cache.hits | Cache hits | ext:cloud.azure.microsoft\_cache.redis.cachehits |
| Cache misses | builtin:cloud.azure.redis.cache.misses | Cache misses | ext:cloud.azure.microsoft\_cache.redis.cachemisses |
| Read bytes/s | builtin:cloud.azure.redis.cache.read | Cache read | ext:cloud.azure.microsoft\_cache.redis.cacheread |
| Write bytes/s | builtin:cloud.azure.redis.cache.write | Cache write | ext:cloud.azure.microsoft\_cache.redis.cachewrite |
| Get commands | builtin:cloud.azure.redis.commands.get | Gets | ext:cloud.azure.microsoft\_cache.redis.getcommands |
| Set commands | builtin:cloud.azure.redis.commands.set | Sets | ext:cloud.azure.microsoft\_cache.redis.setcommands |
| Total no. of processed commands | builtin:cloud.azure.redis.commands.total | Total operations | ext:cloud.azure.microsoft\_cache.redis.totalcommandsprocessed |
| No. of evicted keys | builtin:cloud.azure.redis.keys.evicted | Evicted keys | ext:cloud.azure.microsoft\_cache.redis.evictedkeys |
| No. of expired keys | builtin:cloud.azure.redis.keys.expired | Expired keys | ext:cloud.azure.microsoft\_cache.redis.expiredkeys |
| Total no. of keys | builtin:cloud.azure.redis.keys.total | Total keys | ext:cloud.azure.microsoft\_cache.redis.totalkeys |
| Used memory | builtin:cloud.azure.redis.memory.used | Used memory | ext:cloud.azure.microsoft\_cache.redis.usedmemory |
| Used memory RSS | builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | ext:cloud.azure.microsoft\_cache.redis.usedmemoryrss |
| Connected clients | builtin:cloud.azure.redis.connected | Connected clients | ext:cloud.azure.microsoft\_cache.redis.connectedclients |
| Server load | builtin:cloud.azure.redis.load | Server load | ext:cloud.azure.microsoft\_cache.redis.serverload |
| Processor time | builtin:cloud.azure.redis.processorTime | CPU | ext:cloud.azure.microsoft\_cache.redis.percentprocessortime |

### Azure Cosmos Database

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Available Storage | builtin:cloud.azure.cosmos.availableStorage | - | - |
| Data Usage | builtin:cloud.azure.cosmos.dataUsage | Data usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.datausage |
| Document Count | builtin:cloud.azure.cosmos.documentCount | Document count | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentcount |
| Document Quota | builtin:cloud.azure.cosmos.documentQuota | Document quota | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.documentquota |
| Index Usage | builtin:cloud.azure.cosmos.indexUsage | Index usage | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.indexusage |
| Metadata Requests | builtin:cloud.azure.cosmos.metadataRequests | Metadata requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.metadatarequests |
| Normalized request units consumption | builtin:cloud.azure.cosmos.normalizedRUConsumption | Normalized ru consumption | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.normalizedruconsumption |
| Provisioned Throughput | builtin:cloud.azure.cosmos.provisionedThroughput | Provisioned throughput | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.provisionedthroughput |
| Replication Latency | builtin:cloud.azure.cosmos.replicationLatency | P99 replication latency | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.replicationlatency |
| Total number of request units | builtin:cloud.azure.cosmos.requestUnits | Total request units | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequestunits |
| Total number of requests | builtin:cloud.azure.cosmos.requests | Total requests | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.totalrequests |
| Service Availability | builtin:cloud.azure.cosmos.serviceAvailability | Service availability | ext:cloud.azure.microsoft\_documentdb.databaseaccounts.serviceavailability |

### Azure Iot Hub

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Commands abandoned | builtin:cloud.azure.iotHub.command.abandoned | C2D messages abandoned | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_abandon\_success |
| Commands completed | builtin:cloud.azure.iotHub.command.completed | C2D message deliveries completed | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_complete\_success |
| Commands rejected | builtin:cloud.azure.iotHub.command.rejected | C2D messages rejected | ext:cloud.azure.microsoft\_devices.iothubs.c2d\_commands\_egress\_reject\_success |
| Connected devices | builtin:cloud.azure.iotHub.device.connected | Connected devices | ext:cloud.azure.microsoft\_devices.iothubs.connecteddevicecount |
| Number of throttling errors | builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_sendthrottle |
| Total device data usage | builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage Total device data usage (preview) | ext:cloud.azure.microsoft\_devices.iothubs.devicedatausage ext:cloud.azure.microsoft\_devices.iothubs.devicedatausagev2 |
| Total devices | builtin:cloud.azure.iotHub.device.registered | Total devices | ext:cloud.azure.microsoft\_devices.iothubs.totaldevicecount |
| Messages delivered to the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Routing - messages delivered to messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_builtin\_events |
| Message latency for the built-in endpoint (messages/events) | builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Routing - message latency for messages/events | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_builtin\_events |
| Messages delivered to Event Hub endpoints | builtin:cloud.azure.iotHub.eventHub.messages.delivered | Routing - messages delivered to event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_eventhubs |
| Message latency for event hub endpoints | builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Routing - message latency for event hub | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_eventhubs |
| Dropped messages | builtin:cloud.azure.iotHub.messages.dropped | Routing - telemetry messages dropped | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_dropped |
| Invalid messages | builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Routing - telemetry messages incompatible | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_invalid |
| Orphaned messages | builtin:cloud.azure.iotHub.messages.orphaned | Routing - telemetry messages orphaned | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_orphaned |
| Telemetry message send attempts | builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_allprotocol |
| Telemetry messages sent | builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_ingress\_success |
| Messages matching fallback condition | builtin:cloud.azure.iotHub.messages.sentToFallback | Routing - messages delivered to fallback | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_telemetry\_egress\_fallback |
| Message latency for service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Routing - message latency for service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebusqueues |
| Messages delivered to service bus queue endpoints | builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Routing - messages delivered to service bus queue | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebusqueues |
| Message latency for service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Routing - message latency for service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_servicebustopics |
| Messages delivered to service bus topic endpoints | builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Routing - messages delivered to service bus topic | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_servicebustopics |
| Message latency for storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Routing - message latency for storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_latency\_storage |
| Blobs written to storage | builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Routing - blobs delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_blobs |
| Data written to storage | builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Routing - data delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage\_bytes |
| Messages delivered to storage endpoints | builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Routing - messages delivered to storage | ext:cloud.azure.microsoft\_devices.iothubs.d2c\_endpoints\_egress\_storage |

### Azure SQL Server

#### Azure SQL Databases

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric |
| --- | --- | --- | --- |
| Blocked by firewall | builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | ext:cloud.azure.microsoft\_sql.servers.databases.blocked\_by\_firewall |
| Failed connections | builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections - system errors Failed connections - user errors | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed ext:cloud.azure.microsoft\_sql.servers.databases.connection\_failed\_user\_error |
| Successful connections | builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | ext:cloud.azure.microsoft\_sql.servers.databases.connection\_successful |
| DTU limit | builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_limit |
| DTU used | builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_used |
| DTU percentage | builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.dtu\_consumption\_percent |
| Data I/O percentage | builtin:cloud.azure.sqlDatabase.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlDatabase.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.databases.log\_write\_percent |
| Database size percentage | builtin:cloud.azure.sqlDatabase.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.databases.storage\_percent |
| Total database size | builtin:cloud.azure.sqlDatabase.storage.totalBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.databases.storage |
| In-Memory OLTP storage percent | builtin:cloud.azure.sqlDatabase.storage.xtpPercent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent | ext:cloud.azure.microsoft\_sql.servers.databases.xtp\_storage\_percent |
| CPU percentage | builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.databases.cpu\_percent |
| Deadlocks | builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | ext:cloud.azure.microsoft\_sql.servers.databases.deadlock |
| Sessions percentage | builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.databases.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlDatabase.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.databases.workers\_percent |

#### Azure SQL Database elastic pools

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Storage limit | builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Data max size | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_limit |
| Database size percentage | builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Data space used percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_percent |
| Storage used | builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Data space used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.storage\_used |
| In-memory OLTP storage percent | builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In - memory OLTP storage percent | ext:cloud.azure.microsoft\_sql.servers.elasticpools.xtp\_storage\_percent |
| DTU percentage | builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.dtu\_consumption\_percent |
| eDTU limit | builtin:cloud.azure.sqlElasticPool.edtu.limit | EDTU limit | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_limit |
| eDTU used | builtin:cloud.azure.sqlElasticPool.edtu.used | EDTU used | ext:cloud.azure.microsoft\_sql.servers.elasticpools.edtu\_used |
| Data I/O percentage | builtin:cloud.azure.sqlElasticPool.io.dataRead | Data IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.physical\_data\_read\_percent |
| Log I/O percentage | builtin:cloud.azure.sqlElasticPool.io.logWrite | Log IO percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.log\_write\_percent |
| CPU percentage | builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.cpu\_percent |
| Sessions percentage | builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.sessions\_percent |
| Workers percentage | builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | ext:cloud.azure.microsoft\_sql.servers.elasticpools.workers\_percent |

### Azure Storage Account

| Classic service metric name | Classic service metric key | Cloud service metric name | Cloud service metric key |
| --- | --- | --- | --- |
| Transactions count | builtin:cloud.azure.storage.blob.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.transactions |
| Server success latency | builtin:cloud.azure.storage.blob.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.blob.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.blob.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.ingress |
| Blob capacity | builtin:cloud.azure.storage.blob.capacity | Blob capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcapacity |
| Blob container count | builtin:cloud.azure.storage.blob.containers | Blob container count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.containercount |
| Blob count | builtin:cloud.azure.storage.blob.entities | Blob count | ext:cloud.azure.microsoft\_storage.storageaccounts.blobservices.blobcount |
| Transactions count | builtin:cloud.azure.storage.file.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.file.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.file.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.file.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.ingress |
| File capacity | builtin:cloud.azure.storage.file.capacity | File capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecapacity |
| File share count | builtin:cloud.azure.storage.file.containers | File share count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filesharecount |
| File count | builtin:cloud.azure.storage.file.entities | File count | ext:cloud.azure.microsoft\_storage.storageaccounts.fileservices.filecount |
| Transactions count | builtin:cloud.azure.storage.queue.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.transactions |
| E2E success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successe2elatency |
| Server success latency | builtin:cloud.azure.storage.queue.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.successserverlatency |
| Egress bytes | builtin:cloud.azure.storage.queue.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.queue.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.ingress |
| Queue capacity | builtin:cloud.azure.storage.queue.capacity | Queue capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecapacity |
| Queue count | builtin:cloud.azure.storage.queue.containers | Queue count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuecount |
| Queue message count | builtin:cloud.azure.storage.queue.entities | Queue message count | ext:cloud.azure.microsoft\_storage.storageaccounts.queueservices.queuemessagecount |
| Transactions count | builtin:cloud.azure.storage.table.transactions | Transactions | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.transactions |
| Server success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server | Success server latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successserverlatency |
| E2E success latency | builtin:cloud.azure.storage.table.transactions.network.latency.success.server.e2e | Success E2E latency | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.successe2elatency |
| Egress bytes | builtin:cloud.azure.storage.table.transactions.network.egress | Egress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.egress |
| Ingress bytes | builtin:cloud.azure.storage.table.transactions.network.ingress | Ingress | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.ingress |
| Table capacity | builtin:cloud.azure.storage.table.capacity | Table capacity | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecapacity |
| Table count | builtin:cloud.azure.storage.table.containers | Table count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tablecount |
| Table entity count | builtin:cloud.azure.storage.table.entities | Table entity count | ext:cloud.azure.microsoft\_storage.storageaccounts.tableservices.tableentitycount |


---


## Source: default-azure-metrics.md


---
title: Classic (formerly 'built-in') Azure metrics
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics
scraped: 2026-02-18T05:45:24.832833
---

# Classic (formerly 'built-in') Azure metrics

# Classic (formerly 'built-in') Azure metrics

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jan 29, 2024

For information about differences between classic services and other services, see [Migrate from Azure classic (formerly 'built-in') services to cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Migrate Azure classic services to their new versions.").

The table below lists all Azure metrics that Dynatrace collects by default when you enable [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") monitoring.

For all other metrics collected by Dynatrace per configurable Azure service, see [cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.") pages.

| Metric key | Name | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.azure.apiMgmt.requests.failed | Failed requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.other | Other requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.successful | Successful requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.total | Total requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.requests.unauth | Unauthorized requests | Count | autoavgcountmaxminsum |
| builtin:cloud.azure.apiMgmt.capacity | Capacity | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.apiMgmt.duration | Duration | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.healthy | Healthy host count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.pool.host.unhealthy | Unhealthy host count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.failed | Requests failed | Count | autovalue |
| builtin:cloud.azure.appGateway.backend.settings.traffic.requests.total | Requests total | Count | autovalue |
| builtin:cloud.azure.appGateway.http.status.response | Response status | Count | autovalue |
| builtin:cloud.azure.appGateway.network.connections.count | Current connections count | Count | autoavgmaxmin |
| builtin:cloud.azure.appGateway.network.throughput | Network throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.applicationQueue.requests | Requests in application queue | Count | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.execution.count | Function execution count | Count | autovalue |
| builtin:cloud.azure.appService.functions.execution.unitsCount | Function execution units count | Count | autovalue |
| builtin:cloud.azure.appService.functions.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.functions.io.operations.other | IO other operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.read | IO read operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.operations.write | IO write operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.other | IO other bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.read | IO read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.io.write | IO write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.functions.traffic.bytesReceived | Received bytes | Byte | autovalue |
| builtin:cloud.azure.appService.functions.traffic.bytesSent | Sent bytes | Byte | autovalue |
| builtin:cloud.azure.appService.http.status.http2xx | HTTP 2xx | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http403 | HTTP 403 | Count | autovalue |
| builtin:cloud.azure.appService.http.status.http5xx | HTTP 5xx | Count | autovalue |
| builtin:cloud.azure.appService.io.operations.other | IO other operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.read | IO read operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.operations.write | IO write operations/s | Per second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.other | IO other bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.read | IO read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.io.write | IO write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.appService.response.avg | Response time avg | Second | autoavgmaxmin |
| builtin:cloud.azure.appService.traffic.bytesReceived | Received bytes | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.bytesSent | Sent bytes | Byte | autovalue |
| builtin:cloud.azure.appService.traffic.requests | Requests count | Count | autovalue |
| builtin:cloud.azure.cosmos.availableStorage | Available Storage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.dataUsage | Data Usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentCount | Document Count | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.documentQuota | Document Quota | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.indexUsage | Index Usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.cosmos.metadataRequests | Metadata Requests | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.normalizedRUConsumption | Normalized request units consumption | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.cosmos.provisionedThroughput | Provisioned Throughput | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.replicationLatency | Replication Latency | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requestUnits | Total number of request units | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.requests | Total number of requests | Count | autoavgmaxmin |
| builtin:cloud.azure.cosmos.serviceAvailability | Service Availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.eventHub.capture.backlog | Capture backlog | Count | autovalue |
| builtin:cloud.azure.eventHub.capture.bytes | Captured bytes | Byte | autovalue |
| builtin:cloud.azure.eventHub.capture.msg | Captured messages | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.quotaExceeded | Quota exceeded errors | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.eventHub.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.successful | Successful requests | Count | autovalue |
| builtin:cloud.azure.eventHub.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesIn | Incoming bytes | Byte/minute | autovalue |
| builtin:cloud.azure.eventHub.traffic.bytesOut | Outgoing bytes | Byte | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgIn | Incoming messages | Count | autovalue |
| builtin:cloud.azure.eventHub.traffic.msgOut | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.eventHubNamespace.connections.active | Active connections | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.closed | Closed connections | Count | autoavgmaxmin |
| builtin:cloud.azure.eventHubNamespace.connections.opened | Opened connections | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.command.abandoned | Commands abandoned | Count | autovalue |
| builtin:cloud.azure.iotHub.command.completed | Commands completed | Count | autovalue |
| builtin:cloud.azure.iotHub.command.rejected | Commands rejected | Count | autovalue |
| builtin:cloud.azure.iotHub.device.connected | Connected devices | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.dailyThroughputThrottling | Number of throttling errors | Count | autovalue |
| builtin:cloud.azure.iotHub.device.dataUsage | Total device data usage | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.device.registered | Total devices | Count | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.messages.delivered | Messages delivered to the built-in endpoint (messages/events) | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.builtInEventHub.averageLatencyMs | Message latency for the built-in endpoint (messages/events) | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.eventHub.messages.delivered | Messages delivered to Event Hub endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.eventHub.averageLatencyMs | Message latency for event hub endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.messages.dropped | Dropped messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.invalidForAllEndpoints | Invalid messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.orphaned | Orphaned messages | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sendAttempts | Telemetry message send attempts | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sent | Telemetry messages sent | Count | autovalue |
| builtin:cloud.azure.iotHub.messages.sentToFallback | Messages matching fallback condition | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.queues.averageLatencyMs | Message latency for service bus queue endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.queues.messagesDelivered | Messages delivered to service bus queue endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.serviceBus.topics.averageLatencyMs | Message latency for service bus topic endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.serviceBus.topics.messagesDelivered | Messages delivered to service bus topic endpoints | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.avgLatencyMs | Message latency for storage endpoints | Millisecond | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.blobsWritten | Blobs written to storage | Count | autovalue |
| builtin:cloud.azure.iotHub.storageEndpoints.bytesWritten | Data written to storage | Byte | autoavgmaxmin |
| builtin:cloud.azure.iotHub.storageEndpoints.messageDelivered | Messages delivered to storage endpoints | Count | autovalue |
| builtin:cloud.azure.loadbalancer.availability.dipTcp | Load balancer DIP TCP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.dipUdp | Load balancer DIP UDP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.availability.vip | Load Balancer VIP availability | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.loadbalancer.snatConnection.est | SNAT connections successful | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.pending | SNAT connections pending | Count | autovalue |
| builtin:cloud.azure.loadbalancer.snatConnection.rej | SNAT connections failed | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteIn | Bytes received | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.byteOut | Bytes sent | Byte | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetIn | Packets received | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetOut | Packets sent | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynIn | SYN packets received | Count | autovalue |
| builtin:cloud.azure.loadbalancer.traffic.packetSynOut | SYN packets sent | Count | autovalue |
| builtin:cloud.azure.redis.cache.hits | Cache hits | Count | autovalue |
| builtin:cloud.azure.redis.cache.misses | Cache misses | Count | autovalue |
| builtin:cloud.azure.redis.cache.read | Read bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.cache.write | Write bytes/s | Byte/second | autoavgmaxmin |
| builtin:cloud.azure.redis.commands.get | Get commands | Count | autovalue |
| builtin:cloud.azure.redis.commands.set | Set commands | Count | autovalue |
| builtin:cloud.azure.redis.commands.total | Total no. of processed commands | Count | autovalue |
| builtin:cloud.azure.redis.keys.evicted | No. of evicted keys | Count | autovalue |
| builtin:cloud.azure.redis.keys.expired | No. of expired keys | Count | autovalue |
| builtin:cloud.azure.redis.keys.total | Total no. of keys | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.used | Used memory | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.memory.usedRss | Used memory RSS | Byte | autoavgmaxmin |
| builtin:cloud.azure.redis.connected | Connected clients | Count | autoavgmaxmin |
| builtin:cloud.azure.redis.load | Server load | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.redis.processorTime | Processor time | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.region.vms.initializing | Number of starting VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.running | Number of active VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.stopped | Number of stopped VMs in region | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.connections.active | Total active connections | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.count | Count of messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countActive | Count of active messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countDeadLettered | Count of dead-lettered messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.countScheduled | Count of scheduled messages | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.namespace.cpu | Service bus premium namespace CPU usage metric | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.memory | Service bus premium namespace memory usage metric | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.namespace.size | Service bus size | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.count | Count of messages in queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countActive | Count of active messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countDeadLettered | Count of dead-lettered messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.countScheduled | Count of scheduled messages in a queue | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.queue.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.queue.size | Size of an queue | Byte | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.errors.server | Server errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.errors.user | User errors | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.count | Count of messages in topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countActive | Count of active messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countDeadLettered | Count of dead-lettered messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.countScheduled | Count of scheduled messages in a topic | Count | autoavgmaxmin |
| builtin:cloud.azure.serviceBus.topic.messages.incoming | Incoming messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.messages.outgoing | Outgoing messages | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.incoming | Incoming requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.successful | Total successful requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.requests.throttled | Throttled requests | Count | autovalue |
| builtin:cloud.azure.serviceBus.topic.size | Size of a topic | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.connections.blockedByFirewall | Blocked by firewall | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.failed | Failed connections | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.connections.successful | Successful connections | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.dtu.limit.count | DTU limit | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.limit.used | DTU used | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.dtu.consumptionPerc | DTU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.totalBytes | Total database size | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.storage.xtpPercent | In-Memory OLTP storage percent | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.deadlocks | Deadlocks | Count | autovalue |
| builtin:cloud.azure.sqlDatabase.sessions | Sessions percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlDatabase.workers | Workers percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.limitBytes | Storage limit | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.percent | Database size percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.usedBytes | Storage used | Byte | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.storage.xtpPercent | In-memory OLTP storage percent | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.dtu.consumption | DTU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.limit | eDTU limit | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.edtu.used | eDTU used | Count | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.dataRead | Data I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.io.logWrite | Log I/O percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.cpuPercent | CPU percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.sessions | Sessions percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.sqlElasticPool.workers | Workers percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.read | Disk read bytes | Byte | autovalue |
| builtin:cloud.azure.vm.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.disk.write | Disk write bytes | Byte | autovalue |
| builtin:cloud.azure.vm.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vm.network.bytesIn | Network in bytes | Byte | autovalue |
| builtin:cloud.azure.vm.network.bytesOut | Network out bytes | Byte | autovalue |
| builtin:cloud.azure.vm.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.read | Disk read bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.readOps | Disk read operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.disk.write | Disk write bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.disk.writeOps | Disk write operations per sec | Per second | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.network.bytesIn | Network in bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.network.bytesOut | Network out bytes | Byte | autovalue |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Number of starting VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.running | Number of active VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Number of stopped VMs in scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.cpuUsage | Percentage CPU | Percent (%) | autoavgmaxmin |


---


## Source: limit-api-calls-to-azure.md


---
title: Limit API calls to Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure
scraped: 2026-02-18T05:47:25.647466
---

# Limit API calls to Azure

# Limit API calls to Azure

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 09, 2025

When monitoring large Azure environments (thousands of resources per Azure subscription), there is a risk that Dynatrace will reach Azure API throttling limits. Follow this guide to limit API calls to Azure and help to guarantee full Azure monitoring.

## Azure throttling limits

There are two types of Azure throttled requests that we need to take into account:

1. [Throttled requests in Resource Managerï»¿](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits)âAzure throttles subscription-level and tenant-level read operations.

   * Dynatrace uses Azure Resource Manager queries to collect built-in services and metrics for all services.
2. [Throttled requests in Azure Resource Graphï»¿](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)

   * Dynatrace uses Azure Resource Graph queries to collect all services that are not built-in.

## Dynatrace Azure anti-throttling mechanism

Dynatrace collects Azure resources and metrics every 5 min by default to avoid making API calls every minute. However, the frequency of polling depends on the Azure throttling limit.

Dynatrace calculates how many requests need to be sent to Azure during the upcoming hour. If the number of expected requests exceeds the configured throttling limit (12,000 requests/hour), Dynatrace changes the polling frequency to collect data with an interval of no more than 15 minutes.

## How to avoid Azure throttling

To provide full Dynatrace monitoring, it is important to avoid Azure throttling limits. To decrease API calls to Azure, you can do one of the following.

* Adjust the Azure service principal configuration to your environment on the Azure side.
* Limit the number of monitored resources using monitoring by tags on the Dynatrace side.

See below for details.

### Azure service principal configuration

You have three options to configure [Azure service principalï»¿](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals), depending on your Azure environment.

* Recommended One Azure service principal - one Azure subscription

  + Throttling limit: 12,000 requests/hour per Azure subscription
* One big Azure subscription that exceeds the throttling limit

  Split monitoring between Azure service principals:

  + You can create several Azure service principals for the same Azure subscription setting the `--scope` of each service principal to separate Azure resource groups.
    Copy the following command and edit it to replace the placeholders with actual values as described below.

    ```
    az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID>/resourceGroups/<YourResourceGroupID> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
    ```

    Be sure to replace the placeholders (`<...>`) with your values:

    - `<YourServicePrincipalName>` - the name of the service principal that will be created for Dynatrace to access Azure.
    - `<YourSubscriptionID>`- the name of the subscription you would like to monitor.
    - `<YourResourceGroupID>` - the name of the specific resource group you would like to monitor.
  + You can create several Azure service principals setting the `--scope` to subscription level and add multiple credentials monitoring the same Azure subscription in Dynatrace, but different services.

    For example:

    - One monitoring `Azure Virtual machines (built-in)` service
    - Another monitoring `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services`, and `Azure Storage File Services`, but not monitoring `Azure Virtual machines (built-in)`.

    Remember that the scope of monitored services needs to be different for each credential and must not be left with the default configuration. Otherwise, metric values for overlapping services might be incorrect.
* (not recommended) One Azure service principal - many Azure subscriptions

  If the first option is not suitable in your situation, configure an Azure service principal to monitor up to twenty Azure subscriptions.

  Remember that the number of API calls depends on how large your Azure subscriptions are. If you notice that the Dynatrace integration for Azure monitoring is not working correctly, consider decreasing the number of subscriptions per Azure service principal.

### Limit monitored resources using monitoring based on tags - Dynatrace configuration

If you don't need to monitor all Azure resources in your subscriptions, you can use monitoring by tags to decrease Azure API calls.

If you have a lot of subscriptions, monitoring based on tags might not be enough to avoid throttling, and you should still prepare a proper [Azure service principal configuration](#service-principal).

* Monitoring by tags mostly allows you to limit the calls for metrics and sub-resources (for example, Microsoft.ServiceBus/namespaces/queues for all resources of type Microsoft.ServiceBus/namespaces).
* Calls for top-level resources still need to be made for each subscription.

You can choose to monitor resources based on existing Azure tags, as Dynatrace automatically imports them from service instances.  
To monitor resources based on tags

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, select the **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") icon for the Azure instance.
3. Set **Resources to be monitored** to **Monitor resources selected by tags**.
4. Enter key/value pairs to identify resources to exclude from monitoring or include in monitoring.
   You can enter multiple key/value pairs: each time you enter a pair, another empty row is displayed for you to edit as needed.
5. Select **Save** to save your configuration.

   To import the Azure tags automatically into Dynatrace, turn on **Capture Azure tags automatically**.

## Related topics

* [Microsoft Azure monitoring](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")


---


## Source: set-up-metric-events-for-alerting.md


---
title: Set up metric events for alerting
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting
scraped: 2026-02-17T05:05:40.015134
---

# Set up metric events for alerting

# Set up metric events for alerting

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jan 08, 2021

After [setting up Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), you can start setting up and configuring metric events for alerting.

To configure metric events for alerting, go to **Settings** > **Cloud and virtualization** > **Azure** > **Metric events for alerting** > **Manage alerting rules**. On the **Metric events for alerting** page you can create, enable/disable, and configure recommended alerting rules.  
For an overview of all recommended alerting rules for all cloud services, see the list below.

### Predefined alerting rules per cloud service

| Name | Alerting rules |
| --- | --- |
| Azure Spring Apps | Azure Spring Apps system CPU usage (static threshold: above 95%), Azure Spring Apps process CPU usage (static threshold: above 95%). |
| Azure Blockchain Service | Azure Blockchain Service CPU usage percentage (static threshold: above 95%), Azure Blockchain Service memory usage percentage (static threshold: above 95%). |
| Azure Cache for Redis | Azure Redis memory usage % (Static threshold: above 95 %), Azure Redis CPU usage % (Static threshold: above 95 %) |
| Azure Redis (built-in) | Azure Redis CPU usage % (built-in) (Static threshold: above 95 %) |
| Azure Virtual Machine (classic) | Azure Virtual Machine (classic) percentage CPU (static threshold: above 95%). |
| Azure Storage Account (classic) | Azure Storage Account (classic) availability (static threshold: below 95%). |
| Azure Storage Blob Services (classic) | Azure Storage (classic) Blob Services availability (static threshold: below 95%). |
| Azure Storage File Services (classic) | Azure Storage (classic) File Services availability (static threshold: below 95%). |
| Azure Storage Queue Services (classic) | Azure Storage (classic) Queue Services availability (static threshold: below 95%). |
| Azure Storage Table Services (classic) | Azure Storage (classic) Table Services availability (static threshold: below 95%). |
| Azure Data Factory v2 | Azure Data Factory integration runtime CPU utilization (static threshold: above 95%). |
| Azure DB for MariaDB | Azure DB for MariaDB CPU percent (static threshold: above 95%), Azure DB for MariaDB memory percent (static threshold: above 95%), Azure DB for MariaDB IO percent (static threshold: above 95%), Azure DB for MariaDB server log storage percent (static threshold: above 95%), Azure DB for MariaDB storage percent (static threshold: above 95%). |
| Azure DB for MySQL | Azure DB for MySQL CPU percent (static threshold: above 95%), Azure DB for MySQL memory percent (static threshold: above 95%), Azure DB for MySQL IO percent (static threshold: above 95%), Azure DB for MySQL server log storage percent (static threshold: above 95%), Azure DB for MySQL storage percent (static threshold: above 95%). |
| Azure DB for PostgreSQL - Flexible Server | Azure DB for PostgreSQL (Flexible) CPU percent (Static threshold: above 95 %), Azure DB for PostgreSQL (Flexible) memory percent (Static threshold: above 95 %), Azure DB for PostgreSQL (Flexible) storage percent (Static threshold: above 95 %) |
| Azure DB for PostgreSQL - Server | Azure DB for PostgreSQL CPU percent (static threshold: above 95%), Azure DB for PostgreSQL memory percent (static threshold: above 95%), Azure DB for PostgreSQL IO percent (static threshold: above 95%), Azure DB for PostgreSQL server log storage percent (static threshold: above 95%), Azure DB for PostgreSQL storage percent (static threshold: above 95%). |
| Azure DB for PostgreSQL - Hyperscale | Azure DB for PostgreSQL CPU percent (static threshold: above 95%), Azure DB for PostgreSQL memory percent (static threshold: above 95%), Azure DB for PostgreSQL storage percent (static threshold: above 95%). |
| Azure Event Hubs Cluster | Azure Event Hubs CPU usage (static threshold: above 95%), Azure Event Hubs available memory (static threshold: below 5%). |
| Azure Application Insights | Azure Application Insights availability (static threshold: below 95%), Azure Application Insights process CPU (static threshold: above 95%), Azure Application Insights processor time (static threshold: above 95%). |
| Azure Key Vault | Azure Key Vault availability (static threshold: below 95%), Azure Key Vault saturation (static threshold: above 95%). |
| Azure Data Explorer Cluster | Azure Data Explorer Cluster cache utilization (static threshold: above 95%), Azure Data Explorer Cluster ingestion utilization (static threshold: above 95%), Azure Data Explorer Cluster CPU (static threshold: above 95%), Azure Data Explorer Cluster Export utilization (static threshold: above 95%). |
| Azure Integration Service Environment | Azure ISE run failure percentage (static threshold: above 5%), Azure ISE workflow processor usage (static threshold: above 95%), Azure ISE workflow memory usage (static threshold: above 95%). |
| Azure Logic Apps | Azure Logic Apps run failure percentage (static threshold: above 5%). |
| Azure Machine Learning Workspace | Azure Machine Learning CPU utilization (static threshold: above 95%), Azure Machine Learning GPU utilization (static threshold: above 95%), Azure Machine Learning quota utilization percentage (static threshold: above 95%). |
| Azure Maps Account | Azure Maps Account availability (static threshold: below 95%). |
| Azure Application Gateway (built-in) | Azure Application Gateway unhealthy hosts (built-in) (Static threshold: above 0 ), Azure Application Gateway failed requests (built-in) (Auto-adaptive baseline) |
| Azure Application Gateway | Azure Application Gateway unhealthy hosts count (Static threshold: above 0 ), Azure Application Gateway failed requests (Auto-adaptive baseline) |
| Azure Firewall | Azure Firewall health state (static threshold: below 95%), Azure Firewall SNAT port utilization (static threshold: above 95%). |
| Azure ExpressRoute Circuit | Azure ExpressRoute Circuit BGP availability (static threshold: below 95%), Azure ExpressRoute Circuit ARP availability (static threshold: below 95%). |
| Azure Front Door | Azure Front Door backend health percentage (static threshold: below 95%). |
| Azure Connection Monitors | Azure NetworkWatchers probes failed percent (static threshold: above 5%). |
| Azure Connection Monitors Preview | Azure NetworkWatchers probes failed percent (static threshold: above 5%), Azure NetworkWatchers checks failed percent (static threshold: above 5%). |
| Azure Public IP Address | Azure Public IP Address data path availability (static threshold: below 95%). |
| Azure Power BI Embedded | Azure Power BI embedded memory thrashing (datasets) (static threshold: above 95%). |
| Azure Search Service | Azure Search Service throttled search queries (static threshold: above 5%). |
| Azure Mesh Application | Azure Mesh Application CPU utilization (static threshold: above 95%), Azure Mesh Application memory utilization (static threshold: above 95%). |
| Azure SignalR | Azure SignalR user errors (static threshold: above 5%), Azure SignalR system errors (static threshold: above 5%). |
| Azure SQL (built-in) | Azure SQL Database CPU usage % (built-in) (Static threshold: above 95 %), Azure SQL Database used data space (built-in) (Static threshold: above 95 %) |
| Azure SQL Managed Instance | Azure SQL Managed Instance CPU usage (static threshold: above 95%). |
| Azure SQL Data Warehouse (legacy) | Azure SQL Data Warehouse CPU usage percentage (static threshold: above 95%), Azure SQL Data Warehouse memory percentage (static threshold: above 95%), Azure SQL Data Warehouse Data IO percentage (static threshold: above 95%), Azure SQL Data Warehouse DWU percentage (static threshold: above 95%). |
| Azure SQL Database (DTU) | Azure SQL Database CPU usage % (Static threshold: above 95 %), Azure SQL Database used data space (Static threshold: above 95 %) |
| Azure SQL Database - Hyperscale | Azure SQL Hyperscale Database CPU usage percentage (static threshold: above 95%), Azure SQL Hyperscale server process core percent (static threshold: above 95%), Azure SQL Hyperscale server process memory percent (static threshold: above 95%), Azure SQL Hyperscale Database Sessions percentage (static threshold: above 95%), Azure SQL Hyperscale Database Data IO percentage (static threshold: above 95%), Azure SQL Hyperscale Database Log IO percentage (static threshold: above 95%), Azure SQL Hyperscale Database In - memory OLTP storage percent (static threshold: above 95%), Azure SQL Hyperscale Database Workers percentage (static threshold: above 95%). |
| Azure SQL Database (vCore) | Azure SQL Database CPU usage % (Static threshold: above 95 %), Azure SQL Database used data space (Static threshold: above 95 %) |
| Azure Stream Analytics Job | Azure Stream Analytics job resource utilization (static threshold: above 95%). |
| Azure SQL Pool | Azure Analytics Services DWU used percentage (static threshold: above 95%), Azure Analytics Services Local tempdb used percentage (static threshold: above 95%), Azure Analytics Services memory used percentage (static threshold: above 95%), Azure Analytics Services workload group allocation by system percent (static threshold: above 95%), Azure Analytics Services workload group allocation by max resource percent (static threshold: above 95%). |
| Azure App Service Environment v2 | Azure App Service Environment CPU percentage (static threshold: above 95%), Azure App Service Environment memory percentage (static threshold: above 95%) |
| Azure App Service Plan | Azure App Service CPU percentage (static threshold: above 95%), Azure App Service memory percentage (static threshold: above 95%). |
| Azure API Management Service | Api Management capacity (Static threshold: above 95 %) |
| Azure Storage Blob Services | Azure Storage Blob Services availability (Static threshold: below 95%) |
| Azure Storage File Services | Azure Storage File Services availability (Static threshold: below 95%) |
| Azure Storage Queue Services | Azure Storage Queue Services availability (Static threshold: below 95%) |
| Azure Storage Table Services | Azure Storage Table Services availability (Static threshold: below 95%) |
| Azure Storage Account | Azure Storage Account availability (Static threshold: below 95 %) |

## Add a service to monitoring

The number of recommended alerting rules depends on the number of your monitored cloud services.  
To add recommended alerting rules for a new cloud service, you first need to add the new service to monitoring.

To add a service to monitoring,

1. Go to **Settings**.
2. In **Cloud and virtualization**, select **Azure**.
3. On the Azure overview page, select **Edit** for the desired Azure instance.
4. Go to **Services** and select **Add service**, choose the desired service name from the list, and select **Add service**.
5. Select **Save changes**.

![Add azure service](https://dt-cdn.net/images/configuration-of-supporting-service-add-service-1690-2482af29eb.png)

Not all cloud services have their own predefined alerting rules.

## Create and enable alerting rules

Not applicable to new Dynatrace environments created after January 26, 2026.

To enable recommended alerting rules, you first need to create them. You can create alerting rules and automatically enable them, or (if you clear **Automatically enable created rules**) create them and manually enable them after possible configuration changes.

![Create alerting rules](https://dt-cdn.net/images/2020-11-30-11-56-33-1079-923b3ef77f.png)

For example, you can create and automatically enable a first batch of alerts. When you start monitoring new services, you can create alerts for these new services without automatically enabling them (because you want to configure them first).

## Configure alerting rules

Not applicable to new Dynatrace environments created after January 26, 2026.

How you edit rules depends on whether you chose to automatically enable alerts.

* If you chose to automatically enable alerts when creating them, go to **Adjust recommended alerting rules**, expand **Enabled recommended alerting rules**, and select any rule. This takes you to **Edit custom event for alerting**, where you can change the configuration rules for that specific service.

![Conf alerts 2](https://dt-cdn.net/images/2020-12-01-15-40-01-1011-3206a4bdc7.png)

* If you didn't choose to automatically enable alerts when creating them, go to **Enable recommended alerting rules**, expand **Disabled recommended alerting rules**, and select any of the disabled rules. This takes you to the same **Edit custom event for alerting** page.

![Enable rules](https://dt-cdn.net/images/2020-12-02-08-08-59-1076-1e07d04c6d.png)

## Disable alerting rules

Not applicable to new Dynatrace environments created after January 26, 2026.

You can disable all alerting rules, or disable or delete them selectively.

![Custom alerts](https://dt-cdn.net/images/2020-12-01-14-08-02-1106-a6cabbaddc.png)

* To disable all alerting rules, go to **Adjust recommended alerting rules** and select **Disable all enabled recommended alerting rules**.
* To disable or delete alerting rules selectively, go to **Adjust recommended alerting rules** and select **Metric events**. On the **Metric events** page, you can disable an alert by turning it off in the **On/Off** column, or you can delete it by selecting `x` in the **Delete** column.

![Custom events](https://dt-cdn.net/images/2020-11-30-12-57-44-1098-1e38daa33f.png)

If you disable any or all of the alerting rules, you can always re-enable them.

![Enable rules](https://dt-cdn.net/images/2020-11-30-19-21-05-1110-6b33994c7a.png)

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")


---


## Source: set-up-monitoring-with-azure-alerts.md


---
title: Set up monitoring notifications with Azure Monitor alerts
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts
scraped: 2026-02-17T05:12:49.156842
---

# Set up monitoring notifications with Azure Monitor alerts

# Set up monitoring notifications with Azure Monitor alerts

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 28, 2026

After [setting up Azure Monitor integration](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), you can start setting up monitoring notifications with Azure Monitor alerts.

Azure Monitor alerts is a unified notification hub for all types of important conditions found in Azure monitoring data. The integration of Azure Monitor alerts enables you to consume alerts, which are automatically transformed into events that are leveraged by Dynatrace Intelligence for deeper insights.

To set up monitoring notifications with Azure Monitor alerts, complete the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an API token**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-1 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure one or more designated ActiveGates**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-2 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure Azure Monitor alerts via webhook**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-3 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")

## Step 1 Create an API token

To generate an API token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Find and select the **Ingest metrics** scope.
5. Select **Generate token**.
6. Select **Copy** to copy the generated token to the clipboard. Store the token in a password manager for future use.

You can assign multiple permissions to a single token, or you can generate several tokens, each with different access levels, and use them accordingly. Check your organization's security policies for best practices.

## Step 2 Configure one or more designated ActiveGates

The ActiveGate designated to consume Azure Monitor alerts doesnât have to be the same ActiveGate that runs the Azure Monitor integration. It can be any other [Azure monitoring-enabled ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.").

To configure a designated ActiveGate to consume Azure Monitor alerts:

1. Configure a valid TLS certificate (not a self-signed certificate) for the ActiveGate to communicate via HTTPS. Ensure that the root certificate is accepted by Azure. For details, see [how to configure custom SSL certificate for an ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").
2. Add the following lines to your ActiveGate `custom.properties` file and restart the ActiveGate after applying the configuration.

   ```
   [azure_monitoring]



   event_servlet = true
   ```
3. Give access to ActiveGate for Azure Monitor alerts source IP addresses.

For more details, see [source IP address rangesï»¿](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) in Azure documentation.

## Step 3 Configure Azure Monitor alerts via webhook

Currently, the events/alerts ingested via Azure Monitor alerts webhook donât consume DDUsâalthough, it might change in the future.

Azure Monitor alerts consumed via webhooks are configured in your Azure Alert Rules.
The alerts are mapped to the closest known matching entity. This means that they either map to their related Azure resource entity or, as a fallback, to the Azure subscription of the resource.

To configure Azure Monitor alerts via webhook, you need to create an alert rule and an action group that will trigger a webhook.

1. In Azure Portal, go to **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.
2. Select **Scope** > **Select scope**.
3. Filter for and select the resource you want to monitor, and then select **Done**.
4. Select **Condition** > **Add condition**.
5. Filter for, select, and customize the signal type that will trigger your alert.
6. Select **Next: Actions** > **Create action group**.
7. Enter the **subscription** that will manage the deployed resources and costs, the **resource group** to which the subscription belongs, and the name (and display name) for the **action group**.
8. Select **Actions** and enter the following values:

   * For **Action type**, select **Webhook** and enter a name.
   * For **URI**, enter `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` and `<YOUR_API_TOKEN>` with your own values.
9. Leave the common alert schema disabled, and then select **OK**.

The common alert schema is not supported.

10. Select **Review and create** > **Create**.

After the action group is created, you can view and edit it in **Alerts** > **Action groups**.

For more information, see [Webhook rules in Azure documentationï»¿](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).

## Alert types

The following alert types are supported.

### Metric alerts

Metric alerts are complementary to Dynatrace integration of Azure Monitor metrics.

Metric alerts enable you to retrieve metric-based events without the need to push the metrics to Dynatrace. This is helpful in reducing API and network pressure, especially in cases where you might not need the metric (for example, for charting purposes).

The event type is defined based on alert **Severity**:

* **Sev-0 (Critical)**: `ERROR_EVENT`
* **Sev-1 (Error)**: `PERFORMANCE_EVENT`
* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`
* **Default (Informational)**: `CUSTOM_ANNOTATION`

### Activity log alerts

Dynatrace supports three types of activity notifications.

#### Activity log resource health

The event type is defined based on severity **Level**:

* **Critical**: `AVAILABILITY_EVENT`
* **Error**: `AVAILABILITY_EVENT`
* **Default**: `CUSTOM_ANNOTATION`

See [Configure resource health alerts using Azure portalï»¿](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) in Azure documentation for more information.

#### Activity log service health

The event type is defined based on **IncidentType**

* Case **ActionRequired**: `ERROR_EVENT`
* Case **Incident** or **Security**:

  + Level **Error**: `ERROR_EVENT`
  + Level **Info** or **Warning**: `CUSTOM_ANNOTATION`
* Case **Maintenance** or **Information**: `CUSTOM_ANNOTATION`

Root cause analysis

Events with `Properties.stage=RCA` are skipped. We don't support stage RCA for service health.

See [Create activity log alerts on service notifications using the Azure portalï»¿](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) in Azure documentation for more information.

#### Activity log administrative

* **Default**: `CUSTOM_ANNOTATION`

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Event categories](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")


---


## Source: tags-and-management-zones-azure.md


---
title: Tags and management zones for Azure integration
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/tags-and-management-zones-azure
scraped: 2026-02-18T05:54:10.338907
---

# Tags and management zones for Azure integration

# Tags and management zones for Azure integration

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Oct 14, 2024

To organize cloud entities in your environment and simplify searches for them, you can use tags and basic instance properties imported from the cloud, as well as tags and management zones assigned in Dynatrace. Tags and management zones are applied to cloud entities just as they are for other entities, but they are best applied via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Cloud entities in your environment

You can browse all cloud entites in your environment using their ID or type from [cloud entity types](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Monitor Azure services with Dynatrace and view available metrics.") via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."), just as for other entities. You can also explore all available properties and relationships available for each individual resource or type.

You can also browse their metrics using entity selector as part of [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."), e.g. in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

Cloud entity types

To learn more about Dynatrace cloud entities and to check which ones can have tags imported from the cloud, see [Cloud services with their respective Dynatrace entity types](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Monitor Azure services with Dynatrace and view available metrics.").

## Add an automatically applied tag to cloud entities

Follow the steps below to automatically apply a tag to cloud entities. To learn more about tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

1. Go to **Settings** > **Tags** > **Automatically applied tags**.
2. Select **Create tag** and type a name for the new tag in the **Tag name** field.
3. Select **Add a new rule**.
4. Optional **Optional tag value**. This value appears next to the tag name that the rule is specified for, after a `:`, and is used to provide more precise information based on the individual rule. Note that for rules based on the entity selector, this value cannot be extracted from the entity itself using placeholders.
5. From the **Rule type** list, choose the **Entity selector** type.
6. Use one of the code snippets from the [examples](#entity-selector-examples) and adapt it with your own values to apply tags to cloud entities matching your [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").
7. Select **Preview** to verify the results returned by the specific entity selector.
8. Select **Save changes**.

Example of a rule-based entity selector

![Queue entity selector](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Add cloud entities to existing management zones

Follow the steps below to add cloud entities to existing management zones. To learn more about management zones, see [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.").

1. Go to **Settings** > **Preferences** > **Management zones**.
2. Edit an existing management zone and select **Add a new rule**.
3. In the **Rule applies to** list, choose the **Entity selector**.
4. Use one of the code snippets from the [examples](#entity-selector-examples) and adapt it with your own values to add to the management zone cloud entities matching the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints.").
5. Select **Preview** to verify the results returned by the specific entity selector.
6. Select **Save changes**.

Example of a management zone based on the entity selector

![Management zone for queues](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Entity selector examples for Azure entities

You can use the examples below and [cloud entity types](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Monitor Azure services with Dynatrace and view available metrics.") to suit your own needs.

Regions

Resource groups

Subscriptions

Tags

Other properties

Non-built-in cloud services types

```
type(CUSTOM_DEVICE), customDeviceSource("AZURE"), customProperties("Region:South Africa North")
```

```
type(CUSTOM_DEVICE), customDeviceSource("AZURE"), not(customProperties("Region:South Africa North"))
```

```
type(cloud:azure:batch:account), customDeviceSource("AZURE"), customProperties("Region:South Africa North")
```

Built-in cloud service types

```
type(AZURE_STORAGE_ACCOUNT), toRelationship.isSiteOf(type(AZURE_REGION), entityName(northeurope))
```

Non-built-in cloud services types

```
type(CUSTOM_DEVICE),customProperties("Resource group:test-rg3")
```

```
type(cloud:azure:batch:account),customProperties("Resource group:test-rg3")
```

Built-in cloud service types

```
type(AZURE_STORAGE_ACCOUNT), azureResourceGroupName("cloud-test-rg-westeurope")
```

Non-built-in cloud services types

```
type(CUSTOM_DEVICE),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

```
type(CUSTOM_DEVICE),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),azureSubscriptionUuid("d1234e5f-de67-4db2-ad02-d89d2a1234f5"))
```

```
type(cloud:azure:batch:account),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

Built-in cloud service types

```
type(AZURE_STORAGE_ACCOUNT),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

```
type(AZURE_STORAGE_ACCOUNT),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),azureSubscriptionUuid("d1234e5f-de67-4db2-ad02-d89d2a1234f5"))
```

Non-built-in cloud services

```
type(CUSTOM_DEVICE),tag([AZURE]environment:DEV)
```

```
type(CUSTOM_DEVICE),tag([AZURE]owner:TeamA)
```

Non-built-in cloud service - specific service type

```
type(cloud:azure:batch:account),tag([AZURE]environment:DEV)
```

Built-in cloud services

```
type(AZURE_STORAGE_ACCOUNT),tag([AZURE]environment:DEV)
```

```
type(AZURE_VM),tag([AZURE]owner:TeamA)
```

Tags on parent resource for Azure service that doesn't have tags itself

```
type(AZURE_SERVICE_BUS_TOPIC), toRelationship.isAzrServiceBusNamespaceOfQueue(type(AZURE_SERVICE_BUS_NAMESPACE),tag("[Azure]tagOnParent:valueOnParent"))
```

Non-built-in cloud services

```
type(CUSTOM_DEVICE),customProperties("Resource group:new-resources")
```

```
type(CUSTOM_DEVICE),customDeviceSource("AZURE"),dnsNames(ademotestlab.file.core.windows.net)
```

```
type(CUSTOM_DEVICE),customDeviceSource("AZURE"), ipAddress(172.0.0.202)
```

Non-built-in cloud service - specific service type

```
type(cloud:azure:storage:storageaccounts:file),customProperties("Resource group:new-resources")
```

```
type(cloud:azure:storage:storageaccounts:file),dnsNames(ademodevtestlab5563.file.core.windows.net)
```

```
type("cloud:azure:network:loadbalancers:standard"),ipAddress(10.237.0.223)
```

```
type(cloud:azure:storage:storageaccounts),not(customProperties.exists("Secondary region"))
```

```
type(cloud:azure:storage:storageaccounts:file),customProperties("Status of primary region:available")
```

Built-in cloud services

```
type(AZURE_STORAGE_ACCOUNT), azureStorageAccountSecondaryRegion.exists()
```

```
type(AZURE_STORAGE_ACCOUNT), dnsNames("csb10030000ab28bff8.blob.core.windows.net")
```

```
type(AZURE_SERVICE_BUS_TOPIC), azureServiceBusMaxSizeMb("1024")
```

VMs

Functions

Services

Process groups and hosts

```
type("AZURE_VM"), dnsNames("ag-vm.eastus.cloudapp.azure.com")
```

Azure VMs with OneAgent installed

```
type("AZURE_VM"), toRelationship.runsOn(type(HOST))
```

Azure VMs without OneAgent installed

```
type("AZURE_VM"), not(toRelationship.runsOn(type(HOST)))
```

Azure Functions running on App Service Plan with OneAgent site extension installed

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(HOST))
```

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP_INSTANCE))
```

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP))
```

Azure Functions running on App Service Plan without OneAgent Site extension installed

```
type("AZURE_FUNCTION_APP"),not(sku("Dynamic")),not(fromRelationships.isPgAppOf(type(HOST)))
```

```
type("AZURE_FUNCTION_APP"),sku("Standard"),not(fromRelationships.isPgAppOf(type(HOST)))
```

Azure Functions instrumented with Dynatrace OpenTelemetry libraries (ODIN)

```
type(AZURE_FUNCTION_APP), toRelationship.runsOn(type("SERVICE"))
```

Azure Functions running on Consumption Plan instrumented with Dynatrace OpenTelemetry libraries (ODIN)

```
type(AZURE_FUNCTION_APP), sku("Dynamic"), toRelationship.runsOn(type("SERVICE"))
```

Azure Functions running on Consumption Plan not instrumented with Dynatrace OpenTelemetry libraries (ODIN)

```
type(AZURE_FUNCTION_APP), sku("Dynamic"), not(toRelationship.runsOn(type("SERVICE")))
```

App Services with OneAgent installed

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(HOST))
```

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP_INSTANCE))
```

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP))
```

App Services without OneAgent installed

```
type("AZURE_WEB_APP"),not(fromRelationships.isPgAppOf(type(HOST)))
```

Services which are also monitored by Azure integrationâfor Function Apps on App Service Plan

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP)))
```

```
type(SERVICE), fromRelationships.runsOn(type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnProcessGroupInstance(type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),tag("[Azure]environment:DEV")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription"))))
```

Services which are also monitored by Azure integrationâfor Function Apps instrumented with Dynatrace OpenTelemetry libraries (ODIN)

```
type(SERVICE), fromRelationship.runsOn(type("AZURE_FUNCTION_APP"))
```

Services which are also monitored by Azure integrationâfor Function Apps running on Consumption Plan instrumented with Dynatrace OpenTelemetry libraries (ODIN)

```
type(SERVICE), fromRelationship.runsOn(type("AZURE_FUNCTION_APP"), sku("Dynamic"))
```

Services which are also monitored by Azure integrationâfor Web Apps

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP)))
```

```
type(SERVICE), fromRelationships.runsOn(type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnProcessGroupInstance(type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP),tag("[Azure]environment:DEV")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription"))))
```

Process groups and hosts also monitored by Azure integration

```
type(HOST), fromRelationships.runsOn(type(AZURE_VM),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

## Related topics

* [Management zones](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Queue tags and management zones](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Automatically apply tags to queues and organize them into management zones.")
* [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")
* [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Infrastructure Observability](/docs/observe/infrastructure-observability "The application infrastructure, including cloud and container platforms, that Dynatrace can monitor")


---


## Source: troubleshoot-azure-monitoring-setup.md


---
title: Troubleshooting Azure monitoring setup
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/troubleshoot-azure-monitoring-setup
scraped: 2026-02-18T05:45:22.774337
---

# Troubleshooting Azure monitoring setup

# Troubleshooting Azure monitoring setup

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Mar 01, 2023

This page presents common troubleshooting scenarios for Azure monitoring setup.

* [Why don't I see metric data in my Azure monitoring setup?ï»¿](https://dt-url.net/ry038d4)
* [I don't know how to connect through proxyï»¿](https://dt-url.net/th238qi)
* [What if I have more than one ActiveGate?ï»¿](https://dt-url.net/wa0386g)
* [Timeframe comparison: Custom timeframe versus Last Xï»¿](https://dt-url.net/7j438f0)
* [What are the differences between built-in services and other services?ï»¿](https://dt-url.net/qf638eh)


---


## Source: azure-monitoring-guide.md


---
title: Monitor Azure services with Azure Monitor metrics
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide
scraped: 2026-02-18T05:39:33.713837
---

# Monitor Azure services with Azure Monitor metrics

# Monitor Azure services with Azure Monitor metrics

* Latest Dynatrace
* How-to guide
* 13-min read
* Updated on Jan 28, 2026

Follow this guide to start ingesting data remotely from Azure Monitor.

This guide focuses on infrastructure monitoring of Azure services, specifically the monitoring of Azure cloud services via Azure Monitor. See [What's next](#next) for Full-Stack and Log Monitoring of your Azure services.

Alternatively, you can configure your Dynatrace SaaS environment using [Azure Marketplace](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.").

After you established the initial monitoring, you can add, remove, or modify service monitoring the Dynatrace web UI or, at scale, with the Dynatrace API.

Details of collected measurements

To learn the measurements collected for each of the Azure services, see:

* [Azure cloud services enabled by default and metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.")
* [Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.")

The infrastructure monitoring of Azure services provides metrics from Azure Monitor and infrastructure data available via public Azure API. The data is collected in five-minute intervals.

## Cost of monitoring

Factors that contribute to the cost of monitoring Azure with Dynatrace via Azure Monitor:

* Each service monitored by Dynatrace through Azure Monitor, as well as log processing and analysis, causes the consumption of [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").
* Microsoft may charge you extra for Azure Monitor metric queries if you exceed 1 million API calls monthly. For the details on these additional costs, please consult [Microsoft online documentationï»¿](https://dt-url.net/ie03w85).
* For details regarding the metric ingest costs, see [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Monitoring prerequisites

There are three prerequisites for Azure monitoring setup:

Dynatrace admin permissions

To manage Azure monitoring configuration, you need the **Change monitoring settings** permission in Dynatrace. You can **Change monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment or management-zone level.

ActiveGate capable of Azure monitoring

To monitor Azure services, Dynatrace needs to connect to the Azure Monitor API and query it every 5 minutes. At least one ActiveGate needs to be able to connect to Azure Monitor to perform the monitoring tasks.

To check for the existence of a suitable ActiveGate

1. Go to **Deployment Status** > **ActiveGates**.
2. Set a filter for `With modules: Azure`.

   * If the resulting list is empty, you need to add at least one ActiveGate with the cloud monitoring module enabled
   * If the list is not empty, you are ready to activate Azure monitoring

To add an ActiveGate that is capable of cloud monitoring, follow the [ActiveGate installation guide](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") and resume this guide when done.

#### Allow ActiveGate to access Azure URLs

The integration accesses the following Azure API endpoints, so they must be accessible from your ActiveGate:

```
https://management.azure.com/
```

```
https://login.microsoftonline.com/
```

```
https://management.core.windows.net/
```

Proxy

The most frequent cause of certificate issues with TLS interception proxy is a missing proxy's CA certificate in ActiveGate truststore.
If you're still having proxy issues, see:

* [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.")
* [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.")
* [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.")

"Communication error."

Make sure that the URLs are whitelisted. Otherwise, you might get communication or timeout errors.

Azure roles and permissions

To perform these steps, you need to have Azure admin privileges.

Azure monitoring is performed remotely via Azure Monitor APIs that are created and exposed by Microsoft. Dynatrace needs to be able to access these APIs, so you need to configure Azure to allow for such access. You need the following:

* Sufficient permissions to register an application with your Azure AD tenant and assign the application to a role in your Azure subscription
* An Azure [service principalï»¿](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) to access Azure APIs

For Dynatrace to monitor your services, you need at least reader permissions. The steps below describe adding the service principal reader permissions and refer to a common, single-tenant access approach. Before that, we recommend getting familiar with our recommendations regarding [how to configure Azure service principal to avoid Azure throttling limits](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure#service-principal "Guide how to limit Azure API calls to avoid throttling limits").

Dynatrace integration for Azure supports **Azure Lighthouse**, which allows Dynatrace to have multi-tenant access to Azure.

1. Go to your [Azure CLI 2.0ï»¿](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) terminal.
2. Run the following command to list all the subscriptions so that you can select the one you want to add permissions for.

   ```
   az account list --output table
   ```
3. Copy the following command and edit it to replace the placeholders with actual values as described below.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Be sure to replace the placeholders (`<...>`) with your values:

   * `<YourServicePrincipalName>` - a name of the service principal that will be created for Dynatrace to access Azure
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>` - names of subscriptions listed in the previous step to which you want Dynatrace to have access.
4. Run the edited command.
5. Copy the credentials that are output from the command and save them for later.

#### Other options for required permissions

Create custom role via Azure CLI 2.0

Another way to get reader permission is to create a custom role for Dynatrace with a predefined set of permissions for fine-grained control.

1. Create a custom role by following the [Microsoft guideï»¿](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli#create-a-custom-role). You can use the following JSON template as a base for the permissions:

   ```
   {



   "properties": {



   "roleName": "dynatrace-monitoring-role",



   "description": "",



   "assignableScopes": [],



   "permissions": [



   {



   "actions": [



   "Microsoft.AVS/*/read",



   "Microsoft.Aadiam/*/read",



   "Microsoft.AnalysisServices/*/read",



   "Microsoft.ApiManagement/*/read",



   "Microsoft.App/*/read",



   "Microsoft.AppConfiguration/*/read",



   "Microsoft.AppPlatform/*/read",



   "Microsoft.Automation/*/read",



   "Microsoft.Batch/*/read",



   "Microsoft.Blockchain/*/read",



   "Microsoft.BotService/*/read",



   "Microsoft.Cache/*/read",



   "Microsoft.Cdn/*/read",



   "Microsoft.ClassicCompute/*/read",



   "Microsoft.ClassicStorage/*/read",



   "Microsoft.CognitiveServices/*/read",



   "Microsoft.Compute/*/read",



   "Microsoft.ContainerInstance/*/read",



   "Microsoft.ContainerRegistry/*/read",



   "Microsoft.ContainerService/*/read",



   "Microsoft.CustomProviders/*/read",



   "Microsoft.DBforMariaDB/*/read",



   "Microsoft.DBforMySQL/*/read",



   "Microsoft.DBforPostgreSQL/*/read",



   "Microsoft.DataBoxEdge/*/read",



   "Microsoft.DataCollaboration/*/read",



   "Microsoft.DataFactory/*/read",



   "Microsoft.DataLakeAnalytics/*/read",



   "Microsoft.DataLakeStore/*/read",



   "Microsoft.DataShare/*/read",



   "Microsoft.Devices/*/read",



   "Microsoft.DigitalTwins/*/read",



   "Microsoft.DocumentDB/*/read",



   "Microsoft.EnterpriseKnowledgeGraph/*/read",



   "Microsoft.EventGrid/*/read",



   "Microsoft.EventHub/*/read",



   "Microsoft.HDInsight/*/read",



   "Microsoft.HealthcareApis/*/read",



   "Microsoft.Insights/*/read",



   "Microsoft.IoTCentral/*/read",



   "Microsoft.KeyVault/*/read",



   "Microsoft.Kusto/*/read",



   "Microsoft.Logic/*/read",



   "Microsoft.MachineLearningServices/*/read",



   "Microsoft.Management/*/read/",



   "Microsoft.Maps/*/read",



   "Microsoft.Media/*/read",



   "Microsoft.MixedReality/*/read",



   "Microsoft.NetApp/*/read",



   "Microsoft.Network/*/read",



   "Microsoft.NotificationHubs/*/read",



   "Microsoft.OperationalInsights/*/read",



   "Microsoft.Peering/*/read",



   "Microsoft.PowerBIDedicated/*/read",



   "Microsoft.ProjectBabylon/*/read",



   "Microsoft.Purview/*/read",



   "Microsoft.RecoveryServices/*/read",



   "Microsoft.Relay/*/read",



   "Microsoft.ResourceGraph/*/read/",



   "Microsoft.Search/*/read",



   "Microsoft.SecurityDetonation/*/read",



   "Microsoft.ServiceBus/*/read",



   "Microsoft.ServiceFabricMesh/*/read",



   "Microsoft.SignalRService/*/read",



   "Microsoft.Sql/*/read",



   "Microsoft.StorageCache/*/read",



   "Microsoft.StreamAnalytics/*/read",



   "Microsoft.Synapse/*/read",



   "Microsoft.TimeSeriesInsights/*/read",



   "Microsoft.VMwareCloudSimple/*/read",



   "Microsoft.storagesync/*/read",



   "Microsoft.web/*/read"



   ],



   "notActions": [],



   "dataActions": [],



   "notDataActions": []



   }



   ]



   }



   }
   ```
2. Go to your [Azure CLI 2.0ï»¿](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) terminal.
3. Run the following command to list all the subscriptions so you can select the one for which you want to add permissions.

   ```
   az account list --output table
   ```
4. Copy the following command and edit it to replace the placeholders with actual values as described below.

   ```
   az ad sp create-for-rbac --name <YourServicePrincipalName> --role <YourCustomRole> --scopes /subscriptions/<YourSubscriptionID1> /subscriptions/<YourSubscriptionID2> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
   ```

   Replace the placeholders (`<...>`) with your values:

   * `<YourServicePrincipalName>` - the name of the service principal that will be created for Dynatrace to access Azure
   * `<YourCustomRole>` - the name of the role you have created for Dynatrace
   * `<YourSubscriptionID1>`, `<YourSubscriptionID2>` - names of subscriptions listed in the previous step (subscriptions that you want Dynatrace to have access to)
5. Run the edited command.
6. Copy the credentials that are output from the command and save them for later.

Create service principal via Azure Portal

To create a service principal in Azure Portal, you must register your application in the Microsoft Entra ID and grant access permissions for your service principal.

To register your application

1. Go to the Azure Management Portal and select **Microsoft Entra ID**.
2. Copy the value of **Tenant ID** and save it as `Tenant ID` for future retrieval. This is required to [configure Dynatrace to connect to your Azure account](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide#azureconfig-connect "Set up and configure Azure monitoring in Dynatrace.").
3. Select **App registrations** in the navigation pane of the selected Active Directory.
4. Select **New registration** at the top of the App registrations blade and type the name of your application.
5. Leave all other settings with their default values and select **Register**.
6. Copy the value of **Application (client) ID** and save it as `Client ID` for future retrieval.
7. Select **Certificates & secrets** > **New client secret** to create a new security key.
8. Enter a key description, choose the desired key duration, and then select **Add** to save the new key.
9. Copy the value of **Value** and save it as `Secret Key` for future retrieval.

   You can't retrieve the key value after you leave the **Key** blade.

To grant access permissions for your service principal

1. In Azure Portal, select **All services** > **General** > **Subscriptions**.
2. On the **Subscriptions** page, select your subscription and then select **Access control (IAM)**.

Setup if you assign reader permissions

Setup if you create a custom role

1. Select **Add role assignment** and select **Reader**.
2. Select **Next**.
3. In **Members**, enter the following data:

   * For **Assign access to**, select `User`, `group`, or `service principal`.
   * For **Members**, select **Select members** and then select your service principal from the list on the left.
4. Select **Next**, and then select **Review + assign**.

1. In **Add custom role**, select **Add**.
2. In **Basics**, enter a role name and then select **Start from scratch**.
3. In **JSON**, you can use the template below as a base for the permissions you can choose from.

   ```
   {



   "properties": {



   "roleName": "dynatrace-monitoring-role",



   "description": "",



   "assignableScopes": [],



   "permissions": [



   {



   "actions": [



   "Microsoft.Aadiam/*/read",



   "Microsoft.AnalysisServices/*/read",



   "Microsoft.ApiManagement/*/read",



   "Microsoft.Automation/*/read",



   "Microsoft.Batch/*/read",



   "Microsoft.BotService/*/read",



   "Microsoft.Cache/*/read",



   "Microsoft.Cdn/*/read",



   "Microsoft.ClassicCompute/*/read",



   "Microsoft.ClassicStorage/*/read",



   "Microsoft.CognitiveServices/*/read",



   "Microsoft.Compute/*/read",



   "Microsoft.ContainerInstance/*/read",



   "Microsoft.ContainerRegistry/*/read",



   "Microsoft.ContainerService/*/read",



   "Microsoft.DataFactory/*/read",



   "Microsoft.DataLakeAnalytics/*/read",



   "Microsoft.DataLakeStore/*/read",



   "Microsoft.DBforMySQL/*/read",



   "Microsoft.DBforPostgreSQL/*/read",



   "Microsoft.Devices/*/read",



   "Microsoft.DocumentDB/*/read",



   "Microsoft.EventGrid/*/read",



   "Microsoft.EventHub/*/read",



   "Microsoft.HDInsight/*/read",



   "Microsoft.Insights/*/read",



   "Microsoft.KeyVault/*/read",



   "Microsoft.Kusto/*/read",



   "Microsoft.Logic/*/read",



   "Microsoft.MachineLearningServices/*/read",



   "Microsoft.Maps/*/read",



   "Microsoft.Media/*/read",



   "Microsoft.NetApp/*/read",



   "Microsoft.Network/*/read",



   "Microsoft.NotificationHubs/*/read",



   "Microsoft.OperationalInsights/*/read",



   "Microsoft.PowerBIDedicated/*/read",



   "Microsoft.RecoveryServices/*/read",



   "Microsoft.Relay/*/read",



   "Microsoft.Search/*/read",



   "Microsoft.ServiceBus/*/read",



   "Microsoft.SignalRService/*/read",



   "Microsoft.Sql/*/read",



   "Microsoft.StreamAnalytics/*/read",



   "microsoft.storagesync/*/read",



   "Microsoft.TimeSeriesInsights/*/read",



   "microsoft.web/*/read",



   "Microsoft.DBforMariaDB/*/read",



   "Microsoft.DataBoxEdge/*/read",



   "Microsoft.IoTCentral/*/read",



   "Microsoft.Blockchain/*/read",



   "Microsoft.MixedReality/*/read",



   "Microsoft.EnterpriseKnowledgeGraph/*/read",



   "Microsoft.AppConfiguration/*/read",



   "Microsoft.DataShare/*/read",



   "Microsoft.ServiceFabricMesh/*/read",



   "Microsoft.VMwareCloudSimple/*/read",



   "Microsoft.Peering/*/read",



   "Microsoft.HealthcareApis/*/read",



   "Microsoft.CustomProviders/*/read",



   "Microsoft.StorageCache/*/read",



   "Microsoft.AppPlatform/*/read",



   "Microsoft.ProjectBabylon/*/read",



   "Microsoft.Synapse/*/read",



   "Microsoft.DigitalTwins/*/read",



   "Microsoft.AVS/*/read",



   "Microsoft.DataCollaboration/*/read",



   "Microsoft.SecurityDetonation/*/read",



   "Microsoft.Purview/*/read",



   "Microsoft.Management/*/read/",



   "Microsoft.ResourceGraph/*/read/"



   ],



   "notActions": [],



   "dataActions": [],



   "notDataActions": []



   }



   ]



   }



   }
   ```
4. Select **Review + create** to review the configuration, and then select **Create**.

Create service principal via PowerShell

To create a new service principal and grant it access permissions in PowerShell, see [Create an Azure service principal with Azure PowerShellï»¿](https://docs.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-7.5.0&viewFallbackFrom=azps-2.0.0).

If you choose to create a custom [roleï»¿](https://docs.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-powershell), see [Create custom role via Azure CLI 2.0](#cli).

## Create monitoring configuration

You can create, activate, and manage multiple monitoring connections. Each connection is defined by the credentials and/or access tokens required for Dynatrace to be able to pull in the data, as well as the actual scope of monitoring.

Why configuration is performed per connection?

Allowing for multiple connections and configurations makes it possible to monitor even extremely complex environments. With such an approach, you don't need to configure everything at once. Instead, you can gradually add monitoring configurations to your existing setup. Such an architecture also makes it easy to react to the dynamic changes of the monitored environment, without the need to reconfigure the unaffected elements.

Add a new Azure connection

If you have followed all of the previous steps, you are ready to configure Azure monitoring.

To add a new Azure connection

1. Go to **Settings** > **Cloud and virtualization** > **Azure**. The page lists Azure connections already configured.

   If you haven't provided an ActiveGate required for Azure monitoring (check [Prerequisites](#capable-activegate) for details), the respective information will be provided on the screen and you will not be able to continue with the configuration process.

   Modifying or removing existing connections

   You can go back and change the already configured connections at a later time.

   1. Go to **Settings** > **Cloud and virtualization** > **Azure**. The page lists existing connections.
   2. Edit connections as needed.

      * To edit an existing connection or the monitored services within, select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
      * To delete an existing connection, select **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in that row.
2. Select **Connect new instance** and complete the configuration fields.

   * **Connection ID**âtype a descriptive name for the connection.
   * **Client ID** and **Tenant ID**âenter the values obtained when creating the Azure service principal.

     If you created the Azure service principal in PowerShell, set **Client ID** to the `ApplicationId` value.
   * **Secret Key**âobtained when creating the Azure service principal.

     Limiting data capture

     You can limit the data captured from the Azure Monitor by defining a tag-based filter of specific resources.

     You can choose to monitor resources based on existing Azure tags, as Dynatrace automatically imports them from service instances.  
     To monitor resources based on tags

     1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
     2. On the Azure overview page, select the **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") icon for the Azure instance.
     3. Set **Resources to be monitored** to **Monitor resources selected by tags**.
     4. Enter key/value pairs to identify resources to exclude from monitoring or include in monitoring.
        You can enter multiple key/value pairs: each time you enter a pair, another empty row is displayed for you to edit as needed.
     5. Select **Save** to save your configuration.

        To import the Azure tags automatically into Dynatrace, turn on **Capture Azure tags automatically**.

     Automatic tag import

     Optionally, you can turn off automatic tag import. If turned on, resource tags will be imported, but resource group tags will not be imported.
3. Select **Connect** to add the connection information to the list of Azure connections.

Monitor resources based on tags

There is a limit of 20 entries for either `Include` or `Exclude` tags.

You can choose to monitor resources based on existing Azure tags, as Dynatrace automatically imports them from service instances.  
To monitor resources based on tags

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, select the **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") icon for the Azure instance.
3. Set **Resources to be monitored** to **Monitor resources selected by tags**.
4. Enter key/value pairs to identify resources to exclude from monitoring or include in monitoring.
   You can enter multiple key/value pairs: each time you enter a pair, another empty row is displayed for you to edit as needed.
5. Select **Save** to save your configuration.

   To import the Azure tags automatically into Dynatrace, turn on **Capture Azure tags automatically**.

Azure services monitored by default

After Dynatrace connects to your Azure environment, it immediately starts monitoring Azure's built-in services for the service principal you have defined. [Classic (formerly 'built-in') Azure metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.") lists the metrics of Azure cloud services monitored by default.

Other Azure services

In addition to Azure cloud services that are monitored by default, it is also possible to monitor all other Azure cloud services. Azure cloud services are enabled for monitoring per Azure connection.

To add a service to monitoring

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select **Add service**.
5. Select the service from the list and then select **Add service**.
6. Select **Save changes** to save your configuration.

You can add multiple cloud services by repeating the steps above.

Configuration of collected metrics per Service

After you add a service, Dynatrace automatically starts collecting a set of metrics for this particular service.

Recommended metrics:

* Enabled by default
* Can not be disabled
* Can come with recommended dimensions (enabled by default, can't be disabled)
* Can come with optional dimensions (disabled by default, can be enabled)

Apart from the recommended metrics, most services have the possibility of enabling **optional** metrics that can be added and configured manually.

List of Azure cloud services and collected metrics

To see the complete list of Azure cloud services and learn about the metrics collected for each of them, see [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.").

You can check the list of supported Azure services in [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=azure). You can also access Dynatrace Hub from your monitoring environment and search for "Azure."

To add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select the service for which you want to add metrics. The service details page lists metrics you are monitoring for that service.
5. Select **Add metric**.
6. From the **Add new metric** list, select the metric and then select **Add metric**.
7. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") to expand the metric details and configure the metric.
8. Select **Apply** to save your configuration.

After you select the cloud services and save your changes, monitoring of the newly added services starts automatically.

## What's next?

Within minutes, you'll see the data on your dashboards.

To see the core measurements for each of your Azure connections

1. Go to ![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure") **Azure Classic**.
2. Select the connection for which you want to see an overview of the Azure infrastructure.

You can also build your own dashboard from the metrics collected for your Azure instances. For details on building dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").

Virtual Machines, containers, and deep code monitoring with Dynatrace OneAgent

Dynatrace OneAgent offers unparalleled depth of insight into hosts, containers, and code. To learn more, see [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.").

Further configuration for notifications and alerts

After you set up Azure monitoring, you can:

* [Set up monitoring notifications with Azure Alerts](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts "Integration with Azure Monitor alerts and supported Azure Monitor alerts types"). This allows you to apply alerts and automatically transform them into events that are leveraged by Dynatrace Intelligence for deeper insights.
* [Set up metric events for alerting](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-metric-events-for-alerting "Set up and configure metric events for alerting."). This enables you to create, enable/disable, and configure recommended alerting rules.

Monitoring of Azure logs

You can also monitor Azure logs. For more information, see [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.").


---


## Source: azure-servicefabric.md


---
title: Monitor Azure Service Fabric
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric
scraped: 2026-02-18T05:40:06.903656
---

# Monitor Azure Service Fabric

# Monitor Azure Service Fabric

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jul 19, 2017

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM Metadata such as Azure regions, scale sets and more
* Automatic instrumentation including containerized applications

Note that we don't have an OOTB instrumentation for the Azure Service Fabric Programming Model (Reliable Services and Actors). Instead, use a custom instrumentation using OpenTelemetry.

## Installation

To deploy OneAgent on Azure Service Fabric, follow the same procedure as for [Azure Virtual Machines Scale Set](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.").

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: monitor-azure-spring-apps.md


---
title: Monitor Azure Spring Apps
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps
scraped: 2026-02-18T05:56:26.588474
---

# Monitor Azure Spring Apps

# Monitor Azure Spring Apps

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure Spring Apps. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
* Environment ActiveGate version 1.195+

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## Activate OneAgent Recommended

For an end-to-end view into your Spring Apps workloads, you can [set up OneAgent integration with Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Spring](https://dt-cdn.net/images/2021-03-12-11-35-07-1496-2bea71b55d.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| jvm.gc.live.data.size | Size of old generation memory pool after a full GC | AppName, Pod | Byte | Applicable |
| jvm.gc.max.data.size | Max size of old generation memory pool | AppName, Pod | Byte | Applicable |
| jvm.gc.memory.allocated | Incremented for an increase in the size of the young generation memory pool after one GC to before the next | AppName, Pod | Byte | Applicable |
| jvm.gc.memory.promoted | Count of positive increases in the size of the old generation memory pool before GC to after GC | AppName, Pod | Byte | Applicable |
| jvm.gc.pause.total.count | GC pause count | AppName, Pod | Count | Applicable |
| jvm.gc.pause.total.time | GC pause total time | AppName, Pod | MilliSecond | Applicable |
| jvm.memory.committed | Memory assigned to JVM in bytes | AppName, Pod | Byte | Applicable |
| jvm.memory.max | The maximum amount of memory in bytes that can be used for memory management | AppName, Pod | Byte | Applicable |
| jvm.memory.used | App memory used in bytes | AppName, Pod | Byte | Applicable |
| process.cpu.usage | App JVM CPU usage percentage | AppName, Pod | Percent | Applicable |
| system.cpu.usage | The recent CPU usage for the whole system | AppName, Pod | Percent | Applicable |
| tomcat.global.error | Tomcat global error | AppName, Pod | Count | Applicable |
| tomcat.global.received | Tomcat total received bytes | AppName, Pod | Byte | Applicable |
| tomcat.global.request.avg.time | Tomcat request average time | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.request.max | Tomcat request maximum time | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.request.total.count | Tomcat request total count | AppName, Pod | Count | Applicable |
| tomcat.global.request.total.time | Tomcat request total time | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.sent | Tomcat total sent bytes | AppName, Pod | Byte | Applicable |
| tomcat.sessions.active.current | Tomcat session active count | AppName, Pod | Count | Applicable |
| tomcat.sessions.active.max | Tomcat session maximum active count | AppName, Pod | Count | Applicable |
| tomcat.sessions.alive.max | Tomcat session maximum alive time | AppName, Pod | MilliSecond | Applicable |
| tomcat.sessions.created | Tomcat session created count | AppName, Pod | Count | Applicable |
| tomcat.sessions.expired | Tomcat session expired count | AppName, Pod | Count | Applicable |
| tomcat.sessions.rejected | Tomcat session rejected count | AppName, Pod | Count | Applicable |
| tomcat.threads.config.max | Tomcat configuration maximum thread count | AppName, Pod | Count | Applicable |
| tomcat.threads.current | Tomcat current thread count | AppName, Pod | Count | Applicable |

## Related topics

* [Monitor Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.")


---


## Source: azure-spring.md


---
title: Monitor Azure Spring Apps
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring
scraped: 2026-02-18T05:40:11.698532
---

# Monitor Azure Spring Apps

# Monitor Azure Spring Apps

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 16, 2021

## Capabilities

* Full-stack java monitoring powered by OneAgent
* Integration with [Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")
* Automatic service detection of services running in Azure Spring Apps

Since Azure Spring Apps is a fully managed hosting platform, applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system.

See below how you can integrate OneAgent with your Azure Spring Apps application to monitor your Spring Apps workloads with Dynatrace.

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.")
* [Install the Azure CLIï»¿](https://dt-url.net/cf63rl6)

## Set up integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Prepare your environment in Azure**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#prepare-env "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Determine the values for the required environment variables**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#envvar "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add the environment variables to your application**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#add-variables "Learn how to configure OneAgent for monitoring Azure Spring Apps.")

### Step 1 Prepare your environment in Azure

1. In Azure Portal, create an Azure Spring Apps instance.
2. In the new Azure Spring Apps instance, create an application that you want to report to Dynatrace by running the command below.

   Be sure to replace the placeholders (`<...>`) with your own values.

   ```
   az spring app create --name <your-application-name> --is-public true -s <your-resource-name> -g <your-resource-group-name>
   ```

### Step 2 Determine the values for the required environment variables

To set up OneAgent integration with your Azure Spring Apps instance, you need to configure three environment variables:

* `DT_TENANT`
* `DT_TENANTTOKEN`
* `DT_CONNECTION_POINT`.

Before you begin, collect the following information:

* Your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
* Authentication

  + **PaaS token** authenticates you as a Dynatrace user and is required to determine the tenant token.
  + **Tenant token** allows OneAgent to report data to Dynatrace.
    For more information on tokens, see [Access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").

1. The value for `DT_TENANT`is your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
2. To determine the values for `DT_TENANTTOKEN` and `DT_CONNECTION_POINT`, make an API request to the [Deployment API - GET connectivity information for OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") endpoint. The values you need are returned as `tenantToken` and `communicationEndpoints`.

   You can submit the call to your environment URL (SaaS or Managed) or an Environment ActiveGate URL.

   * **Dynatrace SaaS**:

     ```
     curl https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace:

     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)
   * **Dynatrace Managed**:

     ```
     curl https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace:

     + `<your-domain>` with your Managed deployment domain
     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)
   * **Environment ActiveGate**:

     ```
     curl https://<your-activegate-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace

     + `<your-activegate-domain>` with your ActiveGate domain
     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)

### Step 3 Add the environment variables to your application

Once you have the values for the environment variables required for OneAgent integration, you can add the respective key/value pairs to your application either on Azure Portal, or in the Azure CLI. See the instructions below for each of these options.

In the Azure CLI

In Azure Portal

Run the command below, making sure to replace the placeholders (`<...>`) with your own values determined in the previous steps.

```
az spring app deploy --name <your-application-name> --jar-path app.jar \



-s <your-resource-name> -g <your-resource-group-name> --env DT_TENANT=<your-environment-ID> \



DT_TENANTTOKEN=<your-tenant-token> DT_CONNECTION_POINT=<your-communication-endpoint>
```

1. Go to your Azure Spring Apps instance and select the resource group where Dynatrace will be deployed.
2. Select the application for which you want Dynatrace to report data.
3. Select **Configuration** and enter the following environment variables key/value pairs.

   | Key | Value |
   | --- | --- |
   | `DT_TENANT` | [Your Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |
   | `DT_TENANTTOKEN` | Your tenant token. See [Determine the values for the required environment variables](#envvar) for details. |
   | `DT_CONNECTION_POINT` | Your communication endpoint. See [Determine the values for the required environment variables](#envvar) for details. |
4. [Create a buildpack bindingï»¿](https://dt-url.net/nu036u6) for Dynatrace using the PaaS token (API token) and API url as properties.

   | Property | Value |
   | --- | --- |
   | `api-url` | [Your Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |
   | `api-token` | [PaaS token](#prerequisites) |

Optionally, you can customize the built-in rules for process group detection by setting another environment variable, `DT_CLUSTER_ID`. The value can be the name of the process group you want to see in Dynatrace. See [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") for details.

## View data in Dynatrace

Once you add the environment variables to your application, Dynatrace starts collecting data from it. To view data for your Azure Spring Apps application, go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select your application.

Example service flow:

![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)

Example CPU consumption:

![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)

Example response time analysis:

![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)

## OneAgent updates

OneAgent updates are performed automatically with the JDK.

Following a OneAgent update, you need to restart or redeploy your applications for them to be monitored with a new OneAgent version. This is because some components of OneAgent keep running in processes that are monitored by Dynatrace.

* Before restart, these processes will continue to be monitored with the previous version of OneAgent.
* After restart, these processes will be monitored with the latest version of OneAgent.

## Related topics

* [Monitor Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: monitor-azure-virtual-machines-classic.md


---
title: Monitor Azure Virtual Machines (classic)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic
scraped: 2026-02-17T05:06:52.360975
---

# Monitor Azure Virtual Machines (classic)

# Monitor Azure Virtual Machines (classic)

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 25, 2020

On the Azure Virtual Machine (classic) overview page you get insights into various aspects of performance, including CPU usage, disk throughput, IOPS, and more.

## Prerequisites

* Dynatrace version 1.196+
* Environment ActiveGate version 1.195+

This service monitors Azure Virtual Machine (classic) (`Microsoft.ClassicCompute/virtualMachines`).

You can find the already monitored resources on the Azure overview page in the **Cloud services** section or use a dashboard preset.

To monitor resources of the `Microsoft.Compute/virtualMachines` and `Microsoft.Compute/virtualMachineScaleSets` types, check **Azure Virtual machines** and the **VMs**, and **Scale sets** sections on the Azure overview page.

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Enable Azure monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![VM dash](https://dt-cdn.net/images/azurevirtualmachineclassic-3840-410672d47a.png)

## Available metrics

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Disk Read | Average bytes read from disk during monitoring period. | None | BytesPerSecond | Applicable |
| Disk Read Operations/Sec | Disk Read IOPS. | None | CountPerSecond | Applicable |
| Disk Write | Average bytes written to disk during monitoring period. | None | BytesPerSecond | Applicable |
| Disk Write Operations/Sec | Disk Write IOPS. | None | CountPerSecond | Applicable |
| Network In | The number of bytes received on all network interfaces by the Virtual Machine(s) (Incoming Traffic). | None | Bytes | Applicable |
| Network Out | The number of bytes out on all network interfaces by the Virtual Machine(s) (Outgoing Traffic). | None | Bytes | Applicable |
| Percentage CPU | The percentage of allocated compute units that are currently in use by the Virtual Machine(s). | None | Percent | Applicable |


---


## Source: azure-vm.md


---
title: Monitor Azure Virtual Machines
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm
scraped: 2026-02-18T05:39:32.327837
---

# Monitor Azure Virtual Machines

# Monitor Azure Virtual Machines

* Latest Dynatrace
* How-to guide
* 8-min read
* Published Jul 19, 2017

Dynatrace provides a [VM Extensionï»¿](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) to install OneAgent on Azure Virtual Machines. This enables you to leverage the native deployment automation features using Azure Resource Manager (ARM). The Dynatrace VM extension is available for Windows and Linux in all public Azure regions (including support for Classic Virtual Machines).

The Dynatrace OneAgent site extension doesn't include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/docs/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more
* [Classic Virtual Machines](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Install Dynatrace OneAgent VM extension

There are several ways to install the Dynatrace OneAgent VM extension: through Azure Portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.

Azure Portal

Azure CLI 2.0

PowerShell

### Add the extension to an existing VM

1. In Azure Portal, go to an existing virtual machine where you want to add the OneAgent extension.
2. In the left menu, go to **Settings** and select **Extensions**.
3. Select **Add**.
4. Select **Choose extension**.
5. From the list of extensions, select **Dynatrace OneAgent**.
6. Select **Create** to add the extension.
7. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.
8. Select whether you want to enable Log Monitoring.
9. Optional Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.
10. Select **OK**.
11. To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

### Add the extension to a new VM

1. During the creation of a new VM in the deployment wizard, in **Advanced**, select **Select an extension**.
2. Select **Dynatrace OneAgent**.
3. Select **Create**.
4. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.
5. Select whether you want to enable Log Monitoring.
6. Optional Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.
7. Select **OK**.
8. Continue VM configuration in the deployment wizard.
9. Select **Review and create**.
10. To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

Replace all values marked with `<...>` with your actual values.

```
az vm extension set



--publisher dynatrace.ruxit



-n "<Extension-Type>"



-g "<Resource-Group>"



--vm-name "<VM-Name>"



--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

When using the Azure CLI within PowerShell, the settings have to be formatted as a [here-stringï»¿](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

```
--settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the VM is deployed. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-1-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the `-Settings` string, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

Replace all values marked with `<...>` with your actual values.

```
Set-AzureRmVmExtension



-Name Dynatrace



-Publisher dynatrace.ruxit



-ResourceGroupName "<Resource-Group>"



-Location "<Location>"



-VMName "<VM-Name>"



-ExtensionType "<Extension-Type>"



-TypeHandlerVersion "<Extension-Version>"



-Settings @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the VM is deployed. |
| Location | Required | Location where the VM is deployed. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
| Extension-Version | Optional | Required version of the extension. |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-2-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the `-Settings` string, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

VM extension version 2.201.1.0+

With the VM extension 2.201.1.0 release, you can set the `overrideDefaults` parameter via CLI and PowerShell [installation](#installation) and via [ARM template](#arm-template).

* You can set the custom timeout (`overrideDefaults`) for the Azure VM Extension download, which is helpful in environments with a suboptimal internet connection or smaller network throughput (bandwidth).
* Your error messages became more informative, which is helpful in automated systems.
* Updating the Azure VM Extension on Windows can now be done without uninstalling it first. If the version of OneAgent changes on the tenant, you just need to install the Azure VM Extension again to install this new version.

## Install Dynatrace OneAgent VM extension via an ARM template

Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.  
The JSON file for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. [The placement of the JSON file affects the value of the resource name and typeï»¿](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).

* The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the "resources": [] object of the virtual machine.

  ```
  {



  "type": "extensions",



  "name": "dynatrace",



  "apiVersion": "2018-06-01",



  "location": "[resourceGroup().location]",



  "dependsOn": [



  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"



  ],



  "properties": {



  "publisher": "dynatrace.ruxit",



  "type": "<Extension-Type>",



  "typeHandlerVersion": "<Extension-Version>",



  "autoUpgradeMinorVersion": true,



  "settings": {



  "tenantId": "<Environment-ID>",



  "token": "<API-Token>",



  "server": "<Server-Url>",



  "enableLogAnalytics": "yes",



  "hostGroup": "<Host-Group>"



  },



  }



  }
  ```
* When placing the extension JSON at the root of the template, the resource name includes a reference to the parent virtual machine, and the type reflects the nested configuration.

  ```
  {



  "type": "Microsoft.Compute/virtualMachines/extensions",



  "name": "<Parent-VM-Resource>/dynatrace",



  "apiVersion": "2018-06-01",



  "location": "[resourceGroup().location]",



  "dependsOn": [



  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"



  ],



  "properties": {



  "publisher": "dynatrace.ruxit",



  "type": "<Extension-Type>",



  "typeHandlerVersion": "<Extension-Version>",



  "autoUpgradeMinorVersion": true,



  "settings": {



  "tenantId": "<Environment-ID>",



  "token": "<API-Token>",



  "server": "<Server-Url>",



  "enableLogAnalytics": "yes",



  "hostGroup": "<Host-Group>"



  }



  }



  }
  ```

| Parameter | Required | Description |
| --- | --- | --- |
| Parent-VM-Resource | Required | Name of the parent VM resource where you want to install the extension. Not applicable when using nested resource. |
| VM-Name | Required | Name of the VM where you want to install the extension. |
| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). From `2.200.0.0` version, it's recommended to pass it in `protectedSettings`. |
| Extension-Version | Optional | Required version of the extension. |
| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
| hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
| overrideDefaults [1](#fn-3-1-def) | Optional | Override the default value of the timeoutâ120 seconds. For example, if you want to set the timeout to 600 seconds, add `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` to the ARM template in the `settings` object, you can also leave it empty `\"overrideDefaults\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |

1

Available from VM extension version 2.201.1.0.

To check the deployment status, go to **Deployment Status**.

After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Configure network zones Optional

To configure network zones, use the installer arguments below.

```
az vm extension set



--publisher dynatrace.ruxit



-n "oneAgentLinux"



-g "yourresourcegroup"



--vm-name "awesome-vm"



--settings "{\"tenantId\":\"myawesometenant\",\"token\":\"nope123\", \"installerArguments\":\"--set-host-group=example_hostgroup --set-monitoring-mode=fullstack --set-network-zone=<your.network.zone>\"}"
```

See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: azure-vmss.md


---
title: Monitor Azure Virtual Machine Scale Set (VMSS)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss
scraped: 2026-02-18T05:40:00.516970
---

# Monitor Azure Virtual Machine Scale Set (VMSS)

# Monitor Azure Virtual Machine Scale Set (VMSS)

* Latest Dynatrace
* How-to guide
* 6-min read
* Published Jul 19, 2017

## Capabilities

* Full-stack monitoring powered OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM Metadata such as Azure regions, AutoScale detection, and more

Dynatrace provides a VM extension to install OneAgent on Azure Virtual Machine Scale Set (VMSS). The extension doesn't include the OneAgent installer. Instead, it uses the Dynatrace REST API to download the latest version from the cluster, unless a [default OneAgent versionï»¿](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/) is configured. OneAgent updates are provided automatically.

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Determine your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* Determine your server URL if required.

  The server URL is required only if you use an ActiveGate for a Dynatrace SaaS endpoint. The URL is automatically generated from the environment ID.

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)

## Installation

The Dynatrace VM extension is available for Windows and Linux in all public Azure regions.

Azure CLI 2.0

PowerShell

1. Run the command below.

   Replace all values marked with `<...>` with your actual values.

   ```
   az vmss extension set



   --publisher dynatrace.ruxit



   -n "<Extension-Type>"



   -g "<Resource-Group>"



   --vmss-name "<VMSS-Name>"



   --settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
   ```

   When using the Azure CLI within PowerShell, you need to format the settings as a [here-stringï»¿](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

   ```
   --settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
2. Update the VMSS virtual machines.

   ```
   az vmss update-instances --instance-ids '*' --resource-group $CLUSTER_RESOURCE_GROUP --name $SCALE_SET_NAME
   ```
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VMs. Immediately after restart, OneAgent will begin monitoring them.

1. Run the command below to apply the extension to the VMSS definition.

   Replace all values marked with `<...>` with your actual values.

   ```
   $vmss = Get-AzVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"



   $vmss = Add-AzVmssExtension



   -VirtualMachineScaleSet $vmss



   -Name "dynatrace"



   -Publisher "dynatrace.ruxit"



   -Type "<Extension-Type>"



   -TypeHandlerVersion "2.300"



   -Setting @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |
2. Update the VMSS virtual machines with the new definition.

   ```
   Update-AzVmss



   -ResourceGroupName "<Resource-Group>"



   -Name "<VMSS-Name>"



   -VirtualMachineScaleSet $vmss
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Install Dynatrace OneAgent VM extension via an ARM template

Alternatively to the main installation methods, you can make the Dynatrace site extension part of your ARM templates.

1. Place the JSON configuration for a virtual machine extension in the VMSS resource, under `extensions` in `extensionProfile`.

   Example:

   ```
   {



   "type": "Microsoft.Compute/virtualMachineScaleSets",



   "sku": {...},



   "name": "<VMSS-Name>",



   "apiVersion": "2018-06-01",



   "location": "centralus",



   "properties": {



   "upgradePolicy": {...},



   "virtualMachineProfile": {



   "osProfile": {...},



   "storageProfile": {...},



   "networkProfile": {...},



   "extensionProfile": {



   "extensions": [



   {



   "name": "dynatrace",



   "properties": {



   "publisher": "dynatrace.ruxit",



   "type": "<Extension-Type>",



   "typeHandlerVersion": "<Extension-Version>",



   "autoUpgradeMinorVersion": true,



   "settings": {



   "tenantId": "<Environment-ID>",



   "token": "<API-Token>",



   "enableLogAnalytics": "yes"



   }



   }



   }



   ]



   }



   }



   }



   }
   ```
2. Configure the JSON file.

   ```
   {



   "name": "dynatrace",



   "properties": {



   "publisher": "dynatrace.ruxit",



   "type": "<Extension-Type>",



   "typeHandlerVersion": "<Extension-Version>",



   "autoUpgradeMinorVersion": true,



   "settings": {



   "tenantId": "<Environment-ID>",



   "token": "<API-Token>",



   "server": "<Server-Url>",



   "enableLogAnalytics": "yes",



   "hostGroup": "<Host-Group>"



   },



   }



   }
   ```

   | Parameter | Required | Description |
   | --- | --- | --- |
   | Resource-Group | Required | Name of the resource group on which the VM is deployed. |
   | VMSS-Name | Required | Name of the VMSS where you want to install the extension. |
   | Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |
   | tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |
   | token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |
   | Extension-Version | Optional | Required version[1](#fn-1-1-def) of the extension. |
   | server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |
   | enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |
   | hostGroup | Optional | Define the [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |

   1

   o fetch the list of extension versions, run

   ```
   az vm extension image list --name oneAgentLinux --publisher dynatrace.ruxit
   ```
3. To check the deployment status, go to **Deployment Status**.

   After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.

## Troubleshooting

VMSS nodes not showing up in Dynatrace

Restart the VMSS nodes via PowerShell, replacing all values marked with `<...>` with your actual values:

```
Restart-AzureRmVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"
```

| Parameter | Required | Description |
| --- | --- | --- |
| Resource-Group | Required | Name of the resource group on which the Virtual Machine is deployed |
| VMSS-Name | Required | Name of the VMSS where you want to install the extension. |

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: set-up-log-forwarder-azure.md


---
title: Azure Logs
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure
scraped: 2026-02-18T05:39:51.112332
---

# Azure Logs

# Azure Logs

* Latest Dynatrace
* How-to guide
* 17-min read
* Updated on Oct 17, 2025

DDU consumption for Log Monitoring

DDU pricing applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

Azure log forwarding allows you to stream Azure logs from Azure Event Hubs into Dynatrace logs via an Azure Function App instance. It supports Azure resource logs, activity logs, and Entra ID sign-in logs.

## Resources to be deployed

Azure log forwarding is performed directly through Cluster API. If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.

Deployment of Azure log forwarder results in creating the following resources:

* Storage account (`Microsoft.Storage/storageAccounts`)
* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)
* Azure App Service plan (`Microsoft.Web/serverfarms`)
* Azure Function App (`Microsoft.Web/sites`)

Azure log forwarder uses Linux based Azure function by default. Windows based function is not supported.

For details about the resources created, see the [Azure Resource Manager file on GitHubï»¿](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json)

## Limitations

Logs older than 24 hours are rejected (considered too old by the Dynatrace log ingest endpoint), so we recommend that you don't set a retention time of more than 24 hours for Azure Event Hubs.

The Azure log forwarder supports a maximum 70 MB per minute (~4 GB per hour) in the default configuration. The throughput is measured with Event Hubs metric `Outgoing Bytes` of the Event Hubs instance attached to the function. See [Scaling guide](#scalingguide) for scaling instructions.

## Prerequisites

See below the list of requirements for setting up Azure log forwarding. Some are needed before you start deployment, others during the deployment process.

### Dynatrace

If you're using an earlier version of Dynatrace, see [Alternative deployments](#alternative) for instructions.

* Dynatrace version 1.217+

* [Enable generic log ingestion](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [Enable log monitoring (latest version)](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.")

* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and enable the **Ingest logs** permission. The API token applies to both versions.

### Azure

1. In each Azure location from where you want to pull logs [Create a resource group & Set up an Azure Event Hubs instanceï»¿](https://dt-url.net/8w03rs3).

   To be able to send logs,

   * The Event Hubs instances and the resource group in which the deployment will run need to be in the same region.
   * make sure that in Event Hubs Namespace > Public access > Public network access, the **Disabled** option button is NOT selected. Otherwise, the logs won't be sent to Dynatrace.
2. Create an authorization rule with the **listen** permission for the Event Hubs instance that is configured for receiving logs:

   ```
   az eventhubs eventhub authorization-rule create --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <authorization_rule_name> --rights Listen
   ```
3. Get an Event Hubs connection string for the authorization rule created above:

   ```
   az eventhubs eventhub authorization-rule keys list --resource-group <your_resource_group> --namespace-name <your_event_hub_namespace> --eventhub-name <your_event_hub_instance> --name <your_authorization_rule_name>
   ```
4. Configure the [diagnostic settingsï»¿](https://dt-url.net/se83r02) to stream both resource-related and Entra ID sign-in logs to the Azure Event Hub instances.

### CLI

You can run Azure log forwarding deployment using Azure Portal Cloud Shell (Bash) or from any machine with [Azure CLIï»¿](https://dt-url.net/cf63rl6) and Bash shell (Linux or Windows WSL).

## Deploy

1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values.

   * For `DEPLOYMENT_NAME`, enter your deployment name between 3 and 20 characters long. You can use lowercase letters and numbers.

     **Note:** The name needs to be globally uniqueâit is appended to the created Azure resources.

* For `TARGET_URL`, enter your environment URL: `https://<your_environment_ID>.live.dynatrace.com`. To learn how to determine your environment ID for the SaaS deployment, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

* For `TARGET_API_TOKEN`, enter your API token. See [Dynatrace requirements](#dynatrace) for details.
* For `RESOURCE_GROUP`, enter the name of the Azure resource group in which deployment will run. See [Azure requirements](#azure) for details.
* For `EVENT_HUB_CONNECTION_STRING`, enter the connection string for the Azure Event Hubs instances configured for receiving logs. See [Azure requirements](#azure) for details.

Optional You can enable [self-monitoring](#sfm) and/or [log filtering](#filter) during or after deployment.

```
DEPLOYMENT_NAME=<your_deployment_name>



TARGET_URL=<your_environment_URL>



TARGET_API_TOKEN=<your_API_token>



RESOURCE_GROUP=<your_resource_group>



EVENT_HUB_CONNECTION_STRING="<your_Event_Hub_connection_string>"
```

2. Download the `azure-log-forwarder-function` script and deploy the infrastructure.

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-connection-string $EVENT_HUB_CONNECTION_STRING  --require-valid-certificate true
   ```

## View Azure logs

After deploying the script, you can view and analyze Azure logs in Dynatrace:
Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and, in the attributes filter, search for **Azure**.

* If you see logs coming in, you managed to deploy Azure log forwarder successfully.
* If there are no logs within 10 minutes checkout the **Verification** guide section of the page.

You can use [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to filter for Azure logs.
As an example, you could add the following line to a DQL query:

```
fetch logs



| filter matchesValue(dt.openpipeline.source, "/api/v2/logs/ingest") AND matchesValue(cloud.provider, "Azure")



| sort timestamp desc
```

If you already have multiple integrations, you can additionally use the values `cloud.log_forwarder` and `dt.auth.origin` to further refine your filters.

## Self-monitoring Optional

Self-monitoring allows a quick diagnosis to see if your function processes and sends logs to Dynatrace properly.

### Enable self-monitoring

To enable self-monitoring, you have two options:

* **During deployment:** Set the [`--enable-self-monitoring` parameter](#par) (or the [`SFM_ENABLED` environment variable](#var)) to `true`.
* **After deployment:** In Azure Portal, go to the configuration of your deployed Function App instance and set `SELF_MONITORING_ENABLED` to `true`.

Enable managed identity

After enabling self-monitoring, you need to enable [managed identityï»¿](https://dt-url.net/qj23rie) for
your Function App instance created during deployment, and configure it to allow pushing metrics to the resource.

To set up managed identity

1. In Azure Portal, go to the **Settings** of your Function App instance created during deployment, and select **Identity**.
2. Select **Yes** to **Enable system assigned managed identity**.
3. Go to your resource group where Function App is deployed and select **Access control (IAM)**.
4. Select **Add** to add a role assignment.
5. Set the **Monitoring Metrics Publisher** role.
6. Select **Save** to save your configuration.

### Self-monitoring metrics

Once you enable self-monitoring, you can view the following metrics in your `dynatrace_logs_self_monitoring` namespace of the newly deployed Function App instance.

| Metric name | Description | Dimension |
| --- | --- | --- |
| `all_requests` | All requests sent to Dynatrace. |  |
| `dynatrace_connectivity_failures` | Reported when any Dynatrace connectivity issues occurred. | `connectivity_status` |
| `parsing_errors` | Reported when any parsing errors occurred during log processing. |  |
| `processing_time` | Time needed to process all logs. |  |
| `sending_time` | Time needed to send all requests. |  |
| `too_long_content_size` | Reported when content of log is too long. The content will be trimmed. |  |
| `too_old_records` | Reported when logs received from Event Hubs are too old. |  |

## Log filtering Optional

To reduce the number of logs that are sent to Dynatrace, you can apply filters.  
To apply filters you have two options:

* **During deployment:** Set the `FILTER_CONFIG` environment variable in Azure Portal Cloud Shell (Bash) before running the deployment script.

  1. Add the `FILTER_CONFIG` environment variable to the list of environment variables needed for the deployment script.

     Be sure to replace placeholders with your values. See [Filter options](#options) for details.

     ```
     FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>;FILTER.GLOBAL.CONTAINS_PATTERN=<pattern>;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>;FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<pattern>;FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>;FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<pattern>"
     ```
  2. Set the environment variables.
  3. Download the `azure-log-forwarder-function` script and deploy the infrastructure.
* **After deployment:** Add `FILTER_CONFIG` in Azure Portal.

  1. In Azure Portal, go to **Environment variables** of your deployed Function App instance.
  2. In **App settings**, search and select **FILTER\_CONFIG**.

     **FILTER\_CONFIG** will appear in Azure after running the deployment script.
  3. Select **Edit** to add a **Value** for your filter.

     Example edit

     ![Edit](https://dt-cdn.net/images/image-36-3759-7bc37dfe3c.png)

     Alternatively, you can select **Advanced edit** to enter your value in the JSON.

     Example advanced edit

     ![Advanced](https://dt-cdn.net/images/image-37-3804-dffe41ec79.png)
  4. Select **OK**.
  5. Restart your Function App instance.

### Filter options

`FILTER_CONFIG` is a key-value pair variable. You can set two types of filters (`MIN_LOG_LEVEL` and/or `CONTAINS_PATTERN`) for three filter groups (`GLOBAL`, `RESOURCE_TYPE`, and/or `RESOURCE_ID`).

#### Filter type: `MIN_LOG_LEVEL`

This filter type allows you to filter out logs with unwanted levels. Possible log levels are:

* **Critical** (or `1`)
* **Error** (or `2`)
* **Warning** (or `3`)
* **Informational** (or `4`)

Example:  
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Warning"`  
In the example above, **Informational** logs will be skipped, and only **Warning**, **Error**, and **Critical** logs will be sent to Dynatrace.

Syntax options are:

* `FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>`
* `FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>`
* `FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>`

You can have one global-level filter and additional filters for a particular resource type/ID.

Example:  
`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Error;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.MICROSOFT.WEB/SITES=Informational"`  
In the example above, all logs from instances with resource type `MICROSOFT.WEB/SITES` will be sent to Dynatrace, while for all other resources, **Informational** and **Warning** logs will be filtered out.

#### Filter type: `CONTAINS_PATTERN`

This filter type allows you to collect logs containing a particular text. We use fnmatch that provides support for Unix shellâstyle wildcards. See [Unix filename pattern matchingï»¿](https://docs.python.org/3/library/fnmatch.html) for details.

Syntax options are:

* `FILTER.GLOBAL.CONTAINS_PATTERN=<log_pattern>`
* `FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<log_pattern>`
* `FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<log_pattern>`

#### Filter group: `GLOBAL`

This filter is set for all logs.

#### Filter group: `RESOURCE_TYPE`

This filter is used only for logs coming from resources of the given Azure resource type, such as `Microsoft.Compute/virtualMachines`.

You can find the resource type in Azure Portal, in your resource's **Properties**.

If the **Type** field doesn't appear in **Properties**, you can extract it from the resource ID string.

Resource ID string syntax:  
`/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/<resourceType>/<resourceName>`  
The resource type will be the part between `/providers/` and `/resourceName/`.

#### Filter group: `RESOURCE_ID`

This filter is used only for logs coming from the given resource that is identified by the Azure resource ID.

You can look for the resource type in Azure Portal, in your resource's **Properties**.

### Filter rules

* If you set two filter types for the same group, both conditions need to be met, so the second filter will have to match the first filter.

  For example, if you set `MIN_LOG_LEVEL` to **Warning** and `CONTAINS_PATTERN` to `<some_important_message>`, you will get only **Warning** logs containing `<some_important_message>`, and all other warning logs that don't contain that specific message will be filtered out.
* If you set one filter type for one group, and another filter type for another group, the two conditions do not overlap.

  For example, if you set `MIN_LOG_LEVEL` to **Warning** for `GLOBAL`, and `CONTAINS_PATTERN` to `<some_important_message>` for `RESOURCE_TYPE`, you will get all **Warning**, **Error**, and **Critical** logs from `GLOBAL`, and all logs containing `<some_important_message>` from `RESOURCE_TYPE`.
* If you set more than one pair of filter types (`MIN_LOG_LEVEL` and `CONTAINS_PATTERN`) for the same group (global or resource type/ID), only the last pair of filter types will apply; all the others will be ignored.

## Update Azure log forwarding

To update Azure log forwarding

1. You need a package that contains the source code of Azure log forwarderâdownload the latest Dynatrace version.

   ```
   wget https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-log-forwarder.zip
   ```
2. Deploy the new version, making sure to replace the placeholders with the required values.

   ```
   az webapp deployment source config-zip -g <your_resource_group_name> -n <application_name> --src <zip_file_path>
   ```

Some Azure log forwarder releases include changes that require full reinstallation. For more details, refer to the [GitHub releases pageï»¿](https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases).

## Alternative deployments

### Use existing ActiveGate

If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.

See below for instructions.

#### Prerequisites

Dynatrace version 1.217+

* [Dynatrace requirements](#dynatrace) listed above
* [Azure requirements](#azure) listed above
* [CLI requirements](#cli) listed above

#### Configuration

1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values.

   * For `DEPLOYMENT_NAME`, enter your deployment name (lowercase only).
   * For `TARGET_URL`, enter the API URL of your ActiveGate endpoint: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. To learn how to determine your environment ID, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * For `TARGET_API_TOKEN`, enter your API token. For details, see the prerequisites above.
   * For `RESOURCE_GROUP`, enter the name of the Azure resource group in which deployment will run. See [Azure requirements](#azure) for details.
   * For `EVENT_HUB_CONNECTION_STRING`, enter the connection string for the Azure Event Hubs instances configured for receiving logs. See [Azure requirements](#azure) for details.
   * For `USE_EXISTING_ACTIVE_GATE`, enter `true`.
   * Optional For `REQUIRE_VALID_CERTIFICATE`, enter `true` or `false`. This parameter tells the log forwarder to verify the SSL certificate of your ActiveGate. By default, certificates are validated.

   Optional You can enable [self-monitoring](#sfm) and/or [log filtering](#filter) during or after deployment.

   ```
   DEPLOYMENT_NAME=<your_deployment_name>



   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   RESOURCE_GROUP=<your_resource_group>



   EVENT_HUB_CONNECTION_STRING="<your_Event_Hub_connection_string>"



   USE_EXISTING_ACTIVE_GATE=true



   REQUIRE_VALID_CERTIFICATE=true
   ```
2. Download the `azure-log-forwarder-function` script and deploy the infrastructure.

   Be sure to check whether you want to set other optional parameters as well. All parameters between brackets (`[...]`) are optional. For details, see [Deploy table](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-connection-string $EVENT_HUB_CONNECTION_STRING --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

### Use a user-assigned managed identity

There are two managed identity types: system-assigned and user-assigned. By default, a system-assigned managed identity is used. If you prefer to use a user-assigned managed identity, see below for instructions.

#### Prerequisites

Dynatrace version 1.217+

* [Dynatrace requirements](#dynatrace) listed above
* [Azure requirements](#azure) listed above
* [CLI requirements](#cli) listed above

In addition to the [Azure requirements](#azure) listed above, you should also create a user-assigned managed identity in Azure Portal.

Add Event Hubs roles in the user-assigned managed identity. For the event hub trigger binding, you need to assign corresponding built-in roles. The built-in roles are **Azure Event Hubs Data Receiver** and **Azure Event Hubs Data Owner**.

#### Configuration

1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values.

   ```
   DEPLOYMENT_NAME=<your_deployment_name>



   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   RESOURCE_GROUP=<your_resource_group>



   EVENT_HUB_NAME=<your_Event_Hub_name>



   REQUIRE_VALID_CERTIFICATE=true



   ENABLE_USER_ASSIGNED_MANAGED_IDENTITY=true



   EVENT_HUB_CONNECTION_CLIENT_ID=<your_user_assigned_MI_client_id>



   MANAGED_IDENTITY_RESOURCE_NAME=<your_user_assigned_MI_resource_name>



   EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE="<your_eventhub_namespace_host_name>"



   CONSUMER_GROUP ="<Your_custom_default_consumer_group_name>"
   ```

   * For `DEPLOYMENT_NAME`, enter your deployment name (lowercase only).

* For `TARGET_URL`, enter your environment URL: `https://<your_environment_ID>.live.dynatrace.com`. To learn how to determine your environment ID for a SaaS deployment, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

* For `TARGET_API_TOKEN`, enter your API token. For details, see the prerequisites above.
* For `RESOURCE_GROUP`, enter the name of the Azure resource group in which deployment will run. See [Azure requirements](#azure) for details.
* For `EVENT_HUB_NAME`, enter the name of the Azure Event Hubs instances configured for receiving logs. See [Azure requirements](#azure) for details.
* Optional For `REQUIRE_VALID_CERTIFICATE`, enter `true` or `false`. This parameter tells the log forwarder to verify the SSL certificate of your ActiveGate. By default, certificates are validated.
* For `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY`, enter `true`. This parameter is used to determine if a user-assigned managed identity is used instead of system assigned.
* For `EVENT_HUB_CONNECTION_CLIENT_ID`, enter the `Client ID` of the created managed identity.
* For `MANAGED_IDENTITY_RESOURCE_NAME`, enter the resource name of the created managed identity.
* For `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE`, enter:

  + The `Host name` of the Event Hubs namespace.
  + The custom name of the default consumer group.

Optional You can enable [self-monitoring](#sfm) and/or [log filtering](#filter) during or after deployment.

2. Download the `azure-log-forwarder-function` script and deploy the infrastructure.

   Be sure to check whether you want to set other optional parameters as well. All parameters between brackets (`[...]`) are optional. For details, see [Deploy table](#table).

   ```
   wget -q https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases/latest/download/dynatrace-azure-logs.sh -O dynatrace-azure-logs.sh && chmod +x ./dynatrace-azure-logs.sh \



   && ./dynatrace-azure-logs.sh --deployment-name $DEPLOYMENT_NAME --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --resource-group $RESOURCE_GROUP --event-hub-name $EVENT_HUB_NAME --require-valid-certificate $REQUIRE_VALID_CERTIFICATE --enable-user-assigned-managed-identity $ENABLE_USER_ASSIGNED_MANAGED_IDENTITY --eventhub-connection-client-id $EVENT_HUB_CONNECTION_CLIENT_ID --managed-identity-resource-name $MANAGED_IDENTITY_RESOURCE_NAME --eventhub-connection-fully-qualified-namespace $EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE --custom-consumer-group $CONSUMER_GROUP
   ```

### Deploy table

For a complete list of parameters, see the deploy table below.

| **Command-line parameter** | **Environment variable** | **Description** |  |
| --- | --- | --- | --- |
| `--deployment-name` | `DEPLOYMENT_NAME` | Required Your deployment name. Lowercase only. |  |
| `--target-url` | `TARGET_URL` | Required Your Dynatrace environment where you want to set up generic log ingestion. |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Required Your API token. |  |
| `--resource-group` | `RESOURCE_GROUP` | Required Name of the Azure resource group in which the deployment will run. |  |
| `--event-hub-connection-string` | `EVENT_HUB_CONNECTION_STRING` | Required The connection string for the Azure Event Hubs instance configured for receiving logs. (Azure Event Hubs name that is configured for receiving logs.) |  |
| `--event-hub-name` | `EVENT_HUB_NAME` | Optional Optional by default. If a user-assigned managed identity is your method of authentication, then Required. |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Optional If set to `true`, the log forwarder verifies the SSL certificate of your ActiveGate. By default, certificates are validated. |  |
| `--enable-self-monitoring` | `SFM_ENABLED` | Optional If set to `true`, Dynatrace sends custom metrics to Azure. See [Enable self-monitoring](#sfm) for details. By default, custom metrics aren't sent to Azure. |  |
| `--filter-config` | `FILTER_CONFIG` | Optional Apply filters to reduce the number of logs sent to Dynatrace. See [Log filtering](#filter) for details. |  |
| `--tags` | `TAGS` | Optional Apply Azure tags to newly created resources in comma-separated key:value pair format (for example, `"tag:value,tag2:value2"`). The following characters are not supported in a tag key: `,:<>%&\?/` |  |
| `--enable-user-assigned-managed-identity` | `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` | Optional If set to `true`, options `--eventhub-connection-client-id`, `--managed-identity-resource-name`, `--eventhub-connection-fully-qualified-namespace`, `--event-hub-name` are Required. Enables usage of a user-assigned managed identity instead of a system-assigned managed identity. |  |
| `--custom-consumer-group` | `CONSUMER_GROUP` | Optional If provided, this value will be used as the name of a default consumer group. Leave empty to apply the default Azure value. |  |
| `--eventhub-connection-client-id` | `EVENT_HUB_CONNECTION_CLIENT_ID` | Optional `Client ID` of the created managed identity. Example value: `d8916c27-4c4r-482o-895b-doe0b48c76f7` |  |
| `--managed-identity-resource-name` | `MANAGED_IDENTITY_RESOURCE_NAME` | Optional Resource name of the created managed identity. Example value: `test-managed-identity` |  |
| `--eventhub-connection-fully-qualified-namespace` | `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` | Optional `Host name` of the Azure Event Hubs namespace. Example value: `sample-eventhub-namespace.servicebus.windows.net` |  |

## Verification

To verify if the deployment was successful, in Dynatrace, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** and confirm that the following log line is present:

![Log line](https://dt-cdn.net/images/screenshot-2022-08-11-at-11-49-52-928-5957a24948.png)

In around 10 minutes, further logs should start coming in. If no logs are coming in, make sure that:

* The Event Hubs instances and the resource group in which the deployment will run are in the same region
* You carefully followed the steps to [Configure diagnostic settingsï»¿](https://dt-url.net/se83r02)

Furthermore, you can read Azure Function logs in which the Azure-log-forwarder is running. [Enable streaming execution logs in Azure Functionsï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/streaming-logs)

SNAT port exhaustion: Azure Functions have a limited number of ports that can be opened at a time (128). The number of instances, the number of worker processes, and the number of concurrent calls are the factors that contribute to the open connections. If the limit is reached, see the [scaling guide](#scalingguide) below.

## Check your version

To check the version of the currently deployed Azure log forwarder

1. Open Azure Portal and go to **Subscriptions**.
2. Select your subscription.
3. Go to **Resource groups**.
4. Choose the resource group that contains the function.
5. Choose your deployed function app.
6. Select **log\_ingest** on the **Functions** tab.
7. Select **Code + Test** from the **Developer** menu on the left.
8. Select the dropdown file selector (`main.py` is selected by default).
9. Choose `version.txt`.
10. Open the file to check your currently deployed version.

## Scaling guide

The recommended way of scaling up the default throughput of 70 MB/min is to upgrade the App Service plan, increase the number of App Service instances respectively, increase `FUNCTIONS_WORKER_PROCESS_COUNT` (default is 1), increase `NUMBER_OF_CONCURRENT_SEND_CALLS` (default is 2). You can add `FUNCTIONS_WORKER_PROCESS_COUNT` and `NUMBER_OF_CONCURRENT_SEND_CALLS` as **New application setting** in Azure Portal (**Azure function** > **Configuration** > **New application setting**).

Please note that the performance of the log forwarder may vary depending on the log content (size/ processing complexity).

| **Maximum throughput** | **App Service Plan** | **Number of instances** | **Configuration** |
| --- | --- | --- | --- |
| up to `70 MB/minute` (up to 4 GB/hour) | `S1` | `1` | no configuration |
| up to `580 MB/minute` (up to 32 GB/hour) | `P1V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 4, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| up to `1 GB/minute` (up to 60 GB/hour) | `P2V3` | `1` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |
| up to `2.3 GB/minute` (up to 138 GB/hour) | `P2V3` | `3` | FUNCTIONS\_WORKER\_PROCESS\_COUNT: 8, NUMBER\_OF\_CONCURRENT\_SEND\_CALLS: 5 |

As a last resort, scale horizontally: deploy more integrations and distribute the logs' load into different Event Hubs instances.

## Uninstall Azure log forwarding

To uninstall the Dynatrace Azure log forwarder

1. In Azure Portal, go to the resource group used for installation.
2. Filter resources by tag.

   The deployment script tags all created resources with `LogsForwarderDeployment = <your_deployment_name>`.
3. Delete the resources.

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Azure Log Forwarder Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)


---


## Source: azure-integrations.md


---
title: Microsoft Azure Integrations
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations
scraped: 2026-02-17T04:51:12.821485
---

# Microsoft Azure Integrations

# Microsoft Azure Integrations

* Overview
* 1-min read
* Published Aug 12, 2021

Dynatrace provides comprehensive monitoring support for Azure services, by integration with both OneAgent and Azure Monitor.

## Integrate on Azure compute- and serverless services

[Monitor Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice "Monitor Azure App Service")

[Microsoft Azure Arc-enabled servers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers "Azure integration with ARC servers")

[Monitor Azure Functions using Azure App Service (built-in)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions "Monitor Azure Functions")

[Monitor Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.")

[Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Learn how to deploy, operate, and maintain OneAgent on Azure Kubernetes Service.")

[Monitor Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure Service Fabric using a VM extension.")

[Monitor Azure Virtual Machines](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm "Learn how to install and configure OneAgent for monitoring Azure Virtual Machines using a VM extension.")

[Monitor Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.")

## Azure Monitor integration

In addition to monitoring your Azure workloads using OneAgent, you can integrate Dynatrace with Azure Monitor to monitor infrastructure and gain insight even in serverless application scenarios.

For more information, see [Monitor Azure services with Azure Monitor metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")


---


## Source: azure-native-integration.md


---
title: Azure Native Dynatrace Service
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration
scraped: 2026-02-18T05:47:37.584208
---

# Azure Native Dynatrace Service

# Azure Native Dynatrace Service

* Latest Dynatrace
* Explanation
* 17-min read
* Updated on Jul 23, 2024

Azure Marketplace integration enables you to build a streamlined experience for purchasing, configuring, and managing Dynatrace directly inside the Azure portal. After setting up the integration, Dynatrace appears as an Azure native service, and you can manage its configuration from Azure Portal.

Capabilities and limitations

**Capabilities:**

* **Seamless onboarding:** Easy onboarding to Dynatrace SaaS as an integrated service on Azure via Azure Marketplace. To set up the integration:

  + No event hubs, cloud functions, or configurations are required

* **Unified billing:** Get a single bill for all the resources you consume on Azure, including all Dynatrace SaaS consumption.
* **Single sign-on:** You don't need separate credentials for the Dynatrace portal. Sign in once on the Azure portal and seamlessly transition to Dynatrace when needed.
* **Log monitoring:** Enables forwarding of subscription activity and resource logs to Dynatrace. For details, see [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

* **OneAgent deployment:** You get a unified management experience of Dynatrace OneAgents. You can install and uninstall Dynatrace OneAgents as extensions on Azure Virtual Machines and Azure App Services.

**Limitations:**

* The integration will create a new Dynatrace environment and account; it can't run on an existing Dynatrace environment.

Azure Marketplace

The Azure Native Dynatrace service is available via the [Azure marketplaceï»¿](https://dt-url.net/9n039mv).

For getting a customized private offer for the Azure Native Dynatrace Service, reach out to Dynatrace sales via email to [sales@dynatrace.com](mailto:sales@dynatrace.com).

## Prerequisites

Activate the private plan for Azure Native Dynatrace Service

The Azure Native Dynatrace Service is available via a [private planï»¿](https://dt-url.net/3d03xln). To have Dynatrace create a private plan for you, [contact Dynatraceï»¿](https://dt-url.net/m003xf1). Once you accept the offer, the private plan for Azure Native Dynatrace Service will be accessible on Azure Marketplace.

Register the Dynatrace resource provider

To create and manage the Dynatrace resources using the Azure Portal, you need to register a Dynatrace resource provider named `Dynatrace.Observability` in your Azure subscription.

How to register the Dynatrace resource provider

On the Azure Portal

Using the Azure CLI

Follow the instructions on [Azure resource providers and typesï»¿](https://dt-url.net/fu03x5j).

Run the command below, making sure to replace `<subscription-id>` with your own subscription ID.

```
az provider register --namespace Dynatrace.Observability --subscription <subscription-id>
```

Set up permissions

#### General permissions

* You need a `Contributor` permission to the Azure subscription.

The first user creating the first Dynatrace resource and environment in a subscription becomes the Dynatrace account owner of the Dynatrace account that is created during the integration deployment. For all subsequent Dynatrace resources and environments that are created in the same subscription by other users, the account owner will also have full permissions.

#### SSO permissions

If you use Microsoft Entra ID as your identity provider, you can establish single sign-on (SSO) from the Azure portal to Dynatrace. If you use a different identity provider or you don't want to establish SSO, you can skip this section.

To enable single sign-on authentication for your Dynatrace resource, you need to [set up SSO in Microsoft Entra ID](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-azure#configuration "Learn how to configure Dynatrace SSO in Azure.").

After setting up SSO in Active Directory, you can enable SSO during or after the Azure integration deployment.

## Set up the integration

When you first deploy the Azure Native Dynatrace Service, a new Dynatrace environment hosted on a new Dynatrace resource is created.

* The Dynatrace resource is created in the Azure subscription and resource group that you select during the installation deployment. You can configure, manage, and troubleshoot issues on your Dynatrace resource from the Azure Portal.
* The Dynatrace environment is created in the same Azure region in which you create the Dynatrace resource. In this new environment:

  + After you [install OneAgent](#oa), you can start monitoring [metrics](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") from your Azure resources. You can also collect metrics from the [default services](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration#default "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")
  + You can collect [logs](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") from your Azure resources
  + You do not need an environment ActiveGate for this integration.

To set up the integration

1. Go to the Azure subscription where you want to create the Dynatrace resource.
2. Select **Resources**, and then select **Create**.
3. Search for **Azure Native Dynatrace Service**. You should see the message that a private product is available.
4. Select the tile **Azure Native Dynatrace Service**.
5. In the list for choosing a plan, select the private plan that you accepted in [Activate the private plan for Azure Native Dynatrace Service](#step-1) and then select **Subscribe**.
6. On **Create a new Dynatrace environment**, select **Create**.
7. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overviewï»¿](https://dt-url.net/xv43x96).
8. Enter a **Resource name** for the Dynatrace resource, and then select a **Region** from the dropdown menu. The Dynatrace resource in Azure and the Dynatrace environment will be created in the selected region.
9. Select your **Pricing plan**, and then select **Next: Metrics and Logs**.
10. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

    If you select **Send Azure resource logs for all defined services**, Azure resource logs are sent for all defined resources by default, which means logs are collected for all supported resources. To filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

    * Azure resources with `Include` tags send logs to Dynatrace.
    * Azure resources with `Exclude` tags don't send logs to Dynatrace.
    * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.

      There is a limit of 20 entries for either `Include` or `Exclude` tags.
11. Select **Next: Single sign-on**.
12. Optional Choose whether to **Enable SSO through Microsoft Entra ID**.

    * If you don't want to enable this feature, select **Next: Tags**.
    * If you want to enable this feature, select it, select the Dynatrace application ID that is displayed, and then select **Next: Tags**.
13. Optional [Specify tags](#tags) for the new Dynatrace resource, and then select **Next: Review + create**.
14. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Link multiple Azure subscriptions to one Dynatrace environment Optional

Ensure that your Azure account has access to the Dynatrace account with the following permissions:

* View Account
* View Environment
* Install OneAgent
* Manage Monitoring Settings

For more details, see [Environment permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").

After deploying the Azure integration, you can:

* Link more Azure subscriptions to your newly created Dynatrace environment.
* Link more Dynatrace environments to a single Azure subscription.

  When linking multiple Azure subscriptions and creating the resource, you must have Dynatrace Account privileges `tenant-manage-settings` and `tenant-agent-install` permissions. For more information on how to configure these permissions, see [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Follow the steps below, making sure to repeat the procedure for every subscription that you want to link.

1. Go to Azure Portal and search for `Azure Native Dynatrace Service` from the top search bar.
2. Select **Azure Native Dynatrace Service**.
3. Select **Create**.
4. In **Basics**, for **Resource group**, specify whether to create a new resource group or use an existing one.

   A resource group is a container that holds related resources for an Azure solution. For more information, see [Azure Resource Group overviewï»¿](https://dt-url.net/xv43x96).
5. Enter a **Resource name** and then select a **Region** from the dropdown menu.

   The Dynatrace environment to link and your new Dynatrace resource must be in the same region.
6. Select the **Dynatrace environment** to link to the Azure subscription, and then select **Next: Metrics and Logs**.
7. Optional Select whether to **Send subscription activity logs** and/or **Send Azure resource logs**. For details, see [Configure metrics and logs](#metrics-logs).

   If you select **Send Azure resource logs for all defined services**, Azure resource logs are sent for all defined resources by default, which means that logs are collected for all supported resources. To filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.
8. Skip **Next: Single sign-on** (you can only configure SSO after deployment) and then select **Next: Tags**.
9. Optional [Specify tags](#tags) for the new Dynatrace resource, and then select **Next: Review + create**.
10. Verify if the information submitted is correct, and then select **Create**. When the deployment is complete, you can select **Go to resource** to navigate to the specific Dynatrace resource.

## Access your Dynatrace environment

After you set up the integration, you can access your Dynatrace environment directly from Azure Portal.

In Azure Portal, go to your Dynatrace resource and select **Overview**. All details of your Dynatrace environment will appear there, including direct links to the following web UI pages:

* **Dashboards** - For details, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* **Log Viewer** - For details, see [Log viewer (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").
* **Smartscape topology** - For details, see [Visualize your environment through Smartscape Classic](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").

## Configure metrics and logs

### Metrics

* You can activate [metrics](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") after the Azure integration deployment.

Collect metrics from Virtual Machines and App Services

To start collecting metrics from your Virtual Machines and App Services, you need to [install Dynatrace OneAgent on these resources as an extension](#oa) .

Collect metrics from cloud services

All services and metrics are enabled by default. You can disable them if needed by selecting the delete button from the list of services.
After Dynatrace connects to your Azure environment, it immediately starts monitoring Azure's built-in services for the service principal you have defined. [Classic (formerly 'built-in') Azure metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.") lists the metrics of Azure cloud services monitored by default.

### Manage cloud services

All cloud services are monitored by default, but you can quickly disable them from the list or re-enable them as needed.

To add services to monitoring

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. For each service that you want to add: select **Add service**, select the service from the list, and then select **Add service**.
5. Select **Save changes** to save your configuration.

Configuration of collected metrics per service

After you add a service, Dynatrace automatically starts collecting a set of metrics for that service.

Recommended metrics:

* Are enabled by default and can't be disabled.
* Can come with recommended dimensions (enabled by default, can't be disabled) and optional dimensions (disabled by default, can be enabled).

Apart from the recommended metrics, most services offer the possibility of enabling optional metrics that can be added and configured manually.

List of Azure cloud services and collected metrics

To see the complete list of Azure cloud services and learn about the metrics collected for each of them, see [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.").

Alternatively, you can check the list of supported Azure services within in-product Dynatrace Hub (search for **Azure**) or in the [web version of Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=azure).

To add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, find the connection that you want to change and select **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") in that row.
3. Under **Services**, select **Manage services**.
4. Select the service for which you want to add metrics. The service details page lists the metrics you are already monitoring for that service.
5. Select **Add metric**.
6. From the **Add new metric** list, select the metric and then select **Add metric**.
7. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") to expand the metric details and configure the metric.
8. Select **Apply** to save your configuration.

After you select the cloud services and save your changes, monitoring of the newly added services starts automatically.

### Logs

* You can activate [logs](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-logs).

You can set up two types of logs from Azure to Dynatrace: [subscription activity logs](#activity) and [Azure resource logs](#resource).

#### Subscription activity logs

Subscription activity logs provide insights into the operations (PUT, POST, DELETE) performed on each Azure resource in your subscription (the management plane). For each Azure subscription, there's a single activity log.

#### Azure resource logs

Azure resource logs provide insights into operations that were performed within an Azure resource (the data plane), such as getting a secret from a key vault or making a request to a database. The content of resource logs varies by the Azure service and resource type.

All Azure services in the [Azure Monitor log categoriesï»¿](https://dt-url.net/fja38sr) ingest logs, including Microsoft Entra ID and [Azure Monitor Integration Serviceï»¿](https://dt-url.net/dpc38am).

For a list of Azure resource logs, see [Supported categories for Azure Monitor resource logsï»¿](https://dt-url.net/ea03xvn).

#### How to activate logs after deployment

Activate subscription activity logs

Activate Azure resource logs

1. On the Azure Portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send subscription activity logs**.
3. Select **Save**.

1. On the Azure Portal, go to your Dynatrace resource and select **Metrics and logs**.
2. Select **Send Azure resource logs for all defined sources**.

   When selecting this option, Azure resource logs are sent for all defined resources by default, which means that logs are collected for all supported resources.
3. Optional If you want to filter the specific set of Azure resources sending logs to Dynatrace, you can use Azure resource tags. Tag rules are:

   * Azure resources with `Include` tags send logs to Dynatrace.
   * Azure resources with `Exclude` tags don't send logs to Dynatrace.
   * If there's a conflict between inclusion and exclusion rules, exclusion takes priority.
4. Select **Save**.

Azure Native Dynatrace Service automatically enables log forwarding in the Azure subscription where the Dynatrace resource is enabled. Log forwarding is enabled for all supported services and resources. Tag filtering rules can be defined to include or exclude certain Azure resources from sending logs.

Azure Native Dynatrace Service uses Dynatrace access token called `azure-native-integration` which is rotated every 24 hours.

## Create tags

* You can create [tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") either [during the Azure integration deployment](#setup) or [after deployment](#how-to-tags).

You can apply tags to your Azure resources, resource groups, and subscriptions to logically organize them into a taxonomy. You can specify tags for the new Dynatrace resource in Azure by adding custom key/value pairs:

* For **Name**, enter the name of the tag corresponding to the Azure Dynatrace resource (for example, `owner`).
* For **Value**, enter the value of the tag corresponding to the Azure Dynatrace resource (for example, the owner's email account).

If you don't set any tags, all logs from the monitored resources on your Azure subscription are sent to Dynatrace.

### How to create tags after deployment

On the Azure Portal, go to your new Dynatrace resource, and then select **Tags**. Alternatively, you can select **Monitored resources**, and then select **Edit tags** for the desired resources.

## Manage monitored resources in Azure Portal

After deploying the Azure Native Dynatrace Service, you can view, manage, and monitor your Azure resources, and you can install OneAgent on your Azure Virtual Machines and Azure App Services.

To view your list of resources, on the Azure Portal, go to your Dynatrace resource and select **Monitored resources**. You can filter the list of resources displayed by **Resource name** (Azure resource name), **Resource type** (Azure resource type), **Resource group** (resource group name for the Azure resource), **Region** (location of the Azure resource), and **Logs to Dynatrace** (whether the resource is sending logs to Dynatrace).

## Deploy OneAgent on Azure Virtual Machines and Azure App Services

* You can deploy OneAgent after the Azure integration deployment.

To monitor your Azure Virtual Machines or Azure App Services, you can install Dynatrace OneAgent on these resources as an extension.

Install OneAgent on Virtual Machine

Install OneAgent on App Service

1. On the Azure Portal, go to your Dynatrace resource and select **Virtual Machines**.
2. Select a Virtual Machine from the list, on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your Virtual Machine and go to **Extensions**.
* To uninstall OneAgent, select your Virtual Machine, and then select **Uninstall extension**.

1. On the Azure Portal, go to your Dynatrace resource and select **App Services**.
2. From the list, select the App Service on which you want to install the OneAgent extension.
3. Select **Install extension**.
4. Optional Select whether to enable log analytics.
5. Optional Provide a [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") for OneAgent.
6. Select **OK** to start the installation process.
7. When the installation is complete, the **OneAgent status** for the selected Virtual Machine displays **Installed**.

* To see details about the installed OneAgent, select your App Service and go to **Extensions**.
* To uninstall OneAgent, select your App Service, and then select **Uninstall extension**.

If you cannot see the App Service in Dynatrace after enabling the integration, restart your App Service plan.

To run OneAgent on Virtual Machine Scale Sets with Dynatrace Azure integration, use the [Dynatrace OneAgent extension for Virtual Machines](#vm) and create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

## Uninstall the Azure Native Dynatrace Service

To uninstall the Azure Native Dynatrace Service, you need to delete the Dynatrace resource. When the Dynatrace resource is deleted from Azure, logs and metrics are no longer sent to Dynatrace and all billing for Dynatrace through Azure Marketplace stops.

To delete the Dynatrace resource

1. On the Azure Portal, go to your Dynatrace resource and select **Overview**.
2. Select **Delete**.
3. Enter the name of the application you want to delete, then select **Delete**.

## How to request new features

If you have a feature request, use the [Microsoft Developer Communityï»¿](https://dt-url.net/po239hy) to suggest new features.

## Troubleshooting

* [I can't enable SSO integrationï»¿](https://dt-url.net/tq237c7)
* [I don't have permissions to configure SSO for a linked Dynatrace environmentï»¿](https://dt-url.net/3o038vp)
* [How can I get logs from an Azure subscription in another Azure tenant?ï»¿](https://dt-url.net/4rc37kk)
* [Azure resources not forwarding logs to Dynatraceï»¿](https://dt-url.net/il438i2)

## Log ingest FAQ

* [What are the limits for Azure Native Dynatrace Service log ingest?ï»¿](https://dt-url.net/ine37te)
* [How does the Azure Native Dynatrace Service logging impact Azure costs?ï»¿](https://dt-url.net/da2380g)
* [Isn't it cheaper to send data with the existing Dynatrace Azure log forwarding to Dynatrace SaaS in AWS rather than to use Azure Native Dynatrace Service?ï»¿](https://dt-url.net/bp038gb)

## Related topics

* [Microsoft Azure Integrations](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")


---
