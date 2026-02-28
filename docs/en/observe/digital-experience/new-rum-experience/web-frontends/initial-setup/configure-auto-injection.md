---
title: Configure automatic injection in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection
scraped: 2026-02-28T21:27:56.591303
---

# Configure automatic injection in the New RUM Experience

# Configure automatic injection in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

Once OneAgent is deployed in full-stack monitoring mode on a host, it by default automatically injects the RUM JavaScript into the HTML of your web frontends for the technologies listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). To initiate injection, simply restart your web server processes after installing OneAgent.

## Overview

By default, injection follows a set of [built-in rules for automatic injection](#where-is-rum-js-injected), but there are scenarios where you may need to define a [custom injection rule](#custom-injection-rule) to achieve injection. Custom injection rules also support the [exclusion of specific pages from injection](#disable-injection), which allows you to set up [manual insertion for the pages of an auto-injected frontend](#manual-insertion-using-oneagent).

The RUM JavaScript snippet injected into your application's HTML can have different formats, each designed to meet specific requirements as outlined in [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").
To configure the format used for automatic injection, refer to [Configure the snippet format](#configure-snippet-format).

OneAgent injects the RUM JavaScript into each page based on the current configuration whenever the instrumented web or application server delivers the page. However, the pageâs caching policy determines how frequently OneAgent has the opportunity to perform this injection. To address this, OneAgent includes a feature that optimizes cache control headers. For details on how this feature works and its limitations, see [Cache control header optimizations](#cache-header-optimization).

## Built-in rules for automatic injection

OneAgent detects responses that contain HTML content and injects the RUM JavaScript into the `<head>` element of each page. It does not modify other resources such as images, CSS files, JSON or XML documents, or plain text.

OneAgent tries to inject the RUM JavaScript as the first script on the page, which helps to ensure reliable monitoring results. Injection only works with valid HTML that follows basic best practicesâfor example, ensuring all elements are properly opened and closed. OneAgent follows the built-in rules specified below to determine the most suitable location within an HTML document for injecting the RUM JavaScript.

### Automatic injection rules specification

## Explicitly specify where the RUM JavaScript should be injected

In some cases, OneAgent may be unable to perform injection using the built-in rules. This is typically due to malformed HTML, though other rare conditions may also prevent the ruleset from identifying a suitable injection point. In such scenarios, you can achieve automatic injection by defining a custom injection rule that explicitly specifies where the RUM JavaScript should be injected within the HTML document.

To create a custom injection rule that specifies the injection point in the HTML document

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **Collect and capture** > **Frontend** > **Injection** > **Custom injection rules**.
6. Select **Add custom rule**.
7. Define the **Operator** and, if required, the corresponding **URL pattern** to control to which pages your custom injection rule applies.
8. Under **Rule**, select either **Before specific HTML** or **After specific HTML**, and enter the corresponding HTML pattern.
9. Select **Save changes** to create the custom injection rule.

## Disable injection for particular pages

To disable injection for one or more pages within your frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **Collect and capture** > **Frontend** > **Injection** > **Custom injection rules**.
6. Select **Add custom rule**.
7. Define the **Operator** and, if required, the corresponding **URL pattern** to control to which pages your custom injection rule applies.
8. Under **Rule**, select **Do not inject**.
9. Select **Save changes** to create the custom injection rule.

This rule only disables injection and [cache control header optimizations](#cache-header-optimization); it does not fully disable RUM functionality. For instance, cookies may still be set. If you're looking for a way to selectively enable RUM, please refer to the instructions in [Roll out RUM selectively for your applications](/docs/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts").

## Configure the snippet format

To configure the snippet format for automatic injection

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. Under **Snippet format**, select the desired format.
6. Select **Save**.

To learn more about the different snippet formats, refer to [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").

## Cache control header optimizations

Enabled by default

Your application's caching policy plays a key role in determining whether OneAgent can inject the RUM JavaScript into a page using the current configuration. To ensure timely application of configuration changes, the cache control header optimizations feature modifies HTTP headers so that conditional requests result in a cache miss whenever the RUM configuration has changed, giving OneAgent a chance to inject. Details of these optimizations and the specific header modifications are provided below.

Cache control header optimizations specification

When cache control header optimizations are turned on and the RUM configuration has been changed, the requests that would otherwise result in `304 Not Modified` respond with `200 OK`, giving OneAgent a chance to inject the RUM JavaScript into your application HTML code. If the RUM configuration hasn't been changed, the requests result in a `304 Not Modified` response.

### Modified headers

OneAgent modifies the following response and request headers:

#### Response headers

* `ETag`
* `Last-Modified`

#### Request headers

* `If-None-Match`
* `If-Modified-Since`
* `If-Unmodified-Since`[1](#fn-1-1-def)
* `If-Match`[1](#fn-1-1-def)

1

Not modified for range requests, which are generally excluded from RUM monitoring.

Here's how OneAgent modifies the cache control headers.

#### When the RUM configuration is changed

* The incoming `If-None-Match` and `If-Modified-Since` request headers are removed.
* Modifications made to the `If-Unmodified-Since` and `If-Match` headers are removed.
* When both `ETag` and `Last-Modified` headers are used:

  + A suffix is appended to the `ETag` header.
  + One second is subtracted from the `Last-Modified` header.
* When only the `ETag` header is used:

  + A suffix is appended to the `ETag` header.
* When only the `Last-Modified` header is used:

  + The `ETag` header is created.
  + One second is subtracted from the `Last-Modified` header.

#### When the RUM configuration isn't changed

* Before the request is handled by the web or app server, the modifications made to the headers are removed so that the web or app server doesn't see the changes.

When the application consists of multiple instrumented tiers, the changes to the `ETag` and `Last-Modified` headers are applied on each tier.

OneAgent does not alter the `Expires` and `Cache-Control` headers, which explicitly define resource expiration times. To ensure timely updates, we recommend setting shorter expiration durations in these headers.

### Disabling cache control header optimizations

In rare cases, cache control header optimizations may interfere with your application's functionality. If this occurs, you can disable the feature.
When disabled, the rollout of new RUM configurations will depend entirely on your application's existing caching behavior.

To disable the cache control header optimizations

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Automatic injection**.
5. Turn off **Optimize the value of cache control headers for use with Dynatrace Real User Monitoring**.
6. Select **Save**.

### Disabling cache control header optimizations for non-HTML resources

In some cases, OneAgent may modify the cache control headers of non-HTML resources. This occurs because header modifications are applied before the exact content type can be determined. While OneAgent excludes certain resources from cache control header optimizations based on their URI suffix, it's not possible to account for all non-HTML content types.

If you want to prevent cache control header modifications for specific non-HTML resources, you can create a [custom injection rule that disables injection for those resources](#disable-injection).

## Use manual insertion for pages of an auto-injected frontend

If OneAgent is deployed on your process groups and automatic injection is supported for your technology, then OneAgent injects the RUM JavaScript automatically by default. But if you prefer, you can insert it manually instead into all or specific pages.

First, you need to suppress automatic injection as described in [Disable injection for particular pages](#disable-injection). Then, to insert the RUM JavaScript manually

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select **Manual insertion**.
5. Scroll to the section for the snippet format you want to use and select  to copy the RUM JavaScript to the clipboard.
6. Insert the snippet in your HTML before any other scripts.

Alternatively, you can also retrieve the snippet via the [API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API"), which allows you to integrate its insertion into your build process. This ensures that your frontend consistently operates with the latest configuration.

## Related topics

* [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")
* [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")