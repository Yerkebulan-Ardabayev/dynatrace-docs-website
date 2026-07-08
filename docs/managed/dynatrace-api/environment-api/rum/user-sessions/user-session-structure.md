---
title: User sessions API - User session structure
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure
---

# User sessions API - User session structure

# User sessions API - User session structure

* Reference
* Updated on May 02, 2022

This page provides descriptions of all possible fields that a user session might include.

#### The `UserSession` object

A [user session﻿](https://dt-url.net/xv183rb8), encompassing multiple user actions and additional information about a user's visit.

| Element | Type | Description |
| --- | --- | --- |
| appVersion | string | The version of the application where the user session has been recorded.  This information is provided by another integration, such as OpenKit. |
| applicationType | string | The type of the application used in the user session. The element can hold these values * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` * `WEB_APPLICATION` |
| bounce | boolean | The user session has (`true`) or doesn't have (`false`) a bounce.  A bounce means there is only one (or less) user action in the user session. |
| browserFamily | string | The family of the browser used for the user session. |
| browserMajorVersion | string | The version of the browser used for the user session. |
| browserMonitorId | string | The ID of the Synthetic browser monitor that created the session. |
| browserMonitorName | string | The name of the Synthetic browser monitor that created the session. |
| browserType | string | The type of browser used for the user session. |
| carrier | string | The carrier information of the mobile user session. |
| city | string | The city from which the user session originates (based on the IP address). |
| clientTimeOffset | integer | The time offset of the client, in milliseconds |
| clientType | string | Additional information about the client.  This field can not be queried via the user session query language. Use the **browserType** field instead. |
| connectionType | string | The serialized connection type of the mobile user session. The element can hold these values * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |
| continent | string | The continent from which the user session originates (based on the IP address). |
| country | string | The country from which the user session originates (based on the IP address). |
| crashGroupId | string | If a mobile session crashed, this is the ID of the group to which the crashed session belongs.  If the session did not crash or the session is not a mobile session, it has the `null` value. |
| dateProperties | [DateProperty](#openapi-definition-DateProperty)[] | A list of custom properties of the user session with date values. |
| device | string | The detected device used for the user session. |
| displayResolution | string | The detected screen resolution of the device used for the user session. The element can hold these values * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` |
| doubleProperties | [DoubleProperty](#openapi-definition-DoubleProperty)[] | A list of custom properties of the user session with floating-point numerical values. |
| duration | integer | The duration of the user session, in milliseconds.  This is calculated as the amount of time between the start of the first user action and the end of the last user action. |
| endReason | string | The reason for the end of the user session. The element can hold these values * `DURATION_LIMIT` * `END_EVENT` * `EXTENDED_TIMEOUT` * `TEST_FAILED` * `TIMEOUT` * `USER_ACTION_LIMIT` |
| endTime | integer | The timestamp of the last user action in the user session, in UTC milliseconds. |
| errors | [UserSessionErrors](#openapi-definition-UserSessionErrors)[] | A list of errors recorded in the user session. |
| events | [UserSessionEvents](#openapi-definition-UserSessionEvents)[] | A list of additional events recorded in the user session. |
| hasCrash | boolean | The user session includes (`true`) or doesn't include (`false`) a crash. |
| hasError | boolean | The user session includes (`true`) or doesn't include (`false`) an error. |
| hasSessionReplay | boolean | Session Replay is (`true`) or is not (`false`) available for the session. |
| internalUserId | string | The unique ID of the user that triggered the user session. |
| ip | string | The IP address (IPv4 or IPv6) from which the user session originates. |
| isp | string | The internet service provider from which the user session originates (based on the IP address). |
| longProperties | [LongProperty](#openapi-definition-LongProperty)[] | A list of custom properties of the user session with integer (short or long) values. |
| manufacturer | string | The detected manufacturer of the device used for the user session. |
| matchingConversionGoals | string[] | A list of conversion goals achieved by the user session.  Additionally, you can define conversion goals for a single user action. |
| matchingConversionGoalsCount | integer | The number of conversion goals achieved by the user session. |
| networkTechnology | string | The network technology information of the mobile user session. |
| newUser | boolean | The user is a first-time (`true`) or a returning user (`false`). |
| numberOfRageClicks | integer | The number of rage clicks detected in the user session. |
| numberOfRageTaps | integer | The number of rage taps detected in the user session. |
| osFamily | string | The type of operating system used for the user session. |
| osVersion | string | The version of the operating system used for the user session. |
| partNumber | integer | User sessions can be split into multiple parts for various technical reasons (e.g. after 200 user actions). This `partNumber` represents the number of each part of the overall user session. |
| reasonForNoSessionReplay | string | The reason for absence of Session Replay. The element can hold these values * `KILLED_EMERGENCY` * `KILLED_ERROR` * `KILLED_INVALID_RESPONSE` * `KILLED_MIN_JS_AGENT_VERSION` * `KILLED_NO_LICENSE` * `KILLED_WRONG_CONTENT_TYPE` * `MISCONFIGURED_CLUSTER` * `MODULE_DISABLED` * `NO_ACTIVITY` * `OPTED_OUT_SESSION` * `OPT_IN_MODE` * `ROBOT_DETECTED` * `SAMPLED_OUT` * `UNABLE_TO_LOAD_WORKER` * `UNHANDLED_EXCEPTION` * `UNKNOWN` * `UNKNOWN_DOC_LOADED` * `UNSUPPORTED_BROWSER` * `VIEW_EXCLUDED` |
| reasonForNoSessionReplayMobile | string | The reason for absence of Session Replay on mobile. The element can hold these values * `COST_CONTROL` * `CRASHES_OPTED_IN` * `DISABLED` * `FULL_STORAGE` * `INVALID_CONFIGURATION` * `NO_AGENT` * `OPTED_OUT` * `RETENTION_TIME` * `UNKNOWN` |
| region | string | The region from which the user session originates (based on the IP address). |
| replayEnd | integer | The timestamp of the Session Replay end, in UTC milliseconds. |
| replayStart | integer | The timestamp of the Session Replay start, in UTC milliseconds. |
| rootedOrJailbroken | boolean | The mobile device is rooted/jailbroken (`true`) or genuine (`false`).  Has the value of `null` if the status is unknown or undefined. Custom applications always report unknown/undefined. |
| screenHeight | integer | The detected screen height of the device used for the user session. |
| screenOrientation | string | The detected screen orientation of the device used on the device for the user session. The element can hold these values * `LANDSCAPE` * `PORTRAIT` * `UNDEFINED` |
| screenWidth | integer | The detected screen width of the device used for the user session. |
| startTime | integer | The timestamp of the first user action in the user session, in UTC milliseconds. |
| stringProperties | [StringProperty](#openapi-definition-StringProperty)[] | A list of custom properties of the user session with string values. |
| syntheticEvents | [UserSessionSyntheticEvent](#openapi-definition-UserSessionSyntheticEvent)[] | A list of synthetic events recorded in the user session. |
| tenantId | string | The ID of the Dynatrace environment that captured the user session.  This field can not be queried via the User Session Query Language. |
| totalErrorCount | integer | The number of errors detected in the user session. |
| totalLicenseCreditCount | integer | Number of resulting billed sessions: [Dynatrace classic licensing﻿](https://dt-url.net/u24c0pga), [Dynatrace Platform Subscription﻿](https://www.dynatrace.com/support/help/shortlink/dps-dem). |
| userActionCount | integer | The number of user actions in the user session. |
| userActions | [UserSessionUserAction](#openapi-definition-UserSessionUserAction)[] | A list of user actions recorded in the user session. |
| userExperienceScore | string | The user experience score of the user session. The element can hold these values * `FRUSTRATED` * `SATISFIED` * `TOLERATED` * `UNDEFINED` |
| userId | string | The user ID provided for the user session by session tagging. |
| userSessionId | string | The unique ID of the user session. |
| userType | string | The type of the user. Indicates either a real human user (`REAL_USER`) or a robot (`ROBOT` or `SYNTHETIC`). The element can hold these values * `REAL_USER` * `ROBOT` * `SYNTHETIC` |

#### The `DateProperty` object

A custom property of the user-action with a date value.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The custom key of the property. |
| value | string | The date value of the property. |

#### The `DoubleProperty` object

A custom property of the user action with a Double value.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The custom key of the property. |
| value | number | The floating-point numeric value of the property. |

#### The `UserSessionErrors` object

The error of a user session.

| Element | Type | Description |
| --- | --- | --- |
| application | string | The name of the application, based on the configured detection rules. |
| domain | string | The DNS domain where the error has been recorded. |
| internalApplicationId | string | The Dynatrace entity ID of the application.  This information is useful when calling various REST APIs, for example, as a key for time series queries. |
| name | string | The name of the error. |
| startTime | integer | The timestamp of the error, in UTC milliseconds. |
| type | string | The type of error. The element can hold these values * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |

#### The `UserSessionEvents` object

The external event of a user session.

| Element | Type | Description |
| --- | --- | --- |
| application | string | The name of the application, based on the configured detection rules. |
| domain | string | The DNS domain where the event has been recorded. |
| internalApplicationId | string | The Dynatrace entity ID of the application.  This information is useful when calling various REST APIs, for example, as a key for time series queries. |
| metadata | string | The metadata attached to the event. |
| name | string | The name of the event. |
| page | string | The name of the page the user navigated to during a page change event. |
| pageGroup | string | The page group is automatically derived from the page. |
| pageReferrer | string | The name of the previous page from which the user navigated from during a page change event. |
| pageReferrerGroup | string | The page referrer group is automatically derived from the page referrer. |
| startTime | integer | The timestamp of the event, in UTC milliseconds. |
| type | string | The type of event. The element can hold these values * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |

#### The `LongProperty` object

A custom property of the user action with a Long value.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The custom key of the property. |
| value | integer | The Long value of the property. |

#### The `StringProperty` object

A custom property of the user action with a string value.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The custom key of the property. |
| value | string | The string value of the property. |

#### The `UserSessionSyntheticEvent` object

A synthetic event of a user session.

| Element | Type | Description |
| --- | --- | --- |
| errorCode | integer | The error code of the error that occurred during this event. |
| errorName | string | Description of the error that occurred during this event. |
| name | string | The name of the synthetic event. |
| sequenceNumber | integer | The sequence number of the synthetic event in scope of the complete browser monitor. |
| syntheticEventId | string | The Dynatrace entity ID for the synthetic event. |
| timestamp | integer | The timestamp when the synthetic event was simulated, in UTC milliseconds. |
| type | string | The type of the synthetic event. For example click or keystroke. |

#### The `UserSessionUserAction` object

A user action.

A user action is a single action performed by the user as part of a user session, for example a mouse click.

| Element | Type | Description |
| --- | --- | --- |
| apdexCategory | string | The [user experience index﻿](https://dt-url.net/apdexdoc) of the user action. The element can hold these values * `FRUSTRATED` * `SATISFIED` * `TOLERATING` * `UNKNOWN` |
| application | string | The name of the application where the user action has been recorded. |
| cdnBusyTime | integer | The time spent waiting for CDN resources for the user action, in milliseconds. |
| cdnResources | integer | The number of resources fetched from a CDN for the user action. |
| cumulativeLayoutShift | number | The cumulative layout shift (CLS) is the total amount of all individual scores for every unexpected layout shift that occurs during the entire lifespan of the page.  The CLS is an important user-centric metric for measuring visual stability. It quantifies how often users experience unexpected layout shifts. A low CLS indicates that the page is delightful. |
| customErrorCount | integer | The total number of custom errors during the user action. |
| dateProperties | [DateProperty](#openapi-definition-DateProperty)[] | A list of custom properties of the user session with date values. |
| documentInteractiveTime | integer | The amount of time spent until the document for the user action became interactive, in milliseconds. |
| domCompleteTime | integer | The amount of time until the DOM tree is completed, in milliseconds. |
| domContentLoadedTime | integer | The amount of time until the DOM tree is loaded, in milliseconds. |
| domain | string | The DNS domain where the user action has been recorded. |
| doubleProperties | [DoubleProperty](#openapi-definition-DoubleProperty)[] | A list of custom properties of the user session with floating-point numerical values. |
| duration | integer | The duration of the user action, in milliseconds.  This is calculated as the of time between the start and the end timestamps of the user action. |
| endTime | integer | The end timestamp of the user action, in UTC milliseconds. |
| firstInputDelay | integer | The first input delay (FID) is the time (in milliseconds) that the browser took to respond to the first user input.  The FID is an important user-centric metric for measuring load responsiveness. It quantifies the user experience when trying to interact with unresponsive pages. A low FID indicates that the page is usable. |
| firstPartyBusyTime | integer | The time spent waiting for resources from the originating server for the user action, in milliseconds. |
| firstPartyResources | integer | The number of resources fetched from the originating server for the user action. |
| frontendTime | integer | The amount of time spent on the frontend rendering for the user action, in milliseconds. |
| hasCrash | boolean | The user action has (`true`) or doesn't have (`false`) a crash. |
| internalApplicationId | string | The Dynatrace entity ID of the application where the user action has been recorded.  This information is useful when calling various REST APIs, for example as a key for time series queries. |
| internalKeyUserActionId | string | The Dynatrace entity ID of the key user action. |
| javascriptErrorCount | integer | The total number of Javascript errors during the user action. |
| keyUserAction | boolean | The action is (`true`) or is not (`false`) a key action. |
| largestContentfulPaint | integer | The largest contentful paint (LCP) is the time (in milliseconds) that the largest element on the page took to render.  The LCP is an important user-centric metric for measuring load speed. It marks the point when the page's main content is likely loaded. A low LCP indicates that the page loads quickly. |
| loadEventEnd | integer | The amount of time until the load event ended, in milliseconds. |
| loadEventStart | integer | The amount of time until the load event started, in milliseconds. |
| longProperties | [LongProperty](#openapi-definition-LongProperty)[] | A list of custom properties of the user session with integer (short or long) values. |
| matchingConversionGoals | string[] | A list of conversion goals achieved by the user action.  Additionally, you can define conversion goals for a user session as a whole. |
| name | string | The name of the user action.  Typically, this is the name of the page that is loaded as part of a user action or a textual description of the action, such as a mouse click. |
| navigationStart | integer | The timestamp of the navigation start, in UTC milliseconds. |
| networkTime | integer | The amount of time spent on the data transfer for the user action, in milliseconds. |
| requestErrorCount | integer | The total number of request errors during the user action. |
| requestStart | integer | The amount of time until the request started, in milliseconds. |
| responseEnd | integer | The amount of time until the response ended, in milliseconds. |
| responseStart | integer | The amount of time until the response started, in milliseconds. |
| serverTime | integer | The amount of time spent on the server-side processing for the user action, in milliseconds. |
| speedIndex | integer | The [speed index﻿](https://dt-url.net/qk1a3r19) of the user action, in milliseconds.  This is calculated as average time it takes for all visible parts of a page to display. |
| startTime | integer | The start timestamp of the user action, in UTC milliseconds. |
| stringProperties | [StringProperty](#openapi-definition-StringProperty)[] | A list of custom properties of the user session with string values. |
| syntheticEvent | string | The name of the [Synthetic event﻿](https://dt-url.net/dq1e3rmm) that triggered the user action. |
| syntheticEventId | string | The ID of the [Synthetic event﻿](https://dt-url.net/dq1e3rmm) that triggered the user action. |
| targetUrl | string | The target URL of the user action. |
| thirdPartyBusyTime | integer | The time spent waiting for third party resources for the user action, in milliseconds. |
| thirdPartyResources | integer | The number of third party resources loaded for the user action. |
| ~~totalBlockingTime~~ | integer | DEPRECATED  The total blocking time is the total time (in milliseconds) between the first contentful paint and the time to interactive, during which the browser has been blocked long enough to prevent input responsiveness. |
| type | string | The type of the user action. The element can hold these values * `Custom` * `EndVisit` * `Error` * `Load` * `RageClick` * `SyntheticHiddenAction` * `UserSessionProperties` * `VisitTag` * `Xhr` |
| userActionPropertyCount | integer | The total number of properties in the user action. |
| visuallyCompleteTime | integer | The amount of time until the page is [visually complete﻿](https://dt-url.net/qk1a3r19), in milliseconds. |

## Related topics

* [Custom queries, segmentation, and aggregation of session data in RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")