---
title: Set up OneAgent for your iOS apps in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios
---

# Set up OneAgent for your iOS apps in RUM Classic

# Set up OneAgent for your iOS apps in RUM Classic

* How-to guide
* 8-min read
* Updated on Jan 19, 2026

iOS tvOS

To monitor your mobile app with Dynatrace, you need to create an application in Dynatrace and set up OneAgent for your mobile app.

After that, you might also want to [instrument your app's SwiftUI controls](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps."), fine-tune the [auto-instrumentation features](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features "Explore the list of features that are available after you instrument your application with OneAgent.") via [configuration keys](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps."), or capture additional details via [manual instrumentation](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.").

## Create an app in Dynatrace

To create a mobile application in Dynatrace

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.

## Set up OneAgent

Use [CocoaPods](#cocoapods) or [Swift Package Manager](#swift-pm) to set up Real User Monitoring for your app. You can also follow the [manual approach](#manual), though it's better to use one of the automated approaches.

You can set up OneAgent as a dynamic XCFramework, static XCFramework (available for OneAgent for iOS version 8.237+), traditional framework, or static library.

You can't combine the static Dynatrace XCFramework and the dynamic Session Replay XCFramework. For [Session Replay](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps."), both XCFrameworks have to be dynamic.

If you use the static XCFramework, the traditional framework, or the static library to instrument your iOS app, you'll need to perform some additional steps.

### Set up OneAgent with CocoaPods

1. Add Dynatrace OneAgent as a dependency within the CocoaPods `Podfile` specification. You can do this by setting up OneAgent as a dynamic XCFramework, static XCFramework, traditional framework, or static library.

   Dynamic XCFramework

   Static XCFramework

   Traditional framework

   Static library

   To set up Dynatrace as a dynamic XCFramework, add only **one** pod to your `Podfile`.

   * `Dynatrace` pod to add only OneAgent
   * `Dynatrace/SessionReplay` pod to add both OneAgent and the [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.") module

   Ensure that you uncomment the `use_frameworks!` line.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pod for DemoApp to add only OneAgent



   pod 'Dynatrace', '~> 8.279'



   # Pod for DemoApp to add both OneAgent and Session Replay



   # pod 'Dynatrace/SessionReplay', '~> 8.279'



   end
   ```

   To set up Dynatrace as a static XCFramework, add the `Dynatrace/xcframeworkStatic` pod to your `Podfile`. Ensure that you uncomment the `use_frameworks!` line.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/xcframeworkStatic', '~> 8.279'



   end
   ```

   To set up Dynatrace as a traditional framework, add the `Dynatrace/framework` pod to your `Podfile`. Ensure that you uncomment the `use_frameworks!` line.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/framework', '~> 8.279'



   end
   ```

   To set up Dynatrace as a static library, add the `Dynatrace/lib` pod to your `Podfile`. Ensure that you comment out the `use_frameworks!` line.

   ```
   # Uncomment this line to define a global platform for your project



   # platform :ios, '9.0'



   target 'DemoApp' do



   # Uncomment this line if you're using Swift or want to use dynamic frameworks



   # use_frameworks!



   # Pods for DemoApp



   pod 'Dynatrace/lib', '~> 8.279'



   end
   ```

   The traditional framework and the static library were deprecated as they don't support ARM64 Simulator architecture. This architecture is required to build apps on Mac computers with Apple silicon.
2. Add your application's identification keys to the [`Info.plist` file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."). Check the [instrumentation wizard](#instrumentation-wizard) in Dynatrace for the exact values.
3. Trigger your project build once before using OneAgent SDK or any import declarations in Xcode.

CocoaPods automatically adds OneAgent to your iOS project during the build process.

For more information on Podfiles, see [Podfile Syntax Reference﻿](https://guides.cocoapods.org/syntax/podfile.html#podfile).

Beginning December 2026, the CocoaPods Specs repository will be set to read-only.

After this change, Dynatrace will no longer be able to publish new versions of the OneAgent SDK for iOS to CocoaPods, including hotfixes and critical updates.
To continue receiving updates, please migrate to [Swift Package Manager](#swift-pm).

For timeline details, see the official [CocoaPods blog﻿](https://blog.cocoapods.org/CocoaPods-Specs-Repo/).

### Set up OneAgent with Swift Package Manager

1. In Xcode, select **File** > **Swift Packages** > **Add Package Dependency**.
2. Add `https://github.com/Dynatrace/swift-mobile-sdk.git` as the package repository URL.
3. Select only **one** package product:

   * `Dynatrace` to add only OneAgent
   * `DynatraceSessionReplay` to add both OneAgent and the [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.") module

     Do not select `DynatraceSessionReplay` for tvOS, as Session Replay is not available for this operating system.
   * `Dynatrace-Static` to add only OneAgent as a static XCFramework
4. Perform additional steps depending on the framework you use.
   Static XCFramework: Add a linker flag

   1. In Xcode, go to the **Build Settings** tab of your application target.
   2. Expand **Linking**.
   3. Add the `-ObjC` linker flag to **Other Linker Flags**.

   Static XCFramework: Make Dynatrace available to Swift code

   You can skip this step if your application doesn't have Swift code or doesn't need access to the Dynatrace framework.

   We assume that you already created the Objective-C bridging header file for your Swift code in Xcode.

   1. Make sure you set the bridging header file in your application target build settings.
   2. Add the following import line to the bridging header file:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Static library: Add a linker flag

   1. In Xcode, go to the **Build Settings** tab of your application target.
   2. Expand **Linking**.
   3. Add the `-ObjC` linker flag to **Other Linker Flags**.

   Static library: Make Dynatrace available to Swift code

   You can skip this step if your application doesn't have Swift code or doesn't need access to the Dynatrace library.

   We assume that you already created the Objective-C bridging header file for your Swift code in Xcode.

   1. Make sure you set the bridging header file in your application target build settings.
   2. Add the following import line to the bridging header file:

      ```
      #import Dynatrace.h
      ```
5. Add your application's identification keys to the [`Info.plist` file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."). Check the [instrumentation wizard](#instrumentation-wizard) in Dynatrace for the exact values.
6. Trigger your project build once before using OneAgent SDK or any import declarations in Xcode.

To update the package version rule, double-click the product entry in the **Swift Packages** tab within the Xcode project settings. To change the product selection, remove the package and add it again.

To update the package, select **File** > **Swift Packages** > **Update to Latest Package Versions** in Xcode.

When switching from [Carthage](#carthage) to Swift Package Manager, remove the script that you previously added in Xcode to remove iOS Simulator architecture from the release binary. Otherwise, you might have issues when building your project in Xcode 15+.

### Set up OneAgent manually

1. Access the [mobile instrumentation wizard](#instrumentation-wizard).
2. Select **iOS**, and then go to the **Developer** tab.
3. Follow the provided instructions.

   Add `Dynatrace.xcframework` to have only OneAgent.  
   Add both `Dynatrace.xcframework` and `DynatraceSessionReplay.xcframework` to have both OneAgent and the [Session Replay on crashes](/managed/observe/digital-experience/session-replay/session-replay-ios "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.") module.

   Do not add `DynatraceSessionReplay.xcframework` for tvOS, as Session Replay is not available for this operating system.
4. Perform some additional steps depending on the framework you use.

   Static XCFramework: Add a linker flag

   1. In Xcode, go to the **Build Settings** tab of your application target.
   2. Expand **Linking**.
   3. Add the `-ObjC` linker flag to **Other Linker Flags**.

   Static XCFramework: Add a linked library

   1. In Xcode, go to the **General** tab of your application target.
   2. Expand **Frameworks, Libraries, and Embedded Content**.
   3. Add the `libc++.tbd` library.

   You might need to add this library twice. In our internal tests, the library was linked to the project tree only after we added the library a second time.

   Static XCFramework: Make Dynatrace available to Swift code

   You can skip this step if your application doesn't have Swift code or doesn't need access to the Dynatrace framework.

   We assume that you already created the Objective-C bridging header file for your Swift code in Xcode.

   1. Make sure you set the bridging header file in your application target build settings.
   2. Add the following import line to the bridging header file:

      ```
      #import <DynatraceStatic/Dynatrace.h>
      ```

   Traditional framework: Remove iOS Simulator architecture of the release binary

   1. In Xcode, add a **Run Script** phase as the last **Build Phase** of your application target.
   2. Add the following script:

      ```
      APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"



      find "$APP_PATH" -name '*.framework' -type d | while read -r FRAMEWORK



      do



      FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)



      FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"



      EXTRACTED_ARCHS=()



      for ARCH in $ARCHS



      do



      lipo -extract "$ARCH" "$FRAMEWORK_EXECUTABLE_PATH" -o "$FRAMEWORK_EXECUTABLE_PATH-$ARCH"



      EXTRACTED_ARCHS+=("$FRAMEWORK_EXECUTABLE_PATH-$ARCH")



      done



      lipo -o "$FRAMEWORK_EXECUTABLE_PATH-merged" -create "${EXTRACTED_ARCHS[@]}"



      rm "${EXTRACTED_ARCHS[@]}"



      rm "$FRAMEWORK_EXECUTABLE_PATH"



      mv "$FRAMEWORK_EXECUTABLE_PATH-merged" "$FRAMEWORK_EXECUTABLE_PATH"



      done
      ```
   3. Select **Run script: For install builds only**.

   This removes the iOS Simulator architecture from your release binary used for AppStore Connect upload.

   Static library: Add a linker flag

   1. In Xcode, go to the **Build Settings** tab of your application target.
   2. Expand **Linking**.
   3. Add the `-ObjC` linker flag to **Other Linker Flags**.

   Static library: Make Dynatrace available to Swift code

   You can skip this step if your application doesn't have Swift code or doesn't need access to the Dynatrace library.

   We assume that you already created the Objective-C bridging header file for your Swift code in Xcode.

   1. Make sure you set the bridging header file in your application target build settings.
   2. Add the following import line to the bridging header file:

      ```
      #import Dynatrace.h
      ```
5. Trigger your project build once before using OneAgent SDK or any import declarations in Xcode.

## Access mobile instrumentation wizard

The mobile instrumentation wizard in Dynatrace provides you with get-started instructions on instrumenting your iOS apps. To follow more detailed instructions, go to the [Set up OneAgent](#set-up-oneagent) section on this page.

The wizard also contains code snippets with your app's identification keys that you'll need to add to the [`Info.plist` file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**…**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Instrumentation wizard**.

## Known limitations

* We don't recommend using several monitoring tools simultaneously with crash reporting or web request instrumentation functionality enabled. This might cause compatibility issues, reporting of wrong or invalid information, and loss of monitoring and crash data. Nevertheless, if you decide to do so, verify via manual testing that these tools are compatible.
* To use both Dynatrace and Firebase, do one of the following.

  + [Completely deactivate Firebase Performance Monitoring﻿](https://firebase.google.com/docs/perf-mon/disable-sdk?platform=ios).
  + [Disable automatic web request instrumentation](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") in OneAgent for iOS.

  Follow only one of the approaches above; don't perform both actions.
* To use both Dynatrace and [mPaaS﻿](https://dt-url.net/mPaaS), do one of the following.

  + [Disable automatic web request instrumentation](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#disable-auto-request-instrumentation "Enrich mobile user experience monitoring using OneAgent SDK for iOS.") in OneAgent for iOS.
  + Don't use the [MPNebulaAdapter framework﻿](https://dt-url.net/MPNebulaAdapter).

  Follow only one of the approaches above; don't perform both actions.
* An auto-instrumented application can't carry out functions such as `Dynatrace.shutdown()` or Dynatrace `.flushEvents()`. You can manually insert these methods and other user-defined actions and events before performing auto-instrumentation.
* The following controls can't be used to create autogenerated actions:

  + Gestures
  + Certain `UIBarButton` items, including custom `UIBarButton` items added to the navigation bar by a storyboard (such as `info`) that use segues to transition to other views.

### File encryption compatibility

File-level encryption or restrictive iOS data protection can prevent OneAgent for Mobile from accessing its database files, causing data collection to stop.

**Issue**:
OneAgent for iOS stores data in SQLite files (`DTEvents_*.sqlite`, `DTX*`) in the Application Support directory. If these files are encrypted or protected strictly, OneAgent for iOS cannot read/write data, leading to:

* No new sessions or events collected
* Database corruption errors in logs
* Frequent database recreation

**Solutions**:

* **Recommended**: Exclude OneAgent files from your mobile app's file encryption
* **Alternative**: Use `FileProtectionType.completeUntilFirstUserAuthentication` for OneAgent files
* Apply encryption after OneAgent for iOS initializes

For debugging, see [OneAgent for iOS debug logging](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios "Turn on debug logging for OneAgent.").