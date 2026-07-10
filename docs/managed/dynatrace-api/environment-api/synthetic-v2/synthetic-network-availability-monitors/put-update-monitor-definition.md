---
title: Synthetic monitors API v2 - Update Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/put-update-monitor-definition
---

# Synthetic monitors API v2 - Update Synthetic monitor definition

# Synthetic monitors API v2 - Update Synthetic monitor definition

* Reference
* Updated on May 05, 2026

Update Synthetic monitor definition for a given monitor ID.

The method is available only for browser and NAM monitors.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `settings.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The identifier of the monitor. | path | Required |
| body | [SyntheticMultiProtocolMonitorRequest](#openapi-definition-SyntheticMultiProtocolMonitorRequest) | [SyntheticBrowserMonitorRequest](#openapi-definition-SyntheticBrowserMonitorRequest) | [SyntheticHttpMonitorRequest](#openapi-definition-SyntheticHttpMonitorRequest) | The JSON body of the request. Contains the parameters of the monitor. | body | Required |

### Request body objects

#### The `SyntheticMultiProtocolMonitorRequest` object

Network availability monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | Monitor description | Optional |
| enabled | boolean | If true, the monitor is enabled. | Optional |
| frequencyMin | integer | The frequency of the monitor, in minutes. Default value depends on the monitor type (1 minute for MULTI\_PROTOCOL and HTTP, 15 minutes for BROWSER). | Optional |
| locations | string[] | The locations to which the monitor is assigned. | Required |
| name | string | The name of the monitor. | Required |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. | Optional |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. | Optional |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. | Optional |
| steps | [SyntheticMultiProtocolMonitorStepDto](#openapi-definition-SyntheticMultiProtocolMonitorStepDto)[] | The steps of the monitor. | Required |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. | Optional |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. | Optional |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Required |

#### The `SyntheticMonitorPerformanceThresholdsDto` object

Performance thresholds configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). | Required |
| thresholds | [SyntheticMonitorPerformanceThresholdDto](#openapi-definition-SyntheticMonitorPerformanceThresholdDto)[] | The list of performance threshold rules. | Optional |

#### The `SyntheticMonitorPerformanceThresholdDto` object

The performance threshold rule.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| aggregation | string | Aggregation type The element can hold these values * `AVG` * `MAX` * `MIN` | Optional |
| dealertingSamples | integer | Number of most recent non-violating request executions that closes the problem. | Optional |
| samples | integer | Number of request executions in analyzed sliding window (sliding window size). | Optional |
| stepIndex | integer | Specify the step's index to which a threshold applies. If threshold is monitor-level, no index is needed. | Optional |
| threshold | number | Notify if monitor request takes longer than *X* time units to execute. For network availability monitors the time unit is milliseconds, for browser and HTTP monitors - seconds. | Required |
| type | string | Type of performance threshold The element can hold these values * `STEP` * `MONITOR` | Optional |
| violatingSamples | integer | Number of violating request executions in analyzed sliding window. | Optional |

#### The `SyntheticMonitorPrimaryGrailTagDto` object

Primary grail tag key-value pair.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | Tag key. | Required |
| value | string | Tag value. | Required |

#### The `SyntheticMultiProtocolMonitorStepDto` object

The step of a network availability monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | The list of constraints which apply to all requests in the step. | Required |
| name | string | Step name. | Required |
| properties | object | The properties which apply to all requests in the step. | Required |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto)[] | Request configurations. | Required |
| requestType | string | Request type. The element can hold these values * `ICMP` * `TCP` * `DNS` | Required |
| targetFilter | string | Target filter. | Optional |
| targetList | string[] | Target list. | Optional |

#### The `SyntheticMonitorConstraintDto` object

Synthetic monitor constraint. The allowed type and properties depend on the monitor and step/request context.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| properties | object | Constraint properties. Most constraint types use operator and value keys. Some protocol-specific constraints may use additional keys, for example DNS\_STATUS\_CODE can use status. | Required |
| type | string | Constraint type. Allowed values depend on monitor type and step/request context. HTTP monitor step constraints: HTTP\_STATUSES, HTTP\_RESPONSE\_PATTERN, HTTP\_RESPONSE\_REGEX. Network availability monitor(MULTI\_PROTOCOL) step constraints: SUCCESS\_RATE\_PERCENT. Network availability monitor(MULTI\_PROTOCOL) request configuration constraints are request-type specific, for example ICMP\_SUCCESS\_RATE\_PERCENT (ICMP) and DNS\_STATUS\_CODE (DNS). | Required |

#### The `SyntheticMultiProtocolRequestConfigurationDto` object

The configuration of a network availability monitor request.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Request constraints. | Required |

#### The `SyntheticMonitorOutageHandlingSettingsDto` object

Outage handling configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Number of consecutive failures for all locations. | Optional |
| globalOutages | boolean | Generate a problem and send an alert when the monitor is unavailable at all configured locations. | Required |
| localConsecutiveOutageCountThreshold | integer | Number of consecutive failures. | Optional |
| localLocationOutageCountThreshold | integer | Number of failing locations. | Optional |
| localOutages | boolean | Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. | Required |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Optional |
| retryOnError | boolean | Only Browser Monitor property. If set to true, execution retry will take place in case the monitor fails. | Optional |

#### The `SyntheticTagWithSourceDto` object

The tag with source of a monitored entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. | Optional |
| key | string | The key of the tag. | Required |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO. The element can hold these values * `AUTO` * `RULE_BASED` * `USER` | Optional |
| value | string | The value of the tag. | Optional |

#### The `SyntheticBrowserMonitorRequest` object

Browser monitor update.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| configuration | [SyntheticBrowserMonitorConfigurationDto](#openapi-definition-SyntheticBrowserMonitorConfigurationDto) | Browser Monitor configuration. | Required |
| description | string | Monitor description | Optional |
| enabled | boolean | If true, the monitor is enabled. | Optional |
| frequencyMin | integer | The frequency of the monitor, in minutes. Default value depends on the monitor type (1 minute for MULTI\_PROTOCOL and HTTP, 15 minutes for BROWSER). | Optional |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | The key performance metrics configuration. | Optional |
| locations | string[] | The locations to which the monitor is assigned. | Required |
| manuallyAssignedEntities | string[] | Manually assigned entities. | Optional |
| name | string | The name of the monitor. | Required |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. | Optional |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. | Optional |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. | Optional |
| steps | [SyntheticBrowserMonitorStepDto](#openapi-definition-SyntheticBrowserMonitorStepDto)[] | The steps of the monitor. | Required |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. | Optional |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. | Optional |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Required |

#### The `SyntheticBrowserMonitorConfigurationDto` object

Browser Monitor configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| blockedRequests | string[] | All requests matching the specified patterns will be blocked during the execution of the monitor. | Optional |
| browserPermissions | [BrowserPermissionsDto](#openapi-definition-BrowserPermissionsDto) | Permissions settings for browser. | Optional |
| bypassCSP | boolean | Bypass ContentSecurity Policy for monitored pages. If not defined in request, it will be set to false by default. | Optional |
| chromiumStartupFlags | [ChromiumStartupFlagsDto](#openapi-definition-ChromiumStartupFlagsDto) | Chromium startup flags of a Browser Monitor. | Optional |
| clientCertificates | [ClientCertificateDto](#openapi-definition-ClientCertificateDto)[] | Identifier of stored client's certificate. | Optional |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Cookies list. | Optional |
| device | [TestDeviceDto](#openapi-definition-TestDeviceDto) | Test device of a Browser Monitor. | Required |
| enablement | [EnablementDto](#openapi-definition-EnablementDto) | Browser monitor enablement settings. | Optional |
| experimentalProperties | [MonitorPropertyDto](#openapi-definition-MonitorPropertyDto)[] | Experimental properties list. | Optional |
| filteredRequests | [FilteredRequestsDto](#openapi-definition-FilteredRequestsDto) | Filtered requests of a Browser Monitor. | Optional |
| ignoredErrorCodes | [IgnoredErrorCodesDto](#openapi-definition-IgnoredErrorCodesDto) | Ignored Error Codes of a Browser Monitor. | Optional |
| javaScriptSettings | [JavaScriptAgentSettingsDto](#openapi-definition-JavaScriptAgentSettingsDto) | JavaScript Agent Settings. | Optional |
| monitorFrames | boolean | Capture performance metrics for pages loaded in frames. If not defined in request, it will be set to false by default. | Optional |
| networkThrottling | [NetworkThrottlingDto](#openapi-definition-NetworkThrottlingDto) | Network throttling of a Browser Monitor. | Optional |
| proxy | [ProxyDto](#openapi-definition-ProxyDto) | Browser Monitor proxy. | Optional |
| requestHeaderOptions | [RequestHeaderOptionsDto](#openapi-definition-RequestHeaderOptionsDto) | Header Options of a Browser Monitor. | Optional |
| useIESupportedAgent | boolean | useIESupportedAgent flag. If not defined in request, it will be set to false by default. | Optional |
| userAgent | string | User agent | Optional |

#### The `BrowserPermissionsDto` object

Permissions settings for browser.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| camera | boolean | Camera permission. If not defined in request, it will be set to false by default. | Optional |
| location | boolean | Location permission. If not defined in request, it will be set to false by default. | Optional |
| microphone | boolean | Microphone permission. If not defined in request, it will be set to false by default. | Optional |
| notifications | boolean | Notifications permission. If not defined in request, it will be set to false by default. | Optional |

#### The `ChromiumStartupFlagsDto` object

Chromium startup flags of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| autoplay-policy | string | autoplay-policy type. The element can hold these values * `no-user-gesture-required` * `document-user-activation-required` | Optional |
| disable-features | object | disable-features map | Optional |
| disable-site-isolation-trials | boolean | disable-site-isolation-trials flag. | Optional |
| disable-web-security | boolean | disable-web-security flag. If no value is passed, it will be set to false by default. | Optional |
| host-resolver-rules | string | host-resolver-rules. | Optional |
| ignore-certificate-errors | boolean | ignore-certificate-errors flag. | Optional |
| ssl-version-max | string | ssl-version-max. | Optional |
| ssl-version-min | string | ssl-version-min. | Optional |
| test-type | boolean | test-type flag. | Optional |

#### The `ClientCertificateDto` object

Client certificate.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| credentialId | string | Certificate CV id. | Required |
| domain | string | Domain certificate will be applied to. | Required |

#### The `SyntheticMonitorCookieDto` object

Cookie dto for Synthetic Monitor step.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| domain | string | Cookie domain. | Required |
| name | string | Cookie name. | Required |
| path | string | Cookie path. | Optional |
| value | string | Cookie value. | Required |

#### The `TestDeviceDto` object

Test device of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| height | integer | Device height in px. | Required |
| mobile | boolean | Device is mobile. If not defined in request, it will be set to false by default. | Optional |
| name | string | Device name. | Required |
| touchEnabled | boolean | Device is touch enabled. If not defined in request, it will be set to false by default. | Optional |
| width | integer | Device width in px. | Required |

#### The `EnablementDto` object

Browser monitor enablement settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enableOnGrail | boolean | Enable 3rd gen JS agent reporting. Relevant only for grail-enabled SaaS environments. | Required |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` | Optional |

