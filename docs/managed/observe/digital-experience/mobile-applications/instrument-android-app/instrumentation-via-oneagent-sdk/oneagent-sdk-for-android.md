---
title: Instrumentation via OneAgent SDK for Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android
scraped: 2026-05-12T11:22:06.920502
---

# Instrumentation via OneAgent SDK for Android

# Instrumentation via OneAgent SDK for Android

* How-to guide
* 26-min read
* Updated on Mar 26, 2026

Use the OneAgent SDK for Android to report additional details about the user sessions in your mobile app. The OneAgent SDK for Android allows you to create custom actions, report errors, tag specific users, and more. The sections below explain how to enable these capabilities.

You can use the OneAgent SDK in Java and Kotlin.

## Start OneAgent

You should start OneAgent manually in the following cases:

* If you've [disabled the automatic OneAgent startup](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.")
* If you're using [standalone manual instrumentation](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Use OneAgent SDK for Android to manually instrument your Android application.") instead of auto-instrumentation

Use the [`Dynatrace.startup(Application, Configuration)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) API method, and start OneAgent manually in the [`Application.onCreate`ï»¿](https://developer.android.com/reference/android/app/Application#onCreate()) method.

Java

Kotlin

```
public class YourApplication extends Application {



@Override



public void onCreate() {



super.onCreate();



// provide the application context as parameter



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration());



}



}
```

```
class YourApplication : Application() {



override fun onCreate() {



super.onCreate()



// provide the application context as parameter



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration())



}



}
```

If you need to start OneAgent at a later stage, use the [`Dynatrace.startup(Activity, Configuration)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)) API method. Provide an active `Activity` as a parameter so that OneAgent can immediately monitor it.

Java

Kotlin

```
Dynatrace.startup(yourActiveActivity, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration());
```

```
Dynatrace.startup(yourActiveActivity, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration())
```

