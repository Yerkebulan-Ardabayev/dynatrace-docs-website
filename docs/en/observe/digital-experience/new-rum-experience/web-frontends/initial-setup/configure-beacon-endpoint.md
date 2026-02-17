---
title: Configure the beacon endpoint for web frontends in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint
scraped: 2026-02-17T04:59:47.444177
---

# Configure the beacon endpoint for web frontends in the New RUM Experience

# Configure the beacon endpoint for web frontends in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

The RUM JavaScript sends beacons to Dynatrace to report captured data. The URL where these beacons are delivered is defined by the beacon endpoint. This guide describes the default beacon endpoint, which is suitable for most environments, and then outlines the available configuration options for scenarios that require customization.

## Default beacon endpoint

By default, the beacon endpoint depends on the instrumentation method used for your application:

### Auto-injected frontends

If the [RUM JavaScript is injected automatically](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."), beacons are sent to your web or application server, where OneAgent provides a beacon endpoint that intercepts and forwards them. For this purpose, a root-relative URL is used, with the last path segment prefixed by `rb_`. The exact URL path depends on the technology:

* **Java or IIS:** The path segment is added to the context root if available, for example: `/myapplication/rb_bf12345abc`.
* **Other technologies or when a context root is unavailable:** The path segment is added to the root, for example: `/rb_bf12345abc`. This is also the default if you manually insert the RUM JavaScript as described in [Use manual insertion for pages of an auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.").

### Agentless monitoring

If you use [agentless monitoring](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience."), data is sent to a Cluster ActiveGate that is part of the Dynatrace SaaS infrastructure.

## Configuration options

In certain scenarios, you might need to use an alternative beacon endpoint configuration. For example:

* If your infrastructure blocks beacons of an auto-injected frontend because of their default URL path.
* If you want the monitoring traffic of an auto-injected frontend to bypass your CDN.
* If you prefer RUM beacons not to be handled on the web or application server that hosts your application.

The following sections describe alternative beacon endpoint configurations that allow you to accommodate these and similar constraints.

### Auto-injected frontend Modify the beacon endpoint URL path

Depending on your infrastructure and its configuration, beacons might not pass with their automatically chosen URL and therefore canât be handled by OneAgent. To resolve this, you can change the part of the beacon endpoint URL path that comes before the `rb_` prefix. You can't remove the path segment prefixed by `rb_`, as itâs required for OneAgent to identify RUM beacons.

To modify the beacon endpoint URL for an auto-injected application

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. In the **Type** dropdown list, select **OneAgent**.
7. Under **URL**, enter a relative or root-relative URL.
8. Select **Save changes**.

#### Examples

The following examples assume that RUM beacons are sent to `/rb_bf12345abc` by default.

* **Root-relative URL:** If you set **URL** to `/custompath`, the beacons will be sent to `/custompath/rb_bf12345abc`.
* **Relative URL:** If you set **URL** to `./`, then the URL where the RUM JavaScript sends beacons is relative to the current page. For example:

  + If the current page is `/shop/index.html`, then the beacons are sent to `/shop/rb_bf12345abc`.
  + If the current page is `/account/dashboard/`, then the beacons are sent to `/account/dashboard/rb_bf12345abc`.

### Auto-injected frontend Send beacons to Dynatrace SaaS infrastructure

If you want the RUM beacons of an auto-injected frontend to be handled by Dynatrace SaaS infrastructure instead of OneAgent, follow the steps below.

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. In the **Type** dropdown list, select **Cluster ActiveGate**.
7. Select **Save changes**.

With this configuration, Dynatrace applies the [beacon origin allowlist](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") to the RUM beacons of your frontend.

### Auto-injected frontend Send beacons to a different web server

By default, RUM beacons from an auto-injected frontend are handled by OneAgent on one of the process groups that host your application. Alternatively, beacons can be handled on any other instrumented web or application server of a technology listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To send beacons of an auto-injected frontend to a different instrumented server

1. In the injected RUM JavaScript, find `beaconUri` and copy the last segment of the URL path, which is prefixed with `rb_`.
2. Append this value to the URL of the instrumented web or application server.

   For example, if the last segment of `beaconUri` is `/rb_bf12345abc` and the server URL is `http://www.my-server.com`, the resulting beacon endpoint URL is `http://www.my-server.com/rb_bf12345abc`.
3. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
4. Select  **Web** to view all web frontends.
5. Select the frontend you want to configure.
6. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
7. Go to **Collect and capture** > **Frontend** > **Beacon endpoint**.
8. In the **Type** dropdown list, select **OneAgent**.
9. In **URL**, enter the beacon endpoint that you determined in step 2.
10. Turn on **Send beacon data via CORS**.
11. Select **Save changes**.

With this configuration, Dynatrace applies the [beacon origin allowlist](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") to the RUM beacons of your frontend.