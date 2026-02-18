---
title: Adapt CSP rules for the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules
scraped: 2026-02-18T21:32:40.002567
---

# Adapt CSP rules for the New RUM Experience

# Adapt CSP rules for the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

[Content Security Policy (CSP)ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) is a web standard designed to protect applications from cross-site scripting and other code injection attacks. CSP rules are most commonly defined using the `Content-Security-Policy` response header. Alternatively, they can also be set using a `<meta>` tag placed in the `<head>` section of the HTML document.

If your application has CSP rules in place, they may block the execution of the RUM JavaScript or prevent it from sending RUM beacons to the beacon endpoint.
This page explains how to modify your CSP to ensure that RUM can operate as intended.

The use of CSP nonces and hashes is not supported for the RUM JavaScript. If you need to verify the integrity of the RUM monitoring code, we recommend using Subresource Integrity (SRI) instead. For details, see [Use Subresource Integrity (SRI) in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature in the New RUM Experience to ensure the integrity of Real User Monitoring code.").

## Allow the loading of external monitoring code

Unless you're using the snippet format [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") and have Session Replay Classic disabled, at least part of the monitoring code is included in your application as an external file. To ensure proper functionality, your CSP rules must allow the loading and execution of scripts from the [RUM monitoring code source](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source "Configure the Real User Monitoring code source in the New RUM Experience to meet your specific requirements.").

* For **agentless frontends**, the monitoring code is loaded from the Dynatrace CDN.
* For **automatic injection**, the monitoring code is, by default, served by the OneAgent that instruments your web or application server. However, you can configure it to load from the Dynatrace CDN instead. See [Request the monitoring code from the Dynatrace CDN](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source in the New RUM Experience to meet your specific requirements.") for details.
* If the [RUM JavaScript is inserted manually even though your process groups are instrumented with OneAgent](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience."), the code source configured for automatic injection is used. The only exception is the snippet format [JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), which always loads the monitoring code from the Dynatrace CDN.

To allow the loading and execution of the monitoring code, the `script-src` directive in your CSP rules must include the `'self'` keyword if the code is served by OneAgent, and `https://js-cdn.dynatracelabs.com` if it is served from the Dynatrace CDN.

## Allow the execution of inline code

If you use the snippet format [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), the `script-src` directive in your CSP rules must include the `'unsafe-inline'` keyword to allow the execution of the monitoring code.

## Allow sending RUM beacons

RUM beacons are sent to a beacon endpoint, with the default endpoint varying based on the frontend type:

* For **agentless frontends**, beacons are, by default, reported to a Cluster ActiveGate that is part of the Dynatrace SaaS infrastructure.
* For **auto-injected frontends**, beacons are, by default, reported to the OneAgent that instruments the web or application server where the application is hosted.

Alternative setups are described in [Configure the beacon endpoint for web frontends in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements.").

To allow the RUM JavaScript to send beacons, ensure that your CSP rules include the appropriate endpoint in the `connect-src` directive.

* Use the `'self'` keyword if the beacon endpoint is the OneAgent that instruments the application.
* If you configured a OneAgent that instruments a different web server as a beacon endpoint, specify the corresponding URL.
* If the beacons are handled by a Cluster ActiveGate, use the beacon endpoint URL shown in the UI.

To find the URL for a Cluster ActiveGate

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. Copy the URL next to **Configured beacon endpoint**.

## Allow Session Replay Classic

If you use Session Replay Classic, your CSP rules must allow the RUM JavaScript to load code as a blob. For details, see [Modify Content Security Policy for Session Replay](/docs/observe/digital-experience/session-replay/configure-session-replay-web#sr-csp "Configure monitoring consumption and data privacy settings for Session Replay.").

Additionally, even if you're using the snippet format [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), make sure your CSP rules [allow the loading of external monitoring code](#allow-external-monitoring-code). This is important because the monitoring code for Session Replay Classic is always requested as an external file, regardless of the snippet format.

## Examples

Below is a basic example of a simple CSP rule:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';
```

The following examples show how this rule needs to be adapted for different RUM scenarios.

Examples for automatic injection

If you're using automatic injection with the default configuration for both the beacon endpoint and the monitoring code source, the basic CSP rule above is sufficientâas long as Session Replay Classic is not enabled, and the snippet format [OneAgent JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#oneagent-js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") is used.

If the snippet format is changed to inline code, you must allow inline scripts by adding `'unsafe-inline'`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self';
```

If the monitoring code is loaded from the CDN, update the `script-src` directive accordingly:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self';
```

If the beacon endpoint is changed to a Cluster ActiveGate, update the `connect-src` directive:

```
Content-Security-Policy: script-src 'self'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

If you use Session Replay Classic, you also need to configure the `worker-src` directive:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';  worker-src blob:;
```

Examples for agentless monitoring

For agentless monitoring, both `script-src` and `connect-src` must be adjusted:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

If you're using inline code, include `'unsafe-inline'` in `script-src`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

If beacons are sent to an instrumented web or app server, include its URL in `connect-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' http://www.example.com/rb_abcdefghi;
```

If you use Session Replay Classic, you need to configure the `worker-src` directive:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf; worker-src blob:;
```

If you use Session Replay Classic with the inline code format, you need to configure the `worker-src` directive and include both `'unsafe-inline'` and the code source URL in `script-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com 'unsafe-inline'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf; worker-src blob:;
```