To get the correct application identification keys (`applicationId` and `beaconUrl`), access the [mobile instrumentation wizard](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Learn the steps you need to perform to instrument your Android app for monitoring with Dynatrace.") for your application.

OneAgent can only be started once per application. The OneAgent does not support multiple concurrent initializations in the same running app. The `appId` and `beaconUrl` parameters are not a mechanism for sending data to two different Dynatrace environments from the same application.

If your application supports Direct Boot, never call the `Dynatrace.startup` API method from a Direct Boot aware component. Also, check [Adjust communication with OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Configure communication with OneAgent to report the user experience data to Dynatrace.") to make sure that OneAgent can transmit data to Dynatrace.

### Configure OneAgent

Use the [DynatraceConfigurationBuilderï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/DynatraceConfigurationBuilder.html) class to customize OneAgent settings.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withUserOptIn(true)



.withCrashReporting(true)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withUserOptIn(true)



.withCrashReporting(true)



.buildConfiguration()
```

If you use a combination of manual and auto-instrumentation, the auto-instrumentation injects a `Dynatrace.startup` call into the `Application.onCreate` method. In this case, the injected `Dynatrace.startup` call is called before your manual `Dynatrace.startup` call, so your manual configuration is ignored.

Use the `autoStart.enabled` property to deactivate the auto-start feature from the auto-instrumentation. You can then [define a manual `Dynatrace.startup` call](#start-oneagent). In this case, you can override the values pre-configured from the auto-instrumentation.

OneAgent does not support running multiple instances targeting different environments simultaneously.

## User action monitoring

With user action monitoring, you can define and report custom actions. You can then enrich these custom actions using the following monitoring operations:

* [Create a child action](#child-actions)
* [Report an event](#report-event)
* [Report a value](#report-value)
* [Report an error](#report-errors)
* [Attach a web request to the user action](#attach-request-to-action)

Custom actions are different from the user actions created with the Dynatrace Android Gradle plugin. OneAgent does not automatically add additional events, such as web requests, to custom actions or close custom actions. However, when OneAgent shuts down or has to start a new session, it closes all open custom actions.

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Create custom actions

You can create custom actions and enhance them with additional information. If custom actions are not closed explicitly, OneAgent closes them and sends them to the Dynatrace Cluster.

Call `enterAction` to start a custom action and `leaveAction` to close a custom action. Timing is measured automatically.

Java

Kotlin

```
// start a custom action



DTXAction action = Dynatrace.enterAction("Tap on Search");



// ...do some work here...



// end a custom action



action.leaveAction();
```

```
// start a custom action



val action = Dynatrace.enterAction("Tap on Search")



// ...do some work here...



// end a custom action



action.leaveAction()
```

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

The maximum duration of a mobile custom action is 9 minutes.

If a custom action takes longer than 9 minutes and is not closed, such an action is discarded and not reported to Dynatrace.

### Create child actions

[Child actions](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.") are similar to parent actions. When the parent action is closed, OneAgent automatically closes all child actions of the parent action.

Generate child actions using the [`Dynatrace.enterAction(String, DTXAction)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#enterAction(java.lang.String,com.dynatrace.android.agent.DTXAction)) method.

Java

Kotlin

```
// start a parent custom action



DTXAction parentAction = Dynatrace.enterAction("Tap on Search");



// ...do some work here...



// start a child action



DTXAction childAction = Dynatrace.enterAction("Tap on Confirm", parentAction);



// ...do some work here...



// end a child action



childAction.leaveAction();



// ...do some work here...



// end a parent custom action



parentAction.leaveAction();
```

```
// start a parent custom action



val parentAction = Dynatrace.enterAction("Tap on Search")



// ...do some work here...



// start a child action



val childAction = Dynatrace.enterAction("Tap on Confirm", parentAction)



// ...do some work here...



// end a child action



childAction.leaveAction()



// ...do some work here...



// end a parent custom action



parentAction.leaveAction()
```

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

There's no limit on the number of child actions attached to a parent action. However, note that you can have only nine levels of child actionsâyou can create one parent action and nine levels of child actions (when child action A is added to a parent action, child action B is added to child action A, child action C is added to child action B, and so on). Also, refer to [User session structure for individual user](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Child actions are not displayed on the [user session details page](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), but you can view them on the [waterfall analysis page](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") for a parent action to which these child actions are attached. Even though the child action nesting is not fully preserved in the waterfall analysis view and all child actions are displayed as child actions of level 1, you can still grasp the action nesting from the timings.

### Cancel custom actions

OneAgent for Android version 8.231+

If you need to cancel an already created but not yet completed custom action, use the [`DTXAction#cancel()`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#cancel()) API call.

Canceling an action discards all data associated with it: all reported values are discarded and all child actions are canceled. Also, note that you cannot cancel a completed action.

Java

Kotlin

```
// create a custom action



DTXAction action = Dynatrace.enterAction("Tap on Purchase");



try {



// ...do some work here...



performWork();



// close the custom action. All associated data is stored and sent to Dynatrace



action.leaveAction();



}



catch(Exception e) {



// cancel the custom action. All associated data is discarded.



action.cancel();



}
```

```
// create a custom action



val action = Dynatrace.enterAction("Tap on Purchase")



try {



// ...do some work here...



performWork()



// close the custom action. All associated data is stored and sent to Dynatrace



action.leaveAction()



} catch (e: Exception) {



// cancel the custom action. All associated data is discarded.



action.cancel()



}
```

### Determine custom action state

OneAgent for Android version 8.231+

Sometimes it's helpful to know whether a custom action is still open and can be used to report data.

To check the state of a custom action, use the [`DTXAction#isFinished()`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#isFinished()) method.

A custom action is finished when the action is:

* Completed via `DTXAction#leaveAction()`, or
* Canceled via `DTXAction#cancel()`, or
* Terminated by OneAgent (for example, when OneAgent shuts down)

Note that you shouldn't interact with a finished custom action.

#### Custom action code sample

The following code snippet shows a sample instrumentation of the fictional method search, which makes a web request to an instrumented server and parses the received result. The following instrumentation actions are part of the code snippet:

1. Creates a custom action
2. Reports a value
3. Reports a error
4. Monitors a web request
5. Creates a child action

Java

Kotlin

```
public boolean search(String query) {



// [1a] start a parent custom action



DTXAction searchAction = Dynatrace.enterAction("Tap on Search");



// [2] report a value



searchAction.reportValue("query", query);



URL url;



try {



url = new URL("https://www.example.com/?query=" + query);



} catch (MalformedURLException e) {



// [3] report an error



searchAction.reportError("invalid url", e);



// [1b] end a parent custom action



searchAction.leaveAction();



return false;



}



// [4.1] Generate a new unique tag associated with the custom action "Tap on Search"



String uniqueRequestTag = searchAction.getRequestTag();



// [4.2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



Request request = new Request.Builder()



.url(url)



// [4.3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4.4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (!response.isSuccessful()) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, response.code(), response.message());



return false;



}



String body = response.body().string();



// [4.5] Stop web request timing when the HTTP response is received and the response body is obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



// [5a] start a child action



DTXAction parseAction = Dynatrace.enterAction("Parse result", searchAction);



parseResult(body);



// [5b] end a child action



parseAction.leaveAction();



return true;



} catch (IOException e) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



return false;



}



finally {



// [1b] end a parent custom action



searchAction.leaveAction();



}



}
```

```
fun search(query: String): Boolean {



// [1a] start a parent custom action



val searchAction = Dynatrace.enterAction("Tap on Search")



// [2] report a value



searchAction.reportValue("query", query)



var url: URL? = null



try {



url = URL("https://www.example.com/?query=$query")



} catch (e: MalformedURLException) {



// [3] report an error



searchAction.reportError("invalid url", e)



// [1b] end a parent custom action



searchAction.leaveAction()



return false



}



// [4.1] Generate a new unique tag associated with the custom action "Tap on Search"



val uniqueRequestTag = searchAction.requestTag



// [4.2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



val request = Request.Builder()



.url(url)



// [4.3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4.4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (!response.isSuccessful) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, response.code, response.message)



return false



}



val body = response.body!!.string()



// [4.5] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



// [5a] start a child action



val parseAction = Dynatrace.enterAction("Parse result", searchAction)



parseResult(body)



// [5b] end a child action



parseAction.leaveAction()



}



return true



} catch (e: IOException) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



return false



} finally {



// [1b] end a parent custom action



searchAction.leaveAction()



}



}
```

## Custom value reporting

Using the OneAgent SDK for Android, you can report events, values, and errors. Reported events, values, and errors that are part of a user action are then displayed in the user action waterfall analysis. Reported errors (both standalone and "attached" to a user action) are also displayed on the user session details page and multidimensional **User action analysis** page.

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Report an event

With `reportEvent`, you can report a specific event. The reported event must be part of a user action.

Java

Kotlin

```
action.reportEvent("event_name");
```

```
action.reportEvent("event_name")
```

### Report a value

The `reportValue` method allows you to report key-value pairs of metadata that you can later view in the Dynatrace web UI and convert into [user action and user session properties](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). The reported values must be part of a user action.

You can report values of the following data types:

* [`int`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,int))
* [`long`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,long))
* [`double`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,double))
* [`string`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,java.lang.String))

