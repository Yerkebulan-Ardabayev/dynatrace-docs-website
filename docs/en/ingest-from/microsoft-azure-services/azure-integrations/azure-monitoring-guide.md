---
title: Monitor Azure services with Azure Monitor metrics
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide
scraped: 2026-02-17T21:19:44.980746
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