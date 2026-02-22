---
title: Configure the Real User Monitoring code source
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source
scraped: 2026-02-22T21:16:49.082544
---

# Configure the Real User Monitoring code source

# Configure the Real User Monitoring code source

* How-to guide
* 4-min read
* Updated on Nov 21, 2025

In the majority of RUM scenarios, at least one additional request for monitoring code is issued by the browser:

* All snippet formats except for [inline code](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") include monitoring code as an external resource, which is requested separately by the browser.
* The monitoring code for Session Replay is always requested separately, even if the used tag format is inline code.

The default URL of the requested monitoring code depends on the injection method used for your application.

* **Agentless applications:** If you opted for [agentless monitoring](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), the monitoring code is requested from the Dynatrace CDN. In case of the tag format [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), the filename ends with `_complete.js` and contains an application identifier (for example, `7cab1abeacdfe1_complete.js`). For all other formats, it starts with `ruxitagent_` and contains information about the active code modules and monitoring code version (for example, `ruxitagent_ICA7NQVfqrtux_10307250124095659.js`). The filename of the Session Replay monitoring code starts with `ruxitagent_` (for example, `ruxitagent_D_10307250124095659.js`) for all tag formats.
* **Automatic injection:** If the [RUM JavaScript is injected automatically](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), both RUM and Session Replay monitoring code are requested from your web or application server using a root-relative URL where the filename starts with `ruxitagentjs_` and contains information about the active code modules and monitoring code version (for example, `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js` or `/myapplication/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`).
* **Manual insertion for pages of an auto-injected application:** If the [RUM JavaScript is inserted manually even though your process groups are instrumented with OneAgent](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), the monitoring code, like with automatic injection, is requested from your web or application server using a root-relative URL where the filename starts with `ruxitagentjs_`. The only exception here is the tag format JavaScript tag, where the RUM monitoring code is requested from the CDN and the filename ends with `_complete.js`. The Session Replay monitoring code is requested from your web or application server and has a filename starting with `ruxitagentjs_` for all tag formats.

You usually don't need to do this, but there are certain scenarios where you might need to use an alternative monitoring code source configuration. For example:

* If your infrastructure blocks monitoring code requests of an auto-injected application because of their default URL path.
* If you prefer monitoring code requests not to be handled on the web or application server that hosts your application.
* If you want to prevent ad blockers from blocking the monitoring code.

The following sections describe alternative configurations that allow you to accommodate these constraints.

## Auto-injected app Modify the monitoring code URL path

Depending on your infrastructure and its configuration, it's possible that requests for monitoring code can't pass with their automatically chosen URL path and thus can't be handled by OneAgent. To solve this, you can change the part of the URL that comes before the `ruxitagentjs_` prefix.

To modify the RUM monitoring code URL path for an auto-injected application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Automatic injection**.
5. In the **Real User Monitoring code source** dropdown list, select **OneAgent**.
6. In **Specify path for RUM monitoring code**, enter the relative monitoring code URL path.

Note that you can't eliminate the path segment prefixed by `ruxitagentjs_`, which is necessary for the identification of the request as a monitoring code request.

#### Examples

The following examples assume that the monitoring code is requested from `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js` by default.

* **Root-relative URL:** If you configure the path `/custompath`, the monitoring code will be requested from `/custompath/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
* **Relative URL:** If you configure the path `./`, the URL where the monitoring code is requested from is relative to the current page. For example:

  + If the current page is `/shop/index.html`, then the monitoring code is requested from `/shop/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
  + If the current page is `/account/dashboard/`, then the monitoring code is requested from `/account/dashboard/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.

This configuration is not only effective for automatic injection, but also for [manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). The only exception is the `_complete.js` request for the JavaScript tag format, which will still go to the Dynatrace CDN.

## Auto-injected app Request the monitoring code from the Dynatrace CDN

Note that all connected ActiveGates must be on ActiveGate version 1.310+ for at least 30 days before this feature becomes available.

If you want the monitoring code for an auto-injected application to be requested from the Dynatrace CDN instead of OneAgent, follow the steps below.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Automatic injection**.
5. In the **Real User Monitoring code source** dropdown list, select **CDN**.

This configuration is effective for both automatic injection and [manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). Using it, filenames previously starting with `ruxitagentjs_` will start with `ruxitagent_` instead.

## Configure a custom monitoring code filename prefix

After changing the monitoring code filename prefix, you may experience a temporary reduction in collected RUM data. Therefore, we recommend avoiding frequent changes to this setting.

By default, the monitoring code filename is prefixed with `ruxitagent` or `ruxitagentjs`, unless the tag format JavaScript tag is used. Alternatively, you can specify a custom prefix, which will be used instead for both agentless and auto-injected applications, as well as for both RUM and Session Replay monitoring code.

To specify a custom monitoring code filename prefix

1. Go to **Settings** > **Web and mobile monitoring** > **RUM monitoring code filename**.
2. In **Custom filename prefix**, enter the desired custom prefix.