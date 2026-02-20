---
title: Instrument hybrid apps
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app
scraped: 2026-02-20T21:13:43.905249
---

# Instrument hybrid apps

# Instrument hybrid apps

* How-to guide
* 4-min read
* Published Aug 10, 2021

With Dynatrace, you can set up Real User Monitoring for various types of hybrid and cross-platform mobile applications.

You can instrument your mobile application using one of our plugins. However, if you are using a hybrid platform that doesn't support our plugins or your requirements disallow third-party plugins, follow the steps below to instrument your hybrid application.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a hybrid application in Dynatrace**](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app#create-app-in-ui "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OneAgent and adjust its configuration**](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app#set-up-oneagent "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Insert the RUM JavaScript into your hybrid app's HTML files**](/docs/observe/digital-experience/mobile-applications/instrument-hybrid-app#add-rum-js "Learn how you can instrument various types of hybrid and cross-platform mobile apps.")

For hybrid applications, the native app is monitored via OneAgent for Mobile, while the browser part is observed by the Dynatrace RUM JavaScript.

For hybrid apps, a user session is billed only once. See [Digital Experience Monitoring (DEM units)](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.") for more details.

Also note that one "hybrid" session might be displayed as two separate sessions in Dynatrace: one as a web session and another as a mobile session.

## Step 1 Create a hybrid application in Dynatrace

The first step is to create a hybrid application that consists of two parts:

* **Mobile application** gets the monitoring data from the native part of a hybrid app. User actions and crashes from the mobile app are reported to this application.
* **Web application** captures data from the browser part of a hybrid app. User actions from the web views are reported to this web application.

To create an application in Dynatrace

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.
4. From the application settings, select **Instrumentation wizard** > **Cordova**.
5. Follow the steps described in the wizard. Do not forget to select **Monitor the web view** to create a web application.

   ![Monitor web view via Cordova wizard](https://dt-cdn.net/images/monitor-web-view-cordova-wizard-2440-449be51ccc.png)

   If the app that you're instrumenting is not a [Cordova app](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin."), skip the steps related to the Cordova plugin.

## Step 2 Set up OneAgent and adjust its configuration

Use OneAgent for Mobile to instrument the native part of your hybrid application. The mobile application that you've created in step 1 offers you instrumentation wizards for the native part of your application.

Android

iOS

To auto-instrument your Android project, use the [Dynatrace Android Gradle plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.").

After that, [adjust the default configuration](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration#hybrid-apps "Learn how to configure the Dynatrace Android Gradle plugin to modify the OneAgent SDK configuration.") to allow OneAgent to pass cookies to the WebView and domains specified in your app's top-level build file.

Here is the example configuration for the `easytravel.com` domain:

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



domains '.easytravel.com'



}



}



}



}
```

To monitor your iOS application, you need to instrument [OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.").

After that, use the [`DTXHybridApplication`, `DTXSetCookiesForDomain`, and `DTXSetSecureCookiesForDomain` configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#hybrid "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to allow OneAgent to pass cookies to `WKWebView` and domains specified in your app's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

Here is the example configuration for the `easytravel.com` domain:

```
<key>DTXHybridApplication</key>



<true/>



<key>DTXSetCookiesForDomain</key>



<array>



<string>.easytravel.com</string>



</array>



<key>DTXSetSecureCookiesForDomain</key>



<array>



<string>.example.com</string>



</array>
```

Apple Pay does not work in WKWebView

When the `DTXHybridApplication` configuration key is set to `true`, Apple Pay does not work on webpages loaded in `WKWebView`.

To protect the security of transactions in `WKWebView`, Apple [disallows the use of Apple Pay with script injection APIsï»¿](https://developer.apple.com/documentation/safari-release-notes/safari-13-release-notes#Payment-Request-API), such as `WKUserScript` or `evaluateJavaScript`. Dynatrace uses `evaluateJavascript` to pass the correlation data from the native layer to `WKWebView`, and this process disables Apple Pay.

As a workaround, set the `DTXHybridApplication` [configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to `false` to stop the injection of the script from OneAgent. However, this will also remove the correlation of mobile and web sessions for your hybrid app. Corresponding mobile and web sessions will not be merged, which leads to two billed sessions instead of one.

It is important to add the required domains to your top-level build file (Android) or [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") (iOS) so that Dynatrace can identify mobile and web sessions within your app and merge these sessions into the same "hybrid" session.

## Step 3 Insert the RUM JavaScript into HTML sources

To capture user actions in the web-based part of your hybrid application, use the RUM JavaScript. You'll need to manually insert the JavaScript code or tag into your HTML sources. See [Set up agentless Real User Monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") for more information. Note that the RUM JavaScript is available in [several formats](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").

After you add the RUM JavaScript to the HTML files, user actions from your hybrid app's web views are reported to the web application that you've created in step 1.

If you've already instrumented the web-based part of your hybrid app, then you don't need to manually add the RUM JavaScript to the HTML sources of your app.

## Related topics

* [Instrument mobile apps with Dynatrace Cordova plugin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.")
* [Instrument mobile apps with Dynatrace Flutter plugin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/flutter "Learn how to auto-instrument your Flutter applications with OneAgent.")
* [Instrument mobile apps with Dynatrace React Native plugin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native "Auto-instrument your React Native applications with OneAgent.")
* [Instrument mobile apps with Dynatrace Xamarin NuGet package](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget "Monitor Xamarin apps with Dynatrace OneAgent.")