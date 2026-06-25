---
title: Firewall constraints for RUM
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum
scraped: 2026-05-12T11:34:25.111512
---

# Firewall constraints for RUM

# Firewall constraints for RUM

* Reference
* 9-min read
* Updated on Apr 22, 2026

Real User Monitoring (RUM) uses HTTP technologies to send performance data from your end users' browsers to Dynatrace. To do this, the [RUM JavaScript is injected](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") into your application's webpages. This [tag or code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") communicates with Dynatrace. However, you must verify the configuration of your firewalls, proxies, and web servers to allow all required data to pass through.

## Requests

For RUM to function fully, the following HTTP requests must pass through your infrastructure:

* Requests for the RUM monitoring code.

  + In case of agentless monitoring, these requests are sent to the CDN or the Cluster ActiveGate that you set up according to [Set up agentless Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").
  + In case of auto-injection, they are, by default, sent to the web or app server that hosts the application, and their URL path contains the string `ruxitagentjs_`.

  For details on the default URL and the available configuration options, see [Configure the Real User Monitoring code source](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.").
* RUM beacons reporting the data captured by the RUM JavaScript back to Dynatrace.

  + In case of agentless monitoring, beacons are, by default, sent to a beacon endpoint that is part of a Cluster ActiveGate. The URL path is `/bf` or `/bf/<id>`.
  + In case of auto-injection, beacons are, by default, sent to the web or app server that hosts the application, and the URL path ends with `/rb_<id>`.
  + The beacon URL contains query parameters. Ensure that your firewall does not remove any query parameters.
  + The `POST` body contains the payload. The payload is sent with the `text/plain` content type. For Session Replay, the `application/octet-stream` content type can also be used.

  For the available beacon endpoint configuration options, see [Configure beacon endpoint for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

## Headers

RUM uses the following HTTP headers. All of these headers must be able to reach Dynatrace.

### Request headers

| Header | Purpose |
| --- | --- |
| `x-dynatrace` | Used for transaction stitching in HTTP headers. Set by OneAgent to link web servers. Ensure that network components, such as firewalls and routers, are never configured to remove these headers. Incorrect configuration can potentially lead to broken distributed traces. Some network components disable such requests and throw a `403` HTTP error, which is why it is necessary to configure these components to accept the `x-dynatrace` header. |
| `x-dynatrace-application` | Contains the ID of the RUM application, the cookie domain, and the injection rule (`noop`, `auto`, `before`, or `after`). Also contains the injection pattern when `injectionRule=after` or `injectionRule=before`.  Used in case there's some proxy in between a user's browser and the original process that delivers the page. |
| `x-dynatrace-origin-url` | Preserves the original URL of the request in case of URL rewriting. |
| `X-dynaTrace-RequestState` | Tracks the depth of a subpath tree to avoid endless distributed traces. |
| `x-dtpc` | Identifies proper endpoints for beacon transmission; includes session ID for correlation. |
| `x-dtreferer` | Contains the referer of the page for an action and improves the correlation results. |
| `x-dtc` | Contains information for correlation of cross-origin XHRs. |
| `Cookie` | Sets the `dtCookie` cookie in case the HTTP request doesn't contain any. |
| `X-Ruxit-Forwarded-For` | Used to track proxy scenarios by the NGINX code module. |
| `X-ruxit-Apache-ServerNamePorts` | Used by the Apache code module to synchronize service naming with the PHP code module. |
| `X-ruxit-Disposition` | Used by the IIS code module to declutter .NET code module subpaths. |
| `Accept-Encoding` | Discarded by the Apache code module during the fine-tuning of HTML injection behavior. |
| `Content-Encoding` | Discarded during the fine-tuning of HTML injection behavior. |
| `If-None-Match` | Discarded when caching is suppressed. |
| `If-Not-Modified-Since` | Discarded when caching is suppressed. |
| `If-Match` | Modified when caching is suppressed. |
| `If-Range` | Modified when caching is suppressed. |
| `traceparent` | Used for W3C tagging. |
| `tracestate` | Used for W3C tagging. |
| `referer` | Contains the address of the previous web page from which a link to the currently requested page was followed. |
| `user-agent` | Used for [browser and OS detection](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems."). |
| `x-host` | Contains the host information on non-http(s) domains. |

### Response headers

| Header | Purpose |
| --- | --- |
| `X-OneAgent-JS-Injection` | Confirms that the RUM JavaScript has been injected to avoid duplicate injection.  Has one of the following values:  * `true`: the injection has been completed. * `block`: the injection must not be attempted at this time. |
| `X-ruxit-JS-Agent` | Confirms that the RUM JavaScript has been injected to avoid duplicate injection.  Has one of the following values:  * `true`: the injection has been completed. * `block`: the injection must not be attempted at this time. |
| `x-dtHealthCheck` | Contains the results of the RUM JavaScript injection diagnostics performed by Dynatrace Support. |
| `x-dtAgentId` | If the RUM health check is enabled, any involved OneAgent code module adds its ID here. Set for responses to special requests. |
| `x-dtInjectedServlet` | Contains the fully qualified name of the injected servlet or filter. |
| `Set-Cookie` | Sets the session state cookie of OneAgent. |
| `ETag` | OneAgent appends a custom string to the original `ETag` response header to track the changes in the application configuration. |
| `Last-modified` | If the `ETag` response header is manipulated, OneAgent also subtracts 1 second from the original value of this header. Set for responses to special requests. |
| `Content-Length` | Adapted upon HTML injection. Set for responses to special requests. |
| `Vary` | Adapted during HTML injection into compressed responses. Set for responses to special requests. |
| `Content-Encoding` | Adapted during HTML injection into compressed responses. |
| `Content-Type` | Set for responses to special requests. |
| `Access-Control-Allow-Origin` | Set for responses to special requests. |
| `Cache-Control` | Set for responses to special requests. |
| `Server-Timing` | Used to transport information that is relevant for RUM correlation. |
| `Timing-Allow-Origin` | Allows the RUM JavaScript to access the information that is relevant for RUM correlation in case of cross-origin requests. |
| `Access-Control-Allow-Headers` | Set for responses to special requests. |
| `Access-Control-Allow-Methods` | Set for responses to special requests. |
| `Access-Control-Max-Age` | Set for responses to special requests. |

## Cookies

RUM uses the following cookies. All of these must be able to reach Dynatrace. For more details on how Dynatrace uses cookies, and for an explanation of the `<suffix>` used in the table, see [Cookies and client-side storage for RUM and Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.").

| Cookie | Max size | Purpose |
| --- | --- | --- |
| `dtCookie<suffix>` | No set limitation, but usually less than 100 B | Tracks a visit across multiple requests. |
| `dtPC<suffix>` | 58 B | Identifies proper endpoints for beacon transmission; includes session ID for correlation. |
| `dtSa<suffix>` | Max URL length | Serves as an intermediate store for page-spanning actions. |
| `dtValidationCookie<suffix>` | Length of `dTValidationCookieValue` string, that is `23` | Determines the top-level domain. |
| `rxVisitor<suffix>` | 45 B | Contains the visitor ID to correlate sessions. |
| `rxvt<suffix>` | 27 B | Includes the timestamp of the session timeout. |
| `dtsrVID<suffix>`[1](#fn-1-1-def) | 20 B | Specifies the ID of the current recorded view. |
| `dtSR<suffix>`[2](#fn-1-2-def) | 81 B | If Session Replay is enabled, stores the required values to keep the recording consistent through pages. |

1

`dtsrVID` cookie exists from RUM JavaScript version 1.325+ to RUM JavaScript version 1.333.

2

The optional cookie `dtSR` is available from RUM JavaScript version 1.335+.

## Mobile RUM

For RUM Classic, OneAgent for Mobile tags HTTP requests with the `x-dynatrace` header. Dynatrace uses this header to link the mobile part of a web request with the service part captured by another OneAgent. For the New RUM Experience, OneAgent for Mobile tags HTTP requests using the `traceparent` and `tracestate` headers.

For hybrid applications, the `dtAdk` cookie allows to join a session from OneAgent for Mobile and a session from the RUM JavaScript so that these sessions appear as a single session, while the `dtAdkSettings` cookie is used for syncing settings between OneAgent for Mobile and the RUM JavaScript.

`/mbeacon` is the monitor signal that OneAgent for Mobile sends back to Dynatrace if the data is transferred through ActiveGate. If the data is sent to another OneAgent, the monitor signal is `/dtmb`.