---
title: Manage private Synthetic locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations
scraped: 2026-03-01T21:20:35.171254
---

# Manage private Synthetic locations

# Manage private Synthetic locations

* How-to guide
* 10-min read
* Updated on Feb 11, 2026

[Add a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#add "Learn how to create a private location for synthetic monitoring.") as well as analyze and manage capacity usage in the **Private synthetic locations** global settings page (select the **Private synthetic locations** settings page from search results).

Early Adopter

Synthetic-enabled ActiveGate version 1.217+

Dynatrace version 1.218+

## Overall location status

The colorized overall location status is displayed only in the previous Dynatrace.

Private Synthetic locations in your environment are listed with green, yellow, red, or gray indicators of overall capacity usage status. You can see the type and number of synthetic monitors as well as the number of Synthetic-enabled ActiveGates assigned to each location.

Select the monitor type (**HTTP** or **Browser**) to see the list of synthetic monitors of that type at that location.

You can select multiple locations for bulk management of [outage handling](#outage-handling). Select the checkbox next to each location you want to manage.

![Private Synthetic location settings](https://dt-cdn.net/images/pvtsyntheticlocations-1400-8d3260f571.png)

The colored status indicator for each location shows if it's overloaded in terms of capacity usage, enabling you to make educated decisions about adding more ActiveGates to run additional monitors. (Also check [system and hardware requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").)

For usage calculations on each ActiveGate, Dynatrace allocates CPU and RAM resources for running each type of monitor. Resource allocation per monitor type is resolved into the maximum number of simultaneous monitor executions that may take place at any given point in time. Actual capacity usage calculation per monitor type (see [Location details](#location-details) below) is based on the number of concurrently executed monitors compared to the maximum allowed simultaneous executions over the preceding 30 minutes.

For example, an ActiveGate might support two simultaneous browser monitor executions at a given point. However, depending on the duration of the monitors being executed, this could equate to more than two monitors being executed within a given timeframe. For example, one 55-second monitor and three 10-second monitors could be executed within a single minute with no more than two simultaneous executions at any given point.

Metrics for capacity usage per monitor type provide an accurate view of Synthetic location health and can be used for charting and alertingâbe sure to split these metrics by location (see [Location details](#location-details) below).

## Location details

Location details in latest Dynatrace

The instructions below describe how to view location details in the previous Dynatrace. To learn how to view location details in the latest Dynatrace, see [Private synthetic locations on Grail](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#location-details "Learn how to manage private locations in the Synthetic app.").

Select a location to see the breakdown of its overall status into capacity usage per monitor type. For each of these monitor types, you can see the number of monitors and hourly scheduled executions as well as the capacity use percentage.

* HTTP monitors
* High-resource HTTP monitors
* Browser monitors
* Network Availability monitors

You can't see usage data per monitor type when all ActiveGates or Synthetic engines at a location are down.

The ActiveGates assigned to the location are listed and displayed in red when a Synthetic engine or an ActiveGate itself is offline; the **Status** column shows a corresponding message. You can add or delete ActiveGates from here. Note that the **Add ActiveGate** button is disabled when no ActiveGates are available to be assigned to a locationâyou can check for this in **Deployment Status**.

![Private location details in previous Dynatrace](https://dt-cdn.net/images/screenshot-2025-10-22-171901-1356-64e2b3b050.png)

Metrics for the health status of each monitor type are available for charting and alerting. For example, choose the **Synthetic - Browser - Engine Utilization** metric in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.") or [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."). We strongly recommend splitting these metrics by location to get an accurate view of location health.

![Synthetic monitors metrics in Data Explorer Classic](https://dt-cdn.net/images/screenshot-2025-10-22-174729-1400-717532af10.png)

### Browser autoupdate

You can **Enable Chrome(-ium) auto-update** at the location level, that is, for all ActiveGates assigned to a private location. The browser autoupdate takes place during manual as well as automatic ActiveGate and Synthetic engine updates.

As we recommend using the [latest supported browser version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for the smooth and secure execution of browser monitors from your private location, the browser autoupdate is turned on by default for locations with Linux-based ActiveGates. If you don't want the browser to be updated automatically, for example, to use a specific browser version, or if you have offline environments, turn off the switch **before triggering an ActiveGate update**.

This setting only applies to Linux-based ActiveGates; on Windows-based ActiveGates, the browser is always updated during Synthetic engine updates. If your location has only Windows-based ActiveGates, the toggle is turned on but grayed out.

Successful browser autoupdate requires access to OS (system) repositories for browser dependencies and access to `https://synthetic-packages.s3.amazonaws.com` for browser packages. If you've enabled a [custom local repository](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."), browser packages (but not dependencies) need to be available at the specified HTTP server address. See [Browser autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Analyze and manage capacity usage at your private Synthetic locations.").

You will see a message if the browser autoupdate fails for this or other reasonsâwe recommend either meeting the requirements for autoupdate (such as access to repositories) or disabling browser autoupdate for your private location.

* We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and browser versions updatedâDynatrace supports browser versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for a specific ActiveGate release. If you don't opt for the browser autoupdate, you can [update browser manually](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Analyze and manage capacity usage at your private Synthetic locations.").
* If you disable the browser autoupdate, you can [manually update the browser](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Analyze and manage capacity usage at your private Synthetic locations.") per ActiveGate. However, browser autoupdate is required when using [custom repositories](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."). See [Browser autoupdate from a custom repository](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Analyze and manage capacity usage at your private Synthetic locations.").
* Autoupdate works to update the browser to the latest version that Dynatrace provides for an ActiveGate release. In some cases, this might be different from the [latest Dynatrace-supported browser version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for the ActiveGate release.

Also, check our information on [installing the browser and other dependencies manually (Linux only)](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#manual "Learn how to create a private location for synthetic monitoring.").

### Location outage handling

Location outage handling in latest Dynatrace

The instructions below describe how to handle outages in the previous Dynatrace. To learn how to handle outages in the latest Dynatrace, see [Private synthetic locations on Grail](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#location-outage-handling "Learn how to manage private locations in the Synthetic app.").

For each location, enable the corresponding switches to generate problems when a location or any of its ActiveGates/Synthetic engines are unavailable:

* You can generate a problem when the entire location is unavailable (all assigned ActiveGates or Synthetic engines are offline).
* You can generate a problem when any single ActiveGate or Synthetic engine assigned to the location is offline.

  For example, suppose your location has two ActiveGates, and you enable both problem switches. You will see three problems when your location is unavailableâone for the entire location and one for each ActiveGate that's offline.
* Additionally, you can opt to view a banner notification at the top of the Dynatrace web UI when either the entire location or any individual ActiveGate/Synthetic engine is unavailable.

  ![Banner notification](https://dt-cdn.net/images/pvtsyntheticlocationbannernotification-1290-d2e3105395.png)

From the main settings page listing all your private Synthetic locations, you can select multiple locations for bulk management of outage handling.

1. Select the checkbox next to each location you want to manage.
2. Select **Edit** in the lower-left corner of the page.

   ![Bulk edit locations](https://dt-cdn.net/images/pvtsyntheticlocationbulkedit-1852-dcc12815fd.png)
3. Select the appropriate outage handling checkbox.
4. Enable/disable the switch below the checkbox. This will overwrite the corresponding setting for the selected locations.

   ![Bulk edit location outage handling](https://dt-cdn.net/images/pvtsyntheticlocationbulkedit2-1296-3e4a8e3646.png)
5. **Save changes**.

## Update the browser manually from S3

If you have an offline environment or you installed an ActiveGate manually for dependency management or due to limited access to Amazon S3, you need to update the browser and dependencies manually.

You need to update the browser manually per ActiveGate, and the process varies slightly based on the operating system. Note that manual update of the browser only applies to Linux-based ActiveGates; on Windows-based ActiveGates, the browser is automatically updated during Synthetic engine updates.

Prerequisites:

* Ensure that **Enable Chrome(-ium) auto-update** is turned off for your private location in **Settings** > **Web and Mobile monitoring** > **Private Synthetic locations**. If you disable autoupdate for a location, you need to update the browser manually on every ActiveGate assigned to that location.
* Ensure that you can connect to `https://synthetic-packages.s3.amazonaws.com` to access browser packages.

* The Synthetic engine will use the new browser version after the update is completeânote that the status is updated once every hour, so it may take up to an hour to refresh the browser version displayed for your ActiveGate in **Deployment Status**.
* We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and browser versions updatedâDynatrace supports browser versions that are no more than two versions behind the [latest Dynatrace-supported version](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") for a specific ActiveGate release. (See also [browser update](#browser).)
* We strongly recommend updating all ActiveGates per location to the same version.
* See also [Browser update](#browser) and [Browser autoupdate from a custom repository](#autoupdate-custom-repo).

Since ActiveGate 1.331, on Ubuntu Server 20.04 and 22.04 we use Chrome for Testing. Chromium snap distribution is no longer supported.
If you are using any automation for updating the browser, convert it to use Chrome for Testing. Please refer to [community guideï»¿](https://dt-url.net/il0363p) for details.

Ubuntu (snap)

Red Hat Enterprise Linux and CentOS

Amazon Linux 2023, Ubuntu, and Oracle Linux 9 (Chrome for Testing)

This section is only relevant for releases 1.329 and earlier for Ubuntu Server 20.04 and 22.04.

1. If your ActiveGate and Chromium versions are out of support or have not been updated for several releases, review the Synthetic Engine and Chromium dependencies, and reinstall them if necessary. See the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Learn how to create a private location for synthetic monitoring.") in [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").
2. Download the snap (Ubuntu Server 20.04 and 22.04) package archive. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate and Ubuntu Server versions in the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Learn how to create a private location for synthetic monitoring.").
3. Extract and install the downloaded packages. Be sure to use the correct installation command for your Ubuntu Server version (check the [manual installation instructions for Ubuntu Server](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Learn how to create a private location for synthetic monitoring.")).
4. Verify Chromium update by running the following command from the default installation directory. Command output should match the Chromium version you installed.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Updating Chromium manually is identical on Red Hat Enterprise Linux and CentOS, the only difference being the downloaded packages for Red Hat/CentOS version 7 and version 8.

If you've installed Chromium manually, there's no need at the time of the update to register the Red Hat instance in the subscription manager or to enable the Red Hat repositories or EPEL packages.

1. If your ActiveGate and Chromium versions haven't been updated in a while, you might want to install Synthetic engine dependencies again. See the [manual installation instructions for Red Hat Enterprise Linux and CentOS](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Learn how to create a private location for synthetic monitoring.") in [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").
2. Download the rpm package archive. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate and OS versions in the [manual installation instructions for Red Hat Enterprise Linux and CentOS](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Learn how to create a private location for synthetic monitoring.").
3. Extract and install the downloaded packages. Check the [manual installation instructions for Red Hat Enterprise Linux and CentOS](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Learn how to create a private location for synthetic monitoring.").
4. If necessary, disable the automatic update of Chromium packages. Note that for Red Hat Enterprise Linux and CentOS, packing locking, once performed, remains persistent across all future updates.

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
5. Verify Chromium update by running the following command from the default installation directory. Command output should match the Chromium version you installed.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Chrome for Testing is managed differently from Chromium. To update manually, download the new version and extract it to the Chrome for Testing directory.

Unlike Chromium on other distributions, Chrome for Testing updates do not use package managers. You manually manage the Chrome binaries while dependencies are managed by the system package manager.

Ubuntu Server 20.04 and 22.04

When migrating from the snap Chromium distribution, first update ActiveGate, then install Chrome for Testing and optionally remove the Chromium snap installation.

1. If your ActiveGate and Chrome for Testing versions haven't been updated in a while, you might want to check and install Synthetic engine and Chrome for Testing dependencies again. See the [manual installation instructions for Chrome for Testing](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#chrome-for-testing "Learn how to create a private location for synthetic monitoring.") in [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").
2. Download the Chrome for Testing package archive to a temporary location. This is a safe and verified archive hosted by Dynatrace at `https://synthetic-packages.s3.amazonaws.com`. Be sure to use the specific command provided for your ActiveGate version in the [manual installation instructions for Chrome for Testing](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#chrome-for-testing "Learn how to create a private location for synthetic monitoring."), but modify the output path to `/tmp/chrome.zip`.
3. Remove the old Chrome for Testing directory, extract the new version, and clean up:

   ```
   sudo rm -rf /usr/lib/chrome_for_testing/chrome-linux64



   sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



   rm /tmp/chrome.zip
   ```

   If you configured a custom Chrome for Testing directory via the `synthetic_chrome_for_testing_path` property in `custom.properties`, replace `/usr/lib/chrome_for_testing` with your custom path in the commands above.
4. Verify Chrome for Testing update by running the following command. Command output should match the Chrome version you installed.

   ```
   /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
   ```

   The Synthetic engine will use the new Chrome for Testing version immediately. Note that the status is updated once every hour, so it may take up to an hour to refresh the Chrome version displayed for your ActiveGate in **Deployment Status**.

## Browser autoupdate from a custom repository

If you've enabled a [custom, local repository for the browser installation](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."), the browser can only be autoupdated. Follow this procedure to autoupdate the browser via the same custom repository.

1. After ActiveGate installation, specify the custom repository of the ActiveGate in the [`[synthetic]` section of the `custom.properties` file](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") in the `/var/lib/dynatrace/gateway/config` directory. This allows for automatic browser updates from the custom repository during manual or automatic Synthetic engine updates.

   ```
   [synthetic]



   chromium_repo = https://172.18.0.100/chromium-repo
   ```
2. Turn on **Enable Chrome(-ium) auto-update** for your private location in global settingsâgo to **Settings** > **Web and mobile monitoring** > **Private Synthetic locations**. Then select your location and enable the toggle in **Chrome(-ium) update** section.

   Note that the browser autoupdate UI setting applies to all ActiveGates assigned to your private location.
3. Ensure that the browser packages required for update are available at the custom repository location. The browser is then automatically updated from the custom repository during ActiveGate and Synthetic engine updates.

Browser autoupdate option

If you do not specify the custom repository in `custom.properties`, the browser is downloaded and updated from S3 during a manual or automatic ActiveGate and Synthetic engine update.