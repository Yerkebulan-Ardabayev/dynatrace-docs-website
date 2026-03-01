---
title: Configure the RUM cookie domain for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain
scraped: 2026-03-01T21:24:31.896145
---

# Configure the RUM cookie domain for web applications

# Configure the RUM cookie domain for web applications

* How-to guide
* 4-min read
* Published Mar 21, 2022

Dynatrace Real User Monitoring uses HTTP cookies to group user actions into sessions and link user actions with their corresponding [distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time."). Browsers include a cookie in the `Cookie` request header only if the request URL lies within the scope of the cookie, which is specified by the `Domain` and `Path` cookie attributes.

Dynatrace always sets the `Path` attribute of the RUM cookies to `/` so that the cookie scope covers all URL paths within a domain. The `Domain` attribute is determined automatically by default, but you can also [configure it manually for each application](#configure-cookie-domain).

## Automatic cookie domain determination

If you haven't [configured the cookie domain](#configure-cookie-domain), Dynatrace determines it automatically. Dynatrace chooses the [effective top-level domain plus one (eTLD+1)ï»¿](https://web.dev/same-site-same-origin/) of the request URL. For example, Dynatrace chooses the `example.com` cookie domain for the `www.example.com` domain or the `example.co.uk` cookie domain for the `www.example.co.uk` domain. With this choice, Dynatrace can capture a continuous session even when your users visit multiple subdomains while interacting with your applications, for example, when they navigate from `www.example.com` to `shop.example.com`.

The cookie domain is determined either on the server side by OneAgent or on the client side by the RUM JavaScript, depending on which one is the first to capture a user's interaction with your application. If the RUM JavaScript is injected automatically, it's usually OneAgent that determines the cookie domain. However, when the browser takes a page from the cache, the RUM JavaScript determines the cookie domain.

### Possible issues with automatic cookie domain determination

OneAgent uses the result of host name determination as a starting point when it determines the cookie domain. If there is an uninstrumented component that rewrites the host portion of the URL, it is crucial for automatic cookie domain determination that host name determination is configured correctly. For details, see [What can I do if an uninstrumented component rewrites parts of the URL?](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach.")

## Manual cookie domain configuration

In most scenarios, there is no need to configure the cookie domain manually. There are, however, two use cases when this is necessary:

* You need to separate the user actions of different subdomains into separate user sessions.
* Automatic determination of the cookie domain does not work because an uninstrumented component rewrites the host portion of the URL and does not forward the original host information in a request header. The preferable solution is to configure the component to add such a header (see [What can I do if an uninstrumented component rewrites parts of the URL?](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach.") for instructions). However, manual configuration of the cookie domain is also a possible workaround.

### Configure cookie domain manually

To configure the cookie domain

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **Cookie**.
5. In **Domain to be used for cookie placement**, enter the required domain.

### Possible issues with manual configuration

#### Configured cookie domain is a public suffix

Browsers do not allow you to set cookies with a `Domain` attribute that exceeds a single organization's boundary. Therefore, setting the cookie domain to a [public suffixï»¿](https://publicsuffix.org/list/) does not work.

#### Multiple domains without a common eTLD+1 are mapped into the configured application

Since the cookie domain is configured per application, all domains that map to your application should have at least a common eTLD+1 to allow cookie domain definition.

For example, you cannot manually configure the cookie domain for an application where both `www.example.com` and `www.example.co.uk` map. If you choose the cookie domain `example.com`, the browser rejects the RUM cookies on requests to `www.example.co.uk`.

#### Overlapping cookie domains

If you configure the cookie domain for all or some of your applications manually, you must ensure that the cookie domains of your applications do not overlap.

Consider the following example. The `www.example.com` domain is mapped to the **Example app**, while the `shop.example.com` domain is mapped to the **Shopping app**. By default, the `example.com` cookie domain is detected automatically for both domains. If you set the `shop.example.com` cookie domain for the **Shopping app** and your users navigate back and forth between the two applications, ambiguous situations will arise since the RUM cookies for the **Example app** have the `example.com` cookie domain and therefore are also applicable to the **Shopping app**, which has another set of RUM cookies with the `shop.example.com` domain. With this configuration, Dynatrace might randomly split the captured RUM data into short user sessions and user actions, and distributed traces might be not be linked as expected.