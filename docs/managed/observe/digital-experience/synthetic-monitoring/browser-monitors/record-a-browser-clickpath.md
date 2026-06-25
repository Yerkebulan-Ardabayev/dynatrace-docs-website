---
title: Record a browser clickpath
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath
scraped: 2026-05-12T11:31:53.709030
---

# Record a browser clickpath

# Record a browser clickpath

* How-to guide
* 7-min read
* Updated on Nov 01, 2022

Your web application provides certain key functionality to your customers that is critical to the success of your business. Monitoring your application via browser clickpaths ensures that this functionality is available to your customers 24/7.

With our easy-to-use Dynatrace Synthetic Recorder (a Google Chrome browser extension), you can gain visibility into the availability and performance of your application's most important functionality involving all the elements of your IT infrastructure with just a few clicks.

Use the Dynatrace Synthetic Recorder to record the exact sequences of interaction that you want your simulated user visits to follow. The recorder captures events (such as button clicks, page scrolls, or user input) and converts them into a script that is played back each time you run the clickpath.

Each monitor run begins in a clean state, that is, with a clean browser cache and empty [local storageï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Install the Dynatrace Synthetic Recorder extension

You need to install Dynatrace Synthetic Recorder to begin. After installation, the recorder is automatically updated whenever new features become available.

1. Go to **Synthetic Classic**.
2. Select **Create a synthetic monitor** > **Create a browser monitor**.
3. First-time users are asked to install the Chrome extension: select **Install Dynatrace Synthetic Recorder** at the bottom of the page.
4. On the extension page, select **Add to Chrome** > **Add Extension**.

### Allow extension in incognito

After installing the Dynatrace Synthetic Recorder extension, you need to enable the **Allow in incognito** permission. This is necessary to have a clean browser state for recording and local playback in Chrome incognito mode.

1. Paste `chrome://extensions/` into your Chrome address bar and select Enter.
2. On the **Dynatrace Synthetic Recorder** tile, select **Details**.
3. Turn on **Allow in incognito**.

## Record a browser clickpath

1. Go to **Synthetic Classic**.
2. Select **Create a synthetic monitor** > **Create a browser monitor**.
3. Enter a valid **URL** and check the default **Name** for your clickpath on the Create synthetic monitor page.

   To enhance synthetic monitor security, Dynatrace blocks monitors from sending requests to a local host (for example, `localhost` or `127.0.0.1`).
4. Select **Add tag** to apply manually created tags to the monitor. You can choose from autocomplete suggestions as you type or create your own. (After the monitor has been created, you can manage tags from the [Synthetic details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.").
5. Continue on to [configure the monitor](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")âdevice profile and additional options such as cookies and authentication.

   ![Configure a browser monitor](https://dt-cdn.net/images/configurebrowsermonitor1-1665-749a574062.png)

   Configure a browser monitor

   When initially setting up a browser clickpath, **Enable global login authentication** is not supported for recording.

   * For form-based authentication, you can simply record entering credentials into a web form.
   * For HTTP-based authentication schemes, you need to manually enter the username and password in the browser-native dialog box when recording your clickpath and then enable HTTP authentication in the [Navigate event](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Learn about the event types created when recording a browser clickpath.") in edit mode.

   See [Supported authentication methods in Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.") for more information.
6. Record or define clickpath events.

   * You can **Manually add clickpath events**. You can also **Play back clickpath**, **Record again**, or **Cancel** clickpath creationâsee [Local playback](#playback).

     The **Record again** option lets you choose between recording the clickpath over completely or after playing back to a specified event. Note that any JavaScript events that precede an initial Navigate event will be erased when you re-record your clickpath from scratchâsee [Browser clickpath events](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Learn about the event types created when recording a browser clickpath.").

     + For manual clickpath creation, you can edit in **Visual mode** by adding [events](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Learn about the event types created when recording a browser clickpath.") to your script. You also need to [configure monitor options](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.").

       ![Manual clickpath creation by UI](https://dt-cdn.net/images/manualclickpathvisual-1646-9c8c648618.png)

       Manual clickpath creation by UI
     + For manual clickpath creation in [**Script mode**](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format."), all events and options such as cookies and automated login are defined in JSON.

       ![Manual clickpath script creation](https://dt-cdn.net/images/manualclickpathscript-1667-675cfdda17.png)

       Manual clickpath script creation
   * To use the recorder, select **Record clickpath**.

     Browser clickpaths are hard-coded to time out after 5 minutes. When recording a clickpath, ensure that the clickpath does not exceed this time limit.

     1. In the recorder browser instance that pops up, interact with your application to simulate an important use case (for example, logging in, searching for a product, or placing an order). As you interact with your application, each event is recorded for future playback.
     2. When done, select the Dynatrace extension icon on your browser's menu bar to **Finish** recording.

        ![Finish recording a clickpath](https://dt-cdn.net/images/finishrecordclickpath-1420-6f9197a415.png)

        Finish recording a clickpath
     3. Events in your recorded clickpath are displayed. You can [edit each event](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths."), for example, to add content validation or adjust wait time where needed. Select **Back** to begin monitor setup from scratch. You can also **Play back clickpath** or **Record again**âsee [Local playback](#playback).

        The **Record again** option lets you choose between recording the clickpath over completely or after playing back to a specified event. Note that any JavaScript events that precede an initial Navigate event will be erased when you re-record your clickpath from scratchâsee [Browser clickpath events](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Learn about the event types created when recording a browser clickpath.").

        When your recorded clickpath captures a credential such as a password, you are notified and given the option to save it to the [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault."). The image below shows a recorded clickpath with a captured password. Read more about credentials in the [Navigate event](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Learn about the event types created when recording a browser clickpath.") and [Keystroke event](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#keystroke "Learn about the event types created when recording a browser clickpath.").

        ![Captured credential](https://dt-cdn.net/images/clickpathcapturedpasswordkeystroke2-1617-0dc046deba.png)

        Captured credential
7. When recording is finished, choose **Next** to continue configurationâselect monitor locations and frequency.

   If you select this button without recording a clickpath or manually defining events, you will create a [single-URL browser monitor](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.") for the URL specified.
8. Choose monitor frequency. Scroll down to select locations. Your selections are displayed on the map. Select **Next** to view the monitor summary.

   ![Monitor frequency and locations](https://dt-cdn.net/images/syntheticfrequencylocations2-2223-297d2c4656.png)

   Monitor frequency and locations
9. On the Summary page, you can review and change your configuration (**Change URL or name**; **Change configuration**) or edit your clickpath events (**Edit clickpath**).

   ![Clickpath summary](https://dt-cdn.net/images/summaryclickpath2-2245-f1f7857bcc.png)

   Clickpath summary

   * See [Number of actions consumed by browser clickpaths](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Find out how many actions are consumed by a browser clickpath and how they differ from events.") for an explanation of the difference between actions and events.
   * [Synthetic action consumption](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") is an estimate based on an average of 730 hours per month.
10. At the bottom of the page, select **Create browser monitor**. Within a few minutes, you'll [receive monitoring data](#view-the-analytics-of-a-browser-clickpath) for your new browser clickpath.

### Local playback

You can play back a clickpath locally after you record or manually define clickpath events.

If your browser monitor has any associated credentials, whether public or owner only, users need to enter the credentials in order to play back the monitor locally. However, if you **Enable local playback of Synthetic browser monitors without entering credentials** in the [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault."), users need not enter the credentials that they have access to in order to play back the browser monitor.

The timeouts for local playback are 60 seconds for events and 5 minutes for monitors. These timeouts cannot be changed in the Dynatrace web UI. However, you can use the [PUT configuration method](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration "Update the configuration of Synthetic monitoring via the Synthetic API v2.") request of the Synthetic configuration API v2 to change browser monitor timeouts across your your environment for execution on private locations, local playback, and wait times.

You can opt to keep the playback window open after playing back a clickpath (**Keep window open after playback**), say, to debug a failed execution or add a [JavaScript event](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Learn about the event types created when recording a browser clickpath.").

* Local playback is distinct from [executing a monitor on demand](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations") from assigned locations (public or private).
* Local playback in Dynatrace is in emulation mode, based on the device profile and user agent you select during monitor configuration. That is, playback emulates your chosen device. If you navigate to the same URL or perform the same transaction outside Dynatrace, your experience might vary.

## View the analytics of a browser clickpath

1. Go to **Synthetic Classic**.
2. Optional Filter by **Browser clickpath** in the left menu.
3. From the list of monitors, select the browser clickpath you want to examine. You're directed to the [Synthetic details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.") for the clickpath.

## Disable or delete a browser clickpath

Monitors are enabled by default when you create them.

Disabling a synthetic monitor suspends further executions but retains the monitor and its measurement data. Any open performance and availability problems time out when a monitor is disabled (see [Synthetic calculations](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Understand Synthetic Monitoring metric calculations.") for details). Deletion removes a monitor and its associated measurement data; this is irreversible. Before deleting a monitor, we recommend that you disable it first and ensure that you no longer require its measurement data.

To disable or delete a monitor

1. Go to **Synthetic Classic**.
2. Opt to view your monitors in list format.
3. Select the check box for the monitor you want to delete or disable.
4. Select **Delete** or **Disable** in the lower-left corner.

   ![Delete a clickpath](https://dt-cdn.net/images/deletedisableclickpath1-892-020ec7491d.jpg)

   Delete a clickpath

You can also disable or delete a monitor from the [details page](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Analyze browser monitor and clickpath results on the Synthetic details page.").

1. Go to **Synthetic Classic**.
2. Select the monitor you're interested in.
3. Select the **Browse** button (**â¦**) and select either **Disable** or **Delete**.

[Synthetic monitor execution may be disabled during a maintenance window](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Understand Synthetic Monitoring metric calculations.") in maintenance window settings.