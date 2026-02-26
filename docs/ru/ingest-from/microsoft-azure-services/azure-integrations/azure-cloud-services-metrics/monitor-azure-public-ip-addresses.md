---
title: Azure Public IP Address monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-public-ip-addresses
scraped: 2026-02-26T21:22:45.140599
---

# Azure Public IP Address monitoring

# Azure Public IP Address monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jul 27, 2020

Dynatrace ingests metrics from Azure Metrics API for Azure Public IP Address. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.199+
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

![IP-dash](https://dt-cdn.net/images/dashboard-21-1352-94948a295c.png)

## Available metrics

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| ByteCount | Total number of bytes transmitted within time period | Byte, Port, Direction | Applicable |
| BytesDroppedDDoS | Inbound bytes dropped DDoS | BytePerSecond |  |
| BytesForwardedDDoS | Inbound bytes forwarded DDoS | BytePerSecond |  |
| BytesInDDoS | Inbound bytes DDoS | BytePerSecond |  |
| DDoSTriggerSYNPackets | Inbound SYN packets to trigger DDoS mitigation | PerSecond |  |
| DDoSTriggerTCPPackets | Inbound TCP packets to trigger DDoS mitigation | PerSecond |  |
| DDoSTriggerUDPPackets | Inbound UDP packets to trigger DDoS mitigation | PerSecond |  |
| IfUnderDDoSAttack | Under DDoS attack or not | Count |  |
| PacketCount | Total number of packets transmitted within time period | Count, Port, Direction | Applicable |
| PacketsDroppedDDoS | Inbound packets dropped DDoS | PerSecond |  |
| PacketsForwardedDDoS | Inbound packets forwarded DDoS | PerSecond |  |
| PacketsInDDoS | Inbound packets DDoS | PerSecond |  |
| SynCount | Total number of SYN Packets transmitted within time period | Count, Port, Direction | Applicable |
| TCPBytesDroppedDDoS | Inbound TCP bytes dropped DDoS | BytePerSecond |  |
| TCPBytesForwardedDDoS | Inbound TCP bytes forwarded DDoS | BytePerSecond |  |
| TCPBytesInDDoS | Inbound TCP bytes DDoS | BytePerSecond |  |
| TCPPacketsDroppedDDoS | Inbound TCP packets dropped DDoS | PerSecond |  |
| TCPPacketsForwardedDDoS | Inbound TCP packets forwarded DDoS | PerSecond |  |
| TCPPacketsInDDoS | Inbound TCP packets DDoS | PerSecond |  |
| UDPBytesDroppedDDoS | Inbound UDP bytes dropped DDoS | BytePerSecond |  |
| UDPBytesForwardedDDoS | Inbound UDP bytes forwarded DDoS | BytePerSecond |  |
| UDPBytesInDDoS | Inbound UDP bytes DDoS | BytePerSecond |  |
| UDPPacketsDroppedDDoS | Inbound UDP packets dropped DDoS | PerSecond |  |
| UDPPacketsForwardedDDoS | Inbound UDP packets forwarded DDoS | PerSecond |  |
| UDPPacketsInDDoS | Inbound UDP packets DDoS | PerSecond |  |
| VipAvailability | Average IP address availability per time duration | Percent, Port | Applicable |