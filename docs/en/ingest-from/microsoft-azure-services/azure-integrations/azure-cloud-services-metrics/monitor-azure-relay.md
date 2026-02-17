---
title: Azure Relay monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-relay
scraped: 2026-02-17T05:00:42.751277
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