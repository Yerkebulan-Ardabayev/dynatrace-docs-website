---
title: Instrument Android apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app
scraped: 2026-03-05T21:26:31.388242
---

# Instrument Android apps


* Classic
* Overview
* 2-min read
* Updated on Oct 07, 2025

The process of monitoring the user experience of native mobile applications is different from monitoring browser-based web applications. This is because mobile app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package.

To leverage Dynatrace for your Android app, check the [get started guide](instrument-android-app/get-started-with-android-monitoring.md "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.") for an overview of the required steps.

You can also explore our new [demo mobile applicationï»¿](https://dt-url.net/rs0229z) to get a feel of how the instrumentation with Dynatrace works. This sample application showcases the main features provided by the [Dynatrace Android Gradle Plugin](instrument-android-app/instrumentation-via-plugin.md "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") and the [OneAgent SDK for Android](instrument-android-app/instrumentation-via-oneagent-sdk.md "Learn what OneAgent SDK for Android is.").

[Jetpack Compose auto-instrumentation](instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") is enabled by default starting with Dynatrace Android Gradle plugin version 8.271.

Jetpack Compose auto-instrumentation for [Session Replay](../session-replay.md "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") is enabled by default starting with Dynatrace Android Gradle plugin version 8.325.

### [Dynatrace Android Gradle plugin](instrument-android-app/instrumentation-via-plugin.md "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.")

* [Instrument your application via Dynatrace Android Gradle plugin](instrument-android-app/instrumentation-via-plugin/instrumentation-via-plugin.md "Perform the steps in this topic before you begin instrumenting your app with the Dynatrace Android Gradle plugin.")
* [Configure monitoring capabilities of Dynatrace Android Gradle plugin](instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* [Configure Dynatrace Android Gradle plugin for instrumentation processes](instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation.md "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* [Adjust OneAgent configuration via Dynatrace Android Gradle plugin](instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration.md "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.")
* [Change Dynatrace Android Gradle plugin configuration based on the project structure](instrument-android-app/instrumentation-via-plugin/configure-multi-module-projects.md "Use the Dynatrace Android Gradle plugin for less common project architectures.")
* [Troubleshooting Dynatrace Android Gradle plugin](instrument-android-app/instrumentation-via-plugin/faqs.md "Learn about the problems that might occur while using the Dynatrace Android Gradle plugin.")

### [OneAgent SDK for Android](instrument-android-app/instrumentation-via-oneagent-sdk.md "Learn what OneAgent SDK for Android is.")

* [Instrumentation via OneAgent SDK for Android](instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android.md "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* [Adjust communication with OneAgent SDK for Android](instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication.md "Configure communication with OneAgent to report the user experience data to Dynatrace.")
* [Manually instrument your application using OneAgent SDK for Android](instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation.md "Use OneAgent SDK for Android to manually instrument your Android application.")

### Data privacy

[Configure data privacy settings for mobile applications](additional-configuration/configure-rum-privacy-mobile.md "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[Data safety guidance for Android](../../../manage/data-privacy-and-security/data-privacy/user-privacy-for-android.md "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.")

### Troubleshooting

[Mobile applications: Issues with mobile RUMï»¿](https://dt-url.net/82038db)

[Mobile applications: General issues with Dynatrace Android Gradle pluginï»¿](https://dt-url.net/b9238e6)

[Mobile applications: Build issues with Dynatrace Android Gradle pluginï»¿](https://dt-url.net/wd438of)

We no longer support Java 8 for the [Dynatrace Android Gradle plugin version 8.261+](instrument-android-app/instrumentation-via-plugin.md "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project."), as Java 11 is required for the latest version of the Android Gradle plugin API.

## Related topics

* [Configure Session Replay for Android](../session-replay/session-replay-android.md "Set up Session Replay for your Android apps to learn which actions your users perform.")
* [Instrument mobile apps with Dynatrace Xamarin NuGet package](cross-platform-frameworks/xamarin-nuget.md "Monitor Xamarin apps with Dynatrace OneAgent.")