Java

Kotlin

```
// report int



action.reportValue("int_value_name", 5);



// report long



action.reportValue("long_value_name", 5L);



// report double



action.reportValue("double_value_name", 5.6);



// report string



action.reportValue("string_value_name", "exampleValue");
```

```
// report int



action.reportValue("int_value_name", 5)



// report long



action.reportValue("long_value_name", 5L)



// report double



action.reportValue("double_value_name", 5.6)



// report string



action.reportValue("string_value_name", "exampleValue")
```

To view the reported values in the Dynatrace web UI, go to the details of the user action that should contain that metadata and scroll down to the **Reported values** section.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

User action details page with SDK-reported values

To add action and session properties based on the reported values and then use these properties to create powerful queries, segmentations, and aggregations, see [Define user action and user session properties for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

### Report an error

The `reportError` method is different from the `reportValue` method in that it's specifically identified as an [error type event](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.").

The OneAgent SDK allows you to report the following:

* **Error codes**. Use the [`reportError(String, int)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,int)) method.
* **Handled exceptions**. Use the [`reportError(String, Throwable)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,java.lang.Throwable)) method.

There are two options for reporting an error. You can report an error as part of a user action or as a standalone error, which is generated as a global event that is not tied to a specific user action.

#### Error within a user action

Java

Kotlin

```
// report an error code



action.reportError("error_code_name", -1);



// report an exception



action.reportError("exception_name", exception);
```

```
// report an error code



action.reportError("error_code_name", -1)



// report an exception



action.reportError("exception_name", exception)
```

#### Standalone error

You can report standalone errors via the `Dynatrace` class.

Java

Kotlin

```
// report an error code



Dynatrace.reportError("error_code_name", -1);



// report an exception



Dynatrace.reportError("exception_name", exception);
```

```
// report an error code



Dynatrace.reportError("error_code_name", -1)



// report an exception



Dynatrace.reportError("exception_name", exception)
```

## Activity lifecycle monitoring

