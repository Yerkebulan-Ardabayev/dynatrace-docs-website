---
title: Enable the New RUM Experience for your RUM Classic web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps
scraped: 2026-02-24T21:23:22.151133
---

# Enable the New RUM Experience for your RUM Classic web applications

# Enable the New RUM Experience for your RUM Classic web applications

* Latest Dynatrace
* How-to guide
* Updated on Jan 28, 2026

If you already monitor your web frontends with RUM Classic, upgrading to the New RUM Experience requires only a configuration change. This guide outlines the prerequisites and necessary steps.

## Prerequisites

Before enabling the New RUM Experience, make sure the following conditions are met.

#### Required to enable the setting

* RUM Classic is enabled at the levelâfrontend or environmentâwhere you want to enable the New RUM Experience.
* The RUM JavaScript version is RUM JavaScript version 1.317+.
* The snippet format code snippet, which is not supported by the New RUM Experience, isn't used. For alternatives, see [Recommendations for selecting the snippet format](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#snippet-format-recommendations "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").

#### Required to capture and ingest data

* The OneAgent version is OneAgent version 1.301+.
* Because new features are added regularly, we recommend keeping both OneAgent and the RUM JavaScript up to date. The RUM JavaScript version should be configured to either **Latest stable** or **Previous stable**, as described in [Configure the RUM JavaScript version for a frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/rum-javascript-version#configure-js-version "Learn how to control the RUM JavaScript version used to monitor your frontends in the New RUM Experience.").

## Enable the New RUM Experience for a web frontend

To enable the New RUM Experience for a web frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. Switch to the **Settings** tab.
5. Under **Enablement and cost control**, turn on **RUM**.
6. Optionally, enable **User Interactions** to capture user interactions such as clicks and scrolls.

If you use automatic injection, the new configuration is applied within 5 minutes. If you insert the RUM JavaScript manually, you may need to update the snippet, depending on the [snippet format](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") youâre using:

* **JavaScript tag**: The new configuration is applied automatically, but it may not take effect immediately due to caching. The file that contains the monitoring code and configuration is cached for one hour on the Dynatrace CDN. Additionally, browsers respect the [configured cache duration](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#cache-duration "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").
* **OneAgent JavaScript tag**, **OneAgent JavaScript tag with SRI** or **inline code**: As with any configuration change, you need to update the inserted snippet.

## Enable the New RUM Experience at the environment level

To enable the New RUM Experience for web frontends at the environment level

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Traffic and cost control** > **Web frontends**.
2. Turn on **Enable New Real User Monitoring Experience**. Note that this setting is displayed only if **Enable Real User Monitoring Classic** is enabled; see [Prerequisites](#prerequisites).

## Enable the New RUM Experience via API

The Settings API allows you to enable the New RUM Experience either for a web frontend or at the environment level. For details, see [Settings API - Enablement and cost control schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-enablement "View builtin:rum.web.enablement settings schema table of your monitoring environment via the Dynatrace API.").

Unless you use the **JavaScript tag** snippet format, you need to update the snippet after you've enabled the New RUM Experience if it was manually inserted. For more information, see [Enable the New RUM Experience for a web frontend](#enable-new-rum-for-web-frontend). To retrieve the updated snippet, use the [RUM manual insertion tags API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API").

## Related topics

* [Transition from RUM Classic to the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/transition-from-rum-classic "Learn how to transition from RUM Classic to the New RUM Experience.")