---
title: Azure IoT Central Applications monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-central-applications
scraped: 2026-02-17T05:06:16.744824
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