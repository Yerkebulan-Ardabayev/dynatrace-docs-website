---
title: Select a snippet format in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats
scraped: 2026-02-26T21:27:44.730568
---

# Select a snippet format in the New RUM Experience

# Select a snippet format in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

The RUM JavaScriptâwhether [automatically injected](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.") or [manually inserted](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.") into your web applicationâconsists of two key components:

* **Monitoring code**: The JavaScript code that provides RUM capabilities such as capturing user events.
* **Configuration**: The application configuration that is initially used by the monitoring code. It is updated later via the RUM beacon response in case of configuration changes.

The New RUM Experience provides several snippet formats that integrate these components into your pages in different ways, each tailored to meet specific requirements.

This page [offers guidance](#snippet-format-recommendations) to help you choose the snippet format that best meets your requirements, followed by a [detailed description of each format](#snippet-format-details).

## Recommendations for selecting the snippet format

For most use cases, we recommend the following:

* Use the [JavaScript Tag](#js-tag) for manual insertion.
* Use the [OneAgent JavaScript Tag](#oneagent-js-tag) for automatic injection.

If you want to leverage the subresource integrity (SRI) browser feature to ensure that the monitoring code hasn't been altered, use [OneAgent JavaScript tag with SRI](#oneagent-js-tag-sri) for manual insertion and automatic injection.

To avoid parse-blocking execution of the monitoring code, configure the **script execution** option of your selected snippet format to **async** or **defer**. Instructions for configuring this option are provided in the documentation for each individual snippet format below. Keep in mind that while the monitoring code is not yet fully loaded and initialized, certain timings and user events will be lost.

## Available snippet formats

Below, you'll find all snippet formats available in the New RUM Experience, along with their configuration options. Note that both the New RUM Experience and RUM Classic use the same RUM JavaScript snippet. When the New RUM Experience is enabled, the monitoring code includes additional modules, and the snippet contains extended configuration. However, the underlying snippet remains shared. As a result, any changes you make to the settings described below for the New RUM Experience also apply to RUM Classic.

JavaScript tag

OneAgent JavaScript tag

OneAgent JavaScript tag with SRI

Inline code

**JavaScript tag** links to an external file that includes both the monitoring code and the configuration. JavaScript tag is only available for manual insertion.

[Get JavaScript tag via API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag)

##### Updates

The short cache duration used for the external file ensures regular automatic updates, making JavaScript tag an ideal choice if you don't want to take care of updating the inserted snippet after configuration changes.

##### Monitoring code source

The external file is loaded from the Dynatrace CDN.

##### Cache duration

The external file containing monitoring code and configuration is updated according to its cache duration, which is one hour by default and can be configured. The available values are lowâa few hours or daysâto ensure the configuration is updated regularly. The cache duration specifies how long browsers can cache the file. The Dynatrace CDN caches it for one hour.

To configure the cache duration

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. In the **JavaScript tag** section, use the dropdown under **Cache monitoring code and configuration for** to select the required cache duration.

##### Script execution

By default, the monitoring code is loaded and executed synchronously by the browser. To avoid parse-blocking behavior, you can configure the addition of the `async` or `defer` attributes.

* With the `async` attribute, the monitoring code is loaded in parallel with page parsing and executed immediately once itâs available.
* With the `defer` attribute, the monitoring code is also loaded in parallel, but execution is deferred until after the page has finished parsing.

With both attributes, certain timings and user events will be lost while the monitoring code is not yet fully loaded and initialized.

To configure script execution

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. In the **JavaScript tag** section, set **Script execution attribute** to **async**, **defer**, or **No attribute**.
6. Copy the snippet and insert it into your page.

When fetching the JavaScript tag via the API, you can control script execution by passing a parameter. For details, see [GET JavaScript tag](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.").

##### Addition of the `crossorigin="anonymous"` attribute

ð¢ Enabled by default

The external script referenced by JavaScript tag is served from the Dynatrace CDN, resulting in a cross-origin request. To enable the collection of detailed JavaScript error messages and W3C resource timings, you need to include the `crossorigin="anonymous"` attribute in the script tag.

To enable the addition of the `crossorigin="anonymous"` attribute

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. In the **JavaScript tag** section, enable **Add crossorigin=anonymous attribute**.
6. Copy the snippet and insert it into your page.

When fetching the JavaScript tag via the API, you can control the addition of the `crossorigin="anonymous"` attribute by passing a parameter. For details, see [GET JavaScript tag](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.").

**OneAgent JavaScript tag** includes the configuration and links to an external file containing the monitoring code. It's available for both manual insertion and automatic injection.

[Get OneAgent JavaScript tag via API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag)

##### Updates

When inserting the OneAgent JavaScript tag manually, it must also be manually updated whenever configuration changes occur. To ensure it remains current, we recommend using it together with fully automated updates via the API. Using OneAgent JavaScript tag from the web UI is discouraged unless timely configuration updates are not critical.

In case of automatic injection, OneAgent always injects the OneAgent JavaScript tag using the current configuration. Note, however, that the caching policy of your application may influence how often OneAgent gets a chance to inject. For more information, see [Cache control header optimizations](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Monitoring code source

In case of agentless monitoring, the monitoring code is delivered by the Dynatrace CDN. In case of automatic injection or [manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), the file is, by default, delivered by the OneAgent that instruments your application. Alternatively, it is also possible to load it from the Dynatrace CDN; for details, see [Request the monitoring code from the Dynatrace CDN](/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").

##### Cache duration

Both browsers and the Dynatrace CDN can cache the monitoring code for up to a year. This extended cache duration is made possible by embedding both the RUM JavaScript version and a hash of the active modules in the file URL.

##### Script execution

By default, the monitoring code is loaded and executed synchronously by the browser. To avoid parse-blocking behavior, you can configure the addition of the `async` or `defer` attributes.

* With the `async` attribute, the monitoring code is loaded in parallel with page parsing and executed immediately once itâs available.
* With the `defer` attribute, the monitoring code is also loaded in parallel, but execution is deferred until after the page has finished parsing.

With both attributes, certain timings and user events will be lost while the monitoring code is not yet fully loaded and initialized.

To configure script execution for automatic injection

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. If **Snippet format** is set to **OneAgent JavaScript tag**, the **Script execution attribute** option becomes available. Choose either **async**, **defer**, or **No attribute** from the dropdown.
6. Select **Save**.

To configure script execution for manual insertion

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. In the **OneAgent JavaScript tag** section, set **Script execution attribute** to **async**, **defer**, or **No attribute**.
6. Copy the snippet and insert it into your page.

When fetching the OneAgent JavaScript tag via the API, you can control script execution by passing a parameter. For details, see [GET OneAgent JavaScript tag](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.").

**OneAgent JavaScript tag with SRI** lets you take advantage of the subresource integrity (SRI) browser feature to ensure that the monitoring code hasn't been altered, see [Use Subresource Integrity (SRI) in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature in the New RUM Experience to ensure the integrity of Real User Monitoring code."). It includes configuration, a reference to an external file containing the monitoring code, and an integrity hash for this monitoring code. It is supported for both automatic injection and manual insertion.

[Get OneAgent JavaScript tag with SRI via API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri)

##### Updates

When inserting the OneAgent JavaScript tag with SRI manually, it must also be manually updated whenever configuration changes occur. To ensure it remains current, we recommend using it together with fully automated updates via the API. Using OneAgent JavaScript tag with SRI from the web UI is discouraged unless timely configuration updates are not critical.

In case of automatic injection, OneAgent always injects the OneAgent JavaScript tag with SRI using the current configuration. Note, however, that the caching policy of your application may influence how often OneAgent gets a chance to inject. For more information, see [Cache control header optimizations](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Monitoring code source

The monitoring code is always delivered by the Dynatrace CDN.

##### Cache duration

Both browsers and the Dynatrace CDN can cache the monitoring code for up to a year. This extended cache duration is made possible by embedding both the RUM JavaScript version and a hash of the active modules in the file URL.

##### Script execution

By default, the monitoring code is loaded and executed synchronously by the browser. To avoid parse-blocking behavior, you can configure the addition of the `async` or `defer` attributes.

* With the `async` attribute, the monitoring code is loaded in parallel with page parsing and executed immediately once itâs available.
* With the `defer` attribute, the monitoring code is also loaded in parallel, but execution is deferred until after the page has finished parsing.

With both attributes, certain timings and user events will be lost while the monitoring code is not yet fully loaded and initialized.

To configure script execution for automatic injection

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. If **Snippet format** is set to **OneAgent JavaScript tag with SRI**, the **Script execution attribute** option becomes available. Choose either **async**, **defer**, or **No attribute** from the dropdown.
6. Select **Save**.

To configure script execution for manual insertion

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. In the **OneAgent JavaScript tag with SRI** section, set **Script execution attribute** to **async**, **defer** or **No attribute**.
6. Copy the snippet and insert it into your page.

When fetching the OneAgent JavaScript tag with SRI via the API, you can control script execution by passing a parameter. For details, see [GET OneAgent JavaScript tag with SRI](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.").

**Inline code** contains both the configuration and the RUM monitoring code, keeping the number of web requests at a minimum. Note that the Session Replay Classic monitoring code is not inlined, so there will still be an additional request if you use Session Replay Classic. If your website consists of many individual pages, using inline code may not be beneficial, as it increases the size of each document. However, it can be a suitable choice for single-page applications (SPAs).

[Get inline code via API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code)

##### Updates

When inserting the inline code manually, it must also be manually updated whenever configuration changes occur. To ensure it remains current, we recommend using it together with fully automated updates via the API. Using inline code from the web UI is discouraged unless timely configuration updates are not critical.

In case of automatic injection, OneAgent always injects the inline code using the current configuration. Note, however, that the caching policy of your application may influence how often OneAgent gets a chance to inject. For more information, see [Cache control header optimizations](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Monitoring code source

In case of agentless monitoring, the Session Replay Classic monitoring code is delivered by the Dynatrace CDN. In case of automatic injection or [manual insertion for pages of an auto-injected application](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), it is, by default, delivered by the OneAgent that instruments your application. Alternatively, it is also possible to load it from the Dynatrace CDN, see [Request the monitoring code from the Dynatrace CDN](/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").

##### Cache duration

Because the RUM monitoring code is inlined, its cache duration matches that of your page, which is determined by the cache settings on your web server. The Session Replay Classic monitoring code can be cached for up to a year by both browsers and the Dynatrace CDN. This extended cache duration is made possible by embedding the RUM JavaScript version in the file URL.

##### Script execution

The monitoring code is loaded and evaluated synchronously by the browser.

## Related topics

* [RUM manual insertion tags API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API")
* [Use Subresource Integrity (SRI) in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature in the New RUM Experience to ensure the integrity of Real User Monitoring code.")
* [Set up agentless RUM in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")
* [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")
* [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.")