To track lifecycle events, we use the official Android [`ActivityLifecycleCallbacks`ï»¿](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks) interface. For activities, Dynatrace reports the time of each entered lifecycle state until the activity is visible; if available, the timestamps of lifecycle callbacks are displayed in the user action waterfall analysis and are marked as a **Lifecycle event**.

### Reported lifecycle events

With lifecycle monitoring, OneAgent collects data on the following lifecycle events for the [`Activity`ï»¿](https://developer.android.com/reference/android/app/Activity) class.

* **Activity display**: Measures the time required to display an activity.
* **Activity redisplay**: Measures the time required to redisplay a previously created activity. Two options are possible:

  + Option 1: An activity is in the *Stopped* mode and is not visible on the screen, and then it's *Started* and *Resumed* again.
  + Option 2: An activity is in the *Paused* mode and is not fully visible on the screen but partially obfuscated, and then it's *Resumed* again.

The timespan used for measuring the lifecycle event duration depends on the lifecycle event type and the level of Android API. When Android API level 29+ is used, we can measure the duration of lifecycle events more accurately thanks to pre- and post-lifecycle callbacks.

| Lifecycle event | Android API 29+ | Android API 28 and earlier | Reported lifecycle callbacks |
| --- | --- | --- | --- |
| **Activity display** | `onActivityPreCreated` â `onActivityPostResumed` | `onActivityCreated` â `onActivityResumed` | `onCreate` `onStart` `onResume` |
| **Activity redisplay**, option 1 | `onActivityPreStarted` â `onActivityPostResumed` | `onActivityStarted` â `onActivityResumed` | `onStart` `onResume` |
| **Activity redisplay**, option 2 | `onActivityPreResumed` â `onActivityPostResumed` | Not possible to measure the duration | `onResume` |

### Disable lifecycle monitoring

Activity lifecycle monitoring is turned on by default, but you can disable it with the [`withActivityMonitoring`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withActivityMonitoring(boolean)) method.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withActivityMonitoring(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withActivityMonitoring(false)



.buildConfiguration()
```

## Web request monitoring

The [Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.") automatically instruments most web requests. However, you have to manually instrument requests in the following cases:

* When the requests of a third-party framework aren't instrumented
* When you need to [report non-HTTP(S) requests](#monitor-non-http-requests)
* If you've disabled [web request monitoring](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.")

For HTTP(S) requests, never combine automatic and manual web request instrumentation. However, you can use automatic instrumentation for HTTP(S) requests and manual instrumentation for [non-HTTP(S) requests](#monitor-non-http-requests).

To track web requests, add the `x-dynatrace` HTTP header with a unique value to the web request. This is required to correlate the server-side monitoring data to the corresponding mobile web request. Additionally, the timing values from the mobile side must be measured.

To monitor a web request

1. Generate a new unique tag.
2. Generate a `WebRequestTiming` object based on the tag.
3. Place the Dynatrace HTTP header on your web request.
4. Start web request timing before the HTTP request is sent.
5. Stop web request timing.

   * The HTTP response is received, and the response body is obtained.
   * A connection exception occurs.

There are two types of web requests in terms of their hierarchy:

* [Requests attached to a user action](#attach-request-to-action)
* [Standalone requests](#monitor-standalone-request). For these requests, OneAgent automatically tries to find an appropriate user action. If it finds one, the web request is attached to the user action. The web request is only reported as a standalone web request when no appropriate user action is found.

  Currently, you cannot view standalone requests in [**Session Segmentation**](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").

### Attach a web request to a user action

To attach a web request to a user action, generate a unique tag with the [`DTXAction.getRequestTag()`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#getRequestTag()) method.

The following sample shows how to attach a synchronous `OkHttp` web request to the `"Search request"` user action.

Java

Kotlin

```
URL url = new URL("https://www.example.com");



// First, create a custom action



DTXAction webAction = Dynatrace.enterAction("Search request");



// [1] Generate a new unique tag associated with the user action



String uniqueRequestTag = webAction.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



} catch (IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



}



finally {



// Lastly, end the custom action



webAction.leaveAction();



}
```

```
val url = URL("https://www.example.com")



// First, create a custom action



val webAction = Dynatrace.enterAction("Search request")



// [1] Generate a new unique tag associated with the user action



val uniqueRequestTag = webAction.requestTag



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



}



} catch (e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



} finally {



// Lastly, end the custom action



webAction.leaveAction()



}
```

Attach an asynchronous OkHttp web request to a user action

Java

Kotlin

```
final URL url = new URL("https://www.example.com");



