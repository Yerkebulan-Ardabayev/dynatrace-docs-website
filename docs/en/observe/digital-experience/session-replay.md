---
title: Session Replay
source: https://www.dynatrace.com/docs/observe/digital-experience/session-replay
scraped: 2026-02-18T05:42:38.036842
---

# Session Replay

# Session Replay

* Overview
* 3-min read
* Updated on Jan 27, 2023

Session Replay is a powerful tool that can modernize your Digital Experience Monitoring (DEM) strategy. You can use it to capture and visually replay the complete digital experience of every user.

You can record your customers' interactions with your application and replay each click or tap in a movie-like experience. Session Replay also makes it easy for your QA teams to reproduce production issues, which your developers can use to bridge the gap between code and user experience.

Session Replay helps identify errors that should be fixed immediately and other problems such as malformed pages and infinite spinners. You can also use Session Replay to identify and analyze areas of struggle in your application and improve its overall usability.

Session Replay is currently available for [web applications](/docs/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay."), [Android](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform."), and [iOS](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Fix bugs and simplify complex issues with visual recordings of user sessions.](https://www.dynatrace.com/hub/detail/session-replay/?internal_source=doc&internal_medium=link&internal_campaign=cross)

Session Replay is not supported on Cordova, React Native, Flutter, Xamarin, and .NET MAUI.

## Uses for Session Replay

### Error drill-down

With Session Replay, you can drill down further into the details of detected errors:

* Detect errors and other issues.
* Understand the exact user actions that led to an error.
* Understand the severity of the problem and its effect on user experience.
* Observe the customer impact by replaying and viewing a session when the problem isn't obvious.

Developers can use Session Replay to view, analyze, reproduce, and fix errors.

For error drill-down, you don't need to have all sessions recorded. You can use [cost and traffic control for web applications](/docs/observe/digital-experience/session-replay/configure-session-replay-web#cost-traffic-control "Configure monitoring consumption and data privacy settings for Session Replay.") to record only a subset of sessions. If the error to be analyzed isn't too sporadic, it can be detected even if only 20% of sessions are recorded.

The default [data retention](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") timeframe is applied to these sessions.

The ability to play back recorded user sessions with or without playback [masking](/docs/observe/digital-experience/session-replay/configure-session-replay-web#sr-masking "Configure monitoring consumption and data privacy settings for Session Replay.") settings is permission controlled. Permissions are available at the environment level as well as the management-zone level. Read more in [Manage user groups and permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions#permissions "Role-based permissions").

### Complaint resolution

Because Session Replay is the best way to demonstrate what the user actually did, it provides the means to resolve customer complaints. Use Session Replay to:

* See the exact journey of the customer in your application.
* Identify the exact problem faced by the user.
* Provide correct instructions.

For customer complaint resolution, it's ideal that all sessions be recorded. However, to save storage space, we recommend that a lower retention time be set.

### Usability analysis

You can use Session Replay to detect and analyze the following issues:

* The UX design isn't intuitive enough.
* The process flow is too complicated, and users leave your application midway.
* The application is slow, and the user repeatedly clicks or taps to move to the next page or jump to the next screen.
* The application doesn't work as expected on all browsers or devices.
* The application prompts the user to change the orientation of their device, but the user doesn't understand the prompt.

The default [data retention](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.") time is applied to these sessions.

## Technical restrictions for web applications

For web applications, Session Replay is compatible with page-based applications, single-page applications, and applications that use iFrames. However, [certain restrictions](/docs/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay.") apply.

## Related topics

* [Enable Session Replay for web applications](/docs/observe/digital-experience/session-replay/enable-session-replay-web "Learn the prerequisites and the procedure for enabling Session Replay.")
* [Configure Session Replay for web applications](/docs/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.")
* [Technical restrictions for Session Replay for web applications](/docs/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay.")
* [Configure Session Replay for iOS](/docs/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay for your iOS apps.")
* [Configure Session Replay for Android](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform.")