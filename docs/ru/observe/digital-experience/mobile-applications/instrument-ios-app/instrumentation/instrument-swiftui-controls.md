---
title: Instrument SwiftUI controls
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls
scraped: 2026-02-22T21:16:12.983564
---

# Instrument SwiftUI controls

# Instrument SwiftUI controls

* How-to guide
* 13-min read
* Updated on Feb 18, 2026

OneAgent for iOS version 8.249+

After [instrumenting your mobile app with OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace."), you might also want to instrument your app's SwiftUI controls. This page provides additional information on how to set up your project, update our SwiftUI instrumentor, overcome some known limitations, and more.

To instrument SwiftUI controls, our SwiftUI instrumentor adds additional code to your project's source code (`*.swift` files) during the build process. This code observes the state of UI elements and notifies the OneAgent for iOS about any updates. After the build process is completed, all changes to your project's source code are reverted.

For detailed information on actions performed by the SwiftUI instrumentor and a copy of the altered code files, check the `dynatrace_instrumented` directory. The SwiftUI instrumentor creates backups of the instrumented files and generated logs in ZIP archive format.

## Requirements

* SwiftUI version 2.0+
* iOS 14+
* [OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.")

## Supported controls

We support the instrumentation of the following SwiftUI controls and views.

OneAgent for iOS version 8.249+

* [`Button`ï»¿](https://developer.apple.com/documentation/swiftui/button)
* [`Stepper`ï»¿](https://developer.apple.com/documentation/swiftui/stepper)
* [`Picker`ï»¿](https://developer.apple.com/documentation/swiftui/picker)
* [`Toggle`ï»¿](https://developer.apple.com/documentation/swiftui/toggle)
* [`Slider`ï»¿](https://developer.apple.com/documentation/swiftui/slider)

OneAgent for iOS version 8.265+

* [`PasteButton`ï»¿](https://developer.apple.com/documentation/swiftui/pastebutton)
* [`EditButton`ï»¿](https://developer.apple.com/documentation/swiftui/editbutton)
* [`RenameButton`ï»¿](https://developer.apple.com/documentation/swiftui/renamebutton)
* [`Link`ï»¿](https://developer.apple.com/documentation/swiftui/link)
* [`ShareLink`ï»¿](https://developer.apple.com/documentation/swiftui/sharelink)
* [`NavigationLink`ï»¿](https://developer.apple.com/documentation/swiftui/navigationlink)
* [`DatePicker`ï»¿](https://developer.apple.com/documentation/swiftui/datepicker)
* [`MultiDatePicker`ï»¿](https://developer.apple.com/documentation/swiftui/multidatepicker)
* [`ColorPicker`ï»¿](https://developer.apple.com/documentation/swiftui/colorpicker)
* [`TabView`ï»¿](https://developer.apple.com/documentation/swiftui/tabview)
* [`List`ï»¿](https://developer.apple.com/documentation/swiftui/list)

OneAgent for iOS version 8.269+

* [`Menu`ï»¿](https://developer.apple.com/documentation/swiftui/menu)

When required, you can [globally](#exclude-controls-global) or [locally exclude certain controls from the SwiftUI instrumentation process](#exclude-controls-local).

## Supported methods

OneAgent for iOS version 8.265+

We support the instrumentation of the following SwiftUI methods:

* [`onTapGesture(count:perform:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:perform:))
* [`onTapGesture(count:coordinateSpace:perform:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/ontapgesture(count:coordinatespace:perform:))
* [`refreshable(action:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/refreshable(action:))
* [`sheet(isPresented:onDismiss:content:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))
* [`sheet(item:onDismiss:content:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:))
* [`popover(isPresented:attachmentAnchor:arrowEdge:content:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:))
* [`popover(item:attachmentAnchor:arrowEdge:content:)`ï»¿](https://developer.apple.com/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:))

The following data is reported every time the closure of one of the supported methods is executed:

* Method name
* Type of view the method was attached to
* Parent view name

## Lifecycle monitoring

OneAgent for iOS version 8.265+

The SwiftUI instrumentor collects data on the following events:

* **Application start**
* **Display**: [`onAppear`ï»¿](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) of any SwiftUI view presented from a [`NavigationLink`ï»¿](https://developer.apple.com/documentation/swiftui/navigationlink) or a [`TabView`ï»¿](https://developer.apple.com/documentation/swiftui/tabview) control
* **Redisplay**: [`onAppear`ï»¿](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) of any SwiftUI view presented from a [`NavigationLink`ï»¿](https://developer.apple.com/documentation/swiftui/navigationlink) or a [`TabView`ï»¿](https://developer.apple.com/documentation/swiftui/tabview) control

## Required steps

To instrument your app's SwiftUI controls, make sure you've completed the following steps:

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an application in Dynatrace**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#create-app-in-ui "Set up user experience monitoring for iOS apps within Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OneAgent for your project**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#set-up-oneagent "Set up user experience monitoring for iOS apps within Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Install our SwiftUI instrumentor**](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls#install-instrumentor "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.")

## Manage SwiftUI instrumentor

### Install the instrumentor

To instrument your app's SwiftUI controls, install the Dynatrace SwiftUI instrumentor. You can do that via Homebrew or manually.

[OneAgent for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.") should already be set up for your project. Also, don't forget to back up your project before installing the instrumentor.

Homebrew

Manual

1. Run `brew tap dynatrace/tools` to add one of the Dynatrace taps.
2. Run `brew install DTSwiftInstrumentor` to install our SwiftUI instrumentor.
3. Quit Xcode and execute `DTSwiftInstrumentor install`.

   * Optional Additionally, you can specify `<PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`. If no project details are provided, the tool tries to auto-detect the available targets and schemes and start an interactive selection.

1. Download and extract the ZIP file containing our SwiftUI instrumentor. The link is available in the [mobile instrumentation wizard](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
2. Create a `.dynatrace` folder in your project rootâon the same level as the `*.xcodeproj` file.

   If you receive a system warning stating that you cannot create a folder with a name that begins with a dot, do one of the following:

   * In Terminal, run `mkdir .dynatrace` inside the project root to create a `.dynatrace` folder.
   * In Terminal, run `defaults write com.apple.finder AppleShowAllFiles true` and `killall Finder` to show hidden folders and files. Then create a `.dynatrace` folder in Finder.

     You can also run `defaults write com.apple.finder AppleShowAllFiles false` and `killall Finder` to hide hidden folders and files back.
3. Copy the downloaded `DTSwiftInstrumentor` to the `.dynatrace` folder and make sure that the file is executable.
4. Quit Xcode, and execute `.dynatrace/DTSwiftInstrumentor install <PROJECT.xcodeproj> --scheme <SCHEME> --target <TARGET>`.

If an error occurs during the implementation, check the Xcode build log or the instrumentation log for detailed information on the error. For additional hints, refer to [Mobile applications: Issues with SwiftUI instrumentationï»¿](https://dt-url.net/yh638kl) in the Dynatrace Community.

When you build your app, you should do that with the scheme that you've instrumented.

### Update the instrumentor



When the new version of the SwiftUI instrumentor is available, you can update it via Homebrew or manually.

Homebrew

Manual

Once released, new versions of the instrumentor are loaded through the added tap.

Run `brew update` and `brew upgrade DTSwiftInstrumentor` to update our SwiftUI instrumentor.

1. Download and extract the ZIP file containing the new version of the SwiftUI instrumentor. The link is available in the [mobile instrumentation wizard](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.").
2. Copy the downloaded `DTSwiftInstrumentor` to the `.dynatrace` folder, and replace the existing file.

If you see the following build warning, you also need to update the build scripts that were integrated during the installation of the Dynatrace SwiftUI instrumentor.

```
Dynatrace: There is an upgrade for your project instrumentation. Please execute "DTSwiftInstrumentor project-upgrade <PROJECT.xcodeproj>" to upgrade your project
```

Run the suggested command to update the build scripts, and then save the changes made to your project file.

### Uninstall the instrumentor

If you no longer need the Dynatrace SwiftUI instrumentor, you can delete it from your system via Homebrew, or you can manually remove it from your project.

Homebrew

Manual

Run `brew remove DTSwiftInstrumentor` and `brew untap dynatrace/tools` to remove our SwiftUI instrumentor from your system.

1. Run `DTSwiftInstrumentor uninstall` to remove the SwiftUI instrumentor from your project.

   * Optional Additionally, you can specify `<PROJECT.xcodeproj>`. If no project details are provided, the tool tries to auto-detect and start an interactive selection.
2. Optional Delete the `.dynatrace` and `dynatrace_instrumented` folders from your project.

   These folders contain cache, log data, and, if applicable, manually setup instrumentor binary.
   These folders contain the instrumentor cache, log data, and, if applicable, instrumentor binaries.

## Check SwiftUI instrumentation diff

OneAgent for iOS version 8.257+

To check the difference between your original code and the code modified by the SwiftUI instrumentor, run one of the following commands:

* From the project root:

  + `DTSwiftInstrumentor diff` if you installed the instrumentor via Homebrew
  + `.dynatrace/DTSwiftInstrumentor diff` if you installed the instrumentor manually
* From any directory

  + `DTSwiftInstrumentor diff <root-project-dir-path>`

## Known limitations

### Instrumentation of custom SwiftUI controls not supported

Currently, Dynatrace doesn't support the instrumentation of custom SwiftUI controls. For the list of SwiftUI controls that you can instrument, see [Supported controls](#supported-controls).

### Issue with previews in Xcode

When a simulator build included the SwiftUI instrumentation, the previews were not loaded in Xcode. As a workaround, we disabled the SwiftUI instrumentation for simulator builds. If you want to add the SwiftUI instrumentation to simulator builds, see [Instrument simulator builds](#instrument-simulator-builds).

### SwiftUI 2.0+ only

Dynatrace supports SwiftUI 2.0+ instrumentation because the `onChange` listener is unavailable in earlier SwiftUI releases. For this reason, a deployment target needs to be of iOS 14+.

### Longer build time

Unlike the OneAgent for iOS that modifies your mobile app in memory during runtime, the SwiftUI instrumentor alters your project's source code during build time. For this reason, the SwiftUI instrumentation process has a noticeable impact on the build time.

To decrease the build time

* Build only for **Device**. If you've decided to [instrument simulator builds](#instrument-simulator-builds), disable that feature.
* Don't run SwiftUI instrumentation on every possible build. We suggest running SwiftUI instrumentation on branches like `main` or `release`.

### watchOS incompatibility

It's impossible to compile a project containing files that are added to a watchOS target, as there is no OneAgent for watchOS. In this case, [manually exclude](#exclude-swift-files) all files that are shared with or part of a watchOS target.

### tvOS not supported

Currently, there is no official support for tvOS SwiftUI builds.

## SwiftUI control labels

Unless specified otherwise, the Dynatrace SwiftUI instrumentor attempts to fetch each control name by recursively searching for string literals or variables provided as a title.
In the example below, the instrumentor will extract `"Login"` as a label for the button:

```
Button("Login", action: {



/* perform login */



})
```

The extracted label will be used to report a `"Touch on Login"` auto action when a user interacts with the button.

In the following example, a user interaction with this button would be reported as `"Touch on bookmark"`:

```
Button(action: {



print("Hello world!")



}) {



Image("bookmark")



}
```

### Use a default control name

Use the `withCustomInstrumentationConfig(.useDefaultControlName)` modifier to set the control label to `<Control type>_<index>`:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useDefaultControlName)
```

When the modifier is applied, the instrumentor will report the touch action as `"Touch on Button_0"`.

### Use a custom control name

Use the `withCustomInstrumentationConfig(.useControlName(<Name>)` modifier to specify a custom label for a certain control as follows:

```
Button("Login", action: {



/* perform login */



}).withCustomInstrumentationConfig(.useControlName("Login Button"))
```

This way, every touch on the button would be reported as `"Touch on Login Button"`.

## Configure SwiftUI instrumentation

### Enable Session Replay on crashes

Session Replay on crashes can capture and visually replay the actions that your application user performed before a [crash](/docs/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") occurred.

To turn this feature on, see [Enable Session Replay for SwiftUI apps](/docs/observe/digital-experience/session-replay/session-replay-ios#sr-swiftui "Prerequisites and the procedure for enabling Session Replay for your iOS apps.").

### Globally exclude controls from SwiftUI instrumentation

OneAgent for iOS version 8.263+

The Dynatrace SwiftUI instrumentor instruments all UI elements listed under [Supported controls](#supported-controls). When required, you can globally exclude certain controls from the SwiftUI instrumentation process.

To globally exclude controls from the SwiftUI instrumentation, add the [`DTXSwiftUIExcludedControls` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

```
<key>DTXExcludedSwiftUIFiles</key>



<array>



<string>Button</string>



<string>Slider</string>



</array>
```

### Locally exclude controls from SwiftUI instrumentation

OneAgent for iOS version 8.263+

With the `withCustomInstrumentationConfig(.skipInstrumentation)` function, you can locally exclude controls from SwiftUI instrumentation.

In contrast to the [`DTXSwiftUIExcludedControls` configuration key](#exclude-controls-global), which allows you to prevent the instrumentation of all instances of a specified control type, the `withCustomInstrumentationConfig(.skipInstrumentation)` function can be used to exclude a specific instance of a control type. You can apply this function directly to a control or, to exclude multiple control instances, to a container.

Follow these guidelines when applying the `withCustomInstrumentationConfig(.skipInstrumentation)` function:

* To use the function, first add the `import Dynatrace` import statement.
* Add `withCustomInstrumentationConfig(.skipInstrumentation)` as the last modifier in the list of the view modifiers. For example:

  ```
  Button("Login", action: { /* perform login */ })



  .padding()



  .background(Color.red)



  .frame(width: 40)



  .withCustomInstrumentationConfig(.skipInstrumentation)
  ```

#### Exclude a single control

Use the following code to locally exclude a single control from the SwiftUI instrumentation:

```
import Dynatrace



â¦



Button("Login", action: { /* perform login */ })



.withCustomInstrumentationConfig(.skipInstrumentation)
```

#### Exclude multiple controls

To locally exclude a group of controls, apply the `withCustomInstrumentationConfig(.skipInstrumentation)` function to their parent container.

```
import Dynatrace



â¦



HStack {



Button("Login", action: { /* perform login */ })



Button("Register", action: { /* perform registration */ })



}.withCustomInstrumentationConfig(.skipInstrumentation)
```

### Exclude files from SwiftUI instrumentation



By default, the Dynatrace SwiftUI instrumentor processes all files with a `.swift` file extension, but it only instruments files that contain the [supported controls](#supported-controls). When required, you can exclude certain files and directories from the SwiftUI instrumentation process.

To exclude files and directories from the SwiftUI instrumentation

1. Add the [`DTXExcludedSwiftUIFiles` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").
2. List relative paths of all files and directories that you don't want to instrument. The paths should be relative to the project root, which is the directory where the `.xcodeproj` file is located.

   ```
   <key>DTXExcludedSwiftUIFiles</key>



   <array>



   <string>relative/file/path/</string>



   <string>relative/file.swift</string>



   </array>
   ```

The instrumentation log, which is available after each build, contains the list of files and directories that should be excluded from the SwiftUI instrumentation. The instrumentation log also shows you if a file or directory was excluded during the instrumentation process.

### Instrument simulator builds

We disabled the SwiftUI instrumentation for simulator builds to overcome an [issue with the previews in Xcode](#issue-preview-xcode).

To enable the SwiftUI instrumentation for simulator builds, add the [`DTXSwiftUIInstrumentSimulatorBuilds` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") and set this key to `true`.

```
<key>DTXSwiftUIInstrumentSimulatorBuilds</key>



<true/>
```

### Create builds for unsupported deployment targets

Our SwiftUI instrumentor generates SwiftUI 2.0+ compatible code that only runs on devices with iOS 14+. The attempt to generate builds for deployment targets of iOS 13 and earlier will fail.

To override this check, add the [`DTXSwiftUIIgnoreDeploymentTarget` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") and set this key to `true`.

```
<key>DTXSwiftUIIgnoreDeploymentTarget</key>



<true/>
```

### Enable line number mapping for Objective-C projects

Crash reports that are available in Dynatrace are not based on the source code of your project. These reports are based on the altered code that Dynatrace generates during instrumentation. This is why line number mapping is added to your project during instrumentation and later passed to Dynatrace on app launch. Otherwise, the line numbers in crash reports would be incorrect.

By default, the Dynatrace SwiftUI instrumentor generates a line number mapping and inserts it into your project's main class. This happens automatically for projects with a Swift main class, but not for legacy Objective-C projects. For such projects, you'll get an error, and our SwiftUI instrumentor won't instrument your mobile app.

To enable line number mapping for Objective-C projects

1. Add the [`DTXSwiftUIManualPlaceholder` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") and set this key to `true`.

   ```
   <key>DTXSwiftUIManualPlaceholder</key>



   <true/>
   ```
2. Add the special `AppDelegate.m` placeholder to the main class.
3. Add the `[Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];` line to the main class in either the `init` or the `didFinishLaunchingWithOptions` method (not in both).

   didFinishLaunchingWithOptions

   init

   ```
   - (BOOL)application:(UIApplication *)application



   didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {



   [Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];



   // ... your existing setup code



   return YES;



   }
   ```

   ```
   - (instancetype)init {



   self = [super init];



   if (self) {



   [Dynatrace handoverInstrumentorConfig:@{kDTXSwiftMappingJson: @"_DYNATRACE_SWIFTUI_MAPPING_PLACEHOLDER_"}];



   }



   return self;



   }
   ```

   During the build, the SwiftUI instrumentor replaces part of this line with the generated line number mapping.

### Enable automatic log cleanup

OneAgent for iOS version 8.257+

After each build, the SwiftUI instrumentor creates backups of the instrumented files and generated logs, which are stored under `dynatrace_instrumented`. By default, these files are not deleted, and the total size of the directory will grow over time. For this reason, we recommend that you to enable the automatic log cleanup.

* To delete the SwiftUI instrumentor logs after a certain number of builds, add the [`DTXCleanSwiftUILogsByCount` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your project's [`Info.plist` file](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.").

  ```
  <key>DTXCleanSwiftUILogsByCount</key>



  <number>10</number>
  ```
* To delete the logs after a certain number of days, add the [`DTXCleanSwiftUILogsByAgeDays` configuration key](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#swiftui "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to the `Info.plist` file.

  ```
  <key>DTXCleanSwiftUILogsByAgeDays</key>



  <number>5</number>
  ```

If you add both keys to the `Info.plist` file, the `DTXCleanSwiftUILogsByAgeDays` key takes precedence.

## Troubleshooting

We're still working on improving the SwiftUI instrumentation process. If you face any issues while instrumenting SwiftUI controls, refer to [Mobile applications: Issues with SwiftUI instrumentationï»¿](https://dt-url.net/yh638kl) in the Dynatrace Community.