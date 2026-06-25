---
title: Configure RUM cookie attributes
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes
scraped: 2026-05-12T11:34:14.311788
---

# Configure RUM cookie attributes

# Configure RUM cookie attributes

* How-to guide
* 4-min read
* Updated on Apr 22, 2026

Dynatrace Real User Monitoring uses a set of HTTP cookies; see [Cookies and client-side storage for RUM and Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB."). You can customize some of the cookie attributes.

To access these options

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Cookie**.

The following sections describe the available settings.

## Configure cookie attributes relevant to data privacy

If your company's security policy requires the `Secure` and `SameSite` cookie attributes, you need to configure RUM to set them, because they aren't set by default.

Dynatrace RUM does not support the `HttpOnly` attribute. Since `HttpOnly` cookies are inaccessible to JavaScript, the RUM JavaScript cannot read or modify them. Ensure that your infrastructure doesn't add the `HttpOnly` attribute, because this will break monitoring.

### Set the Secure attribute

The `Secure` cookie attribute ensures that browsers send cookies only over secure connections.

Before enabling the `Secure` cookie attribute, ensure that your application is served entirely over secure connections. Otherwise, you'll lose visibility into any unencrypted HTTP communication.

To set the `Secure` cookie attribute, turn on **Cookie** > **Use the Secure cookie attribute for cookies set by Dynatrace**.

### Set the SameSite attribute

The `SameSite` cookie attribute controls whether the browser sends the cookie with cross-site requests. For a detailed explanation of this attribute and its values, see [SameSite cookies explainedï»¿](https://web.dev/samesite-cookies-explained/).

To set the `SameSite` cookie attribute, go to **Cookie** > **SameSite cookie attribute** and select one of the values **None**, **Lax**, and **Strict**.

## Configure the Domain attribute

The `Domain` and `Path` cookie attributes define a cookie's scope. This scope determines whether browsers send the cookie with a request and whether client-side JavaScript can access it for a given URL.

* Dynatrace always sets the `Path` attribute of the RUM cookies to `/`, so the cookie scope covers all URL paths within a domain. The `Path` attribute cannot be configured.
* By default, the `Domain` attribute is determined automatically, but you can also configure it manually for each application.

The following sections explain how Dynatrace determines the default cookie domain and when you might need to configure it manually.

### Default cookie domain

By default, Dynatrace determines the cookie domain automatically by choosing the [effective top-level domain plus one (eTLD+1)ï»¿](https://web.dev/same-site-same-origin/) of the request URL. For example, Dynatrace chooses the `example.com` cookie domain for `www.example.com` and the `example.co.uk` cookie domain for `www.example.co.uk`. This allows Dynatrace to capture a continuous session even when users move between subdomains while interacting with your applications, for example, from `www.example.com` to `shop.example.com`.

The cookie domain is determined either server-side by OneAgent or client-side by the RUM JavaScript.

* If the RUM JavaScript is [injected automatically](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), OneAgent usually determines the cookie domain, using the result of host name determination as a starting point. If an uninstrumented component rewrites the host portion of the URL, ensure that [host name determination is configured correctly](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach.").
* If you use [agentless RUM](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), the RUM JavaScript determines the cookie domain.

### Manually configure the cookie domain

In most scenarios, you don't need to configure the cookie domain manually. However, manual configuration is useful in the following cases:

* You need to separate the user actions of different subdomains into separate user sessions.
* Automatic cookie domain determination does not work because an uninstrumented component rewrites the host portion of the URL and does not forward the original host information in a request header. The preferred solution is to configure the component to add such a header; see [What can I do if an uninstrumented component rewrites parts of the URL?](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Manual cookie domain configuration is also a possible workaround.

To configure the cookie domain, go to **Cookie** > **Domain to be used for cookie placement** and enter the required domain.

Common pitfalls and limitations of manual configuration

##### Configured cookie domain is a public suffix

Browsers do not allow you to set cookies with a `Domain` attribute that exceeds a single organization's boundary. Therefore, setting the cookie domain to a [public suffixï»¿](https://publicsuffix.org/list/) does not work.

##### Multiple domains without a common eTLD+1 are mapped into the configured application

Since the cookie domain is configured per application, all domains that map to your application should share at least a common eTLD+1.

For example, you cannot manually configure the cookie domain for an application where both `www.example.com` and `www.example.co.uk` map. If you choose the cookie domain `example.com`, the browser rejects the RUM cookies on requests to `www.example.co.uk`.

##### Nested cookie domains

If you configure the cookie domain for all or some of your applications manually, you must ensure that the cookie domains of your applications are not nested.

Consider the following example. The `www.example.com` domain is mapped to the **Example app**, while the `shop.example.com` domain is mapped to the **Shopping app**. By default, the `example.com` cookie domain is detected automatically for both applications. If you manually set the cookie domain for the **Shopping app** to `shop.example.com` and users navigate back and forth between the two applications, ambiguous situations can arise. The RUM cookies for the **Example app** use the `example.com` cookie domain and therefore also apply to the **Shopping app**, which has its own set of RUM cookies with the `shop.example.com` domain. With this configuration, Dynatrace might split the captured RUM data into short user sessions at random, and user actions and distributed traces might not be linked as expected.