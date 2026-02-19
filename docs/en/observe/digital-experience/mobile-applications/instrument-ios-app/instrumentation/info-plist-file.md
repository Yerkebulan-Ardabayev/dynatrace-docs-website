---
title: Info.plist file
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file
scraped: 2026-02-19T21:24:20.073153
---

# Info.plist file

# Info.plist file

* Explanation
* 2-min read
* Updated on Apr 26, 2024

When you use Dynatrace, the `Info.plist` file stores your app identification and configuration keys. Below is some information on this file.

* The `Info.plist` file is available in the Xcode project navigator under **Supporting Files**. For older project files, `Info.plist` is located under **Resources**.
* Regardless of the selected approach to setting up RUM for your app, add your app identification keys (app ID and beacon URL) to your project's `Info.plist` file; the [`DTXApplicationID` and `DTXBeaconURL` keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") are always required. Without the app identification keys, your mobile app won't be able to send monitoring data to Dynatrace.

  To check your app identification keys, access the [mobile instrumentation wizard](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
* You can also use `Info.plist` to enable or disable additional monitoring features by adding [configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to this file.
* To keep your app's `Info.plist` file clean, you can move all OneAgent-related `DTX` keys to a `Dynatrace.plist` file and add `Dynatrace.plist` to the `Copy Bundle Resources` build phase. The `Dynatrace.plist` file must be located at the root of your resources bundle, so create this file in the same location as the `Info.plist` file.
* In some instances, no `Info.plist` file is generated when you use Xcode. For example, when you create a new SwiftUI project, you might notice the project doesn't have this file. See [Xcode Release Notes; issue 68254857ï»¿](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-release-notes#Templates) for more details.

  If you don't have the `Info.plist` file, add your app identification keys and [configuration keys](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") manually as **Custom iOS Target Properties** to the **Info** tab of your application target. Once you make that change, Xcode adds the `Info.plist` file to the project, but it's still better to update the configuration via the **Info** tab of your application target.