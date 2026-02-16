---
title: Configure Session Replay for Android
source: https://www.dynatrace.com/docs/observe/digital-experience/session-replay/session-replay-android
scraped: 2026-02-16T21:29:46.713832
---

# Configure Session Replay for Android

# Configure Session Replay for Android

* How-to guide
* 7-min read
* Updated on Oct 07, 2025

This page describes how to enable and customize Session Replay for your Android apps.

## Full Session Replay

[Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") on Android enables you to capture your customers' interactions with your mobile application and replay each tap, swipe, screen rotation in a movie-like experience.

## Session Replay on crashes

Additionally, you can use it to get additional context for crash analysis in the form of video-like screen recordings that replay the user actions preceding a detected [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.")

## Prerequisites

Make sure that your system meets the following requirements:

* Dynatrace version 1.303
* OneAgent for Android version 8.303
* Real User Monitoring enabled for your application
* Active Dynatrace Digital Experience Monitoring license
* The web UI URL has a trusted certificate

## Supported technologies and known limitations

* Android 5.0+ (API level 21+) is supported.
* Android Gradle plugin 7.0+ is supported.
* Kotlin version 1.9+ is supported.

  + Kotlin version 1.8 supported because of Kotlin compatibility
* Jetpack Compose version 1.4+ is supported starting with OneAgent for Android version 8.325.
* Session Replay is not available for cross-platform frameworks such as Cordova, React Native, Flutter, Xamarin, and more
* For a hybrid app, Session Replay is supported only for the native part of the app. Session Replay is not supported for the browser part of a hybrid app.
* Only AndroidX support libraries are supported. Classes such as Activity or Fragment in com.android.support are not supported.
* We recommend not using other crash reporting tools together with Dynatrace Session Replay.
* Session Replay can capture only certain events. However, if you need to track a specific view or event that is not supported by default, you can [capture a custom event](/docs/observe/digital-experience/session-replay/session-replay-android#capture-custom-events "Set up Session Replay for your Android apps to learn which actions your users perform.").
* You can play back the user sessions recorded with Session Replay only in [certain browsers](/docs/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Find out which browsers Dynatrace applications can run on.").
* See [Technical restrictions for Session Replay for web applications](/docs/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay.") for more information.

Session Replay is a video-like reconstruction of the user interaction with mobile application, that uses captured events and data. Because of this approach replayed session can differ from the actual user experience. Known issues

* Fragments with in-out animations can cause problems, especially when animations are short.
* Floating action buttons can cause data masking issues.
* The inputType attribute within the Button component might result in buttons appearing without text when captured.

## Enable Session Replay on Android

If you haven't done so already, complete all steps described in the instrumentation wizard.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **General** > **Enablement and cost control**.
5. Turn on **Enable Full Session Replay** or **Enable Session Replay on crashes**. You have the following options:

   * Enabling Full Mobile Session Replay on 100%, all sessions will be captured
   * Enabling Full Mobile Session Replay on lower than 100%, randomly selected session will be captured
   * Enabling Session Replay on Crashes means guarantees that, regardless of the Enable Full Session Replay setting and its const and traffic control value, all sessions with crash are will be captured.
6. From the application settings, select **Instrumentation wizard**, and then select **Android** or **iOS**.
7. Follow the steps in the instrumentation wizard.

For Android Gradle plugin versions 4.0 and 4.1, you need to change the compile option to Java 8. This can be done during the instrumentation wizard step called **Apply the Dynatrace plugin and add the plugin configuration**. Add the following code to the top-level build file:

```
compileOptions {



sourceCompatibility 1.8



targetCompatibility 1.8



}
```

For Android Gradle plugin 4.2+, Java 8 is used by default, so no configuration change is needed.

## Mask sensitive data

### Data masking levels

Session Replay on comes with three predefined masking levels:

* **Safest**âall the editable text fields, images, labels, web views, and switches are masked.
* **Safe**âall the editable text fields are masked.
* **Custom**âby default, masks the same elements as **Safest**, but you can decide exactly which application components or views should be masked. See [Configure custom masking](#custom-masking) for details.

### Change masking level

By default, OneAgent applies the **Safest** masking level. To change it to the **Safe** or **Custom** level, use the API to configure OneAgent. If you've opted for the **Custom** level, see [Configure custom masking](#custom-masking) for details on how to set which application components or views should be masked.

#### Example 1: Change masking level to Safe

Use the following code to set the masking level to Safe.

```
MaskingConfiguration config = new MaskingConfiguration.Safe();



// .Safest or .Custom



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Example 2: Change masking level to Custom

Use the following code to set the masking level to Custom. For additional options, see [Configure custom masking](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom();



// .Safest or .Safe



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

#### Example 3: Change masking level to Custom and remove all masked views

Use the following code to set the masking level to Custom and remove all masked views (removeAllMaskedViews). For additional options, see [Configure custom masking](#custom-masking).

```
MaskingConfiguration config = new MaskingConfiguration.Custom().removeAllMaskedViews();



DynatraceSessionReplay.setConfiguration(Configuration.builder()



.withMaskingConfiguration(config)



.build());
```

### Configure custom masking

If you set the [data masking level](#masking-levels) to **Custom**, you can use additional API methods to decide which application components or views should be masked. You can:

* [Mask views](#mask-views).
* [Mask views using android:tag](#mask-views-android-tag).
* [Mask views using a masking tag](#mask-views-masking-tag).
* [Mask Jetpack Compose composables](#mask-jc-composables).

#### Mask views

You can enable or disable masking globally or for the selected components, such as text fields, images, labels, web views, and switches.

```
Set&lt;Class<? extends View&gt;> set = new HashSet&lt;Class<? extends View&gt;>()\\{{



add(ImageView.class);



add(WebView.class);



}};



new MaskingConfiguration.Custom().addMaskedView(ImageView.class); // Adds one masked view



new MaskingConfiguration.Custom().addMaskedViews(set); // Adds all masked views



new MaskingConfiguration.Custom().removeMaskedView(ImageView.class); // Removes one masked view



new MaskingConfiguration.Custom().removeAllMaskedViews(); // Removes all masked views
```

You need to apply the custom masking configuration for it to take effect. See [Change masking level to Custom and remove all masked views](#change-masking-level-custom-remove-all-masked-views) for the example code snippet.

#### Mask views using `android:tag`

You can also enable or disable masking of the selected views based on their `android:tag`.

```
Set&lt;Integer&gt; set = new HashSet&lt;Integer&gt;()\\{{



add(R.id.view_id1);



add(R.id.view_id2);



}};



new MaskingConfiguration.Custom().addMaskedIds(set);



new MaskingConfiguration.Custom().addNonMaskedIds(set);



new MaskingConfiguration.Custom().removeMaskedIds(set);



new MaskingConfiguration.Custom().removeNonMaskedIds(set);
```

You need to apply the custom masking configuration for it to take effect. See [Change masking level to Custom and remove all masked views](#change-masking-level-custom-remove-all-masked-views) for the example code snippet.

#### Mask views using a masking tag

You can also mask a view by adding the `data-dtrum-mask` masking tag to the view's `android:tag`. A view with this masking tag is always masked.

#### Mask Jetpack Compose composables

Jetpack Compose provides manual masking functionality that allows you to control which composables are masked in Session Replay. To mask a composable, use the `dynatraceSessionReplayMasked` modifier.

```
import com.dynatrace.android.api.dynatraceSessionReplayMasked



@Composable



fun MyScreen() {



Column {



Text(



text = "This text will be masked",



modifier = Modifier.dynatraceSessionReplayMasked()



)



}



}
```

## Enable Session Replay logs

You can enable Session Replay logs the same way as for OneAgent. See [Enable debug logging for Dynatrace Android Gradle plugin or OneAgent SDK](/docs/observe/digital-experience/mobile-applications/instrument-android-app/debug-logging-oneagent "Activate the debug logs from OneAgent.") for more information.

## Capture custom events

Session Replay records only certain events. However, you can track an event that is not supported by default.

```
DynatraceSessionReplay.trackCustomEvent("User logged")
```

## Change transmission mode to Wi-Fi for images

By default, all dataâinformation on captured events and imagesâis sent over any connection. However, you can opt to transfer images only when the users are connected to Wi-Fi to save their mobile data.

```
DynatraceSessionReplay.setConfiguration(



Configuration.builder()



.withDataTransmissionMode(DataTransmissionMode.NOT_METERED_NETWORK)



.build()



)
```

## Troubleshooting

* [User sessions are not recorded at allï»¿](https://dt-url.net/cp2385m)
* [User sessions are recorded, but Session Replay is not availableï»¿](https://dt-url.net/4m038d9)

## Related topics

* [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [View crash reports for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")