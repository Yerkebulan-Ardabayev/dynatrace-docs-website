---
title: Tag specific users for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis
scraped: 2026-05-12T11:35:02.443187
---

# Tag specific users for web applications

# Tag specific users for web applications

* How-to guide
* 5-min read
* Updated on Apr 01, 2026

One of the key features of Real User Monitoring is the ability to uniquely identify individual users across different browsers, devices, and user sessions.

With [user tags](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace."), you can analyze a specific user's behavior and experience via [user session analysis](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes.").
By default, Dynatrace assigns a unique, random ID to each new user. However, you can assign more meaningful custom user tags that are comprised of, for example, usernames or emails.

For web applications, you can set up custom user tagging using either the RUM JavaScript API or your application's page metadata.

## User tagging via RUM JavaScript API

Use the [`identifyUser` methodï»¿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#identifyuser) of the [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") to set a user tag.

## User tagging based on page source

This approach to user tagging works by capturing available data in your application's page source: usernames or emails are quite often included in the text of a DOM element or a JavaScript variable. For the full list of page data sources, see [Available source types](#available-page-data-sources).

For example, the **easyTravel** demo application includes the username in a welcome message in the upper-right corner of the home page (see the image below). Using the development tools that are built into most browsers, you can generate a unique CSS selector for this particular element.

![Usertags 2](https://dt-cdn.net/images/usertags2-1872-eaa3cbf0fe.png)

Usertags 2

### Add a user tag rule

Once you've identified where usernames are located in your application's page source, you can create a user tag rule.

To add a user tag rule

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **User tags**.
5. Select **Add user tag rule**.
6. Select a **Source type** and source name for this user tag rule.
   Available source types

   * **CSS selector**. Use when the user's identifier is visible on the page. This mechanism captures the first match `innerText/textContent` value (available for browsers that support `querySelector`). To retrieve a specific attribute value of the element, append the '@' symbol followed by the attribute name, for example, `#someDomElement@someAttribute`.
   * **JavaScript variable**. Use when the user's identifier is available as a JavaScript variable on the `window` object. For example, if you specify the JavaScript variable `userName`, the RUM JavaScript retrieves the value from `window.userName`.
   * **Meta tag**:. Use when your user's identifier is present in one of the meta tags in the page source. This specifies the meta tag name that Dynatrace uses to capture its `content` value.
   * **Cookie value**. Use when your user's identifier is present in one of your existing cookies.

     If you want to use `Cookie value` as a data source, ensure that the cookies don't have the `HttpOnly` attribute. Otherwise, the RUM JavaScript won't be able to read the cookie values because `HttpOnly` cookies are inaccessible to JavaScript.
   * **Query string**. Use when your user's identifier is part of a certain query string parameter, which you can define here.
   * **Server-side request attribute**. Use when you want to use a server-side [request attribute](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") to tag each user session.  
     Once you've [defined a request attribute](/managed/observe/application-observability/services/request-attributes#define-request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."), set **Server-side request attribute** as **Source type**. Note that the request attribute might not be captured for every user action and user session, as your server-side distributed trace might not be captured due to [Adaptive Traffic Management](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").
7. Optional Turn on **Ignore case** if you want to convert the user tag to lower case.
8. Optional To ensure a clean extraction of the username value, turn on **Apply cleanup rule**, and then enter a regular expression.
9. Select **Add user tag rule**.

### Verify the user tag configuration

To verify that Dynatrace has correctly applied your user tag configuration, save the configuration and reload your application's page. After that, take a look at the injected JavaScript in your application's updated page source.

As you can see in the example below, a property called `md=` is now listed in this page's metadata expressions.

![Usertags 4](https://dt-cdn.net/images/usertags4-1873-d1f096ef61.png)

Usertags 4

To find sessions of a particular user

1. Go to **Session Segmentation**.
2. Select the filter box at the top of the page, and select the **User tag** attribute.
3. Choose a user tag from the list, and select **Apply**.

The **User sessions** page now shows a list of sessions related to this specific user. You can select a particular session to view its details. Alternatively, select the name of the user to navigate to this [user's overview page](/managed/observe/digital-experience/session-segmentation/analyze-all-sessions-of-a-single-user "Learn about user behavior by analyzing the user profile (user experience score) and session activity.").

## Limits and notes

* You can add up to 20 user tag rules per application.
* All captured values are cropped to a maximum length of 100 characters.
* If you use the RUM JavaScript API to identify your users, the API might override any existing metadata rules that you have previously configured. User tags might override any other metadata-based tags.
* All configured user tags are captured on every page. The RUM JavaScript is used to evaluate each monitored user action against each user-tag rule that you create, so keep your list of user tag rules to a minimum to reduce overhead.
* The last user action in a session that contains a tag is used as the tag for the entire session.
* The [Do Not Track](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") data privacy setting might affect user tagging.

  If the **Comply with "Do Not Track" browser settings** option is enabled for your web application and a particular user has the "Do Not Track" option enabled in their browser, no user tag information is sent. However, when a user has the "Do Not Track" option disabled in their browser, their user tag is captured.
* If your organization doesn't allow tracking of individual users for privacy reasons, you can alternatively define user tags that correspond to team names or department names. In this way, you can monitor the experience of individual users while not disclosing any identifying information.