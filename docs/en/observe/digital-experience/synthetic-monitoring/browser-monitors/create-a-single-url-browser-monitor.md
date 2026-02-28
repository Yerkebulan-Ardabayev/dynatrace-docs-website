---
title: Create a single-URL browser monitor
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor
scraped: 2026-02-28T21:18:31.079382
---

# Create a single-URL browser monitor

# Create a single-URL browser monitor

* How-to guide
* 3-min read
* Updated on Aug 19, 2025

Synthetic monitoring gives you the option of creating two kinds of browser monitorsâsingle-URL and clickpathsâto check the availability and performance of your web application at regular intervals. Single-URL browser monitors conduct availability tests of a single page of your website or web application. You also have the option of checking performance.

## Create a single-URL browser monitor

1. Go to **Synthetic Classic**.
2. Select **Create a synthetic monitor** at top right > **Create a browser monitor**.
3. On the Configure a browser monitor page, type in the **URL** you want to monitor and either use the default **Name** or provide your own.

   To enhance synthetic monitor security, Dynatrace blocks monitors from sending requests to a local host (for example, `localhost` or `127.0.0.1`).
4. Select **Add tag** to apply manually created tags to the monitor. You can choose from autocomplete suggestions as you type or create your own. (After the monitor has been created, you can manage tags from the [Synthetic details page](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.").
5. [Configure your monitor](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") appropriately, including selecting the profile of your emulated device, authentication, and other settings.

   ![Configure a browser monitor](https://dt-cdn.net/images/configurebrowsermonitor1-1665-749a574062.png)

   Web form authentication is no longer supported for the single-URL browser monitors. You can instead create [browser clickpath](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Learn how to record a browser clickpath to monitor the availability and performance of your application.") monitors for the test scenarios that require web form login. Your previously configured single-URL monitors will run as before, but we recommend to re-record them as clickpaths to clearly separate each step of the login process.

   Re-recording is required if you want to modify any part of your monitor's configuration. You can no longer save changes in their current format.

   Starting from Dynatrace version 1.324+, the single-URL monitors with the web form login will be automatically updated by adding a free JavaScript step to support the login process.
6. Choose **Next** to continue configurationâselect monitor locations and frequency. See [Configure browser monitors](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.") for details.

   ![Monitor frequency and locations](https://dt-cdn.net/images/syntheticfrequencylocations2-2223-297d2c4656.png)
7. Select **Next** at the bottom of the page to view the monitor summary.
8. On the Summary page, you can review and change your configuration (**Change URL or name**; **Change configuration**).

   ![Single-URL browser monitor summary](https://dt-cdn.net/images/summarysingleurl-2246-6f4d67b798.png)
9. At the bottom of the page, select **Create browser monitor**. Within a few minutes, you'll [receive monitoring data](#view-the-analytics-of-a-browser-monitor) for your new browser monitor.

While you cannot play back a single-URL browser monitor locally, you can [execute it on demand](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations") from assigned locations.

## View the analytics of a browser monitor

1. Go to **Synthetic Classic**.
2. Optional Select **Browser** in the left menu to filter by single-URL browser monitors.
3. From the list of monitors, select the browser monitor you want to examine. You're directed to the [Synthetic details page](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") for the browser monitor.

The details page of each monitor provides detailed results, for example, availability metrics and problems detected.

## Disable or delete a browser monitor

Monitors are enabled by default when you create them.

Disabling a synthetic monitor suspends further executions but retains the monitor and its measurement data. Any open performance and availability problems time out when a monitor is disabled (see [Synthetic calculations](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.") for details). Deletion removes a monitor and its associated measurement data; this is irreversible. Before deleting a monitor, we recommend that you disable it first and ensure that you no longer require its measurement data.

To disable or delete a monitor

1. Go to **Synthetic Classic**.
2. Opt to view your monitors in list format.
3. Select the check box for the monitor you want to delete or disable.
4. Select **Delete** or **Disable** in the lower-left corner.

   ![Disable browser monitor](https://dt-cdn.net/images/disabledeletemonitor1-891-3c3e768323.png)

You can also disable or delete a monitor from the [details page](/docs/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.").

1. Go to **Synthetic Classic**.
2. Select the monitor you're interested in.
3. Select the **Browse** button (**â¦**) and select either **Disable** or **Delete**.

[Synthetic monitor execution may be disabled during a maintenance window](/docs/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring metric calculations.") in maintenance window settings.

## Related topics

* [Synthetic Monitors API](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")