---
title: Set up an auto-injected frontend in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend
scraped: 2026-02-18T05:54:20.307307
---

# Set up an auto-injected frontend in the New RUM Experience

# Set up an auto-injected frontend in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Feb 03, 2026

As explained in [Find the suitable instrumentation approach](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup#find-suitable-instrumentation-approach "Learn how to set up the New RUM Experience for web frontends."), automatic injection is available if at least one application tier can be instrumented with OneAgent, and automatic RUM injection is supported for that technology. For details, see [Technology support - Real User Monitoring - Web servers and applications](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). This guide explains how to create a frontend in the New RUM Experience and configure frontend detection rules to ensure captured data is routed to the correct frontend.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Deploy OneAgent**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#deploy-oneagent "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Learn how frontend detection rules are applied**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#learn-application-of-detection-rules "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Account for uninstrumented components**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#account-for-uninstrumented-components "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Create a frontend and define frontend detection rules**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#create-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Set the order of frontend detection rules**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#set-order-of-rules "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 6 optional](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Step 6 optional")

**Configure the RUM JavaScript snippet format**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#configure-snippet-format "Learn how to set up an auto-injected web frontend in the New RUM Experience.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Verify your setup**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend#verify-setup "Learn how to set up an auto-injected web frontend in the New RUM Experience.")

## Step 1 Deploy OneAgent

After deploying OneAgent in full-stack monitoring mode on your application tiers, the RUM JavaScript is automatically injected into HTML pages. Restart the process after OneAgent deployment for the injection to become active. For installation details, see [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.").

If OneAgent doesn't inject the RUM JavaScript, refer to [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.") for guidance.

By default, all captured RUM data is associated with the catch-all frontend **My web application**. We recommend keeping this name to make it easier to distinguish from other frontends.

What can I do if I can't find My web application?

If you canât find **My web application**, it may have been renamed.

To locate the renamed **My web application**

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select any auto-injected frontend.
4. On the **Settings** tab, select **Frontend detection**.
5. Select the link **catch-all frontend**. You'll be redirected to **My web application**.

## Step 2 Learn how frontend detection rules are applied

Frontend detection rules are evaluated on the server side of your application by the OneAgent on the first instrumented tierâthe one closest to the browser.

All frontend detection rules are URL-based and consist of a pattern and a matcher. There are two ways to define them:

* **On the entire URL:** You can use the matchers **URL starts with**, **URL ends with**, **URL contains**, and **URL equals**. The URL follows the format `scheme://host:port/path?query`, where the query string is optional and default ports (`80` for HTTP and `443` for HTTPS) are omitted. The URL does not include a fragment identifier (as in `scheme://host:port/path?query#fragment`), because fragments are only used by the browser and never sent to the server.
* **On the domain only:** The rule is applied to the host portion of the URL. The matchers **Domain (host) starts with**, **Domain (host) ends with**, **Domain (host) contains**, **Domain (host) equals**, and **Domain (host) matches** are available. When using the latter, the pattern `example.com` matches both `example.com` and `shop.example.com`.

## Step 3 Account for uninstrumented components

There may be a componentâsuch as a reverse proxy or load balancerâbetween the browser and the tier responsible for frontend detection that is either uninstrumented or uses a technology without RUM support. If this component rewrites the URL, the URL used for frontend detection differs from the one originally requested by the browser. In such cases, special considerations are required to ensure that your frontend detection rules take effect as expected.

* If the component terminates HTTPS, you cannot use the `https` scheme in the pattern of a frontend detection rule.
* If the component rewrites the host part of the URL, you can still use the original host in your frontend detection rules. However, you may need to set up host name determination for this to work. For details, see [Set up host name determination in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-host-name-determination "Learn how to set up host name determination in the New RUM Experience.").
* If the component rewrites the URL path and removes part of it, you cannot use that removed part in your frontend detection rules.

## Step 4 Create a frontend and define frontend detection rules

With the foundational knowledge from the previous steps, you are now ready to create a frontend and define its detection rules.

To create an auto-injected frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Frontend** to start the **Frontend creation** flow.
3. In the **Start monitoring** step, select the frontend type **Web** and provide a frontend name.
4. In the **Select instrumentation method** step, select **OneAgent injection**.
5. Select **Create**.
6. In the **Setup** > **Configure frontend detection rule** step, configure the matcher and the pattern for your frontend detection rule.
7. Select **Save frontend detection rule**.
8. Under **Select capability and settings**, check if **RUM** is enabled. If it isnât, select  **Override** and turn it on.
9. If you want to capture [user interactions](/docs/observe/digital-experience/new-rum-experience/user-interactions "Learn how to capture and analyze user interactions.") such as clicks and scrolls, enable **User Interactions**.
10. To ensure compliance with applicable data privacy regulations, configure the required settings under **End users' data privacy**. For more information about the available options, see [Configure data privacy settings for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/data-privacy-web "Learn about the available settings that help you ensure your web frontends comply with data privacy regulations.").
11. Select **Next** > **Go to new frontend**.

Youâll now see the detection rule for the frontend you just created. To add additional rules, select  **Add**.

You can create up to 1,000 frontend detection rules per environment.

## Step 5 Set the order of frontend detection rules

Frontend detection rules have a defined order, and OneAgent applies them sequentially. Rules at the top of the list take precedence over those further down. To ensure accurate detection, place more specific rulesâfor example, those that include both a domain and a pathâhigher in the list than generic rulesâsuch as those that include only the domain.

The rules you created in the previous step are added to the bottom of the list, so you may need to move them up for them to take effect. To adjust the order, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Frontend** > **Application detection**. Select and hold ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") next to the rule name, then drag the rule up or down to change its priority.

How quickly do frontend detection rule changes take effect?

When you update your frontend detection rules, the changes are usually communicated to OneAgent within a minute. However, there are scenarios where the updated rules cannot take effect immediately.

When OneAgent injects the RUM JavaScript, it adds an ID for the detected frontend to the injected snippet. This ID is then included when the RUM JavaScript reports the captured user events, allowing the events to be correctly attributed to the corresponding frontend. In the following situations, OneAgent cannot perform a fresh injection with an updated ID, which delays the effectiveness of rule changes:

* **HTML served through a CDN or other cache:** OneAgent can inject the RUM JavaScript only when the HTML code is evicted from the cache and requested again from the instrumented origin server.
* **Long expiration times for HTML documents:** If the application specifies a long expiration time using the `Expires` response header or the `max-age` directive of the `Cache-Control` header, changes to frontend detection rules cannot take effect until the cached document expires.
* **Single-page applications (SPAs):** SPAs rewrite the current page dynamically instead of loading a new page from the server. If the HTML was loaded before the rule changes, the categorization of captured user events does not reflect the updated configuration, which takes effect as soon as the page is refreshed.

## Step 6 optional Configure the RUM JavaScript snippet format Optional

By default, OneAgent injects the [OneAgent JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#oneagent-js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") snippet format, which is recommended for most scenarios.

The New RUM Experience provides snippet formats tailored to different requirements. For details on different formats and their configuration options, see [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). You can configure the snippet format as described in [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#configure-snippet-format "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.").

## Step 7 Verify your setup

If your frontend is receiving traffic, the charts in [![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**](/docs/observe/digital-experience/new-rum-experience/experience-vitals "The Experience Vitals app provides an entry point for monitoring web and mobile frontends.") should begin showing data within ten minutes.

If no data appears yet, your environment may require further configuration steps. The guide [Finalize the initial setup for your auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-auto-injection "Verify and complete the initial setup for your auto-injected frontend.") provides a series of checks to help you identify the configuration needed.

## Related topics

* [Set up host name determination in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-host-name-determination "Learn how to set up host name determination in the New RUM Experience.")
* [Configure automatic injection in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.")
* [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")
* [Finalize the initial setup for your auto-injected frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-auto-injection "Verify and complete the initial setup for your auto-injected frontend.")