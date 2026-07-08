---
title: Microsoft Azure Arc-enabled servers
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers
---

# Microsoft Azure Arc-enabled servers

# Microsoft Azure Arc-enabled servers

* How-to guide
* 4-min read
* Published Dec 10, 2024

## Capabilities

* Full-stack monitoring powered by OneAgent
* [Extensions for easy deployment of OneAgent](#installation)
* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more
* [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported

## Prerequisites

* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
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

## Install Dynatrace OneAgent VM extension

There are several ways to install the Dynatrace OneAgent VM extension: through Azure portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.

Azure portal

Azure CLI 2.0

ARM template

### Add the extension to an existing VM

1. In the Azure portal, go to an existing Azure Arc Machine resource.
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



--name “<Extension-Type>”



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
| hostGroup | Optional | Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |

Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.

The [JSON file﻿](https://dt-url.net/9f03wr8) for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. The placement of the JSON file affects the value of the resource name and type.

Example

The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the `"resources": []` object of the virtual machine.'

```
{



"$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",



"contentVersion": "1.0.0.0",



"parameters": {



"vmName": {



"type": "string"



},



"location": {



"type": "string"



},



"tenant": {



"type": "string"



},



"token": {



"type": "securestring"



},



"server": {



"type": "string",



"defaultValue": ""



}



},



"resources": [



{



"name": "[concat(parameters('vmName'),'/<Extension-Type>')]",



"type": "Microsoft.HybridCompute/machines/extensions",



"location": "[parameters('location')]",



"apiVersion": "2022-03-10",



"properties": {



"publisher": "dynatrace.ruxit",



"type": " <Extension-Type>",



"autoUpgradeMinorVersion": true,



"settings": {



"tenantId": "[parameters('tenant')]",



"server": "[parameters('server')]"



},



"protectedSettings": {



"token": "[parameters('token')]"



}



}



}



]



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