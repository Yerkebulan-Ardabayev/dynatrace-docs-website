---
title: Configure the Real User Monitoring code source in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source
scraped: 2026-02-15T09:11:40.283133
---

# Configure the Real User Monitoring code source in the New RUM Experience

# Configure the Real User Monitoring code source in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 28, 2026

In the majority of RUM scenarios, at least one additional request for monitoring code is issued by the browser:

* All snippet formats except for [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") include monitoring code as an external resource, which is requested separately by the browser.
* The monitoring code for Session Replay Classic is always requested separately, even if the used snippet format is inline code.

The Real User Monitoring code source determines where the monitoring code is loaded from and which URL is used for these requests.

## Default behavior

By default, a monitoring code source is applied that is suitable for most environments and varies based on the instrumentation method used for your frontend. This section describes the default behavior in detail, and the next outlines configuration options for scenarios that require customization.

### Agentless monitoring

If you opted for [agentless monitoring](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience."), the monitoring code is requested from the Dynatrace CDN. In case of the snippet format [JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), the filename ends with `_complete.js` and contains a frontend identifier (for example, `7cab1abeacdfe1_complete.js`). For all other formats, it starts with `ruxitagent_` and contains information about the active code modules and monitoring code version (for example, `ruxitagent_ICA1589ENPQRTUVXfghqru_10307250124095659.js`). The filename of the Session Replay Classic monitoring code starts with `ruxitagent_` (for example, `ruxitagent_D_10307250124095659.js`) for all snippet formats.

### Automatic injection

If the [RUM JavaScript is injected automatically](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."), both RUM and Session Replay Classic monitoring code are requested from your web or application server using a root-relative URL where the filename starts with `ruxitagentjs_` and contains information about the active code modules and monitoring code version. The exact URL path depends on the technology:

* **Java or IIS:** The filename is added to the context root if available, for example: `/contextroot/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js`.
* **Other technologies or when a context root is unavailable:** The filename is added to the root, for example: `/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js`. This is also the default if you manually insert the RUM JavaScript as described in [Use manual insertion for pages of an auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.").

### Manual insertion for pages of an auto-injected frontend

If the [RUM JavaScript is inserted manually even though your process groups are instrumented with OneAgent](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience."), the monitoring code, like with automatic injection, is requested from your web or application server using a root-relative URL where the filename starts with `ruxitagentjs_`. The only exception here is the snippet format JavaScript tag, where the RUM monitoring code is requested from the CDN and the filename ends with `_complete.js`. The Session Replay Classic monitoring code is requested from your web or application server and has a filename starting with `ruxitagentjs_` for all snippet formats.

## Configuration options

In certain scenarios, you may need to use an alternative monitoring code source configuration. For example:

* If your infrastructure blocks monitoring code requests of an auto-injected frontend because of their default URL path.
* If you prefer monitoring code requests not to be handled on the web or application server that hosts your application.
* If you want to prevent ad blockers from blocking the monitoring code.

The following configuration options allow you to address these constraints.

### Auto-injected frontend Modify the monitoring code URL path

Depending on your infrastructure and its configuration, it's possible that requests for monitoring code can't pass with their automatically chosen URL path and thus can't be handled by OneAgent. To solve this, you can change the part of the URL path that comes before the `ruxitagentjs_` prefix.

To modify the RUM monitoring code URL path for an auto-injected frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. In the **Real User Monitoring code source** dropdown list, select **OneAgent**.
6. In **Specify path for RUM monitoring code**, enter the relative monitoring code URL path.
7. Select **Save**.

Note that you can't eliminate the path segment prefixed by `ruxitagentjs_`, which is necessary for the identification of the request as a monitoring code request.

#### Examples

The following examples assume that the monitoring code is requested from `/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js` by default.

* **Root-relative URL:** If you configure the path `/custompath`, the monitoring code will be requested from `/custompath/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js`.
* **Relative URL:** If you configure the path `./`, the URL where the monitoring code is requested from is relative to the current page. For example:

  + If the current page is `/shop/index.html`, then the monitoring code is requested from `/shop/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js`.
  + If the current page is `/account/dashboard/`, then the monitoring code is requested from `/account/dashboard/ruxitagentjs_ICA1589ENPQRTUVXfghqru_10307250124095659.js`.

This configuration is not only effective for automatic injection, but also for [manual insertion for pages of an auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience."). The only exception is the `_complete.js` request for the JavaScript snippet format, which will still go to the Dynatrace CDN.

### Auto-injected frontend Request the monitoring code from the Dynatrace CDN

Note that all connected ActiveGates must be on ActiveGate version 1.310+ for at least 30 days before this feature becomes available.

If you want the monitoring code for an auto-injected frontend to be requested from the Dynatrace CDN instead of OneAgent, follow the steps below.

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. In the **Real User Monitoring code source** dropdown list, select **CDN**.
6. Select **Save**.

This configuration is effective for both automatic injection and [manual insertion for pages of an auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience."). Using it, filenames previously starting with `ruxitagentjs_` will start with `ruxitagent_` instead.

### Configure a custom monitoring code filename prefix

After changing the monitoring code filename prefix, you may experience a temporary reduction in collected RUM data. Therefore, we recommend avoiding frequent changes to this setting.

By default, the monitoring code filename is prefixed with `ruxitagent` or `ruxitagentjs`, unless the snippet format JavaScript tag is used. Alternatively, you can specify a custom prefix, which will be used instead for both agentless and auto-injected frontends, as well as for both RUM and Session Replay Classic monitoring code.

To specify a custom monitoring code filename prefix

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Frontend** > **RUM monitoring code filename**.
2. In **Custom filename prefix**, enter the desired custom prefix.
3. Select **Save changes**.