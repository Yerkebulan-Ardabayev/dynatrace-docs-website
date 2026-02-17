---
title: Link cross-origin XHR user actions and their distributed traces
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs
scraped: 2026-02-17T21:29:55.400549
---

# Link cross-origin XHR user actions and their distributed traces

# Link cross-origin XHR user actions and their distributed traces

* How-to guide
* 4-min read
* Updated on Oct 01, 2025

If you're experiencing issues linking user actions to their corresponding traces, also refer to [Troubleshooting RUM correlation issues for web applicationsï»¿](https://dt-url.net/io63ls2).

Dynatrace links user actions and their corresponding [distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") to provide gapless end-to-end visibility. For example, this allows you to determine the [top 3 web requests contributors](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#top-3-web-request-contributors "Understand how you can access user action detail pages and analyze user actions.") on the user action details page or to drill down from the [waterfall analysis chart](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis#purepath-drilldown "Learn how to analyze all user action monitoring data through waterfall analysis.") to distributed traces.

Linking user actions and their distributed traces works out of the box when the following conditions are met:

* The web request is a same-origin request: the web request target URL and the page where the request was issued have the same protocol, host, and port. In this case, browsers include the RUM cookies on the web request, which are required for user action to distributed trace correlation.
* The technology used on the first instrumented tier (the tier nearest to the browser) is listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). For these technologies, OneAgent adds and evaluates RUM cookies.

Dynatrace cannot automatically link cross-origin XHR actions and their corresponding distributed traces. To enable such a correlation, follow one of the approaches:

* [Include cookies in cross-origin XHR calls](#include-cookies-in-cross-origin-xhr-calls-cookies-in-xhr-calls)
* [Use the `x-dtc` header](#use-the-x-dtc-header-x-dtc-header)

## Include cookies in cross-origin XHR calls

By default, browsers do not include cookies in cross-origin requests due to the [same-origin policyï»¿](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), which restricts how your page interacts with resources from another origin. You can use [CORS requests with credentialsï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#requests_with_credentials) to add the RUM cookies and thus link cross-origin XHRs and their distributed traces.

For this approach, the following prerequisites must be met:

* The technology used on the first instrumented tier is listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* The two domains involved have at least a common [effective top-level domain plus one (eTLD+1)ï»¿](https://web.dev/same-site-same-origin/) to allow the specification of a common [cookie domain](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain "Learn when and how to configure the cookie domain.").

To include cookies in cross-origin XHR calls

1. In your JavaScript code, set the [`withCredentials` propertyï»¿](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) on the XMLHttpRequest object to `true`. If you use Fetch, set the [`credentials` propertyï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials) to `include`.
2. Configure the server that handles the web request to respond with an `Access-Control-Allow-Credentials: true` header and an `Access-Control-Allow-Origin` header that contains the specific origin (that is, not a wildcard).
3. If you [configure the cookie domain manually](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#manual-cookie-domain-config "Learn when and how to configure the cookie domain."), make sure that you choose one that covers both of the domains involved. If [automatic cookie domain determination](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#automatic-cookie-domain-determination "Learn when and how to configure the cookie domain.") is used, which is the default, then the determined cookie domain already meets this requirement.

When the cross-origin XHR action uses an HTTP method, request header, or content type that requires the browser to issue a [preflight requestï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), Dynatrace cannot link this preflight, since preflight requests do not contain cookies.

## Use the `x-dtc` header

To follow the cookie-based approach described above, the involved domains must allow the specification of a common cookie domain. The header-based approach does not have this limitation. This approach is supported for the technologies listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and by the [OneAgent extension for AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.").

The `x-dtc` header is a custom HTTP header added by the RUM JavaScript and contains information that is otherwise propagated using the RUM cookies. Its addition needs to be explicitly enabled because the endpoints that handle the cross-origin requests need to be configured to accept the header.

Do not enable the addition of the `x-dtc` header unless you acknowledge the following:

* The addition of the `x-dtc` header to link cross-origin XHR user actions and their distributed traces is optional.
* You understand the steps required to prepare your endpoints.
* If you do not configure your endpoints correctly before enabling the header addition, your web application may break.
* You fully accept that Dynatrace is neither responsible nor liable for any application malfunction caused by any misconfiguration.
* You should always enable the addition of the `x-dtc` header in a test environment first.

To link cross-origin XHR user actions and their distributed traces using the `x-dtc` header, configure endpoints to accept `x-dtc`, and then add a regex that matches XHR calls.

1. Configure the endpoints that handle the cross-origin requests to accept the `x-dtc` header. The endpoints must handle the [preflight requestsï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests) that the browser issues due to the addition of the header. In particular, the responses to the preflight requests need to contain an `Access-Control-Allow-Headers: x-dtc` header. Otherwise, the XHR will fail with a CORS error.
2. In Dynatrace, go to **Web**.
3. Select the application that you want to configure.
4. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
5. From the application settings, select **Capturing** > **Advanced setup**.
6. Under **Enable Real User Monitoring for cross-origin XHR calls**, specify a regular expression that matches the XHR calls.

If the `x-dtc` header is not added to the request after following the directions above, check your regular expression and ensure that [RUM is configured to capture XHR actions](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

Only the actual request can be linked not the preflight request.