// First, create a custom action



final DTXAction webAction = Dynatrace.enterAction("Search request");



// [1] Generate a new unique tag associated with the user action



String uniqueRequestTag = webAction.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



final WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Call startWebRequestTiming to begin the timing, and then handle the response body from the OkHttp call



timing.startWebRequestTiming();



client.newCall(request).enqueue(new Callback() {



@Override



public void onFailure(Call call, IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



// [8] Lastly, end the custom action



webAction.leaveAction();



}



@Override



public void onResponse(Call call, Response response) throws IOException {



try (ResponseBody responseBody = response.body()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



// Lastly, end the custom action



webAction.leaveAction();



}



}



});
```

```
val url = URL("https://www.example.com")



// First, create a custom action



val webAction = Dynatrace.enterAction("Search request")



// [1] Generate a new unique tag associated with the user action



val uniqueRequestTag = webAction.requestTag



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



// [4] Call startWebRequestTiming to begin the timing, and then handle the response body from the OkHttp call



timing.startWebRequestTiming()



client.newCall(request).enqueue(object : Callback {



override fun onFailure(call: Call, e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



// [8] Lastly, end the custom action



webAction.leaveAction()



}



@Throws(IOException::class)



override fun onResponse(call: Call, response: Response) {



response.use {



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



// Lastly, end the custom action



webAction.leaveAction()



}



}



})
```

### Monitor a standalone web request

To monitor a web request as a standalone request, generate a unique tag with the [`Dynatrace.getRequestTag()`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getRequestTag()) method.

The following sample shows how to monitor a synchronous `OkHttp` web request.

Java

Kotlin

```
URL url = new URL("https://www.example.com");



// [1] Generate a new unique tag



String uniqueRequestTag = Dynatrace.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



} catch (IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



}
```

```
val url = URL("https://www.example.com")



// [1] Generate a new unique tag



val uniqueRequestTag = Dynatrace.getRequestTag()



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



}



} catch (e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



}
```

### Monitor non-HTTP(S) requests

OneAgent for Android version 8.249+

Monitoring of WebSocket connections is available starting with OneAgent for Android version 8.239. Monitoring of all non-HTTP(S) requests is available starting with OneAgent for Android version 8.249.

OneAgent for Android does not support auto-instrumentation of non-HTTP(S) requests. If you need to report requests such as a WebSocket request (starts with `ws://` or `wss://`), check the code samples below.

