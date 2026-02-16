---
title: Azure Virtual Network Gateway monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-virtual-network-gateways
scraped: 2026-02-16T09:27:16.808988
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