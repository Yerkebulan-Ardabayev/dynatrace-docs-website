---
title: New: User session analysis
source: https://www.dynatrace.com/docs/observe/digital-experience/session-segmentation/new-user-sessions
scraped: 2026-02-23T21:24:48.181410
---

# New: User session analysis

# New: User session analysis

* How-to guide
* 21-min read
* Updated on Oct 12, 2023

Dynatrace version 1.224+

While analysis of individual user sessions can be useful in some situations, such analysis is often incomplete. The users of your application behave in unexpected ways, perform different tasks with different goals in mind, reside in various geographic regions, and use countless combinations of devices, operating systems, and browsers.

Dynatrace supports user session segmentation through a powerful filtering mechanism. Dynatrace user session analysis enables you to slice, dice, and combine your application's user sessions into meaningful segments based on shared characteristics of individual user sessionsâoperating system, browser type, location, or user tag. For example, you might segment your analysis based on the following browser types: desktop, mobile, or synthetic. In this way, you can drill deeply into aggregate results to discover meaningful insights into performance problems that may only be experienced by a small subset of your users.

## Analyze a user session

To analyze a user session

1. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Click the text field at the top of the page (see **1** in the example below), and select one of the available filtering attributes.
   Once you select an attribute, the available values for that filter are displayed in a list.

   ### Available filtering attributes

   | Attribute category | Attribute | Description |
   | --- | --- | --- |
   | Applications | Application | Select the name of the application you want to analyze. |
   |  | Application type | Specify whether you want to analyze the sessions of web, mobile, or custom applications. |
   |  | Browser monitor | Select the name of the [browser monitor](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Learn how to set up a single-URL browser monitor to check the availability of your site.") used for Synthetic Monitoring. |
   | Browser | Browser type | Filter sessions based on whether they were performed with a desktop, tablet, or mobile browser or virtually via synthetic agent or bots. |
   |  | Browser family | Filter sessions based on the browser that was used. |
   |  | Browser version | Use this attribute if you want to filter sessions based not only on a specific browser but also on a specific browser version. |
   |  | Screen width | Filter user sessions based on a specific screen width. |
   |  | Screen height | Filter user sessions based on a specific screen height. |
   | Operating system | Operating system family | Filter sessions based on operating system family (Windows, Linux, iOS, etc). |
   |  | Operating system version | Select a specific OS version. |
   | Location | Continent | Filter sessions based on the continent where the sessions originate. |
   |  | Country | Filter sessions based on the country where the sessions originate. |
   |  | Region | Filter sessions based on the geographical region where the sessions originate. |
   |  | City | Filter sessions based on the city where the sessions originate. |
   | Mobile | Application version | Use this filter to view sessions for a specific version of your mobile app. |
   |  | Crashes | Select `Yes` or `No` to filter sessions that have or haven't experienced a [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."). |
   |  | Device | Filter sessions based on the type of mobile device used to access the application. |
   |  | Manufacturer | Filter user sessions based on a specific mobile device manufacturer. |
   |  | Rooted or jailbroken | Select `Yes` or `No` to filter mobile sessions where the device is rooted/jailbroken or genuine. If the device status is unknown or undefined, sessions have the value of `null` and don't appear in the results. Custom applications always report unknown or undefined. |
   | User | User tag | Select a [user tag](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") to analyze the sessions of a specific user. |
   |  | Internal user ID | Filter sessions based on the unique ID of the user that triggered the user session. |
   |  | User type | Choose whether you want to analyze user sessions of robots, synthetic users, or real users. |
   |  | New user | Select `Yes` or `No` to filter sessions based on whether users are new or returning users. |
   | Session | Live | Select `Yes` or `No` to show either [live or completed](/docs/observe/digital-experience/rum-concepts/user-session#live-vs-completed-user-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") sessions. |
   |  | Session Replay | Select `Yes` or `No` to show user session with or without [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers."). |
   |  | Bounced | Select `Yes` or `No` to filter sessions that either were or weren't bounced sessions (bounced sessions are sessions that are immediately abandoned). A bounce is a special type of user session composed of only a single user action. High bounce rates are undesirable. |
   |  | Converted | Select `Yes` or `No` to analyze those user sessions where the associated conversion goal was or was not achieved. |
   |  | Session conversion count | Filter sessions based on the number of times a session reaches any of the session conversion goals. |
   |  | Conversion goal | Select a specific conversion goal to examine those user sessions where this goal was achieved. |
   |  | Has errors | Select either `Yes` or `No` to explicitly filter sessions that did or didn't encounter errors. |
   |  | Error count | Specify a range of error occurrences. Use this to focus on user sessions that have more than a certain number of errors (if you leave the upper bound empty), less than or equal to a value (if you leave the lower bound empty), or fall within a specific value range. |
   |  | Error type | Specify whether you want to analyze the sessions that have request, reported, custom, or JavaScript errors. |
   |  | IP | Filter sessions based on IP addresses. |
   |  | IPS | Filter sessions based on a specific Internet Service Provider. |
   |  | Duration | Specify a session duration in minutes. Use this to filter sessions that have a duration longer than or equal to a value (if you leave the upper bound empty), shorter than or equal to a value (if you leave the lower bound empty), or fall within a specific value range. |
   | Session properties | Session date properties | Filter user sessions based on a particular session date [property](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.") and its value. |
   |  | Session double properties | Filter user sessions based on a particular session double property and its value. |
   |  | Session long properties | Filter user sessions based on a particular session long property and its value. |
   |  | Session string properties | Filter user sessions based on a particular session string property and its value. |
   | User actions | User action count | Specify a range of integers that represent the number of user actions performed within one session. This can help you to identify, for example, sessions that have a high number of actions. |
   |  | User action name | Specify a user action so that you can analyze all sessions that include at least one instance of that action. |
   |  | User action date properties | Filter user sessions based on a particular user action date [property](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.") and its value. |
   |  | User action double properties | Filter user sessions based on a particular user action double property and its value. |
   |  | User action string properties | Filter user sessions based on a particular user action string property and its value. |
   |  | User action long properties | Filter user sessions based on a particular user action long property and its value. |
   | Pages | Page name | Display sessions where a user accessed the specified page. |
   |  | Page group | Display sessions where a user accessed the page from the specified page group. |
   | Usability | Rage click count | Specify a range of [rage click](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") occurrences. Use this to focus on user sessions that have more than a certain number of rage clicks (if you leave the upper bound empty), less than or equal to a value (if you leave the lower bound empty), or fall within a specific value range. |
   |  | User experience score | Show user sessions with Satisfying, Tolerable, or Frustrating [user experience score](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying."). |
   |  | Rage tap count | Specify a range of [rage tap](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") occurrences. Use this to focus on mobile user sessions that have more than a certain number of rage taps (if you leave the upper bound empty), less than or equal to a value (if you leave the lower bound empty), or fall within a specific value range. |

   In filters, the tilde operator (`~`) doesn't work as the `LIKE` keyword in [USQL](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.").
3. Select the attribute value you're interested in. Some attributes provide text fields that you can use for free-text search. You can also select multiple values of one attribute; this works as an `OR` operator for that attribute.
4. Repeat this process for as many attributes as you are interested in. Once you've defined your filter, click anywhere outside the text box.

   The result of the defined filters provides a list of the first 500 sessions, which are ordered by the start time of the newest session. To change the order, sort the table columns in ascending or descending order.
5. Select a session timestamp (see **3** in the example below) to go to the user session details page. Alternatively, to analyze the sessions of a single user, select a username (see **2** in the example below) to navigate to that [user's details page](/docs/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

![User sessions page](https://dt-cdn.net/images/new-user-sessions-page-3342-dd45c41c38.png)

Use the [timeframe selector](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") in the menu bar to adjust the analysis timeframe of your user session analysis.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

Timeframe selector controls

The global timeframe selector serves as a time filter that, in most cases, enables you to select a specific analysis timeframe that persists across all product pages and views as you navigate through your analysis.

![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

* The **Presets** tab lists all standard timeframes available. Select one to change your timeframe to that preset.
* The **Custom** tab displays a calendar. Click a start day, click an end day, and then click **Apply** to select that range of days as your timeframe.

  + Selected calendar intervals are set to end on start of the next day (with the time set to `00:00`). For example, if you select September 3 to September 4 on the calendar, the timeframe starts on September 3 at time `00:00` and ends on September **5** at time `00:00`, so you never miss the last minute of the time range. You can edit these displayed times.
* The **Recent** tab displays recently used timeframes. Select one to revert to that timeframe.
* The **<** and **>** controls shift the timerange forward or backward in time. The increment is the length of the original timerange. For example, if the current timerange is `Last 2 hours` (the two-hour range ending now), click **<** to shift the timerange two hours back, to `-4h to -2h` (the two-hour range ending two hours ago).
* Hover over the timeframe to see the start time, duration, and end time.

  ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

Timeframe selector expressions

If you select the current timeframe in the menu bar, an editable timeframe expression is displayed.

* Reading from left to right, a timeframe expression has a start time, a `to` operator, and an end time.
* If there is no explicit end time, the `to` and `now` are implied. For example, `-2h` is the same `-2h to now`.
* Supported units: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (you can also use whole words such as `minutes` and `quarter`)

**Example timeframe expressions**

**Meaning**

`today`

From the beginning of today to the beginning of tomorrow.

`yesterday`

From the beginning of yesterday to the beginning of today. Like `-1d/d to today`.

`yesterday to now`

From the beginning of yesterday to the current time today.

`previous week`

The previous seven whole days. If today is Monday, you get the previous Monday through the previous Sunday (yesterday).

`this year`

The current calendar year, from January 1 of this year at `00:00` through January 1 of next year at `00:00`.

`last 6 weeks`

The last 42 days (6 weeks \* 7 days) ending now. Equivalent to `-6w to now`.

`-2h`

From 2 hours (120 minutes) ago to the current time (`now` is implied). Equivalent to `Last 2 hours` and `-2h to now`.

`-4d to -1h30m`

From 4 days (96 hours) ago to 1.5 hours ago.

`-1w`

The last 7 days (168 hours), from this time 7 days ago to the current time (`now`). Equivalent to `-7d` and `-168h`.

`-1w/w`

From the beginning of the previous calendar week to the current time (now).

* If you used `-1w/w` on a Friday afternoon at 3:00, you would get a range of 11 days 15 hours, starting with the beginning of the previous week's Monday, because `/w` rounds down to the beginning of the week.
* If you used `-1w` without `/w` on a Friday afternoon at 3:00, the start time would be exactly 7 days (168 hours) earlier: the previous Friday at 3:00 in the afternoon.

In general, `/` used in combination with a unit (such as `/d`, `/w`, `/M`, and `/y`) means to round down the date or time to the beginning of the specified time unit. For example, `-3d` means exactly 72 hours ago, whereas `-3d/d` means three days ago rounded down to the nearest day (starting at time `00:00`, the beginning of the day). Use `now/d` to mean the start of today.

`-1w/w + 8h`

Starting from the beginning of last week plus 8 hours (8:00 AM Monday).

* Note that you can use the `+` and `-` operators with units, timestamps, and `now`.

`-1d/d+9h00m to -1d/d+17h00m`

Business hours yesterday, from 09:00 - 17:00 (9 AM to 5 PM).

`2020-08-16 21:28 to 2020-08-19 10:02`

An absolute range consisting of absolute start and end dates and times in `YYYY-MM-DD hh:mm` format.

* If you provide a date but omit the time (for example, just `2020-08-16`), the time is assumed to be the beginning of day (`00:00`)
* If you provide a time but omit the date (for example, just `21:28`), the date is assumed to be today

`1598545932346 to 1598837052346`

Unix epoch millisecond timestamps.

User sessions that are [live](/docs/observe/digital-experience/rum-concepts/user-session#live-vs-completed-sessions "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") within the timeframe set in the timeframe selector are shown in the session list. The **Analysis over time** [finding](#drill-down-using-findings), on the contrary, shows only those sessions that started within the set timeframe.

For instance, if the timeframe is set for 12:00â12:05, and a session that started at 11:55 is still live during that timeframe, that session is shown in the session list but isn't considered for the **Analysis over time** finding. This is because the session started before the set timeframe.



## Drill down using findings

The findings panel is located on the left side of the **User sessions** page. This panel contains out-of-the-box findings and different visualizations for various attributes. For example, select the **Application versions** category to see which of your application version has more user sessions, or select the **Applications** category to see data on aggregated sessions for each of your applications.

![Mobile application versions on the User sessions page](https://dt-cdn.net/images/user-seesions-mobile-app-versions-1635-29a25ad4eb.png)

![Findings panel on the new user sessions page](https://dt-cdn.net/images/findings-panel-on-the-new-user-sessions-page-3342-e11184615c.png)

## Focus on sessions of an individual user

You can focus on the user sessions of a specific user. Select a user from the **User** column to navigate to that [user's overview page](/docs/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

To search for user sessions of a specific user, select [**User tag**](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") in the **Filter by** box and then choose the user you're interested in. For example, to display user sessions of a user named `Zara`, add the **User tag:** `Zara` filter. Then select **Zara** in the **User** column to navigate to this user's overview page.

![User sessions of a particular user](https://dt-cdn.net/images/user-sessions-of-a-particulra-user-2460-63bd6314da.png)

To learn how to tag each user of your application with a unique user name, check the following pages depending on your application type and operating system:

* [Web applications](/docs/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.")
* Mobile applications

  + [Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
  + [iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#tag-specific-users "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
  + [Cordovaï»¿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#identify-user)
  + [Flutterï»¿](https://pub.dev/packages/dynatrace_flutter_plugin#identifyUser)
  + [React Nativeï»¿](https://www.npmjs.com/package/@dynatrace/react-native-plugin#identify-a-user)
  + [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#identify-user "Monitor Xamarin apps with Dynatrace OneAgent.")
  + [.NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#identify-user "Monitor .NET MAUI applications with Dynatrace OneAgent.")
* [Custom applications: OpenKit](/docs/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#tag-specific-users "Read how Dynatrace OpenKit can be used from the developer's point of view.")

Select one of `Zara`'s sessions to view further details. For example, you can check all actions that the `Zara` user performed during the selected session. The session details contain important device-related information such as the device resolution, manufacturer, operating system, geolocation, and IP address.

![User session details page](https://dt-cdn.net/images/usmobile2-1-1438-7fd0911d36.png)

## View error details

You can also leverage session analysis to get to the details of [errors](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") that occur in your application.

To view the error details page

1. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. In the **Filter by** box, set **Error type** to one of the following values depending on your application type:

   | Error type | Description | Web | Mobile | Custom |
   | --- | --- | --- | --- | --- |
   | Request error | Detected by the browser and OneAgent on your servers | Applicable | Applicable | Applicable |
   | Reported error | Manually reported via dedicated "report an error" API method | Not applicable | Applicable | Applicable |
   | Custom error | Manually reported via the RUM JavaScript API | Applicable | Not applicable | Not applicable |
   | JavaScript error | JavaScript exceptions thrown by the browser | Applicable | Not applicable | Not applicable |
3. Select the user session you're interested in to open the session details page.
4. Under **Events and actions**, expand the user action that contains an error, and select **Perform waterfall analysis**.
5. Perform one of the following actions depending on the application type:

   * Web applications On the **Waterfall analysis** page, select the **Error** tile, and then select the error. The error details page opens.
   * Mobile and custom applications Scroll down to the **Web request errors** or **Reported errors** section and select the error. The error details page opens.

#### Error details page

The error details page provides valuable information about your application's errors.

Web request error details page

Reported error details page

![Web request error details page](https://dt-cdn.net/images/web-request-error-details-page-1772-928bb94d69.png)

![Reported error details page](https://dt-cdn.net/images/reported-error-details-page-new-1644-60289f33a5.png)

This displays error details such as the estimated error count, provider (for a request error), technology (for a reported error), and more. The page also lists affected user sessions and affected user actionsâselect a user action or user session to view its details. The distribution breakdown displays information on the relative frequencies of operating systems, OS versions, application versions, and devices, while the country breakdown shows all affected countries and their corresponding error rate.

## Check sessions with rage events

When your application doesn't respond quickly, a text label looks like a button, or a toggle is hidden under another toggle, users might repeatedly click or tap the affected UI control in frustration. Dynatrace detects such behavior as a [rage event](/docs/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace."): a **rage click** or a **rage tap**.

To view user sessions with rage events

1. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Set **Filter by** to **Rage click count:** `â¥1` or **Rage tap count:** `â¥1`.
3. Select the user session you're interested in to open the session details page.
4. Scroll down to the **Events and actions** section, and expand the rage click or rage tap event to view its details.

## Examine crashes



Mobile and custom applications

When a user session ends in a [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."), you can leverage session analysis to view the complete sequence of user actions that preceded the crash. You can also open a crash report to get all the code-level information and quickly trace the root causes of that crash.

1. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation**.
2. Set **Filter by** to the following filters:

   * **Application type:** `Mobile` to display only mobile user sessions or **Application type:** `Custom` to get user sessions captured in custom applications
   * **Crashes:** `Yes` to show sessions ended with a crash
   * Mobile applications **Session Replay:** `Yes` to display sessions recorded with Session Replay on crashes for [Android](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform.") or [iOS](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps.") applications
3. Select the user session you're interested in to open its session details page.
4. Mobile applications To watch the Session Replay recording, go to the **Session Replay** tab, and select **Play** ![Replay](https://dt-cdn.net/images/replay-button-optimized-41ad05863e.svg "Replay").  
   The last event of the session is the crash, which is represented by a red dot in the timeline. Use the Session Replay controls to analyze the crash in detail.

   ![Mobile user session with Session Replay](https://dt-cdn.net/images/mobile-user-session-with-session-replay-2134-d486b7d1b9.png)
5. To view all user actions and events that preceded the crash, scroll down to the **Events and actions** section.
6. To view the crash report, expand the crash event, and then select **Open crash details**.  
   The crash report provides you with the user's device information and stack trace. You can also analyze the crash groups for your [mobile](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile#crash-groups "Check the latest crash reports for your mobile applications.") and [custom applications](/docs/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom#crash-groups "Check the latest crash reports for your custom applications.") or download the crash stack trace.

   ![Opening the mobile crash report](https://dt-cdn.net/images/open-mobile-crash-details-2132-311049ce33.png)

## Analysis of a single session across different domains

For technical and security reasons, you cannot analyze a single user session across different domains.

Suppose your user visits two completely different domains during a single "session". How would Dynatrace capture this, given that both domains are instrumented with Dynatrace?

You'd actually see two separate user sessions:

1. The first session starts with the page load for the web page of the first domain, and it ends when the user clicks a link that leads them to a web page with a different domain (the second domain).
2. The second session starts with the first page load on the second domain, and it ends when any of the [criteria for ending a user session](#user-session-end) is met.

This happens for the following reasons:

* **Technical reason**: Cookies can't be shared across domains, except for subdomains.
* **Security reason**: It's a security feature of browsers and a limitation that all vendors share.

## Real-time analysis

* Access live user sessions through the **Live user activity** tile on the dashboard.

![Live user activity](https://dt-cdn.net/images/live-user-activity-1567-1df03a6ae5.png)

* Go to one of the problem pages, and select **See user sessions sample**.

![Problem details page](https://dt-cdn.net/images/user-sessions-problems-pages-1635-7fb715b445.png)

* Affected sessions can also be directly accessed from one of the problem pages.

![User sessions affected by a problem](https://dt-cdn.net/images/user-sessions-from-problems-pages-to-sessions-page-1634-805c05bb34.png)

* Bounces and conversions are available for completed user sessions.

![Conversions and bounces on the User sessions page](https://dt-cdn.net/images/user-sessions-conversions-and-bounces-1639-f3a0e84129.png)

## Examples

These examples show how you can gain insight into your users' behavior through Dynatrace user session analysis.

Filter user sessions based on user session duration

You can filter user sessions by duration: longer or shorter than a certain value or within a certain range. In the screenshot below, user sessions that have a duration of at least 10 seconds are displayed.

![Filter user sessions based on user session duration](https://dt-cdn.net/images/image005-2550-69ae07a8ad.png)

Search for all user sessions that include at least one instance of specific user actions

You can search for all user sessions that include at least one instance of any one of multiple user actions in their clickpaths.

![Search for user sessions with specific user actions](https://dt-cdn.net/images/image007-2550-ced4628b80.png)

Create complex filters

Check the filter bar in the example below. This search matches on user sessions that meet the following criteria:

* **Application type: Web** and **Browser Type: Desktop Browser**. The user accessed one of your web applications via desktop browser.
* **Duration 60s**. The session lasted at least 1 minute.
* **Action count = 5**. During the session, the user performed five actions.
* **User action name: test**. The user action called `test` occurred in the user session.

![Create complex filters](https://dt-cdn.net/images/image009-2550-759db59a94.png)

Explore categories on the findings panel

For each category on the findings panel, there's a separate section that shows visualizations and findings for that particular category. For example, **Application type** shows the current distribution, distribution over time, and geographical distribution of the different application types. The geographical map shows the color of the application type with the highest number of sessions.

![Application type category view](https://dt-cdn.net/images/image011-2122-def628c232.png)

You can choose any of the findings and easily apply them by selecting **Apply selection as a filter** in the lower-left corner of the page.

![Apply current category as a filter](https://dt-cdn.net/images/image013-2540-899b1a7298.png)

## Related topics

* [User sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* [Effective customer support with session segmentation](/docs/observe/digital-experience/dem-use-cases/customer-support-with-session-segmentation "Learn how to resolve customer complaints using session segmentation.")