* Use the [`stopWebRequestTiming(URI requestUri, int respCode, String respPhrase)`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/WebRequestTiming.html#stopWebRequestTiming(java.net.URI,int,java.lang.String)) API method to manually instrument non-HTTP(S) requests.
* Make sure to pass along the original URI. Do not retrieve the URI from the `OkHttp` object because this doesn't return the original URI.
* This approach is only suitable for WebSocket connections that are open for up to about 9 minutes. Longer connections may not be reported.
* If you only have non-HTTP(S) requests, you can optionally [disable web request monitoring](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.").
* If you have both HTTP(S) and non-HTTP(S) requests, and HTTP(S) requests are auto-instrumented, don't disable web request monitoring.

Java

Kotlin

```
final URI uri = URI.create("wss://websocket.example.com");



// First, create a custom action



DTXAction webSocketAction = Dynatrace.enterAction("WebSocket");



// Generate a WebRequestTiming object based on the unique request tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(webSocketAction.getRequestTag());



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(uri.toString())



.build();



// Start web request timing when you are about to open a WebSocket connection



timing.startWebRequestTiming();



WebSocket webSocket = client.newWebSocket(request, new WebSocketListener() {



@Override



public void onClosing(@NonNull WebSocket webSocket, int code, @NonNull String reason) {



// Stop web request timing when the webSocket connection closes



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



timing.stopWebRequestTiming(uri, code, reason);



// end the action



webSocketAction.leaveAction();



}



@Override



public void onFailure(@NonNull WebSocket webSocket, @NonNull Throwable t, @Nullable Response response) {



// Stop web request timing when the webSocket connection fails and customize the return code and message



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



timing.stopWebRequestTiming(uri, 1011, "ERROR");



// end the action



webSocketAction.leaveAction();



}



});
```

```
val uri = URI.create("wss://websocket.example.com")



// First, create a custom action



val webSocketAction = Dynatrace.enterAction("WebSocket")



// Generate a WebRequestTiming object based on the unique request tag



val webRequestTiming = Dynatrace.getWebRequestTiming(webSocketAction.requestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(uri.toString())



.build()



// Start web request timing when you are about to open a WebSocket connection



webRequestTiming.startWebRequestTiming()



val webSocket = client.newWebSocket(request, object : WebSocketListener() {



override fun onClosing(webSocket: WebSocket, code: Int, reason: String) {



// Stop web request timing when the webSocket connection closes



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



webRequestTiming.stopWebRequestTiming(uri, code, reason)



// end the action



webSocketAction.leaveAction()



}



override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {



// Stop web request timing when the webSocket connection fails



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



webRequestTiming.stopWebRequestTiming(uri, 1011, "ERROR")



// end the action



webSocketAction.leaveAction()



}



})
```

## Crash reporting

OneAgent captures all [uncaught exceptionsï»¿](https://dt-url.net/UncaughtExceptionHandler). The [crash](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") report includes the occurrence time and the full stack trace of the exception.

In general, the crash details are sent immediately after the crash, so the user doesnât have to relaunch the application. However, in some cases, the application should be reopened within 10 minutes so that the crash report is sent. Note that Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

You can deactivate crash reporting using the [`withCrashReporting`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCrashReporting(boolean)) method.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCrashReporting(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCrashReporting(false)



.buildConfiguration()
```

## Tag specific users

You can tag each user of your mobile apps with a unique user name. This enables you to search and filter specific user sessions and analyze individual user behavior over time. For more details, see [User tagging](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

The following steps explain how to tag an individual user via the Dynatrace API.

Java

Kotlin

```
Dynatrace.identifyUser("john.doe@example.com");
```

```
Dynatrace.identifyUser("john.doe@example.com")
```

OneAgent for Android version 237+ Sessions split due to idle or duration timeout are re-tagged automatically.

When OneAgent ends a tagged session because the session duration has reached its set limit or due to the user's inactivity, the subsequent session is re-tagged automatically. You don't need to provide the user identification information again.

However, note that OneAgent does not re-tag the subsequent session in the following cases:

* When you explicitly end a tagged user session via [`endVisit`](#end-session)
* When the user or the mobile operating system closes or force stops the app
* When OneAgent ends the current user session and generates a new session after the privacy settings have been changed

See [User sessions > Session end](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") to learn when OneAgent ends a mobile user session.

When the [user opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") is enabled for your application, it might affect user tagging and reporting of custom events, user actions, values, and errors. The exact data types not reported to Dynatrace depend on the data collection level set by a particular user. For details, refer to [Data collection levels](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## End a session

You can force a session to end via the Dynatrace API. This also closes all open actions and starts a new session.

Java

Kotlin

```
Dynatrace.endVisit();
```

```
Dynatrace.endVisit()
```

## Configure data privacy (opt-in mode)

With user opt-in mode, each user of your application can set their data privacy preferences and decide whether they want or don't want to share their information. When the opt-in mode is enabled, you need to ask each user for permission to capture their data; then, you store their data privacy preferences. For details, see [User opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Enable user opt-in mode

To activate the user opt-in mode, enable the `userOptIn` flag via the DSL from the Dynatrace Android Gradle plugin or use the `ConfigurationBuilder.withUserOptIn` method.

### Change user's data privacy preferences

With the [`Dynatrace.applyUserPrivacyOptions`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#applyUserPrivacyOptions(com.dynatrace.android.agent.conf.UserPrivacyOptions)) method, you can adjust the data privacy preferences based on the decision of a particular user.

Java

Kotlin

```
Dynatrace.applyUserPrivacyOptions(UserPrivacyOptions.builder()



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingOptedIn(true)



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



.withCrashReplayOptedIn(true)



.build()



);
```

```
Dynatrace.applyUserPrivacyOptions(UserPrivacyOptions.builder()



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingOptedIn(true)



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



.withCrashReplayOptedIn(true)



.build()



)
```

The possible values for the [data collection level](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") are as follows:

* `OFF`
* `PERFORMANCE`
* `USER_BEHAVIOR`

OneAgent persists the data privacy preferences and automatically applies them when the application is restarted. Additionally, OneAgent generates a new session whenever the data privacy preferences are changed.

### Retrieve user's data privacy preferences

You can also retrieve the data privacy preferences of a particular user with the [`Dynatrace.getUserPrivacyOptions`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getUserPrivacyOptions()) method. Use this method only after OneAgent starts.

## Configure hybrid applications

For hybrid applications, the native mobile app is monitored via OneAgent, while the browser part is observed by the [Dynatrace RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API."). For this reason, hybrid application monitoring requires some additional configuration. See [Instrument hybrid apps](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") for more information.

### Enable hybrid application monitoring

To activate the hybrid application monitoring feature, use the [`withHybridMonitoring`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withHybridMonitoring(boolean)) method.

### Specify domains, hostnames, and IP addresses

For hybrid applications that use the RUM JavaScript inside `WebView`, OneAgent must set cookies for each instrumented domain or server that your application communicates with. When the hybrid application monitoring feature is enabled, OneAgent generates these cookies for every specified domain and stores them in `CookieManager`. Dynatrace uses these cookies to identify mobile and web sessions within your application and merge these sessions into the same "hybrid" session.

To specify your domains, hostnames, and IP addresses, use either the [`withMonitoredDomains`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredDomains(java.lang.String...)) or the [`withMonitoredHttpsDomains`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredHttpsDomains(java.lang.String...)) method. Start domains and sub-domains with a period (`.`).

#### `withMonitoredDomains` method

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredDomains(".<domain1>", ".<domain2>")



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredDomains(".<domain1>", ".<domain2>")



.buildConfiguration()
```

#### `withMonitoredHttpsDomains` method

OneAgent for Android version 8.237+

If you use the `withMonitoredHttpsDomains` method, the `Secure` cookie attribute is added for all cookies that Dynatrace sets. This ensures that the browser sends these cookies only over secure connections.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredHttpsDomains("https://.<domain1>", "https://.<domain2>")



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredHttpsDomains("https://.<domain1>", "https://.<domain2>")



.buildConfiguration()
```

### Instrument `WebView`

To enable communication between the RUM JavaScript and OneAgent for Android, instrument all `WebView` objects before the URL is loaded with [`WebView.loadUrl(String)`ï»¿](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)). Instrument the [`Dynatrace.instrumentWebView`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#instrumentWebView(android.webkit.WebView)) method for every `WebView` that contains the RUM JavaScript. Without this, the monitoring data received from `WebView` will not be associated with the same mobile session.

Java

Kotlin

```
WebView myWebView = (WebView) findViewById(R.id.webview);



Dynatrace.instrumentWebView(myWebView);



myWebView.loadUrl("http://www.example.com");
```

```
val myWebView: WebView = findViewById(R.id.webview)



Dynatrace.instrumentWebView(myWebView)



myWebView.loadUrl("http://www.example.com")
```

### Disable cookies for file domains

OneAgent for Android version 8.271+

To set cookies for file domains (starting with `file://`), Dynatrace uses [`setAcceptFileSchemeCookies`ï»¿](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). However, this API is no longer recommended because of security issues; we plan to stop adding cookies to file scheme domains in a couple of months.

If you want to secure your application right now, set `fileDomainCookies` to `false`, and Dynatrace won't add cookies to file scheme domains.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.fileDomainCookies(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.fileDomainCookies(false)



.buildConfiguration()
```

### Preserve Dynatrace cookies

For hybrid applications, it's important to ensure that the Dynatrace cookies are not deleted. Without these cookies, Dynatrace can't combine the monitoring data received from the RUM JavaScript and OneAgent into a single session.

When you delete cookies via [`CookieManager#removeAllCookies(ValueCallback)`ï»¿](https://developer.android.com/reference/android/webkit/CookieManager#removeAllCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) or [`CookieManager#removeSessionCookies(ValueCallback)`ï»¿](https://developer.android.com/reference/android/webkit/CookieManager#removeSessionCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)), you should also call the [`restoreCookies`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#restoreCookies()) method to restore the Dynatrace cookies.

Java

Kotlin

```
CookieManager.getInstance().removeAllCookies(null);



Dynatrace.restoreCookies();
```

```
CookieManager.getInstance().removeAllCookies(null)



Dynatrace.restoreCookies()
```

## Enable load balancing

OneAgent allows you to enable client-side load balancing that helps avoid unbalanced load on the server when multiple OneAgents simultaneously establish a connection to ActiveGate.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withStartupLoadBalancing(true)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withStartupLoadBalancing(true)



.buildConfiguration()
```