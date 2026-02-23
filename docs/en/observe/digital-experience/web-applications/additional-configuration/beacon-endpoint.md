---
title: Configure beacon endpoint for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint
scraped: 2026-02-23T21:22:44.196010
---

# Configure beacon endpoint for web applications

# Configure beacon endpoint for web applications

* How-to guide
* 6-min read
* Updated on Nov 21, 2025

The RUM JavaScript sends RUM beacons to report the captured data to Dynatrace. By default, the beacon endpoint depends on the injection method used for your application.

* **Auto-injected applications:** When the [RUM JavaScript is injected automatically](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), beacons are sent back to your web or application server using a root-relative URL where the last path segment has the `rb_` prefix (for example, `/rb_xxxxxxxxxx` or `/myapplication/rb_xxxxxxxxxx`). The beacon endpoint is provided by OneAgent, which intercepts and forwards RUM beacons.
* **Agentless applications:** If you opted for [agentless monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), data is sent to a beacon endpoint that is part of the Dynatrace SaaS infrastructure.

You usually don't need to change the default beacon endpoint, but there are certain scenarios where you might need to use an alternative beacon endpoint configuration. For example:

* If your infrastructure blocks beacons of an auto-injected application because of their default URL path.
* If you want the monitoring traffic of an auto-injected application to bypass your CDN.
* If you prefer RUM beacons not to be handled on the web or application server that hosts your application.

The following sections describe alternative beacon endpoint configurations that allow you to accommodate these and similar constraints.

The beacon endpoint configurations explained on this page don't affect the correlation between user actions and distributed traces. However, check [Technology support](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.") to see if Real User Monitoring is supported for your technology.

## Auto-injected app Modify the beacon endpoint URL

Depending on your infrastructure and its configuration, it's possible that beacons can't pass with their automatically chosen URL path and thus can't be handled by OneAgent. To solve this, you can change the part of the beacon endpoint URL that comes before the `rb_` prefix.

To modify the beacon endpoint URL for an auto-injected application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **General settings** > **Beacon endpoint**.
5. In the **Type** dropdown list, select **OneAgent**.
6. In **URL**, enter the relative beacon endpoint URL.

Note that you can't remove the path segment prefixed by `rb_`, as itâs required for OneAgent to identify RUM beacons.

#### Examples

The following examples assume that RUM beacons are sent to `/rb_bf12345abc` by default.

* **Root-relative URL:** If you set **URL** to `/custompath`, the beacons will be sent to `/custompath/rb_bf12345abc`.
* **Relative URL:** If you set **URL** to `./`, then the URL where the RUM JavaScript sends beacons is relative to the current page. For example:

  + If the current page is `/shop/index.html`, then the beacons are sent to `/shop/rb_bf12345abc`.
  + If the current page is `/account/dashboard/`, then the beacons are sent to `/account/dashboard/rb_bf12345abc`.

## Auto-injected app Send beacons to Dynatrace SaaS infrastructure

If you want the RUM beacons of an auto-injected application to be handled by the Dynatrace SaaS infrastructure instead of OneAgent, follow the steps below.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **General settings** > **Beacon endpoint**.
5. In the **Type** dropdown list, select **Cluster ActiveGate**.

For this configuration, Dynatrace applies the [beacon origin allowlist](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") to the RUM beacons of your application.

## Auto-injected app Send beacons to a different web server

By default, the RUM beacons of an auto-injected application are handled by one of the process groups that hosts your application. Alternatively, beacons can be handled on any other instrumented web or application server of a technology listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To send beacons of an auto-injected application to a different instrumented server

1. In the injected RUM JavaScript, find `reportUrl` and copy the last segment of the URL path, which is prefixed with `rb_`.
2. Append this value to the URL of the instrumented web or application server.

   For example, if the last segment of `reportUrl` is `/rb_abcdefghi` and the server URL is `http://www.my-server.com`, the resulting beacon endpoint URL is `http://www.my-server.com/rb_abcdefghi`.
3. Go to **Web**.
4. Select the application that you want to configure.
5. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
6. From the application settings, select **General settings** > **Beacon endpoint**.
7. In the **Type** dropdown list, select **OneAgent**.
8. In **URL**, enter the beacon endpoint that you determined in step 2.
9. Turn on **Send beacon data via CORS**.

For this configuration, Dynatrace applies the [beacon origin allowlist](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") to the RUM beacons of your application.

## Agentless app Send beacons to a web server

Instead of using the Dynatrace SaaS infrastructure as a beacon endpoint for your agentless application, you can use any instrumented web or application server of a technology listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

To send beacons of an agentless application to an instrumented server

1. Go to **Web**.
2. Select any **auto-injected** application that doesn't use one of the custom beacon endpoint configurations described on this page.

   In this step, you should select not the agentless application that you're configuring but another **auto-injected** application that has the default beacon endpoint configuration. If you don't have an auto-injected application, temporarily create one as described in [Define applications for Real User Monitoring | Application detection rules approach](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). You can then [delete](/docs/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.") this temporary application.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Manual insertion**.
5. Under **OneAgent JavaScript tag**, find `reportUrl` in the provided snippet, and copy its value.
6. Append the `reportUrl` value to the URL of the instrumented web or application server.

   For example, if the `reportUrl` value is `/rb_abcdefghi` and the server URL is `http://www.my-server.com`, the resulting beacon endpoint URL is `http://www.my-server.com/rb_abcdefghi`.
7. Go to **Web**.
8. Select the agentless application that you want to configure.
9. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
10. From the application settings, select **General settings** > **Beacon endpoint**.
11. In the **Type** dropdown list, select **OneAgent**.
12. In **URL**, enter the beacon endpoint that you determined in step 6.
13. Turn on **Send beacon data via CORS**.

For this configuration, Dynatrace applies the [beacon origin allowlist](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") to the RUM beacons of your application (the same is done for the default beacon endpoint configuration for all agentless applications).