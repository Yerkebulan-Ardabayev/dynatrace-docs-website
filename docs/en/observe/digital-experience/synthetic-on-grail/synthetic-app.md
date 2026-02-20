---
title: Synthetic app
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app
scraped: 2026-02-20T21:08:56.481003
---

# Synthetic app

# Synthetic app

* Latest Dynatrace
* App
* 7-min read
* Updated on Jul 10, 2025

With the ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** app you can create and manage synthetic monitors.

Prerequisites

### Permissions

The following table describes the required permissions.

Permission

Description

geolocation:locations:lookup

allows querying geographic location data for private locations

storage:buckets:read

allows querying data from Grail

storage:entities:read

allows querying monitored entities from Grail

storage:metrics:read

allows querying metrics from Grail

storage:events:read

allows querying events from Grail

storage:user.events:read

allows querying events from Grail

storage:files:read

allows querying events from Grail

document:documents:write

allows creating and updating filter sets

document:documents:read

allows querying stored filter sets

document:documents:delete

allows deleting filter sets

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Use cases

![List of synthetic monitors with powerful filters, key metrics, and a preview panel showing config details and recent execution results](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.synthetic/media/adca5313-1eec-4f64-b9b2-9ded18dd78b7.png)![Shows execution results for a test, highlighting availability and performance, with details at both monitor and step levels](https://cdn.hub.central.dynatrace.com/hub/health_QnbCRwv.png)![Compare past HTTP monitor runs to spot slowdowns, failures, or improvements, with diffs in load times, codes, errors, and payloads](https://cdn.hub.central.dynatrace.com/hub/compare_1ViF4zz.png)![Define this monitorâs scope and config: frequency, locations, success criteria, and rules for triggering problems](https://cdn.hub.central.dynatrace.com/hub/configuration_6h5FfCa_BYo9Dvp.png)![Configure this private synthetic location: geo position, assigned ActiveGates, and rules for selfâmonitoring problem triggers](https://cdn.hub.central.dynatrace.com/hub/private_h1joYiz.png)

1 of 5List of synthetic monitors with powerful filters, key metrics, and a preview panel showing config details and recent execution results

### Navigation and filtering

The synthetic monitors page is the landing page of the ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** app and is the control center for your synthetic monitors. By default, the page displays all monitors in your environment, active or inactive, in a [table](#table) with key availability and performance results, so you can check the health of your monitors at a glance.
Powerful and flexible [filters](#filters) enable you to narrow your search for synthetic monitors.

To find out how to create a new monitor, see [Create monitors](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app#create-monitors "View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.").

### Monitors table

By default, monitors with open problems (issues) are displayed alphabetically at the top of the table. Next, enabled monitors with no problems are displayed alphabetically, followed by disabled monitors displayed alphabetically.

You can hide and sort columns in ascending or descending order. Select **Columns** in the top-right corner of the table to select which columns to display or hide.

Pagination controls at the bottom of the monitor table allow you to specify the number of **rows per page** and to move through the monitor table from page to page.

The columns display the following information for each monitor.

* **Monitor name**âSelect to view a quick overview of the monitor to the right of the Synthetic monitors page
* **Created**âmonitor creation date and time
* **Last modified**âID of the user who last edited the monitor and the date and time of modification
* **ID** - full monitor identifier
* **Last execution**âdate and time of the most recent execution from any location
* **Type**âmonitor type, for example, `HTTP`
* **Frequency**âexecution frequency or `On demand`, as specified in the monitor configuration
* **Availability**âaverage availability during the selected timeframe
* **Duration**âaverage performance during the selected timeframe in seconds

#### Monitor preview

In the ![Synthetic Classic](https://dt-cdn.net/images/synthetic-512-83ec796e54.png "Synthetic Classic") **Synthetic** app, to display the preview panel for a monitor, select the monitor's name in the **Monitor name** column of the **Synthetic monitors** page.

To browse between your monitors, open the preview panel for any monitor and then select another monitor name to switch the preview to the newly selected monitor. Filters are persistent.

The preview panel shows:

* Tiles for important information at a glance:

  + Outage/Available/No dataâthe monitor availability status at the moment of the last executed test
  + Active issuesâthe number of issues being observed at the moment
  + Affected locationsâthe number of locations where outages happened within specific timeframe
  + Availabilityâthe monitors availability rate in percent within specific timeframe
  + Total downtimeâthe total outage time for all locations within specific timeframe
  + Durationâthe average response time for all locations within specific timeframe
* A list of problems, including the problem start date and duration, or **No problems found**. To analyze a problem in the **Problems** app, select the problem link in the list.
* A list of changes. In latest Dynatrace, this section displays changes to the monitor: when it was changed, who changed it, and what they changed. You can only access changes from a specified timeframe.
* Properties such as monitor type, locations, requests in last execution, frequency, steps, and tags.

Use the controls in the upper-right corner of the preview panel to:

* Edit the selected monitor
* Delete the selected monitor
* Enable a disabled monitor
* Disable an enabled monitor
* Display the reporting page for the selected monitor (see below)
* Close the preview panel

### Filters

Filters allowing multiple selections help you find the monitors you're looking for. You can also save frequently used filters. Expand ![Open Dashboards panel](https://dt-cdn.net/images/dashboards-app-dashboards-panel-open-6c03b43117.svg "Open Dashboards panel") or collapse ![Close Dashboards panel](https://dt-cdn.net/images/dashboards-app-dashboards-panel-close-78d6b527ad.svg "Close Dashboards panel") the filters to focus on search or results, as required. The filters are automatically collapsed when viewing the quick overview for a monitor.

The following filter categories (each with multiple options) allow you to search for monitors.

* **Type**âmonitor type
* **Ongoing issues**âmonitors with and without availability or performance problems
* **Frontend application**âassociated [RUM](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels.") application
* **Status**âwhether monitors are active or inactive (disabled)
* **Locations**â[public](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") and [private](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") monitoring locations
* **Device profile**âfor example, `desktop`, `Apple iPhone 8`
* **Last editor**âID of the user who last edited a monitor
* **Tags**âvalues or key-value pairs applied to monitors; you can choose tags to include or exclude from your search.
* **Edited during the timeframe**âmonitors that were or were not edited during the selected global timeframe
* **ISP / Cloud provider**âof public Synthetic locations
* **Frequency**âmonitoring frequency

#### How filters work

Within each category, you can select multiple filters. For example, when selecting monitors by **Type**, you can opt to view **HTTP** as well as **DNS** monitors. Within a category, filters are applied using the `OR` logicâmonitors matching any selection are displayed.

The filter options shown in most categories depend on your monitors; only those filters relevant to your monitors are available. For example, if you have no HTTP monitors, you won't see the **HTTP** option to filter by.

The number of monitors matching each filter is displayed. For example, the list of **Locations** shows the number of monitors per location. This number is dynamically adjusted based on your filter selections in other categories.

You can select filters in multiple categories. Filter categories are applied using the `AND` logic. For example, if you select all **Network availability** monitors (**DNS**, **ICMP**, and **TCP**) and two tags, `IP`, and `host-group`, the resulting list contains network availability monitors with either the `IP` or the `host-group` tags.

#### Filter sets

You can save combinations of filters as named filter sets for quick access to frequently used search criteriaâselect **Save new filter** and provide a filter name. You can set one filter set as default to be applied each time you go to the ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** app.

Select **More** ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") next to a filter set for additional actions such as **Set as default**, **Rename**, **Duplicate**, or **Delete**.

#### Filter bar

The filter bar ![Variable](https://dt-cdn.net/images/dashboards-app-dashboard-add-variable-821b40325c.svg "Variable") at the top of the page displays a fixed filter for searching by monitor name: select **Filter by name** and enter your search string. Any additional filters or [filter sets](#filter-sets) you apply are displayed in the filter bar, from which you can clear applied filters.

### Manage synthetic monitors

In the **Create monitor** section, you can choose the type of synthetic monitor that you want to create.

### Create monitors

To create a monitor:

1. Select **+New monitor** in the upper-right corner of ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.
2. Choose one of the following:

* Browserâchoosing this option will allow you to create a browser monitor in **Synthetic Classic**. Learn how to [Create a single-URL browser monitor](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.").
* HTTPâchoosing this option will allow you to create an HTTP monitor in ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**. Learn how to [Create and configure an HTTP monitor](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor "Learn how to set up and edit an HTTP monitor to check the performance and availability of your site.").
* Network availabilityâchoosing this option will allow you to create a NAM monitor in ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**. Learn how to [Configure a NAM monitor](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor "Learn how to set up a NAM monitor to check the performance and availability of your site.").

### Reporting

For each monitor type, you can display a reporting page. See

* NAM monitor [reporting](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring#reporting "ICMP, TCP, and DNS synthetic monitors") in **Synthetic**.
* HTTP monitor [reporting](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors "Learn about the Synthetic details page for HTTP monitors.") in **Synthetic**.
* HTTP monitor [reporting](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Learn about the Synthetic details page for HTTP monitors.") in **Synthetic Classic**.
* Browser monitor [reporting](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") in **Synthetic Classic**.

### Total downtime calculation for synthetic monitors

The total monitoring time is divided into minute-level data points. All data points count as executions, although they don't necessarily coincide with actual executions.

On the screen below, the blue data points coincide with actual executions, and the white data points don't.

![Up/down executions and data points](https://dt-cdn.net/images/screenshot-2025-07-09-114246-1857-8ed42fbafd.png)

For example, if a monitor is set to execute tests every five minutes, every fifth data point (blue) coincides with an actual execution. All data points following the first failed ("down") execution and preceding the first successful ("up") execution count as "down." Thus, the total downtime is calculated as follows:

Total downtime = the first actual down execution + all following down data points.

![Total downtime displayed in the detailed interface](https://dt-cdn.net/images/total-downtime-1585-bf2c26bbf9.png)

## Learning modules

Go through the following process to learn using the ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** app:

[01HTTP monitors reporting results

* Reference
* Learn about the Synthetic details page for HTTP monitors.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/synthetic-details-for-http-monitors)[02Browser monitors reporting results

* Reference
* Learn about the Browser details page for Browser monitors.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting)[03Create and configure a browser monitor

* How-to guide
* Learn how to create and configure a browser monitor to check the performance and availability of your site.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-configure-browser-monitors)[04NAM monitors results reporting

* Reference
* View the synthetic monitors in your environment, search for monitors, and get a quick overview of a selected monitor.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/nam-monitors-results-reporting-synthetic-app)[05On-demand monitor executions

* How-to guide
* Learn about how to perform on-demand executions.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/on-demand-executions)[06Private synthetic locations

* How-to guide
* Learn how to manage private locations in the Synthetic app.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations)[07Create and configure an HTTP monitor

* How-to guide
* Learn how to set up and edit an HTTP monitor to check the performance and availability of your site.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-and-configure-an-http-monitor)[08Create a NAM monitor

* How-to guide
* Learn how to set up a NAM monitor to check the performance and availability of your site.](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/create-a-nam-monitor-synthetic-app)

## Use cases

* Automatically monitor and test application availability and performance across production and development environments.
* Fix issues and optimize digital experience before users are affected.
* Synthetic capabilities are extended to monitor infrastructure and services that don't expose HTTPS-powered interfaces.sdsd

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

View the status of all data centers and hosts and identify the root cause of infrastructure problems.](https://www.dynatrace.com/hub/detail/synthetic-preview/?internal_source=doc&internal_medium=link&internal_campaign=cross)