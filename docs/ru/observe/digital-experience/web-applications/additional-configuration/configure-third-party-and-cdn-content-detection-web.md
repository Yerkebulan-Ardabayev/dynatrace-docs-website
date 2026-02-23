---
title: Configure first-party, third-party, and CDN resource detection for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web
scraped: 2026-02-23T21:22:09.119923
---

# Configure first-party, third-party, and CDN resource detection for web applications

# Configure first-party, third-party, and CDN resource detection for web applications

* How-to guide
* 1-min read
* Updated on Jun 30, 2022

Dynatrace recognizes more than 1,000 third-party content providers, including Google, Amazon, Twitter, and LinkedIn. Typical third-party content includes Facebook and Twitter widgets, gravatars, and similar resources. It's crucial to see how third-party content providers affect your applications and understand if such content is the root cause of any slowdowns.

Content delivery networks (CDNs) are usually under your control. Your application might use a CDN to store and serve frequently accessed static and dynamic content, which is required to speed up load times in certain geographic regions.

## Difference between third-party providers and CDNs

The difference between third-party content providers and CDNs lies in the control you have over the data.

* If you use external data that you have no control over, the content comes from a third-party provider.
* If you rely on an external resource to deliver static or dynamic content to your application, for example, images or CSS, think of the service as a CDN.

## View your application's top providers

You can view your application's top providers and access the detailed information on each provider from your application overview page. For details, see [Performance analysis > Resources](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis#resources "Understand the available types of performance analysis that are provided by Dynatrace.").

## Manage your environment's providers

### View the full list of providers

Dynatrace detects lots of third-party content providers. When Dynatrace cannot find a host name in the list of known third-party providers, it marks the resource as CDN. Also, Dynatrace can find out which domains your organization hosts and categorize those domains as first-party.

To see the full list of providers detected for your environment, go to **Settings** > **Web and mobile monitoring** > **Provider breakdown**.

* Manually added providers are listed directly under the **Add custom provider item** button. You can [add a provider](#add-provider-manually) and mark it as a first-party, third-party, or CDN.
* Automatically detected CDNs and third-party providers are listed under **Auto detected providers**.

![Provider breakdown settings](https://dt-cdn.net/images/provider-breakdown-settings-1267-bfe07292b6.png)

### Add a provider manually

If you can't find your provider in the list of auto-detected providers or want to override auto-detection rules, you can add a provider manually.

To manually add a provider

1. Go to **Settings** > **Web and mobile monitoring** > **Provider breakdown**.
2. Select **Add custom provider item**.
3. Enter the **Resource name**, and set the **Resource type** to specify if the resource is first-party, third-party, or CDN.
4. Optional Provide a URL for the provider's brand icon.
5. Select **Add name pattern**, and then enter the pattern for the provider's domain name. You can specify several patterns if required.
6. Optional Turn on **Submit this provider-pattern to improve auto-detection** if you believe Dynatrace should automatically detect this resource as a third-party resource.

Starting with Dynatrace version 1.240, auto-detection of first-party providers is enabled by default and cannot be deactivated. If you need to override the auto-detected first-party providers, [add a provider manually](#add-provider-manually).

### Reorganize manually added providers

The list of manually added providers is processed in the order of their appearance in the list. For this reason, a provider with a more specific domain pattern should come first. For example, `api.example.com` should come before `example.com`.

To change the order of manually added providers

1. Go to **Settings** > **Web and mobile monitoring** > **Provider breakdown**.
2. Find the list of manually added providers under the **Add custom provider item** button.
3. Use **Drag handle** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") to change a provider's priority.

## Related topics

* [Content resources API](/docs/dynatrace-api/configuration-api/rum/content-resources "Learn what the Dynatrace configuration API for content resources offers.")