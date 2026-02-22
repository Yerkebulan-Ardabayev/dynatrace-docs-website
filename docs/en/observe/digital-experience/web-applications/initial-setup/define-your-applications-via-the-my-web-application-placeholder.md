---
title: Define applications for Real User Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder
scraped: 2026-02-22T21:17:21.083133
---

# Define applications for Real User Monitoring

# Define applications for Real User Monitoring

* How-to guide
* 14-min read
* Updated on Apr 23, 2024

After [OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") in full-stack monitoring mode is installed on a host, it monitors all applications running on that host. As a starting point, all monitoring data is encapsulated in a placeholder application called **My web application**. We offer this placeholder application to allow for more flexibilityâit's you who decides how to organize your applications.

Dynatrace offers the following approaches to defining your application for RUM.

| Application detection approach | RUM JavaScript injection type | When to use |
| --- | --- | --- |
| [Suggested approach](#automated-approach) | Auto-injection | When your web applications can be easily identified based on domains and you want to create an application from already captured RUM monitoring traffic. |
| [Application detection rules approach](#application-detection-rules) | Auto-injection | When you want to create new applications or when dividing your traffic based on domains isn't sufficient. Use application detection rules to define more complex patterns to group your RUM monitoring traffic into applications. |
| [Manual approach](#alternative-approach) (aka "agentless monitoring") | Manual insertion | When you don't have access to the host of your web application, but you have access to the application code. |

You can choose the injection format for both auto-injected and manually inserted applications. For details, see [Select a snippet format](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").

Java Servletâbased applications

If you're using RUM for a Java Servletâbased application, make sure to restart the process after you finish the initial setup. The RUM sensor isn't enabled until after the restart.

## Suggested approach

The **My web application** placeholder application aggregates the traffic from all detected domains. This application can serve as your starting point for mapping the identified domains to separate applications in your environment.

1. Go to **Web**.
2. Select the **My web application** placeholder application.
3. Scroll down to find the **Top 3 included domains** panel.  
   This panel shows the domains with the largest number of user actions that OneAgent detected in your environment.
4. Select **View full details**.
5. In the **Top domains** list, select the arrow button in the **Transfer domain** column to expand a domain entry.
6. Follow one of the options below:

   * To add a new application, select **Create new application**. Your application is created and listed on the **Applications** page.
   * To add the domain to an existing application, select **Transfer**.

As you may want a more meaningful name for your application, replace the auto-generated name with a custom application name of your choosing.

To rename an application

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **General settings** > **Application name**.
5. Type in the name you prefer in the box at the top of the page. Note that application names must be unique.

### Possible issues for the suggested approach

**Uninstrumented component rewrites the URL**. When you follow the suggested approach, an application detection rule is automatically created for your new or updated application. This rule maps the user actions captured on the domain to your application. OneAgent uses the host portion of the URL to determine the domain. If an uninstrumented component between the browser and the first instrumented tier rewrites the host, you need to [configure the host name determination](#rum-appdetection-uninstrumentedcomponent). Otherwise, OneAgent might not be able to apply your application detection rule.

**Actions still map to the placeholder application**. If user actions still map to **My web application** instead of your application, refer to [How quickly do application detection rule changes take effect?](#rum-appdetection-rule-changes).

## Application detection rules approach

If you want to create more applications, change existing application mappings, or if you need to define more complex rules based not only on domains but also on URLs, you can use the **Application detection** settings page.

The URLs used for application detection have the `scheme://host:port/path?query` structure, where the query string is optional and default ports `80` for HTTP and `443` for HTTPS are omitted. The URL does not include a possible fragment identifier as in `scheme://host:port/path?query#fragment`, since application detection rules are evaluated on the server side of the application and the fragment identifier is only used by the browser and not added to web requests.

To add an application detection rule

1. Go to **Settings** > **Web and mobile monitoring** > **Application detection**. The list of application detection rules is displayed.  
   For each application defined using the [suggested approach](#automated-approach), a detection rule is automatically generated and added to the end of the list. Rules are applied sequentially, with rules at the top of the list taking priority over rules listed further down.
2. Select **Add detection rule**.
3. Use the options offered on the page to create the appropriate detection rule for your application.  
   You can apply rules to new or existing applications as well as create rules based on your application URL or domain (host).
4. Select **Save** to create an application detection rule.  
   The rule is placed at the very end of the application detection rules list.
5. Optional Select and hold **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") next to the rule name, and move the rule up or down in the list to change its priority.

You can create up to 1,000 application detection rules per environment.

### Possible issues for the application detection rules approach

**Uninstrumented component rewrites the URL**. If an uninstrumented component between the browser and the first instrumented tier rewrites the URL, then special considerations must be made (see [What can I do if an uninstrumented component rewrites parts of the URL?](#rum-appdetection-uninstrumentedcomponent) for more details). Otherwise, OneAgent might not be able to apply your application detection rules.

**Actions still map to the previous application**. If user actions still map to their previous application instead of the required one, refer to [How quickly do application detection rule changes take effect?](#rum-appdetection-rule-changes).

### FAQ for the suggested and application detection rules approaches

How does Dynatrace apply your application detection rules?

Application detection rules are evaluated on the server side of your application by OneAgent on the first instrumented tierâthe one nearest to the browser. The result is propagated to subsequent OneAgents using the `x-dynatrace-application` header. With this approach, any URL rewriting that might happen between the instrumented server-side tiers of your application does not influence the application detection result.

OneAgent adds an `app` parameter to the RUM JavaScript injected into the HTML code of your application. This parameter contains the ID of the detected application.

![App parameter in the RUM JavaScript](https://dt-cdn.net/images/injected-app-parameter-2505-7ee0111d11.png)

When sending beacon requests with the captured user actions, the RUM JavaScript includes this `app` parameter into the query string.

![App parameter added to the query string](https://dt-cdn.net/images/app-parameter-in-beacon-query-1922-30c91adb9b.png)

On the Dynatrace cluster, the `app` parameter in the beacon query string is used to assign user actions to applications.

To check the ID of an application to compare it to the `app` parameter

1. In Dynatrace, go to **Web**.
2. Select your application.
3. Check the URL of the page you are currently on. This URL contains a `uemapplicationId` parameter, for example, `uemapplicationId=APPLICATION-4CC1C5694BF9B3AB`. Its value without the `APPLICATION-` prefix is the application ID you are looking for.

   ![Checking the application ID in the Dynatrace web UI](https://dt-cdn.net/images/application-id-2559-b6b9f31629.png)

What can I do if an uninstrumented component rewrites parts of the URL?

As explained in [How does Dynatrace apply your application detection rules?](#rum-appdetection-appparam), your application detection rules are evaluated by OneAgent on the first instrumented tier of your application. However, there may be an uninstrumented component, such as a reverse proxy or a load balancer, between the browser and the first instrumented tier of your application that rewrites the URL. As a result, the URL used for application detection differs from the URL that was originally requested by the browser. In this scenario, special considerations must be made.

### Host is rewritten

You can configure components like proxies and load balancers to transport the original host information to the backend in a request header, for example, in the [`X-Forwarded-Host`ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) or [`Forwarded`ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded) header. OneAgent can retrieve the original host from one of these headers or from any proprietary header that has the same format as `X-Forwarded-Host`.

![Passing the original host information in the X-Forwarded-Host header](https://dt-cdn.net/images/host-name-determination-1093-9025d73d9b.png)

To use the original host name in application detection

1. Configure your uninstrumented component to add a header that forwards the original host name (if it doesn't already do that by default).  
   For instance, if the original host name requested by the browser was `www.example.com`, and your uninstrumented component forwarded the request to the `backend.com` internal host, then the component has to add a request header that passes `www.example.com` as shown in the sequence diagram above.
2. In Dynatrace, go to **Settings** > **Web and mobile monitoring** > **Host name determination**.
3. If the header added by your component is missing in the list, select **Add HTTP header**.
4. The request headers in the list are processed sequentially, with the ones at the top of the list taking priority. Move your new entry above the `Host` header, which is part of every HTTP/1.1 request.

Alternatively, you can also use the internal host name in your application detection rule. However, OneAgent uses the result of host name determination not only for application detection but also for [automatic determination of the cookie domain](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#automatic-cookie-domain-determination "Learn when and how to configure the cookie domain."). Therefore, if you do not configure host name determination as described above, you need to configure the cookie domain manually as described in [Manual configuration of the cookie domain](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#manual-cookie-domain-config "Learn when and how to configure the cookie domain."). The recommended choice is the [eTLD+1ï»¿](https://web.dev/same-site-same-origin/) of the domain, which OneAgent determines automatically.

### URL path is rewritten

In contrast to the host part of the URL, there is no feature to determine the original URL path, since it is uncommon for components to set headers that communicate the original path to subsequent tiers. Therefore, you cannot use a part of the URL path, which is removed by URL rewriting on an uninstrumented component, in your application detection rule.

How quickly do application detection rule changes take effect?

When you change your application detection rules, the updated rules are usually communicated to OneAgent within a minute. OneAgent categorizes incoming requests as configured in your application detection rules and sets the `app` parameter in the injected RUM JavaScript accordingly. The RUM JavaScript then reports its beacons using the updated `app` parameter that determines how the captured user actions are categorized. For more details, see [How does Dynatrace apply application detection rules?](#rum-appdetection-appparam).

The following factors might delay the effectiveness of the updated application detection rules:

* The HTML code is served through a CDN or other cache. In this case, OneAgent can inject the RUM JavaScript only when the HTML code is evicted from the cache and requested from the instrumented origin server again.
* The application specifies a long expiration time for the HTML document using the `Expires` response header or the `max-age` directive of the `Cache-Control` response header. A cache might serve it as long as specified in these headers, including the injected `app` parameter. A change in the application detection rules cannot be reflected immediately, since the cache does not send a request to the origin server while the document has not expired.
* If an application does not specify an explicit expiration time, then this does not mean that the page may not be cached (see [RFC7234: Calculating heuristic freshnessï»¿](https://datatracker.ietf.org/doc/html/rfc7234#section-4.2.2)). The cache may use the page without revalidation as long as it deems appropriate, unless the response contains directives that prevent this, for example, `Cache-Control: no-cache`.
* Single-page applications rewrite the current page dynamically instead of loading a new page from the server. If the HTML code was loaded into the browser tab before the application detection rules changed, then the categorization of the captured XHR user actions does not reflect the updated configuration yet. This changes as soon as the page is refreshed.

## Agentless RUM approach

When you don't have access to your web serverâand therefore can't install OneAgent on the hostâbut when you have access to your application code, opt for [agentless RUM](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").

For some technologies, [automatic RUM JavaScript injection](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") is not supported even when you can install OneAgent. For example, while OneAgent can monitor the server side of a Heroku application, it cannot inject the RUM JavaScript into the application's pages. If that's the case, you need to use agentless RUM and manually add the RUM JavaScript to your application's pages.

For a list of technologies and servers that support automatic RUM JavaScript injection, see [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Best practices and recommendations

* Define your applications based on team ownership so that you can easily make use of [management zones](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") for access restrictions.
* It may make sense to define applications based on their technology stack so that the right settings are applied and the management of specific settings is easier. For example, activating support for specific XHR frameworks is typically required only for specific parts of a large application and for specific user action naming rules. It may help separate such large applications into smaller ones based on the technologies in use or team ownership.
* **My web application** placeholder application

  + Avoid renaming the **My web application** placeholder application, as it includes all user actions on all domains that are not included in an application detection rule. If you rename **My web application**, it might be difficult to distinguish it from your other applications.
  + It's impossible to delete this placeholder application.
  + If you can't find the **My web application** placeholder application, someone might have renamed it. To locate it, open any other application and replace the application ID in the URL with `EA7C4B59F27D43EB`. You'll be redirected to **My web application**.
  + In new environments, youâll only see this placeholder application after the traffic from an auto-injected application starts coming.
* Separating applications based on domains works best as Dynatrace cannot correlate user actions across domains with specific user sessions. This correlation is done via a cookie and therefore only works if the cookie can be set on the same domain. For example, user actions for `www.dynatrace.com` and `blog.dynatrace.com` can be captured in a single application as the cookie can be set to `dynatrace.com`. However, the traffic for `www.dynatrace.com` and `www.internal-dynatrace.com` cannot be captured in a single user session. You can still separate user actions based on the domain, but user sessions cannot include user actions from multiple domains. See [User sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") for more details.
* Group low-traffic applications. If you create an application based on a domain that has fewer than 10 actions per minute, Dynatrace won't automatically detect anomalies for this newly created application. Dynatrace depends on steady application traffic to correctly [learn multidimensional baselines and automatically report application problems](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure "Learn about the fixed thresholds used by Dynatrace to determine when a detected slowdown or error-rate increase justifies the generation of a new problem event."). You can change your application anomaly detection settings on the **Anomaly detection** page within your application settings. Although this recommendation contradicts the one mentioned above, it may make sense to combine low-traffic applications.
* The application detection rules are processed in sequence for each request. More rules means more processing time, and as the rules are processed within OneAgents, you should try to have the rules for the applications with the most traffic at the top of the list. As soon as one rule matches, no further requests are processed.
* The more specific application detection rules should be defined first, while the more generic rules should be at the bottom of the application detection rules list.  
  Let's assume that you want to create an application called `A` onto which the following two domains will be mapped:

  `http://www.mydomain.com/cms/directory/shop/index.html`  
  `http://shop.differentdomain.de/index.html`

  and another application `B` for the following domain:

  `http://newdomain.co.uk/hello/shop.html`

  If you create a generic grouping rule based on the `shop` value, all three domains will be grouped into the same web application for monitoring. Therefore, you should first define a more specific rule, for example, "If the URL ends with `shop.html`" so that only the third URL is mapped to application `B`. Then you can safely define a generic rule based on the `shop` value, as the third URL will have already been mapped to the previous application and therefore won't be included in application `A`.
* Depending on your requirements, you can adjust the monitoring consumption and configure Real User Monitoring accordingly.
* To monitor traffic on a single application, you can opt to use [user actions and session properties](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."). To monitor separate applications and get complete insights into consumption per application, you can configure separate applications, use tagging to split the metrics, and define management zones.