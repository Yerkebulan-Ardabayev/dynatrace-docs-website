---
title: User sessions
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/user-session
scraped: 2026-05-12T11:10:10.558521
---

# User sessions

# User sessions

* Explanation
* 7-min read
* Updated on Feb 26, 2026

A user session, also known as a "visit," "journey," or "clickpath," is a sequence of [user actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") that are performed by the same user in your application during a limited period of time. A single session typically includes multiple page or view loads, third-party content requests, service requests, and user actions such as clicks or taps. Each user session includes at least one user action.

To view user session data, go to **Session Segmentation**. For more details, see [New: User session analysis](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

## User session identification

For web applications, Dynatrace can show you all the sessions of an individual user, even when those sessions are anonymous or when a [user tag](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") has been changed or gone missing. User identification is achieved by storing a persistent cookie within each user's browser. This cookie contains a unique identifier for the user, which is marked as the **Internal user ID** in the Dynatrace web UI. Cookies enable Dynatrace to assign even anonymous user sessions to known users. As long as a user has logged into your application at least once, you can search for and identify that user, even when the user accesses the application in anonymous, unauthenticated sessions. This is particularly useful for analyzing periods of time when a user might not have been able to log into your application because of issues with your authentication service. Note that if a user disables persistent cookies or clears their cookies, the unique identifier is regenerated.

For mobile applications, user identification is achieved by generating and storing a unique identifier when a user launches an application for the first time. This identifier, marked as the **Internal user ID** in the Dynatrace web UI, is regenerated when the user changes their [privacy settings](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."). It's only possible to view all sessions of a particular user when the [data collection level](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is set to **User behavior**; when the data collection level is set to **Off** or **Performance**, the unique identifier is regenerated for every session, making it impossible to list several sessions of a particular user.

For custom applications, user identification is achieved by passing `deviceID`, which should be unique for each user or device. Then `deviceID` is marked as the **Internal user ID** in the Dynatrace web UI.

## User session structure

Dynatrace captures user sessions of web, mobile, and custom applications. The user session structure depends on the application type.

|  | Web | Mobile | Custom |
| --- | --- | --- | --- |
| User session can span multiple applications[1](#fn-1-1-def) | Applicable | Not applicable | Not applicable |
| User actions can have [child actions](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.")[2](#fn-1-2-def) | Applicable | Applicable | Applicable |
| Web requests can be attached to user actions | Applicable | Applicable | Applicable |
| Standalone web requests are possible | Not applicable | Applicable | Applicable |

1

For example, the same user session might happen in **Web application A** and **Web application B**.

2

The possible child action nesting depends on the application type and technology used.

Below is an illustration of the possible user session structure for an individual user.

![User session structure for individual user](https://dt-cdn.net/images/sus-6343-user-session-structure-2500-594cf1dae0.png)

User session structure for individual user

## User action grouping

Dynatrace stores some information in session cookies and local storage. This enables the correlation of user actions into one user session. However, this session information is erased when the browser is closed, the user clears their browser cookies, or the user cleans up their local storage. In such cases, the next initiated user action starts a new user session.

Suppose, for example, that a user of a web application performs 10 user actions every 1â2 minutes and after each user action the user either closes their browser or deletes their browser cookies. In such a situation, 10 user sessions would appear on the **User sessions** page, each composed of a single user action.

Consider another example. A user session is initiated, but after a few minutes the user walks away and leaves their browser window open. After a 45-minute break, the user returns back, and a new user session starts because the browser has been inactive for more than 35 minutes.

## User session timings

### Session start

A user session starts when the first user action is initiated.

### Session end

A user session ends in one of the following ways:

Web applications

Mobile apps

Custom apps

* After 30 minutes of browser inactivity.
* When the user closes their browser.[1](#fn-2-1-def)
* When the session duration reaches 6 hours.
* When the session is ended via the [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") by calling the `dtrum.endSession()` function.

1

A user session remains live in the Dynatrace web UI for up to 35 minutes after the user closes their browser.

* After 10 minutes of inactivity on a mobile device.[1](#fn-3-1-def)
* When the session duration reaches 6 hours.
* When the user or the mobile operating system closes or force stops the app.[1](#fn-3-1-def), [2](#fn-3-2-def)
* When the session is ended via the Dynatrace API.
* When the [data privacy settings](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") are changed.
* When a [crash](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") occurs.[3](#fn-3-3-def)

1

A user session remains live in the Dynatrace web UI for up to 35 minutes after that.

2

A user session does not end when the app is sent to the background, but a session does end if the mobile operating system purges the backgrounded app from memory.

3

Data that is monitored while a crash is processed is added to the same user session.

* After 10 minutes of inactivity, which is 10 minutes after the last [custom action was created](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods#create-custom-and-child-actions "Read how Dynatrace OpenKit can be used from the developer's point of view.").[1](#fn-4-1-def),  [2](#fn-4-2-def)
* When the session duration reaches 6 hours.
* When the session is ended via the Dynatrace API.
* When a [crash](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") is reported.

1

A user session remains live in the Dynatrace web UI for up to 35 minutes after that.

2

Every `enterAction` call resets the timer, but it must be invoked on the session level.

Once a user session has about 200 user actions, a new session is created and all subsequent user actions are included in the new user session. There is no extra charge for additional user sessions that Dynatrace creates following such session splits.

There's a delay in the display of new user session data in the Dynatrace web UI.

New user sessions aren't reported in real time. There is a delay of 5â6 minutes from the moment a new user session begins until the user session is reflected in charts and other analytical views in Dynatrace. This delay results in a slight drop in the number of user sessions that are recorded at the end of each time interval during which new user sessions are started.

### Session duration

User session duration is the elapsed time between the initiation of the first user action in a session and the completion of the last user action in the session. Note that timeout periodsâperiods at the end of the session that include no user activityâaren't factored into user session duration measurements.

Typically, a user session appears in the Dynatrace web UI within 4 minutes. However, this could sometimes exceed 10.5 minutes.

## Live vs. completed user sessions

Live user sessions don't have any information about the user experience score or duration as those metrics are calculated at the end of the session. Live sessions can still get new user actions.

![Live user sessions](https://dt-cdn.net/images/screenshot-2021-03-25-at-14-02-25-2926-00a1d07841.png)

Live user sessions

Use the **Live** filter to separate out live user sessions from completed sessions.

![Using the Live filter on the User sessions page](https://dt-cdn.net/images/user-sessions-live-filter-1639-19ece8581a.png)

Using the Live filter on the User sessions page

## Live vs. active users

* A **live user** is a user who was active once before, but whose session has not yet been ended.
* An **active user** is a user who has been confirmed still active at a given time.

To make the difference tangible, let's look at an example. A user performs their latest action at 8:00 and is then idle. At 8:15, we would still count this user as a live user because their session has not yet timed out, but we wouldn't count this user as an active user from 8:01 to 8:15.

As a rule of thumb, the number of "live user" sessions should be greater than the number of "active user" sessions because the former can include sessions that started even before the start of the selected time frame and might go beyond the end of the selected timeframe. Or, to put it differently, the former is a count that might span beyond the selected timeframe, while the latter is a point-in-time metric and does not span beyond the selected timeframe. Therefore, comparing these two numbers does not really make sense.

## Related topics

* [New: User session analysis](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.")
* [Export user sessions](/managed/observe/digital-experience/session-segmentation/export-session-data "Set up Dynatrace to export user session data to a provided webhook endpoint.")