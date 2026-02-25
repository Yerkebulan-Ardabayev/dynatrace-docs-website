---
title: Azure Logic Apps monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-logic-apps
scraped: 2026-02-25T21:30:02.181997
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