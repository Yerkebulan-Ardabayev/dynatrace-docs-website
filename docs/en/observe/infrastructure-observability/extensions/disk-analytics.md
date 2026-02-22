---
title: Disk Analytics extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/disk-analytics
scraped: 2026-02-22T21:13:03.324774
---

# Disk Analytics extension

# Disk Analytics extension

* Latest Dynatrace
* Extension
* Updated on Dec 18, 2025

Gain detailed visibility into Linux host local datastores where OneAgent is installed.

## Get started

### Overview

The Disk Analytics extension enables you to inspect and analyze physical and logical local data storage devices such as disks, partitions, volumes, and software or hardware raids on Linux machines where OneAgent is installed.

* Inspect disk hardware beyond just the mount points
* Detect disk-related problems directly from Dynatrace
* Detailed metrics for all partitions, software or hardware raid instances, and logical volumes. The details include mount points, file system type, partition sizes, and encryption status
* For devices with an assigned mountpoint, file system stats are presented

### Requirements

* OneAgent 1.233+
* Linux hosts only; see [OneAgent Linux supported technologies](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* Local disks only (network disks are not supported)
* Full-stack OneAgent deployments only. PaaS OneAgent deployments do not support the Disk Analytics extension

## Activation and setup

Before you can enable the extension, you need to install it: In Dynatrace Hub, select and install **Disk Analytics**.

After adding this extension to your environment, you also need to enable data collection in settings either at the host or host group level. The settings name is **Disk Analytics Extension**. This ensures full control of custom metrics and DDU consumption.

Once data collection is enabled on the target Linux hosts, you can view key metrics for all local disk instances and further inspect any of the disk instances on the selected hosts using the host page.

The classic host page does not display this information, but the information is also available using Data Explorer.

### Enable for host group

If you enable the extension for a host group, this setting overrides any setting on the environment level, but could in turn be overridden by a setting on the host level for any host in the host group.

To enable or disable the extension for all Linux hosts in a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Disk Analytics Extension**.
6. On the **Disk Analytics extension** page for the selected host group, turn the extension on or off as needed.

### Enable for host

If you enable the extension for a host, this overrides any setting on the host group or environment level.

To enable or disable the extension on one Linux host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Disk Analytics Extension** and turn the extension on or off as needed for the selected host.

## Details

### Metrics

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host on which you want to analyze local storage devices.
2. Select the **Linux disks** tab to scroll the page down to the **Linux disks** section.

### Licensing and costs

Disk Analytics extension metrics consume Davis data units (DDUs) for the selected hosts. For each disk device, one data point is sent per minute. A disk device includes each mount point, volume, partition, or raid instance.

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Gain detailed visibility into Linux host local datastores where OneAgent is installed.](https://www.dynatrace.com/hub/detail/disk-analytics/)