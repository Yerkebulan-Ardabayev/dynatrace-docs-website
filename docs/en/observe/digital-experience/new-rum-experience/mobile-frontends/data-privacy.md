---
title: Configure data privacy settings for mobile frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/mobile-frontends/data-privacy
scraped: 2026-02-28T21:34:19.425081
---

# Configure data privacy settings for mobile frontends

# Configure data privacy settings for mobile frontends

* Latest Dynatrace
* How-to guide
* Published Jan 12, 2026

For many companies, ensuring the privacy of their customers' personal data is an important component of the digital business success. Dynatrace provides numerous privacy enhancements that you can use to configure the data privacy settings of your apps. When you properly set up these settings, this helps to protect your customers' personal data and to ensure your organization's compliance with the General Data Protection Regulation (GDPR), data disclosure requirements of app stores, and other data protection laws and regulations.

While Dynatrace offers numerous data privacy settings configurable both on the [environment](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") and application levels, it's only your responsibility to properly set up these settings and take precautions that protect your customers' personal data.

## User opt-in mode

With opt-in mode, each user of your application can set their data privacy preferences and decide whether they want or don't want to share their information. They can choose exactly what types of information they are willing to share. For example, one user might allow you only to report crashes, while the other might permit you also to capture performance and user data.

### Possible flow for user opt-in mode

The following steps describe the standard workflow for setting up the user opt-in mode for your mobile applications.

1. You [enable user opt-in mode](#enable-opt-in-mode) via a special flag or key and re-instrument your application.
2. At startup, OneAgent checks whether a user has already configured their data privacy preferences.

   By default, the following default data privacy preferences are used for all users who haven't yet set their data privacy preferences:

   * Data collection level: `Off` (monitoring data is not sent to Dynatrace)
   * Crash reporting: `Off` (crash reports are not sent to Dynatrace)

   Thanks to that, upon the first launch of your app, no data is shared with Dynatrace.
3. If the user hasn't configured their data privacy preferences, you show a dialog (see example below) asking for the user's permission to capture the performance data (corresponds to the **Performance** [data collection level](#data-collection-levels)), include their personal data in the information reported to Dynatrace (corresponds to the **User behavior** data collection level), and report crashes.

   Donât forget to create and show users the dialog with the data privacy settings. The users of your application will use this dialog to set their data privacy settings.
4. The user sets their data privacy preferences; you use the API calls to store the user's data privacy preferences.
5. Upon the next startup of your application, OneAgent applies the new data privacy preferences and reports only as much data as the particular user has agreed to share with Dynatrace.

![User opt in mode mobile](https://dt-cdn.net/images/gdpr-mobile-1-1221-621bb17f17.png)

### Enable opt-in mode

To activate the opt-in mode for mobile applications

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Mobile** to view all mobile frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Data privacy**.
5. Turn on **Enable user opt-in mode**.
6. Update your application's configuration file (build file for Android, [`Info.plist`](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") for iOS, and `dynatrace.config.<extension>` for cross-platform frameworks) by adding a special flag or key that enables opt-in mode.

   Check the instrumentation wizard for the updated configuration code snippet.
7. Rebuild your application so that the new configuration takes effect.

Check the sections below for detailed instructions on how to set up the mobile user opt-in mode for your applications.

[Android SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#data-privacy) [iOS SDK](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#privacy) [Cordova](https://www.npmjs.com/package/@dynatrace/cordova-plugin#user-privacy-options) [Flutter](https://pub.dev/packages/dynatrace_flutter_plugin#useroptin) [React Native](https://www.npmjs.com/package/@dynatrace/react-native-plugin#user-opt-in-mode) [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#useroptin) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui#useroptin) 

### Data collection levels

The table below describes the available data collection levels and shows whether [user tags](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") and custom user actions, events, values, and errors are reported for a particular level.

1

A single `Loading <App>` event is sent to track the number of users that opted out.

2

If you haven't configured user tagging and custom event or value reporting, the **User behavior** level works similarly to the **Performance** level.

## User tracking

For RUM Classic, OneAgent for Mobile tags HTTP requests with the `x-dynatrace` header. Dynatrace uses this header to link the mobile part of a web request with the service part captured by another OneAgent. For the New RUM Experience, OneAgent for Mobile tags HTTP requests using the `traceparent` and `tracestate` headers.

For hybrid applications, the `dtAdk` cookie allows to join a session from OneAgent for Mobile and a session from the RUM JavaScript so that these sessions appear as a single session, while the `dtAdkSettings` cookie is used for syncing settings between OneAgent for Mobile and the RUM JavaScript.

## User action masking

If you want to avoid capturing personal information for all user actions in your mobile app, check the related sections on user action masking for [Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#mask-user-actions "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") or [iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#mask-user-actions "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

After you enable user action masking for your mobile app, OneAgent replaces all `Touch on <control title>` action names with the class name or type of the control that the user touched. For example, `Touch on Account 123456` is changed to `Touch on Button`.

## Data privacy questionnaire in app stores

To learn what data OneAgent captures and complete the data privacy questionnaire in Google Play Console or App Store Connect, see the following pages:

* [Data safety guidance for Android](/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.")
* [User privacy for iOS](/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.")