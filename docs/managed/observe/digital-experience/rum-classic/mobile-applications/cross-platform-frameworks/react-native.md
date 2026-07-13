---
title: Instrument mobile apps with Dynatrace React Native plugin in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native
---

# Instrument mobile apps with Dynatrace React Native plugin in RUM Classic

# Instrument mobile apps with Dynatrace React Native plugin in RUM Classic

* How-to guide
* 4-min read
* Updated on Jul 10, 2026

Our React Native plugin allows you to auto-instrument your React Native apps with Dynatrace OneAgent for Android and iOS. The plugin provides an API to add manual instrumentation and is compatible with raw, ejected React Native projects.

For detailed technical documentation, see the [Dynatrace React Native plugin﻿](https://www.npmjs.com/package/@dynatrace/react-native-plugin) page on the npm site.

Follow the steps below to set up the Dynatrace React Native plugin for your mobile app.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a mobile application in Dynatrace**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#create-app-in-ui "Auto-instrument your React Native applications with OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up React Native plugin**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#set-up-plugin "Auto-instrument your React Native applications with OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Build and run your app**](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native#build-and-run-app "Auto-instrument your React Native applications with OneAgent.")

## Prerequisites

* React 16.8+
* React Native 0.60+
* Android version 5.0+ (API 21+)
* Gradle version 7.0+
* Android Gradle plugin version 7.0+
* Java 11
* iOS version 12+

## Step 1 Create a mobile application in Dynatrace

To create a mobile application in Dynatrace

1. In Dynatrace, go to **Mobile**.
2. Select **Create mobile app**.
3. Enter a name for your application and select **Create mobile app**. The application settings page opens.

## Step 2 Set up React Native plugin

1. From the application settings, select **Instrumentation wizard** > **React Native**. The instrumentation wizard guides you through the set-up process.
2. Install the Dynatrace React Native plugin:

   React Native 0.60.0+

   * Call `npm install @dynatrace/react-native-plugin`.
   * iOS only If you use pods, go to the `ios` directory and execute `pod install` to install the new Dynatrace dependency to your Xcode project.
3. From the instrumentation wizard, download the `dynatrace.config.js` file and place it into the root directory of your project next to `app.json`. If you're upgrading from a previous version of the Dynatrace React Native plugin, copy the old configuration values from `dynatrace.config` to the new `dynatrace.config.js` file.
4. Add the `@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace` babel plugin and the `@dynatrace/react-native-plugin` JSX runtime to your `babel.config.js` file:

   @babel/plugin-transform-react-jsx

   Expo

   ```
   module.exports = {



   presets: [



   ['module:@react-native/babel-preset'], // or 'module:metro-react-native-babel-preset'



   ],



   plugins: [



   '@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace',



   [



   '@babel/plugin-transform-react-jsx',



   {



   runtime: 'automatic',



   importSource: "@dynatrace/react-native-plugin"



   },



   ],



   ],



   };
   ```

   ```
   module.exports = function (api) {



   api.cache(true);



   return {



   presets: [



   ['babel-preset-expo',



   {



   jsxRuntime: 'automatic',



   jsxImportSource: '@dynatrace/react-native-plugin',



   },



   ],



   ],



   plugins: [



   '@dynatrace/react-native-plugin/instrumentation/BabelPluginDynatrace',



   ],



   };



   };
   ```
5. Enable user opt-in mode: your app should include a privacy notice for users to configure their privacy preferences. You can insert the following API call to enable Dynatrace monitoring:

   ```
   import { Dynatrace, DataCollectionLevel, UserPrivacyOptions } from '@dynatrace/react-native-plugin';



   // Privacy settings configured below are only provided



   // to allow a quick start with capturing monitoring data.



   // This has to be requested from the user



   // (for example, in a privacy settings screen) and the user decision



   // has to be applied similar to this example.



   const privacyConfig = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



   Dynatrace.applyUserPrivacyOptions(privacyConfig);
   ```

## Step 3 Build and run your app

* Run `npx instrumentDynatrace` in the root of your React Native project to apply the configuration set in the `dynatrace.config.js` file. This command configures both Android and iOS projects.
* Execute `react-native run-android` or `react-native run-ios` to rebuild and run your app.

  If you're upgrading to React Native 0.70+ or using the @react-native-community/cli 9.x+ version, note that our automated script running before every `react-native run-android` or `react-native run-ios` command is no longer working. If you've changed the configuration in the `dynatrace.config.js` file, execute `npx instrumentDynatrace` to apply the new configuration.
* Whenever you change the configuration in the `dynatrace.config.js` file, run the following commands and then rebuild your app.

  1. `npx instrumentDynatrace` to apply the new configuration from `dynatrace.config.js`
  2. `react-native start --reset-cache` to reset the cache. Not resetting the cache might result in a mixture of old and new configurations.
* Specify custom paths via [custom arguments﻿](https://www.npmjs.com/package/@dynatrace/react-native-plugin#customizing-paths-for-configuration).

## User action naming

See [User action naming rules](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#user-action-naming-rules "Learn what user actions are and how they help you understand what users do with your application.") for more details on user action naming in Dynatrace.

#### React views

* `displayName`: Checks if React views have a display name set.
* `class name`: If the display name is unavailable, the class name is used by taking the name property from the constructor.

#### Touchables

* Accessibility label
* If both are not set, searches for inner text
* For an image button, searches for the source

#### Button Title

* Accessibility label
* For an image button, searches for the source
* If nothing is found, searches for inner text

If you minify the React Native code, you can use the `keep_classname` setting to preserve the class name.

## Related topics

* [React monitoring﻿](https://www.dynatrace.com/technologies/react-monitoring/)