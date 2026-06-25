---
title: Personal data captured by Dynatrace
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace
scraped: 2026-05-12T11:08:58.556166
---

# Personal data captured by Dynatrace

# Personal data captured by Dynatrace

* 12-min read
* Updated on Mar 05, 2026

From monitored environments, Dynatrace may capture end-user data, potentially including personal and confidential information about your end users.

This page identifies where personal data may be captured and how you can limit the capture, storage, and display thereof to help you comply with privacy-related legal requirements, including the California Consumer Privacy Act (CCPA; California, United States), General Data Protection Regulation (GDPR; European Union), or Lei Geral de ProteÃÂ§ÃÂ£o de Dados (LGPD; Brazil).

Dynatrace masks data according to our [three levels of data protection](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection."): **at capture**, **at storage**, and **at display**. In the following sections, icons indicate the level of masking applied to each data type that Dynatrace captures.

|  |  |
| --- | --- |
| Captured by default | Captured by default |
| Not captured by default | Not captured by default |
| Masked | Masked |
| Not masked | Not masked |
| Masking preferences can be configured; masked by default | Masking preferences can be configured; masked by default |
| Masking preferences can be configured; not masked by default | Masking preferences can be configured; not masked by default |
| Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |
| Masking preferences are set according to end-user permission | Masking preferences are set according to end-user permission |

## Service request monitoring

Dynatrace captures the most important data points of incoming requests as well as the web requests of end-users of your application (that is, service requests). URLs, client IPs, and certain HTTP header fields are captured automatically.

You can [configure global privacy settings](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") to mask client IP addresses, URIs, and HTTP post parameters.

| Data type | Default | Masking at capture | Masking at storage | Masking at display |
| --- | --- | --- | --- | --- |
| Client IP addresses[1](#fn-1-1-def) | Captured by default | Masking preferences can be configured; masked by default | Masking preferences can be configured; masked by default | Masking preferences are set according to end-user permission |
| URIs[2](#fn-1-2-def) | Captured by default | Masking preferences can be configured; not masked by default | Masking preferences can be configured; not masked by default | Masking is dependent on the configuration set during capture and storage |
| HTTP headers[2](#fn-1-2-def), [3](#fn-1-3-def) | Captured by default | Not masked | Masking preferences can be configured; not masked by default | Masking preferences are set according to end-user permission |
| HTTP post parameters[2](#fn-1-2-def) | Not captured by default | Not masked | Masking preferences can be configured; not masked by default | Masking preferences are set according to end-user permission |
| URL query parameters[2](#fn-1-2-def), [4](#fn-1-4-def) | Captured by default | Masking preferences can be configured; not masked by default | Masking preferences can be configured; not masked by default | Masking is dependent on the configuration set during capture and storage |
| Exception messages[2](#fn-1-2-def), [5](#fn-1-5-def) | Captured by default | Masking preferences can be configured; not masked by default | Masking preferences can be configured; not masked by default | Masking preferences are set according to end-user permission |
| SQL literals[6](#fn-1-6-def) | Captured by default | Masked | Masked | Masked |
| SQL bind variables[7](#fn-1-7-def) | Not captured by default | Not masked | Not masked | Masking preferences are set according to end-user permission |
| Method arguments / return values[8](#fn-1-8-def) | Not captured by default | Not masked | Not masked | Masking preferences are set according to end-user permission |

1

Configure masking via the [**Mask end-user IP addresses and GPS coordinates** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") in the data privacy settings.

2

Configure masking at capture via the [**OneAgent-side masking** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#oneagent-side-masking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") and masking at storage via the [**Mask personal data in URIs** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-uris "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") in the data privacy settings.

3

Only certain headers are captured automatically. You can capture other headers via [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

4

Query parameters are always masked on display and can also be masked upon storage. To capture parameters explicitly, configure [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

5

To avoid capturing certain exceptions, go to **Settings** > **Server-side service monitoring** > **Deep monitoring**, expand the **Exclude noisy and unnecessary exceptions** section, and add the required exclusion rules.

6

Literals that are part of the `WHERE` clause of an SQL statement are replaced with `*****`, for example, `WHERE userId = '*********'`.

7

Bind variables support availability [depends on your deployment and license](/managed/observe/infrastructure-observability/databases/database-services-classic/support-for-sql-bind-variables#availability "Learn how you can enable Dynatrace OneAgent to capture the values of bind variables."). To learn how to start capturing SQL bind values, see [Support for SQL bind variables](/managed/observe/infrastructure-observability/databases/database-services-classic/support-for-sql-bind-variables "Learn how you can enable Dynatrace OneAgent to capture the values of bind variables."). SQL bind values are replaced with `*****`. Only users who have permission to view a specific entity or management zone can view unmasked bind values within that entity or zone.

8

Configure via [request attributes](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

## OpenTelemetry attributes for distributed tracing

Dynatrace automatically captures all OpenTracing and OpenTelemetry [attributes](/managed/ingest-from/opentelemetry#attribute "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), but it only stores attributes that are not blocked. See [Enable the OpenTelemetry Span Sensor for OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

| Data type | Default | Masking at capture | Masking at storage | Masking at display |
| --- | --- | --- | --- | --- |
| Non-blocked attributes | Captured by default | Not masked | Not masked | Masking preferences are set according to end-user permission |

## Real User Monitoring (RUM)

With [Dynatrace Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more."), you can understand your customers better by accessing performance analysis in real time. This includes all performed user actions and how their impact on performance.

To allow performance analysis based on geographical regions, Dynatrace captures IP addresses and GPS coordinates, which are masked by default. To mask user actions and URIs, [configure the global privacy settings](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."). Dynatrace can also detect returning users by storing a randomly generated ID (a user tag) in each user's browser or on their device; this kind of user tagging is not enabled by default.

| Data type | Default | Masking at capture | Masking at storage | Masking at display |
| --- | --- | --- | --- | --- |
| [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")[1](#fn-2-1-def) | Captured by default | Masking preferences can be configured; not masked by default | Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |
| [IP addresses and GPS coordinates](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")[2](#fn-2-2-def), [3](#fn-2-3-def) | Captured by default[4](#fn-2-4-def) | Masking preferences can be configured; masked by default | Masking preferences can be configured; masked by default | Masking is dependent on the configuration set during capture and storage |
| URIs[3](#fn-2-3-def), [5](#fn-2-5-def) | Captured by default | Not masked | Masking preferences can be configured; not masked by default | Masking is dependent on the configuration set during capture and storage |
| [User tags](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.")[6](#fn-2-6-def) | Not captured by default | Masked | Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |
| Session and action properties[7](#fn-2-7-def) | Not captured by default | Masked | Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |

1

User actions contain a name, a set of timings, and [metadata](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions#add-and-use-placeholders "Customize automatically generated user action names for your web applications.").  
Web applications Configure masking via the [**Mask user actions (web applications only)** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-user-actions "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") in the data privacy settings. You can also [create custom user action names](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.").  
Mobile applications Configure masking via a special [masking property](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#user-action-masking "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") or set action naming and extraction rules (mobile application settings > **Naming rules**).

2

Configure masking via the [**Mask end-user IP addresses and GPS coordinates** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") in the data privacy settings.

3

Dynatrace looks for personal data such as IP addresses, UUIDs, payment card numbers, emails, and other identifiable IDs. However, there might be other personal data or individual characters that Dynatrace isn't able to detect automatically. To mask the URL on display, use [custom names for user actions](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), resource grouping, and naming.

4

By default, [location capturing](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent.") is disabled for mobile applications.

5

Configure masking via the [**Mask personal data in URIs** option](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-uris "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") in the data privacy settings.

6

Web applications You can [set up user tagging](/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") using either the RUM JavaScript API or your application's page metadata.  
Mobile applications Leverage a variant of a "user tagging" method to add a user tag to a session; check the [corresponding documentation](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") for more information.

7

Session and action properties for [web](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."), [mobile](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications."), and [custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.") need to be explicitly defined and contain whatever the selected underlying data sources propagated them with.

You can also use the following settings to control how personal data is captured when RUM is enabled for your applications.

* [Opt-in mode](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#user-opt-in-mode-gdpr "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [Do Not Track](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#do-not-track-gdpr "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [User tracking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#user-tracking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

## Log Monitoring

Log Monitoring is an optional feature that is enabled by default. You can use it to directly access the log content of all your system's mission-critical processes, search for specific log messages, and store all logs centrally.

Log files can include user names, email addresses, URL parameters, and other information that you might not want to disclose. By default, nothing is masked, but Log Monitoring offers the ability to [mask sensitive information](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") in the logs. You define the masking rules, so any data can be replaced with an SHA-1 hash or a fixed phrase, for example, `*****`, `#######`, `MASKED`, or `Last name`.

| Data type | Masking at Dynatrace log processing | Masking at OneAgent configuration |
| --- | --- | --- |
| Log file content | Masking preferences can be configured; not masked by default | Masking preferences can be configured; not masked by default |

## Session Replay

Session Replay is an optional feature that is turned off by default. You can enable [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.") to capture and visually replay users' complete digital interactions with your application.

* For web applications, Session Replay captures all HTML source code and the mutations that are originated by user interactions. It also captures all user interactions obtained through form fields, attributes, content, and interactions such as mouse movement and scrolling.
* For mobile applications, Session Replay is available only for those sessions that end in a crash. To visually recreate the end user's experience with your app before a crash, Session Replay captures screenshots and events from the monitored app.

| Data type | Masking at capture | Masking at storage | Masking at display |
| --- | --- | --- | --- |
| Password form fields | Masked | Masked | Masked |
| User input[1](#fn-3-1-def)  Text[1](#fn-3-1-def)  Images[1](#fn-3-1-def), [2](#fn-3-2-def)  Attributes[1](#fn-3-1-def) | Masking preferences can be configured; masked by default | Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |
| Interactions[3](#fn-3-3-def) | Masking preferences can be configured; not masked by default | Masking is dependent on the configuration set during capture and storage | Masking is dependent on the configuration set during capture and storage |

1

Web applications Configure in the [application masking settings](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-ui "Configure monitoring consumption and data privacy settings for Session Replay.") or by adding the [`data-dtrum-mask` attribute](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-code "Configure monitoring consumption and data privacy settings for Session Replay.") to the required element in the application code. For details, see [Configure Session Replay | Masking](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-masking "Configure monitoring consumption and data privacy settings for Session Replay."). User input and text are replaced with `***` or `000`. Only alphanumeric characters are replaced; format characters such as periods, commas, and colons are not masked. Attributes values are replaced with `***`. Images are replaced with a placeholder image.  
Mobile applications Configure in the application code for [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios#mask-sensitive-data "Prerequisites and the procedure for enabling Session Replay for your iOS apps.") and [Android](/managed/observe/digital-experience/session-replay/session-replay-android#mask-sensitive-data "Set up Session Replay for your Android apps to learn which actions your users perform."). User input and text are replaced with `*****` in the Session Replay timeline and with black boxes in the screenshots. All characters are masked. Images are replaced with a black box.

2

Except background images or images set by CSS.

3

Web applications Configure using the **Block list** option in the [application masking settings](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-ui "Configure monitoring consumption and data privacy settings for Session Replay.").  
Mobile applications Not possible to mask interactions.

You can also use the following settings to control how personal data is captured when Session Replay is enabled for your web and mobile applications.

| Application type | Option name | Description | Default |
| --- | --- | --- | --- |
| Web | [Session Replay opt-in mode](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-opt-in-mode "Configure monitoring consumption and data privacy settings for Session Replay.") | Use to record a particular part of a session or to implement end-user permission for session recording. When this mode is on, Session Replay is disabled until the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`ï»¿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method is called. | Disabled |
| Mobile | [Opt-in mode](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."): permission to record replays of crashes | Use to implement end-user permission for session recording. If a user allowed you to record replays of crashes via Session Replay on crashes:  iOS: Set `privacyConfig.crashReplayOptedIn` to `true`/`YES`.  Android: Set `.withCrashReplayOptedIn` to `true`. Screen requesting permission for session recording Session Replay - Session Replay opt-in mode for mobile apps  Session Replay - Session Replay opt-in mode for mobile apps | â |
| Web | [URL exclusion](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-url-exclusion "Configure monitoring consumption and data privacy settings for Session Replay.") | Use this setting to exclude particular pages from session recording. | â |
| Web | [Do Not Track](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") | Enable this feature if you want to comply with the "Do Not Track" setting that your users can turn on in their browsers.If you select **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**, Session Replay is disabled when the "Do Not Track" setting is detected in your users' browsers. | Comply with 'Do Not Track' browser settings â Capture anonymous user sessions for "Do Not Track"-enabled browsers |
| Web  Mobile | [User permissions](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-permissions "Configure monitoring consumption and data privacy settings for Session Replay.")  [Management zones](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-management-zones "Configure monitoring consumption and data privacy settings for Session Replay.") | Use the **Replay sessions with masking** and **Replay sessions without masking** permissions to control who has access to session recordings with and without masking. | **Replay sessions with masking** permission is enabled for all users |

## OneAgent diagnostics

[OneAgent diagnostics](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") is an optional feature that enables you to collect and analyze support archives for anomalies.

Support archives are created by Dynatrace OneAgent and contain OneAgent log and configuration files as well as specific data from monitored hosts and processes, for example, process names and identification numbers. OneAgent log files may contain personal data, for example, as part of a stack trace.

To comply with regional data protection and privacy regulations, Dynatrace does the following:

* Masks some personal data before storing a support archive in Cassandra and uploading it to an AWS S3 bucket. For example, IBANs and URI credentials are replaced with `<masked>`. However, some personal data may not be masked.
* Writes audit log messages when support archives are created, analyzed, accessed, and deleted to ensure transparency in the use of support archives.
* Provides access to OneAgent support archives only to users that have the **View sensitive request data** [environment permission](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").
* Automatically deletes all diagnostic data 30 days after its collection. This [data retention period](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.") is configurable.

  This applies to the data on the Dynatrace Cluster. You can also choose to delete collected diagnostic data earlier.

| Data type | Masking at capture | Masking at storage | Masking at display |
| --- | --- | --- | --- |
| OneAgent log and config files | Not masked | Masked | Masked |

## Log sharing

The `shareLogsFile` API allows you to share locally stored log files via an iOS sharing sheet (`UIActivityViewController`). This feature requires the [`DTXWriteLogsToFile`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") flag to be set to `true`.

This feature allows logs to be shared directly from the device without requiring access to Xcode for log extraction. It is not intended for use in production applications.

The `shareLogsFile` API is not available on tvOS.

## Live Debugger

Live Debugger is an optional feature. To make it available, enable [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") on your OneAgents. You can use Live Debugger to debug your services and applications in any environment in real time without stopping your applications.

Live Debugger collects snapshots that can include variable values that your application processes. You can [define masking rules](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), so any data can be replaced with an SHA-1 hash or a fixed phrase, for example, `*****`, `#######`, `MASKED`, or `Last name`. Masking is performed by the agent on your server, so sensitive data will not leave your server or network.