---
title: Get started with Android monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring
scraped: 2026-02-25T21:31:24.061629
---

# Get started with Android monitoring

# Get started with Android monitoring

* How-to guide
* 2-min read
* Updated on Sep 06, 2023

To monitor your Android app, you first need to create a mobile application in Dynatrace and then instrument your actual Android app.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a mobile application in Dynatrace**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#create-app-ui "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Instrument your Android app**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrument-app "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Fine-tune the instrumentation**](/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#adjust-instrumentation "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")

## Step 1 Create a mobile application in Dynatrace

Before instrumenting your actual Android app, create a [mobile application](/docs/observe/digital-experience/rum-concepts/applications#mobile "Learn about monitored applications in Real User Monitoring and the different application types supported by Dynatrace.") in Dynatrace. You will use this application to monitor and analyze your Android app.

To create a mobile application in Dynatrace

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.

## Step 2 Instrument your Android app

When you have a mobile application in Dynatrace, instrument your actual Android app with the Dynatrace Android Gradle plugin or OneAgent SDK for Android.

[### Dynatrace Android Gradle plugin

To auto-instrument your Android project, use the Dynatrace Android Gradle plugin. It integrates the auto-instrumentation process into your Android build.](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.")[### OneAgent SDK for Android

If you can't use our plugin due to technical limitations, try standalone manual instrumentation with OneAgent SDK.](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Use OneAgent SDK for Android to manually instrument your Android application.")

## Step 3 Fine-tune the instrumentation

After you've instrumented your Android app, you might want to configure some additional settings:

* [Adjust communication with OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace.")
* [Configure the auto-instrumentation process](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")
* Create custom actions, report errors, tag specific users, and more using [OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* Enable and configure [Session Replay on crashes](/docs/observe/digital-experience/session-replay/session-replay-android "Set up Session Replay for your Android apps to learn which actions your users perform.")
* [Configure the data privacy settings](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")
* Learn what [data Dynatrace captures for your Android app](/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.") to complete or update the Data safety form in Google Play Console

## Access mobile instrumentation wizard

The mobile instrumentation wizard in Dynatrace provides you with get-started instructions on instrumenting your mobile applications. The wizard also contains code snippets with your application identification keys that you'll need to add to your project's build file. The application identification keysâ`applicationId` and `beaconUrl`âare required so that your application can send monitoring data to Dynatrace.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Instrumentation wizard**.
5. Select **Android**.

## Related topics

* [Dynatrace Android Gradle plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.")
* [Manually instrument your application using OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Use OneAgent SDK for Android to manually instrument your Android application.")