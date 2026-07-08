---
title: Synthetic monitors API v2 - GET Synthetic monitor definition
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors/get-monitor-definition
---

# Synthetic monitors API v2 - GET Synthetic monitor definition

# Synthetic monitors API v2 - GET Synthetic monitor definition

* Reference
* Updated on May 05, 2026

Get a Synthetic monitor definition for the given monitor ID.

The method is available only for browser and NAM monitors.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/monitors/{monitorId}` |

## Authentication

To execute this request, you need an access token with `settings.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| monitorId | string | The identifier of the monitor. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticMultiProtocolMonitorResponse](#openapi-definition-SyntheticMultiProtocolMonitorResponse) | [SyntheticBrowserMonitorResponse](#openapi-definition-SyntheticBrowserMonitorResponse) | [SyntheticHttpMonitorResponse](#openapi-definition-SyntheticHttpMonitorResponse) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticMultiProtocolMonitorResponse` object

Network availability monitor.

| Element | Type | Description |
| --- | --- | --- |
| description | string | Monitor description |
| enabled | boolean | If true, the monitor is enabled. |
| entityId | string | The entity id of the monitor. |
| frequencyMin | integer | The frequency of the monitor, in minutes. |
| locations | string[] | The locations to which the monitor is assigned. |
| modificationTimestamp | integer | The timestamp of the last modification |
| name | string | The name of the monitor. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. |
| steps | [SyntheticMultiProtocolMonitorStepDto](#openapi-definition-SyntheticMultiProtocolMonitorStepDto)[] | The steps of the monitor. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` |

#### The `SyntheticMonitorPerformanceThresholdsDto` object

Performance thresholds configuration.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Performance threshold is enabled (`true`) or disabled (`false`). |
| thresholds | [SyntheticMonitorPerformanceThresholdDto](#openapi-definition-SyntheticMonitorPerformanceThresholdDto)[] | The list of performance threshold rules. |

#### The `SyntheticMonitorPerformanceThresholdDto` object

The performance threshold rule.

| Element | Type | Description |
| --- | --- | --- |
| aggregation | string | Aggregation type The element can hold these values * `AVG` * `MAX` * `MIN` |
| dealertingSamples | integer | Number of most recent non-violating request executions that closes the problem. |
| samples | integer | Number of request executions in analyzed sliding window (sliding window size). |
| stepIndex | integer | Specify the step's index to which a threshold applies. If threshold is monitor-level, no index is needed. |
| threshold | number | Notify if monitor request takes longer than *X* time units to execute. For network availability monitors the time unit is milliseconds, for browser and HTTP monitors - seconds. |
| type | string | Type of performance threshold. The element can hold these values * `MONITOR` * `STEP` |
| violatingSamples | integer | Number of violating request executions in analyzed sliding window. |

#### The `SyntheticMonitorPrimaryGrailTagDto` object

Primary grail tag key-value pair.

| Element | Type | Description |
| --- | --- | --- |
| key | string | Tag key. |
| value | string | Tag value. |

#### The `SyntheticMultiProtocolMonitorStepDto` object

The step of a network availability monitor.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | The list of constraints which apply to all requests in the step. |
| name | string | Step name. |
| properties | object | The properties which apply to all requests in the step. |
| requestConfigurations | [SyntheticMultiProtocolRequestConfigurationDto](#openapi-definition-SyntheticMultiProtocolRequestConfigurationDto)[] | Request configurations. |
| requestType | string | Request type. The element can hold these values * `ICMP` * `TCP` * `DNS` |
| targetFilter | string | Target filter. |
| targetList | string[] | Target list. |

#### The `SyntheticMonitorConstraintDto` object

Synthetic monitor constraint. The allowed type and properties depend on the monitor and step/request context.

| Element | Type | Description |
| --- | --- | --- |
| properties | object | Constraint properties. Most constraint types use operator and value keys. Some protocol-specific constraints may use additional keys, for example DNS\_STATUS\_CODE can use status. |
| type | string | Constraint type. Allowed values depend on monitor type and step/request context. HTTP monitor step constraints: HTTP\_STATUSES, HTTP\_RESPONSE\_PATTERN, HTTP\_RESPONSE\_REGEX. Network availability monitor(MULTI\_PROTOCOL) step constraints: SUCCESS\_RATE\_PERCENT. Network availability monitor(MULTI\_PROTOCOL) request configuration constraints are request-type specific, for example ICMP\_SUCCESS\_RATE\_PERCENT (ICMP) and DNS\_STATUS\_CODE (DNS). |

#### The `SyntheticMultiProtocolRequestConfigurationDto` object

The configuration of a network availability monitor request.

| Element | Type | Description |
| --- | --- | --- |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | Request constraints. |

#### The `SyntheticMonitorOutageHandlingSettingsDto` object

Outage handling configuration.

| Element | Type | Description |
| --- | --- | --- |
| globalConsecutiveOutageCountThreshold | integer | Number of consecutive failures for all locations. |
| globalOutages | boolean | Generate a problem and send an alert when the monitor is unavailable at all configured locations. |
| localConsecutiveOutageCountThreshold | integer | Number of consecutive failures. |
| localLocationOutageCountThreshold | integer | Number of failing locations. |
| localOutages | boolean | Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location. |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |
| retryOnError | boolean | Only Browser Monitor property. If set to true, execution retry will take place in case the monitor fails. |

#### The `SyntheticTagWithSourceDto` object

The tag with source of a monitored entity.

| Element | Type | Description |
| --- | --- | --- |
| context | string | The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value. |
| key | string | The key of the tag. |
| source | string | The source of the tag, such as USER, RULE\_BASED or AUTO. The element can hold these values * `AUTO` * `RULE_BASED` * `USER` |
| value | string | The value of the tag. |

#### The `SyntheticBrowserMonitorResponse` object

Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| automaticallyAssignedEntities | string[] | Automatically assigned entities. |
| configuration | [SyntheticBrowserMonitorConfigurationDto](#openapi-definition-SyntheticBrowserMonitorConfigurationDto) | Browser Monitor configuration. |
| description | string | Monitor description |
| enabled | boolean | If true, the monitor is enabled. |
| entityId | string | The entity id of the monitor. |
| frequencyMin | integer | The frequency of the monitor, in minutes. |
| keyPerformanceMetrics | [KeyPerformanceMetrics](#openapi-definition-KeyPerformanceMetrics) | The key performance metrics configuration. |
| locations | string[] | The locations to which the monitor is assigned. |
| manuallyAssignedEntities | string[] | Manually assigned entities. |
| modificationTimestamp | integer | The timestamp of the last modification |
| name | string | The name of the monitor. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. |
| steps | [SyntheticBrowserMonitorStepDto](#openapi-definition-SyntheticBrowserMonitorStepDto)[] | The steps of the monitor. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` |

#### The `SyntheticBrowserMonitorConfigurationDto` object

Browser Monitor configuration.

| Element | Type | Description |
| --- | --- | --- |
| blockedRequests | string[] | All requests matching the specified patterns will be blocked during the execution of the monitor. |
| browserPermissions | [BrowserPermissionsDto](#openapi-definition-BrowserPermissionsDto) | Permissions settings for browser. |
| bypassCSP | boolean | Bypass ContentSecurity Policy for monitored pages. If not defined in request, it will be set to false by default. |
| chromiumStartupFlags | [ChromiumStartupFlagsDto](#openapi-definition-ChromiumStartupFlagsDto) | Chromium startup flags of a Browser Monitor. |
| clientCertificates | [ClientCertificateDto](#openapi-definition-ClientCertificateDto)[] | Identifier of stored client's certificate. |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | Cookies list. |
| device | [TestDeviceDto](#openapi-definition-TestDeviceDto) | Test device of a Browser Monitor. |
| enablement | [EnablementDto](#openapi-definition-EnablementDto) | Browser monitor enablement settings. |
| experimentalProperties | [MonitorPropertyDto](#openapi-definition-MonitorPropertyDto)[] | Experimental properties list. |
| filteredRequests | [FilteredRequestsDto](#openapi-definition-FilteredRequestsDto) | Filtered requests of a Browser Monitor. |
| ignoredErrorCodes | [IgnoredErrorCodesDto](#openapi-definition-IgnoredErrorCodesDto) | Ignored Error Codes of a Browser Monitor. |
| javaScriptSettings | [JavaScriptAgentSettingsDto](#openapi-definition-JavaScriptAgentSettingsDto) | JavaScript Agent Settings. |
| monitorFrames | boolean | Capture performance metrics for pages loaded in frames. If not defined in request, it will be set to false by default. |
| networkThrottling | [NetworkThrottlingDto](#openapi-definition-NetworkThrottlingDto) | Network throttling of a Browser Monitor. |
| proxy | [ProxyDto](#openapi-definition-ProxyDto) | Browser Monitor proxy. |
| requestHeaderOptions | [RequestHeaderOptionsDto](#openapi-definition-RequestHeaderOptionsDto) | Header Options of a Browser Monitor. |
| useIESupportedAgent | boolean | useIESupportedAgent flag. If not defined in request, it will be set to false by default. |
| userAgent | string | User agent |

#### The `BrowserPermissionsDto` object

Permissions settings for browser.

| Element | Type | Description |
| --- | --- | --- |
| camera | boolean | Camera permission. If not defined in request, it will be set to false by default. |
| location | boolean | Location permission. If not defined in request, it will be set to false by default. |
| microphone | boolean | Microphone permission. If not defined in request, it will be set to false by default. |
| notifications | boolean | Notifications permission. If not defined in request, it will be set to false by default. |

#### The `ChromiumStartupFlagsDto` object

Chromium startup flags of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| autoplay-policy | string | autoplay-policy type. The element can hold these values * `no-user-gesture-required` * `document-user-activation-required` |
| disable-features | object | disable-features map |
| disable-site-isolation-trials | boolean | disable-site-isolation-trials flag. |
| disable-web-security | boolean | disable-web-security flag. If no value is passed, it will be set to false by default. |
| host-resolver-rules | string | host-resolver-rules. |
| ignore-certificate-errors | boolean | ignore-certificate-errors flag. |
| ssl-version-max | string | ssl-version-max. |
| ssl-version-min | string | ssl-version-min. |
| test-type | boolean | test-type flag. |

#### The `ClientCertificateDto` object

Client certificate.

| Element | Type | Description |
| --- | --- | --- |
| credentialId | string | Certificate CV id. |
| domain | string | Domain certificate will be applied to. |

#### The `SyntheticMonitorCookieDto` object

Cookie dto for Synthetic Monitor step.

| Element | Type | Description |
| --- | --- | --- |
| domain | string | Cookie domain. |
| name | string | Cookie name. |
| path | string | Cookie path. |
| value | string | Cookie value. |

#### The `TestDeviceDto` object

Test device of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| height | integer | Device height in px. |
| mobile | boolean | Device is mobile. If not defined in request, it will be set to false by default. |
| name | string | Device name. |
| touchEnabled | boolean | Device is touch enabled. If not defined in request, it will be set to false by default. |
| width | integer | Device width in px. |

#### The `EnablementDto` object

Browser monitor enablement settings.

| Element | Type | Description |
| --- | --- | --- |
| enableOnGrail | boolean | Enable 3rd gen JS agent reporting. Relevant only for grail-enabled SaaS environments. |
| origin | string | Indicates the origin of these settings. The element can hold these values * `MONITOR` * `TENANT` * `DEFAULT` * `UNKNOWN` |

#### The `MonitorPropertyDto` object

Property of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| name | string | Property name. |
| value | string | Property value. |

#### The `FilteredRequestsDto` object

Filtered requests of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| mode | string | Filter mode for filtered requests. The element can hold these values * `BLOCK` * `ALLOW` |
| requests | [RequestFilterDto](#openapi-definition-RequestFilterDto)[] | Requests to be filtered. |

#### The `RequestFilterDto` object

Request filter for Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| matchingPattern | string | Regex for request that filter will be applied to. |
| type | string | Filter type. The element can hold these values * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` * `REGEX` |

#### The `IgnoredErrorCodesDto` object

Ignored Error Codes of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| matchingDocumentRequests | string | Ignoring status codes will be applied to requests matching pattern. |
| statusCodes | string | Status codes to be ignored. |

#### The `JavaScriptAgentSettingsDto` object

JavaScript Agent Settings.

| Element | Type | Description |
| --- | --- | --- |
| customProperties | string | Custom configuration properties |
| experimentalValues | boolean | Experimental values support. If not defined in request, it will be set to false by default. |
| fetchRequests | boolean | Capture fetch() requests. If not defined in request, it will be set to true by default. |
| javaScriptErrors | boolean | Enable this setting to monitor JavaScript errors. The window.onError handler is used for capturing JavaScript errors. If not defined in request, it will be set to true by default. |
| javaScriptFrameworkSupport | [FrameworkOptionsDto](#openapi-definition-FrameworkOptionsDto) | JS framework options of a JS Agent. |
| timedActions | boolean | Within JavaScript frameworks, XHRs are often sent via setTimeout methods. Enable this setting to detect actions that trigger such XHRs. If not defined in request, it will be set to true by default. |
| timeoutSettings | [TimeoutSettingsDto](#openapi-definition-TimeoutSettingsDto) | Timeout settings of a Browser Monitor. |
| visuallyCompleteOptions | [VisuallyCompleteOptionsDto](#openapi-definition-VisuallyCompleteOptionsDto) | Visually Complete Options of a Browser Monitor. |
| xmlHttpRequests | boolean | Capture xml Http requests (XHR). If not defined in request, it will be set to true by default. |

#### The `FrameworkOptionsDto` object

JS framework options of a JS Agent.

| Element | Type | Description |
| --- | --- | --- |
| activeXObject | boolean | activeXObject support. If not defined in request, it will be set to false by default. |
| angular | boolean | Angular support. If not defined in request, it will be set to false by default. |
| dojo | boolean | Dojo support. If not defined in request, it will be set to false by default. |
| extJs | boolean | extJs support. If not defined in request, it will be set to false by default. |
| icefaces | boolean | icefaces support. If not defined in request, it will be set to false by default. |
| jQuery | boolean | jquery support. If not defined in request, it will be set to false by default. |
| mooTools | boolean | mooTools support. If not defined in request, it will be set to false by default. |
| prototype | boolean | prototype support. If not defined in request, it will be set to false by default. |

#### The `TimeoutSettingsDto` object

Timeout settings of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| temporaryActionLimit | integer | Cascading setTimeout calls number limit. If not defined in request, it will be set to 1 by default. |
| temporaryActionTotalTimeout | integer | No additional timeout actions will be created once this time limit is reached. Value must be higher than 0 ms. If not defined in request, it will be set to 100 by default. |

#### The `VisuallyCompleteOptionsDto` object

Visually Complete Options of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| excludedElements | string[] | Query CSS selectors to specify mutation nodes (elements that change) to ignore in Visually complete and Speed index calculation. |
| excludedUrls | string[] | Use regular expressions to define URLs for images and iFrames to exclude from detection by the Visually complete module. |
| imageSizeThreshold | integer | Use this setting to define the minimum visible area per element (in pixels) for an element to be counted towards Visually complete and Speed index. If not defined in request, it will be set to 50 by default. |
| inactivityTimeout | integer | The time the Visually complete module waits for inactivity and no further mutations on the page after the load action. If not defined in request, it will be set to 1000 by default. |
| mutationTimeout | integer | The time the Visually complete module waits after an XHR or custom action closes to start the calculation. If not defined in request, it will be set to 50 by default. |

#### The `NetworkThrottlingDto` object

Network throttling of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| download | integer | Download throughput. If not defined in request, it will be set to -1 by default. |
| latency | integer | Latency. If not defined in request, it will be set to 0 by default. |
| name | string | Predefined network type. If not defined in request, it will be set to "" by default. |
| upload | integer | Upload throughput. If not defined in request, it will be set to -1 by default. |

#### The `ProxyDto` object

Browser Monitor proxy.

| Element | Type | Description |
| --- | --- | --- |
| pacUrl | string | pacUrl |

#### The `RequestHeaderOptionsDto` object

Header Options of a Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| matchingPatterns | string[] | Apply headers to requests matching pattern. |
| requestHeaders | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | Request headers list. |

#### The `MonitorRequestHeader` object

A header of the Http request

| Element | Type | Description |
| --- | --- | --- |
| name | string | Header's name. |
| value | string | Header's value. |

#### The `KeyPerformanceMetrics` object

The key performance metrics configuration.

| Element | Type | Description |
| --- | --- | --- |
| loadActionKpm | string | Load action key performance metric. The element can hold these values * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_START` * `LOAD_EVENT_END` * `RESPONSE_START` * `RESPONSE_END` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` |
| xhrActionKpm | string | XHR action key performance metric. The element can hold these values * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `RESPONSE_START` * `RESPONSE_END` |

#### The `SyntheticBrowserMonitorStepDto` object

Base step of Browser Monitor.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Entity Id. |
| name | string | The name of Browser Monitor step. |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `NAVIGATE` -> NavigateStepDto * `CLICK` -> InteractionStepDto * `TAP` -> InteractionStepDto * `KEYSTROKES` -> KeyStrokesStepDto * `JAVASCRIPT` -> JavaScriptStepDto * `SELECT_OPTION` -> SelectOptionStepDto * `COOKIE` -> CookieStepDto The element can hold these values * `CLICK` * `COOKIE` * `JAVASCRIPT` * `KEYSTROKES` * `NAVIGATE` * `SELECT_OPTION` * `TAP` |

#### The `SyntheticHttpMonitorResponse` object

Http monitor.

| Element | Type | Description |
| --- | --- | --- |
| advancedSettings | [SyntheticHttpMonitorAdvancedDto](#openapi-definition-SyntheticHttpMonitorAdvancedDto) | Http monitor's settings. |
| automaticallyAssignedEntities | string[] | Automatically assigned entities. |
| cookies | [SyntheticMonitorCookieDto](#openapi-definition-SyntheticMonitorCookieDto)[] | The cookies of the monitor. |
| description | string | Monitor description |
| enabled | boolean | If true, the monitor is enabled. |
| entityId | string | The entity id of the monitor. |
| frequencyMin | integer | The frequency of the monitor, in minutes. |
| locations | string[] | The locations to which the monitor is assigned. |
| manuallyAssignedEntities | string[] | Manually assigned entities. |
| modificationTimestamp | integer | The timestamp of the last modification |
| name | string | The name of the monitor. |
| performanceThresholds | [SyntheticMonitorPerformanceThresholdsDto](#openapi-definition-SyntheticMonitorPerformanceThresholdsDto) | Performance thresholds configuration. |
| primaryGrailTags | [SyntheticMonitorPrimaryGrailTagDto](#openapi-definition-SyntheticMonitorPrimaryGrailTagDto)[] | Primary Grail tags as a list of key-value pairs. Up to 10 tags. Those fields are only available for SaaS and not for Managed. |
| securityContext | string[] | [FEATURE DISABLED] Security context as a list of strings. Up to 10 values, max 200 characters per value. Those fields are only available for SaaS and not for Managed. |
| steps | [SyntheticHttpMonitorStepDto](#openapi-definition-SyntheticHttpMonitorStepDto)[] | The steps of the monitor. |
| syntheticMonitorOutageHandlingSettings | [SyntheticMonitorOutageHandlingSettingsDto](#openapi-definition-SyntheticMonitorOutageHandlingSettingsDto) | Outage handling configuration. |
| tags | [SyntheticTagWithSourceDto](#openapi-definition-SyntheticTagWithSourceDto)[] | A set of tags assigned to the monitor.  You can specify only the value of the tag here and the `CONTEXTLESS` context and source 'USER' will be added automatically. But preferred option is usage of SyntheticTagWithSourceDto model. |
| type | string | Monitor type. The element can hold these values * `MULTI_PROTOCOL` * `BROWSER` |

#### The `SyntheticHttpMonitorAdvancedDto` object

Http monitor's settings.

| Element | Type | Description |
| --- | --- | --- |
| connectTimeout | integer | Connect timeout per request in ms. |
| dnsQueryTimeout | integer | DNS query timeout in ms. |
| maxCustomScriptSize | integer | Maximum size of each pre- or post- execution script size in bytes. |
| maxHeaderSize | integer | Maximum size of each request header in bytes. |
| maxRequestBodySize | integer | Maximum request body size in bytes. |
| maxResponseBodyReadByScriptSize | integer | Maximum size of response body read by post-execution script in bytes. |
| maxResponseBodySize | integer | Maximum response body size in bytes. |
| monitorExecutionTimeout | integer | Monitor execution timeout in ms. |
| requestTimeout | integer | Request timeout in ms. |
| scriptExecutionTimeout | integer | Pre- or post- execution script timeout in ms. |

#### The `SyntheticHttpMonitorStepDto` object

The step of a Http monitor.

| Element | Type | Description |
| --- | --- | --- |
| authentication | [SyntheticHttpAuthenticationDto](#openapi-definition-SyntheticHttpAuthenticationDto) | The Http step's authentication. |
| configuration | [SyntheticHttpConfigurationDto](#openapi-definition-SyntheticHttpConfigurationDto) | The Http step's configuration. |
| constraints | [SyntheticMonitorConstraintDto](#openapi-definition-SyntheticMonitorConstraintDto)[] | The list of constraints. |
| entityId | string | Entity Id. |
| methodType | string | Method type. The element can hold these values * `GET` * `POST` * `PUT` * `DELETE` * `HEAD` * `OPTIONS` * `PATCH` |
| name | string | Step name. |
| postScript | string | PostScript. |
| preScript | string | PreScript. |
| requestBody | string | Request body. |
| requestTimeout | integer | Request timeout in s. |
| url | string | Step url. |

#### The `SyntheticHttpAuthenticationDto` object

The Http step's authentication.

| Element | Type | Description |
| --- | --- | --- |
| credentials | string | Credential vault identifier. |
| kdcIp | string | KDC IP in case KERBEROS auth type is selected. |
| realmName | string | Realm name in case KERBEROS type is selected. |
| type | string | Authentication type. The element can hold these values * `BASIC_AUTHENTICATION` * `NTLM` * `KERBEROS` |

#### The `SyntheticHttpConfigurationDto` object

The Http step's configuration.

| Element | Type | Description |
| --- | --- | --- |
| acceptAnyCertificate | boolean | If true accept any certificate flag. |
| clientCertificateId | string | Identifier of stored client's certificate. |
| doNotPersistSensitiveData | boolean | If true the step's data aren't stored and displayed. |
| followRedirects | boolean | If true follow redirects. |
| headers | [MonitorRequestHeader](#openapi-definition-MonitorRequestHeader)[] | The headers. |
| sslCertificateExpirationDaysToAlert | integer | Number of days within SSL certificate expires. |

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



"description": "My network availability monitor description",



"enabled": "true",



"entityId": "MULTIPROTOCOL_MONITOR-63653CB579F573D1",



"frequencyMin": "60",



"locations": [



"SYNTHETIC_LOCATION-D3A5BFD8676A4F20"



],



"modificationTimestamp": "1716448454338l",



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