#### The `MonitorPropertyDto` object

Property of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | Property name. | Required |
| value | string | Property value. | Required |

#### The `FilteredRequestsDto` object

Filtered requests of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| mode | string | Filter mode for filtered requests. The element can hold these values * `BLOCK` * `ALLOW` | Required |
| requests | [RequestFilterDto](#openapi-definition-RequestFilterDto)[] | Requests to be filtered. | Required |

#### The `RequestFilterDto` object

Request filter for Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| matchingPattern | string | Regex for request that filter will be applied to. | Required |
| type | string | Filter type. The element can hold these values * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` * `REGEX` | Required |

#### The `IgnoredErrorCodesDto` object

Ignored Error Codes of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| matchingDocumentRequests | string | Ignoring status codes will be applied to requests matching pattern. | Optional |
| statusCodes | string | Status codes to be ignored. | Optional |

#### The `JavaScriptAgentSettingsDto` object

JavaScript Agent Settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customProperties | string | Custom configuration properties | Optional |
| experimentalValues | boolean | Experimental values support. If not defined in request, it will be set to false by default. | Optional |
| fetchRequests | boolean | Capture fetch() requests. If not defined in request, it will be set to true by default. | Optional |
| javaScriptErrors | boolean | Enable this setting to monitor JavaScript errors. The window.onError handler is used for capturing JavaScript errors. If not defined in request, it will be set to true by default. | Optional |
| javaScriptFrameworkSupport | [FrameworkOptionsDto](#openapi-definition-FrameworkOptionsDto) | JS framework options of a JS Agent. | Optional |
| timedActions | boolean | Within JavaScript frameworks, XHRs are often sent via setTimeout methods. Enable this setting to detect actions that trigger such XHRs. If not defined in request, it will be set to true by default. | Optional |
| timeoutSettings | [TimeoutSettingsDto](#openapi-definition-TimeoutSettingsDto) | Timeout settings of a Browser Monitor. | Optional |
| visuallyCompleteOptions | [VisuallyCompleteOptionsDto](#openapi-definition-VisuallyCompleteOptionsDto) | Visually Complete Options of a Browser Monitor. | Optional |
| xmlHttpRequests | boolean | Capture xml Http requests (XHR). If not defined in request, it will be set to true by default. | Optional |

#### The `FrameworkOptionsDto` object

JS framework options of a JS Agent.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeXObject | boolean | activeXObject support. If not defined in request, it will be set to false by default. | Optional |
| angular | boolean | Angular support. If not defined in request, it will be set to false by default. | Optional |
| dojo | boolean | Dojo support. If not defined in request, it will be set to false by default. | Optional |
| extJs | boolean | extJs support. If not defined in request, it will be set to false by default. | Optional |
| icefaces | boolean | icefaces support. If not defined in request, it will be set to false by default. | Optional |
| jQuery | boolean | jquery support. If not defined in request, it will be set to false by default. | Optional |
| mooTools | boolean | mooTools support. If not defined in request, it will be set to false by default. | Optional |
| prototype | boolean | prototype support. If not defined in request, it will be set to false by default. | Optional |

#### The `TimeoutSettingsDto` object

Timeout settings of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| temporaryActionLimit | integer | Cascading setTimeout calls number limit. If not defined in request, it will be set to 1 by default. | Optional |
| temporaryActionTotalTimeout | integer | No additional timeout actions will be created once this time limit is reached. Value must be higher than 0 ms. If not defined in request, it will be set to 100 by default. | Optional |

#### The `VisuallyCompleteOptionsDto` object

Visually Complete Options of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| excludedElements | string[] | Query CSS selectors to specify mutation nodes (elements that change) to ignore in Visually complete and Speed index calculation. | Optional |
| excludedUrls | string[] | Use regular expressions to define URLs for images and iFrames to exclude from detection by the Visually complete module. | Optional |
| imageSizeThreshold | integer | Use this setting to define the minimum visible area per element (in pixels) for an element to be counted towards Visually complete and Speed index. If not defined in request, it will be set to 50 by default. | Optional |
| inactivityTimeout | integer | The time the Visually complete module waits for inactivity and no further mutations on the page after the load action. If not defined in request, it will be set to 1000 by default. | Optional |
| mutationTimeout | integer | The time the Visually complete module waits after an XHR or custom action closes to start the calculation. If not defined in request, it will be set to 50 by default. | Optional |

#### The `NetworkThrottlingDto` object

Network throttling of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| download | integer | Download throughput. If not defined in request, it will be set to -1 by default. | Optional |
| latency | integer | Latency. If not defined in request, it will be set to 0 by default. | Optional |
| name | string | Predefined network type. If not defined in request, it will be set to "" by default. | Optional |
| upload | integer | Upload throughput. If not defined in request, it will be set to -1 by default. | Optional |

#### The `ProxyDto` object

Browser Monitor proxy.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| pacUrl | string | pacUrl | Required |

#### The `RequestHeaderOptionsDto` object

Header Options of a Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| matchingPatterns | string[] | Apply headers to requests matching pattern. | Required |
| requestHeaders | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Request headers list. | Required |

#### The `MonitorRequestHeader` object

A header of the Http request

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | Header's name. | Required |
| value | string | Header's value. | Required |

#### The `KeyPerformanceMetrics` object

The key performance metrics configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| loadActionKpm | string | Load action key performance metric. The element can hold these values * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Optional |
| xhrActionKpm | string | XHR action key performance metric. The element can hold these values * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` | Optional |

#### The `SyntheticBrowserMonitorStepDto` object

Base step of Browser Monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| entityId | string | Entity Id. | Optional |
| name | string | The name of Browser Monitor step. | Required |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `NAVIGATE` -> NavigateStepDto * `CLICK` -> InteractionStepDto * `TAP` -> InteractionStepDto * `KEYSTROKES` -> KeyStrokesStepDto * `JAVASCRIPT` -> JavaScriptStepDto * `SELECT_OPTION` -> SelectOptionStepDto * `COOKIE` -> CookieStepDto The element can hold these values * `CLICK` * `COOKIE` * `JAVASCRIPT` * `KEYSTROKES` * `NAVIGATE` * `SELECT_OPTION` * `TAP` | Required |

#### The `SyntheticHttpMonitorRequest` object

Http monitor's settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| advancedSettings | [SyntheticHttpMonitorAdvancedDto](#openapi-definition-SyntheticHttpMonitorAdvancedDto) | Http monitor's settings. | Optional |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | The cookies of the monitor. | Optional |
| description | string | Monitor description | Optional |
| enabled | boolean | If true, the monitor is enabled. | Optional |
| frequencyMin | integer | The frequency of the monitor, in minutes. Default value depends on the monitor type (1 minute for MULTI\_PROTOCOL and HTTP, 15 minutes for BROWSER). | Optional |
| locations | string[] | The locations to which the monitor is assigned. | Required |
| manuallyAssignedEntities | string[] | Manually assigned entities. | Optional |
| name | string | The name of the monitor. | Required |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. | Optional |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. | Optional |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. | Optional |
| steps | [SyntheticHttpMonitorStepDto](#openapi-definition-SyntheticHttpMonitorStepDto)[] | The steps of the monitor. | Required |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. | Optional |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. | Optional |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` * `HTTP` | Required |

#### The `SyntheticHttpMonitorAdvancedDto` object

Http monitor's settings.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| connectTimeout | integer | Connect timeout per request in ms. | Optional |
| dnsQueryTimeout | integer | DNS query timeout in ms. | Optional |
| maxCustomScriptSize | integer | Maximum size of each pre- or post- execution script size in bytes. | Optional |
| maxHeaderSize | integer | Maximum size of each request header in bytes. | Optional |
| maxRequestBodySize | integer | Maximum request body size in bytes. | Optional |
| maxResponseBodyReadByScriptSize | integer | Maximum size of response body read by post-execution script in bytes. | Optional |
| maxResponseBodySize | integer | Maximum response body size in bytes. | Optional |
| monitorExecutionTimeout | integer | Monitor execution timeout in ms. | Optional |
| requestTimeout | integer | Request timeout in ms. | Optional |
| scriptExecutionTimeout | integer | Pre- or post- execution script timeout in ms. | Optional |

#### The `SyntheticHttpMonitorStepDto` object

The step of a Http monitor.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| authentication | [SyntheticHttpAuthenticationDto](#openapi-definition-SyntheticHttpAuthenticationDto) | The Http step's authentication. | Optional |
| configuration | [SyntheticHttpConfigurationDto](#openapi-definition-SyntheticHttpConfigurationDto) | The Http step's configuration. | Optional |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | The list of constraints. | Required |
| entityId | string | Entity Id. | Optional |
| methodType | string | Method type. The element can hold these values * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `OPTIONS` * `PATCH` | Required |
| name | string | Step name. | Required |
| postScript | string | PostScript. | Optional |
| preScript | string | PreScript. | Optional |
| requestBody | string | Request body. | Optional |
| requestTimeout | integer | Request timeout in s. | Optional |
| url | string | Step url. | Required |

#### The `SyntheticHttpAuthenticationDto` object

The Http step's authentication.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| credentials | string | Credential vault identifier. | Required |
| kdcIp | string | KDC IP in case KERBEROS auth type is selected. | Optional |
| realmName | string | Realm name in case KERBEROS type is selected. | Optional |
| type | string | Authentication type. The element can hold these values * `BASIC_AUTHENTICATION` * `NTLM` * `KERBEROS` | Required |

#### The `SyntheticHttpConfigurationDto` object

The Http step's configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| acceptAnyCertificate | boolean | If true accept any certificate flag. | Optional |
| clientCertificateId | string | Identifier of stored client's certificate. | Optional |
| doNotPersistSensitiveData | boolean | If true the step's data aren't stored and displayed. | Optional |
| followRedirects | boolean | If true follow redirects. | Optional |
| headers | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | The headers. | Optional |
| sslCertificateExpirationDaysToAlert | integer | Number of days within SSL certificate expires. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"description": "My network availability monitor description",



"enabled": "true",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F19"



],



"name": "My network availability monitor",



"performanceThresholds": {



"enabled": "true",



"thresholds": [



{



"aggregation": "AVG",



"dealertingSamples": "5",



"samples": "5",



"stepIndex": "0",



"threshold": "200",



"violatingSamples": "3"



}



]



},



"primaryGrailTags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "another sample key",



"value": "another sample value"



}



],



"securityContext": [



"sample security context",



"another security context"



],



"steps": [



{



"constraints": [



{



"properties": {



"operator": ">=",



"value": "95"



},



"type": "SUCCESS_RATE_PERCENT"



}



],



"name": "Step 1",



"properties": {



"ICMP_IP_VERSION": "4",



"ICMP_NUMBER_OF_PACKETS": "8",



"ICMP_TIMEOUT_FOR_REPLY": "PT1S"



},



"requestConfigurations": [



{



"constraints": [



{



"properties": {



"operator": "=",



"value": "100"



},



"type": "ICMP_SUCCESS_RATE_PERCENT"



}



]



}



],



"requestType": "ICMP",



"targetFilter": "ipMask == 127.0.0.1/24",



"targetList": [



"127.0.0.1",



"127.0.0.2"



]



}



],



"syntheticMonitorOutageHandlingSettings": {



"globalConsecutiveOutageCountThreshold": "1",



"globalOutages": "true",



"localConsecutiveOutageCountThreshold": "3",



"localLocationOutageCountThreshold": "3",



"localOutages": "true"



},



"tags": [



{



"key": "sample key",



"value": "sample value"



},



{



"key": "sample key"



}



],



"type": "MULTI_PROTOCOL"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

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

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")