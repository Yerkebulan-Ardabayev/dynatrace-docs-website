---
title: OneAgent for iOS debug logging in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/logging-for-ios
---

# OneAgent for iOS debug logging in RUM Classic

# OneAgent for iOS debug logging in RUM Classic

* How-to guide
* 1-min read
* Updated on Oct 24, 2023

To enable debug logging for iOS, add the [`DTXLogLevel` configuration key](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") to your app's [`Info.plist` file](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration."):

```
<key>DTXLogLevel</key>



<string>ALL</string>
```

The available log levels are listed below in order of increasing detail—each level includes the information of the preceding log levels.

| Log level | Information captured |
| --- | --- |
| `OFF` | OneAgent version only |
| `SEVERE` | Events impacting OneAgent functionality that might disable monitoring |
| `WARNING` | Events that might lead to problems |
| `INFO` | Additional informational messages |
| `ALL` | All debug information |

While running your app, you should find logs in the console within the Xcode debug area. Note that the log level is designed for troubleshooting and has no impact on the data captured by OneAgent.

The default log level is `OFF`, as heavy logging can impact your app's performance.

Additionally, make sure that environment variable `OS_ACTIVITY_MODE` is not set to `disabled`, which would disable debug logging.

The logging output in the Xcode 15+ console no longer shows timestamps. When you copy the logs, for example, to submit them to a Dynatrace product expert, select all log lines in the console and select **Copy Rows with All Metadata**.