---
title: Infrastructure pass-through requirements for RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/infrastructure-pass-through-requirements-classic
---

# Infrastructure pass-through requirements for RUM Classic

# Infrastructure pass-through requirements for RUM Classic

* Reference
* 9-min read
* Updated on Jun 01, 2026

Real User Monitoring Classic (RUM Classic) operates within an HTTP ecosystem and relies on a set of requests, headers, and cookies to capture and report real user data, and to link it with backend distributed traces. For RUM to work as expected, your infrastructure—including firewalls, proxies, load balancers, content delivery networks, web servers, and any other components in the request path—must allow these requests, headers, and cookies to pass through unaltered. In addition, OneAgent uses the headers described in [Span and trace context propagation in Distributed Traces Classic](/managed/observe/application-observability/distributed-traces/context-propagation "Understand span and trace context propagation in Dynatrace and how to set them up.") for distributed tracing, which also need to pass through your infrastructure.

## Web applications

### Requests

On web applications, the RUM JavaScript is either [injected automatically](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") or [inserted manually](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") into webpages. The RUM monitoring code is loaded as an external file unless you use the [snippet format inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case")—and even then, the Session Replay monitoring code is loaded as a separate file. Once active, the RUM JavaScript starts sending beacon requests to report the captured RUM data.

For RUM to function fully, both requests for the RUM monitoring code and RUM beacons must pass through your infrastructure.

#### Requests for the RUM monitoring code

* For agentless monitoring, requests are sent to the CDN or the Cluster ActiveGate that you set up according to [Set up agentless Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").
* For auto-injection, requests are, by default, sent to the web or app server that hosts the application, and the URL path contains the string `ruxitagentjs_`.

For details on the default URL and the available configuration options, see [Configure the Real User Monitoring Classic code source](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring Classic code source for your specific requirements.").

#### RUM beacons

RUM beacons report the data captured by the RUM JavaScript back to a [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

* For agentless monitoring, beacons are, by default, sent to a beacon endpoint with the URL path `/bf/<id>` that is part of a Cluster ActiveGate.
* For auto-injection, beacons are, by default, sent to the web or app server that hosts the application, and the URL path ends with `/rb_<id>`.
* The beacon URL includes a query string that must not be altered—this includes modifying, removing, or reordering parameters.
* The `POST` body contains the payload, sent with the `text/plain` content type. For Session Replay, the `application/octet-stream` content type can also be used.
* For Session Replay, `POST` requests may be preceded by [CORS preflight requests﻿](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request), which are `OPTIONS` requests.

For the available beacon endpoint configuration options, see [Configure beacon endpoint for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

### Headers

RUM uses the following HTTP headers, all of which must be allowed to pass through your infrastructure.

#### Custom request headers

| Header | Purpose |
| --- | --- |
| `x-dtc` | Set by the RUM JavaScript when configured as described in [Link cross-origin XHR user actions and their distributed traces in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs#x-dtc-header "Enable the correlation between cross-origin XHR actions and distributed traces.") to carry information required for correlating cross-origin XHRs. |
| `x-dtpc` | Set by the RUM JavaScript to carry IDs required for RUM beacon routing, user session aggregation, and RUM correlation. |
| `x-dtreferer` | Set by the RUM JavaScript when the instrumented application modifies the standard `Referer` header during a user action, to preserve the original referer for RUM correlation. |
| `x-dynatrace-application` | Set by OneAgent on the first instrumented server-side tier (the one closest to the browser) to forward context to downstream OneAgents, such as the [detected application ID](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."), the [cookie domain](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#cookie-domain "Learn which RUM cookie attributes you can configure and how."), and any applicable [custom injection rule](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#custom-injection-rule "Configure automatic injection of the RUM JavaScript into the pages of your applications"). |
| `x-dynatrace-origin-url` | OneAgent versions before 1.167 Legacy header set on the first instrumented server-side tier (the one closest to the browser) to preserve the original URL of the request in case of URL rewriting. |
| `X-ruxit-Disposition` | Set by OneAgent to prevent the .NET code module from capturing distributed traces for RUM beacons. |

#### Standard request headers

| Header | Purpose |
| --- | --- |
| [`Accept-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Encoding) | Read by OneAgent to determine whether to compress the RUM JavaScript before delivery. |
| [`Cookie`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cookie) | Set or modified by OneAgent on the first instrumented server-side tier (the one closest to the browser) when no `dtCookie` is present yet, to propagate the cookie value to downstream OneAgents. Once RUM is active in the browser, the browser also adds cookies set by the RUM JavaScript to this header. See [Cookies](#cookies-web) for details on all RUM cookies. |
| [`If-Match`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Match) [`If-Modified-Since`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Modified-Since) [`If-None-Match`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) [`If-Unmodified-Since`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Unmodified-Since) | Modified by OneAgent when [cache control header optimizations](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications") are active. |
| [`Referer`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer) | Set by the browser. Captured by OneAgent and by the [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") on the Cluster ActiveGate for RUM correlation. |
| [`User-Agent`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent) | Set by the browser. Read by OneAgent to evaluate [browser exclusion rules](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring#exclude-browsers "Disable Real User Monitoring Classic for certain IP addresses, browsers, bots, and spiders."), and captured by [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") for [browser and OS detection](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems."). Setting it to `dtHealthCheck` triggers [OneAgent's RUM health check﻿](https://dt-url.net/qg037fw). |

#### Custom response headers

| Header | Purpose |
| --- | --- |
| `x-dtAgentId` | Set by OneAgent when its [RUM health check﻿](https://dt-url.net/qg037fw) is active, carrying the IDs of the OneAgent code modules involved in handling the request. |
| `x-dtHealthCheck` | Set by OneAgent when its [RUM health check﻿](https://dt-url.net/qg037fw) is active, carrying the health check results. |
| `X-OneAgent-JS-Injection` `X-ruxit-JS-Agent` | Set by OneAgent to indicate that it has started injecting the RUM JavaScript, preventing duplicate injection. |

#### Standard response headers

| Header | Purpose |
| --- | --- |
| [`Access-Control-Allow-Headers`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Headers) [`Access-Control-Allow-Methods`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Methods) [`Access-Control-Max-Age`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age) | Set by [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") for responses to [`OPTIONS` requests](#beacons-web). |
| [`Access-Control-Allow-Origin`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) | Set by [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") for responses to [RUM beacons](#beacons-web). To control from which origins beacons are accepted, configure the [beacon origin allowlist](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted."). Also set for responses to [requests for the RUM monitoring code](#requests-monitoring-code) when they are handled via the Dynatrace CDN. |
| [`Cache-Control`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) | Set for responses to [RUM beacons and requests for the RUM monitoring code](#requests-web). |
| [`Content-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Encoding) | Set for responses to [requests for the RUM monitoring code](#requests-monitoring-code); also read during HTML injection. |
| [`Content-Length`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Length) | Adapted upon HTML injection, and set for responses to [RUM beacons and requests for the RUM monitoring code](#requests-web). |
| [`Content-Type`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) | Set for responses to [RUM beacons and requests for the RUM monitoring code](#requests-web), and read during HTML injection. |
| [`ETag`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag) | When [cache control header optimizations](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications") are active, OneAgent appends a suffix to the original header value. It may set the header if the application doesn't. |
| [`Expires`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Expires) | Set for responses to [requests for the RUM monitoring code](#requests-monitoring-code) when they are handled via the Dynatrace CDN. |
| [`Last-Modified`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Last-Modified) | When [cache control header optimizations](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications") are active, OneAgent subtracts 1 second from the original header value. The header is also set for responses to [requests for the RUM monitoring code](#requests-monitoring-code). |
| [`Server-Timing`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing) | Set by OneAgent to carry information relevant for RUM correlation. |
| [`Set-Cookie`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) | Set by OneAgent to place the [`dtCookie`](#cookies-web). |
| [`Strict-Transport-Security`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) | Set by the [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") on the Cluster ActiveGate. |
| [`Timing-Allow-Origin`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Timing-Allow-Origin) | Set by OneAgent to allow the RUM JavaScript to access the content of the `Server-Timing` header in cross-origin scenarios. Also set for responses to [requests for the RUM monitoring code](#requests-monitoring-code) when they are handled via the Dynatrace CDN. |
| [`Transfer-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Transfer-Encoding) | Read by OneAgent during HTML injection. |
| [`Vary`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary) | Set for responses to [RUM beacons and requests for the RUM monitoring code](#requests-web). |

### Cookies

RUM uses the following cookies. All of these must be able to reach Dynatrace. For more details on how Dynatrace uses cookies, and for an explanation of the `<suffix>` used in the table, see [Cookies and client-side storage for RUM and Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.").

| Cookie | Max size | Purpose |
| --- | --- | --- |
| `dtCookie<suffix>` | No set limitation, but usually less than 100 B | Tracks a visit across multiple requests. |
| `dtPC<suffix>` | 58 B | Required for routing RUM beacons; includes session ID for user session aggregation. |
| `dtSa<suffix>` | Max URL length | Serves as an intermediate storage for page-spanning actions. |
| `dtValidationCookie<suffix>` | Length of `dTValidationCookieValue` string, that is `23` | Used to determine the top-level domain. |
| `rxVisitor<suffix>` | 45 B | Contains the visitor ID to correlate sessions. |
| `rxvt<suffix>` | 27 B | Stores the session timeout. |
| `dtsrVID<suffix>`[1](#fn-1-1-def) | 20 B | Specifies the ID of the current recorded view. |
| `dtSR<suffix>`[2](#fn-1-2-def) | 81 B | If Session Replay is enabled, stores the required values to keep the recording consistent through pages. |

1

`dtsrVID` cookie exists from RUM JavaScript version 1.325+ to RUM JavaScript version 1.333.

2

The optional cookie `dtSR` is available from RUM JavaScript version 1.335+.

## Mobile applications

### Requests

OneAgent for Mobile sends beacon requests to report the captured RUM data. The beacon URL path depends on the configured beacon endpoint:

* If beacons are handled by an ActiveGate, the URL path is `/mbeacon`.
* If beacons are [handled by a OneAgent instrumenting a web or application server](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/oneagent-as-beacon-forwarder-mobile "Use Dynatrace OneAgent as a beacon endpoint for mobile applications."), the URL path is `/dtmb`.

In addition to the `POST` requests that report the captured data, OneAgent for Mobile also sends `GET` requests to the beacon endpoint to retrieve configuration updates. Beacon responses have a `text/plain` content type.

The beacon URL includes a query string that must not be altered—this includes modifying, removing, or reordering parameters.

### Headers

On mobile applications, the following HTTP headers are used, all of which must be allowed to pass through your infrastructure.

#### Request headers

| Header | Purpose |
| --- | --- |
| `x-dtc` | Set when you use the [Cordova Plugin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.") and manually instrument [native web requests﻿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#native-webrequests). Links native web requests with their server-side distributed traces. |
| `x-dynatrace` | Set by OneAgent for Mobile to link the mobile part of a web request with the server-side distributed trace. |

#### Response headers

| Header | Purpose |
| --- | --- |
| [`Cache-Control`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) [`Content-Length`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Length) [`Content-Type`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) | Set for responses to [RUM beacons](#requests-mobile). |
| [`Strict-Transport-Security`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) | Set by the ActiveGate beacon endpoint for responses to [RUM beacons](#requests-mobile). |

### Cookies

The following cookies are used for hybrid applications that combine OneAgent for Mobile with the RUM JavaScript. They need to pass through your infrastructure unaltered.

| Cookie | Max size | Purpose |
| --- | --- | --- |
| `dtAdk` | 92 B | Joins sessions captured by the OneAgent for Mobile and the RUM JavaScript. |
| `dtAdkSettings` | 36 B | Propagates settings between OneAgent for Mobile and the RUM JavaScript. |