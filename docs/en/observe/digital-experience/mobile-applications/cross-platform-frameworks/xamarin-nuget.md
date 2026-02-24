---
title: Instrument mobile apps with Dynatrace Xamarin NuGet package
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget
scraped: 2026-02-24T21:32:50.023514
---

# Instrument mobile apps with Dynatrace Xamarin NuGet package

# Instrument mobile apps with Dynatrace Xamarin NuGet package

* How-to guide
* 12-min read
* Updated on Apr 16, 2024

The Dynatrace Xamarin NuGet package helps auto-instrument your Xamarin app with OneAgent for Android and iOS as well as provides an API for [manual instrumentation](#usage-mobile-agent). The package is compatible with `Xamarin.iOS`, `Xamarin.Android`, and `Xamarin.Forms` projects.

Deprecation and end of support for Dynatrace Xamarin NuGet package

On May 1, 2024, [Microsoft will end support for all Xamarin SDKsï»¿](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin#microsoft-support). For this reason, we're deprecating the Dynatrace Xamarin NuGet package in May 2024. We will let you know in which upcoming package version we will be only fixing bugs and addressing important security issues.

Also, in accordance with the [Dynatrace Support Policyï»¿](https://www.dynatrace.com/company/trust-center/support-policy/), we will end support for the Dynatrace Xamarin NuGet package in May 2025.

We recommend that you [upgrade your Xamarin projects to .NETï»¿](https://learn.microsoft.com/en-gb/dotnet/maui/migration) and use the [Dynatrace .NET MAUI NuGet package](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui "Monitor .NET MAUI applications with Dynatrace OneAgent.") instead of the deprecated Xamarin NuGet package.

## Supported features

#### Auto-instrumentation

* User actions
* Lifecycle events
* Web requests
* Crashes

#### Manual instrumentation

* Custom actions
* Web requests
* Values
* Events
* Errors
* Crashes
* User tagging

## Requirements

* **For Android:**

  + Android version 5.0+ (API 21+)
  + Xamarin.Android SDK version 10.1.x+
* **For iOS:** iOS version 12+
* **For Xamarin.Forms:** .NET Standard version 2.0+

## Set up the package

Perform the following steps to set up the Dynatrace Xamarin NuGet package for your Xamarin app.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install the Dynatrace Xamarin NuGet package**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#install-package "Monitor Xamarin apps with Dynatrace OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create an application and get the config file**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#installation-dynatrace "Monitor Xamarin apps with Dynatrace OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add the config file to your project**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#configure-app "Monitor Xamarin apps with Dynatrace OneAgent.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Add the OneAgent start method**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#start-method "Monitor Xamarin apps with Dynatrace OneAgent.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

Xamarin.Forms only

**Set up Xamarin.Forms DependencyService**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#usage-forms "Monitor Xamarin apps with Dynatrace OneAgent.")[![Step 6 optional](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Step 6 optional")

**Enable automatic web request instrumentation**](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#http-client "Monitor Xamarin apps with Dynatrace OneAgent.")

### Step 1 Install the NuGet package

Add the Dynatrace Xamarin NuGet package to all the required projects.

1. In Visual Studio, right-click the main project of your app and select **Manage NuGet packages**.
2. Find [**Dynatrace.OneAgent.Xamarin** from nuget.orgï»¿](https://www.nuget.org/packages/Dynatrace.OneAgent.Xamarin) and select **Add Package**.
3. Select the checkboxes of all the projects to which you want to add the NuGet package.
4. Select **OK**.

### Step 2 Create an application and get the config file

Create a new mobile application in Dynatrace and download the configuration file.

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.
4. From the application settings, select **Instrumentation wizard** > **Xamarin**.
5. Under step 2, select **Download dynatrace.config.json** to get the configuration file.

### Step 3 Add the config file to your project

Add the [`dynatrace.config.json` file](#config-file), which you downloaded in the previous step, to your project.

Android

iOS

Add the `dynatrace.config.json` file to the `Assets` directory of your Android project.

Add the `dynatrace.config.json` file to the `Resources` directory of your iOS project.

Before each build, our package automatically creates a new `Dynatrace.plist` file based on the options set in your configuration file.

### Step 4 Add the OneAgent start method

The start method is required for OneAgent to start.

Android

iOS

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

### Step 5 Set up Xamarin.Forms `DependencyService`

Xamarin.Forms only

This instruction is for Xamarin.Forms versions 4.7.0+, which use `RegisterSingleton`. For earlier Xamarin.Forms versions, see the [instruction below](#xamarin-forms-4-6).

Register the interface at startup in the native part of your Xamarin.Forms application, and paste the following code right after `Forms.Init()`.

The following example is for an Android Forms application:

```
using Dynatrace.Xamarin;



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



Xamarin.Forms.DependencyService.RegisterSingleton<IDynatrace>(Agent.Instance);



LoadApplication(new App());
```

The following code in your Xamarin.Forms application allows you to access OneAgent:

```
using Dynatrace.Xamarin;



IDynatrace dynatrace = DependencyService.Get<IDynatrace>();
```

In case of auto-instrumentation, you also need to apply the Dynatrace Xamarin NuGet package to the native parts of your application.

Xamarin.Forms 4.6.0 and earlier

If you can't use `DependencyService.RegisterSingleton` as your Xamarin.Forms version is 4.6.0 or earlier, there is a workaround. The following code snippet shows how this works for Xamarin.Forms and Android, but you can easily apply it to iOS as well.

The `App.xaml.cs` file in the Xamarin.Forms part:

```
public partial class App : Application



{



static readonly Dictionary<Type, Func<object, object>> factories = new Dictionary<Type, Func<object, object>>();



public App()



{



InitializeComponent();



DependencyResolver.ResolveUsing((type, args) => factories.ContainsKey(type) ? factories[type].Invoke(args) : null);



IDynatrace Dynatrace = DependencyService.Resolve<IDynatrace>();



Dynatrace.Start(null);



}



public static void Register(Type type, Func<object, object> factory)



{



factories[type] = factory;



}



...



}
```

The Android part, where you have to call `RegisterSingleton`, should look like this:

```
public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity



{



protected override void OnCreate(Bundle savedInstanceState)



{



...



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



App.Register(typeof(IDynatrace), (o) => Agent.Instance);



LoadApplication(new App());



}



...



}
```

### Step 6 optional Enable automatic web request instrumentation Optional

You can optionally use the following method to enable the auto-instrumentation of web requests. The `HttpMessageHandler` used by `HttpClient` takes care of the manual web request instrumentation.

```
using Dynatrace.Xamarin;



var httpHandler = Agent.Instance.GetHttpMessageHandler();



var httpClient = new HttpClient(httpHandler);
```

Moreover, you can also have your own HTTP handler:

```
using Dynatrace.Xamarin;



var defaultHttpHandler = new HttpClientHandler();



var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);



var httpClient = new HttpClient(httpHandler);
```

## Manual instrumentation

The sections below describe how to start OneAgent manually, create custom actions, instrument web requests, and report values, events, and crashes.

### Start OneAgent

You can use the manual startup with a configuration builder (Android) or a configuration dictionary (iOS).

1. Modify the [`dynatrace.config.json` file](#config-file) to disable OneAgent autostart.

   Android

   iOS

   ```
   {



   "android": {



   "autoStart": {



   "enabled": false



   }



   }



   }
   ```

   ```
   {



   "ios": {



   "DTXAutoStart": false



   }



   }
   ```

   Don't add additional properties to the configuration file. If you do that, the build fails with an exception.
2. Start OneAgent manually and pass the required properties.

   Android

   iOS

   ```
   using Dynatrace.Xamarin;



   Agent.Instance.Start(new ConfigurationBuilder("<insertBeaconURL>","<insertApplicationID>") .BuildConfiguration());
   ```

   ```
   using Dynatrace.Xamarin;



   var configDict = new Dictionary<string, object>();



   configDict.Add("DTXApplicationID", "<insertApplicationID>");



   configDict.Add("DTXBeaconURL", "<insertBeaconURL");



   Agent.Instance.Start(configDict);
   ```

### Create custom actions

You can create custom actions and enhance them with additional information such as values, events, and errors.

Call `EnterAction` to start a custom action and `LeaveAction` to close a custom action. Timing is measured automatically.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



//Perform the action and whatever else is needed.



myAction.LeaveAction();
```

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

Check the following links for information on user action naming: [Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-naming "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") and [iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

When the [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Create child actions

Besides generating standalone custom actions, you can also create [child actions](/docs/observe/digital-experience/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.").

Child actions are similar to parent custom actions. When a parent action is closed, all child actions of the parent action are automatically closed.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



var mySubAction = myAction.EnterAction("Tap on Confirm again");



//Perform the action and whatever else is needed.



mySubAction.LeaveAction();



myAction.LeaveAction();
```

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

There's no limit on the number of child actions attached to a custom action. However, note that you can have only one level of child actionsâyou can't create a child action for another child action (child actions can't have their own child actions). Also, refer to [User session structure for individual user](/docs/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Child actions are not displayed on the [user session details page](/docs/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), but you can view them on the [waterfall analysis page](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a custom action to which these child actions are attached.

### Cancel custom actions

If you need to cancel an already created but not yet closed custom action, call `Cancel`. Canceling an action discards all data associated with it: all reported values, events, and errors are discarded; all child actions are canceled.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



// Action is canceled



myAction.Cancel();
```

You can't cancel a closed action, so calling `Cancel` after `LeaveAction` is impossible for the same action. The same goes for closing a canceled action: you can't call `LeaveAction` after using `Cancel` for the same action.

### Instrument web requests

Use the following code snippet to instrument web requests:

```
using Dynatrace.Xamarin;



// Create an action



var webAction = Agent.Instance.EnterAction(actionName: "WebRequest Action");



// Generate a new unique tag associated with the web request action



string requestTag = webAction.GetRequestTag(url);



string requestTagHeader = webAction.GetRequestTagHeader();



// Place the Dynatrace HTTP header on your web request



httpClient.DefaultRequestHeaders.Add(requestTagHeader, requestTag);



// Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = (WebRequestTiming)Agent.Instance.GetWebRequestTiming(requestTag, url);



// Start web request timing before the HTTP request is sent



timing.StartWebRequestTiming();



try



{



var response = await httpClient.GetAsync(url);



// Stop web request timing when the HTTP response is received and the response body is obtained



timing.StopWebRequestTiming(url, (int)response.StatusCode, response.ReasonPhrase);



}



catch (HttpRequestException exception)



{



// Stop web request timing when a connection exception occurs



timing.StopWebRequestTiming(url, -1, exception.ToString());



}



finally



{



// Leave an action



webAction.LeaveAction();



}
```

### Report a value

The `reportValue` method allows you to report key-value pairs of metadata that you can later view in the Dynatrace web UI and convert into [user action and user session properties](/docs/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). The reported values must be part of a user action.

You can report values of the following data types:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);



ReportValue(valueName: string, value: double);



ReportValue(valueName: string, value: string);
```

For instance, to report a `string` value within the `Tap on Confirm` action, use the following code:

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



myAction.ReportValue("Customer type", "Gold");



myAction.LeaveAction();
```

To view the reported values in the Dynatrace web UI, go to the details of the user action that should contain that metadata and scroll down to the **Reported values** section.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

To add action and session properties based on the reported values and then use these properties to create powerful queries, segmentations, and aggregations, see [Define user action and user session properties for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

When the [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Report an event

For any open action, you can report an event. Use the following API call:

```
ReportEvent(eventName: string);
```

If you want to report standalone events with lots of additional information, see [Report a business event](#report-business-event).

When the [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Report an error

To report an [error](/docs/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace."), use the `ReportError` method.

```
ReportError(errorName: string, errorCode: number);
```

When the [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Report an error stack trace

To report an error stack trace, use the following API call:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Report a crash

To report a [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace."), use the following API call.

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

You can also use an exception object:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

The time when the crash details are sent to Dynatrace depends on your mobile application operating system.

* **Android**

  In general, the crash details are sent immediately after the crash, so the user doesnât have to relaunch the application. However, in some cases, the application should be reopened within 10 minutes so that the crash report is sent. Note that Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).
* **iOS**

  The crash details are sent only when the user reopens the mobile application (so on the next application launch). However, if the user doesn't open the application within 10 minutes, the crash report is deleted. This is because Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

Reporting a crash forces a user session to be completed. Any subsequent actions are included in a new user session.

Android only When you use automated crash reporting, Visual Studio might catch the exception before OneAgent. If you notice that Dynatrace doesn't report crashes to your environment, make sure that [you're not using the debug option in Visual Studio](#debugger-turn-off). Otherwise, the debugger catches the crash and nothing is reported to your Dynatrace environment.

### Report a business event

Dynatrace SaaS version 1.253+

With `sendBizEvent`, you can report business events. These are standalone events, as Dynatrace sends them separately from user actions or user sessions.

Business events are only captured for monitored sessions. When OneAgent is disabled either through a special flag or due to [cost and traffic control](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-cost-and-traffic-control-mobile "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for mobile apps."), business events are not reported for such sessions. Note that this behavior might be subject to change in the future, potentially allowing business events to be sent to Dynatrace regardless of session monitoring.

For additional details on business events, refer to [Business Observability](/docs/observe/business-observability "Basic concepts, setup and configuration, and use cases for Dynatrace Business Observability").

```
using Dynatrace.Xamarin;



var attributes = new Dictionary<string, JsonValue>();



attributes.Add("event.name", "Confirmed Booking");



attributes.Add("screen", "booking-confirmation");



attributes.Add("product", "Danube Anna Hotel");



attributes.Add("amount", 358.35);



attributes.Add("currency", "USD");



attributes.Add("reviewScore", 4.8);



attributes.Add("arrivalDate", "2022-11-05");



attributes.Add("departureDate", "2022-11-15");



attributes.Add("journeyDuration", 10);



attributes.Add("adultTravelers", 2);



attributes.Add("childrenTravelers", 0);



Agent.Instance.SendBizEvent("com.easytravel.funnel.booking-finished", attributes);
```

### Tag specific users

You can tag each user of your application with a unique user name. This enables you to search and filter specific user sessions and analyze individual user behavior over time. For more details, see [User tagging](/docs/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Make the following API call to tag the current session with a particular name:

```
using Dynatrace.Xamarin;



Agent.Instance.IdentifyUser("John Smith");
```

OneAgent for Android version 237+ OneAgent for iOS version 235+ Sessions split due to idle or duration timeout are re-tagged automatically.

When OneAgent ends a tagged session because the session duration has reached its set limit or due to the user's inactivity, the subsequent session is re-tagged automatically. You don't need to provide the user identification information again.

However, note that OneAgent does not re-tag the subsequent session in the following cases:

* When you explicitly end a tagged user session via [`endVisit`](#end-session)
* When the user or the mobile operating system closes or force stops the app
* When OneAgent ends the current user session and generates a new session after the privacy settings have been changed

See [User sessions > Session end](/docs/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") to learn when OneAgent ends a mobile user session.

When the [user opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### End a session

You can force a session to end via the API call. This also closes all open actions and starts a new session.

```
using Dynatrace.Xamarin;



Agent.Instance.EndVisit();
```

### Configure data privacy (opt-in mode)

With user opt-in mode, each user of your application can set their data privacy preferences and decide whether they want or don't want to share their information. When the opt-in mode is enabled, you need to ask each user for permission to capture their data; then, you store their data privacy preferences. For details, see [User opt-in mode](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

#### Enable user opt-in mode

To activate the user opt-in mode, set the `userOptIn` property (Android) or [`DTXUserOptIn` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") (iOS) to `true` in the [`dynatrace.config.json` file](#config-file).

#### Retrieve user's data privacy preferences

You can retrieve the data privacy preferences of a particular user.

To get the current `UserPrivacyOptions` configuration, use the following API call:

```
using Dynatrace.Xamarin;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();



// Get the individual settings for DataCollectionLevel and crash reporting



bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;



DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Change user's data privacy preferences

You can adjust the data privacy preferences based on the decision of a particular user.

To set new options on a `UserPrivacyOptions` object, use the following code:

```
using Dynatrace.Xamarin;



// Creating a new UserPrivacyOptions object requires setting the two parameters of DataCollectionLevel and crash reporting



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.Performance, false);



// Update the options with the setter



// Set a data collection level (user allowed you to capture performance and personal data)



options.DataCollectionLevel = DataCollectionLevel.UserBehavior;



// Allow crash reporting (user allowed you to collect information on crashes)



options.CrashReportingOptedIn = true;



// Get the values of the configuration with the getter



options.DataCollectionLevel;



options.CrashReportingOptedIn;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();
```

To apply the new `UserPrivacyOptions` configuration, use this code:

```
using Dynatrace.Xamarin;



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



Agent.Instance.ApplyUserPrivacyOptions(options);
```

The possible values for the [data collection level](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") are as follows:

* `Off`
* `Performance`
* `UserBehavior`

### Report GPS location

You can report the latitude and longitude.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Configuration file

The `dynatrace.config.json` configuration file contains your application ID, beacon URL, and some other settings.

* You can [download this file from Dynatrace](#installation-dynatrace) or create it manually.
* If you don't add a configuration file with at least the beacon URL and the application ID properties, the build fails. Alternatively, use the [manual startup](#start-agent) with a configuration builder (Android) or a configuration dictionary (iOS).
* When you use a specific build configurationâfor example, `Debug`, `Release`, or a custom-defined configurationâour package searches the `Assets` (Android) or `Resources` (iOS) directory for a configuration file named `dynatrace<Configuration>.config.json`. For example, if you're using the `Debug` build configuration, our package looks for a file named `dynatraceDebug.config.json`.
* If you want to specify a custom path for your configuration, set it via the `DynatraceConfigurationFile` property.

  Create `Directory.Build.props` in the Android/iOS (or general) project directory:

  ```
  <Project>



  <PropertyGroup>



  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>



  </PropertyGroup>



  </Project>
  ```

In summary, this results in the following order in which the configuration will be used:

1. Custom configuration path through `DynatraceConfigurationFile` property
2. Configuration-specific file like `dynatrace<Configuration>.config.json`
3. Default name `dynatrace.config.json`

The following is the `dynatrace.config.json` file structure for Android and iOS.

Android

iOS

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"agentBehavior": {



"startupLoadBalancing": true



}



}



}
```

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXStartupLoadBalancing": true



}



}
```

Never use dot notation for the configuration file. Always write in full bracket style.

## Enable OneAgent debug logs

If the instrumentation runs through and your application starts, but you see no data in your Dynatrace environment, you probably need to dig deeper to find out why OneAgents aren't sending any data. Opening up a support ticket is a great idea but gathering logs first is even better.

Android

iOS

Update your [`dynatrace.config.json` file](#config-file) to enable OneAgent debug logs.

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"debug": {



"agentLogging": true



}



}



}
```

Add the following configuration snippet to the [`dynatrace.config.json` file](#config-file):

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXLogLevel": "ALL"



}



}
```

## Enable build debug logs for Android

Android only

If the Android instrumentation fails, you most likely need to open a support ticket and provide build debug logs. To provide those logs, you need to set the `DynatraceInstrumentationLogging` property and change the build log level to `Diagnostic`.

1. Set the `DynatraceInstrumentationLogging` property. Choose one of the following options to do that:

   * Create `Directory.Build.props` in the Android project directory:

   ```
   <Project>



   <PropertyGroup>



   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>



   </PropertyGroup>



   </Project>
   ```

   * Add the `DynatraceInstrumentationLogging` property to the `.csproj` file of your project. Insert it into some existing `PropertyGroup`, depending on the configuration that you're executing.
2. Change the build output verbosity to `Diagnostic`. For details, see the Microsoft documentation on how to [change the amount of information included in the build logï»¿](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Rebuild your project.
4. Attach the build logs to the support ticket so that we can further analyze your issue.

## Troubleshooting

If you can't resolve a problem, check [Mobile applications: Issues with Dynatrace Xamarin NuGet packageï»¿](https://dt-url.net/xn638zc) in the Dynatrace Community.

## Related topics

* [Instrument Android apps](/docs/observe/digital-experience/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")
* [Instrument iOS apps](/docs/observe/digital-experience/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.")