---
title: Modify Content Security Policy for RUM
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum
scraped: 2026-05-12T11:34:29.332705
---

# Modify Content Security Policy for RUM

# Modify Content Security Policy for RUM

* How-to guide
* 5-min read
* Updated on Mar 13, 2026

[Content Security Policy (CSP)ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) is a web standard designed to protect applications from cross-site scripting and other code injection attacks. CSP rules are most commonly defined using the `Content-Security-Policy` response header. Alternatively, they can also be set using a `<meta>` tag placed in the `<head>` section of the HTML document.

If your application has CSP rules in place, they may block the execution of the RUM JavaScript or prevent it from sending RUM beacons to the beacon endpoint.
This page explains how to modify your CSP to ensure that RUM can operate as intended.

The use of CSP nonces and hashes is not supported for the RUM JavaScript. If you need to verify the integrity of the RUM monitoring code, we recommend using Subresource Integrity (SRI) instead. For details, see [Use Subresource Integrity (SRI) for Real User Monitoring code](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.").

## Allow the loading of external monitoring code

Unless you're using the snippet format [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") and have Session Replay disabled, at least part of the monitoring code is included in your application as an external file. To ensure proper functionality, your CSP rules must allow the loading and execution of scripts from the [RUM monitoring code source](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.").

* For **agentless applications**, the monitoring code is loaded from your CDN.
* For **automatic injection**, the monitoring code is, by default, served by the OneAgent that instruments your web or application server. However, you can configure it to load from your CDN instead. See [Request the monitoring code from your CDN](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.") for details.
* If the [RUM JavaScript is inserted manually even though your process groups are instrumented with OneAgent](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), the code source configured for automatic injection is used. The only exception is the snippet format [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), which always loads the monitoring code from your CDN.

To allow the loading and execution of the monitoring code, the `script-src` directive in your CSP rules must include the `'self'` keyword if the code is served by OneAgent, and your CDN URL if the monitoring code is served from there.

## Allow the execution of inline code

If you use the snippet formats [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") or [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), the `script-src` directive in your CSP rules must include the `'unsafe-inline'` keyword to allow the execution of the monitoring code.

## Allow sending RUM beacons

RUM beacons are sent to a beacon endpoint, with the default endpoint varying based on the application type:

* For **agentless applications**, beacons are, by default, reported to a Cluster ActiveGate.
* For **auto-injected applications**, beacons are, by default, reported to the OneAgent that instruments the web or application server where the application is hosted.

Alternative setups are described in [Configure beacon endpoint for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

To allow the RUM JavaScript to send beacons, ensure that your CSP rules include the appropriate endpoint in the `connect-src` directive.

* Use the `'self'` keyword if the beacon endpoint is the OneAgent that instruments the application.
* If you configured a OneAgent that instruments a different web server as a beacon endpoint, specify the corresponding URL.
* If the beacons are handled by a Cluster ActiveGate, use the beacon endpoint URL shown in the UI.

To find the URL for a Cluster ActiveGate

1. Go to **Web**.
2. Select the application you're adjusting the CSP rules for.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **General settings** > **Beacon endpoint**.
5. Copy the URL next to **Configured beacon endpoint**.

## Allow Session Replay

If you use Session Replay, your CSP rules must allow the RUM JavaScript to load code as a blob. For details, see [Modify Content Security Policy for Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-csp "Configure monitoring consumption and data privacy settings for Session Replay.").

Additionally, even if you're using the snippet format [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case"), make sure your CSP rules [allow the loading of external monitoring code](#allow-external-monitoring-code). This is important because the monitoring code for Session Replay is always requested as an external file, regardless of the snippet format.

## Examples

Below is a basic example of a simple CSP rule:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';
```

The following examples show how this rule needs to be adapted for different RUM scenarios.

Examples for automatic injection

If you're using automatic injection with the default configuration for both the beacon endpoint and the monitoring code source, the basic CSP rule above is sufficientâas long as Session Replay is not enabled, and the snippet format [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") is used.

If the snippet format is changed to inline code or code snippet, you must allow inline scripts by adding `'unsafe-inline'`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self';
```

If the monitoring code is loaded from the CDN, update the `script-src` directive accordingly:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self';
```

If the beacon endpoint is changed to a Cluster ActiveGate, update the `connect-src` directive:

```
Content-Security-Policy: script-src 'self'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

If you use Session Replay, you also need to configure the `worker-src` directive:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';  worker-src blob:;
```

Examples for agentless monitoring

For agentless monitoring, both `script-src` and `connect-src` must be adjusted:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

If you're using inline code, include `'unsafe-inline'` in `script-src`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

If you're using the code snippet format, include both `'unsafe-inline'` and the code source URL in `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

If beacons are sent to an instrumented web or app server, include its URL in `connect-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' http://www.example.com/rb_abcdefghi;
```

If you use Session Replay, you need to configure the `worker-src` directive:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```

If you use Session Replay with the code snippet or inline code format, you need to configure the `worker-src` directive and include both `'unsafe-inline'` and the code source URL in `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```