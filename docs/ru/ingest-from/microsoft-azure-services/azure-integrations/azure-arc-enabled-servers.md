---
title: Microsoft Azure Arc-enabled servers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers
scraped: 2026-03-01T21:21:11.330469
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