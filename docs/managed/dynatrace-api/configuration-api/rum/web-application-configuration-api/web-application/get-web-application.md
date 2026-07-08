---
title: Web application configuration API - GET a web application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application
---

# Web application configuration API - GET a web application

# Web application configuration API - GET a web application

* Reference
* Published Sep 03, 2019

Gets parameters of the specified web application.

This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the requested web application. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [WebApplicationConfig](#openapi-definition-WebApplicationConfig) | Success |

### Response body objects

#### The `WebApplicationConfig` object

Configuration of a web application.

| Element | Type | Description |
| --- | --- | --- |
| conversionGoals | [ConversionGoal](#openapi-definition-ConversionGoal)[] | A list of conversion goals of the application. |
| costControlUserSessionPercentage | number | Analize *X*% of user sessions. |
| customActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. |
| identifier | string | Dynatrace entity ID of the web application. |
| loadActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. |
| loadActionKeyPerformanceMetric | string | The key performance metric of load actions. The element can hold these values * `ACTION_DURATION` * `CUMULATIVE_LAYOUT_SHIFT` * `DOM_INTERACTIVE` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `SPEED_INDEX` * `VISUALLY_COMPLETE` |
| metaDataCaptureSettings | [MetaDataCapturing](#openapi-definition-MetaDataCapturing)[] | Java script agent meta data capture settings. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| monitoringSettings | [MonitoringSettings](#openapi-definition-MonitoringSettings) | Real user monitoring settings. |
| name | string | The name of the web application, displayed in the UI. |
| realUserMonitoringEnabled | boolean | Real user monitoring enabled/disabled. |
| sessionReplayConfig | [SessionReplaySetting](#openapi-definition-SessionReplaySetting) | Session replay settings |
| type | string | The type of the web application. The element can hold these values * `AUTO_INJECTED` * `BROWSER_EXTENSION_INJECTED` * `MANUALLY_INJECTED` |
| urlInjectionPattern | string | Url injection pattern for manual web application. |
| userActionAndSessionProperties | [UserActionAndSessionProperties](#openapi-definition-UserActionAndSessionProperties)[] | User action and session properties settings. Empty List means no change |
| userActionNamingSettings | [UserActionNamingSettings](#openapi-definition-UserActionNamingSettings) | The settings of user action naming. |
| userTags | [UserTag](#openapi-definition-UserTag)[] | User tags settings. |
| waterfallSettings | [WaterfallSettings](#openapi-definition-WaterfallSettings) | These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources. |
| xhrActionApdexSettings | [Apdex](#openapi-definition-Apdex) | Defines the Apdex settings of an application. |
| xhrActionKeyPerformanceMetric | string | The key performance metric of XHR actions. The element can hold these values * `ACTION_DURATION` * `RESPONSE_END` * `RESPONSE_START` * `VISUALLY_COMPLETE` |

#### The `ConversionGoal` object

A conversion goal of the application.

| Element | Type | Description |
| --- | --- | --- |
| destinationDetails | [DestinationDetails](#openapi-definition-DestinationDetails) | Configuration of a destination-based conversion goal. |
| id | string | The ID of conversion goal.  Omit it while creating a new conversion goal. |
| name | string | The name of the conversion goal. |
| type | string | The type of the conversion goal. The element can hold these values * `Destination` * `UserAction` * `VisitDuration` * `VisitNumActions` |
| userActionDetails | [UserActionDetails](#openapi-definition-UserActionDetails) | Configuration of a user action-based conversion goal. |
| visitDurationDetails | [VisitDurationDetails](#openapi-definition-VisitDurationDetails) | Configuration of a visit duration-based conversion goal. |
| visitNumActionDetails | [VisitNumActionDetails](#openapi-definition-VisitNumActionDetails) | Configuration of a number of user actions-based conversion goal. |

#### The `DestinationDetails` object

Configuration of a destination-based conversion goal.

| Element | Type | Description |
| --- | --- | --- |
| caseSensitive | boolean | The match is case-sensitive (`true`) or (`false`). |
| matchType | string | The operator of the match. The element can hold these values * `Begins` * `Contains` * `Ends` |
| urlOrPath | string | The path to be reached to hit the conversion goal. |

#### The `UserActionDetails` object

Configuration of a user action-based conversion goal.

| Element | Type | Description |
| --- | --- | --- |
| actionType | string | Type of the action to which the rule applies. The element can hold these values * `Custom` * `Load` * `Xhr` |
| caseSensitive | boolean | The match is case-sensitive (`true`) or (`false`). |
| matchEntity | string | The type of the entity to which the rule applies. The element can hold these values * `ActionName` * `PageUrl` |
| matchType | string | The operator of the match. The element can hold these values * `Begins` * `Contains` * `Ends` |
| value | string | The value to be matched to hit the conversion goal. |

#### The `VisitDurationDetails` object

Configuration of a visit duration-based conversion goal.

| Element | Type | Description |
| --- | --- | --- |
| durationInMillis | integer | The duration of session to hit the conversion goal, in milliseconds. |

#### The `VisitNumActionDetails` object

Configuration of a number of user actions-based conversion goal.

| Element | Type | Description |
| --- | --- | --- |
| numUserActions | integer | The number of user actions to hit the conversion goal. |

#### The `Apdex` object

Defines the Apdex settings of an application.

| Element | Type | Description |
| --- | --- | --- |
| frustratingFallbackThreshold | number | Fallback threshold of an XHR action, defining a tolerable user experience, when the configured KPM is not available. |
| frustratingThreshold | number | Maximal value of apdex, which is considered as tolerable user experience. |
| toleratedFallbackThreshold | number | Fallback threshold of an XHR action, defining a satisfied user experience, when the configured KPM is not available. |
| toleratedThreshold | number | Maximal value of apdex, which is considered as satisfied user experience. |

#### The `MetaDataCapturing` object

Configuration to capture meta data with the Javascript agent. The captured metadata can be referenced by its uniqueId in UserTags, UserActionAndSessionProperties or UserActionNamingPlaceholder

| Element | Type | Description |
| --- | --- | --- |
| capturingName | string | The name of the meta data to capture. |
| name | string | Name for displaying the captured values in Dynatrace. |
| publicMetadata | boolean | True if this metadata should be captured regardless of the privacy settings |
| type | string | The type of the meta data to capture. The element can hold these values * `COOKIE` * `CSS_SELECTOR` * `JAVA_SCRIPT_FUNCTION` * `JAVA_SCRIPT_VARIABLE` * `META_TAG` * `QUERY_STRING` * `RESPONSE_HEADER` |
| uniqueId | integer | The unique id of the meta data to capture. |
| useLastValue | boolean | True if the last captured value should be used for this metadata. By default the first value will be used. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `MonitoringSettings` object

Real user monitoring settings.

| Element | Type | Description |
| --- | --- | --- |
| addCrossOriginAnonymousAttribute | boolean | Add the cross origin = anonymous attribute to capture JavaScript error messages and W3C resource timings. |
| advancedJavaScriptTagSettings | [AdvancedJavaScriptTagSettings](#openapi-definition-AdvancedJavaScriptTagSettings) | Advanced JavaScript tag settings. |
| angularPackageName | string | The name of the angular package. |
| browserRestrictionSettings | [WebApplicationConfigBrowserRestrictionSettings](#openapi-definition-WebApplicationConfigBrowserRestrictionSettings) | Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode. |
| cacheControlHeaderOptimizations | boolean | Optimize the value of cache control headers for use with Dynatrace real user monitoring enabled/disabled. |
| contentCapture | [ContentCapture](#openapi-definition-ContentCapture) | Settings for content capture. |
| cookiePlacementDomain | string | Domain for cookie placement. |
| correlationHeaderInclusionRegex | string | To enable RUM for XHR calls to AWS Lambda, define a regular expression matching these calls, Dynatrace can then automatically add a custom header (x-dtc) to each such request to the respective endpoints in AWS.  Important: These endpoints must accept the x-dtc header, or the requests will fail. |
| customConfigurationProperties | string | Additional JavaScript tag properties that are specific to your application. To do this, type key=value pairs separated using a (|) symbol. |
| excludeXhrRegex | string | You can exclude some actions from becoming XHR actions.  Put a regular expression, matching all the required URLs, here.  If noting specified the feature is disabled. |
| fetchRequests | boolean | `fetch()` request capture enabled/disabled. |
| injectionMode | string | JavaScript injection mode. The element can hold these values * `CODE_SNIPPET` * `CODE_SNIPPET_ASYNC` * `INLINE_CODE` * `JAVASCRIPT_TAG` * `JAVASCRIPT_TAG_COMPLETE` * `JAVASCRIPT_TAG_SRI` |
| instrumentedWebServer | boolean | Instrumented web or app server. |
| ipAddressRestrictionSettings | [WebApplicationConfigIpAddressRestrictionSettings](#openapi-definition-WebApplicationConfigIpAddressRestrictionSettings) | Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode. |
| javaScriptFrameworkSupport | [JavaScriptFrameworkSupport](#openapi-definition-JavaScriptFrameworkSupport) | Support of various JavaScript frameworks. |
| javaScriptInjectionRules | [JavaScriptInjectionRules](#openapi-definition-JavaScriptInjectionRules)[] | Java script injection rules. |
| libraryFileFromCdn | boolean | Get the JavaScript library file from the CDN.  Not supported by agentless applications and assumed to be false for auto-injected applications if omitted. |
| libraryFileLocation | string | The location of your application’s custom JavaScript library file.  If nothing specified the root directory of your web server is used.  **Required** for auto-injected applications, not supported by agentless applications. |
| monitoringDataPath | string | The location to send monitoring data from the JavaScript tag.  Specify either a relative or an absolute URL. If you use an absolute URL, data will be sent using CORS.  **Required** for auto-injected applications, optional for agentless applications. |
| sameSiteCookieAttribute | string | Same site cookie attribute The element can hold these values * `LAX` * `NONE` * `STRICT` |
| scriptTagCacheDurationInHours | integer | Time duration for the cache settings. |
| secureCookieAttribute | boolean | Secure attribute usage for Dynatrace cookies enabled/disabled. |
| serverRequestPathId | string | Path to identify the server’s request ID. |
| useCors | boolean | Send beacon data via CORS. |
| xmlHttpRequest | boolean | `XmlHttpRequest` support enabled/disabled. |

#### The `AdvancedJavaScriptTagSettings` object

Advanced JavaScript tag settings.

| Element | Type | Description |
| --- | --- | --- |
| additionalEventHandlers | [AdditionalEventHandlers](#openapi-definition-AdditionalEventHandlers) | Additional event handlers and wrappers. |
| eventWrapperSettings | [EventWrapperSettings](#openapi-definition-EventWrapperSettings) | In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page. |
| globalEventCaptureSettings | [GlobalEventCaptureSettings](#openapi-definition-GlobalEventCaptureSettings) | Global event capture settings. |
| instrumentUnsupportedAjaxFrameworks | boolean | Instrumentation of unsupported Ajax frameworks enabled/disabled. |
| maxActionNameLength | integer | Maximum character length for action names. Valid values range from 5 to 10000. |
| maxErrorsToCapture | integer | Maximum number of errors to be captured per page. Valid values range from 0 to 50. |
| proxyWrapperEnabled | boolean | Proxy wrapper enabled/disabled. |
| specialCharactersToEscape | string | Additional special characters that are to be escaped using non-alphanumeric characters in HTML escape format. |
| syncBeaconFirefox | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Firefox enabled/disabled. |
| syncBeaconInternetExplorer | boolean | Send the beacon signal as a synchronous XMLHttpRequest using Internet Explorer enabled/disabled. |
| userActionNameAttribute | string | User action name attribute. |

#### The `AdditionalEventHandlers` object

Additional event handlers and wrappers.

| Element | Type | Description |
| --- | --- | --- |
| blurEventHandler | boolean | Blur event handler enabled/disabled. |
| changeEventHandler | boolean | Change event handler enabled/disabled. |
| clickEventHandler | boolean | Click event handler enabled/disabled. |
| maxDomNodesToInstrument | integer | Max. number of DOM nodes to instrument. Valid values range from 0 to 100000. |
| mouseupEventHandler | boolean | Mouseup event handler enabled/disabled. |
| toStringMethod | boolean | toString method enabled/disabled. |
| userMouseupEventForClicks | boolean | Use mouseup event for clicks enabled/disabled. |

#### The `EventWrapperSettings` object

In addition to the event handlers, events called using `addEventListener` or `attachEvent` can be captured. Be careful with this option! Event wrappers can conflict with the JavaScript code on a web page.

| Element | Type | Description |
| --- | --- | --- |
| blur | boolean | Blur enabled/disabled. |
| change | boolean | Change enabled/disabled. |
| click | boolean | Click enabled/disabled. |
| mouseUp | boolean | MouseUp enabled/disabled. |
| touchEnd | boolean | TouchEnd enabled/disabled. |
| touchStart | boolean | TouchStart enabled/disabled. |

#### The `GlobalEventCaptureSettings` object

Global event capture settings.

| Element | Type | Description |
| --- | --- | --- |
| additionalEventCapturedAsUserInput | string | Additional events to be captured globally as user input.  For example, DragStart or DragEnd. |
| change | boolean | Change enabled/disabled. |
| click | boolean | Click enabled/disabled. |
| doubleClick | boolean | DoubleClick enabled/disabled. |
| keyDown | boolean | KeyDown enabled/disabled. |
| keyUp | boolean | KeyUp enabled/disabled. |
| mouseDown | boolean | MouseDown enabled/disabled. |
| mouseUp | boolean | MouseUp enabled/disabled. |
| scroll | boolean | Scroll enabled/disabled. |
| touchEnd | boolean | TouchEnd enabled/disabled. |
| touchStart | boolean | TouchStart enabled/disabled. |

#### The `WebApplicationConfigBrowserRestrictionSettings` object

Settings for restricting certain browser type, version, platform and, comparator. It also restricts the mode.

| Element | Type | Description |
| --- | --- | --- |
| browserRestrictions | [WebApplicationConfigBrowserRestriction](#openapi-definition-WebApplicationConfigBrowserRestriction)[] | A list of browser restrictions. |
| mode | string | The mode of the list of browser restrictions. The element can hold these values * `EXCLUDE` * `INCLUDE` |

#### The `WebApplicationConfigBrowserRestriction` object

Browser exclusion rules for the browsers that are to be excluded.

| Element | Type | Description |
| --- | --- | --- |
| browserType | string | The type of the browser that is used. The element can hold these values * `ANDROID_WEBKIT` * `BOTS_SPIDERS` * `CHROME` * `CHROME_HEADLESS` * `EDGE` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` |
| browserVersion | string | The version of the browser that is used. |
| comparator | string | Compares different browsers together. The element can hold these values * `EQUALS` * `GREATER_THAN_OR_EQUAL` * `LOWER_THAN_OR_EQUAL` |
| platform | string | The platform on which the browser is being used. The element can hold these values * `ALL` * `DESKTOP` * `MOBILE` |

#### The `ContentCapture` object

Settings for content capture.

| Element | Type | Description |
| --- | --- | --- |
| javaScriptErrors | boolean | JavaScript errors monitoring enabled/disabled. |
| resourceTimingSettings | [ResourceTimingSettings](#openapi-definition-ResourceTimingSettings) | Settings for resource timings capture. |
| timeoutSettings | [TimeoutSettings](#openapi-definition-TimeoutSettings) | Settings for timed action capture. |
| visuallyComplete2Settings | [VisuallyComplete2Settings](#openapi-definition-VisuallyComplete2Settings) | Settings for VisuallyComplete2 |
| visuallyCompleteAndSpeedIndex | boolean | Visually complete and Speed index support enabled/disabled. |

#### The `ResourceTimingSettings` object

Settings for resource timings capture.

| Element | Type | Description |
| --- | --- | --- |
| nonW3cResourceTimings | boolean | Timing for JavaScript files and images on non-W3C supported browsers enabled/disabled. |
| nonW3cResourceTimingsInstrumentationDelay | integer | Instrumentation delay for monitoring resource and image resource impact in browsers that don't offer W3C resource timings.  Valid values range from 0 to 9999.  Only effective if **nonW3cResourceTimings** is enabled. |
| resourceTimingCaptureType | string | Defines how detailed resource timings are captured.  Only effective if **w3cResourceTimings** or **nonW3cResourceTimings** is enabled. The element can hold these values * `CAPTURE_ALL_SUMMARIES` * `CAPTURE_FULL_DETAILS` * `CAPTURE_LIMITED_SUMMARIES` |
| resourceTimingsDomainLimit | integer | Limits the number of domains for which W3C resource timings are captured.  Only effective if **resourceTimingCaptureType** is `CAPTURE_LIMITED_SUMMARIES`. |
| w3cResourceTimings | boolean | W3C resource timings for third party/CDN enabled/disabled. |

#### The `TimeoutSettings` object

Settings for timed action capture.

| Element | Type | Description |
| --- | --- | --- |
| temporaryActionLimit | integer | Defines how deep temporary actions may cascade. 0 disables temporary actions completely. Recommended value if enabled is 3. |
| temporaryActionTotalTimeout | integer | The total timeout of all cascaded timeouts that should still be able to create a temporary action |
| timedActionSupport | boolean | Timed action support enabled/disabled.  Enable to detect actions that trigger sending of XHRs via *setTimout* methods. |

#### The `VisuallyComplete2Settings` object

Settings for VisuallyComplete2

| Element | Type | Description |
| --- | --- | --- |
| excludeUrlRegex | string | A RegularExpression used to exclude images and iframes from being detected by the VC module. |
| ignoredMutationsList | string | Query selector for mutation nodes to ignore in VC and SI calculation |
| inactivityTimeout | integer | The time in ms the VC module waits for no mutations happening on the page after the load action. Defaults to 1000. |
| mutationTimeout | integer | Determines the time in ms VC waits after an action closes to start calculation. Defaults to 50. |
| threshold | integer | Minimum visible area in pixels of elements to be counted towards VC and SI. Defaults to 50. |

#### The `WebApplicationConfigIpAddressRestrictionSettings` object

Settings for restricting certain ip addresses and for introducing subnet mask. It also restricts the mode.

| Element | Type | Description |
| --- | --- | --- |
| ipAddressRestrictions | [IpAddressRange](#openapi-definition-IpAddressRange)[] | - |
| mode | string | The mode of the list of ip address restrictions. The element can hold these values * `EXCLUDE` * `INCLUDE` |

#### The `IpAddressRange` object

The IP address or the IP address range to be mapped to the location.

| Element | Type | Description |
| --- | --- | --- |
| address | string | The IP address to be mapped.  For an IP address range, this is the **from** address. |
| addressTo | string | The **to** address of the IP address range. |
| subnetMask | integer | The subnet mask of the IP address range. |

#### The `JavaScriptFrameworkSupport` object

Support of various JavaScript frameworks.

| Element | Type | Description |
| --- | --- | --- |
| activeXObject | boolean | ActiveXObject detection support enabled/disabled. |
| angular | boolean | AngularJS and Angular support enabled/disabled. |
| dojo | boolean | Dojo support enabled/disabled. |
| extJS | boolean | ExtJS, Sencha Touch support enabled/disabled. |
| icefaces | boolean | ICEfaces support enabled/disabled. |
| jQuery | boolean | jQuery, Backbone.js support enabled/disabled. |
| mooTools | boolean | MooTools support enabled/disabled. |
| prototype | boolean | Prototype support enabled/disabled. |

#### The `JavaScriptInjectionRules` object

Rules for javascript injection

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The enable or disable rule of the java script injection. |
| htmlPattern | string | The html pattern of the java script injection. |
| rule | string | The url rule of the java script injection. The element can hold these values * `AFTER_SPECIFIC_HTML` * `AUTOMATIC_INJECTION` * `BEFORE_SPECIFIC_HTML` * `DO_NOT_INJECT` |
| target | string | The target against which the rule of the java script injection should be matched. The element can hold these values * `PAGE_QUERY` * `URL` |
| urlOperator | string | The url operator of the java script injection. The element can hold these values * `ALL_PAGES` * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| urlPattern | string | The url pattern of the java script injection. |

#### The `SessionReplaySetting` object

Session replay settings

| Element | Type | Description |
| --- | --- | --- |
| costControlPercentage | integer | Session replay sampling rating in percentage. |
| cssResourceCapturingExclusionRules | string[] | A list of URLs to be excluded from CSS resource capturing. |
| enableCssResourceCapturing | boolean | Capture (`true`) or don't capture (`false`) CSS resources from the session. |
| enabled | boolean | SessionReplay Enabled. |

#### The `UserActionAndSessionProperties` object

Defines userAction and session custom defined properties settings of an application.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | The aggregation type of the property.  It defines how multiple values of the property are aggregated. The element can hold these values * `AVERAGE` * `FIRST` * `LAST` * `MAXIMUM` * `MINIMUM` * `SUM` |
| cleanupRule | string | The cleanup rule of the property.  Defines how to extract the data you need from a string value. Specify the [regular expression﻿](https://dt-url.net/k9e0iaq) for the data you need there. |
| displayName | string | The display name of the property. |
| ignoreCase | boolean | If true, the value of this property will always be stored in lower case. Defaults to false. |
| key | string | Key of the property |
| longStringLength | integer | If the type is LONG\_STRING, the max length for this property. Must be a multiple of 100. Defaults to 200. |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig.Must be set if "origin" is of type META\_DATA. |
| origin | string | The origin of the property The element can hold these values * `JAVASCRIPT_API` * `META_DATA` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | The ID of the request attribute.  Only applicable when the **origin** is set to `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | If `true`, the property is stored as a session property |
| storeAsUserActionProperty | boolean | If `true`, the property is stored as a user action property |
| type | string | The data type of the property. The element can hold these values * `DATE` * `DOUBLE` * `LONG` * `LONG_STRING` * `STRING` |
| uniqueId | integer | Unique id among all userTags and properties of this application |

#### The `UserActionNamingSettings` object

The settings of user action naming.

| Element | Type | Description |
| --- | --- | --- |
| customActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for custom actions. |
| ignoreCase | boolean | Case insensitive naming. |
| loadActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for loading actions. |
| placeholders | [UserActionNamingPlaceholder](#openapi-definition-UserActionNamingPlaceholder)[] | User action placeholders. |
| queryParameterCleanups | string[] | List of parameters that should be removed from the query before using the query in the user action name. |
| splitUserActionsByDomain | boolean | Deactivate this setting if different domains should not result in separate user actions. |
| useFirstDetectedLoadAction | boolean | First load action found under an XHR action should be used when true. Else the deepest one under the xhr action is used |
| xhrActionNamingRules | [UserActionNamingRule](#openapi-definition-UserActionNamingRule)[] | User action naming rules for xhr actions. |

#### The `UserActionNamingRule` object

The settings of naming rule.

| Element | Type | Description |
| --- | --- | --- |
| conditions | [UserActionNamingRuleCondition](#openapi-definition-UserActionNamingRuleCondition)[] | Defines the conditions when the naming rule should apply. |
| template | string | Naming pattern. Use Curly brackets `{}` to select placeholders. |
| useOrConditions | boolean | If set to `true` the conditions will be connected by logical OR instead of logical AND. |

#### The `UserActionNamingRuleCondition` object

The settings of conditions for user action naming.

| Element | Type | Description |
| --- | --- | --- |
| operand1 | string | Must be a defined placeholder wrapped in curly braces |
| operand2 | string | Must be null if operator is "IS\_EMPTY", a regex if operator is "MATCHES\_REGULAR\_ERPRESSION". In all other cases the value can be a freetext or a placeholder wrapped in curly braces |
| operator | string | The operator of the condition The element can hold these values * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `IS_EMPTY` * `IS_NOT_EMPTY` * `MATCHES_REGULAR_EXPRESSION` * `NOT_CONTAINS` * `NOT_ENDS_WITH` * `NOT_EQUALS` * `NOT_MATCHES_REGULAR_EXPRESSION` * `NOT_STARTS_WITH` * `STARTS_WITH` |

#### The `UserActionNamingPlaceholder` object

The placeholder settings.

| Element | Type | Description |
| --- | --- | --- |
| input | string | Input. The element can hold these values * `ELEMENT_IDENTIFIER` * `INPUT_TYPE` * `METADATA` * `PAGE_TITLE` * `PAGE_URL` * `SOURCE_URL` * `TOP_XHR_URL` * `XHR_URL` |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if "Input" is of type METADATA. |
| name | string | Placeholder name. |
| processingPart | string | Part. The element can hold these values * `ALL` * `ANCHOR` * `PATH` |
| processingSteps | [UserActionNamingPlaceholderProcessingStep](#openapi-definition-UserActionNamingPlaceholderProcessingStep)[] | Processing actions. |
| useGuessedElementIdentifier | boolean | Use the element identifier that was selected by Dynatrace. |

#### The `UserActionNamingPlaceholderProcessingStep` object

The processing step settings.

| Element | Type | Description |
| --- | --- | --- |
| fallbackToInput | boolean | If set to true: Returns the input if **patternBefore** or **patternAfter** cannot be found and the **type** is `SUBSTRING`.  Returns the input if **regularExpression** doesn't match and **type** is `EXTRACT_BY_REGULAR_EXPRESSION`.  Otherwise null is returned. |
| patternAfter | string | The pattern after the required value. It will be removed. |
| patternAfterSearchType | string | The required occurrence of **patternAfter**. The element can hold these values * `FIRST` * `LAST` |
| patternBefore | string | The pattern before the required value. It will be removed. |
| patternBeforeSearchType | string | The required occurrence of **patternBefore**. The element can hold these values * `FIRST` * `LAST` |
| patternToReplace | string | The pattern to be replaced.  Only applicable if the **type** is `REPLACE_WITH_PATTERN`. |
| regularExpression | string | A regular expression for the string to be extracted or replaced.  Only applicable if the **type** is `EXTRACT_BY_REGULAR_EXPRESSION` or `REPLACE_WITH_REGULAR_EXPRESSION`. |
| replacement | string | Replacement for the original value. |
| type | string | An action to be taken by the processing:  * `SUBSTRING`: Extracts the string between **patternBefore** and **patternAfter**. * `REPLACEMENT`: Replaces the string between **patternBefore** and **patternAfter** with the specified **replacement**. * `REPLACE_WITH_PATTERN`: Replaces the **patternToReplace** with the specified **replacement**. * `EXTRACT_BY_REGULAR_EXPRESSION`: Extracts the part of the string that matches the **regularExpression**. * `REPLACE_WITH_REGULAR_EXPRESSION`: Replaces all occurrences that match **regularExpression** with the specified **replacement**. * `REPLACE_IDS`: Replaces all IDs and UUIDs with the specified **replacement**. The element can hold these values * `EXTRACT_BY_REGULAR_EXPRESSION` * `REPLACEMENT` * `REPLACE_IDS` * `REPLACE_WITH_PATTERN` * `REPLACE_WITH_REGULAR_EXPRESSION` * `SUBSTRING` |

#### The `UserTag` object

Defines UserTags settings of an application.

| Element | Type | Description |
| --- | --- | --- |
| cleanupRule | string | Cleanup rule expression of the userTag |
| ignoreCase | boolean | If true, the value of this tag will always be stored in lower case. Defaults to false. |
| metadataId | integer | A reference to the uniqueId of a MetadataCapturingConfig. Must be set if the UserTag is based on metadata captured by the Javascript agent (e.g. a Javascript variable, CSS selector, etc.) |
| serverSideRequestAttribute | string | Serverside request attribute id of the userTag. Must be set if the UserTag is based on a serverside request attribute. |
| uniqueId | integer | uniqueId, unique among all userTags and properties of this application |

#### The `WaterfallSettings` object

These settings influence the monitoring data you receive for 3rd party, CDN, and 1st party resources.

| Element | Type | Description |
| --- | --- | --- |
| resourceBrowserCachingThreshold | integer | Warn about resources with a lower browser cache rate above *X*%. |
| resourcesThreshold | integer | Warn about resources larger than *X* bytes. |
| slowCdnResourcesThreshold | integer | Warn about slow CDN resources with a response time above *X* ms. |
| slowFirstPartyResourcesThreshold | integer | Warn about slow 1st party resources with a response time above *X* ms. |
| slowThirdPartyResourcesThreshold | integer | Warn about slow 3rd party resources with a response time above *X* ms. |
| speedIndexVisuallyCompleteRatioThreshold | integer | Warn if Speed index exceeds *X* % of Visually complete. |
| uncompressedResourcesThreshold | integer | Warn about uncompressed resources larger than *X* bytes. |

### Response body JSON models

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