---
title: Configure automatic injection
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/rum-injection
scraped: 2026-02-15T21:20:42.326172
---

# Configure automatic injection

# Configure automatic injection

* How-to guide
* Updated on Jul 01, 2025

Once OneAgent is deployed in full-stack monitoring mode on a host, it by default automatically injects the RUM JavaScript into the HTML of your web applications for the technologies listed in [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). To initiate injection, simply restart your web server processes after installing OneAgent.

By default, injection follows a set of [built-in rules for automatic injection](#where-is-rum-js-injected), but there are scenarios where you may need to define a [custom injection rule](#custom-injection-rule) to achieve injection. Custom injection rules also support the [exclusion of specific pages from injection](#disable-injection), which allows you to set up [manual insertion for the pages of an auto-injected application](#manual-insertion-using-oneagent).

The RUM JavaScript is responsible for collecting RUM data from your customers' web browsers. It sends this data as XHR POST requests to a beacon endpoint, which performs initial validation before forwarding the data to Dynatrace. The default beacon endpoint in automatic injection scenarios is provided by the OneAgent instrumenting your web or application server, but alternative setups are possible, see [Configure beacon endpoint for web applications](/docs/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

The RUM JavaScript snippet injected into your application's HTML can vary in format, each designed to meet specific requirements as outlined in [Select a snippet format](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").
To configure the format used for automatic injection, refer to [Configure the snippet format](#configure-snippet-format).

OneAgent injects the RUM JavaScript into each page based on the current configuration whenever the instrumented web or application server delivers the page. However, the pageâs caching policy determines how frequently OneAgent has the opportunity to perform this injection. To address this, OneAgent includes a feature that optimizes cache control headers. For details on how this feature works and its limitations, see [Cache control header optimizations](#cache-header-optimization).

If you don't have access to the web server hosting your application and therefore can't install OneAgent, you can monitor your application using [agentless RUM](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").

## Built-in rules for automatic injection

OneAgent detects responses containing HTML content and injects the RUM JavaScript into the head section of each page. It does not modify other resources such as images, CSS files, JSON or XML documents, or plain text.

OneAgent tries to inject the RUM JavaScript as the first script on the page, which helps to ensure reliable monitoring results. Injection only works with valid HTML that follows basic best practicesâfor example, ensuring all elements are properly opened and closed. OneAgent follows the built-in rules specified below to determine the most suitable location within an HTML document for injecting the RUM JavaScript.

### Automatic injection rules specification

Name

Condition

Action

Overrules

<!DOCTYPE>

The `<!DOCTYPE>` tag is not `<!DOCTYPE html>`.

Abort and do not inject. Note that only a single Doctype declaration is allowed.

initial tag

A tag appears before `<html>` that is not one of the following:

* `<!DOCTYPE ...>`
* `<html>`
* `<link>`
* `<meta>`
* `<script>`
* `<style>`

Abort without injecting.

<?xml?>

an `<?xml ...?>` specification is encountered.

Ignore and continue to scan the document.

non-<meta> tag

non-<head> tag

initial tag

<html> tag

The `<html>` tag is encountered.

If a potential injection point is found earlier, inject there, and do not scan further. If there are multiple potential injection points, the earliest one is used.

Otherwise continue to scan the document

<script src> tag

A `<script src="...">` tag is found within `<head>`.

If a potential injection point is found earlier, inject there, and do not scan further. If there are multiple potential injection points, the earliest one is used.

Otherwise, inject before this `<script>` tag and do not scan further.

non-<meta> tag

<base>/<meta> tag

<title>/<noscript> tag

The `<title>` or the `<noscript>` tag is encountered.

Ignore everything until the `</title>` or the `</noscript>` tag, then continue to scan the document.

<body> tag

<base>/<meta> tag

Either the `<base>` or the `<meta>` tag is encountered.

Discard any conditional injection point found earlier. Continue to scan the document.

any conditional injection point found earlier by:

non-<meta> tag

unclosed <meta>

non-<head> tag

non-<meta> tag

A tag is found within `<head>` that is neither `<meta>` nor `<title>`.

Inject before it (conditional injection).

Continue to scan the document, in case this injection choice is overruled.

unclosed <meta>

The `</head>` tag arrives after a `<meta>` tag that isn't closed either by the closing `</meta>` tag or by the XML-style `<meta ... />` tag.

Add `</meta>` followed by the injection, both before the `</head>` (conditional injection).

Continue to scan the document, in case this injection choice is overruled.

comment

The `<!- comment ->` tag is encountered.

Ignore and continue to scan the document.

non-<meta> tag

non-<head> tag

non-<head> tag

A tag is found after `<html>` but before `<head>` that is neither `<head>` nor `<body>`.

Inject before it (conditional injection).

Continue to scan the document, in case this injection choice is overruled.

</head> tag

The `</head>` tag encountered.

If a potential injection point is found earlier, inject there, and do not scan further. If there are multiple potential injection points, the earliest is used

Otherwise, continue to scan the document.

flush

Java only

Flush is called on the injecting stream/writer outside of the `<head></head>` section and a conditional injection awaits confirmation.

Discard the conditional injection point, propagate the flush, and continue to scan the document for a new injection point.

any conditional injection point found before by:

non-<head> tag

flush in <head>

Java only

Flush is called on the injecting stream/writer inside `<head></head>` and conditional injection awaits confirmation.

Keep the injection point and continue to scan the document.

Disregard the flush.

<body> tag

The `<body>` tag is encountered.

Document scan stops. Any potential injection point found earlier is used. If there are multiple potential injection points, the earliest one is used

If no rule matched earlier, inject after the `<body>`.

end of file

End of file is reached and scanning didn't terminate before that.

Don't perform an injection.

any conditional injection point found before by:

non-<meta> tag

unclosed <meta>

non-<head tag

parse error

The document's contents don't appear to exhibit the basic structure expected from HTML tags and attributes

Document scan stops.

If a potential injection point is found earlier, inject there, and do not scan further. If there are multiple potential injection points, the earliest one is used.

If no rule provides an earlier injection point, don't perform an injection

If you're unsure whether the RUM JavaScript was injected successfully or you're experiencing issues with your RUM setup, refer to [Web applications: Issues with RUM JavaScriptï»¿](https://dt-url.net/up03l19).

## Explicitly specify where the RUM JavaScript should be injected

In some cases, OneAgent may be unable to perform injection using the [built-in rules](#where-is-rum-js-injected). This is typically due to malformed HTML, though other rare conditions may also prevent the ruleset from identifying a suitable injection point. In such scenarios, you can achieve automatic injection by defining a custom injection rule that explicitly specifies where the RUM JavaScript should be injected within the HTML document.

To create a custom injection rule that specifies the injection point in the HTML document

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Custom injection rules**.
5. Under **Define custom injection rules**, select **Add custom rule**.
6. Define the **Operator** and, if required, the corresponding **URL pattern** to control to which pages your custom injection rule applies.
7. Under **Rule**, select either **Before specific HTML** or **After specific HTML**, and enter the corresponding HTML pattern.
8. Select **Save changes** to create the custom injection rule.

## Disable injection for particular pages

To disable injection for one or more pages within your application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Custom injection rules**.
5. Under **Define custom injection rules**, select **Add custom rule**.
6. Define the **Operator** and, if required, the corresponding **URL pattern** to control to which pages your custom injection rule applies.
7. Under **Rule**, select **Do not inject**.
8. Select **Save changes** to create the custom injection rule.

This rule only disables injection and [cache control header optimizations](#cache-header-optimization); it does not fully disable RUM functionality. For instance, cookies may still be set. If you're looking for a way to selectively enable RUM, please refer to the instructions in [Roll out RUM selectively for your applications](/docs/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts").

## Configure the snippet format

To configure the snippet format for automatic injection

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Automatic injection**.
5. Under **Snippet format**, select the desired format.

To learn more about the different snippet formats, refer to [Select a snippet format](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").

## Cache control header optimizations

ð¢ Enabled by default

Your application's caching policy directly influences how often OneAgent can inject the RUM JavaScript into a page using the current configuration. To ensure timely application of configuration changes, the cache control header optimizations feature modifies HTTP headers so that conditional requests result in a cache miss whenever the RUM configuration has changed, giving OneAgent a chance to inject. Details of these optimizations and the specific header modifications are provided below.

Cache control header optimizations specification

When the cache control header optimization is turned on and the RUM configuration has been changed, the requests that would otherwise result in `304 Not Modified` respond with `200 OK`, giving OneAgent a chance to inject the RUM JavaScript into your application HTML code. If the RUM configuration hasn't been changed, the requests result in a `304 Not Modified` response.

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

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Automatic injection**.
5. Turn off **Optimize the value of cache control headers for use with Dynatrace Real User Monitoring**.
6. Select **Save changes**.

### Disabling cache control header optimizations for non-HTML resources

In some cases, OneAgent may modify the cache control headers of non-HTML resources. This occurs because header modifications are applied before the exact content type can be determined. While OneAgent excludes certain resources from cache control header optimizations based on their URI suffix, it's not possible to account for all non-HTML content types.

If you want to prevent cache control header modifications for specific non-HTML resources, you can create a [custom injection rule that disables injection for those resources](#disable-injection).

## Use manual insertion for pages of an auto-injected application

If OneAgent is deployed on your process groups and automatic injection is supported for your technology, then OneAgent injects the RUM JavaScript automatically by default. But if you prefer, you can insert it manually instead into all or specific pages.

First, you need to suppress automatic injection as described in [Disable injection for particular pages](#disable-injection). Then, to insert the RUM JavaScript manually

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Manual insertion**.
5. Select the required [snippet format](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case"), and copy the provided snippet.
6. Insert the snippet in your HTML before any other scripts.

Alternatively, you can also retrieve the snippet via the [API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API."), which allows you to integrate its insertion into your build process. This ensures that your application consistently operates with the latest configuration.