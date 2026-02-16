---
title: Instrument mobile apps with Dynatrace Cordova plugin
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova
scraped: 2026-02-16T09:21:33.659717
---

# Instrument mobile apps with Dynatrace Cordova plugin

# Instrument mobile apps with Dynatrace Cordova plugin

* How-to guide
* 5-min read
* Updated on Oct 12, 2022

Hybrid mobile apps combine the benefits of native mobile apps, such as phone hardware and deployment via an app store, with the flexibility and platform independence of modern web technologies.

The Dynatrace Cordova plugin allows you to instrument apps that are built on top of Apache Cordova. This includes apps that use Capacitor, Ionic, or IBM mobile first. The Cordova plugin makes it easy to monitor your hybrid apps using the following technologies:

* OneAgent for Mobile, which monitors the native part of your app
* RUM JavaScript, which monitors the performance of the web-based part of your app

For detailed technical documentation, see the [Dynatrace Cordova pluginï»¿](https://www.npmjs.com/package/@dynatrace/cordova-plugin) page on the npm site.

## Set up hybrid mobile app monitoring

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.
4. From the application settings, select **Instrumentation wizard** and select your mobile app platform, for example, **Cordova**.

   ![Creating an app in Dynatrace](https://dt-cdn.net/images/setup-wizard-1764-763c621790.png)
5. Enter the `cordova plugin add @dynatrace/cordova-plugin --save` command in the root directory of your Cordova-based project to install the Dynatrace Cordova plugin.
6. Select **Monitor the web view** to enable the web view monitoring.
7. Select **Download dynatrace.config.js**, and add the downloaded file to the root of your Cordova app workspace next to the `config.xml` file.
8. Build your project using `cordova build android` or `cordova build ios`.

When you build your Android or iOS app, the Cordova plugin automatically instruments your app using OneAgent for Mobile, which monitors the native part of your hybrid app. This provides visibility into app starts, user actions, crash reports, and device metadata such as model and OS version. The monitoring data collected by OneAgent for Mobile is encapsulated in a mobile app in Dynatrace.

To capture user actions in web views, Dynatrace uses the [RUM JavaScript](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case"), which is also used for all web applications that are [set up for agentless Dynatrace monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."). The Cordova plugin automatically injects the RUM JavaScript directly into your HTML sources. The monitoring data collected by the RUM JavaScript is encapsulated in a web application in Dynatrace. This application receives all monitoring data and generates an API token so that the Cordova plugin can retrieve the RUM JavaScript from the REST API.

![Cordova app instrumentation](https://dt-cdn.net/images/instrumentcordovaapp-1913-f1c90c1409.png)

## Start monitoring and analyzing your app

1. Launch your hybrid app in an emulator or on a test device, and click through the use cases to generate some traffic that Dynatrace can monitor. When you're done, close your app to ensure that all data is sent to Dynatrace. Note that OneAgent for Mobile may cache the data for up to 2 minutes.
2. In Dynatrace, go to **Mobile**.
3. Select your new hybrid app from the list of applications.

   All performance analysis metrics data related to your app is displayed on your hybrid app's overview page. The **Hybrid app** section displays the overall details of the performance of the web portion of your app.

   ![Analyze mobile apps](https://dt-cdn.net/images/analyze-mobile-app-1954-6c4199ccdd.png)
4. Select **View web application** to analyze performance data that Dynatrace captures via the injected RUM JavaScript.

   The web application overview page contains user actions that are captured in the web view, so you'll find a high percentage of your app's user actions listed here.

   ![Analyze web apps](https://dt-cdn.net/images/analyze-web-app-1954-d5e81e0ff9.png)

   Performance data is split across two application views. However, Dynatrace consolidates all detected user actions from these application views to a single user and a single user session.
5. Go to ![Session Segmentation](https://dt-cdn.net/images/session-segmentation-512-5278e8fa16.png "Session Segmentation") **Session Segmentation** to access the **User sessions** page. In the **Filtered by** field, enter **Application**, and select your hybrid mobile app, which allows you to focus analysis on your newly created app.
6. Select the default user created for your hybrid app from the **User** column. Notice that this user has accessed two appsâa mobile app and a web app.

   ![Analyze user](https://dt-cdn.net/images/analyze-user-1950-e23a310611.png)
7. Select a user session. You should see that all user actions captured in the mobile and web part of your hybrid app have been combined into a single session, along with the metadata that enables Dynatrace to show which user actions were captured by OneAgent for Mobile and which were captured by the RUM JavaScript.

   The following chart shows the sequence of user actions, when they occurred during a user session, and the wait time between the actions.

   ![Joined user session](https://dt-cdn.net/images/joined-user-session-1571-0684cc8268.png)

From here, you can continue with your user-experience analysis. You can add additional filters to focus on the sessions you want to take a closer look at, or you can drill down to the user action waterfalls of your app's web and mobile sessions.

## Related topics

* [Apache Cordova monitoringï»¿](https://www.dynatrace.com/technologies/cordova-monitoring/)
* [Dynatrace Cordova plugin (npm site)ï»¿](https://www.npmjs.com/package/@dynatrace/cordova-plugin)