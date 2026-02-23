---
title: Azure Stream Analytics monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics
scraped: 2026-02-23T21:37:05.498398
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