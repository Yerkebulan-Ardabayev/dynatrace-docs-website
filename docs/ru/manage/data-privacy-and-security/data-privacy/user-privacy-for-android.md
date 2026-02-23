---
title: Data safety guidance for Android
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android
scraped: 2026-02-23T21:32:17.384486
---

# Data safety guidance for Android

# Data safety guidance for Android

* Latest Dynatrace
* 5-min read
* Updated on Sep 15, 2025

Starting July 20, 2022, Google requires you to provide your users with information on how your mobile app collects, protects, and shares their data. This also includes data collected by third-party partners like Dynatrace.

This page can help you with completing the [Data safety formï»¿](https://support.google.com/googleplay/android-developer/answer/10787469#complete_form_steps) in Google Play Console. The questions and data types reflect the Data safety form, but note that the answers reflect the out-of-the-box, default state.

OneAgent might capture additional data through your [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Learn what OneAgent SDK for Android is."). If you instrument your app to collect additional data, make sure you reflect this in the **Data safety** section in Google Play Console.

To fill out the Data safety form

1. Sign in to Google Play Console, and select the required mobile app.
2. From the menu on the left, go to **Policy** > **App content**.
3. Under **Data safety**, select **Manage**.
4. Complete the Data safety form using the information provided on this page.

## Data collection and security

Use the table below to answer the questions in this section.

Question

Answer

Note

Does your app collect or share any of the required user data types?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")Yes

Is all of the user data collected by your app encrypted in transit?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")Yes

Which of the following methods of account creation does your app support?

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") My app does not allow users to create an account

Dynatrace does not provide user accounts

Can users login to your app with accounts created outside of the app?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")No

Do you provide a way for users to request that their data is deleted?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")No

## Data types

Select all types of data that your mobile app collects or shares.

The table below contains all data that OneAgent captures by default.

Category

Data type

Captured by default?

Note

Location

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Select **Approximate location** if you've enabled [location monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#location-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") and your mobile app has the permission to use the device's geolocation information.

Dynatrace can capture the [approximate location](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), but it never collects a precise location.

Personal info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Select **User IDs** or other personal information data types if you collect your users' personal information via [user tagging](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#tag-specific-users "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

Financial info

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Health and fitness

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Messages

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Photos and videos

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Audio files

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Files and docs

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Calendar

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Contacts

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

App activity

App interactions

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures user interactions, for example, app launches or taps, and reports them as user actions.

See [User action monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#action-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") and [Lifecycle monitoring](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#lifecycle-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") for information on how to configure or disable these features.

Web browsing

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

App info and performance

Crash logs

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures information on [crashes](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."). If you've also enabled [Session Replay on crashes](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform."), Dynatrace collects several screenshots before a crash occurs.

Clear **Crash logs** if you've disabled [crash reporting](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#crash-reporting "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.").

App info and performance

Diagnostics

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace collects some performance information, for example, loading time of applications and activities or travel time of web requests.

App info and performance

Other app performance data

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") Yes

Dynatrace captures some app performance data, for example, a device's battery level or screen resolution. In Google Play Console, you cannot specify what app performance data is collected.

App performance data collected by Dynatrace

* Battery level
* Built-in RAM
* Free RAM
* Device model
* CPU type
* Carrier name
* Network connection type, for example, mobile, WiFi, or LAN
* Network technology, for example, 2G, 3G, 4G, 5G, 802.11x
* Screen resolution
* Orientation (portrait or landscape)
* App version
* App name
* User language
* Android version
* New user (for the first session)

Device or other IDs

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Dynatrace does not capture or report any device ID. We suggest that you avoid reporting device IDs via manual instrumentation.

## Data usage and handling

You also need to provide the information on how the data is used and handled for each data type that you've selected in the **Data types** section. Select **Start** to proceed.

Use the table below for all data types captured by OneAgent.

Question

Answer

Note

Is this data collected, shared or both?

Collected

Is this data processed ephemerally?

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") No

Is this data required for your app, or can users choose whether it's collected?

Data collected is required (users can't turn off this data collection)

Select **Users can choose whether this data is collected** if you've enabled the [user opt-in](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") for your mobile app.

Why is this user data collected?

Analytics

## Related topics

* [Preparing for Google Play's new safety sectionï»¿](https://android-developers.googleblog.com/2021/07/new-google-play-safety-section.html)
* [Provide information for Google Play's Data safety sectionï»¿](https://support.google.com/googleplay/android-developer/answer/10787469)
* [Configure data privacy settings for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")