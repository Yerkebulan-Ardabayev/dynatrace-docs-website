---
title: Manage your monitoring environments
source: https://docs.dynatrace.com/managed/managed-cluster/operation/manage-your-monitoring-environments
scraped: 2026-05-12T11:22:12.862572
---

# Manage your monitoring environments

# Manage your monitoring environments

* Published Aug 10, 2017

You can easily create and manage your monitoring environments using the Cluster Management Console.

![Managed deployment](https://dt-cdn.net/images/managed-deployment-1329-1278e41da4.png)

Managed deployment

## Create an environment

1. Go to **Environments**.
2. Click the **+ Add another environment** button.
3. In the **Environment name** text box, type in a name for your environment.
4. Optional You can disable synthetic monitors by setting the **Enable synthetic monitors** switch to the **off** position.
5. Click **Save**.

## Configure an environment

After creating an environment and clicking **Save**, you are directed to the environmentâs configuration page. You can however access an environment's configuration page at any time. Go to **Environments** and select the environment you want to configure.

On the configuration page, you can set the total as well as the monthly and annual quotas for your environment.

### Total environment quotas

* **Host units** - The size of a host for licensing purposes (based on the amount of RAM provided by a host). For full-stack monitoring, a host with 16 GB of RAM (or any portion thereof) equates to 1 host unit. For cloud-infrastructure monitoring, a host with 16 GB of RAM (or any portion thereof) equates to 0.3 of a host unit.  
  For full details, see [How to calculate monitoring consumption](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").
* **Custom metrics** - Number of unique timeseries metrics in a 24-hour sliding window.  
  For full details, see [DDUs for metrics](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

### Monthly and annual quotas

* **User sessions** - Number of user sessions (i.e., "RUM sessions") to be monitored per month/year.  
  For details, see [DEM units - Real User Monitoring](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#rum "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").
* **Synthetic monitors** - Number of synthetic monitors to be performed per month/year.  
  For details, see [How to calculate monitoring consumption](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#synthetic "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").
* **Avg. daily log volume** - Volume of Log monitoring traffic per month/year.  
  For details, see [How to calculate monitoring consumption](/managed/license/monitoring-consumption-classic/log-monitoring-consumption-legacy#managed-log-storage "Understand how Log Monitoring consumption is calculated for Dynatrace versions 1.207 and earlier.").

Also, you can configure the storage settings, which include:

* **Transaction storage** - Volume of disk space to be reserved for transactions (for example, service calls, call stacks, and SQL statements).
* **Symbol files from mobile apps** - Amount of storage that can be consumed by the symbol files from mobile apps.
* **Service request level retention** - Amount of time the disk space for a service request is to be retained.
* **Service code level retention** - Amount of time the disk space for code-level visibility is to be retained.
* **Real user monitoring retention** - Amount of time the disk space for user sessions is to be retained.
* **Synthetic monitoring retention** - Amount of time the disk space for synthetic monitors is to be retained.
* **Session Replay retention** - Amount of time the disk space for Session Replay data is to be retained.
* **Log Monitoring storage** - Volume of disk space to be reserved for Log Monitoring.
* **Log Monitoring storage retention** - Amount of time the specified disk space for Log Monitoring is to be retained.

Once any one of these limits is consumed, the respective monitoring will no longer be available and you'll need to purchase more monitoring. To purchase Dynatrace, [contact Dynatrace Salesï»¿](https://dt-url.net/c901yj9). Your sales representative will provide you with further details.

### Assign environment permissions to user groups

Use these controls to assign environment permissions to defined user groups.  
For details, see [Manage user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

## Rename an environment

1. Go to **Environments**.
2. Select the environment you want to rename.
3. Click the small pencil icon next to the environment's name.
4. Type in the new name and click the tick mark button.

## Disable/delete an environment

1. Go to **Environments**.
2. Select the environment you want to disable/delete.
3. Click the Browse (**â¦**) button in the upper right corner.
4. Select **Disable environment** or **Permanently delete environment**.

## Access an environment

To access an environment from your Dynatrace Managed administration page:

1. Go to **Environments**.
2. Select the environment you want to access.
3. Click the **Go to environment** button in the upper right corner.  
   The monitoring data related to selected environment are displayed on your dashboard.

   ![Dashboard](https://dt-cdn.net/images/dashboard-2235-901caf1901.png)

   Dashboard

To access an environment from your Dynatrace Managed administration page another way:

1. Open the User menu by clicking the User icon in the upper-right corner.
2. Open the **Cluster Management** drop list.
3. Select the environment you want to access.

To return to your Cluster Management Console at any time:

1. From dashboard view, open the User menu by clicking the User icon in the upper-right corner.
2. Click the environmentâs name to open the drop list.
3. Select **Cluster Management**.

## Switch between environments

While on the dashboard view of a specific environment

1. Open the User menu by clicking the User icon in the upper-right corner.
2. Click the environmentâs name to open the drop list.
3. Select another environment you want to access.