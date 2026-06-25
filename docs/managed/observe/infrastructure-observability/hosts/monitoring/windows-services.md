---
title: Classic Windows services monitoring
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/monitoring/windows-services
scraped: 2026-05-12T12:11:58.138818
---

# Classic Windows services monitoring

# Classic Windows services monitoring

* How-to guide
* 6-min read
* Published Jul 10, 2020

Deprecated

The Classic Windows services feature described below is deprecated. Instead, use [OS services monitoring](/managed/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

Dynatrace provides out-of-the-box availability monitoring of Windows services.

To monitor the availability of a service, specify the `Service name` and `Display name`. To simplify management in a large-scale environment, adjust settings on the host-group level.

Changes to OS service monitoring

In Dynatrace versions 1.214-1.218, Windows service availability monitoring configuration at the host level took precedence over the host group configuration, which in turn took precedence over the environment configuration. In Dynatrace version 219+, this is no longer the case. Configurations at the environment, host group, and host level are combined as described below.

You can configure service monitoring at the environment, host group, and host levels. Service monitoring is a combination of the settings you make at any of the three levels.

Example

Suppose you have the following:

* Services A, B, C, D, and E
* Host groups J and K
* Hosts X and Y
* Host X is a member of host group J
* Host Y is not a member of any host group

If you configured the following:

* Monitor services A and B at the environment level
* Monitor services B and C for host group J
* Monitor services A and D for host X
* Monitor services A and E for host Y

You would monitor the following:

* Monitor services A and B on all hosts
* Monitor services A, B, and C on all hosts belonging to group J
* Monitor services A, B, C, and D on host X
* Monitor services A, B, and E on host Y

## Monitor a service

To monitor an OS service

1. Determine the service name. Be sure to use the exact OS-provided service name, because this is how Dynatrace identifies your service.

   To determine a Windows service name

   1. In Windows, open **Services** and find the service.
   2. Check the service properties. In this example, we display the properties of Windows License Manager Service to see that the Windows service name is `LicenseManager`.

      ![Windows services availability: example service name](https://dt-cdn.net/images/windowsservicenameexample-1212-546952d557.png)

      Windows services availability: example service name
2. In Dynatrace, go to **OS service monitoring** for the level you are configuring.

   Host level

   1. Go to **Hosts**.
   2. Optional Filter by `Operating system` (Windows).
   3. Find your host and select it to display the host page.
   4. On the host page, open the browse menu (**â¦**) and select **Settings**.
   5. Select the **OS service monitoring** tab.

   Host-group level

   1. Go to **Hosts**.
   2. Optional Filter by `Operating system` (Windows).
   3. Filter by `Host group` and start typing the name of a host group to find and select a host group name.
   4. Open any host in that host group.
   5. On the host page, expand the **Properties and tags** section and select the host group name.
   6. Select the **OS service monitoring** tab.

   Environment level

   Go to **Settings** > **Monitoring** > **OS services monitoring**.
3. On **OS service monitoring** for the level you are configuring, select **Add new service** and specify the service you want to monitor.

   * **Service name** is the exact service name as determined in step 1.
   * **Display name** is the freeform label that will be displayed in the table of monitored services.
4. Select **Save changes**.

## Manage monitored OS services

To manage the OS services you monitor

1. In Dynatrace, go to **OS service monitoring** for the level you are configuring.

   Host level

   1. Go to **Hosts**.
   2. Optional Filter by `Operating system` (Windows).
   3. Find your host and select it to display the host page.
   4. On the host page, open the browse menu (**â¦**) and select **Settings**.
   5. Select the **OS service monitoring** tab.

   Host-group level

   6. Go to **Hosts**.
   7. Optional Filter by `Operating system` (Windows).
   8. Filter by `Host group` and start typing the name of a host group to find and select a host group name.
   9. Open any host in that host group.
   10. On the host page, expand the **Properties and tags** section and select the host group name.
   11. Select the **OS service monitoring** tab.

   Environment level

   Go to **Settings** > **Monitoring** > **OS services monitoring**.
2. The OS services you monitor are displayed in a table under the **Add new service** button.

   * To filter the table, type a search string in the **Filter itemsâ¦** box
   * To stop monitoring a listed service, turn the **Enabled** setting off.
   * To delete a service from the table, select the delete button in the **Delete** column
   * To view and edit details, select the expand control in the **Details** column. You can change the service name or edit the display name.

## Metric events for alerting on service availability

After you add a service, you can create a custom event for the availability of your service based on the **OS Service availability** metric.

Provide the following information:

* **Category** - Hosts
* **Metric** - OS Service availability
* **Aggregation** - Average
* **Dimension** - Service name of your choice

See [Metric events for alerting](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") for details on creating and customizing metric events for alerting.

## Configure at scale using Settings API

You can use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure your service availability monitoring at scale.

1. To learn the schema, use [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:os.services.monitoring` as the schemaId.
2. Based on the `builtin:os.services.monitoring` schema, create your configuration object.
3. To create your configuration, use [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").