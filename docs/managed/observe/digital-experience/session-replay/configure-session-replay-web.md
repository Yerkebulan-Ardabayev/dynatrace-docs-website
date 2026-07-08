---
title: Configure Session Replay Classic for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/configure-session-replay-web
---

# Configure Session Replay Classic for web applications

# Configure Session Replay Classic for web applications

* How-to guide
* 22-min read
* Updated on Mar 05, 2026

You can configure monitoring consumption and data privacy settings for Session Replay. The following sections describe all possible configuration options:

* [**Cost and traffic control**](#cost-traffic-control) to reduce the number of recorded user sessions
* [**Opt-in mode**](#sr-opt-in-mode) to decide which parts of a user session should be recorded and enable your application's users to approve recording of their sessions
* [**URL exclusion**](#sr-url-exclusion) to exclude pages and views from recording
* [**Masking**](#sr-masking) to prevent the recording and display of private user information
* [**Resource capture**](#sr-resource-capturing) to capture and store stylesheets during user session recording
* [**User permissions and management zones**](#sr-permissions-and-management-zones) to control who has access to session recordings

Dynatrace has introduced several Session Replay configuration settings that you should use to protect your customers' personal information. Before enabling Session Replay and proceeding with the privacy configuration settings explained on this page, ensure that your organization has taken all other [necessary steps to protect your customers' data](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

The ability to replay recorded user sessions, with or without playback [masking](#sr-masking) settings, is [permission controlled](#sr-permissions). The **Replay sessions with masking** and **Replay sessions without masking** permissions are available at the environment and management-zone level.

## Cost and traffic control

After you enable Session Replay, all user sessions analyzed with RUM are also recorded with Session Replay. However, you might want to limit the number of sessions recorded with Session Replay to reduce the volume of data that this feature generates. To do that, configure the cost and traffic control setting.

### Adjust number of sessions recorded with SR

To limit the number of sessions recorded with Session Replay

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Enablement and cost control**.
5. Under **Session Replay**, enter the new value for **Cost and traffic control**.

### Calculate number of sessions recorded with SR

To determine the actual percentage of user sessions recorded with Session Replay, you should consider the [cost and traffic control for RUM](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.") setting defined for your application, which is the overall percentage of user sessions to be analyzed with RUM.

#### Formula

Use the following formula to calculate the actual percentage of sessions recorded with Session Replay:

**Actual percentage of sessions recorded with SR = cost and traffic control for RUM × cost and traffic control for Session Replay**

#### Calculation example

| Parameter | Value |
| --- | --- |
| Cost and traffic control for RUM | 50% |
| Cost and traffic control for Session Replay | 20% |
| Actual percentage of sessions recorded with Session Replay | 50% × 20% = 10% |
| Total number of sessions | 2500 |
| Number of sessions analyzed with RUM | 2500 × 50% = 1250 |
| Number of sessions recorded with Session Replay | 2500 × 10% = 250 |

![Enablement and cost control](https://dt-cdn.net/images/enablement-and-cost-control-997-caeb5b3d6d.png)

Enablement and cost control

#### Sessions spanning multiple applications

When you have several applications and a user switches from one application to another, Dynatrace creates only one user session, with all the user activity recorded in the context of that session. Such a session is attributed to all the applications that the user visited.

To determine whether a multi-application session should be recorded with Session Replay, Dynatrace uses the cost and traffic control configuration of the application that the user entered first.

For example, suppose that the cost and traffic for Session Replay is set to `1%` for application A and `100%` for application B. When the user first enters application A and then switches to application B, Dynatrace uses the `1%` value to determine whether to record the session with Session Replay. This might result in a smaller or greater percentage of sessions recorded with Session Replay compared to the configured values of the cost and traffic control setting.

## Opt-in mode

Session Replay opt-in mode gives you the freedom to decide which parts of a user session must be recorded and when recording is permitted to begin. For example, you may choose to record user sessions in the following cases:

* As soon as any user logs in
* Only for certain customers so that you can offer them premium support
* Only for certain pages of your application

This mechanism enables you to implement end-user permission for session recording.

When you enable Session Replay opt-in mode for your web application, recording of the active user session begins only after you invoke the [`enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method on the `dtrum` global object. The `dtrum` global object is available if the [RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") has either been [injected automatically](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") or [inserted manually](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").

This command starts session recording. Session Replay remains active, and recording begins automatically on all subsequent pages visited during the same session or until [`dtrum.disableSessionReplay()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablesessionreplay) is called.

The [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method includes the `ignoreCostControl` parameter, which you can use to record certain user sessions by disregarding the value in the [Cost and traffic control](#cost-traffic-control) section of your application settings.

If [Real User Monitoring opt-in mode](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#user-opt-in-mode-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") is enabled, Real User Monitoring must be enabled before you can enable Session Replay, for example:

`dtrum.enable();`
`dtrum.enableSessionReplay(true);`

### Example

Consider the following scenario. As an application owner, you want to record all user sessions that include **Page 2** through **Page 5** of your application. Session activities involving **Page 1** or **Page 6** of your application are to be excluded from recording. The following diagram illustrates where the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) and [`dtrum.disableSessionReplay()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablesessionreplay) methods are required in the sequence.

![Session recording illustration](https://dt-cdn.net/images/session-recording-illustration-568-a36c3c47ad.png)

Session recording illustration

In such cases, you can display a consent banner to enable session recording when the user lands on **Page 2** (see the callout at the bottom of the following image). When the user selects **Accept** to allow session recording, the application responds by invoking the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method and recording the session.

![Session Replay opt-in banner example](https://dt-cdn.net/images/banner-example-2569-b86bd49e59.png)

Session Replay opt-in banner example

You can use a cookie in your application to record user content history within the browser. The content of this cookie is checked during each session to determine if the consent banner must be displayed. For example, if the cookie that stores the consent is named `sessionReplayConsent`, the application flow would be something like this:

1. The application checks the value of the `sessionReplayConsent` cookie.
2. If the value is `true`, the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) call is invoked.
3. If the value is `false`, the consent banner is displayed.
4. If the user provides their consent, the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) call is invoked.
5. User consent is written to the `sessionReplayConsent` cookie.

With this cookie, Session Replay continues to remain active until **Page 5** of the application.

Once the user leaves **Page 5**, you can use the [`dtrum.disableSessionReplay()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablesessionreplay) method to stop recording the session. Then, you must remove the cookie that has been used to store the consent.

You can use the JavaScript methods used for enabling and disabling Session Replay without displaying a banner to obtain consent. For example, if you wish to record a session each time any user logs in, you can use the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method to start recording and the [`dtrum.disableSessionReplay()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablesessionreplay) method to stop recording following successful logout. This gives you complete control over the start and stop of Session Replay.

### Enable Session Replay Classic opt-in mode

Session Replay opt-in mode is disabled by default.

To enable Session Replay opt-in mode

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Data privacy** > **Session Replay**.
5. Turn on **Enable opt-in mode for Session Replay**.

With these configuration settings, Session Replay is inactive in your end users' browsers, and sessions are not recorded until the [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay) method is called from the application.

If you choose not to **Enable opt-in mode for Session Replay**, all user sessions are recorded from the beginning until [`dtrum.disableSessionReplay()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disablesessionreplay) is called from the application.

## URL exclusion

URL exclusion is applicable to pages and views. If you want to exclude a page from Session Replay recording, define the regular expression that should be used to match against the specific page URL. You can configure rules for individual webpages, entire websites, and single-page applications.

* If a URL matches an exclusion rule, that rule is applied and all subsequent rules are ignored.
* If a URL doesn't match any rule, all applicable pages are recorded with Session Replay.
* If Session Replay is enabled and no URL exclusion rules are defined, all pages are recorded with Session Replay by default.

![Session Replay - URL exclusion](https://dt-cdn.net/images/sr-url-exclusion-700-395161c0b1.png)

Session Replay - URL exclusion

To exclude pages from recording

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Data privacy** > **Session Replay**.
5. Under **URL exclusion**, select **Add exclusion rule**.

   ![URL exclusion](https://dt-cdn.net/images/url-exclusion-1343-e10f29c49d.png)

   URL exclusion
6. Enter a regular expression that matches the page URL, and then select **Add rule**.

## Masking

Session Replay records every user interaction. Therefore, protecting confidential user data by masking is of utmost importance. Masking settings give you options to protect confidential user data when recording and playing back sessions. You can specify separate masking rules for recording sessions and, additionally, for playing back captured sessions, enabling you to apply layers of masking controlled by [user permissions](#sr-permissions).

Session Replay implements masking functionality that ensures that private user information is either not captured at the time of recording or masked at the time of session playback.

The masking option masks only alphanumeric characters; format characters such as periods, commas, and colons are not masked. Therefore, when user sessions are played back, you can still validate the format of the content without viewing the actual information.

As an example, consider an email address field on a typical web form. The user enters their email address, as shown below:

![Email field with content](https://dt-cdn.net/images/2018-10-25-12-34-34-312-26653a5668.png)

Email field with content

Session Replay masks this data and displays asterisks in place of the nonnumeric characters:

![Email field with masked content](https://dt-cdn.net/images/2018-10-25-12-40-06-317-b9aa2a3f8c.png)

Email field with masked content

The masked data—displayed in the replayed session as asterisks (`*****`) for nonnumeric input or as zeros (`0000`) for numeric input—either never leaves the client browser (masked at recording) or is captured but masked during playback. Note that playing back captured sessions is [permission controlled](#sr-permissions).

Session Replay provides two options for configuring content masking.

* [`data-dtrum-mask` attribute](#mask-data-via-code)
* [Session Replay configuration page](#mask-data-via-ui)

### Mask data with `data-dtrum-mask` attribute

The `data-dtrum-mask` attribute requires a change in the application code and is secure by design. It allows you to consider the elements that can contain confidential information at the design and implementation stages. The recorder automatically detects and masks the content (text, input values, and attributes values) and interactions (cursor movements and scrolls) in the node that contains the attribute as well as its descendants.

The application code must be modified to incorporate the `data-dtrum-mask` attribute.

![The data-drum-mask attribute displayed in the code](https://dt-cdn.net/images/data-dtrum-mask-example-655-045d2f8d23.png)

The data-drum-mask attribute displayed in the code

### Mask data via UI

The page for configuring Session Replay settings in Dynatrace allows a more customized approach. You can change the configuration to suit your session-recording requirements. Also, there's no need to change the application code if you go with this option.

This settings page also provides masking options that you can use to hide interactions with specific elements that might inadvertently reveal confidential end-user information. For example, consider a list that provides multiple options for responding to a form question about the user's religion or gender. Even with the text masked, others would still be able to deduce the end user's response by seeing the selected option.

To configure Session Replay masking

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Data privacy** > **Session Replay**.
5. Under **Content masking preferences**, select a [predefined masking option](#masking-preset-options) for recording and playback.
6. If you selected **Allow list** or **Block list**, add the desired masking rules.

#### Content masking levels

Session Replay predefined [masking options](#masking-preset-options) are available for both recording and playback:

* **Recording masking settings** control data masking at the time of recording ("masking at capture"). Masked user data never leaves the client browser and is not captured. Note that when you set the **Recording masking settings** to a more restrictive level, the same settings are also applied to **Playback masking settings**, which affects all past recorded sessions as well.
* **Playback masking settings** affect data masking at the time of playback ("masking at display"). Data captured during recording can still be masked and restricted from being viewed at the time of playback.

You can define masking rules for session recording and session playback.

Playback masking rules are meant to provide an additional layer of masking over recording masking rules. Playback masking settings cannot be less restrictive than recording masking settings.

You can use [user permissions](#sr-permissions) to decide whether to allow session playback with or without playback masking rules in effect.

#### Content masking options

The following predefined masking options can be used to restrict capturing and playing back personal and confidential end-user data:

| Masking option | What is masked | When to use |
| --- | --- | --- |
| **Mask all** | All texts, user input, attributes values, and images | Use to test Session Replay and ensure that confidential data is not collected. You'll still be able to see how users interact with your application.Use for troubleshooting your applications when the order in which the users interact with different web UI controls is of importance. |
| **Mask user input** | All user input, including options in list boxes | Select this option when confidential information comes only from user input. |
| **Allow list** | All elements in the **Mask all** option except for the elements that you've specified | We recommend this option for most applications; it allows you to collect only the required information.This option ensures that, even with subsequent code changes, new elements that display confidential information are not recorded by the Session Replay recorder.The elements are defined by the CSS selector. |
| **Block list** | Only elements specified in this block list | When you select this option, a list with all the rules applied to the **Mask all** option is presented to you. Use this list to clear elements and attributes that you want to capture. You can also create your own additional block list rules. |

**Mask user input** is the default masking option starting with Dynatrace version 1.262. Previously, the default option was **Mask all**.

The **Mask all**, **Mask user input**, and **Allow list** options do not hide user interactions with elements. With the **Block list** option, you can decide if you want to hide user interactions with masked elements.

## Resource capture

With Dynatrace Session Replay, stylesheets are captured and stored during user session recording. You don't have to keep your CSS files at a publicly accessible location, mark the resources as modified, or give permissions to a process that can access the protected stylesheets. It's an entirely automated process that ensures that resources are captured and made available for future replay.

Resource capture for Session Replay is enabled by default.

### Enable resource capture

To enable and configure resource capture

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Capturing** > **Resource capture for Session Replay**.
5. Turn on **Enable resource capture**.
6. Optional To avoid capturing resources for certain pages, select **Add exclusion rule**, enter a regular expression, and then select **Add rule**.

   The exclusion rules are processed as follows.

   * If a URL matches an exclusion rule, the rule is applied and the subsequent rules are ignored.
   * If a URL doesn't match any listed rule, all resources are captured.
   * If Session Replay is enabled and no URL exclusion rules are defined, all CSS resources are eligible for recording.

### Notes and limitations for resource capture

* If a resource hasn't been captured or is unavailable in the Dynatrace resource storage, this resource is retrieved from the original source.
* Images and fonts aren't captured. During session playback, they're retrieved from the original location, so certain [restrictions](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web#resources "Learn which restrictions apply to Session Replay Classic.") apply. To enhance Session Replay playback, use the **Session Replay browser extension**. To get started, see [What does the Session Replay browser extension do and how do I install it?](#extension).
* Dynatrace doesn't capture a resource that is bigger than 3 MB.
* The default [retention time](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.") for captured resources is 35 days.
* Dynatrace captures resources for up to 0.1% of user sessions recorded with Session Replay. This is usually enough to properly replay user sessions, as a resource captured for one session is reused for all other sessions. However, capturing all resources for a low-traffic application might take some time.

  Calculate sessions with captured resources

  See the formula and example below to calculate the number of user sessions for which Dynatrace captures resources.

  **Sessions with captured resources =
  Total sessions × RUM cost and traffic control × SR cost and traffic control × 0.1%**

  | Parameter | Explanation | Example value |
  | --- | --- | --- |
  | Total sessions | Total number of user sessions in your application | 1,000,000 |
  | [RUM cost and traffic control](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.") | Percentage of user sessions captured and analyzed with RUM | 50% |
  | [Session Replay cost and traffic control](#cost-traffic-control) | Percentage of user sessions recorded with Session Replay | 10% |

  In our example, resources are captured for 50 user sessions (1,000,000 × 50% × 10% × 0.1% = 50).

## User permissions and management zones

### User permissions

Use the **Replay sessions with masking** and **Replay sessions without masking** permissions to control who has access to session recordings. For more details, see [Manage user groups and permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").

No permission

Replay session data with masking

Replay session data without masking

For users that don't need the access, disable both permissions in user and group settings.

![Session Replay - No permission to replay a session](https://dt-cdn.net/images/sr-permission-no-permission-430-42ceb0d0d2.png)

Session Replay - No permission to replay a session

For users that need to replay user sessions but don't need to see all captured information, assign the **Replay sessions with masking** permission. Note that this permission is given to all users by default.

![Session Replay - Replay session data with masking permission](https://dt-cdn.net/images/sr-permission-replay-with-masking-430-afce4988e8.png)

Session Replay - Replay session data with masking permission

For users that need to play back sessions and see all recorded information, select the **Replay sessions without masking** user permission.

![Session Replay - Replay session data without masking permission](https://dt-cdn.net/images/sr-permission-replay-without-masking-430-8ecf1dada3.png)

Session Replay - Replay session data without masking permission

### Management zones

The ability to view and play back user sessions is further protected by management zones. If a user session traverses applications within different management zones, Dynatrace users with Session Replay permissions may only view those parts of the session associated with applications in the management zones that they have access to. For details, check [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.").

![Session Replay - Management zones](https://dt-cdn.net/images/sr-management-zones-1150-f13652bc3a.png)

Session Replay - Management zones

## Modify Content Security Policy for Session Replay Classic

Session Replay uses web workers to process data during recording, offloading logic from the UI thread to improve performance. The RUM JavaScript achieves this by loading the code as a blob. For this to work, you must add `blob:` to the `worker-src` directive of your CSP rules, in addition to the adaptations described in [Modify Content Security Policy for RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/modify-csp-for-rum "Learn how to enable and modify CSP for your RUM-monitored applications."). You can define CSP rules via the `Content-Security-Policy` HTTP response header or using a `<meta>` tag placed in the `<head>` section of the HTML document.

If `blob:` is not allowed in `worker-src`—or, as a fallback, in `script-src`—a CSP violation will occur when the page loads, and all code will run in the UI thread instead.

If you can’t run web workers on your website or want to disable their use by Session Replay, you can do so by adding a custom configuration property.

To disable the use of web workers by Session Replay

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **Capturing** > **Custom configuration properties**.
5. Select **Add a custom configuration property**.
6. Enter the property `srbw=0` and save the changes.

We do not recommend running the Session Replay code in the UI thread instead of using web workers, since it will impact page performance.

## FAQ

Does Session Replay consume a lot of storage?

Around 100 kB of data is generated for every minute of a session and around 500 kB of storage is consumed by a fully recorded session.

Do all sessions consume the same amount of storage volume?

No. Session volume depends on a variety of factors, including the application size, session duration, and users' interactivity with the application.

Session sizes vary from 100 kB to over 1 MB.

Are sessions recorded as videos?

No. To record sessions, Session Replay monitors changes on the DOM tree of a web application. Every visual change in a web application has a corresponding change in the underlying DOM. Session Replay captures and recreates these changes. Because all of this is text-based data, small session sizes are achieved through compact representation and compression.

What is the bandwidth consumption like?

Because compression takes place on the client side, the bandwidth consumption is the same as the storage consumption: around 100 kB per minute or 500 kB per session.

This is advantageous for recording sessions from users on mobile devices with limited internet data or with connections that have limited bandwidth.

Does compression impact the client browser?

Session Replay was designed to have a low impact on the UI thread, which impacts user experience. Most Session Replay tasks, including an efficient compression algorithm, are executed by a worker thread that runs in the background and doesn't interfere with the user interface.

Are masking rules applied on the Dynatrace Server?

[Recording masking rules](/managed/observe/digital-experience/session-replay/configure-session-replay-web#masking-preset-options "Configure monitoring consumption and data privacy settings for Session Replay Classic.") are transmitted to the client. This ensures that confidential data does not leave the client browser by default. [Masking settings](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-masking "Configure monitoring consumption and data privacy settings for Session Replay Classic.") for recording as well as playback are configurable.

What does the Session Replay browser extension do and how do I install it?

The Session Replay browser extension allows proxy loading of resources when replaying a session.
You can use the extension to enhance Session Replay playback, for example in the following cases:

* Font and stylesheet resources are loaded from HTTPS origins.
* Resources are loaded from HTTP origins.

The extension can be installed from the Chrome Web Store: [`Session Replay browser extension`﻿](https://chromewebstore.google.com/detail/session-replay-browser-ex/hjbdnbhpfiionafiooklnafmaojjfljh)

What are the recommendations for ensuring user privacy?

Privacy must be built into applications by design, implemented from the beginning when an application is created. Any feature that involves the processing of private data or non-functional requirements as relevant dimensions should be evaluated for data privacy risk early on. Dynatrace recommends that user-confidential elements and input fields be flagged. For instance, if Session Replay detects an HTML attribute, such as [`data-dtrum-mask`](#mask-data-via-code), it automatically masks its data.

We recommend that you start with the **Mask all** option and then gradually tweak your settings if you think some of the blocked elements can be safely allowed for display.

If you do record some sensitive user data or your application contains sensitive label text, you can use more restrictive playback masking rules to limit what's displayed at the time of playback. And you can use [user permissions](#sr-permissions) to determine which users can replay sessions with or without playback masking rules applied.

What happens if masking rules are incorrectly configured and confidential data becomes accessible during Session Replay?

Following any accidental display of confidential data, once you configure the masking rules correctly, Session Replay applies the latest masking configuration to all recorded sessions, including those that were recorded before the correct masking rules were implemented. Updated masking rules are applied at the time of playback, and [users who have permission to replay sessions](#sr-permissions) are not able to view masked user data. Note that playback masking rules are ignored for those users who have permission to replay sessions without masking.

How can you configure an application not to mask any element?

Use the **Block list** approach and remove all the predefined rules.

What is the best way to use the Mask all masking option?

**Mask all** is the best masking option for testing Session Replay with no risk of exposing confidential user data. This option is also handy when using Session Replay for troubleshooting and you want to see how the user interacts with the controls of your application.

Why is Session Replay data partially missing when I replay a session?

On the user session details page, the **Session Replay** timeline shows both [Real User Monitoring (RUM)](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.") and Session Replay events.

When you replay a user session, you might notice that even though the timeline shows all the user actions and events, the Session Replay player skips some of the events and jumps to the end of the session. If you're not seeing the Session Replay data corresponding to all the events on the timeline, this is usually because there is no Session Replay data available for this part of the session.

The following are the most common reasons for partially missing Session Replay data.

* A session spanned a second application for which Session Replay was disabled.
* A Session Replay recording was paused because a page was [excluded from Session Replay recording](#sr-url-exclusion).
* Session Replay data is available, but you [don't have permission to access this data](#no-permission).

## Related topics

* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Enable Session Replay Classic for web applications](/managed/observe/digital-experience/session-replay/enable-session-replay-web "Learn the prerequisites and the procedure for enabling Session Replay Classic.")
* [Technical restrictions for Session Replay Classic for web applications](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay Classic.")