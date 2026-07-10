---
title: Web application configuration API - PUT default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration
---

# Web application configuration API - PUT default application

# Web application configuration API - PUT default application

* Reference
* Published Sep 03, 2019

Updates the default web application of your Dynatrace environment.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | JSON body of the request, containing the new parameters of the default web application. | body | Optional |

### Request body objects

#### The `WebApplicationConfig` object

Configuration of a web application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | A list of conversion goals of the application. | Optional |
| costControlUserSessionPercentage | number | Analize *X*% of user sessions. | Required |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. | Required |
| identifier | string | Dynatrace entity ID of the web application. | Optional |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. | Required |
| loadActionKeyPerformanceMetric | string | The key performance metric of load actions. The element can hold these values * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` | Required |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Java script agent meta data capture settings. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Real user monitoring settings. | Required |
| name | string | The name of the web application, displayed in the UI. | Required |
| realUserMonitoringEnabled | boolean | Real user monitoring enabled/disabled. | Required |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Session replay settings | Optional |
| type | string | The type of the web application. The element can hold these values * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` | Optional |
| urlInjectionPattern | string | Url injection pattern for manual web application. | Optional |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | User action and session properties settings. Empty List means no change | Optional |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | The settings of user action naming. | Optional |
| userTags | [UserTag](#openapi-definition-UserTag)[] | User tags settings. | Optional |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources. | Required |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. | Required |
| xhrActionKeyPerformanceMetric | string | The key performance metric of XHR actions. The element can hold these values * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` | Required |

#### The `ConversionGoal` object

A conversion goal of the application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Configuration of a destination-based conversion goal. | Optional |
| id | string | The ID of conversion goal.  Omit it while creating a new conversion goal. | Optional |
| name | string | The name of the conversion goal. | Required |
| type | string | The type of the conversion goal. The element can hold these values * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` | Optional |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Configuration of a user action-based conversion goal. | Optional |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Configuration of a visit duration-based conversion goal. | Optional |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Configuration of a number of user actions-based conversion goal. | Optional |

#### The `DestinationDetails` object

Configuration of a destination-based conversion goal.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| caseSensitive | boolean | The match is case-sensitive (`true`) or (`false`). | Optional |
| matchType | string | The operator of the match. The element can hold these values * `Begins` * `Contains` * `Ends` | Optional |
| urlOrPath | string | The path to be reached to hit the conversion goal. | Required |

#### The `UserActionDetails` object

Configuration of a user action-based conversion goal.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| actionType | string | Type of the action to which the rule applies. The element can hold these values * `Custom` * `Load` * `Xhr` | Optional |
| caseSensitive | boolean | The match is case-sensitive (`true`) or (`false`). | Optional |
| matchEntity | string | The type of the entity to which the rule applies. The element can hold these values * `ActionName` * `PageUrl` | Optional |
| matchType | string | The operator of the match. The element can hold these values * `Begins` * `Contains` * `Ends` | Optional |
| value | string | The value to be matched to hit the conversion goal. | Optional |

#### The `VisitDurationDetails` object

Configuration of a visit duration-based conversion goal.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| durationInMillis | integer | The duration of session to hit the conversion goal, in milliseconds. | Required |

#### The `VisitNumActionDetails` object

Configuration of a number of user actions-based conversion goal.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| numUserActions | integer | The number of user actions to hit the conversion goal. | Optional |

#### The `Apdex` object

Defines the Apdex settings of an application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| frustratingFallbackThreshold | number | Fallback threshold of an XHR action, defining a tolerable user experience, when the configured KPM is not available. | Optional |
| frustratingThreshold | number | Maximal value of apdex, which is considered as tolerable user experience. | Optional |
| toleratedFallbackThreshold | number | Fallback threshold of an XHR action, defining a satisfied user experience, when the configured KPM is not available. | Optional |
| toleratedThreshold | number | Maximal value of apdex, which is considered as satisfied user experience. | Optional |

#### The `MetaDataCapturing` object

Configuration to capture meta data with the Javascript agent. The captured metadata can be referenced by its uniqueId in UserTags, UserActionAndSessionProperties or UserActionNamingPlaceholder

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| capturingName | string | The name of the meta data to capture. | Required |
| name | string | Name for displaying the captured values in Dynatrace. | Required |
| publicMetadata | boolean | True if this metadata should be captured regardless of the privacy settings | Optional |
| type | string | The type of the meta data to capture. The element can hold these values * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` | Required |
| uniqueId | integer | The unique id of the meta data to capture. | Optional |
| useLastValue | boolean | True if the last captured value should be used for this metadata. By default the first value will be used. | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `MonitoringSettings` object

Real user monitoring settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Add the cross origin = anonymous attribute to capture JavaScript error messages and W3C resource timings. | Optional |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Advanced JavaScript tag settings. | Required |
| angularPackageName | string | The name of the angular package. | Optional |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode. | Optional |
| cacheControlHeaderOptimizations | boolean | Optimize the value of cache control headers for use with Dynatrace real user monitoring enabled/disabled. | Required |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Settings for content capture. | Required |
| cookiePlacementDomain | string | Domain for cookie placement. | Optional |
| correlationHeaderInclusionRegex | string | To enable RUM for XHR calls to AWS Lambda, define a regular expression matching these calls, Dynatrace can then automatically add a custom header (x-dtc) to each such request to the respective endpoints in AWS.  Important: These endpoints must accept the x-dtc header, or the requests will fail. | Optional |
| customConfigurationProperties | string | Additional JavaScript tag properties that are specific to your application. To do this, type key=value pairs separated using a (|) symbol. | Required |
| excludeXhrRegex | string | You can exclude some actions from becoming XHR actions.  Put a regular expression, matching all the required URLs, here.  If noting specified the feature is disabled. | Required |
| fetchRequests | boolean | `fetch()` request capture enabled/disabled. | Required |
| injectionMode | string | JavaScript injection mode. The element can hold these values * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` | Required |
| instrumentedWebServer | boolean | Instrumented web or app server. | Optional |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode. | Optional |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Support of various JavaScript frameworks. | Required |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Java script injection rules. | Optional |
| libraryFileFromCdn | boolean | Get the JavaScript library file from the CDN.  Not supported by agentless applications and assumed to be false for auto-injected applications if omitted. | Optional |
| libraryFileLocation | string | The location of your application’s custom JavaScript library file.  If nothing specified the root directory of your web server is used.  **Required** for auto-injected applications, not supported by agentless applications. | Optional |
| monitoringDataPath | string | The location to send monitoring data from the JavaScript tag.  Specify either a relative or an absolute URL. If you use an absolute URL, data will be sent using CORS.  **Required** for auto-injected applications, optional for agentless applications. | Optional |
| sameSiteCookieAttribute | string | Same site cookie attribute The element can hold these values * `LAX` * `NONE` * `STRICT` | Optional |
| scriptTagCacheDurationInHours | integer | Time duration for the cache settings. | Optional |
| secureCookieAttribute | boolean | Secure attribute usage for Dynatrace cookies enabled/disabled. | Required |
| serverRequestPathId | string | Path to identify the server’s request ID. | Required |
| useCors | boolean | Send beacon data via CORS. | Optional |
| xmlHttpRequest | boolean | `XmlHttpRequest` support enabled/disabled. | Required |

#### The `AdvancedJavaScriptTagSettings` object

Advanced JavaScript tag settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Additional event handlers and wrappers. | Required |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page. | Required |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Global event capture settings. | Required |
| instrumentUnsupportedAjaxFrameworks | boolean | Instrumentation of unsupported Ajax frameworks enabled/disabled. | Required |
| maxActionNameLength | integer | Maximum character length for action names. Valid values range from 5 to 10000. | Required |
| maxErrorsToCapture | integer | Maximum number of errors to be captured per page. Valid values range from 0 to 50. | Required |
| proxyWrapperEnabled | boolean | Proxy wrapper enabled/disabled. | Optional |
| specialCharactersToEscape | string | Additional special characters that are to be escaped using non-alphanumeric characters in HTML escape format. | Required |
| syncBeaconFirefox | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Firefox enabled/disabled. | Optional |
| syncBeaconInternetExplorer | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Internet Explorer enabled/disabled. | Optional |
| userActionNameAttribute | string | User action name attribute. | Optional |

#### The `AdditionalEventHandlers` object

Additional event handlers and wrappers.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| blurEventHandler | boolean | Blur event handler enabled/disabled. | Required |
| changeEventHandler | boolean | Change event handler enabled/disabled. | Required |
| clickEventHandler | boolean | Click event handler enabled/disabled. | Required |
| maxDomNodesToInstrument | integer | Max. number of DOM nodes to instrument. Valid values range from 0 to 100000. | Required |
| mouseupEventHandler | boolean | Mouseup event handler enabled/disabled. | Required |
| toStringMethod | boolean | toString method enabled/disabled. | Required |
| userMouseupEventForClicks | boolean | Use mouseup event for clicks enabled/disabled. | Required |

#### The `EventWrapperSettings` object

In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| blur | boolean | Blur enabled/disabled. | Required |
| change | boolean | Change enabled/disabled. | Required |
| click | boolean | Click enabled/disabled. | Required |
| mouseUp | boolean | MouseUp enabled/disabled. | Required |
| touchEnd | boolean | TouchEnd enabled/disabled. | Required |
| touchStart | boolean | TouchStart enabled/disabled. | Required |

#### The `GlobalEventCaptureSettings` object

Global event capture settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Additional events to be captured globally as user input.  For example, DragStart or DragEnd. | Required |
| change | boolean | Change enabled/disabled. | Optional |
| click | boolean | Click enabled/disabled. | Required |
| doubleClick | boolean | DoubleClick enabled/disabled. | Required |
| keyDown | boolean | KeyDown enabled/disabled. | Required |
| keyUp | boolean | KeyUp enabled/disabled. | Required |
| mouseDown | boolean | MouseDown enabled/disabled. | Required |
| mouseUp | boolean | MouseUp enabled/disabled. | Required |
| scroll | boolean | Scroll enabled/disabled. | Required |
| touchEnd | boolean | TouchEnd enabled/disabled. | Optional |
| touchStart | boolean | TouchStart enabled/disabled. | Optional |

#### The `WebApplicationConfigBrowserRestrictionSettings` object

Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | A list of browser restrictions. | Optional |
| mode | string | The mode of the list of browser restrictions. The element can hold these values * `EXCLUDE` * `INCLUDE` | Required |

#### The `WebApplicationConfigBrowserRestriction` object

Browser exclusion rules for the browsers that are to be excluded.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| browserType | string | The type of the browser that is used. The element can hold these values * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` | Required |
| browserVersion | string | The version of the browser that is used. | Optional |
| comparator | string | Compares different browsers together. The element can hold these values * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` | Optional |
| platform | string | The platform on which the browser is being used. The element can hold these values * `ALL` * `DESKTOP` * `MOBILE` | Optional |

#### The `ContentCapture` object

Settings for content capture.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| javaScriptErrors | boolean | JavaScript errors monitoring enabled/disabled. | Required |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Settings for resource timings capture. | Required |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Settings for timed action capture. | Required |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Settings for VisuallyComplete2 | Optional |
| visuallyCompleteAndSpeedIndex | boolean | Visually complete and Speed index support enabled/disabled. | Required |

#### The `ResourceTimingSettings` object

Settings for resource timings capture.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| nonW3cResourceTimings | boolean | Timing for JavaScript files and images on non-W3C supported browsers enabled/disabled. | Required |
| nonW3cResourceTimingsInstrumentationDelay | integer | Instrumentation delay for monitoring resource and image resource impact in browsers that don't offer W3C resource timings.  Valid values range from 0 to 9999.  Only effective if **nonW3cResourceTimings** is enabled. | Required |
| resourceTimingCaptureType | string | Defines how detailed resource timings are captured.  Only effective if **w3cResourceTimings** or **nonW3cResourceTimings** is enabled. The element can hold these values * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` | Optional |
| resourceTimingsDomainLimit | integer | Limits the number of domains for which W3C resource timings are captured.  Only effective if **resourceTimingCaptureType** is `CAPTURE_LIMITED_SUMMARIES`. | Optional |
| w3cResourceTimings | boolean | W3C resource timings for third party/CDN enabled/disabled. | Required |

#### The `TimeoutSettings` object

Settings for timed action capture.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Defines how deep temporary actions may cascade. 0 disables temporary actions completely. Recommended value if enabled is 3. | Required |
| temporaryActionTotalTimeout | integer | The total timeout of all cascaded timeouts that should still be able to create a temporary action | Required |
| timedActionSupport | boolean | Timed action support enabled/disabled.  Enable to detect actions that trigger sending of XHRs via *setTimout* methods. | Required |

#### The `VisuallyComplete2Settings` object

Settings for VisuallyComplete2

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| excludeUrlRegex | string | A RegularExpression used to exclude images and iframes from being detected by the VC module. | Optional |
| ignoredMutationsList | string | Query selector for mutation nodes to ignore in VC and SI calculation | Optional |
| inactivityTimeout | integer | The time in ms the VC module waits for no mutations happening on the page after the load action. Defaults to 1000. | Optional |
| mutationTimeout | integer | Determines the time in ms VC waits after an action closes to start calculation. Defaults to 50. | Optional |
| threshold | integer | Minimum visible area in pixels of elements to be counted towards VC and SI. Defaults to 50. | Optional |

#### The `WebApplicationConfigIpAddressRestrictionSettings` object

Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - | Optional |
| mode | string | The mode of the list of ip address restrictions. The element can hold these values * `EXCLUDE` * `INCLUDE` | Required |

#### The `IpAddressRange` object

The IP address or the IP address range to be mapped to the location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| address | string | The IP address to be mapped.  For an IP address range, this is the **from** address. | Required |
| addressTo | string | The **to** address of the IP address range. | Optional |
| subnetMask | integer | The subnet mask of the IP address range. | Optional |

#### The `JavaScriptFrameworkSupport` object

Support of various JavaScript frameworks.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeXObject | boolean | ActiveXObject detection support enabled/disabled. | Required |
| angular | boolean | AngularJS and Angular support enabled/disabled. | Required |
| dojo | boolean | Dojo support enabled/disabled. | Required |
| extJS | boolean | ExtJS, Sencha Touch support enabled/disabled. | Required |
| icefaces | boolean | ICEfaces support enabled/disabled. | Required |
| jQuery | boolean | jQuery, Backbone.js support enabled/disabled. | Required |
| mooTools | boolean | MooTools support enabled/disabled. | Required |
| prototype | boolean | Prototype support enabled/disabled. | Required |

#### The `JavaScriptInjectionRules` object

Rules for javascript injection

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The enable or disable rule of the java script injection. | Required |
| htmlPattern | string | The html pattern of the java script injection. | Optional |
| rule | string | The url rule of the java script injection. The element can hold these values * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` | Required |
| target | string | The target against which the rule of the java script injection should be matched. The element can hold these values * `PAGE_QUERY` * `URL` | Optional |
| urlOperator | string | The url operator of the java script injection. The element can hold these values * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| urlPattern | string | The url pattern of the java script injection. | Optional |

#### The `SessionReplaySetting` object

Session replay settings

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| costControlPercentage | integer | Session replay sampling rating in percentage. | Required |
| cssResourceCapturingExclusionRules | string[] | A list of URLs to be excluded from CSS resource capturing. | Optional |
| enableCssResourceCapturing | boolean | Capture (`true`) or don't capture (`false`) CSS resources from the session. | Optional |
| enabled | boolean | SessionReplay Enabled. | Required |

#### The `UserActionAndSessionProperties` object

Defines userAction and session custom defined properties settings of an application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | The aggregation type of the property.  It defines how multiple values of the property are aggregated. The element can hold these values * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` | Optional |
| cleanupRule | string | The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expression﻿](https://dt-url.net/k9e0iaq?dt=m) for the data you need there. | Optional |
| displayName | string | The display name of the property. | Optional |
| ignoreCase | boolean | If true, the value of this property will always be stored in lower case. Defaults to false. | Optional |
| key | string | Key of the property | Required |
| longStringLength | integer | If the type is LONG\_STRING, the max length for this property. Must be a multiple of 100. Defaults to 200. | Optional |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig.Must be set if "origin" is of type META\_DATA. | Optional |
| origin | string | The origin of the property The element can hold these values * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` | Required |
| serverSideRequestAttribute | string | The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`. | Optional |
| storeAsSessionProperty | boolean | If `true`, the property is stored as a session property | Optional |
| storeAsUserActionProperty | boolean | If `true`, the property is stored as a user action property | Optional |
| type | string | The data type of the property. The element can hold these values * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` | Required |
| uniqueId | integer | Unique id among all userTags and properties of this application | Required |

#### The `UserActionNamingSettings` object

The settings of user action naming.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for custom actions. | Optional |
| ignoreCase | boolean | Case insensitive naming. | Optional |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for loading actions. | Optional |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | User action placeholders. | Optional |
| queryParameterCleanups | string[] | List of parameters that should be removed from the query before using the query in the user action name. | Optional |
| splitUserActionsByDomain | boolean | Deactivate this setting if different domains should not result in separate user actions. | Optional |
| useFirstDetectedLoadAction | boolean | First load action found under an XHR action should be used when true. Else the deepest one under the xhr action is used | Optional |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for xhr actions. | Optional |

#### The `UserActionNamingRule` object

The settings of naming rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Defines the conditions when the naming rule should apply. | Optional |
| template | string | Naming pattern. Use Curly brackets `{}` to select placeholders. | Required |
| useOrConditions | boolean | If set to `true` the conditions will be connected by logical OR instead of logical AND. | Optional |

#### The `UserActionNamingRuleCondition` object

The settings of conditions for user action naming.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| operand1 | string | Must be a defined placeholder wrapped in curly braces | Required |
| operand2 | string | Must be null if operator is "IS\_EMPTY", a regex if operator is "MATCHES\_REGULAR\_ERPRESSION". In all other cases the value can be a freetext or a placeholder wrapped in curly braces | Optional |
| operator | string | The operator of the condition The element can hold these values * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` | Required |

#### The `UserActionNamingPlaceholder` object

The placeholder settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| input | string | Input. The element can hold these values * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` | Required |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if "Input" is of type METADATA. | Optional |
| name | string | Placeholder name. | Required |
| processingPart | string | Part. The element can hold these values * `ALL` * `ANCHOR` * `PATH` | Required |
| processingSteps | [UserActionNamingPlaceholderProcessingStep](#openapi-definition-UserActionNamingPlaceholderProcessingStep)[] | Processing actions. | Optional |
| useGuessedElementIdentifier | boolean | Use the element identifier that was selected by Dynatrace. | Required |

#### The `UserActionNamingPlaceholderProcessingStep` object

The processing step settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| fallbackToInput | boolean | If set to true: Returns the input if **patternBefore** or **patternAfter** cannot be found and the **type** is `SUBSTRING`.  Returns the input if **regularExpression** doesn't match and **type** is `EXTRACT_BY_REGULAR_EXPRESSION`.  Otherwise null is returned. | Optional |
| patternAfter | string | The pattern after the required value. It will be removed. | Optional |
| patternAfterSearchType | string | The required occurrence of **patternAfter**. The element can hold these values * `FIRST` * `LAST` | Optional |
| patternBefore | string | The pattern before the required value. It will be removed. | Optional |
| patternBeforeSearchType | string | The required occurrence of **patternBefore**. The element can hold these values * `FIRST` * `LAST` | Optional |
| patternToReplace | string | The pattern to be replaced.  Only applicable if the **type** is `REPLACE_WITH_PATTERN`. | Optional |
| regularExpression | string | A regular expression for the string to be extracted or replaced.  Only applicable if the **type** is `EXTRACT_BY_REGULAR_EXPRESSION` or `REPLACE_WITH_REGULAR_EXPRESSION`. | Optional |
| replacement | string | Replacement for the original value. | Optional |
| type | string | An action to be taken by the processing:  * `SUBSTRING`: Extracts the string between **patternBefore** and **patternAfter**. * `REPLACEMENT`: Replaces the string between **patternBefore** and **patternAfter** with the specified **replacement**. * `REPLACE_WITH_PATTERN`: Replaces the **patternToReplace** with the specified **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: Extracts the part of the string that matches the **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: Replaces all occurrences that match **regularExpression** with the specified **replacement**. * `REPLACE_IDS`: Replaces all IDs and UUIDs with the specified **replacement**. The element can hold these values * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` | Required |

#### The `UserTag` object

Defines UserTags settings of an application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| cleanupRule | string | Cleanup rule expression of the userTag | Optional |
| ignoreCase | boolean | If true, the value of this tag will always be stored in lower case. Defaults to false. | Optional |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if the UserTag is based on metadata captured by the Javascript agent (e.g. a Javascript variable, CSS selector, etc.) | Optional |
| serverSideRequestAttribute | string | Serverside request attribute id of the userTag. Must be set if the UserTag is based on a serverside request attribute. | Optional |
| uniqueId | integer | uniqueId, unique among all userTags and properties of this application | Required |

#### The `WaterfallSettings` object

These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Warn about resources with a lower browser cache rate above *X*%. | Required |
| resourcesThreshold | integer | Warn about resources larger than *X* bytes. | Required |
| slowCdnResourcesThreshold | integer | Warn about slow CDN resources with a response time above *X* ms. | Required |
| slowFirstPartyResourcesThreshold | integer | Warn about slow 1st party resources with a response time above *X* ms. | Required |
| slowThirdPartyResourcesThreshold | integer | Warn about slow 3rd party resources with a response time above *X* ms. | Required |
| speedIndexVisuallyCompleteRatioThreshold | integer | Warn if Speed index exceeds *X* % of Visually complete. | Required |
| uncompressedResourcesThreshold | integer | Warn about uncompressed resources larger than *X* bytes. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"conversionGoals": [



{



"destinationDetails": {



"caseSensitive": false,



"matchType": "Begins",



"urlOrPath": "url or path"



},



"name": "conversionGoalName",



"type": "UserAction",



"userActionDetails": {



"actionType": "Load",



"caseSensitive": true,



"matchEntity": "ActionName",



"matchType": "Ends",



"value": "value to match"



},



"visitDurationDetails": {



"durationInMillis": 1



},



"visitNumActionDetails": {



"numUserActions": 2



}



}



],



"costControlUserSessionPercentage": 100,



"customActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 12000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 3000



},



"loadActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 12000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 3000



},



"loadActionKeyPerformanceMetric": "VISUALLY_COMPLETE",



"metaDataCaptureSettings": [



{



"capturingName": "variableName",



"name": "display name",



"type": "JAVA_SCRIPT_VARIABLE"



}



],



"monitoringSettings": {



"advancedJavaScriptTagSettings": {



"additionalEventHandlers": {



"blurEventHandler": false,



"changeEventHandler": false,



"clickEventHandler": false,



"maxDomNodesToInstrument": 5000,



"mouseupEventHandler": false,



"toStringMethod": false,



"userMouseupEventForClicks": false



},



"eventWrapperSettings": {



"blur": false,



"change": false,



"click": false,



"mouseUp": false,



"touchEnd": false,



"touchStart": false



},



"globalEventCaptureSettings": {



"additionalEventCapturedAsUserInput": "",



"click": true,



"doubleClick": true,



"keyDown": true,



"keyUp": true,



"mouseDown": true,



"mouseUp": true,



"scroll": true



},



"instrumentUnsupportedAjaxFrameworks": false,



"maxActionNameLength": 100,



"maxErrorsToCapture": 10,



"specialCharactersToEscape": "",



"syncBeaconFirefox": false,



"syncBeaconInternetExplorer": false



},



"browserRestrictionSettings": {



"browserRestrictions": [



{



"browserType": "INTERNET_EXPLORER",



"browserVersion": "0",



"comparator": "EQUALS",



"platform": "ALL"



}



],



"mode": "EXCLUDE"



},



"cacheControlHeaderOptimizations": true,



"contentCapture": {



"javaScriptErrors": true,



"resourceTimingSettings": {



"nonW3cResourceTimings": false,



"nonW3cResourceTimingsInstrumentationDelay": 50,



"w3cResourceTimings": true



},



"timeoutSettings": {



"temporaryActionLimit": 0,



"temporaryActionTotalTimeout": 100,



"timedActionSupport": false



},



"visuallyCompleteAndSpeedIndex": true



},



"cookiePlacementDomain": "",



"correlationHeaderInclusionRegex": "",



"customConfigurationProperties": "",



"excludeXhrRegex": "",



"fetchRequests": true,



"injectionMode": "JAVASCRIPT_TAG",



"ipAddressRestrictionSettings": {



"ipAddressRestrictions": [



{



"address": "10.0.0.1",



"subnetMask": 3



},



{



"address": "10.0.0.1",



"addressTo": "10.0.0.2"



}



],



"mode": "EXCLUDE"



},



"javaScriptFrameworkSupport": {



"activeXObject": false,



"angular": true,



"dojo": false,



"extJS": false,



"icefaces": false,



"jQuery": true,



"mooTools": false,



"prototype": true



},



"javaScriptInjectionRules": [



{



"enabled": true,



"htmlPattern": "</title>",



"rule": "AFTER_SPECIFIC_HTML",



"urlOperator": "CONTAINS",



"urlPattern": "/lorem/ipsum.jsp"



}



],



"libraryFileLocation": "",



"monitoringDataPath": "",



"secureCookieAttribute": false,



"serverRequestPathId": "",



"xmlHttpRequest": true



},



"name": "application name",



"realUserMonitoringEnabled": true,



"sessionReplayConfig": {



"costControlPercentage": 100,



"cssResourceCapturingExclusionRules": [



"rule"



],



"enableCssResourceCapturing": true,



"enabled": true



},



"type": "AUTO_INJECTED",



"userActionNamingSettings": {



"ignoreCase": true,



"loadActionNamingRules": [



{



"conditions": [



{



"operand1": "{myPlaceholder}",



"operand2": "foo",



"operator": "CONTAINS"



}



],



"template": "Loading of {myPlaceholder}"



}



],



"placeholders": [



{



"input": "PAGE_URL",



"name": "myPlaceholder",



"processingPart": "ALL",



"processingSteps": [



{



"patternAfter": ".*a",



"patternAfterSearchType": "LAST",



"patternBefore": ".*b",



"patternBeforeSearchType": "FIRST",



"replacement": "value",



"type": "SUBSTRING"



}



],



"useGuessedElementIdentifier": false



}



],



"splitUserActionsByDomain": true,



"xhrActionNamingRules": [



{



"conditions": [



{



"operand1": "{myPlaceholder}",



"operand2": "foo",



"operator": "CONTAINS"



}



],



"template": "Loading of {myPlaceholder}"



}



]



},



"waterfallSettings": {



"resourceBrowserCachingThreshold": 50,



"resourcesThreshold": 100000,



"slowCdnResourcesThreshold": 200000,



"slowFirstPartyResourcesThreshold": 200000,



"slowThirdPartyResourcesThreshold": 200000,



"speedIndexVisuallyCompleteRatioThreshold": 50,



"uncompressedResourcesThreshold": 860



},



"xhrActionApdexSettings": {



"frustratingFallbackThreshold": 12000,



"frustratingThreshold": 10000,



"toleratedFallbackThreshold": 3000,



"toleratedThreshold": 2500



},



"xhrActionKeyPerformanceMetric": "ACTION_DURATION"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```