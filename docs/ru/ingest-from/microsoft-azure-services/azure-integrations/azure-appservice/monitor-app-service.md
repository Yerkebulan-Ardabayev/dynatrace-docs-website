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