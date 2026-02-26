---
title: Configure Session Replay for iOS
source: https://www.dynatrace.com/docs/observe/digital-experience/session-replay/session-replay-ios
scraped: 2026-02-26T21:26:18.045817
---

# Configure Session Replay for iOS

# Configure Session Replay for iOS

* How-to guide
* 8-min read
* Updated on Sep 25, 2025

This page describes how to enable and customize Session Replay for your iOS apps.

OneAgent for iOS version 8.323 or later is required for applications compiled with Xcode 26.

## Full Session Replay

[Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") on iOS enables you to capture your customers' interactions with your mobile and replay each tap, swipe, screen rotation in a movie-like experience.

## Session Replay on crashes

Additionally, you can use it to get more context for crash analysis in the form of video-like screen recordings that replay the user actions preceding a detected [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.").

## Prerequisites

Make sure that your system meets the following requirements:

* Dynatrace version 1.303
* OneAgent for iOS version 8.323
* Real User Monitoring enabled for your application
* Active Dynatrace Digital Experience Monitoring license
* The web UI URL has a trusted certificate

## Known limitations and issues

### Technical limitations

* iOS 12.0+ is supported.
* Swift 5+
* Xcode 15+
* SwiftUI is supported.
* Session Replay is not available for tvOS and iPadOS.
* Session Replay is not available for cross-platform frameworks such as Cordova, React Native, Flutter, Xamarin, and similar.
* For a hybrid app, Session Replay is supported only for the native part of the app. For the browser part, Session Replay only supports webpage load events.
* We recommend not using other crash reporting tools together with Dynatrace Session Replay.
* Session Replay can capture only certain events. However, if you need to track a specific view or event that is not supported by default, you can [capture a custom event](#capture-custom-events).
* You can only play back the user sessions recorded with Session Replay in [certain browsers](/docs/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements#session-replay "Find out which browsers Dynatrace applications can run on.").
* For iOS 26 applications generated with Xcode 26, masking functionality is only available with OneAgent for iOS version 8.323+.

See [Technical restrictions for Session Replay for web applications](/docs/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay.") for more information.

Session Replay is a video-like reconstruction of the user interactions with mobile applications that use captured events and data. Because of this approach, replayed sessions can differ from the actual user experience. Known issues

## Enable Session Replay on iOS

If you haven't done so already, complete all steps described in the instrumentation wizard.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name
4. From the application settings, select **General** > **Enablement and cost control**.
5. Turn on **Enable Full Session Replay** and/or **Enable Session Replay on crashes**. You have the following options:

   * Enabling Full Mobile Session Replay on 100%, all sessions will be captured
   * Enabling Full Mobile Session Replay on less than 100%, randomly selected session will be captured
   * Enabling Session Replay on Crashes guarantees that, regardless of the Enable Full Session Replay setting and its const and traffic control value, all sessions with crash will be captured
6. From the application settings, select **Instrumentation wizard**, and then select **Android** or **iOS**.
7. Follow the steps in the instrumentation wizard.

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
let maskingConfiguration = MaskingConfiguration(maskingLevelType: .safe)



try? AgentManager.setMaskingConfiguration(maskingConfiguration)
```

### Configure custom masking

If you set the [data masking level](#data-masking-levels) to **Custom**, you can use additional API methods to decide which application components or views should be masked. You can:

* [Enable or disable masking rules](#enable-disable-masking-rules).
* [Mask views using accessibilityIdentifier](#mask-views-accessibilityIdentifier).
* [Mask views using a masking tag](#mask-views-masking-tag).

#### Enable or disable masking rules

You can enable or disable rules globally or for the selected components, such as text fields, images, labels, web views, and switches.

```
try? maskingConfiguration.add(rule: .maskAllImages) // Adds one rule



try? maskingConfiguration.remove(rule: .maskAllSwitches) // Removes one rule



try? maskingConfiguration.addAllRules() // Adds all rules



try? maskingConfiguration.removeAllRules() // Removes all rules
```

If you remove all masking rules, Session Replay won't mask anything. If you enable all masking rules, it's equivalent to the Safest masking level.

#### Mask views using accessibilityIdentifier

You can enable or disable masking of the selected views based on their accessibilityIdentifier.

```
try? maskingConfiguration.addMaskedView(viewIds: \["masked_view_id"\])



try? maskingConfiguration.removeMaskedView(viewIds: \["masked_view_id"\])



try? maskingConfiguration.addNonMaskedView(viewIds: \["nonMasked_view_id"\])



try? maskingConfiguration.removeNonMaskedView(viewIds: \["nonMasked_view_id"\])
```

#### Mask views using a masking tag

You can also mask a view by adding the data-dtrum-mask masking tag to the view's accessibilityIdentifier. A view with this masking tag is always masked.

## Enable Session Replay logs

You can enable Session Replay logs the same way as for OneAgent. See [OneAgent for iOS debug logging](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.") for more information

## Capture custom events

Session Replay records only certain events. You can additionally capture custom events that are not supported by default. You can capture a custom event with an included screenshot of a specific view, specific screen region, or full screen

All methods for capturing custom events can throw a TrackCustomEventError.notInMainThread error if you try to capture a custom event from a thread that is not the main thread. We suggest that you include a do-catch clause until everything works properly; then you can replace the clause with a simpler version that, even in case of an error, just doesn't capture the custom event

```
do {



try AgentManager.trackCustomEvent(name: "my_event_name", view: nil)



} catch {



print(error)



}
```

### Specific view

Capture a custom event with a screenshot of the specific view

```
try? AgentManager.trackCustomEvent(name: "my_view_name", view: myView)
```

### Specific screen region

Capture a custom event with a screenshot of the specific screen region

```
try? AgentManager.trackCustomEvent(name: "my_view_name", frame: anyFrame)
```

### Full screen

Capture a custom event with a screenshot of the full screen

```
try? AgentManager.trackCustomEvent(name: "my_view_name")
```

## Change transmission mode to Wi-Fi for images

By default, all dataâinformation on captured events and imagesâis sent over any connection. However, you can opt to transfer images only when the users are connected to Wi-Fi to save their mobile data

```
AgentManager.setTransmissionMode(.wifi) // .data by default
```

## Screenshot debugger

The Session Replay screenshot debugger allows you to see when the screenshots are taken, which parts of the screen are captured, and what dataâtext fields, images, labels, web views, and togglesâis masked

You can use the Session Replay screenshot debugger when running your mobile app in the simulator, so you don't have to wait until the session is closed and uploaded to Dynatrace.

![Screenshot debugger](https://dt-cdn.net/images/session-replay-screenshot-debugger-25-62c2c0bcf4.gif)

After you enable the Session Replay screenshot debugger, you can see the corresponding keys in your project. Note that these keys are not sent to the app code for release or archive compilations, so they are never included in the production code. These keys are used only for debug runs.

![Screenshot debugger](https://dt-cdn.net/images/xcode-936-179db4b123.webp)

To enable the Session Replay screenshot debugger:

1. In Xcode, select **Edit Scheme** from the Scheme menu to change your application scheme
2. From your application scheme settings, select the **Run** action, and then switch to the **Arguments** tab
3. Under Environment Variables, add one or both of the following keys

   * **DTXDebugMasking**. This key shows screenshots taken by Session Replay, including masked content and UI controls. For each captured screenshot, you see a brief flash
   * **DTXDebugFrameHighlight**. This key highlights the captured part of the screen with a red frame so that you can know exactly what part of the screen is captured

## Troubleshooting

* [User sessions are not recorded at allï»¿](https://dt-url.net/yw438pl)
* [User sessions are recorded, but Session Replay is not availableï»¿](https://dt-url.net/74638c2)

## Related topics

* [Session Replay](/docs/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [View crash reports for mobile applications](/docs/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Check the latest crash reports for your mobile applications.")