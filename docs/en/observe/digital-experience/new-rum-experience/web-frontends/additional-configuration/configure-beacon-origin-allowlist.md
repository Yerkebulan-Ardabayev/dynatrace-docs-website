---
title: Configure the beacon origin allowlist
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist
scraped: 2026-02-17T05:00:04.578656
---

# Configure the beacon origin allowlist

# Configure the beacon origin allowlist

* Latest Dynatrace
* How-to guide
* Published Feb 04, 2026

To prevent untrusted origins from sending RUM data, Dynatrace provides a beacon origin allowlist. By configuring it, you restrict crossâorigin RUM beacons to only those origins you explicitly approve.

## Understanding sameâorigin and crossâorigin RUM beacons

The RUM JavaScript reports captured data to Dynatrace by sending beacons to a [beacon endpoint](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements."). These beacons can be either sameâorigin or crossâorigin, depending on the instrumentation method and any additional configuration.

The term [originï»¿](https://developer.mozilla.org/en-US/docs/Glossary/Origin) refers to the protocol, host, and port of the URL. A request is considered sameâorigin when the protocol, host, and port of the page sending the request are exactly the same as those of the requested resource.

### Agentless frontends

When [agentless monitoring](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.") is used, RUM beacons are sent to a Cluster ActiveGate that is part of the Dynatrace SaaS infrastructure. These beacons are cross-origin.

### Auto-injected frontends

When the RUM JavaScript is [injected automatically](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."), RUM beacons are, by default, sent back to the web or application server that hosts the frontend, where OneAgent provides a beacon endpoint. These are same-origin beacons.

You can configure alternative beacon endpoint setups where beacons are [sent to a Cluster ActiveGate](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint#auto-injected-to-saas-infrastructure "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements.") or [to another instrumented web server on a different domain](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint#auto-injected-to-different-server "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements."). Since these endpoints use a different domain, the beacons are cross-origin.

## Default CORS handling for beacon requests

Browsers enforce the same-origin policy, which by default allows scripts to send requests only to the same origin. To send cross-origin requests, [Cross-Origin Resource Sharing (CORS)ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) must be used. It allows servers to specify which origins are permitted to access them. Therefore, cross-origin beacons need to be sent using CORS.

In its default CORS handling, the beacon endpoint accepts all origins by adding an `Access-Control-Allow-Origin` header to the response. The header echoes the origin provided in the `Origin` request header. The endpoint then forwards the beacon payload to Dynatrace.

If you send cross-origin beacons to OneAgent, you must turn on the setting **Send beacon data via CORS** for the `Access-Control-Allow-Origin` header to be added; see [Send beacons to a different web server](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint#auto-injected-to-different-server "Learn how to configure the beacon endpoint for web frontends to meet your specific requirements.").

If the permissive default doesnât align with your requirements, use the beacon origin allowlist to specify which origins are accepted.

## Add rules to the beacon origin allowlist

To specify from which origins OneAgents and Cluster ActiveGates should accept RUM beacons, add rules to the beacon origin allowlist.

As soon as you add the first rule, any frontend that doesnât match it will stop collecting RUM data unless its beacons are sent to the same origin and handled by OneAgent.

To add a beacon origin rule

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Frontend** > **Beacon origins for CORS**.
2. Select **Add item**.
3. Under **Matcher**, select **contains**, **starts with**, **ends with** or **equals**.
4. Under **Pattern**, provide a pattern that identifies the origin or origins the rule should accept. An origin consists of the protocol, host, and port; default ports are omitted.

You can add up to 20 beacon origin rules per environment.

## How the beacon origin allowlist is applied

If the beacon's origin specified in the `Origin` request header matches one of the rules in the allowlist, the beacon is accepted. The origin is copied to the `Access-Control-Allow-Origin` response header, and a `200 OK` status code is returned. The beacon payload is forwarded to Dynatrace.

If, on the other hand, the origin doesn't match any rule in the allowlist, the beacon is rejected with a `403 Forbidden` status code and its payload is discarded.

The beacon origin allowlist isn't applied to same-origin beacons. If the allowlist is empty, the default behavior described in [Default CORS handling for beacon requests](#default-cors-handling) is applied.