---
title: Get started with Android monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring
scraped: 2026-03-06T21:28:16.242622
---

# Get started with Android monitoring


* Classic
* How-to guide
* 2-min read
* Updated on Sep 06, 2023

To monitor your Android app, you first need to create a mobile application in Dynatrace and then instrument your actual Android app.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a mobile application in Dynatrace**](get-started-with-android-monitoring.md#create-app-ui "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Instrument your Android app**](get-started-with-android-monitoring.md#instrument-app "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Fine-tune the instrumentation**](get-started-with-android-monitoring.md#adjust-instrumentation "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.")

## Step 1 Create a mobile application in Dynatrace

Before instrumenting your actual Android app, create a mobile application in Dynatrace. You will use this application to monitor and analyze your Android app.

To create a mobile application in Dynatrace

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.

## Step 2 Instrument your Android app

When you have a mobile application in Dynatrace, instrument your actual Android app with the Dynatrace Android Gradle plugin or OneAgent SDK for Android.

### Dynatrace Android Gradle plugin

To auto-instrument your Android project, use the Dynatrace Android Gradle plugin. It integrates the auto-instrumentation process into your Android build.### OneAgent SDK for Android

If you can't use our plugin due to technical limitations, try standalone manual instrumentation with OneAgent SDK.

## Step 3 Fine-tune the instrumentation

After you've instrumented your Android app, you might want to configure some additional settings:

* Adjust communication with OneAgent SDK for Android
* Configure the auto-instrumentation process
* Create custom actions, report errors, tag specific users, and more using OneAgent SDK for Android
* Enable and configure Session Replay on crashes
* Configure the data privacy settings
* Learn what data Dynatrace captures for your Android app to complete or update the Data safety form in Google Play Console

## Access mobile instrumentation wizard

The mobile instrumentation wizard in Dynatrace provides you with get-started instructions on instrumenting your mobile applications. The wizard also contains code snippets with your application identification keys that you'll need to add to your project's build file. The application identification keysâ`applicationId` and `beaconUrl`âare required so that your application can send monitoring data to Dynatrace.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Instrumentation wizard**.
5. Select **Android**.

## Related topics

* Dynatrace Android Gradle plugin
* Manually instrument your application using OneAgent SDK for Android