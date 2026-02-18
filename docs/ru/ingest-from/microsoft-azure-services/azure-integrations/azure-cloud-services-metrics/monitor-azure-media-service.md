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