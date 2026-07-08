---
title: View crash reports for custom applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/crash-reports-custom
---

# View crash reports for custom applications in RUM Classic

# View crash reports for custom applications in RUM Classic

* How-to guide
* 1-min read
* Updated on Mar 20, 2024

Reviewing and fixing [crashes](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") is vital to improving your application's user experience. Dynatrace captures crashes and their stack traces so that you can assess the criticality of a crash and identify the root cause of the issue. With the crash-analysis workflow, you can see the impact of crashes, identify the affected user groups, and quickly get to the root cause. By proactively resolving issues, you can ensure that your applications consistently meet your business goals.

When working with a client-server setup, some crashes have their root cause on the server side. Dynatrace uses PurePath® technology and OneAgent® to correlate user actions with web requests, thereby giving you complete visibility, from individual user actions to the specific server-side database statements that contribute to crashes.

To view the basic information on crashes for your application

1. Go to **Frontend**.
2. Select the application you want to analyze.
3. From the application overview page, select the **Crashes & Errors** tile.

The **Crashes & Errors** tile shows the number of crash occurrences, percentage of crash-free users, and crash rate for the currently selected timeframe. The **Crashes by version** chart displays the total number of crashes by version for the currently selected timeframe.

![Crashes tile on the application overview page](https://dt-cdn.net/images/crashes-tile-mobile-app-852-77531749a6.png)

Crashes tile on the application overview page

To access crash reports for your application

1. From your application overview page, select the **Crashes & Errors** tile.
2. Under the **Crashes by version** chart, select **Analyze crashes**. The **Crash analysis** page opens.

![Crash analysis page](https://dt-cdn.net/images/crash-analysis-mobile-app-2519-daa9f932f4.png)

Crash analysis page

## Crash analysis page

The **Crash analysis** page gives you an overview of all crash groups that occurred during the selected timeframe and allows you to focus on a range of properties and dimensions that might be specific to the crash pattern. Therefore, you can analyze crashes based on the operating system version, application version, user region, session duration, connectivity type, and other dimensions.

### Latest app versions

The **Latest app versions** section provides crash information for four latest app versions. For each app version, you can check the percentage of crash-free users, number of affected users, and number of crashes per certain number of sessions.

### Crash statistics

In the **Crash statistics** section, you can check the total crash count, number of crash groups, and number of affected versions for the currently selected timeframe. In the **Latest app versions** section, select **Filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter") next to the version you're interested in to get this information for a particular version.

You can also use other filters, such as **Connection type**, **Country**, or **Manufacturer**.

### Crash groups

Dynatrace groups crashes by similarity of the stack trace and occurrence in the source code. This usually also works across different versions of your application so that you can easily find out if a crash is still present in the latest release.

## Crash group details page

Under **Crash groups** on the **Crash analysis** page, select a crash group you're interested in to access all crash instances. Filter them to investigate a particular part of the crash group.

![Crash group information](https://dt-cdn.net/images/crash-group-mobile-app-2518-9324fa74b5.png)

Crash group information

On the crash group details page, select **Next / previous crash occurrence** ![Left and right arrows](https://dt-cdn.net/images/analysisarrowbuttons-49-c49391e1bc.png "Left and right arrows") to browse through all the crash occurrences. Choose the crash occurrence you're interested in, and then switch between the tabs to view the detailed information on the selected crash occurrence.

Stack trace

Device information

Session information

On the **Stack trace** tab, examine the stack trace or download the stack trace to share it with your team.

![Stack trace for a crash occurrence](https://dt-cdn.net/images/crash-occurence-stack-trace-tab-2520-f9c5b285f0.png)

Stack trace for a crash occurrence

On the **Device information** tab, view the detailed information on the device where the current crash occurrence happened. For instance, you can check the device geolocation, OS version, user language, and much more.

![Device information for a crash occurrence](https://dt-cdn.net/images/crash-occurence-device-info-tab-2520-8e77ca1904.png)

Device information for a crash occurrence

On the **Session information** tab, select **View full session** to jump to the user session details page, where you can get more information on the crashed session, examine the list of all user actions and events that occurred before the crash, or select a crash instance. For more details, see [User session analysis in RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.").

![Session information for a crash occurrence](https://dt-cdn.net/images/crash-occurence-session-info-tab-2520-e40fca17fd.png)

Session information for a crash occurrence

## Related topics

* [Crash analysis](/managed/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes.")
* [User and error events in RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [User session analysis in RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.")