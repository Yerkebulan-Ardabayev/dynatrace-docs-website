---
title: Enable service monitoring
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring
---

# Enable service monitoring

# Enable service monitoring

* How-to guide
* 1-min read
* Updated on Apr 02, 2025

To enable monitoring for this service, you first need to [set up integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.").

## Add the service to monitoring

In order to view the service metrics, you must add the service to monitoring in your Dynatrace environment.

To add a service to monitoring

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, select **Edit** for the desired Azure instance.
3. Go to **Services** > **Add service**, choose the desired service name from the list, and select **Add service**.
4. Select **Save changes** to save your configuration.

## Configure service metrics

Once you add a service, Dynatrace starts automatically collecting a suite of metrics for this particular service. These are **recommended** metrics.

### Recommended metrics

* Are enabled by default
* Can't be disabled
* Can have recommended dimensions (enabled by default, can't be disabled)
* Can have optional dimensions (disabled by default, can be enabled)

### Optional metrics

Apart from the recommended metrics, most services have the possibility of enabling **optional** metrics.

* Can be added and configured manually

### Add and configure metrics

1. Go to **Settings** > **Cloud and virtualization** > **Azure**.
2. On the Azure overview page, scroll down and select **Edit** for the desired Azure instance.
3. Go to **Services** and select **Manage services**.
4. To add a metric, select the service for which you want to add metrics.
5. Select **Add new metric**.
6. From the menu, select the metric you want.
7. Select **Add metric** to add the metric to monitoring.
8. To configure a metric, select **Edit**.
9. Select **Apply** to save your configuration.

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to **Technologies & Processes**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**…**) and select **Clone**.  
To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (**…**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure