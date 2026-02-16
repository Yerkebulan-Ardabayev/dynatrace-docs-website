---
title: Azure NetApp Files monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-netapp-files
scraped: 2026-02-16T09:38:47.236567
---

# Azure NetApp Files monitoring

# Azure NetApp Files monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Aug 19, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Azure NetApp Files. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

* Dynatrace version 1.200+
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

![Netapp](https://dt-cdn.net/images/image-9-2557-4d14b532da.png)

## Available metrics

## Azure NetApp Files

| Name | Description | Unit | Recommended |
| --- | --- | --- | --- |
| VolumePoolAllocatedSize | Provisioned size of the pool | Byte | Applicable |
| VolumePoolAllocatedUsed | Allocated used size of the pool | Byte | Applicable |
| VolumePoolTotalLogicalSize | Sum of the logical size of all the volumes belonging to the pool | Byte | Applicable |
| VolumePoolTotalSnapshotSize | Sum of snapshot size of all volumes in this pool | Byte | Applicable |

## Azure NetApp Files - Volumes

| Name | Description | Unit |  |
| --- | --- | --- | --- |
| AverageReadLatency | The average time for reads from the volume in milliseconds | MilliSecond | Applicable |
| AverageWriteLatency | The average time for writes from the volume in milliseconds | MilliSecond | Applicable |
| CbsVolumeBackupActive | Volume backup active state | Count |  |
| CbsVolumeLogicalBackupBytes | Logical bytes backed up | Byte |  |
| CbsVolumeOperationComplete | Operation state | Count |  |
| CbsVolumeOperationTransferredBytes | Bytes transferred for operation | Byte |  |
| CbsVolumeProtected | Volume protected state | Count |  |
| ReadIops | Read IOPS | PerSecond | Applicable |
| VolumeAllocatedSize | Volume allocated size | Byte | Applicable |
| VolumeLogicalSize | Volume consumed size | Byte | Applicable |
| VolumeSnapshotSize | Volume snapshot size | Byte |  |
| WriteIops | Write IOPS | PerSecond | Applicable |
| XregionReplicationHealthy | Checks if volume replication status is healthy | Count |  |
| XregionReplicationLagTime | Volume replication lag time | Second |  |
| XregionReplicationLastTransferDuration | Volume replication last transfer duration | Second |  |
| XregionReplicationLastTransferSize | Volume replication last transfer size | Byte |  |
| XregionReplicationRelationshipProgress | Volume replication progress | Byte |  |
| XregionReplicationRelationshipTransferring | Checks if volume replication is transferring | Count |  |
| XregionReplicationTotalTransferBytes | Volume replication total transfer | Byte |  |