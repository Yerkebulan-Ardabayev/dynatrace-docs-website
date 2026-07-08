---
title: Applications in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/applications
---

# Applications in RUM Classic

# Applications in RUM Classic

* Explanation
* 4-min read
* Updated on Aug 18, 2025

In Real User Monitoring Classic (RUM Classic), monitored applications are logical constructs onto which customer applications—websites, mobile apps, and more—are mapped for monitoring with regard to traffic from real users. Therefore, it's implied that such customer applications have an end-user interface. Typical end-user interfaces include browser-based interfaces of web applications and sites as well as iOS- or Android-based interfaces of mobile apps running on smartphones or tablets.

The end-user interface determines the type of application created within Dynatrace. The way Dynatrace obtains the monitoring data and the type of data that is collected differ for each application type. For example, for a web application running in a browser, the [Real User Monitoring Classic (RUM Classic) JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") is [automatically injected](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") or [manually inserted](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") into the application's HTML pages and starts monitoring each user action.

## RUM application definition

The definition of the RUM application for web applications is generated automatically. More specifically, if your web applications are running on systems where you can install [OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms."), Dynatrace automatically injects the RUM JavaScript into the HTML pages. Therefore, every [monitoring environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") automatically obtains a default application named ["My web application."](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.") All RUM data are assigned to this application by default.

For mobile and custom applications, the definition is generated when you create the application and start setting up the Dynatrace monitoring. These application types are not monitored in an automated way.

## Supported application types

Dynatrace supports various application types: web and mobile, as well as rich client applications, applications running in a car, and IoT applications with user interactions. Each type has different monitoring capabilities and a different user interface within Dynatrace. However, all types are permeated by common concepts like [user sessions](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") and [user actions](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.").

You can find more information on each application type below.

Web applications

Mobile applications

Custom applications

All HTML pages—like static webpages or single-page applications running in a browser—are regarded as web applications.

|  |  |
| --- | --- |
| **User interface** | JavaScript-enabled browser (mobile or desktop) |
| **Monitoring approach** | Dynatrace RUM JavaScript |
| **Injection type** | Injection of the RUM JavaScript can be done automatically by OneAgent or manually for [agentless monitoring](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") |
| **How to get started** | [Define your applications via the "My web application" placeholder](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.") |

Mobile applications are native mobile apps on iOS or Android as well as hybrid apps accessed through a browser.

|  |  |
| --- | --- |
| **User interface** | Native mobile application on iOS or Android |
| **Monitoring approach** | OneAgent for iOS or Android; for hybrid applications, the browser part is monitored by the RUM JavaScript |
| **Injection type** | No injection is required—lifecycle events, user actions, and web requests are monitored out of the box. |
| **How to get started** | [Instrument your Android applications](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")[Instrument your iOS applications](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") |

Custom applications relate to all digital touchpoints in your environment, from traditional rich client applications to smart IoT applications or even Alexa Skills. Such applications are supported through [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Learn how you can instrument your application using OpenKit, how you can use Dynatrace OpenKit API methods, and more.").

|  |  |
| --- | --- |
| **User interface** | Any digital touchpoint a customer wants to monitor—from rich client applications over applications running in a car up to IoT applications with user interactions. The user interface could even be hardware like Amazon Alexa. |
| **Monitoring approach** | Dynatrace RUM JavaScript |
| **Injection type** | Injection is done by the customer using [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Learn how you can instrument your application using OpenKit, how you can use Dynatrace OpenKit API methods, and more.") for their technology. |
| **How to get started** | [Instrument your applications using Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit "Learn how to use Dynatrace OpenKit to instrument all non-web and mobile-based digital touchpoints in your environment, whether or not they’re traditional rich client applications, smart IoT applications, or even Alexa skills.") |

Dynatrace captures user sessions from custom applications as mobile user sessions. Built-in metrics are captured without the indication of whether it's a mobile or a custom application. For more details, see [Built-in metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").